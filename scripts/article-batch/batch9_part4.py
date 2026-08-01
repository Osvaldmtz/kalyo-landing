#!/usr/bin/env python3
"""Batch 9 part 4 clinical SEO article specs (articles 36-40)."""
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
    min_words = 2000 if slug == "tests-psicologicos-hub" else 1250
    if bw < min_words:
        raise ValueError(f"{slug} body words {bw} < {min_words}")
    if kalyo_count(spec) != 1:
        raise ValueError(f"{slug} kalyo links {kalyo_count(spec)}")
    if len(spec["sections"]) != 6:
        raise ValueError(f"{slug} sections {len(spec['sections'])}")
    if len(spec["faqs"]) != 5:
        raise ValueError(f"{slug} faqs {len(spec['faqs'])}")


ARTICLES: list[dict] = []

# --- Article 36: test-personalidad-tipos-clinica ---
ARTICLES.append(
{
    "slug": "test-personalidad-tipos-clinica",
    "title": "Test de personalidad tipos: guía clínica México | Kalyo",
    "description": "Test de personalidad tipos: NEO PI-R, PID-5, interpretación clínica y registro ético de resultados para psicólogos clínicos en consulta privada en México.",
    "keywords": "test de personalidad tipos, NEO PI-R, PID-5, MMPI, evaluación personalidad, psicología clínica México",
    "h1": "Test de personalidad tipos: modelos clínicos y uso responsable",
    "breadcrumb_short": "Test personalidad tipos",
    "hero_alt": "Psicóloga revisando resultados de test de personalidad en consulta clínica",
    "inline_alt": "Esquema de modelos de personalidad: rasgos, dimensiones y patología",
    "intro": "Los tests de personalidad tipos agrupan instrumentos que miden rasgos estables, estilos interpersonales y, en algunos casos, facetas de psicopatología dimensional. Para psicólogos en México, elegir el instrumento adecuado depende del objetivo clínico, la edad, el nivel educativo y el marco legal de confidencialidad. Esta guía orienta selección, administración e interpretación sin reducir a la persona a una etiqueta diagnóstica.",
    "sections": [
        {
            "h2": "Qué significa test de personalidad tipos en la práctica clínica",
            "html": "<p>Cuando colegas o pacientes buscan un <strong>test de personalidad tipos</strong>, suelen mezclar pruebas proyectivas, cuestionarios de rasgos y medidas de personalidad patológica del DSM-5. En la práctica contemporánea predominan modelos dimensionales: el modelo de cinco factores (Extraversión, Amabilidad, Responsabilidad, Neuroticismo, Apertura) y enfoques alineados al PID-5 para trastornos de personalidad.</p><p>El psicólogo debe clarificar si la evaluación busca orientación vocacional, psicoterapia, peritaje o screening de riesgo. Cada objetivo implica distintos instrumentos y límites de validez. Un perfil de rasgos no diagnostica trastorno de personalidad; requiere historia longitudinal, impacto funcional y entrevista clínica estructurada.</p><p>En México, muchos consultorios combinan entrevista semi-estructurada con cuestionarios autorreportados. Respete tiempos de aplicación y fatiga del evaluado; dividir la batería en dos sesiones suele mejorar calidad de respuestas y reduce invalidaciones por cansancio.</p><ul><li><a href=\"/articulos/neo-pi-r-personalidad.html\">NEO PI-R</a></li><li><a href=\"/articulos/pid-5-bf-personalidad-dsm5.html\">PID-5-BF</a></li><li><a href=\"/articulos/mmpi-2-rf-test-personalidad.html\">MMPI-2-RF</a></li></ul><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Modelos de personalidad: tipos, rasgos y dimensiones patológicas",
            "html": "<p>Históricamente se hablaba de «tipos» (introvertido/extrovertido); hoy la psicometría clínica prefiere dimensiones continuas. El NEO PI-R evalúa cinco dominios con facetas que afinan interpretación (p. ej., ansiedad vs vulnerabilidad dentro de Neuroticismo).</p><p>El PID-5-BF mide facetas maladaptativas relacionadas con criterios DSM-5 de trastornos de personalidad, útil en formulación dimensional. No reemplace entrevista SCID-II o equivalente cuando el objetivo es diagnóstico formal de trastorno de personalidad.</p><p>Evite presentar resultados como «personalidad tipo A/B» popular; use gráficos de facetas y ejemplos conductuales observables en entrevista y situaciones reales reportadas por el paciente.</p><table class=\"items-table\"><thead><tr><th>Instrumento</th><th>Tipo</th><th>Uso</th></tr></thead><tbody><tr><td><a href=\"/articulos/neo-pi-r-personalidad.html\">NEO PI-R</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/pid-5-bf-personalidad-dsm5.html\">PID-5-BF</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/tests-psicologicos-de-personalidad.html\">Tests personalidad</a></td><td>Guía clínica</td><td>Consulta</td></tr></tbody></table><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Selección del instrumento según objetivo clínico",
            "html": "<p>Para psicoterapia focalizada en regulación emocional, Neuroticismo y facetas afines orientan técnicas (TCC, ACT, DBT). En selección de personal no clínica, delimitar rol y evitar uso de tests sin permiso laboral cuando la ley lo prohíbe.</p><p>En evaluación de riesgo (violencia, autolesión), combine personalidad con escalas específicas de riesgo; ningún test de rasgos predice por sí solo conductas violentas.</p><p>Consulte <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">cómo interpretar tests psicológicos</a> antes de emitir informes externos a terceros o instituciones educativas.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Administración, sesgo y validez de respuestas",
            "html": "<p>Instruya al paciente sobre honestidad y ausencia de respuestas «correctas». Vigile deseabilidad social excesiva, respuestas aleatorias o patrones de negación defensiva según escalas de validez del instrumento cuando existan en el manual.</p><p>Adapte lenguaje sin alterar ítems estandarizados. Si el paciente tiene baja lectoescritura, considere aplicación oral registrada o instrumentos alternativos validados para su población.</p><p>Documente medicación, sueño, consumo reciente de alcohol y estado anímico el día de la prueba; factores que pueden transitoriamente elevar Neuroticismo o confusión atencional.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Integración con entrevista y formulación de caso",
            "html": "<p>La regla de oro: prueba más entrevista más observación en múltiples contextos. Contrastar perfil NEO con relatos de pareja o empleador (con consentimiento) enriquece validez ecológica.</p><p>Formule hipótesis en lenguaje accesible: «patrón de alta Responsabilidad con rigidez en facetas de orden» en lugar de jerga críptica. Vincule a plan terapéutico y metas SMART revisables.</p><p>Revise <a href=\"/articulos/que-es-la-psicologia-clinica.html\">qué es la psicología clínica</a> para enmarcar la evaluación dentro de proceso integral, no aislado de historia y contexto vital.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Documentación, informes y registro clínico",
            "html": "<p>El informe debe incluir instrumentos aplicados, fechas, condiciones de aplicación, limitaciones (fatiga, interrupciones) y recomendaciones basadas en evidencia, sin extrapolar más allá del constructo medido.</p><p>Para peritajes, siga requisitos del tribunal o empresa solicitante; mantenga copias seguras conforme a NOM-004 en México y consentimiento informado firmado.</p><p>Centralice resultados, consentimientos y notas de devolución en <a href=\"https://app.kalyo.io/register\">Kalyo</a> para continuidad si el paciente continúa psicoterapia a largo plazo en su consultorio.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        }
    ],
    "faqs": [
        {
            "q": "¿Un test de personalidad tipos diagnostica trastornos?",
            "a": "No por sí solo. Los cuestionarios orientan hipótesis que deben confirmarse con entrevista clínica, historia de vida e impacto funcional persistente."
        },
        {
            "q": "¿NEO PI-R o PID-5-BF?",
            "a": "NEO PI-R describe rasgos normativos; PID-5-BF enfatiza facetas maladaptativas alineadas al DSM-5. Muchos equipos usan ambos según pregunta clínica."
        },
        {
            "q": "¿Puedo aplicar MMPI-2-RF sin certificación?",
            "a": "Requiere formación específica y acceso legal al manual. No es tamizaje rápido; resérvelo a preguntas complejas de personalidad y psicopatología general."
        },
        {
            "q": "¿Cada cuánto repetir un test de personalidad?",
            "a": "Los rasgos son relativamente estables; repetir antes de seis meses rara vez aporta salvo cambio clínico mayor. En psicoterapia, reevalúe facetas objetivo cada seis a doce meses."
        },
        {
            "q": "¿Cómo devolver resultados al paciente?",
            "a": "Use sesión dedicada, gráficos claros, ejemplos conductuales y espacio para preguntas. Evite etiquetas peyorativas; enfatice plasticidad y metas de cambio."
        }
    ],
    "howto": {
        "name": "Cómo elegir un test de personalidad en consulta",
        "steps": [
            {
                "name": "Definir objetivo",
                "text": "Aclare si busca psicoterapia, diagnóstico diferencial o orientación."
            },
            {
                "name": "Elegir instrumento",
                "text": "Seleccione NEO PI-R, PID-5-BF u otro según constructo y tiempo."
            },
            {
                "name": "Consentimiento",
                "text": "Explique propósito, límites y confidencialidad antes de aplicar."
            },
            {
                "name": "Integrar entrevista",
                "text": "Contraste puntajes con ejemplos concretos de conducta."
            },
            {
                "name": "Informe y seguimiento",
                "text": "Redacte recomendaciones accionables y programe reevaluación si aplica."
            }
        ]
    },
    "related": [
        {
            "href": "/articulos/neo-pi-r-personalidad.html",
            "label": "NEO PI-R: personalidad"
        },
        {
            "href": "/articulos/pid-5-bf-personalidad-dsm5.html",
            "label": "PID-5-BF: personalidad DSM-5"
        },
        {
            "href": "/articulos/como-interpretar-tests-psicologicos.html",
            "label": "Cómo interpretar tests psicológicos"
        }
    ],
    "cta_h2": "Gestiona el expediente de tus pacientes con Kalyo",
    "cta_p": "Registra perfiles de personalidad, consentimientos e informes en un expediente clínico ordenado.",
    "after_href": "/articulos/neo-pi-r-personalidad.html",
    "after_loc": "https://kalyo.io/articulos/neo-pi-r-personalidad.html",
    "card_title": "Test de personalidad tipos",
    "card_p": "Modelos dimensionales, NEO PI-R, PID-5 e interpretación clínica responsable."
}
)

# --- Article 37: evaluacion-psicologica-proceso ---
ARTICLES.append(
{
    "slug": "evaluacion-psicologica-proceso",
    "title": "Evaluación psicológica: proceso clínico paso a paso | Kalyo",
    "description": "Evaluación psicológica proceso: entrevista, consentimiento, pruebas, integración e informe clínico ético para psicólogos en México y Latinoamérica hoy.",
    "keywords": "evaluación psicológica proceso, entrevista clínica, informe psicológico, consentimiento informado, psicología clínica México",
    "h1": "Evaluación psicológica proceso: etapas clínicas integradas",
    "breadcrumb_short": "Evaluación psicológica proceso",
    "hero_alt": "Psicólogo con expediente clínico durante evaluación psicológica integral",
    "inline_alt": "Diagrama de etapas del proceso de evaluación psicológica clínica",
    "intro": "La evaluación psicológica proceso es la secuencia ordenada de entrevista, observación, pruebas, integración de datos e informe que permite comprender el funcionamiento psicológico de una persona. En México, psicólogos clínicos deben alinear cada etapa con ética profesional, NOM-004 y objetivos claros acordados con el paciente o institución referente. Esta guía describe fases prácticas sin confundir evaluación con psicoterapia de seguimiento.",
    "sections": [
        {
            "h2": "Definición y alcance de la evaluación psicológica proceso",
            "html": "<p>La <strong>evaluación psicológica proceso</strong> responde preguntas clínicas específicas: diagnóstico diferencial, nivel de severidad, recomendaciones de tratamiento, ajustes escolares o laborales, o evaluación de riesgo. No es un conjunto aleatorio de pruebas; comienza con una pregunta de referencia explícita.</p><p>Diferencie evaluación de psicoterapia: en evaluación, el psicólogo sintetiza datos para un informe con conclusiones y recomendaciones; en terapia, el foco es cambio terapéutico continuo. Puede coexistir, pero los roles deben clarificarse al inicio.</p><p>Consulte <a href=\"/articulos/que-es-la-psicologia-clinica.html\">qué es la psicología clínica</a> para situar la evaluación dentro del quehacer clínico amplio.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Etapa 1: entrevista inicial, anamnesis y consentimiento informado",
            "html": "<p>La entrevista inicial recoge motivo de consulta, historia del problema actual, antecedentes personales y familiares, desarrollo, salud física, consumo de sustancias, medicación, apoyo social y expectativas. Use escucha activa y preguntas abiertas antes de cerrar hipótesis.</p><p>El consentimiento informado explica propósito, procedimientos, duración estimada, límites de confidencialidad, destinatarios del informe y derecho a retirarse. En menores, incluya tutores legales. Documente firma y versión entregada.</p><p>Explore factores culturales, espirituales y socioeconómicos que modulan presentación del cuadro. En LATAM, migración, violencia comunitaria y acceso desigual a servicios influyen en síntomas y ayuda buscada.</p><ol><li>Acordar pregunta clínica.</li><li>Firmar consentimiento.</li><li>Registrar datos sociodemográficos.</li><li>Explorar riesgo agudo (suicidio, violencia).</li></ol><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Etapa 2: selección y aplicación de pruebas psicológicas",
            "html": "<p>Seleccione instrumentos según pregunta clínica, edad, idioma y tiempo disponible. Combine tamizajes breves (PHQ-9, GAD-7) con pruebas amplias cuando la complejidad lo requiera. Evite sobre-evaluar por hábito institucional.</p><p>Administre pruebas en condiciones estandarizadas: ambiente tranquilo, instrucciones completas, registro de interrupciones. Para inteligencia, use baterías apropiadas como <a href=\"/articulos/wisc-v-test-inteligencia-ninos.html\">WISC-V</a> o <a href=\"/articulos/wais-iv-evaluacion-inteligencia-adultos.html\">WAIS-IV</a> según edad.</p><p>Antes de interpretar, revise <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">cómo interpretar tests psicológicos</a> y manuales oficiales de cada instrumento.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Etapa 3: observación, colaterales y registros complementarios",
            "html": "<p>La observación clínica durante entrevista y pruebas aporta datos sobre atención, cooperación, ansiedad, psicomotricidad y estilo interpersonal. Registre conductas, no solo inferencias.</p><p>Con consentimiento, entreviste padres, pareja o maestros cuando evalúe niños o adolescentes. Solicite registros escolares, informes médicos previos o escalas completadas en casa.</p><p>Integre tamizajes de ánimo (<a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a>, <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a>) y personalidad (<a href=\"/articulos/neo-pi-r-personalidad.html\">NEO PI-R</a>) solo si responden a la pregunta clínica.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Etapa 4: integración, formulación de caso y conclusiones",
            "html": "<p>Integre datos convergentes y divergentes. Si prueba y entrevista discrepan, indague sesgo de deseabilidad, estado anímico transitorio o comprensión lectora. Formule caso en biopsicosocial: predisponentes, precipitantes, mantenedores y protectores.</p><p>Las conclusiones responden la pregunta de referencia con lenguaje claro, grados de certeza («compatible con», «sugiere») y recomendaciones priorizadas. Evite diagnósticos múltiples sin jerarquía clínica.</p><p>Derive a psiquiatría, neurología, trabajo social o escuela según hallazgos, documentando urgencia y datos compartidos con consentimiento.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Etapa 5: informe, devolución y registro en expediente clínico",
            "html": "<p>El informe incluye identificación, motivo, métodos, resultados, integración, conclusiones, recomendaciones y limitaciones. Adjunte gráficos comprensibles para el paciente en devolución oral dedicada.</p><p>Archivar pruebas originales, protocolos y consentimientos conforme a NOM-004 y políticas de retención. Si usa plataforma digital, verifique cifrado y control de accesos.</p><p>Organice evaluaciones, informes y seguimiento en <a href=\"https://app.kalyo.io/register\">Kalyo</a> para continuidad cuando el paciente inicia psicoterapia posterior en su consulta.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        }
    ],
    "faqs": [
        {
            "q": "¿Cuánto dura una evaluación psicológica completa?",
            "a": "Varía según complejidad: tamizaje breve puede ser una sesión; evaluación neuropsicológica o pericial puede requerir varias sesiones y colaterales."
        },
        {
            "q": "¿Debo aplicar siempre batería fija?",
            "a": "No. La batería debe derivarse de la pregunta clínica. Aplicar pruebas por rutina aumenta costo, fatiga y riesgo de interpretaciones irrelevantes."
        },
        {
            "q": "¿Puedo evaluar a un familiar?",
            "a": "Evite dualidad de roles cuando sea posible. Si no hay alternativa, documente conflicto de interés y límites estrictos de confidencialidad."
        },
        {
            "q": "¿Qué incluir en devolución al paciente?",
            "a": "Resumen comprensible, implicaciones para tratamiento o ajustes, espacio para preguntas y acuerdo sobre destinatarios del informe escrito."
        },
        {
            "q": "¿La evaluación sustituye psicoterapia?",
            "a": "No. Puede informar el plan terapéutico, pero el proceso evaluativo tiene objetivos distintos y debe cerrarse con informe y recomendaciones claras."
        }
    ],
    "howto": {
        "name": "Cómo estructurar una evaluación psicológica clínica",
        "steps": [
            {
                "name": "Pregunta clínica",
                "text": "Defina qué debe responder la evaluación."
            },
            {
                "name": "Plan de métodos",
                "text": "Seleccione entrevista, pruebas y colaterales necesarios."
            },
            {
                "name": "Consentimiento",
                "text": "Informe y documente acuerdos con el paciente."
            },
            {
                "name": "Aplicación",
                "text": "Administre pruebas en condiciones estandarizadas."
            },
            {
                "name": "Informe y devolución",
                "text": "Integre datos, redacte conclusiones y entregue resultados."
            }
        ]
    },
    "related": [
        {
            "href": "/articulos/que-es-la-psicologia-clinica.html",
            "label": "Qué es la psicología clínica"
        },
        {
            "href": "/articulos/como-interpretar-tests-psicologicos.html",
            "label": "Cómo interpretar tests psicológicos"
        },
        {
            "href": "/articulos/software-para-psicologos-clinicos.html",
            "label": "Software para psicólogos clínicos"
        }
    ],
    "cta_h2": "Gestiona el expediente de tus pacientes con Kalyo",
    "cta_p": "Centraliza entrevistas, pruebas aplicadas e informes de evaluación en un solo expediente clínico.",
    "after_href": "/articulos/que-es-la-psicologia-clinica.html",
    "after_loc": "https://kalyo.io/articulos/que-es-la-psicologia-clinica.html",
    "card_title": "Evaluación psicológica proceso",
    "card_p": "Etapas clínicas: entrevista, pruebas, integración e informe ético."
}
)

# --- Article 38: escala-wechsler-guia-completa ---
ARTICLES.append(
{
    "slug": "escala-wechsler-guia-completa",
    "title": "Escala Wechsler: guía completa WISC-V y WAIS-IV | Kalyo",
    "description": "Escala Wechsler: WISC-V, WAIS-IV, administración clínica, interpretación de índices e integración neuropsicológica para psicólogos clínicos en México hoy.",
    "keywords": "escala Wechsler, WISC-V, WAIS-IV, evaluación inteligencia, neuropsicología, psicología clínica México",
    "h1": "Escala Wechsler: guía clínica WISC-V y WAIS-IV",
    "breadcrumb_short": "Escala Wechsler",
    "hero_alt": "Aplicación clínica de subpruebas Wechsler en evaluación de inteligencia",
    "inline_alt": "Perfil de índices WISC-V y WAIS-IV en informe neuropsicológico",
    "intro": "La escala Wechsler es la familia de baterías más utilizada para evaluar inteligencia y funcionamiento cognitivo en niños, adolescentes y adultos. En México, psicólogos clínicos y neuropsicólogos aplican WISC-V y WAIS-IV en procesos diagnósticos, educativos y de rehabilitación. Esta guía resume administración responsable, interpretación de índices e integración clínica sin reducir a la persona a un número de CI.",
    "sections": [
        {
            "h2": "Qué es la escala Wechsler y cuándo usarla",
            "html": "<p>Las baterías Wechsler miden razonamiento verbal, razonamiento perceptivo, memoria de trabajo y velocidad de procesamiento mediante subpruebas estandarizadas. La <strong>escala Wechsler</strong> no evalúa solo «talento»; describe perfil cognitivo actual relevante para aprendizaje, trabajo y autonomía.</p><p>Indicaciones: sospecha de discapacidad intelectual, TDAH con dudas atencionales, lesión cerebral, deterioro cognitivo, giftedness con disfunción escolar, o planificación de apoyos educativos. Contraindicaciones relativas: agitación extrema, visión/audición no corregida, fatiga severa.</p><p>Ubique la evaluación dentro de <a href=\"/articulos/evaluacion-neuropsicologica-guia-clinica.html\">evaluación neuropsicológica</a> cuando haya múltiples dominios afectados.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "WISC-V: aplicación clínica en niños y adolescentes",
            "html": "<p>El <a href=\"/articulos/wisc-v-test-inteligencia-ninos.html\">WISC-V</a> cubre edades 6:0 a 16:11. Índices principales: Comprensión Verbal, Razonamiento Visual Espacial, Razonamiento Fluido, Memoria de Trabajo y Velocidad de Procesamiento. Opcionalmente Índice de Capacidad General (GAI) cuando velocidad está distorsionada por TDAH o motricidad fina.</p><p>Administre subpruebas en orden recomendado por manual, con descansos según edad y cooperación. Observe frustración, impulsividad y estrategias espontáneas (verbalización, dedos para contar).</p><p>En México, resultados suelen solicitarse para apoyos escolares; el informe debe traducir índices a recomendaciones concretas (tiempo extra, instrucciones segmentadas, material visual).</p><table class=\"items-table\"><thead><tr><th>Instrumento</th><th>Tipo</th><th>Uso</th></tr></thead><tbody><tr><td><a href=\"/articulos/wisc-v-test-inteligencia-ninos.html\">WISC-V</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/conners-3-tdah-ninos.html\">Conners-3 TDAH</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/cbcl-cuestionario-capacidades-comportamiento.html\">CBCL</a></td><td>Guía clínica</td><td>Consulta</td></tr></tbody></table><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "WAIS-IV: evaluación cognitiva en adultos",
            "html": "<p>El <a href=\"/articulos/wais-iv-evaluacion-inteligencia-adultos.html\">WAIS-IV</a> evalúa adultos 16–90 años. Índices: Comprensión Verbal, Razonamiento Perceptivo, Memoria de Trabajo y Velocidad de Procesamiento; Índice General (FSIQ) integra desempeño global con precauciones cuando hay dispersiones marcadas.</p><p>En adultos mayores, considere MoCA o MMSE complementarios para cribado de deterioro, pero no sustituyen perfil Wechsler cuando se requiere detalle.</p><p>Dispersiones significativas entre índices orientan intervenciones: baja Memoria de Trabajo sugiere apoyos externos; baja Velocidad puede reflejar medicación, ansiedad o patología neurológica.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Interpretación clínica de índices y subpruebas",
            "html": "<p>Priorice análisis de perfil sobre FSIQ único. Compare índices entre sí y con historial educativo/laboral. Subpruebas aportan pistas cualitativas (estilo de error, perseveración, abandono).</p><p>Siga principios de <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">cómo interpretar tests psicológicos</a>: convergencia con entrevista, registros escolares y observación.</p><p>Evite inferir trastornos específicos solo por un índice bajo; integre con <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a> y <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a> si hay síntomas afectivos que distorsionan atención el día de la prueba.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Errores frecuentes y consideraciones éticas",
            "html": "<p>Errores: practicar subpruebas antes de reevaluación oficial, mezclar versiones, ignorar ajustes por visión/audición, o interpretar sin formación en test.</p><p>No use Wechsler como único criterio de empleo o escolaridad sin contexto y sin consentimiento. Proteja resultados; son datos sensibles.</p><p>Si perfil sugiere discapacidad intelectual, acompañe devolución con recursos comunitarios y enfoque de apoyos, no solo etiqueta.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Informe, recomendaciones y registro clínico",
            "html": "<p>Informe Wechsler debe incluir tablas de índices, observaciones conductuales, validez de la sesión, integración con pregunta clínica y recomendaciones educativas/laborales/rehabilitación.</p><p>Programe reevaluación solo cuando cambie condición médica, tras rehabilitación cognitiva o para seguimiento escolar acordado.</p><p>Archiva protocolos, audio de tiempos si aplica y versiones de software en <a href=\"https://app.kalyo.io/register\">Kalyo</a> junto con resto del expediente neuropsicológico.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        }
    ],
    "faqs": [
        {
            "q": "¿WISC-V y WAIS-IV son intercambiables?",
            "a": "No. Cada batería está estandarizada para rangos etarios distintos. En transición adolescente tardía, siga manual para decidir batería apropiada."
        },
        {
            "q": "¿Qué hacer si hay dispersión extrema de índices?",
            "a": "Reporte perfil, evite confiar en FSIQ único y explique implicaciones funcionales de fortalezas y debilidades específicas."
        },
        {
            "q": "¿Puedo aplicar Wechsler sin certificación?",
            "a": "Requiere formación y adquisición legal de materiales. Aplicación incorrecta invalida resultados y puede ser antiética."
        },
        {
            "q": "¿Cómo integrar Wechsler con TDAH?",
            "a": "Combine con entrevista DIVA/ASRS y escalas conductuales. Baja velocidad o memoria de trabajo pueden reflejar TDAH, ansiedad o ambos."
        },
        {
            "q": "¿Reevaluar cada cuánto tiempo?",
            "a": "Depende del objetivo clínico. En estabilidad, reevaluaciones anuales o más espaciadas suelen bastar salvo cambio neurológico."
        }
    ],
    "howto": {
        "name": "Cómo planificar una evaluación Wechsler",
        "steps": [
            {
                "name": "Elegir batería",
                "text": "WISC-V para niños/adolescentes; WAIS-IV para adultos."
            },
            {
                "name": "Preparar sesión",
                "text": "Verifique materiales, descansos y condiciones sensoriales."
            },
            {
                "name": "Aplicar y observar",
                "text": "Siga manual; registre conducta y validez."
            },
            {
                "name": "Interpretar perfil",
                "text": "Analice índices y convergencia con historia."
            },
            {
                "name": "Informar",
                "text": "Redacte recomendaciones accionables y devuelva al paciente."
            }
        ]
    },
    "related": [
        {
            "href": "/articulos/wisc-v-test-inteligencia-ninos.html",
            "label": "WISC-V: inteligencia infantil"
        },
        {
            "href": "/articulos/wais-iv-evaluacion-inteligencia-adultos.html",
            "label": "WAIS-IV: inteligencia adultos"
        },
        {
            "href": "/articulos/evaluacion-neuropsicologica-guia-clinica.html",
            "label": "Evaluación neuropsicológica"
        }
    ],
    "cta_h2": "Gestiona el expediente de tus pacientes con Kalyo",
    "cta_p": "Guarda protocolos Wechsler, informes y seguimiento cognitivo en expediente digital seguro.",
    "after_href": "/articulos/wisc-v-test-inteligencia-ninos.html",
    "after_loc": "https://kalyo.io/articulos/wisc-v-test-inteligencia-ninos.html",
    "card_title": "Escala Wechsler: guía completa",
    "card_p": "WISC-V, WAIS-IV, interpretación de índices e integración clínica."
}
)

# --- Article 39: psicologia-clinica-herramientas ---
ARTICLES.append(
{
    "slug": "psicologia-clinica-herramientas",
    "title": "Herramientas psicología clínica: guía para México | Kalyo",
    "description": "Herramientas psicología clínica: tamizajes, escalas, entrevistas estructuradas y software para organizar evaluación en consulta privada en México hoy.",
    "keywords": "herramientas psicología clínica, escalas clínicas, tamizaje, software psicólogos, evaluación psicológica México",
    "h1": "Herramientas psicología clínica: selección y uso en consulta",
    "breadcrumb_short": "Herramientas psicología clínica",
    "hero_alt": "Psicóloga organizando herramientas clínicas digitales y escalas en consultorio",
    "inline_alt": "Clasificación de herramientas clínicas: tamizaje, diagnóstico y seguimiento",
    "intro": "Las herramientas psicología clínica abarcan entrevistas, escalas autorreportadas, observación estructurada, pruebas cognitivas y plataformas de registro. En consulta privada mexicana, elegir instrumentos adecuados equilibra evidencia, tiempo, costo y formación del profesional. Esta guía clasifica herramientas por función clínica y muestra cómo integrarlas en un flujo de trabajo ético y eficiente sin convertir la práctica en acumulación de cuestionarios.",
    "sections": [
        {
            "h2": "Panorama de herramientas psicología clínica por función",
            "html": "<p>Clasifique herramientas en: tamizaje breve (PHQ-2, GAD-2), medida de severidad (<a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a>, <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a>), evaluación amplia de personalidad (<a href=\"/articulos/neo-pi-r-personalidad.html\">NEO PI-R</a>, <a href=\"/articulos/pid-5-bf-personalidad-dsm5.html\">PID-5-BF</a>), cognición (<a href=\"/articulos/wisc-v-test-inteligencia-ninos.html\">WISC-V</a>, <a href=\"/articulos/wais-iv-evaluacion-inteligencia-adultos.html\">WAIS-IV</a>), riesgo (C-SSRS) y medidas de resultado terapéutico (OQ-45).</p><p>Cada categoría responde preguntas distintas. Tamizaje orienta derivación; evaluación amplia profundiza formulación; medidas de resultado monitorizan psicoterapia.</p><p>Enmarque su caja de herramientas dentro de <a href=\"/articulos/que-es-la-psicologia-clinica.html\">qué es la psicología clínica</a>: relación, formulación y intervención basada en evidencia.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Tamizajes de ánimo, ansiedad y funcionamiento general",
            "html": "<p>En atención primaria psicológica, PHQ-9 y GAD-7 son pilares por brevedad y utilidad longitudinal. WHO-5 aporta bienestar positivo. GHQ-12/28 criban distress general.</p><p>Repita escalas cada cuatro a ocho semanas en psicoterapia para graficar tendencia, no solo puntaje aislado. Discuta cambios con el paciente para ajustar intervención.</p><table class=\"items-table\"><thead><tr><th>Instrumento</th><th>Tipo</th><th>Uso</th></tr></thead><tbody><tr><td><a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/who-5-bienestar-psicologico.html\">WHO-5</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/ghq-12-cuestionario-salud-general.html\">GHQ-12</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/k6-tamizaje-salud-mental.html\">K6</a></td><td>Guía clínica</td><td>Consulta</td></tr></tbody></table><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Entrevistas estructuradas y evaluación diagnóstica",
            "html": "<p>Entrevistas como MINI o SCID-5 apoyan diagnóstico diferencial cuando el psicólogo tiene formación. No sustituyen juicio clínico ni exploración psicodinámica cuando es pertinente.</p><p>Combine entrevista con escalas específicas: LSAS para ansiedad social, PCL-5 para TEPT, ASRS para TDAH adulto.</p><p>Consulte <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">cómo interpretar tests psicológicos</a> al integrar múltiples fuentes en un informe único.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Pruebas cognitivas, infantiles y de neurodesarrollo",
            "html": "<p>Además de Wechsler, use MoCA o MMSE para cribado cognitivo breve; SDQ/CBCL en pediatría; M-CHAT y ADOS-2 en sospecha de TEA cuando corresponda formación.</p><p>Evite sobre-etiquetar con un solo cuestionario parental; integre observación directa y contexto escolar.</p><table class=\"items-table\"><thead><tr><th>Instrumento</th><th>Tipo</th><th>Uso</th></tr></thead><tbody><tr><td><a href=\"/articulos/test-moca-evaluacion-cognitiva.html\">MoCA</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/mmse-mini-mental-estado-mental.html\">MMSE</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/sdq-cuestionario-fortalezas-dificultades.html\">SDQ</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/mchat-rf-autismo-infantil.html\">M-CHAT-R/F</a></td><td>Guía clínica</td><td>Consulta</td></tr></tbody></table><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Software clínico y organización del consultorio",
            "html": "<p>El <a href=\"/articulos/software-para-psicologos-clinicos.html\">software para psicólogos clínicos</a> centraliza agenda, expediente, consentimientos, escalas aplicadas e informes. Reduce errores de archivo físico y facilita continuidad en teleconsulta.</p><p>Elija plataformas conformes a NOM-004, con control de accesos y respaldo. Evite almacenar resultados en correo personal sin cifrado.</p><p>Automatice recordatorios de reevaluación y plantillas de informe, pero personalice conclusiones; ningún software reemplaza formulación clínica.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Ética, formación continua y calidad de la práctica",
            "html": "<p>Use solo instrumentos para los que tiene formación y licencia. Mantenga manuales actualizados y supervisión clínica periódica.</p><p>Documente limitaciones de cada herramienta en informes. No prometa certeza diagnóstica absoluta basada en un solo puntaje.</p><p>Integre agenda, pruebas y notas de sesión en <a href=\"https://app.kalyo.io/register\">Kalyo</a> para mantener trazabilidad cuando trabaja solo o en equipo multidisciplinario.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        }
    ],
    "faqs": [
        {
            "q": "¿Cuántas herramientas necesito en consulta privada?",
            "a": "Un núcleo breve (PHQ-9, GAD-7, escalas de riesgo, medida de resultado) más profundización según especialización suele ser suficiente al inicio."
        },
        {
            "q": "¿Puedo usar versiones gratuitas no oficiales?",
            "a": "Evite formularios sin respaldo de manual y derechos de autor. Priorice versiones validadas y aplicación estandarizada."
        },
        {
            "q": "¿Software sustituye expediente clínico papel?",
            "a": "Puede cumplir NOM-004 si cumple requisitos técnicos y de seguridad. Revise políticas de retención y consentimiento digital."
        },
        {
            "q": "¿Cómo elegir entre dos escalas similares?",
            "a": "Compare constructo medido, tiempo, población y utilidad longitudinal en su setting. Consistencia en el tiempo importa más que perfección teórica."
        },
        {
            "q": "¿Debo cobrar aparte cada cuestionario?",
            "a": "Transparente en honorarios: incluya evaluación psicométrica en paquete o desglose según política del consultorio y expectativas del paciente."
        }
    ],
    "howto": {
        "name": "Cómo armar tu kit clínico inicial",
        "steps": [
            {
                "name": "Definir población",
                "text": "Niños, adultos o mixto; orienta selección."
            },
            {
                "name": "Núcleo de tamizaje",
                "text": "Incluya PHQ-9, GAD-7 y escala de riesgo."
            },
            {
                "name": "Profundización",
                "text": "Añada herramientas según especialización."
            },
            {
                "name": "Software",
                "text": "Centralice expediente y recordatorios."
            },
            {
                "name": "Revisión anual",
                "text": "Actualice instrumentos y formación."
            }
        ]
    },
    "related": [
        {
            "href": "/articulos/software-para-psicologos-clinicos.html",
            "label": "Software para psicólogos clínicos"
        },
        {
            "href": "/articulos/que-es-el-phq-9.html",
            "label": "PHQ-9: depresión"
        },
        {
            "href": "/articulos/que-es-el-gad-7.html",
            "label": "GAD-7: ansiedad"
        }
    ],
    "cta_h2": "Gestiona el expediente de tus pacientes con Kalyo",
    "cta_p": "Organiza escalas, informes y seguimiento clínico en una plataforma diseñada para psicólogos.",
    "after_href": "/articulos/software-para-psicologos-clinicos.html",
    "after_loc": "https://kalyo.io/articulos/software-para-psicologos-clinicos.html",
    "card_title": "Herramientas psicología clínica",
    "card_p": "Tamizajes, escalas, entrevistas y software para consulta privada."
}
)

# --- Article 40: tests-psicologicos-hub ---
ARTICLES.append(
{
    "slug": "tests-psicologicos-hub",
    "title": "Tests psicológicos: guía completa psicólogos México | Kalyo",
    "description": "Tests psicológicos: hub clínico con tablas por ansiedad, depresión, cognición, personalidad, infantil, TDAH, TEA, trauma, sustancias y suicidio en México.",
    "keywords": "tests psicológicos, hub clínico, escalas psicológicas, evaluación psicológica, psicología clínica México",
    "h1": "Tests Psicológicos: Guía Completa para Psicólogos en México",
    "breadcrumb_short": "Tests psicológicos hub",
    "hero_alt": "Mapa de categorías de tests psicológicos clínicos para psicólogos en México",
    "inline_alt": "Tabla resumen de instrumentos psicológicos por categoría clínica",
    "intro": "Los tests psicológicos son herramientas estandarizadas que apoyan —sin sustituir— el juicio clínico del psicólogo. Este hub centraliza guías por categoría (ansiedad, depresión, cognición, personalidad, infancia, TDAH, TEA, trauma, sustancias y suicidio) con enlaces a fichas detalladas. Está pensado para consulta privada en México: seleccionar instrumentos con criterio, interpretar con ética y registrar resultados en expediente clínico ordenado.",
    "sections": [
        {
            "h2": "Tabla resumen: tests psicológicos por categoría clínica",
            "html": "<p>Este hub reúne guías clínicas de tests psicológicos publicadas en Kalyo, organizadas por problema o dominio de evaluación. Use la tabla para localizar instrumentos de ansiedad, depresión, cognición, personalidad, infancia, TDAH, TEA, trauma, sustancias y riesgo suicida. Cada enlace conduce a una ficha con indicaciones, administración e interpretación responsable.</p><p>Para profundizar en evaluación integral, consulte <a href=\"/articulos/que-es-la-psicologia-clinica.html\">qué es la psicología clínica</a> y <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">cómo interpretar tests psicológicos</a>.</p><table class=\"items-table\"><thead><tr><th>Instrumento</th><th>Categoría</th><th>Enlace</th></tr></thead><tbody><tr><td>GAD-7</td><td>Ansiedad y estrés</td><td><a href=\"/articulos/que-es-el-gad-7.html\">Ver guía</a></td></tr><tr><td>GAD-2</td><td>Ansiedad y estrés</td><td><a href=\"/articulos/gad-2-tamizaje-ansiedad-breve.html\">Ver guía</a></td></tr><tr><td>STAI</td><td>Ansiedad y estrés</td><td><a href=\"/articulos/stai-ansiedad-estado-rasgo.html\">Ver guía</a></td></tr><tr><td>PHQ-9</td><td>Depresión</td><td><a href=\"/articulos/que-es-el-phq-9.html\">Ver guía</a></td></tr><tr><td>PHQ-2</td><td>Depresión</td><td><a href=\"/articulos/phq-2-tamizaje-depresion-breve.html\">Ver guía</a></td></tr><tr><td>BDI-II</td><td>Depresión</td><td><a href=\"/articulos/inventario-depresion-beck-bdi.html\">Ver guía</a></td></tr><tr><td>WISC-V</td><td>Cognición</td><td><a href=\"/articulos/wisc-v-test-inteligencia-ninos.html\">Ver guía</a></td></tr><tr><td>WAIS-IV</td><td>Cognición</td><td><a href=\"/articulos/wais-iv-evaluacion-inteligencia-adultos.html\">Ver guía</a></td></tr><tr><td>MMSE</td><td>Cognición</td><td><a href=\"/articulos/mmse-mini-mental-estado-mental.html\">Ver guía</a></td></tr><tr><td>NEO PI-R</td><td>Personalidad</td><td><a href=\"/articulos/neo-pi-r-personalidad.html\">Ver guía</a></td></tr><tr><td>PID-5-BF</td><td>Personalidad</td><td><a href=\"/articulos/pid-5-bf-personalidad-dsm5.html\">Ver guía</a></td></tr><tr><td>MMPI-2-RF</td><td>Personalidad</td><td><a href=\"/articulos/mmpi-2-rf-test-personalidad.html\">Ver guía</a></td></tr><tr><td>SDQ</td><td>Infantil</td><td><a href=\"/articulos/sdq-cuestionario-fortalezas-dificultades.html\">Ver guía</a></td></tr><tr><td>CBCL</td><td>Infantil</td><td><a href=\"/articulos/cbcl-cuestionario-capacidades-comportamiento.html\">Ver guía</a></td></tr><tr><td>CDI-2</td><td>Infantil</td><td><a href=\"/articulos/cdi-2-inventario-depresion-infantil.html\">Ver guía</a></td></tr><tr><td>ASRS</td><td>TDAH</td><td><a href=\"/articulos/asrs-tdah-adultos.html\">Ver guía</a></td></tr><tr><td>Conners-3</td><td>TDAH</td><td><a href=\"/articulos/conners-3-tdah-ninos.html\">Ver guía</a></td></tr><tr><td>SNAP-IV</td><td>TDAH</td><td><a href=\"/articulos/snap-iv-tdah-ninos.html\">Ver guía</a></td></tr><tr><td>M-CHAT-R/F</td><td>TEA</td><td><a href=\"/articulos/mchat-rf-autismo-infantil.html\">Ver guía</a></td></tr><tr><td>ADOS-2</td><td>TEA</td><td><a href=\"/articulos/ados-2-evaluacion-tea.html\">Ver guía</a></td></tr><tr><td>ADI-R</td><td>TEA</td><td><a href=\"/articulos/adir-r-entrevista-autismo.html\">Ver guía</a></td></tr><tr><td>PCL-5</td><td>Trauma</td><td><a href=\"/articulos/escala-pcl-5-estres-postraumatico.html\">Ver guía</a></td></tr><tr><td>IES-R</td><td>Trauma</td><td><a href=\"/articulos/ies-r-impacto-estres-postraumatico.html\">Ver guía</a></td></tr><tr><td>ITQ</td><td>Trauma</td><td><a href=\"/articulos/itq-trauma-complejo-cptsd.html\">Ver guía</a></td></tr><tr><td>ASSIST</td><td>Sustancias</td><td><a href=\"/articulos/assist-evaluacion-sustancias-oms.html\">Ver guía</a></td></tr><tr><td>AUDIT</td><td>Sustancias</td><td><a href=\"/articulos/audit-test-alcoholismo.html\">Ver guía</a></td></tr><tr><td>AUDIT-C</td><td>Sustancias</td><td><a href=\"/articulos/audit-c-tamizaje-alcohol-breve.html\">Ver guía</a></td></tr><tr><td>BSS</td><td>Suicidio</td><td><a href=\"/articulos/bssi-ideacion-suicida-beck.html\">Ver guía</a></td></tr><tr><td>C-SSRS</td><td>Suicidio</td><td><a href=\"/articulos/c-ssrs-escala-columbia-suicidio.html\">Ver guía</a></td></tr><tr><td>SBQ-R</td><td>Suicidio</td><td><a href=\"/articulos/sbq-r-conducta-suicida.html\">Ver guía</a></td></tr></tbody></table><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Tests psicológicos: Ansiedad y estrés",
            "html": "<p>En la categoría ansiedad y estrés, estos instrumentos apoyan tamizaje, evaluación de severidad o seguimiento clínico. Seleccione según edad, tiempo disponible y pregunta de referencia. No acumule cuestionarios sin integración clínica.</p><p>Revise manuales, consentimiento informado y confidabilidad de aplicación antes de emitir conclusiones externas.</p><table class=\"items-table\"><thead><tr><th>Instrumento</th><th>Tipo</th><th>Uso</th></tr></thead><tbody><tr><td><a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/gad-2-tamizaje-ansiedad-breve.html\">GAD-2</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/stai-ansiedad-estado-rasgo.html\">STAI</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/escala-hamilton-ansiedad-ham-a.html\">HAM-A</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/lsas-ansiedad-social-liebowitz.html\">LSAS</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/spin-inventario-fobia-social.html\">SPIN</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/mini-spin-ansiedad-social-breve.html\">Mini-SPIN</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/pass-sensibilidad-ansiedad.html\">PASS</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/hads-ansiedad-depresion-hospitalaria.html\">HADS</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/zung-escala-ansiedad.html\">Zung ansiedad</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/scared-ansiedad-infantil.html\">SCARED</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/rcmas-2-ansiedad-infantil.html\">RCMAS-2</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/test-beck-ansiedad-bai.html\">BAI</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/pss-10-escala-estres-percibido.html\">PSS-10</a></td><td>Guía clínica</td><td>Consulta</td></tr></tbody></table><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Tests psicológicos: Depresión",
            "html": "<p>En la categoría depresión, estos instrumentos apoyan tamizaje, evaluación de severidad o seguimiento clínico. Seleccione según edad, tiempo disponible y pregunta de referencia. No acumule cuestionarios sin integración clínica.</p><p>Revise manuales, consentimiento informado y confidabilidad de aplicación antes de emitir conclusiones externas.</p><table class=\"items-table\"><thead><tr><th>Instrumento</th><th>Tipo</th><th>Uso</th></tr></thead><tbody><tr><td><a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/phq-2-tamizaje-depresion-breve.html\">PHQ-2</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/inventario-depresion-beck-bdi.html\">BDI-II</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/ces-d-escala-depresion.html\">CES-D</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/ham-d-escala-hamilton-depresion.html\">HAM-D</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/hamilton-depresion-hdrs-17.html\">HDRS-17</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/escala-madrs-depresion.html\">MADRS</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/zung-escala-depresion.html\">Zung depresión</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/gds-15-depresion-geriatrica.html\">GDS-15</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/cdi-2-inventario-depresion-infantil.html\">CDI-2</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/rads-2-depresion-adolescentes.html\">RADS-2</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/epds-depresion-postparto.html\">EPDS</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/trastorno-depresivo-mayor.html\">Depresión mayor</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/depresion-sintomas.html\">Síntomas depresión</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/who-5-bienestar-psicologico.html\">WHO-5</a></td><td>Guía clínica</td><td>Consulta</td></tr></tbody></table><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Tests psicológicos: Cognición",
            "html": "<p>En la categoría cognición, estos instrumentos apoyan tamizaje, evaluación de severidad o seguimiento clínico. Seleccione según edad, tiempo disponible y pregunta de referencia. No acumule cuestionarios sin integración clínica.</p><p>Revise manuales, consentimiento informado y confidabilidad de aplicación antes de emitir conclusiones externas.</p><table class=\"items-table\"><thead><tr><th>Instrumento</th><th>Tipo</th><th>Uso</th></tr></thead><tbody><tr><td><a href=\"/articulos/wisc-v-test-inteligencia-ninos.html\">WISC-V</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/wais-iv-evaluacion-inteligencia-adultos.html\">WAIS-IV</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/mmse-mini-mental-estado-mental.html\">MMSE</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/test-moca-evaluacion-cognitiva.html\">MoCA</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/test-reloj-dibujo-cognicion.html\">Test del reloj</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/raven-spm-razonamiento-no-verbal.html\">Raven</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/brief-funciones-ejecutivas.html\">BRIEF</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/coeficiente-intelectual.html\">CI</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/evaluacion-neuropsicologica-guia-clinica.html\">Neuropsicología</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/tipos-de-memoria.html\">Memoria</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/como-interpretar-tests-psicologicos.html\">Interpretación tests</a></td><td>Guía clínica</td><td>Consulta</td></tr></tbody></table><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Tests psicológicos: Personalidad",
            "html": "<p>En la categoría personalidad, estos instrumentos apoyan tamizaje, evaluación de severidad o seguimiento clínico. Seleccione según edad, tiempo disponible y pregunta de referencia. No acumule cuestionarios sin integración clínica.</p><p>Revise manuales, consentimiento informado y confidabilidad de aplicación antes de emitir conclusiones externas.</p><table class=\"items-table\"><thead><tr><th>Instrumento</th><th>Tipo</th><th>Uso</th></tr></thead><tbody><tr><td><a href=\"/articulos/neo-pi-r-personalidad.html\">NEO PI-R</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/pid-5-bf-personalidad-dsm5.html\">PID-5-BF</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/mmpi-2-rf-test-personalidad.html\">MMPI-2-RF</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/epq-r-cuestionario-eysenck.html\">EPQ-R</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/cuestionario-16pf-personalidad.html\">16PF</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/tests-psicologicos-de-personalidad.html\">Tests personalidad</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/trastorno-limite-personalidad.html\">TLP</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/trastorno-narcisista-personalidad.html\">Narcisismo</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/trastorno-antisocial-personalidad.html\">Antisocial</a></td><td>Guía clínica</td><td>Consulta</td></tr></tbody></table><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        },
        {
            "h2": "Tests psicológicos: Infantil",
            "html": "<p>En la categoría infantil, estos instrumentos apoyan tamizaje, evaluación de severidad o seguimiento clínico. Seleccione según edad, tiempo disponible y pregunta de referencia. No acumule cuestionarios sin integración clínica.</p><p>Revise manuales, consentimiento informado y confidabilidad de aplicación antes de emitir conclusiones externas.</p><table class=\"items-table\"><thead><tr><th>Instrumento</th><th>Tipo</th><th>Uso</th></tr></thead><tbody><tr><td><a href=\"/articulos/sdq-cuestionario-fortalezas-dificultades.html\">SDQ</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/cbcl-cuestionario-capacidades-comportamiento.html\">CBCL</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/cdi-2-inventario-depresion-infantil.html\">CDI-2</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/scared-ansiedad-infantil.html\">SCARED</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/terapia-infantil.html\">Terapia infantil</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/psc-17-tamizaje-pediatrico.html\">PSC-17</a></td><td>Guía clínica</td><td>Consulta</td></tr><tr><td><a href=\"/articulos/vineland-3-conducta-adaptativa.html\">Vineland-3</a></td><td>Guía clínica</td><td>Consulta</td></tr></tbody></table><p>Para consultorios que aplican decenas de escalas, <a href=\"https://app.kalyo.io/register\">Kalyo</a> ayuda a registrar resultados, fechas de reevaluación y devoluciones al paciente sin perder trazabilidad clínica.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p><p>En consulta privada en México, documente motivo de referencia, contexto cultural, lengua materna y nivel educativo antes de interpretar cualquier puntaje. Explique al paciente que los resultados describen funcionamiento actual en un momento y contexto específicos, no definen identidad ni capacidad futura. Evite lenguaje estigmatizante y vincule hallazgos a metas terapéuticas concretas acordadas en sesión. Revise contraindicaciones: crisis aguda, intoxicación, falta de sueño extremo o comprensión lectora insuficiente para autoinformes. Coordine con psiquiatría cuando haya psicosis activa, riesgo suicida inminente o sospecha de condición médica que explique el cuadro. Registre versiones de instrumentos, tiempos de aplicación y observaciones conductuales durante la evaluación.</p>"
        }
    ],
    "faqs": [
        {
            "q": "¿Este hub reemplaza formación en tests?",
            "a": "No. Cada instrumento requiere capacitación, manual y aplicación estandarizada. El hub orienta y enlaza recursos clínicos."
        },
        {
            "q": "¿Puedo usar solo tamizajes para diagnosticar?",
            "a": "Los tamizajes orientan derivación o profundización. El diagnóstico clínico integra entrevista, historia y, cuando procede, evaluación ampliada."
        },
        {
            "q": "¿Qué tests recomiendan para consulta general?",
            "a": "PHQ-9, GAD-7, escalas de riesgo suicida breves y medida de resultado terapéutica suelen ser un núcleo útil; amplíe según población atendida."
        },
        {
            "q": "¿Cómo mantener actualizado mi repertorio?",
            "a": "Revise guías anuales, supervisión clínica y actualizaciones de manuales. Evite versiones obsoletas sin respaldo normativo vigente."
        },
        {
            "q": "¿Dónde registrar resultados de múltiples escalas?",
            "a": "Use expediente clínico digital con trazabilidad, consentimientos y gráficos de seguimiento longitudinal por paciente."
        }
    ],
    "howto": {
        "name": "Cómo navegar el hub de tests psicológicos",
        "steps": [
            {
                "name": "Identificar categoría",
                "text": "Localice ansiedad, depresión, cognición u otra según pregunta clínica."
            },
            {
                "name": "Abrir ficha",
                "text": "Lea guía del instrumento elegido."
            },
            {
                "name": "Planificar batería",
                "text": "Combine tamizaje y profundización necesaria."
            },
            {
                "name": "Aplicar con ética",
                "text": "Siga manual y documente condiciones."
            },
            {
                "name": "Integrar e informar",
                "text": "Contraste prueba con entrevista y contexto."
            }
        ]
    },
    "related": [
        {
            "href": "/articulos/como-interpretar-tests-psicologicos.html",
            "label": "Cómo interpretar tests psicológicos"
        },
        {
            "href": "/articulos/que-es-la-psicologia-clinica.html",
            "label": "Qué es la psicología clínica"
        },
        {
            "href": "/articulos/software-para-psicologos-clinicos.html",
            "label": "Software para psicólogos clínicos"
        }
    ],
    "cta_h2": "Gestiona el expediente de tus pacientes con Kalyo",
    "cta_p": "Centraliza resultados de múltiples tests, gráficos de seguimiento e informes en un expediente clínico.",
    "after_href": "/articulos/como-interpretar-tests-psicologicos.html",
    "after_loc": "https://kalyo.io/articulos/como-interpretar-tests-psicologicos.html",
    "card_title": "Tests psicológicos: hub clínico",
    "card_p": "Guía completa por categorías con enlaces a instrumentos clínicos."
}
)


if __name__ == "__main__":
    for s in ARTICLES:
        validate(s)
        print(s["slug"], body_words(s), "words")
    print("articles", len(ARTICLES))
    print("lines", len(Path(__file__).read_text(encoding="utf-8").splitlines()))
