"""Google Search Console — fetch real query data for keyword scoring."""

from __future__ import annotations

import json
import os
import re
import unicodedata
from datetime import date, timedelta
from pathlib import Path

SCOPES_READONLY = ["https://www.googleapis.com/auth/webmasters.readonly"]
SCOPES_WRITE = [
    "https://www.googleapis.com/auth/webmasters.readonly",
    "https://www.googleapis.com/auth/webmasters",
    "https://www.googleapis.com/auth/indexing",
]
SCOPES = SCOPES_WRITE
DEFAULT_SITE_URL = "https://kalyo.io/"
ARTICLE_BASE_URL = "https://kalyo.io/articulos"


def _normalize(text: str) -> str:
    text = unicodedata.normalize("NFD", text.lower())
    return "".join(c for c in text if unicodedata.category(c) != "Mn")


def _tokenize(text: str) -> set[str]:
    return {t for t in re.split(r"[^a-z0-9]+", _normalize(text)) if len(t) > 2}


GOOGLE_ENV_KEYS = frozenset({
    "GOOGLE_CLIENT_ID",
    "GOOGLE_CLIENT_SECRET",
    "GOOGLE_REFRESH_TOKEN",
    "GSC_SITE_URL",
})

PLACEHOLDER_REFRESH_TOKENS = frozenset({
    "",
    "TU_REFRESH_TOKEN",
    "PASTE_REFRESH_TOKEN",
    "PASTE_NEW_REFRESH_TOKEN",
    "your_refresh_token_here",
})


def env_local_path() -> Path:
    return Path(__file__).resolve().parents[2] / ".env.local"


def _load_env_local() -> Path | None:
    """Load Kalyo .env.local. Google/GSC keys always override shell env (no stale cache)."""
    env_path = env_local_path()
    if not env_path.exists():
        return None
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key in GOOGLE_ENV_KEYS:
            os.environ[key] = value
        else:
            os.environ.setdefault(key, value)
    return env_path


def _refresh_token_hint() -> str:
    env_path = env_local_path()
    token = os.environ.get("GOOGLE_REFRESH_TOKEN", "")
    source = str(env_path) if env_path.exists() else "environment"
    return f"source={source} token_len={len(token)}"


def _validate_refresh_token(refresh_token: str) -> None:
    if refresh_token.endswith(".apps.googleusercontent.com"):
        raise ValueError(
            "GOOGLE_REFRESH_TOKEN is set to GOOGLE_CLIENT_ID by mistake. "
            "Use the refresh token from auth-write.js (starts with 1//), not the client ID."
        )
    if refresh_token in PLACEHOLDER_REFRESH_TOKENS:
        raise ValueError(
            "GOOGLE_REFRESH_TOKEN is missing or still a placeholder in Kalyo/.env.local. "
            "Run: ~/gsc-auth/update-token.sh \"<token from auth-write.js>\""
        )
    if len(refresh_token) < 30:
        raise ValueError(
            f"GOOGLE_REFRESH_TOKEN looks invalid (len={len(refresh_token)}). "
            f"Update Kalyo/.env.local with the token from auth-write.js ({_refresh_token_hint()})"
        )


def get_credentials_path() -> Path | None:
    explicit = os.environ.get("GSC_CREDENTIALS_PATH")
    if explicit and Path(explicit).exists():
        return Path(explicit)
    default = Path(__file__).resolve().parent / "gsc-service-account.json"
    return default if default.exists() else None


def get_oauth_credentials(scopes: list[str] | None = None):
    """OAuth2 user credentials via refresh token (Botio / Vercel pattern)."""
    _load_env_local()

    client_id = os.environ.get("GOOGLE_CLIENT_ID")
    client_secret = os.environ.get("GOOGLE_CLIENT_SECRET")
    refresh_token = os.environ.get("GOOGLE_REFRESH_TOKEN")
    if not client_id or not client_secret:
        print("ERROR: GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET missing in Kalyo/.env.local")
        return None
    if not refresh_token:
        print(
            "ERROR: GOOGLE_REFRESH_TOKEN missing in Kalyo/.env.local. "
            "Local scripts do not read Vercel — run: ~/gsc-auth/update-token.sh \"<token>\""
        )
        return None

    try:
        _validate_refresh_token(refresh_token)
    except ValueError as exc:
        print(f"ERROR: {exc}")
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
        scopes=scopes or SCOPES,
    )
    try:
        if not creds.valid:
            creds.refresh(Request())
    except Exception as exc:
        err = str(exc).lower()
        if "invalid_grant" in err:
            print(
                "ERROR: invalid_grant — refresh token rejected by Google. "
                f"{_refresh_token_hint()}"
            )
            print(
                "       Ensure Kalyo/.env.local has the NEW token from auth-write.js "
                "(not a placeholder). Vercel env is not read by local scripts."
            )
        else:
            print(f"ERROR: OAuth refresh failed: {exc}")
        return None
    return creds


def get_access_token(scopes: list[str] | None = None) -> str | None:
    creds = get_oauth_credentials(scopes=scopes)
    if creds is None:
        return None
    return creds.token


def article_url(slug: str) -> str:
    return f"{ARTICLE_BASE_URL}/{slug}.html"


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
