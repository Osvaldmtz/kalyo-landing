#!/usr/bin/env python3
"""Generate one low-cost blog-style test image via fal.ai (flux/schnell)."""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import requests

FAL_KEY = os.environ.get("FAL_KEY")
if not FAL_KEY:
    print("ERROR: FAL_KEY environment variable is not set")
    sys.exit(1)

PROMPT = (
    "Minimal flat digital illustration for psychology blog article hero image, "
    "tablet showing mental health questionnaire with purple UI elements and checkmarks, "
    "purple stethoscope, notebook with pen, small potted plant with purple leaves, "
    "brain profile icon with heart shape, clean white background with soft light purple "
    "circles, modern clinical wellness aesthetic, no text, no watermark, no people faces, "
    "professional healthcare SaaS blog illustration style"
)

OUTPUT_JPG = Path("assets/blog/fal-api-test-hero.jpg")


def generate() -> str:
    print("Calling fal-ai/flux/schnell (low cost)...")
    resp = requests.post(
        "https://queue.fal.run/fal-ai/flux/schnell",
        headers={"Authorization": f"Key {FAL_KEY}", "Content-Type": "application/json"},
        json={
            "prompt": PROMPT,
            "image_size": "landscape_4_3",
            "num_images": 1,
            "num_inference_steps": 4,
        },
        timeout=60,
    )
    print(f"Queue HTTP {resp.status_code}")
    if not resp.ok:
        print(resp.text)
        sys.exit(1)

    payload = resp.json()
    response_url = payload.get("response_url")
    status_url = payload.get("status_url")
    poll_url = response_url or status_url
    if not poll_url:
        print("ERROR: No response_url in queue response:", payload)
        sys.exit(1)

    for attempt in range(40):
        time.sleep(2)
        poll = requests.get(poll_url, headers={"Authorization": f"Key {FAL_KEY}"}, timeout=60)
        poll.raise_for_status()
        result = poll.json()
        status = result.get("status")
        print(f"Poll {attempt + 1}: status={status!r}")

        if result.get("images"):
            return result["images"][0]["url"]

        if status in ("FAILED", "ERROR"):
            print("ERROR:", result)
            sys.exit(1)

    print("ERROR: Timed out waiting for image")
    sys.exit(1)


def main() -> None:
    image_url = generate()
    print(f"Downloading: {image_url}")
    img_resp = requests.get(image_url, timeout=120)
    img_resp.raise_for_status()

    OUTPUT_JPG.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JPG.write_bytes(img_resp.content)
    print(f"OK: saved {OUTPUT_JPG} ({len(img_resp.content):,} bytes)")


if __name__ == "__main__":
    main()
