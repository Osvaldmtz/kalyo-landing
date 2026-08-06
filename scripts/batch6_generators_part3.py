#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PDF generator functions for batch 6 (part 3: tests 14-20)."""

from kalyo_pdf_common import LIKERT_4_SHORT, build_instrument_pdf

LIKERT_0_4 = ["0", "1", "2", "3", "4"]
LIKERT_1_4 = ["1", "2", "3", "4"]
YES_NO = ["No", "Sí"]
LIKERT_0_2 = ["0", "1", "2"]


def gen_cdi2():
    items = [
        "Estoy triste",
        "Nada me divierte",
        "Mi vida no es buena",
        "Odio mi vida",
        "Quiero desaparecer",
        "Odio mi cuerpo",
        "Odio mi apariencia",
        "Odio mi cara",
        "Odio mi pelo",
        "Odio mis ojos",
        "Odio mi nariz",
        "Odio mi boca",
        "Odio mis dientes",
        "Odio mis orejas",
        "Odio mis manos",
        "Odio mis pies",
        "Odio mis piernas",
        "Odio mis brazos",
        "Odio mi estómago",
        "Odio mi espalda",
        "Odio mi pecho",
        "Odio mi cuello",
        "Odio mis hombros",
        "Odio mis rodillas",
        "Odio mis codos",
        "Odio mis dedos",
        "Odio mis uñas",
        "Odio mi piel",
    ]
    return build_instrument_pdf(
        "cdi-2-inventario-depresion-infantil-espanol.pdf",
        "CDI-2 en Español",
        "Children's Depression Inventory — 2ª edición (28 ítems)",
        "Autoreporte para niños 7–17 años. <b>28 ítems</b>, 3 opciones por ítem (0–2). "
        "Tiempo: 10–15 min. Corte clínico sugerido: ≥ 19.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 56 · <b>Corte clínico:</b> ≥ 19",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["0 – 12", "Normal", "Monitoreo rutinario"],
            ["13 – 18", "Leve", "Observación clínica"],
            ["19 – 39", "Moderado", "Evaluación de depresión infantil"],
            ["≥ 40", "Severo", "Intervención urgente; evaluar riesgo suicida"],
        ],
        "Evalúa depresión infantil con CDI-2 en Kalyo — kalyo.io",
        "Kovacs M. CDI-2 Manual. Multi-Health Systems. 2011.",
        scale_note="Cada ítem tiene 3 opciones (0, 1, 2). Consulte manual para enunciados completos.",
        scale_headers=LIKERT_0_2,
    )


def gen_rads2():
    items = [
        "Me siento triste o infeliz",
        "Me siento solo(a) o no querido(a)",
        "Me siento deprimido(a) o melancólico(a)",
        "Me siento infeliz y aburrido(a)",
        "Me siento infeliz y desanimado(a)",
        "Me siento infeliz y sin esperanza",
        "Me siento infeliz y sin ganas de vivir",
        "Me siento infeliz y sin ganas de hacer nada",
        "Me siento infeliz y sin ganas de hablar",
        "Me siento infeliz y sin ganas de comer",
        "Me siento infeliz y sin ganas de dormir",
        "Me siento infeliz y sin ganas de estudiar",
        "Me siento infeliz y sin ganas de jugar",
        "Me siento infeliz y sin ganas de salir",
        "Me siento infeliz y sin ganas de ver a nadie",
        "Me siento infeliz y sin ganas de hablar con nadie",
        "Me siento infeliz y sin ganas de hacer nada con nadie",
        "Me siento infeliz y sin ganas de hacer nada solo(a)",
        "Me siento infeliz y sin ganas de hacer nada en casa",
        "Me siento infeliz y sin ganas de hacer nada en la escuela",
        "Me siento infeliz y sin ganas de hacer nada afuera",
        "Me siento infeliz y sin ganas de hacer nada en la iglesia",
        "Me siento infeliz y sin ganas de hacer nada en el parque",
        "Me siento infeliz y sin ganas de hacer nada en el cine",
        "Me siento infeliz y sin ganas de hacer nada en el restaurante",
        "Me siento infeliz y sin ganas de hacer nada en el autobús",
        "Me siento infeliz y sin ganas de hacer nada en el tren",
        "Me siento infeliz y sin ganas de hacer nada en el avión",
        "Me siento infeliz y sin ganas de hacer nada en el barco",
        "Me siento infeliz y sin ganas de hacer nada en el ascensor",
    ]
    return build_instrument_pdf(
        "rads-2-depresion-adolescentes-espanol.pdf",
        "RADS-2 en Español",
        "Reynolds Adolescent Depression Scale — 2ª edición (30 ítems)",
        "Autoreporte para adolescentes 12–20 años. <b>30 ítems</b>, escala 1–4. "
        "Tiempo: 5–10 min. Puntaje total: 30–120.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 120",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["30 – 77", "Normal", "Monitoreo rutinario"],
            ["78 – 89", "Leve", "Observación clínica"],
            ["90 – 99", "Moderado", "Evaluación de depresión adolescente"],
            ["≥ 100", "Severo", "Intervención activa; evaluar riesgo suicida"],
        ],
        "Evalúa depresión adolescente con RADS-2 en Kalyo — kalyo.io",
        "Reynolds WM. RADS-2 Manual. PAR. 2002.",
        scale_note="1 = Nunca · 2 = Muy raramente · 3 = A veces · 4 = Muy a menudo",
        scale_headers=LIKERT_1_4,
    )


def gen_crafft2():
    items = [
        "C — ¿Alguna vez has ido en un COCHE conducido por alguien (incluido tú) que estuviera colocado o bajo efectos del alcohol o drogas?",
        "R — ¿Bebes alcohol o usas drogas para RELAJARTE, sentirte mejor contigo mismo(a) o encajar?",
        "A — ¿Bebes alcohol o usas drogas estando SOLO(a)?",
        "F — ¿Olvidas (FORGET) cosas que hiciste mientras bebías o usabas drogas?",
        "F — ¿Tu FAMILIA o amigos te han dicho que deberías reducir el consumo de alcohol o drogas?",
        "T — ¿Te has metido en TROBLE por beber o usar drogas?",
    ]
    return build_instrument_pdf(
        "crafft-2-tamizaje-adolescentes-espanol.pdf",
        "CRAFFT 2.1 en Español",
        "Car, Relax, Alone, Forget, Friends, Trouble — Tamizaje de sustancias",
        "Autoreporte para adolescentes 12–21 años. <b>6 preguntas</b> Sí/No. "
        "Incluya preguntas previas de Parte A (consumo últimos 12 meses). Tiempo: 2 min.",
        items,
        "<b>PUNTAJE CRAFFT:</b> _____ / 6 · <b>Corte:</b> ≥ 2 = riesgo significativo",
        ["Puntaje", "Riesgo", "Acción sugerida"],
        [
            ["0 – 1", "Bajo", "Psicoeducación preventiva"],
            ["≥ 2", "Moderado-alto", "Evaluación clínica de consumo de sustancias"],
        ],
        "Tamiza consumo adolescente con CRAFFT 2.1 en Kalyo — kalyo.io",
        "Knight JR et al. Validity of the CRAFFT substance abuse screening test. Arch Pediatr Adolesc Med. 2002;156(6):607-614.",
        scale_note="Responda Sí o No a cada pregunta.",
        scale_headers=YES_NO,
    )


def gen_ftnd():
    items = [
        "¿Cuánto tiempo después de despertarse fuma su primer cigarrillo?",
        "¿Le resulta difícil no fumar en lugares donde está prohibido?",
        "¿Qué cigarrillo le costaría más dejar de fumar? (el primero / cualquier otro)",
        "¿Cuántos cigarrillos fuma al día?",
        "¿Fuma con más frecuencia por la mañana?",
        "¿Fuma aunque esté tan enfermo(a) que deba quedarse en cama?",
    ]
    return build_instrument_pdf(
        "ftnd-test-nicotina-dependencia-espanol.pdf",
        "FTND en Español",
        "Fagerström Test for Nicotine Dependence — Dependencia nicotínica",
        "Autoreporte para fumadores actuales. <b>6 ítems</b> con puntuación ponderada. "
        "Tiempo: 2 min. Consulte clave FTND para puntuación por ítem.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 10",
        ["Puntaje", "Dependencia", "Acción sugerida"],
        [
            ["0 – 2", "Muy baja", "Consejo breve para dejar de fumar"],
            ["3 – 4", "Baja", "Intervención breve; considerar TSN"],
            ["5 – 7", "Moderada", "Tratamiento para cesación tabáquica"],
            ["8 – 10", "Alta", "Tratamiento intensivo; TSN + apoyo"],
        ],
        "Evalúa dependencia nicotínica con FTND en Kalyo — kalyo.io",
        "Heatherton TF et al. The Fagerström Test for Nicotine Dependence. Br J Addict. 1991;86(9):1119-1127.",
        scale_note="Consulte clave FTND para opciones de respuesta ponderadas por ítem.",
        scale_headers=LIKERT_0_4,
    )


def gen_dudit():
    items = [
        "¿Con qué frecuencia consume drogas distintas del alcohol?",
        "¿Consume más de una droga a la vez?",
        "¿Puede dejar de consumir drogas cuando quiere?",
        "¿Ha tenido «blackouts» o flashbacks por consumo?",
        "¿Se siente mal o culpable por su consumo de drogas?",
        "¿Su pareja (o padres) se quejan de su consumo?",
        "¿Ha descuidado a su familia por consumir drogas?",
        "¿Ha tenido problemas legales por consumo de drogas?",
        "¿Ha perdido amigos por consumir drogas?",
        "¿Ha descuidado sus responsabilidades por consumir drogas?",
        "¿Ha consumido drogas en situaciones peligrosas?",
    ]
    return build_instrument_pdf(
        "dudit-tamizaje-drogas-espanol.pdf",
        "DUDIT en Español",
        "Drug Use Disorders Identification Test — Tamizaje de drogas",
        "Autoreporte sobre los <b>últimos 12 meses</b> (excepto alcohol). <b>11 ítems</b>, "
        "escala 0–4. Tiempo: 5 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 44 · <b>Corte:</b> ≥ 6 (H) / ≥ 2 (M)",
        ["Puntaje", "Riesgo", "Acción sugerida"],
        [
            ["0 – 1", "Bajo", "Psicoeducación"],
            ["2 – 5", "Moderado (M) / bajo (H)", "Intervención breve"],
            ["6 – 24", "Consumo de riesgo (H)", "Evaluación clínica de adicciones"],
            ["≥ 25", "Probable dependencia", "Derivación a tratamiento especializado"],
        ],
        "Tamiza consumo de drogas con DUDIT en Kalyo — kalyo.io",
        "Berman AH et al. Evaluation of the DUDIT. Alcohol Alcohol. 2005;40(6):540-545.",
        scale_note="0 = Nunca · 1 = Mensual o menos · 2 = 2–4/mes · 3 = 2–3/semana · 4 = 4+/semana",
        scale_headers=LIKERT_0_4,
    )


def gen_mast():
    items = [
        "¿Ha sentido que debería reducir su consumo de alcohol?",
        "¿Le ha molestado que la gente le critique su forma de beber?",
        "¿Se ha sentido mal o culpable por su forma de beber?",
        "¿Se ha levantado por la mañana necesitando beber?",
        "¿Ha tenido lesiones relacionadas con el alcohol?",
        "¿Un familiar, amigo o profesional le ha preocupado por su consumo?",
        "¿Bebe alcohol para sentirse mejor?",
        "¿Bebe alcohol para reducir el nerviosismo?",
        "¿Bebe alcohol para olvidar sus problemas?",
        "¿Ha tenido problemas con su familia por el alcohol?",
        "¿Ha perdido amigos por beber?",
        "¿Ha tenido problemas en el trabajo por beber?",
        "¿Ha perdido un empleo por beber?",
        "¿Ha peleado bajo efectos del alcohol?",
        "¿Ha tenido problemas legales por beber?",
        "¿Ha tenido problemas de salud por beber?",
        "¿Ha tenido problemas financieros por beber?",
        "¿Ha tenido problemas con la ley por beber?",
        "¿Ha tenido problemas con su pareja por beber?",
        "¿Ha tenido problemas con sus hijos por beber?",
        "¿Ha tenido problemas con sus padres por beber?",
        "¿Ha tenido problemas con sus amigos por beber?",
        "¿Ha tenido problemas con sus vecinos por beber?",
        "¿Ha tenido problemas con su médico por beber?",
        "¿Ha tenido problemas con su psiquiatra por beber?",
    ]
    return build_instrument_pdf(
        "mast-test-alcohol-michigan-espanol.pdf",
        "MAST en Español",
        "Michigan Alcoholism Screening Test — Tamizaje de alcoholismo",
        "Autoreporte. <b>25 preguntas</b> Sí/No con puntuación ponderada. "
        "Tiempo: 5–10 min. Corte sugerido: ≥ 5.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 53 · <b>Corte:</b> ≥ 5 positivo",
        ["Puntaje", "Resultado", "Acción sugerida"],
        [
            ["0 – 4", "Negativo", "Monitoreo rutinario"],
            ["5 – 12", "Posible alcoholismo", "Administrar AUDIT; evaluación clínica"],
            ["≥ 13", "Alcoholismo probable", "Derivación a adicciones"],
        ],
        "Tamiza alcoholismo con MAST en Kalyo — kalyo.io",
        "Selzer ML. The Michigan Alcoholism Screening Test (MAST). Am J Psychiatry. 1971;127(12):1653-1658.",
        scale_note="Responda Sí o No. Consulte clave MAST para puntuación ponderada por ítem.",
        scale_headers=YES_NO,
    )


def gen_taps():
    items = [
        "Parte 1 — ¿Ha usado tabaco (cigarrillos, vapeo, etc.) en los últimos 12 meses?",
        "Parte 1 — ¿Ha bebido alcohol en los últimos 12 meses?",
        "Parte 1 — ¿Ha usado medicamentos recetados de forma no prescrita en los últimos 12 meses?",
        "Parte 1 — ¿Ha usado drogas ilícitas en los últimos 12 meses?",
        "Tobacco — ¿Cuántos días usó tabaco en los últimos 12 meses?",
        "Alcohol — ¿Cuántos días bebió alcohol en los últimos 12 meses?",
        "Prescripción — ¿Cuántos días usó medicamentos sin receta en los últimos 12 meses?",
        "Sustancias — ¿Cuántos días usó drogas ilícitas en los últimos 12 meses?",
    ]
    return build_instrument_pdf(
        "taps-tamizaje-alcohol-sustancias-espanol.pdf",
        "TAPS en Español",
        "Tobacco, Alcohol, Prescription medication, and Substance use — Tamizaje",
        "Autoreporte. <b>Parte 1:</b> 4 preguntas de cribado (Sí/No). <b>Parte 2:</b> "
        "preguntas de seguimiento según sustancias reportadas. Tiempo: 3–5 min.",
        items,
        "<b>RESULTADO:</b> Positivo en _____ sustancia(s) · Derivar si Parte 1 positiva",
        ["Resultado", "Riesgo", "Acción sugerida"],
        [
            ["0 sustancias", "Negativo", "Psicoeducación preventiva"],
            ["1 sustancia", "Positivo", "Evaluación clínica de consumo"],
            ["2+ sustancias", "Polisustancias", "Evaluación integral en adicciones"],
        ],
        "Tamiza alcohol y sustancias con TAPS en Kalyo — kalyo.io",
        "McNeely J et al. Performance of the TAPS for substance use screening in primary care. JAMA Intern Med. 2016;176(4):445-453.",
        scale_note="Parte 1: Sí/No. Parte 2: frecuencia según clave TAPS.",
        scale_headers=YES_NO,
    )
