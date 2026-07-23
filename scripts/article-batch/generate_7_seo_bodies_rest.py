# -*- coding: utf-8 -*-
"""Articles 2–7 for generate_7_seo_bodies.py"""

KALYO = '<a href="https://app.kalyo.io/register">Kalyo</a>'


def add_remaining_articles(ARTICLES, p, validate=None, wc=None):
    for cfg in CONFIGS:
        ARTICLES.append(build_article(p, cfg))


def build_article(p, c):
    sections = []
    for h2, blocks in c["blocks"]:
        parts = []
        for b in blocks:
            if b.lstrip().startswith("<"):
                parts.append(b)
            else:
                parts.append(f"<p>{b}</p>")
        sections.append({"h2": h2, "html": "\n".join(parts)})
    return {
        "slug": c["slug"],
        "title": c["title"],
        "description": c["description"],
        "h1": c["h1"],
        "breadcrumb_short": c["breadcrumb_short"],
        "intro": c["intro"],
        "sections": sections,
        "faqs": c["faqs"],
        "howto": c.get("howto"),
        "related": [{"href": h, "label": l} for h, l in c["related"]],
        "cta_h2": c["cta_h2"],
        "cta_p": c["cta_p"],
        "keywords": c["keywords"],
        "card_title": c["card_title"],
        "card_p": c["card_p"],
        "after_href": c["after_href"],
        "after_loc": f"https://kalyo.io{c['after_href']}",
    }


from batch7_specs import CONFIGS  # noqa: E402
