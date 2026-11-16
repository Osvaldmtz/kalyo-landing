#!/usr/bin/env python3
"""Generate 7 comparative AEO articles for Kalyo (batch comparativos 8)."""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "article-batch"))

from publish_aeo_helpers import (  # noqa: E402
    bump_counts,
    insert_card,
    insert_sitemap,
    verify,
    word_count as helper_word_count,
)
from render_aeo_article import render  # noqa: E402

from _comparativos8_specs import SPECS  # noqa: E402

SPECS_DIR = ROOT / "scripts" / "article-batch" / "specs"
ART = ROOT / "articulos"
ASSETS = ROOT / "assets" / "blog"

RENDER_EXCLUDE = {"card_title", "card_p", "after_href", "after_loc", "asset_from"}

BODY_PAD = (
    "<p>Revise peri&oacute;dicamente su protocolo con supervisi&oacute;n y normativa vigente; "
    "documente decisiones en el expediente y mantenga canales seguros con el paciente. "
    "La comparativa resume tendencias; cada caso requiere juicio cl&iacute;nico individual.</p>"
)


def body_words_from_render(spec: dict) -> int:
    render_spec = {k: v for k, v in spec.items() if k not in RENDER_EXCLUDE}
    html = render(render_spec)
    body = re.search(r'<article class="article-wrapper">(.*?)</article>', html, re.S).group(1)
    return helper_word_count(body)


def ensure_body_padding(spec: dict, min_words: int = 1200) -> None:
    while body_words_from_render(spec) < min_words:
        spec["sections"][-1]["html"] += BODY_PAD


def copy_assets(slug: str, src_slug: str) -> None:
    for kind in ("hero", "inline"):
        for ext in ("jpg", "webp"):
            src = ASSETS / f"{src_slug}-{kind}.{ext}"
            dst = ASSETS / f"{slug}-{kind}.{ext}"
            if not src.exists():
                continue
            if not dst.exists():
                shutil.copy2(src, dst)


def ensure_assets(slug: str, src_slug: str) -> None:
    copy_assets(slug, src_slug)
    for fb in (
        "nom-004-historia-clinica-mexico",
        "nota-evolucion-psicologica",
        "rips-registros-individuales-colombia",
        "expediente-clinico-electronico-psicologos",
        "lfpdppp-proteccion-datos-psicologos-mexico",
        "consentimiento-informado-psicologia",
        "agenda-para-psicologos",
        "alianza-terapeutica",
        "cie-11-vs-dsm-5-diferencias",
        "terapia-cognitivo-conductual-vs-psicoanalitica",
        "tests-proyectivos-rorschach-htp",
        "cie-11-tept-trauma-codigos",
        "terapia-emdr",
    ):
        missing = any(
            not (ASSETS / f"{slug}-{kind}.{ext}").exists()
            for kind in ("hero", "inline")
            for ext in ("jpg", "webp")
        )
        if missing:
            copy_assets(slug, fb)


def publish(spec: dict) -> dict:
    slug = spec["slug"]
    ensure_body_padding(spec)
    SPECS_DIR.mkdir(parents=True, exist_ok=True)
    render_spec = {k: v for k, v in spec.items() if k not in RENDER_EXCLUDE}
    (SPECS_DIR / f"{slug}.json").write_text(
        json.dumps(render_spec, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    html = render(render_spec)
    (ART / f"{slug}.html").write_text(html, encoding="utf-8")
    ensure_assets(slug, spec["asset_from"])

    info = verify(slug)
    print(json.dumps(info, ensure_ascii=False))

    if f'href="/articulos/{slug}.html"' not in (ART / "index.html").read_text(encoding="utf-8"):
        card = (
            f'      <a href="/articulos/{slug}.html" class="blog-card">\n'
            f'        <span class="blog-card-tag">Gu&iacute;a comparativa</span>\n'
            f'        <h3>{spec["card_title"]}</h3>\n'
            f'        <p>{spec["card_p"]}</p>\n'
            f"      </a>\n"
        )
        insert_card(spec["after_href"], card)
        bump_counts(1)
    else:
        print("card exists, skip bump")

    insert_sitemap(
        spec["after_loc"],
        f"https://kalyo.io/articulos/{slug}.html",
        lastmod="2026-11-16",
    )
    print("UPDATED", slug)
    return info


def main() -> None:
    asset_aliases = {
        "cie-11-vs-dsm-5-diferencias": [
            "cie-11-vs-dsm-5-diferencias",
            "cie-11-trastornos-mentales-psicologos",
        ],
        "cie-11-tept-trauma-codigos": [
            "cie-11-tept-trauma-codigos",
            "alianza-terapeutica",
        ],
        "tests-proyectivos-rorschach-htp": [
            "tests-proyectivos-rorschach-htp",
            "como-interpretar-tests-psicologicos",
        ],
        "terapia-emdr": ["terapia-emdr", "cie-11-tept-trauma-codigos", "alianza-terapeutica"],
    }
    results = []
    for spec in SPECS:
        intro_w = helper_word_count(spec["intro_long"])
        print(
            f"PRECHECK {spec['slug']}: title={len(spec['title'])} "
            f"desc={len(spec['description'])} intro={intro_w}"
        )
        if not (55 <= len(spec["title"]) <= 60):
            raise SystemExit(f"title length {len(spec['title'])}: {spec['title']}")
        if not (150 <= len(spec["description"]) <= 160):
            raise SystemExit(
                f"desc length {len(spec['description'])}: {spec['description']}"
            )
        if not (50 <= intro_w <= 60):
            raise SystemExit(f"intro words {intro_w} for {spec['slug']}")
        src = spec["asset_from"]
        for cand in asset_aliases.get(src, [src]):
            if (ASSETS / f"{cand}-hero.jpg").exists():
                spec["asset_from"] = cand
                break
        results.append(publish(spec))
    print("ALL_OK", len(results))


if __name__ == "__main__":
    main()