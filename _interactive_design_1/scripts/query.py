#!/usr/bin/env python3
"""Semantic search for LanceDB knowledge base.

Usage:
    python scripts/query.py "<your search query>" [top_k]
    python scripts/query.py "<your search query>" --json

Example:
    python scripts/query.py "important architecture status"
    python scripts/query.py "recent decisions" 5
    python scripts/query.py "recent decisions" --json

Output: Top-k matching chunks with source file, similarity score, and text preview.
        With --json: machine-readable JSON result envelope.
"""
import os
import sys
import json as _json
import argparse
from pathlib import Path

DB_PATH = ".lancedb"
TABLE_NAME = "project_chunks"
EMBED_MODEL = os.environ.get('AIMOS_EMBED_MODEL', 'sentence-transformers/all-MiniLM-L6-v2')


def query(query_str: str, top_k: int = 5, use_json: bool = False) -> None:
    """Embed query, search LanceDB, print top_k results."""
    db_path = Path(DB_PATH)
    if not db_path.exists():
        if use_json:
            print(_json.dumps({"status": "error", "message": "LanceDB not initialized", "remedy": "Run scripts/ingest.py first"}))
        else:
            print("\u26a0\ufe0f  LanceDB not initialized. Run scripts/ingest.py first.")
        return
    try:
        import lancedb
        from langchain_huggingface import HuggingFaceEmbeddings
    except ImportError as e:
        if use_json:
            print(_json.dumps({"status": "error", "reason": str(e), "remedy": "uv pip install lancedb langchain-huggingface sentence-transformers"}))
        else:
            print(f"\u274c Missing dependency: {e}")
            print("   Run: uv pip install lancedb langchain-huggingface sentence-transformers")
        sys.exit(1)

    db = lancedb.connect(DB_PATH)
    if TABLE_NAME not in db.table_names():
        if use_json:
            print(_json.dumps({"status": "error", "message": f"Table '{TABLE_NAME}' not found", "remedy": "Run scripts/ingest.py first"}))
        else:
            print(f"\u26a0\ufe0f  Table '{TABLE_NAME}' not found. Run scripts/ingest.py first.")
        return

    table = db.open_table(TABLE_NAME)
    embedder = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    q_vector = embedder.embed_query(query_str)

    results = table.search(q_vector).limit(top_k).to_list()

    if use_json:
        json_results = []
        for r in results:
            json_results.append({
                "source": r.get('source', 'unknown'),
                "chunk_index": r.get('chunk_index', 0),
                "distance": round(r.get('_distance', 0.0), 4),
                "text": r.get('text', '')[:500],
            })
        print(_json.dumps({"status": "ok", "query": query_str, "count": len(json_results), "results": json_results}))
    else:
        print(f"\ud83d\udd0d Query: '{query_str}' (top {top_k})")
        print(f"   Found {len(results)} results\n")
        for i, r in enumerate(results, 1):
            score = r.get('_distance', 0.0)
            source = r.get('source', 'unknown')
            chunk_idx = r.get('chunk_index', '?')
            text = r.get('text', '')[:200]
            print(f"--- [{i}] {source} (chunk {chunk_idx}, distance={score:.4f}) ---")
            print(f"{text}")
            if len(r.get('text', '')) > 200:
                print("...")
            print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Semantic search for LanceDB knowledge base.")
    parser.add_argument("query", help="The search query string")
    parser.add_argument("top_k", nargs="?", type=int, default=5, help="Number of results (default: 5)")
    parser.add_argument(
        "--json", action="store_true", dest="use_json",
        help="Output machine-readable JSON result envelope"
    )
    args = parser.parse_args()
    query(args.query, args.top_k, args.use_json)


if __name__ == "__main__":
    main()
