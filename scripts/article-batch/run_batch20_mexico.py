#!/usr/bin/env python3
"""Generate batch 20 Mexico SEO articles and update index/sitemap."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BATCH_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(BATCH_DIR))

from render_aeo_article import render  # noqa: E402
from batch20_mexico_part1 import articles_part1  # noqa: E402
from batch20_mexico_part2 import articles_part2  # noqa: E402


def p(*paras: str) -> str:
    return "\n".join(f"<p>{x}</p>" for x in paras)


def table(headers, rows, cls="severity-table") -> str:
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = ""
    for row in rows:
        body += "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>"
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table>'


def word_count(text: str) -> int:
    text = re.sub(r"<[^>]+>", " ", text)
    return len(re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ]+\b", text, flags=re.UNICODE))


def visible_len(text: str) -> int:
    import html as html_mod

    return len(html_mod.unescape(text))


def validate_spec(spec: dict) -> None:
    slug = spec["slug"]
    dl = visible_len(spec["description"])
    if not (150 <= dl <= 160):
        raise ValueError(f"{slug}: description length {dl} (visible chars)")
    qw = word_count(spec["quick_answer"])
    if not (40 <= qw <= 60):
        raise ValueError(f"{slug}: quick_answer words {qw}")
    body_parts = [spec["quick_answer"], spec.get("intro_long", "")]
    for sec in spec["sections"]:
        body_parts.append(sec["html"])
    for f in spec["faqs"]:
        body_parts.append(f["q"] + " " + f["a"])
    bw = sum(word_count(x) for x in body_parts)
    if bw < 1200:
        raise ValueError(f"{slug}: body words {bw} < 1200")
    if len(spec["faqs"]) != 5:
        raise ValueError(f"{slug}: expected 5 faqs")
    if len(spec.get("related", [])) < 3:
        raise ValueError(f"{slug}: need 3+ related links")


def card_html(spec: dict) -> str:
    title = spec.get("card_title") or spec["h1"][:60]
    desc = spec.get("card_p") or spec["description"][:120]
    slug = spec["slug"]
    # decode basic entities for card display
    title_clean = (
        title.replace("&aacute;", "á")
        .replace("&eacute;", "é")
        .replace("&iacute;", "í")
        .replace("&oacute;", "ó")
        .replace("&uacute;", "ú")
        .replace("&ntilde;", "ñ")
        .replace("&mdash;", "—")
    )
    desc_clean = (
        desc.replace("&aacute;", "á")
        .replace("&eacute;", "é")
        .replace("&iacute;", "í")
        .replace("&oacute;", "ó")
        .replace("&uacute;", "ú")
        .replace("&ntilde;", "ñ")
    )
    return f'''      <a href="/articulos/{slug}.html" class="blog-card">
        <span class="blog-card-tag">Psicometría</span>
        <h3>{title_clean}</h3>
        <p>{desc_clean}</p>
      </a>
'''


def bump_index(cards: list[str], delta: int) -> None:
    index_path = ROOT / "articulos" / "index.html"
    text = index_path.read_text(encoding="utf-8")
    m = re.search(r'"numberOfItems":\s*(\d+)', text)
    if m:
        n = int(m.group(1)) + delta
        text = text.replace(m.group(0), f'"numberOfItems": {n}', 1)
    anchor = 'href="/articulos/wais-iv-evaluacion-inteligencia-adultos.html"'
    pos = text.find(anchor)
    if pos < 0:
        anchor = 'href="/articulos/que-es-el-phq-9.html"'
        pos = text.find(anchor)
    if pos < 0:
        raise RuntimeError("index anchor not found")
    end = text.find("</a>", pos)
    end = text.find("\n", end) + 1
    block = "".join(cards)
    if cards[0].strip()[:40] not in text:
        text = text[:end] + block + text[end:]
    index_path.write_text(text, encoding="utf-8")


def insert_sitemap_entries(specs: list[dict]) -> None:
    sm_path = ROOT / "sitemap.xml"
    text = sm_path.read_text(encoding="utf-8")
    anchor = "https://kalyo.io/articulos/wais-iv-evaluacion-inteligencia-adultos.html"
    pos = text.find(f"<loc>{anchor}</loc>")
    if pos < 0:
        anchor = "https://kalyo.io/articulos/que-es-el-phq-9.html"
        pos = text.find(f"<loc>{anchor}</loc>")
    end = text.find("</url>", pos) + len("</url>\n")
    blocks = []
    for spec in specs:
        loc = f"https://kalyo.io/articulos/{spec['slug']}.html"
        if loc in text:
            continue
        blocks.append(
            f"  <url>\n"
            f"    <loc>{loc}</loc>\n"
            f"    <lastmod>2026-08-01</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n"
            f"    <priority>0.8</priority>\n"
            f"  </url>\n"
        )
    if blocks:
        text = text[:end] + "".join(blocks) + text[end:]
        sm_path.write_text(text, encoding="utf-8")


def main() -> None:
    faqs_std = None
    specs = articles_part1(p, table, faqs_std) + articles_part2(p, table, faqs_std)
    out_dir = ROOT / "articulos"
    cards = []
    for spec in specs:
        validate_spec(spec)
        html = render(spec)
        path = out_dir / f"{spec['slug']}.html"
        path.write_text(html, encoding="utf-8")
        cards.append(card_html(spec))
        print(f"OK {spec['slug']} ({word_count(html)} words in file)")

    bump_index(cards, len(specs))
    insert_sitemap_entries(specs)
    print(f"\nGenerated {len(specs)} articles. Updated index and sitemap.")


if __name__ == "__main__":
    main()
