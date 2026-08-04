#!/usr/bin/env python3
"""Render a Kalyo AEO article HTML from a JSON spec (PHQ-9 template)."""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_STYLE_PATH = ROOT / "articulos" / "que-es-el-phq-9.html"


def load_inline_style() -> str:
    text = TEMPLATE_STYLE_PATH.read_text(encoding="utf-8")
    m = re.search(r"<style>([\s\S]*?)</style>", text)
    if not m:
        raise RuntimeError("Could not extract <style> from PHQ-9 template")
    return m.group(1)


STYLE = f'''<!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="/assets/blog.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap">

  <style>
{load_inline_style()}
  </style>
<!-- Google Analytics (deferred until load) -->
<script>
window.addEventListener('load', function () {{
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  window.gtag = gtag;
  var script = document.createElement('script');
  script.async = true;
  script.src = 'https://www.googletagmanager.com/gtag/js?id=G-RTBRDTN5BK';
  document.head.appendChild(script);
  gtag('js', new Date());
  gtag('config', 'G-RTBRDTN5BK');
  gtag('config', 'AW-18345611562');
  gtag('config', 'AW-18371122366');
}});
</script>
<script src="/scripts/attribution.js"></script>'''


def j(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2)


def meta_attr(s: str) -> str:
    prev = None
    while prev != s:
        prev = s
        s = html.unescape(s)
    return s.replace('"', "&quot;")


def img_title_attr(s: str) -> str:
    return html.unescape(s).replace('"', "&quot;")


def render(spec: dict) -> str:
    slug = spec["slug"]
    url = f"https://kalyo.io/articulos/{slug}.html"
    title = spec["title"]
    desc = spec["description"]
    quick = spec.get("quick_answer") or spec.get("intro", "")
    intro = spec.get("intro_long") or spec.get("intro", "")
    test_name = spec.get("test_name", spec["h1"].split(":")[0].strip())
    faqs = [
        {
            "@type": "Question",
            "name": f["q"],
            "acceptedAnswer": {"@type": "Answer", "text": f["a"]},
        }
        for f in spec["faqs"]
    ]
    schemas = [
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title.replace(" | Kalyo", ""),
            "description": desc,
            "image": f"https://kalyo.io/assets/blog/{slug}-hero.jpg",
            "author": {
                "@type": "Organization",
                "name": "Equipo Kalyo",
                "url": "https://kalyo.io/sobre-kalyo.html",
            },
            "publisher": {
                "@type": "Organization",
                "name": "Kalyo",
                "url": "https://kalyo.io",
                "logo": {"@type": "ImageObject", "url": "https://kalyo.io/assets/logo.png"},
            },
            "datePublished": spec.get("date_published", "2026-01-01"),
            "dateModified": spec.get("date_modified", "2026-08-01"),
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://kalyo.io/"},
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": "Recursos para psicólogos",
                    "item": "https://kalyo.io/articulos/",
                },
                {"@type": "ListItem", "position": 3, "name": spec["breadcrumb_short"], "item": url},
            ],
        },
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faqs},
    ]

    schema_html = "\n".join(f'  <script type="application/ld+json">\n{j(s)}\n</script>' for s in schemas)

    quick_action = ""
    if spec.get("quick_action"):
        qa = spec["quick_action"]
        quick_action = (
            f'    <p class="article-quick-actions">\n'
            f'      <a href="{qa["href"]}"'
            f'{(" download=\"" + qa["download"] + "\"") if qa.get("download") else ""}'
            f' class="btn-solid">{qa["label"]}</a>\n'
            f"    </p>\n"
        )

    sections_html = []
    for i, sec in enumerate(spec["sections"]):
        sections_html.append(f"    <h2>{sec['h2']}</h2>\n    {sec['html']}")
        if i == 1:
            sections_html.append(
                f'''    <figure class="article-inline-img">
      <picture>
        <source srcset="/assets/blog/{slug}-inline.webp" type="image/webp">
        <img src="/assets/blog/{slug}-inline.jpg" alt="{html.escape(spec.get('inline_alt', spec['h1']))}" title="{img_title_attr(spec.get('inline_alt', spec['h1']))}" width="800" height="450" loading="lazy">
      </picture>
    </figure>'''
            )

    refs = spec.get("references", [])
    if refs:
        refs_html = "    <p><strong>Referencias:</strong></p>\n    <ol>\n"
        for ref in refs:
            refs_html += f"      <li>{ref}</li>\n"
        refs_html += "    </ol>"
        sections_html.append(refs_html)

    faq_html = ["    <h2>Preguntas frecuentes</h2>"]
    for f in spec["faqs"]:
        faq_html.append(f"    <h3>{f['q']}</h3>\n    <p>{f['a']}</p>")

    related = []
    for r in spec.get("related", []):
        related.append(
            f'<li><a href="{r["href"]}" style="display:block;padding:14px 16px;background:#F8F7FF;border:1px solid #EDE7F6;border-radius:8px;text-decoration:none;color:#7C3DE3;font-size:14px;font-weight:500;line-height:1.4">{r["label"]}</a></li>'
        )

    cta_h2 = spec.get("cta_h2") or f"Aplica {test_name} en el expediente de tu paciente con Kalyo"
    cta_p = spec.get("cta_p") or f"Administra, califica e interpreta {test_name} de forma digital. kalyo.io"

    meta_label = spec.get("meta_label", "Psicometr&iacute;a cl&iacute;nica &middot; Actualizaci&oacute;n 2026")

    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{spec['keywords']}">
  <link rel="canonical" href="{url}">

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
  <meta property="og:locale" content="es_MX">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{meta_attr(title)}">
  <meta name="twitter:description" content="{meta_attr(desc)}">
  <meta name="twitter:image" content="https://kalyo.io/assets/blog/{slug}-hero.jpg">

{schema_html}
{STYLE}
</head>
<body>

  <header class="header">
    <div class="header-inner">
      <a href="/" class="header-logo">Kalyo</a>
      <div class="header-nav">
        <a href="/articulos/" class="header-link">Recursos</a>
        <a href="https://app.kalyo.io/login" class="header-btn">Iniciar sesi&oacute;n</a>
      </div>
    </div>
  </header>

  <article class="article-wrapper">
    <nav class="article-breadcrumb" aria-label="Breadcrumb">
      <a href="/">Inicio</a> &rsaquo; <a href="/articulos/">Recursos</a> &rsaquo; {spec['breadcrumb_short']}
    </nav>
    <div class="article-hero-img">
      <picture>
        <source srcset="/assets/blog/{slug}-hero.webp" type="image/webp">
        <img src="/assets/blog/{slug}-hero.jpg" alt="{html.escape(spec.get('hero_alt', spec['h1']))}" title="{img_title_attr(spec.get('hero_alt', spec['h1']))}" width="1200" height="630" loading="eager" fetchpriority="high">
      </picture>
    </div>
    <p class="article-meta">{meta_label}</p>

    <h1>{spec['h1']}</h1>

{quick_action}
    <p class="article-date">Publicado el 1 de agosto de 2026 &middot; Lectura: 11 min</p>

    <h2 id="respuesta-rapida">Respuesta r&aacute;pida</h2>
    <p>{quick}</p>

    <div class="article-intro">
      {intro}
    </div>

{chr(10).join(sections_html)}

{chr(10).join(faq_html)}

    <div class="cta-box">
      <h2>{cta_h2}</h2>
      <p>{cta_p}</p>
      <a href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign={slug}" class="cta-btn">Comenzar gratis &rarr;</a>
    </div>
    <section style="margin-top:48px;padding-top:32px;border-top:1px solid #EDE7F6">
      <h2 style="font-size:18px;font-weight:700;color:#1A1A2E;margin-bottom:20px">Art&iacute;culos relacionados</h2>
      <ul style="list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px">
        {''.join(related)}
      </ul>
    </section>
  </article>

  <footer class="footer">
    <p>&copy; 2026 Endeavor Ventures LLC &middot; <a href="https://kalyo.io">kalyo.io</a> &middot; <a href="/sobre-kalyo.html">Sobre Kalyo</a> &middot; <a href="/contacto.html">Contacto</a></p>
  </footer>

</body>
</html>
'''


def main() -> None:
    spec_path = Path(sys.argv[1])
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    out = ROOT / "articulos" / f"{spec['slug']}.html"
    out.write_text(render(spec), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
