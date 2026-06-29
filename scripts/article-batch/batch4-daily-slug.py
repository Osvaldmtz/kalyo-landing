#!/usr/bin/env python3
"""Return today's batch-4 slug for the daily cron, or SKIP."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

START = date(2026, 6, 30)
BATCH_DIR = Path(__file__).resolve().parent
ROOT = BATCH_DIR.parents[1]
TOPICS_PATH = BATCH_DIR / "topics-batch4.json"


def main() -> None:
    meta = json.loads(TOPICS_PATH.read_text(encoding="utf-8"))
    topics = meta["topics"]
    offset = (date.today() - START).days

    if offset < 0:
        print("SKIP", end="")
        return
    if offset >= len(topics):
        print("SKIP", end="")
        return

    slug = topics[offset]["slug"]
    html = ROOT / "articulos" / f"{slug}.html"
    if html.exists():
        print("SKIP", end="")
        return

    print(slug, end="")


if __name__ == "__main__":
    main()
