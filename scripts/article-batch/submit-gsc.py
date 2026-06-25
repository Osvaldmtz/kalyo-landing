#!/usr/bin/env python3
"""Submit sitemap and request indexing for new article URLs via Google APIs."""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

import requests

BATCH_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BATCH_DIR))

from gsc_client import DEFAULT_SITE_URL, _load_env_local, get_gsc_credentials  # noqa: E402

SITE_URL = os.environ.get("GSC_SITE_URL", DEFAULT_SITE_URL)
SITEMAP_URL = "https://kalyo.io/sitemap.xml"
INDEXING_SCOPE = "https://www.googleapis.com/auth/indexing"
TOPICS_PATH = BATCH_DIR / "topics-batch3.json"


def get_indexing_access_token() -> str | None:
    client_id = os.environ.get("GOOGLE_CLIENT_ID")
    client_secret = os.environ.get("GOOGLE_CLIENT_SECRET")
    refresh_token = os.environ.get("GOOGLE_REFRESH_TOKEN")
    if not all([client_id, client_secret, refresh_token]):
        return None
    resp = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
            "scope": INDEXING_SCOPE,
        },
        timeout=30,
    )
    if not resp.ok:
        print(f"WARN: Indexing API token failed: {resp.text[:200]}")
        return None
    return resp.json().get("access_token")


def submit_sitemap() -> bool:
    creds, auth_mode = get_gsc_credentials()
    if creds is None:
        print("ERROR: no GSC credentials")
        return False

    from googleapiclient.discovery import build

    service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    try:
        service.sitemaps().submit(siteUrl=SITE_URL, feedpath=SITEMAP_URL).execute()
        print(f"OK: sitemap submitted to GSC ({auth_mode}, {SITE_URL})")
        return True
    except Exception as exc:
        print(f"WARN: sitemap submit failed: {exc}")
        return False


def request_indexing_url(url: str, access_token: str) -> bool:
    resp = requests.post(
        "https://indexing.googleapis.com/v3/urlNotifications:publish",
        headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"},
        json={"url": url, "type": "URL_UPDATED"},
        timeout=30,
    )
    if resp.status_code == 200:
        return True
    print(f"  FAIL {url}: {resp.status_code} {resp.text[:120]}")
    return False


def batch3_urls() -> list[str]:
    topics = json.loads(TOPICS_PATH.read_text(encoding="utf-8"))["topics"]
    return [f"https://kalyo.io/articulos/{t['slug']}.html" for t in topics]


def request_indexing_batch(urls: list[str], delay_s: float = 0.5) -> int:
    token = get_indexing_access_token()
    if not token:
        print("WARN: Indexing API unavailable — OAuth token may lack indexing scope.")
        print("      Sitemap submit still helps; re-authorize with indexing scope if needed.")
        return 0

    ok = 0
    for url in urls:
        if request_indexing_url(url, token):
            ok += 1
            print(f"  OK: {url}")
        time.sleep(delay_s)
    return ok


def main() -> None:
    _load_env_local()

    print("=== GSC sitemap submit ===")
    submit_sitemap()

    print("\n=== Indexing API (batch 3 + library) ===")
    urls = ["https://kalyo.io/articulos/"] + batch3_urls()
    n = request_indexing_batch(urls)
    print(f"\nIndexing requests: {n}/{len(urls)}")


if __name__ == "__main__":
    main()
