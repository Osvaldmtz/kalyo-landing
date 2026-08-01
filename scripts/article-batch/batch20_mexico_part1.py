# -*- coding: utf-8 -*-
"""Batch 20 Mexico part 1 — 10 clinical psychometric article specs for Kalyo renderer."""


def articles_part1(p, table, faqs_std):
    """Return article specs 1-10 for batch 20 Mexico SEO."""
    _ = faqs_std  # optional helper from caller
    return [
        _art_test_psicologico_mexico(p, table),
        _art_gad7(p, table),
        _art_beck_bdi_ii(p, table),
        _art_wisc_v(p, table),
        _art_mmpi2(p, table),
        _art_test_inteligencia_adultos(p, table),
        _art_16pf(p, table),
        _art_historia_clinica(p, table),
        _art_mbi(p, table),
        _art_bdi(p, table),
    ]


def _art_test_psicologico_mexico(p, table):
    return {'slug': 'test-psicologico-mas-usados-mexico',
 'title': 'Test psicol&oacute;gico m&aacute;s usados en M&eacute;xico: gu&iacute;a cl&iacute;nica | Kalyo',
 'description': 'Gu&iacute;a de los test psicol&oacute;gicos m&aacute;s usados en M&eacute;xico: PHQ-9, GAD-7, Beck, '
                'WISC-V y MMPI-2. Selecci&oacute;n, interpretaci&oacute;n y registro cl&iacute;nico para '
                'psic&oacute;logos.',
 'keywords': 'test psicológico, tests psicométricos México, PHQ-9, GAD-7, evaluación psicológica, psicometría clínica',
 'h1': 'Test psicológico más usados en México: panorama clínico para psicólogos',
 'breadcrumb_short': 'Tests psicológicos en México',
 'quick_answer': 'El test psicológico más empleado en consulta mexicana combina tamizajes breves como PHQ-9 y GAD-7 '
                 'con instrumentos de personalidad e inteligencia según la pregunta clínica. La elección depende de '
                 'objetivos, edad, validez y normas disponibles; el test psicológico nunca sustituye la entrevista ni '
                 'el juicio profesional.',
 'intro_long': 'En México, la demanda de evaluación psicológica crece en consulta privada, escuelas, empresas y '
               'servicios de salud mental. Conocer qué test psicológico se utiliza con mayor frecuencia — y por qué — '
               'ayuda a estandarizar la práctica, cumplir criterios de calidad y comunicar hallazgos con claridad a '
               'pacientes e instituciones.',
 'test_name': 'tests psicológicos estandarizados',
 'hero_alt': 'Psicóloga revisando resultados de tests psicológicos en consulta clínica en México',
 'inline_alt': 'Cuadro comparativo de tests psicológicos más usados en evaluación clínica mexicana',
 'sections': [{'h2': 'Por qué el test psicológico es central en la práctica mexicana',
               'html': '<p>Un <strong>test psicológico</strong> es un procedimiento estandarizado para medir '
                       'constructos psicológicos con reglas de aplicación, puntuación e interpretación. En México, su '
                       'uso se ha expandido por la necesidad de objetivar síntomas, apoyar diagnósticos diferenciales, '
                       'documentar evolución y responder a requerimientos de escuelas, aseguradoras o procesos '
                       'laborales. No obstante, la calidad clínica depende de seleccionar el instrumento adecuado, '
                       'respetar derechos de autor y contextualizar resultados dentro de la entrevista y la historia '
                       'del paciente.</p>\n'
                       '<p>Los tamizajes breves como el <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a> y el <a '
                       'href="/articulos/que-es-el-gad-7.html">GAD-7</a> dominan la atención primaria emocional porque '
                       'son rápidos, sensibles al cambio y compatibles con telepsicología. En evaluación profunda, el '
                       'psicólogo recurre a inventarios de personalidad, escalas de inteligencia y baterías '
                       'neuropsicológicas. La clave no es acumular pruebas, sino responder preguntas clínicas '
                       'precisas: ¿hay depresión significativa?, ¿ansiedad generalizada?, ¿déficit cognitivo?, ¿perfil '
                       'de personalidad que explique conflicto interpersonal?</p>\n'
                       '<p>La <a href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a> exige registrar '
                       'hallazgos relevantes en la historia clínica; integrar un test psicológico bien elegido mejora '
                       'trazabilidad y continuidad asistencial. Consultorios que migran a <a '
                       'href="/articulos/tests-psicologicos-digitales.html">tests psicológicos digitales</a> reducen '
                       'errores de captura y facilitan gráficas de seguimiento, siempre con respaldo ético y '
                       'confidencialidad.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p>'},
              {'h2': 'Tamizaje emocional: PHQ-9, GAD-7 y DASS-21',
               'html': '<p>En consulta privada mexicana, los cuestionarios de síntomas emocionales son el primer '
                       'escalón. El PHQ-9 mide severidad depresiva en nueve ítems; el GAD-7 evalúa ansiedad '
                       'generalizada; la <a href="/articulos/escala-dass-21.html">DASS-21</a> ofrece subescalas de '
                       'depresión, ansiedad y estrés. Estos instrumentos no diagnostican por sí solos, pero orientan '
                       'entrevista, psicoeducación y decisiones sobre frecuencia de sesiones o derivación '
                       'psiquiátrica.</p>\n'
                       '<p>Ventajas clínicas: bajo costo, re aplicación seriada, comparabilidad entre sesiones. '
                       'Limitaciones: sesgo de deseabilidad social, lectura heterogénea en pacientes con baja '
                       'escolaridad (requiere apoyo o versiones oralizadas) y riesgo de sobreinterpretar un puntaje '
                       'sin explorar contexto traumático, duelo reciente o condiciones médicas. Combine tamizaje con '
                       'exploración de ideas suicidas, funcionamiento laboral y red de apoyo.</p><table '
                       'class="items-table"><thead><tr><th>Instrumento</th><th>Constructo</th><th>Tiempo '
                       'aprox.</th></tr></thead><tbody><tr><td>PHQ-9</td><td>Depresión</td><td>3–5 '
                       'min</td></tr><tr><td>GAD-7</td><td>Ansiedad generalizada</td><td>2–4 '
                       'min</td></tr><tr><td>DASS-21</td><td>Depresión, ansiedad, estrés</td><td>5–7 '
                       'min</td></tr></tbody></table><p>Documente fecha, contexto de aplicación, versión del '
                       'instrumento y limitaciones cuando no existan baremos locales. La trazabilidad mejora '
                       'continuidad asistencial, supervisión clínica y comunicación con otros profesionales de la red '
                       'de salud mental en México.</p>'},
              {'h2': 'Evaluación de personalidad: MMPI-2, 16PF y Conners',
               'html': '<p>Cuando la pregunta clínica exige perfilar rasgos, estilos interpersonales o validez de '
                       'respuesta, entran inventarios extensos. El <a '
                       'href="/articulos/mmpi-2-rf-test-personalidad.html">MMPI-2-RF</a> es referente en salud mental '
                       'forense y clínica por sus escalas de validez; el <a '
                       'href="/articulos/cuestionario-16pf-personalidad.html">16PF</a> describe factores primarios de '
                       'personalidad útiles en orientación vocacional y selección; el <a '
                       'href="/articulos/conners-3-tdah-ninos.html">Conners-3</a> aporta perspectiva multimodal en '
                       'sospecha de TDAH infantil.</p>\n'
                       '<p>Estos test psicológicos requieren capacitación específica: interpretación actuarial vs. '
                       'configural, manejo de escalas de mentira o simulación, y comunicación de resultados sin '
                       'etiquetar al paciente. En México, verifique disponibilidad de manual en español, normas '
                       'latinoamericanas cuando existan y restricciones de copyright al imprimir o digitalizar '
                       'formularios.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p>'},
              {'h2': 'Inteligencia y neuropsicología: WISC-V y baterías cognitivas',
               'html': '<p>La evaluación cognitiva responde a preguntas sobre rendimiento intelectual, aptitudes '
                       'académicas o secuelas de lesión cerebral. El <a '
                       'href="/articulos/wisc-v-test-inteligencia-ninos.html">WISC-V</a> es el test de inteligencia '
                       'infantil más extendido; en adultos se emplean WAIS-IV o baterías breves según el contexto '
                       'descrito en nuestra guía de <a '
                       'href="/articulos/evaluacion-neuropsicologica-guia-clinica.html">evaluación '
                       'neuropsicológica</a>.</p>\n'
                       '<p>Interpretar un CI o índices factoriales sin integrar historia escolar, condiciones '
                       'sensoriales, ansiedad durante la prueba o bilingüismo puede conducir a diagnósticos erróneos '
                       'de discapacidad intelectual o, inversamente, subestimar dificultades de aprendizaje. Documente '
                       'comportamiento durante la administración, validez de la sesión y recomendaciones funcionales, '
                       'no solo números.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p>'},
              {'h2': 'Criterios para elegir un test psicológico en consulta',
               'html': '<p>Antes de administrar cualquier prueba, defina la pregunta clínica, población objetivo y uso '
                       'previsto del informe (tratamiento, escuela, laboral). Revise evidencia de validez y '
                       'fiabilidad, existencia de baremos en español y nivel de escolaridad requerido. Evite baterías '
                       'redundantes que fatiguen al paciente y aumenten costo sin aportar datos nuevos.</p>\n'
                       '<p>La guía <a href="/articulos/como-interpretar-tests-psicologicos.html">cómo interpretar '
                       'tests psicológicos</a> enfatiza integrar múltiples fuentes: entrevista, observación, '
                       'colaterales y escalas autorreportadas. Registre limitaciones cuando no haya normas mexicanas '
                       'oficiales y utilice interpretación conservadora. Para continuidad documental, centralice '
                       'aplicaciones, puntajes e interpretación en <a href="https://app.kalyo.io/register">Kalyo</a> '
                       'manteniendo confidencialidad y trazabilidad clínica.</p><p>Documente fecha, contexto de '
                       'aplicación, versión del instrumento y limitaciones cuando no existan baremos locales. La '
                       'trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación con otros '
                       'profesionales de la red de salud mental en México.</p>'},
              {'h2': 'Ética, derechos de autor y calidad psicométrica',
               'html': '<p>Adquirir test psicológico implica respetar derechos de autor y restricciones de '
                       'reproducción. Compartir formularios por WhatsApp o usar versiones pirateadas invalida '
                       'resultados y expone legalmente al profesional. Informe al paciente el propósito de la '
                       'evaluación, obtenga consentimiento informado y explique que puede preguntar sobre sus '
                       'resultados.</p>\n'
                       '<p>La calidad psicométrica exige supervisión, actualización continua y revisión crítica de '
                       'baremos obsoletos. En poblaciones indígenas o rurales, considere sesgo cultural y posible '
                       'necesidad de interpretación con intérprete. El test psicológico es herramienta, no veredicto: '
                       'el juicio clínico integra contexto sociopolítico mexicano — violencia comunitaria, migración, '
                       'inequidad en salud — que ninguna escala captura por completo.</p><p>Documente fecha, contexto '
                       'de aplicación, versión del instrumento y limitaciones cuando no existan baremos locales. La '
                       'trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación con otros '
                       'profesionales de la red de salud mental en México.</p>'}],
 'faqs': [{'q': '¿Cuál es el test psicológico más usado en México?',
           'a': 'No existe un único ganador: PHQ-9 y GAD-7 lideran tamizaje emocional; WISC-V domina inteligencia '
                'infantil; MMPI-2 es frecuente en personalidad clínica. La elección depende del objetivo evaluativo y '
                'del setting.'},
          {'q': '¿Puede un test psicológico diagnosticar por sí solo?',
           'a': 'No. Los tests aportan evidencia cuantitativa que debe integrarse con entrevista clínica, criterios '
                'diagnósticos y, cuando aplique, exploración médica. Un puntaje elevado orienta, no confirma '
                'automáticamente un trastorno.'},
          {'q': '¿Se pueden usar tests psicológicos en telepsicología?',
           'a': 'Sí, especialmente autorreportes breves digitales con plataformas seguras. Pruebas que exigen '
                'observación presencial o materiales manipulativos requieren presencialidad o adaptación profesional '
                'justificada.'},
          {'q': '¿Qué hacer si no hay normas mexicanas para un instrumento?',
           'a': 'Documente la limitación, utilice baremos regionales con cautela, enfatice interpretación cualitativa '
                'y evite conclusiones absolutas sobre percentiles. Considere reevaluación con instrumento alternativo '
                'validado.'},
          {'q': '¿Cómo registrar resultados en la historia clínica?',
           'a': 'Incluya nombre del test, fecha, puntajes relevantes, interpretación clínica y recomendaciones. La '
                'NOM-004 exige contenido mínimo en la historia; evite copiar ítems protegidos por copyright.'}],
 'related': [{'href': '/articulos/que-es-el-phq-9.html', 'label': 'PHQ-9: escala de depresión'},
             {'href': '/articulos/que-es-el-gad-7.html', 'label': 'GAD-7: ansiedad generalizada'},
             {'href': '/articulos/tests-psicologicos-digitales.html', 'label': 'Tests psicológicos digitales'},
             {'href': '/articulos/como-interpretar-tests-psicologicos.html',
              'label': 'Cómo interpretar tests psicológicos'}],
 'references': ['American Psychiatric Association (2013). <em>Diagnostic and Statistical Manual of Mental '
                'Disorders</em> (5th ed.). Arlington, VA: APA.',
                'Secretaría de Salud (1999). <em>Norma Oficial Mexicana NOM-004-SSA3-2012</em>, Expediente clínico. '
                'Diario Oficial de la Federación.',
                'International Test Commission (2014). ITC Guidelines on Test Use. <em>International Journal of '
                'Testing</em>, 14(2), 123–142.']}

def _art_gad7(p, table):
    return {'slug': 'gad-7-escala-ansiedad-generalizada',
 'title': 'GAD-7: escala de ansiedad generalizada &mdash; gu&iacute;a cl&iacute;nica | Kalyo',
 'description': 'GAD-7 en M&eacute;xico: siete &iacute;tems, puntajes de corte, interpretaci&oacute;n cl&iacute;nica y '
                'tamizaje de ansiedad generalizada en consulta privada, salud mental y telepsicolog&iacute;a.',
 'keywords': 'GAD-7, ansiedad generalizada, escala ansiedad, tamizaje ansiedad, psicología clínica México',
 'h1': 'GAD-7: escala de ansiedad generalizada — interpretación para psicólogos',
 'breadcrumb_short': 'GAD-7 escala ansiedad',
 'quick_answer': 'El GAD-7 es un cuestionario breve de siete ítems que mide síntomas de ansiedad generalizada durante '
                 'las últimas dos semanas. Puntajes de 10 o más sugieren ansiedad clínica significativa; el GAD-7 es '
                 'ideal para tamizaje, seguimiento terapéutico y combinación rutinaria con PHQ-9 en consulta mexicana.',
 'intro_long': 'La ansiedad generalizada es de las consultas más frecuentes en México urbano, y el GAD-7 se ha '
               'convertido en estándar de facto por su brevedad y evidencia empírica. Esta guía profundiza en '
               'administración, puntos de corte, diferencial diagnóstico y uso clínico más allá del artículo '
               'introductorio, orientada a psicólogos que buscan estandarizar su práctica.',
 'test_name': 'GAD-7',
 'hero_alt': 'Escala GAD-7 de ansiedad generalizada en formato clínico digital',
 'inline_alt': 'Tabla de puntuación y niveles de severidad del GAD-7',
 'sections': [{'h2': 'Qué mide el GAD-7 y cuándo administrarlo',
               'html': '<p>El <strong>GAD-7</strong> (Generalized Anxiety Disorder-7) evalúa nucleos sintomáticos del '
                       'trastorno de ansiedad generalizada: preocupación excesiva, dificultad para controlarla, '
                       'inquietud, fatiga, concentración pobre, irritabilidad y tensión muscular o sueño alterado. '
                       'Cada ítem se puntúa de 0 (nada) a 3 (casi todos los días), total 0–21. Es autoadministrado y '
                       'requiere menos de cinco minutos.</p>\n'
                       '<p>Adminístrelo en evaluación inicial, antes de iniciar psicoterapia, tras intervenciones '
                       'breves y en controles periódicos. En servicios de salud mental pública mexicana, su uso '
                       'permite triage rápido cuando el tiempo de consulta es limitado. Compare con el artículo base '
                       '<a href="/articulos/que-es-el-gad-7.html">qué es el GAD-7</a> y complemente con <a '
                       'href="/articulos/stai-ansiedad-estado-rasgo.html">STAI</a> cuando necesite distinguir ansiedad '
                       'estado vs. rasgo.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite '
                       'conclusiones categóricas basadas en un solo puntaje; integre entrevista, observación, historia '
                       'de tratamiento previo y factores contextuales. El informe debe ser comprensible para el '
                       'paciente sin perder rigor técnico ni omitir recomendaciones accionables.</p>'},
              {'h2': 'Puntuación, puntos de corte y tabla de severidad',
               'html': '<p>Los puntos de corte más citados provienen de Spitzer et al. (2006): 0–4 mínima, 5–9 leve, '
                       '10–14 moderada, 15–21 severa. Un puntaje ≥10 tiene buena sensibilidad para detectar TAG '
                       'probable, aunque el diagnóstico exige entrevista clínica según DSM-5. Un ítem adicional '
                       'opcional pregunta por dificultad funcional causada por los síntomas.</p>\n'
                       '<p>Registre puntaje total, fecha y cambio respecto a línea base. En telepsicología, confirme '
                       'que el paciente comprendió la ventana temporal («últimas dos semanas»). Evite comparar '
                       'puntajes obtenidos durante crisis agudas con controles en remisión sin anotar '
                       'contexto.</p><table '
                       'class="severity-table"><thead><tr><th>Puntuaci&oacute;n</th><th>Severidad</th><th>Acci&oacute;n '
                       'cl&iacute;nica</th></tr></thead><tbody><tr><td><span class="score-badge">0 &ndash; '
                       '4</span></td><td><strong>M&iacute;nima</strong></td><td>Monitoreo; psicoeducaci&oacute;n si '
                       'hay factores de riesgo.</td></tr><tr><td><span class="score-badge">5 &ndash; '
                       '9</span></td><td><strong>Leve</strong></td><td>Vigilancia activa; reevaluar en 2&ndash;4 '
                       'semanas.</td></tr><tr><td><span class="score-badge">10 &ndash; '
                       '14</span></td><td><strong>Moderada</strong></td><td>Plan de tratamiento; TCC '
                       'recomendada.</td></tr><tr><td><span class="score-badge">15 &ndash; '
                       '21</span></td><td><strong>Severa</strong></td><td>Tratamiento activo; valorar '
                       'derivaci&oacute;n psiqui&aacute;trica.</td></tr></tbody></table><p>Documente fecha, contexto '
                       'de aplicación, versión del instrumento y limitaciones cuando no existan baremos locales. La '
                       'trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación con otros '
                       'profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme identidad '
                       'del evaluado, condiciones de privacidad y comprensión de instrucciones antes de puntuar. '
                       'Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad '
                       'o fatiga atencional.</p>'},
              {'h2': 'GAD-7 vs. otras escalas de ansiedad',
               'html': '<p>Frente al <a href="/articulos/stai-ansiedad-estado-rasgo.html">STAI</a>, el GAD-7 es más '
                       'breve y centrado en TAG; el STAI diferencia ansiedad estado y rasgo con 40 ítems. La <a '
                       'href="/articulos/escala-dass-21.html">DASS-21</a> incluye subescalas de depresión y estrés, '
                       'útil cuando el cuadro es mixto. En depresión comórbida, aplique también <a '
                       'href="/articulos/que-es-el-phq-9.html">PHQ-9</a>: más del 60% de pacientes con TAG presentan '
                       'síntomas depresivos significativos.</p>\n'
                       '<p>Escalas heteroaplicadas como HAM-A requieren entrevista clínica entrenada; resérvelas para '
                       'investigación o casos donde la deseabilidad social distorsiona autorreportes. El GAD-7 '
                       'permanece como primera línea en consultorio privado por eficiencia y '
                       'evidencia.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p>'},
              {'h2': 'Interpretación clínica más allá del puntaje',
               'html': '<p>Explore falsos positivos: consumo de cafeína, hipotiroidismo, efectos secundarios de '
                       'broncodilatadores o situaciones vitales estresantes (litigio, cuidado de familiar enfermo). '
                       'Falsos negativos aparecen cuando el paciente minimiza por estigma laboral o desea evitar '
                       'medicación. Observe congruencia entre puntaje, lenguaje corporal y relato.</p>\n'
                       '<p>Traduzca resultados a lenguaje comprensible: «Su puntaje sugiere ansiedad moderada; '
                       'trabajaremos en técnicas de regulación y revisaremos en cuatro semanas». Vincule con plan de '
                       'tratamiento (TCC, activación conductual, higiene del sueño). Si hay ideación suicida, el GAD-7 '
                       'no sustituye evaluación de riesgo específica.</p><p>Documente fecha, contexto de aplicación, '
                       'versión del instrumento y limitaciones cuando no existan baremos locales. La trazabilidad '
                       'mejora continuidad asistencial, supervisión clínica y comunicación con otros profesionales de '
                       'la red de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p>'},
              {'h2': 'Seguimiento terapéutico y sensibilidad al cambio',
               'html': '<p>Repita el GAD-7 cada cuatro a ocho sesiones o tras módulos terapéuticos. Una reducción ≥5 '
                       'puntos suele considerarse cambio clínicamente relevante en investigación, aunque adapte metas '
                       'individualmente. Grafique evolución para motivar al paciente y documentar respuesta ante '
                       'aseguradoras o referentes médicos.</p>\n'
                       '<p>Digitalice aplicaciones con <a href="/articulos/tests-psicologicos-digitales.html">tests '
                       'psicológicos digitales</a> para evitar errores de suma. Consulte <a '
                       'href="/articulos/como-interpretar-tests-psicologicos.html">cómo interpretar tests '
                       'psicológicos</a> al redactar informes. Plataformas como <a '
                       'href="https://app.kalyo.io/register">Kalyo</a> permiten administrar GAD-7, almacenar historial '
                       'y generar recordatorios de reevaluación.</p><p>Documente fecha, contexto de aplicación, '
                       'versión del instrumento y limitaciones cuando no existan baremos locales. La trazabilidad '
                       'mejora continuidad asistencial, supervisión clínica y comunicación con otros profesionales de '
                       'la red de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p>'},
              {'h2': 'Consideraciones en contexto mexicano',
               'html': '<p>En pacientes con baja escolaridad, lea ítems en voz alta o use versión oral sin alterar '
                       'contenido. Considere somatización cultural: algunos pacientes reportan más síntomas físicos '
                       'que preocupación cognitiva; explore equivalentes idiomáticos («nervios», «coraje», «presión en '
                       'el pecho»).</p>\n'
                       '<p>En zonas con violencia crónica, distinga ansiedad generalizada de respuestas normativas a '
                       'inseguridad; documente factores contextuales. Si deriva a psiquiatría, adjunte GAD-7 seriado y '
                       'PHQ-9 para decisiones farmacológicas informadas.</p><p>Documente fecha, contexto de '
                       'aplicación, versión del instrumento y limitaciones cuando no existan baremos locales. La '
                       'trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación con otros '
                       'profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme identidad '
                       'del evaluado, condiciones de privacidad y comprensión de instrucciones antes de puntuar. '
                       'Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad '
                       'o fatiga atencional.</p>'}],
 'faqs': [{'q': '¿El GAD-7 diagnostica trastorno de ansiedad generalizada?',
           'a': 'No por sí solo. Detecta síntomas compatibles; el diagnóstico requiere entrevista, duración ≥6 meses, '
                'dificultad para controlar la preocupación e impacto funcional según DSM-5.'},
          {'q': '¿Qué puntaje del GAD-7 indica tratamiento?',
           'a': 'Generalmente ≥10 justifica intervención psicológica activa; entre 5 y 9, vigilancia y psicoeducación. '
                'Ajuste según funcionamiento, comorbilidades y preferencia del paciente.'},
          {'q': '¿Puedo combinar GAD-7 con PHQ-9?',
           'a': 'Sí; es práctica recomendada porque depresión y ansiedad coexisten frecuentemente. Aplicar ambos en la '
                'primera sesión ofrece perfil emocional integral en pocos minutos.'},
          {'q': '¿GAD-7 sirve en población adolescente?',
           'a': 'Ha sido validado en jóvenes en varios estudios, pero interprete con cautela en menores de 14 años; '
                'considere entrevista desarrollista y escalas específicas si hay duda.'},
          {'q': '¿Cada cuánto repetir el GAD-7?',
           'a': 'Cada 4–8 semanas en tratamiento activo, o tras intervenciones específicas. En remisión, espaciar a '
                'controles trimestrales según riesgo de recaída.'}],
 'related': [{'href': '/articulos/que-es-el-gad-7.html', 'label': 'Qué es el GAD-7'},
             {'href': '/articulos/que-es-el-phq-9.html', 'label': 'PHQ-9 depresión'},
             {'href': '/articulos/escala-dass-21.html', 'label': 'DASS-21 estrés y ansiedad'},
             {'href': '/articulos/stai-ansiedad-estado-rasgo.html', 'label': 'STAI ansiedad estado-rasgo'}],
 'references': ['Spitzer, R. L., Kroenke, K., Williams, J. B., & Löwe, B. (2006). A brief measure for assessing '
                'generalized anxiety disorder: The GAD-7. <em>Archives of Internal Medicine</em>, 166(10), 1092–1097.',
                'Löwe, B., Decker, O., Müller, S., et al. (2008). Validation and standardization of the GAD-7 in the '
                'general population. <em>Medical Care</em>, 46(3), 266–274.',
                'Plummer, F., Manea, L., Trepel, D., & McMillan, D. (2016). Screening for anxiety disorders with the '
                'GAD-7. <em>General Hospital Psychiatry</em>, 39, 24–31.']}

def _art_beck_bdi_ii(p, table):
    return {'slug': 'escala-de-beck-bdi-ii',
 'title': 'Escala de Beck BDI-II: gu&iacute;a cl&iacute;nica en M&eacute;xico | Kalyo',
 'description': 'Escala de Beck BDI-II: aplicaci&oacute;n, puntuaci&oacute;n, sensibilidad al cambio y diferencias con '
                'PHQ-9. Gu&iacute;a pr&aacute;ctica para psic&oacute;logos que eval&uacute;an depresi&oacute;n en '
                'M&eacute;xico.',
 'keywords': 'escala de Beck, BDI-II, inventario depresión Beck, evaluación depresión, psicometría clínica México',
 'h1': 'Escala de Beck BDI-II: aplicación e interpretación clínica',
 'breadcrumb_short': 'Escala de Beck BDI-II',
 'quick_answer': 'La escala de Beck BDI-II es un inventario de 21 ítems que mide severidad depresiva en adultos y '
                 'adolescentes desde los 13 años. Evalúa síntomas cognitivos, afectivos y somáticos durante las '
                 'últimas dos semanas. Es sensible al cambio terapéutico y complementa el PHQ-9 cuando se requiere '
                 'mayor detalle sintomático.',
 'intro_long': 'El BDI-II permanece entre los instrumentos más citados para evaluar depresión en investigación y '
               'clínica. En México, psicólogos lo emplean en consulta privada, hospitales y estudios de outcome. Esta '
               'guía detalla administración, puntuación, diferencias con tamizajes breves y buenas prácticas de '
               'interpretación.',
 'test_name': 'BDI-II',
 'hero_alt': 'Formulario BDI-II escala de Beck para evaluación de depresión clínica',
 'inline_alt': 'Tabla de severidad y puntos de corte del BDI-II escala de Beck',
 'sections': [{'h2': 'Qué mide la escala de Beck BDI-II',
               'html': '<p>La <strong>escala de Beck</strong> BDI-II (Beck Depression Inventory-II) cuantifica '
                       'síntomas depresivos: tristeza, pesimismo, fracaso, anhedonia, culpa, castigo, autodesprecio, '
                       'ideas suicidas, llanto, irritabilidad, retraimiento social, indecisión, imagen corporal, '
                       'dificultad para trabajar, alteraciones del sueño y del apetito, fatiga y pérdida de interés '
                       'sexual. Cada ítem ofrece cuatro opciones graduadas en intensidad, puntuadas 0 a 3.</p>\n'
                       '<p>A diferencia del <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a>, el BDI-II es más '
                       'extenso y captura matices cognitivos (sentimientos de fracaso, autocrítica) útiles en '
                       'psicoterapia cognitiva. No diagnostica trastorno depresivo mayor por sí solo; integra '
                       'entrevista clínica y criterios DSM-5. Compare también con el <a '
                       'href="/articulos/inventario-depresion-beck-bdi.html">inventario depresión Beck</a> en su '
                       'versión histórica BDI-I cuando revise literatura antigua.</p>\n'
                       '<p>En adolescentes, verifique comprensión de ítems abstractos; en adultos mayores, distinga '
                       'síntomas depresivos de quejas somáticas propias del envejecimiento o comorbilidades '
                       'médicas.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y limitaciones '
                       'cuando no existan baremos locales. La trazabilidad mejora continuidad asistencial, supervisión '
                       'clínica y comunicación con otros profesionales de la red de salud mental en México.</p><p>En '
                       'telepsicología, confirme identidad del evaluado, condiciones de privacidad y comprensión de '
                       'instrucciones antes de puntuar. Registre interrupciones, apoyo de terceros o necesidad de '
                       'oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite conclusiones categóricas '
                       'basadas en un solo puntaje; integre entrevista, observación, historia de tratamiento previo y '
                       'factores contextuales. El informe debe ser comprensible para el paciente sin perder rigor '
                       'técnico ni omitir recomendaciones accionables.</p>'},
              {'h2': 'Administración, puntuación y tabla de severidad',
               'html': '<p>Tiempo de aplicación: 5 a 10 minutos autoadministrado. Instrucciones: responder según cómo '
                       'se ha sentido durante las <em>últimas dos semanas</em>, incluyendo el día de hoy. Sume ítems '
                       'para obtener puntaje total (0–63). Revise coherencia interna: respuestas extremas en todos los '
                       'ítems sugieren lectura aleatoria o simulación.</p>\n'
                       '<p>Registre puntaje total, fecha y contexto (inicio vs. seguimiento de tratamiento). En '
                       'telepsicología, confirme que el paciente no recibió ayuda para responder. Si hay ideación '
                       'suicida elevada en ítem 9, active protocolo de evaluación de riesgo inmediato.</p><table '
                       'class="severity-table"><thead><tr><th>Puntuaci&oacute;n</th><th>Severidad</th><th>Acci&oacute;n '
                       'cl&iacute;nica</th></tr></thead><tbody><tr><td><span class="score-badge">0 &ndash; '
                       '13</span></td><td><strong>M&iacute;nima</strong></td><td>Monitoreo; psicoeducaci&oacute;n '
                       'sobre s&iacute;ntomas.</td></tr><tr><td><span class="score-badge">14 &ndash; '
                       '19</span></td><td><strong>Leve</strong></td><td>Vigilancia; considerar psicoterapia '
                       'breve.</td></tr><tr><td><span class="score-badge">20 &ndash; '
                       '28</span></td><td><strong>Moderada</strong></td><td>Tratamiento activo; valorar '
                       'combinaci&oacute;n con psiquiatr&iacute;a.</td></tr><tr><td><span class="score-badge">29 '
                       '&ndash; 63</span></td><td><strong>Severa</strong></td><td>Intervenci&oacute;n intensiva; '
                       'evaluar riesgo suicida.</td></tr></tbody></table><p>Documente fecha, contexto de aplicación, '
                       'versión del instrumento y limitaciones cuando no existan baremos locales. La trazabilidad '
                       'mejora continuidad asistencial, supervisión clínica y comunicación con otros profesionales de '
                       'la red de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p>'},
              {'h2': 'BDI-II vs. PHQ-9 y otros tamizajes',
               'html': '<p>El PHQ-9 es más breve y ampliamente usado en atención primaria; el BDI-II ofrece mayor '
                       'granularidad sintomática. En estudios de cambio terapéutico, el BDI-II muestra buena '
                       'sensibilidad; en triage rápido, el PHQ-9 puede ser preferible. La <a '
                       'href="/articulos/escala-dass-21.html">DASS-21</a> añade ansiedad y estrés cuando el cuadro es '
                       'mixto.</p>\n'
                       '<p>Evite administrar BDI-II y PHQ-9 en la misma sesión sin justificación: redundancia fatiga '
                       'al paciente. Elija uno como outcome principal y manténgalo seriado. Consulte <a '
                       'href="/articulos/como-interpretar-tests-psicologicos.html">cómo interpretar tests '
                       'psicológicos</a> al integrar múltiples fuentes.</p><p>Documente fecha, contexto de aplicación, '
                       'versión del instrumento y limitaciones cuando no existan baremos locales. La trazabilidad '
                       'mejora continuidad asistencial, supervisión clínica y comunicación con otros profesionales de '
                       'la red de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p>'},
              {'h2': 'Interpretación clínica y comunicación de resultados',
               'html': '<p>Explore falsos positivos: duelo reciente, enfermedad médica, efectos secundarios de '
                       'medicación. Falsos negativos: deseabilidad social, minimización por estigma laboral. Observe '
                       'congruencia entre puntaje, afecto observado y relato del paciente.</p>\n'
                       '<p>Comunique resultados en lenguaje accesible: «Su puntaje indica depresión moderada; '
                       'trabajaremos en activación conductual y revisaremos la escala en un mes». Vincule ítems '
                       'elevados con objetivos terapéuticos concretos (sueño, autocrítica, '
                       'aislamiento).</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p>'},
              {'h2': 'Seguimiento terapéutico y registro digital',
               'html': '<p>Repita BDI-II cada cuatro a ocho semanas en tratamiento activo. Una reducción ≥10 puntos '
                       'suele considerarse cambio clínicamente significativo en investigación con BDI-II, aunque '
                       'adapte metas individualmente. Grafique evolución para motivar al paciente.</p>\n'
                       '<p>Use <a href="/articulos/tests-psicologicos-digitales.html">tests psicológicos digitales</a> '
                       'para reducir errores de suma. Registre resultados conforme a <a '
                       'href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a>. Centralice historial en <a '
                       'href="https://app.kalyo.io/register">Kalyo</a> para trazabilidad entre '
                       'sesiones.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p>'},
              {'h2': 'Consideraciones éticas y culturales en México',
               'html': '<p>Respete derechos de autor del BDI-II; no reproduzca ítems completos en informes públicos o '
                       'redes sociales. Obtenga consentimiento informado para evaluación y explique propósito clínico '
                       'vs. laboral.</p>\n'
                       '<p>En poblaciones con somatización predominante, explore equivalentes culturales de síntomas. '
                       'En contextos de violencia o pérdida reciente, distinga reacción situacional de episodio '
                       'depresivo mayor persistente.</p><p>Documente fecha, contexto de aplicación, versión del '
                       'instrumento y limitaciones cuando no existan baremos locales. La trazabilidad mejora '
                       'continuidad asistencial, supervisión clínica y comunicación con otros profesionales de la red '
                       'de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p>'}],
 'faqs': [{'q': '¿Qué edad mínima tiene el BDI-II?',
           'a': 'Desde 13 años con comprensión lectora adecuada. En menores, valide comprensión oralmente y considere '
                'instrumentos específicos para infancia si hay duda.'},
          {'q': '¿BDI-II diagnostica depresión mayor?',
           'a': 'No. Cuantifica severidad sintomática. El diagnóstico requiere entrevista clínica, duración, impacto '
                'funcional y exclusión de otras causas según DSM-5.'},
          {'q': '¿Cuándo preferir BDI-II sobre PHQ-9?',
           'a': 'Cuando necesita detalle sintomático para psicoterapia cognitiva, investigación de cambio o '
                'seguimiento en consulta privada con tiempo suficiente.'},
          {'q': '¿Cómo manejar ideación suicida en ítem 9?',
           'a': 'Un puntaje alto exige evaluación de riesgo inmediata: plan, medios, intentos previos, factores '
                'protectores. No finalice sesión sin plan de seguridad si hay riesgo.'},
          {'q': '¿Existen baremos mexicanos para BDI-II?',
           'a': 'Consulte manual en español y estudios locales. Si no hay normas específicas, documente limitación e '
                'interprete con conservadurismo usando rangos generales de severidad.'}],
 'related': [{'href': '/articulos/inventario-depresion-beck-bdi.html', 'label': 'Inventario depresión Beck BDI'},
             {'href': '/articulos/que-es-el-phq-9.html', 'label': 'PHQ-9: tamizaje depresión'},
             {'href': '/articulos/como-interpretar-tests-psicologicos.html', 'label': 'Interpretar tests psicológicos'},
             {'href': '/articulos/escala-dass-21.html', 'label': 'DASS-21 depresión y ansiedad'}],
 'references': ['Beck, A. T., Steer, R. A., & Brown, G. K. (1996). <em>Manual for the Beck Depression '
                'Inventory-II</em>. San Antonio, TX: Psychological Corporation.',
                'Beck, A. T., Steer, R. A., & Garbin, M. G. (1988). Psychometric properties of the Beck Depression '
                'Inventory. <em>Clinical Psychology Review</em>, 8(1), 77–100.']}

def _art_wisc_v(p, table):
    return {'slug': 'wisc-v-escala-inteligencia-ninos',
 'title': 'WISC V: escala de inteligencia infantil &mdash; gu&iacute;a M&eacute;xico | Kalyo',
 'description': 'WISC-V en M&eacute;xico: &iacute;ndices, administraci&oacute;n, interpretaci&oacute;n cl&iacute;nica '
                'y consideraciones culturales para evaluaci&oacute;n de inteligencia infantil en contexto escolar.',
 'keywords': 'WISC V, WISC-V, escala inteligencia niños, evaluación cognitiva infantil, CI infantil México',
 'h1': 'WISC V: escala de inteligencia para niños — guía clínica en México',
 'breadcrumb_short': 'WISC V inteligencia infantil',
 'quick_answer': 'El WISC V (Wechsler Intelligence Scale for Children, quinta edición) evalúa capacidad intelectual en '
                 'niños de 6 a 16 años mediante índices verbales, visoespaciales, fluidos, de memoria de trabajo y '
                 'velocidad de procesamiento. Genera CI total e índices factoriales con intervalos de confianza. '
                 'Requiere aplicación presencial estandarizada por psicólogo capacitado.',
 'intro_long': 'La evaluación de inteligencia infantil es recurrente en consultas mexicanas por dificultades '
               'escolares, sospecha de discapacidad intelectual, altas capacidades o requerimientos de becas. El WISC '
               'V es el instrumento de referencia; esta guía complementa el artículo introductorio con énfasis en '
               'índices, interpretación integrada y contexto cultural.',
 'test_name': 'WISC-V',
 'hero_alt': 'Psicóloga aplicando WISC V a escolar en evaluación de inteligencia infantil',
 'inline_alt': 'Esquema de índices del WISC V escala de inteligencia para niños',
 'sections': [{'h2': 'Estructura del WISC V e índices principales',
               'html': '<p>El <strong>WISC V</strong> organiza la evaluación en cinco índices primarios: Comprensión '
                       'Verbal (ICV), Visoespacial (IVE), Razonamiento Fluido (IRF), Memoria de Trabajo (IMT) y '
                       'Velocidad de Procesamiento (IVP). El CI Total (CIT) resume funcionamiento intelectual global. '
                       'Subpruebas núcleo y complementarias permiten perfilar fortalezas y debilidades.</p>\n'
                       '<p>Compare con la guía <a href="/articulos/wisc-v-test-inteligencia-ninos.html">WISC-V test '
                       'inteligencia niños</a> para fundamentos. En interpretación, priorice discrepancias '
                       'significativas entre índices sobre un CI único: un niño con IRF alto e IMT bajo puede requerir '
                       'apoyos distintos a uno con perfil homogéneo.</p>\n'
                       '<p>Documente comportamiento durante la aplicación: fatiga, ansiedad, negativa a cooperar, '
                       'dolor de cabeza o hambre distorsionan resultados. La validez de la sesión es tan importante '
                       'como el puntaje.</p><table '
                       'class="items-table"><thead><tr><th>Índice</th><th>Constructo</th><th>Ejemplo de implicación '
                       'clínica</th></tr></thead><tbody><tr><td>ICV</td><td>Conocimiento verbal, '
                       'razonamiento</td><td>Rendimiento académico en lectura</td></tr><tr><td>IVE</td><td>Integración '
                       'visoespacial</td><td>Geometría, mapas, construcción</td></tr><tr><td>IRF</td><td>Razonamiento '
                       'lógico novel</td><td>Resolución de problemas nuevos</td></tr><tr><td>IMT</td><td>Retención y '
                       'manipulación</td><td>Seguir instrucciones complejas</td></tr><tr><td>IVP</td><td>Velocidad y '
                       'atención</td><td>Tareas cronometradas escolares</td></tr></tbody></table><p>Documente fecha, '
                       'contexto de aplicación, versión del instrumento y limitaciones cuando no existan baremos '
                       'locales. La trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación '
                       'con otros profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme '
                       'identidad del evaluado, condiciones de privacidad y comprensión de instrucciones antes de '
                       'puntuar. Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja '
                       'escolaridad o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo '
                       'puntaje; integre entrevista, observación, historia de tratamiento previo y factores '
                       'contextuales. El informe debe ser comprensible para el paciente sin perder rigor técnico ni '
                       'omitir recomendaciones accionables.</p>'},
              {'h2': 'Cuándo solicitar evaluación WISC V en México',
               'html': '<p>Indicaciones frecuentes: bajo rendimiento escolar persistente, sospecha de discapacidad '
                       'intelectual o aprendizaje, evaluación de altas capacidades, requerimientos de SEP o '
                       'instituciones educativas, seguimiento post lesión cerebral pediátrica. Coordine con pedagogía '
                       'y medicina antes de concluir.</p>\n'
                       '<p>Evite evaluar en crisis familiar aguda o tras suspensión escolar reciente sin '
                       'estabilización emocional. En <a '
                       'href="/articulos/evaluacion-neuropsicologica-guia-clinica.html">evaluación '
                       'neuropsicológica</a> integral, el WISC V es componente, no batería completa.</p><p>Documente '
                       'fecha, contexto de aplicación, versión del instrumento y limitaciones cuando no existan '
                       'baremos locales. La trazabilidad mejora continuidad asistencial, supervisión clínica y '
                       'comunicación con otros profesionales de la red de salud mental en México.</p><p>En '
                       'telepsicología, confirme identidad del evaluado, condiciones de privacidad y comprensión de '
                       'instrucciones antes de puntuar. Registre interrupciones, apoyo de terceros o necesidad de '
                       'oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite conclusiones categóricas '
                       'basadas en un solo puntaje; integre entrevista, observación, historia de tratamiento previo y '
                       'factores contextuales. El informe debe ser comprensible para el paciente sin perder rigor '
                       'técnico ni omitir recomendaciones accionables.</p>'},
              {'h2': 'Administración estandarizada y validez',
               'html': '<p>Requiere aplicación individual presencial, tiempo 60–90 minutos según edad y protocolo. '
                       'Respete orden, tiempos y criterios de puntuación del manual. Interrupciones, traducción '
                       'improvisada o ayuda parental invalidan estandarización.</p>\n'
                       '<p>En niños bilingües, documente dominancia lingüística y años de exposición académica en '
                       'español. Considere pruebas complementarias no verbales si el ICV está sesgado por barrera '
                       'idiomática reciente.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite '
                       'conclusiones categóricas basadas en un solo puntaje; integre entrevista, observación, historia '
                       'de tratamiento previo y factores contextuales. El informe debe ser comprensible para el '
                       'paciente sin perder rigor técnico ni omitir recomendaciones accionables.</p>'},
              {'h2': 'Interpretación clínica más allá del CI',
               'html': '<p>Reporte índices con intervalos de confianza (95%), fortalezas/debilidades significativas y '
                       'recomendaciones funcionales para escuela y familia. Evite etiquetas deterministas («bajo '
                       'cociente») sin describir apoyos concretos.</p>\n'
                       '<p>Integre informes escolares, historial médico y escalas conductuales como <a '
                       'href="/articulos/conners-3-tdah-ninos.html">Conners-3</a> cuando hay sospecha de TDAH '
                       'comórbido. Un CI promedio con IVP muy bajo puede explicar dificultades en exámenes '
                       'cronometrados.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite '
                       'conclusiones categóricas basadas en un solo puntaje; integre entrevista, observación, historia '
                       'de tratamiento previo y factores contextuales. El informe debe ser comprensible para el '
                       'paciente sin perder rigor técnico ni omitir recomendaciones accionables.</p>'},
              {'h2': 'Consideraciones culturales y baremos',
               'html': '<p>Verifique baremos disponibles para población mexicana o latinoamericana en manual. Si usa '
                       'normas extranjeras, documente limitación. Considere acceso desigual a estimulación cognitiva, '
                       'interrupción escolar por migración o trabajo infantil.</p>\n'
                       '<p>En comunidades indígenas, evalúe necesidad de intérprete y validez de subpruebas verbales. '
                       'La interpretación debe ser conservadora y centrada en necesidades de apoyo, no en ranking '
                       'social.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y limitaciones '
                       'cuando no existan baremos locales. La trazabilidad mejora continuidad asistencial, supervisión '
                       'clínica y comunicación con otros profesionales de la red de salud mental en México.</p><p>En '
                       'telepsicología, confirme identidad del evaluado, condiciones de privacidad y comprensión de '
                       'instrucciones antes de puntuar. Registre interrupciones, apoyo de terceros o necesidad de '
                       'oralizar ítems por baja escolaridad o fatiga atencional.</p>'},
              {'h2': 'Informes, derechos y registro clínico',
               'html': '<p>El informe WISC V debe incluir motivo de evaluación, procedimiento, observaciones '
                       'conductuales, puntajes, interpretación y recomendaciones. Proteja confidencialidad conforme a '
                       '<a href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a>.</p>\n'
                       '<p>Respete copyright de Pearson; no reproduzca ítems. Para continuidad documental, archive '
                       'puntajes e interpretación en <a href="https://app.kalyo.io/register">Kalyo</a>. Consulte <a '
                       'href="/articulos/como-interpretar-tests-psicologicos.html">cómo interpretar tests '
                       'psicológicos</a> al redactar conclusiones.</p><p>Documente fecha, contexto de aplicación, '
                       'versión del instrumento y limitaciones cuando no existan baremos locales. La trazabilidad '
                       'mejora continuidad asistencial, supervisión clínica y comunicación con otros profesionales de '
                       'la red de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p>'}],
 'faqs': [{'q': '¿Desde qué edad se aplica el WISC V?',
           'a': 'De 6 años 0 meses a 16 años 11 meses. Para menores de 6 años, considere WPPSI-IV; para adolescentes '
                'mayores próximos a adultez, evalúe WAIS-IV según contexto.'},
          {'q': '¿El WISC V diagnostica TDAH o dislexia?',
           'a': 'No. Evalúa funcionamiento intelectual e índices cognitivos. Diagnósticos específicos requieren '
                'baterías adicionales, historial escolar y criterios clínicos.'},
          {'q': '¿Se puede aplicar WISC V en línea?',
           'a': 'No de forma estandarizada. Requiere materiales manipulativos y administración presencial certificada. '
                'Teleconsulta puede usarse solo para devolución de resultados.'},
          {'q': '¿Qué hacer con discrepancia grande entre índices?',
           'a': 'Analice validez de sesión, perfil de aprendizaje, posible trastorno específico de aprendizaje o TDAH. '
                'Recomiende apoyos acordes a debilidades significativas, no solo CI total.'},
          {'q': '¿Cuánto dura la validez de un informe WISC V?',
           'a': 'Generalmente 2–3 años en infancia por cambio desarrollador rápido. Reevalúe antes si hay intervención '
                'intensiva, lesión neurológica o cambio escolar significativo.'}],
 'related': [{'href': '/articulos/wisc-v-test-inteligencia-ninos.html', 'label': 'WISC-V test inteligencia niños'},
             {'href': '/articulos/evaluacion-neuropsicologica-guia-clinica.html',
              'label': 'Evaluación neuropsicológica'},
             {'href': '/articulos/conners-3-tdah-ninos.html', 'label': 'Conners-3 TDAH niños'},
             {'href': '/articulos/como-interpretar-tests-psicologicos.html',
              'label': 'Interpretar tests psicológicos'}],
 'references': ['Wechsler, D. (2014). <em>WISC-V: Escala de Inteligencia de Wechsler para Niños</em>. Manual de '
                'aplicación y corrección. Pearson.',
                'Sattler, J. M., & Ryan, J. J. (2009). <em>Assessment of Child and Adolescent Intelligence</em> (4th '
                'ed.). Springer.']}

def _art_mmpi2(p, table):
    return {'slug': 'mmpi-2-inventario-personalidad',
 'title': 'MMPI-2: inventario de personalidad cl&iacute;nica en M&eacute;xico | Kalyo',
 'description': 'MMPI-2 en evaluaci&oacute;n cl&iacute;nica mexicana: escalas cl&iacute;nicas, validez e '
                'interpretaci&oacute;n cautelosa. Gu&iacute;a para psic&oacute;logos con formaci&oacute;n en '
                'psicometr&iacute;a avanzada.',
 'keywords': 'MMPI-2, inventario personalidad, evaluación psicológica forense, psicometría avanzada, MMPI México',
 'h1': 'MMPI-2: inventario de personalidad — interpretación clínica avanzada',
 'breadcrumb_short': 'MMPI-2 personalidad',
 'quick_answer': 'El MMPI-2 es un inventario de personalidad de 567 ítems (567 verdadero/falso) ampliamente usado en '
                 'salud mental, forense y selección con precaución. Incluye escalas clínicas, de contenido y de '
                 'validez esenciales para detectar simulación, negación o respuesta aleatoria. Requiere formación '
                 'especializada y nunca debe interpretarse sin revisar validez.',
 'intro_long': 'En México, el MMPI-2 aparece en evaluaciones clínicas complejas, peritajes y contextos '
               'organizacionales con restricciones éticas. Esta guía orienta a psicólogos con base psicométrica sobre '
               'escalas clave, interpretación integrada y límites del instrumento, complementando el artículo sobre '
               'MMPI-2-RF.',
 'test_name': 'MMPI-2',
 'hero_alt': 'Psicólogo interpretando perfil MMPI-2 de personalidad en consulta clínica',
 'inline_alt': 'Esquema de escalas clínicas y de validez del MMPI-2',
 'sections': [{'h2': 'Estructura del MMPI-2 y escalas de validez',
               'html': '<p>El <strong>MMPI-2</strong> (Minnesota Multiphasic Personality Inventory-2) evalúa '
                       'psicopatología y rasgos de personalidad mediante ítems de acuerdo/desacuerdo. Antes de '
                       'interpretar escalas clínicas, revise <em>siempre</em> validez: ? (no se puede calificar), L '
                       '(mentira), F (infrecuencia), K (corrección defensiva) y escalas de consistencia. Perfiles '
                       'inválidos invalidan conclusiones clínicas.</p>\n'
                       '<p>Compare con <a href="/articulos/mmpi-2-rf-test-personalidad.html">MMPI-2-RF</a> para la '
                       'versión reestructurada con menos ítems y modelo dimensional. En clínica mexicana, verifique '
                       'acceso a software autorizado y baremos; la interpretación actuarial requiere tablas '
                       'oficiales.</p>\n'
                       '<p>Documente tiempo de aplicación (60–90 min), interrupciones y nivel educativo. Respuestas '
                       'aleatorias o simulación consciente distorsionan todo el perfil.</p><p>Documente fecha, '
                       'contexto de aplicación, versión del instrumento y limitaciones cuando no existan baremos '
                       'locales. La trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación '
                       'con otros profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme '
                       'identidad del evaluado, condiciones de privacidad y comprensión de instrucciones antes de '
                       'puntuar. Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja '
                       'escolaridad o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo '
                       'puntaje; integre entrevista, observación, historia de tratamiento previo y factores '
                       'contextuales. El informe debe ser comprensible para el paciente sin perder rigor técnico ni '
                       'omitir recomendaciones accionables.</p><p>Revise coherencia entre síntomas reportados, '
                       'conducta observada en sesión e informes de terceros cuando estén disponibles. Las '
                       'discrepancias orientan exploración adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Escalas clínicas básicas y contenido',
               'html': '<p>Escalas clínicas clásicas (1 Hipocondriasis, 2 Depresión, 3 Histeria, 4 Desviación '
                       'psicopática, 6 Paranoia, 7 Psicastenia, 8 Esquizofrenia, 9 Hipomanía, 0 Introversión social) '
                       'deben interpretarse en conjunto, no aisladamente. Escalas de contenido (ANS, DEP, ANG, etc.) '
                       'afinan temas específicos.</p>\n'
                       '<p>Evite etiquetar al paciente con nombres de escalas («es esquizofrenia en MMPI»). Describa '
                       'elevaciones como «tendencia a experiencias inusuales/perceptivas que requieren corroboración '
                       'clínica». Integre entrevista e historial.</p><table class="items-table"><thead><tr><th>Escala '
                       'validez</th><th>Indica</th><th>Acción</th></tr></thead><tbody><tr><td>F '
                       'elevada</td><td>Exageración o simulación</td><td>Reentrevistar; considerar '
                       'invalidar</td></tr><tr><td>K elevada</td><td>Defensividad</td><td>Interpretar con cautela; '
                       'explorar vergüenza</td></tr><tr><td>? >30</td><td>Respuestas omitidas</td><td>Completar o '
                       'invalidar perfil</td></tr></tbody></table><p>Documente fecha, contexto de aplicación, versión '
                       'del instrumento y limitaciones cuando no existan baremos locales. La trazabilidad mejora '
                       'continuidad asistencial, supervisión clínica y comunicación con otros profesionales de la red '
                       'de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Usos clínicos vs. organizacionales en México',
               'html': '<p>En salud mental, el MMPI-2 apoya diagnóstico diferencial, plan de tratamiento y evaluación '
                       'prequirúrgica (bariatría, trasplante). En forense, exige estándares de evidencia más estrictos '
                       'y posible testimonio pericial.</p>\n'
                       '<p>En selección laboral, su uso es controvertido; requiere justificación psicométrica, '
                       'consentimiento y no discriminación. La interpretación debe vincularse a competencias del '
                       'puesto, no a estigmatización.</p><p>Documente fecha, contexto de aplicación, versión del '
                       'instrumento y limitaciones cuando no existan baremos locales. La trazabilidad mejora '
                       'continuidad asistencial, supervisión clínica y comunicación con otros profesionales de la red '
                       'de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p>'},
              {'h2': 'Interpretación configural y actuarial',
               'html': '<p>Analice codigotipos (dos escalas clínicas más elevadas), configuraciones de validez y '
                       'congruencia con entrevista. Software autorizado genera interpretaciones actuariales que el '
                       'clínico debe revisar críticamente.</p>\n'
                       '<p>Consulte <a href="/articulos/como-interpretar-tests-psicologicos.html">cómo interpretar '
                       'tests psicológicos</a> y contraste con <a '
                       'href="/articulos/cuestionario-16pf-personalidad.html">16PF</a> cuando la pregunta es perfil de '
                       'rasgos normativos, no psicopatología.</p><p>Documente fecha, contexto de aplicación, versión '
                       'del instrumento y limitaciones cuando no existan baremos locales. La trazabilidad mejora '
                       'continuidad asistencial, supervisión clínica y comunicación con otros profesionales de la red '
                       'de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p>'},
              {'h2': 'Comunicación de resultados y ética',
               'html': '<p>Devolución debe ser presencial o videollamada segura, con lenguaje comprensible y espacio '
                       'para preguntas. Evite entregar solo reporte computarizado sin contexto.</p>\n'
                       '<p>Proteja datos conforme a <a '
                       'href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a>. Respete copyright; no '
                       'comparta perfiles en redes. Archive resultados en <a '
                       'href="https://app.kalyo.io/register">Kalyo</a> con acceso restringido.</p><p>Documente fecha, '
                       'contexto de aplicación, versión del instrumento y limitaciones cuando no existan baremos '
                       'locales. La trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación '
                       'con otros profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme '
                       'identidad del evaluado, condiciones de privacidad y comprensión de instrucciones antes de '
                       'puntuar. Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja '
                       'escolaridad o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo '
                       'puntaje; integre entrevista, observación, historia de tratamiento previo y factores '
                       'contextuales. El informe debe ser comprensible para el paciente sin perder rigor técnico ni '
                       'omitir recomendaciones accionables.</p>'},
              {'h2': 'Limitaciones y supervisión clínica',
               'html': '<p>El MMPI-2 no diagnostica por sí solo; puede reflejar estado transitorio, somatización '
                       'cultural o respuesta defensiva. Supervisión periódica es recomendable, especialmente en '
                       'forense.</p>\n'
                       '<p>En poblaciones sin baremos locales, documente cautela interpretativa. Reevalúe si hay '
                       'cambio terapéutico significativo antes de decisiones de alto impacto.</p><p>Documente fecha, '
                       'contexto de aplicación, versión del instrumento y limitaciones cuando no existan baremos '
                       'locales. La trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación '
                       'con otros profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme '
                       'identidad del evaluado, condiciones de privacidad y comprensión de instrucciones antes de '
                       'puntuar. Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja '
                       'escolaridad o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo '
                       'puntaje; integre entrevista, observación, historia de tratamiento previo y factores '
                       'contextuales. El informe debe ser comprensible para el paciente sin perder rigor técnico ni '
                       'omitir recomendaciones accionables.</p>'}],
 'faqs': [{'q': '¿MMPI-2 o MMPI-2-RF?',
           'a': 'MMPI-2-RF es más breve y dimensional; MMPI-2 clásico sigue usándose donde hay tradición '
                'institucional. Elija según formación, software disponible y pregunta clínica.'},
          {'q': '¿Puede invalidarse un MMPI-2?',
           'a': 'Sí. Escalas de validez elevadas, ? excesivo o inconsistencia indican perfil no interpretable. '
                'Reaplicar o usar entrevista estructurada.'},
          {'q': '¿MMPI-2 en adolescentes?',
           'a': 'Use MMPI-A-RF para adolescentes. MMPI-2 adulto no es apropiado para menores.'},
          {'q': '¿Cuánto tarda la corrección?',
           'a': 'Con software autorizado, minutos; manualmente no es práctico. Invierta en plataforma legítima.'},
          {'q': '¿Se puede aplicar por internet?',
           'a': 'Solo plataformas seguras autorizadas con supervisión profesional. Evite versiones no oficiales sin '
                'control de validez.'}],
 'related': [{'href': '/articulos/mmpi-2-rf-test-personalidad.html', 'label': 'MMPI-2-RF personalidad'},
             {'href': '/articulos/cuestionario-16pf-personalidad.html', 'label': '16PF cuestionario personalidad'},
             {'href': '/articulos/como-interpretar-tests-psicologicos.html', 'label': 'Interpretar tests psicológicos'},
             {'href': '/articulos/nom-004-historia-clinica-mexico.html', 'label': 'NOM-004 historia clínica'}],
 'references': ['Butcher, J. N., Graham, J. R., Ben-Porath, Y. S., et al. (2001). <em>MMPI-2: Manual for '
                'Administration and Scoring</em>. University of Minnesota Press.',
                'Ben-Porath, Y. S., & Tellegen, A. (2008). <em>MMPI-2-RF Manual</em>. University of Minnesota Press.']}

def _art_test_inteligencia_adultos(p, table):
    return {'slug': 'test-de-inteligencia-adultos',
 'title': 'Test de inteligencia para adultos: WAIS-IV y gu&iacute;a cl&iacute;nica | Kalyo',
 'description': 'Tests de inteligencia para adultos: WAIS-IV, matrices y bater&iacute;as breves. Cu&aacute;ndo '
                'aplicarlos, interpretaci&oacute;n de CI y uso en evaluaci&oacute;n cl&iacute;nica en M&eacute;xico.',
 'keywords': 'test de inteligencia, WAIS-IV, evaluación cognitiva adultos, CI adultos, neuropsicología México',
 'h1': 'Test de inteligencia para adultos: guía clínica en México',
 'breadcrumb_short': 'Test inteligencia adultos',
 'quick_answer': 'El test de inteligencia para adultos más utilizado es la WAIS-IV, que evalúa comprensión verbal, '
                 'razonamiento perceptivo, memoria de trabajo y velocidad de procesamiento en personas de 16 a 90 '
                 'años. Baterías breves y matrices progresivas complementan cuando el tiempo o la condición médica '
                 'limitan evaluación completa. Siempre integre contexto educativo, médico y funcional.',
 'intro_long': 'La evaluación cognitiva en adultos se solicita por deterioro sospechado, rehabilitación '
               'neuropsicológica, orientación vocacional tardía o requerimientos periciales. Elegir el test de '
               'inteligencia adecuado y comunicar resultados con prudencia es competencia central del psicólogo '
               'clínico en México.',
 'test_name': 'WAIS-IV',
 'hero_alt': 'Evaluación WAIS-IV test de inteligencia en adulto en consultorio psicológico',
 'inline_alt': 'Comparativa de tests de inteligencia para adultos WAIS-IV y baterías breves',
 'sections': [{'h2': 'WAIS-IV: referente en test de inteligencia adultos',
               'html': '<p>La <strong>WAIS-IV</strong> (Wechsler Adult Intelligence Scale) genera CI Total e índices: '
                       'Comprensión Verbal, Razonamiento Perceptivo, Memoria de Trabajo y Velocidad de Procesamiento. '
                       'Aplicación presencial 60–90 minutos. Requiere certificación y materiales oficiales.</p>\n'
                       '<p>Relaciona con evaluación infantil en <a '
                       'href="/articulos/wisc-v-test-inteligencia-ninos.html">WISC-V</a> para continuidad '
                       'desarrolladora. En adultos mayores, considere efectos de fatiga, medicación y deterioro '
                       'sensorial sobre IVP.</p><table '
                       'class="items-table"><thead><tr><th>Instrumento</th><th>Edad</th><th>Uso '
                       'principal</th></tr></thead><tbody><tr><td>WAIS-IV</td><td>16–90</td><td>Evaluación integral '
                       'adultos</td></tr><tr><td>Matrices progresivas</td><td>Amplio rango</td><td>Tamizaje no '
                       'verbal</td></tr><tr><td>Baterías breves</td><td>Adultos</td><td>Screening cognitivo '
                       'médico</td></tr></tbody></table><p>Documente fecha, contexto de aplicación, versión del '
                       'instrumento y limitaciones cuando no existan baremos locales. La trazabilidad mejora '
                       'continuidad asistencial, supervisión clínica y comunicación con otros profesionales de la red '
                       'de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Indicaciones clínicas del test de inteligencia',
               'html': '<p>Sospecha de deterioro cognitivo leve, secuelas de TCE, esclerosis múltiple, esquizofrenia '
                       'con déficit cognitivo, discapacidad intelectual no diagnosticada en infancia, evaluación '
                       'prequirúrgica. Coordine con neurología cuando proceda.</p>\n'
                       '<p>En <a href="/articulos/evaluacion-neuropsicologica-guia-clinica.html">evaluación '
                       'neuropsicológica</a>, el test de inteligencia es núcleo pero insuficiente: añada memoria, '
                       'funciones ejecutivas y praxias.</p><p>Documente fecha, contexto de aplicación, versión del '
                       'instrumento y limitaciones cuando no existan baremos locales. La trazabilidad mejora '
                       'continuidad asistencial, supervisión clínica y comunicación con otros profesionales de la red '
                       'de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Baterías breves y matrices cuando el tiempo es limitado',
               'html': '<p>Hospitalización, fatiga severa o urgencia pericial pueden requerir screening con MoCA, MMSE '
                       '(limitado) o matrices Raven. Documente que no sustituyen WAIS-IV completa.</p>\n'
                       '<p>Matrices reducen sesgo verbal en migrantes recientes o baja escolaridad, pero no capturan '
                       'perfil completo. Interprete conservadoramente.</p><p>Documente fecha, contexto de aplicación, '
                       'versión del instrumento y limitaciones cuando no existan baremos locales. La trazabilidad '
                       'mejora continuidad asistencial, supervisión clínica y comunicación con otros profesionales de '
                       'la red de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Interpretación del CI en contexto mexicano',
               'html': '<p>Reporte intervalos de confianza, no un número único determinista. Integre años de '
                       'escolaridad, ocupación previa, calidad de sueño y depresión comórbida (tamice con <a '
                       'href="/articulos/que-es-el-phq-9.html">PHQ-9</a>).</p>\n'
                       '<p>Evite conclusiones sobre capacidad legal sin evaluación específica de competencia. El CI no '
                       'mide creatividad, inteligencia emocional ni sabiduría práctica.</p><p>Documente fecha, '
                       'contexto de aplicación, versión del instrumento y limitaciones cuando no existan baremos '
                       'locales. La trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación '
                       'con otros profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme '
                       'identidad del evaluado, condiciones de privacidad y comprensión de instrucciones antes de '
                       'puntuar. Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja '
                       'escolaridad o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo '
                       'puntaje; integre entrevista, observación, historia de tratamiento previo y factores '
                       'contextuales. El informe debe ser comprensible para el paciente sin perder rigor técnico ni '
                       'omitir recomendaciones accionables.</p><p>Revise coherencia entre síntomas reportados, '
                       'conducta observada en sesión e informes de terceros cuando estén disponibles. Las '
                       'discrepancias orientan exploración adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Informes y recomendaciones funcionales',
               'html': '<p>Traduzca resultados a apoyos: memoria externa, rutinas, adaptaciones laborales, '
                       'rehabilitación cognitiva. Consulte <a '
                       'href="/articulos/como-interpretar-tests-psicologicos.html">cómo interpretar tests '
                       'psicológicos</a> al redactar.</p>\n'
                       '<p>Registre en expediente conforme a <a '
                       'href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a>. Use <a '
                       'href="https://app.kalyo.io/register">Kalyo</a> para archivo seguro de puntajes e '
                       'informes.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite '
                       'conclusiones categóricas basadas en un solo puntaje; integre entrevista, observación, historia '
                       'de tratamiento previo y factores contextuales. El informe debe ser comprensible para el '
                       'paciente sin perder rigor técnico ni omitir recomendaciones accionables.</p><p>Revise '
                       'coherencia entre síntomas reportados, conducta observada en sesión e informes de terceros '
                       'cuando estén disponibles. Las discrepancias orientan exploración adicional, no descalificación '
                       'automática del paciente.</p>'},
              {'h2': 'Ética, derechos de autor y reevaluación',
               'html': '<p>Respete copyright Pearson. Obtenga consentimiento informado explicando propósito y límites. '
                       'Reevalúe según condición: anual en deterioro progresivo, más espaciado en adultos jóvenes '
                       'estables.</p>\n'
                       '<p>En peritajes, declare conflictos de interés y métodos. Supervisión cruzada recomendable en '
                       'casos forenses de alto impacto.</p><p>Documente fecha, contexto de aplicación, versión del '
                       'instrumento y limitaciones cuando no existan baremos locales. La trazabilidad mejora '
                       'continuidad asistencial, supervisión clínica y comunicación con otros profesionales de la red '
                       'de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p>'}],
 'faqs': [{'q': '¿WAIS-IV desde qué edad?',
           'a': '16 años en adelante. Entre 6 y 16 use WISC-V. En límites etarios, elige instrumento según madurez y '
                'manual.'},
          {'q': '¿Test de inteligencia en línea es válido?',
           'a': 'Tests recreativos en internet no son WAIS-IV. Evaluación clínica requiere administración '
                'estandarizada presencial.'},
          {'q': '¿Depresión baja el CI?',
           'a': 'Puede reducir memoria de trabajo y velocidad de procesamiento transitoriamente. Trate comorbilidad '
                'antes de concluir deterioro permanente.'},
          {'q': '¿Cuándo usar matrices Raven?',
           'a': 'Tamizaje no verbal, barrera idiomática o complemento cuando ICV no es interpretable. No reemplaza '
                'WAIS completa en evaluación clínica profunda.'},
          {'q': '¿Validez del informe de inteligencia?',
           'a': 'Depende de contexto: 1–2 años en adultos jóvenes estables; reevaluación más frecuente en deterioro '
                'neurológico progresivo.'}],
 'related': [{'href': '/articulos/wisc-v-test-inteligencia-ninos.html', 'label': 'WISC-V niños'},
             {'href': '/articulos/evaluacion-neuropsicologica-guia-clinica.html',
              'label': 'Evaluación neuropsicológica'},
             {'href': '/articulos/que-es-el-phq-9.html', 'label': 'PHQ-9 depresión'},
             {'href': '/articulos/como-interpretar-tests-psicologicos.html',
              'label': 'Interpretar tests psicológicos'}],
 'references': ['Wechsler, D. (2008). <em>WAIS-IV: Escala de Inteligencia de Wechsler para Adultos</em>. Manual '
                'técnico. Pearson.',
                'Lezak, M. D., Howieson, D. B., Bigler, E. D., & Tranel, D. (2012). <em>Neuropsychological '
                'Assessment</em> (5th ed.). Oxford University Press.']}

def _art_16pf(p, table):
    return {'slug': '16pf-cuestionario-personalidad',
 'title': '16PF test: cuestionario de personalidad Cattell en M&eacute;xico | Kalyo',
 'description': '16PF test: cuestionario Cattell, factores primarios e interpretaci&oacute;n en selecci&oacute;n y '
                'cl&iacute;nica. Gu&iacute;a psicom&eacute;trica para psic&oacute;logos en M&eacute;xico con enfoque '
                'riguroso.',
 'keywords': '16PF test, cuestionario 16PF, personalidad Cattell, evaluación personalidad México, psicometría '
             'organizacional',
 'h1': '16PF test: cuestionario de personalidad — guía para psicólogos',
 'breadcrumb_short': '16PF test personalidad',
 'quick_answer': 'El 16PF test evalúa dieciséis factores primarios de personalidad de Cattell mediante autoinforme, '
                 'útil en orientación vocacional, selección de personal y psicoterapia cuando se busca perfil de '
                 'rasgos estables. Los factores incluyen calidez, razonamiento, estabilidad emocional, dominancia y '
                 'autodisciplina. Requiere interpretación por estenotypes y congruencia con entrevista.',
 'intro_long': 'El cuestionario 16PF ocupa un lugar histórico en psicometría de personalidad por su modelo factorial. '
               'En México se emplea en recursos humanos y consulta clínica para perfilar estilos interpersonales. Esta '
               'guía detalla factores, interpretación prudente y diferencias con inventarios clínicos como el MMPI-2.',
 'test_name': '16PF',
 'hero_alt': 'Gráfico de factores primarios del 16PF test de personalidad Cattell',
 'inline_alt': 'Tabla de factores primarios del 16PF test cuestionario de personalidad',
 'sections': [{'h2': 'Modelo factorial del 16PF test',
               'html': '<p>El <strong>16PF test</strong> mide factores primarios: Afabilidad (A), Razonamiento (B), '
                       'Estabilidad (C), Dominancia (E), Expresividad (F), Regulación (G), Atrevimiento (H), '
                       'Sensibilidad (I), Vigilancia (L), Abstracción (M), Privacidad (N), Aprensión (O), Apertura al '
                       'cambio (Q1), Autocontrol (Q2), Tensión (Q3) y Vitalidad (Q4). Segunda orden agrupa en cinco '
                       'dimensiones globales.</p>\n'
                       '<p>Compare con <a href="/articulos/cuestionario-16pf-personalidad.html">cuestionario 16PF '
                       'personalidad</a> introductorio. A diferencia del <a '
                       'href="/articulos/mmpi-2-rf-test-personalidad.html">MMPI-2-RF</a>, el 16PF enfatiza rasgos '
                       'normativos más que psicopatología.</p><table '
                       'class="items-table"><thead><tr><th>Factor</th><th>Polo bajo</th><th>Polo '
                       'alto</th></tr></thead><tbody><tr><td>C Estabilidad</td><td>Reactivo '
                       'emocional</td><td>Emocionalmente estable</td></tr><tr><td>E '
                       'Dominancia</td><td>Deferente</td><td>Dominante, assertivo</td></tr><tr><td>G '
                       'Regulación</td><td>Flexible, impulsivo</td><td>Regulado, '
                       'consciente</td></tr></tbody></table><p>Documente fecha, contexto de aplicación, versión del '
                       'instrumento y limitaciones cuando no existan baremos locales. La trazabilidad mejora '
                       'continuidad asistencial, supervisión clínica y comunicación con otros profesionales de la red '
                       'de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Administración y puntuación por estenotypes',
               'html': '<p>Autoadministrado, 35–50 minutos según versión. Puntuación en estenotypes (1–10) con media '
                       '5.5 y desviación estándar 2. Evite interpretar un factor aislado; analice patrón '
                       'configuracional.</p>\n'
                       '<p>Revise validez de respuesta si la versión incluye escalas de consistencia. En selección, '
                       'combine con entrevista estructurada y pruebas de competencia.</p><p>Documente fecha, contexto '
                       'de aplicación, versión del instrumento y limitaciones cuando no existan baremos locales. La '
                       'trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación con otros '
                       'profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme identidad '
                       'del evaluado, condiciones de privacidad y comprensión de instrucciones antes de puntuar. '
                       'Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad '
                       'o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'},
              {'h2': '16PF en selección y orientación vocacional',
               'html': '<p>Recursos humanos usan 16PF para perfilar liderazgo, trabajo en equipo o tolerancia al '
                       'estrés. Debe cumplir no discriminación y consentimiento informado del candidato.</p>\n'
                       '<p>Orientación vocacional vincula factores con intereses RIASEC y habilidades académicas. No '
                       'predice éxito por sí solo.</p><p>Documente fecha, contexto de aplicación, versión del '
                       'instrumento y limitaciones cuando no existan baremos locales. La trazabilidad mejora '
                       'continuidad asistencial, supervisión clínica y comunicación con otros profesionales de la red '
                       'de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Uso clínico del 16PF test',
               'html': '<p>En psicoterapia, perfila estilos interpersonales (dominancia vs. deferencia, apertura '
                       'emocional). Complementa entrevista; no sustituye evaluación de psicopatología cuando hay '
                       'sospecha de trastorno grave.</p>\n'
                       '<p>Integre con <a href="/articulos/stai-ansiedad-estado-rasgo.html">STAI</a> o <a '
                       'href="/articulos/que-es-el-phq-9.html">PHQ-9</a> si hay síntomas emocionales '
                       'actuales.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite '
                       'conclusiones categóricas basadas en un solo puntaje; integre entrevista, observación, historia '
                       'de tratamiento previo y factores contextuales. El informe debe ser comprensible para el '
                       'paciente sin perder rigor técnico ni omitir recomendaciones accionables.</p><p>Revise '
                       'coherencia entre síntomas reportados, conducta observada en sesión e informes de terceros '
                       'cuando estén disponibles. Las discrepancias orientan exploración adicional, no descalificación '
                       'automática del paciente.</p>'},
              {'h2': 'Interpretación y comunicación de resultados',
               'html': '<p>Describa factores en lenguaje conductual observable. Evite determinismo («usted es '
                       'introvertido y no servirá para ventas»). Enfatice flexibilidad situacional.</p>\n'
                       '<p>Consulte <a href="/articulos/como-interpretar-tests-psicologicos.html">cómo interpretar '
                       'tests psicológicos</a>. Archive perfiles en <a href="https://app.kalyo.io/register">Kalyo</a> '
                       'con consentimiento.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite '
                       'conclusiones categóricas basadas en un solo puntaje; integre entrevista, observación, historia '
                       'de tratamiento previo y factores contextuales. El informe debe ser comprensible para el '
                       'paciente sin perder rigor técnico ni omitir recomendaciones accionables.</p><p>Revise '
                       'coherencia entre síntomas reportados, conducta observada en sesión e informes de terceros '
                       'cuando estén disponibles. Las discrepancias orientan exploración adicional, no descalificación '
                       'automática del paciente.</p>'},
              {'h2': 'Limitaciones y baremos en México',
               'html': '<p>Verifique manual en español y muestra normativa. Sin baremos locales, documente cautela. '
                       'Sesgo de deseabilidad social puede elevar G Regulación artificialmente.</p>\n'
                       '<p>No use 16PF como único criterio en decisiones de alto impacto (despido, custodia). '
                       'Supervisión ética en contextos organizacionales.</p><p>Documente fecha, contexto de '
                       'aplicación, versión del instrumento y limitaciones cuando no existan baremos locales. La '
                       'trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación con otros '
                       'profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme identidad '
                       'del evaluado, condiciones de privacidad y comprensión de instrucciones antes de puntuar. '
                       'Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad '
                       'o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'}],
 'faqs': [{'q': '¿16PF test mide trastornos mentales?',
           'a': 'No está diseñado para psicopatología. Para clínica forense o grave, prefiera MMPI-2-RF u otro '
                'inventario clínico.'},
          {'q': '¿Qué versión del 16PF usar?',
           'a': 'Consulte editor autorizado (5ª edición u actual). Evite versiones abreviadas no validadas para su '
                'objetivo.'},
          {'q': '¿16PF en adolescentes?',
           'a': 'Existen versiones específicas; no aplique adulto en menores sin manual apropiado.'},
          {'q': '¿Cómo leer estenotypes?',
           'a': '1–3 bajo, 4–7 promedio, 8–10 alto respecto a norma. Interprete patrón, no un solo número.'},
          {'q': '¿Puedo dar feedback al candidato?',
           'a': 'En selección, depende de política de empresa y legislación laboral. En clínica, la devolución es '
                'parte ética del proceso.'}],
 'related': [{'href': '/articulos/cuestionario-16pf-personalidad.html', 'label': 'Cuestionario 16PF'},
             {'href': '/articulos/mmpi-2-rf-test-personalidad.html', 'label': 'MMPI-2-RF'},
             {'href': '/articulos/como-interpretar-tests-psicologicos.html', 'label': 'Interpretar tests'},
             {'href': '/articulos/stai-ansiedad-estado-rasgo.html', 'label': 'STAI ansiedad'}],
 'references': ['Cattell, H. E. P., & Mead, A. D. (2008). The Sixteen Personality Factor Questionnaire (16PF). In G. '
                'J. Boyle et al. (Eds.), <em>The SAGE Handbook of Personality Theory and Assessment</em>. SAGE.',
                "Russell, M. T., & Karol, D. L. (2002). <em>16PF Fifth Edition Administrator's Manual</em>. IPAT."]}

def _art_historia_clinica(p, table):
    return {'slug': 'historia-clinica-psicologica-formato',
 'title': 'Historia cl&iacute;nica psicol&oacute;gica: formato NOM-004 en M&eacute;xico | Kalyo',
 'description': 'Formato de historia cl&iacute;nica psicol&oacute;gica conforme NOM-004: contenido m&iacute;nimo, '
                'notas SOAP, confidencialidad y registro digital seguro en consulta privada.',
 'keywords': 'historia clínica psicológica, NOM-004, expediente clínico, notas SOAP, registro digital psicología '
             'México',
 'h1': 'Historia clínica psicológica: formato y registro conforme NOM-004',
 'breadcrumb_short': 'Historia clínica psicológica',
 'quick_answer': 'La historia clínica psicológica es el registro sistemático de identificación, motivo de consulta, '
                 'antecedentes, evaluación, diagnóstico, plan de tratamiento y evolución. En México, la NOM-004 define '
                 'contenido mínimo del expediente clínico. Debe garantizar confidencialidad, legibilidad, trazabilidad '
                 'y acceso restringido al equipo tratante autorizado.',
 'intro_long': 'Una historia clínica psicológica bien estructurada protege al paciente, al profesional y a la '
               'continuidad asistencial. En consulta privada mexicana, cumplir NOM-004 no es opcional: define qué '
               'registrar, cómo conservar documentos y cuándo compartir información. Esta guía ofrece formato práctico '
               'integrando psicometría y notas SOAP.',
 'test_name': 'historia clínica psicológica',
 'hero_alt': 'Psicóloga documentando historia clínica psicológica digital en consultorio mexicano',
 'inline_alt': 'Esquema de secciones del formato de historia clínica psicológica NOM-004',
 'quick_action': {'href': '/assets/downloads/formato-historia-clinica-psicologica-kalyo.pdf',
                  'label': 'Descargar formato PDF historia clínica psicológica',
                  'download': 'formato-historia-clinica-psicologica-kalyo.pdf'},
 'sections': [{'h2': 'Contenido mínimo según NOM-004',
               'html': '<p>La <strong>historia clínica psicológica</strong> debe incluir: identificación del paciente, '
                       'motivo de consulta, antecedentes heredo-familiares y personales, exploración psicológica '
                       '(entrevista, tests aplicados), diagnósticos o hipótesis, plan terapéutico, evolución y notas '
                       'de sesión. Consulte la guía <a href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004 '
                       'historia clínica México</a> para detalle normativo.</p>\n'
                       '<p>Incluya fecha, firma o identificación electrónica del profesional y número de cédula. Evite '
                       'almacenar datos en apps de mensajería sin cifrado.</p><table '
                       'class="items-table"><thead><tr><th>Sección</th><th>Contenido '
                       'esencial</th></tr></thead><tbody><tr><td>Identificación</td><td>Nombre, edad, contacto, '
                       'referencia</td></tr><tr><td>Motivo consulta</td><td>En palabras del paciente y '
                       'clínico</td></tr><tr><td>Evaluación</td><td>Entrevista, escalas, '
                       'observación</td></tr><tr><td>Plan</td><td>Objetivos, frecuencia, '
                       'derivaciones</td></tr><tr><td>Evolución</td><td>Notas SOAP '
                       'seriadas</td></tr></tbody></table><p>Documente fecha, contexto de aplicación, versión del '
                       'instrumento y limitaciones cuando no existan baremos locales. La trazabilidad mejora '
                       'continuidad asistencial, supervisión clínica y comunicación con otros profesionales de la red '
                       'de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Notas SOAP en psicología clínica',
               'html': '<p>SOAP estructura cada nota de sesión: Subjetivo (relato paciente), Objetivo (observación, '
                       'escalas como <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a> o <a '
                       'href="/articulos/que-es-el-gad-7.html">GAD-7</a>), Assessment (formulación clínica) y Plan '
                       '(intervenciones, tareas, próxima cita).</p>\n'
                       '<p>Redacte notas contemporáneas (misma sesión o inmediatamente después). Evite jerga '
                       'incomprensible para auditorías o continuidad con otro colega.</p><p>Documente fecha, contexto '
                       'de aplicación, versión del instrumento y limitaciones cuando no existan baremos locales. La '
                       'trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación con otros '
                       'profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme identidad '
                       'del evaluado, condiciones de privacidad y comprensión de instrucciones antes de puntuar. '
                       'Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad '
                       'o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Integrar resultados de tests psicológicos',
               'html': '<p>Registre nombre del test, fecha, puntajes clave e interpretación clínica resumida. No copie '
                       'ítems con copyright. Vincule hallazgos con plan terapéutico.</p>\n'
                       '<p>Use <a href="/articulos/tests-psicologicos-digitales.html">tests psicológicos digitales</a> '
                       'que exporten a expediente. Consulte <a '
                       'href="/articulos/como-interpretar-tests-psicologicos.html">cómo interpretar tests '
                       'psicológicos</a> al documentar.</p><p>Documente fecha, contexto de aplicación, versión del '
                       'instrumento y limitaciones cuando no existan baremos locales. La trazabilidad mejora '
                       'continuidad asistencial, supervisión clínica y comunicación con otros profesionales de la red '
                       'de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Confidencialidad y acceso al expediente',
               'html': '<p>El paciente puede solicitar copia conforme a ley. Divulgación a terceros requiere '
                       'consentimiento escrito excepto urgencias o mandatos legales. Menores: consentimiento de '
                       'tutores según normativa.</p>\n'
                       '<p>Contraseñas fuertes, respaldo cifrado y política de retención (años mínimos según NOM). '
                       'Elimine datos obsoletos según procedimiento legal, no arbitrariamente.</p><p>Documente fecha, '
                       'contexto de aplicación, versión del instrumento y limitaciones cuando no existan baremos '
                       'locales. La trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación '
                       'con otros profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme '
                       'identidad del evaluado, condiciones de privacidad y comprensión de instrucciones antes de '
                       'puntuar. Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja '
                       'escolaridad o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo '
                       'puntaje; integre entrevista, observación, historia de tratamiento previo y factores '
                       'contextuales. El informe debe ser comprensible para el paciente sin perder rigor técnico ni '
                       'omitir recomendaciones accionables.</p><p>Revise coherencia entre síntomas reportados, '
                       'conducta observada en sesión e informes de terceros cuando estén disponibles. Las '
                       'discrepancias orientan exploración adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Historia clínica digital segura',
               'html': '<p>Migrar de papel a digital reduce pérdida de archivos y facilita gráficas de escalas '
                       'seriadas. Verifique que el proveedor cumpla confidencialidad y residencia de datos '
                       'aceptable.</p>\n'
                       '<p>Centralice en <a href="https://app.kalyo.io/register">Kalyo</a> para administrar tests, '
                       'notas SOAP y recordatorios en un solo expediente con control de acceso.</p><p>Documente fecha, '
                       'contexto de aplicación, versión del instrumento y limitaciones cuando no existan baremos '
                       'locales. La trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación '
                       'con otros profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme '
                       'identidad del evaluado, condiciones de privacidad y comprensión de instrucciones antes de '
                       'puntuar. Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja '
                       'escolaridad o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo '
                       'puntaje; integre entrevista, observación, historia de tratamiento previo y factores '
                       'contextuales. El informe debe ser comprensible para el paciente sin perder rigor técnico ni '
                       'omitir recomendaciones accionables.</p><p>Revise coherencia entre síntomas reportados, '
                       'conducta observada en sesión e informes de terceros cuando estén disponibles. Las '
                       'discrepancias orientan exploración adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Errores frecuentes y auditoría clínica',
               'html': '<p>Errores: notas genéricas repetidas, falta de plan medible, no registrar riesgo suicida '
                       'evaluado, mezclar opinión personal con dato clínico. Revise expedientes trimestralmente en '
                       'supervisión.</p>\n'
                       '<p>Ante demanda legal, historial incompleto perjudica defensa profesional. La historia clínica '
                       'psicológica es evidencia de estándar de cuidado.</p><p>Documente fecha, contexto de '
                       'aplicación, versión del instrumento y limitaciones cuando no existan baremos locales. La '
                       'trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación con otros '
                       'profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme identidad '
                       'del evaluado, condiciones de privacidad y comprensión de instrucciones antes de puntuar. '
                       'Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad '
                       'o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p>'}],
 'faqs': [{'q': '¿Es obligatoria la NOM-004 en consulta privada?',
           'a': 'Sí, aplica al expediente clínico en general incluyendo psicología. El incumplimiento puede tener '
                'consecuencias administrativas y legales.'},
          {'q': '¿Cuánto tiempo conservar la historia clínica?',
           'a': 'Consulte NOM vigente; típicamente años mínimos desde última atención. No destruya antes del plazo '
                'legal.'},
          {'q': '¿Puedo usar WhatsApp como expediente?',
           'a': 'No es recomendable ni seguro. Use plataforma clínica con cifrado y respaldo.'},
          {'q': '¿Qué incluir si solo hago evaluación única?',
           'a': 'Motivo, procedimiento, resultados, limitaciones, recomendaciones y derivaciones. Cierre formal del '
                'proceso evaluativo.'},
          {'q': '¿SOAP en cada sesión?',
           'a': 'Idealmente sí, aunque breve. Documenta evolución y justifica continuidad o alta.'}],
 'related': [{'href': '/articulos/nom-004-historia-clinica-mexico.html', 'label': 'NOM-004 México'},
             {'href': '/articulos/tests-psicologicos-digitales.html', 'label': 'Tests digitales'},
             {'href': '/articulos/como-interpretar-tests-psicologicos.html', 'label': 'Interpretar tests'},
             {'href': '/articulos/que-es-el-phq-9.html', 'label': 'PHQ-9 en expediente'}],
 'references': ['Secretaría de Salud (2012). <em>Norma Oficial Mexicana NOM-004-SSA3-2012</em>, Del expediente '
                'clínico. Diario Oficial de la Federación.',
                'American Psychological Association (2017). <em>Ethical Principles of Psychologists and Code of '
                'Conduct</em>. APA.']}

def _art_mbi(p, table):
    return {'slug': 'maslach-burnout-inventory-mbi',
 'title': 'Maslach Burnout Inventory: gu&iacute;a MBI para psic&oacute;logos | Kalyo',
 'description': 'Maslach Burnout Inventory: dimensiones, puntuaci&oacute;n e interpretaci&oacute;n del burnout '
                'laboral. Gu&iacute;a para psic&oacute;logos organizacionales y de salud mental en M&eacute;xico.',
 'keywords': 'Maslach burnout inventory, MBI, burnout laboral, agotamiento emocional, psicología organizacional México',
 'h1': 'Maslach Burnout Inventory (MBI): interpretación clínica y organizacional',
 'breadcrumb_short': 'Maslach Burnout Inventory',
 'quick_answer': 'El Maslach Burnout Inventory (MBI) mide burnout laboral en tres dimensiones: agotamiento emocional, '
                 'despersonalización y realización personal reducida. Es el instrumento más validado en profesiones de '
                 'ayuda, incluida psicología clínica y enfermería. Los puntajes altos en agotamiento y '
                 'despersonalización con baja realización personal sugieren síndrome de burnout significativo.',
 'intro_long': 'El burnout laboral creció como motivo de consulta en México tras pandemia y teletrabajo. El Maslach '
               'Burnout Inventory permite cuantificar severidad y orientar intervenciones individuales y '
               'organizacionales. Esta guía detalla dimensiones, versiones y uso ético en empresas y clínica.',
 'test_name': 'MBI',
 'hero_alt': 'Profesional de salud completando Maslach Burnout Inventory en evaluación laboral',
 'inline_alt': 'Dimensiones del Maslach Burnout Inventory MBI agotamiento y despersonalización',
 'sections': [{'h2': 'Dimensiones del Maslach Burnout Inventory',
               'html': '<p>El <strong>Maslach Burnout Inventory</strong> evalúa: <em>Agotamiento emocional</em> '
                       '(fatiga por demanda interpersonal), <em>despersonalización</em> (actitudes cínicas o distantes '
                       'hacia usuarios/clientes) y <em>realización personal</em> (competencia y satisfacción en el '
                       'trabajo; puntuaciones bajas indican problema).</p>\n'
                       '<p>Existen versiones MBI-HSS (servicios humanos), MBI-GS (general) y MBI-ES (educadores). '
                       'Elija según población. Relaciona con artículo <a '
                       'href="/articulos/burnout-laboral.html">burnout laboral</a> para contexto.</p><table '
                       'class="severity-table"><thead><tr><th>Puntuaci&oacute;n</th><th>Severidad</th><th>Acci&oacute;n '
                       'cl&iacute;nica</th></tr></thead><tbody><tr><td><span class="score-badge">Bajo en '
                       'EE/DP/DPA</span></td><td><strong>Sin burnout cl&iacute;nico</strong></td><td>Prevenci&oacute;n '
                       'y monitoreo anual.</td></tr><tr><td><span '
                       'class="score-badge">Moderado</span></td><td><strong>Riesgo '
                       'moderado</strong></td><td>Intervenciones organizacionales y '
                       'individuales.</td></tr><tr><td><span class="score-badge">Alto en &ge;1 '
                       'dimensi&oacute;n</span></td><td><strong>Burnout significativo</strong></td><td>Plan de '
                       'intervenci&oacute;n; evaluar licencia.</td></tr></tbody></table><p>Documente fecha, contexto '
                       'de aplicación, versión del instrumento y limitaciones cuando no existan baremos locales. La '
                       'trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación con otros '
                       'profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme identidad '
                       'del evaluado, condiciones de privacidad y comprensión de instrucciones antes de puntuar. '
                       'Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad '
                       'o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Administración y puntuación',
               'html': '<p>Autoadministrado, frecuencia Likert 0–6 (nunca a todos los días). Calcule medias o sumas '
                       'por subescala según manual. Compare con puntos de corte normativos del manual para su '
                       'versión.</p>\n'
                       '<p>Aplique en evaluación organizacional baseline y post-intervención (6–12 meses). '
                       'Confidencialidad individual vs. reporte agregado al empleador debe acordarse por '
                       'escrito.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y limitaciones '
                       'cuando no existan baremos locales. La trazabilidad mejora continuidad asistencial, supervisión '
                       'clínica y comunicación con otros profesionales de la red de salud mental en México.</p><p>En '
                       'telepsicología, confirme identidad del evaluado, condiciones de privacidad y comprensión de '
                       'instrucciones antes de puntuar. Registre interrupciones, apoyo de terceros o necesidad de '
                       'oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite conclusiones categóricas '
                       'basadas en un solo puntaje; integre entrevista, observación, historia de tratamiento previo y '
                       'factores contextuales. El informe debe ser comprensible para el paciente sin perder rigor '
                       'técnico ni omitir recomendaciones accionables.</p><p>Revise coherencia entre síntomas '
                       'reportados, conducta observada en sesión e informes de terceros cuando estén disponibles. Las '
                       'discrepancias orientan exploración adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'MBI vs. otras escalas de estrés laboral',
               'html': '<p>La <a href="/articulos/escala-dass-21.html">DASS-21</a> mide depresión, ansiedad y estrés '
                       'general, no burnout específico. MBI es preferible cuando la pregunta es agotamiento '
                       'profesional en contexto de cuidado.</p>\n'
                       '<p>Combine con entrevista sobre carga horaria, conflicto rol, falta de control y apoyo '
                       'supervisor. No culpabilice al trabajador por factores organizacionales.</p><p>Documente fecha, '
                       'contexto de aplicación, versión del instrumento y limitaciones cuando no existan baremos '
                       'locales. La trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación '
                       'con otros profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme '
                       'identidad del evaluado, condiciones de privacidad y comprensión de instrucciones antes de '
                       'puntuar. Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja '
                       'escolaridad o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo '
                       'puntaje; integre entrevista, observación, historia de tratamiento previo y factores '
                       'contextuales. El informe debe ser comprensible para el paciente sin perder rigor técnico ni '
                       'omitir recomendaciones accionables.</p><p>Revise coherencia entre síntomas reportados, '
                       'conducta observada en sesión e informes de terceros cuando estén disponibles. Las '
                       'discrepancias orientan exploración adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Interpretación clínica en profesionales de salud mental',
               'html': '<p>Psicólogos con burnout pueden mostrar cinismo hacia pacientes, errores de empathic fatigue '
                       'y riesgo de abandono profesional. Intervención incluye límites de carga, supervisión, '
                       'autocompasión y revisión de casos.</p>\n'
                       '<p>Tamice depresión comórbida con <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a>. Burnout '
                       'y depresión mayor pueden coexistir; el plan difiere si hay síntomas endógenos.</p><p>Documente '
                       'fecha, contexto de aplicación, versión del instrumento y limitaciones cuando no existan '
                       'baremos locales. La trazabilidad mejora continuidad asistencial, supervisión clínica y '
                       'comunicación con otros profesionales de la red de salud mental en México.</p><p>En '
                       'telepsicología, confirme identidad del evaluado, condiciones de privacidad y comprensión de '
                       'instrucciones antes de puntuar. Registre interrupciones, apoyo de terceros o necesidad de '
                       'oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite conclusiones categóricas '
                       'basadas en un solo puntaje; integre entrevista, observación, historia de tratamiento previo y '
                       'factores contextuales. El informe debe ser comprensible para el paciente sin perder rigor '
                       'técnico ni omitir recomendaciones accionables.</p><p>Revise coherencia entre síntomas '
                       'reportados, conducta observada en sesión e informes de terceros cuando estén disponibles. Las '
                       'discrepancias orientan exploración adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Intervenciones basadas en resultados MBI',
               'html': '<p>Individual: TCC, mindfulness, reestructuración de expectativas, higiene laboral. '
                       'Organizacional: redistribución de carga, pausas, liderazgo transformacional, políticas '
                       'anti-acoso.</p>\n'
                       '<p>Reevalúe MBI tras intervención. Documente en expediente ocupacional o clínico según '
                       'contexto. Use <a href="https://app.kalyo.io/register">Kalyo</a> para seguimiento seriado en '
                       'consulta privada.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite '
                       'conclusiones categóricas basadas en un solo puntaje; integre entrevista, observación, historia '
                       'de tratamiento previo y factores contextuales. El informe debe ser comprensible para el '
                       'paciente sin perder rigor técnico ni omitir recomendaciones accionables.</p><p>Revise '
                       'coherencia entre síntomas reportados, conducta observada en sesión e informes de terceros '
                       'cuando estén disponibles. Las discrepancias orientan exploración adicional, no descalificación '
                       'automática del paciente.</p>'},
              {'h2': 'Ética en evaluación organizacional',
               'html': '<p>Informe al evaluado propósito, quién verá resultados y límites de confidencialidad. No use '
                       'MBI como único criterio de despido. Respete copyright Mind Garden.</p>\n'
                       '<p>Consulte <a href="/articulos/como-interpretar-tests-psicologicos.html">cómo interpretar '
                       'tests psicológicos</a> al redactar informes para RRHH.</p><p>Documente fecha, contexto de '
                       'aplicación, versión del instrumento y limitaciones cuando no existan baremos locales. La '
                       'trazabilidad mejora continuidad asistencial, supervisión clínica y comunicación con otros '
                       'profesionales de la red de salud mental en México.</p><p>En telepsicología, confirme identidad '
                       'del evaluado, condiciones de privacidad y comprensión de instrucciones antes de puntuar. '
                       'Registre interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad '
                       'o fatiga atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'}],
 'faqs': [{'q': '¿MBI diagnostica depresión?',
           'a': 'No. Mide burnout laboral. Depresión requiere evaluación clínica adicional con entrevista y escalas '
                'específicas.'},
          {'q': '¿Qué versión MBI usar?',
           'a': 'MBI-HSS para servicios humanos y clínicos; MBI-GS para otros empleos. Consulte manual.'},
          {'q': '¿Puntos de corte universales?',
           'a': 'Varían por versión y norma. Use baremos oficiales, no cortes arbitrarios de internet.'},
          {'q': '¿MBI anónimo en empresas?',
           'a': 'Recomendable para honestidad. Reporte solo datos agregados si n < umbral que identifique personas.'},
          {'q': '¿Cada cuánto repetir MBI?',
           'a': 'Anual en monitoreo organizacional; 3–6 meses post-intervención clínica individual.'}],
 'related': [{'href': '/articulos/burnout-laboral.html', 'label': 'Burnout laboral'},
             {'href': '/articulos/escala-dass-21.html', 'label': 'DASS-21 estrés'},
             {'href': '/articulos/que-es-el-phq-9.html', 'label': 'PHQ-9 depresión'},
             {'href': '/articulos/como-interpretar-tests-psicologicos.html', 'label': 'Interpretar tests'}],
 'references': ['Maslach, C., Jackson, S. E., & Leiter, M. P. (1996). <em>Maslach Burnout Inventory Manual</em> (3rd '
                'ed.). Consulting Psychologists Press.',
                'Maslach, C., & Leiter, M. P. (2016). Understanding the burnout experience. <em>World Psychiatry</em>, '
                '15(2), 103–111.']}

def _art_bdi(p, table):
    return {'slug': 'bdi-inventario-depresion-beck',
 'title': 'BDI test Beck: inventario de depresi&oacute;n cl&iacute;nica | Kalyo',
 'description': 'BDI test Beck: versiones, puntajes, sensibilidad al cambio e integraci&oacute;n con PHQ-9. '
                'Gu&iacute;a para tamizaje e intervenci&oacute;n en depresi&oacute;n para psic&oacute;logos en '
                'M&eacute;xico.',
 'keywords': 'BDI test, BDI-II, inventario depresión Beck, escala depresión, tamizaje depresión México',
 'h1': 'BDI test Beck: inventario de depresión — guía clínica',
 'breadcrumb_short': 'BDI test Beck',
 'quick_answer': 'El BDI test (Beck Depression Inventory) en su versión BDI-II es un autorreporte de 21 ítems que '
                 'cuantifica severidad depresiva en las últimas dos semanas. Es ampliamente usado en investigación y '
                 'clínica por sensibilidad al cambio terapéutico. Complementa el PHQ-9 cuando se requiere perfil '
                 'sintomático detallado para psicoterapia cognitiva.',
 'intro_long': 'El inventario de depresión Beck es uno de los instrumentos más reconocidos mundialmente. En México, '
               'psicólogos lo aplican en consulta privada, hospitales universitarios y estudios de outcome. Esta guía '
               'orienta sobre versiones, puntuación, integración con PHQ-9 y registro clínico.',
 'test_name': 'BDI-II',
 'hero_alt': 'Paciente completando BDI test inventario de depresión Beck en consulta',
 'inline_alt': 'Tabla de severidad del BDI test Beck inventario de depresión',
 'sections': [{'h2': 'Versiones del BDI test: BDI-I vs. BDI-II',
               'html': '<p>El <strong>BDI test</strong> original (BDI-I, 1961) reflejaba constructos depresivos '
                       'clásicos; el <strong>BDI-II</strong> (1996) actualiza criterios DSM-IV/5, incluye cambios de '
                       'peso y enfatiza últimas dos semanas. Use BDI-II salvo requisito de investigación '
                       'histórica.</p>\n'
                       '<p>Compare con <a href="/articulos/inventario-depresion-beck-bdi.html">inventario depresión '
                       'Beck BDI</a> y la guía <a href="/articulos/escala-de-beck-bdi-ii.html">escala de Beck '
                       'BDI-II</a> para profundización. El <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a> es '
                       'alternativa breve para atención primaria.</p><p>Documente fecha, contexto de aplicación, '
                       'versión del instrumento y limitaciones cuando no existan baremos locales. La trazabilidad '
                       'mejora continuidad asistencial, supervisión clínica y comunicación con otros profesionales de '
                       'la red de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p><p>Capacite al paciente para '
                       'interpretar sus resultados como indicadores revisables, no como etiquetas permanentes. La '
                       'alianza terapéutica mejora cuando el evaluado comprende el propósito del instrumento y sus '
                       'límites.</p>'},
              {'h2': 'Puntuación y tabla de severidad BDI-II',
               'html': '<p>Suma 21 ítems (0–3 cada uno), total 0–63. Rangos habituales: 0–13 mínima, 14–19 leve, 20–28 '
                       'moderada, 29–63 severa. Revise ítem 9 (ideación suicida) siempre.</p>\n'
                       '<p>Registre puntaje, fecha y fase de tratamiento. En telepsicología, confirme comprensión de '
                       'opciones graduadas.</p><table '
                       'class="severity-table"><thead><tr><th>Puntuaci&oacute;n</th><th>Severidad</th><th>Acci&oacute;n '
                       'cl&iacute;nica</th></tr></thead><tbody><tr><td><span class="score-badge">0 &ndash; '
                       '13</span></td><td><strong>M&iacute;nima</strong></td><td>Psicoeducaci&oacute;n y '
                       'monitoreo.</td></tr><tr><td><span class="score-badge">14 &ndash; '
                       '19</span></td><td><strong>Leve</strong></td><td>Psicoterapia breve o '
                       'vigilancia.</td></tr><tr><td><span class="score-badge">20 &ndash; '
                       '28</span></td><td><strong>Moderada</strong></td><td>Tratamiento activo '
                       'recomendado.</td></tr><tr><td><span class="score-badge">29 &ndash; '
                       '63</span></td><td><strong>Severa</strong></td><td>Intervenci&oacute;n intensiva; riesgo '
                       'suicida.</td></tr></tbody></table><p>Documente fecha, contexto de aplicación, versión del '
                       'instrumento y limitaciones cuando no existan baremos locales. La trazabilidad mejora '
                       'continuidad asistencial, supervisión clínica y comunicación con otros profesionales de la red '
                       'de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'},
              {'h2': 'Sensibilidad al cambio y seguimiento terapéutico',
               'html': '<p>BDI-II detecta mejoras tras psicoterapia cognitiva o farmacoterapia en estudios clínicos. '
                       'Repita cada 4–8 semanas. Reducción ≥10 puntos suele considerarse cambio clínicamente '
                       'significativo.</p>\n'
                       '<p>Grafique evolución para feedback al paciente y aseguradoras. Digitalice con <a '
                       'href="/articulos/tests-psicologicos-digitales.html">tests psicológicos '
                       'digitales</a>.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite '
                       'conclusiones categóricas basadas en un solo puntaje; integre entrevista, observación, historia '
                       'de tratamiento previo y factores contextuales. El informe debe ser comprensible para el '
                       'paciente sin perder rigor técnico ni omitir recomendaciones accionables.</p><p>Revise '
                       'coherencia entre síntomas reportados, conducta observada en sesión e informes de terceros '
                       'cuando estén disponibles. Las discrepancias orientan exploración adicional, no descalificación '
                       'automática del paciente.</p>'},
              {'h2': 'BDI test vs. PHQ-9: cuándo usar cada uno',
               'html': '<p>PHQ-9: triage rápido, atención primaria, telepsicología breve. BDI-II: consulta privada con '
                       'foco cognitivo, investigación, seguimiento detallado. No administre ambos sin razón '
                       'clínica.</p>\n'
                       '<p>Si PHQ-9 ≥10, BDI-II puede afinar objetivos terapéuticos ( culpa, insomnio, fatiga). '
                       'Consulte <a href="/articulos/como-interpretar-tests-psicologicos.html">cómo interpretar tests '
                       'psicológicos</a>.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite '
                       'conclusiones categóricas basadas en un solo puntaje; integre entrevista, observación, historia '
                       'de tratamiento previo y factores contextuales. El informe debe ser comprensible para el '
                       'paciente sin perder rigor técnico ni omitir recomendaciones accionables.</p><p>Revise '
                       'coherencia entre síntomas reportados, conducta observada en sesión e informes de terceros '
                       'cuando estén disponibles. Las discrepancias orientan exploración adicional, no descalificación '
                       'automática del paciente.</p>'},
              {'h2': 'Interpretación cautelosa y factores confusos',
               'html': '<p>Duelo, enfermedad médica, trastorno bipolar en fase depresiva pueden elevar puntajes. '
                       'Explore duración, funcionalidad y historia manic/hypomanic antes de concluir trastorno '
                       'depresivo mayor unipolar.</p>\n'
                       '<p>Deseabilidad social puede subestimar; entrevista clínica equilibra '
                       'autorreporte.</p><p>Documente fecha, contexto de aplicación, versión del instrumento y '
                       'limitaciones cuando no existan baremos locales. La trazabilidad mejora continuidad '
                       'asistencial, supervisión clínica y comunicación con otros profesionales de la red de salud '
                       'mental en México.</p><p>En telepsicología, confirme identidad del evaluado, condiciones de '
                       'privacidad y comprensión de instrucciones antes de puntuar. Registre interrupciones, apoyo de '
                       'terceros o necesidad de oralizar ítems por baja escolaridad o fatiga atencional.</p><p>Evite '
                       'conclusiones categóricas basadas en un solo puntaje; integre entrevista, observación, historia '
                       'de tratamiento previo y factores contextuales. El informe debe ser comprensible para el '
                       'paciente sin perder rigor técnico ni omitir recomendaciones accionables.</p><p>Revise '
                       'coherencia entre síntomas reportados, conducta observada en sesión e informes de terceros '
                       'cuando estén disponibles. Las discrepancias orientan exploración adicional, no descalificación '
                       'automática del paciente.</p>'},
              {'h2': 'Registro en historia clínica y Kalyo',
               'html': '<p>Documente conforme a <a href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a>: '
                       'test, puntajes, interpretación, plan. No reproduzca ítems completos en informes públicos.</p>\n'
                       '<p>Centralice aplicaciones seriadas en <a href="https://app.kalyo.io/register">Kalyo</a> para '
                       'trazabilidad y recordatorios de reevaluación.</p><p>Documente fecha, contexto de aplicación, '
                       'versión del instrumento y limitaciones cuando no existan baremos locales. La trazabilidad '
                       'mejora continuidad asistencial, supervisión clínica y comunicación con otros profesionales de '
                       'la red de salud mental en México.</p><p>En telepsicología, confirme identidad del evaluado, '
                       'condiciones de privacidad y comprensión de instrucciones antes de puntuar. Registre '
                       'interrupciones, apoyo de terceros o necesidad de oralizar ítems por baja escolaridad o fatiga '
                       'atencional.</p><p>Evite conclusiones categóricas basadas en un solo puntaje; integre '
                       'entrevista, observación, historia de tratamiento previo y factores contextuales. El informe '
                       'debe ser comprensible para el paciente sin perder rigor técnico ni omitir recomendaciones '
                       'accionables.</p><p>Revise coherencia entre síntomas reportados, conducta observada en sesión e '
                       'informes de terceros cuando estén disponibles. Las discrepancias orientan exploración '
                       'adicional, no descalificación automática del paciente.</p>'}],
 'faqs': [{'q': '¿BDI test es gratuito?',
           'a': 'No. BDI-II es instrumento con copyright. Adquiera formularios y manual autorizados.'},
          {'q': '¿BDI-II en adolescentes?',
           'a': 'Desde 13 años con lectura adecuada. Interprete con cautela en menores.'},
          {'q': '¿Cuánto tarda en aplicarse?', 'a': '5–10 minutos autoadministrado. Más si requiere oralización.'},
          {'q': '¿BDI reemplaza entrevista diagnóstica?',
           'a': 'Nunca. Cuantifica severidad; diagnóstico exige evaluación integral.'},
          {'q': '¿Integrar BDI con GAD-7?',
           'a': 'Sí en cuadros mixtos ansiedad-depresión. Aplicar ambos toma pocos minutos adicionales.'}],
 'related': [{'href': '/articulos/inventario-depresion-beck-bdi.html', 'label': 'Inventario depresión Beck'},
             {'href': '/articulos/que-es-el-phq-9.html', 'label': 'PHQ-9'},
             {'href': '/articulos/escala-de-beck-bdi-ii.html', 'label': 'Escala Beck BDI-II'},
             {'href': '/articulos/tests-psicologicos-digitales.html', 'label': 'Tests digitales'}],
 'references': ['Beck, A. T., Steer, R. A., & Brown, G. K. (1996). <em>BDI-II Manual</em>. San Antonio, TX: '
                'Psychological Corporation.',
                'Beck, A. T., Ward, C. H., Mendelson, M., et al. (1961). An inventory for measuring depression. '
                '<em>Archives of General Psychiatry</em>, 4, 561–571.']}

