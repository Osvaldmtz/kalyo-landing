# -*- coding: utf-8 -*-
"""Articles 4-7 for finalize_phase1.py"""
from __future__ import annotations

import textwrap

HC = "/articulos/historia-clinica-psicologica-paso-a-paso.html"
DSM = "/articulos/que-es-el-dsm-5.html"
OV = "/articulos/orientacion-vocacional-psicologia.html"


def articles_4_through_7() -> list[dict]:
    return [
        _article4(),
        _article5(),
        _article6(),
        _article7(),
    ]


def _article4() -> dict:
    return {
        "slug": "inteligencias-multiples-evaluacion-clinica",
        "title": "Inteligencias M\u00faltiples de Gardner: Evaluaci\u00f3n Cl\u00ednica | Kalyo",
        "description": "Inteligencias m&uacute;ltiples de Gardner en evaluaci&oacute;n cl&iacute;nica: 9 inteligencias, diferencia con CI Wechsler/Raven, WISC-V, TDAH, TEA, dificultades de aprendizaje y cr&iacute;tica cient&iacute;fica para psic&oacute;logos LATAM.",
        "description_plain": "Inteligencias múltiples de Gardner en evaluación clínica: 9 inteligencias, diferencia con CI Wechsler/Raven, WISC-V, TDAH, TEA, dificultades de aprendizaje y crítica científica para psicólogos LATAM.",
        "keywords": "inteligencias m\u00faltiples Gardner, evaluaci\u00f3n cl\u00ednica, WISC-V, CI Wechsler, Raven, TDAH, TEA, dificultades aprendizaje",
        "h1": "Inteligencias m&uacute;ltiples de Gardner: evaluaci&oacute;n cl&iacute;nica",
        "intro": f"La teor&iacute;a de <strong>inteligencias m&uacute;ltiples</strong> de Howard Gardner propone capacidades relativamente independientes (ling&uuml;&iacute;stica, l&oacute;gico-matem&aacute;tica, espacial, musical, corporal-kinest&eacute;sica, interpersonal, intrapersonal, naturalista y existencial). En escuelas y consultorios de LATAM es muy difundida, pero en psicolog&iacute;a cl&iacute;nica debe distinguirse del <strong>coeficiente intelectual</strong> (Wechsler, Raven). Esta gu&iacute;a orienta uso prudente en evaluaci&oacute;n de TDAH, TEA y dificultades de aprendizaje, integraci&oacute;n con <strong>WISC-V</strong> y registro en <a href=\"{HC}\">historia cl&iacute;nica psicol&oacute;gica</a>.",
        "hero_alt": "Psic\u00f3logo cl\u00ednico evaluando perfil cognitivo de ni\u00f1o con bater\u00eda WISC-V",
        "inline_alt": "Tabla de nueve inteligencias m\u00faltiples de Gardner en contexto cl\u00ednico",
        "meta_label": "Evaluaci&oacute;n psicopedag&oacute;gica &middot; Actualizaci&oacute;n 2026",
        "body_html": textwrap.dedent("""
    <h2>Teor&iacute;a de Gardner vs coeficiente intelectual</h2>
    <p>Gardner cuestiona reducir capacidad humana a un &uacute;nico CI. Propone <strong>inteligencias m&uacute;ltiples</strong> como dominios que interact&uacute;an en contexto cultural. En cl&iacute;nica, familias piden &laquo;test de inteligencias m&uacute;ltiples&raquo; esperando validar talentos o explicar fracaso escolar. El psic&oacute;logo debe aclarar que Gardner es marco educativo y descriptivo, no bater&iacute;a psicom&eacute;trica unificada con baremos nacionales como <strong>WISC-V</strong> o matrices <strong>Raven</strong>.</p>
    <p>El <strong>CI global y &iacute;ndices factoriales</strong> de Wechsler miden funcionamiento cognitivo general y perfil de fortalezas/debilidades con estandarizaci&oacute;n rigurosa. Raven estima razonamiento fluido no verbal. Ninguno mapea directamente las nueve inteligencias de Gardner; hay solapamientos parciales (p. ej., l&oacute;gico-matem&aacute;tica con &iacute;ndice de razonamiento fluido).</p>
    <p>Confundir ambos constructos genera informes contradictorios: un ni&ntilde;o con CI promedio puede mostrar talento musical o corporal elevado sin que ello invalide evaluaci&oacute;n est&aacute;ndar ni justifique omitir intervenci&oacute;n en lectura.</p>

    <h2>Las nueve inteligencias en contexto cl&iacute;nico</h2>
    <table class="items-table">
      <thead><tr><th>Inteligencia (Gardner)</th><th>Manifestaci&oacute;n</th><th>Nota cl&iacute;nica</th></tr></thead>
      <tbody>
        <tr><td>Ling&uuml;&iacute;stica</td><td>Lectura, escritura, narraci&oacute;n</td><td>Dislexia afecta dominio, no &laquo;falta&raquo; de inteligencia</td></tr>
        <tr><td>L&oacute;gico-matem&aacute;tica</td><td>Razonamiento, n&uacute;meros</td><td>Correlaciona parcialmente con WISC &iacute;ndices fluido/cuantitativo</td></tr>
        <tr><td>Espacial</td><td>Visualizaci&oacute;n, orientaci&oacute;n</td><td>&Uacute;til en disgraf&iacute;a, TEA visual-espacial</td></tr>
        <tr><td>Musical</td><td>Ritmo, tono, composici&oacute;n</td><td>Puede ser isla de habilidad en TEA</td></tr>
        <tr><td>Corporal-kinest&eacute;sica</td><td>Coordinaci&oacute;n, expresi&oacute;n f&iacute;sica</td><td>TDAH puede afectar control motor fino</td></tr>
        <tr><td>Interpersonal</td><td>Empat&iacute;a, liderazgo social</td><td>TEA: d&eacute;ficit pragm&aacute;tico vs inteligencia social</td></tr>
        <tr><td>Intrapersonal</td><td>Autoconocimiento, regulaci&oacute;n</td><td>Ansiedad/depression distorsionan autorreporte</td></tr>
        <tr><td>Naturalista</td><td>Clasificaci&oacute;n naturaleza</td><td>Menos evaluada en consultorio urbano</td></tr>
        <tr><td>Existencial (propuesta)</td><td>Preguntas sobre sentido</td><td>Adolescentes en crisis existencial</td></tr>
      </tbody>
    </table>
    <p>Use la tabla para psicoeducar y dise&ntilde;ar estrategias multimodales, no para etiquetar &laquo;inteligente solo en m&uacute;sica&raquo; y abandonar lectura.</p>

    <h2>WISC-V y evaluaci&oacute;n cl&iacute;nica integrada</h2>
    <p>En sospecha de <strong>TDAH</strong>, <strong>TEA</strong> o trastorno espec&iacute;fico de aprendizaje, la evaluaci&oacute;n cl&iacute;nica LATAM suele incluir entrevista, escalas conductuales, prueba de rendimiento acad&eacute;mico y, cuando procede, <strong>WISC-V</strong> (o WAIS-IV en adultos). Los &iacute;ndices Verbal Comprension, Razonamiento Fluido, Memoria de Trabajo y Velocidad de Procesamiento orientan ajustes curriculares y descartan discapacidad intelectual.</p>
    <p>Si el colegio menciona Gardner, integre lenguaje: &laquo;fortaleza en expresi&oacute;n corporal&raquo; puede traducirse en apoyos kinest&eacute;sicos para matem&aacute;ticas, sin negar necesidad de ense&ntilde;anza expl&iacute;cita en dominios d&eacute;biles seg&uacute;n WISC.</p>
    <p>Documente discrepancias entre rendimiento escolar, CI y observaci&oacute;n cl&iacute;nica. Derive a psicopedagog&iacute;a cuando hay retraso persistente en lectura/escritura pese a CI promedio.</p>

    <h2>TDAH, TEA y dificultades de aprendizaje</h2>
    <p>En <strong>TDAH</strong>, memoria de trabajo y velocidad de procesamiento suelen estar afectadas en WISC; Gardner no captura impulsividad ni funciones ejecutivas. Las adaptaciones deben incluir estructura, refuerzo y farmacoterapia si indicada, no solo &laquo;ense&ntilde;ar seg&uacute;n inteligencia corporal&raquo;.</p>
    <p>En <strong>TEA</strong>, puede haber perfil desigual: razonamiento fluido alto con pragm&aacute;tica social baja. Gardner ayuda a comunicar islas de habilidad a familias; el diagn&oacute;stico sigue criterios <a href="/articulos/que-es-el-dsm-5.html">DSM-5</a>/CIE-11 y evaluaci&oacute;n del desarrollo.</p>
    <p>En dificultades espec&iacute;ficas de aprendizaje, la intervenci&oacute;n fonol&oacute;gica estructurada tiene evidencia; rotar solo por estilo preferido no sustituye remediaci&oacute;n.</p>

    <h2>Cr&iacute;tica cient&iacute;fica y uso &eacute;tico</h2>
    <p>Revisiones se&ntilde;alan escasa evidencia emp&iacute;rica de inteligencias estrictamente independientes y riesgo de etiquetar ni&ntilde;os sin base psicom&eacute;trica. Cuestionarios comerciales &laquo;MI&raquo; suelen carecer de validez cl&iacute;nica. Evite informes que listan ocho inteligencias altas/bajas sin prueba estandarizada.</p>
    <p>En peritajes laborales o escolares, priorice WISC, evaluaci&oacute;n de logros y entrevista cl&iacute;nica. Gardner puede enriquecer recomendaciones pedag&oacute;gicas como marco inclusivo, no como sustituto legal de evaluaci&oacute;n de necesidades educativas.</p>
    <p>Registre en HC qu&eacute; instrumentos estandarizados aplic&oacute;, qu&eacute; marco te&oacute;rico us&oacute; para recomendaciones y l&iacute;mites de interpretaci&oacute;n. Vincule con <a href="/articulos/orientacion-vocacional-psicologia.html">orientaci&oacute;n vocacional</a> solo despu&eacute;s de estabilizar aprendizaje b&aacute;sico.</p>
        """),
        "faqs": [
            {"q": "\u00bfLas inteligencias m\u00faltiples son cient\u00edficamente v\u00e1lidas?", "q_html": "&iquest;Las inteligencias m&uacute;ltiples son cient&iacute;ficamente v&aacute;lidas?", "a_plain": "Gardner aporta marco educativo influyente, pero la independencia estricta de nueve inteligencias tiene evidencia limitada. \u00daselas para diversificar estrategias pedag\u00f3gicas, no como diagn\u00f3stico psicom\u00e9trico equivalente al CI.", "a_html": "Marco educativo influyente, pero evidencia limitada de independencia estricta. No equivalente al CI."},
            {"q": "\u00bfQu\u00e9 test mide inteligencias m\u00faltiples?", "q_html": "&iquest;Qu&eacute; test mide inteligencias m&uacute;ltiples?", "a_plain": "No existe un test estandarizado universal aceptado cl\u00ednicamente como WISC. Hay inventarios comerciales con validez cuestionable. En evaluaci\u00f3n formal use WISC-V, Raven, pruebas de logro y observaci\u00f3n cl\u00ednica.", "a_html": "No hay test universal cl&iacute;nicamente equivalente a WISC. Use bater&iacute;as estandarizadas."},
            {"q": "\u00bfC\u00f3mo documento inteligencias m\u00faltiples en la HC?", "q_html": "&iquest;C&oacute;mo documento inteligencias m&uacute;ltiples en la HC?", "a_plain": "Registre pruebas estandarizadas aplicadas (WISC-V, Raven), perfiles de \u00edndices, observaciones cualitativas de fortalezas y recomendaciones pedag\u00f3gicas. Indique si Gardner se us\u00f3 solo como marco psicoeducativo.", "a_html": "Registre pruebas estandarizadas, perfiles e indique si Gardner fue marco psicoeducativo."},
            {"q": "\u00bfEn qu\u00e9 se diferencia del CI?", "q_html": "&iquest;En qu&eacute; se diferencia del CI?", "a_plain": "El CI resume funcionamiento cognitivo general con baremos y validez predictiva establecida. Gardner describe dominios de habilidad en contexto educativo sin un \u00fanico puntaje estandarizado comparables entre pa\u00edses.", "a_html": "CI tiene baremos y validez predictiva; Gardner es marco descriptivo educativo."},
        ],
        "related": [("historia-clinica-psicologica-paso-a-paso", "Historia cl&iacute;nica paso a paso"), ("tdah-adultos-evaluacion-diagnostico", "TDAH: evaluaci&oacute;n"), ("evaluacion-neuropsicologica-instrumentos", "Evaluaci&oacute;n neuropsicol&oacute;gica"), ("que-es-el-dsm-5", "Qu&eacute; es el DSM-5")],
    }


def _article5() -> dict:
    return {
        "slug": "cie-11-trastornos-mentales-psicologos",
        "title": "CIE-11 Trastornos Mentales: Gu\u00eda para Psic\u00f3logos Cl\u00ednicos | Kalyo",
        "description": "CIE-11 trastornos mentales para psic&oacute;logos: implementaci&oacute;n OPS/LATAM 2022-2025, cambios vs CIE-10, CPSD, gaming disorder, duelo prolongado, c&oacute;digos 6A70 TDAH, codificaci&oacute;n en HC y adopci&oacute;n MX/CO/AR/PE/ES.",
        "description_plain": "CIE-11 trastornos mentales para psicólogos: implementación OPS/LATAM 2022-2025, cambios vs CIE-10, CPSD, gaming disorder, duelo prolongado, códigos 6A70 TDAH, codificación en HC y adopción MX/CO/AR/PE/ES.",
        "keywords": "CIE-11, ICD-11, trastornos mentales, OPS, TDAH 6A70, gaming disorder, duelo prolongado, psic\u00f3logos cl\u00ednicos LATAM",
        "h1": "CIE-11 trastornos mentales: gu&iacute;a para psic&oacute;logos cl&iacute;nicos",
        "intro": f"La <strong>CIE-11</strong> (Clasificaci&oacute;n Internacional de Enfermedades, 11.&ordf; revisi&oacute;n) de la OMS actualiza diagn&oacute;sticos de salud mental con categor&iacute;as nuevas y criterios revisados. En LATAM, la <strong>OPS</strong> impulsa adopci&oacute;n gradual 2022&ndash;2025. Esta gu&iacute;a resume cambios respecto a CIE-10, c&oacute;digos frecuentes (p. ej. <strong>6A70 TDAH</strong>), trastornos emergentes (CPSD, gaming disorder, duelo prolongado), relaci&oacute;n con <a href=\"{DSM}\">DSM-5</a> y codificaci&oacute;n en <a href=\"{HC}\">historia cl&iacute;nica</a> en M&eacute;xico, Colombia, Argentina, Per&uacute; y Espa&ntilde;a.",
        "hero_alt": "Psic\u00f3logo cl\u00ednico revisando manual CIE-11 en consultorio",
        "inline_alt": "Tabla comparativa CIE-10 vs CIE-11 trastornos mentales",
        "meta_label": "Clasificaci&oacute;n diagn&oacute;stica &middot; Actualizaci&oacute;n 2026",
        "body_html": textwrap.dedent("""
    <h2>Qu&eacute; es la CIE-11 y calendario LATAM</h2>
    <p>La <strong>CIE-11</strong> entr&oacute; en vigor oficialmente en enero de 2022 (OMS). Incluye cap&iacute;tulo 06 sobre trastornos mentales, comportamentales o del neurodesarrollo, con estructura digital y c&oacute;digos alfanum&eacute;ricos (p. ej. 6A70). La <strong>OPS/PAHO</strong> apoya pa&iacute;ses latinoamericanos en migraci&oacute;n desde CIE-10, capacitaci&oacute;n cl&iacute;nica y sistemas de informaci&oacute;n en salud.</p>
    <p>La adopci&oacute;n legal var&iacute;a: Espa&ntilde;a y varios pa&iacute;ses avanzan en normativa sanitaria; M&eacute;xico, Colombia, Argentina, Per&uacute; y Chile actualizan gu&iacute;as, facturaci&oacute;n y registros hospitalarios en plazos distintos. El psic&oacute;logo debe verificar normativa colegiada y de aseguradoras locales, no asumir cambio autom&aacute;tico overnight.</p>
    <p>La CIE-11 es referencia internacional para estad&iacute;stica, epidemiolog&iacute;a y compatibilidad global; el DSM-5 sigue muy usado en investigaci&oacute;n y algunos sistemas privados.</p>

    <h2>Cambios principales respecto a CIE-10</h2>
    <table class="items-table">
      <thead><tr><th>&Aacute;rea</th><th>CIE-10</th><th>CIE-11</th></tr></thead>
      <tbody>
        <tr><td>Estructura</td><td>Categor&iacute;as r&iacute;gidas</td><td>Enfoque dimensional + espectros</td></tr>
        <tr><td>TEPT</td><td>Subtipos limitados</td><td>Incluye TEPT complejo (CPSD)</td></tr>
        <tr><td>Duelo</td><td>No categor&iacute;a propia</td><td>Trastorno de duelo prolongado</td></tr>
        <tr><td>Conducta</td><td>Varios c&oacute;digos dispersos</td><td>Gaming disorder, compulsi&oacute;n compras</td></tr>
        <tr><td>Personalidad</td><td>Categor&iacute;as m&uacute;ltiples</td><td>Trastorno de personalidad + severidad</td></tr>
        <tr><td>Autismo</td><td>F84.x</td><td>Trastorno del espectro autista unificado</td></tr>
      </tbody>
    </table>
    <p>Revise manual cl&iacute;nico digital de OMS (ICD-11 Browser) para redacci&oacute;n exacta de criterios antes de codificar informes.</p>

    <h2>CPSD, gaming disorder y duelo prolongado</h2>
    <p><strong>Trastorno de estr&eacute;s postraum&aacute;tico complejo (CPSD / 6B41)</strong> reconoce alteraciones de regulaci&oacute;n afectiva, autoconcepto negativo y dificultades relacionales tras trauma prolongado o repetido. Relevante en violencia dom&eacute;stica, abuso cr&oacute;nico y contextos de inseguridad en LATAM.</p>
    <p><strong>Gaming disorder (6C51)</strong> exige patr&oacute;n persistente de juego digital con deterioro funcional, no ocio recreativo normal en adolescentes. Diferencie de TDAH, depresi&oacute;n o aislamiento social secundario.</p>
    <p><strong>Trastorno de duelo prolongado (6B42)</strong> captura duelo intenso &gt;6 meses (adultos) con anhelo/disfunci&oacute;n marcada. &Uacute;til en consultas de duelo perinatal, homicidio o desaparici&oacute;n forzada.</p>

    <h2>C&oacute;digos frecuentes en consulta cl&iacute;nica</h2>
    <table class="items-table">
      <thead><tr><th>Trastorno</th><th>C&oacute;digo CIE-11</th><th>Nota cl&iacute;nica</th></tr></thead>
      <tbody>
        <tr><td>TDAH</td><td>6A70</td><td>Presentaciones combinada, inatenta, impulsiva</td></tr>
        <tr><td>Trastorno depresivo</td><td>6A7x</td><td>Subtipos seg&uacute;n gravedad y curso</td></tr>
        <tr><td>Trastorno de ansiedad generalizada</td><td>6B00</td><td>Ansiedad excesiva persistente</td></tr>
        <tr><td>TEPT</td><td>6B40</td><td>Reexperimentaci&oacute;n, evitaci&oacute;n, hiperalerta</td></tr>
        <tr><td>TOC</td><td>6B20</td><td>Obsesiones/compulsiones</td></tr>
        <tr><td>TEA</td><td>6A02</td><td>Espectro autista con niveles de apoyo</td></tr>
      </tbody>
    </table>
    <p>Confirme c&oacute;digo en versi&oacute;n espa&ntilde;ola oficial antes de facturaci&oacute;n o registros ministeriales.</p>

    <h2>CIE-11 vs DSM-5 y codificaci&oacute;n en HC</h2>
    <p>Muchos criterios son conceptualmente cercanos al <a href="/articulos/que-es-el-dsm-5.html">DSM-5</a>, pero diferencias existen (p. ej. TEPT complejo, personalidad dimensional). En informes puede consignar ambos si el destinatario lo requiere: &laquo;6A70 TDAH (CIE-11) / 314.01 (DSM-5)&raquo; con criterios cumplidos listados.</p>
    <p>En <strong>historia cl&iacute;nica</strong>, registre: versi&oacute;n de clasificaci&oacute;n, c&oacute;digo, criterios positivos, gravedad funcional, fecha de evaluaci&oacute;n y plan terap&eacute;utico. Sistemas digitales como Kalyo facilitan trazabilidad para auditor&iacute;as y aseguradoras.</p>
    <p>Implementaci&oacute;n por pa&iacute;s: verifique si colegios profesionales exigen CIE-10 a&uacute;n en formulaciones p&uacute;blicas; algunos hospitales privados adoptan CIE-11 antes que sector p&uacute;blico.</p>

    <h2>Implementaci&oacute;n pr&aacute;ctica MX, CO, AR, PE, ES</h2>
    <p><strong>M&eacute;xico:</strong> transici&oacute;n en SSA e IMSS hacia CIE-11 en registros; consulte NOM vigentes. <strong>Colombia:</strong> Resoluci&oacute;n 5596/2015 a&uacute;n referencia CIE-10 en muchos entornos; actualizaci&oacute;n en curso con OPS. <strong>Argentina:</strong> ministerios provinciales diversos; CIE-10 Fxx com&uacute;n en obras sociales. <strong>Per&uacute;:</strong; MINSA alinea con OMS gradualmente. <strong>Espa&ntilde;a:</strong> CIE-10-ES en uso cl&iacute;nico con roadmap CIE-11. Mantenga formaci&oacute;n continua y software actualizado.</p>
        """),
        "faqs": [
            {"q": "\u00bfEs obligatorio usar CIE-11 ya?", "q_html": "&iquest;Es obligatorio usar CIE-11 ya?", "a_plain": "Depende del pa\u00eds y del sistema (p\u00fablico vs privado). OMS la recomienda desde 2022, pero muchos sistemas LATAM a\u00fan operan con CIE-10 mientras migran. Verifique normativa local y requisitos de aseguradoras.", "a_html": "Depende del pa&iacute;s y sistema. Verifique normativa local."},
            {"q": "\u00bfDebo dejar de usar CIE-10?", "q_html": "&iquest;Debo dejar de usar CIE-10?", "a_plain": "Mientras su sistema de salud o colegio profesional exija CIE-10, consigne el c\u00f3digo requerido. Puede anotar equivalencia CIE-11 en notas cl\u00ednicas para preparar transici\u00f3n.", "a_html": "Use el c&oacute;digo exigido localmente; anote equivalencia CIE-11 si \u00fatil."},
            {"q": "\u00bfUso CIE-11 o DSM-5?", "q_html": "&iquest;Uso CIE-11 o DSM-5?", "a_plain": "CIE-11 para registros oficiales, epidemiolog\u00eda y muchos sistemas p\u00fablicos; DSM-5 sigue frecuente en investigaci\u00f3n y cl\u00ednica privada. Documente criterios cumplidos independientemente del sistema elegido.", "a_html": "CIE-11 en registros oficiales; DSM-5 frecuente en investigaci&oacute;n y privada."},
            {"q": "\u00bfD\u00f3nde descargar CIE-11 en espa\u00f1ol?", "q_html": "&iquest;D&oacute;nde descargar CIE-11 en espa&ntilde;ol?", "a_plain": "Consulte el ICD-11 Browser de la OMS (icd.who.int) y recursos de OPS/PAHO en espa\u00f1ol. Algunos pa\u00edses publican adaptaciones nacionales en sitios oficiales de salud.", "a_html": "ICD-11 Browser OMS y recursos OPS/PAHO en espa&ntilde;ol."},
        ],
        "related": [("que-es-el-dsm-5", "Qu&eacute; es el DSM-5"), ("historia-clinica-psicologica-paso-a-paso", "Historia cl&iacute;nica paso a paso"), ("tdah-adultos-evaluacion-diagnostico", "TDAH evaluaci&oacute;n"), ("como-redactar-informe-psicologico", "Redactar informe psicol&oacute;gico")],
        "references": ['<a href="https://icd.who.int/" rel="nofollow noopener noreferrer" target="_blank">WHO ICD-11 Browser</a>'],
    }


def _article6() -> dict:
    return {
        "slug": "ley-20584-derechos-paciente-chile",
        "title": "Ley 20.584 en Chile: Derechos del Paciente para Psic\u00f3logos | Kalyo",
        "description": "Ley 20.584 Chile 2012: derechos del paciente en psicolog&iacute;a cl&iacute;nica, consentimiento informado, propiedad y acceso a HC, l&iacute;mites de confidencialidad, FONASA/ISAPRE y consulta privada.",
        "description_plain": "Ley 20.584 Chile 2012: derechos del paciente en psicología clínica, consentimiento informado, propiedad y acceso a HC, límites de confidencialidad, FONASA/ISAPRE y consulta privada.",
        "keywords": "Ley 20584 Chile, derechos paciente, psicolog\u00eda cl\u00ednica, consentimiento informado, historia cl\u00ednica, confidencialidad, FONASA ISAPRE",
        "h1": "Ley 20.584 en Chile: derechos del paciente para psic&oacute;logos",
        "intro": f"La <strong>Ley 20.584</strong> (2012) establece derechos y deberes de las personas en relaci&oacute;n con acciones de salud en Chile, incluida atenci&oacute;n psicol&oacute;gica en consulta privada, FONASA e ISAPRE. Esta gu&iacute;a resume derechos aplicables al psic&oacute;logo cl&iacute;nico: consentimiento informado, propiedad y acceso a ficha cl&iacute;nica, confidencialidad y l&iacute;mites legales, con registro en <a href=\"{HC}\">historia cl&iacute;nica psicol&iacute;gica</a> y consideraciones de telepsicolog&iacute;a.",
        "hero_alt": "Psic\u00f3logo en Chile explicando derechos del paciente seg\u00fan Ley 20.584",
        "inline_alt": "Tabla de derechos del paciente en psicolog\u00eda cl\u00ednica Chile",
        "meta_label": "Normativa Chile &middot; Actualizaci&oacute;n 2026",
        "body_html": textwrap.dedent("""
    <h2>Marco legal: Ley 20.584 de 2012</h2>
    <p>La <strong>Ley 20.584</strong> reconoce derechos como informaci&oacute;n clara, consentimiento libre e informado, confidencialidad, acceso a ficha cl&iacute;nica, respeto dignidad y no discriminaci&oacute;n. Aplica a prestadores institucionales y profesionales independientes que realizan acciones de salud, incluida psicolog&iacute;a cl&iacute;nica regulada por el Colegio de Psic&oacute;logos de Chile y normativa MINSAL.</p>
    <p>Complementa C&oacute;digo Sanitario, ley de protecci&oacute;n de datos personales y normas espec&iacute;ficas de salud mental. El psic&oacute;logo debe conocer actualizaciones reglamentarias y protocolos de su establecimiento o consulta privada.</p>
    <p>Diferencie acciones de salud de asesor&iacute;as no cl&iacute;nicas (coaching sin diagn&oacute;stico); la ley aplica cuando hay evaluaci&oacute;n o intervenci&oacute;n en salud mental.</p>

    <h2>Derechos del paciente en psicolog&iacute;a cl&iacute;nica</h2>
    <table class="items-table">
      <thead><tr><th>Derecho</th><th>Implicaci&oacute;n cl&iacute;nica</th></tr></thead>
      <tbody>
        <tr><td>Informaci&oacute;n</td><td>Explicar prop&oacute;sito, m&eacute;todos, riesgos, alternativas y costos</td></tr>
        <tr><td>Consentimiento informado</td><td>Documento escrito para evaluaciones, informes, grabaciones</td></tr>
        <tr><td>Confidencialidad</td><td>Reserva salvo excepciones legales</td></tr>
        <tr><td>Acceso a ficha cl&iacute;nica</td><td>Copia o visualizaci&oacute;n seg&uacute;n procedimiento</td></tr>
        <tr><td>Propiedad de datos</td><td>Paciente titular; profesional custodio</td></tr>
        <tr><td>Segunda opini&oacute;n</td><td>No obstruir derivaci&oacute;n razonable</td></tr>
        <tr><td>Rechazo de tratamiento</td><td>Salvo excepciones de urgencia/psiquiatr&iacute;a legal</td></tr>
        <tr><td>Reclamo</td><td>Informar v&iacute;as Superintendencia de Salud / colegio</td></tr>
      </tbody>
    </table>

    <h2>Consentimiento informado chileno</h2>
    <p>El consentimiento debe ser <strong>libre, informado y espec&iacute;fico</strong>: evaluaci&oacute;n psicol&oacute;gica, psicoterapia, informe a terceros (colegio, tribunal, empleador), grabaci&oacute;n de sesi&oacute;n o aplicaci&oacute;n de tests. En menores, representante legal firma con escucha del ni&ntilde;o seg&uacute;n edad y madurez; en adolescentes, equilibre autonom&iacute;a emergente y patria potestad.</p>
    <p>Incluya l&iacute;mites de confidencialidad (riesgo vital, abuso a menor, orden judicial). Renueve consentimiento si cambia objetivo (de evaluaci&oacute;n a peritaje). Archivar en HC digital o f&iacute;sica con trazabilidad.</p>

    <h2>Historia cl&iacute;nica: propiedad, conservaci&oacute;n y acceso</h2>
    <p>La ficha cl&iacute;nica es propiedad del paciente; el prestador es custodio con deber de conservaci&oacute;n, seguridad y exactitud. Plazos de conservaci&oacute;n siguen normativa MINSAL (a&ntilde;os seg&uacute;n tipo de registro). Debe permitir acceso razonable, copias y correcci&oacute;n de errores formales seg&uacute;n procedimiento.</p>
    <p>En psicolog&iacute;a, proteja notas de proceso vs informes formales. Terceros solo acceden con consentimiento o mandato legal. Documente entregas de informes: destinatario, fecha, alcance.</p>
    <p>Plataformas digitales deben cumplir ciberseguridad y respaldo; Kalyo y sistemas similares ayudan a trazabilidad exigida en auditor&iacute;as ISAPRE o procesos judiciales.</p>

    <h2>L&iacute;mites de confidencialidad</h2>
    <p>Rompimiento justificado: riesgo inminente de suicidio/homicidio, sospecha fundada de abuso infantil, vulneraci&oacute;n grave de adulto mayor dependiente, mandato judicial, notificaciones epidemiol&oacute;gicas obligatorias. Documente decisi&oacute;n, hora, destinatario y base legal en HC.</p>
    <p>Comunique al paciente el rompimiento cuando sea seguro hacerlo, salvo que aumente riesgo. En pareja/familia, clarifique secretos cl&iacute;nicos vs informaci&oacute;n compartida desde inicio.</p>

    <h2>Consulta privada vs FONASA e ISAPRE</h2>
    <p><strong>Consulta privada:</strong> contrato directo; Ley 20.584 igualmente aplica; facturaci&oacute;n y boletas seg&uacute;n SII. <strong>FONASA/ISAPRE:</strong> bonos, convenios y requisitos de informe para reembolso; verifique cobertura de psicolog&iacute;a (modalidad GES/LEAS seg&uacute;n patolog&iacute;a). No todos los trastornos tienen garant&iacute;as expl&iacute;citas; informe al paciente costos no cubiertos.</p>
    <p>Telepsicolog&iacute;a: consentimiento espec&iacute;fico para modalidad remota, verificaci&oacute;n identidad, confidencialidad del entorno del paciente y plan ante desconexi&oacute;n o riesgo. Colegio profesional puede tener gu&iacute;as adicionales post-pandemia.</p>
        """),
        "faqs": [
            {"q": "\u00bfLa Ley 20.584 aplica en consulta privada?", "q_html": "&iquest;La Ley 20.584 aplica en consulta privada?", "a_plain": "S\u00ed. Regula derechos en acciones de salud prestadas por profesionales e instituciones, incluida psicolog\u00eda cl\u00ednica privada. Debe informar derechos, obtener consentimiento y custodiar ficha cl\u00ednica.", "a_html": "S&iacute; aplica en consulta privada cl&iacute;nica."},
            {"q": "\u00bfEl paciente puede pedir copia de la HC?", "q_html": "&iquest;El paciente puede pedir copia de la HC?", "a_plain": "S\u00ed, tiene derecho de acceso y copia seg\u00fan procedimiento y plazos razonables. Puede cobrarse costo de reproducci\u00f3n seg\u00fan normativa. Entregue informes formales y registros acordados.", "a_html": "S&iacute;, derecho de acceso y copia seg&uacute;n procedimiento."},
            {"q": "\u00bfCu\u00e1ndo puedo romper confidencialidad?", "q_html": "&iquest;Cu&aacute;ndo puedo romper confidencialidad?", "a_plain": "Ante riesgo vital inminente, abuso a menor o adulto vulnerable, mandato judicial u obligaciones legales espec\u00edficas. Documente decisi\u00f3n y base legal en historia cl\u00ednica.", "a_html": "Riesgo vital, abuso, mandato judicial u obligaci&oacute;n legal."},
            {"q": "\u00bfQu\u00e9 exige la ley en telepsicolog\u00eda?", "q_html": "&iquest;Qu&eacute; exige la ley en telepsicolog&iacute;a?", "a_plain": "Consentimiento informado para modalidad remota, protecci\u00f3n de datos, identificaci\u00f3n del paciente y plan de manejo de crisis. Cumpla gu\u00edas del colegio profesional y MINSAL.", "a_html": "Consentimiento remoto, protecci&oacute;n de datos y plan de crisis."},
        ],
        "related": [("historia-clinica-psicologica-paso-a-paso", "Historia cl&iacute;nica paso a paso"), ("consentimiento-informado-psicologia-mexico", "Consentimiento informado"), ("como-redactar-informe-psicologico", "Informe psicol&oacute;gico"), ("etica-psicologo-mexico", "&Eacute;tica profesional")],
        "references": ['<a href="https://www.bcn.cl/leychile/" rel="nofollow noopener noreferrer" target="_blank">Biblioteca del Congreso Nacional de Chile &mdash; Ley 20.584</a>'],
    }


def _article7() -> dict:
    return {
        "slug": "cie-11-vs-dsm-5-diferencias",
        "title": "CIE-11 vs DSM-5: Diferencias Clave para Psic\u00f3logos Cl\u00ednicos | Kalyo",
        "description": "CIE-11 vs DSM-5: OMS vs APA, tabla comparativa depresi&oacute;n, ansiedad, TDAH, TEA, TEPT, TOC, criterios, uso por contexto, normativa MX/CO/AR/PE/CL/ES y documentaci&oacute;n en HC.",
        "description_plain": "CIE-11 vs DSM-5: OMS vs APA, tabla comparativa depresión, ansiedad, TDAH, TEA, TEPT, TOC, criterios, uso por contexto, normativa MX/CO/AR/PE/CL/ES y documentación en HC.",
        "keywords": "CIE-11 vs DSM-5, ICD-11, clasificaci\u00f3n diagn\u00f3stica, psic\u00f3logos cl\u00ednicos, LATAM, depresi\u00f3n, TDAH, TEPT",
        "h1": "CIE-11 vs DSM-5: diferencias clave para psic&oacute;logos cl&iacute;nicos",
        "intro": f"<strong>CIE-11</strong> (OMS) y <strong>DSM-5</strong> (APA) son los sistemas diagn&oacute;sticos m&aacute;s usados en salud mental. No son id&eacute;nticos: difieren en estructura, categor&iacute;as y algunos criterios. Esta gu&iacute;a compara trastornos frecuentes (depresi&oacute;n, ansiedad, TDAH, TEA, TEPT, TOC), orienta cu&aacute;l usar seg&uacute;n contexto legal y asegurador en M&eacute;xico, Colombia, Argentina, Per&uacute;, Chile y Espa&ntilde;a, y c&oacute;mo documentar ambos en <a href=\"{HC}\">historia cl&iacute;nica psicol&oacute;gica</a>.",
        "hero_alt": "Comparativa CIE-11 y DSM-5 en escritorio de psic\u00f3logo cl\u00ednico",
        "inline_alt": "Tabla comparativa CIE-11 vs DSM-5 trastornos mentales",
        "meta_label": "Diagn&oacute;stico diferencial &middot; Actualizaci&oacute;n 2026",
        "body_html": textwrap.dedent("""
    <h2>OMS vs APA: prop&oacute;sitos distintos</h2>
    <p>La <strong>CIE-11</strong> es clasificaci&oacute;n internacional de enfermedades para estad&iacute;stica, salud p&uacute;blica y sistemas nacionales de salud. El <strong>DSM-5</strong> es manual diagn&icoacute;stico de la APA orientado a cl&iacute;nica e investigaci&oacute;n en psiquiatr&iacute;a y psicolog&iacute;a, muy difundido en formaci&oacute;n universitaria LATAM.</p>
    <p>Ninguno es &laquo;m&aacute;s verdadero&raquo;; son herramientas estandarizadas. El cl&iacute;nico diagnostica por criterios cl&iacute;nicos integrados con entrevista, historia y pruebas; los c&oacute;digos comunican el juicio profesional a terceros.</p>
    <p>Conozca qu&eacute; exige su colegio profesional, hospital, aseguradora o tribunal: a veces CIE obligatorio, a veces DSM aceptado en privado.</p>

    <h2>Tabla comparativa por trastornos frecuentes</h2>
    <table class="items-table">
      <thead><tr><th>Trastorno</th><th>CIE-11 (ejemplo)</th><th>DSM-5 (ejemplo)</th><th>Diferencia cl&iacute;nica notable</th></tr></thead>
      <tbody>
        <tr><td>Depresi&oacute;n</td><td>6A70.x subtipos</td><td>296.xx / F32-F33 CIE-10 legacy</td><td>CIE-11 enfatiza curso y gravedad funcional</td></tr>
        <tr><td>Ansiedad generalizada</td><td>6B00</td><td>300.02</td><td>Criterios temporales similares; redacci&oacute;n distinta</td></tr>
        <tr><td>TDAH</td><td>6A70</td><td>314.0x</td><td>Presentaciones convergentes; edad inicio</td></tr>
        <tr><td>TEA</td><td>6A02 espectro</td><td>299.00 espectro</td><td>Niveles de apoyo vs gravedad DSM-5</td></tr>
        <tr><td>TEPT</td><td>6B40; CPSD 6B41</td><td>309.81; no CPSD pleno</td><td>CIE-11 reconoce TEPT complejo expl&iacute;cito</td></tr>
        <tr><td>TOC</td><td>6B20</td><td>300.3</td><td>Estructura dimensional CIE-11 m&aacute;s marcada</td></tr>
      </tbody>
    </table>
    <p>Consulte manuales completos antes de peritajes; esta tabla es orientativa.</p>

    <h2>Criterios y enfoque dimensional</h2>
    <p>CIE-11 incorpora m&aacute;s <strong>dimensiones de gravedad</strong> (p. ej. trastornos de personalidad) y espectros. DSM-5 introdujo especificadores y algunos espectros (autismo, adicciones) pero mantiene categor&iacute;as m&aacute;s cl&aacute;sicas en otros cap&iacute;tulos.</p>
    <p>En pr&aacute;ctica, muchos criterios nucleares se solapan: episodio depresivo mayor, ataques de p&aacute;nico, obsesiones/compulsiones. Las discrepancias aparecen en casos l&iacute;mite, comorbilidades y codificaci&oacute;n administrativa.</p>
    <p>Documente <em>qu&eacute; criterios</em> cumple el paciente en prosa cl&iacute;nica, no solo el c&oacute;digo; facilita auditor&iacute;a si cambia sistema.</p>

    <h2>Cu&aacute;l usar seg&uacute;n contexto</h2>
    <p><strong>Salud p&uacute;blica e informes oficiales:</strong> CIE-11 (o CIE-10 mientras transici&oacute;n) en MX, CO, AR, PE, CL, ES seg&uacute;n ministerio. <strong>Investigaci&oacute;n internacional:</strong> a menudo DSM-5 por tradici&oacute;n de journals. <strong>Cl&iacute;nica privada:</strong> frecuente DSM-5 en formularios, pero verifique aseguradora.</p>
    <p>Peritajes judiciales: siga mandato del tribunal o perito coordinador. Informes escolares: a vece piden DSM; sistemas GES Chile usan diagn&oacute;sticos F/CIE.</p>
    <p>Capacitaci&oacute;n: domine un sistema primario y conozca equivalencias del otro. Cursos OPS/APA ayudan.</p>

    <h2>Normativa por pa&iacute;s (MX, CO, AR, PE, CL, ES)</h2>
    <p><strong>M&eacute;xico:</strong> CIE en SSA; DSM com&uacute;n en privado. <strong>Colombia:</strong> Res. 5596 CIE-10; migraci&oacute;n CIE-11 en curso. <strong>Argentina:</strong> mixto por obra social/provincia. <strong>Per&uacute;:</strong> MINSA alineado OMS. <strong>Chile:</strong> GES con CIE-10; actualizaci&oacute;n gradual. <strong>Espa&ntilde;a:</strong> CIE-10-ES cl&iacute;nico, roadmap CIE-11. Verifique siempre circular vigente.</p>

    <h2>Documentar ambos sistemas en HC</h2>
    <p>Cuando el destinatario lo requiera, consigne: diagn&oacute;stico principal en sistema obligatorio, equivalencia secundaria, criterios cumplidos, gravedad funcional, comorbilidades y plan. Ejemplo: &laquo;TEPT CIE-11 6B40 / DSM-5 309.81; criterios A-H cumplidos; CPSD no aplicable&raquo;.</p>
    <p>Evite listar c&oacute;digos contradictorios sin explicaci&oacute;n. En <a href="/articulos/que-es-el-dsm-5.html">formaci&oacute;n DSM-5</a> y capacitaci&oacute;n CIE-11, mantenga fichas de equivalencia personalizadas por pa&iacute;s.</p>
    <p>Sistemas EHR reducen errores de codificaci&oacute;n; revisi&oacute;n humana sigue siendo responsabilidad profesional del psic&oacute;logo cl&iacute;nico.</p>
        """),
        "faqs": [
            {"q": "\u00bfCu\u00e1l est\u00e1 m\u00e1s actualizado, CIE-11 o DSM-5?", "q_html": "&iquest;Cu&aacute;l est&aacute; m&aacute;s actualizado, CIE-11 o DSM-5?", "a_plain": "CIE-11 (2022) es m\u00e1s reciente que DSM-5 (2013); existe DSM-5-TR (2022) con revisiones menores. Ninguno invalida al otro; elija seg\u00fan contexto legal y cl\u00ednico.", "a_html": "CIE-11 m&aacute;s reciente; DSM-5-TR revisiones menores."},
            {"q": "\u00bfQu\u00e9 piden las aseguradoras?", "q_html": "&iquest;Qu&eacute; piden las aseguradoras?", "a_plain": "Var\u00eda: muchas exigen CIE-10/CIE-11 en reembolsos p\u00fablicos; privadas internacionales a veces aceptan DSM-5. Consulte convenio y formulario antes del informe.", "a_html": "Var&iacute;a por aseguradora y pa&iacute;s."},
            {"q": "\u00bfPuedo usar ambos a la vez?", "q_html": "&iquest;Puedo usar ambos a la vez?", "a_plain": "S\u00ed, documentando criterios y c\u00f3digos equivalentes cuando aporta claridad. Priorice el sistema exigido por la instituci\u00f3n destinataria del informe.", "a_html": "S&iacute;, con criterios claros y prioridad al sistema exigido."},
            {"q": "\u00bfCu\u00e1ndo sale el DSM-6?", "q_html": "&iquest;Cu&aacute;ndo sale el DSM-6?", "a_plain": "La APA no ha anunciado fecha de DSM-6; se esperan a\u00f1os de desarrollo y revisi\u00f3n. Mantenga actualizaci\u00f3n con CIE-11 y DSM-5-TR mientras tanto.", "a_html": "Sin fecha anunciada; use CIE-11 y DSM-5-TR."},
        ],
        "related": [("que-es-el-dsm-5", "Qu&eacute; es el DSM-5"), ("cie-11-trastornos-mentales-psicologos", "CIE-11 trastornos mentales"), ("historia-clinica-psicologica-paso-a-paso", "Historia cl&iacute;nica"), ("como-redactar-informe-psicologico", "Redactar informe psicol&oacute;gico")],
    }
