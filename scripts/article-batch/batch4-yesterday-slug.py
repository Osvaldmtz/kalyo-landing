#!/usr/bin/env python3
"""Return the most recently published batch-4 slug for the enrich cron, or SKIP."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

BATCH_DIR = Path(__file__).resolve().parent
ROOT = BATCH_DIR.parents[1]
PUBLISH_COMMIT_PREFIX = "Publish batch 4 article: "
PUBLISH_COMMIT_PATTERN = re.compile(re.escape(PUBLISH_COMMIT_PREFIX) + r"(.+)")


def latest_published_slug() -> str | None:
    """Read slug from the latest official batch-4 publish commit message."""
    result = subprocess.run(
        [
            "git",
            "log",
            f"--grep={PUBLISH_COMMIT_PREFIX}",
            "--fixed-strings",
            "-1",
            "--pretty=format:%s",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    message = result.stdout.strip()
    if not message:
        return None

    match = PUBLISH_COMMIT_PATTERN.fullmatch(message)
    if not match:
        return None

    return match.group(1).strip()


def main() -> None:
    slug = latest_published_slug()
    if not slug:
        print("SKIP", end="")
        return

    html = ROOT / "articulos" / f"{slug}.html"
    if not html.exists():
        print("SKIP", end="")
        return

    content = html.read_text(encoding="utf-8")
    if "Referencias:" in content or "<strong>Referencias:</strong>" in content:
        print("SKIP", end="")
        return

    print(slug, end="")


if __name__ == "__main__":
    main()
