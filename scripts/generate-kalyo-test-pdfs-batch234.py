#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Kalyo-branded clinical test PDFs (batches 2–4) and patch blog HTML download buttons."""

from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

from kalyo_pdf_common import (
    ASSETS,
    LIKERT_4_SHORT,
    build_instrument_pdf,
    build_styles,
    footer_block,
    interp_table,
    items_table,
    kalyo_header,
    write_pdf,
)

ROOT = Path(__file__).resolve().parents[1]
ARTICULOS = ROOT / "articulos"

LIKERT_0_4 = ["0", "1", "2", "3", "4"]
LIKERT_0_5 = ["0", "1", "2", "3", "4", "5"]
LIKERT_0_6 = ["0", "1", "2", "3", "4", "5", "6"]
LIKERT_1_4 = ["1", "2", "3", "4"]
PHQ15_HEADERS = ["0", "1", "2"]
YES_NO = ["No", "Sí"]
DES_PERCENT = ["0%", "25%", "50%", "75%", "100%"]

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


# ---------------------------------------------------------------------------
# Lote 2 — trauma, somático, suicidio, disociación
# ---------------------------------------------------------------------------

def gen_hads():
    items = [
        "Me siento tenso(a) o alterado(a)",
        "Disfruto de las mismas cosas que solía (invertido)",
        "Tengo una sensación de miedo, como si algo horrible fuera a ocurrir",
        "Puedo reírme y ver el lado bueno de las cosas (invertido)",
        "Tengo muchas preocupaciones en la cabeza",
        "Me siento alegre (invertido)",
        "Puedo estar sentado(a) tranquilamente y sentirme relajado(a) (invertido)",
        "Me siento lento(a) y como atontado(a)",
        "Tengo sensaciones extrañas en el estómago",
        "He perdido interés en mi apariencia personal",
        "Me siento inquieto(a), como si tuviera que estar en movimiento",
        "Espero las cosas con ilusión (invertido)",
        "Tengo accesos de pánico",
        "Puedo disfrutar de un buen libro o un programa de radio o TV (invertido)",
    ]
    return build_instrument_pdf(
        "hads-escala-ansiedad-depresion-espanol.pdf",
        "HADS en Español",
        "Hospital Anxiety and Depression Scale — Ansiedad y depresión",
        "Autoreporte sobre la <b>última semana</b>. 14 ítems (7 ansiedad + 7 depresión), escala 0–3. "
        "Tiempo: 2–5 min. Ítems invertidos se recodifican. Puntúe subescalas por separado.",
        items,
        "<b>PUNTAJES:</b> HADS-A (ansiedad) _____ / 21 · HADS-D (depresión) _____ / 21",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["0 – 7", "Normal", "Sin intervención específica"],
            ["8 – 10", "Leve", "Monitoreo y psicoeducación"],
            ["11 – 14", "Moderado", "Evaluación clínica; considerar tratamiento"],
            ["15 – 21", "Severo", "Intervención activa; valorar derivación"],
        ],
        "Aplica HADS y registra subescalas en expediente con Kalyo — kalyo.io",
        "Zigmond AS, Snaith RP. The HADS. Acta Psychiatr Scand. 1983;67(6):361-370. Validación en español.",
        scale_note="0 = Casi siempre · 1 = A menudo · 2 = A veces · 3 = Casi nunca (ítems invertidos al revés)",
        scale_headers=LIKERT_4_SHORT,
    )


def gen_pcl5():
    items = [
        "Recuerdos repetidos, perturbadores e involuntarios del evento",
        "Sueños repetidos y perturbadores del evento",
        "De repente sentir o actuar como si el evento volviera a ocurrir",
        "Sentirse muy alterado(a) cuando algo le recuerda el evento",
        "Reacciones físicas fuertes cuando algo le recuerda el evento",
        "Evitar recuerdos, pensamientos o sentimientos sobre el evento",
        "Evitar lugares, actividades o personas que le recuerden el evento",
        "Dificultad para recordar partes importantes del evento",
        "Creencias o expectativas negativas persistentes sobre uno mismo o el mundo",
        "Pensamientos distorsionados sobre la causa o las consecuencias del evento",
        "Estado emocional negativo persistente (miedo, horror, culpa, vergüenza)",
        "Pérdida de interés en actividades significativas",
        "Sentirse distante o desconectado(a) de otras personas",
        "Dificultad para experimentar emociones positivas",
        "Comportamiento irritable o arrebatos de ira",
        "Comportamiento imprudente o autodestructivo",
        "Estar en alerta o vigilante excesiva",
        "Estar muy sobresaltado(a) o asustado(a) con facilidad",
        "Dificultad para concentrarse",
        "Dificultad para conciliar o mantener el sueño",
    ]
    return build_instrument_pdf(
        "pcl-5-estres-postraumatico-espanol.pdf",
        "PCL-5 en Español",
        "PTSD Checklist for DSM-5 — TEPT",
        "Indique cuánto le ha molestado cada problema durante el <b>último mes</b> en relación con el evento traumático "
        "más estresante. 20 ítems, escala 0–4. Tiempo: 5–10 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 80 · <b>Probable TEPT (corte sugerido):</b> ≥ 31–33",
        ["Puntaje", "Interpretación", "Acción sugerida"],
        [
            ["0 – 30", "Por debajo del corte", "Monitoreo; evaluar síntomas clínicos"],
            ["31 – 44", "Probable TEPT", "Evaluación clínica estructurada (CAPS-5)"],
            ["45 – 80", "TEPT probable severo", "Tratamiento especializado en trauma"],
        ],
        "Documenta PCL-5 y seguimiento de trauma con Kalyo — kalyo.io",
        "Weathers FW et al. The PCL-5. National Center for PTSD. 2013. Validación en español disponible.",
        scale_note="0 = Nada · 1 = Un poco · 2 = Moderadamente · 3 = Bastante · 4 = Extremadamente",
        scale_headers=LIKERT_0_4,
    )


def gen_cssrs():
    items = [
        "¿Ha deseado estar muerto(a) o poder dormir y no despertar?",
        "¿Ha tenido pensamientos de hacerse daño o quitarse la vida?",
        "¿Ha pensado en cómo podría hacerse daño o quitarse la vida?",
        "¿Ha tenido intención de actuar según estos pensamientos?",
        "¿Ha empezado a preparar o ha preparado algo para hacerse daño o quitarse la vida?",
        "¿Ha hecho algún intento de suicidio en su vida?",
        "¿Ha hecho algún intento de suicidio en los últimos 3 meses?",
        "¿Ha hecho algo para hacerse daño aunque no quisiera morir?",
    ]
    return build_instrument_pdf(
        "c-ssrs-escala-columbia-suicidio-espanol.pdf",
        "C-SSRS — Tamizaje en Español",
        "Columbia Suicide Severity Rating Scale — Versión de screening",
        "<b>Heteroaplicada o autoreporte guiado.</b> Preguntas en orden jerárquico; detenerse según protocolo "
        "institucional si hay ideación activa. Evaluar riesgo inmediato y plan de seguridad.",
        items,
        "<b>Clasificación de riesgo:</b> _____ · <b>Intervención:</b> _____",
        ["Nivel", "Criterio", "Acción sugerida"],
        [
            ["Bajo", "Sin ideación o deseo pasivo", "Monitoreo rutinario"],
            ["Moderado", "Ideación sin intención/plan", "Plan de seguridad; seguimiento cercano"],
            ["Alto", "Intención, plan o preparación", "Intervención urgente; no dejar solo(a)"],
            ["Muy alto", "Intento reciente o conducta", "Hospitalización / crisis inmediata"],
        ],
        "Registra evaluaciones de riesgo suicida con protocolo C-SSRS en Kalyo — kalyo.io",
        "Posner K et al. The C-SSRS. Am J Psychiatry. 2011;168(12):1266-1277. Uso clínico con formación.",
        scale_note="Marque Sí/No según respuesta del paciente. Aplicar protocolo de seguridad según nivel.",
        scale_headers=YES_NO,
    )


def gen_ies_r():
    items = [
        "Cualquier recordatorio me trae sentimientos sobre el evento",
        "Tenía problemas para dormir",
        "Otras cosas me hacían pensar en el evento",
        "Me sentía irritable y enfadado(a)",
        "Evitaba recordar el evento o pensar en él",
        "Pensaba en el evento cuando no quería",
        "Sentía que el evento no había ocurrido o no era real",
        "Me mantenía alejado(a) de recordatorios del evento",
        "Imágenes sobre el evento me venían a la mente",
        "Me sentía sobresaltado(a) y fácil de asustar",
        "Intentaba no hablar del evento",
        "Notaba que seguía teniendo sentimientos sobre el evento",
        "Evitaba sentir algo sobre el evento",
        "Notaba que mi corazón latía rápido sin esfuerzo",
        "Me enfadaba por cosas que me recordaban el evento",
        "Tenía sueños sobre el evento",
        "Sentía que el evento volvía a ocurrir",
        "Me sentía alterado(a) cuando algo me recordaba el evento",
        "Intentaba no pensar en el evento",
        "Sentía que no podía sentir emociones",
        "Me sentía débil y vulnerable",
        "Tenía dificultad para concentrarme",
    ]
    return build_instrument_pdf(
        "ies-r-impacto-estres-postraumatico-espanol.pdf",
        "IES-R en Español",
        "Impact of Event Scale — Revised",
        "Indique cuánto le molestó cada dificultad durante la <b>última semana</b> en relación con el evento "
        "traumático. 22 ítems, escala 0–4. Subescalas: Intrusión, Evitación, Hiperactivación.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 88 · <b>Corte clínico sugerido:</b> ≥ 33",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["0 – 23", "Subclínico", "Psicoeducación y monitoreo"],
            ["24 – 32", "Leve", "Evaluación clínica de estrés postraumático"],
            ["33 – 36", "Moderado", "Intervención psicológica en trauma"],
            ["37 – 88", "Severo", "Tratamiento especializado; valorar TEPT"],
        ],
        "Integra IES-R en evaluaciones de trauma con Kalyo — kalyo.io",
        "Weiss DS, Marmar CR. The Impact of Event Scale-Revised. 1997. Validación en español.",
        scale_note="0 = Nada · 1 = Un poco · 2 = Moderadamente · 3 = Bastante · 4 = Extremadamente",
        scale_headers=LIKERT_0_4,
    )


def gen_phq15():
    items = [
        "Dolor de estómago",
        "Dolor de espalda",
        "Dolor en brazos, piernas o articulaciones",
        "Menstruaciones dolorosas o problemas menstruales (si aplica)",
        "Dolores de cabeza",
        "Dolor en el pecho",
        "Mareos",
        "Desmayos",
        "Palpitaciones o taquicardia",
        "Falta de aire",
        "Dolor o problemas al tener relaciones sexuales",
        "Estreñimiento, diarrea o problemas intestinales",
        "Náuseas, gases o indigestión",
        "Sensación de que el corazón late demasiado rápido",
        "Falta de energía o cansancio",
    ]
    return build_instrument_pdf(
        "phq-15-sintomas-somaticos-espanol.pdf",
        "PHQ-15 en Español",
        "Patient Health Questionnaire-15 — Síntomas somáticos",
        "Durante las <b>últimas 4 semanas</b>, ¿qué tanto le ha molestado cada problema? "
        "15 ítems, escala 0–2. Tiempo: 3–5 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 30",
        ["Puntaje", "Severidad", "Acción sugerida"],
        [
            ["0 – 4", "Mínima", "Sin intervención específica"],
            ["5 – 9", "Baja", "Monitoreo; descartar causa orgánica"],
            ["10 – 14", "Media", "Evaluación biopsicosocial; tratamiento"],
            ["15 – 30", "Alta", "Intervención activa; valorar trastorno somático"],
        ],
        "Registra PHQ-15 y seguimiento somático con Kalyo — kalyo.io",
        "Kroenke K, Spitzer RL, Williams JB. The PHQ-15. J Psychosom Res. 2002;53(4):603-613.",
        scale_note="0 = Nada · 1 = Levemente · 2 = Moderadamente · 3 = Severamente (usar 0–2)",
        scale_headers=PHQ15_HEADERS,
    )


def gen_bhs():
    items = [
        "Esperanza en el futuro",
        "Cambios en el futuro",
        "Expectativas sobre el futuro",
        "Perspectiva general del futuro",
        "Probabilidad de éxito personal",
        "Miedo al futuro",
        "Planes para el futuro",
        "Perspectiva sobre el mundo futuro",
        "Expectativas sobre uno mismo",
        "Perspectiva sobre el futuro en general",
        "Motivación para el futuro",
        "Expectativas sobre logros futuros",
        "Visión del futuro personal",
        "Expectativas sobre la vida",
        "Perspectiva sobre el mañana",
        "Expectativas sobre la felicidad futura",
        "Visión del futuro a largo plazo",
        "Expectativas sobre el éxito",
        "Perspectiva sobre el destino",
        "Expectativas sobre la resolución de problemas",
    ]
    return build_instrument_pdf(
        "bhs-escala-desesperanza-beck-espanol.pdf",
        "BHS en Español",
        "Beck Hopelessness Scale — Escala de desesperanza",
        "Marque <b>Sí</b> o <b>No</b> según cómo se siente en general. 20 ítems. "
        "Tiempo: 5–10 min. Consulte manual BHS para enunciados completos por ítem.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 20 · <b>Corte clínico:</b> ≥ 9",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["0 – 3", "Mínima desesperanza", "Monitoreo rutinario"],
            ["4 – 8", "Leve", "Explorar factores protectores y de riesgo"],
            ["9 – 14", "Moderada", "Evaluación de riesgo suicida; intervención"],
            ["15 – 20", "Severa", "Intervención urgente; plan de seguridad"],
        ],
        "Documenta BHS y evaluación de riesgo con Kalyo — kalyo.io",
        "Beck AT, Weissman A, Lester D, Trexler L. The BHS. J Consulting Clin Psychol. 1974. Pearson.",
        scale_note="Responda Sí o No a cada afirmación sobre expectativas futuras (ítems completos en manual).",
        scale_headers=YES_NO,
    )


def gen_bssi():
    items = [
        "Deseo de vivir / deseo de morir",
        "Deseo de quitarse la vida",
        "Razones para quitarse la vida",
        "Razones contra quitarse la vida",
        "Forma, plan o intención suicida",
        "Control sobre el acto suicida",
        "Deterrentes (factores que lo impiden)",
        "Preparativos para el suicidio",
        "Comunicación de intención suicida",
        "Intentos previos de suicidio",
        "Duración de la ideación suicida",
        "Control sobre los pensamientos suicidas",
        "Resistencia a la ideación suicida",
        "Razones para el intento (si aplica)",
        "Actitud hacia la posibilidad de morir",
        "Actitud hacia la posibilidad de vivir",
        "Método concreto considerado",
        "Accesibilidad al método",
        "Sensación de estar atrapado(a)",
        "Expectativas sobre el intento",
        "Disposición actual para intentar",
    ]
    return build_instrument_pdf(
        "bssi-ideacion-suicida-beck-espanol.pdf",
        "BSSI en Español",
        "Beck Scale for Suicide Ideation — Ideación suicida",
        "<b>Heteroaplicada</b> por clínico entrenado. 21 ítems, escala 0–3 por ítem. "
        "Evalúa intensidad y riesgo de ideación suicida. Consulte manual para anclajes por ítem.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 63 · <b>Riesgo elevado:</b> ≥ 19",
        ["Puntaje", "Riesgo", "Acción sugerida"],
        [
            ["0 – 5", "Bajo", "Monitoreo; factores protectores"],
            ["6 – 18", "Moderado", "Plan de seguridad; seguimiento frecuente"],
            ["19 – 38", "Alto", "Intervención inmediata; no dejar solo(a)"],
            ["39 – 63", "Muy alto", "Hospitalización / servicios de crisis"],
        ],
        "Registra BSSI y protocolos de seguridad con Kalyo — kalyo.io",
        "Beck AT, Steer RA, Ranieri WF. Scale for Suicide Ideation. J Consulting Clin Psychol. 1988. Pearson.",
        scale_note="0 = No presente · 1 = Leve · 2 = Moderado · 3 = Severo (anclajes en manual BSSI)",
        scale_headers=LIKERT_4_SHORT,
    )


def gen_sbq_r():
    items = [
        "¿Alguna vez en su vida ha pensado en quitarse la vida?",
        "¿Con qué frecuencia ha pensado en quitarse la vida en el último año?",
        "¿Alguna vez ha intentado quitarse la vida?",
        "¿Es probable que alguna vez intente quitarse la vida?",
    ]
    return build_instrument_pdf(
        "sbq-r-conducta-suicida-espanol.pdf",
        "SBQ-R en Español",
        "Suicidal Behaviors Questionnaire — Revised",
        "Autoreporte breve (4 ítems). Ítem 1: Sí/No. Ítem 2: escala de frecuencia 1–5. "
        "Ítems 3–4: Sí/No y probabilidad 0–10. Tiempo: 2 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 18 · <b>Corte sugerido:</b> ≥ 7",
        ["Puntaje", "Riesgo", "Acción sugerida"],
        [
            ["0 – 6", "Bajo", "Monitoreo rutinario"],
            ["7 – 8", "Moderado", "Evaluación clínica de riesgo suicida"],
            ["9 – 18", "Alto", "Intervención inmediata; plan de seguridad"],
        ],
        "Tamiza riesgo suicida con SBQ-R y documenta en Kalyo — kalyo.io",
        "Osman A et al. The Suicidal Behaviors Questionnaire-Revised. J Clin Psychol. 2001;57(7):855-867.",
        scale_note="Consulte clave de puntuación SBQ-R para ítems 2 y 4 (frecuencia y probabilidad).",
        scale_headers=LIKERT_4_SHORT,
    )


def gen_lec5():
    items = [
        "Desastre natural (inundación, tornado, terremoto, etc.)",
        "Incendio o explosión",
        "Accidente de tránsito u otro accidente grave",
        "Accidente grave en el trabajo, en casa o durante recreación",
        "Exposición a sustancia tóxica (químicos, radiación)",
        "Agresión física (golpes, empujones, etc.)",
        "Agresión con arma (cuchillo, pistola, etc.)",
        "Agresión sexual",
        "Otra experiencia sexual no deseada o incómoda",
        "Experiencia de combate o zona de guerra",
        "Cautiverio (secuestro, rehenía)",
        "Enfermedad potencialmente mortal o lesión grave",
        "Sufrimiento humano severo",
        "Muerte violenta o repentina (homicidio, suicidio)",
        "Muerte accidental repentina",
        "Causó lesión grave, daño o muerte a otra persona",
        "Cualquier otro evento muy estresante",
    ]
    return build_instrument_pdf(
        "lec-5-eventos-vitales-traumaticos-espanol.pdf",
        "LEC-5 en Español",
        "Life Events Checklist for DSM-5 — Eventos traumáticos",
        "Marque <b>Sí</b> si alguna vez ha experimentado, presenciado o conocido de cerca cada evento. "
        "17 categorías de eventos traumáticos según DSM-5. Tiempo: 5 min.",
        items,
        "<b>Eventos experimentados:</b> _____ · <b>Presenciados:</b> _____ · <b>Conocidos de cerca:</b> _____",
        ["Respuesta", "Uso clínico", "Acción sugerida"],
        [
            ["0 eventos", "Sin exposición reportada", "Evaluar otros factores de riesgo"],
            ["1+ eventos", "Exposición a trauma", "Administrar PCL-5 o CAPS-5"],
            ["Múltiples", "Trauma repetido", "Evaluación integral de TEPT y comorbilidad"],
        ],
        "Registra historial de trauma con LEC-5 en Kalyo — kalyo.io",
        "Weathers FW et al. The Life Events Checklist for DSM-5. National Center for PTSD. 2013.",
        scale_note="Marque Sí si el evento ocurrió alguna vez en su vida (experiencia directa, presenciado o conocido).",
        scale_headers=YES_NO,
    )


def gen_des_ii():
    items = [
        "Alguien más habla dentro de mi cabeza",
        "Alguien más hace cosas con mis manos o piernas",
        "Me siento como si no fuera yo mismo(a)",
        "Mi cuerpo se siente diferente, como si no fuera el mío",
        "Me siento separado(a) de lo que me rodea",
        "Las cosas me parecen irreales o extrañas",
        "Me siento como si estuviera soñando despierto(a)",
        "Me siento emocionalmente distante de las personas",
        "Me siento como si estuviera observándome desde afuera",
        "Las cosas a mi alrededor parecen irreales",
        "Me siento como si fuera otra persona",
        "No estoy seguro(a) si lo que recuerdo realmente ocurrió",
        "Encuentro cosas mías que no recuerdo haber comprado",
        "Encuentro notas o dibujos que no recuerdo haber hecho",
        "Encuentro ropa mía que no recuerdo haber usado",
        "Encuentro evidencia de haber hecho cosas que no recuerdo",
        "Me encuentro en un lugar sin saber cómo llegué",
        "Me encuentro vestido(a) de forma diferente a como recuerdo",
        "Olvido cosas importantes de mi vida personal",
        "Olvido cómo hacer algo que sé hacer",
        "Olvido información personal importante",
        "Olvido eventos importantes de mi vida",
        "Olvido conversaciones enteras",
        "Olvido dónde puse las cosas",
        "Olvido lo que acabo de decir o hacer",
        "Olvido lo que acabo de pensar",
        "Olvido lo que otra persona acaba de decir",
        "Olvido mi nombre o datos personales básicos",
    ]
    return build_instrument_pdf(
        "des-ii-experiencias-disociativas-espanol.pdf",
        "DES-II en Español",
        "Dissociative Experiences Scale-II",
        "Indique qué tan frecuentemente le ocurre cada experiencia en la <b>vida diaria</b> "
        "(no solo bajo alcohol o drogas). 28 ítems. Tiempo: 10 min.",
        items,
        "<b>PUNTAJE MEDIO:</b> _____ / 100 · <b>Corte sugerido:</b> ≥ 30",
        ["Puntaje medio", "Nivel", "Acción sugerida"],
        [
            ["0 – 19", "Normal", "Sin intervención específica"],
            ["20 – 29", "Leve", "Monitoreo; explorar estrés"],
            ["30 – 49", "Moderado", "Evaluación clínica de disociación"],
            ["50 – 100", "Severo", "Evaluación especializada; trastorno disociativo"],
        ],
        "Integra DES-II en evaluaciones de disociación con Kalyo — kalyo.io",
        "Carlson EB, Putnam FW. An update on the DES. Dissociation. 1993;6(1):16-27.",
        scale_note="0% = Nunca · 25% = Rara vez · 50% = A veces · 75% = A menudo · 100% = Casi siempre",
        scale_headers=DES_PERCENT,
    )


# ---------------------------------------------------------------------------
# Lote 3 — cognición, TDAH, sueño, funciones ejecutivas
# ---------------------------------------------------------------------------

def gen_mmse():
    items = [
        "Orientación temporal: ¿Qué día es hoy? ¿Fecha? ¿Mes? ¿Año? ¿Estación?",
        "Orientación espacial: ¿Dónde estamos? ¿País? ¿Ciudad? ¿Lugar? ¿Piso?",
        "Registro (memoria inmediata): Repetir 3 palabras (p. ej. manzana, centavo, mesa)",
        "Atención y cálculo: Restar 7 de 100 consecutivamente (o deletrear MUNDO al revés)",
        "Recuerdo diferido: Recordar las 3 palabras del registro (sin pistas)",
        "Lenguaje — Denominación: Señalar y nombrar objetos (reloj, lápiz)",
        "Repetición: Repetir frase compleja (p. ej. «Ni sí, ni no, ni pero»)",
        "Comprensión — Orden de 3 pasos: «Tome el papel, dóblelo y póngalo en el suelo»",
        "Lectura: Leer y obedecer orden escrita «CIERRE LOS OJOS»",
        "Escritura: Escribir una oración completa con sujeto y verbo",
        "Copia: Copiar el dibujo de dos pentágonos entrelazados",
    ]
    return build_instrument_pdf(
        "mmse-mini-mental-estado-mental-espanol.pdf",
        "MMSE en Español",
        "Mini-Mental State Examination — Estado mental",
        "<b>Heteroaplicada</b> (10–15 min). Evalúa orientación, memoria, atención, lenguaje y praxias. "
        "Puntaje total 0–30. Ajustar por escolaridad según normas locales.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 30",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["24 – 30", "Normal", "Sin deterioro significativo"],
            ["18 – 23", "Deterioro leve", "Evaluación neuropsicológica ampliada"],
            ["10 – 17", "Deterioro moderado", "Estudio etiológico; seguimiento"],
            ["0 – 9", "Deterioro severo", "Evaluación neurológica/psiquiátrica urgente"],
        ],
        "Registra MMSE y seguimiento cognitivo con Kalyo — kalyo.io",
        "Folstein MF, Folstein SE, McHugh PR. Mini-Mental State. J Psychiatr Res. 1975;12(3):189-198.",
        scale_note="Puntúe cada sección según manual MMSE (0–30 total). Marque ítems completados correctamente.",
        scale_headers=["OK", "—"],
    )


def gen_moca():
    items = [
        "Visuoespacial/ ejecutivo: Trail Making B alternado + cubo + reloj (0–5)",
        "Denominación: Identificar 3 animales con imágenes (0–3)",
        "Memoria: Registrar 5 palabras para recuerdo diferido (sin puntaje inmediato)",
        "Atención: Restar 7 de 100 (3 restas) + deletrear MUNDO al revés (0–6)",
        "Lenguaje: Repetir 2 frases + fluencia verbal (≥11 palabras en 60 s) (0–3)",
        "Abstracción: Similitudes entre pares (tren-bicicleta; regla-escalera) (0–2)",
        "Recuerdo diferido: Recordar 5 palabras sin pistas (0–5)",
        "Orientación: Fecha, mes, año, día, lugar, ciudad (0–6)",
    ]
    return build_instrument_pdf(
        "moca-evaluacion-cognitiva-espanol.pdf",
        "MoCA en Español",
        "Montreal Cognitive Assessment — Evaluación cognitiva breve",
        "<b>Heteroaplicada</b> (10 min). Detecta deterioro cognitivo leve mejor que MMSE. "
        "Puntaje 0–30. Sumar +1 si escolaridad ≤12 años.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 30 · <b>Corte:</b> &lt; 26 sugiere deterioro cognitivo",
        ["Puntaje", "Interpretación", "Acción sugerida"],
        [
            ["26 – 30", "Normal", "Monitoreo según contexto clínico"],
            ["18 – 25", "Deterioro leve (MCI)", "Evaluación neuropsicológica completa"],
            ["10 – 17", "Deterioro moderado", "Estudio etiológico; plan de cuidados"],
            ["0 – 9", "Deterioro severo", "Derivación especializada urgente"],
        ],
        "Documenta MoCA y evolución cognitiva con Kalyo — kalyo.io",
        "Nasreddine ZS et al. The MoCA. J Am Geriatr Soc. 2005;53(4):695-699. Validación en español.",
        scale_note="Consulte manual MoCA para puntuación detallada por subprueba.",
        scale_headers=["Pts", "—"],
    )


def gen_asrs():
    items = [
        "¿Qué tan a menudo tiene dificultad para terminar los detalles finales de un proyecto?",
        "¿Qué tan a menudo le cuesta ordenar las cosas cuando debe hacer una tarea?",
        "¿Qué tan a menudo tiene problemas para recordar citas u obligaciones?",
        "¿Qué tan a menudo evita o retrasa empezar tareas que requieren mucho pensamiento?",
        "¿Qué tan a menudo mueve las manos o los pies cuando debe quedarse sentado(a)?",
        "¿Qué tan a menudo se siente demasiado activo(a) y obligado(a) a hacer cosas?",
        "¿Qué tan a menudo comete errores por descuido en tareas aburridas o difíciles?",
        "¿Qué tan a menudo le cuesta mantener la atención en tareas o actividades?",
        "¿Qué tan a menudo le cuesta escuchar cuando le hablan directamente?",
        "¿Qué tan a menudo pierde cosas necesarias para tareas o actividades?",
        "¿Qué tan a menudo se distrae con estímulos o pensamientos externos?",
        "¿Qué tan a menudo olvida lo que iba a hacer en actividades cotidianas?",
        "¿Qué tan a menudo interrumpe a otros cuando están ocupados?",
        "¿Qué tan a menudo tiene dificultad para esperar su turno?",
        "¿Qué tan a menudo interrumpe conversaciones o actividades ajenas?",
        "¿Qué tan a menudo habla en exceso?",
        "¿Qué tan a menudo termina frases de otros o responde antes de que terminen?",
        "¿Qué tan a menudo le cuesta hacer actividades de ocio en silencio?",
    ]
    return build_instrument_pdf(
        "asrs-tdah-adultos-espanol.pdf",
        "ASRS v1.1 en Español",
        "Adult ADHD Self-Report Scale — TDAH en adultos",
        "Autoreporte sobre los <b>últimos 6 meses</b>. Parte A: ítems 1–6 (tamizaje). "
        "Parte B: ítems 7–18. Escala 0–4. Tiempo: 5 min.",
        items,
        "<b>Parte A (tamizaje):</b> _____ ítems positivos · <b>Total:</b> _____ / 72",
        ["Criterio", "Resultado", "Acción sugerida"],
        [
            ["Parte A ≥4 ítems", "Positivo", "Evaluación clínica estructurada de TDAH"],
            ["Parte A &lt;4", "Negativo", "Descartar TDAH si clínica compatible"],
            ["Parte B elevada", "Síntomas significativos", "Confirmar con entrevista DIVA o equivalente"],
        ],
        "Tamiza TDAH en adultos con ASRS y registra en Kalyo — kalyo.io",
        "Kessler RC et al. The World Health Organization ASRS. Psychol Med. 2005;35(2):245-256.",
        scale_note="0 = Nunca · 1 = Rara vez · 2 = A veces · 3 = A menudo · 4 = Muy a menudo",
        scale_headers=LIKERT_0_4,
    )


def gen_conners3():
    items = [
        "Inquietud motora",
        "Dificultad para permanecer sentado(a)",
        "Actuar sin pensar",
        "Interrumpir a otros",
        "Dificultad para esperar turno",
        "Hablar en exceso",
        "Impulsividad verbal",
        "Distracción por estímulos externos",
        "Dificultad para mantener atención",
        "Olvidos frecuentes",
        "Pérdida de objetos necesarios",
        "Evitar tareas que requieren esfuerzo mental",
        "Dificultad para organizar tareas",
        "Errores por descuido",
        "Dificultad para seguir instrucciones",
        "Abandono de tareas sin terminar",
        "Dificultad para escuchar cuando le hablan",
        "Mala gestión del tiempo",
        "Problemas para planificar",
        "Dificultad para terminar proyectos",
        "Impulsividad en decisiones",
        "Dificultad para controlar emociones",
        "Baja tolerancia a la frustración",
        "Conducta desafiante",
        "Problemas con pares",
        "Bajo rendimiento académico por desorganización",
    ]
    return build_instrument_pdf(
        "conners-3-tdah-breve-espanol.pdf",
        "Conners 3 — Breve en Español",
        "Conners 3rd Edition — Formulario breve (adaptación clínica)",
        "Informe de padres/madres o docentes sobre el <b>último mes</b>. 26 ítems representativos, escala 0–3. "
        "Consulte manual Conners 3 para enunciados completos y puntuación estandarizada T.",
        items,
        "<b>PUNTAJE BRUTO:</b> _____ · <b>T estandarizada:</b> _____ (consultar manual)",
        ["T score", "Nivel", "Acción sugerida"],
        [
            ["≤ 59", "Normal", "Monitoreo rutinario"],
            ["60 – 64", "Levemente elevado", "Observación clínica"],
            ["65 – 69", "Moderadamente elevado", "Evaluación integral de TDAH"],
            ["≥ 70", "Marcadamente elevado", "Diagnóstico diferencial; intervención"],
        ],
        "Integra Conners 3 en evaluaciones de TDAH con Kalyo — kalyo.io",
        "Conners CK. Conners 3rd Edition Manual. Multi-Health Systems. 2008. Uso profesional con licencia.",
        scale_note="0 = Nada/Para nada · 1 = Solo un poco · 2 = Bastante · 3 = Mucho/Muy frecuente",
        scale_headers=LIKERT_4_SHORT,
    )


def gen_snap_iv():
    items = [
        "A menudo no presta atención a detalles o comete errores por descuido",
        "A menudo le cuesta mantener la atención en tareas o juegos",
        "A menudo parece no escuchar cuando le hablan directamente",
        "A menudo no sigue instrucciones y no termina tareas",
        "A menudo le cuesta organizar tareas y actividades",
        "A menudo evita tareas que requieren esfuerzo mental sostenido",
        "A menudo pierde cosas necesarias para tareas",
        "A menudo se distrae fácilmente con estímulos externos",
        "A menudo es olvidadizo(a) en actividades cotidianas",
        "A menudo mueve manos o pies o se retuerce en el asiento",
        "A menudo se levanta del asiento en situaciones inapropiadas",
        "A menudo corre o trepa en exceso cuando no es apropiado",
        "A menudo le cuesta jugar o participar en actividades en silencio",
        "A menudo está «en marcha» o actúa como «impulsado por motor»",
        "A menudo habla en exceso",
        "A menudo responde antes de que terminen la pregunta",
        "A menudo le cuesta esperar su turno",
        "A menudo interrumpe o se entromete en lo que hacen otros",
        "A menudo pierde los estribos",
        "A menudo discute con adultos",
        "A menudo desafía activamente a adultos o se niega a obedecer",
        "A menudo molesta deliberadamente a otras personas",
        "A menudo culpa a otros de sus errores o conducta",
        "A menudo es susceptible o se molesta fácilmente",
        "A menudo está enojado(a) o resentido(a)",
        "A menudo es malhumorado(a) o hostil",
    ]
    return build_instrument_pdf(
        "snap-iv-tdah-ninos-espanol.pdf",
        "SNAP-IV en Español",
        "Swanson, Nolan and Pelham Rating Scale — TDAH y oposición",
        "Informe de padres/madres o docentes. 26 ítems basados en criterios DSM. "
        "Subescalas: Inatención (1–9), Hiperactividad/Impulsividad (10–18), ODD (19–26). Escala 0–3.",
        items,
        "<b>Inatención:</b> _____ / 27 · <b>HI:</b> _____ / 27 · <b>ODD:</b> _____ / 24",
        ["Subescala", "Corte sugerido", "Acción sugerida"],
        [
            ["Inatención ≥1.78 promedio", "Positivo", "Evaluación clínica de TDAH"],
            ["HI ≥1.44 promedio", "Positivo", "Confirmar con entrevista y observación"],
            ["ODD ≥1.88 promedio", "Positivo", "Evaluar trastorno oposicionista"],
        ],
        "Registra SNAP-IV y seguimiento pediátrico con Kalyo — kalyo.io",
        "Swanson JM et al. SNAP-IV Rating Scale. Int J Methods Psychiatr Res. 2001. Validación en español.",
        scale_note="0 = Nada · 1 = Solo un poco · 2 = Bastante · 3 = Mucho",
        scale_headers=LIKERT_4_SHORT,
    )


def gen_brief_a():
    items = [
        "Me distraigo fácilmente",
        "Actúo sin pensar",
        "Tengo problemas para organizarme",
        "Me cuesta terminar lo que empiezo",
        "Pierdo cosas que necesito",
        "Olvido lo que debo hacer",
        "Me cuesta cambiar de una actividad a otra",
        "Me cuesta planificar con anticipación",
        "Tengo dificultad para priorizar tareas",
        "Me cuesta iniciar tareas aburridas",
        "Me cuesta controlar impulsos emocionales",
        "Reacciono exageradamente a situaciones",
        "Me cuesta regular mi estado de ánimo",
        "Interrumpo a otros",
        "Hablo sin pensar en las consecuencias",
        "Me cuesta esperar mi turno",
        "Tomo decisiones impulsivas",
        "Me cuesta mantener la atención",
        "Pierdo la concentración con facilidad",
        "Me cuesta seguir instrucciones complejas",
        "Olvido instrucciones recientes",
        "Me cuesta recordar lo que acabo de leer",
        "Necesito que me repitan las cosas",
        "Me cuesta encontrar palabras adecuadas",
        "Me cuesta expresar mis ideas con claridad",
        "Me cuesta entender lo que leo",
        "Me cuesta resolver problemas cotidianos",
        "Me cuesta adaptarme a cambios inesperados",
        "Me cuesta manejar múltiples tareas a la vez",
        "Me siento abrumado(a) con demandas diarias",
        "Me cuesta usar el tiempo eficientemente",
        "Llego tarde a citas o compromisos",
        "Me cuesta estimar cuánto tardará una tarea",
        "Dejo tareas importantes para el último momento",
        "Me cuesta mantener rutinas organizadas",
        "Tengo problemas para autorregularme",
    ]
    return build_instrument_pdf(
        "brief-a-funciones-ejecutivas-espanol.pdf",
        "BRIEF-A en Español",
        "Behavior Rating Inventory of Executive Function — Adult Version (36 ítems clave)",
        "Autoinforme o informe de familiar sobre las <b>últimas 2 semanas</b>. "
        "36 ítems clave de 9 subescalas (0–3). Consulte manual BRIEF-A para puntuación T.",
        items,
        "<b>PUNTAJE BRUTO:</b> _____ · <b>Índices:</b> BRI, MI, GEC (consultar manual)",
        ["T score", "Nivel", "Acción sugerida"],
        [
            ["≤ 59", "Normal", "Funciones ejecutivas dentro de rango"],
            ["60 – 64", "Levemente elevado", "Monitoreo; estrategias compensatorias"],
            ["65 – 69", "Moderadamente elevado", "Evaluación neuropsicológica"],
            ["≥ 70", "Marcadamente elevado", "Intervención en funciones ejecutivas"],
        ],
        "Evalúa funciones ejecutivas con BRIEF-A en Kalyo — kalyo.io",
        "Roth RM, Isquith PK, Gioia GA. BRIEF-A Manual. PAR. 2005. Uso profesional con licencia.",
        scale_note="0 = Nunca · 1 = A veces · 2 = A menudo · 3 = Muy a menudo",
        scale_headers=LIKERT_4_SHORT,
    )


def gen_isi():
    items = [
        "Dificultad para conciliar el sueño (quedarse dormido)",
        "Dificultad para mantener el sueño (despertares nocturnos)",
        "Problemas de despertar demasiado temprano",
        "¿Qué tan satisfecho(a) está con su patrón de sueño actual?",
        "¿En qué medida considera que su problema de sueño interfiere con su funcionamiento diario?",
        "¿Qué tan notorio es su problema de sueño para los demás?",
        "¿Qué tan preocupado(a) está por su problema de sueño?",
    ]
    return build_instrument_pdf(
        "isi-indice-severidad-insomnio-espanol.pdf",
        "ISI en Español",
        "Insomnia Severity Index — Índice de severidad del insomnio",
        "Autoreporte sobre las <b>últimas 2 semanas</b>. 7 ítems, escala 0–4. "
        "Ítems 4–7 evalúan impacto y preocupación. Tiempo: 2 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 28",
        ["Puntaje", "Severidad", "Acción sugerida"],
        [
            ["0 – 7", "Sin insomnio clínico", "Higiene del sueño"],
            ["8 – 14", "Insomnio subclínico", "Intervención breve; monitoreo"],
            ["15 – 21", "Insomnio clínico moderado", "CBT-I o tratamiento activo"],
            ["22 – 28", "Insomnio clínico severo", "Tratamiento especializado urgente"],
        ],
        "Registra ISI y evolución del sueño con Kalyo — kalyo.io",
        "Bastien CH, Vallières A, Morin CM. Validation of the ISI. Sleep. 2001;24(4):401-407.",
        scale_note="0 = Ninguna · 4 = Muy severa (ítems 1–3 y 4–7 según manual ISI)",
        scale_headers=LIKERT_0_4,
    )


def gen_psqi():
    items = [
        "Hora habitual de acostarse",
        "Tiempo para conciliar el sueño (minutos)",
        "Hora habitual de levantarse",
        "Horas de sueño efectivo por noche",
        "Frecuencia de dificultad para conciliar el sueño (30 min)",
        "Frecuencia de despertares nocturnos",
        "Frecuencia de levantarse para ir al baño",
        "Frecuencia de dificultad para respirar",
        "Frecuencia de tos o ronquidos fuertes",
        "Frecuencia de sensación de frío",
        "Frecuencia de sensación de calor",
        "Frecuencia de pesadillas",
        "Frecuencia de dolor que interrumpe el sueño",
        "Frecuencia de otras razones que interrumpen el sueño",
        "Calidad global del sueño (autoevaluación)",
        "Frecuencia de uso de medicación para dormir",
        "Frecuencia de somnolencia diurna al conducir/comer",
        "Frecuencia de entusiasmo para realizar tareas",
        "¿Tiene compañero(a) de cama? ¿Observa ronquidos, pausas respiratorias?",
    ]
    return build_instrument_pdf(
        "psqi-indice-calidad-sueno-espanol.pdf",
        "PSQI en Español",
        "Pittsburgh Sleep Quality Index — Calidad del sueño",
        "Autoreporte sobre el <b>último mes</b>. 19 componentes agrupados en 7 dominios. "
        "Tiempo: 5–10 min. Puntaje global 0–21.",
        items,
        "<b>PUNTAJE GLOBAL:</b> _____ / 21 · <b>Corte:</b> &gt; 5 = mala calidad de sueño",
        ["Puntaje", "Calidad", "Acción sugerida"],
        [
            ["0 – 5", "Buena calidad", "Mantener higiene del sueño"],
            ["6 – 10", "Mala calidad leve", "Intervención en hábitos de sueño"],
            ["11 – 15", "Mala calidad moderada", "CBT-I; evaluar trastornos del sueño"],
            ["16 – 21", "Mala calidad severa", "Estudio polisomnográfico; tratamiento"],
        ],
        "Documenta PSQI y seguimiento del sueño con Kalyo — kalyo.io",
        "Buysse DJ et al. The PSQI. Psychiatry Res. 1989;28(2):193-213. Validación en español.",
        scale_note="Consulte clave PSQI para puntuación por componentes (0–3 cada uno).",
        scale_headers=LIKERT_4_SHORT,
    )


def gen_ess():
    items = [
        "Sentado(a) y leyendo",
        "Viendo televisión",
        "Sentado(a) inactivo(a) en un lugar público (teatro, reunión)",
        "Como pasajero(a) en un auto por una hora sin parar",
        "Recostado(a) para descansar por la tarde cuando las circunstancias lo permiten",
        "Sentado(a) conversando con alguien",
        "Sentado(a) quieto(a) después de comer sin haber bebido alcohol",
        "En un auto detenido por unos minutos en el tráfico",
    ]
    return build_instrument_pdf(
        "ess-escala-somnolencia-epworth-espanol.pdf",
        "ESS en Español",
        "Epworth Sleepiness Scale — Somnolencia diurna",
        "¿Qué probabilidad tiene de quedarse dormido(a) (no solo cansado) en cada situación? "
        "Evalúe la <b>vida reciente normal</b>. 8 ítems, escala 0–3. Tiempo: 2 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 24 · <b>Corte:</b> ≥ 10 = somnolencia excesiva",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["0 – 9", "Normal", "Sin somnolencia patológica"],
            ["10 – 14", "Somnolencia leve-moderada", "Evaluar higiene del sueño; descartar apnea"],
            ["15 – 18", "Somnolencia moderada-severa", "Estudio del sueño recomendado"],
            ["19 – 24", "Somnolencia severa", "Derivación urgente a medicina del sueño"],
        ],
        "Registra ESS y evaluación de somnolencia con Kalyo — kalyo.io",
        "Johns MW. A new method for measuring daytime sleepiness: the ESS. Sleep. 1991;14(6):540-545.",
        scale_note="0 = Ninguna · 1 = Baja · 2 = Moderada · 3 = Alta probabilidad de dormirse",
        scale_headers=LIKERT_4_SHORT,
    )


def gen_wurs():
    items = [
        "¿Activo(a), inquieto(a), siempre en movimiento?",
        "¿Miedoso(a), sensible, fácil de llorar?",
        "¿Concentración pobre, fácilmente distraído(a)?",
        "¿Ansioso(a), preocupado(a)?",
        "¿Nervioso(a), tenso(a)?",
        "¿Inseguro(a), baja autoestima?",
        "¿Irritable, arrebatos de ira?",
        "¿Temperamental, cambios de humor?",
        "¿Impulsivo(a), actúa sin pensar?",
        "¿Problemas para terminar lo que empieza?",
        "¿Desorganizado(a), mala gestión del tiempo?",
        "¿Problemas para despertarse por la mañana?",
        "¿Sueño inquieto, difícil de despertar?",
        "¿Problemas de conducta en la escuela?",
        "¿Problemas con la autoridad?",
        "¿Problemas con compañeros?",
        "¿Castigado(a) con frecuencia?",
        "¿Problemas con padres/madres?",
        "¿Mal rendimiento escolar a pesar de inteligencia?",
        "¿Repetidor(a) de grado?",
        "¿Suspendido(a) o expulsado(a)?",
        "¿Problemas de aprendizaje?",
        "¿Dificultad para leer o escribir?",
        "¿Problemas de coordinación motora?",
        "¿Historial familiar de TDAH o trastornos similares?",
    ]
    return build_instrument_pdf(
        "wurs-tdah-infancia-adultos-espanol.pdf",
        "WURS en Español",
        "Wender Utah Rating Scale — TDAH retrospectivo en adultos",
        "Recuerde cómo era entre los <b>8 y 12 años</b>. 25 ítems, escala 0–4. "
        "Tamizaje retrospectivo de TDAH en la infancia. Tiempo: 5 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 100 · <b>Corte sugerido:</b> ≥ 46",
        ["Puntaje", "Resultado", "Acción sugerida"],
        [
            ["0 – 45", "Negativo", "TDAH infantil retrospectivo poco probable"],
            ["46 – 70", "Positivo", "Complementar con ASRS y entrevista clínica"],
            ["71 – 100", "Muy positivo", "Evaluación integral de TDAH en adultos"],
        ],
        "Evalúa TDAH retrospectivo con WURS en Kalyo — kalyo.io",
        "Ward MF, Wender PH, Reimherr FW. The WURS. Am J Psychiatry. 1993;150(6):885-890.",
        scale_note="0 = Nada/Para nada · 1 = Solo un poco · 2 = Bastante · 3 = Mucho · 4 = Muy mucho",
        scale_headers=LIKERT_0_4,
    )


# ---------------------------------------------------------------------------
# Lote 4 — sustancias, burnout, estrés, bienestar
# ---------------------------------------------------------------------------

def gen_audit():
    items = [
        "¿Con qué frecuencia consume alguna bebida alcohólica?",
        "¿Cuántas bebidas alcohólicas consume un día típico cuando bebe?",
        "¿Con qué frecuencia toma 6 o más bebidas en una sola ocasión?",
        "¿Con qué frecuencia no pudo dejar de beber una vez había empezado?",
        "¿Con qué frecuencia no pudo hacer lo que se esperaba de usted por haber bebido?",
        "¿Con qué frecuencia necesitó beber en la mañana para recuperarse?",
        "¿Con qué frecuencia se sintió culpable o con remordimientos por haber bebido?",
        "¿Con qué frecuencia no pudo recordar lo ocurrido la noche anterior por haber bebido?",
        "¿Ha resultado herido(a) usted o alguien más por haber bebido?",
        "¿Algún familiar, amigo, médico o profesional ha mostrado preocupación por su consumo?",
    ]
    return build_instrument_pdf(
        "audit-test-alcoholismo-espanol.pdf",
        "AUDIT en Español",
        "Alcohol Use Disorders Identification Test — OMS",
        "Autoreporte sobre los <b>últimos 12 meses</b>. 10 ítems, escala 0–4 (ítems 9–10: 0/2/4). "
        "Tiempo: 2–5 min. Tamizaje de consumo de riesgo y dependencia.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 40",
        ["Puntaje", "Riesgo", "Acción sugerida"],
        [
            ["0 – 7", "Bajo riesgo", "Psicoeducación sobre consumo"],
            ["8 – 15", "Consumo de riesgo", "Intervención breve; consejo médico"],
            ["16 – 19", "Consumo perjudicial", "Tratamiento breve o derivación"],
            ["20 – 40", "Probable dependencia", "Evaluación especializada en adicciones"],
        ],
        "Tamiza consumo de alcohol con AUDIT en Kalyo — kalyo.io",
        "Babor TF, Higgins-Biddle JC, Saunders JB, Monteiro MG. AUDIT Manual. WHO. 2001.",
        scale_note="0 = Nunca · 1 = Mensual o menos · 2 = 2–4 veces/mes · 3 = 2–3/semana · 4 = 4+/semana",
        scale_headers=LIKERT_0_4,
    )


def gen_audit_c():
    items = [
        "¿Con qué frecuencia consume alguna bebida alcohólica?",
        "¿Cuántas bebidas alcohólicas consume un día típico cuando bebe?",
        "¿Con qué frecuencia toma 6 o más bebidas en una sola ocasión?",
    ]
    return build_instrument_pdf(
        "audit-c-tamizaje-alcohol-breve-espanol.pdf",
        "AUDIT-C en Español",
        "AUDIT-Consumption — Tamizaje breve de alcohol",
        "Autoreporte sobre los <b>últimos 12 meses</b>. 3 ítems del AUDIT completo. "
        "Tiempo: 1 min. Corte ≥4 (hombres) o ≥3 (mujeres) sugiere consumo de riesgo.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 12 · <b>Corte:</b> ≥ 4 (H) / ≥ 3 (M)",
        ["Puntaje", "Resultado", "Acción sugerida"],
        [
            ["0 – 3", "Negativo", "Monitoreo rutinario"],
            ["4 – 7", "Positivo (tamizaje)", "Administrar AUDIT completo"],
            ["8 – 12", "Positivo alto", "Evaluación clínica de consumo de riesgo"],
        ],
        "Tamiza alcohol con AUDIT-C y registra en Kalyo — kalyo.io",
        "Bush K et al. AUDIT-C. Arch Intern Med. 1998;158(16):1789-1795.",
        scale_note="0 = Nunca · 1 = Mensual o menos · 2 = 2–4 veces/mes · 3 = 2–3/semana · 4 = 4+/semana",
        scale_headers=LIKERT_0_4,
    )


def gen_cage():
    items = [
        "¿Ha sentido alguna vez que debería reducir su consumo de alcohol?",
        "¿Le ha molestado que la gente le critique su forma de beber?",
        "¿Se ha sentido alguna vez mal o culpable por su forma de beber?",
        "¿Se ha levantado alguna vez por la mañana necesitando beber (ojos de golpe)?",
    ]
    return build_instrument_pdf(
        "cage-tamizaje-alcoholismo-espanol.pdf",
        "CAGE en Español",
        "CAGE Questionnaire — Tamizaje de alcoholismo",
        "Autoreporte. 4 preguntas Sí/No. Tiempo: 1 min. "
        "Corte ≥2 sugiere posible dependencia alcohólica.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 4 · <b>Corte:</b> ≥ 2 positivo",
        ["Puntaje", "Resultado", "Acción sugerida"],
        [
            ["0 – 1", "Negativo", "Sin tamizaje positivo; monitoreo"],
            ["2 – 4", "Positivo", "Evaluación clínica; administrar AUDIT completo"],
        ],
        "Aplica CAGE y documenta tamizaje de alcohol en Kalyo — kalyo.io",
        "Ewing JA. Detecting alcoholism: the CAGE questionnaire. JAMA. 1984;252(14):1905-1907.",
        scale_note="Responda Sí o No a cada pregunta.",
        scale_headers=YES_NO,
    )


def gen_dast10():
    items = [
        "¿Ha usado drogas distintas del alcohol o medicamentos recetados?",
        "¿Abusa de más de una droga a la vez?",
        "¿No puede dejar de usar drogas cuando quiere?",
        "¿Ha tenido «blackouts» o flashbacks como resultado del uso?",
        "¿Se siente mal o culpable por su uso de drogas?",
        "¿Su cónyuge (o padres) se queja de su uso de drogas?",
        "¿Ha descuidado a su familia por su uso de drogas?",
        "¿Ha tenido problemas legales por su uso de drogas?",
        "¿Ha perdido amigos por su uso de drogas?",
        "¿Ha descuidado sus responsabilidades por su uso de drogas?",
    ]
    return build_instrument_pdf(
        "dast-10-deteccion-drogas-espanol.pdf",
        "DAST-10 en Español",
        "Drug Abuse Screening Test — 10 ítems",
        "Autoreporte sobre el <b>último año</b> (excepto alcohol y tabaco). "
        "10 preguntas Sí/No. Tiempo: 2 min. Corte ≥3 sugiere abuso de sustancias.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 10 · <b>Corte:</b> ≥ 3",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["0 – 2", "Bajo riesgo", "Psicoeducación; monitoreo"],
            ["3 – 5", "Moderado", "Intervención breve; evaluación clínica"],
            ["6 – 8", "Sustancial", "Tratamiento en adicciones"],
            ["9 – 10", "Severo", "Derivación urgente a servicios especializados"],
        ],
        "Tamiza abuso de drogas con DAST-10 en Kalyo — kalyo.io",
        "Skinner HA. The DAST-10. Addict Behav. 1982;7(4):363-371.",
        scale_note="Responda Sí o No. No incluya alcohol ni tabaco.",
        scale_headers=YES_NO,
    )


def gen_assist():
    items = [
        "¿Alguna vez ha consumido alguna sustancia psicoactiva (tabaco, alcohol, cannabis, cocaína, etc.)?",
        "¿Ha consumido alguna sustancia psicoactiva en los últimos 3 meses?",
        "¿Con qué frecuencia ha consumido [sustancia] en los últimos 3 meses?",
        "¿Con qué frecuencia siente un fuerte deseo o urgencia de consumir [sustancia]?",
        "¿Con qué frecuencia su consumo de [sustancia] le ha causado problemas de salud, sociales, legales o financieros?",
        "¿Con qué frecuencia ha dejado de hacer cosas que normalmente esperaba de usted por consumir [sustancia]?",
        "¿Algún amigo, familiar o profesional ha expresado preocupación por su consumo?",
        "¿Ha intentado alguna vez reducir o dejar de consumir [sustancia] sin lograrlo?",
    ]
    return build_instrument_pdf(
        "assist-evaluacion-sustancias-oms-espanol.pdf",
        "ASSIST en Español",
        "Alcohol, Smoking and Substance Involvement Screening Test — OMS",
        "Autoreporte. Repita ítems 3–8 por cada sustancia consumida en la vida. "
        "Escala de riesgo por sustancia. Tiempo: 5–10 min.",
        items,
        "<b>Riesgo por sustancia:</b> Bajo / Moderado / Alto (consultar clave ASSIST)",
        ["Riesgo", "Puntaje", "Acción sugerida"],
        [
            ["Bajo", "0 – 3", "Psicoeducación breve"],
            ["Moderado", "4 – 26", "Intervención breve (BI)"],
            ["Alto", "≥ 27", "Derivación a tratamiento especializado"],
        ],
        "Evalúa consumo de sustancias con ASSIST en Kalyo — kalyo.io",
        "WHO ASSIST Working Group. The ASSIST. Addiction. 2002;97(9):1183-1194.",
        scale_note="0 = Nunca · 2 = Mensual · 3 = Semanal · 4 = Diario o casi diario (ítems 3–8)",
        scale_headers=LIKERT_0_4,
    )


def gen_mbi():
    items = [
        "Me siento emocionalmente agotado(a) por mi trabajo",
        "Al final del día me siento agotado(a)",
        "Me siento fatigado(a) cuando me levanto por la mañana",
        "Trabajar con personas todo el día es un esfuerzo",
        "Me siento quemado(a) (burnout) por mi trabajo",
        "Siento frustración en mi trabajo",
        "Creo que estoy trabajando demasiado",
        "Trabajar directamente con personas me estresa demasiado",
        "Me siento agotado(a) por la cantidad de trabajo",
        "Siento que ya no impacto positivamente en la vida de las personas",
        "Puedo entender fácilmente cómo se sienten las personas a las que atiendo",
        "Trato eficazmente los problemas personales de las personas",
        "Siento que influyo positivamente en la vida de las personas",
        "Me siento muy enérgico(a)",
        "Puedo crear fácilmente una atmósfera relajada con las personas",
        "Me siento estimulado(a) después de trabajar con personas",
        "He logrado muchas cosas valiosas en esta profesión",
        "En mi trabajo trato los problemas emocionales con mucha calma",
        "Me siento desanimado(a) por mi trabajo",
        "Creo que trato a algunas personas como objetos impersonales",
        "Me preocupa que este trabajo me endurezca emocionalmente",
        "No me importa realmente lo que les ocurre a las personas",
    ]
    return build_instrument_pdf(
        "mbi-inventario-burnout-espanol.pdf",
        "MBI en Español",
        "Maslach Burnout Inventory — Inventario de burnout",
        "Autoreporte sobre su <b>experiencia laboral actual</b>. 22 ítems: "
        "Agotamiento emocional (9), Despersonalización (5), Realización personal (8). Escala 0–6.",
        items,
        "<b>EE:</b> _____ / 54 · <b>D:</b> _____ / 30 · <b>RP:</b> _____ / 48",
        ["Subescala", "Nivel alto", "Acción sugerida"],
        [
            ["Agotamiento emocional", "≥ 27", "Reducir carga; apoyo institucional"],
            ["Despersonalización", "≥ 13", "Supervisión clínica; balance vida-trabajo"],
            ["Realización personal baja", "≤ 31", "Intervención en burnout; cambios organizacionales"],
        ],
        "Evalúa burnout con MBI y monitorea bienestar profesional en Kalyo — kalyo.io",
        "Maslach C, Jackson SE. MBI Manual. Consulting Psychologists Press. 1986. Uso profesional.",
        scale_note="0 = Nunca · 1 = Pocas veces al año · 2 = Una vez al mes · 3 = Pocas veces al mes · "
        "4 = Una vez a la semana · 5 = Pocas veces a la semana · 6 = Todos los días",
        scale_headers=LIKERT_0_6,
    )


def gen_pss10():
    items = [
        "¿Con qué frecuencia se ha sentido perturbado(a) por algo inesperado?",
        "¿Con qué frecuencia ha sentido que no podía controlar las cosas importantes?",
        "¿Con qué frecuencia se ha sentido nervioso(a) o estresado(a)?",
        "¿Con qué frecuencia ha manejado con confianza sus problemas personales? (invertido)",
        "¿Con qué frecuencia ha sentido que las cosas le van bien? (invertido)",
        "¿Con qué frecuencia ha sentido que no podía afrontar todas las cosas que debía hacer?",
        "¿Con qué frecuencia ha podido controlar las molestias de su vida? (invertido)",
        "¿Con qué frecuencia ha sentido que dominaba la situación? (invertido)",
        "¿Con qué frecuencia se ha enfadado por cosas fuera de su control?",
        "¿Con qué frecuencia ha sentido que las dificultades se acumulaban tanto que no podía superarlas?",
    ]
    return build_instrument_pdf(
        "pss-10-escala-estres-percibido-espanol.pdf",
        "PSS-10 en Español",
        "Perceived Stress Scale — Estrés percibido",
        "Indique con qué frecuencia se ha sentido de cierta forma durante el <b>último mes</b>. "
        "10 ítems, escala 0–4. Ítems invertidos: 4, 5, 7, 8. Tiempo: 3 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 40",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["0 – 13", "Bajo estrés", "Mantener estrategias de afrontamiento"],
            ["14 – 26", "Estrés moderado", "Intervención en manejo del estrés"],
            ["27 – 40", "Estrés alto", "Evaluación clínica; intervención activa"],
        ],
        "Mide estrés percibido con PSS-10 en Kalyo — kalyo.io",
        "Cohen S, Kamarck T, Mermelstein R. A global measure of perceived stress. J Health Soc Behav. 1983.",
        scale_note="0 = Nunca · 1 = Casi nunca · 2 = A veces · 3 = A menudo · 4 = Muy a menudo",
        scale_headers=LIKERT_0_4,
    )


def gen_rosenberg():
    items = [
        "Siento que soy una persona digna de aprecio, al menos igual que los demás",
        "Creo que tengo buenas cualidades",
        "En general, me inclino a pensar que soy un(a) fracasado(a)",
        "Soy capaz de hacer las cosas tan bien como la mayoría de la gente",
        "Siento que no tengo mucho de qué enorgullecerme",
        "Tengo una actitud positiva hacia mí mismo(a)",
        "En conjunto, estoy satisfecho(a) conmigo mismo(a)",
        "Desearía tener más respeto por mí mismo(a)",
        "A veces pienso que no sirvo para nada",
        "A veces creo que no valgo nada",
    ]
    return build_instrument_pdf(
        "rosenberg-escala-autoestima-espanol.pdf",
        "Escala de Rosenberg en Español",
        "Rosenberg Self-Esteem Scale — Autoestima global",
        "Indique su grado de acuerdo con cada afirmación. 10 ítems, escala 1–4. "
        "Ítems 3, 5, 8, 9, 10 invertidos. Tiempo: 3 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 40",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["10 – 25", "Baja autoestima", "Intervención psicológica; explorar autoconcepto"],
            ["26 – 30", "Autoestima moderada", "Fortalecimiento de recursos personales"],
            ["31 – 40", "Alta autoestima", "Monitoreo rutinario"],
        ],
        "Evalúa autoestima con Rosenberg y registra en Kalyo — kalyo.io",
        "Rosenberg M. Society and the Adolescent Self-Image. Princeton University Press. 1965.",
        scale_note="1 = Totalmente en desacuerdo · 2 = En desacuerdo · 3 = De acuerdo · 4 = Totalmente de acuerdo",
        scale_headers=LIKERT_1_4,
    )


def gen_cd_risc():
    items = [
        "Puedo adaptarme cuando ocurren cambios",
        "Puedo lidiar con lo que venga",
        "Trato de ver el lado humorístico de las cosas cuando enfrento problemas",
        "Tener que lidiar con el estrés me fortalece",
        "Tiendo a recuperarme rápidamente después de enfermedad, lesión u otra dificultad",
        "Creo que puedo lograr mis metas, a pesar de los obstáculos",
        "Bajo presión, me concentro y pienso con claridad",
        "No me desanimo fácilmente por el fracaso",
        "Pienso en mí mismo(a) como una persona fuerte",
        "Puedo manejar sentimientos desagradables o dolorosos",
    ]
    return build_instrument_pdf(
        "cd-risc-resiliencia-espanol.pdf",
        "CD-RISC-10 en Español",
        "Connor-Davidson Resilience Scale — Resiliencia",
        "Indique cuánto se identifica con cada afirmación durante las <b>últimas 2 semanas</b>. "
        "10 ítems, escala 0–4. Tiempo: 3 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 40",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["0 – 19", "Resiliencia baja", "Intervención en afrontamiento y apoyo social"],
            ["20 – 29", "Resiliencia moderada", "Fortalecimiento de recursos de resiliencia"],
            ["30 – 40", "Resiliencia alta", "Mantener factores protectores"],
        ],
        "Mide resiliencia con CD-RISC-10 en Kalyo — kalyo.io",
        "Campbell-Sills L, Stein MB. Psychometric analysis of CD-RISC-10. J Trauma Stress. 2007;20(6):1019-1028.",
        scale_note="0 = Nunca · 1 = Rara vez · 2 = A veces · 3 = A menudo · 4 = Casi siempre",
        scale_headers=LIKERT_0_4,
    )


def gen_who5():
    items = [
        "Me he sentido alegre y de buen humor",
        "Me he sentido calmado(a) y relajado(a)",
        "Me he sentido activo(a) y enérgico(a)",
        "Me desperté sintiéndome fresco(a) y descansado(a)",
        "Mi vida diaria ha estado llena de cosas que me interesan",
    ]
    return build_instrument_pdf(
        "who-5-bienestar-psicologico-espanol.pdf",
        "WHO-5 en Español",
        "WHO Well-Being Index — Bienestar psicológico",
        "Durante las <b>últimas 2 semanas</b>, ¿con qué frecuencia ha experimentado cada sensación? "
        "5 ítems, escala 0–5. Tiempo: 1 min. Puntaje bruto ×4 = 0–100.",
        items,
        "<b>PUNTAJE BRUTO:</b> _____ / 25 · <b>Índice (×4):</b> _____ / 100",
        ["Índice", "Nivel", "Acción sugerida"],
        [
            ["0 – 28", "Bienestar muy bajo", "Tamizaje positivo depresión; evaluación clínica"],
            ["29 – 50", "Bienestar bajo", "Intervención en bienestar; monitoreo"],
            ["51 – 100", "Bienestar adecuado", "Mantener hábitos saludables"],
        ],
        "Tamiza bienestar psicológico con WHO-5 en Kalyo — kalyo.io",
        "Topp CW et al. The WHO-5 Well-Being Index. Psychother Psychosom. 2015;84(3):167-176.",
        scale_note="0 = En ningún momento · 1 = Algún tiempo · 2 = Menos de la mitad · "
        "3 = Más de la mitad · 4 = La mayor parte · 5 = Todo el tiempo",
        scale_headers=LIKERT_0_5,
    )


GENERATORS = [
    ("HADS", gen_hads),
    ("PCL-5", gen_pcl5),
    ("C-SSRS", gen_cssrs),
    ("IES-R", gen_ies_r),
    ("PHQ-15", gen_phq15),
    ("BHS", gen_bhs),
    ("BSSI", gen_bssi),
    ("SBQ-R", gen_sbq_r),
    ("LEC-5", gen_lec5),
    ("DES-II", gen_des_ii),
    ("MMSE", gen_mmse),
    ("MoCA", gen_moca),
    ("ASRS", gen_asrs),
    ("Conners-3", gen_conners3),
    ("SNAP-IV", gen_snap_iv),
    ("BRIEF-A", gen_brief_a),
    ("ISI", gen_isi),
    ("PSQI", gen_psqi),
    ("ESS", gen_ess),
    ("WURS", gen_wurs),
    ("AUDIT", gen_audit),
    ("AUDIT-C", gen_audit_c),
    ("CAGE", gen_cage),
    ("DAST-10", gen_dast10),
    ("ASSIST", gen_assist),
    ("MBI", gen_mbi),
    ("PSS-10", gen_pss10),
    ("Rosenberg", gen_rosenberg),
    ("CD-RISC-10", gen_cd_risc),
    ("WHO-5", gen_who5),
]

HTML_PATCHES: list[tuple[str, str, str, str]] = [
    ("hads-ansiedad-depresion-hospitalaria.html", "/assets/hads-escala-ansiedad-depresion-espanol.pdf", "HADS-espanol-Kalyo.pdf", "Descargar HADS en espa&ntilde;ol (PDF gratuito)"),
    ("escala-pcl-5-estres-postraumatico.html", "/assets/pcl-5-estres-postraumatico-espanol.pdf", "PCL-5-espanol-Kalyo.pdf", "Descargar PCL-5 en espa&ntilde;ol (PDF gratuito)"),
    ("c-ssrs-escala-columbia-suicidio.html", "/assets/c-ssrs-escala-columbia-suicidio-espanol.pdf", "C-SSRS-espanol-Kalyo.pdf", "Descargar C-SSRS en espa&ntilde;ol (PDF gratuito)"),
    ("ies-r-impacto-estres-postraumatico.html", "/assets/ies-r-impacto-estres-postraumatico-espanol.pdf", "IES-R-espanol-Kalyo.pdf", "Descargar IES-R en espa&ntilde;ol (PDF gratuito)"),
    ("phq-15-sintomas-somaticos.html", "/assets/phq-15-sintomas-somaticos-espanol.pdf", "PHQ-15-espanol-Kalyo.pdf", "Descargar PHQ-15 en espa&ntilde;ol (PDF gratuito)"),
    ("bhs-escala-desesperanza-beck.html", "/assets/bhs-escala-desesperanza-beck-espanol.pdf", "BHS-espanol-Kalyo.pdf", "Descargar BHS en espa&ntilde;ol (PDF gratuito)"),
    ("bssi-ideacion-suicida-beck.html", "/assets/bssi-ideacion-suicida-beck-espanol.pdf", "BSSI-espanol-Kalyo.pdf", "Descargar BSSI en espa&ntilde;ol (PDF gratuito)"),
    ("sbq-r-conducta-suicida.html", "/assets/sbq-r-conducta-suicida-espanol.pdf", "SBQ-R-espanol-Kalyo.pdf", "Descargar SBQ-R en espa&ntilde;ol (PDF gratuito)"),
    ("lec-5-eventos-vitales-traumaticos.html", "/assets/lec-5-eventos-vitales-traumaticos-espanol.pdf", "LEC-5-espanol-Kalyo.pdf", "Descargar LEC-5 en espa&ntilde;ol (PDF gratuito)"),
    ("des-ii-experiencias-disociativas.html", "/assets/des-ii-experiencias-disociativas-espanol.pdf", "DES-II-espanol-Kalyo.pdf", "Descargar DES-II en espa&ntilde;ol (PDF gratuito)"),
    ("mmse-mini-mental-estado-mental.html", "/assets/mmse-mini-mental-estado-mental-espanol.pdf", "MMSE-espanol-Kalyo.pdf", "Descargar MMSE en espa&ntilde;ol (PDF gratuito)"),
    ("test-moca-evaluacion-cognitiva.html", "/assets/moca-evaluacion-cognitiva-espanol.pdf", "MoCA-espanol-Kalyo.pdf", "Descargar MoCA en espa&ntilde;ol (PDF gratuito)"),
    ("asrs-tdah-adultos.html", "/assets/asrs-tdah-adultos-espanol.pdf", "ASRS-espanol-Kalyo.pdf", "Descargar ASRS en espa&ntilde;ol (PDF gratuito)"),
    ("test-conners-evaluacion-tdah.html", "/assets/conners-3-tdah-breve-espanol.pdf", "Conners-3-espanol-Kalyo.pdf", "Descargar Conners 3 (breve) en espa&ntilde;ol (PDF gratuito)"),
    ("snap-iv-tdah-ninos.html", "/assets/snap-iv-tdah-ninos-espanol.pdf", "SNAP-IV-espanol-Kalyo.pdf", "Descargar SNAP-IV en espa&ntilde;ol (PDF gratuito)"),
    ("brief-funciones-ejecutivas.html", "/assets/brief-a-funciones-ejecutivas-espanol.pdf", "BRIEF-A-espanol-Kalyo.pdf", "Descargar BRIEF-A en espa&ntilde;ol (PDF gratuito)"),
    ("isi-indice-severidad-insomnio.html", "/assets/isi-indice-severidad-insomnio-espanol.pdf", "ISI-espanol-Kalyo.pdf", "Descargar ISI en espa&ntilde;ol (PDF gratuito)"),
    ("psqi-indice-calidad-sueno.html", "/assets/psqi-indice-calidad-sueno-espanol.pdf", "PSQI-espanol-Kalyo.pdf", "Descargar PSQI en espa&ntilde;ol (PDF gratuito)"),
    ("ess-escala-somnolencia-epworth.html", "/assets/ess-escala-somnolencia-epworth-espanol.pdf", "ESS-espanol-Kalyo.pdf", "Descargar ESS en espa&ntilde;ol (PDF gratuito)"),
    ("wurs-tdah-infancia-adultos.html", "/assets/wurs-tdah-infancia-adultos-espanol.pdf", "WURS-espanol-Kalyo.pdf", "Descargar WURS en espa&ntilde;ol (PDF gratuito)"),
    ("audit-test-alcoholismo.html", "/assets/audit-test-alcoholismo-espanol.pdf", "AUDIT-espanol-Kalyo.pdf", "Descargar AUDIT en espa&ntilde;ol (PDF gratuito)"),
    ("audit-c-tamizaje-alcohol-breve.html", "/assets/audit-c-tamizaje-alcohol-breve-espanol.pdf", "AUDIT-C-espanol-Kalyo.pdf", "Descargar AUDIT-C en espa&ntilde;ol (PDF gratuito)"),
    ("cage-tamizaje-alcoholismo.html", "/assets/cage-tamizaje-alcoholismo-espanol.pdf", "CAGE-espanol-Kalyo.pdf", "Descargar CAGE en espa&ntilde;ol (PDF gratuito)"),
    ("dast-10-deteccion-drogas.html", "/assets/dast-10-deteccion-drogas-espanol.pdf", "DAST-10-espanol-Kalyo.pdf", "Descargar DAST-10 en espa&ntilde;ol (PDF gratuito)"),
    ("assist-evaluacion-sustancias-oms.html", "/assets/assist-evaluacion-sustancias-oms-espanol.pdf", "ASSIST-espanol-Kalyo.pdf", "Descargar ASSIST en espa&ntilde;ol (PDF gratuito)"),
    ("inventario-burnout-mbi.html", "/assets/mbi-inventario-burnout-espanol.pdf", "MBI-espanol-Kalyo.pdf", "Descargar MBI en espa&ntilde;ol (PDF gratuito)"),
    ("pss-10-escala-estres-percibido.html", "/assets/pss-10-escala-estres-percibido-espanol.pdf", "PSS-10-espanol-Kalyo.pdf", "Descargar PSS-10 en espa&ntilde;ol (PDF gratuito)"),
    ("rosenberg-escala-autoestima.html", "/assets/rosenberg-escala-autoestima-espanol.pdf", "Rosenberg-espanol-Kalyo.pdf", "Descargar Rosenberg en espa&ntilde;ol (PDF gratuito)"),
    ("resiliencia-cd-risc.html", "/assets/cd-risc-resiliencia-espanol.pdf", "CD-RISC-10-espanol-Kalyo.pdf", "Descargar CD-RISC-10 en espa&ntilde;ol (PDF gratuito)"),
    ("who-5-bienestar-psicologico.html", "/assets/who-5-bienestar-psicologico-espanol.pdf", "WHO-5-espanol-Kalyo.pdf", "Descargar WHO-5 en espa&ntilde;ol (PDF gratuito)"),
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
