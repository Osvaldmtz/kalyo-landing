# -*- coding: utf-8 -*-
"""SPECS for generate_aeo_comparativos8.py — 7 comparative AEO articles."""
from __future__ import annotations

TABLE_TAIL = (
    '<p>La tabla orienta respuestas r&aacute;pidas; los apartados siguientes '
    "detallan matices cl&iacute;nicos y de pr&aacute;ctica.</p>"
)


def kalyo(slug: str) -> str:
    return (
        f'<a href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article'
        f'&utm_campaign={slug}">Kalyo</a>'
    )


SPECS = [
    {
        "slug": "tcc-vs-act-diferencias",
        "title": "TCC vs ACT: diferencias clínicas clave MX/CO 2026 | Kalyo",
        "description": "Terapia cognitivo conductual vs ACT: diferencias de modelo, técnicas clave, indicaciones y cuándo elegir cada enfoque en México y Colombia. Tabla comparativa.",
        "keywords": "terapia cognitivo conductual, terapia de aceptacion y compromiso, TCC vs ACT, diferencias TCC ACT",
        "h1": "TCC vs ACT (Acceptance and Commitment Therapy): diferencias clínicas",
        "breadcrumb_short": "TCC vs ACT",
        "hero_alt": "Comparativa terapia cognitivo conductual y ACT en consulta",
        "inline_alt": "Tabla TCC versus terapia de aceptación y compromiso",
        "meta_label": "Psicoterapia &middot; Comparativa 2026",
        "date_published": "2026-11-16",
        "date_modified": "2026-11-16",
        "quick_answer": "La <strong>terapia cognitivo conductual (TCC)</strong> trabaja pensamientos y conductas con reestructuraci&oacute;n, exposici&oacute;n y experimentos para reducir s&iacute;ntomas. La <strong>terapia de aceptaci&oacute;n y compromiso (ACT)</strong> usa defusi&oacute;n, aceptaci&oacute;n y valores para flexibilidad psicol&oacute;gica. No compiten siempre: TCC encaja en metas conductuales claras; ACT en evitaci&oacute;n experiencial y falta de valores. Vea <a href=\"/articulos/terapia-cognitivo-conductual-guia.html\">gu&iacute;a TCC</a> y <a href=\"/articulos/alianza-terapeutica.html\">alianza terap&eacute;utica</a>.",
        "intro_long": "Elegir entre <strong>terapia cognitivo conductual y ACT</strong> exige conocer objetivos, evidencia y estilo del paciente, no solo modas de posgrado. Esta gu&iacute;a compara TCC vs ACT con tabla, indicaciones en ansiedad, depresi&oacute;n y cr&oacute;nico, y criterios de derivaci&oacute;n en M&eacute;xico y Colombia. Complementa <a href=\"/articulos/terapia-cognitivo-conductual-vs-psicoanalitica.html\">TCC vs psicoan&aacute;lisis</a> y la <a href=\"/articulos/terapia-cognitivo-conductual-guia.html\">gu&iacute;a de TCC</a> para decisiones informadas en consultorio.",
        "cta_h2": "Registra objetivos y técnicas terapéuticas en Kalyo",
        "cta_p": "Notas, plan y seguimiento por sesi&oacute;n &mdash; kalyo.io",
        "card_title": "TCC vs ACT: diferencias clínicas",
        "card_p": "Modelo, técnicas, indicaciones y cuándo elegir TCC o ACT.",
        "after_href": "/articulos/terapia-cognitivo-conductual-vs-psicoanalitica.html",
        "after_loc": "https://kalyo.io/articulos/terapia-cognitivo-conductual-vs-psicoanalitica.html",
        "asset_from": "alianza-terapeutica",
        "sections": [
            {
                "h2": "Tabla comparativa TCC vs ACT",
                "html": (
                    '<table class="items-table">\n'
                    "<thead><tr><th>Aspecto</th><th>TCC</th><th>ACT</th></tr></thead>\n"
                    "<tbody>\n"
                    "<tr><td>Meta principal</td><td>Reducir s&iacute;ntomas y cambiar patrones</td>"
                    "<td>Aumentar flexibilidad psicol&oacute;gica y acci&oacute;n valiosa</td></tr>\n"
                    "<tr><td>Relaci&oacute;n con pensamientos</td><td>Evaluar y reestructurar distorsiones</td>"
                    "<td>Defusi&oacute;n; menos litigio cognitivo</td></tr>\n"
                    "<tr><td>T&eacute;cnicas n&uacute;cleo</td><td>Exposici&oacute;n, reestructuraci&oacute;n, tareas</td>"
                    "<td>Aceptaci&oacute;n, valores, mindfulness</td></tr>\n"
                    "<tr><td>Ideal si</td><td>Meta conductual concreta, TAG, TOC</td>"
                    "<td>Evitaci&oacute;n experiencial, dolor cr&oacute;nico, valores difusos</td></tr>\n"
                    "<tr><td>Evidencia</td><td>Muy alta en depresi&oacute;n y ansiedad</td>"
                    "<td>Creciente en ansiedad, depresi&oacute;n y salud</td></tr>\n"
                    "</tbody></table>\n" + TABLE_TAIL
                ),
            },
            {
                "h2": "Terapia cognitivo conductual: cu&aacute;ndo priorizarla",
                "html": (
                    "<p>La <strong>terapia cognitivo conductual</strong> asume que cogniciones, conductas y "
                    "sensaciones se mantienen en ciclos que se pueden intervenir con tareas medibles. "
                    "En consulta privada funciona bien cuando el paciente pide alivio r&aacute;pido de "
                    "p&aacute;nico, insomnio, rumiaci&oacute;n rumiante o procrastinaci&oacute;n con metas claras.</p>\n"
                    "<p>Use psicoeducaci&oacute;n breve, registro de pensamientos autom&aacute;ticos y "
                    "exposici&oacute;n graduada. Documente nivel de respuesta con escalas (GAD-7, PHQ-9) "
                    "cada dos a cuatro semanas. Si el paciente rechaza &laquo;cambiar pensamientos&raquo;, "
                    "no fuerce TCC pura: explore ACT o integraci&oacute;n.</p>\n"
                    "<p>Revise competencia: ACT y TCC comparten tercera ola contextual pero difieren en "
                    "postura ante el contenido mental. Supervisi&oacute;n evita mezclar t&eacute;cnicas sin "
                    "formulaci&oacute;n coherente.</p>\n"
                ),
            },
            {
                "h2": "Terapia de aceptaci&oacute;n y compromiso: aportes cl&iacute;nicos",
                "html": (
                    "<p>La <strong>terapia de aceptaci&oacute;n y compromiso</strong> enfatiza contacto "
                    "presente, aceptaci&oacute;n de experiencias internas y compromiso con valores aun "
                    "con malestar. Es &uacute;til cuando el paciente est&aacute; atrapado en evitaci&oacute;n "
                    "experiencial (&laquo;no puedo sentir esto&raquo;) o cuando la reestructuraci&oacute;n "
                    "cognitiva genera resistencia.</p>\n"
                    "<p>Ejercicios t&iacute;picos: hoja de valores, defusi&oacute;n (&laquo;estoy teniendo el "
                    "pensamiento de que&hellip;&raquo;), exposici&oacute;n con aceptaci&oacute;n. En dolor "
                    "cr&oacute;nico y enfermedad, ACT complementa intervenciones m&eacute;dicas sin prometer "
                    "eliminar sensaci&oacute;n.</p>\n"
                    "<p>No confunda aceptaci&oacute;n con resignaci&oacute;n: el plan sigue orientado a acci&oacute;n "
                    "valiosa. Registre valores y compromisos en nota SOAP para continuidad.</p>\n"
                ),
            },
            {
                "h2": "Integraci&oacute;n, derivaci&oacute;n y documentaci&oacute;n",
                "html": (
                    "<p>Muchos cl&iacute;nicos usan t&eacute;cnicas ACT dentro de un encuadre TCC o viceversa; "
                    "lo cr&iacute;tico es explicar al paciente el &laquo;por qu&eacute;&raquo; de cada "
                    "intervenci&oacute;n. Si tras ocho a doce sesiones no hay avance medible, renegocie modelo "
                    "o derive. Compare con <a href=\"/articulos/terapia-cognitivo-conductual-vs-psicoanalitica.html\">"
                    "TCC vs psicoan&aacute;lisis</a> si el conflicto es de profundidad versus brevedad.</p>\n"
                    "<p>En el expediente anote: hip&oacute;tesis de caso, t&eacute;cnicas usadas, respuesta y "
                    "tarea entre sesiones. La <a href=\"/articulos/alianza-terapeutica.html\">alianza "
                    "terap&eacute;utica</a> predice resultado en ambos modelos; midala si puede (WAI-SR).</p>\n"
                    f"<p>{kalyo('tcc-vs-act-diferencias')} ayuda a registrar objetivos, tareas y notas por sesi&oacute;n "
                    "sin perder el hilo del modelo elegido.</p>\n"
                    "<p>Actualice consentimiento si graba ejercicios de mindfulness o usa apps de terceros. "
                    "Revise pol&iacute;ticas de datos si el paciente comparte registros por mensajer&iacute;a.</p>\n"
                ),
            },
        ],
        "faqs": [
            {
                "q": "&iquest;ACT reemplaza a la TCC?",
                "a": "No. Son modelos distintos con solapamiento. TCC sigue primera l&iacute;nea en muchos trastornos de ansiedad y depresi&oacute;n seg&uacute;n gu&iacute;as; ACT aporta cuando la evitaci&oacute;n experiencial domina.",
            },
            {
                "q": "&iquest;Puedo mezclar t&eacute;cnicas sin entrenamiento ACT?",
                "a": "Use solo lo que domina. Mindfulness suelto sin marco ACT puede confundir al paciente. Busque supervisi&oacute;n o formaci&oacute;n breve certificada.",
            },
            {
                "q": "&iquest;Cu&aacute;l tiene m&aacute;s evidencia en M&eacute;xico?",
                "a": "La TCC acumula m&aacute;s ensayos en depresi&oacute;n y ansiedad. ACT crece en salud y dolor cr&oacute;nico. Elija por encaje cl&iacute;nico, no por volumen de b&uacute;squeda aislado.",
            },
            {
                "q": "&iquest;Duraci&oacute;n t&iacute;pica de cada una?",
                "a": "Ambas pueden ser breves (8&ndash;20 sesiones) seg&uacute;n protocolo. ACT a veces requiere m&aacute;s tiempo para clarificar valores en casos complejos.",
            },
            {
                "q": "&iquest;C&oacute;mo explicarlo al paciente?",
                "a": "TCC: &laquo;trabajamos pensamientos y conductas para aliviar s&iacute;ntomas&raquo;. ACT: &laquo;aprendemos a actuar seg&uacute;n valores aun con pensamientos dif&iacute;ciles&raquo;.",
            },
        ],
        "related": [
            {"href": "/articulos/terapia-cognitivo-conductual-guia.html", "label": "Gu&iacute;a TCC"},
            {"href": "/articulos/terapia-cognitivo-conductual-vs-psicoanalitica.html", "label": "TCC vs psicoan&aacute;lisis"},
            {"href": "/articulos/alianza-terapeutica.html", "label": "Alianza terap&eacute;utica"},
            {"href": "/articulos/nota-evolucion-soap-psicologia.html", "label": "Nota SOAP"},
        ],
    },
    {
        "slug": "dsm-5-vs-cie-11-documentacion-clinica",
        "title": "DSM-5 vs CIE-11: documentación clínica MX/CO 2026 | Kalyo",
        "description": "DSM-5 y CIE-11 en documentación clínica: cuándo citar cada manual en notas, informes e historia psicológica en México y Colombia. Guía con tabla comparativa.",
        "keywords": "dsm-5, dsm 5, cie 11, documentación clínica, codificación psicología, historia clínica",
        "h1": "DSM-5 vs CIE-11 en documentación clínica para psicólogos",
        "breadcrumb_short": "DSM-5 vs CIE-11 documentación",
        "hero_alt": "Psicólogo documentando diagnóstico con DSM-5 y CIE-11",
        "inline_alt": "Tabla DSM-5 versus CIE-11 en expediente clínico",
        "meta_label": "Documentaci&oacute;n &middot; Comparativa 2026",
        "date_published": "2026-11-16",
        "date_modified": "2026-11-16",
        "quick_answer": "El <strong>DSM-5</strong> sigue siendo referencia frecuente en formaci&oacute;n y convenios privados en LATAM; la <strong>CIE-11</strong> es el clasificador internacional de la OMS para estad&iacute;stica, interoperabilidad y muchos sistemas p&uacute;blicos. En <em>documentaci&oacute;n cl&iacute;nica</em> del psic&oacute;logo, cite el sistema acordado con la instituci&oacute;n, el pagador o el pa&iacute;s, y cruce c&oacute;digos si el informe viaja. Vea el panorama en <a href=\"/articulos/cie-11-vs-dsm-5-diferencias.html\">CIE-11 vs DSM-5</a> y <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a>.",
        "intro_long": "Confundir <strong>DSM-5 y CIE-11</strong> en notas e informes genera rechazos de facturaci&oacute;n, informes incompletos y riesgo &eacute;tico. Esta gu&iacute;a &mdash;complemento de <a href=\"/articulos/cie-11-vs-dsm-5-diferencias.html\">CIE-11 vs DSM-5</a>&mdash; explica cu&aacute;ndo citar cada manual en historia cl&iacute;nica, informes y codificaci&oacute;n para psic&oacute;logos en M&eacute;xico y Colombia, con tabla y ejemplos de redacci&oacute;n. Apl&iacute;quela en su flujo de expediente digital diario.",
        "cta_h2": "Estandariza diagnósticos y notas en Kalyo",
        "cta_p": "Expediente, plantillas y trazabilidad &mdash; kalyo.io",
        "card_title": "DSM-5 vs CIE-11 en documentación",
        "card_p": "Cuándo citar cada manual en notas e informes MX/CO.",
        "after_href": "/articulos/cie-11-vs-dsm-5-diferencias.html",
        "after_loc": "https://kalyo.io/articulos/cie-11-vs-dsm-5-diferencias.html",
        "asset_from": "cie-11-vs-dsm-5-diferencias",
        "sections": [
            {
                "h2": "Tabla comparativa DSM-5 vs CIE-11 en documentaci&oacute;n",
                "html": (
                    '<table class="items-table">\n'
                    "<thead><tr><th>Aspecto</th><th>DSM-5</th><th>CIE-11</th></tr></thead>\n"
                    "<tbody>\n"
                    "<tr><td>Origen</td><td>APA (EE. UU.)</td><td>OMS / clasificaci&oacute;n mundial</td></tr>\n"
                    "<tr><td>Uso en nota cl&iacute;nica MX/CO</td><td>Frecuente en privado y formaci&oacute;n</td>"
                    "<td>Creciente en p&uacute;blico, RIPS, interoperabilidad</td></tr>\n"
                    "<tr><td>C&oacute;digos</td><td>C&oacute;digos DSM + a menudo CIE enlazada</td>"
                    "<td>C&oacute;digos ICD-11 (ej. 6A70 depresi&oacute;n)</td></tr>\n"
                    "<tr><td>En informe psicol&oacute;gico</td><td>Diagn&oacute;stico nosol&oacute;gico habitual</td>"
                    "<td>Indicar c&oacute;digo si el destinatario lo exige</td></tr>\n"
                    "<tr><td>Riesgo si mezcla</td><td>Inconsistencia entre sistemas</td>"
                    "<td>Rechazo administrativo o auditor&iacute;a</td></tr>\n"
                    "</tbody></table>\n" + TABLE_TAIL
                ),
            },
            {
                "h2": "Qu&eacute; escribir en la historia cl&iacute;nica",
                "html": (
                    "<p>La historia debe reflejar <strong>impresi&oacute;n diagn&oacute;stica</strong> o "
                    "formulaci&oacute;n seg&uacute;n su marco, criterios considerados y plan. Si usa DSM-5, "
                    "nombre el trastorno y severidad cuando aplique; si la EPS o aseguradora exige CIE-11, "
                    "añada el c&oacute;digo correspondiente en el mismo bloque o en anexo estructurado.</p>\n"
                    "<p>En M&eacute;xico, el contenido m&iacute;nimo sigue alineado a <a "
                    'href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a>: no prescribe un '
                    "manual &uacute;nico, pero s&iacute; coherencia. En Colombia, concilie con historia "
                    "cl&iacute;nica institucional y <a href=\"/articulos/rips-registros-individuales-colombia.html\">"
                    "RIPS</a> si reporta.</p>\n"
                    "<p>Evite listar c&oacute;digos sin justificaci&oacute;n cl&iacute;nica: documente "
                    "s&iacute;ntomas, duraci&oacute;n, funcionalidad y exclusiones.</p>\n"
                ),
            },
            {
                "h2": "Informes, derivaciones y terceros",
                "html": (
                    "<p>Antes de emitir informe laboral, escolar o judicial, pregunte qu&eacute; "
                    "clasificaci&oacute;n espera el destinatario. Muchos formatos privados siguen DSM-5; "
                    "instituciones de salud migran a CIE-11. Si solo conoce DSM, use tablas de "
                    "concordancia oficiales o de su colegio; no adivine c&oacute;digos.</p>\n"
                    "<p>En derivaci&oacute;n a psiquiatr&iacute;a, incluya diagn&oacute;stico diferencial, "
                    "riesgo y tratamiento actual. El psiquiatra puede recodificar al formato m&eacute;dico; "
                    "su nota debe ser clara y fechada.</p>\n"
                    "<p>Para panorama conceptual (no solo codificaci&oacute;n), remita al paciente o colega a "
                    "<a href=\"/articulos/cie-11-vs-dsm-5-diferencias.html\">CIE-11 vs DSM-5: diferencias</a>.</p>\n"
                ),
            },
            {
                "h2": "Buenas pr&aacute;cticas en expediente digital",
                "html": (
                    "<p>Configure plantillas con campos: sistema de clasificaci&oacute;n, c&oacute;digo, "
                    "criterios cumplidos, fecha de evaluaci&oacute;n. Revise cada a&ntilde;o si su "
                    "consultorio cambió de pagador o convenio p&uacute;blico.</p>\n"
                    "<p>Capacite a practicantes: un c&oacute;digo copiado de internet sin exploraci&oacute;n "
                    "es riesgo &eacute;tico y legal. Supervisi&oacute;n debe muestrear coherencia DSM&ndash;CIE.</p>\n"
                    f"<p>{kalyo('dsm-5-vs-cie-11-documentacion-clinica')} facilita plantillas de impresi&oacute;n "
                    "diagn&oacute;stica y notas con historial por paciente.</p>\n"
                    "<p>Mantenga biblioteca de referencia actualizada (DSM-5-TR, CIE-11 MH). No sustituya "
                    "juicio cl&iacute;nico por automatizaci&oacute;n sin revisi&oacute;n profesional.</p>\n"
                ),
            },
        ],
        "faqs": [
            {
                "q": "&iquest;Debo abandonar DSM-5 en 2026?",
                "a": "No necesariamente en consulta privada. Adopte CIE-11 donde la ley o el contrato lo exijan y mantenga concordancia documentada.",
            },
            {
                "q": "&iquest;El psic&oacute;logo solo usa CIE-11?",
                "a": "Depende del contexto. Muchos combinan formulaci&oacute;n DSM en nota y c&oacute;digo CIE para reportes oficiales.",
            },
            {
                "q": "&iquest;Qu&eacute; pasa si uso el c&oacute;digo equivocado?",
                "a": "Corrija con addendum fechado. Errores sistem&aacute;ticos pueden afectar auditor&iacute;as y cobertura.",
            },
            {
                "q": "&iquest;Es lo mismo que el art&iacute;culo CIE-11 vs DSM-5?",
                "a": "Ese art&iacute;culo compara manuales en general; esta gu&iacute;a se centra en documentaci&oacute;n cl&iacute;nica diaria.",
            },
            {
                "q": "&iquest;Kalyo codifica autom&aacute;ticamente?",
                "a": "Ofrece estructura para registrar diagn&oacute;sticos; el criterio y la elecci&oacute;n del sistema siguen siendo suyos.",
            },
        ],
        "related": [
            {"href": "/articulos/cie-11-vs-dsm-5-diferencias.html", "label": "CIE-11 vs DSM-5"},
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004"},
            {"href": "/articulos/como-redactar-informe-psicologico.html", "label": "Informe psicol&oacute;gico"},
            {"href": "/articulos/rips-registros-individuales-colombia.html", "label": "RIPS Colombia"},
        ],
    },
    {
        "slug": "evaluacion-psicometrica-vs-proyectiva",
        "title": "Evaluación psicométrica vs proyectiva: guía clínica | Kalyo",
        "description": "Evaluación psicométrica vs pruebas proyectivas: objetivos, validez, informes y cuándo combinar ambos en la práctica clínica. Tabla comparativa para psicólogos.",
        "keywords": "evaluacion psicometrica, pruebas proyectivas, evaluación psicológica, tests psicológicos",
        "h1": "Evaluación psicométrica vs pruebas proyectivas en clínica",
        "breadcrumb_short": "Psicométrica vs proyectiva",
        "hero_alt": "Comparativa evaluación psicométrica y pruebas proyectivas",
        "inline_alt": "Tabla evaluación psicométrica versus tests proyectivos",
        "meta_label": "Evaluaci&oacute;n &middot; Comparativa 2026",
        "date_published": "2026-11-16",
        "date_modified": "2026-11-16",
        "quick_answer": "La <strong>evaluaci&oacute;n psicom&eacute;trica</strong> usa instrumentos estandarizados con normas, confiabilidad y validez conocidas (escalas, inventarios). Las <strong>pruebas proyectivas</strong> inferen din&aacute;mica a partir de respuestas abiertas (Rorschach, HTP, dibujo familiar). No son opuestas excluyentes: la psicom&eacute;trica orienta severidad y diagn&oacute;stico; la proyectiva aporta hip&oacute;tesis cualitativas. Vea <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">interpretaci&oacute;n de tests</a>.",
        "intro_long": "Elegir entre <strong>evaluaci&oacute;n psicom&eacute;trica y pruebas proyectivas</strong> define costo, tiempo y defensibilidad del informe en evaluaciones cl&iacute;nicas complejas. Esta gu&iacute;a compara objetivos, evidencia, informes y criterios de uso en consultorio latinoamericano, con tabla directa para educaci&oacute;n. Complementa <a href=\"/articulos/tests-proyectivos-rorschach-htp.html\">tests proyectivos Rorschach y HTP</a> y la <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">gu&iacute;a de interpretaci&oacute;n</a> para armar bater&iacute;as coherentes sin sobre-evaluar al paciente.",
        "cta_h2": "Archiva resultados e informes en Kalyo",
        "cta_p": "Expediente, informes y trazabilidad &mdash; kalyo.io",
        "card_title": "Evaluación psicométrica vs proyectiva",
        "card_p": "Objetivos, validez, informes y cuándo combinar baterías.",
        "after_href": "/articulos/tests-proyectivos-rorschach-htp.html",
        "after_loc": "https://kalyo.io/articulos/tests-proyectivos-rorschach-htp.html",
        "asset_from": "tests-proyectivos-rorschach-htp",
        "sections": [
            {
                "h2": "Tabla comparativa evaluaci&oacute;n psicom&eacute;trica vs proyectiva",
                "html": (
                    '<table class="items-table">\n'
                    "<thead><tr><th>Aspecto</th><th>Psicom&eacute;trica</th><th>Proyectiva</th></tr></thead>\n"
                    "<tbody>\n"
                    "<tr><td>Formato</td><td>&Iacute;tems cerrados, puntuaci&oacute;n</td>"
                    "<td>Est&iacute;mulo + producci&oacute;n libre</td></tr>\n"
                    "<tr><td>Normas</td><td>Muestras representativas</td>"
                    "<td>Variable seg&uacute;n sistema de codificaci&oacute;n</td></tr>\n"
                    "<tr><td>Objetivo</td><td>Severidad, tamizaje, seguimiento</td>"
                    "<td>Hip&oacute;tesis din&aacute;mica, personalidad</td></tr>\n"
                    "<tr><td>Tiempo</td><td>15&ndash;60 min por escala</td>"
                    "<td>1&ndash;3 h seg&uacute;n bater&iacute;a</td></tr>\n"
                    "<tr><td>Informe</td><td>Cifras + interpretaci&oacute;n cauta</td>"
                    "<td>Narrativa cualitativa argumentada</td></tr>\n"
                    "</tbody></table>\n" + TABLE_TAIL
                ),
            },
            {
                "h2": "Cu&aacute;ndo priorizar evaluaci&oacute;n psicom&eacute;trica",
                "html": (
                    "<p>La <strong>evaluaci&oacute;n psicom&eacute;trica</strong> es id&oacute;nea para tamizaje "
                    "(PHQ-9, GAD-7), evaluaci&oacute;n de personalidad con inventarios validados, neuropsicolog&iacute;a "
                    "breve y monitorizaci&oacute;n de tratamiento. En convenios con aseguradoras suele ser lo que "
                    "exigen para autorizar sesiones.</p>\n"
                    "<p>Documente manual aplicado, fecha, puntuaci&oacute;n bruta/est&aacute;ndar y limitaciones "
                    "(idioma, educaci&oacute;n, visi&oacute;n). No extrapole trastornos solo por un punto de corte "
                    "sin entrevista cl&iacute;nica.</p>\n"
                    "<p>Use <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">gu&iacute;a de "
                    "interpretaci&oacute;n</a> para evitar sobreinterpretaci&oacute;n.</p>\n"
                ),
            },
            {
                "h2": "Rol de las pruebas proyectivas",
                "html": (
                    "<p>Las <strong>pruebas proyectivas</strong> pueden enriquecer comprensi&oacute;n de conflictos, "
                    "mecanismos de defensa y representaci&oacute;n del self cuando el evaluador est&aacute; "
                    "capacitado en el sistema (p. ej. Rorschach seg&uacute;n manual actual). No sustituyen "
                    "entrevista ni escalas cuando se necesita medir cambio objetivo.</p>\n"
                    "<p>En menores, dibujos y juegos proyectivos ayudan cuando el lenguaje es limitado; igual requiere "
                    "formulaci&oacute;n integradora. Vea <a href=\"/articulos/tests-proyectivos-rorschach-htp.html\">"
                    "Rorschach y HTP</a> para cuidados de aplicaci&oacute;n.</p>\n"
                    "<p>Evite conclusiones forenses solo con proyectivas si el tribunal pide datos psicom&eacute;tricos "
                    "replicables.</p>\n"
                ),
            },
            {
                "h2": "Bater&iacute;a integrada e informe",
                "html": (
                    "<p>La mejor pr&aacute;ctica combina entrevista estructurada, psicom&eacute;trica para severidad "
                    "y, si aplica, proyectiva para hip&oacute;tesis. El informe debe separar datos, interpretaci&oacute;n "
                    "y recomendaciones; cite instrumentos por nombre y edici&oacute;n.</p>\n"
                    "<p>Conserve protocolos y hojas de respuesta seg&uacute;n plazos &eacute;ticos y legales. "
                    "Digitalice con control de acceso; no env&iacute;e PDFs sin cifrar por correo personal.</p>\n"
                    f"<p>{kalyo('evaluacion-psicometrica-vs-proyectiva')} centraliza informes, escalas aplicadas "
                    "y fechas de reevaluaci&oacute;n.</p>\n"
                    "<p>Revise sesgo cultural al interpretar normas importadas: validez local importa tanto "
                    "como validez publicada.</p>\n"
                ),
            },
        ],
        "faqs": [
            {
                "q": "&iquest;Las proyectivas est&aacute;n obsoletas?",
                "a": "No en todos los contextos; s&iacute; requieren formaci&oacute;n rigurosa. La psicom&eacute;trica domina tamizaje y outcome medible.",
            },
            {
                "q": "&iquest;Puedo cobrar solo un cuestionario?",
                "a": "Si el encuadre lo define, s&iacute;; documente que no hubo evaluaci&oacute;n integral completa.",
            },
            {
                "q": "&iquest;Qu&eacute; va primero en la bater&iacute;a?",
                "a": "Entrevista y consentimiento; luego escalas breves; proyectivas si aportan hip&oacute;tesis no cubiertas.",
            },
            {
                "q": "&iquest;Tests digitales reemplazan papel?",
                "a": "Pueden, si hay licencia y validez demostrada en formato digital. Archive resultados en expediente.",
            },
            {
                "q": "&iquest;Un informe sin n&uacute;meros es v&aacute;lido?",
                "a": "Puede serlo en modelos cualitativos, pero debe explicitar m&eacute;todos y limitaciones.",
            },
        ],
        "related": [
            {"href": "/articulos/tests-proyectivos-rorschach-htp.html", "label": "Rorschach y HTP"},
            {"href": "/articulos/como-interpretar-tests-psicologicos.html", "label": "Interpretar tests"},
            {"href": "/articulos/como-redactar-informe-psicologico.html", "label": "Redactar informe"},
            {"href": "/articulos/tests-psicologicos-digitales.html", "label": "Tests digitales"},
        ],
    },
    {
        "slug": "terapia-individual-vs-grupal",
        "title": "Terapia grupal vs individual: diferencias MX/CO 2026 | Kalyo",
        "description": "Terapia grupal vs individual: indicaciones, confidencialidad y costos en México y Colombia. Tabla comparativa y criterios para derivar o combinar formatos.",
        "keywords": "terapia grupal, terapia individual, terapia grupal vs individual, psicoterapia grupal",
        "h1": "Terapia grupal vs terapia individual: diferencias en clínica",
        "breadcrumb_short": "Terapia grupal vs individual",
        "hero_alt": "Comparativa terapia grupal y terapia individual",
        "inline_alt": "Tabla terapia grupal versus sesión individual",
        "meta_label": "Psicoterapia &middot; Comparativa 2026",
        "date_published": "2026-11-16",
        "date_modified": "2026-11-16",
        "quick_answer": "La <strong>terapia grupal</strong> aprovecha din&aacute;mica colectiva, retroalimentaci&oacute;n entre pares y costo menor por persona; la <strong>terapia individual</strong> ofrece profundidad, confidencialidad m&aacute;xima y flexibilidad de agenda. Elija seg&uacute;n trastorno, motivaci&oacute;n grupal, riesgo y etapa del tratamiento. Muchos planes combinan ambas. Vea <a href=\"/articulos/terapia-grupal.html\">terapia grupal</a> y <a href=\"/articulos/alianza-terapeutica.html\">alianza terap&eacute;utica</a>.",
        "intro_long": "Decidir entre <strong>terapia grupal e individual</strong> afecta resultados, costo y log&iacute;stica del consultorio. Esta gu&iacute;a compara indicaciones, confidencialidad, din&aacute;mica y criterios de derivaci&oacute;n en M&eacute;xico y Colombia, con tabla para respuestas directas. Complementa <a href=\"/articulos/terapia-grupal.html\">terapia grupal</a> y el trabajo sobre <a href=\"/articulos/alianza-terapeutica.html\">alianza terap&eacute;utica</a> sin asumir que un formato sirve para todos los perfiles cl&iacute;nicos.",
        "cta_h2": "Coordina grupos e individuales en Kalyo",
        "cta_p": "Agenda, notas y expediente &mdash; kalyo.io",
        "card_title": "Terapia grupal vs individual",
        "card_p": "Indicaciones, confidencialidad y cuándo combinar formatos.",
        "after_href": "/articulos/terapia-grupal.html",
        "after_loc": "https://kalyo.io/articulos/terapia-grupal.html",
        "asset_from": "alianza-terapeutica",
        "sections": [
            {
                "h2": "Tabla comparativa terapia grupal vs individual",
                "html": (
                    '<table class="items-table">\n'
                    "<thead><tr><th>Aspecto</th><th>Terapia grupal</th><th>Terapia individual</th></tr></thead>\n"
                    "<tbody>\n"
                    "<tr><td>Din&aacute;mica</td><td>Pares, normalizaci&oacute;n, modelado</td>"
                    "<td>Foco exclusivo en un paciente</td></tr>\n"
                    "<tr><td>Confidencialidad</td><td>Acuerdo grupal + límites</td>"
                    "<td>M&aacute;xima entre terapeuta y paciente</td></tr>\n"
                    "<tr><td>Costo</td><td>Menor por participante</td>"
                    "<td>Mayor por hora cl&iacute;nica</td></tr>\n"
                    "<tr><td>Indicaciones</td><td>Aislamiento, habilidades sociales, adicciones</td>"
                    "<td>Trauma reciente, verg&uuml;enza extrema, alto riesgo</td></tr>\n"
                    "<tr><td>Documentaci&oacute;n</td><td>Nota grupal + notas individuales si aplica</td>"
                    "<td>Nota por sesi&oacute;n SOAP habitual</td></tr>\n"
                    "</tbody></table>\n" + TABLE_TAIL
                ),
            },
            {
                "h2": "Indicaciones de la terapia grupal",
                "html": (
                    "<p>La <strong>terapia grupal</strong> funciona en trastornos donde el apoyo entre pares acelera "
                    "cambio: dependencia, duelos, habilidades sociales, algunos trastornos de personalidad en "
                    "estabilizaci&oacute;n. El terapeuta facilita normas, turnos y manejo de rupturas.</p>\n"
                    "<p>Screening previo: excluya psicosis activa no controlada, violencia grave o conductas que "
                    "pongan al grupo en riesgo. Contrato escrito con reglas de confidencialidad y consecuencias "
                    "de incumplimiento.</p>\n"
                    "<p>Profundice en log&iacute;stica con <a href=\"/articulos/terapia-grupal.html\">gu&iacute;a de "
                    "terapia grupal</a>.</p>\n"
                ),
            },
            {
                "h2": "Cu&aacute;ndo priorizar terapia individual",
                "html": (
                    "<p>La <strong>terapia individual</strong> es preferible con trauma reciente, disociaci&oacute;n "
                    "severa, verg&uuml;enza paralizante, riesgo suicida que requiere monitoreo estrecho o cuando el "
                    "paciente rechaza exponerse al grupo. Tambi&eacute;n en fases de estabilizaci&oacute;n antes de "
                    "derivar a grupal.</p>\n"
                    "<p>Algunos pacientes usan individual para procesar material que surge en grupo: documente "
                    "coherencia entre ambas notas sin violar secreto grupal.</p>\n"
                    "<p>Renegocie formato si no hay avance tras tiempo razonable en uno de los modos.</p>\n"
                ),
            },
            {
                "h2": "Combinar formatos y registrar en expediente",
                "html": (
                    "<p>Modelos escalonados (individual &rarr; grupal &rarr; individual de cierre) son comunes en "
                    "hospitales y consulta privada. Defina objetivos distintos por modalidad y comunique al paciente.</p>\n"
                    "<p>En nota grupal registre tema, participaci&oacute;n observada, din&aacute;mica relevante y plan; "
                    "evite identificar secretos de otros miembros en expediente individual ajeno.</p>\n"
                    f"<p>{kalyo('terapia-individual-vs-grupal')} ayuda a separar agendas, asistencias y notas por "
                    "modalidad sin mezclar historiales.</p>\n"
                    "<p>Revise honorarios y pol&iacute;tica de cancelaci&oacute;n distinta para grupo (m&iacute;nimo "
                    "de participantes).</p>\n"
                ),
            },
        ],
        "faqs": [
            {
                "q": "&iquest;La grupal es m&aacute;s efectiva?",
                "a": "Depende del trastorno y del grupo. Meta-an&aacute;lisis en adicciones y algunos trastornos favorecen grupal; otros requieren individual.",
            },
            {
                "q": "&iquest;Cu&aacute;ntas personas por grupo?",
                "a": "Suele ir de 6 a 12 en psicoeducaci&oacute;n; menos en psicoterapia profunda. Ajuste por espacio y competencia.",
            },
            {
                "q": "&iquest;Mismo consentimiento que individual?",
                "a": "A&ntilde;ada cl&aacute;usulas de confidencialidad grupal y l&iacute;mites de contacto entre miembros.",
            },
            {
                "q": "&iquest;Puedo llevar individual y grupal al mismo paciente?",
                "a": "S&iacute;, con roles claros. Evite competencia entre co-terapeutas sin comunicaci&oacute;n.",
            },
            {
                "q": "&iquest;Telegrupo es viable?",
                "a": "S&iacute;, con plataforma segura y reglas de privacidad domiciliaria; documente modalidad.",
            },
        ],
        "related": [
            {"href": "/articulos/terapia-grupal.html", "label": "Terapia grupal"},
            {"href": "/articulos/alianza-terapeutica.html", "label": "Alianza terap&eacute;utica"},
            {"href": "/articulos/encuadre-terapeutico.html", "label": "Encuadre"},
            {"href": "/articulos/consentimiento-informado-psicologia.html", "label": "Consentimiento"},
        ],
    },
    {
        "slug": "psicologia-clinica-vs-salud",
        "title": "Psicología clínica vs de la salud: guía MX/CO 2026 | Kalyo",
        "description": "Psicología clínica vs psicología de la salud: objetivos, métodos y contextos de intervención en MX/CO. Tabla comparativa para profesionales en consultorio.",
        "keywords": "psicologia clinica, psicologia de la salud, diferencias psicología clínica salud",
        "h1": "Psicología clínica vs psicología de la salud",
        "breadcrumb_short": "Clínica vs salud",
        "hero_alt": "Comparativa psicología clínica y psicología de la salud",
        "inline_alt": "Tabla psicología clínica versus psicología de la salud",
        "meta_label": "Pr&aacute;ctica profesional &middot; Comparativa 2026",
        "date_published": "2026-11-16",
        "date_modified": "2026-11-16",
        "quick_answer": "La <strong>psicolog&iacute;a cl&iacute;nica</strong> eval&uacute;a y trata trastornos mentales y conductuales mediante psicoterapia y diagn&oacute;stico psicol&oacute;gico. La <strong>psicolog&iacute;a de la salud</strong> interviene promoci&oacute;n, prevenci&oacute;n, adherencia y manejo de enfermedad cr&oacute;nica en contextos m&eacute;dicos y comunitarios. En la pr&aacute;ctica real se solapan: un cl&iacute;nico trata depresi&oacute;n; un de la salud mejora adherencia en diabetes. Vea <a href=\"/articulos/alianza-terapeutica.html\">alianza terap&eacute;utica</a>.",
        "intro_long": "Diferenciar <strong>psicolog&iacute;a cl&iacute;nica y psicolog&iacute;a de la salud</strong> orienta formaci&oacute;n, marketing y derivaciones interdisciplinares sin confundir roles. Esta gu&iacute;a compara objetivos, m&eacute;todos, contextos y competencias en M&eacute;xico y Colombia, con tabla clara. Complementa <a href=\"/articulos/alianza-terapeutica.html\">alianza terap&eacute;utica</a> y modelos de intervenci&oacute;n en consultorio e instituciones de salud sin etiquetar al paciente solo por el &aacute;rea del psic&oacute;logo.",
        "cta_h2": "Documenta intervenciones clínicas en Kalyo",
        "cta_p": "Expediente, notas y seguimiento &mdash; kalyo.io",
        "card_title": "Psicología clínica vs de la salud",
        "card_p": "Objetivos, métodos y contextos de intervención.",
        "after_href": "/articulos/alianza-terapeutica.html",
        "after_loc": "https://kalyo.io/articulos/alianza-terapeutica.html",
        "asset_from": "alianza-terapeutica",
        "sections": [
            {
                "h2": "Tabla comparativa psicolog&iacute;a cl&iacute;nica vs de la salud",
                "html": (
                    '<table class="items-table">\n'
                    "<thead><tr><th>Aspecto</th><th>Psicolog&iacute;a cl&iacute;nica</th>"
                    "<th>Psicolog&iacute;a de la salud</th></tr></thead>\n"
                    "<tbody>\n"
                    "<tr><td>Foco</td><td>Trastornos mentales, psicoterapia</td>"
                    "<td>Conducta saludable, enfermedad cr&oacute;nica</td></tr>\n"
                    "<tr><td>Contexto</td><td>Consulta privada, salud mental</td>"
                    "<td>Hospitales, APS, empresas, comunidad</td></tr>\n"
                    "<tr><td>Metas</td><td>Alivio s&iacute;ntomas, funcionamiento</td>"
                    "<td>Prevenci&oacute;n, adherencia, calidad de vida</td></tr>\n"
                    "<tr><td>M&eacute;todos</td><td>Psicoterapia, evaluaci&oacute;n cl&iacute;nica</td>"
                    "<td>Psicoeducaci&oacute;n, modelos biopsicosociales</td></tr>\n"
                    "<tr><td>Colaboraci&oacute;n</td><td>Psiquiatr&iacute;a, trabajo social</td>"
                    "<td>Medicina, nutrici&oacute;n, enfermer&iacute;a</td></tr>\n"
                    "</tbody></table>\n" + TABLE_TAIL
                ),
            },
            {
                "h2": "Psicolog&iacute;a cl&iacute;nica en consultorio",
                "html": (
                    "<p>La <strong>psicolog&iacute;a cl&iacute;nica</strong> se centra en evaluaci&oacute;n diagn&oacute;stica "
                    "psicol&oacute;gica, formulaci&oacute;n de caso y tratamiento de trastornos (depresi&oacute;n, ansiedad, "
                    "TEPT, adicciones, etc.). El psic&oacute;logo cl&iacute;nico documenta con criterios DSM o CIE, aplica "
                    "protocolos de psicoterapia y monitoriza riesgo.</p>\n"
                    "<p>En consulta privada en LATAM este es el perfil m&aacute;s visible. Mantenga l&iacute;mites: no prescribe "
                    "ni sustituye atenci&oacute;n m&eacute;dica urgente. Derive cuando hay indicaci&oacute;n farmacol&oacute;gica "
                    "o psicosis.</p>\n"
                    "<p>La calidad de la <a href=\"/articulos/alianza-terapeutica.html\">alianza terap&eacute;utica</a> "
                    "sigue siendo predictor central del resultado.</p>\n"
                ),
            },
            {
                "h2": "Psicolog&iacute;a de la salud: &aacute;mbitos y tareas",
                "html": (
                    "<p>La <strong>psicolog&iacute;a de la salud</strong> trabaja adherencia a tratamiento, manejo del dolor, "
                    "estilos de vida, prevenci&oacute;n de ITS, programas en diabetes, hipertensi&oacute;n o oncolog&iacute;a. "
                    "Usa modelos como transte&oacute;rico de cambio, entrevista motivacional y TCC adaptada a enfermedad.</p>\n"
                    "<p>En empresas aparece en programas de bienestar y NOM-035 en M&eacute;xico. No es &laquo;cl&iacute;nica "
                    "light&raquo;: requiere competencia en trabajo interdisciplinar y comunicaci&oacute;n con m&eacute;dicos.</p>\n"
                    "<p>Si su paciente cl&iacute;nico tiene comorbilidad m&eacute;dica severa, integre t&eacute;cnicas de "
                    "salud sin abandonar tratamiento mental.</p>\n"
                ),
            },
            {
                "h2": "Solapamiento, derivaci&oacute;n y expediente",
                "html": (
                    "<p>Muchos profesionales ejercen ambos roles seg&uacute;n caso. Defina en su sitio web y consentimiento "
                    "qu&eacute; servicios ofrece para evitar expectativas incorrectas.</p>\n"
                    "<p>Derive a cl&iacute;nica especializada si detecta trastorno grave en programa de salud; derive a salud "
                    "p&uacute;blica o educaci&oacute;n si el paciente cl&iacute;nico necesita rehabilitaci&oacute;n cardiaca "
                    "estructurada.</p>\n"
                    f"<p>{kalyo('psicologia-clinica-vs-salud')} permite separar plantillas de nota para programa de "
                    "salud versus psicoterapia sin duplicar expedientes.</p>\n"
                    "<p>Registre colaboraciones con otros profesionales con consentimiento del paciente y canal seguro.</p>\n"
                ),
            },
        ],
        "faqs": [
            {
                "q": "&iquest;Son dos licencias distintas?",
                "a": "En la mayoría de países LATAM es la misma formación base; la especialización define el rol. Marketing debe ser honesto.",
            },
            {
                "q": "&iquest;Qui&eacute;n atiende dolor cr&oacute;nico?",
                "a": "Ambos pueden: clínico desde salud mental; de la salud desde adherencia y estilo de vida. Colaboren.",
            },
            {
                "q": "&iquest;La salud mental es solo clínica?",
                "a": "No. Promoción y prevención son psicología de la salud y salud pública; tratamiento de trastorno es clínica.",
            },
            {
                "q": "&iquest;Puedo facturar igual en ambos?",
                "a": "Depende de códigos y convenios locales. Documente el tipo de intervención en factura e informe.",
            },
            {
                "q": "&iquest;Dónde me capacito en salud?",
                "a": "Posgrados en psicología de la salud, hospitales universitarios y certificaciones en enfermedad crónica.",
            },
        ],
        "related": [
            {"href": "/articulos/alianza-terapeutica.html", "label": "Alianza terap&eacute;utica"},
            {"href": "/articulos/psicologo-vs-psiquiatra-diferencias.html", "label": "Psic&oacute;logo vs psiquiatra"},
            {"href": "/articulos/nom-035-ssa3-salud-mental-trabajo.html", "label": "NOM-035"},
            {"href": "/articulos/depresion-tratamiento-psicologico.html", "label": "Depresi&oacute;n tratamiento"},
        ],
    },
    {
        "slug": "emdr-vs-tcc-trauma",
        "title": "EMDR vs TCC para trauma: evidencia clínica 2026 | Kalyo",
        "description": "EMDR vs TCC para trauma: evidencia, fases, duración y cuándo elegir cada intervención en TEPT. Tabla comparativa para psicólogos en México y Colombia.",
        "keywords": "emdr, terapia emdr, TCC trauma, TEPT, terapia cognitivo conductual trauma",
        "h1": "EMDR vs TCC para trauma y TEPT",
        "breadcrumb_short": "EMDR vs TCC trauma",
        "hero_alt": "Comparativa EMDR y TCC en tratamiento de trauma",
        "inline_alt": "Tabla EMDR versus TCC para TEPT",
        "meta_label": "Trauma &middot; Comparativa 2026",
        "date_published": "2026-11-16",
        "date_modified": "2026-11-16",
        "quick_answer": "<strong>EMDR</strong> (desensibilizaci&oacute;n y reprocesamiento) usa estimulaci&oacute;n bilateral y protocolo de fases para procesar memorias traum&aacute;ticas. La <strong>TCC para trauma</strong> (p. ej. exposici&oacute;n prolongada, CPT) trabaja cogniciones y exposici&oacute;n narrativa con fuerte evidencia en TEPT. Gu&iacute;as citan ambas como opciones de primera l&iacute;nea; elija por formaci&oacute;n, preferencia del paciente y complejidad del caso. Vea <a href=\"/articulos/terapia-emdr.html\">terapia EMDR</a> y <a href=\"/articulos/cie-11-tept-trauma-codigos.html\">TEPT CIE-11</a>.",
        "intro_long": "Comparar <strong>EMDR y TCC para trauma</strong> ayuda a elegir protocolo sin prometer curas m&aacute;gicas ni ignorar evidencia publicada. Esta gu&iacute;a contrasta fases, mecanismos, estudios y criterios cl&iacute;nicos en TEPT, con tabla para respuestas directas en b&uacute;squedas. Complementa <a href=\"/articulos/terapia-emdr.html\">terapia EMDR</a> y <a href=\"/articulos/cie-11-tept-trauma-codigos.html\">c&oacute;digos TEPT</a> para documentaci&oacute;n y derivaci&oacute;n segura en consultorio latinoamericano.",
        "cta_h2": "Registra evaluaciones de trauma en Kalyo",
        "cta_p": "Expediente, escalas y notas &mdash; kalyo.io",
        "card_title": "EMDR vs TCC para trauma",
        "card_p": "Evidencia, fases y cuándo elegir cada protocolo.",
        "after_href": "/articulos/terapia-emdr.html",
        "after_loc": "https://kalyo.io/articulos/terapia-emdr.html",
        "asset_from": "cie-11-tept-trauma-codigos",
        "sections": [
            {
                "h2": "Tabla comparativa EMDR vs TCC para trauma",
                "html": (
                    '<table class="items-table">\n'
                    "<thead><tr><th>Aspecto</th><th>EMDR</th><th>TCC trauma (EP/CPT)</th></tr></thead>\n"
                    "<tbody>\n"
                    "<tr><td>Enfoque</td><td>Reprocesamiento de memorias</td>"
                    "<td>Exposici&oacute;n y reestructuraci&oacute;n cognitiva</td></tr>\n"
                    "<tr><td>Fases</td><td>8 fases estandarizadas</td>"
                    "<td>Psicoeducaci&oacute;n, exposici&oacute;n, cogniciones</td></tr>\n"
                    "<tr><td>Sesi&oacute;n tipo</td><td>Movimientos o taps + target</td>"
                    "<td>Narrativa repetida / escritura</td></tr>\n"
                    "<tr><td>Evidencia TEPT</td><td>Fuerte en adultos</td>"
                    "<td>Fuerte; referencia en gu&iacute;as VA/APA</td></tr>\n"
                    "<tr><td>Contraindicaciones relativas</td><td>Disociaci&oacute;n sin estabilizar</td>"
                    "<td>Evitaci&oacute;n extrema sin preparaci&oacute;n</td></tr>\n"
                    "</tbody></table>\n" + TABLE_TAIL
                ),
            },
            {
                "h2": "Terapia EMDR: protocolo y seguridad",
                "html": (
                    "<p><strong>EMDR</strong> requiere entrenamiento oficial y adherencia a fases (historia, preparaci&oacute;n, "
                    "evaluaci&oacute;n, desensibilizaci&oacute;n, instalaci&oacute;n, escaneo corporal, cierre, reevaluaci&oacute;n). "
                    "No es hipnosis ni solo movimiento ocular: integra cognici&oacute;n, afecto y sensaci&oacute;n corporal.</p>\n"
                    "<p>Estabilice recursos y disociaci&oacute;n antes de abrir memorias. En trauma complejo o abuso prolongado, "
                    "alargue preparaci&oacute;n. Documente SUD y VOC seg&uacute;n protocolo.</p>\n"
                    "<p>Ampl&iacute;e en <a href=\"/articulos/terapia-emdr.html\">gu&iacute;a de terapia EMDR</a>.</p>\n"
                ),
            },
            {
                "h2": "TCC orientada a trauma",
                "html": (
                    "<p>La <strong>terapia cognitivo conductual</strong> para TEPT usa exposici&oacute;n prolongada, terapia "
                    "cognitiva de procesamiento (CPT) o modelos similares. El paciente confronta narrativa evitada y "
                    "cuestiona cogniciones de culpa o mundo peligroso.</p>\n"
                    "<p>Exige tolerancia a activaci&oacute;n fisiol&oacute;gica durante tarea. Psicoeducaci&oacute;n sobre "
                    "respuesta de alarma es clave. Monitoree con PCL-5 o similar cada pocas sesiones.</p>\n"
                    "<p>Combine con manejo de sueño e irritabilidad; no trate TEPT aislado de comorbilidad si existe.</p>\n"
                ),
            },
            {
                "h2": "Elegir protocolo y codificar TEPT",
                "html": (
                    "<p>Si el paciente rechaza exposici&oacute;n narrativa prolongada, EMDR puede ser alternativa aceptable "
                    "con mismo nivel de evidencia en muchas gu&iacute;as. Si prefiere estructura cognitiva expl&iacute;cita, "
                    "CPT puede encajar mejor. La preferencia importa en adherencia.</p>\n"
                    "<p>Documente criterios TEPT seg&uacute;n manual usado; en reportes oficiales vea "
                    "<a href=\"/articulos/cie-11-tept-trauma-codigos.html\">TEPT y c&oacute;digos CIE-11</a>. "
                    "Eval&uacute;e riesgo suicida y abuso actual antes de cualquier protocolo.</p>\n"
                    f"<p>{kalyo('emdr-vs-tcc-trauma')} ayuda a registrar escalas de trauma, fases completadas y planes "
                    "de seguridad.</p>\n"
                    "<p>No prometa borrado de memoria: ambas terapias buscan integraci&oacute;n funcional, no amnesia.</p>\n"
                ),
            },
        ],
        "faqs": [
            {
                "q": "&iquest;EMDR es m&aacute;s r&aacute;pida que TCC?",
                "a": "La duración depende de complejidad del trauma. Algunos casos únicos resuelven en pocas sesiones; trauma complejo requiere meses en ambos.",
            },
            {
                "q": "&iquest;Puedo hacer EMDR sin certificación?",
                "a": "No es ético ni seguro. Busque entrenamiento nivel I/II reconocido y supervisión.",
            },
            {
                "q": "&iquest;TCC para trauma sirve en niños?",
                "a": "Hay adaptaciones (TF-CBT). EMDR también tiene protocolos infantiles con formación específica.",
            },
            {
                "q": "&iquest;Cuál elige la guía clínica?",
                "a": "Muchas listan EMDR, TCC trauma y EMDR como equivalentes de primera línea; el factor decisivo es competencia del terapeuta.",
            },
            {
                "q": "&iquest;Combinar ambas?",
                "a": "Evite mezclar protocolos en la misma sesión sin modelo claro. Secuencie estabilización y luego un protocolo principal.",
            },
        ],
        "related": [
            {"href": "/articulos/terapia-emdr.html", "label": "Terapia EMDR"},
            {"href": "/articulos/cie-11-tept-trauma-codigos.html", "label": "TEPT CIE-11"},
            {"href": "/articulos/terapia-cognitivo-conductual-guia.html", "label": "Gu&iacute;a TCC"},
            {"href": "/articulos/primeros-auxilios-psicologicos.html", "label": "Primeros auxilios"},
        ],
    },
    {
        "slug": "hipnosis-clinica-vs-relajacion",
        "title": "Técnicas de relajación vs hipnosis clínica 2026 | Kalyo",
        "description": "Técnicas de relajación vs hipnosis clínica: mecanismos, indicaciones, límites éticos y evidencia en ansiedad, dolor y hábitos. Tabla comparativa práctica.",
        "keywords": "tecnicas de relajacion, hipnosis clinica, relajación vs hipnosis, intervención ansiedad",
        "h1": "Técnicas de relajación vs hipnosis clínica",
        "breadcrumb_short": "Relajación vs hipnosis",
        "hero_alt": "Comparativa técnicas de relajación e hipnosis clínica",
        "inline_alt": "Tabla relajación versus hipnosis clínica",
        "meta_label": "Intervenci&oacute;n &middot; Comparativa 2026",
        "date_published": "2026-11-16",
        "date_modified": "2026-11-16",
        "quick_answer": "Las <strong>t&eacute;cnicas de relajaci&oacute;n</strong> (respiraci&oacute;n, PMR, mindfulness breve) bajan activaci&oacute;n fisiol&oacute;gica y son puerta de entrada universal en ansiedad e insomnio. La <strong>hipnosis cl&iacute;nica</strong> usa absorci&oacute;n focalizada y sugestiones terap&eacute;uticas dentro de marco &eacute;tico; no es espect&aacute;culo ni p&eacute;rdida de control. La relajaci&oacute;n puede usarse sola; la hipnosis requiere formaci&oacute;n y consentimiento expl&iacute;cito. Vea <a href=\"/articulos/nota-evolucion-soap-psicologia.html\">documentaci&oacute;n cl&iacute;nica</a>.",
        "intro_long": "Confundir <strong>t&eacute;cnicas de relajaci&oacute;n con hipnosis cl&iacute;nica</strong> lleva a promesas irreales o a subutilizar herramientas basales en ansiedad. Esta gu&iacute;a compara mecanismos, indicaciones, riesgos y evidencia en consultorio, con tabla directa. Complementa buenas pr&aacute;cticas de <a href=\"/articulos/nota-soap-vs-nota-evolucion-libre.html\">nota SOAP</a> y documentaci&oacute;n en <a href=\"/articulos/nota-evolucion-soap-psicologia.html\">evoluci&oacute;n cl&iacute;nica</a> para registrar t&eacute;cnicas sin caer en lenguaje pseudocient&iacute;fico.",
        "cta_h2": "Registra técnicas aplicadas en Kalyo",
        "cta_p": "Notas SOAP, plan y seguimiento &mdash; kalyo.io",
        "card_title": "Relajación vs hipnosis clínica",
        "card_p": "Mecanismos, indicaciones y límites éticos en consulta.",
        "after_href": "/articulos/nota-soap-vs-nota-evolucion-libre.html",
        "after_loc": "https://kalyo.io/articulos/nota-soap-vs-nota-evolucion-libre.html",
        "asset_from": "alianza-terapeutica",
        "sections": [
            {
                "h2": "Tabla comparativa t&eacute;cnicas de relajaci&oacute;n vs hipnosis cl&iacute;nica",
                "html": (
                    '<table class="items-table">\n'
                    "<thead><tr><th>Aspecto</th><th>Relajaci&oacute;n</th><th>Hipnosis cl&iacute;nica</th></tr></thead>\n"
                    "<tbody>\n"
                    "<tr><td>Estado</td><td>Calma activa, menor activaci&oacute;n</td>"
                    "<td>Absorci&oacute;n focalizada + sugesti&oacute;n</td></tr>\n"
                    "<tr><td>Formaci&oacute;n</td><td>B&aacute;sica en grado/pósgrado</td>"
                    "<td>Curso especializado y supervisi&oacute;n</td></tr>\n"
                    "<tr><td>Indicaciones</td><td>Ansiedad, insomnio, estrés</td>"
                    "<td>Dolor, ansiedad, h&aacute;bitos (con evidencia)</td></tr>\n"
                    "<tr><td>Riesgos</td><td>Bajos; evitar en trauma agudo sin cuidado</td>"
                    "<td>False memories si mal usada; siempre voluntaria</td></tr>\n"
                    "<tr><td>Evidencia</td><td>Alta como componente TCC</td>"
                    "<td>Moderada seg&uacute;n indicaci&oacute;n</td></tr>\n"
                    "</tbody></table>\n" + TABLE_TAIL
                ),
            },
            {
                "h2": "T&eacute;cnicas de relajaci&oacute;n en la pr&aacute;ctica",
                "html": (
                    "<p>Las <strong>t&eacute;cnicas de relajaci&oacute;n</strong> incluyen respiraci&oacute;n diafragmática, "
                    "relajación muscular progresiva, imaginería tranquila y mindfulness breve. Son hijas de acceso en TCC "
                    "y en psicología de la salud.</p>\n"
                    "<p>Enseñe con demo en sesión y audio grabado para casa. Mida adherencia en Plan de nota SOAP. "
                    "No sustituyen exposición en fobias: preparan, no curan solas.</p>\n"
                    "<p>En trauma, la relajación puede disparar sensaciones corporales: vaya despacio y priorice "
                    "psicoeducación sobre ventana de tolerancia.</p>\n"
                ),
            },
            {
                "h2": "Hipnosis cl&iacute;nica: marco &eacute;tico y uso",
                "html": (
                    "<p>La <strong>hipnosis clínica</strong> es un procedimiento consentido donde el paciente mantiene "
                    "control y puede salir del estado focalizado. Las sugestiones apuntan a analgesia, ansiedad, "
                    "n&aacute;usea médica o preparación para procedimientos — no a “resetear” personalidad.</p>\n"
                    "<p>Evite espectáculos en redes y grabaciones sin consentimiento. Documente qué sugestión usó y "
                    "respuesta subjetiva. No trabaje memorias forenses con hipnosis: riesgo de contaminación.</p>\n"
                    "<p>Si no tiene certificación, remita o limítese a relajación estructurada sin llamarla hipnosis.</p>\n"
                ),
            },
            {
                "h2": "Integraci&oacute;n en psicoterapia y notas",
                "html": (
                    "<p>Muchas terapias integran relajación como tarea entre sesiones y hipnosis puntual para dolor "
                    "procedimental o fobia específica dentro de protocolo mayor.</p>\n"
                    "<p>Registre en Objetivo/Plan de <a href=\"/articulos/nota-evolucion-soap-psicologia.html\">nota SOAP</a>: "
                    "técnica, duración, respuesta y tarea. Compare formatos en "
                    "<a href=\"/articulos/nota-soap-vs-nota-evolucion-libre.html\">SOAP vs nota libre</a>.</p>\n"
                    f"<p>{kalyo('hipnosis-clinica-vs-relajacion')} guarda plantillas de plan y seguimiento de tareas "
                    "de regulación fisiológica.</p>\n"
                    "<p>Psicoeducación honesta: ninguna técnica reemplaza evaluación de trastorno de base ni "
                    "tratamiento evidenciado cuando hay severidad.</p>\n"
                ),
            },
        ],
        "faqs": [
            {
                "q": "&iquest;La hipnosis es peligrosa?",
                "a": "En manos formadas y con consentimiento, es segura. El riesgo sube con pseudociencia, falsas memorias o uso forense.",
            },
            {
                "q": "&iquest;Todos son hipnotizables?",
                "a": "Hay variabilidad. La relajación funciona en casi todos con adaptación; hipnosis profunda no es requisito terapéutico.",
            },
            {
                "q": "&iquest;Relajación basta para TEPT?",
                "a": "No como monoterapia. Puede ser auxiliar de estabilización antes de EMDR o TCC trauma.",
            },
            {
                "q": "&iquest;Puedo vender hipnosis en redes?",
                "a": "Evite promesas milagrosas. Marca regulatoria y colegios pueden sancionar publicidad engañosa.",
            },
            {
                "q": "&iquest;Grabar audios para pacientes?",
                "a": "Sí con consentimiento y sin datos identificables en el archivo compartido.",
            },
        ],
        "related": [
            {"href": "/articulos/nota-soap-vs-nota-evolucion-libre.html", "label": "SOAP vs nota libre"},
            {"href": "/articulos/nota-evolucion-soap-psicologia.html", "label": "Nota SOAP"},
            {"href": "/articulos/terapia-cognitivo-conductual-guia.html", "label": "Gu&iacute;a TCC"},
            {"href": "/articulos/alianza-terapeutica.html", "label": "Alianza terap&eacuteutica"},
        ],
    },
]