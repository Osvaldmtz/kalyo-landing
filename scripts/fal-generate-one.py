#!/usr/bin/env python3
"""Generate one blog image via fal.ai flux/schnell and save jpg + webp."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
FAL_MODEL = "fal-ai/flux/schnell"


def fal_generate(prompt: str, fal_key: str, retries: int = 3) -> bytes:
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            resp = requests.post(
                f"https://queue.fal.run/{FAL_MODEL}",
                headers={"Authorization": f"Key {fal_key}", "Content-Type": "application/json"},
                json={
                    "prompt": prompt,
                    "image_size": "landscape_4_3",
                    "num_images": 1,
                    "num_inference_steps": 4,
                    "output_format": "jpeg",
                },
                timeout=60,
            )
            resp.raise_for_status()
            poll_url = resp.json().get("response_url") or resp.json().get("status_url")
            if not poll_url:
                raise RuntimeError(f"No poll URL: {resp.json()}")
            for _ in range(40):
                time.sleep(2)
                poll = requests.get(poll_url, headers={"Authorization": f"Key {fal_key}"}, timeout=60)
                poll.raise_for_status()
                data = poll.json()
                if data.get("images"):
                    url = data["images"][0]["url"]
                    img = requests.get(url, timeout=120)
                    img.raise_for_status()
                    return img.content
                if data.get("status") in ("FAILED", "ERROR"):
                    raise RuntimeError(data)
            raise TimeoutError("FAL image generation timed out")
        except Exception as exc:
            last_err = exc
            print(f"  FAL attempt {attempt + 1}/{retries} failed: {exc}", file=sys.stderr)
            time.sleep(3)
    raise last_err or RuntimeError("FAL image generation failed")


def to_webp(jpeg_bytes: bytes, quality: int = 82) -> bytes:
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp_in:
        tmp_in.write(jpeg_bytes)
        tmp_in_path = tmp_in.name
    tmp_out_path = tmp_in_path.replace(".jpg", ".webp")
    script = f"""
import sharp from 'sharp';
await sharp({json.dumps(tmp_in_path)}).webp({{ quality: {quality} }}).toFile({json.dumps(tmp_out_path)});
"""
    subprocess.run(
        ["node", "--input-type=module", "-e", script],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    webp = Path(tmp_out_path).read_bytes()
    Path(tmp_in_path).unlink(missing_ok=True)
    Path(tmp_out_path).unlink(missing_ok=True)
    return webp


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True)
    parser.add_argument("--kind", required=True, choices=("hero", "inline"))
    parser.add_argument("--prompt", required=True)
    args = parser.parse_args()

    fal_key = os.environ.get("FAL_KEY")
    if not fal_key:
        print("ERROR: FAL_KEY not set", file=sys.stderr)
        sys.exit(1)

    out_dir = ROOT / "assets" / "blog"
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{args.slug}-{args.kind}"
    jpg_path = out_dir / f"{stem}.jpg"
    webp_path = out_dir / f"{stem}.webp"

    print(f"Generating {stem} via {FAL_MODEL}...")
    jpeg = fal_generate(args.prompt, fal_key)
    jpg_path.write_bytes(jpeg)
    print(f"OK jpg: {jpg_path} ({len(jpeg):,} bytes)")

    webp = to_webp(jpeg)
    webp_path.write_bytes(webp)
    print(f"OK webp: {webp_path} ({len(webp):,} bytes)")


if __name__ == "__main__":
    main()
