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

FONTS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Outfit:wght@300;400;500;600&"
    "family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap"
)

BLOCK_TAG = (
    r"(?:table|ul|ol|div|h[1-6]|blockquote|pre|figure|section|article|nav|aside|"
    r"header|footer|form|fieldset|dl|hr|p)(?:\s|>)"
)


def _has_block_markup(inner: str) -> bool:
    return bool(re.search(rf"<{BLOCK_TAG}", inner, re.IGNORECASE))

BLOG_CSS_BLOCKING = '  <link rel="stylesheet" href="/assets/blog.css">'
FONTS_BLOCKING = f'  <link rel="stylesheet" href="{FONTS_URL}">'

PRELOAD_BLOG_PATTERN = re.compile(
    r'\s*<link rel="preload" href="/assets/blog\.css" as="style" '
    r'onload="this\.onload=null;this\.rel=\'stylesheet\'">\s*'
    r'<noscript><link rel="stylesheet" href="/assets/blog\.css"></noscript>'
)

PRELOAD_FONTS_PATTERN = re.compile(
    r'\s*<link rel="preload" href="' + re.escape(FONTS_URL) + r'" as="style" '
    r'onload="this\.onload=null;this\.rel=\'stylesheet\'">\s*'
    r'<noscript><link href="' + re.escape(FONTS_URL) + r'" rel="stylesheet"></noscript>'
)

DEFERRED_GA = """<!-- Google Analytics (deferred until load) -->
<script>
window.addEventListener('load', function () {
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  window.gtag = gtag;
  var script = document.createElement('script');
  script.async = true;
  script.src = 'https://www.googletagmanager.com/gtag/js?id=G-RTBRDTN5BK';
  document.head.appendChild(script);
  gtag('js', new Date());
  gtag('config', 'G-RTBRDTN5BK');
  gtag('config', 'AW-18345611562');
});
</script>"""

BLOCKING_GA_PATTERN = re.compile(
    r"<script async src=\"https://www\.googletagmanager\.com/gtag/js\?id=G-RTBRDTN5BK\"></script>\s*"
    r"<script>[\s\S]*?</script>",
    re.MULTILINE,
)


def meta_content(value: str) -> str:
    prev = None
    while prev != value:
        prev = value
        value = html.unescape(value)
    return value.replace('"', "&quot;")


def fix_lt_in_text_nodes(text: str) -> str:
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
        r'<div class="article-intro">\s*([^<][\s\S]*?)\s*</p>\s*(?=</div>)',
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


def _fix_p_block_region(text: str) -> str:
    text = re.sub(
        r'<div class="article-meta">([\s\S]*?)</p>',
        r'<div class="article-meta">\1</div>',
        text,
    )

    text = re.sub(
        r"<div(\s[^>]*)?>\s*<p(\s[^>]*)?>([\s\S]*?)</div>\s*</p>",
        lambda m: f"<div{m.group(1) or ''}>{m.group(3)}</div>",
        text,
    )

    text = re.sub(
        r"<p(\s[^>]*)?>([\s\S]*?)</div>",
        lambda m: (
            m.group(0)
            if _has_block_markup(m.group(2))
            else f"<p{m.group(1) or ''}>{m.group(2)}</p>"
        ),
        text,
    )

    block_in_p = re.compile(rf"<p(\s[^>]*)?>([\s\S]*?)</p>", re.MULTILINE)

    def repl(match: re.Match[str]) -> str:
        attrs = match.group(1) or ""
        inner = match.group(2)
        if _has_block_markup(inner):
            return f"<div{attrs}>{inner}</div>"
        return match.group(0)

    return block_in_p.sub(repl, text)


def fix_p_block_elements(text: str) -> str:
    """Convert invalid <p> wrappers to <div> or fix closing tags."""

    chunks: list[str] = []
    last = 0
    for match in re.finditer(r"<style[\s\S]*?</style>|<script[\s\S]*?</script>", text):
        chunks.append(_fix_p_block_region(text[last : match.start()]))
        chunks.append(match.group(0))
        last = match.end()
    chunks.append(_fix_p_block_region(text[last:]))
    return "".join(chunks)


def fix_render_blocking_assets(text: str) -> str:
    """Keep layout CSS blocking (prevents CLS); only defer third-party JS."""
    text = PRELOAD_BLOG_PATTERN.sub("\n" + BLOG_CSS_BLOCKING, text)
    text = PRELOAD_FONTS_PATTERN.sub("\n" + FONTS_BLOCKING, text)

    if "deferred until load" not in text:
        text = BLOCKING_GA_PATTERN.sub(DEFERRED_GA, text)

    return text


def fix_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    text = original
    text = fix_favicon(text)
    text = fix_meta_tags(text)
    text = fix_article_intro(text)
    text = fix_img_tags(text)
    text = fix_lt_in_text_nodes(text)
    text = fix_p_block_elements(text)
    text = fix_render_blocking_assets(text)
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
