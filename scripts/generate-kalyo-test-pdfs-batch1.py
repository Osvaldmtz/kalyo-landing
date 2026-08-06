#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Kalyo-branded clinical test PDFs (batch 1) matching phq9-escala-depresion-espanol.pdf style."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
LOGO = ASSETS / "logo-120.png"

PURPLE = colors.HexColor("#7C3DE3")
PURPLE_DARK = colors.HexColor("#5B21B6")
PURPLE_LIGHT = colors.HexColor("#F8F7FF")
INK = colors.HexColor("#1A1A2E")
INK_MUTED = colors.HexColor("#64748B")

LIKERT_4 = ["Para nada (0)", "Varios días (1)", "Más de la mitad (2)", "Casi todos los días (3)"]
LIKERT_4_SHORT = ["0", "1", "2", "3"]


def build_styles():
    base = getSampleStyleSheet()
    return {
        "header_brand": ParagraphStyle(
            "header_brand",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=11,
            textColor=PURPLE,
            leading=14,
        ),
        "header_tag": ParagraphStyle(
            "header_tag",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            textColor=INK_MUTED,
            leading=12,
        ),
        "title": ParagraphStyle(
            "title",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=18,
            textColor=INK,
            spaceAfter=4,
            leading=22,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=11,
            textColor=INK_MUTED,
            spaceAfter=12,
            leading=14,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            textColor=PURPLE_DARK,
            spaceBefore=10,
            spaceAfter=6,
            leading=15,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            textColor=INK,
            leading=13,
            spaceAfter=6,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            textColor=INK_MUTED,
            leading=11,
        ),
        "cta": ParagraphStyle(
            "cta",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.5,
            textColor=PURPLE,
            alignment=TA_CENTER,
            spaceBefore=8,
            spaceAfter=4,
        ),
        "cell": ParagraphStyle(
            "cell",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            textColor=INK,
            leading=10,
        ),
        "cell_hdr": ParagraphStyle(
            "cell_hdr",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8,
            textColor=colors.white,
            leading=10,
        ),
    }


def kalyo_header(styles) -> list:
    logo_w = 0.45 * inch
    if LOGO.exists():
        img = Image(str(LOGO), width=logo_w, height=logo_w)
        brand = Paragraph("<b>Kalyo</b> · kalyo.io", styles["header_brand"])
        tag = Paragraph("Recurso clínico gratuito", styles["header_tag"])
        inner = Table(
            [[img, [brand, tag]]],
            colWidths=[logo_w + 4, 5.8 * inch],
        )
        inner.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]
            )
        )
    else:
        inner = Paragraph(
            "<b>Kalyo</b> · kalyo.io · Recurso clínico gratuito",
            styles["header_brand"],
        )
    band = Table([[inner]], colWidths=[6.5 * inch])
    band.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PURPLE_LIGHT),
                ("BOX", (0, 0), (-1, -1), 0.5, PURPLE),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ]
        )
    )
    return [band, Spacer(1, 0.15 * inch)]


def items_table(items: list[str], scale_headers: list[str] | None = None) -> Table:
    styles = build_styles()
    headers = scale_headers or LIKERT_4_SHORT
    data = [["#", "Ítem / Pregunta"] + headers]
    for i, item in enumerate(items, 1):
        row = [str(i), Paragraph(item, styles["cell"])] + ["☐"] * len(headers)
        data.append(row)
    col_widths = [0.35 * inch, 3.55 * inch] + [0.45 * inch] * len(headers)
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PURPLE),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#E2E8F0")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFAFA")]),
            ]
        )
    )
    return t


def interp_table(headers: list[str], rows: list[list[str]]) -> Table:
    data = [headers] + rows
    t = Table(data, colWidths=[1.3 * inch, 1.5 * inch, 3.4 * inch])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PURPLE),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#E2E8F0")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFAFA")]),
            ]
        )
    )
    return t


def footer_block(styles, cta_text: str, reference: str) -> list:
    return [
        Spacer(1, 0.12 * inch),
        Paragraph(cta_text, styles["cta"]),
        Spacer(1, 0.08 * inch),
        Paragraph(reference, styles["small"]),
        Paragraph(
            "© Kalyo — kalyo.io | Recurso de uso clínico libre. No sustituye evaluación profesional.",
            styles["small"],
        ),
    ]


def write_pdf(filename: str, story: list) -> Path:
    out = ASSETS / filename
    doc = SimpleDocTemplate(
        str(out),
        pagesize=letter,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        title=filename,
    )
    doc.build(story)
    return out


def gen_phq2():
    s = build_styles()
    items = [
        "Durante las últimas 2 semanas, ¿ha sentido poco interés o placer en hacer las cosas?",
        "Durante las últimas 2 semanas, ¿se ha sentido decaído(a), deprimido(a) o sin esperanzas?",
    ]
    story = kalyo_header(s)
    story += [
        Paragraph("PHQ-2 en Español", s["title"]),
        Paragraph("Patient Health Questionnaire-2 — Tamizaje breve de depresión", s["subtitle"]),
        Paragraph("Instrucciones de aplicación", s["h2"]),
        Paragraph(
            "Autoreporte. Indique con qué frecuencia le han molestado los problemas durante las <b>últimas 2 semanas</b>. "
            "Tiempo estimado: menos de 1 minuto. Puede administrarse en papel, digital o de forma verbal en atención primaria.",
            s["body"],
        ),
        Paragraph("Escala de respuesta: " + " · ".join(LIKERT_4), s["body"]),
        Spacer(1, 0.08 * inch),
        items_table(items),
        Spacer(1, 0.1 * inch),
        Paragraph("<b>PUNTAJE TOTAL:</b> _____ / 6", s["body"]),
        Paragraph("Interpretación del puntaje", s["h2"]),
        interp_table(
            ["Puntaje", "Resultado", "Acción sugerida"],
            [
                ["0 – 2", "Negativo", "Sin intervención específica; monitoreo rutinario"],
                ["≥ 3", "Positivo (tamizaje)", "Administrar PHQ-9 completo o entrevista clínica"],
            ],
        ),
    ]
    story += footer_block(
        s,
        "Aplica el PHQ-2 y registra resultados en el expediente con Kalyo — kalyo.io",
        "Kroenke K, Spitzer RL, Williams JB. The PHQ-2. Med Care. 2003;41(11):1284-1292. Instrumento de dominio público.",
    )
    return write_pdf("phq2-tamizaje-depresion-espanol.pdf", story)


def gen_gad2():
    s = build_styles()
    items = [
        "Sentirse nervioso(a), ansioso(a) o muy alterado(a)",
        "No poder dejar de preocuparse o no poder controlar la preocupación",
    ]
    story = kalyo_header(s)
    story += [
        Paragraph("GAD-2 en Español", s["title"]),
        Paragraph("Generalized Anxiety Disorder-2 — Tamizaje breve de ansiedad", s["subtitle"]),
        Paragraph("Instrucciones de aplicación", s["h2"]),
        Paragraph(
            "Autoreporte sobre las <b>últimas 2 semanas</b>. Útil en atención primaria cuando el tiempo es limitado. "
            "Un puntaje ≥ 3 sugiere aplicar GAD-7 o exploración clínica de trastorno de ansiedad generalizada.",
            s["body"],
        ),
        Paragraph("Escala de respuesta: " + " · ".join(LIKERT_4), s["body"]),
        Spacer(1, 0.08 * inch),
        items_table(items),
        Spacer(1, 0.1 * inch),
        Paragraph("<b>PUNTAJE TOTAL:</b> _____ / 6", s["body"]),
        Paragraph("Interpretación del puntaje", s["h2"]),
        interp_table(
            ["Puntaje", "Resultado", "Acción sugerida"],
            [
                ["0 – 2", "Negativo", "Sin tamizaje positivo; reevaluar si cambia el cuadro"],
                ["≥ 3", "Positivo", "Confirmar con GAD-7, entrevista clínica o derivación"],
            ],
        ),
    ]
    story += footer_block(
        s,
        "Registra tamizajes de ansiedad en tu consulta con Kalyo — kalyo.io",
        "Spitzer RL, Kroenke K, Williams JBW, Löwe B. A brief measure for assessing GAD: the GAD-7. Arch Intern Med. 2006.",
    )
    return write_pdf("gad2-tamizaje-ansiedad-espanol.pdf", story)


def gen_bdi():
    s = build_styles()
    items = [
        "Tristeza",
        "Pesimismo",
        "Sentimiento de fracaso",
        "Pérdida de placer (anhedonia)",
        "Sentimientos de culpa",
        "Sentimientos de castigo",
        "Decepción con uno mismo",
        "Autocrítica",
        "Pensamientos o deseos suicidas",
        "Llanto",
        "Agitación",
        "Pérdida de interés",
        "Indecisión",
        "Desvalorización",
        "Pérdida de energía",
        "Cambios en patrones de sueño",
        "Irritabilidad",
        "Cambios en el apetito",
        "Dificultad de concentración",
        "Cansancio o fatiga",
        "Pérdida de interés en el sexo",
    ]
    story = kalyo_header(s)
    story += [
        Paragraph("BDI-II en Español", s["title"]),
        Paragraph("Inventario de Depresión de Beck — Segunda Edición", s["subtitle"]),
        Paragraph("Instrucciones de aplicación", s["h2"]),
        Paragraph(
            "Seleccione la afirmación que mejor describa cómo se ha sentido durante las <b>últimas 2 semanas, incluido hoy</b>. "
            "Cada ítem se puntúa de 0 a 3. Tiempo estimado: 5–10 minutos. Desde 13 años.",
            s["body"],
        ),
        Paragraph(
            "Para cada ítem marque UNA opción: 0 = mínima · 1 = leve · 2 = moderada · 3 = severa "
            "(consulte manual BDI-II para enunciados completos por nivel).",
            s["body"],
        ),
        Spacer(1, 0.06 * inch),
        items_table(items, ["0", "1", "2", "3"]),
        Spacer(1, 0.1 * inch),
        Paragraph("<b>PUNTAJE TOTAL:</b> _____ / 63", s["body"]),
        Paragraph("Interpretación del puntaje", s["h2"]),
        interp_table(
            ["Puntaje", "Nivel", "Acción sugerida"],
            [
                ["0 – 13", "Depresión mínima", "Psicoeducación y monitoreo"],
                ["14 – 19", "Leve", "Psicoterapia breve o seguimiento activo"],
                ["20 – 28", "Moderada", "Tratamiento psicológico activo; valorar farmacoterapia"],
                ["29 – 63", "Severa", "Intervención intensiva; evaluar riesgo suicida (ítem 9)"],
            ],
        ),
    ]
    story += footer_block(
        s,
        "Documenta evolución del BDI-II sesión a sesión con Kalyo — kalyo.io",
        "Beck AT, Steer RA, Brown GK. BDI-II Manual. 1996. Pearson. Adaptación clínica en español — uso profesional.",
    )
    return write_pdf("bdi-ii-inventario-depresion-beck-espanol.pdf", story)


def gen_bai():
    s = build_styles()
    items = [
        "Entumecimiento u hormigueo",
        "Sensación de calor",
        "Debilidad en piernas",
        "Incapacidad para relajarse",
        "Miedo a que ocurra lo peor",
        "Mareo o aturdimiento",
        "Palpitaciones o taquicardia",
        "Inestabilidad",
        "Sentirse asustado(a) o atemorizado(a)",
        "Nerviosismo",
        "Sensación de asfixia",
        "Temblores en manos",
        "Inquietud / no poder quedarse quieto(a)",
        "Miedo a perder el control",
        "Dificultad para respirar",
        "Miedo a morir",
        "Sentirse asustado(a)",
        "Indigestión o molestia abdominal",
        "Desmayos (sensación)",
        "Rubor facial",
        "Sudoración (no por calor)",
    ]
    story = kalyo_header(s)
    story += [
        Paragraph("BAI en Español", s["title"]),
        Paragraph("Inventario de Ansiedad de Beck (Beck Anxiety Inventory)", s["subtitle"]),
        Paragraph("Instrucciones de aplicación", s["h2"]),
        Paragraph(
            "Indique cuánto le han molestado los síntomas durante la <b>última semana, incluido hoy</b>. "
            "Escala 0–3 por ítem. Autoadministrado; calificación manual < 1 minuto.",
            s["body"],
        ),
        Paragraph("0 = Nada · 1 = Levemente · 2 = Moderadamente · 3 = Severamente", s["body"]),
        Spacer(1, 0.06 * inch),
        items_table(items, ["0", "1", "2", "3"]),
        Spacer(1, 0.1 * inch),
        Paragraph("<b>PUNTAJE TOTAL:</b> _____ / 63", s["body"]),
        Paragraph("Interpretación del puntaje", s["h2"]),
        interp_table(
            ["Puntaje", "Nivel", "Acción sugerida"],
            [
                ["0 – 7", "Ansiedad mínima", "Rango normal; sin intervención"],
                ["8 – 15", "Leve", "Monitoreo y psicoeducación"],
                ["16 – 25", "Moderada", "Iniciar plan de tratamiento"],
                ["26 – 63", "Severa", "Tratamiento activo; valorar derivación médica"],
            ],
        ),
    ]
    story += footer_block(
        s,
        "Integra el BAI en evaluaciones digitales con Kalyo — kalyo.io",
        "Beck AT, Steer RA. BAI Manual. 1993. Pearson. Validado en español (Sanz & Vázquez, 2003).",
    )
    return write_pdf("bai-inventario-ansiedad-beck-espanol.pdf", story)


def gen_hamd():
    s = build_styles()
    items = [
        "Humor deprimido",
        "Sentimientos de culpa",
        "Suicidio",
        "Insomnio inicial",
        "Insomnio intermedio",
        "Insomnio terminal",
        "Trabajo y actividades",
        "Inhibición psicomotora (retardo)",
        "Agitación psicomotora",
        "Ansiedad psíquica",
        "Ansiedad somática",
        "Síntomas somáticos gastrointestinales",
        "Síntomas somáticos generales",
        "Síntomas genitales",
        "Hipocondría",
        "Pérdida de peso",
        "Insight (conciencia de enfermedad)",
    ]
    scale = ["0 Ausente", "1 Leve", "2 Moderado", "3 Grave", "4 Muy grave"]
    story = kalyo_header(s)
    story += [
        Paragraph("HAM-D (HDRS-17) en Español", s["title"]),
        Paragraph("Escala de Depresión de Hamilton — 17 ítems", s["subtitle"]),
        Paragraph("Instrucciones de aplicación", s["h2"]),
        Paragraph(
            "<b>Heteroaplicada</b> por profesional entrenado durante entrevista clínica (15–20 min). "
            "Integrar observación conductual y relato del paciente. Reaplicar cada 2–4 semanas; respuesta = reducción ≥ 50%.",
            s["body"],
        ),
        Paragraph("Escala por ítem: " + " · ".join(scale), s["body"]),
        Spacer(1, 0.06 * inch),
        items_table(items, ["0", "1", "2", "3", "4"]),
        Spacer(1, 0.1 * inch),
        Paragraph("<b>PUNTAJE TOTAL:</b> _____ / 52", s["body"]),
        Paragraph("Interpretación del puntaje", s["h2"]),
        interp_table(
            ["Puntaje", "Severidad", "Acción sugerida"],
            [
                ["0 – 7", "Ausencia / mínima", "Sin depresión clínica significativa"],
                ["8 – 13", "Leve", "Seguimiento; psicoeducación"],
                ["14 – 18", "Moderada", "Tratamiento activo recomendado"],
                ["19 – 22", "Grave", "Intervención intensiva"],
                ["≥ 23", "Muy grave", "Tratamiento urgente; evaluar hospitalización"],
            ],
        ),
    ]
    story += footer_block(
        s,
        "Registra HAM-D y evolución clínica con Kalyo — kalyo.io",
        "Hamilton M. A rating scale for depression. J Neurol Neurosurg Psychiatry. 1960;23:56-62.",
    )
    return write_pdf("ham-d-escala-hamilton-depresion-espanol.pdf", story)


def gen_hama():
    s = build_styles()
    items = [
        "Humor ansioso (preocupación, anticipación del peor)",
        "Tensión (incapacidad para relajarse, llanto fácil)",
        "Miedos (hipocondría, fobias)",
        "Insomnio",
        "Funciones intelectuales (concentración, memoria)",
        "Humor depresivo",
        "Síntomas somáticos musculares",
        "Síntomas somáticos sensoriales",
        "Síntomas cardiovasculares",
        "Síntomas respiratorios",
        "Síntomas gastrointestinales",
        "Síntomas genitourinarios",
        "Síntomas del sistema nervioso autónomo",
        "Conducta en la entrevista",
    ]
    story = kalyo_header(s)
    story += [
        Paragraph("HAM-A en Español", s["title"]),
        Paragraph("Escala de Hamilton para la Ansiedad — 14 ítems", s["subtitle"]),
        Paragraph("Instrucciones de aplicación", s["h2"]),
        Paragraph(
            "<b>Heteroaplicada</b> (10–20 min). El clínico puntúa según entrevista y observación. "
            "Subescalas: ítems 1–6 ansiedad psíquica (0–24); ítems 7–14 ansiedad somática (0–32).",
            s["body"],
        ),
        Paragraph("0 = Ausente · 1 = Leve · 2 = Moderado · 3 = Grave · 4 = Muy grave/incapacitante", s["body"]),
        Spacer(1, 0.06 * inch),
        items_table(items, ["0", "1", "2", "3", "4"]),
        Spacer(1, 0.1 * inch),
        Paragraph("<b>PUNTAJE TOTAL:</b> _____ / 56", s["body"]),
        Paragraph("Interpretación del puntaje", s["h2"]),
        interp_table(
            ["Puntaje", "Interpretación", "Acción sugerida"],
            [
                ["≤ 14", "Bajo umbral clínico", "Ansiedad no significativa o en remisión"],
                ["> 14", "Ansiedad clínica", "Evaluación e intervención; Hamilton (1959)"],
                ["Reducción ≥ 50%", "Respuesta al tratamiento", "Continuar plan terapéutico"],
                ["< 7–8", "Remisión", "Mantenimiento y prevención de recaídas"],
            ],
        ),
    ]
    story += footer_block(
        s,
        "Aplica y documenta HAM-A con Kalyo — kalyo.io",
        "Hamilton M. The assessment of anxiety states by rating. Br J Med Psychol. 1959;32(1):50-55.",
    )
    return write_pdf("ham-a-escala-hamilton-ansiedad-espanol.pdf", story)


def gen_dass21():
    s = build_styles()
    items = [
        "Me costó mucho relajarme",
        "Noté sequedad en la boca",
        "No pude sentir ningún sentimiento positivo",
        "Tuve dificultad para respirar (p. ej. respiración acelerada)",
        "Me costó tomar la iniciativa para hacer cosas",
        "Reaccioné exageradamente ante las situaciones",
        "Sentí temblores (p. ej. en las manos)",
        "Sentí que usaba mucha energía nerviosa",
        "Estuve preocupado(a) por situaciones en las que pudiera entrar en pánico",
        "Sentí que no tenía nada que esperar",
        "Me sentí agitado(a)",
        "Me costó relajarme",
        "Me sentí decaído(a) y triste",
        "Fui intolerante ante cualquier interrupción",
        "Sentí que estaba cerca del pánico",
        "No pude entusiasmarme con nada",
        "Sentí que no valía mucho como persona",
        "Sentí que estaba muy irritable",
        "Noté los latidos de mi corazón sin esfuerzo físico",
        "Sentí miedo sin razón aparente",
        "Sentí que la vida no tenía sentido",
    ]
    subscale = (
        "Subescalas: D=Depresión (3,5,10,13,16,17,21) · A=Ansiedad (2,4,7,9,15,19,20) · "
        "E=Estrés (1,6,8,11,12,14,18). Sume 7 ítems por subescala (0–21) y <b>multiplique × 2</b> (0–42)."
    )
    story = kalyo_header(s)
    story += [
        Paragraph("DASS-21 en Español", s["title"]),
        Paragraph("Depression Anxiety Stress Scales — Versión breve", s["subtitle"]),
        Paragraph("Instrucciones de aplicación", s["h2"]),
        Paragraph(
            "Indique cuánto le afectó cada ítem durante la <b>última semana</b>. "
            "Autoinforme (~5 min). No usar puntaje total global; interpretar cada subescala por separado.",
            s["body"],
        ),
        Paragraph("0 = No me aplicó · 1 = Aplicó un poco · 2 = Aplicó bastante · 3 = Me aplicó mucho", s["body"]),
        Paragraph(subscale, s["body"]),
        Spacer(1, 0.06 * inch),
        items_table(items, ["0", "1", "2", "3"]),
        Spacer(1, 0.1 * inch),
        Paragraph(
            "<b>PUNTAJES (bruto × 2):</b> Depresión _____ / 42 · Ansiedad _____ / 42 · Estrés _____ / 42",
            s["body"],
        ),
        Paragraph("Interpretación por subescala (puntaje convertido)", s["h2"]),
        interp_table(
            ["Severidad", "Depresión", "Ansiedad", "Estrés"],
            [
                ["Normal", "0 – 9", "0 – 7", "0 – 14"],
                ["Leve", "10 – 13", "8 – 9", "15 – 18"],
                ["Moderado", "14 – 20", "10 – 14", "19 – 25"],
                ["Severo", "21 – 27", "15 – 19", "26 – 33"],
                ["Extremo", "28+", "20+", "34+"],
            ],
        ),
    ]
    story += footer_block(
        s,
        "Calcula DASS-21 automáticamente en Kalyo — kalyo.io",
        "Lovibond PF, Lovibond SH. Manual for the DASS. 1995. Antony et al. Psychol Assessment. 1998.",
    )
    return write_pdf("dass-21-escala-espanol.pdf", story)


def gen_madrs():
    s = build_styles()
    items = [
        "Tristeza aparente (observada)",
        "Tristeza referida (subjetiva)",
        "Tensión interna",
        "Sueño reducido",
        "Apetito reducido",
        "Dificultad de concentración",
        "Lassitud / falta de energía",
        "Incapacidad de sentir",
        "Pensamientos pesimistas",
        "Pensamientos suicidas",
    ]
    story = kalyo_header(s)
    story += [
        Paragraph("MADRS en Español", s["title"]),
        Paragraph("Montgomery-Åsberg Depression Rating Scale", s["subtitle"]),
        Paragraph("Instrucciones de aplicación", s["h2"]),
        Paragraph(
            "<b>Heteroaplicada</b> con entrevista clínica (15–20 min). Cada ítem se puntúa 0–6 según criterios anclados. "
            "Seguimiento cada 2–4 semanas; respuesta = reducción ≥ 50%; remisión < 10.",
            s["body"],
        ),
        Paragraph("0 = No presente · 6 = Severo (consultar manual para descriptores intermedios)", s["body"]),
        Spacer(1, 0.06 * inch),
        items_table(items, ["0", "1", "2", "3", "4", "5", "6"]),
        Spacer(1, 0.1 * inch),
        Paragraph("<b>PUNTAJE TOTAL:</b> _____ / 60", s["body"]),
        Paragraph("Interpretación del puntaje", s["h2"]),
        interp_table(
            ["Puntaje", "Severidad", "Acción sugerida"],
            [
                ["0 – 6", "Síntomas mínimos", "Sin intervención específica"],
                ["7 – 19", "Depresión leve", "Monitoreo; psicoterapia según contexto"],
                ["20 – 34", "Depresión moderada", "Tratamiento activo (corte ≥20 en Colombia)"],
                ["35 – 60", "Depresión severa", "Intervención intensiva; evaluar riesgo"],
                ["< 10", "Remisión", "Mantenimiento y prevención"],
            ],
        ),
    ]
    story += footer_block(
        s,
        "Monitorea respuesta al tratamiento con MADRS en Kalyo — kalyo.io",
        "Montgomery SA, Åsberg M. A new depression scale designed to be sensitive to change. Br J Psychiatry. 1979;134:382-389.",
    )
    return write_pdf("madrs-escala-depresion-espanol.pdf", story)


def gen_zung_dep():
    s = build_styles()
    items = [
        "Me siento decaído(a) y triste",
        "Por la mañana es cuando me siento peor",
        "Tengo episodios de llanto o ganas de llorar",
        "Duermo mal por la noche",
        "El apetito no es tan bueno como solía ser",
        "Todavía disfruto de relaciones sexuales (invertido)",
        "He notado que estoy perdiendo peso",
        "Tengo problemas de estreñimiento",
        "El corazón me late más rápido de lo normal",
        "Me canso sin razón aparente",
        "Mi mente está tan clara como antes (invertido)",
        "Puedo realizar mi trabajo como antes (invertido)",
        "Estoy inquieto(a) y no puedo quedarme quieto(a)",
        "Siento que hay futuro para mí (invertido)",
        "Estoy más irritable de lo habitual",
        "Me resulta fácil tomar decisiones (invertido)",
        "Siento que soy útil y necesario(a) (invertido)",
        "Disfruto de la vida como antes (invertido)",
        "Creo que los demás estarían mejor sin mí",
        "Todavía disfruto de las cosas que solía disfrutar (invertido)",
    ]
    zung_scale = ["Nunca / Rara vez (1)", "Algunas veces (2)", "Buena parte del tiempo (3)", "Casi siempre (4)"]
    story = kalyo_header(s)
    story += [
        Paragraph("Escala de Depresión de Zung (SDS)", s["title"]),
        Paragraph("Self-Rating Depression Scale — Autoadministrada", s["subtitle"]),
        Paragraph("Instrucciones de aplicación", s["h2"]),
        Paragraph(
            "Marque la opción que mejor describa cómo se ha sentido durante los <b>últimos días</b>. "
            "5–10 minutos. Ítems marcados (invertido) se puntúan en reversa.",
            s["body"],
        ),
        Paragraph(" · ".join(zung_scale), s["body"]),
        Spacer(1, 0.06 * inch),
        items_table(items, ["1", "2", "3", "4"]),
        Spacer(1, 0.1 * inch),
        Paragraph(
            "<b>Puntuación bruta:</b> _____ / 80 · <b>Índice:</b> (bruta ÷ 80) × 100 = _____",
            s["body"],
        ),
        Paragraph("Interpretación del índice", s["h2"]),
        interp_table(
            ["Índice", "Nivel", "Acción sugerida"],
            [
                ["< 50", "Sin depresión", "Monitoreo rutinario"],
                ["50 – 59", "Leve", "Seguimiento clínico"],
                ["60 – 69", "Moderada", "Tratamiento psicológico activo"],
                ["≥ 70", "Severa", "Intervención intensiva; evaluar riesgo"],
            ],
        ),
    ]
    story += footer_block(
        s,
        "Registra la Escala de Zung en expedientes digitales con Kalyo — kalyo.io",
        "Zung WW. A Self-Rating Depression Scale. Arch Gen Psychiatry. 1965;12:63-70.",
    )
    return write_pdf("zung-escala-depresion-espanol.pdf", story)


def gen_zung_anx():
    s = build_styles()
    items = [
        "Me siento más nervioso(a) y ansioso(a) de lo normal",
        "Siento miedo sin razón",
        "Puedo tener pensamientos de pánico o desmayo",
        "Siento que todo está bien y que nada malo va a pasar (invertido)",
        "Me siento inquieto(a) y no puedo quedarme quieto(a)",
        "Me siento agobiado(a) y tengo ganas de llorar",
        "Las ideas me vienen a la mente más lento que antes (invertido)",
        "Me siento triste",
        "Me cuesta más trabajo dormir que antes",
        "Me canso con facilidad",
        "Siento palpitaciones o taquicardia",
        "Tengo molestias estomacales o indigestión",
        "Orino con frecuencia",
        "Mis manos tiemblan",
        "Tengo la boca seca o la garganta seca",
        "Puedo leer con facilidad (invertido)",
        "Me siento agitado(a) y alterado(a)",
        "Tengo pesadillas",
        "Tengo dificultad para tragar",
        "Mis manos están frías y sudorosas",
    ]
    story = kalyo_header(s)
    story += [
        Paragraph("Escala de Ansiedad de Zung (SAS)", s["title"]),
        Paragraph("Self-Rating Anxiety Scale — Autoadministrada", s["subtitle"]),
        Paragraph("Instrucciones de aplicación", s["h2"]),
        Paragraph(
            "Indique con qué frecuencia le ha ocurrido cada situación durante la <b>última semana</b>. "
            "Entorno tranquilo; 5–10 minutos.",
            s["body"],
        ),
        Paragraph(
            "1 = Nunca o rara vez · 2 = Algunas veces · 3 = Buena parte del tiempo · 4 = Casi siempre",
            s["body"],
        ),
        Spacer(1, 0.06 * inch),
        items_table(items, ["1", "2", "3", "4"]),
        Spacer(1, 0.1 * inch),
        Paragraph(
            "<b>Puntuación bruta:</b> _____ / 80 · <b>Índice:</b> (bruta × 100) ÷ 80 = _____",
            s["body"],
        ),
        Paragraph("Interpretación del índice", s["h2"]),
        interp_table(
            ["Índice", "Nivel", "Acción sugerida"],
            [
                ["< 45", "Normal / mínimo", "Sin intervención específica"],
                ["45 – 59", "Leve", "Monitoreo y psicoeducación"],
                ["60 – 74", "Moderada", "Tratamiento psicológico activo"],
                ["≥ 75", "Severa", "Intervención inmediata; valorar derivación"],
            ],
        ),
    ]
    story += footer_block(
        s,
        "Aplica la SAS de Zung en tu consulta con Kalyo — kalyo.io",
        "Zung WW. A Rating Instrument for Anxiety Disorders. Psychosomatics. 1971;12(6):371-379.",
    )
    return write_pdf("zung-escala-ansiedad-espanol.pdf", story)


GENERATORS = [
    ("PHQ-2", gen_phq2),
    ("GAD-2", gen_gad2),
    ("BDI-II", gen_bdi),
    ("BAI", gen_bai),
    ("HAM-D", gen_hamd),
    ("HAM-A", gen_hama),
    ("DASS-21", gen_dass21),
    ("MADRS", gen_madrs),
    ("Zung Depresión", gen_zung_dep),
    ("Zung Ansiedad", gen_zung_anx),
]


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    created = []
    for name, fn in GENERATORS:
        path = fn()
        created.append((name, path.name, path.stat().st_size))
        print(f"OK  {path.name} ({path.stat().st_size:,} bytes)")
    print(f"\nGenerated {len(created)} PDFs in {ASSETS}")


if __name__ == "__main__":
    main()
