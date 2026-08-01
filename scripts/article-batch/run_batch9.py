#!/usr/bin/env python3
"""Generate batch 9 clinical guide articles (21-40) using render_aeo_article."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "articulos"
BATCH_DIR = Path(__file__).resolve().parent
SPECS_DIR = BATCH_DIR / "specs"

sys.path.insert(0, str(ROOT / "scripts"))
from render_aeo_article import render  # noqa: E402

from batch9_part1 import ARTICLES as A1  # noqa: E402
from batch9_part2 import ARTICLES as A2  # noqa: E402
from batch9_part3 import ARTICLES as A3  # noqa: E402
from batch9_part4 import ARTICLES as A4  # noqa: E402

ALL_ARTICLES = A1 + A2 + A3 + A4

HERO_FALLBACK = {
    "escalas-ansiedad-psicologia-clinica": "que-es-el-gad-7",
    "escalas-depresion-validadas-espanol": "que-es-el-phq-9",
    "evaluacion-cognitiva-moca-mmse": "test-moca-evaluacion-cognitiva",
    "tests-proyectivos-rorschach-htp": "test-wartegg-proyectiva",
    "historia-clinica-psicologica-paso-a-paso": "nom-004-historia-clinica-mexico",
    "test-inteligencia-ninos-guia": "wisc-v-test-inteligencia-ninos",
    "sindrome-burnout-evaluacion": "inventario-burnout-mbi",
    "tdah-adultos-evaluacion-diagnostico": "tdah-adultos",
    "evaluacion-neuropsicologica-instrumentos": "evaluacion-neuropsicologica-guia-clinica",
    "trastornos-personalidad-dsm5": "tlp-trastorno-limite",
    "consentimiento-informado-psicologia-mexico": "consentimiento-informado-psicologia",
    "nota-evolucion-psicologica": "nom-004-historia-clinica-mexico",
    "plan-tratamiento-psicologico": "que-es-la-psicologia-clinica",
    "psicometria-que-es": "como-interpretar-tests-psicologicos",
    "etica-psicologo-mexico": "nom-004-historia-clinica-mexico",
    "test-personalidad-tipos-clinica": "neo-pi-r-personalidad",
    "evaluacion-psicologica-proceso": "que-es-la-psicologia-clinica",
    "escala-wechsler-guia-completa": "wisc-v-test-inteligencia-ninos",
    "psicologia-clinica-herramientas": "software-para-psicologos-clinicos",
    "tests-psicologicos-hub": "que-es-el-phq-9",
}


def word_count(html: str) -> int:
    m = re.search(r"<article[\s\S]*?</article>", html, re.I)
    plain = re.sub(r"<script[\s\S]*?</script>", " ", m.group(0) if m else html, flags=re.I)
    plain = re.sub(r"<[^>]+>", " ", plain)
    return len(re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ]+\b", plain, flags=re.UNICODE))


def fix_hero(html: str, slug: str) -> str:
    fb = HERO_FALLBACK.get(slug)
    if not fb:
        return html
    hero_jpg = ROOT / "assets" / "blog" / f"{fb}-hero.jpg"
    if hero_jpg.exists():
        html = html.replace(f"/assets/blog/{slug}-hero", f"/assets/blog/{fb}-hero")
        html = html.replace(f"/assets/blog/{slug}-inline", f"/assets/blog/{fb}-inline")
        html = html.replace(
            f"https://kalyo.io/assets/blog/{slug}-hero",
            f"https://kalyo.io/assets/blog/{fb}-hero",
        )
    return html


def insert_sitemap(new_loc: str, lastmod: str = "2026-08-01") -> None:
    sm = ROOT / "sitemap.xml"
    text = sm.read_text(encoding="utf-8")
    if new_loc in text:
        return
    block = (
        f"  <url>\n"
        f"    <loc>{new_loc}</loc>\n"
        f"    <lastmod>{lastmod}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n"
        f"    <priority>0.8</priority>\n"
        f"  </url>\n"
    )
    anchor = "https://kalyo.io/articulos/tests-psicologicos-hub.html"
    if anchor not in text:
        anchor = "https://kalyo.io/articulos/que-es-el-phq-9.html"
    pos = text.find(f"<loc>{anchor}</loc>")
    if pos < 0:
        pos = text.rfind("</url>")
        end = pos + len("</url>\n")
    else:
        end = text.find("</url>", pos) + len("</url>\n")
    sm.write_text(text[:end] + block + text[end:], encoding="utf-8")


def insert_index_card(spec: dict) -> None:
    slug = spec["slug"]
    index = ART / "index.html"
    html = index.read_text(encoding="utf-8")
    href = f"/articulos/{slug}.html"
    if href in html:
        return
    h3 = spec["title"].split("|")[0].strip()
    desc = spec["description"]
    if len(desc) > 120:
        desc = desc[:117] + "…"
    card = (
        f'      <a href="{href}" class="blog-card">\n'
        f'        <span class="blog-card-tag">Gu&iacute;a cl&iacute;nica</span>\n'
        f"        <h3>{h3}</h3>\n"
        f"        <p>{desc}</p>\n"
        f"      </a>\n"
    )
    marker = 'href="/articulos/tests-psicologicos-hub.html"'
    if marker not in html:
        marker = 'href="/articulos/que-es-el-phq-9.html"'
    pos = html.find(marker)
    if pos < 0:
        return
    end = html.find("</a>", pos) + 4
    html = html[:end] + "\n" + card + html[end:]
    index.write_text(html, encoding="utf-8")


def bump_index_count(delta: int) -> None:
    index = ART / "index.html"
    text = index.read_text(encoding="utf-8")
    m = re.search(r'"numberOfItems":\s*(\d+)', text)
    if m:
        n = int(m.group(1)) + delta
        text = text.replace(m.group(0), f'"numberOfItems": {n}', 1)
    index.write_text(text, encoding="utf-8")


def main() -> None:
    SPECS_DIR.mkdir(exist_ok=True)
    results = []
    new_count = 0

    for spec in ALL_ARTICLES:
        slug = spec["slug"]
        spec_path = SPECS_DIR / f"{slug}.json"
        spec_path.write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")

        out = ART / f"{slug}.html"
        existed = out.exists()
        html = render(spec)
        html = fix_hero(html, slug)
        out.write_text(html, encoding="utf-8")
        wc = word_count(html)
        results.append({"slug": slug, "words": wc, "path": str(out)})

        if not existed:
            insert_sitemap(f"https://kalyo.io/articulos/{slug}.html")
            insert_index_card(spec)
            new_count += 1

        print(f"OK {slug} ({wc} words)")

    if new_count:
        bump_index_count(new_count)

    print(f"\nGenerated {len(results)} articles ({new_count} new index/sitemap entries)")
    short = [r for r in results if r["words"] < 1200]
    if short:
        print("WARNING: below 1200 words:", [r["slug"] for r in short])
        sys.exit(1)


if __name__ == "__main__":
    main()
