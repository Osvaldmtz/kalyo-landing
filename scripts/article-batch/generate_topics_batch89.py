#!/usr/bin/env python3
"""Generate topics-batch-8.json and topics-batch-9.json from article specs."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BATCH_DIR = Path(__file__).resolve().parent
ROOT = BATCH_DIR.parents[1]
sys.path.insert(0, str(BATCH_DIR))

from batch20_mexico_part1 import articles_part1  # noqa: E402
from batch20_mexico_part2 import articles_part2  # noqa: E402
from batch9_part1 import ARTICLES as A1  # noqa: E402
from batch9_part2 import ARTICLES as A2  # noqa: E402
from batch9_part3 import ARTICLES as A3  # noqa: E402
from batch9_part4 import ARTICLES as A4  # noqa: E402

B8_KEYWORDS = {
    "test-psicologico-mas-usados-mexico": "test psicológico",
    "gad-7-escala-ansiedad-generalizada": "GAD-7",
    "escala-de-beck-bdi-ii": "escala de Beck",
    "wisc-v-escala-inteligencia-ninos": "WISC V",
    "mmpi-2-inventario-personalidad": "MMPI-2",
    "test-de-inteligencia-adultos": "test de inteligencia",
    "16pf-cuestionario-personalidad": "16PF test",
    "historia-clinica-psicologica-formato": "historia clínica psicológica",
    "maslach-burnout-inventory-mbi": "Maslach burnout inventory",
    "bdi-inventario-depresion-beck": "BDI test",
    "gad-7-espanol-pdf": "GAD-7 PDF",
    "expediente-psicologico-estructura": "expediente psicológico",
    "test-conners-evaluacion-tdah": "test Conners",
    "escala-de-ansiedad-clinica": "escala de ansiedad",
    "phq9-vs-gad7-diferencias": "PHQ-9 GAD-7",
    "test-beck-depresion-interpretacion": "test Beck",
    "maslach-burnout-test-interpretacion": "test de Maslach",
    "wisc-iv-vs-wisc-v-diferencias": "WISC IV",
    "mmpi-inventario-multifasico": "MMPI",
    "wais-iv-escala-inteligencia-adultos": "WAIS IV",
}


def p(*_args):
    return ""


def table(*_args, **_kwargs):
    return ""


def topic_from_spec(spec: dict, primary_keyword: str | None = None) -> dict:
    slug = spec["slug"]
    kw = primary_keyword or B8_KEYWORDS.get(slug) or spec.get("keywords", slug).split(",")[0].strip()
    return {
        "slug": slug,
        "primary_keyword": kw,
        "title_hint": spec.get("title", spec.get("h1", slug)),
        "keywords": spec.get("keywords", kw),
        "category": "psicometria_clinica",
    }


def main() -> None:
    b8_specs = articles_part1(p, table, None) + articles_part2(p, table, None)
    b9_specs = A1 + A2 + A3 + A4

    topics8 = {
        "meta": {
            "batch": 8,
            "target_count": 20,
            "markets": ["MX"],
            "intent": "seo_psicometria_mexico",
        },
        "topics": [topic_from_spec(s) for s in b8_specs],
    }
    topics9 = {
        "meta": {
            "batch": 9,
            "target_count": 20,
            "markets": ["MX"],
            "intent": "seo_guias_clinicas_mexico",
        },
        "topics": [topic_from_spec(s) for s in b9_specs],
    }

    (BATCH_DIR / "topics-batch-8.json").write_text(
        json.dumps(topics8, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (BATCH_DIR / "topics-batch-9.json").write_text(
        json.dumps(topics9, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"topics-batch-8.json: {len(topics8['topics'])} topics")
    print(f"topics-batch-9.json: {len(topics9['topics'])} topics")


if __name__ == "__main__":
    main()
