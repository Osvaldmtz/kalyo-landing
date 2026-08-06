#!/usr/bin/env python3
"""Render Kalyo blog articles using the ley-1616-2013 template structure."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_PATH = ROOT / "articulos" / "ley-1616-2013-salud-mental-colombia.html"

CTA_H2 = "Gestiona expedientes cl&iacute;nicos digitales"
CTA_P = "Kalyo te permite gestionar expedientes cl&iacute;nicos digitales."
CTA_BTN = "Prueba gratis &rarr;"
DATE = "2026-08-01"


def load_style_block() -> str:
    text = TEMPLATE_PATH.read_text(encoding="utf-8")
    m = re.search(r"<style>([\s\S]*?)<\/style>", text)
    if not m:
        raise RuntimeError("Could not extract <style> from ley-1616 template")
    return m.group(1)


STYLE_BLOCK = load_style_block()


def esc_attr(s: str) -> str:
    return html.escape(s, quote=True)


def meta_attr(s: str) -> str:
    prev = None
    while prev != s:
        prev = s
        s = html.unescape(s)
    return s.replace('"', "&quot;")


def img_title_attr(s: str) -> str:
    return html.unescape(s).replace('"', "&quot;")


def word_count(html_text: str) -> int:
    plain = re.sub(r"<script[\s\S]*?</script>", " ", html_text, flags=re.I)
    plain = re.sub(r"<[^>]+>", " ", plain)
    repl = {
        "&aacute;": "á", "&eacute;": "é", "&iacute;": "í", "&oacute;": "ó", "&uacute;": "ú",
        "&ntilde;": "ñ", "&uuml;": "ü", "&mdash;": "—", "&ndash;": "–", "&middot;": "·",
        "&iacute;": "í", "&oacute;": "ó", "&aacute;": "á", "&eacute;": "é", "&uacute;": "ú",
        "&ntilde;": "ñ", "&amp;": "&",
    }
    for a, b in repl.items():
        plain = plain.replace(a, b)
    return len(re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ]+\b", plain, flags=re.UNICODE))


def insert_inline_before_third_h2(body: str, slug: str, inline_alt: str) -> str:
    figure = f'''    <figure class="article-inline-img">
      <picture>
      <source srcset="/assets/blog/{slug}-inline.webp" type="image/webp">
      <img src="/assets/blog/{slug}-inline.jpg" alt="{esc_attr(inline_alt)}" title="{img_title_attr(inline_alt)}" width="800" height="450" loading="lazy">
    </picture>
    </figure>'''
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        if count == 3:
            return f"{figure}\n\n    <h2>"
        return match.group(0)

    return re.sub(r"<h2>", repl, body)


def build_faq_json_ld(faqs: list[dict]) -> str:
    entities = [
        {
            "@type": "Question",
            "name": f["q"],
            "acceptedAnswer": {"@type": "Answer", "text": f["a_plain"]},
        }
        for f in faqs
    ]
    return json.dumps(
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities},
        ensure_ascii=False,
        indent=2,
    )


def build_article_json_ld(spec: dict) -> str:
    slug = spec["slug"]
    url = f"https://kalyo.io/articulos/{slug}.html"
    obj = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": spec["title"],
        "description": spec["description_plain"],
        "image": f"https://kalyo.io/assets/blog/{slug}-hero.jpg",
        "author": {"@type": "Organization", "name": "Kalyo", "url": "https://kalyo.io"},
        "publisher": {
            "@type": "Organization",
            "name": "Kalyo",
            "logo": {"@type": "ImageObject", "url": "https://kalyo.io/assets/logo.png"},
        },
        "datePublished": DATE,
        "dateModified": DATE,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
    }
    return json.dumps(obj, ensure_ascii=False, indent=2)


def render_faq_html(faqs: list[dict]) -> str:
    parts = ["    <h2>Preguntas frecuentes</h2>"]
    for f in faqs:
        parts.append(f"    <h3>{f['q_html']}</h3>\n    <p>\n      {f['a_html']}\n    </p>")
    return "\n\n".join(parts)


def render_related(related: list[tuple[str, str]]) -> str:
    items = "\n      ".join(
        f'<li><a href="/articulos/{slug}.html" style="display:block;padding:14px 16px;background:#F8F7FF;border:1px solid #EDE7F6;border-radius:8px;text-decoration:none;color:#7C3DE3;font-size:14px;font-weight:500;line-height:1.4">{label}</a></li>'
        for slug, label in related
    )
    return f'''  <section style="margin-top:48px;padding-top:32px;border-top:1px solid #EDE7F6">
    <h2 style="font-size:18px;font-weight:700;color:#1A1A2E;margin-bottom:20px">Art&iacute;culos relacionados</h2>
    <ul style="list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px">
      {items}
    </ul>
  </section>'''


def render(spec: dict) -> str:
    slug = spec["slug"]
    url = f"https://kalyo.io/articulos/{slug}.html"
    title = spec["title"]
    desc = spec["description"]
    keywords = spec["keywords"]
    body = insert_inline_before_third_h2(spec["body_html"], slug, spec["inline_alt"])
    faq_html = render_faq_html(spec["faqs"])
    related_html = render_related(spec.get("related", []))
    cta_h2 = spec.get("cta_h2", CTA_H2)
    cta_p = spec.get("cta_p", CTA_P)
    cta_btn = spec.get("cta_btn", CTA_BTN)

    refs_html = ""
    if spec.get("references"):
        refs_html = "\n  <section class=\"article-references\">\n  <h2>Referencias</h2>\n  <ul>\n"
        for ref in spec["references"]:
            refs_html += f"    <li>{ref}</li>\n"
        refs_html += "  </ul>\n</section>\n"

    article_ld = build_article_json_ld(spec)
    faq_ld = build_faq_json_ld(spec["faqs"])

    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{keywords}">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="es" href="{url}">

  <link rel="preload" as="image" href="/assets/blog/{slug}-hero.webp" type="image/webp">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{meta_attr(title)}">
  <meta property="og:description" content="{meta_attr(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="https://kalyo.io/assets/blog/{slug}-hero.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="Kalyo">
  <meta property="og:locale" content="es_419">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{meta_attr(title)}">
  <meta name="twitter:description" content="{meta_attr(desc)}">
  <meta name="twitter:image" content="https://kalyo.io/assets/blog/{slug}-hero.jpg">

  <script type="application/ld+json">
{article_ld}
</script>
  <script type="application/ld+json">
{faq_ld}
</script>
<!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="/assets/blog.css">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap" rel="stylesheet">

  <style>
{STYLE_BLOCK}
  </style>
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RTBRDTN5BK"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-RTBRDTN5BK');
  gtag('config', 'AW-18371122366');
</script>
<script src="/scripts/attribution.js"></script>
</head>
<body>

  <header class="header">
    <div class="header-inner">
      <a href="/" class="header-logo">Kalyo</a>
      <a href="https://app.kalyo.io/login" class="header-btn">Iniciar sesi&oacute;n</a>
    </div>
  </header>

  <article class="article-wrapper">
    <div class="article-hero-img">
      <picture>
      <source srcset="/assets/blog/{slug}-hero.webp" type="image/webp">
      <img src="/assets/blog/{slug}-hero.jpg" alt="{esc_attr(spec['hero_alt'])}" title="{img_title_attr(spec['hero_alt'])}" width="1200" height="630" loading="eager" fetchpriority="high">
    </picture>
    </div>
    <p class="article-meta">{spec.get("meta_label", "Gu&iacute;a cl&iacute;nica &middot; Actualizaci&oacute;n 2026")}</p>

    <h1>{spec["h1"]}</h1>

    <div class="article-intro">
      {spec["intro"]}
    </div>

{body}

{faq_html}

    <div class="cta-box">
      <h2>{cta_h2}</h2>
      <p>{cta_p}</p>
      <a href="https://app.kalyo.io/login?utm_source=blog&utm_medium=article&utm_campaign={slug}" class="cta-btn">{cta_btn}</a>
    </div>
{related_html}
{refs_html}
  </article>

  <footer class="footer">
    <p>&copy; 2026 Endeavor Ventures LLC &middot; <a href="https://kalyo.io">kalyo.io</a></p>
  </footer>

</body>
</html>
'''
