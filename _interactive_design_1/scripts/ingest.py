#!/usr/bin/env python3
"""Index project files into LanceDB for semantic search.

Purpose: Scan project directory, split files into chunks, embed with local
         HuggingFace model, write to LanceDB. Supports incremental indexing
         via a manifest file (.ingest_state.json) to skip unchanged files.

Usage:
    python scripts/ingest.py                          # incremental (default)
    python scripts/ingest.py --full                   # force full rebuild
    python scripts/ingest.py --dirs src scripts docs
    python scripts/ingest.py --chunk-size 512 --overlap 64
    python scripts/ingest.py --json

Output: .lancedb/ (local serverless vector database)
        With --json: machine-readable JSON result envelope.

Chunking strategy: chunk_size=800, overlap=100 (paragraph -> line -> word -> char)
"""
import os
import sys
import json as _json
import argparse
from pathlib import Path

INCLUDE_EXTS = {".py", ".ts", ".tsx", ".js", ".jsx", ".md", ".txt",
                ".yaml", ".yml", ".toml", ".sh"}
EXCLUDE_DIRS = {"node_modules", ".git", "__pycache__", ".venv", "dist", "build", ".lancedb"}
DEFAULT_DIRS  = ["src", "scripts", "docs", "."]
DB_PATH       = ".lancedb"
TABLE_NAME    = "project_chunks"
EMBED_MODEL   = os.environ.get('AIMOS_EMBED_MODEL', 'sentence-transformers/all-MiniLM-L6-v2')
CHUNK_SIZE    = 800
CHUNK_OVERLAP = 100
MANIFEST_PATH = Path('.ingest_state.json')


def collect_files(search_dirs: list) -> list:
    """Return absolute Paths for all indexable files under search_dirs."""
    seen = set()
    files = []
    for d in search_dirs:
        p = Path(d)
        if not p.exists():
            continue
        for f in p.rglob("*"):
            if f.is_file() and f.suffix in INCLUDE_EXTS:
                if any(part in EXCLUDE_DIRS for part in f.parts):
                    continue
                if f not in seen:
                    seen.add(f)
                    files.append(f)
    return files


def load_manifest() -> dict:
    """Load previous ingest state manifest."""
    if MANIFEST_PATH.exists():
        try:
            return _json.loads(MANIFEST_PATH.read_text())
        except Exception:
            return {}
    return {}


def save_manifest(files: list) -> None:
    """Save current file state as manifest for future incremental runs."""
    state = {}
    for f in files:
        try:
            stat = f.stat()
            state[str(f)] = {'mtime': stat.st_mtime, 'size': stat.st_size}
        except OSError:
            pass
    MANIFEST_PATH.write_text(_json.dumps(state, indent=2))


def filter_changed(files: list, manifest: dict) -> tuple:
    """Return (changed_files, skipped_count) based on manifest comparison."""
    if not manifest:
        return files, 0
    changed = []
    skipped = 0
    for f in files:
        key = str(f)
        prev = manifest.get(key)
        if prev:
            try:
                stat = f.stat()
                if stat.st_mtime == prev.get('mtime') and stat.st_size == prev.get('size'):
                    skipped += 1
                    continue
            except OSError:
                pass
        changed.append(f)
    return changed, skipped


def chunk_files(files: list, chunk_size: int, overlap: int) -> list:
    """Split files into chunks; return list of dicts with text + metadata."""
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
    )
    chunks = []
    for f in files:
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"  \u26a0\ufe0f  Skipping {f}: {e}")
            continue
        for i, chunk in enumerate(splitter.split_text(text)):
            chunks.append({"text": chunk, "source": str(f), "chunk_index": i})
    return chunks


def ingest(dirs: list, chunk_size: int, overlap: int, use_json: bool = False, full: bool = False) -> None:
    """Full pipeline: collect -> filter changed -> chunk -> embed -> write to LanceDB."""
    import lancedb
    from langchain_huggingface import HuggingFaceEmbeddings

    if not use_json:
        print(f"\ud83d\udcc2 Scanning: {dirs}")
    all_files = collect_files(dirs)
    if not use_json:
        print(f"   Found {len(all_files)} indexable files")
    if not all_files:
        if use_json:
            print(_json.dumps({"status": "warning", "message": "No files found", "files": 0, "chunks": 0}))
        else:
            print("\u26a0\ufe0f  No files found. Check --dirs and INCLUDE_EXTS.")
        return

    # Incremental filtering
    if full:
        files, skipped = all_files, 0
        if not use_json:
            print("\ud83d\udd04 Full rebuild requested")
    else:
        manifest = load_manifest()
        files, skipped = filter_changed(all_files, manifest)
        if not use_json and skipped > 0:
            print(f"   \u23e9 Skipped {skipped} unchanged files")

    if not files:
        if use_json:
            print(_json.dumps({"status": "ok", "message": "No changes detected", "files": 0, "files_skipped": skipped, "chunks": 0}))
        else:
            print("\u2705 No changes detected — index is up to date.")
        save_manifest(all_files)
        return

    if not use_json:
        print(f"\u2702\ufe0f  Chunking {len(files)} files (size={chunk_size}, overlap={overlap})...")
    chunks = chunk_files(files, chunk_size, overlap)
    if not use_json:
        print(f"   Created {len(chunks)} chunks")

    if not use_json:
        print(f"\ud83d\udd22 Loading embedding model: {EMBED_MODEL}")
    embedder = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

    if not use_json:
        print("\u2699\ufe0f  Embedding chunks (this may take a while on first run)...")
    texts = [c["text"] for c in chunks]
    vectors = embedder.embed_documents(texts)

    records = []
    for chunk, vector in zip(chunks, vectors):
        records.append({
            "vector":      vector,
            "text":        chunk["text"],
            "source":      chunk["source"],
            "chunk_index": chunk["chunk_index"],
        })

    if not use_json:
        print(f"\ud83d\udcbe Writing to LanceDB: {DB_PATH}/{TABLE_NAME}")
    db = lancedb.connect(DB_PATH)
    db.create_table(TABLE_NAME, data=records, mode="overwrite")
    save_manifest(all_files)
    if use_json:
        print(_json.dumps({"status": "ok", "files": len(files), "files_skipped": skipped, "chunks": len(records), "db": f"{DB_PATH}/{TABLE_NAME}"}))
    else:
        print(f"\u2705 Indexed {len(records)} chunks from {len(files)} files ({skipped} skipped) \u2192 {DB_PATH}/{TABLE_NAME}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest project files into LanceDB.")
    parser.add_argument(
        "--dirs", nargs="+", default=DEFAULT_DIRS,
        help=f"Directories to scan (default: {DEFAULT_DIRS})"
    )
    parser.add_argument(
        "--chunk-size", type=int, default=CHUNK_SIZE,
        help=f"Characters per chunk (default: {CHUNK_SIZE})"
    )
    parser.add_argument(
        "--overlap", type=int, default=CHUNK_OVERLAP,
        help=f"Overlap between chunks (default: {CHUNK_OVERLAP})"
    )
    parser.add_argument(
        "--json", action="store_true", dest="use_json",
        help="Output machine-readable JSON result envelope"
    )
    parser.add_argument(
        "--full", action="store_true",
        help="Force full rebuild, ignoring incremental manifest"
    )
    args = parser.parse_args()
    try:
        ingest(args.dirs, args.chunk_size, args.overlap, args.use_json, args.full)
    except ImportError as e:
        if args.use_json:
            print(_json.dumps({"status": "error", "reason": str(e), "remedy": "uv pip install lancedb langchain-huggingface sentence-transformers langchain-text-splitters"}))
        else:
            print(f"\u274c Missing dependency: {e}")
            print("   Run: uv pip install lancedb langchain-huggingface sentence-transformers langchain-text-splitters")
        sys.exit(1)


if __name__ == "__main__":
    main()
