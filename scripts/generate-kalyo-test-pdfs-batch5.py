#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Kalyo-branded clinical test PDFs (batch 5) and patch blog HTML download buttons."""

from __future__ import annotations

import re
from pathlib import Path

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
LIKERT_1_5 = ["1", "2", "3", "4", "5"]
LIKERT_1_7 = ["1", "2", "3", "4", "5", "6", "7"]
YES_NO = ["No", "Sí"]

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
# Batch 5 — salud general, ansiedad, TOC, alimentación, bipolar, pareja, resultados
# ---------------------------------------------------------------------------

def gen_scl90r():
    items = [
        "Dolores de cabeza",
        "Nerviosismo o temblores internos",
        "Pensamientos, palabras o ideas no deseadas que no puede sacar de la mente",
        "Desmayos o mareos",
        "Pérdida de interés o placer sexual",
        "Sentirse muy crítico(a) con los demás",
        "La idea de que otra persona puede controlar sus pensamientos",
        "Sentir que la mayoría de sus problemas se deben a los demás",
        "Problemas para recordar las cosas",
        "Preocuparse por ser descuidado(a) o desordenado(a)",
        "Sentirse fácilmente molesto(a) o irritado(a)",
        "Dolores en el pecho o corazón",
        "Miedo a espacios abiertos o a las calles",
        "Sentirse con poca energía o enlentecido(a)",
        "Pensamientos de quitarse la vida",
        "Oír voces que otras personas no oyen",
        "Temblores",
        "Sentir que la mayoría de las personas no son de fiar",
        "Poco apetito",
        "Llorar con facilidad",
        "Sentirse tímido(a) o incómodo(a) con el sexo opuesto",
        "Sensación de estar atrapado(a) o cogido(a)",
        "Sentirse asustado(a) de repente sin razón",
        "Arrebatos de ira que no pudo controlar",
        "Miedo a viajar en autobuses, metro o trenes",
        "Tener que comprobar y volver a comprobar lo que hace",
        "Dificultad para tomar decisiones",
        "Sentirse incómodo(a) comiendo o bebiendo en público",
        "Entrar en discusiones frecuentes",
        "Sentirse nervioso(a) cuando se queda solo(a), aunque sea poco tiempo",
        "Que los demás no le den el crédito debido por sus logros",
        "Sentirse triste",
        "Enfadarse consigo mismo(a)",
        "Dificultad para conciliar el sueño",
        "Tener que hacer las cosas muy despacio para asegurarse de que están bien",
        "Sensación de pesadez en brazos o piernas",
        "Pensamientos sobre la muerte o morir",
        "Sentirse solo(a)",
        "Sentirse decaído(a) o deprimido(a)",
        "Sentir falta de interés por las cosas",
        "Sentir que todo es un esfuerzo",
        "Ataques de terror o pánico",
        "Problemas con la ley",
        "Entrar en discusiones con otras personas",
        "Sentirse inquieto(a) e incapaz de quedarse quieto(a)",
        "Sentirse solo(a) incluso estando con otras personas",
        "Entumecimiento u hormigueo en partes del cuerpo",
        "Sensación de bloqueo en la garganta",
        "Sentirse desesperanzado(a) respecto al futuro",
        "Problemas para concentrarse",
        "Debilidad en partes del cuerpo",
        "Sentirse tenso(a) o alterado(a)",
        "Sensación de pesadez en brazos o piernas",
        "Pensamientos sobre la muerte o morir",
        "Impulsos de golpear, herir o hacer daño a alguien",
        "Impulsos de romper o destrozar cosas",
        "Miedo a salir solo(a) de casa",
        "Sentir que la gente es antipática o no le cae bien",
        "Necesidad de orinar con frecuencia",
        "Preocupaciones sobre el sexo",
        "Sentir que la mayoría de las personas están mejor que usted",
        "Alterarse con facilidad",
        "Tener pensamientos sobre sexo que le molestan mucho",
        "Sentir que los demás son culpables de la mayoría de sus problemas",
        "Sentirse aislado(a) o solo(a) respecto a los demás",
        "Tener discusiones frecuentes con otros",
        "Sentirse nervioso(a) cuando se queda solo(a)",
        "Que la gente no sea comprensiva con sus problemas",
        "Sentir que la gente no le agrada",
        "Incapacidad para terminar las cosas",
        "Problemas para respirar",
        "Sensaciones de calor o frío",
        "Tener que evitar ciertas cosas, lugares, actividades o personas porque le asustan",
        "La mente se queda en blanco",
        "Entumecimiento u hormigueo en el cuerpo",
        "Debilidad en el cuerpo",
        "Sentir que lo observan o hablan de usted",
        "Problemas con los músculos",
        "Sentir que no puede quitarse pensamientos malos",
        "Tener que lavarse o limpiarse con mucha frecuencia",
        "Sentirse inferior a los demás",
        "Dolor muscular",
        "Sentir que lo observan cuando está entre otras personas",
        "Dificultad para conciliar el sueño",
        "Tener que repetir ciertas acciones",
        "Sueño inquieto o perturbado",
        "Tener ideas o creencias que otros no comparten",
        "Sentirse muy cohibido(a) con los demás",
        "Sentirse incómodo(a) o torpe con los demás",
        "Algo en su mente que no funciona bien",
    ]
    return build_instrument_pdf(
        "scl-90-r-lista-sintomas-revisada-espanol.pdf",
        "SCL-90-R en Español",
        "Symptom Checklist-90-Revised — Lista de síntomas revisada",
        "Indique cuánto le ha molestado cada problema durante la <b>última semana</b>, "
        "incluyendo hoy. 90 ítems, escala 0–4. Tiempo: 12–15 min. "
        "<b>9 subescalas:</b> Somatización, Obsesivo-compulsivo, Sensibilidad interpersonal, "
        "Depresión, Ansiedad, Hostilidad, Ansiedad fóbica, Ideación paranoide, Psicoticismo.",
        items,
        "<b>GSI (índice global):</b> _____ · <b>PST:</b> _____ · <b>PSDI:</b> _____",
        ["Índice", "Interpretación", "Acción sugerida"],
        [
            ["GSI &lt; 0.5", "Bajo", "Monitoreo rutinario"],
            ["GSI 0.5 – 1.0", "Moderado", "Evaluación clínica ampliada"],
            ["GSI 1.0 – 2.0", "Elevado", "Intervención psicológica activa"],
            ["GSI &gt; 2.0", "Muy elevado", "Evaluación especializada urgente"],
        ],
        "Administra SCL-90-R y registra subescalas con Kalyo — kalyo.io",
        "Derogatis LR. SCL-90-R Manual. NCS Pearson. 1977. Validación en español disponible.",
        scale_note="0 = Nada · 1 = Un poco · 2 = Moderadamente · 3 = Bastante · 4 = Extremadamente",
        scale_headers=LIKERT_0_4,
    )


def gen_ghq12():
    items = [
        "¿Ha podido concentrarse bien en lo que hace?",
        "¿Ha perdido mucho sueño por preocupaciones?",
        "¿Ha sentido que está desempeñando un papel útil?",
        "¿Ha podido tomar decisiones sobre problemas cotidianos?",
        "¿Se ha sentido constantemente tenso(a) y alterado(a)?",
        "¿Ha sentido que no puede superar sus dificultades?",
        "¿Ha podido disfrutar de sus actividades normales?",
        "¿Ha podido afrontar sus problemas?",
        "¿Se ha sentido infeliz y deprimido(a)?",
        "¿Ha perdido confianza en sí mismo(a)?",
        "¿Ha pensado en sí mismo(a) como una persona que no vale nada?",
        "¿Se ha sentido razonablemente feliz, considerando todas las circunstancias?",
    ]
    return build_instrument_pdf(
        "ghq-12-cuestionario-salud-general-espanol.pdf",
        "GHQ-12 en Español",
        "General Health Questionnaire-12 — Salud general",
        "Responda según cómo se ha sentido durante las <b>últimas semanas</b>. "
        "12 ítems, escala 0–3 (método Likert o GHQ binario según protocolo). Tiempo: 2–3 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 36 · <b>Corte GHQ:</b> ≥ 12–15 sugiere malestar",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["0 – 11", "Bajo malestar", "Monitoreo rutinario"],
            ["12 – 15", "Malestar moderado", "Evaluación clínica breve"],
            ["16 – 24", "Malestar significativo", "Intervención psicológica"],
            ["25 – 36", "Malestar severo", "Evaluación integral de salud mental"],
        ],
        "Tamiza salud general con GHQ-12 en Kalyo — kalyo.io",
        "Goldberg DP, Hillier VF. A scaled version of the GHQ. Psychol Med. 1979;9(1):139-145.",
        scale_note="0 = Mejor que lo normal · 1 = Igual que siempre · 2 = Peor que lo normal · 3 = Mucho peor",
        scale_headers=LIKERT_4_SHORT,
    )


def gen_ghq28():
    items = [
        "¿Ha podido concentrarse bien en lo que hace?",
        "¿Ha perdido mucho sueño por preocupaciones?",
        "¿Ha sentido que está desempeñando un papel útil?",
        "¿Ha podido tomar decisiones sobre problemas cotidianos?",
        "¿Se ha sentido constantemente tenso(a) y alterado(a)?",
        "¿Ha sentido que no puede superar sus dificultades?",
        "¿Ha podido disfrutar de sus actividades normales?",
        "¿Ha podido afrontar sus problemas?",
        "¿Se ha sentido infeliz y deprimido(a)?",
        "¿Ha perdido confianza en sí mismo(a)?",
        "¿Ha pensado en sí mismo(a) como una persona que no vale nada?",
        "¿Se ha sentido razonablemente feliz, considerando todas las circunstancias?",
        "¿Ha tenido dolores de cabeza?",
        "¿Ha tenido sensación de presión o pesadez en la cabeza?",
        "¿Ha tenido dolores en brazos, piernas o espalda?",
        "¿Ha tenido sensación de debilidad o cansancio general?",
        "¿Ha tenido mareos o sensación de desmayo?",
        "¿Ha tenido palpitaciones o taquicardia?",
        "¿Ha tenido sensación de opresión en el pecho?",
        "¿Ha tenido dificultad para respirar sin esfuerzo?",
        "¿Ha tenido sensación de calor o sudoración excesiva?",
        "¿Ha tenido problemas digestivos o molestias abdominales?",
        "¿Ha tenido pérdida de interés por la comida?",
        "¿Ha tenido sensación de malestar o indisposición?",
        "¿Ha tenido sensación de estar enfermo(a) sin causa clara?",
        "¿Ha tenido sensación de estar perdiendo el control?",
        "¿Ha tenido sensación de que algo terrible va a ocurrir?",
        "¿Ha tenido sensación de estar al borde del pánico?",
    ]
    return build_instrument_pdf(
        "ghq-28-cuestionario-salud-general-espanol.pdf",
        "GHQ-28 en Español",
        "General Health Questionnaire-28 — Salud general ampliada",
        "Responda según las <b>últimas semanas</b>. 28 ítems: Somatización (1–7), "
        "Ansiedad/Insomnio (8–14), Disfunción social (15–21), Depresión grave (22–28). Escala 0–3.",
        items,
        "<b>TOTAL:</b> _____ / 84 · <b>Subescalas:</b> SOM _____ · ANX _____ · SOC _____ · DEP _____",
        ["Subescala", "Corte sugerido", "Acción sugerida"],
        [
            ["Somatización elevada", "≥ 5", "Descartar causa orgánica; evaluación biopsicosocial"],
            ["Ansiedad/Insomnio", "≥ 5", "Intervención en ansiedad o sueño"],
            ["Disfunción social", "≥ 4", "Evaluar funcionamiento y apoyo social"],
            ["Depresión grave", "≥ 4", "Tamizaje de depresión; intervención activa"],
        ],
        "Evalúa salud general con GHQ-28 y subescalas en Kalyo — kalyo.io",
        "Goldberg DP. Manual of the General Health Questionnaire. NFER-Nelson. 1978.",
        scale_note="0 = Mejor que lo normal · 1 = Igual · 2 = Peor · 3 = Mucho peor",
        scale_headers=LIKERT_4_SHORT,
    )


def gen_k10():
    items = [
        "¿Cuánto tiempo se sintió cansado(a) sin una buena razón?",
        "¿Cuánto tiempo se sintió nervioso(a)?",
        "¿Cuánto tiempo se sintió tan nervioso(a) que nada podía calmarle?",
        "¿Cuánto tiempo se sintió desesperanzado(a)?",
        "¿Cuánto tiempo se sintió inquieto(a) o agitado(a)?",
        "¿Cuánto tiempo se sintió tan inquieto(a) que no podía quedarse quieto(a)?",
        "¿Cuánto tiempo se sintió deprimido(a)?",
        "¿Cuánto tiempo sintió que todo era un esfuerzo?",
        "¿Cuánto tiempo se sintió tan triste que nada podía animarle?",
        "¿Cuánto tiempo se sintió sin valor?",
    ]
    return build_instrument_pdf(
        "k10-escala-distress-psicologico-espanol.pdf",
        "K10 en Español",
        "Kessler Psychological Distress Scale — Distress psicológico",
        "Durante los <b>últimos 30 días</b>, ¿cuánto tiempo le afectó cada problema? "
        "10 ítems, escala 1–5. Tiempo: 2–3 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 50",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["10 – 19", "Bienestar", "Sin intervención específica"],
            ["20 – 24", "Malestar leve", "Monitoreo; psicoeducación"],
            ["25 – 29", "Malestar moderado", "Evaluación clínica breve"],
            ["30 – 50", "Malestar severo", "Intervención activa; valorar K6 y tratamiento"],
        ],
        "Mide distress psicológico con K10 en Kalyo — kalyo.io",
        "Kessler RC et al. Short screening scales to monitor population prevalences. Psychol Med. 2002;32(6):959-976.",
        scale_note="1 = Ninguna · 2 = Un poco · 3 = A veces · 4 = La mayor parte · 5 = Todo el tiempo",
        scale_headers=LIKERT_1_5,
    )


def gen_k6():
    items = [
        "¿Cuánto tiempo se sintió nervioso(a)?",
        "¿Cuánto tiempo se sintió sin esperanza?",
        "¿Cuánto tiempo se sintió inquieto(a) o agitado(a)?",
        "¿Cuánto tiempo se sintió tan inquieto(a) que no podía quedarse quieto(a)?",
        "¿Cuánto tiempo se sintió deprimido(a)?",
        "¿Cuánto tiempo sintió que todo era un esfuerzo?",
    ]
    return build_instrument_pdf(
        "k6-tamizaje-salud-mental-espanol.pdf",
        "K6 en Español",
        "Kessler 6 — Tamizaje breve de salud mental",
        "Durante los <b>últimos 30 días</b>, ¿cuánto tiempo le afectó cada problema? "
        "6 ítems del K10, escala 1–5. Tiempo: 1 min. Corte ≥ 13 sugiere probable trastorno.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 30 · <b>Corte:</b> ≥ 13 positivo",
        ["Puntaje", "Resultado", "Acción sugerida"],
        [
            ["6 – 12", "Negativo", "Monitoreo rutinario"],
            ["13 – 18", "Positivo leve", "Evaluación clínica; considerar K10 completo"],
            ["19 – 24", "Positivo moderado", "Intervención en salud mental"],
            ["25 – 30", "Positivo severo", "Derivación a servicios especializados"],
        ],
        "Tamiza salud mental con K6 en Kalyo — kalyo.io",
        "Kessler RC et al. Screening for serious mental illness in the general population. Arch Gen Psychiatry. 2003;60(2):184-189.",
        scale_note="1 = Ninguna · 2 = Un poco · 3 = A veces · 4 = La mayor parte · 5 = Todo el tiempo",
        scale_headers=LIKERT_1_5,
    )


def gen_srq20():
    items = [
        "¿Con qué frecuencia tiene dolores de cabeza?",
        "¿Con qué frecuencia tiene falta de apetito?",
        "¿Duerme mal?",
        "¿Se asusta con facilidad?",
        "¿Tiene temblores de manos?",
        "¿Se siente nervioso(a), tenso(a) o alterado(a)?",
        "¿Tiene mala digestión?",
        "¿Tiene dificultad para pensar con claridad?",
        "¿Se siente infeliz?",
        "¿Llora con frecuencia?",
        "¿Le cuesta disfrutar de sus actividades diarias?",
        "¿Tiene dificultad para tomar decisiones?",
        "¿Tiene dificultades en su trabajo diario?",
        "¿Es incapaz de desempeñar un papel útil en su vida?",
        "¿Ha perdido interés por las cosas?",
        "¿Siente que es una persona que no vale nada?",
        "¿Tiene ideas de acabar con su vida?",
        "¿Se siente cansado(a) todo el tiempo?",
        "¿Tiene molestias en el estómago?",
        "¿Se siente agotado(a) o agobiado(a) por sus problemas?",
    ]
    return build_instrument_pdf(
        "srq-20-salud-mental-autorreportado-espanol.pdf",
        "SRQ-20 en Español",
        "Self-Reporting Questionnaire-20 — Salud mental autorreportada (OMS)",
        "Responda <b>Sí</b> o <b>No</b> según cómo se ha sentido durante los <b>últimos 30 días</b>. "
        "20 ítems. Tiempo: 5 min. Corte ≥ 8 sugiere probable trastorno mental.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 20 · <b>Corte:</b> ≥ 8 positivo",
        ["Puntaje", "Resultado", "Acción sugerida"],
        [
            ["0 – 7", "Negativo", "Monitoreo rutinario"],
            ["8 – 11", "Positivo leve", "Evaluación clínica breve"],
            ["12 – 15", "Positivo moderado", "Intervención en salud mental"],
            ["16 – 20", "Positivo severo", "Evaluación integral y derivación"],
        ],
        "Tamiza salud mental con SRQ-20 en Kalyo — kalyo.io",
        "Harding TW et al. Mental disorders in primary health care. Psychol Med. 1980;10(2):231-241. OMS.",
        scale_note="Responda Sí o No a cada pregunta.",
        scale_headers=YES_NO,
    )


def gen_stai():
    state = [
        "Me siento calmado(a)",
        "Me siento seguro(a)",
        "Estoy tenso(a)",
        "Me siento angustiado(a)",
        "Me siento a gusto",
        "Me siento alterado(a)",
        "Estoy preocupado(a) por posibles desgracias",
        "Me siento descansado(a)",
        "Me siento ansioso(a)",
        "Me siento cómodo(a)",
        "Tengo confianza en mí mismo(a)",
        "Me siento nervioso(a)",
        "Estoy relajado(a)",
        "Me siento vacilante o indeciso(a)",
        "Me siento tenso(a)",
        "Me siento satisfecho(a)",
        "Estoy preocupado(a)",
        "Me siento confundido(a) y aturdido(a)",
        "Me siento alegre",
        "Me siento bien",
    ]
    trait = [
        "Me siento bien",
        "Me canso pronto",
        "Me siento como si fuera a desmayarme",
        "Creo que las cosas me salen bien",
        "Me preocupo demasiado por cosas sin importancia",
        "Me siento descansado(a)",
        "Me siento inquieto(a), tenso(a) o alterado(a)",
        "Me siento que las dificultades se acumulan y no puedo superarlas",
        "Me preocupo demasiado por cosas que en realidad no tienen importancia",
        "Estoy feliz",
        "Me altero o perturbo con demasiada facilidad",
        "Me falta confianza en mí mismo(a)",
        "Me siento seguro(a)",
        "Evito enfrentar crisis o dificultades",
        "Me siento deprimido(a)",
        "Estoy satisfecho(a)",
        "Ideas sin importancia entran en mi mente y me molestan",
        "Me afectan pequeños contratiempos",
        "Confío en mí mismo(a)",
        "Me siento nervioso(a)",
    ]
    items = [f"[Estado] {i}" for i in state] + [f"[Rasgo] {i}" for i in trait]
    return build_instrument_pdf(
        "stai-ansiedad-estado-rasgo-espanol.pdf",
        "STAI en Español",
        "State-Trait Anxiety Inventory — Ansiedad estado y rasgo",
        "Escala 1–4. <b>STAI-E (ítems 1–20):</b> cómo se siente <b>ahora, en este momento</b>. "
        "<b>STAI-R (ítems 21–40):</b> cómo se siente <b>en general</b>. Tiempo: 10 min.",
        items,
        "<b>STAI-E:</b> _____ / 80 · <b>STAI-R:</b> _____ / 80",
        ["Subescala", "Corte orientativo", "Acción sugerida"],
        [
            ["STAI-E ≤ 39", "Ansiedad estado baja", "Monitoreo rutinario"],
            ["STAI-E 40 – 59", "Moderada", "Explorar factores situacionales"],
            ["STAI-E ≥ 60", "Alta", "Evaluación clínica de ansiedad"],
            ["STAI-R elevada", "Ansiedad rasgo", "Intervención en ansiedad crónica"],
        ],
        "Evalúa ansiedad estado-rasgo con STAI en Kalyo — kalyo.io",
        "Spielberger CD et al. Manual for the STAI. Consulting Psychologists Press. 1983.",
        scale_note="1 = Casi nunca · 2 = A veces · 3 = A menudo · 4 = Casi siempre (ítems invertidos según clave)",
        scale_headers=LIKERT_1_4,
    )


def gen_spin():
    items = [
        "Me da miedo hacer cosas mientras alguien me observa",
        "Me da miedo hacer cosas mientras otros me observan",
        "Me da miedo dar un discurso ante un grupo de personas",
        "Me da miedo intentar entablar conversación con alguien que no conozco",
        "Me da miedo hablar con personas en posición de autoridad",
        "Me da miedo hablar con personas que no conozco bien",
        "Me da miedo hablar con extraños",
        "Me da miedo ser el centro de atención",
        "Me da miedo expresar mi opinión en un grupo",
        "Me da miedo hablar con alguien a quien me atraigo",
        "Me da miedo expresar desacuerdo con alguien que no conozco bien",
        "Me da miedo hablar con alguien a quien no conozco bien",
        "Me da miedo hablar con alguien a quien acabo de conocer",
        "Me da miedo hablar con alguien a quien no conozco",
        "Me da miedo hablar con alguien a quien no conozco bien en una fiesta",
        "Me da miedo hablar con alguien a quien no conozco en una reunión social",
        "Me da miedo hablar con alguien a quien no conozco en una situación social",
    ]
    return build_instrument_pdf(
        "spin-inventario-fobia-social-espanol.pdf",
        "SPIN en Español",
        "Social Phobia Inventory — Fobia social",
        "Indique cuánto le han molestado cada uno de los problemas durante la <b>última semana</b>. "
        "17 ítems, escala 0–4. Tiempo: 5 min. Corte ≥ 19 sugiere fobia social.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 68 · <b>Corte:</b> ≥ 19 positivo",
        ["Puntaje", "Severidad", "Acción sugerida"],
        [
            ["0 – 18", "Subclínico", "Monitoreo rutinario"],
            ["19 – 29", "Leve", "Psicoeducación; intervención breve"],
            ["30 – 49", "Moderada", "TCC para ansiedad social"],
            ["50 – 68", "Severa", "Tratamiento especializado en fobia social"],
        ],
        "Evalúa fobia social con SPIN en Kalyo — kalyo.io",
        "Connor KM et al. Psychometric properties of the SPIN. Br J Psychiatry. 2000;176:379-386.",
        scale_note="0 = Nada · 1 = Leve · 2 = Moderado · 3 = Severo · 4 = Extremadamente",
        scale_headers=LIKERT_0_4,
    )


def gen_mini_spin():
    items = [
        "Miedo a causar vergüenza o humillación",
        "Miedo a ser rechazado en situaciones sociales",
        "Miedo a ser criticado por otros en situaciones sociales",
    ]
    return build_instrument_pdf(
        "mini-spin-ansiedad-social-breve-espanol.pdf",
        "Mini-SPIN en Español",
        "Mini Social Phobia Inventory — Tamizaje breve de ansiedad social",
        "Indique cuánto le han molestado durante la <b>última semana</b>. "
        "3 ítems del SPIN, escala 0–4. Tiempo: 1 min. Corte ≥ 6 positivo.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 12 · <b>Corte:</b> ≥ 6",
        ["Puntaje", "Resultado", "Acción sugerida"],
        [
            ["0 – 5", "Negativo", "Monitoreo rutinario"],
            ["6 – 8", "Positivo leve", "Administrar SPIN completo"],
            ["9 – 12", "Positivo alto", "Evaluación clínica de fobia social"],
        ],
        "Tamiza ansiedad social con Mini-SPIN en Kalyo — kalyo.io",
        "Connor KM et al. Mini-SPIN: A brief screening assessment. Depress Anxiety. 2001;14(2):137-140.",
        scale_note="0 = Nada · 1 = Leve · 2 = Moderado · 3 = Severo · 4 = Extremadamente",
        scale_headers=LIKERT_0_4,
    )


def gen_lsas():
    items = [
        "Actuar, actuar en un escenario, dar un discurso",
        "Ir a una fiesta",
        "Comer en un lugar público",
        "Beber con otras personas en lugares públicos",
        "Hablar con personas en posición de autoridad",
        "Actuar, actuar en un escenario, dar un discurso (grupo pequeño)",
        "Ir a una fiesta (conocidos)",
        "Trabajar mientras alguien observa",
        "Escribir mientras alguien observa",
        "Llamar por teléfono a alguien que no conoce bien",
        "Hablar con alguien que no conoce bien",
        "Conocer gente nueva",
        "Orinar en baño público",
        "Entrar a una habitación donde ya hay personas sentadas",
        "Ser el centro de atención",
        "Hablar en una reunión",
        "Tomar un examen",
        "Expresar desacuerdo con alguien que no conoce bien",
        "Mirar a los ojos a alguien que no conoce bien",
        "Devolver un artículo a una tienda",
        "Dar una fiesta",
        "Resistir a un vendedor insistente",
        "Entrevista de trabajo",
        "Reunión con desconocidos",
    ]
    return build_instrument_pdf(
        "lsas-ansiedad-social-liebowitz-espanol.pdf",
        "LSAS en Español",
        "Liebowitz Social Anxiety Scale — Ansiedad social",
        "Para cada situación, puntúe <b>Miedo/Ansiedad</b> (0–3) y <b>Evitación</b> (0–3) "
        "durante la <b>última semana</b>. 24 situaciones. Tiempo: 10 min.",
        items,
        "<b>Total Miedo:</b> _____ / 72 · <b>Total Evitación:</b> _____ / 72 · <b>Total LSAS:</b> _____ / 144",
        ["Puntaje total", "Severidad", "Acción sugerida"],
        [
            ["0 – 54", "Leve", "Monitoreo; psicoeducación"],
            ["55 – 64", "Moderada", "Intervención en ansiedad social"],
            ["65 – 79", "Marcada", "TCC especializada"],
            ["80 – 144", "Severa", "Tratamiento intensivo en fobia social"],
        ],
        "Evalúa ansiedad social con LSAS en Kalyo — kalyo.io",
        "Liebowitz MR. Social phobia. Mod Probl Pharmacopsychiatry. 1987;22:141-173.",
        scale_note="Miedo y Evitación: 0 = Ninguno · 1 = Leve · 2 = Moderado · 3 = Severo (puntúe ambos por situación)",
        scale_headers=["M0", "M1", "M2", "M3", "E0", "E1", "E2", "E3"],
    )


def gen_pass():
    items = [
        "Me siento tenso(a) o alterado(a)",
        "Me siento asustado(a) sin razón aparente",
        "Me siento nervioso(a)",
        "Me siento inquieto(a)",
        "Me siento tenso(a) en el cuerpo",
        "Me siento tenso(a) en los músculos",
        "Me siento tenso(a) en el pecho",
        "Me siento tenso(a) en el estómago",
        "Me siento tenso(a) en la garganta",
        "Me siento tenso(a) en la cabeza",
        "Me siento tenso(a) en las manos",
        "Me siento tenso(a) en las piernas",
        "Me siento tenso(a) en la espalda",
        "Me siento tenso(a) en el cuello",
        "Me siento tenso(a) en los hombros",
        "Me siento tenso(a) en la mandíbula",
        "Me siento tenso(a) en todo el cuerpo",
        "Me siento tenso(a) cuando pienso en cosas que me preocupan",
        "Me siento tenso(a) cuando estoy en situaciones estresantes",
        "Me siento tenso(a) cuando no sé qué va a pasar",
    ]
    return build_instrument_pdf(
        "pass-sensibilidad-ansiedad-espanol.pdf",
        "PASS en Español",
        "Panic and Agoraphobia Scale — Sensibilidad a la ansiedad / pánico",
        "Indique cuánto le han molestado durante la <b>última semana</b>. "
        "20 ítems representativos, escala 0–4. Subescalas: pánico, agorafobia, anticipación, sensación.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 80 · <b>Subescalas:</b> consultar manual PASS",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["0 – 19", "Bajo", "Monitoreo rutinario"],
            ["20 – 39", "Leve", "Psicoeducación sobre ansiedad"],
            ["40 – 59", "Moderado", "Evaluación de trastorno de pánico"],
            ["60 – 80", "Severo", "Tratamiento especializado en ansiedad/pánico"],
        ],
        "Evalúa sensibilidad a la ansiedad con PASS en Kalyo — kalyo.io",
        "Bandelow B. Assessing the efficacy of treatments for panic disorder. J Psychosom Res. 1995;39(Suppl):163-170.",
        scale_note="0 = Nada · 1 = Leve · 2 = Moderado · 3 = Severo · 4 = Extremadamente",
        scale_headers=LIKERT_0_4,
    )


def gen_pdss():
    items = [
        "Número de ataques de pánico durante la semana",
        "Distress durante los ataques de pánico",
        "Anticipación de ataques de pánico (miedo/frecuencia)",
        "Evitación de situaciones por miedo a ataques",
        "Evitación de actividades por miedo a ataques",
        "Interferencia en el trabajo por miedo a ataques",
        "Interferencia en la vida social por miedo a ataques",
    ]
    return build_instrument_pdf(
        "pdss-trastorno-panico-shear-espanol.pdf",
        "PDSS en Español",
        "Panic Disorder Severity Scale — Shear",
        "Evalúe la <b>última semana</b>. 7 ítems, escala 0–4 por ítem. "
        "<b>Heteroaplicada</b> o autoreporte guiado. Tiempo: 5 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 28",
        ["Puntaje", "Severidad", "Acción sugerida"],
        [
            ["0 – 5", "Normal", "Sin trastorno de pánico clínico"],
            ["6 – 9", "Leve", "Monitoreo; intervención breve"],
            ["10 – 13", "Moderada", "Tratamiento activo en pánico"],
            ["14 – 28", "Severa", "Tratamiento intensivo; valorar farmacoterapia"],
        ],
        "Monitorea trastorno de pánico con PDSS en Kalyo — kalyo.io",
        "Shear MK et al. Multicenter collaborative panic disorder severity scale. Am J Psychiatry. 1997;154(8):1051-1057.",
        scale_note="0 = Ninguno · 1 = Leve · 2 = Moderado · 3 = Severo · 4 = Extremadamente",
        scale_headers=LIKERT_0_4,
    )


def gen_ybocs():
    items = [
        "Tiempo ocupado por pensamientos obsesivos",
        "Interferencia de pensamientos obsesivos",
        "Distress por pensamientos obsesivos",
        "Resistencia a pensamientos obsesivos",
        "Control sobre pensamientos obsesivos",
        "Tiempo ocupado por conductas compulsivas",
        "Interferencia de conductas compulsivas",
        "Distress si se impide la compulsión",
        "Resistencia a conductas compulsivas",
        "Control sobre conductas compulsivas",
    ]
    return build_instrument_pdf(
        "y-bocs-escala-yale-brown-toc-espanol.pdf",
        "Y-BOCS en Español",
        "Yale-Brown Obsessive Compulsive Scale — TOC",
        "<b>Heteroaplicada</b> con lista de síntomas previa (10 categorías: obsesiones y compulsiones comunes). "
        "10 ítems de severidad (5 obsesiones + 5 compulsiones), escala 0–4. "
        "Completar checklist de síntomas antes de puntuar subescalas de tiempo, interferencia, "
        "distress, resistencia y control.",
        items,
        "<b>Obsesiones:</b> _____ / 20 · <b>Compulsiones:</b> _____ / 20 · <b>TOTAL Y-BOCS:</b> _____ / 40",
        ["Puntaje", "Severidad TOC", "Acción sugerida"],
        [
            ["0 – 7", "Subclínico", "Monitoreo rutinario"],
            ["8 – 15", "Leve", "Psicoeducación; TCC para TOC"],
            ["16 – 23", "Moderado", "Tratamiento activo (ERP/TCC)"],
            ["24 – 31", "Severo", "Tratamiento intensivo; valorar ISRS"],
            ["32 – 40", "Extremo", "Derivación especializada urgente"],
        ],
        "Evalúa TOC con Y-BOCS y checklist en Kalyo — kalyo.io",
        "Goodman WK et al. The Yale-Brown Obsessive Compulsive Scale. Arch Gen Psychiatry. 1989;46(11):1006-1011.",
        scale_note="0 = Ninguno · 1 = Leve · 2 = Moderado · 3 = Severo · 4 = Extremadamente (use 0–4 por subescala)",
        scale_headers=LIKERT_0_4,
    )


def gen_ocir():
    items = [
        "He guardado cosas innecesarias",
        "He revisado las cosas más veces de las necesarias",
        "He tenido pensamientos de contaminación y me he sentido sucio(a)",
        "He tenido pensamientos de hacer daño a otros",
        "He tenido pensamientos de hacer daño a mí mismo(a)",
        "He tenido pensamientos de hacer cosas inmorales",
        "He tenido pensamientos de hacer cosas prohibidas",
        "He tenido pensamientos de hacer cosas que no quiero hacer",
        "He tenido pensamientos de hacer cosas que me avergüenzan",
        "He tenido pensamientos de hacer cosas que me dan miedo",
        "He tenido pensamientos de hacer cosas que no tienen sentido",
        "He tenido pensamientos de hacer cosas que no puedo controlar",
        "He tenido pensamientos de hacer cosas que no quiero pensar",
        "He tenido pensamientos de hacer cosas que no quiero sentir",
        "He tenido pensamientos de hacer cosas que no quiero recordar",
        "He tenido pensamientos de hacer cosas que no quiero imaginar",
        "He tenido pensamientos de hacer cosas que no quiero creer",
        "He tenido pensamientos de hacer cosas que no quiero desear",
    ]
    return build_instrument_pdf(
        "oci-r-obsesiones-compulsiones-espanol.pdf",
        "OCI-R en Español",
        "Obsessive-Compulsive Inventory-Revised",
        "Indique cuánto le ha molestado cada problema durante el <b>último mes</b>. "
        "18 ítems, escala 0–4. Subescalas: lavado, orden, dudas, obsesiones, acumulación.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 72 · <b>Corte sugerido:</b> ≥ 21",
        ["Puntaje", "Resultado", "Acción sugerida"],
        [
            ["0 – 20", "Negativo", "Monitoreo rutinario"],
            ["21 – 40", "Positivo leve", "Evaluación clínica de TOC"],
            ["41 – 55", "Positivo moderado", "Tratamiento TCC/ERP"],
            ["56 – 72", "Positivo severo", "Tratamiento especializado en TOC"],
        ],
        "Tamiza TOC con OCI-R en Kalyo — kalyo.io",
        "Foa EB et al. The Obsessive-Compulsive Inventory. Psychol Assess. 2002;14(4):485-496.",
        scale_note="0 = Nada · 1 = Un poco · 2 = Moderadamente · 3 = Bastante · 4 = Extremadamente",
        scale_headers=LIKERT_0_4,
    )


def gen_epds():
    items = [
        "He podido reírme y ver el lado divertido de las cosas",
        "Me he sentido con ganas de disfrutar de las cosas",
        "Me he culpado innecesariamente cuando las cosas han ido mal",
        "Me he sentido ansioso(a) o preocupado(a) sin razón",
        "Me he sentido asustado(a) o en pánico sin razón",
        "Se me ha ido todo encima",
        "Me he sentido tan infeliz que he tenido dificultad para dormir",
        "Me he sentido triste o muy desdichado(a)",
        "Me he sentido tan infeliz que he llorado",
        "Se me han ocurrido ideas de hacerme daño",
    ]
    return build_instrument_pdf(
        "epds-depresion-postnatal-edimburgo-espanol.pdf",
        "EPDS en Español",
        "Edinburgh Postnatal Depression Scale — Depresión postnatal",
        "Marque la respuesta que mejor describe cómo se ha sentido durante la <b>última semana</b>. "
        "10 ítems, escala 0–3. Tiempo: 3 min. Corte ≥ 10 sugiere depresión postnatal.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 30 · <b>Corte:</b> ≥ 10 · <b>Ítem 10 &gt; 0:</b> evaluar riesgo",
        ["Puntaje", "Resultado", "Acción sugerida"],
        [
            ["0 – 9", "Negativo", "Monitoreo rutinario postparto"],
            ["10 – 12", "Posible depresión", "Evaluación clínica; seguimiento"],
            ["13 – 30", "Probable depresión", "Intervención activa; valorar tratamiento"],
        ],
        "Tamiza depresión postnatal con EPDS en Kalyo — kalyo.io",
        "Cox JL, Holden JM, Sagovsky R. Detection of postnatal depression. Br J Psychiatry. 1987;150:782-786.",
        scale_note="Consulte clave EPDS: algunos ítems invertidos (0 = como siempre · 3 = nunca/casi nunca)",
        scale_headers=LIKERT_4_SHORT,
    )


def gen_scoff():
    items = [
        "¿Se provoca vómitos porque se siente incómodamente lleno(a)?",
        "¿Le preocupa haber perdido el control sobre la cantidad que come?",
        "¿Ha perdido recientemente más de 6 kg (14 lb) en un período de 3 meses?",
        "¿Cree que está gordo(a) aunque otros digan que está demasiado delgado(a)?",
        "¿Diría que la comida domina su vida?",
    ]
    return build_instrument_pdf(
        "scoff-trastornos-alimentarios-espanol.pdf",
        "SCOFF en Español",
        "SCOFF Questionnaire — Tamizaje de trastornos alimentarios",
        "Responda <b>Sí</b> o <b>No</b>. 5 preguntas. Tiempo: 1 min. "
        "Corte ≥ 2 sugiere posible trastorno alimentario.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 5 · <b>Corte:</b> ≥ 2 positivo",
        ["Puntaje", "Resultado", "Acción sugerida"],
        [
            ["0 – 1", "Negativo", "Monitoreo rutinario"],
            ["2 – 3", "Positivo", "Evaluación clínica de trastorno alimentario"],
            ["4 – 5", "Positivo alto", "Derivación a equipo especializado"],
        ],
        "Tamiza trastornos alimentarios con SCOFF en Kalyo — kalyo.io",
        "Morgan JF, Reid F, Lacey JH. The SCOFF questionnaire. BMJ. 1999;319(7223):1467-1468.",
        scale_note="Responda Sí o No a cada pregunta.",
        scale_headers=YES_NO,
    )


def gen_eat26():
    items = [
        "Me asusta estar con sobrepeso",
        "Evito comer cuando tengo hambre",
        "Me preocupa mucho buscar comida",
        "He tenido episodios de atracones donde siento que no puedo parar",
        "Recorto mi comida en porciones pequeñas",
        "Conozco el contenido calórico de los alimentos que como",
        "Evito especialmente alimentos con alto contenido de carbohidratos",
        "Siento que los demás preferirían que comiera más",
        "Vomito después de comer",
        "Me siento extremadamente culpable después de comer",
        "Estoy preocupado(a) por el deseo de estar más delgado(a)",
        "Pienso en quemar calorías cuando hago ejercicio",
        "Otras personas piensan que estoy demasiado delgado(a)",
        "Estoy preocupado(a) por la idea de tener grasa en el cuerpo",
        "Tardo más que los demás en comer",
        "Evito alimentos con azúcar",
        "Como alimentos dietéticos",
        "Siento que la comida controla mi vida",
        "Muestro autocontrol en torno a la comida",
        "Siento que los demás me presionan para comer",
        "Dedico demasiado tiempo pensando en comida",
        "Me siento incómodo(a) después de comer dulces",
        "Hago dietas estrictas",
        "Me gusta sentir el estómago vacío",
        "Tengo ganas de vomitar después de comer",
        "Estoy preocupado(a) por comer en público",
    ]
    return build_instrument_pdf(
        "eat-26-trastornos-alimentarios-espanol.pdf",
        "EAT-26 en Español",
        "Eating Attitudes Test-26 — Trastornos alimentarios",
        "Indique con qué frecuencia le ocurre cada conducta. 26 ítems, escala 0–3. "
        "Tiempo: 5–10 min. Subescalas: Dieting, Bulimia, Oral control.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 78 · <b>Corte:</b> ≥ 20 positivo",
        ["Puntaje", "Resultado", "Acción sugerida"],
        [
            ["0 – 19", "Negativo", "Monitoreo rutinario"],
            ["20 – 39", "Positivo leve", "Evaluación clínica nutricional y psicológica"],
            ["40 – 78", "Positivo alto", "Derivación a equipo de trastornos alimentarios"],
        ],
        "Evalúa actitudes alimentarias con EAT-26 en Kalyo — kalyo.io",
        "Garner DM, Olmsted MP, Bohr Y, Garfinkel PE. The EAT-26. Psychol Med. 1982;12(4):871-878.",
        scale_note="0 = Nunca · 1 = Rara vez · 2 = A veces · 3 = A menudo",
        scale_headers=LIKERT_4_SHORT,
    )


def gen_edeq():
    items = [
        "¿Ha intentado limitar la cantidad de comida para influir en su forma o peso?",
        "¿Ha ido periodos largos (8+ horas) sin comer para influir en su forma o peso?",
        "¿Ha intentado excluir de su dieta alimentos que le gustan?",
        "¿Ha intentado seguir reglas estrictas sobre comer?",
        "¿Ha deseado tener un estómago vacío?",
        "¿Ha tenido un deseo intenso y irresistible de comer?",
        "¿Ha tenido episodios de comer excesivamente?",
        "¿Ha sentido que ha perdido el control sobre la cantidad que come?",
        "¿Ha tenido episodios de comer excesivamente y luego vomitar?",
        "¿Ha usado laxantes para influir en su forma o peso?",
        "¿Ha usado diuréticos para influir en su forma o peso?",
        "¿Ha hecho ejercicio excesivo para influir en su forma o peso?",
        "¿Ha tenido pensamientos sobre comer, comida o calorías?",
        "¿Ha tenido pensamientos sobre su forma corporal?",
        "¿Ha tenido pensamientos sobre su peso?",
        "¿Ha sentido que su peso ha influido en cómo piensa de sí mismo(a)?",
        "¿Ha sentido que su forma corporal ha influido en cómo piensa de sí mismo(a)?",
        "¿Ha sentido que su peso ha influido en cómo se siente?",
        "¿Ha sentido que su forma corporal ha influido en cómo se siente?",
        "¿Ha sentido disconformidad con su peso?",
        "¿Ha sentido disconformidad con su forma corporal?",
        "¿Ha sentido disconformidad con su estómago?",
        "¿Ha sentido disconformidad con sus caderas?",
        "¿Ha sentido disconformidad con sus muslos?",
        "¿Ha sentido disconformidad con su cintura?",
        "¿Ha sentido disconformidad con su aspecto general?",
        "¿Ha sentido disconformidad con otras partes del cuerpo?",
        "¿Ha sentido disconformidad con su rostro?",
    ]
    return build_instrument_pdf(
        "ede-q-cuestionario-trastornos-alimentarios-espanol.pdf",
        "EDE-Q en Español",
        "Eating Disorder Examination Questionnaire — Trastornos alimentarios",
        "Indique cuántos días de los <b>últimos 28</b> le ha ocurrido cada conducta o pensamiento. "
        "28 ítems clave, escala 0–6. Subescalas: Restricción, Comer excesivo, Preocupación forma/peso.",
        items,
        "<b>Global:</b> _____ · <b>Restricción:</b> _____ · <b>Comer excesivo:</b> _____ · <b>Forma/Peso:</b> _____",
        ["Subescala", "Elevación", "Acción sugerida"],
        [
            ["Global bajo", "Por debajo de corte", "Monitoreo rutinario"],
            ["Restricción elevada", "≥ 2.5 promedio", "Evaluación nutricional y psicológica"],
            ["Comer excesivo elevado", "≥ 2.5 promedio", "Evaluar bulimia/atracones"],
            ["Forma/peso elevada", "≥ 3.0 promedio", "Intervención en imagen corporal"],
        ],
        "Evalúa trastornos alimentarios con EDE-Q en Kalyo — kalyo.io",
        "Fairburn CG, Beglin SJ. Assessment of eating disorders: interview or self-report. Int J Eat Disord. 1994;16(4):363-370.",
        scale_note="0 = Ningún día · 1–2 = Algunos días · 3–5 = Más de la mitad · 6 = Todos los días (adaptado 0–6)",
        scale_headers=LIKERT_0_6,
    )


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


def gen_cage():
    items = [
        "¿Ha sentido alguna vez que debería reducir su consumo de alcohol?",
        "¿Le ha molestado que la gente le critique su forma de beber?",
        "¿Se ha sentido alguna vez mal o culpable por su forma de beber?",
        "¿Se ha levantado alguna vez por la mañana necesitando beber (ojos de golpe)?",
    ]
    return build_instrument_pdf(
        "cage-alcoholismo-test-espanol.pdf",
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


def gen_ymrs():
    items = [
        "Elevación del humor (euforia, irritabilidad, labilidad)",
        "Actividad motora aumentada (energía, aceleración)",
        "Interés sexual aumentado",
        "Sueño disminuido (horas de sueño)",
        "Irritabilidad (comportamiento, actitud)",
        "Habla (velocidad, cantidad, dificultad para interrumpir)",
        "Trastorno del lenguaje (lenguaje incoherente, logorrea)",
        "Contenido del pensamiento (grandiosidad, ideas de referencia, paranoia)",
        "Comportamiento agresivo o destructivo",
        "Aspecto (cuidado personal, vestimenta)",
        "Conciencia de enfermedad",
    ]
    return build_instrument_pdf(
        "ymrs-escala-mania-young-espanol.pdf",
        "YMRS en Español",
        "Young Mania Rating Scale — Manía",
        "<b>Heteroaplicada</b> por clínico. 11 ítems, escala 0–4 (algunos 0–8 en manual; "
        "use anclajes 0–4 en esta versión). Evalúe síntomas durante la <b>última semana</b>.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 60 · <b>Manía leve:</b> ≥ 12 · <b>Moderada:</b> ≥ 20",
        ["Puntaje", "Severidad", "Acción sugerida"],
        [
            ["0 – 11", "Sin manía", "Monitoreo rutinario"],
            ["12 – 19", "Manía leve", "Ajuste tratamiento; seguimiento cercano"],
            ["20 – 29", "Manía moderada", "Intervención farmacológica/psicológica activa"],
            ["30 – 60", "Manía severa", "Hospitalización / manejo de crisis"],
        ],
        "Evalúa manía con YMRS en Kalyo — kalyo.io",
        "Young RC, Biggs JT, Ziegler VE, Meyer DA. A rating scale for mania. Br J Psychiatry. 1978;133:429-435.",
        scale_note="0 = Ausente · 1 = Leve · 2 = Moderado · 3 = Severo · 4 = Muy severo (consultar manual para ítems 5, 8)",
        scale_headers=LIKERT_0_4,
    )


def gen_mdq():
    items = [
        "¿Alguna vez ha tenido un período en el que no era usted mismo(a) y se sentía muy bien o muy irritable?",
        "¿Durante ese período, se sentía mucho más seguro(a) o con más energía de lo normal?",
        "¿Durante ese período, necesitaba menos sueño de lo normal y aun así se sentía descansado(a)?",
        "¿Durante ese período, hablaba más o más rápido de lo normal?",
        "¿Durante ese período, pensaba más rápido de lo normal o no podía frenar su mente?",
        "¿Durante ese período, se distraía fácilmente y le costaba concentrarse?",
        "¿Durante ese período, tenía mucha más energía de lo normal?",
        "¿Durante ese período, era mucho más activo(a) o hacía más cosas de lo normal?",
        "¿Durante ese período, era mucho más sociable o extrovertido(a) de lo normal?",
        "¿Durante ese período, estaba mucho más interesado(a) en el sexo de lo normal?",
        "¿Durante ese período, hacía cosas inusuales o que otras personas consideraban excesivas?",
        "¿Durante ese período, gastaba dinero de forma que le causó problemas?",
        "¿Si marcó «sí» a varios ítems, ¿alguna vez ocurrió todo al mismo tiempo?",
    ]
    return build_instrument_pdf(
        "mdq-trastorno-bipolar-tamizaje-espanol.pdf",
        "MDQ en Español",
        "Mood Disorder Questionnaire — Tamizaje de trastorno bipolar",
        "Responda <b>Sí</b>, <b>No</b> o <b>Mixto</b> (sí y no en distintos momentos). "
        "13 ítems. Tiempo: 5 min. Positivo: ≥7 sí + mismo período + problemas moderados/graves.",
        items,
        "<b>Ítems «Sí»:</b> _____ / 13 · <b>Mismo período:</b> Sí/No · <b>Problemas:</b> _____",
        ["Criterio", "Resultado", "Acción sugerida"],
        [
            ["&lt;7 sí", "Negativo", "Monitoreo rutinario"],
            ["≥7 sí + mismo período", "Positivo", "Evaluación clínica de trastorno bipolar"],
            ["Positivo + problemas graves", "Alta probabilidad", "Derivación psiquiátrica especializada"],
        ],
        "Tamiza trastorno bipolar con MDQ en Kalyo — kalyo.io",
        "Hirschfeld RM et al. Development and validation of a screening instrument for bipolar disorder. Am J Psychiatry. 2000;157(11):1873-1875.",
        scale_note="Sí / No / Mixto (sí y no en distintos momentos de la vida)",
        scale_headers=["No", "Sí", "Mixto"],
    )


def gen_asrm():
    items = [
        "Me siento más feliz o alegre que lo normal",
        "Me siento más seguro(a) de mí mismo(a) que lo normal",
        "Necesito menos sueño que lo normal",
        "Me siento más activo(a) o tengo más energía que lo normal",
        "Soy más sociable o extrovertido(a) que lo normal",
    ]
    return build_instrument_pdf(
        "asrm-escala-mania-altman-espanol.pdf",
        "ASRM en Español",
        "Altman Self-Rating Mania Scale — Manía autorreportada",
        "Durante la <b>última semana</b>, indique cuánto se ha sentido así. "
        "5 ítems, escala 0–4. Tiempo: 2 min. Corte ≥6 sugiere manía.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 20 · <b>Corte:</b> ≥ 6 positivo",
        ["Puntaje", "Resultado", "Acción sugerida"],
        [
            ["0 – 5", "Negativo", "Monitoreo rutinario"],
            ["6 – 10", "Positivo leve", "Evaluación clínica de bipolaridad"],
            ["11 – 15", "Positivo moderado", "Intervención activa; valorar YMRS"],
            ["16 – 20", "Positivo alto", "Derivación psiquiátrica urgente"],
        ],
        "Tamiza manía con ASRM en Kalyo — kalyo.io",
        "Altman EG et al. The Altman Self-Rating Mania Scale. Biol Psychiatry. 1997;42(10):948-955.",
        scale_note="0 = No presente · 1 = Leve · 2 = Moderado · 3 = Severo · 4 = Muy severo",
        scale_headers=LIKERT_0_4,
    )


def gen_panss():
    positive = [
        "Delirios",
        "Desorganización conceptual",
        "Alucinaciones",
        "Excitación",
        "Grandiosidad",
        "Suspicacia/persecución",
        "Hostilidad",
    ]
    negative = [
        "Afecto embotado",
        "Retraimiento emocional",
        "Empobrecimiento del lenguaje",
        "Empobrecimiento del contenido del pensamiento",
        "Falta de espontaneidad en la conversación",
        "Anhedonia social",
        "Estereotipias motoras",
    ]
    general = [
        "Ansiedad somática",
        "Ansiedad psíquica",
        "Sentimientos de culpa",
        "Tensión",
        "Manierismos y pos tura",
        "Depresión",
        "Retardo motor",
        "Falta de cooperación",
        "Contenido de pensamiento inusual",
        "Desorientación",
        "Atención deficiente",
        "Falta de juicio e insight",
        "Evitación de contacto social",
        "Disturbios volitivos",
        "Impulsividad",
        "Preocupación somática",
    ]
    items = [f"[Positiva] {i}" for i in positive] + [f"[Negativa] {i}" for i in negative] + [f"[General] {i}" for i in general]
    return build_instrument_pdf(
        "panss-esquizofrenia-espanol.pdf",
        "PANSS en Español",
        "Positive and Negative Syndrome Scale — Esquizofrenia",
        "<b>Heteroaplicada</b> por clínico entrenado. 30 ítems: 7 positivos + 7 negativos + 16 generales. "
        "Escala 1–7. Tiempo: 30–45 min. Basada en entrevista clínica estructurada.",
        items,
        "<b>Positiva:</b> _____ / 49 · <b>Negativa:</b> _____ / 49 · <b>General:</b> _____ / 112 · <b>TOTAL:</b> _____ / 210",
        ["Subescala", "Rango", "Acción sugerida"],
        [
            ["Positiva elevada", "≥ 20", "Ajuste antipsicótico; manejo de síntomas positivos"],
            ["Negativa elevada", "≥ 20", "Rehabilitación psicosocial; psicoterapia"],
            ["General elevada", "≥ 40", "Evaluación integral; manejo de comorbilidad"],
            ["Total ≥ 75", "Psicosis activa", "Intervención farmacológica y seguimiento intensivo"],
        ],
        "Documenta PANSS y evolución en psicosis con Kalyo — kalyo.io",
        "Kay SR, Fiszbein A, Opler LA. The PANSS. Schizophr Bull. 1987;13(2):261-276.",
        scale_note="1 = Ausente · 2 = Mínimo · 3 = Leve · 4 = Moderado · 5 = Moderado-severo · 6 = Severo · 7 = Extremo",
        scale_headers=LIKERT_1_7,
    )


def gen_ecr():
    items = [
        "Me preocupa que no me quieran",
        "Me preocupa que me abandonen",
        "Me preocupa que me rechacen",
        "Me preocupa que me dejen",
        "Me preocupa que no me necesiten",
        "Me preocupa que no me valoren",
        "Me preocupa que no me respeten",
        "Me preocupa que no me comprendan",
        "Me preocupa que no me apoyen",
        "Me preocupa que no me cuiden",
        "Me preocupa que no me escuchen",
        "Me preocupa que no me acepten",
        "Prefiero no depender de los demás",
        "Prefiero no necesitar a los demás",
        "Prefiero no confiar en los demás",
        "Prefiero no abrirme a los demás",
        "Prefiero no mostrar mis sentimientos",
        "Prefiero no pedir ayuda",
        "Prefiero no mostrar vulnerabilidad",
        "Prefiero no depender emocionalmente",
        "Prefiero mantener distancia emocional",
        "Prefiero ser autosuficiente",
        "Prefiero no depender de mi pareja",
        "Prefiero no necesitar a mi pareja",
        "Prefiero no confiar en mi pareja",
        "Prefiero no abrirme a mi pareja",
        "Prefiero no mostrar mis sentimientos a mi pareja",
        "Prefiero no pedir ayuda a mi pareja",
        "Prefiero no mostrar vulnerabilidad a mi pareja",
        "Prefiero no depender emocionalmente de mi pareja",
        "Prefiero mantener distancia emocional con mi pareja",
        "Prefiero ser autosuficiente en la relación",
        "Me siento cómodo(a) dependiendo de los demás",
        "Me siento cómodo(a) necesitando a los demás",
        "Me siento cómodo(a) confiando en los demás",
        "Me siento cómodo(a) abriéndome a los demás",
    ]
    return build_instrument_pdf(
        "ecr-cuestionario-apego-adultos-espanol.pdf",
        "ECR-R en Español",
        "Experiences in Close Relationships-Revised — Apego en adultos",
        "Indique cuánto está de acuerdo con cada afirmación sobre sus relaciones cercanas. "
        "36 ítems (versión corta ECR-R), escala 1–7. Subescalas: Ansiedad y Evitación.",
        items,
        "<b>Ansiedad:</b> _____ · <b>Evitación:</b> _____ · <b>Estilo:</b> _____",
        ["Estilo", "Perfil", "Acción sugerida"],
        [
            ["Seguro", "Ansiedad baja + Evitación baja", "Fortalecer recursos relacionales"],
            ["Preocupado", "Ansiedad alta + Evitación baja", "Trabajar ansiedad de apego"],
            ["Evitativo", "Ansiedad baja + Evitación alta", "Trabajar intimidad y confianza"],
            ["Desorganizado", "Ansiedad alta + Evitación alta", "Terapia focalizada en apego"],
        ],
        "Evalúa estilo de apego con ECR-R en Kalyo — kalyo.io",
        "Fraley RC, Waller NG, Brennan KA. An item response theory analysis of self-report measures of adult attachment. J Pers Soc Psychol. 2000;78(2):350-365.",
        scale_note="1 = Muy en desacuerdo · 4 = Ni de acuerdo ni en desacuerdo · 7 = Muy de acuerdo",
        scale_headers=LIKERT_1_7,
    )


def gen_enrich():
    items = [
        "Mi pareja y yo compartimos ideas similares sobre el matrimonio",
        "Mi pareja y yo compartimos ideas similares sobre la forma de expresar afecto",
        "Mi pareja y yo tenemos buena comunicación",
        "Mi pareja y yo resolvemos bien los conflictos",
        "Mi pareja y yo tenemos buena relación sexual",
        "Mi pareja y yo compartimos tiempo de calidad",
        "Mi pareja y yo tenemos objetivos similares para el futuro",
        "Mi pareja y yo compartimos valores similares",
        "Mi pareja y yo nos apoyamos mutuamente",
        "Mi pareja y yo respetamos nuestras diferencias",
        "Mi pareja y yo tenemos buena relación con la familia extensa",
        "Mi pareja y yo manejamos bien el dinero",
        "Mi pareja y yo compartimos responsabilidades domésticas",
        "Mi pareja y yo tenemos buena relación con los hijos (si aplica)",
        "Mi pareja y yo compartimos actividades de ocio",
        "Mi pareja y yo tenemos buena relación espiritual/religiosa (si aplica)",
        "Mi pareja y yo tenemos buena relación con amigos",
        "Mi pareja y yo tenemos buena relación laboral/vida-trabajo",
        "Mi pareja y yo tenemos buena relación emocional",
        "Mi pareja y yo tenemos buena relación intelectual",
        "Mi pareja y yo tenemos buena relación recreativa",
        "Mi pareja y yo tenemos buena relación de pareja en general",
        "Estoy satisfecho(a) con mi relación de pareja",
        "Mi pareja está satisfecha con nuestra relación",
        "Recomendaría la terapia de pareja a otros en situación similar",
        "Nuestra relación ha mejorado con el tiempo",
        "Nuestra relación es estable",
        "Nuestra relación es satisfactoria",
        "Nuestra relación es saludable",
        "Nuestra relación es equilibrada",
        "Nuestra relación es respetuosa",
        "Nuestra relación es amorosa",
        "Nuestra relación es comprometida",
        "Nuestra relación es duradera",
        "Nuestra relación es confiable y segura",
    ]
    return build_instrument_pdf(
        "enrich-inventario-relacion-pareja-espanol.pdf",
        "ENRICH en Español",
        "Enriching and Nurturing Relationship Issues — Relación de pareja",
        "35 ítems representativos de las principales áreas del ENRICH (versión completa: 125 ítems). "
        "Escala 1–5. Tiempo: 10 min. Evalúa satisfacción y áreas de conflicto.",
        items,
        "<b>PUNTAJE:</b> _____ · <b>Áreas de conflicto:</b> _____ · <b>Satisfacción pareja:</b> _____",
        ["Percentil", "Interpretación", "Acción sugerida"],
        [
            ["≥ 40", "Relación satisfactoria", "Mantenimiento y fortalecimiento"],
            ["30 – 39", "Relación con áreas de mejora", "Terapia de pareja focalizada"],
            ["20 – 29", "Relación disfuncional", "Terapia de pareja activa"],
            ["&lt; 20", "Relación en crisis", "Intervención intensiva; evaluar separación"],
        ],
        "Evalúa relación de pareja con ENRICH en Kalyo — kalyo.io",
        "Olson DH, Fowers BJ, Simon M. ENRICH Marital Inventory. Life Innovations. 1996. Versión completa: 125 ítems.",
        scale_note="1 = Totalmente en desacuerdo · 3 = Neutral · 5 = Totalmente de acuerdo",
        scale_headers=LIKERT_1_5,
    )


def gen_faces_iv():
    items = [
        "En nuestra familia nos decimos las cosas directamente",
        "En nuestra familia nos apoyamos mutuamente",
        "En nuestra familia nos expresamos libremente",
        "En nuestra familia nos escuchamos unos a otros",
        "En nuestra familia resolvemos los problemas juntos",
        "En nuestra familia tenemos reglas claras",
        "En nuestra familia hay estructura y organización",
        "En nuestra familia hay roles definidos",
        "En nuestra familia hay límites claros",
        "En nuestra familia hay disciplina consistente",
        "En nuestra familia hay calidez y afecto",
        "En nuestra familia nos sentimos unidos",
        "En nuestra familia nos sentimos seguros",
        "En nuestra familia nos sentimos valorados",
        "En nuestra familia nos sentimos respetados",
        "En nuestra familia nos sentimos comprendidos",
        "En nuestra familia nos sentimos apoyados",
        "En nuestra familia nos sentimos aceptados",
        "En nuestra familia nos sentimos amados",
        "En nuestra familia nos sentimos conectados",
        "En nuestra familia hay comunicación abierta",
        "En nuestra familia hay cooperación",
        "En nuestra familia hay flexibilidad",
        "En nuestra familia hay adaptabilidad",
    ]
    return build_instrument_pdf(
        "faces-iv-escala-adaptabilidad-familiar-espanol.pdf",
        "FACES IV en Español",
        "Family Adaptability and Cohesion Evaluation Scales IV",
        "Indique qué tan bien describe cada afirmación a su familia. "
        "24 ítems, escala 1–5. Subescalas: Cohesión y Adaptabilidad (balanceado/desbalanceado).",
        items,
        "<b>Cohesión:</b> _____ · <b>Adaptabilidad:</b> _____ · <b>Ratio balanceado:</b> _____",
        ["Perfil", "Interpretación", "Acción sugerida"],
        [
            ["Balanceado", "Cohesión y adaptabilidad equilibradas", "Fortalecer dinámica familiar"],
            ["Desconectado", "Cohesión baja", "Trabajar conexión y comunicación"],
            ["Enmeshed", "Cohesión excesiva", "Trabajar límites y autonomía"],
            ["Rígido/Flexible extremo", "Adaptabilidad desbalanceada", "Terapia familiar sistémica"],
        ],
        "Evalúa adaptabilidad familiar con FACES IV en Kalyo — kalyo.io",
        "Olson DH. FACES IV and the Circumplex Model. J Marital Fam Ther. 2011;37(4):403-406.",
        scale_note="1 = Casi nunca · 2 = Rara vez · 3 = A veces · 4 = A menudo · 5 = Casi siempre",
        scale_headers=LIKERT_1_5,
    )


def gen_oq45():
    items = [
        "Me siento triste o deprimido(a)",
        "Me siento ansioso(a) o nervioso(a)",
        "Me siento enfadado(a) o irritable",
        "Me siento solo(a) o aislado(a)",
        "Me siento sin esperanza",
        "Me siento culpable",
        "Me siento sin valor",
        "Me siento abrumado(a)",
        "Me siento estresado(a)",
        "Me siento agotado(a)",
        "Tengo problemas para dormir",
        "Tengo problemas para concentrarme",
        "Tengo problemas para tomar decisiones",
        "Tengo problemas para relacionarme con otros",
        "Tengo problemas en el trabajo o estudios",
        "Tengo problemas en la relación de pareja",
        "Tengo problemas con la familia",
        "Tengo problemas con amigos",
        "Tengo problemas para disfrutar de las cosas",
        "Tengo problemas para relajarme",
        "Tengo problemas para controlar mis emociones",
        "Tengo problemas para controlar mi comportamiento",
        "Tengo problemas para afrontar el estrés",
        "Tengo problemas para resolver conflictos",
        "Tengo problemas para comunicarme",
        "Tengo problemas para expresar mis sentimientos",
        "Tengo problemas para pedir ayuda",
        "Tengo problemas para establecer límites",
        "Tengo problemas para confiar en otros",
        "Tengo problemas para sentirme seguro(a)",
        "Tengo problemas para sentirme satisfecho(a)",
        "Tengo problemas para sentirme en paz",
        "Tengo problemas para sentirme motivado(a)",
        "Tengo problemas para sentirme optimista",
        "Tengo problemas para sentirme conectado(a)",
        "Tengo problemas para sentirme útil",
        "Tengo problemas para sentirme amado(a)",
        "Tengo problemas para sentirme respetado(a)",
        "Tengo problemas para sentirme comprendido(a)",
        "Tengo problemas para sentirme aceptado(a)",
        "Tengo problemas para sentirme valorado(a)",
        "Tengo problemas para sentirme capaz",
        "Tengo problemas para sentirme en control",
        "Tengo problemas para sentirme bien conmigo mismo(a)",
        "Tengo problemas para sentirme bien en general",
    ]
    return build_instrument_pdf(
        "oq-45-resultados-terapia-espanol.pdf",
        "OQ-45 en Español",
        "Outcome Questionnaire-45 — Resultados en psicoterapia",
        "Indique cuánto le ha molestado cada problema durante la <b>última semana</b>. "
        "45 ítems, escala 0–4. Subescalas: Síntomas, Relaciones, Funcionamiento social.",
        items,
        "<b>TOTAL:</b> _____ / 180 · <b>Síntomas:</b> _____ · <b>Relaciones:</b> _____ · <b>Social:</b> _____",
        ["Puntaje", "Nivel", "Acción sugerida"],
        [
            ["0 – 62", "Funcionamiento normal", "Alta del tratamiento o mantenimiento"],
            ["63 – 80", "Distress leve", "Continuar tratamiento; monitoreo"],
            ["81 – 100", "Distress clínico", "Intervención activa"],
            ["101 – 180", "Distress severo", "Revisar plan de tratamiento urgente"],
        ],
        "Monitorea resultados terapéuticos con OQ-45 en Kalyo — kalyo.io",
        "Lambert MJ et al. The OQ-45. Psychotherapy. 2004;41(2):191-205.",
        scale_note="0 = Nada · 1 = Raramente · 2 = A veces · 3 = Frecuentemente · 4 = Casi siempre",
        scale_headers=LIKERT_0_4,
    )


def gen_core_om():
    items = [
        "Me he sentido muy ansioso(a) o tenso(a)",
        "Me he sentido muy deprimido(a) o desanimado(a)",
        "Me he sentido muy irritable o enfadado(a)",
        "Me he sentido muy solo(a) o aislado(a)",
        "Me he sentido muy culpable",
        "Me he sentido muy sin esperanza",
        "Me he sentido muy abrumado(a)",
        "Me he sentido muy estresado(a)",
        "He tenido dificultad para dormir",
        "He tenido dificultad para concentrarme",
        "He tenido dificultad para tomar decisiones",
        "He tenido dificultad para relacionarme con otros",
        "He tenido dificultad para disfrutar de las cosas",
        "He tenido dificultad para relajarme",
        "He tenido dificultad para controlar mis emociones",
        "He tenido dificultad para afrontar el estrés",
        "He tenido dificultad para resolver problemas",
        "He tenido dificultad para comunicarme",
        "He tenido dificultad para pedir ayuda",
        "He tenido dificultad para confiar en otros",
        "He tenido dificultad para sentirme seguro(a)",
        "He tenido dificultad para sentirme satisfecho(a)",
        "He tenido dificultad para sentirme en paz",
        "He tenido dificultad para sentirme motivado(a)",
        "He tenido dificultad para sentirme optimista",
        "He tenido dificultad para sentirme conectado(a)",
        "He tenido dificultad para sentirme útil",
        "He tenido dificultad para sentirme amado(a)",
        "He tenido dificultad para sentirme respetado(a)",
        "He tenido dificultad para sentirme comprendido(a)",
        "He tenido dificultad para sentirme aceptado(a)",
        "He tenido dificultad para sentirme valorado(a)",
        "He tenido dificultad para sentirme capaz",
        "He tenido dificultad para sentirme en control",
    ]
    return build_instrument_pdf(
        "core-om-medida-resultados-clinicos-espanol.pdf",
        "CORE-OM en Español",
        "Clinical Outcomes in Routine Evaluation — Outcome Measure",
        "Indique con qué frecuencia le ha ocurrido durante la <b>última semana</b>. "
        "34 ítems, escala 0–4. Tiempo: 5–10 min. Mide distress psicológico global.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 136 · <b>Media:</b> _____ · <b>Corte clínico:</b> ≥ 1.0",
        ["Media", "Nivel", "Acción sugerida"],
        [
            ["0 – 0.49", "Subclínico", "Alta o mantenimiento"],
            ["0.50 – 0.99", "Leve", "Monitoreo en tratamiento"],
            ["1.00 – 1.49", "Clínico", "Intervención activa"],
            ["1.50 – 4.00", "Severo", "Revisar plan de tratamiento"],
        ],
        "Mide resultados clínicos con CORE-OM en Kalyo — kalyo.io",
        "Evans C et al. CORE-OM manual. CORE System Trust. 2000. Validación en español disponible.",
        scale_note="0 = Nada · 1 = Solo ocasionalmente · 2 = A veces · 3 = A menudo · 4 = Muy a menudo o siempre",
        scale_headers=LIKERT_0_4,
    )


def gen_wai_sr():
    items = [
        "Aprecio este cliente como persona",
        "Siento que este cliente aprecia a mí",
        "Siento que este cliente confía en mí",
        "Siento que confío en este cliente",
        "Siento que este cliente y yo colaboramos bien",
        "Siento que este cliente y yo tenemos metas acordadas",
        "Siento que este cliente y yo entendemos lo que hacemos en terapia",
        "Siento que este cliente y yo estamos de acuerdo en lo importante",
        "Siento que la terapia con este cliente es productiva",
        "Siento que la terapia con este cliente me satisface",
        "Siento que este cliente y yo tenemos una buena relación",
        "Siento que este cliente y yo nos respetamos mutuamente",
    ]
    return build_instrument_pdf(
        "wai-sr-alianza-terapeutica-espanol.pdf",
        "WAI-SR en Español",
        "Working Alliance Inventory — Short Revised (autoreporte terapeuta)",
        "Indique su grado de acuerdo con cada afirmación sobre la <b>alianza terapéutica</b> "
        "con su cliente actual. 12 ítems, escala 1–7. Tiempo: 3 min.",
        items,
        "<b>PUNTAJE TOTAL:</b> _____ / 84 · <b>Objetivos:</b> _____ · <b>Tareas:</b> _____ · <b>Vínculo:</b> _____",
        ["Puntaje", "Alianza", "Acción sugerida"],
        [
            ["12 – 48", "Alianza baja", "Trabajar ruptura de alianza; revisar encuadre"],
            ["49 – 65", "Alianza moderada", "Fortalecer objetivos y vínculo terapéutico"],
            ["66 – 84", "Alianza fuerte", "Mantener y aprovechar alianza en tratamiento"],
        ],
        "Evalúa alianza terapéutica con WAI-SR en Kalyo — kalyo.io",
        "Hatcher RL, Gillaspy JA. Development and validation of a revised WAI-SR. Psychotherapy. 2006;43(4):443-456.",
        scale_note="1 = Nunca · 4 = A veces · 7 = Siempre",
        scale_headers=LIKERT_1_7,
    )


GENERATORS = [
    ("SCL-90-R", gen_scl90r),
    ("GHQ-12", gen_ghq12),
    ("GHQ-28", gen_ghq28),
    ("K10", gen_k10),
    ("K6", gen_k6),
    ("SRQ-20", gen_srq20),
    ("STAI", gen_stai),
    ("SPIN", gen_spin),
    ("Mini-SPIN", gen_mini_spin),
    ("LSAS", gen_lsas),
    ("PASS", gen_pass),
    ("PDSS", gen_pdss),
    ("Y-BOCS", gen_ybocs),
    ("OCI-R", gen_ocir),
    ("EPDS", gen_epds),
    ("SCOFF", gen_scoff),
    ("EAT-26", gen_eat26),
    ("EDE-Q", gen_edeq),
    ("AUDIT", gen_audit),
    ("CAGE", gen_cage),
    ("YMRS", gen_ymrs),
    ("MDQ", gen_mdq),
    ("ASRM", gen_asrm),
    ("PANSS", gen_panss),
    ("ECR-R", gen_ecr),
    ("ENRICH", gen_enrich),
    ("FACES IV", gen_faces_iv),
    ("OQ-45", gen_oq45),
    ("CORE-OM", gen_core_om),
    ("WAI-SR", gen_wai_sr),
]

HTML_PATCHES: list[tuple[str, str, str, str]] = [
    ("scl-90-r-lista-sintomas-revisada.html", "/assets/scl-90-r-lista-sintomas-revisada-espanol.pdf", "SCL-90-R-espanol-Kalyo.pdf", "Descargar SCL-90-R en espa&ntilde;ol (PDF gratuito)"),
    ("ghq-12-cuestionario-salud-general.html", "/assets/ghq-12-cuestionario-salud-general-espanol.pdf", "GHQ-12-espanol-Kalyo.pdf", "Descargar GHQ-12 en espa&ntilde;ol (PDF gratuito)"),
    ("ghq-28-cuestionario-salud-general.html", "/assets/ghq-28-cuestionario-salud-general-espanol.pdf", "GHQ-28-espanol-Kalyo.pdf", "Descargar GHQ-28 en espa&ntilde;ol (PDF gratuito)"),
    ("k10-escala-distress-psicologico.html", "/assets/k10-escala-distress-psicologico-espanol.pdf", "K10-espanol-Kalyo.pdf", "Descargar K10 en espa&ntilde;ol (PDF gratuito)"),
    ("k6-tamizaje-salud-mental.html", "/assets/k6-tamizaje-salud-mental-espanol.pdf", "K6-espanol-Kalyo.pdf", "Descargar K6 en espa&ntilde;ol (PDF gratuito)"),
    ("srq-20-salud-mental-autorreportado.html", "/assets/srq-20-salud-mental-autorreportado-espanol.pdf", "SRQ-20-espanol-Kalyo.pdf", "Descargar SRQ-20 en espa&ntilde;ol (PDF gratuito)"),
    ("stai-ansiedad-estado-rasgo.html", "/assets/stai-ansiedad-estado-rasgo-espanol.pdf", "STAI-espanol-Kalyo.pdf", "Descargar STAI en espa&ntilde;ol (PDF gratuito)"),
    ("spin-inventario-fobia-social.html", "/assets/spin-inventario-fobia-social-espanol.pdf", "SPIN-espanol-Kalyo.pdf", "Descargar SPIN en espa&ntilde;ol (PDF gratuito)"),
    ("mini-spin-ansiedad-social-breve.html", "/assets/mini-spin-ansiedad-social-breve-espanol.pdf", "Mini-SPIN-espanol-Kalyo.pdf", "Descargar Mini-SPIN en espa&ntilde;ol (PDF gratuito)"),
    ("lsas-ansiedad-social-liebowitz.html", "/assets/lsas-ansiedad-social-liebowitz-espanol.pdf", "LSAS-espanol-Kalyo.pdf", "Descargar LSAS en espa&ntilde;ol (PDF gratuito)"),
    ("pass-sensibilidad-ansiedad.html", "/assets/pass-sensibilidad-ansiedad-espanol.pdf", "PASS-espanol-Kalyo.pdf", "Descargar PASS en espa&ntilde;ol (PDF gratuito)"),
    ("pdss-trastorno-panico-shear.html", "/assets/pdss-trastorno-panico-shear-espanol.pdf", "PDSS-espanol-Kalyo.pdf", "Descargar PDSS en espa&ntilde;ol (PDF gratuito)"),
    ("y-bocs-escala-yale-brown-toc.html", "/assets/y-bocs-escala-yale-brown-toc-espanol.pdf", "Y-BOCS-espanol-Kalyo.pdf", "Descargar Y-BOCS en espa&ntilde;ol (PDF gratuito)"),
    ("oci-r-obsesiones-compulsiones.html", "/assets/oci-r-obsesiones-compulsiones-espanol.pdf", "OCI-R-espanol-Kalyo.pdf", "Descargar OCI-R en espa&ntilde;ol (PDF gratuito)"),
    ("epds-depresion-postnatal-edimburgo.html", "/assets/epds-depresion-postnatal-edimburgo-espanol.pdf", "EPDS-espanol-Kalyo.pdf", "Descargar EPDS en espa&ntilde;ol (PDF gratuito)"),
    ("scoff-trastornos-alimentarios.html", "/assets/scoff-trastornos-alimentarios-espanol.pdf", "SCOFF-espanol-Kalyo.pdf", "Descargar SCOFF en espa&ntilde;ol (PDF gratuito)"),
    ("eat-26-trastornos-alimentarios.html", "/assets/eat-26-trastornos-alimentarios-espanol.pdf", "EAT-26-espanol-Kalyo.pdf", "Descargar EAT-26 en espa&ntilde;ol (PDF gratuito)"),
    ("ede-q-cuestionario-trastornos-alimentarios.html", "/assets/ede-q-cuestionario-trastornos-alimentarios-espanol.pdf", "EDE-Q-espanol-Kalyo.pdf", "Descargar EDE-Q en espa&ntilde;ol (PDF gratuito)"),
    ("audit-test-alcoholismo.html", "/assets/audit-test-alcoholismo-espanol.pdf", "AUDIT-espanol-Kalyo.pdf", "Descargar AUDIT en espa&ntilde;ol (PDF gratuito)"),
    ("cage-alcoholismo-test.html", "/assets/cage-alcoholismo-test-espanol.pdf", "CAGE-espanol-Kalyo.pdf", "Descargar CAGE en espa&ntilde;ol (PDF gratuito)"),
    ("ymrs-escala-mania-young.html", "/assets/ymrs-escala-mania-young-espanol.pdf", "YMRS-espanol-Kalyo.pdf", "Descargar YMRS en espa&ntilde;ol (PDF gratuito)"),
    ("mdq-trastorno-bipolar-tamizaje.html", "/assets/mdq-trastorno-bipolar-tamizaje-espanol.pdf", "MDQ-espanol-Kalyo.pdf", "Descargar MDQ en espa&ntilde;ol (PDF gratuito)"),
    ("asrm-escala-mania-altman.html", "/assets/asrm-escala-mania-altman-espanol.pdf", "ASRM-espanol-Kalyo.pdf", "Descargar ASRM en espa&ntilde;ol (PDF gratuito)"),
    ("panss-esquizofrenia.html", "/assets/panss-esquizofrenia-espanol.pdf", "PANSS-espanol-Kalyo.pdf", "Descargar PANSS en espa&ntilde;ol (PDF gratuito)"),
    ("ecr-cuestionario-apego-adultos.html", "/assets/ecr-cuestionario-apego-adultos-espanol.pdf", "ECR-R-espanol-Kalyo.pdf", "Descargar ECR-R en espa&ntilde;ol (PDF gratuito)"),
    ("enrich-inventario-relacion-pareja.html", "/assets/enrich-inventario-relacion-pareja-espanol.pdf", "ENRICH-espanol-Kalyo.pdf", "Descargar ENRICH en espa&ntilde;ol (PDF gratuito)"),
    ("faces-iv-escala-adaptabilidad-familiar.html", "/assets/faces-iv-escala-adaptabilidad-familiar-espanol.pdf", "FACES-IV-espanol-Kalyo.pdf", "Descargar FACES IV en espa&ntilde;ol (PDF gratuito)"),
    ("oq-45-resultados-terapia.html", "/assets/oq-45-resultados-terapia-espanol.pdf", "OQ-45-espanol-Kalyo.pdf", "Descargar OQ-45 en espa&ntilde;ol (PDF gratuito)"),
    ("core-om-medida-resultados-clinicos.html", "/assets/core-om-medida-resultados-clinicos-espanol.pdf", "CORE-OM-espanol-Kalyo.pdf", "Descargar CORE-OM en espa&ntilde;ol (PDF gratuito)"),
    ("wai-sr-alianza-terapeutica.html", "/assets/wai-sr-alianza-terapeutica-espanol.pdf", "WAI-SR-espanol-Kalyo.pdf", "Descargar WAI-SR en espa&ntilde;ol (PDF gratuito)"),
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

