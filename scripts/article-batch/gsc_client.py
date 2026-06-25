"""Google Search Console — fetch real query data for keyword scoring."""

from __future__ import annotations

import json
import os
import re
import unicodedata
from datetime import date, timedelta
from pathlib import Path

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
DEFAULT_SITE_URL = "https://kalyo.io/"


def _normalize(text: str) -> str:
    text = unicodedata.normalize("NFD", text.lower())
    return "".join(c for c in text if unicodedata.category(c) != "Mn")


def _tokenize(text: str) -> set[str]:
    return {t for t in re.split(r"[^a-z0-9]+", _normalize(text)) if len(t) > 2}


def _load_env_local() -> None:
    """Load .env.local into os.environ if present (does not override existing)."""
    env_path = Path(__file__).resolve().parents[2] / ".env.local"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def get_credentials_path() -> Path | None:
    explicit = os.environ.get("GSC_CREDENTIALS_PATH")
    if explicit and Path(explicit).exists():
        return Path(explicit)
    default = Path(__file__).resolve().parent / "gsc-service-account.json"
    return default if default.exists() else None


def get_oauth_credentials():
    """OAuth2 user credentials via refresh token (Botio / Vercel pattern)."""
    client_id = os.environ.get("GOOGLE_CLIENT_ID")
    client_secret = os.environ.get("GOOGLE_CLIENT_SECRET")
    refresh_token = os.environ.get("GOOGLE_REFRESH_TOKEN")
    if not all([client_id, client_secret, refresh_token]):
        return None

    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
    except ImportError:
        print("WARN: pip install google-auth google-api-python-client for GSC integration")
        return None

    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
        scopes=SCOPES,
    )
    if not creds.valid:
        creds.refresh(Request())
    return creds


def get_gsc_credentials():
    """Prefer OAuth refresh token; fall back to service account JSON."""
    _load_env_local()
    oauth_creds = get_oauth_credentials()
    if oauth_creds is not None:
        return oauth_creds, "oauth"

    creds_path = get_credentials_path()
    if not creds_path:
        return None, None

    try:
        from google.oauth2 import service_account
    except ImportError:
        print("WARN: pip install google-auth google-api-python-client for GSC integration")
        return None, None

    return service_account.Credentials.from_service_account_file(str(creds_path), scopes=SCOPES), "service_account"


def fetch_search_queries(site_url: str | None = None, days: int = 90, row_limit: int = 500) -> list[dict]:
    """Return GSC queries: [{query, clicks, impressions, ctr, position}, ...]."""
    creds, auth_mode = get_gsc_credentials()
    if creds is None:
        return []

    site = site_url or os.environ.get("GSC_SITE_URL", DEFAULT_SITE_URL)

    try:
        from googleapiclient.discovery import build
    except ImportError:
        print("WARN: pip install google-auth google-api-python-client for GSC integration")
        return []

    service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)

    end = date.today() - timedelta(days=3)
    start = end - timedelta(days=days)
    body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": ["query"],
        "rowLimit": row_limit,
    }

    try:
        response = service.searchanalytics().query(siteUrl=site, body=body).execute()
    except Exception as exc:
        print(f"WARN: GSC API error ({auth_mode}, site={site}): {exc}")
        return []

    rows = []
    for row in response.get("rows", []):
        keys = row.get("keys", [])
        rows.append(
            {
                "query": keys[0] if keys else "",
                "clicks": row.get("clicks", 0),
                "impressions": row.get("impressions", 0),
                "ctr": round(row.get("ctr", 0), 4),
                "position": round(row.get("position", 0), 1),
            }
        )
    if rows:
        print(f"GSC auth: {auth_mode} | site: {site} | queries: {len(rows)}")
    return rows


def match_queries_to_topics(topics: list[dict], queries: list[dict], top_n: int = 5) -> dict[str, list[dict]]:
    """Map each topic slug to best-matching GSC queries by token overlap."""
    matches: dict[str, list[dict]] = {}
    for topic in topics:
        slug = topic["slug"]
        seeds = " ".join(
            filter(
                None,
                [
                    topic.get("primary_keyword", ""),
                    topic.get("keywords", ""),
                    slug.replace("-", " "),
                ],
            )
        )
        seed_tokens = _tokenize(seeds)
        scored = []
        for q in queries:
            query = q.get("query", "")
            overlap = len(seed_tokens & _tokenize(query))
            if overlap == 0:
                continue
            score = overlap * 10 + q.get("impressions", 0) * 0.01 + q.get("clicks", 0) * 0.5
            scored.append({**q, "match_score": round(score, 2)})
        scored.sort(key=lambda x: x["match_score"], reverse=True)
        matches[slug] = scored[:top_n]
    return matches


def save_gsc_snapshot(queries: list[dict], matches: dict[str, list[dict]], output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / "gsc-queries.json"
    payload = {
        "source": "google_search_console",
        "auth": "oauth" if os.environ.get("GOOGLE_REFRESH_TOKEN") else "service_account",
        "site_url": os.environ.get("GSC_SITE_URL", DEFAULT_SITE_URL),
        "query_count": len(queries),
        "queries": queries[:100],
        "topic_matches": matches,
    }
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return out
