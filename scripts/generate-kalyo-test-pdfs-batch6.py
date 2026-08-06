#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Kalyo-branded clinical test PDFs (batch 6) and patch blog HTML download buttons."""

from __future__ import annotations

import re
from pathlib import Path

from kalyo_pdf_common import (
    ASSETS,
    LIKERT_4_SHORT,
    build_instrument_pdf,
)

ROOT = Path(__file__).resolve().parents[1]
ARTICULOS = ROOT / "articulos"

from batch6_generators_part1 import (  # noqa: E402
    gen_epq_r,
    gen_neo_ffi,
    gen_pid5_bf,
    gen_sf36,
    gen_whodas,
)
from batch6_generators_part2 import (  # noqa: E402
    gen_cbcl,
    gen_cope,
    gen_psc17,
    gen_rcmas2,
    gen_scared,
    gen_sdq,
    gen_tmms24,
    gen_ucla,
)
from batch6_generators_part3 import (  # noqa: E402
    gen_cdi2,
    gen_crafft2,
    gen_dudit,
    gen_ftnd,
    gen_mast,
    gen_rads2,
    gen_taps,
)

LIKERT_0_4 = ["0", "1", "2", "3", "4"]
LIKERT_0_5 = ["0", "1", "2", "3", "4", "5"]
LIKERT_1_4 = ["1", "2", "3", "4"]
LIKERT_1_5 = ["1", "2", "3", "4", "5"]
YES_NO = ["No", "Sí"]
LIKERT_0_3 = ["0", "1", "2", "3"]
LIKERT_1_7 = ["1", "2", "3", "4", "5", "6", "7"]

BTN_SOLID_CSS = """
    .btn-solid {
      display: inline-block;
      font-family: 'Outfit', sans-serif;
      padding: 12px 24px;
      background: var(--purple);
      color: #fff;
      border-radius: 10px;
      font-size: 15px;
      font-weight: 600;
      text-decoration: none;
      transition: background 0.2s, transform 0.2s, box-shadow 0.2s;
      box-shadow: 0 4px 14px rgba(124, 61, 227, 0.3);
    }

    .btn-solid:hover {
      background: var(--purple-dark);
      transform: translateY(-1px);
    }

    .article-quick-actions {
      margin: 0 0 24px;
    }
"""

# Generators and HTML patches
GENERATORS: list[tuple[str, object]] = [
    ("SF-36", gen_sf36),
    ("WHODAS 2.0", gen_whodas),
    ("NEO-FFI", gen_neo_ffi),
    ("PID-5-BF", gen_pid5_bf),
    ("EPQ-R", gen_epq_r),
    ("UCLA-LS", gen_ucla),
    ("TMMS-24", gen_tmms24),
    ("Brief COPE", gen_cope),
    ("SCARED", gen_scared),
    ("RCMAS-2", gen_rcmas2),
    ("CBCL", gen_cbcl),
    ("SDQ", gen_sdq),
    ("PSC-17", gen_psc17),
    ("CDI-2", gen_cdi2),
    ("RADS-2", gen_rads2),
    ("CRAFFT 2.1", gen_crafft2),
    ("FTND", gen_ftnd),
    ("DUDIT", gen_dudit),
    ("MAST", gen_mast),
    ("TAPS", gen_taps),
]

HTML_PATCHES: list[tuple[str, str, str, str]] = [
    ("sf-36-calidad-vida-salud.html", "/assets/sf-36-calidad-vida-salud-espanol.pdf", "SF-36-espanol-Kalyo.pdf", "Descargar SF-36 en espa&ntilde;ol (PDF gratuito)"),
    ("whodas-discapacidad-funcionamiento.html", "/assets/whodas-discapacidad-funcionamiento-espanol.pdf", "WHODAS-espanol-Kalyo.pdf", "Descargar WHODAS 2.0 en espa&ntilde;ol (PDF gratuito)"),
    ("neo-pi-r-personalidad.html", "/assets/neo-pi-r-personalidad-espanol.pdf", "NEO-FFI-espanol-Kalyo.pdf", "Descargar NEO-FFI en espa&ntilde;ol (PDF gratuito)"),
    ("pid-5-bf-personalidad-dsm5.html", "/assets/pid-5-bf-personalidad-dsm5-espanol.pdf", "PID-5-BF-espanol-Kalyo.pdf", "Descargar PID-5-BF en espa&ntilde;ol (PDF gratuito)"),
    ("epq-r-cuestionario-eysenck.html", "/assets/epq-r-cuestionario-eysenck-espanol.pdf", "EPQ-R-espanol-Kalyo.pdf", "Descargar EPQ-R en espa&ntilde;ol (PDF gratuito)"),
    ("ucla-escala-soledad.html", "/assets/ucla-escala-soledad-espanol.pdf", "UCLA-espanol-Kalyo.pdf", "Descargar UCLA Escala de Soledad en espa&ntilde;ol (PDF gratuito)"),
    ("tmms-24-inteligencia-emocional.html", "/assets/tmms-24-inteligencia-emocional-espanol.pdf", "TMMS-24-espanol-Kalyo.pdf", "Descargar TMMS-24 en espa&ntilde;ol (PDF gratuito)"),
    ("cope-inventario-afrontamiento.html", "/assets/cope-inventario-afrontamiento-espanol.pdf", "Brief-COPE-espanol-Kalyo.pdf", "Descargar Brief COPE en espa&ntilde;ol (PDF gratuito)"),
    ("scared-ansiedad-infantil.html", "/assets/scared-ansiedad-infantil-espanol.pdf", "SCARED-espanol-Kalyo.pdf", "Descargar SCARED en espa&ntilde;ol (PDF gratuito)"),
    ("rcmas-2-ansiedad-infantil.html", "/assets/rcmas-2-ansiedad-infantil-espanol.pdf", "RCMAS-2-espanol-Kalyo.pdf", "Descargar RCMAS-2 en espa&ntilde;ol (PDF gratuito)"),
    ("cbcl-cuestionario-capacidades-comportamiento.html", "/assets/cbcl-cuestionario-capacidades-comportamiento-espanol.pdf", "CBCL-espanol-Kalyo.pdf", "Descargar CBCL en espa&ntilde;ol (PDF gratuito)"),
    ("sdq-cuestionario-fortalezas-dificultades.html", "/assets/sdq-cuestionario-fortalezas-dificultades-espanol.pdf", "SDQ-espanol-Kalyo.pdf", "Descargar SDQ en espa&ntilde;ol (PDF gratuito)"),
    ("psc-17-tamizaje-pediatrico.html", "/assets/psc-17-tamizaje-pediatrico-espanol.pdf", "PSC-17-espanol-Kalyo.pdf", "Descargar PSC-17 en espa&ntilde;ol (PDF gratuito)"),
    ("cdi-2-inventario-depresion-infantil.html", "/assets/cdi-2-inventario-depresion-infantil-espanol.pdf", "CDI-2-espanol-Kalyo.pdf", "Descargar CDI-2 en espa&ntilde;ol (PDF gratuito)"),
    ("rads-2-depresion-adolescentes.html", "/assets/rads-2-depresion-adolescentes-espanol.pdf", "RADS-2-espanol-Kalyo.pdf", "Descargar RADS-2 en espa&ntilde;ol (PDF gratuito)"),
    ("crafft-2-tamizaje-adolescentes.html", "/assets/crafft-2-tamizaje-adolescentes-espanol.pdf", "CRAFFT-2-espanol-Kalyo.pdf", "Descargar CRAFFT 2.1 en espa&ntilde;ol (PDF gratuito)"),
    ("ftnd-test-nicotina-dependencia.html", "/assets/ftnd-test-nicotina-dependencia-espanol.pdf", "FTND-espanol-Kalyo.pdf", "Descargar FTND en espa&ntilde;ol (PDF gratuito)"),
    ("dudit-tamizaje-drogas.html", "/assets/dudit-tamizaje-drogas-espanol.pdf", "DUDIT-espanol-Kalyo.pdf", "Descargar DUDIT en espa&ntilde;ol (PDF gratuito)"),
    ("mast-test-alcohol-michigan.html", "/assets/mast-test-alcohol-michigan-espanol.pdf", "MAST-espanol-Kalyo.pdf", "Descargar MAST en espa&ntilde;ol (PDF gratuito)"),
    ("taps-tamizaje-alcohol-sustancias.html", "/assets/taps-tamizaje-alcohol-sustancias-espanol.pdf", "TAPS-espanol-Kalyo.pdf", "Descargar TAPS en espa&ntilde;ol (PDF gratuito)"),
]


def patch_html_articles() -> int:
    """Add btn-solid CSS and download button after first </h1> in blog articles."""
    patched = 0
    for html_name, pdf_href, download_name, btn_label in HTML_PATCHES:
        path = ARTICULOS / html_name
        if not path.exists():
            print(f"SKIP  {html_name} (not found)")
            continue
        text = path.read_text(encoding="utf-8")
        original = text

        if ".btn-solid" not in text:
            anchor = "    /* Footer */"
            if anchor in text:
                text = text.replace(anchor, BTN_SOLID_CSS + "\n" + anchor, 1)
            elif "</style>" in text:
                text = text.replace("</style>", BTN_SOLID_CSS + "\n  </style>", 1)

        btn_block = (
            f'    <p class="article-quick-actions">\n'
            f'      <a href="{pdf_href}" download="{download_name}" class="btn-solid">{btn_label}</a>\n'
            f"    </p>\n"
        )

        if pdf_href not in text:
            text, count = re.subn(r"(</h1>\s*)", r"\1\n\n" + btn_block, text, count=1)
            if count == 0:
                print(f"WARN  {html_name} — no </h1> found")
                continue

        if text != original:
            path.write_text(text, encoding="utf-8")
            patched += 1
            print(f"PATCH {html_name}")
        else:
            print(f"OK    {html_name} (already patched)")

    return patched


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    created = []
    for name, fn in GENERATORS:
        path = fn()
        created.append((name, path.name, path.stat().st_size))
        print(f"OK  {path.name} ({path.stat().st_size:,} bytes)")
    print(f"\nGenerated {len(created)} PDFs in {ASSETS}")

    n = patch_html_articles()
    print(f"\nPatched {n} HTML articles in {ARTICULOS}")


if __name__ == "__main__":
    main()
