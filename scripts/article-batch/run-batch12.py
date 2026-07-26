#!/usr/bin/env python3
"""Generate BATCH 12 therapy + DSM pillar articles."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parents[2]
BATCH_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BATCH_DIR / "output"
ART = ROOT / "articulos"
TOPICS = BATCH_DIR / "topics-batch-12.json"
MODEL = os.environ.get("ARTICLE_MODEL", "claude-haiku-4-5-20251001")

SOFTAPP = {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Kalyo",
    "applicationCategory": "HealthApplication",
    "operatingSystem": "Web",
    "url": "https://kalyo.io",
    "offers": {"@type": "Offer", "price": "29.00", "priceCurrency": "USD"},
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "reviewCount": "47",
    },
}

HERO_FALLBACK = {
    "terapia-de-pareja": "enrich-inventario-relacion-pareja",
    "terapia-emdr": "escala-pcl-5-estres-postraumatico",
    "terapia-dialectico-conductual": "tlp-trastorno-limite",
    "terapia-racional-emotiva": "distorsiones-cognitivas",
    "terapia-sistemica": "terapia-familiar-sistemica",
    "tipos-de-terapias-psicologicas": "psicologia-humanista",
    "terapia-humanista": "psicologia-humanista",
    "terapia-grupal": "habilidades-sociales",
    "terapia-infantil": "cdi-2-inventario-depresion-infantil",
    "terapia-narrativa": "terapia-familiar-sistemica",
    "que-es-el-dsm-5": "scid-5-entrevista-clinica",
    "trastorno-negativista-desafiante": "cbcl-cuestionario-capacidades-comportamiento",
    "trastorno-depresivo-mayor": "que-es-el-phq-9",
    "trastorno-depresivo-persistente": "inventario-depresion-beck-bdi",
    "que-es-la-psicologia-clinica": "software-para-psicologos-clinicos",
}

THERAPY_SLUGS = [
    "terapia-de-pareja",
    "terapia-emdr",
    "terapia-dialectico-conductual",
    "terapia-racional-emotiva",
    "terapia-sistemica",
    "terapia-humanista",
    "terapia-grupal",
    "terapia-infantil",
    "terapia-narrativa",
    "terapia-gestalt",
    "terapia-familiar-sistemica",
    "psicologia-humanista",
    "desensibilizacion-sistematica",
]


def load_env() -> None:
    env_path = ROOT / ".env.local"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


def generate_content(client: anthropic.Anthropic, topic: dict) -> dict:
    title_hint = topic["title_hint"]
    h1_hint = topic.get("h1_hint", "")
    required = topic.get("required_sections", [])
    extra = ""
    if topic.get("umbrella_therapy_links"):
        extra += (
            "\nArtículo PARAGUAS: incluye una sección H2 con lista de enlaces internos "
            "a enfoques terapéuticos (/articulos/terapia-*.html y afines).\n"
        )
    if topic.get("umbrella_disorder_links"):
        extra += (
            "\nArtículo PARAGUAS DSM: enlaza a trastornos específicos "
            "(esquizofrenia, depresión, TEA, TLP, ansiedad, etc.).\n"
        )
    if topic.get("pillar_links"):
        extra += (
            "\nArtículo PILAR: enlaza a evaluación (PHQ-9, GAD-7), terapias y trastornos.\n"
        )

    prompt = f"""Eres redactor clínico SEO para kalyo.io (psicólogos LATAM).
Escribe un artículo clínico de guía:
{json.dumps({k: v for k, v in topic.items() if k != 'link_from'}, ensure_ascii=False)}
{extra}

Título exacto: {title_hint}
H1 exacto (con entidades HTML para acentos): convierte "{h1_hint}" a HTML entities
Keyword principal: "{topic['primary_keyword']}"
Secciones obligatorias H2: {required}

Devuelve SOLO JSON:
{{
  "slug": "{topic['slug']}",
  "title": "{title_hint}",
  "description": "meta max 155 chars",
  "keywords": "{topic['keywords']}",
  "h1": "...",
  "intro": "intro con keyword, entidades HTML",
  "heroAlt": "alt",
  "inlineAlt": "alt",
  "ctaTitle": "CTA Kalyo",
  "sections": [{{"title": "H2", "paragraphs": ["p1", "p2", "p3"]}}],
  "faq": [{{"q": "...", "a": "..."}}],
  "related_slugs": {json.dumps(topic.get("related_slugs", [])[:5])}
}}

Requisitos:
- 9+ secciones H2, 1800-2200 palabras
- Incluir "Herramientas de evaluación" y "Abordaje terapéutico"
- Criterios DSM-5 cuando aplique
- Enlaces internos /articulos/....html en el cuerpo
- H1 distinto del title
- 4 FAQs
- HTML entities para acentos
SOLO JSON válido."""

    last_err: Exception | None = None
    for attempt in range(3):
        msg = client.messages.create(
            model=MODEL,
            max_tokens=16384,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = msg.content[0].text.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        try:
            data = json.loads(raw)
            data["title"] = title_hint
            data["slug"] = topic["slug"]
            out = OUTPUT_DIR / f"{topic['slug']}.json"
            out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            print(
                f"  OK {topic['slug']} in={msg.usage.input_tokens} out={msg.usage.output_tokens}"
            )
            return data
        except json.JSONDecodeError as exc:
            last_err = exc
            print(f"  JSON fail {topic['slug']} #{attempt+1}: {exc}")
            time.sleep(2)
    raise last_err or RuntimeError(topic["slug"])


def inject_softapp(html: str) -> str:
    if "SoftwareApplication" in html:
        return html
    block = (
        '<script type="application/ld+json">\n'
        + json.dumps(SOFTAPP, ensure_ascii=False, indent=2)
        + "\n</script>\n"
    )
    return html.replace("</head>", block + "</head>", 1)


def fix_cta_login(html: str) -> str:
    html = re.sub(r'href="https://app\.kalyo\.io"(?!/)', 'href="https://app.kalyo.io/login"', html)
    html = re.sub(r'href="https://app\.kalyo\.io\?', 'href="https://app.kalyo.io/login?', html)
    html = re.sub(
        r'https://app\.kalyo\.io/register',
        "https://app.kalyo.io/login",
        html,
    )
    return html


def fix_hero(html: str, slug: str) -> str:
    fb = HERO_FALLBACK.get(slug)
    if not fb:
        return html
    if (ROOT / "assets" / "blog" / f"{fb}-hero.jpg").exists():
        html = html.replace(f"/assets/blog/{slug}-hero", f"/assets/blog/{fb}-hero")
        html = html.replace(f"/assets/blog/{slug}-inline", f"/assets/blog/{fb}-inline")
        html = html.replace(
            f"https://kalyo.io/assets/blog/{slug}-hero",
            f"https://kalyo.io/assets/blog/{fb}-hero",
        )
    else:
        html = re.sub(
            r'<div class="article-hero-img">\s*<picture>[\s\S]*?</picture>\s*</div>',
            f'<div class="article-hero-img article-hero-placeholder" role="img" aria-label="{slug}">'
            f'<span class="article-hero-placeholder-label">{slug.replace("-", " ").title()}</span></div>',
            html,
            count=1,
        )
        html = re.sub(
            r'<link rel="preload" as="image" href="/assets/blog/[^"]+" type="image/webp">\s*',
            "",
            html,
            count=1,
        )
        html = html.replace(
            f"https://kalyo.io/assets/blog/{slug}-hero.jpg",
            "https://kalyo.io/og-image.jpg",
        )
    return html


def update_title(html: str, title: str) -> str:
    html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, count=1, flags=re.S)
    esc = title.replace('"', "&quot;")
    html = re.sub(r'(property="og:title" content=")[^"]*"', rf'\1{esc}"', html, count=1)
    html = re.sub(r'(name="twitter:title" content=")[^"]*"', rf'\1{esc}"', html, count=1)
    return html


def force_h1(html: str, h1_plain: str) -> str:
    # convert accents to entities lightly
    entities = {
        "á": "&aacute;",
        "é": "&eacute;",
        "í": "&iacute;",
        "ó": "&oacute;",
        "ú": "&uacute;",
        "ñ": "&ntilde;",
        "Á": "&Aacute;",
        "É": "&Eacute;",
        "Í": "&Iacute;",
        "Ó": "&Oacute;",
        "Ú": "&Uacute;",
        "Ñ": "&Ntilde;",
        "¿": "&iquest;",
    }
    h1 = h1_plain
    for a, b in entities.items():
        h1 = h1.replace(a, b)
    return re.sub(r"<h1>.*?</h1>", f"<h1>{h1}</h1>", html, count=1, flags=re.S)


def word_count(path: Path) -> int:
    t = path.read_text(encoding="utf-8")
    t = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    m = re.search(r"<article[\s\S]*?</article>", t, re.I)
    plain = re.sub(r"<[^>]+>", " ", m.group(0) if m else t)
    return len(re.findall(r"\w+", plain))


def enrich_umbrella(html: str, topic: dict) -> str:
    if topic.get("umbrella_therapy_links"):
        items = []
        for s in THERAPY_SLUGS:
            if (ART / f"{s}.html").exists():
                items.append(
                    f'<li><a href="/articulos/{s}.html">{s.replace("-", " ").title()}</a></li>'
                )
        if items and "Mapa de enfoques" not in html:
            block = (
                "\n    <h2>Mapa de enfoques terap&eacute;uticos en Kalyo</h2>\n"
                "    <p>Explora gu&iacute;as cl&iacute;nicas por enfoque:</p>\n"
                f"    <ul>\n      {chr(10).join(items)}\n    </ul>\n"
            )
            html = html.replace('<div class="cta-box">', block + '<div class="cta-box">', 1)
    if topic.get("umbrella_disorder_links"):
        disorders = [
            ("esquizofrenia", "Esquizofrenia"),
            ("depresion-sintomas", "Síntomas de depresión"),
            ("trastorno-depresivo-mayor", "Trastorno depresivo mayor"),
            ("autismo-espectro-autista", "TEA"),
            ("trastorno-limite-personalidad", "TLP"),
            ("agorafobia", "Agorafobia"),
            ("tdah-adultos", "TDAH en adultos"),
            ("adiccion-psicologia", "Adicción"),
        ]
        items = []
        for s, label in disorders:
            if (ART / f"{s}.html").exists():
                items.append(f'<li><a href="/articulos/{s}.html">{label}</a></li>')
        if items:
            block = (
                "\n    <h2>Trastornos y cuadros relacionados</h2>\n"
                "    <ul>\n      "
                + "\n      ".join(items)
                + "\n    </ul>\n"
            )
            html = html.replace('<div class="cta-box">', block + '<div class="cta-box">', 1)
    if topic.get("pillar_links"):
        pillars = [
            ("tipos-de-terapias-psicologicas", "Tipos de terapias"),
            ("que-es-el-dsm-5", "DSM-5"),
            ("que-es-el-phq-9", "PHQ-9"),
            ("que-es-el-gad-7", "GAD-7"),
            ("como-interpretar-tests-psicologicos", "Interpretar tests"),
            ("software-para-psicologos-clinicos", "Software clínico"),
        ]
        items = [
            f'<li><a href="/articulos/{s}.html">{lab}</a></li>'
            for s, lab in pillars
            if (ART / f"{s}.html").exists()
        ]
        if items:
            block = (
                "\n    <h2>Rutas de aprendizaje en Kalyo</h2>\n"
                "    <ul>\n      "
                + "\n      ".join(items)
                + "\n    </ul>\n"
            )
            html = html.replace('<div class="cta-box">', block + '<div class="cta-box">', 1)
    return html


def add_cross_links(topics: list[dict]) -> None:
    for topic in topics:
        orphan = f"{topic['slug']}.html"
        label = topic.get("h1_hint") or topic["primary_keyword"]
        sentence = (
            f' Para profundizar, consulta <a href="/articulos/{orphan}">{label}</a>.'
        )
        for donor in topic.get("link_from", []):
            path = ART / donor
            if not path.exists():
                print(f"  skip link_from missing {donor}")
                continue
            t = path.read_text(encoding="utf-8")
            if orphan in t:
                print(f"  has {donor} -> {orphan}")
                continue
            inserted = False
            for m in re.finditer(r"</p>", t):
                start = t.rfind("<p", 0, m.start())
                if start < 0:
                    continue
                para = t[start : m.end()]
                if len(re.sub(r"<[^>]+>", "", para)) < 90:
                    continue
                t = t[: m.start()] + " " + sentence + t[m.start() :]
                inserted = True
                break
            if not inserted:
                m = re.search(r"<h2[^>]*>\s*Art", t)
                if m:
                    t = t[: m.start()] + f"<p>{sentence.strip()}</p>\n\n    " + t[m.start() :]
                    inserted = True
            if inserted:
                path.write_text(t, encoding="utf-8")
                print(f"  linked {donor} -> {orphan}")


def index_cards(topics: list[dict]) -> None:
    index = ART / "index.html"
    html = index.read_text(encoding="utf-8")
    for topic in topics:
        slug = topic["slug"]
        if f"/articulos/{slug}.html" in html:
            continue
        p = ART / f"{slug}.html"
        if not p.exists():
            continue
        page = p.read_text(encoding="utf-8")
        title = re.search(r"<title>(.*?)</title>", page).group(1)
        h3 = title.split("|")[0].strip()
        desc_m = re.search(r'<meta name="description" content="(.*?)"', page)
        d = desc_m.group(1) if desc_m else h3
        if len(d) > 120:
            d = d[:117] + "…"
        card = (
            f'      <a href="/articulos/{slug}.html" class="blog-card">\n'
            f'        <span class="blog-card-tag">Gu&iacute;a cl&iacute;nica</span>\n'
            f"        <h3>{h3}</h3>\n"
            f"        <p>{d}</p>\n"
            f"      </a>\n"
        )
        links = list(
            re.finditer(r'<a href="/articulos/([a-z0-9-]+)\.html" class="blog-card">', html)
        )
        insert_at = None
        for m in links:
            if m.group(1) > slug:
                insert_at = m.start()
                break
        if insert_at is None and links:
            start = links[-1].start()
            insert_at = html.find("</a>", start) + 4
            card = "\n" + card
        if insert_at is None:
            continue
        html = html[:insert_at] + card + html[insert_at:]
        print(f"  indexed {slug}")
    index.write_text(html, encoding="utf-8")


def main() -> None:
    load_env()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY missing")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    topics = json.loads(TOPICS.read_text(encoding="utf-8"))["topics"]
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    for topic in topics:
        slug = topic["slug"]
        out = OUTPUT_DIR / f"{slug}.json"
        html_path = ART / f"{slug}.html"
        if html_path.exists() and word_count(html_path) >= 1200 and "--force" not in sys.argv:
            print(f"SKIP {slug}")
            continue
        if out.exists() and "--force" not in sys.argv and not html_path.exists():
            print(f"JSON exists {slug}, will assemble")
            continue
        if out.exists() and "--force" not in sys.argv and html_path.exists():
            print(f"SKIP {slug}")
            continue
        print(f"GEN {slug}...")
        generate_content(client, topic)
        time.sleep(1)

    print("ASSEMBLE...")
    subprocess.check_call(
        ["node", str(BATCH_DIR / "assemble-batch.mjs"), "--batch", "12", "--limit", "40"],
        cwd=str(ROOT),
    )

    for topic in topics:
        path = ART / f"{topic['slug']}.html"
        if not path.exists():
            print("MISSING after assemble", topic["slug"])
            continue
        html = path.read_text(encoding="utf-8")
        html = inject_softapp(html)
        html = fix_cta_login(html)
        html = fix_hero(html, topic["slug"])
        html = update_title(html, topic["title_hint"])
        if topic.get("h1_hint"):
            html = force_h1(html, topic["h1_hint"])
        html = enrich_umbrella(html, topic)
        path.write_text(html, encoding="utf-8")
        print(f"  polished {topic['slug']} words={word_count(path)}")

    print("CROSS-LINKS...")
    add_cross_links(topics)
    print("INDEX...")
    index_cards(topics)
    print("DONE")


if __name__ == "__main__":
    main()
