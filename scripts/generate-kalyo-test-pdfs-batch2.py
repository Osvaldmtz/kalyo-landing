#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate clinical PDFs for batch-2 article slugs (PHQ-2 article template companions).

Reuses kalyo_pdf_common design (same as batch 1) and clinical item banks from batch234,
writing files named exactly {article-slug}-espanol.pdf under assets/.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import kalyo_pdf_common as common
from kalyo_pdf_common import LIKERT_4, LIKERT_4_SHORT, build_instrument_pdf  # noqa: E402


def _load_batch234():
    path = SCRIPTS / "generate-kalyo-test-pdfs-batch234.py"
    spec = importlib.util.spec_from_file_location("kalyo_pdf_batch234", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b234 = _load_batch234()
LIKERT_0_4 = b234.LIKERT_0_4
LIKERT_0_5 = b234.LIKERT_0_5
LIKERT_0_6 = b234.LIKERT_0_6
LIKERT_1_4 = b234.LIKERT_1_4
YES_NO = b234.YES_NO
gen_audit = b234.gen_audit
gen_audit_c = b234.gen_audit_c
gen_bhs = b234.gen_bhs
gen_cage = b234.gen_cage
gen_cd_risc = b234.gen_cd_risc
gen_cssrs = b234.gen_cssrs
gen_dast10 = b234.gen_dast10
gen_hads = b234.gen_hads
gen_ies_r = b234.gen_ies_r
gen_isi = b234.gen_isi
gen_mbi = b234.gen_mbi
gen_pcl5 = b234.gen_pcl5
gen_psqi = b234.gen_psqi
gen_pss10 = b234.gen_pss10
gen_rosenberg = b234.gen_rosenberg
gen_sbq_r = b234.gen_sbq_r
gen_who5 = b234.gen_who5
gen_wurs = b234.gen_wurs

# Remap legacy batch234 filenames → article-slug filenames
FILENAME_REMAP = {
    "hads-escala-ansiedad-depresion-espanol.pdf": "hads-ansiedad-depresion-hospitalaria-espanol.pdf",
    "c-ssrs-escala-columbia-suicidio-espanol.pdf": "c-ssrs-riesgo-suicida-espanol.pdf",
    "ies-r-impacto-estres-postraumatico-espanol.pdf": "ies-r-impacto-evento-espanol.pdf",
    "bhs-escala-desesperanza-beck-espanol.pdf": "bhs-desesperanza-beck-espanol.pdf",
    "sbq-r-conducta-suicida-espanol.pdf": "sbq-r-comportamiento-suicida-espanol.pdf",
    "psqi-indice-calidad-sueno-espanol.pdf": "psqi-calidad-sueno-pittsburg-espanol.pdf",
    "wurs-tdah-infancia-adultos-espanol.pdf": "wurs-tdah-adultos-espanol.pdf",
    "audit-c-tamizaje-alcohol-breve-espanol.pdf": "audit-c-consumo-alcohol-espanol.pdf",
    "cage-tamizaje-alcoholismo-espanol.pdf": "cage-dependencia-alcohol-espanol.pdf",
    "dast-10-deteccion-drogas-espanol.pdf": "dast-10-abuso-sustancias-espanol.pdf",
    "mbi-inventario-burnout-espanol.pdf": "mbi-burnout-maslach-espanol.pdf",
    "rosenberg-escala-autoestima-espanol.pdf": "escala-autoestima-rosenberg-espanol.pdf",
    "who-5-bienestar-psicologico-espanol.pdf": "who-5-bienestar-espanol.pdf",
}

_orig_write_pdf = common.write_pdf


def _write_pdf(filename: str, story: list) -> Path:
    return _orig_write_pdf(FILENAME_REMAP.get(filename, filename), story)


common.write_pdf = _write_pdf


def gen_phq9():
    items = [
        "Poco interés o placer en hacer las cosas",
        "Sentirse decaído(a), deprimido(a) o sin esperanzas",
        "Dificultad para dormir o dormir demasiado",
        "Sentirse cansado(a) o con poca energía",
        "Poco apetito o comer en exceso",
        "Sentirse mal consigo mismo(a) — o que es un fracaso o ha fallado a sí mismo(a) o a su familia",
        "Dificultad para concentrarse en cosas como leer el periódico o ver televisión",
        "Moverse o hablar tan lento que otros lo notan — o al contrario, estar tan inquieto(a) o agitado(a) que se mueve más de lo habitual",
        "Pensamientos de que estaría mejor muerto(a) o de hacerse daño de alguna forma",
    ]
    return build_instrument_pdf(
        "phq-9-escala-depresion-espanol.pdf",
        "PHQ-9 en Español",
        "Patient Health Questionnaire-9 — Escala de depresión",
        "Autoreporte. Indique con qué frecuencia le han molestado los problemas durante las <b>últimas 2 semanas</b>. "
        "9 ítems, escala 0–3. Tiempo: 2–5 minutos. El ítem 9 requiere evaluación de seguridad si es positivo.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 27",
        ["Puntaje", "Severidad", "Acción sugerida"],
        [
            ["0 – 4", "Mínima / ausente", "Monitoreo según criterio clínico"],
            ["5 – 9", "Leve", "Psicoeducación y reevaluación"],
            ["10 – 14", "Moderada", "Evaluación integral y plan de tratamiento"],
            ["15 – 19", "Moderadamente grave", "Intervención prioritaria"],
            ["20 – 27", "Grave", "Manejo intensivo; evaluar riesgo (ítem 9)"],
        ],
        "Aplica el PHQ-9 y registra resultados en el expediente con Kalyo — kalyo.io",
        "Kroenke K, Spitzer RL, Williams JB. The PHQ-9. J Gen Intern Med. 2001;16(9):606-613. Instrumento de dominio público.",
        scale_note="Escala de respuesta: " + " · ".join(LIKERT_4),
        scale_headers=LIKERT_4_SHORT,
    )


def gen_gad7():
    items = [
        "Sentirse nervioso(a), ansioso(a) o muy alterado(a)",
        "No poder dejar de preocuparse o no poder controlar la preocupación",
        "Preocuparse demasiado por diferentes cosas",
        "Dificultad para relajarse",
        "Estar tan inquieto(a) que es difícil quedarse quieto(a)",
        "Molestarse o irritarse con facilidad",
        "Sentir miedo como si algo terrible pudiera pasar",
    ]
    return build_instrument_pdf(
        "gad-7-escala-ansiedad-generalizada-espanol.pdf",
        "GAD-7 en Español",
        "Generalized Anxiety Disorder-7 — Escala de ansiedad generalizada",
        "Autoreporte sobre las <b>últimas 2 semanas</b>. 7 ítems, escala 0–3. "
        "Tiempo: 2–3 minutos. Útil para tamizaje y seguimiento de severidad.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 21",
        ["Puntaje", "Severidad", "Acción sugerida"],
        [
            ["0 – 4", "Mínima", "Seguimiento habitual"],
            ["5 – 9", "Leve", "Estrategias de afrontamiento y reevaluación"],
            ["10 – 14", "Moderada", "Evaluación clínica y plan terapéutico"],
            ["15 – 21", "Grave", "Intervención prioritaria"],
        ],
        "Registra tamizajes GAD-7 en tu consulta con Kalyo — kalyo.io",
        "Spitzer RL, Kroenke K, Williams JBW, Löwe B. A brief measure for assessing GAD: the GAD-7. Arch Intern Med. 2006;166(10):1092-1097.",
        scale_note="Escala de respuesta: " + " · ".join(LIKERT_4),
        scale_headers=LIKERT_4_SHORT,
    )


GENERATORS = [
    ("PHQ-9", gen_phq9, "phq-9-escala-depresion-espanol.pdf"),
    ("GAD-7", gen_gad7, "gad-7-escala-ansiedad-generalizada-espanol.pdf"),
    ("PCL-5", gen_pcl5, "pcl-5-estres-postraumatico-espanol.pdf"),
    ("AUDIT", gen_audit, "audit-test-alcoholismo-espanol.pdf"),
    ("AUDIT-C", gen_audit_c, "audit-c-consumo-alcohol-espanol.pdf"),
    ("CAGE", gen_cage, "cage-dependencia-alcohol-espanol.pdf"),
    ("ISI", gen_isi, "isi-indice-severidad-insomnio-espanol.pdf"),
    ("PSQI", gen_psqi, "psqi-calidad-sueno-pittsburg-espanol.pdf"),
    ("PSS-10", gen_pss10, "pss-10-escala-estres-percibido-espanol.pdf"),
    ("WHO-5", gen_who5, "who-5-bienestar-espanol.pdf"),
    ("Rosenberg", gen_rosenberg, "escala-autoestima-rosenberg-espanol.pdf"),
    ("HADS", gen_hads, "hads-ansiedad-depresion-hospitalaria-espanol.pdf"),
    ("IES-R", gen_ies_r, "ies-r-impacto-evento-espanol.pdf"),
    ("C-SSRS", gen_cssrs, "c-ssrs-riesgo-suicida-espanol.pdf"),
    ("BHS", gen_bhs, "bhs-desesperanza-beck-espanol.pdf"),
    ("SBQ-R", gen_sbq_r, "sbq-r-comportamiento-suicida-espanol.pdf"),
    ("MBI", gen_mbi, "mbi-burnout-maslach-espanol.pdf"),
    ("CD-RISC", gen_cd_risc, "cd-risc-resiliencia-espanol.pdf"),
    ("DAST-10", gen_dast10, "dast-10-abuso-sustancias-espanol.pdf"),
    ("WURS", gen_wurs, "wurs-tdah-adultos-espanol.pdf"),
]


def main() -> None:
    # silence unused-import lint for scale constants re-exported via batch234 gens
    _ = (LIKERT_0_4, LIKERT_0_5, LIKERT_0_6, LIKERT_1_4, YES_NO)

    assets = common.ASSETS
    print(f"Output dir: {assets}")
    ok = []
    for name, fn, expected in GENERATORS:
        path = fn()
        if path.name != expected:
            raise SystemExit(f"{name}: wrote {path.name}, expected {expected}")
        size = path.stat().st_size
        print(f"  ✓ {name:10} → {path.name} ({size:,} bytes)")
        ok.append(path)

    missing = [e for _, _, e in GENERATORS if not (assets / e).exists()]
    if missing:
        raise SystemExit(f"Missing files: {missing}")
    print(f"\nDone: {len(ok)} PDFs in {assets}")


if __name__ == "__main__":
    main()
