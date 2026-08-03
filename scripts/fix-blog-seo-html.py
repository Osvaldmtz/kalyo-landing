#!/usr/bin/env python3
"""Fix DataForSEO HTML issues in Kalyo blog articles."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICULOS = ROOT / "articulos"
FAVICON = '<link rel="icon" type="image/x-icon" href="/favicon.ico">'
META_PROPS = (
    "og:title",
    "og:description",
    "twitter:title",
    "twitter:description",
)


def meta_content(value: str) -> str:
    prev = None
    while prev != value:
        prev = value
        value = html.unescape(value)
    return value.replace('"', "&quot;")


def fix_lt_in_text_nodes(text: str) -> str:
    # Numeric comparisons like "CI < 70" are misparsed as HTML tags; fix globally.
    text = re.sub(r" < (\d)", " &lt; \\1", text)
    return text


def fix_article_intro(text: str) -> str:
    text = text.replace('<p class="article-intro">', '<div class="article-intro">')

    def close_intro(match: re.Match[str]) -> str:
        inner = match.group(1)
        return f'<div class="article-intro">{inner}</div>'

    text = re.sub(
        r'<div class="article-intro">\s*(<p>[\s\S]*?</p>)\s*</p>',
        close_intro,
        text,
        count=1,
    )
    text = re.sub(
        r'<div class="article-intro">\s*\n?\s*([^<][\s\S]*?)\s*</p>',
        close_intro,
        text,
        count=1,
    )
    text = re.sub(
        r'<div class="article-intro">([^<][\s\S]*?)</p>',
        close_intro,
        text,
        count=1,
    )
    return text


def fix_img_tags(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        if " title=" in tag:
            return tag
        alt_match = re.search(r'alt="([^"]*)"', tag)
        if not alt_match:
            return tag
        title = html.unescape(alt_match.group(1)).replace('"', "&quot;")
        return tag[:-1] + f' title="{title}"' + tag[-1]

    return re.sub(r"<img\b[^>]*>", repl, text)


def fix_meta_tags(text: str) -> str:
    for prop in META_PROPS:
        pattern = rf'(<meta (?:property|name)="{re.escape(prop)}" content=")([^"]*)(">)'

        def repl(match: re.Match[str], _prop=prop) -> str:
            return match.group(1) + meta_content(match.group(2)) + match.group(3)

        text = re.sub(pattern, repl, text)
    return text


def fix_favicon(text: str) -> str:
    if 'rel="icon"' in text:
        text = re.sub(
            r'<link rel="icon"[^>]*href="(?!/)[^"]*"[^>]*>',
            FAVICON,
            text,
        )
        return text
    return text.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n  ' + FAVICON,
        1,
    )


def fix_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    text = original
    text = fix_favicon(text)
    text = fix_meta_tags(text)
    text = fix_article_intro(text)
    text = fix_img_tags(text)
    text = fix_lt_in_text_nodes(text)
    text = text.replace("secund.ario", "secundario")
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed = 0
    for path in sorted(ARTICULOS.glob("*.html")):
        if fix_file(path):
            changed += 1
            print(f"fixed: {path.name}")
    print(f"Updated {changed} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
