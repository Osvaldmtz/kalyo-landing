#!/usr/bin/env python3
"""Ensure all batch 8+9 slugs are in index.html and sitemap.xml; regenerate sitemap if needed."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

BATCH_DIR = Path(__file__).resolve().parent
ROOT = BATCH_DIR.parents[1]


def all_slugs() -> list[str]:
    slugs: list[str] = []
    for batch in ("8", "9"):
        data = json.loads((BATCH_DIR / f"topics-batch-{batch}.json").read_text(encoding="utf-8"))
        slugs.extend(t["slug"] for t in data["topics"])
    return slugs


def main() -> None:
    slugs = all_slugs()
    index = (ROOT / "articulos" / "index.html").read_text(encoding="utf-8")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    missing_idx = [s for s in slugs if f"/articulos/{s}.html" not in index]
    missing_sm = [s for s in slugs if f"articulos/{s}.html" not in sitemap]
    missing_html = [s for s in slugs if not (ROOT / "articulos" / f"{s}.html").exists()]

    if missing_html:
        print("ERROR: missing HTML:", missing_html)
        sys.exit(1)

    if missing_idx or missing_sm:
        print(f"Missing index ({len(missing_idx)}): {missing_idx[:5]}")
        print(f"Missing sitemap ({len(missing_sm)}): {missing_sm[:5]}")
        print("Regenerating sitemap.xml via regenerate-sitemap.mjs...")
        subprocess.run(["node", str(ROOT / "scripts" / "regenerate-sitemap.mjs")], cwd=ROOT, check=True)
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        missing_sm = [s for s in slugs if f"articulos/{s}.html" not in sitemap]
        if missing_sm:
            print("ERROR: still missing from sitemap after regen:", missing_sm)
            sys.exit(1)

    if missing_idx:
        print("WARN: index.html missing cards for:", missing_idx)
        print("Run run_batch20_mexico.py / run_batch9.py to insert cards, or add manually.")
        sys.exit(1)

    n = re.search(r'"numberOfItems":\s*(\d+)', index)
    print(f"OK: {len(slugs)} slugs verified in index + sitemap (numberOfItems={n.group(1) if n else '?'})")


if __name__ == "__main__":
    main()
