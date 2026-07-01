#!/usr/bin/env python3
"""Return today's batch-4 slug for the daily cron, or SKIP."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import date
from pathlib import Path

START = date(2026, 6, 30)
BATCH_DIR = Path(__file__).resolve().parent
ROOT = BATCH_DIR.parents[1]
TOPICS_PATH = BATCH_DIR / "topics-batch4.json"
PUBLISH_COMMIT_PREFIX = "Publish batch 4 article: "


def is_officially_published(slug: str) -> bool:
    """True if the official batch-4 pipeline already committed this slug."""
    message = f"{PUBLISH_COMMIT_PREFIX}{slug}"
    result = subprocess.run(
        ["git", "log", "-1", f"--grep={message}", "--format=%H"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return bool(result.stdout.strip())


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

    # Catch up: publish the earliest topic through today not yet in the official pipeline.
    for topic in topics[: offset + 1]:
        slug = topic["slug"]
        if not is_officially_published(slug):
            print(slug, end="")
            return

    print("SKIP", end="")


if __name__ == "__main__":
    main()
