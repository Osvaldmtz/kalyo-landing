#!/usr/bin/env python3
"""Batch 8 remaining clinical SEO article specs (6 slugs)."""
from __future__ import annotations

import json
import re
from pathlib import Path

KALYO = '<a href="https://app.kalyo.io/register">Kalyo</a>'


def wc(text: str) -> int:
    t = re.sub(r"<[^>]+>", " ", text)
    return len(re.sub(r"\s+", " ", t).strip().split())


def body_words(spec: dict) -> int:
    parts = [spec["intro"]]
    for s in spec["sections"]:
        parts.append(s["html"])
    for f in spec["faqs"]:
        parts.append(f["q"] + " " + f["a"])
    return sum(wc(p) for p in parts)


def kalyo_count(spec: dict) -> int:
    blob = json.dumps(spec, ensure_ascii=False)
    return blob.count("https://app.kalyo.io/register")


def p(*paras: str) -> str:
    return "".join(f"<p>{x}</p>" for x in paras)


def validate(spec: dict) -> None:
    slug = spec["slug"]
    tl = len(spec["title"])
    if not (55 <= tl <= 60):
        raise ValueError(f"{slug} title len {tl}: {spec['title']!r}")
    dl = len(spec["description"])
    if not (150 <= dl <= 160):
        raise ValueError(f"{slug} desc len {dl}: {spec['description']!r}")
    iw = wc(spec["intro"])
    if not (50 <= iw <= 60):
        raise ValueError(f"{slug} intro words {iw}")
    bw = body_words(spec)
    if bw < 1250:
        raise ValueError(f"{slug} body words {bw} < 1250")
    if kalyo_count(spec) != 1:
        raise ValueError(f"{slug} kalyo links {kalyo_count(spec)}")
    if len(spec["sections"]) != 6:
        raise ValueError(f"{slug} sections {len(spec['sections'])}")
    if len(spec["faqs"]) != 5:
        raise ValueError(f"{slug} faqs {len(spec['faqs'])}")


SPECS: list[dict] = []

# --- 1 adiccion-que-es ---
SPECS.append(
    {
        "slug": "adiccion-que-es",
        "title": "Adicción qué es: tipos, DSM-5 y protocolo clínico | Kalyo",
        "description": "Adicción qué es: trastornos DSM-5, entrevista motivacional, protocolo clínico integral y derivación oportuna para psicólogos en consulta privada y pública.",
        "keywords": "adicción qué es, DSM-5, trastorno por uso de sustancias, entrevista motivacional, psicología clínica, dependencia, intervención breve",
        "h1": "Adicción qué es: tipos, criterios DSM-5 e intervención clínica",
        "breadcrumb_short": "Adicción qué es",
        "hero_alt": "Consulta psicológica sobre adicción, evaluación clínica y plan de tratamiento",
        "inline_alt": "Esquema de tipos de adicción y niveles de severidad según DSM-5",
        "intro": "La adicción, en sentido clínico, designa trastornos por uso de sustancias o conductas compulsivas con pérdida de control, craving y deterioro funcional pese a consecuencias. El DSM-5 unifica dependencia y abuso en un espectro de severidad. Para psicólogos en Latinoamérica, reconocer subtipos, comorbilidades y aplicar entrevista motivacional dentro de un protocolo estructurado es clave para derivación oportuna y continuidad asistencial.",
        "sections": [
            {
                "h2": "Definición clínica: adicción qué es en DSM-5",
                "html": p(
                    "Cuando familias o instituciones preguntan <strong>adicción qué es</strong>, conviene traducir el concepto popular a categorías diagnósticas. El DSM-5 agrupa los <strong>trastornos por uso de sustancias</strong> (alcohol, cannabis, opioides, estimulantes, sedantes, tabaco, entre otros) y reconoce el <strong>trastorno por juego</strong> como adicción conductual prototípica. El núcleo clínico incluye consumo o conducta en cantidad o frecuencia mayor a la planificada, deseo intenso (craving), tiempo dedicado a obtener, usar o recuperarse, tolerancia, abstinencia cuando aplica, y uso continuado pese a problemas interpersonales, laborales, legales o de salud.",
                    "La severidad se gradúa leve, moderada o grave según número de criterios cumplidos (2–3, 4–5, 6 o más en un periodo de 12 meses). En consulta privada es frecuente que el paciente minimice daños o externalice causas; el psicólogo debe documentar ejemplos conductuales concretos, no solo autoinforme. La adicción no es sinónimo de «mala voluntad»: implica circuitos de recompensa, aprendizaje asociativo y factores biopsicosociales que modulan recaída.",
                    "En población adolescente y adulta joven conviene diferenciar experimentación normativa, uso social ocasional y trastorno. En adultos mayores, el uso de benzodiacepinas o alcohol puede enmascararse como insomnio o dolor crónico. La formulación clínica debe integrar historia familiar, trauma, trastornos del ánimo, TDAH no tratado y contexto socioeconómico (acceso a sustancias, violencia, desempleo).",
                )
                + """
<ul>
<li><strong>Control perdido:</strong> intentos fallidos de reducir o dejar.</li>
<li><strong>Craving:</strong> deseo urgente o obsesivo de la sustancia o conducta.</li>
<li><strong>Roles sociales:</strong> abandono de actividades importantes por el uso.</li>
<li><strong>Uso riesgoso:</strong> situaciones peligrosas (p. ej., conducir intoxicado).</li>
</ul>""",
            },
            {
                "h2": "Tipos de adicción: sustancias, conductas y patrones mixtos",
                "html": p(
                    "Clínicamente distinguimos adicciones a sustancias psicoactivas y adicciones conductuales (juego, en investigación otras como compras compulsivas o uso problemático de internet). Cada sustancia tiene perfil de abstinencia, riesgo médico agudo y vía de administración que altera curso y urgencia de derivación. El alcohol y los opioides tienen alto riesgo de abstinencia grave; cannabis y estimulantes pueden presentar craving intenso con menor riesgo vital inmediato, pero sí deterioro psiquiátrico.",
                    "Las adicciones conductuales comparten pérdida de control, preocupación cognitiva y escalada de la conducta. El juego patológico puede destruir finanzas familiares antes de que el paciente consulte psicología. En LATAM, coexistencia de alcohol con violencia de pareja o trabajo informal complica adherencia. Documentar policonsumo y secuencia temporal (p. ej., alcohol como «downer» tras cocaína) orienta intervención y psicoeducación.",
                )
                + """
<table class="items-table">
<thead><tr><th>Clase</th><th>Ejemplos</th><th>Nota clínica</th></tr></thead>
<tbody>
<tr><td>Sustancias legales</td><td>Alcohol, tabaco, benzodiacepinas</td><td>Alta prevalencia; tamizaje en atención primaria</td></tr>
<tr><td>Sustancias ilícitas</td><td>Cocaína, cannabis, opioides</td><td>Evaluar vías, overdose, VIH/hepatitis</td></tr>
<tr><td>Conductual (DSM-5)</td><td>Trastorno por juego</td><td>Craving y abstinencia conductual reportados</td></tr>
<tr><td>Policonsumo</td><td>Alcohol + estimulantes</td><td>Priorizar seguridad y desintoxicación médica</td></tr>
</tbody>
</table>
<ol>
<li>Identificar sustancia o conducta principal y secundarias.</li>
<li>Valorar último uso, cantidad y contexto de riesgo inmediato.</li>
<li>Explorar motivadores de cambio y barreras (estigma, empleo, familia).</li>
</ol>""",
            },
            {
                "h2": "Evaluación inicial y cribado en consulta psicológica",
                "html": p(
                    "La evaluación combina entrevista clínica estructurada, escalas breves y exploración de comorbilidades. Instrumentos como AUDIT (alcohol), DAST (drogas) o ASSIST (OMS) orientan severidad y derivación; no sustituyen diagnóstico. Registre antecedentes de convulsiones por abstinencia, intentos previos de desintoxicación, red de apoyo y acceso a tratamiento residencial o ambulatorio.",
                    "Explore motivación al cambio con escala tipo regla de Readiness Ruler. Indague trauma, TEPT, trastorno bipolar (automedicación con estimulantes o alcohol), y trastornos de personalidad que dificultan alianza. En menores, la evaluación requiere consentimiento parental y enfoque sistémico. Si hay riesgo de autolesión, intoxicación aguda o violencia doméstica, la prioridad es seguridad y coordinación con medicina de urgencias o psiquiatría.",
                    "Documente objetivos del paciente en sus palabras: «bajar consumo», «recuperar custodia», «dejar de apostar». Esos objetivos anclan la entrevista motivacional y el plan de seguimiento. Evite confrontación prematura; la ambivalencia es normativa, no resistencia terapéutica per se.",
                ),
            },
            {
                "h2": "Entrevista motivacional: principios y microhabilidades",
                "html": p(
                    "La <strong>entrevista motivacional (EM)</strong> es un estilo de conversación centrado en el paciente que evoca cambio desde sus propios valores. Principios: expresar empatía, desarrollar discrepancia entre conducta actual y metas vitales, sortear resistencia sin confrontar y apoyar autoeficacia. Microhabilidades OARS: preguntas abiertas, afirmaciones, reflexiones y resúmenes que consolidan motivación.",
                    "Técnicas clave incluyen exploración de ambivalencia («de un lado… de otro lado…»), preguntas de desarrollo de discrepancia («¿Cómo encaja el consumo con ser buen padre?») y escala de importancia/confianza. El psicólogo evita la trampa del «experto que sabe por qué debe dejar»; el cambio sostenido suele requerir que el paciente verbalice razones propias. EM puede integrarse en pocas sesiones (SBIRT) o en tratamiento prolongado con terapia cognitivo-conductual o grupos.",
                    "En adicciones conductuales, adaptar EM al ciclo de pérdidas financieras o vergüenza. Refuerce fortalezas previas de control en otras áreas de vida. Si el paciente está en precontemplación, el objetivo realista puede ser reducción de daños o acuerdo de revisión, no abstinencia inmediata.",
                )
                + """
<ul>
<li><strong>Reflexión doble:</strong> «Te preocupa tu salud y a la vez el consumo te alivia el estrés».</li>
<li><strong>Pregunta clave:</strong> «¿Qué te gustaría que fuera distinto en seis meses?»</li>
<li><strong>Planificación:</strong> convertir intención en pasos SMART verificables.</li>
</ul>""",
            },
            {
                "h2": "Protocolo de intervención psicológica y coordinación médica",
                "html": p(
                    "Un <strong>protocolo de intervención</strong> típico incluye: (1) evaluación y triage de riesgo médico; (2) acuerdo de objetivos (abstinencia, reducción guiada cuando sea clínicamente aceptable); (3) psicoeducación sobre craving, recaída y señales de alerta; (4) habilidades de afrontamiento (manejo de estímulos, prevención de recaída de Marlatt adaptada); (5) tratamiento de comorbilidades (TCC para depresión/ansiedad); (6) vinculación a grupos de autoayuda o programas intensivos.",
                    "La desintoxicación de alcohol o benzodiacepinas puede requerir hospitalización; el psicólogo no sustituye ese cuidado. Tras estabilización, la terapia individual o familiar reduce recaídas. En opioides, el tratamiento de mantenimiento con agonistas es competencia médica; el rol psicológico es adherencia, prevención de recaída y reinserción. Registre sesiones, objetivos por visita y contactos con médico tratante.",
                    "Para continuidad documental y recordatorios de control, muchos consultorios centralizan historias, escalas AUDIT/DAST y planes en {kalyo}, manteniendo confidencialidad y trazabilidad sin sustituir supervisión en adicciones.".format(
                        kalyo=KALYO
                    ),
                ),
            },
            {
                "h2": "Recaída, prevención y derivación en el sistema de salud",
                "html": p(
                    "La recaída se conceptualiza como proceso, no evento único: cambios emocionales, exposición a contextos, creencias de eficacia reducida. Enseñe análisis funcional breve: antecedentes, conducta, consecuencias. Planifique estrategias para «días de alto riesgo» (festividades, duelos, conflictos laborales). Si hay recaída, evite etiqueta de fracaso; reevalúe severidad y nivel de cuidado.",
                    "Derive a psiquiatría cuando hay psicosis inducida, bipolaridad activa, embarazo con dependencia o polifarmacia. Derive a trabajo social si hay riesgo de indigencia o violencia. En LATAM, mapee recursos públicos limitados y sea transparente sobre listas de espera, combinando EM con metas intermedias realistas.",
                    "El seguimiento a largo plazo monitoriza consumo (autoinforme, pruebas cuando hay consentimiento), funcionamiento laboral, red social y salud mental. Revisar contraindicaciones si el paciente retoma consumo de riesgo mientras toma medicación psiquiátrica.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "¿Toda adicción requiere abstinencia total?",
                "a": "No siempre. En algunos contextos clínicos se trabaja reducción de daños o metas graduales, especialmente cuando no hay riesgo médico inmediato y el paciente no acepta abstinencia. La decisión debe ser informada, documentada y revisada con criterios de seguridad.",
            },
            {
                "q": "¿La entrevista motivacional sustituye la terapia de adicciones?",
                "a": "No. EM es un marco comunicacional que puede ser fase inicial o componente transversal. Trastornos moderados-graves suelen requerir protocolos más intensivos, grupos, tratamiento de comorbilidades y, en sustancias específicas, manejo médico.",
            },
            {
                "q": "¿Cómo diferenciar uso recreativo de trastorno en adolescentes?",
                "a": "Busque criterios DSM-5: fallos escolares, conflictos legales, uso en situaciones peligrosas, tolerancia, abandono de actividades y persistencia pese a problemas. El contexto familiar y el desarrollo cerebral aumentan vulnerabilidad; no normalice consumo frecuente por «etapa».",
            },
            {
                "q": "¿El psicólogo puede tratar intoxicación aguda?",
                "a": "No. Intoxicación o abstinencia grave requieren valoración médica urgente. El psicólogo estabiliza alianza posterior, psicoeduca y continuidad ambulatoria una vez resuelto el riesgo vital.",
            },
            {
                "q": "¿Qué escalas usar en consulta privada?",
                "a": "AUDIT para alcohol, DAST-10 o ASSIST para otras sustancias, más PHQ-9/GAD-7 para comorbilidad. Repita en seguimiento para objetivar cambio. Las escalas orientan; el diagnóstico integra entrevista y observación clínica.",
            },
        ],
        "howto": {
            "name": "Cómo estructurar la primera consulta por adicción",
            "steps": [
                {
                    "name": "Triage de seguridad",
                    "text": "Evalúe intoxicación, abstinencia grave, ideación suicida o violencia; derive a urgencias si aplica.",
                },
                {
                    "name": "Historia de uso",
                    "text": "Documente sustancias, cantidad, vía, edad de inicio, intentos previos de tratamiento y consecuencias legales o médicas.",
                },
                {
                    "name": "Cribado estandarizado",
                    "text": "Aplique AUDIT, DAST o ASSIST y explore comorbilidades psiquiátricas.",
                },
                {
                    "name": "Entrevista motivacional",
                    "text": "Explore ambivalencia, valores y disposición al cambio con reflexiones y resúmenes.",
                },
                {
                    "name": "Plan y derivación",
                    "text": "Acuerde objetivos, psicoeducación, frecuencia de sesiones y vinculación médica o programas intensivos según severidad.",
                },
            ],
        },
        "related": [
            {"href": "/articulos/audit-test-alcoholismo.html", "label": "AUDIT: cribado de alcohol"},
            {"href": "/articulos/dudit-tamizaje-drogas.html", "label": "DUDIT: tamizaje de drogas"},
            {"href": "/articulos/adiccion-redes-sociales.html", "label": "Adicción a redes sociales"},
        ],
        "cta_h2": "Organiza el seguimiento en adicciones con Kalyo",
        "cta_p": "Registra escalas, objetivos terapéuticos y coordinación con medicina en un expediente clínico digital.",
        "after_href": "/articulos/adiccion-redes-sociales.html",
        "after_loc": "https://kalyo.io/articulos/adiccion-redes-sociales.html",
        "card_title": "Adicción qué es: DSM-5 e intervención",
        "card_p": "Tipos de adicción, entrevista motivacional y protocolo clínico para psicólogos.",
    }
)

# --- 2 anorexia-que-es ---
SPECS.append(
    {
        "slug": "anorexia-que-es",
        "title": "Anorexia qué es: DSM-5, EAT-26 y abordaje clínico | Kalyo",
        "description": "Anorexia nerviosa: criterios DSM-5, diferencial con bulimia, escalas EAT-26/EDI, abordaje multidisciplinario y rol del psicólogo clínico en Latinoamérica.",
        "keywords": "anorexia qué es, anorexia nerviosa, DSM-5, EAT-26, EDI, bulimia, trastornos alimentarios, psicología clínica",
        "h1": "Anorexia qué es: criterios DSM-5, evaluación y tratamiento multidisciplinario",
        "breadcrumb_short": "Anorexia qué es",
        "hero_alt": "Evaluación clínica de anorexia nerviosa y trastornos alimentarios en consulta",
        "inline_alt": "Comparación clínica entre anorexia restrictiva y presentaciones purgativas",
        "intro": "La anorexia nerviosa es un trastorno alimentario grave con restricción calórica, miedo intenso a engordar y alteración de la imagen corporal. El DSM-5 especifica subtipos restrictivo y purgativo. El psicólogo clínico participa en evaluación, psicoeducación familiar y terapia cognitivo-conductual dentro de un equipo multidisciplinario con medicina y nutrición. La detección temprana con EAT-26 reduce riesgo médico.",
        "sections": [
            {
                "h2": "Definición clínica: anorexia qué es en DSM-5",
                "html": p(
                    "La <strong>anorexia nerviosa</strong> se define por restricción persistente de ingesta energética relativa a necesidades, con peso corporal significativamente bajo, miedo intenso a ganar peso o conductas que interfieren con aumento de peso, y alteración en la experiencia del peso o la forma corporal. En adolescentes, el criterio de peso bajo se interpreta respecto a percentiles evolutivos, no solo IMC adulto.",
                    "El DSM-5 especifica gravedad según IMC aproximado (leve ≥17, moderada 16–16.99, grave 15–15.99, extrema <15 en adultos). Subtipo restrictivo: solo restricción. Subtipo purgativo: purgas, laxantes, ejercicio compulsivo o ayuno extremo. Muchas personas alternan patrones; documente curso longitudinal, no solo última semana.",
                    "En consulta hispanohablante, familias pueden normalizar dietas «saludables» extremas o deporte competitivo. Explore funcionamiento escolar, aislamiento social, rigidez alimentaria, rituales (cortar en cubos, pesar alimentos) y amenorrea o retraso puberal. La anorexia tiene una de las mayores mortalidades entre trastornos psiquiátricos; el riesgo médico guía urgencia de derivación.",
                ),
            },
            {
                "h2": "Anorexia frente a bulimia nerviosa: diferencial clínico",
                "html": p(
                    "Tanto anorexia como <a href=\"/articulos/bulimia-que-es.html\">bulimia nerviosa</a> incluyen preocupación por peso y forma, pero difieren en peso corporal, patrón alimentario y complicaciones médicas inmediatas. La bulimia típica presenta episodios recurrentes de atracón con conductas compensatorias en peso normal o sobrepeso; la anorexia destaca restricción crónica con peso bajo.",
                    "Existen presentaciones atípicas: anorexia purgativa sin bajo peso (especificador DSM-5), trastorno por atracón, ARFID. El diferencial con depresión mayor (apetito reducido sin miedo a engordar), hipotiroidismo, enfermedad inflamatoria intestinal o celiaquía requiere historia médica y laboratorios. Documente inicio, precipitantes (bullying, deporte, trauma) y creencias centrales sobre valor personal ligado al control alimentario.",
                )
                + """
<ul>
<li><strong>Anorexia:</strong> restricción, peso bajo, miedo a ganar.</li>
<li><strong>Bulimia:</strong> atracones + compensación, peso usualmente normal-alto.</li>
<li><strong>Común:</strong> vergüenza, secreto, comorbilidad ansiosa/depresiva.</li>
</ul>
<ol>
<li>Registrar peso, talla, IMC o percentil y tendencia reciente.</li>
<li>Preguntar por purgas, laxantes, diuréticos y ejercicio compulsivo.</li>
<li>Explorar imagen corporal con ejemplos conductuales concretos.</li>
</ol>""",
            },
            {
                "h2": "Evaluación psicológica: EAT-26, EDI y entrevista clínica",
                "html": p(
                    "Las escalas <a href=\"/articulos/eat-26-trastornos-alimentarios.html\">EAT-26</a> y el Eating Disorder Inventory (EDI) aportan cribado de actitudes alimentarias, miedo a engordar, perfeccionismo e interocepción. Son útiles como línea base y seguimiento, pero no diagnostican solas. Complemente con entrevista semiestructurada (p. ej. EDE-Q) cuando haya formación.",
                    "Explore historia del desarrollo, eventos vitales, trauma, bullying por peso, deporte de alto rendimiento y modelado familiar de dieta. Valore comorbilidades: TOC (rituales alimentarios), TDAH (olvido de comidas vs restricción), trastornos de personalidad, abuso de sustancias. En menores, incluir a cuidadores con cuidado: la parentalidad puede ser sobreprotectora o crítica, ambas relevantes para mantenimiento.",
                )
                + """
<table class="items-table">
<thead><tr><th>Instrumento</th><th>Enfoque</th><th>Uso clínico</th></tr></thead>
<tbody>
<tr><td>EAT-26</td><td>Actitudes y conductas alimentarias</td><td>Tamizaje rápido en consulta</td></tr>
<tr><td>EDI-3</td><td>Dimensiones psicológicas</td><td>Perfil cognitivo-afectivo</td></tr>
<tr><td>EDE-Q</td><td>Entrevista autorreporte</td><td>Seguimiento de síntomas DSM</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "Riesgo médico y coordinación multidisciplinaria",
                "html": p(
                    "Priorice signos de inestabilidad: bradicardia, hipotensión ortostática, hipoglucemia, alteraciones electrolíticas, prolongación QT, osteoporosis, amenorrea. La hospitalización médica es indicada con criterios de gravedad (p. ej. peso muy bajo, síncope, potasio bajo). El psicólogo coordina con pediatría, medicina interna, psiquiatría y nutrición clínica; no trate restricción severa solo en ambulatorio.",
                    "El plan multidisciplinario define metas de restitución ponderal gradual, normalización de conductas alimentarias, reducción de ejercicio compulsivo y manejo de comorbilidades. Psicoeducación familiar sobre no culpar, supervisión de comidas en fases agudas y manejo de conflictos en la mesa. En adultos, explore impacto laboral y de pareja; en adolescentes, acuerdos escolares de adaptación temporal.",
                    "Documente consentimientos, contactos de emergencia y señales de alarma para familias. Si hay ideación suicida elevada (frecuente en anorexia), active protocolo de seguridad. La recuperación es lenta; fije metas intermedias realistas y celebre avances funcionales, no solo números en báscula.",
                ),
            },
            {
                "h2": "Intervención psicológica basada en evidencia",
                "html": p(
                    "En adolescentes, la terapia familiar basada en la evidencia (FBT/Maudsley) suele ser primera línea: padres temporalmente a cargo de la re-nutrición con apoyo terapéutico. En adultos, terapia cognitivo-conductual para trastornos alimentarios (CBT-E) aborda restricción, pesaje, evitación de «alimentos prohibidos» y sobrevaloración del peso. Integre habilidades de regulación emocional cuando hay alexitimia o trauma.",
                    "Evite reforzar conductas de búsqueda de reassurance sobre peso. Trabaje creencias nucleares («ser delgada es ser valiosa») con experimentos conductuales graduados. Para continuidad de sesiones, escalas EAT-26/EDI y planes de comidas acordados, centralice registro en {kalyo} sin sustituir supervisión en trastornos alimentarios.".format(
                        kalyo=KALYO
                    ),
                    "Coordine con nutricionista para planes individualizados; el psicólogo no prescribe dietas. Si hay purgas, monitorice riesgo de hipopotasemia. Derive a psiquiatría si hay indicación de ISRS para comorbilidad o antipsicóticos de baja dosis en casos seleccionados (decisión médica).",
                ),
            },
            {
                "h2": "Seguimiento, recaídas y pronóstico",
                "html": p(
                    "El seguimiento combina peso/medidas acordadas clínicamente, frecuencia de atracones o purgas, flexibilidad alimentaria, funcionamiento social y escalas repetidas. Las recaídas suelen aparecer en transiciones (vuelta a clases, rupturas). Planifique prevención identificando disparadores y red de apoyo.",
                    "Algunas personas evolucionan hacia patrón bulímico o trastorno por atracón tras restitución; reevalúe diagnóstico. Mantenga enfoque compasivo: la vergüenza alimentaria dificulta divulgación honesta. En LATAM, acceso limitado a equipos especializados obliga a redes de derivación claras y teleconsulta coordinada cuando sea posible.",
                    "Informe a escuela o trabajo solo con consentimiento y en términos funcionales. Proteja confidencialidad del adolescente dentro de límites de seguridad. Documente criterios de alta: peso estable en rango acordado, menstruación recuperada si aplica, disminución de rituales y mejoría en salud mental comórbida.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "¿EAT-26 positivo confirma anorexia?",
                "a": "No. EAT-26 es cribado de riesgo. Confirma necesidad de evaluación clínica completa con peso, historia médica, entrevista especializada y coordinación multidisciplinaria.",
            },
            {
                "q": "¿Cuándo hospitalizar por anorexia?",
                "a": "Ante inestabilidad médica, peso extremadamente bajo, síncope, electrolitos críticos, bradicardia significativa o riesgo suicida agudo. La decisión es médica con apoyo del equipo.",
            },
            {
                "q": "¿Puede haber anorexia sin bajo peso visible?",
                "a": "Sí, con especificadores o presentaciones atípicas, o en fases tempranas. No descarte preocupación clínica solo por IMC aparentemente normal si hay restricción severa y miedo intenso.",
            },
            {
                "q": "¿El psicólogo debe pesar al paciente?",
                "a": "Depende del protocolo del equipo. Si se pesa, hacerlo con acuerdo terapéutico claro y enfoque en tendencias, no en números aislados que alimenten rumiación.",
            },
            {
                "q": "¿Cómo involucrar a la familia sin culpar?",
                "a": "Psicoeducar sobre biopsicosocial del trastorno, roles de apoyo concreto (supervisión de comidas al inicio en FBT), y terapia familiar para comunicación y límites.",
            },
        ],
        "howto": {
            "name": "Cómo abordar la sospecha de anorexia nerviosa",
            "steps": [
                {"name": "Tamizaje", "text": "Aplique EAT-26, explore miedo a engordar, restricción y peso reciente."},
                {"name": "Valoración médica", "text": "Derive o coordine signos vitales, laboratorios y evaluación de riesgo de hospitalización."},
                {"name": "Entrevista clínica", "text": "Documente inicio, subtipo, purgas, ejercicio y comorbilidades psiquiátricas."},
                {"name": "Plan multidisciplinario", "text": "Acuerde metas de restitución, nutrición, terapia (FBT/CBT-E) y frecuencia de control."},
                {"name": "Seguimiento", "text": "Monitoree peso tendencial, escalas, funcionamiento y señales de recaída con plan de crisis."},
            ],
        },
        "related": [
            {"href": "/articulos/bulimia-que-es.html", "label": "Bulimia qué es"},
            {"href": "/articulos/eat-26-trastornos-alimentarios.html", "label": "EAT-26: trastornos alimentarios"},
            {"href": "/articulos/ede-q-cuestionario-trastornos-alimentarios.html", "label": "EDE-Q: evaluación alimentaria"},
        ],
        "cta_h2": "Da seguimiento a trastornos alimentarios con orden",
        "cta_p": "Centraliza escalas, planes terapéuticos y notas de equipo multidisciplinario en tu consultorio.",
        "after_href": "/articulos/alexitimia.html",
        "after_loc": "https://kalyo.io/articulos/alexitimia.html",
        "card_title": "Anorexia qué es: DSM-5 y evaluación",
        "card_p": "Criterios DSM-5, EAT-26/EDI, diferencial con bulimia y abordaje multidisciplinario.",
    }
)

# --- 3 tlp-trastorno-limite ---
SPECS.append(
    {
        "slug": "tlp-trastorno-limite",
        "title": "TLP qué es: 9 criterios DSM-5, DBT y evaluación PAI | Kalyo",
        "description": "TLP qué es: los 9 criterios DSM-5, evaluación con PAI/ZAN-BPD, terapia dialéctico-conductual DBT y manejo clínico del trastorno límite para psicólogos.",
        "keywords": "TLP, trastorno límite de la personalidad, DSM-5, DBT, PAI, ZAN-BPD, psicología clínica, personalidad",
        "h1": "Trastorno límite de la personalidad (TLP): criterios, evaluación y DBT",
        "breadcrumb_short": "TLP: trastorno límite",
        "hero_alt": "Formulación clínica del trastorno límite de la personalidad en psicoterapia",
        "inline_alt": "Esquema de criterios DSM-5 del TLP y enfoque dialéctico-conductual",
        "intro": "El trastorno límite de la personalidad (TLP) se caracteriza por inestabilidad afectiva, impulsividad, alteraciones de la identidad y dificultades interpersonales intensas. El DSM-5 exige cinco o más de nueve criterios. Para psicólogos clínicos, combinar evaluación estructurada (PAI, ZAN-BPD), manejo de riesgo suicida y terapia dialéctico-conductual (DBT) es central en consulta ambulatoria y derivación.",
        "sections": [
            {
                "h2": "TLP qué es: definición y prevalencia clínica",
                "html": p(
                    "El <strong>trastorno límite de la personalidad</strong> es un patrón persistente de inestabilidad en relaciones, autoimagen y afectos, con marcada impulsividad que inicia en la adultez emergente. Prevalencia aproximada 1–2% en comunidad, mayor en consulta ambulatoria y hospitalización psiquiátrica. Históricamente estigmatizado; hoy se conceptualiza como disregulación emocional y de conducta con bases biopsicosociales (temperamento, invalidación crónica, trauma).",
                    "En LATAM, acceso limitado a DBT especializada obliga a adaptar protocolos y supervisión. El psicólogo debe equilibrar validación empática con límites claros sobre conductas de riesgo. Evite etiquetas peyorativas en historias clínicas; use lenguaje diagnóstico preciso y plan de tratamiento orientado a habilidades.",
                    "El TLP se asocia con alta comorbilidad: depresión, TEPT, trastornos alimentarios, abuso de sustancias y trastornos del ánimo bipolares II. La formulación debe distinguir labilidad borderline de episodios maniacos verdaderos y de reexperimentación traumática.",
                ),
            },
            {
                "h2": "Los 9 criterios DSM-5 del TLP explicados",
                "html": p(
                    "El DSM-5 lista nueve criterios; se requieren al menos cinco para el diagnóstico. Cada criterio debe ser persistente y causar malestar o deterioro significativo.",
                )
                + """
<table class="items-table">
<thead><tr><th>#</th><th>Criterio DSM-5 (resumen)</th><th>Manifestación clínica</th></tr></thead>
<tbody>
<tr><td>1</td><td>Esquivenza de abandono real o imaginado</td><td>Clinginess, celos, prisa en vínculos</td></tr>
<tr><td>2</td><td>Relaciones inestables e intensas</td><td>Idealización/devaluación alternantes</td></tr>
<tr><td>3</td><td>Alteración de identidad</td><td>Sentido de self vacío o cambiante</td></tr>
<tr><td>4</td><td>Impulsividad dañina (≥2 áreas)</td><td>Gastos, sexo, sustancias, conducción</td></tr>
<tr><td>5</td><td>Conducta suicida o autolesiones</td><td>Amenazas, intentos, cortes repetidos</td></tr>
<tr><td>6</td><td>Labilidad afectiva</td><td>Episodios disfóricos horas a días</td></tr>
<tr><td>7</td><td>Crónica sensación de vacío</td><td>Aburrimiento existencial intenso</td></tr>
<tr><td>8</td><td>Ira inapropiada e intensa</td><td>Explosiones o ira sostenida</td></tr>
<tr><td>9</td><td>Ideación paranoide/disociativa transitoria</td><td>Bajo estrés, breve duración</td></tr>
</tbody>
</table>
<p>Documente ejemplos conductuales por criterio y duración mínima de un año en adultez joven. En adolescentes, use cautela diagnóstica: muchos síntomas pueden ser inespecíficos del desarrollo.</p>""",
            },
            {
                "h2": "Evaluación con PAI, ZAN-BPD y entrevista de personalidad",
                "html": p(
                    "El Inventario de Evaluación de la Personalidad (PAI) incluye escalas relevantes para impulsividad, inestabilidad afectiva y indicadores de TLP; útil como complemento, no como diagnóstico aislado. El ZAN-BPD es entrevista breve de gravedad que cuantifica síntomas nucleares y orienta seguimiento.",
                    "Combine con entrevista clínica longitudinal, historia de trauma (abuso, negligencia, invalidación emocional), patrones vinculares desde infancia y conductas autolesivas previas. Explore episodios disociativos breves bajo estrés. Diferencie TLP de trastorno bipolar, TEPT complejo, TDAH adulto y trastornos narcisista o antisocial cuando hay overlap conductual.",
                    "Registre nivel de riesgo suicida con plan, medios, intentos previos y factores protectores. En TLP, la autolesión puede regular emoción más que deseo de muerte; aun así evalúe riesgo letal en cada sesión inicial.",
                )
                + """
<ul>
<li><strong>PAI:</strong> perfil amplio de psicopatología y personalidad.</li>
<li><strong>ZAN-BPD:</strong> seguimiento de gravedad en tiempo.</li>
<li><strong>MSI-BPD / SCID-II:</strong> cuando hay formación en entrevistas estructuradas.</li>
</ul>""",
            },
            {
                "h2": "Terapia dialéctico-conductual (DBT): principios y módulos",
                "html": p(
                    "La <strong>DBT</strong>, desarrollada por Linehan, integra validación dialéctica con cambio conductual. Componentes estándar: terapia individual, grupo de habilidades, coaching telefónico (cuando el protocolo lo permite) y equipo de consultores para el terapeuta. Habilidades en cuatro módulos: mindfulness, tolerancia al malestar, regulación emocional y efectividad interpersonal.",
                    "La jerarquía de objetivos prioriza (1) conductas suicidas/ autolesivas, (2) conductas que interfieren terapia, (3) calidad de vida, (4) habilidades adicionales. Los acuerdos sobre coaching y límites de contacto entre sesiones deben ser explícitos para evitar refuerzo inadvertido de crisis como única vía de regulación.",
                    "Si no hay DBT completa disponible, adapte protocolos basados en habilidades (DBT-informed CBT, mentalización, schema therapy) con supervisión. Evite terapias puramente exploratorias sin manejo de riesgo en fases agudas.",
                ),
            },
            {
                "h2": "Manejo de crisis, autolesión y contratos de seguridad",
                "html": p(
                    "Ante crisis, use validación, análisis en cadena (vulnerabilidad → precipitante → pensamiento → emoción → conducta → consecuencias) y sustitución por habilidades TIPP (temperatura, ejercicio intenso breve, respiración, relajación muscular). Los contratos de seguridad tienen evidencia mixta; enfoque en plan escrito de pasos antes de autolesión y contactos de emergencia.",
                    "Coordinación con psiquiatría para farmacoterapia sintomática (p. ej. afectividad) sin esperar que medicación sustituya psicoterapia estructurada. Hospitalización breve puede ser necesaria en riesgo inminente; planifique reingreso ambulatorio intensivo para evitar ciclos de «puerta giratoria».",
                    "Para documentar planes de crisis, habilidades practicadas y contactos del equipo, use herramientas de expediente que permitan continuidad entre sesiones en {kalyo}, especialmente si hay múltiples profesionales involucrados.".format(
                        kalyo=KALYO
                    ),
                ),
            },
            {
                "h2": "Pronóstico, estigma y trabajo interdisciplinario",
                "html": p(
                    "Estudios longitudinales muestran remisión sintomática sustancial en una proporción importante de personas con TLP a mediano plazo, especialmente con tratamiento especializado y reducción de conductas de riesgo. Comunique esperanza realista sin minimizar sufrimiento actual.",
                    "Combata estigma interno del paciente y del sistema de salud. Capacite a familiares en validación y límites (programas psychoeducativos). En pareja, evalúe violencia bidireccional y dinámicas de invalidación.",
                    "Supervisión clínica regular es casi obligatoria dado impacto emocional en terapeutas. Establezca límites de disponibilidad fuera de horario salvo protocolo DBT acordado. Derive a grupos de habilidades o programas intensivos cuando la frecuencia semanal individual sea insuficiente.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "¿Cuántos criterios DSM-5 se necesitan para TLP?",
                "a": "Al menos cinco de nueve criterios, persistentes y con deterioro clínico significativo, típicamente iniciando en adultez emergente.",
            },
            {
                "q": "¿PAI diagnostica TLP?",
                "a": "No. Aporta hipótesis y perfil; el diagnóstico requiere entrevista clínica cuidadosa, historia longitudinal y, idealmente, entrevistas estructuradas de personalidad.",
            },
            {
                "q": "¿DBT es la única terapia efectiva?",
                "a": "DBT tiene fuerte evidencia, pero también mentalización, TFP y schema therapy muestran beneficio. Elija según formación, acceso y perfil del paciente.",
            },
            {
                "q": "¿Cómo diferenciar TLP de trastorno bipolar?",
                "a": "En TLP la labilidad suele ser reactiva a interpersonales y de horas a días; en bipolar II los episodios hipomaníacos son más sostenidos y con patrones distintos de sueño y energía.",
            },
            {
                "q": "¿Debo hospitalizar por autolesión sin intento suicida?",
                "a": "Depende de gravedad, acceso a medios, riesgo de escalada e incapacidad de usar plan de seguridad. Muchas autolesiones se manejan ambulatoriamente con DBT intensiva si hay contención adecuada.",
            },
        ],
        "howto": {
            "name": "Cómo evaluar y planificar tratamiento en TLP",
            "steps": [
                {"name": "Entrevista de riesgo", "text": "Evalúe suicidio, autolesión, impulsividad y factores protectores en cada inicio."},
                {"name": "Mapeo de criterios", "text": "Documente al menos cinco criterios DSM-5 con ejemplos conductuales."},
                {"name": "Instrumentos", "text": "Aplique PAI, ZAN-BPD u otras herramientas según formación y contexto."},
                {"name": "Formulación", "text": "Integre trauma, invalidación, patrones vinculares y comorbilidades."},
                {"name": "Plan DBT o equivalente", "text": "Defina jerarquía de objetivos, habilidades, frecuencia y coordinación psiquiátrica."},
            ],
        },
        "related": [
            {"href": "/articulos/terapia-familiar-sistemica.html", "label": "Terapia familiar sistémica"},
            {"href": "/articulos/escala-pcl-5-estres-postraumatico.html", "label": "PCL-5: trauma y TEPT"},
            {"href": "/articulos/mmpi-2-rf-test-personalidad.html", "label": "MMPI-2-RF: evaluación de personalidad"},
        ],
        "cta_h2": "Documenta el seguimiento en TLP con claridad",
        "cta_p": "Registra planes de crisis, habilidades DBT y escalas de gravedad en un expediente ordenado.",
        "after_href": "/articulos/terapia-familiar-sistemica.html",
        "after_loc": "https://kalyo.io/articulos/terapia-familiar-sistemica.html",
        "card_title": "TLP: trastorno límite de la personalidad",
        "card_p": "Nueve criterios DSM-5, PAI/ZAN-BPD, DBT y manejo de crisis para psicólogos.",
    }
)

# --- 4 paralisis-del-sueno ---
SPECS.append(
    {
        "slug": "paralisis-del-sueno",
        "title": "Parálisis del sueño: causas, REM y manejo clínico | Kalyo",
        "description": "Parálisis del sueño: fisiología REM, causas frecuentes, vínculo con ansiedad y TEPT, manejo clínico psicológico y criterios de derivación médica urgente.",
        "keywords": "parálisis del sueño, hipnagogia, REM, narcolepsia, ansiedad, TEPT, PCL-5, psicología del sueño",
        "h1": "Parálisis del sueño: mecanismos, causas y abordaje clínico",
        "breadcrumb_short": "Parálisis del sueño",
        "hero_alt": "Consulta psicológica sobre parálisis del sueño e higiene del descanso",
        "inline_alt": "Diagrama del ciclo REM y atonia muscular durante el sueño",
        "intro": "La parálisis del sueño es un episodio breve de incapacidad para moverse o hablar al dormir o despertar, con conciencia preservada y alucinaciones hipnagogias frecuentes. Refleja atonia REM desincronizada. En consulta psicológica descarte narcolepsia, explore ansiedad y TEPT con PCL-5, y ofrezca psicoeducación e intervención basada en higiene del sueño.",
        "sections": [
            {
                "h2": "Qué es la parálisis del sueño: fisiología del REM",
                "html": p(
                    "Durante la fase <strong>REM</strong>, el tronco encefálico induce atonia muscular para evitar que actuemos sueños. La parálisis del sueño refleja persistencia de esa atonia unos segundos a minutos mientras la corteza sensorial y autoconciencia están activas. Puede ir acompañada de sensación de peso en el pecho, dificultad respiratoria subjetiva, miedo intenso y experiencias visuales o táctiles breves.",
                    "Es relativamente frecuente en población general (hasta un tercio reporta al menos un episodio), más en privación de sueño, horarios irregulares y trastornos del sueño primarios. No es peligrosa en sí misma, pero el miedo anticipatorio puede deteriorar higiene del sueño y aumentar ansiedad nocturna.",
                    "El psicólogo diferencia experiencia benigna aislada de patología del sueño o psiquiátrica comórbida. Pregunte frecuencia, contexto (dormir boca arriba, siestas), consumo de alcohol o estimulantes, turnos rotativos y antecedentes familiares de narcolepsia.",
                ),
            },
            {
                "h2": "Causas y factores predisponentes",
                "html": p(
                    "Factores precipitantes incluyen privación crónica de sueño, estrés agudo, cambios bruscos de horario (jet lag), consumo de alcohol nocturno y ciertos fármacos (p. ej. algunos antidepresivos pueden modificar arquitectura REM). Posición supina se asocia con más reportes, posiblemente por vía aérea y percepción de opresión torácica.",
                    "Trastornos primarios del sueño como <strong>narcolepsia</strong> (con cataplejía, somnolencia diurna irresistible) requieren derivación a medicina del sueño y pruebas como polisomnografía y test de latencias múltiples. Apnea obstructiva del sueño puede coexistir y empeorar microdespertares.",
                    "En adolescentes y adultos jóvenes universitarios, horarios caóticos y uso de pantallas nocturnas son modificables. Documente cronología y busque patrones circadianos.",
                )
                + """
<ul>
<li><strong>Privación de sueño:</strong> factor más común y modificable.</li>
<li><strong>Estrés/ansiedad:</strong> aumenta hipervigilia al despertar.</li>
<li><strong>TEPT:</strong> pesadillas y microdespertares fragmentados.</li>
<li><strong>Genética:</strong> mayor familiaridad en narcolepsia tipo 1.</li>
</ul>
<ol>
<li>Registrar hora, posición, duración y contenido fenomenológico del episodio.</li>
<li>Explorar somnolencia diurna, cataplejía y ronquidos.</li>
<li>Revisar medicación psicotrópica y sustancias.</li>
</ol>""",
            },
            {
                "h2": "Vínculo con ansiedad, TEPT y evaluación con PCL-5",
                "html": p(
                    "Personas con trastornos de ansiedad reportan más parálisis y las interpretan catastróficamente («voy a morir», «presencia maligna»). La psicoeducación reduce miedo y evita conductas de evitación del dormitorio. En <strong>TEPT</strong>, hiperactivación autonómica, pesadillas y sueño fragmentado aumentan probabilidad de experiencias intrusivas al límite del sueño.",
                    "Administre <a href=\"/articulos/escala-pcl-5-estres-postraumatico.html\">PCL-5</a> cuando haya trauma conocido o síntomas de reexperimentación, evitación e hiperactivación. Un PCL-5 elevado orienta tratamiento traumático (TCC, EMDR, imaginal exposure) además de higiene del sueño. Diferencie alucinaciones breves hipnagogias de psicosis: en parálisis son segundos-minutos, el paciente conserva insight posterior.",
                    "Explore también pánico nocturno y trastorno de pánico diurno. Algunos pacientes confunden parálisis con ataque cardíaco; derive a medicina si hay dolor torácico atípico persistente fuera del contexto REM.",
                ),
            },
            {
                "h2": "Evaluación clínica y cuándo derivar a medicina del sueño",
                "html": p(
                    "La evaluación psicológica incluye historia del sueño (diario 2 semanas), escalas de insomnio (ISI), somnolencia (Epworth si disponible), ansiedad (GAD-7) y depresión (PHQ-9). Derive a especialista del sueño si hay somnolencia diurna marcada, cataplejía, episodios muy frecuentes (varias veces por semana) pese a higiene, o sospecha de apnea.",
                    "Polisomnografía no se indica en episodios aislados benignos, pero sí en sospecha de narcolepsia o apnea. Explique al paciente que el objetivo es descartar condiciones tratables, no «buscar enfermedad» innecesariamente.",
                    "En embarazo o posparto, privación de sueño y ansiedad elevan reportes; adapte intervenciones. En trastorno bipolar, alteraciones de sueño pueden ser prodromo de episodio; coordine con psiquiatría.",
                ),
            },
            {
                "h2": "Manejo psicológico: psicoeducación, CBT-I y regulación",
                "html": p(
                    "Intervenciones de primera línea incluyen <strong>psicoeducación</strong> sobre mecanismo REM-atonia, normalización de frecuencia poblacional y técnicas de afrontamiento durante el episodio (enfoque en respiración, intentar mover dedos pequeños, recordar naturaleza transitoria). Evite reforzar narrativas paranormales si el paciente las usa para explicar experiencias.",
                    "La <strong>terapia cognitivo-conductual para insomnio (CBT-I)</strong> mejora higiene del sueño, horarios regulares, restricción de estímulos y manejo de cogniciones nocturnas. Para ansiedad/TEPT comórbido, integre exposición a recuerdos seguros, reentrenamiento de pesadillas (IRT) cuando aplique.",
                    "Registre intervenciones, diarios de sueño y escalas repetidas. Para continuidad entre sesiones y recordatorios de hábitos, puede apoyarse en {kalyo} documentando planes de sueño acordados.".format(
                        kalyo=KALYO
                    ),
                ),
            },
            {
                "h2": "Prevención de recurrencias y mitos frecuentes",
                "html": p(
                    "Recomiende horario de sueño regular, limitar siestas largas, reducir alcohol y cafeína vespertina, y posición lateral si la supina precipita episodios. Tratar apnea o narcolepsia reduce frecuencia de forma sustancial.",
                    "Desmitifique: no es posesión ni daño cerebral agudo; no requiere exorcismo ni intervenciones peligrosas. En culturas con alta carga de interpretación sobrenatural, respete creencias mientras ofrece modelo biológico alternativo comprensible.",
                    "Si el miedo lleva a evitar dormir solo o a uso excesivo de sedantes sin prescripción, aborde riesgo de dependencia y derive médicamente. Seguimiento a 4–8 semanas evalúa frecuencia de episodios y mejoría de ansiedad nocturna.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "¿La parálisis del sueño es peligrosa?",
                "a": "En la mayoría de casos no. Es autolimitada. El riesgo principal es ansiedad secundaria o privación de sueño por miedo a dormir. Derive si hay somnolencia diurna grave o síntomas de apnea o narcolepsia.",
            },
            {
                "q": "¿Se relaciona con lo paranormal?",
                "a": "Las experiencias pueden interpretarse culturalmente de muchas formas. Clínicamente se explica por atonia REM y estado híbrido de conciencia. Respete creencias del paciente sin dejar de ofrecer psicoeducación basada en evidencia.",
            },
            {
                "q": "¿Cuándo usar PCL-5 en parálisis del sueño?",
                "a": "Cuando hay trauma previo, pesadillas recurrentes, hiperactivación o sospecha de TEPT comórbido que mantiene sueño fragmentado y experiencias al despertar.",
            },
            {
                "q": "¿Los antidepresivos causan parálisis?",
                "a": "Algunos modifican REM y pueden aumentar reportes en personas susceptibles. No suspenda medicación sin psiquiatría; evalúe balance riesgo-beneficio y horario de dosis.",
            },
            {
                "q": "¿CBT-I ayuda aunque no haya insomnio crónico?",
                "a": "Sí, cuando hay higiene deficiente, miedo anticipatorio o horarios irregulares que precipitan episodios. Adaptar intensidad al caso.",
            },
        ],
        "howto": None,
        "related": [
            {"href": "/articulos/pass-sensibilidad-ansiedad.html", "label": "PASS: sensibilidad a la ansiedad"},
            {"href": "/articulos/escala-pcl-5-estres-postraumatico.html", "label": "PCL-5: estrés postraumático"},
            {"href": "/articulos/gad-2-tamizaje-ansiedad-breve.html", "label": "GAD-2: tamizaje de ansiedad"},
        ],
        "cta_h2": "Registra hábitos de sueño y seguimiento",
        "cta_p": "Documenta diarios de sueño, escalas y planes de higiene en un expediente clínico continuo.",
        "after_href": "/articulos/pass-sensibilidad-ansiedad.html",
        "after_loc": "https://kalyo.io/articulos/pass-sensibilidad-ansiedad.html",
        "card_title": "Parálisis del sueño: guía clínica",
        "card_p": "REM, causas, ansiedad/TEPT, PCL-5 y manejo psicológico para consulta.",
    }
)

# --- 5 tdah-adultos ---
SPECS.append(
    {
        "slug": "tdah-adultos",
        "title": "TDAH en adultos: CAARS, DIVA, TCC y guía clínica | Kalyo",
        "description": "TDAH en adultos: presentación clínica, diferencial con infancia, escalas CAARS/DIVA, TCC basada en evidencia y coordinación con psiquiatría en consulta.",
        "keywords": "TDAH adultos, CAARS, DIVA, TCC, ASRS, psicología clínica, déficit de atención, hiperactividad",
        "h1": "TDAH en adultos: diagnóstico diferencial, evaluación y tratamiento psicológico",
        "breadcrumb_short": "TDAH en adultos",
        "hero_alt": "Evaluación clínica de TDAH en adultos en consulta psicológica",
        "inline_alt": "Perfil de inatención e impulsividad en TDAH adulto",
        "intro": "El TDAH en adultos persiste en muchos casos con inatención, impulsividad emocional y desorganización más que hiperactividad motora externa. El DSM-5 exige síntomas antes de los 12 años y deterioro en al menos dos contextos. Use DIVA, CAARS o ASRS, TCC adaptada y coordinación con psiquiatría cuando haya indicación farmacológica.",
        "sections": [
            {
                "h2": "Presentación clínica del TDAH en la edad adulta",
                "html": p(
                    "Los adultos consultan por procrastinación crónica, olvidos laborales, dificultad para completar proyectos, impulsividad en compras o conversaciones, inquietud interna, baja tolerancia a la frustración y desregulación emocional. A menudo hubo diagnóstico tardío tras fracaso académico repetido, cambios de carrera o conflictos de pareja atribuidos a «pereza».",
                    "La hiperactividad puede manifestarse como hablar en exceso, interrumpir, sensación de motor encendido o necesidad de estimulación constante. En mujeres, perfil inatento con compensación y mayor comorbilidad ansiosa/depressiva es frecuente, lo que retrasa identificación.",
                    "Explore impacto funcional en trabajo (evaluaciones, plazos), hogar (facturas, citas), conducción (multas, distracción) y relaciones. Documente ejemplos concretos de los últimos seis meses y retrospectiva infantil con informantes si es posible.",
                ),
            },
            {
                "h2": "Diferencias respecto al TDAH infantil y criterios DSM-5",
                "html": p(
                    "El DSM-5 mantiene dos dominios (inatención e hiperactividad-impulsividad) con umbral de cinco síntomas en adultos (vs seis en menores). Requiere presencia antes de los 12 años, varios síntomas en dos o más entornos y deterioro claro. Síntomas no se explican mejor por otro trastorno mental.",
                    "En adultos, los síntomas hiperactivos suelen atenuarse mientras persisten olvidos, desorganización y impulsividad. El requisito de inicio infantil implica recoger historias escolares, informes antiguos o entrevistas a padres cuando estén disponibles; en ausencia, use entrevistas retrospectivas validadas con cautela.",
                )
                + """
<ul>
<li><strong>Inatención adulta:</strong> errores por descuido, evitar tareas sostenidas, distractibilidad.</li>
<li><strong>Impulsividad:</strong> interrupciones, decisiones apresuradas, baja tolerancia al aburrimiento.</li>
<li><strong>Funcionamiento:</strong> al menos dos áreas (trabajo, hogar, relaciones, estudios).</li>
</ul>""",
            },
            {
                "h2": "Evaluación con CAARS, DIVA y ASRS",
                "html": p(
                    "El <a href=\"/articulos/asrs-tdah-adultos.html\">ASRS v1.1</a> es cribado rápido OMS ampliamente usado. CAARS aporta perfiles de inatención, hiperactividad-impulsividad e índices de inconsistencia/impression management en algunas versiones. La entrevista <strong>DIVA</strong> (Diagnostic Interview for ADHD in Adults) sistematiza criterios DSM en infancia y adultez con ejemplos por área de vida.",
                    "Combine autorreporte con colateral (pareja, familiar) cuando haya consentimiento. Evalúe comorbilidades: trastornos de ansiedad, depresión, trastorno bipolar II, consumo de sustancias, TLP, apnea del sueño. PHQ-9, GAD-7 y cribado de bipolaridad (MDQ) ayudan. Neuropsicología puede clarificar perfil atencional cuando hay duda diagnóstica o solicitud laboral.",
                )
                + """
<table class="items-table">
<thead><tr><th>Herramienta</th><th>Tipo</th><th>Nota</th></tr></thead>
<tbody>
<tr><td>ASRS v1.1</td><td>Cribado breve</td><td>Orienta necesidad de evaluación completa</td></tr>
<tr><td>CAARS</td><td>Cuestionario amplio</td><td>Perfil dimensional adulto</td></tr>
<tr><td>DIVA-5</td><td>Entrevista estructurada</td><td>Criterios DSM infancia + adultez</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "Diagnóstico diferencial en consulta psicológica",
                "html": p(
                    "Diferencie TDAH de trastornos de ansiedad (preocupación interfiere atención), depresión (lentitud cognitiva), hipotiroidismo, apnea del sueño (somnolencia diurna), secuelas de conmoción, trastorno bipolar (síntomas episódicos) y estrés crónico laboral. El TDAH suele mostrar trayectoria longitudinal desde infancia con patrones estables de desorganización.",
                    "Sustancias (cannabis crónico, estimulantes) confunden el cuadro. En adultos mayores, descarte deterioro cognitivo incipiente. Documente respuesta previa a estimulantes si las usó sin prescripción: mejora no confirma diagnóstico pero es dato relevante para psiquiatría.",
                ),
            },
            {
                "h2": "Terapia cognitivo-conductual adaptada al TDAH adulto",
                "html": p(
                    "La <strong>TCC para TDAH adulto</strong> incluye psicoeducación, entrenamiento en organización (agendas, recordatorios, desglose de tareas), manejo del tiempo, regulación emocional e intervención sobre creencias («debería poder solo»). Sesiones estructuradas con agenda escrita, tareas breves y seguimiento de implementación mejoran adherencia.",
                    "Integre mindfulness adaptado cuando ayude a pausar impulsos. Trabaje entornos: reducir distractores, acuerdos con pareja sobre responsabilidades. Si hay comorbilidad depresiva o ansiosa, trate en paralelo con protocolos específicos.",
                    "Centralice objetivos por sesión, resultados CAARS/ASRS y acuerdos con psiquiatría en {kalyo} para continuidad cuando coexiste farmacoterapia.".format(
                        kalyo=KALYO
                    ),
                ),
            },
            {
                "h2": "Coordinación con psiquiatría y ajustes funcionales",
                "html": p(
                    "Estimulantes y atomoxetina son decisión médica; el psicólogo monitoriza adherencia, efectos en sueño/ansiedad y combina con habilidades conductuales. No todos los adultos requieren fármacos; algunos prefieren solo psicoterapia y adaptaciones laborales.",
                    "Oriente sobre derechos laborales razonables cuando corresponda (documentación clínica sobria, ajustes de plazos o entorno). Evite prometer mejoras cognitivas milagrosas; enfoque en funcionamiento y autocompasión.",
                    "Seguimiento trimestral inicial evalúa metas SMART, efectos secundarios y necesidad de reevaluación neuropsicológica. Recaídas organizacionales son normales; trátelas como datos, no fracaso moral.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "¿ASRS positivo diagnostica TDAH en adultos?",
                "a": "No. Es cribado. Se requiere entrevista clínica, evidencia de inicio infantil, deterioro en múltiples áreas y diagnóstico diferencial amplio.",
            },
            {
                "q": "¿DIVA sustituye la evaluación neuropsicológica?",
                "a": "No. DIVA cubre criterios diagnósticos; la neuropsicología aporta perfil cognitivo detallado cuando hay indicación clínica o forense/laboral.",
            },
            {
                "q": "¿TDAH adulto se trata solo con medicación?",
                "a": "La evidencia favorece combinación de psicoeducación, TCC y, cuando hay indicación, farmacoterapia. Muchos pacientes benefician de habilidades conductuales aun con medicación.",
            },
            {
                "q": "¿Puede aparecer TDAH de novo en adultez?",
                "a": "El DSM-5 requiere síntomas antes de los 12 años. Diagnósticos «nuevos» en adultos suelen ser reconocimiento tardío, no aparición genuina sin historia previa.",
            },
            {
                "q": "¿CAARS detecta simulación?",
                "a": "Algunas versiones incluyen índices de validez; interprete con cautela en contextos legales o laborales. Combine con entrevista y colaterales.",
            },
        ],
        "howto": {
            "name": "Cómo evaluar TDAH en adultos en consulta",
            "steps": [
                {"name": "Cribado", "text": "Aplique ASRS y explore quejas funcionales en trabajo, hogar y relaciones."},
                {"name": "Historia infantil", "text": "Documente síntomas antes de los 12 años con DIVA o entrevista equivalente."},
                {"name": "Comorbilidades", "text": "Administre PHQ-9, GAD-7 y evalúe bipolaridad, sustancias y sueño."},
                {"name": "Formulación", "text": "Integre CAARS/DIVA, colaterales y juicio clínico DSM-5."},
                {"name": "Plan", "text": "Acuerde TCC, adaptaciones y derivación psiquiátrica si hay indicación de fármacos."},
            ],
        },
        "related": [
            {"href": "/articulos/asrs-tdah-adultos.html", "label": "ASRS: TDAH en adultos"},
            {"href": "/articulos/conners-3-tdah-ninos.html", "label": "Conners 3: TDAH infantil"},
            {"href": "/articulos/wurs-tdah-infancia-adultos.html", "label": "WURS: retrospectiva infantil"},
        ],
        "cta_h2": "Evalúa TDAH adulto con expediente ordenado",
        "cta_p": "Guarda ASRS, CAARS, objetivos de TCC y notas de coordinación médica en un solo lugar.",
        "after_href": "/articulos/srq-20-salud-mental-autorreportado.html",
        "after_loc": "https://kalyo.io/articulos/srq-20-salud-mental-autorreportado.html",
        "card_title": "TDAH en adultos: evaluación y TCC",
        "card_p": "CAARS, DIVA, diferencial clínico y terapia cognitivo-conductual adaptada.",
    }
)

# --- 6 esquizofrenia-que-es ---
SPECS.append(
    {
        "slug": "esquizofrenia-que-es",
        "title": "Esquizofrenia qué es: síntomas, DSM-5 y rol clínico | Kalyo",
        "description": "Esquizofrenia qué es: síntomas positivos y negativos, criterios DSM-5, escalas PANSS/BPRS y rol del psicólogo en equipo interdisciplinario de salud mental.",
        "keywords": "esquizofrenia qué es, síntomas positivos, síntomas negativos, DSM-5, PANSS, BPRS, psicología clínica",
        "h1": "Esquizofrenia qué es: síntomas, diagnóstico DSM-5 y rol del psicólogo",
        "breadcrumb_short": "Esquizofrenia qué es",
        "hero_alt": "Atención psicológica en esquizofrenia dentro de equipo de salud mental",
        "inline_alt": "Esquema de síntomas positivos y negativos en esquizofrenia",
        "intro": "La esquizofrenia es un trastorno psicótico crónico con psicosis, deterioro funcional y a menudo síntomas negativos y cognitivos persistentes. El DSM-5 requiere dos síntomas característicos durante un mes y curso total de seis meses. El psicólogo clínico aplica PANSS o BPRS, psicoeducación sistemática y rehabilitación psicosocial junto a antipsicóticos prescritos.",
        "sections": [
            {
                "h2": "Esquizofrenia qué es: definición DSM-5",
                "html": p(
                    "La <strong>esquizofrenia</strong> se diagnostica cuando hay dos o más síntomas característicos (delirios, alucinaciones, discurso desorganizado, conducta catatónica o desorganizada, síntomas negativos) durante al menos un mes, con al menos uno de los tres primeros si solo hay dos. Debe existir deterioro funcional en trabajo, relaciones o autocuidado y signos continuos durante seis meses incluyendo fases prodrómicas o residuales.",
                    "Excluya trastornos del estado de ánimo con psicosis, efectos directos de sustancias o condición médica. Especifique si hay catatonía comórbida. En Latinoamérica, retrasos en tratamiento y estigma complican curso; el acceso a antipsicóticos y rehabilitación es variable.",
                    "El psicólogo no establece solo el diagnóstico de esquizofrenia sin valoración psiquiátrica en la mayoría de protocolos; colabora en descripción fenomenológica, impacto funcional y plan psicosocial.",
                ),
            },
            {
                "h2": "Síntomas positivos, negativos y cognitivos",
                "html": p(
                    "<strong>Síntomas positivos</strong> (exceso psicótico): delirios (persecutorios, referenciales, grandiosos), alucinaciones (auditivas más frecuentes), discurso tangencial o incoherente, agitación o catatonía. <strong>Síntomas negativos</strong>: afecto plano, alogia, anhedonia, avolición, retraimiento social. <strong>Déficits cognitivos</strong> en atención, memoria de trabajo y funciones ejecutivas persisten entre episodios y predicen funcionamiento.",
                    "La distinción tipo I / II clásica (positivos vs negativos predominantes) es heurística; hoy se enfatiza espectro y fases. En primera psicosis, intervención precoz mejora pronóstico; el psicólogo apoya engagement terapéutico y adherencia.",
                )
                + """
<table class="items-table">
<thead><tr><th>Dimensión</th><th>Ejemplos</th><th>Implicación clínica</th></tr></thead>
<tbody>
<tr><td>Positivos</td><td>Delirios, alucinaciones, desorganización</td><td>Objetivo de antipsicóticos y TCCp</td></tr>
<tr><td>Negativos</td><td>Aplanamiento, aislamiento, apatía</td><td>Rehabilitación psicosocial, ACT</td></tr>
<tr><td>Cognitivos</td><td>Atención, memoria de trabajo</td><td>Adaptaciones, entrenamiento cognitivo</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "Evaluación con PANSS, BPRS y entrevista psicopatológica",
                "html": p(
                    "La <strong>PANSS</strong> (Positive and Negative Syndrome Scale) cuantifica siete positivos, siete negativos y siete psicopatología general; requiere entrenamiento. La <strong>BPRS</strong> es más breve para seguimiento en hospital o ambulatorio intensivo. Ambas apoyan monitorizar respuesta a tratamiento, no reemplazan entrevista clínica.",
                    "Explore inicio (insidioso vs agudo), consumo de cannabis o estimulantes, antecedentes familiares, estresores vitales y adherencia previa. Evalúe riesgo suicida (elevado en esquizofrenia, especialmente jóvenes y posdescompensación). Use escalas de funcionamiento (GAF/ WHODAS) cuando sea posible.",
                ),
            },
            {
                "h2": "Diagnóstico diferencial y trastorno esquizoafectivo",
                "html": p(
                    "Diferencie esquizofrenia de trastorno esquizoafectivo (episodios afectivos mayores concurrentes con psicosis), trastorno bipolar con psicosis, TEPT con síntomas disociativos/psicóticos breves, psicosis inducida por sustancias y psicosis del espectro del humor.",
                    "En jóvenes, psicosis bref psicótico o trastorno psicótico no especificado pueden ser diagnósticos temporales. Documente curso a 6–12 meses antes de etiqueta definitiva cuando el cuadro es incipiente.",
                )
                + """
<ul>
<li><strong>Esquizoafectivo:</strong> episodios maniacos/depresivos mayores con psicosis superpuesta.</li>
<li><strong>Bipolar I:</strong> psicosis típicamente durante manía grave.</li>
<li><strong>TEPT:</strong> flashbacks con insight variable; no curso crónico psicótico típico.</li>
</ul>""",
            },
            {
                "h2": "Rol del psicólogo: psicoeducación, TCC para psicosis y rehabilitación",
                "html": p(
                    "La farmacoterapia antipsicótica es primera línea médica; el psicólogo aporta <strong>psicoeducación</strong> (naturaleza de síntomas, medicación, señales de recaída), <strong>TCC para psicosis (TCCp)</strong> en delirios/alucinaciones no agudamente peligrosos, entrenamiento en habilidades sociales, manejo de estrés y apoyo a familiares.",
                    "Modelos de assertive community treatment (ACT) integran equipo multidisciplinario para personas con recaídas frecuentes. Trabaje metas realistas de autonomía, vivienda y empleo apoyado. Evite confrontar delirios de forma invalidante; use técnicas de evaluación de evidencias y distancia cognitiva.",
                    "Registre PANSS/BPRS serial, planes de crisis y contactos psiquiátricos en {kalyo} para continuidad cuando hay múltiples hospitalizaciones.".format(
                        kalyo=KALYO
                    ),
                ),
            },
            {
                "h2": "Familia, estigma y prevención de recaídas",
                "html": p(
                    "Programas de intervención familiar reducen recaídas al mejorar comunicación y reducir crítica alta emocionalmente expresada. Capacite en señales tempranas (sueño, aislamiento, suspicacia creciente) y plan con psiquiatría.",
                    "Combata estigma interno y externo; promueva recuperación orientada a metas personales, no solo ausencia de síntomas positivos. Coordine con trabajo social y rehabilitación vocacional cuando existan.",
                    "Supervisión clínica ayuda al psicólogo a manejar contratransferencia ante agresividad, desconfianza o anosognosia. Derive urgente ante agresión, descompensación aguda o abandono abrupto de medicación con riesgo.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "¿PANSS diagnostica esquizofrenia?",
                "a": "No. Cuantifica severidad de síntomas. El diagnóstico es clínico integrando historia, curso de seis meses y exclusión de otras causas, usualmente con psiquiatría.",
            },
            {
                "q": "¿El psicólogo puede hacer terapia sin antipsicóticos?",
                "a": "En psicosis aguda activa, la estabilización médica es prioritaria. La psicoterapia estructurada suele iniciar o intensificarse cuando hay cierta estabilidad y alianza.",
            },
            {
                "q": "¿Qué son síntomas negativos?",
                "a": "Disminución de funciones normales: afecto restringido, pobre habla espontánea, falta de motivación, anhedonia y retraimiento social. Impactan pronóstico funcional.",
            },
            {
                "q": "¿Cannabis causa esquizofrenia?",
                "a": "Aumenta riesgo en personas vulnerables y puede precipitar psicosis. No explica todos los casos; integre historia de consumo en evaluación.",
            },
            {
                "q": "¿BPRS o PANSS para seguimiento ambulatorio?",
                "a": "BPRS es más breve; PANSS más detallada. Elija según setting y entrenamiento; lo crucial es aplicación consistente en el tiempo.",
            },
        ],
        "howto": {
            "name": "Cómo apoyar psicológicamente a una persona con esquizofrenia",
            "steps": [
                {"name": "Evaluación inicial", "text": "Describa síntomas positivos/negativos, riesgo y funcionamiento con PANSS/BPRS si hay formación."},
                {"name": "Coordinación psiquiátrica", "text": "Acuerde roles, adherencia farmacológica y señales de recaída con médico tratante."},
                {"name": "Psicoeducación", "text": "Explique enfermedad, medicación y plan de crisis a paciente y familia."},
                {"name": "Intervención psicosocial", "text": "Implemente TCCp, habilidades sociales o apoyo cognitivo según fase y gravedad."},
                {"name": "Seguimiento", "text": "Monitoree escalas, metas funcionales y ajuste intensidad de apoyo."},
            ],
        },
        "related": [
            {"href": "/articulos/epq-r-cuestionario-eysenck.html", "label": "EPQ-R: personalidad y psicosis"},
            {"href": "/articulos/mini-entrevista-diagnostica-estructurada.html", "label": "MINI: entrevista diagnóstica"},
            {"href": "/articulos/whodas-discapacidad-funcionamiento.html", "label": "WHODAS: funcionamiento y discapacidad"},
        ],
        "cta_h2": "Coordina el seguimiento en psicosis",
        "cta_p": "Documenta PANSS/BPRS, psicoeducación y planes de crisis en un expediente clínico compartido.",
        "after_href": "/articulos/epq-r-cuestionario-eysenck.html",
        "after_loc": "https://kalyo.io/articulos/epq-r-cuestionario-eysenck.html",
        "card_title": "Esquizofrenia qué es: guía DSM-5",
        "card_p": "Síntomas positivos/negativos, PANSS/BPRS y rol del psicólogo en equipo.",
    }
)

_EXTRA_DEPTH: dict[str, list[str]] = {
    "anorexia-que-es": [
        "En la anamnesis, diferencie restricción intencional de apetito bajo por depresión o dolor abdominal orgánico. Pregunte por uso de aplicaciones calóricas, ayunos intermitentes extremos y comparación social en redes. Registre conductas de comprobación corporal y evitación de eventos con comida.",
        "El duelo del diagnóstico en familias puede incluir culpa materna infundada; psicoeducar sobre modelos biopsicosociales reduce conflicto. Acuerde reglas de comunicación en la mesa: temas neutrales, supervisión sin coerción humillante, y pausas cuando la tensión escala.",
        "Al interpretar EAT-26, considere sesgo de deseabilidad social: algunas personas ocultan síntomas. Combine con entrevista motivacional para aumentar honestidad. Repita la escala cada cuatro a ocho semanas para graficar tendencia, no solo un puntaje aislado.",
        "En pacientes con trauma, explore si la restricción regula emociones o reproduce control en contextos de abuso. No asuma causalidad única; la formulación transdiagnóstica guía si priorizar estabilización traumática antes de exposición alimentaria intensa.",
        "La reintroducción de grupos alimentarios prohibidos en CBT-E debe ser gradual, con registro de ansiedad anticipatoria y experimentos conductuales. El terapeuta modela flexibilidad y normaliza saciedad. Evite comentarios sobre «elecciones saludables» que refuercen reglas rígidas.",
        "Al alta, planifique controles espaciados, señales de recaída (aumento de ejercicio, aislamiento, pesaje compulsivo) y contacto con nutrición. Documente acuerdos con escuela o trabajo sobre adaptaciones temporales y criterios para reevaluación médica urgente.",
    ],
    "tlp-trastorno-limite": [
        "En la primera entrevista, valide el sufrimiento sin reforzar conductas de crisis como único medio de obtener alivio. Establezca expectativas realistas sobre ritmo de cambio y límites de contacto fuera de sesión, salvo protocolo DBT explícito con coaching acordado.",
        "Al mapear criterio 1 (abandono), explore historias de separaciones reales, migración, pérdidas y invalidación crónica. Diferencie sensibilidad borderline de dependencia psicótica. Registre disparadores interpersonales recurrentes (mensajes no respondidos, cambios de planes).",
        "Para criterio 5 (autolesión), documente método, frecuencia, función afectiva (regulación vs autopunitiva) y acceso a medios. Acuerde plan alternativo de habilidades antes de próximo impulso. Coordinación con psiquiatría si hay riesgo de lesión grave.",
        "En DBT, el diario de cartas (chain analysis) después de episodios críticos convierte crisis en aprendizaje. Revise vulnerabilidades biológicas (sueño, hambre, dolor) que bajan umbral de desregulación. Refuerce práctica diaria de mindfulness aunque sea breve.",
        "La transferencia y contratransferencia pueden intensificarse; busque supervisión cuando sienta desesperanza o enojo. Evite spliting del equipo: comunicación clínica unificada entre profesionales reduce reforzamiento de polarización del paciente.",
        "Al planificar alta o reducción de frecuencia, acuerde señales tempranas de recaída, contactos de crisis y refuerzo de habilidades de efectividad interpersonal en vínculos actuales. Mantenga puerta abierta para reingreso breve sin castigo.",
    ],
    "paralisis-del-sueno": [
        "Pregunte si el paciente duerme boca arriba; sugerir dormir de lado puede ser intervención simple. Explore siestas largas que reducen presión homeostática de sueño nocturno y aumentan probabilidad de entrar en REM con deuda parcial.",
        "Si hay historial de abuso sexual nocturno o violencia, las alucinaciones hipnagogias pueden reactivar hipervigilia; integre PCL-5 y plan traumático antes de insistir solo en higiene del sueño. Respete ritmo del paciente para no retraumatizar.",
        "En estudiantes con exámenes, la privación voluntaria de sueño precipita episodios; enseñe planificación de estudio con bloques de sueño protegidos. Normalice que la parálisis no indica locura ni daño cerebral permanente.",
        "Cuando derive a medicina del sueño, prepare al paciente sobre polisomnografía (expectativas, sensores, primera noche posible efecto «primera noche»). Eso reduce ansiedad anticipatoria y abandono de estudios diagnósticos.",
        "Para ansiedad nocturna, practique en sesión reestructuración de pensamientos catastróficos («no podré respirar») con evidencia de resolución espontánea. Entrene respiración diafragmática en vigilia para usar durante atonia.",
        "Seguimiento a ocho semanas: compare frecuencia de episodios, calidad subjetiva del sueño (ISI) y evitación del dormitorio. Si persiste TEPT activo, priorice tratamiento traumático paralelo.",
    ],
    "tdah-adultos": [
        "Solicite informes escolares antiguos o entreviste a padres cuando haya consentimiento; busque comentarios de maestros sobre dispersión, olvidos de tareas e impulsividad en recreo. En ausencia de colaterales, use entrevista DIVA con ejemplos concretos por década.",
        "Explore gender bias: mujeres con TDAH adulto a menudo recibieron diagnósticos de ansiedad o depresión primero. Pregunte por compensación mediante listas rígidas, perfeccionismo y agotamiento cuando la estructura externa desaparece (teletrabajo).",
        "En evaluación laboral, aclare si el referido proviene de RR.HH. por bajo desempeño; mantenga rol clínico, no disciplinario. Documente fortalezas (creatividad, hiperfoco en intereses) junto a áreas de ajuste razonable.",
        "La TCC debe incluir recordatorios externos (alarmas, ubicación fija de llaves), descomposición de proyectos en pasos de quince minutos, y revisión semanal de «buckets» de tareas. Celebre finalización parcial para contrarrestar sesgo de autosabotaje.",
        "Si hay comorbilidad sustancias (cafeína excesiva, cannabis para dormir, alcohol para frenar mente), aborde en mismo plan. Estimulantes prescritos requieren monitoreo de sueño y presión arterial en coordinación con psiquiatría.",
        "Reevalúe diagnóstico si no hay respuesta a intervenciones tras seis meses: podría haber apnea, hipotiroidismo, trastorno bipolar o estrés laboral tóxico sin TDAH primario. Mantenga humildad diagnóstica y comunicación transparente con el paciente.",
    ],
    "esquizofrenia-que-es": [
        "En primera entrevista psicológica, priorice contención y alianza; no confronte delirios centrales de inmediato. Explore impacto funcional: higiene, alimentación, aislamiento, uso de sustancias y adherencia a antipsicóticos según relato del paciente y familia.",
        "Al puntuar PANSS, aplique entrevista en momentos comparables (misma hora, sin cambios recientes de dosis) para series longitudinalmente válidas. Registre efectos extrapiramidales o sedación que confundan síntomas negativos con efectos iatrogénicos.",
        "La psicoeducación familiar debe incluir diferencia entre síntomas positivos agudos y rasgos de personalidad premórbidos. Enseñe comunicación breve, baja emoción expresada excesiva y resolución de problemas prácticos (pagos, citas).",
        "TCC para psicosis adaptada trabaja con distancia metacognitiva: «tengo la experiencia de escuchar voces» vs «soy las voces». Evite debates lógicos sobre veracidad del delirio; explore consecuencias conductuales y seguridad.",
        "Rehabilitación psicosocial incluye entrenamiento en habilidades de vida diaria, manejo de dinero con apoyos graduados y reinserción laboral en entornos protegidos. Metas pequeñas sostenidas superan planes ambiciosos que fracasan y confirman desesperanza.",
        "Ante recaída, active plan escrito con psiquiatría: ajuste de dosis, hospitalización día o ingreso breve. El psicólogo documenta cambios en PANSS/BPRS, factores estresores y adherencia. Post-alta, intensifique visitas domiciliarias o ACT si el servicio existe.",
    ],
}

_EXTRA_DEPTH_B: dict[str, list[str]] = {
    "anorexia-que-es": [
        "Considere impacto cultural de ideal de delgadez en medios y deportes de apariencia. Explore comentarios de entrenadores o redes que refuercen restricción. Derive a endocrinología si hay amenorrea prolongada, osteoporosis o bradicardia en adolescentes.",
        "Trabaje con familia acuerdos sobre baño y espejos en fases agudas si aumentan comprobación. Algunos protocolos limitan pesajes en casa; decida con equipo médico. Documente consentimientos informados para intervenciones familiares.",
        "Si hay comorbilidad TOC, diferencie rituales alimentarios de restricción anorexígena primaria. La jerarquía terapéutica puede requerir tratar TOC concurrentemente para permitir flexibilidad alimentaria.",
        "En hombres y personas no binarias, la anorexia puede pasar desapercibida; pregunte por musculatura y «cutting» en gimnasio. Ajuste lenguaje clínico inclusivo y evite supuestos de género en evaluación de imagen corporal.",
        "Prepare devolución diagnóstica sin alarmismo pero con claridad sobre riesgo médico. Ofrezca hoja de recursos de crisis y horarios de nutrición. Programe siguiente cita antes de salir para reducir abandono.",
        "En seguimiento a largo plazo, vigile transición a bulimia o atracones durante restitución ponderal; reevalúe diagnóstico si cambia fenomenología. Mantenga vínculo terapéutico aun con recaídas parciales.",
    ],
    "tlp-trastorno-limite": [
        "Documente acuerdos sobre confidencialidad y límites cuando hay riesgo suicida; explique excepciones legales de forma comprensible. Involucre a familia solo con consentimiento y enfoque en apoyo, no en culpa.",
        "Explore consumo de alcohol o sustancias como regulador emocional; deriva a adicciones si interfiere DBT. Registre patrones de idealización/devaluación con parejas actuales y historial de relaciones violentas.",
        "En sesión, use validación antes de soluciones. Microinterrupciones empáticas evitan escalada. Practique role-play de conversaciones difíciles cuando el paciente lo solicite.",
        "Para criterio 9 (paranoia/disociación), diferencie experiencias breves bajo estrés de psicosis primaria. Si persisten fuera de estrés, reevalúe espectro psicótico con psiquiatría.",
        "Mida progreso con ZAN-BPD serial, no solo impresión clínica global. Celebre reducción de autolesiones aunque persistan pensamientos; refuerce habilidades usadas.",
        "Ante hospitalizaciones repetidas, revise si el entorno post-alta carece de apoyos. Conecte con recursos comunitarios, grupos DBT locales o telepsicología estructurada cuando haya acceso.",
    ],
    "paralisis-del-sueno": [
        "Registre consumo de suplementos melatonina o cannabis para dormir; ambos pueden alterar arquitectura REM. Eduque sobre riesgos de automedicación crónica sin evaluación médica.",
        "Si el paciente teme dormir, aplique exposición gradual al dormitorio con jerarquía de miedos. Combine con técnicas de relajación aplicadas en vigilia antes de intentar exposición nocturna.",
        "En parejas, explique naturaleza benigna a la pareja para evitar respuestas alarmistas que aumenten miedo del paciente. Acuerden señal discreta de apoyo si ocurre episodio.",
        "Evalúe horarios de trabajo a turnos; trabajadores nocturnos tienen mayor desincronización circadiana. Cuando sea posible, estabilice horarios antes de intervenciones psicológicas profundas.",
        "Contraste parálisis aislada con narcolepsia: somnolencia irresistible diurna y cataplejía son banderas rojas. No retrase derivación si hay dudas.",
        "Cierra cada consulta con plan escrito de sueño: hora de levantarse fija, límite de cafeína, rutina de desconexión digital, y qué hacer si ocurre parálisis (anclaje respiratorio, mover dedos).",
    ],
    "tdah-adultos": [
        "Use entrevista DIVA o equivalente para anclar cada criterio DSM a ejemplos de infancia y adultez. Evite diagnóstico solo por cuestionarios sin historia longitudinal coherente.",
        "Explore impacto en pareja: olvidos de compromisos, impulsividad financiera, dificultad para escuchar. Ofrezca sesión conjunta breve si ambos consienten, con foco en acuerdos prácticos.",
        "Para estudiantes universitarios, coordine con servicios de discapacidad cuando haya diagnóstico confirmado; documentación clínica sobria facilita adaptaciones de tiempo en exámenes.",
        "Entrene uso de temporizadores Pomodo adaptados, no rígidos; permita flexibilidad para evitar abandono del método. Revise barreras ejecutivas reales en cada sesión.",
        "Si hay trauma infantil, no confunda desatención por disociación o hipervigilia con TDAH primario. Formule hipótesis múltiples y trate comorbilidades en paralelo.",
        "Planifique seguimiento: muchos adultos requieren mantenimiento de habilidades meses o años, no solo diez sesiones. Ajuste frecuencia según demandas vitales (maternidad, nuevo empleo).",
    ],
    "esquizofrenia-que-es": [
        "Revise efectos adversos de antipsicóticos (ganancia de peso, sedación, akathisia) que el paciente atribuye a «empeoramiento»; coordine ajuste con psiquiatría y psicoeducación sobre efectos esperables.",
        "Explore tabaquismo y sedentarismo, frecuentes en esquizofrenia; aborde como metas de salud física integradas, no moralismo. Vincule con medicina general cuando haya acceso.",
        "En jóvenes en primer episodio, enfatice mensaje de recuperación funcional. Evite pronósticos catastróficos que se autocumplen. Involucre a familia con permiso del paciente.",
        "Use BPRS en settings con poco tiempo; reserve PANSS para evaluaciones formales o investigación clínica. Interprete cambios mínimamente clínicamente significativos en contexto.",
        "Ante agresividad, evalúe comando de voces, paranoia persecutoria y acceso a armas. Priorice seguridad y plan con equipo; no trabaje solos situaciones de alto riesgo.",
        "Documente metas de rehabilitación concretas: asistir a centro de día, curso vocacional, voluntariado gradual. Revisión trimestral de funcionamiento con WHODAS o equivalente cuando esté disponible.",
    ],
}

for _spec in SPECS:
    _extras = _EXTRA_DEPTH.get(_spec["slug"])
    if not _extras:
        continue
    for _sec, _para in zip(_spec["sections"], _extras):
        _sec["html"] += p(_para)

for _spec in SPECS:
    _extras_b = _EXTRA_DEPTH_B.get(_spec["slug"])
    if not _extras_b:
        continue
    for _sec, _para in zip(_spec["sections"], _extras_b):
        _sec["html"] += p(_para)

_FINAL_TAIL: dict[str, str] = {
    "paralisis-del-sueno": (
        "En población migrante o con trabajo a turnos rotativos, la parálisis del sueño puede aumentar por desajuste circadiano; "
        "combine psicoeducación sobre luz matutina, horarios regulares y evaluación médica si la somnolencia diurna compromete seguridad laboral. "
        "Registre cada episodio en diario breve para detectar patrones estacionales o ligados a estrés académico."
    ),
    "tdah-adultos": (
        "La psicoeducación sobre TDAH adulto reduce autoestigma y explica bases neurobiológicas de la desatención ejecutiva, favoreciendo adherencia a estrategias externas. "
        "Revise en cada sesión qué herramientas digitales usa el paciente (apps, calendarios compartidos) y elimine fricción innecesaria: menos apps, más rutinas repetibles. "
        "Si el paciente es padre o madre con TDAH, adapte metas a carga de cuidado: microtareas y apoyo comunitario pueden ser más realistas que planes de productividad estándar. "
        "Documente respuesta a ajustes laborales o académicos solicitados y reevalúe necesidad de informes periódicos para empleador o universidad. "
        "Incluya entrenamiento en tolerancia al aburrimiento y manejo de impulsos emocionales en conflictos interpersonales, con role-play breve cuando la alianza lo permita. "
        "Repita CAARS o ASRS cada tres meses si busca objetivar cambio; discuta resultados con el paciente para ajustar metas, no solo para facturación o informes externos. "
        "Si hay comorbilidad ansiosa, enseñe a distinguir preocupación rumiativa de olvidos por inatención para no sobrediagnosticar múltiples trastornos sin jerarquía clínica clara en consulta ambulatoria segura y ética."
    ),
    "esquizofrenia-que-es": (
        "La estigmatización internalizada puede manifestarse como baja expectativa de recuperación; aborde con narrativas de personas que logran metas significativas con tratamiento continuado. "
        "Coordine con trabajador social acceso a prestaciones, vivienda tutelada o programas de empleo apoyado cuando existan en su región. "
        "El psicólogo debe mantener comunicación regular con psiquiatría sobre adherencia, efectos adversos y señales de descompensación, "
        "sin cruzar límites profesionales ni modificar medicación. En supervisiones de equipo, revise casos complejos de anosognosia y abandono de tratamiento. "
        "Ofrezca intervenciones breves sobre sueño y rutina diaria, porque la desorganización circadiana empeora síntomas positivos y negativos. "
        "Cuando el paciente permita contacto familiar, practique psicoeducación sobre no discutir delirios en calor del momento y sobre reforzar adherencia con apoyo práctico, no con crítica. "
        "Registre en informes descriptivos conductas observables antes que etiquetas peyorativas, y vincule recomendaciones a metas de autonomía que el propio paciente considere valiosas. "
        "En primera línea comunitaria, el psicólogo puede ser el profesional de mayor continuidad relacional; use ese vínculo para sostener adherencia y detectar recaídas tempranas con escalas seriadas y comunicación coordinada, informada, ética y documentada con la familia cuando haya consentimiento."
    ),
}

for _spec in SPECS:
    _tail = _FINAL_TAIL.get(_spec["slug"])
    if _tail:
        _spec["sections"][-1]["html"] += p(_tail)


if __name__ == "__main__":
    for s in SPECS:
        validate(s)
    out = Path(__file__).parent / "specs"
    out.mkdir(exist_ok=True)
    for s in SPECS:
        (out / f"{s['slug']}.json").write_text(
            json.dumps(s, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print("OK", s["slug"], len(s["title"]), len(s["description"]))
    print("done", len(SPECS))

