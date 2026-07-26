#!/usr/bin/env python3
"""Generate BATCH 7-11 clinical concept articles (missing slugs) + polish existing ones."""
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
TOPICS = BATCH_DIR / "topics-batch-7.json"
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

EXISTING_TITLE_UPDATES = {
    "tdah-adultos.html": "TDAH en Adultos: Síntomas, Evaluación y Tratamiento | Kalyo",
    "apego-desorganizado.html": "Apego Desorganizado: Evaluación y Tratamiento | Kalyo",
    "habilidades-sociales.html": "Entrenamiento en Habilidades Sociales: Técnicas y Aplicación | Kalyo",
    "condicionamiento-operante.html": "Condicionamiento Operante: Qué Es y Aplicaciones Clínicas | Kalyo",
    "comunicacion-asertiva.html": "Comunicación Asertiva: Qué Es y Cómo Enseñarla | Kalyo",
    "claustrofobia.html": "Claustrofobia: Diagnóstico y Desensibilización Sistemática | Kalyo",
    "disonancia-cognitiva.html": "Disonancia Cognitiva: Qué Es y Aplicaciones Clínicas | Kalyo",
    "agorafobia.html": "Agorafobia: Evaluación y Tratamiento Conductual | Kalyo",
    "psicologia-humanista.html": "Psicología Humanista: Fundamentos y Aplicación Clínica | Kalyo",
    "fases-del-duelo.html": "Las 5 Fases del Duelo: Guía Clínica para Psicólogos | Kalyo",
    "violencia-psicologica.html": "Violencia Psicológica: Identificación y Abordaje Clínico | Kalyo",
    "distorsiones-cognitivas.html": "Distorsiones Cognitivas: Tipos y Técnicas de Reestructuración | Kalyo",
    "terapia-familiar-sistemica.html": "Terapia Familiar Sistémica: Fundamentos y Técnicas | Kalyo",
}

HERO_FALLBACK = {
    "bulimia-nerviosa": "bulimia-que-es",
    "empatia": "empatia-que-es",
    "resiliencia": "resiliencia-que-es",
    "autismo-espectro-autista": "autismo-que-es",
    "adiccion-psicologia": "adiccion-que-es",
    "trastorno-limite-personalidad": "tlp-trastorno-limite",
    "esquizofrenia": "esquizofrenia-que-es",
    "psicosis": "panss-esquizofrenia",
    "estres-psicologia": "pss-10-escala-estres-percibido",
    "trastorno-disociativo-identidad": "escala-pcl-5-estres-postraumatico",
    "terapia-gestalt": "psicologia-humanista",
    "inteligencias-multiples": "wais-iv-evaluacion-inteligencia-adultos",
    "primeros-auxilios-psicologicos": "evaluacion-riesgo-suicida",
    "trastorno-narcisista-personalidad": "tlp-trastorno-limite",
    "trastorno-antisocial-personalidad": "tlp-trastorno-limite",
    "depresion-sintomas": "que-es-el-phq-9",
    "autocompasion": "resiliencia-que-es",
}


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


def html_entities(text: str) -> str:
    repl = {
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
        "¡": "&iexcl;",
        "ü": "&uuml;",
        "Ü": "&Uuml;",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    return text


def generate_content(client: anthropic.Anthropic, topic: dict) -> dict:
    title_hint = topic.get("title_hint", "")
    required = topic.get("required_sections", [])
    prompt = f"""Eres redactor clínico SEO para kalyo.io (psicólogos LATAM).
Escribe un artículo clínico de guía (NO solo un test) sobre:
{json.dumps(topic, ensure_ascii=False)}

Título obligatorio (úsalo exacto o muy cercano): {title_hint}
Keyword principal a incluir en intro/H1/body: "{topic['primary_keyword']}"
Secciones obligatorias (como H2): {required}

Devuelve SOLO JSON:
{{
  "slug": "{topic['slug']}",
  "title": "{title_hint}",
  "description": "meta max 155 chars",
  "keywords": "{topic['keywords']}",
  "h1": "H1 distinto del title, con entidades HTML",
  "intro": "párrafo intro con keyword, entidades HTML",
  "heroAlt": "alt hero",
  "inlineAlt": "alt inline",
  "ctaTitle": "CTA Kalyo",
  "sections": [{{"title": "H2 entidades", "paragraphs": ["p1", "p2", "p3"]}}],
  "faq": [{{"q": "...", "a": "..."}}],
  "related_slugs": {json.dumps(topic.get("related_slugs", [])[:4])}
}}

Requisitos:
- Mínimo 9 secciones H2, 1800-2200 palabras
- Incluir DSM-5 o criterios cuando aplique
- Incluir H2 "Herramientas de evaluación" con instrumentos nombrados y links internos /articulos/....html cuando existan
- Incluir H2 "Abordaje terapéutico" con técnicas concretas
- Tono profesional
- HTML entities para acentos
- H1 DEBE diferir del title
- 4 FAQs
Responde SOLO JSON válido."""

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
            data["title"] = title_hint  # force
            data["slug"] = topic["slug"]
            out = OUTPUT_DIR / f"{topic['slug']}.json"
            out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            print(
                f"  OK content {topic['slug']} "
                f"(in={msg.usage.input_tokens} out={msg.usage.output_tokens})"
            )
            return data
        except json.JSONDecodeError as exc:
            last_err = exc
            print(f"  JSON fail {topic['slug']} attempt {attempt+1}: {exc}")
            time.sleep(2)
    raise last_err or RuntimeError(f"content failed for {topic['slug']}")


def inject_softapp(html: str) -> str:
    if '"@type": "SoftwareApplication"' in html or '"@type":"SoftwareApplication"' in html:
        return html
    block = (
        '<script type="application/ld+json">\n'
        + json.dumps(SOFTAPP, ensure_ascii=False, indent=2)
        + "\n</script>\n"
    )
    # insert after first ld+json script close or before </head>
    m = re.search(r'</script>\s*(?=<!-- Open Graph|<!-- Twitter|<link rel="stylesheet"|</head>)', html)
    if m:
        return html[: m.end()] + "\n" + block + html[m.end() :]
    return html.replace("</head>", block + "</head>", 1)


def fix_cta_login(html: str) -> str:
    html = re.sub(
        r'href="https://app\.kalyo\.io"(?!/)',
        'href="https://app.kalyo.io/login"',
        html,
    )
    html = re.sub(
        r'href="https://app\.kalyo\.io\?',
        'href="https://app.kalyo.io/login?',
        html,
    )
    # register stays; ensure at least one /login CTA in cta-box
    html = re.sub(
        r'(class="cta-btn"[^>]*href=")https://app\.kalyo\.io/register',
        r"\1https://app.kalyo.io/login",
        html,
    )
    html = re.sub(
        r'(href=")https://app\.kalyo\.io/register([^"]*")([^>]*class="cta-btn")',
        r"\1https://app.kalyo.io/login\2\3",
        html,
    )
    # simpler: any cta-btn to register → login
    def cta_repl(m):
        tag = m.group(0)
        tag = re.sub(
            r'https://app\.kalyo\.io/register[^"\']*',
            "https://app.kalyo.io/login",
            tag,
        )
        if "app.kalyo.io" in tag and "/login" not in tag and "/register" not in tag:
            tag = tag.replace("https://app.kalyo.io", "https://app.kalyo.io/login")
        return tag

    html = re.sub(r"<a[^>]*class=\"cta-btn\"[^>]*>.*?</a>", cta_repl, html, flags=re.S)
    return html


def fix_hero(html: str, slug: str) -> str:
    fb = HERO_FALLBACK.get(slug)
    if not fb:
        return html
    hero_jpg = ROOT / "assets" / "blog" / f"{fb}-hero.jpg"
    if not hero_jpg.exists():
        # placeholder
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
    # point images to fallback asset
    html = html.replace(f"/assets/blog/{slug}-hero", f"/assets/blog/{fb}-hero")
    html = html.replace(f"/assets/blog/{slug}-inline", f"/assets/blog/{fb}-inline")
    html = html.replace(
        f"https://kalyo.io/assets/blog/{slug}-hero",
        f"https://kalyo.io/assets/blog/{fb}-hero",
    )
    return html


def update_title_in_html(html: str, new_title: str) -> str:
    html = re.sub(r"<title>.*?</title>", f"<title>{new_title}</title>", html, count=1, flags=re.S)
    html = re.sub(
        r'(property="og:title" content=")[^"]*"',
        rf'\1{new_title.replace(chr(34), "&quot;")}"',
        html,
        count=1,
    )
    html = re.sub(
        r'(name="twitter:title" content=")[^"]*"',
        rf'\1{new_title.replace(chr(34), "&quot;")}"',
        html,
        count=1,
    )
    return html


def polish_html(path: Path, slug: str | None = None) -> None:
    html = path.read_text(encoding="utf-8")
    slug = slug or path.stem
    html = inject_softapp(html)
    html = fix_cta_login(html)
    html = fix_hero(html, slug)
    path.write_text(html, encoding="utf-8")


def word_count(path: Path) -> int:
    t = path.read_text(encoding="utf-8")
    t = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    m = re.search(r"<article[\s\S]*?</article>", t, re.I)
    plain = re.sub(r"<[^>]+>", " ", m.group(0) if m else t)
    return len(re.findall(r"\w+", plain))


def main() -> None:
    load_env()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY missing")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    topics = json.loads(TOPICS.read_text(encoding="utf-8"))["topics"]
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    # 1) Generate missing content JSON
    for topic in topics:
        slug = topic["slug"]
        out = OUTPUT_DIR / f"{slug}.json"
        html_path = ART / f"{slug}.html"
        if out.exists() and html_path.exists() and word_count(html_path) >= 1200:
            print(f"SKIP content {slug} (already exists)")
            continue
        if out.exists() and "--force" not in sys.argv:
            print(f"SKIP LLM {slug} (json exists); will assemble")
            continue
        print(f"GEN {slug}...")
        generate_content(client, topic)
        time.sleep(1)

    # 2) Assemble via node
    print("ASSEMBLE...")
    subprocess.check_call(
        ["node", str(BATCH_DIR / "assemble-batch.mjs"), "--batch", "7", "--limit", "40"],
        cwd=str(ROOT),
    )

    # 3) Polish new articles
    for topic in topics:
        path = ART / f"{topic['slug']}.html"
        if path.exists():
            polish_html(path, topic["slug"])
            # force exact title
            html = path.read_text(encoding="utf-8")
            html = update_title_in_html(html, topic["title_hint"])
            path.write_text(html, encoding="utf-8")
            print(f"  polished {topic['slug']} words={word_count(path)}")

    # 4) Update existing titles + SoftApp
    for fname, title in EXISTING_TITLE_UPDATES.items():
        path = ART / fname
        if not path.exists():
            print(f"MISSING existing {fname}")
            continue
        html = path.read_text(encoding="utf-8")
        html = update_title_in_html(html, title)
        path.write_text(html, encoding="utf-8")
        polish_html(path, path.stem)
        print(f"  updated existing {fname} words={word_count(path)}")

    print("DONE")


if __name__ == "__main__":
    main()
