#!/usr/bin/env python3
"""Restore slug-specific hero/inline paths in batch-9 HTML after image generation."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BATCH_DIR = Path(__file__).resolve().parent
ROOT = BATCH_DIR.parents[1]
ART = ROOT / "articulos"

# Must match run_batch9.py HERO_FALLBACK
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


def fix_paths(slug: str, fallback: str) -> bool:
    path = ART / f"{slug}.html"
    if not path.exists():
        print(f"  SKIP missing HTML: {slug}")
        return False

    html = path.read_text(encoding="utf-8")
    updated = html
    updated = updated.replace(f"/assets/blog/{fallback}-hero", f"/assets/blog/{slug}-hero")
    updated = updated.replace(f"/assets/blog/{fallback}-inline", f"/assets/blog/{slug}-inline")
    updated = updated.replace(
        f"https://kalyo.io/assets/blog/{fallback}-hero",
        f"https://kalyo.io/assets/blog/{slug}-hero",
    )

    if updated == html:
        print(f"  unchanged: {slug}")
        return False

    path.write_text(updated, encoding="utf-8")
    print(f"  fixed: {slug} ({fallback} -> {slug})")
    return True


def main() -> None:
    fixed = 0
    for slug, fallback in HERO_FALLBACK.items():
        if fix_paths(slug, fallback):
            fixed += 1
    print(f"Fixed {fixed}/{len(HERO_FALLBACK)} batch-9 articles")


if __name__ == "__main__":
    main()
