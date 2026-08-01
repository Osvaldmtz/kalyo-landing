#!/usr/bin/env python3
"""Generate Phase 2+3 part 2: Bolivia, Paraguay, CIE-11 TOC and Bipolar."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "articulos"
BATCH_DIR = Path(__file__).resolve().parent

sys.path.insert(0, str(BATCH_DIR))
from phase2_phase3_part2_batch_content import ARTICLES  # noqa: E402
from render_ley1616_article import render, word_count  # noqa: E402

INDEX_CARDS = {
    "normativa-psicologia-bolivia": ("normativas-leyes", "Normativa"),
    "normativa-psicologia-paraguay": ("normativas-leyes", "Normativa"),
    "cie-11-toc-codigos-psicologos": ("practica-clinica", "Gu&iacute;a cl&iacute;nica"),
    "cie-11-trastorno-bipolar-codigos": ("practica-clinica", "Gu&iacute;a cl&iacute;nica"),
}

SECTION_MARKERS = {
    "normativas-leyes": 'id="normativas-leyes"',
    "practica-clinica": 'id="practica-clinica"',
}


def make_card(spec: dict, tag: str) -> str:
    slug = spec["slug"]
    h3 = spec["title"].split("|")[0].strip()
    desc = spec["description"]
    if len(desc) > 120:
        desc = desc[:117] + "…"
    return (
        f'      <a href="/articulos/{slug}.html" class="blog-card">\n'
        f'        <span class="blog-card-tag">{tag}</span>\n'
        f"        <h3>{h3}</h3>\n"
        f"        <p>{desc}</p>\n"
        f"      </a>\n"
    )


def insert_cards(specs: list[dict]) -> int:
    index_path = ART / "index.html"
    html = index_path.read_text(encoding="utf-8")
    added = 0
    for spec in specs:
        slug = spec["slug"]
        href = f'/articulos/{slug}.html'
        if href in html:
            print(f"  index card exists: {slug}")
            continue
        section_id, tag = INDEX_CARDS[slug]
        marker = SECTION_MARKERS[section_id]
        pos = html.find(marker)
        if pos < 0:
            raise SystemExit(f"section not found: {section_id}")
        grid_pos = html.find('<div class="blog-grid blog-grid--library">', pos)
        if grid_pos < 0:
            raise SystemExit(f"grid not found in {section_id}")
        insert_at = grid_pos + len('<div class="blog-grid blog-grid--library">') + 1
        card = make_card(spec, tag)
        html = html[:insert_at] + "\n" + card + html[insert_at:]
        added += 1
        print(f"  inserted card: {slug} -> {section_id}")
    index_path.write_text(html, encoding="utf-8")
    return added


def bump_index_count(delta: int) -> None:
    index_path = ART / "index.html"
    text = index_path.read_text(encoding="utf-8")
    m = re.search(r'"numberOfItems":\s*(\d+)', text)
    if not m:
        raise SystemExit("numberOfItems not found")
    n = int(m.group(1)) + delta
    text = text.replace(m.group(0), f'"numberOfItems": {n}', 1)
    index_path.write_text(text, encoding="utf-8")
    print(f"  numberOfItems: {m.group(1)} -> {n}")


def main() -> None:
    results = []
    for spec in ARTICLES:
        slug = spec["slug"]
        out = ART / f"{slug}.html"
        html = render(spec)
        m = re.search(r'<article class="article-wrapper">([\s\S]*?)</article>', html)
        wc = word_count(m.group(1) if m else html)
        if wc < 1200:
            print(f"WARNING: {slug} only {wc} words", file=sys.stderr)
        out.write_text(html, encoding="utf-8")
        results.append((slug, wc))
        print(f"Created {slug}.html ({wc} words)")

    inserted = insert_cards(ARTICLES)
    if inserted:
        bump_index_count(inserted)

    print("\n=== Regenerating sitemap ===")
    subprocess.run(["node", str(ROOT / "scripts" / "regenerate-sitemap.mjs")], cwd=ROOT, check=True)

    print("\n--- Summary ---")
    for slug, wc in results:
        print(f"  {slug}: {wc} words")
    print(f"  index cards added: {inserted}")


if __name__ == "__main__":
    main()
