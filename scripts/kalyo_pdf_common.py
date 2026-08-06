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
LOGO = ASSETS / "kalyo-logo.png"
LOGO_ASPECT = 2516 / 1066  # width / height from source asset

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
    logo_h = 0.32 * inch
    logo_w = logo_h * LOGO_ASPECT
    if LOGO.exists():
        img = Image(str(LOGO), width=logo_w, height=logo_h)
        domain = Paragraph("kalyo.io", styles["header_brand"])
        left_stack = Table(
            [[img], [domain]],
            colWidths=[logo_w],
        )
        left_stack.setStyle(
            TableStyle(
                [
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (0, 0), 0),
                    ("BOTTOMPADDING", (0, 1), (0, 1), 0),
                    ("TOPPADDING", (0, 1), (0, 1), 2),
                ]
            )
        )
        tag = Paragraph("Recurso clínico gratuito", styles["header_tag"])
        inner = Table(
            [[left_stack, tag]],
            colWidths=[logo_w + 8, 6.5 * inch - logo_w - 8],
        )
        inner.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("ALIGN", (1, 0), (1, 0), "RIGHT"),
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

def build_instrument_pdf(
    filename: str,
    title: str,
    subtitle: str,
    instructions: str,
    items: list[str],
    score_line: str,
    interp_headers: list[str],
    interp_rows: list[list[str]],
    cta: str,
    reference: str,
    scale_note: str | None = None,
    scale_headers: list[str] | None = None,
    extra_story: list | None = None,
) -> Path:
    s = build_styles()
    story = kalyo_header(s)
    story += [
        Paragraph(title, s["title"]),
        Paragraph(subtitle, s["subtitle"]),
        Paragraph("Instrucciones de aplicación", s["h2"]),
        Paragraph(instructions, s["body"]),
    ]
    if scale_note:
        story.append(Paragraph(scale_note, s["body"]))
    story += [Spacer(1, 0.06 * inch), items_table(items, scale_headers)]
    if extra_story:
        story += extra_story
    story += [
        Spacer(1, 0.1 * inch),
        Paragraph(score_line, s["body"]),
        Paragraph("Interpretación del puntaje", s["h2"]),
        interp_table(interp_headers, interp_rows),
    ]
    story += footer_block(s, cta, reference)
    return write_pdf(filename, story)

