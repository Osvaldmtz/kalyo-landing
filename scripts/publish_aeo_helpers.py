#!/usr/bin/env python3
"""Helpers to verify AEO articles and update index/sitemap."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def word_count(text: str) -> int:
    text = re.sub(r"<[^>]+>", " ", text)
    repl = {
        "&mdash;": "—",
        "&ndash;": "–",
        "&oacute;": "ó",
        "&aacute;": "á",
        "&eacute;": "é",
        "&iacute;": "í",
        "&uacute;": "ú",
        "&ntilde;": "ñ",
        "&uuml;": "ü",
        "&laquo;": "«",
        "&raquo;": "»",
        "&hellip;": "…",
        "&middot;": "·",
        "&ge;": "≥",
        "&le;": "≤",
        "&amp;": "&",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    return len(re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ]+\b", text, flags=re.UNICODE))


def verify(slug: str) -> dict:
    html = (ROOT / "articulos" / f"{slug}.html").read_text()
    title = re.search(r"<title>(.*?)</title>", html).group(1)
    desc = re.search(r'name="description" content="(.*?)"', html).group(1)
    m = re.search(r'id="respuesta-rapida".*?<p class="article-intro">(.*?)</p>', html, re.S)
    if not m:
        raise SystemExit("respuesta-rapida/article-intro missing")
    intro_words = word_count(m.group(1))
    body = re.search(r'<article class="article-wrapper">(.*?)</article>', html, re.S).group(1)
    body_words = word_count(body)
    for i, block in enumerate(re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', html, re.S), 1):
        json.loads(block)
    assert 55 <= len(title) <= 60, f"title {len(title)}"
    assert 150 <= len(desc) <= 160, f"desc {len(desc)}"
    assert 50 <= intro_words <= 60, f"intro {intro_words}"
    assert body_words >= 1200, f"body {body_words}"
    return {
        "slug": slug,
        "title_chars": len(title),
        "desc_chars": len(desc),
        "intro_words": intro_words,
        "body_words": body_words,
        "title": title,
    }


def bump_counts(delta: int = 1) -> None:
    index = ROOT / "articulos" / "index.html"
    text = index.read_text()
    m = re.search(r'"numberOfItems":\s*(\d+)', text)
    n = int(m.group(1)) + delta
    text = text.replace(m.group(0), f'"numberOfItems": {n}', 1)
    m2 = re.search(r"Escalas Cl&iacute;nicas <span[^>]*>\((\d+)\)</span>", text)
    if m2:
        c = int(m2.group(1)) + delta
        text = text.replace(m2.group(0), m2.group(0).replace(f"({m2.group(1)})", f"({c})"), 1)
    index.write_text(text)


def insert_card(after_href: str, card_html: str) -> None:
    index = ROOT / "articulos" / "index.html"
    text = index.read_text()
    marker = f'href="{after_href}"'
    pos = text.find(marker)
    if pos < 0:
        raise SystemExit(f"anchor card not found: {after_href}")
    end = text.find("</a>", pos)
    end = text.find("\n", end) + 1
    if card_html.strip() in text:
        print("card already present")
        return
    text = text[:end] + card_html + text[end:]
    index.write_text(text)


def insert_sitemap(after_loc: str, new_loc: str, lastmod: str = "2026-07-23") -> None:
    sm = ROOT / "sitemap.xml"
    text = sm.read_text()
    if new_loc in text:
        print("sitemap already present")
        return
    block = (
        f"  <url>\n"
        f"    <loc>{new_loc}</loc>\n"
        f"    <lastmod>{lastmod}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n"
        f"    <priority>0.8</priority>\n"
        f"  </url>\n"
    )
    needle = f"<loc>{after_loc}</loc>"
    pos = text.find(needle)
    if pos < 0:
        raise SystemExit(f"sitemap anchor not found: {after_loc}")
    end = text.find("</url>", pos) + len("</url>\n")
    text = text[:end] + block + text[end:]
    sm.write_text(text)


if __name__ == "__main__":
    print(json.dumps(verify(sys.argv[1]), ensure_ascii=False, indent=2))
