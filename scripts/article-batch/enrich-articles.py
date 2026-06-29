#!/usr/bin/env python3
"""
Enrich Kalyo article HTML with real academic citations via Perplexity Sonar + Claude Haiku.

Usage:
  python scripts/article-batch/enrich-articles.py --batch inmediato
  python scripts/article-batch/enrich-articles.py --batch 4 --slug phq-2-tamizaje-depresion-breve
  python scripts/article-batch/enrich-articles.py phq-2-tamizaje-depresion-breve tmms-24-inteligencia-emocional
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

import anthropic
import requests

ROOT = Path(__file__).resolve().parents[2]
ARTICULOS = ROOT / "articulos"
BATCH_DIR = Path(__file__).resolve().parent
LOG_PATH = BATCH_DIR / "output" / "enrich-log.json"

ENRICH_SECTION_RE = re.compile(
    r"propiedades psicom|validez|confiabilidad|fiabilidad|evidencia cient|"
    r"psicometr|interpretaci.*cl.nica|criterios diagn|instrumentos de eval|"
    r"marco normativo|implicaciones para|evaluaci.*diagn|baremos y normaliz",
    re.I,
)
SKIP_SECTION_RE = re.compile(
    r"preguntas frecuentes|accede|kalyo|consulta nuestro|solicita|administra|"
    r"eval&uacute;a|aplica el|prueba gratis",
    re.I,
)


def resolve_topics_path(batch: str) -> Path:
    if batch in ("3", "4"):
        return BATCH_DIR / f"topics-batch{batch}.json"
    return BATCH_DIR / f"topics-batch-{batch}.json"


def load_topics(batch: str | None) -> list[dict]:
    if not batch:
        return []
    path = resolve_topics_path(batch)
    return json.loads(path.read_text(encoding="utf-8"))["topics"]


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


def topic_to_config(topic: dict) -> dict:
    keyword = topic.get("primary_keyword", topic["slug"])
    instrument = keyword.split("|")[0].strip()
    category = topic.get("category", "")
    if category.startswith("normativa") or category.startswith("inclusion") or topic.get("test_slug") is None:
        search = f"{keyword} Colombia evidence clinical guidelines research"
    else:
        search = f"{instrument} psychometric validation sensitivity specificity reliability"
    return {
        "instrument": instrument,
        "topic": search,
        "sections": None,
    }


def list_h2_sections(html: str) -> list[str]:
    return re.findall(r"<h2>([^<]+)</h2>", html)


def section_body(html: str, section_title: str) -> str:
    pattern = rf"<h2>{re.escape(section_title)}</h2>([\s\S]*?)(?=<h2>|$)"
    match = re.search(pattern, html)
    return match.group(1) if match else ""


def is_section_enriched(html: str, section_title: str) -> bool:
    body = section_body(html, section_title)
    return "Referencias:" in body or "<strong>Referencias:</strong>" in body


def is_article_enriched(html: str) -> bool:
    return html.count("Referencias:") >= 1 or html.count("<strong>Referencias:</strong>") >= 1


def detect_sections(html: str, max_sections: int = 2) -> list[str]:
    candidates: list[tuple[int, int, str]] = []
    for idx, title in enumerate(list_h2_sections(html)):
        plain = html_lib.unescape(title)
        if SKIP_SECTION_RE.search(plain):
            continue
        if is_section_enriched(html, title):
            continue
        priority = 0
        if ENRICH_SECTION_RE.search(plain):
            priority = 2
        elif idx >= 1:
            priority = 1
        if priority:
            candidates.append((priority, idx, title))

    candidates.sort(key=lambda x: (-x[0], x[1]))
    seen: list[str] = []
    for _, _, title in candidates:
        if title not in seen:
            seen.append(title)
        if len(seen) >= max_sections:
            break

    if not seen:
        for idx, title in enumerate(list_h2_sections(html)):
            plain = html_lib.unescape(title)
            if SKIP_SECTION_RE.search(plain) or is_section_enriched(html, title):
                continue
            if idx == 0:
                continue
            seen.append(title)
            if len(seen) >= max_sections:
                break
    return seen


def build_config(slug: str, topics_by_slug: dict[str, dict]) -> dict | None:
    html_path = ARTICULOS / f"{slug}.html"
    if not html_path.exists():
        print(f"WARN: HTML not found for {slug}, skipping")
        return None
    html = html_path.read_text(encoding="utf-8")
    if is_article_enriched(html) and os.environ.get("ENRICH_FORCE") != "1":
        print(f"  skip {slug}: already enriched")
        return None

    topic = topics_by_slug.get(slug, {"slug": slug, "primary_keyword": slug.replace("-", " ")})
    cfg = topic_to_config(topic)
    sections = detect_sections(html)
    if not sections:
        print(f"WARN: no enrichable sections for {slug}, skipping")
        return None
    cfg["sections"] = sections
    return cfg


def perplexity_research(instrument: str, topic: str) -> dict:
    key = os.environ.get("PERPLEXITY_API_KEY")
    if not key:
        raise RuntimeError("PERPLEXITY_API_KEY missing in .env.local")

    prompt = f"""Find exactly 3 peer-reviewed scientific studies or official primary sources about {instrument}.

Search focus: {topic}

Return ONLY valid JSON (no markdown) with this structure:
{{
  "studies": [
    {{
      "authors": "LastName et al.",
      "year": 2003,
      "title": "Full study title",
      "journal": "Journal name",
      "doi_or_pmid": "DOI or PMID URL",
      "key_findings": "2-3 sentences with specific numbers: sensitivity, specificity, Cronbach alpha, cutpoints, sample size",
      "inline_citation": "Author et al., 2003"
    }}
  ]
}}

Requirements:
- Only real published studies or official legal/government primary documents for normative topics
- Include at least one original validation or primary source
- Prefer studies with PMID or DOI
- Numbers must come from the actual study"""

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
        timeout=90,
    )
    resp.raise_for_status()
    raw = resp.json()["choices"][0]["message"]["content"].strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(raw)


def parse_json_response(raw: str) -> dict:
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        start = raw.find("{")
        end = raw.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(raw[start:end])
        raise


def rewrite_section(
    client: anthropic.Anthropic,
    instrument: str,
    section_title: str,
    original_paragraphs: list[str],
    studies: list[dict],
) -> tuple[list[str], str]:
    studies_json = json.dumps(studies, ensure_ascii=False, indent=2)
    originals = "\n\n".join(original_paragraphs)

    prompt = f"""Eres redactor clínico para kalyo.io (psicólogos Colombia/México).

Instrumento: {instrument}
Sección: {html_lib.unescape(section_title)}

Párrafos originales (HTML entities):
{originals}

Estudios verificados (usa SOLO estos, no inventes otros):
{studies_json}

Reescribe los párrafos enriqueciéndolos con:
- Citas inline en formato (Autor et al., AÑO)
- Datos numéricos específicos de los estudios
- Tono profesional clínico, español
- HTML entities para acentos (&aacute; &eacute; &iacute; &oacute; &uacute; &ntilde; &ge; &le;)
- NO uses markdown
- Mantén 2 párrafos de longitud similar o ligeramente mayor

Devuelve SOLO JSON válido escapando comillas dentro de strings:
{{
  "paragraphs": ["p1", "p2"],
  "references_html": "<p><strong>Referencias:</strong></p><ol><li>Autor (Año). Título. <em>Journal</em>. DOI</li></ol>"
}}

En references_html: formato APA breve, 3 items (uno por estudio), sin saltos de línea dentro del JSON string."""

    last_err = None
    for attempt in range(3):
        msg = client.messages.create(
            model=os.environ.get("ARTICLE_MODEL", "claude-haiku-4-5-20251001"),
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = msg.content[0].text.strip()
        try:
            data = parse_json_response(raw)
            return data["paragraphs"], data["references_html"]
        except (json.JSONDecodeError, KeyError) as exc:
            last_err = exc
            print(f"    JSON retry {attempt + 1}/3: {exc}")
            time.sleep(2)
    raise last_err or RuntimeError("rewrite_section failed")


def extract_section(html: str, section_title: str) -> tuple[str, list[str], int, int]:
    pattern = rf"(<h2>{re.escape(section_title)}</h2>)([\s\S]*?)(?=<h2>|$)"
    match = re.search(pattern, html)
    if not match:
        raise ValueError(f"Section not found: {section_title}")

    body = match.group(2)
    paragraphs = re.findall(r"<p>\s*([\s\S]*?)\s*</p>", body)
    paragraphs = [
        p.strip()
        for p in paragraphs
        if "Referencias:" not in p and "<ol>" not in p and "<strong>Referencias:</strong>" not in p
    ]
    return match.group(1) + body, paragraphs, match.start(), match.end()


def paragraphs_to_html(paragraphs: list[str]) -> str:
    return "\n\n    ".join(f"<p>\n      {p}\n    </p>" for p in paragraphs)


def enrich_html(html: str, section_title: str, new_paragraphs: list[str], references_html: str) -> str:
    pattern = rf"(<h2>{re.escape(section_title)}</h2>)([\s\S]*?)(?=<h2>)"
    match = re.search(pattern, html)
    if not match:
        raise ValueError(f"Section not found for replace: {section_title}")

    refs_html = references_html.replace("<ol>", "<ol>\n      ").replace("</li><li>", "</li>\n      <li>")
    new_body = "\n    " + paragraphs_to_html(new_paragraphs) + "\n\n    " + refs_html + "\n\n    "
    return html[: match.start()] + match.group(1) + new_body + html[match.end() :]


def enrich_article(slug: str, cfg: dict, client: anthropic.Anthropic, log: dict) -> bool:
    html_path = ARTICULOS / f"{slug}.html"
    if not html_path.exists():
        raise FileNotFoundError(html_path)

    print(f"\n=== Enriching {slug} ===")
    print(f"  Perplexity research: {cfg['instrument']}...")
    research = perplexity_research(cfg["instrument"], cfg["topic"])
    studies = research.get("studies", [])
    print(f"  Found {len(studies)} studies")

    html = html_path.read_text(encoding="utf-8")
    article_log = {
        "slug": slug,
        "instrument": cfg["instrument"],
        "studies": studies,
        "sections_enriched": [],
    }

    for section_title in cfg["sections"]:
        if is_section_enriched(html, section_title):
            print(f"  skip section (already enriched): {html_lib.unescape(section_title)}")
            continue
        print(f"  Rewriting section: {html_lib.unescape(section_title)}")
        _, original_paras, _, _ = extract_section(html, section_title)
        if not original_paras:
            print(f"    no paragraphs, skipping section")
            continue
        new_paras, refs_html = rewrite_section(
            client, cfg["instrument"], section_title, original_paras, studies
        )
        html = enrich_html(html, section_title, new_paras, refs_html)
        article_log["sections_enriched"].append(
            {
                "section": section_title,
                "original_paragraphs": original_paras,
                "enriched_paragraphs": new_paras,
            }
        )
        time.sleep(1)

    if not article_log["sections_enriched"]:
        print(f"  nothing enriched for {slug}")
        return False

    html_path.write_text(html, encoding="utf-8")
    log["articles"].append(article_log)
    print(f"  OK: {html_path.name}")
    return True


def append_log(new_log: dict) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    if LOG_PATH.exists():
        try:
            existing = json.loads(LOG_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = {"articles": []}
    else:
        existing = {"articles": []}

    existing_slugs = {a["slug"] for a in existing.get("articles", [])}
    for article in new_log.get("articles", []):
        if article["slug"] in existing_slugs:
            existing["articles"] = [a for a in existing["articles"] if a["slug"] != article["slug"]]
        existing["articles"].append(article)
    existing["generated_at"] = new_log.get("generated_at")
    LOG_PATH.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")


def resolve_slugs(args: argparse.Namespace, topics: list[dict]) -> list[str]:
    if args.slugs:
        return args.slugs
    if args.slug:
        return [args.slug]
    if args.batch:
        slugs = [t["slug"] for t in topics]
        if args.limit:
            slugs = slugs[: args.limit]
        return slugs
    return []


def main() -> None:
    load_env()
    parser = argparse.ArgumentParser(description="Enrich Kalyo articles with academic citations")
    parser.add_argument("slugs", nargs="*", help="Article slugs (optional if --batch or --slug)")
    parser.add_argument("--batch", help="Topic batch: inmediato, 3, 4")
    parser.add_argument("--slug", help="Single slug to enrich")
    parser.add_argument("--limit", type=int, help="Max articles when using --batch")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY missing")
        sys.exit(1)

    topics = load_topics(args.batch)
    topics_by_slug = {t["slug"]: t for t in topics}
    slugs = resolve_slugs(args, topics)
    if not slugs:
        print("ERROR: provide slugs, --slug, or --batch")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    log = {"generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "articles": []}
    enriched_count = 0

    for slug in slugs:
        cfg = build_config(slug, topics_by_slug)
        if not cfg:
            continue
        if enrich_article(slug, cfg, client, log):
            enriched_count += 1

    if log["articles"]:
        append_log(log)
        print(f"\nLog updated: {LOG_PATH} ({enriched_count} articles)")
    else:
        print("\nNo articles enriched.")


if __name__ == "__main__":
    main()
