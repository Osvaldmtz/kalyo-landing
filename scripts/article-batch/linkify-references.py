#!/usr/bin/env python3
"""Wrap reference URLs in <a target="_blank" rel="noopener noreferrer"> in enriched articles."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTICULOS = ROOT / "articulos"

REF_BLOCK = re.compile(
    r"(<p><strong>Referencias:</strong></p>\s*<ol>)([\s\S]*?)(</ol>)",
    re.IGNORECASE,
)
URL_RE = re.compile(r"https://[^\s<\"']+")
ANCHOR_OPEN = re.compile(r'<a\s+href="([^"]+)"([^>]*)>', re.IGNORECASE)


def add_target_to_anchors(html: str) -> str:
    def repl(m: re.Match) -> str:
        href, rest = m.group(1), m.group(2)
        if 'target="_blank"' in rest:
            return m.group(0)
        return f'<a href="{href}" target="_blank" rel="noopener noreferrer"{rest}>'

    return ANCHOR_OPEN.sub(repl, html)


def wrap_bare_urls(text: str) -> str:
    parts = re.split(r"(<a [^>]*>|</a>)", text, flags=re.IGNORECASE)
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
            out.append(
                URL_RE.sub(
                    lambda m: (
                        f'<a href="{m.group(0)}" target="_blank" rel="noopener noreferrer">'
                        f"{m.group(0)}</a>"
                    ),
                    part,
                )
            )
    return "".join(out)


def process_reference_block(content: str) -> str:
    content = add_target_to_anchors(content)
    return wrap_bare_urls(content)


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


def main() -> None:
    updated = 0
    for path in sorted(ARTICULOS.glob("*.html")):
        if path.name == "index.html":
            continue
        if process_file(path):
            updated += 1
            print(f"  updated: {path.name}")
    print(f"Done: {updated} files updated")


if __name__ == "__main__":
    main()
