#!/usr/bin/env python3
"""Render a Kalyo AEO article HTML from a JSON spec file."""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STYLE = r'''<!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="/assets/blog.css">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap" rel="stylesheet">
  <style>
    :root { --purple:#7C3DE3; --purple-light:#9B6EF0; --purple-dark:#5B21B6; --purple-soft:#EDE9FE; --cream:#FAF8F5; --ink:#1A1612; --ink-mid:#3D3530; --ink-light:#7A736D; }
    *,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
    body{font-family:'Outfit',sans-serif;background-color:var(--cream);color:var(--ink);line-height:1.7;font-size:17px;-webkit-font-smoothing:antialiased}
    .header{position:fixed;top:0;left:0;right:0;z-index:100;background:rgba(255,255,255,.85);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid rgba(124,61,227,.08)}
    .header-inner{max-width:1120px;margin:0 auto;padding:0 24px;height:64px;display:flex;align-items:center;justify-content:space-between}
    .header-logo{font-family:'Playfair Display',serif;font-size:24px;font-weight:700;color:var(--purple);text-decoration:none}
    .header-btn{font-family:'Outfit',sans-serif;font-size:14px;font-weight:500;color:var(--purple);border:1.5px solid var(--purple);background:transparent;padding:8px 20px;border-radius:8px;text-decoration:none;transition:background .2s,color .2s}
    .header-btn:hover{background:var(--purple);color:#fff}
    .header-nav{display:flex;align-items:center;gap:12px}
    .header-link{font-size:14px;font-weight:500;color:var(--ink-mid);text-decoration:none;padding:8px 12px;border-radius:8px;transition:color .2s,background .2s}
    .header-link:hover{color:var(--purple);background:var(--purple-soft)}
    .article-breadcrumb{font-size:14px;color:var(--ink-light);margin-bottom:20px}
    .article-breadcrumb a{color:var(--purple);text-decoration:none}
    .article-breadcrumb a:hover{text-decoration:underline}
    .article-wrapper{max-width:720px;margin:0 auto;padding:120px 24px 80px}
    .article-meta,.article-date{font-size:14px;color:var(--ink-light);margin-bottom:16px;font-weight:400}
    .article-date{margin-bottom:24px}
    .article-wrapper h1{font-family:'Playfair Display',serif;font-size:40px;font-weight:700;line-height:1.2;color:var(--ink);margin-bottom:24px}
    .article-intro{font-size:19px;color:var(--ink-mid);line-height:1.75;margin-bottom:48px;font-weight:300}
    .article-wrapper h2{font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:var(--ink);margin-top:48px;margin-bottom:16px;line-height:1.3}
    .article-wrapper h3{font-family:'Outfit',sans-serif;font-size:20px;font-weight:600;color:var(--ink);margin-top:32px;margin-bottom:12px}
    .article-wrapper p{margin-bottom:20px;color:var(--ink-mid)}
    .article-wrapper ul,.article-wrapper ol{margin-bottom:20px;padding-left:24px;color:var(--ink-mid)}
    .article-wrapper li{margin-bottom:8px}
    .article-wrapper strong{color:var(--ink);font-weight:600}
    .article-wrapper a{color:var(--purple);text-decoration:none}
    .article-wrapper a:hover{text-decoration:underline}
    .items-table,.scoring-table{width:100%;border-collapse:collapse;margin:24px 0 32px;font-size:15px}
    .items-table th,.scoring-table th{background:var(--purple-soft);color:var(--purple-dark);font-weight:600;text-align:left;padding:12px 16px}
    .items-table td,.scoring-table td{padding:10px 16px;border-bottom:1px solid rgba(0,0,0,.06);color:var(--ink-mid);vertical-align:top}
    .items-table tr:last-child td,.scoring-table tr:last-child td{border-bottom:none}
    .cta-box{margin-top:56px;padding:48px 40px;border-radius:16px;background:linear-gradient(135deg,var(--purple) 0%,var(--purple-dark) 100%);text-align:center}
    .cta-box h2{font-family:'Playfair Display',serif;color:#fff!important;font-size:28px;margin-top:0;margin-bottom:12px}
    .cta-box p{color:rgba(255,255,255,.85)!important;font-size:16px;margin-bottom:28px;max-width:480px;margin-left:auto;margin-right:auto}
    .cta-btn{display:inline-block;font-family:'Outfit',sans-serif;font-size:16px;font-weight:600;color:var(--purple);background:#fff;padding:14px 32px;border-radius:10px;text-decoration:none;transition:transform .2s,box-shadow .2s}
    .cta-btn:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.18)}
    .footer{border-top:1px solid rgba(0,0,0,.06);padding:32px 24px;text-align:center;font-size:14px;color:var(--ink-light)}
    .footer a{color:var(--purple);text-decoration:none}
    .footer a:hover{text-decoration:underline}
    @media (max-width:640px){.article-wrapper h1{font-size:30px}.article-wrapper h2{font-size:24px}.article-intro{font-size:17px}.cta-box{padding:36px 24px}.items-table,.scoring-table{font-size:14px}.items-table th,.items-table td,.scoring-table th,.scoring-table td{padding:8px 10px}}
  </style>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RTBRDTN5BK"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-RTBRDTN5BK');</script>
'''


def j(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2)


def render(spec: dict) -> str:
    slug = spec["slug"]
    url = f"https://kalyo.io/articulos/{slug}.html"
    title = spec["title"]
    desc = spec["description"]
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
            "headline": spec["h1"],
            "description": desc,
            "image": f"https://kalyo.io/assets/blog/{slug}-hero.jpg",
            "author": {"@type": "Organization", "name": "Equipo Kalyo", "url": "https://kalyo.io/sobre-kalyo.html"},
            "publisher": {
                "@type": "Organization",
                "name": "Kalyo",
                "url": "https://kalyo.io",
                "logo": {"@type": "ImageObject", "url": "https://kalyo.io/assets/logo.png"},
            },
            "datePublished": "2026-07-23",
            "dateModified": "2026-07-23",
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://kalyo.io/"},
                {"@type": "ListItem", "position": 2, "name": "Recursos para psicólogos", "item": "https://kalyo.io/articulos/"},
                {"@type": "ListItem", "position": 3, "name": spec["breadcrumb_short"], "item": url},
            ],
        },
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faqs},
    ]
    if spec.get("howto"):
        schemas.append(
            {
                "@context": "https://schema.org",
                "@type": "HowTo",
                "name": spec["howto"]["name"],
                "step": [
                    {"@type": "HowToStep", "name": s["name"], "text": s["text"]}
                    for s in spec["howto"]["steps"]
                ],
            }
        )

    schema_html = "\n".join(f'  <script type="application/ld+json">\n{j(s)}\n</script>' for s in schemas)

    sections_html = []
    for i, sec in enumerate(spec["sections"]):
        sections_html.append(f"    <h2>{sec['h2']}</h2>\n    {sec['html']}")
        if i == 1:
            sections_html.append(
                f'''    <figure class="article-inline-img">
      <picture>
        <source srcset="/assets/blog/{slug}-inline.webp" type="image/webp">
        <img src="/assets/blog/{slug}-inline.jpg" alt="{html.escape(spec.get('inline_alt', spec['h1']))}" width="800" height="450" loading="lazy">
      </picture>
    </figure>'''
            )

    faq_html = ["    <h2>Preguntas frecuentes</h2>"]
    for f in spec["faqs"]:
        faq_html.append(f"    <h3>{f['q']}</h3>\n    <p>{f['a']}</p>")

    related = []
    for r in spec.get("related", []):
        related.append(
            f'<li><a href="{r["href"]}" style="display:block;padding:14px 16px;background:#F8F7FF;border:1px solid #EDE7F6;border-radius:8px;text-decoration:none;color:#7C3DE3;font-size:14px;font-weight:500;line-height:1.4">{r["label"]}</a></li>'
        )

    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{spec['keywords']}">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="es" href="{url}">
  <link rel="alternate" hreflang="es-MX" href="{url}">
  <link rel="alternate" hreflang="x-default" href="{url}">
  <link rel="preload" as="image" href="/assets/blog/{slug}-hero.webp" type="image/webp">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="https://kalyo.io/assets/blog/{slug}-hero.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="Kalyo">
  <meta property="og:locale" content="es_MX">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
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
        <a href="https://app.kalyo.io" class="header-btn">Iniciar sesión</a>
      </div>
    </div>
  </header>
  <article class="article-wrapper">
    <nav class="article-breadcrumb" aria-label="Breadcrumb">
      <a href="/">Inicio</a> › <a href="/articulos/">Recursos</a> › {spec['breadcrumb_short']}
    </nav>
    <div class="article-hero-img">
      <picture>
        <source srcset="/assets/blog/{slug}-hero.webp" type="image/webp">
        <img src="/assets/blog/{slug}-hero.jpg" alt="{html.escape(spec.get('hero_alt', spec['h1']))}" width="1200" height="630" loading="eager" fetchpriority="high">
      </picture>
    </div>
    <p class="article-meta">Psicología clínica · Actualización 2026</p>
    <h1>{spec['h1']}</h1>
    <p class="article-date">Publicado el 23 de julio de 2026 · Lectura: 11 min</p>
    <h2 id="respuesta-rapida">Respuesta rápida</h2>
    <p class="article-intro">{spec['intro']}</p>
{chr(10).join(sections_html)}
{chr(10).join(faq_html)}
    <div class="cta-box">
      <h2>{spec['cta_h2']}</h2>
      <p>{spec['cta_p']}</p>
      <a href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign={slug}" class="cta-btn">Comenzar gratis →</a>
    </div>
    <section style="margin-top:48px;padding-top:32px;border-top:1px solid #EDE7F6">
      <h2 style="font-size:18px;font-weight:700;color:#1A1A2E;margin-bottom:20px">Artículos relacionados</h2>
      <ul style="list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px">
        {''.join(related)}
      </ul>
    </section>
  </article>
  <footer class="footer">
    <p>© 2026 Endeavor Ventures LLC · <a href="https://kalyo.io">kalyo.io</a> · <a href="/sobre-kalyo.html">Sobre Kalyo</a> · <a href="/contacto.html">Contacto</a></p>
  </footer>
</body>
</html>
'''


def main() -> None:
    spec_path = Path(sys.argv[1])
    spec = json.loads(spec_path.read_text())
    out = ROOT / "articulos" / f"{spec['slug']}.html"
    out.write_text(render(spec))
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
