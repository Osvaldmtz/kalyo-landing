#!/usr/bin/env python3
"""Generate batch-2 clinical test articles using the PHQ-2 HTML template."""
from __future__ import annotations

import html as html_lib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
ART_DIR = ROOT / "articulos"
BLOG_DIR = ROOT / "assets" / "blog"
OUT_DIR = Path(__file__).resolve().parent / "output"
STYLE = (Path(__file__).resolve().parent / "_phq2_style.css").read_text(encoding="utf-8")
FONTS_GA = (Path(__file__).resolve().parent / "_phq2_fonts_ga.html").read_text(encoding="utf-8")
FAL_MODEL = "fal-ai/flux/schnell"
TODAY = date.today().isoformat()

ARTICLES = [
    {
        "slug": "phq-9-escala-depresion",
        "test": "PHQ-9",
        "full": "Patient Health Questionnaire-9",
        "domain": "depresión",
        "keyword": "PHQ-9 escala depresión",
        "related": [
            ("/articulos/phq-2-tamizaje-depresion-breve.html", "PHQ-2 tamizaje depresión"),
            ("/articulos/que-es-el-phq-9.html", "¿Qué es el PHQ-9?"),
            ("/articulos/gad-7-escala-ansiedad-generalizada.html", "GAD-7 ansiedad"),
        ],
        "hero_visual": "tablet showing a short depression questionnaire checklist, purple flat design, no readable text",
        "inline_visual": "abstract purple mental health wellness symbols, soft geometric shapes, no text no labels",
        "scoring_headers": ["Puntaje", "Severidad", "Acción clínica sugerida"],
        "scoring_rows": [
            ["0–4", "Mínima / ausente", "Monitoreo según criterio clínico"],
            ["5–9", "Leve", "Psicoeducación y reevaluación"],
            ["10–14", "Moderada", "Evaluación integral y plan de tratamiento"],
            ["15–19", "Moderadamente grave", "Intervención prioritaria"],
            ["20–27", "Grave", "Manejo intensivo y evaluar riesgo"],
        ],
    },
    {
        "slug": "gad-7-escala-ansiedad-generalizada",
        "test": "GAD-7",
        "full": "Generalized Anxiety Disorder-7",
        "domain": "ansiedad generalizada",
        "keyword": "GAD-7 escala ansiedad",
        "related": [
            ("/articulos/gad-2-tamizaje-ansiedad-breve.html", "GAD-2 tamizaje ansiedad"),
            ("/articulos/phq-9-escala-depresion.html", "PHQ-9 depresión"),
            ("/articulos/hads-ansiedad-depresion-hospitalaria.html", "HADS hospitalaria"),
        ],
        "hero_visual": "calm clinical tablet with anxiety screening form icons, lavender purple flat illustration, no text",
        "inline_visual": "abstract purple waves representing calm and tension balance, geometric, no text",
        "scoring_headers": ["Puntaje", "Severidad", "Orientación"],
        "scoring_rows": [
            ["0–4", "Mínima", "Seguimiento habitual"],
            ["5–9", "Leve", "Estrategias de afrontamiento y reevaluación"],
            ["10–14", "Moderada", "Evaluación clínica y plan terapéutico"],
            ["15–21", "Grave", "Intervención prioritaria"],
        ],
    },
    {
        "slug": "pcl-5-estres-postraumatico",
        "test": "PCL-5",
        "full": "PTSD Checklist for DSM-5",
        "domain": "estrés postraumático",
        "keyword": "PCL-5 estrés postraumático",
        "related": [
            ("/articulos/ies-r-impacto-evento.html", "IES-R impacto del evento"),
            ("/articulos/c-ssrs-riesgo-suicida.html", "C-SSRS riesgo suicida"),
            ("/articulos/dts-escala-trauma-davidson.html", "Escala Davidson trauma"),
        ],
        "hero_visual": "supportive therapy scene with soft purple tones, clipboard and calm figure silhouette, flat design, no text",
        "inline_visual": "abstract healing journey path with soft purple shapes, no text no labels",
        "scoring_headers": ["Puntaje total", "Interpretación", "Notas"],
        "scoring_rows": [
            ["0–30", "Síntomas bajos / subumbrales", "Integrar con entrevista clínica"],
            ["31–32", "Zona de corte frecuente", "Evaluar criterios DSM-5"],
            ["33+", "Sugiere TEPT probable", "Evaluación diagnóstica completa"],
        ],
    },
    {
        "slug": "audit-test-alcoholismo",
        "test": "AUDIT",
        "full": "Alcohol Use Disorders Identification Test",
        "domain": "consumo de alcohol",
        "keyword": "AUDIT test alcoholismo",
        "related": [
            ("/articulos/audit-c-consumo-alcohol.html", "AUDIT-C consumo alcohol"),
            ("/articulos/cage-dependencia-alcohol.html", "CAGE dependencia alcohol"),
            ("/articulos/dast-10-abuso-sustancias.html", "DAST-10 sustancias"),
        ],
        "hero_visual": "clinical assessment desk with purple clipboard and subtle alcohol awareness icons, flat illustration, no text",
        "inline_visual": "abstract purple continuum from balance to risk, geometric icons only, no text",
        "scoring_headers": ["Puntaje", "Nivel de riesgo", "Acción sugerida"],
        "scoring_rows": [
            ["0–7", "Bajo", "Psicoeducación breve"],
            ["8–15", "Riesgoso", "Intervención breve"],
            ["16–19", "Alto / dañino", "Evaluación especializada"],
            ["20–40", "Dependencia probable", "Derivación a tratamiento"],
        ],
    },
    {
        "slug": "audit-c-consumo-alcohol",
        "test": "AUDIT-C",
        "full": "AUDIT Consumption (3 ítems)",
        "domain": "consumo de alcohol",
        "keyword": "AUDIT-C consumo alcohol",
        "related": [
            ("/articulos/audit-test-alcoholismo.html", "AUDIT completo"),
            ("/articulos/cage-dependencia-alcohol.html", "CAGE alcohol"),
            ("/articulos/dast-10-abuso-sustancias.html", "DAST-10"),
        ],
        "hero_visual": "short screening card on tablet in purple clinic, flat design, no readable text",
        "inline_visual": "three abstract purple markers representing brief screening steps, no text",
        "scoring_headers": ["Puntaje", "Interpretación habitual", "Siguiente paso"],
        "scoring_rows": [
            ["0–2 (mujeres) / 0–3 (hombres)*", "Bajo riesgo relativo", "Consejo preventivo"],
            ["≥3 / ≥4*", "Tamizaje positivo", "Aplicar AUDIT completo"],
        ],
    },
    {
        "slug": "cage-dependencia-alcohol",
        "test": "CAGE",
        "full": "Cut down, Annoyed, Guilty, Eye-opener",
        "domain": "dependencia al alcohol",
        "keyword": "CAGE dependencia alcohol",
        "related": [
            ("/articulos/audit-test-alcoholismo.html", "AUDIT alcoholismo"),
            ("/articulos/audit-c-consumo-alcohol.html", "AUDIT-C"),
            ("/articulos/dast-10-abuso-sustancias.html", "DAST-10"),
        ],
        "hero_visual": "four soft purple icon cards representing brief alcohol questions, flat design, no letters no text",
        "inline_visual": "abstract purple interview conversation bubbles without words, calm clinical style",
        "scoring_headers": ["Respuestas positivas", "Interpretación", "Acción"],
        "scoring_rows": [
            ["0–1", "Baja sospecha", "Psicoeducación si hay factores de riesgo"],
            ["≥2", "Tamizaje positivo", "Evaluación clínica y AUDIT"],
        ],
    },
    {
        "slug": "isi-indice-severidad-insomnio",
        "test": "ISI",
        "full": "Insomnia Severity Index",
        "domain": "insomnio",
        "keyword": "ISI índice severidad insomnio",
        "related": [
            ("/articulos/psqi-calidad-sueno-pittsburg.html", "PSQI calidad del sueño"),
            ("/articulos/pss-10-escala-estres-percibido.html", "PSS-10 estrés"),
            ("/articulos/gad-7-escala-ansiedad-generalizada.html", "GAD-7 ansiedad"),
        ],
        "hero_visual": "peaceful night bedroom silhouette with soft purple moon and sleep clinic motif, flat design, no text",
        "inline_visual": "abstract crescent and soft waves suggesting sleep quality, purple palette, no text",
        "scoring_headers": ["Puntaje", "Severidad", "Orientación"],
        "scoring_rows": [
            ["0–7", "Sin insomnia clínicamente significativa", "Higiene del sueño"],
            ["8–14", "Insomnio subumbral", "Monitoreo e intervención breve"],
            ["15–21", "Insomnio moderado", "Evaluación y TCC-I / manejo clínico"],
            ["22–28", "Insomnio grave", "Intervención prioritaria"],
        ],
    },
    {
        "slug": "psqi-calidad-sueno-pittsburg",
        "test": "PSQI",
        "full": "Pittsburgh Sleep Quality Index",
        "domain": "calidad del sueño",
        "keyword": "PSQI calidad sueño Pittsburgh",
        "related": [
            ("/articulos/isi-indice-severidad-insomnio.html", "ISI insomnio"),
            ("/articulos/pss-10-escala-estres-percibido.html", "PSS-10"),
            ("/articulos/who-5-bienestar.html", "WHO-5 bienestar"),
        ],
        "hero_visual": "sleep diary notebook and soft purple night icons, flat clinical illustration, no text",
        "inline_visual": "seven abstract purple component blocks representing sleep domains, no labels no text",
        "scoring_headers": ["Puntaje global", "Interpretación", "Nota"],
        "scoring_rows": [
            ["0–5", "Buena calidad de sueño (habitual)", "Confirmar con entrevista"],
            [">5", "Mala calidad de sueño", "Explorar componentes y comorbilidades"],
        ],
    },
    {
        "slug": "pss-10-escala-estres-percibido",
        "test": "PSS-10",
        "full": "Perceived Stress Scale-10",
        "domain": "estrés percibido",
        "keyword": "PSS-10 escala estrés percibido",
        "related": [
            ("/articulos/mbi-burnout-maslach.html", "MBI burnout"),
            ("/articulos/gad-7-escala-ansiedad-generalizada.html", "GAD-7"),
            ("/articulos/who-5-bienestar.html", "WHO-5"),
        ],
        "hero_visual": "balanced scales and soft purple stress relief icons in modern clinic, flat design, no text",
        "inline_visual": "abstract purple tension and release curves, geometric, no text",
        "scoring_headers": ["Rango orientativo*", "Nivel", "Uso clínico"],
        "scoring_rows": [
            ["Bajos", "Estrés percibido bajo", "Prevención y hábitos"],
            ["Medios", "Estrés moderado", "Estrategias de afrontamiento"],
            ["Altos", "Estrés elevado", "Evaluación integral y plan"],
        ],
    },
    {
        "slug": "who-5-bienestar",
        "test": "WHO-5",
        "full": "WHO-Five Well-Being Index",
        "domain": "bienestar psicológico",
        "keyword": "WHO-5 bienestar OMS",
        "related": [
            ("/articulos/pss-10-escala-estres-percibido.html", "PSS-10 estrés"),
            ("/articulos/escala-autoestima-rosenberg.html", "Rosenberg autoestima"),
            ("/articulos/cd-risc-resiliencia.html", "CD-RISC resiliencia"),
        ],
        "hero_visual": "bright purple wellness sun and calm figure silhouette, optimistic flat design, no text",
        "inline_visual": "five soft purple ascending bars as abstract wellbeing, no numbers no text",
        "scoring_headers": ["Puntaje bruto (0–25)", "Interpretación frecuente", "Acción"],
        "scoring_rows": [
            ["≥13", "Bienestar relativo preservado", "Promoción de salud"],
            ["≤12", "Posible malestar / riesgo", "Evaluar depresión u otros factores"],
        ],
    },
    {
        "slug": "escala-autoestima-rosenberg",
        "test": "Rosenberg",
        "full": "Rosenberg Self-Esteem Scale (RSES)",
        "domain": "autoestima",
        "keyword": "escala autoestima Rosenberg",
        "related": [
            ("/articulos/who-5-bienestar.html", "WHO-5 bienestar"),
            ("/articulos/bhs-desesperanza-beck.html", "BHS desesperanza"),
            ("/articulos/cd-risc-resiliencia.html", "CD-RISC"),
        ],
        "hero_visual": "mirror silhouette and soft purple self-compassion symbols, flat clinical style, no text",
        "inline_visual": "abstract purple balance of self view, geometric hearts without text",
        "scoring_headers": ["Puntaje (10–40)*", "Nivel orientativo", "Uso"],
        "scoring_rows": [
            ["30–40", "Autoestima alta", "Fortalecer recursos"],
            ["26–29", "Autoestima media", "Trabajo preventivo"],
            ["<26", "Autoestima baja", "Evaluación e intervención"],
        ],
    },
    {
        "slug": "hads-ansiedad-depresion-hospitalaria",
        "test": "HADS",
        "full": "Hospital Anxiety and Depression Scale",
        "domain": "ansiedad y depresión hospitalaria",
        "keyword": "HADS ansiedad depresión hospitalaria",
        "related": [
            ("/articulos/gad-7-escala-ansiedad-generalizada.html", "GAD-7"),
            ("/articulos/phq-9-escala-depresion.html", "PHQ-9"),
            ("/articulos/pss-10-escala-estres-percibido.html", "PSS-10"),
        ],
        "hero_visual": "hospital corridor soft purple tones with calm assessment clipboard, flat design, no text",
        "inline_visual": "two abstract purple panels representing anxiety and depression subscales, no text",
        "scoring_headers": ["Subescala (0–21)", "Interpretación", "Nota"],
        "scoring_rows": [
            ["0–7", "Normal / no caso", "Seguimiento contextual"],
            ["8–10", "Caso dudoso", "Reevaluación clínica"],
            ["11–21", "Caso probable", "Evaluación e intervención"],
        ],
    },
    {
        "slug": "ies-r-impacto-evento",
        "test": "IES-R",
        "full": "Impact of Event Scale-Revised",
        "domain": "impacto de eventos traumáticos",
        "keyword": "IES-R impacto del evento",
        "related": [
            ("/articulos/pcl-5-estres-postraumatico.html", "PCL-5 TEPT"),
            ("/articulos/c-ssrs-riesgo-suicida.html", "C-SSRS"),
            ("/articulos/dts-escala-trauma-davidson.html", "Davidson trauma"),
        ],
        "hero_visual": "gentle memory processing visual with soft purple threads, trauma-informed flat design, no text",
        "inline_visual": "three abstract purple clusters for intrusion avoidance hyperarousal, no labels",
        "scoring_headers": ["Uso del puntaje", "Enfoque", "Precaución"],
        "scoring_rows": [
            ["Total y subescalas", "Monitoreo de sintomatología", "No diagnostica solo"],
            ["Cambio en el tiempo", "Respuesta a intervención", "Integrar entrevista"],
        ],
    },
    {
        "slug": "c-ssrs-riesgo-suicida",
        "test": "C-SSRS",
        "full": "Columbia-Suicide Severity Rating Scale",
        "domain": "riesgo suicida",
        "keyword": "C-SSRS riesgo suicida",
        "related": [
            ("/articulos/sbq-r-comportamiento-suicida.html", "SBQ-R"),
            ("/articulos/bhs-desesperanza-beck.html", "BHS Beck"),
            ("/articulos/phq-9-escala-depresion.html", "PHQ-9"),
        ],
        "hero_visual": "protective hands and soft purple safety net illustration, clinical and hopeful, no text",
        "inline_visual": "abstract purple pathway from risk to support, geometric, no text no icons with letters",
        "scoring_headers": ["Dominio", "Qué evalúa", "Uso clínico"],
        "scoring_rows": [
            ["Ideación", "Severidad e intensidad", "Estratificar riesgo"],
            ["Conducta", "Intentos, preparativos, ABISI", "Plan de seguridad"],
        ],
    },
    {
        "slug": "bhs-desesperanza-beck",
        "test": "BHS",
        "full": "Beck Hopelessness Scale",
        "domain": "desesperanza",
        "keyword": "BHS desesperanza Beck",
        "related": [
            ("/articulos/c-ssrs-riesgo-suicida.html", "C-SSRS"),
            ("/articulos/sbq-r-comportamiento-suicida.html", "SBQ-R"),
            ("/articulos/phq-9-escala-depresion.html", "PHQ-9"),
        ],
        "hero_visual": "soft light breaking through purple clouds, hope metaphor, flat design, no text",
        "inline_visual": "abstract gradient from dark purple to light lavender, no text",
        "scoring_headers": ["Puntaje (0–20)", "Nivel orientativo", "Acción"],
        "scoring_rows": [
            ["0–3", "Mínima / leve", "Monitoreo"],
            ["4–8", "Leve a moderada", "Explorar factores"],
            ["9–14", "Moderada", "Evaluación de riesgo"],
            ["15–20", "Grave", "Intervención prioritaria"],
        ],
    },
    {
        "slug": "sbq-r-comportamiento-suicida",
        "test": "SBQ-R",
        "full": "Suicidal Behaviors Questionnaire-Revised",
        "domain": "comportamiento suicida",
        "keyword": "SBQ-R comportamiento suicida",
        "related": [
            ("/articulos/c-ssrs-riesgo-suicida.html", "C-SSRS"),
            ("/articulos/bhs-desesperanza-beck.html", "BHS"),
            ("/articulos/phq-9-escala-depresion.html", "PHQ-9"),
        ],
        "hero_visual": "supportive clinical conversation silhouette in purple tones, safety-focused flat design, no text",
        "inline_visual": "four abstract purple checkpoints in a gentle arc, no numbers no text",
        "scoring_headers": ["Puntaje total", "Interpretación frecuente*", "Nota"],
        "scoring_rows": [
            ["<7 adultos / umbrales según población", "Menor riesgo relativo", "No excluye riesgo"],
            ["≥7 (adultos, corte habitual)", "Mayor riesgo / positivo", "Evaluación completa"],
        ],
    },
    {
        "slug": "mbi-burnout-maslach",
        "test": "MBI",
        "full": "Maslach Burnout Inventory",
        "domain": "burnout laboral",
        "keyword": "MBI burnout Maslach",
        "related": [
            ("/articulos/pss-10-escala-estres-percibido.html", "PSS-10"),
            ("/articulos/who-5-bienestar.html", "WHO-5"),
            ("/articulos/inventario-burnout-mbi.html", "Inventario burnout MBI"),
        ],
        "hero_visual": "tired professional silhouette recovering with purple calm energy, workplace wellness flat design, no text",
        "inline_visual": "three abstract purple pillars for exhaustion cynicism efficacy, no labels",
        "scoring_headers": ["Dimensión", "Qué mide", "Uso"],
        "scoring_rows": [
            ["Agotamiento emocional", "Cansancio / sobrecarga", "Interpretar por baremo"],
            ["Despersonalización / cinismo", "Distanciamiento", "Contexto organizacional"],
            ["Realización personal", "Eficacia percibida", "No usar un solo total"],
        ],
    },
    {
        "slug": "cd-risc-resiliencia",
        "test": "CD-RISC",
        "full": "Connor-Davidson Resilience Scale",
        "domain": "resiliencia",
        "keyword": "CD-RISC resiliencia",
        "related": [
            ("/articulos/who-5-bienestar.html", "WHO-5"),
            ("/articulos/escala-autoestima-rosenberg.html", "Rosenberg"),
            ("/articulos/pss-10-escala-estres-percibido.html", "PSS-10"),
        ],
        "hero_visual": "growing plant through purple geometric rocks, resilience metaphor, flat design, no text",
        "inline_visual": "abstract purple upward spiral of strength, no text",
        "scoring_headers": ["Versión", "Ítems", "Uso clínico"],
        "scoring_rows": [
            ["CD-RISC-25", "25", "Perfil amplio de resiliencia"],
            ["CD-RISC-10", "10", "Screening / seguimiento breve"],
            ["CD-RISC-2", "2", "Tamizaje ultracorto"],
        ],
    },
    {
        "slug": "dast-10-abuso-sustancias",
        "test": "DAST-10",
        "full": "Drug Abuse Screening Test-10",
        "domain": "abuso de sustancias",
        "keyword": "DAST-10 abuso sustancias",
        "related": [
            ("/articulos/audit-test-alcoholismo.html", "AUDIT"),
            ("/articulos/audit-c-consumo-alcohol.html", "AUDIT-C"),
            ("/articulos/cage-dependencia-alcohol.html", "CAGE"),
        ],
        "hero_visual": "clinical screening folder with purple substance awareness icons, flat design, no text no logos",
        "inline_visual": "abstract purple risk ladder without numbers or words",
        "scoring_headers": ["Puntaje", "Nivel de problema", "Acción sugerida"],
        "scoring_rows": [
            ["0", "Ninguno reportado", "Prevención"],
            ["1–2", "Bajo", "Monitoreo / consejo breve"],
            ["3–5", "Moderado", "Evaluación adicional"],
            ["6–8", "Sustancial", "Tratamiento intensivo"],
            ["9–10", "Severo", "Derivación especializada"],
        ],
    },
    {
        "slug": "wurs-tdah-adultos",
        "test": "WURS",
        "full": "Wender Utah Rating Scale",
        "domain": "TDAH en adultos (síntomas retrospectivos)",
        "keyword": "WURS TDAH adultos",
        "related": [
            ("/articulos/asrs-tdah-adultos.html", "ASRS TDAH adultos"),
            ("/articulos/tdah-adultos-sintomas-diagnostico.html", "TDAH adultos síntomas"),
            ("/articulos/snap-iv-tdah-ninos.html", "SNAP-IV niños"),
        ],
        "hero_visual": "adult reviewing childhood memory timeline with purple clinical notes, flat design, no text",
        "inline_visual": "abstract purple past-to-present timeline shapes, no text no dates",
        "scoring_headers": ["Versión común", "Enfoque", "Uso"],
        "scoring_rows": [
            ["WURS-25", "Ítems más discriminativos", "Apoyo retrospectivo"],
            ["WURS-61", "Forma extendida", "Investigación / clínica amplia"],
        ],
    },
]


def load_env() -> None:
    env_path = ROOT / ".env.local"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def fit_meta(text: str, lo: int = 140, hi: int = 155) -> str:
    text = re.sub(r"\s+", " ", text).strip().replace('"', "")
    if not text.endswith("."):
        text += "."
    if lo <= len(text) <= hi:
        return text
    if len(text) > hi:
        base = text[:-1] if text.endswith(".") else text
        while len(base) + 1 > hi and " " in base:
            base = base.rsplit(" ", 1)[0].rstrip(" ,;:")
        return (base + ".")[:hi]
    # expand
    extras = [
        " Guía clínica para psicólogos.",
        " Uso e interpretación en consulta.",
        " Orientación para práctica clínica.",
    ]
    for e in extras:
        t = text[:-1] + e if text.endswith(".") else text + e
        t = re.sub(r"\s+", " ", t).strip()
        if not t.endswith("."):
            t += "."
        if lo <= len(t) <= hi:
            return t
        if len(t) > hi:
            return t[: hi - 1].rsplit(" ", 1)[0] + "."
    return text[:hi]


def scoring_table(meta: dict) -> str:
    heads = "".join(f"<th>{html_lib.escape(h)}</th>" for h in meta["scoring_headers"])
    rows = []
    for row in meta["scoring_rows"]:
        cells = "".join(f"<td>{html_lib.escape(c)}</td>" for c in row)
        rows.append(f"<tr>{cells}</tr>")
    note = (
        "<p><em>Los puntos de corte pueden variar según población, versión y baremo local. "
        "Interprete siempre junto a la entrevista clínica.</em></p>"
    )
    return (
        f'<table class="scoring-table"><thead><tr>{heads}</tr></thead>'
        f"<tbody>{''.join(rows)}</tbody></table>{note}"
    )


SECTION_TITLES = [
    "¿Qué es {test}?",
    "Estructura e ítems del {test}",
    "Interpretación clínica de puntajes",
    "Validación psicométrica y evidencia",
    "Aplicaciones clínicas y contextos de uso",
    "Limitaciones y consideraciones importantes",
    "Criterios para derivación o profundización",
    "Comparación con otros instrumentos",
    "Recomendaciones para profesionales de la salud",
]


def generate_spec_with_llm(meta: dict, client) -> dict:
    prompt = {
        "slug": meta["slug"],
        "test": meta["test"],
        "full_name": meta["full"],
        "domain": meta["domain"],
        "keyword": meta["keyword"],
        "section_titles": [t.format(test=meta["test"]) for t in SECTION_TITLES],
        "instructions": (
            "Escribe contenido clínico en español LATAM para psicólogos. "
            "Devuelve JSON con keys: title (<=60 chars + ' | Kalyo'), h1, description (140-155 chars con punto final), "
            "meta_keywords (string), intro (2-3 frases), "
            "sections: array de 9 objetos {h2, paragraphs: [2-3 strings]}, "
            "faqs: 7 objetos {q, a}, "
            "references: 4 objetos {label, url} preferible PubMed/OMS/APA cuando aplique, "
            "cta_h2, cta_p, hero_alt, inline_alt. "
            "Sin inventar estadísticas imposibles; usa rangos conocidos del instrumento. "
            "No uses comillas dobles dentro de strings (usa comillas tipográficas o evita)."
        ),
    }
    msg = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=8000,
        system="Eres un redactor clínico SEO para Kalyo. Responde SOLO JSON válido.",
        messages=[{"role": "user", "content": json.dumps(prompt, ensure_ascii=False)}],
    )
    text = msg.content[0].text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\n?", "", text)
        text = re.sub(r"\n?```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{[\s\S]*\}", text)
        if not m:
            raise
        return json.loads(m.group(0))


def paragraphs_html(paragraphs: list[str]) -> str:
    return "\n".join(f"    <p>\n      {p}\n    </p>" for p in paragraphs)


def render_article(meta: dict, spec: dict) -> str:
    slug = meta["slug"]
    url = f"https://kalyo.io/articulos/{slug}.html"
    title = spec["title"]
    if "Kalyo" not in title:
        title = title.rstrip(" |") + " | Kalyo"
    desc = fit_meta(spec["description"])
    h1 = spec["h1"]
    intro = spec["intro"]
    keywords = spec.get("meta_keywords") or meta["keyword"]
    pdf_href = f"/assets/{slug}-espanol.pdf"
    pdf_label = f"Descargar {meta['test']} en español (PDF gratuito)"

    faqs = spec["faqs"][:8]
    if len(faqs) < 6:
        raise ValueError(f"{slug}: need >=6 faqs, got {len(faqs)}")

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f["q"],
                "acceptedAnswer": {"@type": "Answer", "text": f["a"]},
            }
            for f in faqs
        ],
    }
    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "image": f"https://kalyo.io/assets/blog/{slug}-hero.jpg",
        "author": {"@type": "Organization", "name": "Kalyo", "url": "https://kalyo.io"},
        "publisher": {
            "@type": "Organization",
            "name": "Kalyo",
            "logo": {"@type": "ImageObject", "url": "https://kalyo.io/assets/logo.png"},
        },
        "datePublished": "2026-10-09",
        "dateModified": TODAY,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
    }

    sections = spec["sections"]
    if len(sections) < 9:
        raise ValueError(f"{slug}: need 9 sections, got {len(sections)}")

    body_sections = []
    for i, sec in enumerate(sections[:9]):
        h2 = sec["h2"]
        paras = sec.get("paragraphs") or [sec.get("html", "")]
        if isinstance(paras, str):
            paras = [paras]
        body_sections.append(f"    <h2>{h2}</h2>\n{paragraphs_html(paras)}")
        if i == 1:
            # structure section: add scoring table + inline image
            body_sections.append("    " + scoring_table(meta).replace("\n", "\n    "))
            body_sections.append(
                f'''    <figure class="article-inline-img">
      <picture>
      <source srcset="/assets/blog/{slug}-inline.webp" type="image/webp">
      <img src="/assets/blog/{slug}-inline.jpg" alt="{html_lib.escape(spec.get('inline_alt', h1))}" width="800" height="450" loading="lazy" title="{html_lib.escape(spec.get('inline_alt', h1))}">
    </picture>
    </figure>'''
            )

    faq_html = ["    <h2>Preguntas frecuentes</h2>"]
    for f in faqs:
        faq_html.append(f"    <h3>{f['q']}</h3>\n    <p>\n      {f['a']}\n    </p>")

    related_items = []
    for href, label in meta["related"]:
        related_items.append(
            f'<li><a href="{href}" style="display:block;padding:14px 16px;background:#F8F7FF;border:1px solid #EDE7F6;border-radius:8px;text-decoration:none;color:#7C3DE3;font-size:14px;font-weight:500;line-height:1.4">{label}</a></li>'
        )

    refs = []
    for r in spec.get("references", [])[:6]:
        if isinstance(r, dict):
            label = r.get("label") or "Ver fuente"
            href = r.get("url") or "#"
            refs.append(
                f'<li><a href="{html_lib.escape(href)}" rel="nofollow noopener noreferrer" target="_blank">{html_lib.escape(label)}</a></li>'
            )
        else:
            refs.append(f"<li>{r}</li>")

    cta_h2 = spec.get("cta_h2") or f"Accede al Test {meta['test']} en Kalyo"
    cta_p = (
        spec.get("cta_p")
        or f"Administra, califica e interpreta {meta['test']} de forma digital en Kalyo."
    )

    def esc_attr(s: str) -> str:
        return html_lib.escape(s, quote=True)

    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <title>{esc_attr(title)}</title>
  <meta name="description" content="{esc_attr(desc)}">
  <meta name="keywords" content="{esc_attr(keywords)}">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="es" href="{url}">

  <link rel="preload" as="image" href="/assets/blog/{slug}-hero.webp" type="image/webp">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{esc_attr(title)}">
  <meta property="og:description" content="{esc_attr(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="https://kalyo.io/assets/blog/{slug}-hero.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="Kalyo">
  <meta property="og:locale" content="es_419">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc_attr(title)}">
  <meta name="twitter:description" content="{esc_attr(desc)}">
  <meta name="twitter:image" content="https://kalyo.io/assets/blog/{slug}-hero.jpg">

  <script type="application/ld+json">
{json.dumps(article_schema, ensure_ascii=False, indent=2)}
</script>
  <script type="application/ld+json">
{json.dumps(faq_schema, ensure_ascii=False, indent=2)}
</script>
<!-- Fonts -->
  <link rel="stylesheet" href="/assets/blog.css">
  <link rel="preload" href="/assets/fonts/outfit-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/playfair-latin.woff2" as="font" type="font/woff2" crossorigin>
<style>
{STYLE}
</style>
{FONTS_GA}
</head>
<body>

  <header class="header">
    <div class="header-inner">
      <a href="/" class="header-logo">Kalyo</a>
      <a href="https://app.kalyo.io/login" class="header-btn">Iniciar sesi&oacute;n</a>
    </div>
  </header>

  <article class="article-wrapper">
    <div class="article-hero-img">
      <picture>
      <source srcset="/assets/blog/{slug}-hero.webp" type="image/webp">
      <img src="/assets/blog/{slug}-hero.jpg" alt="{esc_attr(spec.get('hero_alt', h1))}" width="1200" height="630" loading="eager" fetchpriority="high" title="{esc_attr(spec.get('hero_alt', h1))}">
    </picture>
    </div>
    <p class="article-meta">Psicometr&iacute;a cl&iacute;nica &middot; Actualizaci&oacute;n 2026</p>

    <h1>{h1}</h1>


    <p class="article-quick-actions">
      <a href="{pdf_href}" download="{meta['test']}-espanol-Kalyo.pdf" class="btn-solid">{pdf_label}</a>
    </p>

    <div class="article-intro">{intro}</div>

{chr(10).join(body_sections)}

{chr(10).join(faq_html)}

    <div class="cta-box">
      <h2>{cta_h2}</h2>
      <p>{cta_p}</p>
      <a href="https://app.kalyo.io/login?utm_source=blog&utm_medium=article&utm_campaign={slug}" class="cta-btn">Prueba gratis 7 d&iacute;as &rarr;</a>
    </div>
  <section style="margin-top:48px;padding-top:32px;border-top:1px solid #EDE7F6">
    <h2 style="font-size:18px;font-weight:700;color:#1A1A2E;margin-bottom:20px">Art&iacute;culos relacionados</h2>
    <ul style="list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px">
      {chr(10).join('      ' + x for x in related_items)}
    </ul>
  </section>
  
  <section class="article-references">
  <h2>Referencias</h2>
  <ul>
    {chr(10).join('    ' + x for x in refs)}
  </ul>
</section>

  </article>

  <footer class="footer">
    <p>&copy; 2026 Endeavor Ventures LLC &middot; <a href="https://kalyo.io">kalyo.io</a></p>
  </footer>

</body>
</html>
'''


def fal_generate(prompt: str, fal_key: str, image_size, retries: int = 3) -> bytes:
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            resp = requests.post(
                f"https://queue.fal.run/{FAL_MODEL}",
                headers={"Authorization": f"Key {fal_key}", "Content-Type": "application/json"},
                json={
                    "prompt": prompt,
                    "image_size": image_size,
                    "num_images": 1,
                    "num_inference_steps": 4,
                    "output_format": "jpeg",
                },
                timeout=90,
            )
            resp.raise_for_status()
            data0 = resp.json()
            poll_url = data0.get("status_url") or data0.get("response_url")
            result_url = data0.get("response_url") or poll_url
            if data0.get("images"):
                url = data0["images"][0]["url"]
                img = requests.get(url, timeout=120)
                img.raise_for_status()
                return img.content
            if not poll_url:
                raise RuntimeError(f"No poll URL: {data0}")
            for _ in range(40):
                time.sleep(2)
                poll = requests.get(poll_url, headers={"Authorization": f"Key {fal_key}"}, timeout=60)
                if poll.status_code == 400:
                    time.sleep(2)
                    continue
                poll.raise_for_status()
                data = poll.json()
                if data.get("images"):
                    url = data["images"][0]["url"]
                    img = requests.get(url, timeout=120)
                    img.raise_for_status()
                    return img.content
                status = data.get("status")
                if status in ("FAILED", "ERROR"):
                    raise RuntimeError(data)
                if status == "COMPLETED":
                    final = requests.get(result_url, headers={"Authorization": f"Key {fal_key}"}, timeout=60)
                    final.raise_for_status()
                    final_data = final.json()
                    if final_data.get("images"):
                        url = final_data["images"][0]["url"]
                        img = requests.get(url, timeout=120)
                        img.raise_for_status()
                        return img.content
                    raise RuntimeError(f"Completed but no images: {final_data}")
            raise TimeoutError("FAL timeout")
        except Exception as exc:
            last_err = exc
            print(f"    FAL retry {attempt+1}: {exc}", file=sys.stderr)
            time.sleep(2)
    raise last_err or RuntimeError("FAL failed")


def resize_and_save(jpeg: bytes, size: tuple[int, int], jpg_path: Path, webp_path: Path) -> None:
    from PIL import Image
    import io

    im = Image.open(io.BytesIO(jpeg)).convert("RGB")
    im = im.resize(size, Image.Resampling.LANCZOS)
    im.save(jpg_path, "JPEG", quality=88, optimize=True)
    im.save(webp_path, "WEBP", quality=82, method=6)


def hero_prompt(meta: dict) -> str:
    return (
        f"Kalyo brand flat vector illustration, soft purple and lavender palette (#7C3DE3), "
        f"cream background accents, minimalist clinical psychology aesthetic, "
        f"{meta['hero_visual']}, no text, no letters, no numbers, no watermarks, no logos, "
        f"clean composition for blog hero image"
    )


def inline_prompt(meta: dict) -> str:
    return (
        f"Kalyo brand flat vector illustration, purple lavender palette, "
        f"{meta['inline_visual']}, absolutely no text, no labels, no numbers, no watermarks, "
        f"abstract clinical wellness concept, clean blog inline image"
    )


def generate_images(meta: dict, fal_key: str, force: bool = False) -> None:
    BLOG_DIR.mkdir(parents=True, exist_ok=True)
    jobs = [
        ("hero", hero_prompt(meta), (1200, 630), {"width": 1200, "height": 630}),
        ("inline", inline_prompt(meta), (800, 450), {"width": 800, "height": 450}),
    ]
    for kind, prompt, size, fal_size in jobs:
        jpg = BLOG_DIR / f"{meta['slug']}-{kind}.jpg"
        webp = BLOG_DIR / f"{meta['slug']}-{kind}.webp"
        if jpg.exists() and webp.exists() and not force:
            # ensure correct dimensions
            from PIL import Image

            im = Image.open(jpg)
            if im.size == size and not force:
                print(f"    skip existing {kind} {im.size}")
                continue
        print(f"    generating {kind}...")
        jpeg = fal_generate(prompt, fal_key, image_size=fal_size)
        resize_and_save(jpeg, size, jpg, webp)
        print(f"    OK {jpg.name} {size[0]}x{size[1]}")


def main() -> None:
    load_env()
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    specs_path = OUT_DIR / "batch2-clinical-specs.json"

    if mode in ("content", "all"):
        from anthropic import Anthropic

        client = Anthropic()
        specs = {}
        if specs_path.exists():
            specs = json.loads(specs_path.read_text(encoding="utf-8"))
        for i, meta in enumerate(ARTICLES, 1):
            slug = meta["slug"]
            if slug in specs and mode == "all":
                print(f"[{i}/20] content exists: {slug}")
                continue
            print(f"[{i}/20] generating content: {slug}")
            for attempt in range(3):
                try:
                    spec = generate_spec_with_llm(meta, client)
                    # normalize
                    spec["description"] = fit_meta(spec["description"])
                    specs[slug] = spec
                    specs_path.write_text(json.dumps(specs, ensure_ascii=False, indent=2), encoding="utf-8")
                    print(f"  OK meta_len={len(spec['description'])} faqs={len(spec['faqs'])} sections={len(spec['sections'])}")
                    break
                except Exception as e:
                    print(f"  attempt {attempt+1} failed: {e}")
                    time.sleep(1.5)
            else:
                raise RuntimeError(f"Failed content for {slug}")
            time.sleep(0.4)

    if mode in ("html", "all"):
        specs = json.loads(specs_path.read_text(encoding="utf-8"))
        for i, meta in enumerate(ARTICLES, 1):
            slug = meta["slug"]
            print(f"[{i}/20] render HTML: {slug}")
            html_out = render_article(meta, specs[slug])
            path = ART_DIR / f"{slug}.html"
            path.write_text(html_out, encoding="utf-8")
            print(f"  wrote {path.relative_to(ROOT)} ({len(html_out)} bytes)")

    if mode in ("images", "all"):
        fal_key = os.environ.get("FAL_KEY")
        if not fal_key:
            raise SystemExit("FAL_KEY missing")
        force = "--force" in sys.argv
        for i, meta in enumerate(ARTICLES, 1):
            print(f"[{i}/20] images: {meta['slug']}")
            generate_images(meta, fal_key, force=force)

    if mode in ("validate", "all"):
        specs = json.loads(specs_path.read_text(encoding="utf-8"))
        errors = []
        for meta in ARTICLES:
            slug = meta["slug"]
            path = ART_DIR / f"{slug}.html"
            if not path.exists():
                errors.append(f"missing html {slug}")
                continue
            text = path.read_text(encoding="utf-8")
            m = re.search(r'<meta name="description" content="([^"]*)"', text)
            desc = html_lib.unescape(m.group(1)) if m else ""
            if not (140 <= len(desc) <= 155) or not desc.endswith("."):
                errors.append(f"meta bad {slug} len={len(desc)}")
            for kind, size in [("hero", (1200, 630)), ("inline", (800, 450))]:
                jpg = BLOG_DIR / f"{slug}-{kind}.jpg"
                webp = BLOG_DIR / f"{slug}-{kind}.webp"
                if not jpg.exists() or not webp.exists():
                    errors.append(f"missing image {slug} {kind}")
                    continue
                from PIL import Image

                im = Image.open(jpg)
                if im.size != size:
                    errors.append(f"size {slug} {kind} {im.size} != {size}")
            if "FAQPage" not in text:
                errors.append(f"no FAQPage {slug}")
            if f"/assets/{slug}-espanol.pdf" not in text:
                errors.append(f"no pdf slot {slug}")
            if text.count("<h2") < 11:
                errors.append(f"few h2 {slug} count={text.count('<h2')}")
        if errors:
            print("VALIDATION ERRORS:")
            for e in errors:
                print(" -", e)
            raise SystemExit(1)
        print("VALIDATION OK: 20 articles")


if __name__ == "__main__":
    main()
