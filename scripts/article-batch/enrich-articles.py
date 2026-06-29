#!/usr/bin/env python3
"""
Enrich Kalyo article HTML with real academic citations via Perplexity Sonar + Claude Haiku.

Usage:
  python scripts/article-batch/enrich-articles.py \\
    phq-2-tamizaje-depresion-breve gad-2-tamizaje-ansiedad-breve tmms-24-inteligencia-emocional
"""

from __future__ import annotations

import argparse
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

ARTICLE_CONFIG = {
    "phq-2-tamizaje-depresion-breve": {
        "instrument": "PHQ-2 (Patient Health Questionnaire-2)",
        "topic": "PHQ-2 depression screening validation sensitivity specificity cutpoint",
        "sections": [
            "Interpretaci&oacute;n de Puntuaciones",
            "Evidencia Cient&iacute;fica y Validaci&oacute;n",
        ],
    },
    "gad-2-tamizaje-ansiedad-breve": {
        "instrument": "GAD-2 (Generalized Anxiety Disorder-2)",
        "topic": "GAD-2 anxiety screening validation Spitzer sensitivity specificity",
        "sections": [
            "Criterios de Interpretaci&oacute;n Cl&iacute;nica",
            "Propiedades Psicom&eacute;tricas y Validez",
        ],
    },
    "tmms-24-inteligencia-emocional": {
        "instrument": "TMMS-24 (Trait Meta-Mood Scale)",
        "topic": "TMMS-24 emotional intelligence validation Spanish Salovey Cronbach",
        "sections": [
            "Propiedades psicom&eacute;tricas y confiabilidad",
        ],
    },
}


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


def perplexity_research(instrument: str, topic: str) -> dict:
    key = os.environ.get("PERPLEXITY_API_KEY")
    if not key:
        raise RuntimeError("PERPLEXITY_API_KEY missing in .env.local")

    prompt = f"""Find exactly 3 peer-reviewed scientific studies about {instrument} psychometric validation.

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
- Only real published studies (no blogs or guidelines unless they cite primary research)
- Include at least one original validation study
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
Sección: {section_title}

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
    """Return (section_html, paragraphs, start, end) for a h2 section."""
    pattern = rf"(<h2>{re.escape(section_title)}</h2>)([\s\S]*?)(?=<h2>|$)"
    match = re.search(pattern, html)
    if not match:
        raise ValueError(f"Section not found: {section_title}")

    header = match.group(1)
    body = match.group(2)
    paragraphs = re.findall(r"<p>\s*([\s\S]*?)\s*</p>", body)
    # Skip references if already enriched
    paragraphs = [p.strip() for p in paragraphs if "Referencias:" not in p and "<ol>" not in p]
    return header + body, paragraphs, match.start(), match.end()


def paragraphs_to_html(paragraphs: list[str]) -> str:
    return "\n\n    ".join(f"<p>\n      {p}\n    </p>" for p in paragraphs)


def enrich_html(html: str, section_title: str, new_paragraphs: list[str], references_html: str) -> str:
    pattern = rf"(<h2>{re.escape(section_title)}</h2>)([\s\S]*?)(?=<h2>)"
    match = re.search(pattern, html)
    if not match:
        raise ValueError(f"Section not found for replace: {section_title}")

    new_body = (
        "\n    "
        + paragraphs_to_html(new_paragraphs)
        + "\n\n    "
        + refs_html.replace("<ol>", "<ol>\n      ").replace("</li><li>", "</li>\n      <li>")
        + "\n\n    "
    )
    return html[: match.start()] + match.group(1) + new_body + html[match.end() :]


def enrich_article(slug: str, client: anthropic.Anthropic, log: dict) -> None:
    cfg = ARTICLE_CONFIG[slug]
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
        print(f"  Rewriting section: {section_title}")
        _, original_paras, _, _ = extract_section(html, section_title)
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

    html_path.write_text(html, encoding="utf-8")
    log["articles"].append(article_log)
    print(f"  OK: {html_path.name}")


def main() -> None:
    load_env()
    parser = argparse.ArgumentParser(description="Enrich Kalyo articles with academic citations")
    parser.add_argument("slugs", nargs="*", default=list(ARTICLE_CONFIG.keys()))
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY missing")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    log = {"generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "articles": []}

    for slug in args.slugs:
        if slug not in ARTICLE_CONFIG:
            print(f"WARN: unknown slug {slug}, skipping")
            continue
        enrich_article(slug, client, log)

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nLog written: {LOG_PATH}")


if __name__ == "__main__":
    main()
