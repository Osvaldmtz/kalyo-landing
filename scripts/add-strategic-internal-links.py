#!/usr/bin/env python3
"""Add strategic internal links for GSC priority articles."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EDITS: list[tuple[str, str, str]] = [
    # Unknown: gad-2
    (
        "articulos/ghq-12-cuestionario-salud-general.html",
        "instrumentos m&aacute;s espec&iacute;ficos como el <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a> o el <a href=\"/articulos/escala-dass-21.html\">DASS-21</a>.",
        "instrumentos m&aacute;s espec&iacute;ficos como el <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a>, el <a href=\"/articulos/gad-2-tamizaje-ansiedad-breve.html\">GAD-2</a>, el <a href=\"/articulos/stai-ansiedad-estado-rasgo.html\">STAI</a> o el <a href=\"/articulos/escala-dass-21.html\">DASS-21</a>.",
    ),
    (
        "articulos/stai-ansiedad-estado-rasgo.html",
        "Los resultados deben triangularse con otras evaluaciones (entrevista cl&iacute;nica, escalas complementarias, historia cl&iacute;nica) para fundamentar un diagn&oacute;stico y plan de intervenci&oacute;n.",
        "Los resultados deben triangularse con otras evaluaciones (entrevista cl&iacute;nica, escalas complementarias como el <a href=\"/articulos/gad-2-tamizaje-ansiedad-breve.html\">GAD-2</a>, la <a href=\"/articulos/lsas-ansiedad-social-liebowitz.html\">LSAS</a> o la <a href=\"/articulos/pdss-trastorno-panico-shear.html\">PDSS</a>, e historia cl&iacute;nica) para fundamentar un diagn&oacute;stico y plan de intervenci&oacute;n.",
    ),
    (
        "articulos/que-es-el-gad-7.html",
        "Para consultas a&uacute;n m&aacute;s breves, el <a href=\"/articulos/gad-2-tamizaje-ansiedad-breve.html\">GAD-2</a> utiliza los dos primeros &iacute;tems del GAD-7 como puerta de entrada.",
        "Para consultas a&uacute;n m&aacute;s breves, el <a href=\"/articulos/gad-2-tamizaje-ansiedad-breve.html\">GAD-2</a> utiliza los dos primeros &iacute;tems del GAD-7 como puerta de entrada; el <a href=\"/articulos/stai-ansiedad-estado-rasgo.html\">STAI</a> aporta la distinci&oacute;n estado-rasgo cuando se requiere mayor profundidad.",
    ),
    # Unknown: lsas
    (
        "articulos/ghq-12-cuestionario-salud-general.html",
        "Un puntaje &ge;3 activa la recomendaci&oacute;n de evaluaci&oacute;n cl&iacute;nica m&aacute;s detallada, preferiblemente con instrumentos espec&iacute;ficos de depresi&oacute;n, ansiedad y estr&eacute;s.",
        "Un puntaje &ge;3 activa la recomendaci&oacute;n de evaluaci&oacute;n cl&iacute;nica m&aacute;s detallada, preferiblemente con instrumentos espec&iacute;ficos de depresi&oacute;n, ansiedad (como la <a href=\"/articulos/lsas-ansiedad-social-liebowitz.html\">LSAS</a> cuando predomina ansiedad social) y estr&eacute;s.",
    ),
    (
        "articulos/stai-ansiedad-estado-rasgo.html",
        "Esta diferenciaci&oacute;n te&oacute;rica es fundamental para la evaluaci&oacute;n cl&iacute;nica, pues permite identificar si la ansiedad es una respuesta contextual o un patr&oacute;n persistente que requiere intervenci&oacute;n terap&eacute;utica especializada.",
        "Esta diferenciaci&oacute;n te&oacute;rica es fundamental para la evaluaci&oacute;n cl&iacute;nica, pues permite identificar si la ansiedad es una respuesta contextual o un patr&oacute;n persistente que requiere intervenci&oacute;n terap&eacute;utica especializada. Cuando el cuadro sugiere ansiedad social m&aacute;s que ansiedad generalizada, la <a href=\"/articulos/lsas-ansiedad-social-liebowitz.html\">LSAS de Liebowitz</a> suele ser el siguiente paso.",
    ),
    (
        "articulos/test-beck-ansiedad-bai.html",
        "Esto lo convierte en una herramienta especialmente &uacute;til cuando se sospecha de trastorno de p&aacute;nico o ansiedad con fuerte componente fisiol&oacute;gico.",
        "Esto lo convierte en una herramienta especialmente &uacute;til cuando se sospecha de trastorno de p&aacute;nico o ansiedad con fuerte componente fisiol&oacute;gico; en ese perfil, la <a href=\"/articulos/pdss-trastorno-panico-shear.html\">PDSS de Sheehan</a> complementa el BAI para cuantificar severidad y seguimiento.",
    ),
    # Unknown: alternativas-doctoralia
    (
        "articulos/software-para-psicologos-clinicos.html",
        "Utilizar hojas de c&aacute;lculo, documentos de texto o incluso libretas f&iacute;sicas puede funcionar temporalmente, pero estas soluciones improvisadas se vuelven insostenibles conforme crece el n&uacute;mero de pacientes.",
        "Utilizar hojas de c&aacute;lculo, documentos de texto o incluso libretas f&iacute;sicas puede funcionar temporalmente, pero estas soluciones improvisadas se vuelven insostenibles conforme crece el n&uacute;mero de pacientes. Si hoy dependes de directorios o agendas externas, conviene comparar <a href=\"/articulos/alternativas-a-doctoralia-para-psicologos.html\">alternativas a Doctoralia</a> que integren evaluaci&oacute;n y expediente cl&iacute;nico.",
    ),
    (
        "articulos/alternativas-elo-psicologos-mexico.html",
        "En esta gu&iacute;a comparamos las principales alternativas disponibles en 2026 para que elijas la plataforma que mejor se adapte a tu pr&aacute;ctica.</p>",
        "En esta gu&iacute;a comparamos las principales alternativas disponibles en 2026 para que elijas la plataforma que mejor se adapte a tu pr&aacute;ctica. Si tambi&eacute;n eval&uacute;as directorios de pacientes, revisa nuestra comparativa de <a href=\"/articulos/alternativas-a-doctoralia-para-psicologos.html\">alternativas a Doctoralia</a>.</p>",
    ),
    # Unknown: teleconsulta
    (
        "articulos/nom-004-historia-clinica-mexico.html",
        "Para un consultorio de psicolog&iacute;a que digitaliza historias cl&iacute;nicas, la NOM-024 implica elegir herramientas que no solo almacenen notas de sesi&oacute;n, sino que documenten qui&eacute;n accedi&oacute; al expediente, cu&aacute;ndo se modific&oacute; y c&oacute;mo se protege la confidencialidad de los datos.",
        "Para un consultorio de psicolog&iacute;a que digitaliza historias cl&iacute;nicas o presta <a href=\"/articulos/teleconsulta-para-psicologos-latinoamerica.html\">teleconsulta</a>, la NOM-024 implica elegir herramientas que no solo almacenen notas de sesi&oacute;n, sino que documenten qui&eacute;n accedi&oacute; al expediente, cu&aacute;ndo se modific&oacute; y c&oacute;mo se protege la confidencialidad de los datos.",
    ),
    (
        "articulos/consentimiento-informado-psicologia.html",
        "En psicolog&iacute;a cl&iacute;nica, el consentimiento informado cumple funciones espec&iacute;ficas que lo distinguen del consentimiento en otras &aacute;reas de la salud: establece los l&iacute;mites de la confidencialidad, define el encuadre terap&eacute;utico y anticipa situaciones en las que el psic&oacute;logo podr&iacute;a verse obligado a romper el secreto profesional.",
        "En psicolog&iacute;a cl&iacute;nica, el consentimiento informado cumple funciones espec&iacute;ficas que lo distinguen del consentimiento en otras &aacute;reas de la salud: establece los l&iacute;mites de la confidencialidad, define el encuadre terap&eacute;utico (presencial o en <a href=\"/articulos/teleconsulta-para-psicologos-latinoamerica.html\">teleconsulta</a>) y anticipa situaciones en las que el psic&oacute;logo podr&iacute;a verse obligado a romper el secreto profesional.",
    ),
    # Unknown: nom-047
    (
        "articulos/nom-004-historia-clinica-mexico.html",
        "Para el psic&oacute;logo en consulta privada o institucional, comprender c&oacute;mo se relacionan estas tres normas es clave para documentar con respaldo legal.",
        "Para el psic&oacute;logo en consulta privada o institucional, comprender c&oacute;mo se relacionan estas tres normas es clave para documentar con respaldo legal. En atenci&oacute;n a adolescentes, la <a href=\"/articulos/nom-047-ssa2-salud-mental-adolescentes.html\">NOM-047-SSA2</a> complementa la NOM-004 con criterios espec&iacute;ficos de salud mental.",
    ),
    (
        "articulos/ley-1090-psicologia-colombia.html",
        "La evaluaci&oacute;n psicol&oacute;gica con fines laborales, forenses o educativos requiere competencias adicionales y, en algunos casos, certificaciones espec&iacute;ficas.",
        "La evaluaci&oacute;n psicol&oacute;gica con fines laborales, forenses o educativos requiere competencias adicionales y, en algunos casos, certificaciones espec&iacute;ficas. En atenci&oacute;n a menores, es &uacute;til contrastar el marco colombiano con referentes regionales como la <a href=\"/articulos/nom-047-ssa2-salud-mental-adolescentes.html\">NOM-047 de salud mental en adolescentes (M&eacute;xico)</a> cuando se trabaja con familias binacionales o equipos interdisciplinarios.",
    ),
    # Unknown: pdss
    (
        "articulos/lsas-ansiedad-social-liebowitz.html",
        "No obstante, la interpretaci&oacute;n debe integrar informaci&oacute;n cl&iacute;nica adicional, historia del paciente y evaluaci&oacute;n de criterios diagn&oacute;sticos del DSM-5 o ICD-11 seg&uacute;n corresponda, ya que la puntuaci&oacute;n por s&iacute; sola no es suficiente para establecer un diagn&oacute;stico.",
        "No obstante, la interpretaci&oacute;n debe integrar informaci&oacute;n cl&iacute;nica adicional, historia del paciente y evaluaci&oacute;n de criterios diagn&oacute;sticos del DSM-5 o ICD-11 seg&uacute;n corresponda, ya que la puntuaci&oacute;n por s&iacute; sola no es suficiente para establecer un diagn&oacute;stico. Si coexisten ataques de p&aacute;nico, la <a href=\"/articulos/pdss-trastorno-panico-shear.html\">PDSS</a> ayuda a cuantificar severidad y respuesta al tratamiento.",
    ),
    # Unknown: asrm
    (
        "articulos/mdq-trastorno-bipolar-tamizaje.html",
        "Un resultado positivo en el MDQ (7 o m&aacute;s s&iacute;ntomas que co-ocurren m&aacute;s de una vez, con impacto funcional) sugiere posible trastorno bipolar tipo I o II, o ciclotimia.",
        "Un resultado positivo en el MDQ (7 o m&aacute;s s&iacute;ntomas que co-ocurren m&aacute;s de una vez, con impacto funcional) sugiere posible trastorno bipolar tipo I o II, o ciclotimia. Como tamizaje breve complementario de man&iacute;a, la <a href=\"/articulos/asrm-escala-mania-altman.html\">ASRM de Altman</a> puede readministrarse en seguimiento.",
    ),
    (
        "articulos/ymrs-escala-mania-young.html",
        "El instrumento tampoco proporciona informaci&oacute;n sobre s&iacute;ntomas de depresi&oacute;n o sobre funcionamiento cognitivo y psicosocial m&aacute;s all&aacute; del humor.",
        "El instrumento tampoco proporciona informaci&oacute;n sobre s&iacute;ntomas de depresi&oacute;n o sobre funcionamiento cognitivo y psicosocial m&aacute;s all&aacute; del humor. Para monitorizar s&iacute;ntomas man&iacute;acos en autoinforme entre consultas, la <a href=\"/articulos/asrm-escala-mania-altman.html\">ASRM</a> es una alternativa breve y complementaria al YMRS.",
    ),
    # Discovered: asq
    (
        "articulos/evaluacion-riesgo-suicida.html",
        "Las plataformas digitales cl&iacute;nicas pueden facilitar la evaluaci&oacute;n sistem&aacute;tica del riesgo suicida de varias maneras. En primer lugar, la aplicaci&oacute;n digital de escalas como la C-SSRS o el PHQ-9 garantiza que la calificaci&oacute;n sea correcta y que las alertas se activen autom&aacute;ticamente cuando se detectan puntuaciones de riesgo.",
        "Las plataformas digitales cl&iacute;nicas pueden facilitar la evaluaci&oacute;n sistem&aacute;tica del riesgo suicida de varias maneras. En primer lugar, la aplicaci&oacute;n digital de escalas como la C-SSRS, el <a href=\"/articulos/asq-tamizaje-suicidio-pediatrico.html\">ASQ pedi&aacute;trico</a> o el PHQ-9 garantiza que la calificaci&oacute;n sea correcta y que las alertas se activen autom&iacute;ticamente cuando se detectan puntuaciones de riesgo.",
    ),
    # Discovered: aq-10
    (
        "articulos/ados-2-evaluacion-tea.html",
        "El ADOS-2 est&aacute; indicado cuando existe sospecha cl&iacute;nica de Trastorno del Espectro Autista basada en preocupaciones de padres, educadores o profesionales de salud. Es especialmente &uacute;til en evaluaciones de ni&ntilde;os con retrasos en el desarrollo, dificultades de comunicaci&oacute;n social, o patrones conductuales inusuales. Tambi&eacute;n es apropiado en evaluaciones de diagn&oacute;stico diferencial cuando se requiere excluir o confirmar autismo.",
        "El ADOS-2 est&aacute; indicado cuando existe sospecha cl&iacute;nica de Trastorno del Espectro Autista basada en preocupaciones de padres, educadores o profesionales de salud. Antes de la evaluaci&oacute;n observacional completa, tamizajes como el <a href=\"/articulos/aq-10-cociente-autista-tamizaje.html\">AQ-10</a> orientan la priorizaci&oacute;n del caso. Es especialmente &uacute;til en evaluaciones de ni&ntilde;os con retrasos en el desarrollo, dificultades de comunicaci&oacute;n social, o patrones conductuales inusuales. Tambi&eacute;n es apropiado en evaluaciones de diagn&oacute;stico diferencial cuando se requiere excluir o confirmar autismo.",
    ),
    (
        "articulos/evaluacion-tea-ninos-colombia.html",
        "La evaluaci&oacute;n no se limita a confirmar o descartar un diagn&oacute;stico, sino que proporciona informaci&oacute;n crucial sobre el perfil de fortalezas y necesidades del ni&ntilde;o, permitiendo dise&ntilde;ar intervenciones personalizadas.",
        "La evaluaci&oacute;n no se limita a confirmar o descartar un diagn&oacute;stico, sino que proporciona informaci&oacute;n crucial sobre el perfil de fortalezas y necesidades del ni&ntilde;o, permitiendo dise&ntilde;ar intervenciones personalizadas. En etapas tempranas, el <a href=\"/articulos/aq-10-cociente-autista-tamizaje.html\">AQ-10</a> funciona como filtro breve antes de bater&iacute;as m&aacute;s extensas.",
    ),
    (
        "articulos/ruta-atencion-tea-colombia.html",
        "Su objetivo es facilitar el acceso oportuno a evaluaci&oacute;n diagn&oacute;stica, intervenciones basadas en evidencia y apoyo psicosocial para personas con autismo y sus familias.",
        "Su objetivo es facilitar el acceso oportuno a evaluaci&oacute;n diagn&oacute;stica, intervenciones basadas en evidencia y apoyo psicosocial para personas con autismo y sus familias. En primer contacto, tamizajes como el <a href=\"/articulos/aq-10-cociente-autista-tamizaje.html\">AQ-10</a> ayudan a decidir derivaci&oacute;n o seguimiento.",
    ),
    # Discovered: trastornos-neurodesarrollo
    (
        "articulos/ados-2-evaluacion-tea.html",
        "No. El ADOS-2 es una herramienta valiosa de apoyo diagn&oacute;stico, pero no debe utilizarse como &uacute;nico instrumento de diagn&oacute;stico. El diagn&oacute;stico del TEA requiere evaluaci&oacute;n integral que incluya historia del desarrollo, evaluaci&oacute;n cognitiva, evaluaci&oacute;n del lenguaje, informes de padres (como ADI-R), y consideraci&oacute;n del contexto cl&iacute;nico completo.",
        "No. El ADOS-2 es una herramienta valiosa de apoyo diagn&oacute;stico, pero no debe utilizarse como &uacute;nico instrumento de diagn&oacute;stico. Para diferenciar TEA, TDAH, DI y TDL, consulte la gu&iacute;a de <a href=\"/articulos/trastornos-neurodesarrollo-tipos.html\">trastornos del neurodesarrollo</a>. El diagn&oacute;stico del TEA requiere evaluaci&oacute;n integral que incluya historia del desarrollo, evaluaci&oacute;n cognitiva, evaluaci&oacute;n del lenguaje, informes de padres (como ADI-R), y consideraci&oacute;n del contexto cl&iacute;nico completo.",
    ),
    (
        "articulos/evaluacion-tea-ninos-colombia.html",
        "Tambi&eacute;n es relevante evaluar aspectos espec&iacute;ficos del neurodesarrollo mediante pruebas de funci&oacute;n ejecutiva, flexibilidad cognitiva y procesamiento visoespacial.",
        "Tambi&eacute;n es relevante evaluar aspectos espec&iacute;ficos del neurodesarrollo mediante pruebas de funci&oacute;n ejecutiva, flexibilidad cognitiva y procesamiento visoespacial, junto con un <a href=\"/articulos/trastornos-neurodesarrollo-tipos.html\">diagn&oacute;stico diferencial entre trastornos del neurodesarrollo</a>.",
    ),
    (
        "articulos/ruta-atencion-tea-colombia.html",
        "La coordinaci&oacute;n entre profesionales incluye reuniones de caso, compartir hallazgos, unificar criterios diagn&oacute;sticos y asegurar coherencia en recomendaciones. Esto es especialmente importante cuando existen hallazgos discordantes o cuando la presentaci&oacute;nica es atipica.",
        "La coordinaci&oacute;n entre profesionales incluye reuniones de caso, compartir hallazgos, unificar criterios diagn&oacute;sticos y asegurar coherencia en recomendaciones. Esto es especialmente importante cuando existen hallazgos discordantes o cuando la presentaci&oacute;n es at&iacute;pica; en esos casos, la gu&iacute;a de <a href=\"/articulos/trastornos-neurodesarrollo-tipos.html\">trastornos del neurodesarrollo</a> orienta el diagn&oacute;stico diferencial.",
    ),
    # Discovered: escala-madrs
    (
        "articulos/inventario-depresion-beck-bdi.html",
        "El PHQ-9 es ideal para el tamizaje r&aacute;pido en atenci&oacute;n primaria y para el seguimiento peri&oacute;dico en consultas con alta demanda. El BDI-II es preferible en contextos de evaluaci&oacute;n cl&iacute;nica especializada, en investigaci&oacute;n donde se requiere una medici&oacute;n detallada de la severidad y en el monitoreo del tratamiento en entornos de psicoterapia donde se dispone de tiempo suficiente para una evaluaci&oacute;n m&aacute;s profunda.",
        "El PHQ-9 es ideal para el tamizaje r&aacute;pido en atenci&oacute;n primaria y para el seguimiento peri&oacute;dico en consultas con alta demanda. En psiquiatr&iacute;a y ensayos cl&iacute;nicos, la <a href=\"/articulos/escala-madrs-depresion.html\">MADRS</a> suele preferirse para cuantificar cambio sintom&aacute;tico con mayor sensibilidad. El BDI-II es preferible en contextos de evaluaci&oacute;n cl&iacute;nica especializada, en investigaci&oacute;n donde se requiere una medici&oacute;n detallada de la severidad y en el monitoreo del tratamiento en entornos de psicoterapia donde se dispone de tiempo suficiente para una evaluaci&oacute;n m&aacute;s profunda.",
    ),
    (
        "articulos/phq-2-tamizaje-depresion-breve.html",
        "Otros instrumentos brevres como la Escala de Depresi&oacute;n de Zung o el Test de Depresi&oacute;n de Beck de 7 &iacute;tems existen en la literatura, pero el PHQ-2 mantiene posici&oacute;n destacada por su validaci&oacute;n robusta y facilidad administrativa.",
        "Otros instrumentos brevres como la Escala de Depresi&oacute;n de Zung o el Test de Depresi&oacute;n de Beck de 7 &iacute;tems existen en la literatura, pero el PHQ-2 mantiene posici&oacute;n destacada por su validaci&oacute;n robusta y facilidad administrativa. En seguimiento especializado, la <a href=\"/articulos/escala-madrs-depresion.html\">MADRS</a> documenta cambios de severidad con mayor granularidad.",
    ),
    (
        "articulos/who-5-bienestar-psicologico.html",
        "Por debajo de 28, la probabilidad de depresi&oacute;n cl&iacute;nica aumenta significativamente, y se recomienda administrar un instrumento espec&iacute;fico de tamizaje depresivo, como el PHQ-9, para confirmar o descartar un trastorno depresivo.",
        "Por debajo de 28, la probabilidad de depresi&oacute;n cl&iacute;nica aumenta significativamente, y se recomienda administrar un instrumento espec&iacute;fico de tamizaje depresivo, como el PHQ-9 o la <a href=\"/articulos/escala-madrs-depresion.html\">MADRS</a> en contextos cl&iacute;nicos especializados, para confirmar o descartar un trastorno depresivo.",
    ),
    # Discovered: stai
    (
        "articulos/test-beck-ansiedad-bai.html",
        "cu&aacute;ndo es la mejor opci&oacute;n frente a otros instrumentos como el <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a> o la <a href=\"/articulos/lsas-ansiedad-social-liebowitz.html\">LSAS</a> cuando predomina ansiedad social.",
        "cu&aacute;ndo es la mejor opci&oacute;n frente a otros instrumentos como el <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a>, el <a href=\"/articulos/stai-ansiedad-estado-rasgo.html\">STAI</a> o la <a href=\"/articulos/lsas-ansiedad-social-liebowitz.html\">LSAS</a> cuando predomina ansiedad social.",
    ),
    (
        "articulos/que-es-el-gad-7.html",
        "el GAD-7 puede ser completado directamente por el paciente en menos de tres minutos, lo que lo convierte en una herramienta excepcionalmente eficiente para el tamizaje y el seguimiento longitudinal.",
        "el GAD-7 puede ser completado directamente por el paciente en menos de tres minutos, lo que lo convierte en una herramienta excepcionalmente eficiente para el tamizaje y el seguimiento longitudinal. Cuando se requiere diferenciar ansiedad estado y rasgo, el <a href=\"/articulos/stai-ansiedad-estado-rasgo.html\">STAI</a> es la alternativa m&aacute;s utilizada.",
    ),
    # Discovered: raads-r
    (
        "articulos/ados-2-evaluacion-tea.html",
        "El ADOS-2 puede ser menos sensible en detecci&oacute;n de TEA en ni&ntilde;as y mujeres, particularmente aquellas que camuflan o enmascaran sus dificultades sociales.",
        "El ADOS-2 puede ser menos sensible en detecci&oacute;n de TEA en ni&ntilde;as y mujeres, particularmente aquellas que camuflan o enmascaran sus dificultades sociales. En adultos con sospecha tard&iacute;a, el <a href=\"/articulos/raads-r-autismo-adultos.html\">RAADS-R</a> complementa la evaluaci&oacute;n observacional.",
    ),
    (
        "articulos/adir-r-entrevista-autismo.html",
        "Esta herramienta se administra a cuidadores y recopila informaci&oacute;n detallada sobre el desarrollo temprano, patrones de comportamiento y comunicaci&oacute;n.",
        "Esta herramienta se administra a cuidadores y recopila informaci&oacute;n detallada sobre el desarrollo temprano, patrones de comportamiento y comunicaci&oacute;n. En evaluaciones de adultos, el <a href=\"/articulos/raads-r-autismo-adultos.html\">RAADS-R</a> aporta autoinforme estructurado que complementa la ADI-R.",
    ),
    (
        "articulos/ruta-atencion-tea-colombia.html",
        "Un psic&oacute;logo en atenci&oacute;n primaria debe derivar a nivel secundario o terciario cuando existan indicadores de TEA confirmado o altamente probable, especialmente si se requiere evaluaci&oacute;n interdisciplinaria no disponible en el nivel inicial.",
        "Un psic&oacute;logo en atenci&oacute;n primaria debe derivar a nivel secundario o terciario cuando existan indicadores de TEA confirmado o altamente probable, especialmente si se requiere evaluaci&oacute;n interdisciplinaria no disponible en el nivel inicial. En adultos no diagnosticados en infancia, el <a href=\"/articulos/raads-r-autismo-adultos.html\">RAADS-R</a> es un recurso frecuente en la evaluaci&oacute;n inicial.",
    ),
    # Discovered: core-om
    (
        "articulos/inventario-burnout-mbi.html",
        "El Inventario de Burnout de Maslach (MBI) es la escala de referencia para medir el s&iacute;ndrome de agotamiento profesional en tres dimensiones: agotamiento emocional, despersonalizaci&oacute;n y realizaci&oacute;n personal.",
        "El Inventario de Burnout de Maslach (MBI) es la escala de referencia para medir el s&iacute;ndrome de agotamiento profesional en tres dimensiones: agotamiento emocional, despersonalizaci&oacute;n y realizaci&oacute;n personal. Para medir resultados terap&eacute;uticos de forma transdiagn&oacute;stica, el <a href=\"/articulos/core-om-medida-resultados-clinicos.html\">CORE-OM</a> es ampliamente usado en psicoterapia.",
    ),
    (
        "articulos/who-5-bienestar-psicologico.html",
        "En la pr&aacute;ctica, muchos cl&iacute;nicos utilizan ambos instrumentos de forma complementaria: el WHO-5 como medida de bienestar y recuperaci&oacute;n, y el PHQ-9 como tamizaje depresivo cuando el bienestar cae por debajo de 50.",
        "En la pr&aacute;ctica, muchos cl&iacute;nicos utilizan ambos instrumentos de forma complementaria: el WHO-5 como medida de bienestar y recuperaci&oacute;n, y el PHQ-9 como tamizaje depresivo cuando el bienestar cae por debajo de 50. Cuando el objetivo es evaluar cambio cl&iacute;nico global en psicoterapia, el <a href=\"/articulos/core-om-medida-resultados-clinicos.html\">CORE-OM</a> ofrece mayor amplitud.",
    ),
    (
        "articulos/evaluacion-psicologica-colombia-mexico.html",
        "Los resultados se registran en expedientes f&iacute;sicos o, en el mejor de los casos, en documentos de procesador de texto sin integraci&oacute;n con el historial cl&iacute;nico del paciente.",
        "Los resultados se registran en expedientes f&iacute;sicos o, en el mejor de los casos, en documentos de procesador de texto sin integraci&oacute;n con el historial cl&iacute;nico del paciente. Escalas de resultados como el <a href=\"/articulos/core-om-medida-resultados-clinicos.html\">CORE-OM</a> pierden valor si no se readministran de forma sistem&aacute;tica.",
    ),
    # Discovered: enrich
    (
        "articulos/evaluacion-psicologica-colombia-mexico.html",
        "Los instrumentos psicom&eacute;tricos m&aacute;s utilizados en la pr&aacute;ctica cl&iacute;nica de ambos pa&iacute;ses abarcan tamizajes breves, evaluaci&oacute;n cognitiva",
        "Los instrumentos psicom&eacute;tricos m&aacute;s utilizados en la pr&aacute;ctica cl&iacute;nica de ambos pa&iacute;ses abarcan tamizajes breves, evaluaci&oacute;n de pareja (como el <a href=\"/articulos/enrich-inventario-relacion-pareja.html\">ENRICH</a>), evaluaci&oacute;n cognitiva",
    ),
    (
        "articulos/resolucion-1888-salud-mental-colombia.html",
        "Cada intervenci&oacute;n psicol&oacute;gica &ndash;incluyendo tamizaje, psicoeducaci&oacute;n, intervenciones breves basadas en evidencia (TCC, activaci&oacute;n conductual, manejo de estr&eacute;s) y seguimiento longitudinal en atenci&oacute;n primaria, as&iacute; como psicoterapia estructurada, evaluaciones especializadas (EMDR, DBT, terapia de pareja) en nivel secundario&ndash; debe registrarse utilizando cat&aacute;logos nacionales oficiales",
        "Cada intervenci&oacute;n psicol&oacute;gica &ndash;incluyendo tamizaje, psicoeducaci&oacute;n, intervenciones breves basadas en evidencia (TCC, activaci&oacute;n conductual, manejo de estr&eacute;s) y seguimiento longitudinal en atenci&oacute;n primaria, as&iacute; como psicoterapia estructurada, evaluaciones especializadas (EMDR, DBT, <a href=\"/articulos/enrich-inventario-relacion-pareja.html\">terapia de pareja con ENRICH</a>) en nivel secundario&ndash; debe registrarse utilizando cat&aacute;logos nacionales oficiales",
    ),
    (
        "articulos/inventario-burnout-mbi.html",
        "Para entender el proceso de desarrollo del burnout en un individuo o equipo, se requieren aplicaciones repetidas a lo largo del tiempo, idealmente integradas en una plataforma que facilite el seguimiento longitudinal y la comparaci&oacute;n de perfiles entre evaluaciones.",
        "Para entender el proceso de desarrollo del burnout en un individuo o equipo, se requieren aplicaciones repetidas a lo largo del tiempo, idealmente integradas en una plataforma que facilite el seguimiento longitudinal y la comparaci&oacute;n de perfiles entre evaluaciones. En consulta de pareja afectada por estr&eacute;s laboral, el <a href=\"/articulos/enrich-inventario-relacion-pareja.html\">ENRICH</a> objetiva conflictos recurrentes.",
    ),
    # Discovered: lec-5
    (
        "articulos/evaluacion-riesgo-suicida.html",
        "La evaluaci&oacute;n del riesgo suicida y la atenci&oacute;n de pacientes en crisis tiene un impacto emocional significativo en el psic&oacute;logo.",
        "La evaluaci&oacute;n del riesgo suicida y la atenci&oacute;n de pacientes en crisis tiene un impacto emocional significativo en el psic&oacute;logo. Cuando hay antecedentes traum&aacute;ticos, conviene documentarlos con el <a href=\"/articulos/lec-5-eventos-vitales-traumaticos.html\">LEC-5</a> antes de cerrar el plan de seguridad.",
    ),
    (
        "articulos/resolucion-1888-salud-mental-colombia.html",
        "Define las rutas integrales de atenci&oacute;n en salud mental (RIAS) para trastornos mentales comunes, trastornos por consumo de sustancias, trastornos mentales severos y suicidio.",
        "Define las rutas integrales de atenci&oacute;n en salud mental (RIAS) para trastornos mentales comunes, trastornos por consumo de sustancias, trastornos mentales severos y suicidio, integrando evaluaci&oacute;n de trauma con instrumentos como el <a href=\"/articulos/lec-5-eventos-vitales-traumaticos.html\">LEC-5</a> cuando corresponda.",
    ),
    # Discovered: ces-d
    (
        "articulos/inventario-depresion-beck-bdi.html",
        "A diferencia de instrumentos de tamizaje breves como el PHQ-9 o escalas heteroaplicadas como la <a href=\"/articulos/hamilton-depresion-hdrs-17.html\">Hamilton de depresi&oacute;n (HDRS-17)</a>, el BDI-II ofrece una evaluaci&oacute;n m&aacute;s detallada",
        "A diferencia de instrumentos de tamizaje breves como el PHQ-9, la <a href=\"/articulos/ces-d-escala-depresion.html\">CES-D</a> o escalas heteroaplicadas como la <a href=\"/articulos/hamilton-depresion-hdrs-17.html\">Hamilton de depresi&oacute;n (HDRS-17)</a>, el BDI-II ofrece una evaluaci&oacute;n m&aacute;s detallada",
    ),
    (
        "articulos/phq-2-tamizaje-depresion-breve.html",
        "Para evaluaciones m&aacute;s exhaustivas de depresi&oacute;n, ansiedad comórbida o sintomatolog&iacute;a asociada, pueden complementarse con PHQ-9, PHQ-15 o Escalas de Ansiedad de Generalizada (GAD-7).",
        "Para evaluaciones m&aacute;s exhaustivas de depresi&oacute;n, ansiedad comórbida o sintomatolog&iacute;a asociada, pueden complementarse con PHQ-9, PHQ-15, la <a href=\"/articulos/ces-d-escala-depresion.html\">CES-D</a> o Escalas de Ansiedad de Generalizada (GAD-7).",
    ),
    (
        "articulos/who-5-bienestar-psicologico.html",
        "Un puntaje bajo en el WHO-5 no equivale a un diagn&oacute;stico de depresi&oacute;n, sino que indica deterioro del bienestar que requiere evaluaci&oacute;n adicional mediante entrevista cl&iacute;nica y, cuando proceda, instrumentos diagn&oacute;sticos complementarios.",
        "Un puntaje bajo en el WHO-5 no equivale a un diagn&oacute;stico de depresi&oacute;n, sino que indica deterioro del bienestar que requiere evaluaci&oacute;n adicional mediante entrevista cl&iacute;nica y, cuando proceda, instrumentos diagn&oacute;sticos complementarios como la <a href=\"/articulos/ces-d-escala-depresion.html\">CES-D</a> en contextos comunitarios.",
    ),
]


def main() -> None:
    changed: set[str] = set()
    errors: list[str] = []

    for rel, old, new in EDITS:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        count = text.count(old)
        if count != 1:
            errors.append(f"{rel}: expected 1 match, found {count}")
            continue
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        changed.add(rel)

    print(f"Updated {len(changed)} files ({len(EDITS)} edits)")
    for err in errors:
        print(f"ERROR: {err}")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
