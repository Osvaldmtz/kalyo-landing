#!/usr/bin/env python3
"""Insert blog.css link, hero and inline images into all article HTML files."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "articulos"

ARTICLES = {
    "inventario-depresion-beck-bdi.html": {
        "slug": "inventario-depresion-beck-bdi",
        "hero_alt": "Inventario BDI-II de depresi\u00f3n en cuestionario digital con interfaz cl\u00ednica p\u00farpura",
        "inline_alt": "Gr\u00e1fico de interpretaci\u00f3n de puntuaciones del Inventario de Depresi\u00f3n de Beck",
    },
    "test-beck-ansiedad-bai.html": {
        "slug": "test-beck-ansiedad-bai",
        "hero_alt": "Inventario de Ansiedad de Beck BAI en pantalla digital con interfaz p\u00farpura",
        "inline_alt": "Visualizaci\u00f3n de s\u00edntomas de ansiedad en herramienta de evaluaci\u00f3n cl\u00ednica",
    },
    "que-es-el-phq-9.html": {
        "slug": "que-es-el-phq-9",
        "hero_alt": "Cuestionario PHQ-9 de tamizaje de depresi\u00f3n en tablet con dise\u00f1o minimalista p\u00farpura",
        "inline_alt": "Escala de puntuaci\u00f3n e interpretaci\u00f3n cl\u00ednica del PHQ-9",
    },
    "que-es-el-gad-7.html": {
        "slug": "que-es-el-gad-7",
        "hero_alt": "Evaluaci\u00f3n GAD-7 de ansiedad en formato digital con tema p\u00farpura cl\u00ednico",
        "inline_alt": "Escala de severidad GAD-7 para medici\u00f3n de ansiedad cl\u00ednica",
    },
    "escala-pcl-5-estres-postraumatico.html": {
        "slug": "escala-pcl-5-estres-postraumatico",
        "hero_alt": "Lista de verificaci\u00f3n PCL-5 para TEPT en herramienta cl\u00ednica digital p\u00farpura",
        "inline_alt": "Visualizaci\u00f3n de evaluaci\u00f3n de estr\u00e9s postraum\u00e1tico en psicolog\u00eda cl\u00ednica",
    },
    "escala-dass-21.html": {
        "slug": "escala-dass-21",
        "hero_alt": "Escala DASS-21 de depresi\u00f3n, ansiedad y estr\u00e9s en evaluaci\u00f3n digital p\u00farpura",
        "inline_alt": "Comparaci\u00f3n de subescalas DASS-21 para interpretaci\u00f3n cl\u00ednica",
    },
    "escala-hamilton-ansiedad-ham-a.html": {
        "slug": "escala-hamilton-ansiedad-ham-a",
        "hero_alt": "Escala Hamilton de Ansiedad HAM-A en herramienta cl\u00ednica digital p\u00farpura",
        "inline_alt": "Gr\u00e1fico de evaluaci\u00f3n de los 14 \u00edtems HAM-A de ansiedad",
    },
    "inventario-burnout-mbi.html": {
        "slug": "inventario-burnout-mbi",
        "hero_alt": "Inventario de Burnout de Maslach MBI en evaluaci\u00f3n profesional digital p\u00farpura",
        "inline_alt": "Visualizaci\u00f3n de las tres dimensiones del burnout: agotamiento, cinismo y eficacia",
    },
    "resiliencia-cd-risc.html": {
        "slug": "resiliencia-cd-risc",
        "hero_alt": "Escala de Resiliencia Connor-Davidson CD-RISC en evaluaci\u00f3n digital p\u00farpura",
        "inline_alt": "Gr\u00e1fico de medici\u00f3n de resiliencia y fortalezas psicol\u00f3gicas",
    },
    "audit-test-alcoholismo.html": {
        "slug": "audit-test-alcoholismo",
        "hero_alt": "Test AUDIT de identificaci\u00f3n de trastornos por consumo de alcohol en formato digital",
        "inline_alt": "Gr\u00e1fico de puntuaci\u00f3n y niveles de riesgo del test AUDIT",
    },
    "evaluacion-riesgo-suicida.html": {
        "slug": "evaluacion-riesgo-suicida",
        "hero_alt": "Protocolo digital de evaluaci\u00f3n de riesgo suicida en entorno cl\u00ednico seguro",
        "inline_alt": "Visualizaci\u00f3n de niveles de riesgo en protocolo de seguridad cl\u00ednica",
    },
    "test-vocacional-riasec.html": {
        "slug": "test-vocacional-riasec",
        "hero_alt": "Test vocacional RIASEC de Holland con hex\u00e1gono de carreras en formato digital",
        "inline_alt": "Hex\u00e1gono RIASEC con los seis tipos vocacionales de Holland",
    },
    "orientacion-vocacional-psicologia.html": {
        "slug": "orientacion-vocacional-psicologia",
        "hero_alt": "Sesi\u00f3n de orientaci\u00f3n vocacional con herramientas digitales en consultorio p\u00farpura",
        "inline_alt": "Visualizaci\u00f3n de trayectorias profesionales en psicolog\u00eda vocacional",
    },
    "como-interpretar-tests-psicologicos.html": {
        "slug": "como-interpretar-tests-psicologicos",
        "hero_alt": "Psic\u00f3logo interpretando resultados de tests en pantalla en consultorio cl\u00ednico",
        "inline_alt": "Flujo de trabajo para interpretaci\u00f3n de puntuaciones en psicolog\u00eda cl\u00ednica",
    },
    "como-documentar-sesion-clinica.html": {
        "slug": "como-documentar-sesion-clinica",
        "hero_alt": "Documentaci\u00f3n digital de sesi\u00f3n cl\u00ednica con notas SOAP en tablet p\u00farpura",
        "inline_alt": "Estructura de notas SOAP para documentaci\u00f3n cl\u00ednica",
    },
    "consentimiento-informado-psicologia.html": {
        "slug": "consentimiento-informado-psicologia",
        "hero_alt": "Formulario digital de consentimiento informado firmado en tablet en consultorio",
        "inline_alt": "Checklist de elementos del consentimiento informado en psicolog\u00eda cl\u00ednica",
    },
    "evaluacion-psicologica-colombia-mexico.html": {
        "slug": "evaluacion-psicologica-colombia-mexico",
        "hero_alt": "Evaluaci\u00f3n psicol\u00f3gica digital en contexto cl\u00ednico de Colombia y M\u00e9xico",
        "inline_alt": "Visualizaci\u00f3n de evaluaci\u00f3n psicol\u00f3gica transcultural en Latinoam\u00e9rica",
    },
    "software-para-psicologos-clinicos.html": {
        "slug": "software-para-psicologos-clinicos",
        "hero_alt": "Panel de software cl\u00ednico para psic\u00f3logos con m\u00faltiples herramientas digitales",
        "inline_alt": "Comparaci\u00f3n de funciones de gesti\u00f3n de consultorio psicol\u00f3gico",
    },
    "tests-psicologicos-digitales.html": {
        "slug": "tests-psicologicos-digitales",
        "hero_alt": "Plataforma de tests psicol\u00f3gicos digitales en tablet y laptop con tema p\u00farpura",
        "inline_alt": "Comparaci\u00f3n visual entre tests psicol\u00f3gicos digitales y en papel",
    },
    "alternativas-elo-psicologos-mexico.html": {
        "slug": "alternativas-elo-psicologos-mexico",
        "hero_alt": "Comparaci\u00f3n de alternativas de software para psic\u00f3logos en M\u00e9xico",
        "inline_alt": "Gr\u00e1fico comparativo de herramientas cl\u00ednicas para psic\u00f3logos en M\u00e9xico",
    },
}

CSS_LINK = '  <link rel="stylesheet" href="/assets/blog.css">\n'


def hero_html(meta):
    slug = meta["slug"]
    alt = meta["hero_alt"]
    return f"""    <div class="article-hero-img">
      <img src="/assets/blog/{slug}-hero.jpg"
           alt="{alt}"
           width="1200" height="630"
           loading="eager" fetchpriority="high">
    </div>
"""


def inline_html(meta):
    slug = meta["slug"]
    alt = meta["inline_alt"]
    return f"""    <figure class="article-inline-img">
      <img src="/assets/blog/{slug}-inline.jpg"
           alt="{alt}"
           width="800" height="450"
           loading="lazy">
    </figure>
"""


def process_file(path: Path, meta: dict) -> None:
    content = path.read_text(encoding="utf-8")

    if "/assets/blog.css" not in content:
        content = content.replace(
            '  <link href="https://fonts.googleapis.com/css2?family=Outfit',
            CSS_LINK + '  <link href="https://fonts.googleapis.com/css2?family=Outfit',
        )

    hero = hero_html(meta)
    if "article-hero-img" not in content:
        content = content.replace(
            '  <article class="article-wrapper">\n',
            '  <article class="article-wrapper">\n' + hero,
        )

    inline = inline_html(meta)
    if "article-inline-img" not in content:
        h2_matches = list(re.finditer(r"<h2[^>]*>", content))
        if len(h2_matches) >= 3:
            insert_pos = h2_matches[2].start()
            # Find end of the h2 section's first paragraph block - insert before 3rd h2
            content = content[:insert_pos] + inline + "\n" + content[insert_pos:]

    path.write_text(content, encoding="utf-8")
    print(f"Updated: {path.name}")


def main():
    for filename, meta in ARTICLES.items():
        path = ROOT / filename
        if not path.exists():
            print(f"MISSING: {filename}")
            continue
        process_file(path, meta)


if __name__ == "__main__":
    main()
