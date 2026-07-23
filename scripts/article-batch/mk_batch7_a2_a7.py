# -*- coding: utf-8 -*-
"""Articles 2-7 for batch 7 SEO body JSON."""


def articles(p):
    return [
        adiccion(p),
        anorexia(p),
        tlp(p),
        paralisis(p),
        tdah_adultos(p),
        esquizofrenia(p),
    ]


def adiccion(p):
    return {
        "slug": "adiccion-que-es",
        "title": "Adicción qué es: tipos, DSM-5 e intervención clínica | Kalyo",
        "description": "Adicción qué es según DSM-5: sustancias y conductas, criterios clínicos, entrevista motivacional y abordaje psicológico para psicólogos en Latinoamérica.",
        "h1": "Adicción: qué es y cómo abordarla desde psicología clínica",
        "breadcrumb_short": "Adicción: qué es",
        "intro": "La adicción, en sentido clínico, describe un patrón persistente de uso de sustancias o conductas gratificantes pese a consecuencias adversas, con pérdida de control, craving y deterioro funcional. Comprender adicción qué es en DSM-5 permite al psicólogo orientar tamizaje, entrevista motivacional e intervención breve coordinada con medicina y redes de apoyo familiar.",
        "sections": [
            {
                "h2": "Adicción qué es: del uso recreativo al trastorno clínico",
                "html": p(
                    "Coloquialmente se habla de adicción al alcohol, cannabis, cocaína, opioides, tabaco o pantallas. Clínicamente, el DSM-5 distingue trastornos por uso de sustancias y trastornos relacionados (intoxicación, abstinencia). También reconoce trastorno por juego de apuestas; otras conductas compulsivas se estudian como trastornos relacionados. El núcleo compartido incluye uso repetido, incapacidad de reducir a pesar del deseo, tiempo dedicado, craving, fallos en roles, uso en situaciones riesgosas y tolerancia o abstinencia cuando aplica.",
                    "La gravedad (leve, moderada, severa) depende del número de criterios cumplidos en doce meses. En Latinoamérica, violencia, desempleo y acceso desigual a rehabilitación modulan evolución y adherencia. El psicólogo no sustituye desintoxicación médica cuando hay riesgo vital; lidera evaluación psicosocial, motivación al cambio y prevención de recaídas ambulatoria.",
                    "Diferenciar abuso ocasional de trastorno requiere entrevista estructurada, colaterales cuando sea ético y tamizaje (AUDIT, DAST-10, ASSIST). Documente edad de inicio, patrón, intentos de abstinencia, comorbilidades y factores protectores que sostengan recuperación.",
                ),
            },
            {
                "h2": "Tipos de adicción frecuentes en consulta psicológica",
                "html": p(
                    "Alcohol y tabaco suelen iniciarse en contextos socialmente aceptados, retrasando la consulta. Estimulantes asocian impulsividad, psicosis inducida y riesgo cardiovascular. Opioides y policonsumo elevan mortalidad por sobredosis; evalúe acceso a antídotos y reducción de daños según normativa local.",
                    "Conductas (juego, compras, pornografía, redes) comparten circuitos de recompensa; criterios diagnósticos aún en consolidación. En adolescentes, distinga experimentación normativa de trastorno sin minimizar escalada.",
                )
                + """
<table class="items-table">
<thead><tr><th>Dimensión</th><th>Sustancias</th><th>Conductas</th></tr></thead>
<tbody>
<tr><td>Mecanismo</td><td>Tolerancia, abstinencia</td><td>Refuerzo intermitente</td></tr>
<tr><td>Riesgo agudo</td><td>Intoxicación, convulsiones</td><td>Deudas, aislamiento</td></tr>
<tr><td>Tamizaje</td><td>ASSIST, AUDIT</td><td>Tiempo, impacto funcional</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "Criterios DSM-5 del trastorno por uso",
                "html": p(
                    "Once criterios incluyen cantidad persistente, deseo fallido de control, craving, incumplimiento de obligaciones, problemas interpersonales, abandono de actividades, uso peligroso, uso pese a daño físico o psicológico, tolerancia y abstinencia (estos últimos no cuentan si hay prescripción médica adecuada). Tres o más criterios sugieren trastorno.",
                    "Especifique abstinencia actual, entorno controlado o remisión. Registre sustancia principal y policonsumo. Comorbilidades frecuentes: ansiedad, depresión, TLP, TDAH y trauma; abordarlas en paralelo mejora resultados.",
                ),
            },
            {
                "h2": "Entrevista motivacional y terapias basadas en evidencia",
                "html": p(
                    "La entrevista motivacional es primera línea para ambivalencia: empatía, desarrollo de discrepancia, evitar confrontación y apoyar autoeficacia. OARS (preguntas abiertas, afirmaciones, reflexiones, resúmenes) prepara el cambio. La TCC para adicciones trabaja activadores, creencias, afrontamiento y prevención de recaída.",
                    "Grupos de apoyo complementan pero no reemplazan tratamiento profesional en trastorno severo. Psicoeducación familiar sobre adicción como condición crónica, no falta de voluntad. Coordine psiquiatría si farmacoterapia (naltrexona, acamprosato, buprenorfina según sustancia y país).",
                ),
            },
            {
                "h2": "Riesgo, urgencias y derivación interdisciplinaria",
                "html": p(
                    "Derive con urgencia si intoxicación aguda, abstinencia convulsiva, ideación suicida, psicosis, embarazo con consumo activo o violencia intrafamiliar. Riesgo moderado: consumo diario con deterioro laboral — intensifique frecuencia y contratos de seguridad.",
                    "Documente consentimiento, confidencialidad y límites con menores o mandatos legales. Informes psicológicos bien fundados facilitan acceso a programas públicos saturados en la región.",
                ),
            },
            {
                "h2": "Seguimiento clínico y registro de progreso",
                "html": p(
                    "Registre línea base de consumo, objetivos negociados y escalas cada cuatro a ocho semanas. Supervisión clínica ayuda ante recaídas repetidas y contratransferencia.",
                    "Integrar expediente, recordatorios y tamizajes repetidos reduce abandono; equipos en Latinoamérica centralizan ASSIST y notas en <a href=\"https://app.kalyo.io/register\">Kalyo</a> para evitar duplicar captura administrativa.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "¿Toda persona que bebe en exceso tiene trastorno por uso de alcohol?",
                "a": "No. El DSM-5 exige un patrón maladaptativo persistente con criterios específicos en doce meses. Episodios aislados de borrachera no equivalen a trastorno, aunque pueden indicar riesgo. AUDIT ayuda a estratificar.",
            },
            {
                "q": "¿La adicción a redes sociales está en el DSM-5?",
                "a": "El trastorno por juego de apuestas está codificado; otras conductas se investigan como trastornos relacionados. Documente deterioro funcional y plan de reducción conductual mientras la nosología evoluciona.",
            },
            {
                "q": "¿Puede el psicólogo indicar medicación para abstinencia?",
                "a": "La prescripción corresponde al médico. El psicólogo identifica indicación, coordina derivación y continúa psicoterapia y seguimiento de adherencia.",
            },
            {
                "q": "¿Qué hacer ante recaída?",
                "a": "Normalícela como parte frecuente del curso, revise disparadores, ajuste prevención de recaída y evalúe mayor intensidad terapéutica. Evite castigo moral que aumente vergüenza.",
            },
            {
                "q": "¿Cómo involucrar a la familia?",
                "a": "Con consentimiento del adulto. En menores, equilibre confidencialidad adolescente y responsabilidad parental. Psicoeducación sobre craving y apoyo sin control coercitivo.",
            },
        ],
        "howto": {
            "name": "Protocolo breve de entrevista motivacional para adicción",
            "steps": [
                {"name": "Explorar consumo", "text": "Preguntas abiertas sobre patrón, consecuencias y metas. Refleje ambivalencia sin confrontar."},
                {"name": "Desarrollar discrepancia", "text": "Contraste valores (familia, salud) con conducta actual. Deje que el paciente verbalice motivos de cambio."},
                {"name": "Afirmar fortalezas", "text": "Reconozca intentos previos y recursos para sostener autoeficacia."},
                {"name": "Plan SMART", "text": "Objetivo pequeño verificable y cita de seguimiento con escala acordada."},
                {"name": "Resumen motivacional", "text": "Sintetice motivos declarados por el paciente y próximo paso concreto."},
            ],
        },
        "related": [
            {"href": "/articulos/dast-10-deteccion-drogas.html", "label": "DAST-10: tamizaje de consumo de drogas"},
            {"href": "/articulos/assist-evaluacion-sustancias-oms.html", "label": "ASSIST: evaluación de sustancias OMS"},
            {"href": "/articulos/cage-tamizaje-alcoholismo.html", "label": "CAGE: tamizaje breve de alcohol"},
            {"href": "/articulos/adiccion-redes-sociales.html", "label": "Adicción a redes sociales"},
        ],
        "cta_h2": "Da seguimiento a tamizajes de adicción",
        "cta_p": "Aplica AUDIT, DAST o ASSIST y guarda la evolución del consumo con recordatorios de sesión.",
        "keywords": "adiccion que es, trastorno por uso sustancias, DSM-5, entrevista motivacional, ASSIST",
        "card_title": "Adicción: qué es",
        "card_p": "Tipos, DSM-5, entrevista motivacional e intervención para psicólogos.",
        "after_href": "/articulos/adiccion-redes-sociales.html",
        "after_loc": "https://kalyo.io/articulos/adiccion-redes-sociales.html",
    }


# Remaining five articles imported at runtime to keep file size manageable
def anorexia(p):
    from mk_batch7_a2_a7_part2 import anorexia as fn

    return fn(p)


def tlp(p):
    from mk_batch7_a2_a7_part2 import tlp as fn

    return fn(p)


def paralisis(p):
    from mk_batch7_a2_a7_part2 import paralisis as fn

    return fn(p)


def tdah_adultos(p):
    from mk_batch7_a2_a7_part2 import tdah_adultos as fn

    return fn(p)


def esquizofrenia(p):
    from mk_batch7_a2_a7_part2 import esquizofrenia as fn

    return fn(p)
