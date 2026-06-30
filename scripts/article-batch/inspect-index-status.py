#!/usr/bin/env python3
"""Inspect Google indexing status for all sitemap URLs via GSC URL Inspection API."""

from __future__ import annotations

import argparse
import json
import sys
import time
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

BATCH_DIR = Path(__file__).resolve().parent
ROOT = BATCH_DIR.parents[1]
OUTPUT_PATH = BATCH_DIR / "output" / "index-status.json"
SITEMAP_PATH = ROOT / "sitemap.xml"

sys.path.insert(0, str(BATCH_DIR))

from gsc_client import DEFAULT_SITE_URL, _load_env_local, get_gsc_credentials  # noqa: E402

INSPECT_DELAY_S = 0.35


def load_sitemap_urls() -> list[str]:
    root = ET.parse(SITEMAP_PATH).getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [node.find("sm:loc", ns).text for node in root.findall("sm:url", ns)]


def is_indexed(result: dict) -> bool:
    coverage = (result.get("coverageState") or "").lower()
    verdict = (result.get("verdict") or "").upper()
    return verdict == "PASS" and "indexed" in coverage


def inspect_urls(urls: list[str], site_url: str, delay_s: float) -> tuple[list[dict], list[dict]]:
    creds, auth_mode = get_gsc_credentials()
    if creds is None:
        raise RuntimeError("GSC credentials unavailable")

    from googleapiclient.discovery import build

    service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    inspect_api = service.urlInspection().index()

    results: list[dict] = []
    errors: list[dict] = []

    for i, url in enumerate(urls, 1):
        try:
            response = inspect_api.inspect(
                body={"inspectionUrl": url, "siteUrl": site_url}
            ).execute()
            idx = response.get("inspectionResult", {}).get("indexStatusResult", {})
            results.append(
                {
                    "url": url,
                    "verdict": idx.get("verdict"),
                    "coverageState": idx.get("coverageState"),
                    "indexingState": idx.get("indexingState"),
                    "robotsTxtState": idx.get("robotsTxtState"),
                    "pageFetchState": idx.get("pageFetchState"),
                    "lastCrawlTime": idx.get("lastCrawlTime"),
                    "googleCanonical": idx.get("googleCanonical"),
                    "userCanonical": idx.get("userCanonical"),
                    "indexed": is_indexed(idx),
                }
            )
        except Exception as exc:
            errors.append({"url": url, "error": str(exc)})

        if i % 10 == 0:
            print(f"  inspected {i}/{len(urls)}...", flush=True)
        time.sleep(delay_s)

    print(f"Auth: {auth_mode}")
    return results, errors


def build_report(results: list[dict], errors: list[dict], urls: list[str]) -> dict:
    article_urls = [
        u for u in urls if u.startswith("https://kalyo.io/articulos/") and u.endswith(".html")
    ]
    indexed = [r for r in results if r.get("indexed")]
    not_indexed = [r for r in results if not r.get("indexed")]
    article_results = [r for r in results if r["url"] in article_urls]
    article_indexed = [r for r in article_results if r.get("indexed")]
    coverage = Counter(r.get("coverageState") or "UNKNOWN" for r in results)

    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "site_url": DEFAULT_SITE_URL,
        "sitemap_total": len(urls),
        "articles_total": len(article_urls),
        "inspected": len(results),
        "errors": errors,
        "summary": {
            "indexed_all": len(indexed),
            "not_indexed_all": len(not_indexed),
            "indexed_articles": len(article_indexed),
            "not_indexed_articles": len(article_results) - len(article_indexed),
            "coverage_state": dict(coverage),
        },
        "not_indexed": [
            {
                "url": r["url"],
                "coverageState": r.get("coverageState"),
                "verdict": r.get("verdict"),
                "pageFetchState": r.get("pageFetchState"),
                "lastCrawlTime": r.get("lastCrawlTime"),
            }
            for r in not_indexed
        ],
        "results": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect GSC indexing status for sitemap URLs")
    parser.add_argument("--articles-only", action="store_true")
    parser.add_argument("--delay", type=float, default=INSPECT_DELAY_S)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()

    _load_env_local()
    all_urls = load_sitemap_urls()
    urls = all_urls
    if args.articles_only:
        urls = [u for u in urls if u.startswith("https://kalyo.io/articulos/") and u.endswith(".html")]

    print(f"Inspecting {len(urls)} URLs...")
    results, errors = inspect_urls(urls, DEFAULT_SITE_URL, args.delay)
    report = build_report(results, errors, all_urls)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    s = report["summary"]
    print(f"Done: {s['indexed_all']}/{report['inspected']} indexed ({s['indexed_articles']}/{report['articles_total']} articles)")
    print(f"Report: {args.output}")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
