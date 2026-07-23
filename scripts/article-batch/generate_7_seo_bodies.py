#!/usr/bin/env python3
"""Generate 7 clinical 'qué es' SEO article JSON specs."""
from __future__ import annotations

import json
import re
import sys


def wc(text: str) -> int:
    t = re.sub(r"<[^>]+>", " ", text)
    return len(re.sub(r"\s+", " ", t).strip().split())


def body_words(article: dict) -> int:
    parts = [article["intro"]]
    for s in article["sections"]:
        parts.append(s["html"])
    for f in article["faqs"]:
        parts.append(f["q"] + " " + f["a"])
    return sum(wc(p) for p in parts)


def kalyo_count(article: dict) -> int:
    blob = json.dumps(article, ensure_ascii=False)
    return blob.count("https://app.kalyo.io/register")


def p(*paras: str) -> str:
    return "\n".join(f"<p>{x}</p>" for x in paras)


def validate(a: dict) -> None:
    slug = a["slug"]
    tl = len(a["title"])
    if not (55 <= tl <= 60):
        raise ValueError(f"{slug} title len {tl}: {a['title']}")
    dl = len(a["description"])
    if not (150 <= dl <= 160):
        raise ValueError(f"{slug} desc len {dl}: {a['description']}")
    iw = wc(a["intro"])
    if not (50 <= iw <= 60):
        raise ValueError(f"{slug} intro words {iw}")
    bw = body_words(a)
    if bw < 1200:
        raise ValueError(f"{slug} body words {bw} < 1200")
    if kalyo_count(a) != 1:
        raise ValueError(f"{slug} kalyo links {kalyo_count(a)}")
    if len(a["sections"]) != 6:
        raise ValueError(f"{slug} sections {len(a['sections'])}")
    if len(a["faqs"]) != 5:
        raise ValueError(f"{slug} faqs")


ARTICLES: list[dict] = []

# --- 1 autismo-que-es ---
ARTICLES.append(
    {
        "slug": "autismo-que-es",
        "title": "Autismo qué es: TEA, DSM-5 y evaluación clínica | Kalyo",
        "description": "Autismo qué es: criterios DSM-5 del TEA, tamizaje M-CHAT, evaluación ADOS-2 y ADI-R, enfoque clínico integral y derivación oportuna para psicólogos en LATAM.",
        "h1": "Autismo: qué es el trastorno del espectro autista (TEA)",
        "breadcrumb_short": "Autismo: qué es",
        "intro": "El trastorno del espectro autista (TEA) es una condición del neurodesarrollo con déficits persistentes en comunicación social e intereses o conductas restringidas y repetitivas. Para psicólogos clínicos en Latinoamérica, dominar criterios DSM-5, herramientas de tamizaje y evaluación estandarizada resulta esencial para un diagnóstico diferencial riguroso y planes de intervención basados en evidencia.",
        "sections": [
            {
                "h2": "Definición clínica: autismo qué es en DSM-5 y CIE-11",
                "html": p(
                    "En el DSM-5, el autismo se conceptualiza como un trastorno del espectro autista (TEA), unificado respecto a categorías previas (autismo, Asperger, trastorno generalizado del desarrollo). La condición se define por dos dominios obligatorios: (A) déficits persistentes en la comunicación e interacción social en múltiples contextos, y (B) patrones restringidos y repetitivos de comportamiento, intereses o actividades. Los síntomas deben estar presentes en la fase temprana del desarrollo, causar deterioro clínico significativo en funcionamiento social, laboral u otras áreas, y no explicarse mejor por retraso intelectual global o retraso global del desarrollo.",
                    "La CIE-11 agrupa condiciones similares bajo trastornos del espectro autista, enfatizando variaciones en necesidades de apoyo más que subtipos rígidos. En consulta, conviene documentar nivel de apoyo (DSM-5: con o sin deterioro intelectual y con o sin deterioro del lenguaje) y describir el perfil funcional: comunicación, flexibilidad cognitiva, regulación sensorial y habilidades adaptativas. El término coloquial «autismo qué es» suele reflejar dudas de familias sobre si las dificultades sociales, el lenguaje retrasado o los rituales encajan en TEA o en otro cuadro del desarrollo.",
                    "El diagnóstico es clínico, apoyado en historia del desarrollo, observación estructurada e informes de cuidadores. No existe un biomarcador único. La heterogeneidad del espectro implica que dos personas con TEA pueden diferir radicalmente en cognición, lenguaje, comorbilidades (TDAH, ansiedad, epilepsia) y necesidades de apoyo. Por ello, la evaluación debe ser dimensional y longitudinal, no reducirse a una puntuación aislada.",
                ),
            },
            {
                "h2": "Criterios DSM-5: comunicación social y conductas restringidas",
                "html": p(
                    "El criterio A exige déficits en reciprocidad socioemocional (p. ej., compartir emociones o intereses, iniciar o responder a interacciones), en comunicación no verbal (contacto visual, gestos, expresión facial) y en desarrollo, mantenimiento y comprensión de relaciones. En lactantes puede manifestarse como poca orientación social; en escolares, dificultad para amistades; en adultos, parejas laborales o románticas limitadas. El criterio B incluye estereotipias motoras o de lenguaje, adherencia inflexible a rutinas, intereses fijos de intensidad anormal o hipersensibilidad o hiposensibilidad sensorial.",
                    "Se requieren al menos tres síntomas del criterio A (dos si historia completa) y dos del B, con inicio en la infancia aunque pueda volverse evidente cuando las demandas sociales exceden capacidades. Es frecuente el diagnóstico tardío en mujeres y personas con lenguaje fluido que «camuflan» dificultades mediante reglas aprendidas, lo que aumenta riesgo de agotamiento, ansiedad y depresión secundaria.",
                )
                + """
<ul>
<li><strong>Criterio A (social-comunicativo):</strong> al menos 3 de 3 áreas (reciprocidad, comunicación no verbal, relaciones).</li>
<li><strong>Criterio B (RRB):</strong> al menos 2 de 4 (estereotipias, rutinas, intereses, sensorial).</li>
<li><strong>Contexto:</strong> síntomas presentes en infancia; impacto funcional actual; no atribuibles solo a discapacidad intelectual.</li>
</ul>""",
            },
            {
                "h2": "Tamizaje en atención primaria: M-CHAT-R/F y señales de alerta",
                "html": p(
                    "El M-CHAT-R/F es el tamizaje más extendido entre 16 y 30 meses, administrado a cuidadores con seguimiento entrevistado si hay riesgo. Identifica señales tempranas: poco señalamiento compartido, falta de respuesta al nombre, escaso juego pretendido, pérdida de habilidades. Un resultado positivo no diagnostica TEA; indica evaluación especializada urgente. En LATAM, adaptar lenguaje cultural y considerar acceso limitado a evaluadores certificados: documentar derivación y coordinar con pediatría y estimulación temprana.",
                    "En escolares y adolescentes, los tamizajes parentales pierden sensibilidad; conviene combinar cuestionarios breves (p. ej., AQ-10 en adultos sospechosos) con entrevista clínica y observación en aula. Señales de alerta en cualquier edad: aislamiento progresivo, rigidez extrema ante cambios, regresión del lenguaje, intereses que interfieren con autocuidado o estudios, crisis sensoriales recurrentes.",
                ),
            },
            {
                "h2": "Evaluación estandarizada: ADOS-2, ADI-R y batería complementaria",
                "html": p(
                    "El ADOS-2 observa comunicación social y conductas restringidas en contexto semiestructurado (módulos según edad y lenguaje). Requiere entrenamiento formal; aporta evidencia objetiva pero no sustituye el juicio clínico. El ADI-R recoge historia del desarrollo con cuidadores, crucial para criterios de inicio temprano y diferencial con trastornos del lenguaje o retraso global.",
                    "La evaluación integral suele incluir medida cognitiva (WPPSI, WISC, WAIS según edad), lenguaje, habilidades adaptativas (Vineland o equivalentes), screening auditivo y registro de comorbilidades. En adultos, añadir entrevista autobiográfica detallada y explorar camuflaje, alexitimia y burnout. Integrar hallazgos en un informe que vincule perfil de fortalezas, barreras contextuales y recomendaciones educativas o laborales.",
                )
                + """
<table class="items-table">
<thead><tr><th>Herramienta</th><th>Función</th><th>Nota clínica</th></tr></thead>
<tbody>
<tr><td>M-CHAT-R/F</td><td>Tamizaje 16–30 meses</td><td>Derivar si positivo; no diagnóstico</td></tr>
<tr><td>ADOS-2</td><td>Observación estandarizada</td><td>Certificación del aplicador</td></tr>
<tr><td>ADI-R</td><td>Historia con cuidadores</td><td>Complementa ADOS-2</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "Diagnóstico diferencial y comorbilidades frecuentes",
                "html": p(
                    "Diferenciar TEA de trastorno de comunicación social (pragmática), TDAH (in atención sin déficit primario de reciprocidad), trastornos de ansiedad (evitación social secundaria), esquizofrenia de inicio temprano (psicosis con desorganización distinta) y discapacidad intelectual sin perfil autista. La clave está en la calidad de la reciprocidad social, no solo en retraso del lenguaje o conducta desafiante.",
                    "Comorbilidades elevadas: TDAH, trastornos de ansiedad, TOC, epilepsia, problemas gastrointestinales y del sueño. Cada una modifica intervención: p. ej., TDAH no invalida TEA pero sí requiere adaptar psicoeducación y estrategias conductuales. Evaluar riesgo suicida en adolescentes con bullying, rechazo social o depresión no reconocida. En consulta privada, acordar con la familia prioridades de tratamiento y tiempos realistas de derivación a servicios públicos cuando existan listas de espera prolongadas.",
                ),
            },
            {
                "h2": "Intervención psicológica y coordinación interdisciplinaria",
                "html": p(
                    "Las guías recomiendan intervenciones basadas en evidencia centradas en comunicación social, habilidades adaptativas y apoyo a la familia (p. ej., modelos de enseñanza naturalista, entrenamiento a cuidadores, intervención en comunicación aumentativa cuando hay poco lenguaje funcional). Objetivos SMART alineados con contexto escolar o laboral; medir progreso con escalas adaptativas y registros conductuales, no solo sesiones asistidas. Revisar periódicamente si los objetivos siguen siendo relevantes para la persona y su entorno.",
                    "Coordinar con fonoaudiología, pedagogía especial, psiquiatría cuando hay agresividad grave o psicosis, y trabajo social para acceso a derechos. Psicoeducación clara a la familia sobre neurodiversidad y expectativas realistas. Para organizar evaluaciones, informes y seguimiento longitudinal, muchos consultorios en la región centralizan expediente y recordatorios en <a href=\"https://app.kalyo.io/register\">Kalyo</a>, sin sustituir la formación específica en TEA.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "¿El autismo siempre incluye discapacidad intelectual?",
                "a": "No. El DSM-5 permite especificar con o sin deterioro intelectual asociado. Hay personas con TEA y cognición promedio o superior, así como personas con discapacidad intelectual comórbida. La evaluación cognitiva independiente del diagnóstico de TEA es esencial para planificar apoyos educativos y adaptaciones.",
            },
            {
                "q": "¿Se puede diagnosticar TEA en adultos?",
                "a": "Sí, cada vez más solicitudes provienen de adultos con sospecha tardía, especialmente mujeres. Requiere entrevista developmental retrospectiva, observación (ADOS-2 módulo 4 cuando procede) y exploración de camuflaje, salud mental secundaria y funcionamiento actual. La ausencia de informantes infantiles complica pero no impide el diagnóstico si la evidencia acumulada es sólida y coherente en el tiempo.",
            },
            {
                "q": "¿M-CHAT positivo confirma autismo?",
                "a": "No. Es un tamizaje con falsos positivos posibles en contextos de desarrollo retrasado o estrés familiar. Confirma la necesidad de evaluación especializada completa. Repetir tamizaje sin evaluar puede retrasar intervención temprana o generar ansiedad innecesaria en familias que merecen orientación clara.",
            },
            {
                "q": "¿Qué papel tiene el psicólogo frente al pediatra o psiquiatra?",
                "a": "El psicólogo clínico con formación puede administrar ADOS-2/ADI-R, realizar evaluación cognitiva y conductual, diseñar intervención y psicoeducación. La prescripción farmacológica corresponde a médico. El equipo ideal combina disciplinas con un plan de seguimiento compartido.",
            },
            {
                "q": "¿Cómo documentar nivel de apoyo en el informe?",
                "a": "Describir necesidades actuales en comunicación, autonomía, flexibilidad y entornos (hogar, escuela, trabajo). Evitar etiquetas estigmatizantes. Incluir fortalezas, ajustes razonables recomendados, criterios de reevaluación periódica y coordinación con escuela o empleador cuando el paciente lo autorice.",
            },
        ],
        "howto": None,
        "related": [
            {"href": "/articulos/ados-2-evaluacion-tea.html", "label": "ADOS-2: evaluación estandarizada del TEA"},
            {"href": "/articulos/adir-r-entrevista-autismo.html", "label": "ADI-R: entrevista diagnóstica con cuidadores"},
            {"href": "/articulos/mchat-r-tamizaje-autismo.html", "label": "M-CHAT-R/F: tamizaje temprano de autismo"},
            {"href": "/articulos/aq-10-cociente-autista-tamizaje.html", "label": "AQ-10: tamizaje breve en adultos"},
        ],
        "cta_h2": "Evalúa y da seguimiento al TEA con orden clínico",
        "cta_p": "Centraliza expediente, resultados de tamizajes y recordatorios de reevaluación para familias con sospecha o diagnóstico de espectro autista.",
        "keywords": "autismo qué es, TEA, DSM-5, ADOS-2, ADI-R, M-CHAT, evaluación autismo, psicología clínica LATAM",
        "card_title": "Autismo: qué es el TEA",
        "card_p": "Criterios DSM-5, tamizaje M-CHAT y evaluación ADOS-2/ADI-R para psicólogos clínicos.",
        "after_href": "/articulos/audit-test-alcoholismo.html",
        "after_loc": "https://kalyo.io/articulos/audit-test-alcoholismo.html",
    }
)

from mk_batch7_rest import extend_articles
import batch7_pads
from batch7_pads import apply_pads

extend_articles(ARTICLES, p)
batch7_pads.apply_pads_done.clear()
for _a in ARTICLES[1:]:
    apply_pads(_a)
    apply_pads(_a)
    apply_pads(_a)

if __name__ == "__main__":
    for a in ARTICLES:
        validate(a)
    json.dump(ARTICLES, sys.stdout, ensure_ascii=False, indent=2)
    sys.stderr.write(f"articles={len(ARTICLES)}\n")
