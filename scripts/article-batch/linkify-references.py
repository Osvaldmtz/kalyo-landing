#!/usr/bin/env python3
"""Linkify academic references in enriched Kalyo articles.

Modes:
  python linkify-references.py              # wrap bare URLs, DOIs, PMIDs
  python linkify-references.py --resolve    # + Perplexity Sonar for author/year refs
"""

from __future__ import annotations

import argparse
import html as html_lib
import json
import os
import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
ARTICULOS = ROOT / "articulos"
BATCH_DIR = Path(__file__).resolve().parent
CACHE_PATH = BATCH_DIR / "output" / "reference-link-cache.json"

REF_BLOCK = re.compile(
    r"(<p><strong>Referencias:</strong></p>\s*<ol>)([\s\S]*?)(</ol>)",
    re.IGNORECASE,
)
LI_RE = re.compile(r"(<li>)([\s\S]*?)(</li>)", re.IGNORECASE)
URL_RE = re.compile(r"https://[^\s<\"']+")
DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s<\"']+)", re.IGNORECASE)
PMID_RE = re.compile(r"PMID:\s*(\d+)", re.IGNORECASE)
HAS_LINK = re.compile(r'<a\s+href=', re.IGNORECASE)
HTTP_RE = re.compile(r"https?://", re.IGNORECASE)
SKIP_RE = re.compile(
    r"no se dispone|no hay estudios|nota:\s*no se",
    re.IGNORECASE,
)
ANCHOR_OPEN = re.compile(r'<a\s+href="([^"]+)"([^>]*)>', re.IGNORECASE)
ANCHOR_SPLIT = re.compile(r"(<a [^>]*>|</a>)", re.IGNORECASE)


def load_env() -> None:
    env_path = ROOT / ".env.local"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        val = val.strip().strip('"').strip("'")
        os.environ.setdefault(key.strip(), val)


def plain_text(html_fragment: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html_fragment)
    return re.sub(r"\s+", " ", html_lib.unescape(text)).strip()


def is_unlinked_reference(li_inner: str) -> bool:
    if SKIP_RE.search(li_inner):
        return False
    if HAS_LINK.search(li_inner):
        return False
    if PMID_RE.search(li_inner):
        return False
    if HTTP_RE.search(li_inner):
        return False
    return bool(plain_text(li_inner))


def normalize_doi(raw: str | None) -> str | None:
    if not raw:
        return None
    doi = raw.strip()
    for prefix in (
        "https://doi.org/",
        "http://doi.org/",
        "doi.org/",
        "DOI:",
        "doi:",
    ):
        if doi.lower().startswith(prefix.lower()):
            doi = doi[len(prefix) :].strip()
    doi = doi.rstrip(".,;)")
    return doi if doi.startswith("10.") else None


def normalize_pmid(raw: str | None) -> str | None:
    if not raw:
        return None
    digits = re.sub(r"\D", "", str(raw))
    return digits if 5 <= len(digits) <= 9 else None


def make_reference_link(doi: str | None = None, pmid: str | None = None) -> str:
    doi = normalize_doi(doi)
    pmid = normalize_pmid(pmid)
    if doi:
        url = f"https://doi.org/{doi}"
        return (
            f' <a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
        )
    if pmid:
        url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        return (
            f' <a href="{url}" target="_blank" rel="noopener noreferrer">'
            f"PMID: {pmid}</a>"
        )
    return ""


def add_target_to_anchors(html: str) -> str:
    def repl(m: re.Match) -> str:
        href, rest = m.group(1), m.group(2)
        if 'target="_blank"' in rest:
            return m.group(0)
        return f'<a href="{href}" target="_blank" rel="noopener noreferrer"{rest}>'

    return ANCHOR_OPEN.sub(repl, html)


def _outside_anchors(text: str, replacer) -> str:
    parts = ANCHOR_SPLIT.split(text)
    out: list[str] = []
    in_anchor = False
    for part in parts:
        if part.lower().startswith("<a "):
            in_anchor = True
            out.append(part)
        elif part.lower() == "</a>":
            in_anchor = False
            out.append(part)
        elif in_anchor:
            out.append(part)
        else:
            out.append(replacer(part))
    return "".join(out)


def wrap_bare_urls(text: str) -> str:
    return _outside_anchors(
        text,
        lambda part: URL_RE.sub(
            lambda m: (
                f'<a href="{m.group(0)}" target="_blank" rel="noopener noreferrer">'
                f"{m.group(0)}</a>"
            ),
            part,
        ),
    )


def wrap_doi(text: str) -> str:
    return _outside_anchors(
        text,
        lambda part: DOI_RE.sub(
            lambda m: make_reference_link(doi=m.group(1)).lstrip(),
            part,
        ),
    )


def wrap_pmid(text: str) -> str:
    return _outside_anchors(
        text,
        lambda part: PMID_RE.sub(
            lambda m: make_reference_link(pmid=m.group(1)).lstrip(),
            part,
        ),
    )


def process_reference_block(content: str) -> str:
    content = add_target_to_anchors(content)
    content = wrap_bare_urls(content)
    content = wrap_doi(content)
    return wrap_pmid(content)


def load_cache() -> dict[str, dict]:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    return {}


def save_cache(cache: dict[str, dict]) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")


def perplexity_resolve_batch(citations: list[str]) -> list[dict]:
    key = os.environ.get("PERPLEXITY_API_KEY")
    if not key:
        raise RuntimeError("PERPLEXITY_API_KEY missing in .env.local")

    numbered = "\n".join(f"{i + 1}. {c}" for i, c in enumerate(citations))
    prompt = f"""For each academic citation below, find the real DOI or PubMed PMID.

Return ONLY a JSON array with one object per citation, in the same order:
[
  {{"id": 1, "doi": "10.xxxx/yyyy" or null, "pmid": "12345678" or null}},
  ...
]

Rules:
- Prefer DOI when both exist
- doi must be the bare DOI (no https://doi.org/ prefix)
- pmid must be digits only
- Use null for both fields if the source has no DOI/PMID (laws, manuals, books, gray literature)
- Only include verified identifiers for the exact publication described

Citations:
{numbered}"""

    last_err: Exception | None = None
    for attempt in range(3):
        try:
            resp = requests.post(
                "https://api.perplexity.ai/chat/completions",
                headers={
                    "Authorization": f"Bearer {key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "sonar",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.1,
                },
                timeout=120,
            )
            resp.raise_for_status()
            raw = resp.json()["choices"][0]["message"]["content"].strip()
            if raw.startswith("```"):
                raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()
            data = json.loads(raw)
            if not isinstance(data, list):
                raise ValueError("Expected JSON array")
            if len(data) != len(citations):
                raise ValueError(f"Expected {len(citations)} results, got {len(data)}")
            return data
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, ValueError, json.JSONDecodeError) as exc:
            last_err = exc
            print(f"    Perplexity retry {attempt + 1}/3: {exc}")
            time.sleep(8 * (attempt + 1))
    raise last_err or RuntimeError("Perplexity resolve failed")


def resolve_unlinked_references(batch_size: int = 6) -> dict[str, dict]:
    cache = load_cache()
    pending: list[str] = []

    for path in sorted(ARTICULOS.glob("*.html")):
        if path.name == "index.html":
            continue
        html = path.read_text(encoding="utf-8")
        for m in REF_BLOCK.finditer(html):
            for _, inner, _ in LI_RE.findall(m.group(2)):
                if not is_unlinked_reference(inner):
                    continue
                key = inner.strip()
                if key not in cache and key not in pending:
                    pending.append(key)

    print(f"Pending citations to resolve: {len(pending)}")
    for i in range(0, len(pending), batch_size):
        batch = pending[i : i + batch_size]
        plain_batch = [plain_text(item) for item in batch]
        print(f"  resolving batch {i // batch_size + 1}/{(len(pending) + batch_size - 1) // batch_size} ({len(batch)} items)")
        try:
            results = perplexity_resolve_batch(plain_batch)
        except Exception as exc:
            print(f"  WARN batch failed: {exc}")
            for item in batch:
                cache.setdefault(item, {"doi": None, "pmid": None, "error": str(exc)})
            save_cache(cache)
            time.sleep(5)
            continue

        for item, result in zip(batch, results):
            cache[item] = {
                "doi": normalize_doi(result.get("doi")),
                "pmid": normalize_pmid(result.get("pmid")),
            }
            label = cache[item]["doi"] or (f"PMID:{cache[item]['pmid']}" if cache[item]["pmid"] else "none")
            print(f"    {plain_text(item)[:70]}... -> {label}")
        save_cache(cache)
        time.sleep(2)

    return cache


def apply_resolved_links(cache: dict[str, dict] | None = None) -> int:
    if cache is None:
        cache = load_cache()
    updated_files = 0

    for path in sorted(ARTICULOS.glob("*.html")):
        if path.name == "index.html":
            continue
        html = path.read_text(encoding="utf-8")
        if "Referencias:" not in html:
            continue

        changed = False

        def block_repl(m: re.Match) -> str:
            nonlocal changed
            before, body, after = m.group(1), m.group(2), m.group(3)

            def li_repl(li_m: re.Match) -> str:
                nonlocal changed
                open_tag, inner, close_tag = li_m.group(1), li_m.group(2), li_m.group(3)
                if not is_unlinked_reference(inner):
                    return li_m.group(0)
                key = inner.strip()
                resolved = cache.get(key, {})
                link = make_reference_link(resolved.get("doi"), resolved.get("pmid"))
                if not link:
                    return li_m.group(0)
                changed = True
                return open_tag + inner.rstrip() + link + close_tag

            new_body = LI_RE.sub(li_repl, body)
            new_body = process_reference_block(new_body)
            if new_body != body:
                changed = True
            return before + new_body + after

        new_html = REF_BLOCK.sub(block_repl, html)
        if changed:
            path.write_text(new_html, encoding="utf-8")
            updated_files += 1
            print(f"  updated: {path.name}")

    return updated_files


def process_file(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    if "Referencias:" not in html:
        return False

    changed = False

    def repl(m: re.Match) -> str:
        nonlocal changed
        before, body, after = m.group(1), m.group(2), m.group(3)
        new_body = process_reference_block(body)
        if new_body != body:
            changed = True
        return before + new_body + after

    new_html = REF_BLOCK.sub(repl, html)
    if changed:
        path.write_text(new_html, encoding="utf-8")
    return changed


def linkify_all() -> int:
    updated = 0
    for path in sorted(ARTICULOS.glob("*.html")):
        if path.name == "index.html":
            continue
        if process_file(path):
            updated += 1
            print(f"  linkified: {path.name}")
    return updated


def main() -> None:
    parser = argparse.ArgumentParser(description="Linkify academic references in articles")
    parser.add_argument(
        "--resolve",
        action="store_true",
        help="Resolve bare author/year citations via Perplexity Sonar",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=6,
        help="Citations per Perplexity request (default: 6)",
    )
    args = parser.parse_args()

    load_env()

    if args.resolve:
        cache = resolve_unlinked_references(batch_size=args.batch_size)
        count = apply_resolved_links(cache)
        print(f"Applied resolved links: {count} files updated")
    else:
        count = linkify_all()
        print(f"Done: {count} files linkified")


if __name__ == "__main__":
    main()
