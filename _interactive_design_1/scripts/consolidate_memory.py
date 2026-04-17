#!/usr/bin/env python3
"""Memory Consolidation — Deduplicate and merge similar LanceDB chunks.

Purpose:
    Over time, the semantic knowledge base accumulates near-duplicate entries.
    This script scans all chunks, identifies pairs with cosine similarity > 0.95,
    and merges them by keeping the most recently ingested version.

Usage:
    python scripts/consolidate_memory.py
    python scripts/consolidate_memory.py --threshold 0.90 --dry-run

Output: Summary of merged/removed entries.
"""
import sys
import math
from pathlib import Path

import os
DB_PATH = Path('.lancedb')
EMBED_MODEL = os.environ.get('AIMOS_EMBED_MODEL', 'sentence-transformers/all-MiniLM-L6-v2')
DEFAULT_THRESHOLD = 0.95


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x ** 2 for x in a))
    mag_b = math.sqrt(sum(x ** 2 for x in b))
    return dot / (mag_a * mag_b) if mag_a and mag_b else 0.0


def consolidate(threshold: float = DEFAULT_THRESHOLD, dry_run: bool = False) -> dict:
    if not DB_PATH.exists():
        print('\u274c LanceDB not found. Run scripts/ingest.py first.')
        return {'status': 'error', 'message': 'DB not found'}

    try:
        import lancedb
        db = lancedb.connect(str(DB_PATH))
        table = db.open_table('knowledge')
        df = table.to_pandas()
    except Exception as e:
        print(f'\u274c Error opening LanceDB: {e}')
        return {'status': 'error', 'message': str(e)}

    if len(df) < 2:
        print('\u2705 Only', len(df), 'entries — no consolidation needed.')
        return {'status': 'ok', 'merged': 0, 'remaining': len(df)}

    # Find duplicate pairs
    to_remove: set[int] = set()
    vectors = df['vector'].tolist()
    n = len(vectors)

    for i in range(n):
        if i in to_remove:
            continue
        for j in range(i + 1, n):
            if j in to_remove:
                continue
            sim = cosine_similarity(vectors[i], vectors[j])
            if sim >= threshold:
                # Keep the one with later index (more recent)
                to_remove.add(i)
                if not dry_run:
                    print(f'  \u2702\ufe0f Merging chunk {i} into {j} (similarity={sim:.4f})')
                else:
                    print(f'  [DRY RUN] Would merge chunk {i} into {j} (similarity={sim:.4f})')
                break

    if not dry_run and to_remove:
        keep_indices = [i for i in range(n) if i not in to_remove]
        keep_df = df.iloc[keep_indices].reset_index(drop=True)
        db.drop_table('knowledge')
        db.create_table('knowledge', keep_df)

    result = {
        'status': 'ok',
        'total_before': n,
        'merged': len(to_remove),
        'remaining': n - len(to_remove),
    }
    print(f'\n\u2705 Consolidation complete: {n} \u2192 {n - len(to_remove)} entries ({len(to_remove)} merged)')
    return result


def main() -> None:
    threshold = DEFAULT_THRESHOLD
    dry_run = '--dry-run' in sys.argv

    for i, arg in enumerate(sys.argv):
        if arg == '--threshold' and i + 1 < len(sys.argv):
            threshold = float(sys.argv[i + 1])

    consolidate(threshold=threshold, dry_run=dry_run)


if __name__ == '__main__':
    main()
