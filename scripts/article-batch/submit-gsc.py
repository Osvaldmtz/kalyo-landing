#!/usr/bin/env python3
"""Submit sitemap and request Google indexing for published article URLs."""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

import requests

BATCH_DIR = Path(__file__).resolve().parent
ROOT = BATCH_DIR.parents[1]
sys.path.insert(0, str(BATCH_DIR))

from gsc_client import (  # noqa: E402
    DEFAULT_SITE_URL,
    _load_env_local,
    article_url,
    get_access_token,
    get_gsc_credentials,
)

SITE_URL = DEFAULT_SITE_URL
SITEMAP_URL = "https://kalyo.io/sitemap.xml"
INDEX_DELAY_S = 0.5


def resolve_topics_path(batch: str) -> Path:
    if batch in ("3", "4", "5", "6"):
        return BATCH_DIR / f"topics-batch{batch}.json"
    return BATCH_DIR / f"topics-batch-{batch}.json"


def regenerate_sitemap() -> None:
    script = ROOT / "scripts" / "regenerate-sitemap.mjs"
    subprocess.run(["node", str(script)], cwd=ROOT, check=True)


def submit_sitemap() -> bool:
    creds, auth_mode = get_gsc_credentials()
    if creds is None:
        print("ERROR: no GSC credentials (GOOGLE_CLIENT_ID/SECRET/REFRESH_TOKEN)")
        return False

    from googleapiclient.discovery import build

    service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    try:
        service.sitemaps().submit(siteUrl=SITE_URL, feedpath=SITEMAP_URL).execute()
        print(f"OK: sitemap submitted ({auth_mode}, {SITEMAP_URL})")
        return True
    except Exception as exc:
        print(f"ERROR: sitemap submit failed: {exc}")
        print("      Re-authorize with ~/gsc-auth/auth-write.js (webmasters + indexing scopes)")
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
    print(f"  FAIL {url}: {resp.status_code} {resp.text[:160]}")
    return False


def verify_url_live(url: str) -> bool:
    try:
        resp = requests.head(url, timeout=15, allow_redirects=True)
        return resp.status_code == 200
    except requests.RequestException:
        return False


def request_indexing_batch(urls: list[str], delay_s: float = INDEX_DELAY_S) -> int:
    token = get_access_token()
    if not token:
        print("ERROR: Indexing API token unavailable — re-authorize with ~/gsc-auth/auth-write.js")
        return 0

    ok = 0
    for url in urls:
        if not verify_url_live(url):
            print(f"  SKIP (not live): {url}")
            continue
        if request_indexing_url(url, token):
            ok += 1
            print(f"  OK: {url}")
        time.sleep(delay_s)
    return ok


def publish_articles(
    slugs: list[str],
    *,
    regenerate_sitemap_first: bool = True,
    submit_sitemap_flag: bool = True,
    include_library_index: bool = True,
) -> dict:
    """Regenerate sitemap, submit to GSC, and request indexing for article slugs."""
    _load_env_local()

    if regenerate_sitemap_first:
        print("=== Regenerating sitemap.xml ===")
        regenerate_sitemap()

    if submit_sitemap_flag:
        print("\n=== GSC sitemap submit ===")
        submit_sitemap()

    urls: list[str] = []
    if include_library_index:
        urls.append("https://kalyo.io/articulos/")
    urls.extend(article_url(slug) for slug in slugs)

    print(f"\n=== Indexing API ({len(urls)} URLs) ===")
    indexed = request_indexing_batch(urls)

    return {
        "slugs": slugs,
        "urls_requested": len(urls),
        "urls_indexed": indexed,
    }


def slugs_from_args(slug: str | None, slugs: list[str], all_batch: bool, batch: str = "3") -> list[str]:
    if slug:
        return [slug]
    if slugs:
        return slugs
    if all_batch:
        import json

        topics_path = resolve_topics_path(batch)
        topics = json.loads(topics_path.read_text(encoding="utf-8"))["topics"]
        return [t["slug"] for t in topics]
    return []


def main() -> None:
    parser = argparse.ArgumentParser(description="Submit sitemap + request Google indexing")
    parser.add_argument("--slug", help="Single article slug")
    parser.add_argument("--slugs", nargs="+", help="Multiple slugs")
    parser.add_argument("--all-batch3", "--all-batch", action="store_true", help="Index all topics in selected batch")
    parser.add_argument("--batch", default="3", help="Topic batch: 3, 4, or inmediato")
    parser.add_argument("--skip-sitemap-regen", action="store_true")
    parser.add_argument("--skip-sitemap-submit", action="store_true")
    parser.add_argument("--no-library-index", action="store_true")
    args = parser.parse_args()

    slugs = slugs_from_args(args.slug, args.slugs or [], args.all_batch3, args.batch)
    if not slugs and not args.all_batch3:
        print("ERROR: pass --slug, --slugs, or --all-batch")
        sys.exit(1)

    result = publish_articles(
        slugs,
        regenerate_sitemap_first=not args.skip_sitemap_regen,
        submit_sitemap_flag=not args.skip_sitemap_submit,
        include_library_index=not args.no_library_index,
    )
    print(f"\nDone: {result['urls_indexed']}/{result['urls_requested']} indexing requests sent")
    if result["urls_indexed"] < result["urls_requested"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
