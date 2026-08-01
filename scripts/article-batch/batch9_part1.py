# -*- coding: utf-8 -*-
"""Batch 9 part 1: article specs 21-25 for Kalyo AEO blog."""
from __future__ import annotations

import re


def p(*paras: str) -> str:
    return "".join(f"<p>{x}</p>" for x in paras)


def wc(text: str) -> int:
    t = re.sub(r"<[^>]+>", " ", text)
    repl = {
        "&mdash;": "—", "&ndash;": "–", "&oacute;": "ó", "&aacute;": "á",
        "&eacute;": "é", "&iacute;": "í", "&uacute;": "ú", "&ntilde;": "ñ",
        "&uuml;": "ü", "&amp;": "&",
    }
    for a, b in repl.items():
        t = t.replace(a, b)
    return len(re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ]+\b", t, flags=re.UNICODE))


def body_words(spec: dict) -> int:
    parts = [spec.get("intro_long") or spec.get("intro", "")]
    for s in spec["sections"]:
        parts.append(s["html"])
    for f in spec["faqs"]:
        parts.append(f["q"] + " " + f["a"])
    return sum(wc(x) for x in parts)


ARTICLES: list[dict] = []

# --- 21 escalas-ansiedad-psicologia-clinica ---
ARTICLES.append(
    {
        "slug": "escalas-ansiedad-psicologia-clinica",
        "title": "Escalas de ansiedad en psicolog&iacute;a cl&iacute;nica: gu&iacute;a | Kalyo",
        "description": "Escalas de ansiedad para psic&oacute;logos en M&eacute;xico: cu&aacute;ndo usar GAD-7, STAI, Zung o PASS, criterios cl&iacute;nicos, l&iacute;mites y registro seguro en expediente digital.",
        "keywords": "escalas de ansiedad, GAD-7, STAI, Zung, PASS, psicolog&iacute;a cl&iacute;nica, tamizaje ansiedad, evaluaci&oacute;n psicol&oacute;gica M&eacute;xico",
        "h1": "Escalas de ansiedad en psicolog&iacute;a cl&iacute;nica: c&oacute;mo elegir y aplicar",
        "breadcrumb_short": "Escalas de ansiedad",
        "hero_alt": "Psic&oacute;logo aplicando escalas de ansiedad en consulta cl&iacute;nica digital",
        "inline_alt": "Comparativa de escalas de ansiedad autorreportadas en psicolog&iacute;a cl&iacute;nica",
        "quick_answer": "Las <strong>escalas de ansiedad</strong> son cuestionarios breves que orientan severidad y seguimiento, no sustituyen el diagn&oacute;stico. En consulta privada mexicana suelen usarse GAD-7 para ansiedad generalizada, STAI para estado y rasgo, Zung en contextos cl&aacute;sicos y PASS cuando interesa la sensibilidad a sensaciones corporales. Elija seg&uacute;n objetivo cl&iacute;nico, tiempo disponible y versi&oacute;n en espa&ntilde;ol con manual local.",
        "intro_long": "Elegir entre las distintas <strong>escalas de ansiedad</strong> puede abrumar al cl&iacute;nico que inicia consulta o actualiza su bater&iacute;a. En M&eacute;xico, donde conviven modelos de atenci&oacute;n p&uacute;blica, privada y telepsicolog&iacute;a, lo pr&aacute;ctico es combinar tamizaje breve, entrevista cl&iacute;nica estructurada y registro longitudinal en expediente. Este art&iacute;culo resume cu&aacute;ndo aplicar instrumentos frecuentes, c&oacute;mo interpretarlos sin sobremedicalizar malestar normativo y c&oacute;mo documentar resultados de forma &eacute;tica. Tambi&eacute;n aborda errores comunes: aplicar demasiados cuestionarios en una sesi&oacute;n, olvidar exploraci&oacute;n de p&aacute;nico o trauma, o comunicar puntajes sin devoluci&oacute;n terap&eacute;utica. No reemplaza manuales oficiales ni formaci&oacute;n en psicometr&iacute;a; orienta decisiones cotidianas en gabinete con criterio prudente.",
        "meta_label": "Psicometr&iacute;a cl&iacute;nica &middot; Actualizaci&oacute;n 2026",
        "cta_h2": "Gestiona el expediente de tus pacientes con Kalyo",
        "cta_p": "Expediente cl&iacute;nico, tests y notas en una sola plataforma &mdash; kalyo.io",
        "sections": [
            {
                "h2": "Qu&eacute; miden las escalas de ansiedad y qu&eacute; no",
                "html": p(
                    "Las <strong>escalas de ansiedad</strong> autorreportadas recogen s&iacute;ntomas subjetivos en un periodo definido: preocupaci&oacute;n excesiva, tensi&oacute;n som&aacute;tica, irritabilidad, evitaci&oacute;n o sensaci&oacute;n de peligro inminente. Son &uacute;tiles para tamizaje, planificar intervenci&oacute;n y comparar cambio entre sesiones. No confirman por s&iacute; solas trastorno de ansiedad generalizada, p&aacute;nico o fobia espec&iacute;fica; el DSM-5 y la entrevista cl&iacute;nica integran duraci&oacute;n, deterioro funcional y diferencial con depresi&oacute;n, trauma, consumo de sustancias o condiciones m&eacute;dicas.",
                    "En poblaci&oacute;n mexicana conviene considerar expresiones som&aacute;ticas frecuentes (palpitaciones, mareo, tensi&oacute;n muscular) y evitar interpretar puntajes altos sin explorar contexto: estr&eacute;s laboral reciente, duelo, violencia de pareja o insomnio cr&oacute;nico pueden elevar respuestas sin cumplir criterios completos. Documente siempre el prop&oacute;sito: tamizaje inicial, seguimiento terap&eacute;utico o informe pericial con consentimiento espec&iacute;fico.",
                    "Diferencie ansiedad normativa ante examen, entrevista laboral o procedimiento m&eacute;dico de trastorno que requiere tratamiento. Pregunte duraci&oacute;n, frecuencia, evitaci&oacute;n y costo funcional. Si el paciente reporta ataques de p&aacute;nico, explore sensibilidad som&aacute;tica con <a href=\"/articulos/pass-sensibilidad-ansiedad.html\">PASS</a> en una sesi&oacute;n dedicada, no mezclada con cinco cuestionarios m&aacute;s.",
                )
                + """
<ul>
<li><strong>Tamizaje:</strong> detectar posible ansiedad cl&iacute;nica y priorizar exploraci&oacute;n.</li>
<li><strong>Seguimiento:</strong> graficar cambio tras TCC, exposici&oacute;n o intervenci&oacute;n farmacol&oacute;gica coordinada.</li>
<li><strong>Comunicaci&oacute;n:</strong> psicoeducar al paciente con lenguaje accesible sobre su perfil sintom&aacute;tico.</li>
</ul>""",
            },
            {
                "h2": "GAD-7: tamizaje breve de ansiedad generalizada",
                "html": p(
                    "El <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a> es uno de los instrumentos m&aacute;s usados por su brevedad (siete &iacute;tems) y aplicaci&oacute;n en atenci&oacute;n primaria y consulta psicol&oacute;gica. Explora preocupaci&oacute;n, nerviosismo, dificultad para relajarse, inquietud, irritabilidad, miedo a que algo malo ocurra y molestias som&aacute;ticas asociadas. Los puntos de corte habituales en gu&iacute;as cl&iacute;nicas distinguen ansiedad m&iacute;nima, leve, moderada y severa; &uacute;selos como orientaci&oacute;n, no como veredicto diagn&oacute;stico autom&aacute;tico.",
                    "Ventajas en M&eacute;xico: f&aacute;cil de aplicar en teleconsulta, integrable en expediente digital y repetible cada cuatro a ocho semanas. Limitaciones: no diferencia subtipos de ansiedad ni detecta fobias espec&iacute;ficas sin entrevista. Si el puntaje es alto, ampl&iacute;e con exploraci&oacute;n de ataques de p&aacute;nico, obsesiones, trauma y consumo de cafe&iacute;na o estimulantes. Para profundizar en interpretaci&oacute;n cl&iacute;nica, revise la gu&iacute;a sobre <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">c&oacute;mo interpretar tests psicol&oacute;gicos</a>.",
                ),
            },
            {
                "h2": "STAI: ansiedad estado versus rasgo",
                "html": p(
                    "El <a href=\"/articulos/stai-ansiedad-estado-rasgo.html\">STAI</a> separa <strong>ansiedad-estado</strong> (reactividad al momento o situaci&oacute;n evaluada) de <strong>ansiedad-rasgo</strong> (tendencia estable a experimentar ansiedad). Esa distinci&oacute;n es cl&iacute;nicamente valiosa antes de sesiones de exposici&oacute;n, evaluaciones periciales o pruebas acad&eacute;micas estresantes: un puntaje alto en estado puede reflejar contexto evaluativo, no necesariamente patolog&iacute;a de personalidad.",
                    "Aplique el STAI cuando necesite comparar activaci&oacute;n pre y post intervenci&oacute;n, en investigaci&oacute;n de estr&eacute;s acad&eacute;mico o en pacientes que minimizan s&iacute;ntomas cr&oacute;nicos pero muestran marcada activaci&oacute;n situacional. Requiere m&aacute;s tiempo que GAD-7; reserve para evaluaciones integrales o cuando el diferencial estado/rasgo informa el plan terap&eacute;utico. Registre condiciones de aplicaci&oacute;n (hora, lugar, presencia de acompa&ntilde;ante) para evitar interpretaciones err&oacute;neas.",
                )
                + """
<table class="items-table">
<thead><tr><th>Instrumento</th><th>Enfoque</th><th>Nota cl&iacute;nica</th></tr></thead>
<tbody>
<tr><td>GAD-7</td><td>Ansiedad generalizada reciente</td><td>Tamizaje r&aacute;pido y seguimiento</td></tr>
<tr><td>STAI</td><td>Estado vs rasgo</td><td>&Uacute;til pre/post intervenci&oacute;n</td></tr>
<tr><td>Zung</td><td>Ansiedad global cl&aacute;sica</td><td>Contextos con experiencia previa</td></tr>
<tr><td>PASS</td><td>Sensibilidad ansiedad</td><td>Complemento en s&iacute;ntomas som&aacute;ticos</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "Zung y PASS: cu&aacute;ndo sumarlos a la bater&iacute;a",
                "html": p(
                    "La <a href=\"/articulos/zung-escala-ansiedad.html\">escala de ansiedad de Zung</a> permanece en uso por tradici&oacute;n docente y cl&iacute;nica en varios entornos hispanohablantes. Cubre aspectos cognitivos, som&aacute;ticos y auton&oacute;micos con formato Likert. Puede ser &uacute;til cuando el paciente ya conoce el instrumento o cuando el centro donde usted labora estandariz&oacute; su interpretaci&oacute;n interna con supervisi&oacute;n.",
                    "El <a href=\"/articulos/pass-sensibilidad-ansiedad.html\">PASS</a> (cuestionario de sensibilidad a la ansiedad) orienta el miedo a sensaciones corporales asociadas a ansiedad, relevante en trastorno de p&aacute;nico, hipocondr&iacute;a leve o pacientes que interpretan taquicardia o mareo como se&ntilde;al de cat&aacute;strofe. No sustituye entrevista de p&aacute;nico ni interocepci&oacute;n cl&iacute;nica, pero gu&iacute;a psicoeducaci&oacute;n sobre ciclo sensaci&oacute;n-catastrofizaci&oacute;n-evitaci&oacute;n. Combine PASS con GAD-7 o STAI seg&uacute;n hip&oacute;tesis, evitando fatiga por exceso de cuestionarios en una sola sesi&oacute;n.",
                ),
            },
            {
                "h2": "Protocolo pr&aacute;ctico de aplicaci&oacute;n en consulta",
                "html": p(
                    "Proponga un flujo reproducible: (1) entrevista breve sobre motivo de consulta y contexto; (2) tamizaje con GAD-7 si busca eficiencia; (3) ampliaci&oacute;n con STAI, Zung o PASS seg&uacute;n hip&oacute;tesis; (4) devoluci&oacute;n al paciente en lenguaje claro; (5) reevaluaci&oacute;n programada. Explique que las escalas son herramientas de apoyo, no etiquetas definitivas. Obtenga consentimiento informado cuando los resultados integran informes externos, como orienta la pr&aacute;ctica descrita en <a href=\"/articulos/consentimiento-informado-psicologia.html\">consentimiento informado en psicolog&iacute;a</a>.",
                    "En telepsicolog&iacute;a, confirme que el paciente completa el cuestionario sin interrupciones y en privacidad. Evite aplicar m&uacute;ltiples escalas redundantes el mismo d&iacute;a salvo evaluaci&oacute;n integral planificada. Archivar puntajes, fecha, versi&oacute;n del instrumento y observaciones conductuales durante la aplicaci&oacute;n mejora trazabilidad ante auditor&iacute;as &eacute;ticas o solicitudes de informe.",
                )
                + """
<ol>
<li>Registrar motivo de evaluaci&oacute;n y contexto vital reciente.</li>
<li>Elegir escala principal seg&uacute;n objetivo (tamizaje vs diferencial).</li>
<li>Integrar resultados con entrevista y observaci&oacute;n cl&iacute;nica.</li>
<li>Planificar reevaluaci&oacute;n con intervalo acordado con el paciente.</li>
</ol>""",
            },
            {
                "h2": "Interpretaci&oacute;n &eacute;tica y registro en expediente",
                "html": p(
                    "Interprete puntajes como hip&oacute;tesis cl&iacute;nicas: un GAD-7 elevado con functioning laboral intacto puede orientar psicoeducaci&oacute;n y manejo de estr&eacute;s; el mismo puntaje con evitaci&oacute;n marcada, insomnio y deterioro relacional sugiere plan de tratamiento m&aacute;s intensivo. Evite language alarmista; prefiera descripci&oacute;n dimensional y metas compartidas.",
                    "Centralizar escalas repetidas, notas de sesi&oacute;n y acuerdos terap&eacute;uticos en un expediente cl&iacute;nico digital reduce p&eacute;rdida de datos entre consultas y facilita gr&aacute;ficas de progreso. Documente limitaciones: autocuestionario sujeto a deseabilidad social, estado de &aacute;nimo del d&iacute;a y comprensi&oacute;n lectora. Si el paciente tiene baja escolaridad, aplique con asistencia de lectura sin alterar contenido de &iacute;tems.",
                    "En informes para escuela o empresa, evite incluir puntajes crudos sin contexto cl&iacute;nico ni consentimiento espec&iacute;fico. Describa recomendaciones funcionales cuando proceda. Si combina ansiedad con depresi&oacute;n, considere tamizaje complementario con <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a> para no perder sintomatolog&iacute;a afectiva que modifica prioridades terap&eacute;uticas.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "&iquest;Basta una escala de ansiedad para diagnosticar?",
                "a": "No. Las escalas orientan severidad y seguimiento; el diagn&oacute;stico requiere entrevista cl&iacute;nica, criterios DSM-5 o CIE-11, exploraci&oacute;n de comorbilidades y, cuando corresponda, derivaci&oacute;n m&eacute;dica para descartar causas org&aacute;nicas.",
            },
            {
                "q": "&iquest;GAD-7 o STAI en primera sesi&oacute;n?",
                "a": "GAD-7 suele ser m&aacute;s pr&aacute;ctico por brevedad. Elija STAI si necesita diferenciar ansiedad situacional de rasgo o comparar activaci&oacute;n antes y despu&eacute;s de una intervenci&oacute;n espec&iacute;fica.",
            },
            {
                "q": "&iquest;Con qu&eacute; frecuencia repetir las escalas?",
                "a": "En tratamiento activo, cada cuatro a ocho semanas es habitual. Ajuste seg&uacute;n gravedad, tipo de intervenci&oacute;n y acuerdo con el paciente; evite repetir sin devolver resultados ni utilidad cl&iacute;nica.",
            },
            {
                "q": "&iquest;Puedo aplicar escalas por telepsicolog&iacute;a?",
                "a": "S&iacute;, si garantiza confidencialidad, identidad del respondiente y comprensi&oacute;n de instrucciones. Registre modalidad de aplicaci&oacute;n y cualquier dificultad t&eacute;cnica que pueda afectar validez aparente.",
            },
            {
                "q": "&iquest;Qu&eacute; hacer si el paciente niega s&iacute;ntomas pero el puntaje es alto?",
                "a": "Explore discrepancia con empat&iacute;a: verg&uuml;enza, miedo a diagn&oacute;stico, deseabilidad social o diferencias entre malestar subjetivo y reporte. Contraste con ejemplos conductuales concretos de las &uacute;ltimas semanas. Repita la escala en otra sesi&oacute;n si el rapport inicial fue tenso; a veces el primer puntaje refleja desconfianza m&aacute;s que ausencia real de s&iacute;ntomas.",
            },
        ],
        "related": [
            {"href": "/articulos/que-es-el-gad-7.html", "label": "GAD-7: escala de ansiedad generalizada"},
            {"href": "/articulos/stai-ansiedad-estado-rasgo.html", "label": "STAI: ansiedad estado y rasgo"},
            {"href": "/articulos/pass-sensibilidad-ansiedad.html", "label": "PASS: sensibilidad a la ansiedad"},
            {"href": "/articulos/como-interpretar-tests-psicologicos.html", "label": "C&oacute;mo interpretar tests psicol&oacute;gicos"},
        ],
    }
)

# --- 22 escalas-depresion-validadas-espanol ---
ARTICLES.append(
    {
        "slug": "escalas-depresion-validadas-espanol",
        "title": "Escalas de depresi&oacute;n validadas en espa&ntilde;ol: gu&iacute;a | Kalyo",
        "description": "Escalas de depresi&oacute;n en espa&ntilde;ol para psic&oacute;logos: PHQ-9, BDI-II, CES-D, cu&aacute;ndo usarlas, l&iacute;mites cl&iacute;nicos, riesgo suicida y registro en consulta mexicana.",
        "keywords": "escalas de depresi&oacute;n, PHQ-9, BDI-II, CES-D, depresi&oacute;n espa&ntilde;ol, psicolog&iacute;a cl&iacute;nica, tamizaje depresi&oacute;n M&eacute;xico",
        "h1": "Escalas de depresi&oacute;n validadas en espa&ntilde;ol: selecci&oacute;n cl&iacute;nica",
        "breadcrumb_short": "Escalas de depresi&oacute;n",
        "hero_alt": "Aplicaci&oacute;n de escalas de depresi&oacute;n en espa&ntilde;ol en consultorio psicol&oacute;gico",
        "inline_alt": "PHQ-9, BDI-II y CES-D como herramientas de tamizaje depresivo",
        "quick_answer": "Las <strong>escalas de depresi&oacute;n</strong> en espa&ntilde;ol m&aacute;s usadas en consulta son PHQ-9 (tamizaje breve alineado a criterios), BDI-II (severidad sintom&aacute;tica amplia) y CES-D (epidemiolog&iacute;a y comunidad). Ninguna sustituye entrevista ni evaluaci&oacute;n de riesgo suicida. Elija seg&uacute;n tiempo, poblaci&oacute;n y si necesita seguimiento dimensional repetido en expediente cl&iacute;nico.",
        "intro_long": "Trabajar con <strong>escalas de depresi&oacute;n</strong> exige distinguir tamizaje, evaluaci&oacute;n de severidad y monitorizaci&oacute;n terap&eacute;utica. En M&eacute;xico muchos pacientes llegan con somatizaciones, duelos no reconocidos o agotamiento laboral que elevan puntajes sin cumplir episodio depresivo mayor completo. Este art&iacute;culo compara PHQ-9, BDI-II y CES-D en espa&ntilde;ol desde la pr&aacute;ctica cl&iacute;nica: cu&aacute;ndo aplicar cada uno, c&oacute;mo comunicar resultados sin estigmatizar y c&oacute;mo integrarlos con exploraci&oacute;n de ideaci&oacute;n suicida. Tambi&eacute;n revisa errores frecuentes: diagnosticar solo por puntaje, ignorar man&iacute;a o consumo de alcohol, o no repetir escalas cuando el tratamiento ya cambi&oacute;. Evitamos cifras psicom&eacute;tricas no verificables; priorizamos criterio cl&iacute;nico responsable en consultorio privado y comunitario.",
        "meta_label": "Psicometr&iacute;a cl&iacute;nica &middot; Actualizaci&oacute;n 2026",
        "cta_h2": "Gestiona el expediente de tus pacientes con Kalyo",
        "cta_p": "Expediente cl&iacute;nico, tests y notas en una sola plataforma &mdash; kalyo.io",
        "sections": [
            {
                "h2": "Funci&oacute;n cl&iacute;nica de las escalas de depresi&oacute;n",
                "html": p(
                    "Las <strong>escalas de depresi&oacute;n</strong> cuantifican s&iacute;ntomas como humor bajo, anhedonia, alteraciones del sue&ntilde;o o apetito, fatiga, culpa, dificultad concentraci&oacute;n e ideaci&oacute;n de muerte. Su valor est&aacute; en estandarizar preguntas, facilitar seguimiento y mejorar comunicaci&oacute;n entre profesionales. No definen por s&iacute; solas un trastorno; el cl&iacute;nico integra duraci&oacute;n, exclusiones (sustancias, luto, condiciones m&eacute;dicas) y deterioro funcional.",
                    "En espa&ntilde;ol, verifique que utiliza versiones con instrucciones claras para su poblaci&oacute;n (escolaridad, variantes regionales). En consulta mexicana es frecuente encontrar depresi&oacute;n com&oacute;rbida con ansiedad, trauma o dolor cr&oacute;nico; los puntajes deben leerse en ese contexto biopsicosocial, no como n&uacute;meros aislados en un informe.",
                ),
            },
            {
                "h2": "PHQ-9: tamizaje alineado a criterios depresivos",
                "html": p(
                    "El <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a> es ampliamente adoptado por brevedad y correspondencia pr&aacute;ctica con s&iacute;ntomas del episodio depresivo mayor. Incluye &iacute;tem sobre ideas de autolesi&oacute;n o muerte que obliga a exploraci&oacute;n de riesgo suicida inmediata si se endosa. Los puntos de corte usuales distinguen depresi&oacute;n m&iacute;nima, leve, moderada y severa; util&iacute;celos para orientar intensidad de intervenci&oacute;n y derivaci&oacute;n psiqui&aacute;trica, no como etiqueta autom&aacute;tica.",
                    "Ventajas: aplicaci&oacute;n r&aacute;pida, repetici&oacute;n en seguimiento y compatibilidad con atenci&oacute;n primaria. Limitaciones: solapamiento con s&iacute;ntomas f&iacute;sicos cr&oacute;nicos; un paciente con hipotiroidismo o insomnio severo puede puntuar alto sin episodio depresivo puro. Combine con entrevista cl&iacute;nica y, cuando proceda, exploraci&oacute;n m&eacute;dica. Para criterios de interpretaci&oacute;n responsable, consulte <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">c&oacute;mo interpretar tests psicol&oacute;gicos</a>.",
                ),
            },
            {
                "h2": "BDI-II: severidad sintom&aacute;tica en profundidad",
                "html": p(
                    "El <a href=\"/articulos/inventario-depresion-beck-bdi.html\">Inventario de Depresi&oacute;n de Beck (BDI-II)</a> ofrece un perfil m&aacute;s amplio de s&iacute;ntomas cognitivos y som&aacute;ticos. Es &uacute;til cuando necesita describir severidad con mayor granularidad en informes cl&iacute;nicos o investigaci&oacute;n aplicada con supervisi&oacute;n. Requiere m&aacute;s tiempo que PHQ-9; valore fatiga del paciente en sesiones largas.",
                    "Interpretar BDI-II implica revisar patrones por &aacute;reas (cognici&oacute;n negativa, s&iacute;ntomas som&aacute;ticos, afecto) m&aacute;s que obsesionarse con un total &uacute;nico. En pacientes con enfermedad m&eacute;dica, algunos &iacute;tems som&aacute;ticos pueden inflarse sin indicar necesariamente depresi&oacute;n primaria. Documente esa limitaci&oacute;n al redactar conclusiones.",
                )
                + """
<table class="items-table">
<thead><tr><th>Escala</th><th>Extensi&oacute;n</th><th>Uso t&iacute;pico</th></tr></thead>
<tbody>
<tr><td>PHQ-9</td><td>9 &iacute;tems</td><td>Tamizaje y seguimiento breve</td></tr>
<tr><td>BDI-II</td><td>21 &iacute;tems</td><td>Severidad y perfil sintom&aacute;tico</td></tr>
<tr><td>CES-D</td><td>20 &iacute;tems</td><td>Tamizaje comunitario o investigaci&oacute;n</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "CES-D: utilidad en comunidad y investigaci&oacute;n",
                "html": p(
                    "La <a href=\"/articulos/ces-d-escala-depresion.html\">CES-D</a> fue dise&ntilde;ada para detectar sintomatolog&iacute;a depresiva en estudios poblacionales. Incluye &iacute;tems sobre tristeza, miedo, sue&ntilde;o, soledad y esperanza; algunos est&aacute;n redactados en sentido positivo y requieren puntuaci&oacute;n invertida seg&uacute;n manual. En consulta individual puede servir cuando busca instrumento con sensibilidad a malestar subcl&iacute;nico en contextos comunitarios, universitarios o laborales.",
                    "No es sustituto de evaluaci&oacute;n de riesgo suicida estructurada si hay alertas cl&iacute;nicas. Al comparar CES-D con PHQ-9, evite doble aplicaci&oacute;n redundante sin prop&oacute;sito; el paciente puede percibir repetici&oacute;n como falta de escucha cl&iacute;nica.",
                ),
            },
            {
                "h2": "Seguridad, suicidio y derivaci&oacute;n",
                "html": p(
                    "Todo protocolo con <strong>escalas de depresi&oacute;n</strong> debe incluir exploraci&oacute;n de ideaci&oacute;n suicida aunque el cuestionario no la destaque. PHQ-9 incluye un &iacute;tem directo; si se endosa, indague plan, medios, intentos previos y factores protectores antes de cerrar sesi&oacute;n. En M&eacute;xico, conozca líneas de crisis locales y rutas de urgencia psiqui&aacute;trica de su entidad.",
                    "Derive cuando hay riesgo inminente, psicosis, man&iacute;a, dependencia severa de alcohol o deterioro funcional extremo con resistencia al tratamiento ambulatorio. El psic&oacute;logo documenta indicaci&oacute;n, contactos de emergencia acordados y continuidad posterior. Obtenga consentimiento para compartir informes con otros profesionales seg&uacute;n <a href=\"/articulos/consentimiento-informado-psicologia.html\">consentimiento informado en psicolog&iacute;a</a>.",
                )
                + """
<ul>
<li><strong>Riesgo bajo:</strong> seguimiento ambulatorio y plan de seguridad b&aacute;sico.</li>
<li><strong>Riesgo moderado:</strong> aumentar frecuencia, involucrar red de apoyo con permiso.</li>
<li><strong>Riesgo alto:</strong> no dejar solo; activar protocolo de urgencia institucional.</li>
</ul>""",
            },
            {
                "h2": "Integraci&oacute;n en historial y seguimiento terap&eacute;utico",
                "html": p(
                    "Registre fecha, puntaje total, subescalas si aplica, versi&oacute;n del instrumento y observaciones (llanto durante aplicaci&oacute;n, dificultad lectora, presencia de familiar). Repita escalas en intervalos acordados para visualizar respuesta a TCC, activaci&oacute;n conductual o tratamiento psiqui&aacute;trico conjunto. Devuelva resultados al paciente: muchos desconocen que la mejora parcial es progreso v&aacute;lido.",
                    "Un expediente digital ordenado evita comparar puntajes de instrumentos distintos como si fueran equivalentes. Si cambia de PHQ-9 a BDI-II, explique al paciente que las m&eacute;tricas no son directamente comparables. La consistencia cl&iacute;nica importa m&aacute;s que acumular cuestionarios.",
                    "Cuando la depresi&oacute;n coexiste con ansiedad marcada, complemente con <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a> o <a href=\"/articulos/stai-ansiedad-estado-rasgo.html\">STAI</a> para priorizar intervenciones. En seguimiento, celebre mejor&iacute;as parciales: reducir dos puntos en PHQ-9 puede coincidir con retorno a actividades significativas aunque el paciente a&uacute;n se sienta fr&aacute;gil.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "&iquest;PHQ-9 diagnostica depresi&oacute;n mayor?",
                "a": "Orienta probabilidad cl&iacute;nica seg&uacute;n puntos de corte, pero el diagn&oacute;stico requiere entrevista, duraci&oacute;n de s&iacute;ntomas, exclusiones y evaluaci&oacute;n de deterioro funcional. Nunca base un diagn&oacute;stico solo en el puntaje.",
            },
            {
                "q": "&iquest;Cu&aacute;l escala usar en poblaci&oacute;n adulta mayor?",
                "a": "PHQ-9 o CES-D suelen ser manejables por brevedad. Considere ayuda de lectura, presencia de demencia o delirio que invalida autorreporte, y derivaci&oacute;n m&eacute;dica ante confusi&oacute;n aguda.",
            },
            {
                "q": "&iquest;BDI-II o PHQ-9 para seguimiento semanal?",
                "a": "PHQ-9 es m&aacute;s viable por extensi&oacute;n. BDI-II res&eacute;rvelo para evaluaciones integrales peri&oacute;dicas, no para cada sesi&oacute;n breve.",
            },
            {
                "q": "&iquest;Puedo usar puntos de corte publicados en otro pa&iacute;s?",
                "a": "Use manuales y referencias de la versi&oacute;n en espa&ntilde;ol que aplica, con criterio cl&iacute;nico local. Los puntos de corte orientan; no reemplazan juicio profesional ni contexto cultural.",
            },
            {
                "q": "&iquest;Qu&eacute; hacer si el puntaje mejora pero el paciente empeora funcionalmente?",
                "a": "Priorice funcionamiento real, relaciones y seguridad sobre n&uacute;meros. Explore minimizaci&oacute;n en cuestionario, efectos secundarios de medicaci&oacute;n o problemas contextuales no capturados por la escala.",
            },
        ],
        "related": [
            {"href": "/articulos/que-es-el-phq-9.html", "label": "PHQ-9: tamizaje de depresi&oacute;n"},
            {"href": "/articulos/inventario-depresion-beck-bdi.html", "label": "BDI-II: Inventario de Depresi&oacute;n de Beck"},
            {"href": "/articulos/ces-d-escala-depresion.html", "label": "CES-D: escala de depresi&oacute;n"},
            {"href": "/articulos/como-interpretar-tests-psicologicos.html", "label": "C&oacute;mo interpretar tests psicol&oacute;gicos"},
        ],
    }
)

# --- 23 evaluacion-cognitiva-moca-mmse ---
ARTICLES.append(
    {
        "slug": "evaluacion-cognitiva-moca-mmse",
        "title": "Evaluaci&oacute;n cognitiva cl&iacute;nica: MoCA, MMSE y gu&iacute;a | Kalyo",
        "description": "Evaluaci&oacute;n cognitiva con MoCA y MMSE: cu&aacute;ndo aplicarlos, l&iacute;mites, escolaridad, derivaci&oacute;n neurol&oacute;gica y registro cl&iacute;nico para psic&oacute;logos en consulta mexicana.",
        "keywords": "evaluaci&oacute;n cognitiva, MoCA, MMSE, mini mental, deterioro cognitivo, psicolog&iacute;a cl&iacute;nica, tamizaje cognitivo M&eacute;xico",
        "h1": "Evaluaci&oacute;n cognitiva con MoCA y MMSE en consulta psicol&iacute;gica",
        "breadcrumb_short": "Evaluaci&oacute;n cognitiva",
        "hero_alt": "Psic&oacute;logo aplicando evaluaci&oacute;n cognitiva MoCA o MMSE en adulto mayor",
        "inline_alt": "Comparaci&oacute;n entre MoCA y MMSE en tamizaje cognitivo breve",
        "quick_answer": "La <strong>evaluaci&oacute;n cognitiva</strong> breve con MoCA o MMSE tamiza alteraciones de memoria, atenci&oacute;n, lenguaje y funciones ejecutivas; no diagnostica demencia. MoCA suele ser m&aacute;s sensible a deterioro leve; MMSE es cl&aacute;sico y ampliamente conocido. En M&eacute;xico &uacute;selos dentro de entrevista cl&iacute;nica, considerando escolaridad, sensorio y estado de &aacute;nimo, y derive a neurolog&iacute;a o geriatr&iacute;a ante sospecha persistente.",
        "intro_long": "La demanda de <strong>evaluaci&oacute;n cognitiva</strong> crece en consultorios mexicanos: familias preocupadas por olvidos, adultos mayores post-COVID o pacientes con depresi&oacute;n que reportan niebla mental. MoCA y MMSE son tamices breves, no bater&iacute;as neuropsicol&oacute;gicas completas. Este art&iacute;culo explica cu&aacute;ndo elegir cada uno, c&oacute;mo administrarlos con validez pr&aacute;ctica, qu&eacute; factores confunden resultados (ansiedad, dolor, poca escolaridad, hipoacusia) y cu&aacute;ndo escalar a evaluaci&oacute;n especializada. Tambi&eacute;n advierte sobre uso indebido: diagnosticar demencia en una sola visita, ignorar delirium reversible o no registrar condiciones de aplicaci&oacute;n. El objetivo es criterio cl&iacute;nico prudente, sin prometer diagn&oacute;sticos que solo pueden confirmarse con estudio integral.",
        "meta_label": "Psicometr&iacute;a cl&iacute;nica &middot; Actualizaci&oacute;n 2026",
        "cta_h2": "Gestiona el expediente de tus pacientes con Kalyo",
        "cta_p": "Expediente cl&iacute;nico, tests y notas en una sola plataforma &mdash; kalyo.io",
        "sections": [
            {
                "h2": "Qu&eacute; es una evaluaci&oacute;n cognitiva breve y qu&eacute; no cubre",
                "html": p(
                    "La <strong>evaluaci&oacute;n cognitiva</strong> con MoCA o MMSE explora dominios b&aacute;sicos: orientaci&oacute;n temporal y espacial, registro y evocaci&oacute;n de palabras, atenci&oacute;n y c&aacute;lculo sencillo, lenguaje, praxias y funciones ejecutivas (m&aacute;s marcadas en MoCA). Sirven para detectar posible deterioro que requiere estudio ampliado, no para clasificar subtipos de demencia ni pronosticar autonom&iacute;a por s&iacute; solos.",
                    "Un resultado normal no descarta deterioro leve si la queja es rica en detalles funcionales (olvidos que afectan finanzas, medicaci&oacute;n o conducci&oacute;n). Un resultado bajo puede reflejar depresi&oacute;n pseudodemencia, delirium, efectos de benzodiacepinas o baja escolaridad. Siempre integre informantes confiables cuando el paciente lo autorice.",
                ),
            },
            {
                "h2": "MMSE: tamizaje cl&aacute;sico de estado mental",
                "html": p(
                    "El <a href=\"/articulos/mmse-mini-mental-estado-mental.html\">MMSE (Mini-Mental State Examination)</a> permanece como referencia docente y cl&iacute;nica por rapidez y familiaridad. Eval&uacute;a orientaci&oacute;n, memoria inmediata, atenci&oacute;n, recuerdo diferido, lenguaje y praxia constructiva. Es sensible a nivel educativo: interpretar sin considerar a&ntilde;os de escolaridad puede sobreestimar deterioro en personas con poca instrucci&oacute;n formal o subestimarlo en profesionales con alta reserva cognitiva.",
                    "Administre en ambiente silencioso, con buena audici&oacute;n y visi&oacute;n corregida. Registre puntuaci&oacute;n total y errores cualitativos (perseveraciones, desorientaci&oacute;n parcial, fallos de evocaci&oacute;n con pistas). Si MMSE es bajo, repita tras tratar depresi&oacute;n severa o corregir delirium antes de concluir deterioro neurodegenerativo.",
                ),
            },
            {
                "h2": "MoCA: mayor &eacute;nfasis en funciones ejecutivas",
                "html": p(
                    "El <a href=\"/articulos/test-moca-evaluacion-cognitiva.html\">MoCA (Montreal Cognitive Assessment)</a> incluye tareas de trazado alterno, cubo, reloj, fluencia verbal y resta serial que captan alteraciones ejecutivas tempranas con m&aacute;s frecuencia que MMSE en algunos cuadros. Es preferido cuando sospecha deterioro leve, pacientes j&oacute;venes con quejas cognitivas postevento o seguimiento de condiciones neurol&oacute;gicas ya diagnosticadas en coordinaci&oacute;n m&eacute;dica.",
                    "Requiere estandarizar aplicaci&oacute;n seg&uacute;n manual oficial: tiempo, pistas permitidas y puntuaci&oacute;n de dibujos. MoCA no reemplaza resonancia magn&eacute;tica ni evaluaci&oacute;n neuropsicol&oacute;gica completa cuando el cuadro es complejo. Documente versi&oacute;n y ajustes por escolaridad si su protocolo institucional los contempla.",
                )
                + """
<table class="items-table">
<thead><tr><th>Instrumento</th><th>Duraci&oacute;n aprox.</th><th>Fortaleza cl&iacute;nica</th></tr></thead>
<tbody>
<tr><td>MMSE</td><td>10&ndash;15 min</td><td>Rapidez y difusi&oacute;n cl&aacute;sica</td></tr>
<tr><td>MoCA</td><td>10&ndash;15 min</td><td>Funciones ejecutivas y deterioro leve</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "Factores que distorsionan resultados en M&eacute;xico",
                "html": p(
                    "La <strong>evaluaci&oacute;n cognitiva</strong> breve est&aacute; influida por lengua materna, dialecto, escolaridad, fatiga, dolor cr&oacute;nico, ansiedad evaluativa y uso de psicof&aacute;rmacos. En adultos mayores rurales, preguntas de orientaci&oacute;n temporal pueden confundirse con baja familiaridad con calendario gregoriano si no adapta examples contextualmente sin alterar est&iacute;mulos estandarizados.",
                    "Hipoacusia no corregida reduce comprensi&oacute;n de instrucciones; ofrezca volumen adecuado o derivaci&oacute;n auditiva previa. Depresi&oacute;n mayor puede mimetizar deterioro; aplique tamizaje afectivo y repita cognici&oacute;n tras mejor&iacute;a parcial. Evite administrar durante crisis aguda o intoxicaci&oacute;n.",
                ),
            },
            {
                "h2": "Cu&aacute;ndo derivar y qu&eacute; documentar",
                "html": p(
                    "Derive a neurolog&iacute;a, geriatr&iacute;a o neuropsicolog&iacute;a cuando hay declive progresivo documentado, desorientaci&oacute;n frecuente, ca&iacute;das inexplicables, cambios de personalidad, antecedentes familiares fuertes de demencia o discrepancia marcada entre queja funcional y tamizaje normal. Incluya en derivaci&oacute;n puntajes seriados, medicamentos, comorbilidades psiqui&aacute;tricas y observaciones conductuales.",
                    "Redacte informes evitando diagn&oacute;sticos neurol&oacute;gicos definitivos si no corresponde a su competencia; describa hallazgos, limitaciones del tamizaje y recomendaciones. Para marco interpretativo de pruebas, ap&oacute;yese en <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">c&oacute;mo interpretar tests psicol&oacute;gicos</a>. Obtenga consentimiento para compartir resultados con m&eacute;dicos tratantes seg&uacute;n <a href=\"/articulos/consentimiento-informado-psicologia.html\">consentimiento informado en psicolog&iacute;a</a>.",
                )
                + """
<ol>
<li>Registrar escolaridad, audici&oacute;n, visi&oacute;n y estado afectivo del d&iacute;a.</li>
<li>Aplicar MoCA o MMSE con manual estandarizado.</li>
<li>Contrastar con informante si hay autorizaci&oacute;n.</li>
<li>Planificar repetici&oacute;n o derivaci&oacute;n seg&uacute;n curso y riesgo funcional.</li>
</ol>""",
            },
            {
                "h2": "Seguimiento en consulta psicol&iacute;gica",
                "html": p(
                    "En pacientes con depresi&oacute;n mayor, TEPT o TDAH adulto, la queja cognitiva puede mejorar con tratamiento de base; repita tamizaje a los tres o seis meses si cl&iacute;nicamente relevante. No administre MoCA y MMSE el mismo d&iacute;a salvo protocolo de investigaci&oacute;n; elige uno y mantenga continuidad longitudinal.",
                    "Archivar puntuaciones, condiciones de aplicaci&oacute;n y notas cualitativas en expediente facilita comunicaci&oacute;n interdisciplinaria. Psicoeducar a la familia sobre diferencia entre olvidos normales del envejecimiento y se&ntilde;ales de alerta reduce ansiedad innecesaria y retrasa consultas cuando s&iacute; hacen falta.",
                    "Si el paciente presenta depresi&oacute;n com&oacute;rbida, aplique <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a> en paralelo y repita tamizaje cognitivo tras mejor&iacute;a parcial del estado de &aacute;nimo. Muchos «olvidos» mejoran cuando se trata insomnio, ansiedad o episodio depresivo subyacente antes de concluir deterioro neurodegenerativo.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "&iquest;MoCA o MMSE para adulto mayor en consulta privada?",
                "a": "MoCA suele preferirse cuando busca sensibilidad a deterioro leve; MMSE si necesita instrumento muy conocido y comparaci&oacute;n hist&oacute;rica. En ambos casos ajuste interpretaci&oacute;n por escolaridad y contexto cl&iacute;nico.",
            },
            {
                "q": "&iquest;Un puntaje bajo confirma demencia?",
                "a": "No. Confirma necesidad de estudio ampliado. Demencia requiere evaluaci&oacute;n m&eacute;dica, historia longitudinal, pruebas complementarias y, frecuentemente, neuropsicolog&iacute;a completa.",
            },
            {
                "q": "&iquest;Puedo aplicar MoCA por telepsicolog&iacute;a?",
                "a": "Existen adaptaciones validadas en algunos contextos, pero la estandarizaci&oacute;n presencial es la referencia cl&iacute;nica habitual. Si aplica versi&oacute;n remota, documente limitaciones y siga manual autorizado.",
            },
            {
                "q": "&iquest;Cada cu&aacute;nto repetir el tamizaje?",
                "a": "En seguimiento de quejas cognitivas estables, cada seis a doce meses puede bastar. Ante cambio abrupto, repita pronto y descarte delirium o evento m&eacute;dico agudo.",
            },
            {
                "q": "&iquest;El psic&oacute;logo cl&iacute;nico puede informar diagn&oacute;stico de Alzheimer?",
                "a": "Salvo formaci&oacute;n y marco legal espec&iacute;ficos, describa hallazgos cognitivos y recomiende valoraci&oacute;n neurol&oacute;gica. Evite etiquetas etiol&oacute;gicas sin respaldo m&eacute;dico integral.",
            },
        ],
        "related": [
            {"href": "/articulos/test-moca-evaluacion-cognitiva.html", "label": "MoCA: evaluaci&oacute;n cognitiva"},
            {"href": "/articulos/mmse-mini-mental-estado-mental.html", "label": "MMSE: Mini-Mental State Examination"},
            {"href": "/articulos/como-interpretar-tests-psicologicos.html", "label": "C&oacute;mo interpretar tests psicol&oacute;gicos"},
            {"href": "/articulos/consentimiento-informado-psicologia.html", "label": "Consentimiento informado en psicolog&iacute;a"},
        ],
    }
)

# --- 24 tests-proyectivos-rorschach-htp ---
ARTICLES.append(
    {
        "slug": "tests-proyectivos-rorschach-htp",
        "title": "Tests proyectivos: Rorschach, HTP y abordaje cl&iacute;nico | Kalyo",
        "description": "Tests proyectivos como Rorschach y HTP: uso cl&iacute;nico contempor&aacute;neo, l&iacute;mites, &eacute;tica, informes y alternativas para psic&oacute;logos en M&eacute;xico sin sobreinterpretar.",
        "keywords": "tests proyectivos, Rorschach, HTP, dibujo de la figura humana, evaluaci&oacute;n proyectiva, psicolog&iacute;a cl&iacute;nica M&eacute;xico",
        "h1": "Tests proyectivos: Rorschach, HTP y criterio cl&iacute;nico actual",
        "breadcrumb_short": "Tests proyectivos",
        "hero_alt": "Aplicaci&oacute;n de test proyectivo HTP o Rorschach en evaluaci&oacute;n psicol&oacute;gica",
        "inline_alt": "L&aacute;minas de Rorschach y dibujo HTP en contexto cl&iacute;nico",
        "quick_answer": "Los <strong>tests proyectivos</strong> como Rorschach y HTP (House-Tree-Person) exploran experiencia subjetiva mediante est&iacute;mulos ambiguos o dibujo libre. Hoy se usan con moderaci&oacute;n, formaci&oacute;n espec&iacute;fica y integraci&oacute;n con entrevista y pruebas objetivas. No son detector de mentiras ni prueba forense infalible; en M&eacute;xico requieren consentimiento claro, informes prudentes y evitar conclusiones deterministas.",
        "intro_long": "Los <strong>tests proyectivos</strong> divide opiniones: algunos colegas los consideran insustituibles para acceder a fantas&iacute;a y conflicto; otros prefieren bater&iacute;as emp&iacute;ricas. En la pr&aacute;ctica cl&iacute;nica mexicana persisten Rorschach (sistemas contempor&aacute;neos de codificaci&oacute;n), HTP y t&eacute;cnicas gr&aacute;ficas como Wartegg en ciertos contextos. Este art&iacute;culo ofrece criterio prudente: cu&aacute;ndo tienen sentido, c&oacute;mo administrarlos, l&iacute;mites &eacute;ticos en peritajes y c&oacute;mo redactar hallazgos sin caer en especulaci&oacute;n. Tambi&eacute;n se&ntilde;ala demandas poco fundadas: usar proyectivos como prueba de verdad en laboral o familiar sin multim&eacute;todo. No sustituye supervisi&oacute;n en evaluaci&oacute;n proyectiva ni manuales oficiales de cada sistema.",
        "meta_label": "Pr&aacute;ctica cl&iacute;nica &middot; Actualizaci&oacute;n 2026",
        "cta_h2": "Gestiona el expediente de tus pacientes con Kalyo",
        "cta_p": "Expediente cl&iacute;nico, tests y notas en una sola plataforma &mdash; kalyo.io",
        "sections": [
            {
                "h2": "Qu&eacute; son los tests proyectivos en la pr&aacute;ctica actual",
                "html": p(
                    "Los <strong>tests proyectivos</strong> presentan est&iacute;mulos estructurados o semiestructurados (manchas, dibujos, frases incompletas) para analizar respuestas verbales, gr&aacute;ficas y comportamiento durante la tarea. La hip&oacute;tesis cl&iacute;nica cl&aacute;sica sugiere que aspectos de la experiencia interna se manifestar&iacute;an en la elaboraci&oacute;n; la pr&aacute;ctica contempor&aacute;nea enfatiza integraci&oacute;n con datos observables, historia y otras fuentes.",
                    "En M&eacute;xico aparecen en evaluaciones cl&iacute;nicas profundas, contextos organizacionales (con cautela) y algunos informes escolares. Su uso responsable exige formaci&oacute;n en un sistema espec&iacute;fico (p. ej., codificaci&oacute;n Rorschach pericial o cl&iacute;nica), supervisi&oacute;n continua y humildad interpretativa: una respuesta raramente prueba una hip&oacute;tesis por s&iacute; sola.",
                ),
            },
            {
                "h2": "Rorschach: administraci&oacute;n y sistemas de codificaci&oacute;n",
                "html": p(
                    "El Rorschach utiliza diez l&aacute;minas de manchas sim&eacute;tricas. El evaluador registra respuestas verbales, tiempos, localizaci&oacute;n, determinantes formales y contenido, luego codifica seg&uacute;n el sistema que domina (existen enfoques cl&iacute;nicos y de codificaci&oacute;n estructurada). Sin entrenamiento formal, reducir la prueba a «temas» intuitivos es poco &eacute;tico y dif&iacute;cil de defender en informes.",
                    "Indicaciones prudentes: evaluaci&oacute;n de personalidad cuando entrevista y cuestionarios dejan dudas, exploraci&oacute;n de pensamiento en contextos psiqui&aacute;tricos estables, o complemento en psicoterapia psicodin&aacute;mica con paciente que tolera tareas largas. Contraindicaciones relativas: psicosis aguda, fatiga extrema, baja colaboraci&oacute;n, prisa pericial sin rapport. Compare con criterios de <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">interpretaci&oacute;n de tests psicol&oacute;gicos</a> antes de redactar conclusiones amplias.",
                ),
            },
            {
                "h2": "HTP: dibujo de casa, &aacute;rbol y persona",
                "html": p(
                    "El <strong>HTP (House-Tree-Person)</strong> solicita tres dibujos con instrucciones estandarizadas y entrevista post-dibujo sobre elementos, tama&ntilde;o, omisiones y afecto asociado. Es accesible en poblaciones con dificultad lectora o ni&ntilde;ez, pero vulnerable a interpretaci&oacute;n especulativa si se asignan significados universales («casa peque&ntilde;a = autoestima baja») sin corroboraci&oacute;n.",
                    "Registre orden de ejecuci&oacute;n, tiempo, presi&oacute;n del trazo, borrones, comentarios espont&aacute;neos y respuestas del paciente a preguntas abiertas. Integre con datos desarrollales: un ni&ntilde;o expuesto a violencia dom&eacute;stica puede omitir ventanas por miedo real, no por «cerraz&oacute;n emocional» metaf&oacute;rica. En adultos, compare con funcionamiento actual y objetivos terap&eacute;uticos.",
                )
                + """
<ul>
<li><strong>Fortalezas:</strong> acceso a material gr&aacute;fico, &uacute;til con menores.</li>
<li><strong>Riesgos:</strong> sobreinterpretaci&oacute;n simb&oacute;lica sin base conductual.</li>
<li><strong>Complemento:</strong> entrevista cl&iacute;nica y escalas cuando proceda.</li>
</ul>""",
            },
            {
                "h2": "Wartegg y otras t&eacute;cnicas gr&aacute;ficas",
                "html": p(
                    "En entornos hispanohablantes el <a href=\"/articulos/test-wartegg-proyectiva.html\">Test de Wartegg</a> aparece como alternativa gr&aacute;fica breve con ocho campos. Al igual que HTP, requiere evitar lecturas deterministas. Puede ser &uacute;til como punto de partida conversacional en adolescentes reticentes al discurso verbal prolongado.",
                    "No acumule m&uacute;ltiples pruebas gr&aacute;ficas el mismo d&iacute;a sin justificaci&oacute;n; genera fatiga y respuestas estereotipadas. Seleccione una t&eacute;cnica coherente con hip&oacute;tesis cl&iacute;nica y tiempo disponible.",
                ),
            },
            {
                "h2": "&Eacute;tica, consentimiento e informes periciales",
                "html": p(
                    "Los <strong>tests proyectivos</strong> en peritajes laborales, familiares o penales exigen competencia espec&iacute;fica y transparencia sobre limitaciones. Informe al evaluado para qu&eacute; se aplican las pruebas, qui&eacute;n recibir&aacute; resultados y que las conclusiones son opiniones profesionales sujetas a contraste con otras evidencias. Revise <a href=\"/articulos/consentimiento-informado-psicologia.html\">consentimiento informado en psicolog&iacute;a</a> antes de evaluaciones extensas.",
                    "Evite lenguaje definitivo («el sujeto es agresivo», «miente habitualmente») basado solo en contenido proyectivo. Prefiera descripciones de procesos observados, consistencia entre fuentes y recomendaciones prudentes. En menores, adapte devoluci&oacute;n a edad y proteja material gr&aacute;fico en expediente seg&uacute;n confidencialidad.",
                )
                + """
<table class="items-table">
<thead><tr><th>T&eacute;cnica</th><th>Modalidad</th><th>Nota de uso responsable</th></tr></thead>
<tbody>
<tr><td>Rorschach</td><td>Verbal + codificaci&oacute;n</td><td>Requiere entrenamiento sistem&aacute;tico</td></tr>
<tr><td>HTP</td><td>Dibujo + entrevista</td><td>Evitar simbolismo universal</td></tr>
<tr><td>Wartegg</td><td>Gr&aacute;fico breve</td><td>Complemento, no prueba &uacute;nica</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "Integraci&oacute;n con evaluaci&oacute;n multim&eacute;todo",
                "html": p(
                    "La evaluaci&oacute;n cl&iacute;nica s&oacute;lida combina entrevista semiestructurada, observaci&oacute;n, escalas emp&iacute;ricas cuando corresponda y, opcionalmente, proyectivos si aportan datos no obtenidos por otras v&iacute;as. Formule hip&oacute;tesis previas y registre evidencia convergente o discrepante. Si Rorschach sugiere rigidez cognitiva pero entrevista muestra flexibilidad, reporte la discrepancia en lugar de forzar coherencia narrativa.",
                    "Documente tiempo de administraci&oacute;n, estado del paciente y calidad de rapport. Archivar respuestas verbatim (Rorschach) o escaneos de dibujos (HTP) respeta est&aacute;ndares de trazabilidad. En psicoterapia, use material proyectivo para facilitar elaboraci&oacute;n simb&oacute;lica, no para imponer interpretaciones del terapeuta.",
                    "Cuando el contexto requiere documentaci&oacute;n formal del expediente, alinee sus informes con requisitos de <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">historia cl&iacute;nica seg&uacute;n NOM-004</a>: identificaci&oacute;n del evaluador, fecha, procedimiento aplicado y conclusiones prudentes. Si complementa con escalas emp&iacute;ricas, registre tambi&eacute;n su aporte convergente o discrepante con el material proyectivo.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "&iquest;Los tests proyectivos siguen siendo v&aacute;lidos cl&iacute;nicamente?",
                "a": "Dependen del sistema, formaci&oacute;n del evaluador e integraci&oacute;n multim&eacute;todo. Usados con criterio y supervisi&oacute;n pueden aportar datos cl&iacute;nicos; usados de forma intuitiva pierden utilidad y pueden ser poco &eacute;ticos en informes.",
            },
            {
                "q": "&iquest;Puedo usar HTP sin entrevista post-dibujo?",
                "a": "Perder&iacute;a gran parte de la informaci&oacute;n cl&iacute;nica. La entrevista sobre el dibujo y la observaci&oacute;n del proceso son tan importantes como el producto gr&aacute;fico final.",
            },
            {
                "q": "&iquest;Rorschach detecta mentira o simulaci&oacute;n?",
                "a": "No est&aacute; dise&ntilde;ado como detector de simulaci&oacute;n confiable por s&iacute; solo. Cualquier afirmaci&oacute;n pericial sobre enga&ntilde;o exige bater&iacute;a espec&iacute;fica y competencia forense acreditada.",
            },
            {
                "q": "&iquest;Son apropiados en ni&ntilde;os peque&ntilde;os?",
                "a": "HTP y dibujos pueden ser &uacute;tiles con adaptaci&oacute;n evolutiva, pero la interpretaci&oacute;n debe considerar desarrollo, trauma reciente y contexto escolar. Evite conclusiones adultoc&eacute;ntricas.",
            },
            {
                "q": "&iquest;Debo incluir copias de dibujos en informes externos?",
                "a": "Solo con consentimiento expl&iacute;cito y cuando aporten valor cl&iacute;nico acordado. Proteja material sensible y minimice exposici&oacute;n innecesaria en informes laborales o legales.",
            },
        ],
        "related": [
            {"href": "/articulos/test-wartegg-proyectiva.html", "label": "Test de Wartegg: t&eacute;cnica proyectiva"},
            {"href": "/articulos/como-interpretar-tests-psicologicos.html", "label": "C&oacute;mo interpretar tests psicol&oacute;gicos"},
            {"href": "/articulos/consentimiento-informado-psicologia.html", "label": "Consentimiento informado en psicolog&iacute;a"},
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004 e historia cl&iacute;nica en M&eacute;xico"},
        ],
    }
)

# --- 25 historia-clinica-psicologica-paso-a-paso ---
ARTICLES.append(
    {
        "slug": "historia-clinica-psicologica-paso-a-paso",
        "title": "Historia cl&iacute;nica psicol&oacute;gica paso a paso en consulta | Kalyo",
        "description": "Historia cl&iacute;nica psicol&oacute;gica paso a paso: motivo de consulta, NOM-004, consentimiento, notas SOAP, archivo digital y buenas pr&aacute;cticas para psic&oacute;logos en M&eacute;xico.",
        "keywords": "historia cl&iacute;nica psicol&oacute;gica paso a paso, NOM-004, expediente cl&iacute;nico, notas SOAP, psicolog&iacute;a M&eacute;xico, documentaci&oacute;n cl&iacute;nica",
        "h1": "Historia cl&iacute;nica psicol&oacute;gica paso a paso: gu&iacute;a para consulta",
        "breadcrumb_short": "Historia cl&iacute;nica psicol&oacute;gica",
        "hero_alt": "Elaboraci&oacute;n de historia cl&iacute;nica psicol&iacute;gica en expediente digital",
        "inline_alt": "Estructura paso a paso de la historia cl&iacute;nica psicol&oacute;gica",
        "quick_answer": "La <strong>historia cl&iacute;nica psicol&oacute;gica paso a paso</strong> integra identificaci&oacute;n, motivo de consulta, antecedentes, exploraci&oacute;n mental, hip&oacute;tesis, plan y consentimientos. En M&eacute;xico debe alinearse a buenas pr&aacute;cticas de la <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> cuando aplique, con confidencialidad, leyenda de responsable y archivo seguro. No es relleno administrativo: es base legal, cl&iacute;nica y de continuidad asistencial.",
        "intro_long": "Documentar una <strong>historia cl&iacute;nica psicol&oacute;gica paso a paso</strong> protege al paciente, al profesional y a la calidad del tratamiento. Muchos psic&oacute;logos en M&eacute;xico inician consulta privada con plantillas incompletas o notas post sesi&oacute;n demasiado vagas. Esta gu&iacute;a describe secuencia pr&aacute;ctica desde primer contacto hasta plan terap&eacute;utico inicial, incorporando consentimiento informado, exploraci&oacute;n psicopatol&oacute;gica b&aacute;sica, registro de pruebas aplicadas y criterios de actualizaci&oacute;n del expediente. Tambi&eacute;n cubre telepsicolog&iacute;a, menores de edad y solicitudes de informes externos. El tono es cl&iacute;nico y accesible, orientado a consultorio real, no a ideal administrativo inalcanzable.",
        "meta_label": "Pr&aacute;ctica cl&iacute;nica &middot; Actualizaci&oacute;n 2026",
        "cta_h2": "Gestiona el expediente de tus pacientes con Kalyo",
        "cta_p": "Expediente cl&iacute;nico, tests y notas en una sola plataforma &mdash; kalyo.io",
        "sections": [
            {
                "h2": "Primer contacto: identificaci&oacute;n y motivo de consulta",
                "html": p(
                    "Inicie la <strong>historia cl&iacute;nica psicol&iacute;gica</strong> con datos de identificaci&oacute;n necesarios (nombre, edad, contacto de emergencia acordado), persona que refiere y motivo de consulta en palabras del paciente. Registre duraci&oacute;n del problema, factores precipitantes, expectativas de tratamiento y intentos previos de ayuda (terapias, medicaci&oacute;n, apoyo espiritual o comunitario).",
                    "Explore de forma breve contexto sociodemogr&aacute;fico relevante para formulaci&oacute;n: trabajo, estudios, vivienda, migraci&oacute;n reciente, acceso a servicios. Evite interrogatorio mec&aacute;nico; alterne preguntas abiertas con clarificaciones. Si el paciente llega derivado por m&eacute;dico o escuela, anote contacto profesional solo con consentimiento. Cuando el motivo incluye ansiedad o tristeza intensa, planifique desde el inicio tamizaje con <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a> o <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a> en sesiones posteriores, sin convertir la primera entrevista en bater&iacute;a de cuestionarios.",
                ),
            },
            {
                "h2": "Antecedentes personales, familiares y de desarrollo",
                "html": p(
                    "Recoja antecedentes psiqui&aacute;tricos y psicol&oacute;gicos previos, hospitalizaciones, consumo de sustancias, traumas significativos, enfermedades m&eacute;dicas actuales y medicamentos. En menores o adolescentes, historia del desarrollo, rendimiento escolar, bullying y din&aacute;mica familiar. Antecedentes familiares de trastornos del estado de &aacute;nimo, suicidio o adicciones orientan riesgo, sin determinismo.",
                    "Documente fortalezas y recursos: red de apoyo, creencias que sostienen, actividades con sentido. Una historia cl&iacute;nica &uacute;til no es solo lista de patolog&iacute;as; equilibra vulnerabilidades y factores protectores para planificar intervenci&oacute;n realista.",
                )
                + """
<ul>
<li><strong>Personales:</strong> tratamientos previos, diagn&oacute;sticos referidos, adherencia.</li>
<li><strong>M&eacute;dicos:</strong> condiciones cr&oacute;nicas, medicaci&oacute;n psicotr&oacute;pica actual.</li>
<li><strong>Familiares:</strong> historia psiqui&aacute;trica relevante y apoyo disponible.</li>
</ul>""",
            },
            {
                "h2": "Exploraci&oacute;n del estado mental y riesgo",
                "html": p(
                    "Registre apariencia, conducta, actitud, lenguaje, proceso y contenido del pensamiento, percepci&oacute;n, afecto, ansiedad, cognici&oacute;n, insight y juicio. Use observaciones concretas («contacto visual intermitente, voz baja, llanto al narrar conflicto conyugal») en lugar de adjetivos vagos («deprimido» sin describir).",
                    "Eval&uacute;e riesgo suicida y homicida cuando proceda: ideaci&oacute;n, plan, medios, intentos previos, factores protectores. Un tamizaje con escalas como PHQ-9 o GAD-7 no sustituye esta exploraci&oacute;n. Si aplica pruebas, registre cu&aacute;les, resultados orientativos y enlace a gu&iacute;a de <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">interpretaci&oacute;n de tests psicol&oacute;gicos</a>.",
                ),
            },
            {
                "h2": "Consentimiento informado y marco NOM-004",
                "html": p(
                    "Antes o durante la primera sesi&oacute;n formal, obtenga <a href=\"/articulos/consentimiento-informado-psicologia.html\">consentimiento informado</a>: naturaleza del servicio, confidencialidad y sus l&iacute;mites legales (riesgo vital, abuso a menores seg&uacute;n legislaci&oacute;n), honorarios, cancelaciones, modalidad presencial o remota y uso de expediente digital. En instituciones reguladas, alinee formato con <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004 sobre historias cl&iacute;nicas</a>: identificaci&oacute;n del profesional responsable, fecha, firma o equivalente digital.",
                    "Explique al paciente que puede solicitar copia de su historia seg&uacute;n marco aplicable y que las notas son herramienta cl&iacute;nica protegida. Menores requieren consentimiento de titulares legales y asentimiento del menor acorde a edad.",
                ),
            },
            {
                "h2": "Formulaci&oacute;n, hip&oacute;tesis y plan terap&eacute;utico inicial",
                "html": p(
                    "Cierre la evaluaci&oacute;n inicial con formulaci&oacute;n integradora: problemas prioritarios, factores precipitantes y mantenedores, hip&oacute;tesis diagn&oacute;sticas provisionales (si corresponde), objetivos terap&eacute;uticos SMART y plan de intervenci&oacute;n (frecuencia, enfoque, tareas, derivaciones m&eacute;dicas o psiqui&aacute;tricas). Evite diagn&oacute;sticos apresurados en una sola sesi&oacute;n salvo urgencia.",
                    "Acuerde criterios de reevaluaci&oacute;n: cu&aacute;ndo repetir escalas, cu&aacute;ndo convocar sesi&oacute;n familiar o revisar medicaci&oacute;n con psiquiatr&iacute;a. El plan debe ser comprensible para el paciente; comparta versi&oacute;n resumida sin jerga innecesaria.",
                )
                + """
<ol>
<li>Priorizar uno o dos problemas focales iniciales.</li>
<li>Definir objetivos observables a cuatro u ocho semanas.</li>
<li>Registrar derivaciones y compromisos mutuos.</li>
<li>Programar fecha de revisi&oacute;n de formulaci&oacute;n.</li>
</ol>""",
            },
            {
                "h2": "Notas de evoluci&oacute;n, SOAP y archivo seguro",
                "html": p(
                    "Tras la historia inicial, cada sesi&oacute;n merece nota de evoluci&oacute;n breve. El formato SOAP (Subjetivo, Objetivo, An&aacute;lisis, Plan) ayuda a mantener enfoque: reporte del paciente, observaciones cl&iacute;nicas, formulaci&oacute;n actualizada y tareas hasta siguiente cita. Evite transcribir verbatim conversaciones &iacute;ntimas innecesarias; registre datos cl&iacute;nicos pertinentes.",
                    "Use expediente digital con respaldo, control de acceso y contrase&ntilde;as robustas. En telepsicolog&iacute;a, documente plataforma utilizada y medidas de privacidad acordadas. Actualice historia cuando cambien medicamentos, diagn&oacute;sticos m&eacute;dicos relevantes o situaciones legales (custodia, violencia). La historia cl&iacute;nica viva refleja el curso del tratamiento, no un formulario congelado del d&iacute;a uno.",
                    "Revise peri&oacute;dicamente si su plantilla cumple elementos esenciales descritos en <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> y si el paciente firm&oacute; <a href=\"/articulos/consentimiento-informado-psicologia.html\">consentimiento informado</a> antes de compartir datos con terceros. Un expediente ordenado facilita continuidad si usted ausenta vacaciones o si el paciente retoma tratamiento a&ntilde;os despu&eacute;s.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "&iquest;Cu&aacute;nto debe durar la historia cl&iacute;nica inicial?",
                "a": "Suele requerir una a tres sesiones seg&uacute;n complejidad. Priorice completitud cl&iacute;nica sobre velocidad; puede ampliar antecedentes en sesiones siguientes sin omitir exploraci&oacute;n de riesgo desde el inicio.",
            },
            {
                "q": "&iquest;La NOM-004 aplica a consultorio privado?",
                "a": "Muchos profesionales adoptan sus criterios como est&aacute;ndar de calidad y respaldo ante auditor&iacute;as o demandas. Verifique obligaciones espec&iacute;ficas seg&uacute;n su entidad y tipo de servicio.",
            },
            {
                "q": "&iquest;Debo incluir todos los resultados de tests en la historia?",
                "a": "Registre instrumentos aplicados, puntajes orientativos, fecha y versi&oacute;n. Informes extensos pueden anexarse; la historia debe permitir entender decisiones cl&iacute;nicas tomadas.",
            },
            {
                "q": "&iquest;Puedo usar plantillas gen&eacute;ricas descargadas en internet?",
                "a": "S&iacute;, si las adapta a su marco &eacute;tico, legislaci&oacute;n local y tipo de paciente. Revise que incluyan consentimiento, identificaci&oacute;n del profesional y espacio para evoluci&oacute;n.",
            },
            {
                "q": "&iquest;Qu&eacute; hacer si el paciente pide borrar su historia?",
                "a": "Explique marco legal y &eacute;tico aplicable en M&eacute;xico; algunos datos deben conservarse por plazos regulados. Ofrezca copia y canalice solicitud seg&uacute;n normativa y c&oacute;digo de &eacute;tica profesional.",
            },
        ],
        "related": [
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004 e historia cl&iacute;nica"},
            {"href": "/articulos/consentimiento-informado-psicologia.html", "label": "Consentimiento informado"},
            {"href": "/articulos/como-interpretar-tests-psicologicos.html", "label": "C&oacute;mo interpretar tests psicol&iacute;gicos"},
            {"href": "/articulos/que-es-el-phq-9.html", "label": "PHQ-9 en evaluaci&oacute;n inicial"},
        ],
    }
)


SECTION_PADS: dict[str, list[str]] = {
    "escalas-ansiedad-psicologia-clinica": [
        "<p>En adolescentes, valide con el paciente si prefiere completar el cuestionario solo o con apoyo; la presi&oacute;n parental puede distorsionar respuestas. En adultos mayores, descarte confusi&oacute;n o delirium antes de atribuir ansiedad primaria.</p>",
        "<p>Si administra GAD-7 en waiting room digital, confirme al inicio de sesi&oacute;n que la persona comprendi&oacute; la escala temporal (&uacute;ltimas dos semanas) y que no hubo eventos at&iacute;picos ese d&iacute;a (noticia grave, discusi&oacute;n previa a la cita).</p>",
        "<p>Al devolver resultados, use gr&aacute;ficas simples o comparaci&oacute;n con sesi&oacute;n anterior; muchos pacientes motivan cambio cuando ven tendencia, no solo n&uacute;mero aislado.</p>",
        "<p>En equipos interdisciplinarios, acuerde qui&eacute;n aplica cada escala para no duplicar carga al paciente entre psicolog&iacute;a, medicina y trabajo social.</p>",
        "<p>Registre si el paciente estaba bajo efectos de alcohol o benzodiacepinas el d&iacute;a de aplicaci&oacute;n; puede reducir o aumentar reporte de activaci&oacute;n.</p>",
        "<p>Ante litigios o quejas institucionales, conserve hoja de respuestas o registro digital con fecha y firma del profesional responsable.</p>",
    ],
    "escalas-depresion-validadas-espanol": [
        "<p>Explore luto reciente antes de interpretar PHQ-9 elevado; el DSM-5 contempla exclusores temporales que la escala no distingue autom&aacute;ticamente.</p>",
        "<p>En embarazo y posparto, adapte lenguaje de devoluci&oacute;n y coordine con ginecolog&iacute;a; algunos &iacute;tems som&aacute;ticos se solapan con cambios fisiol&oacute;gicos normales.</p>",
        "<p>BDI-II puede cansar a pacientes con concentraci&oacute;n reducida; ofrezca pausa breve entre bloques sin invalidar la prueba.</p>",
        "<p>CES-D en contextos comunitarios requiere explicar &iacute;tems positivos invertidos; errores de puntuaci&oacute;n son frecuentes sin revisi&oacute;n en sesi&oacute;n.</p>",
        "<p>Si hay ideaci&oacute;n activa, la escala queda en segundo plano: active protocolo de riesgo antes de continuar evaluaci&oacute;n estandarizada.</p>",
        "<p>En informes laborales, evite divulgar puntajes sin necesidad; describa funcionamiento y recomendaciones con consentimiento expl&iacute;cito.</p>",
        "<p>Cuando el paciente mejora funcionalmente pero el puntaje cae poco, explore si &iacute;tems som&aacute;ticos persisten por condici&oacute;n m&eacute;dica no tratada.</p>",
    ],
    "evaluacion-cognitiva-moca-mmse": [
        "<p>Antes de aplicar, confirme que el paciente durmi&oacute; adecuadamente; privaci&oacute;n de sue&ntilde;o reduce evocaci&oacute;n y atenci&oacute;n en ambos tamices.</p>",
        "<p>En MMSE, registre si requiri&oacute; repetir instrucciones; es dato cualitativo &uacute;til aunque no altere puntaje estandarizado.</p>",
        "<p>MoCA en manos no entrenadas genera variabilidad; busque capacitaci&oacute;n formal o supervisi&oacute;n antes de usar en informes externos.</p>",
        "<p>Contraste con informante: olvidos negados por el paciente pero reportados por pareja merecen estudio ampliado aunque MMSE sea normal.</p>",
        "<p>No aplique tamizaje cognitivo durante crisis psic&iacute;atrica aguda; posponga para fase estable.</p>",
        "<p>Guarde copia de hoja de registro oficial; facilita reevaluaci&oacute;n por otro profesional sin repetir sesi&oacute;n completa.</p>",
        "<p>En pacientes biling&uuml;es, aplique en el idioma de mayor fluidez para evitar confusi&oacute;n por traducci&oacute;n mental durante la prueba.</p>",
    ],
    "tests-proyectivos-rorschach-htp": [
        "<p>Establezca rapport antes de proyectivos extensos; sin confianza, respuestas pueden ser breves o evasivas sin valor cl&iacute;nico.</p>",
        "<p>En Rorschach, evite comentar validez de respuestas durante la prueba; anote y analice despu&eacute;s seg&uacute;n sistema elegido.</p>",
        "<p>HTP con ni&ntilde;os requiere papel y crayones adecuados a edad; materiales pobres distraen del contenido cl&iacute;nico.</p>",
        "<p>Wartegg no reemplaza entrevista de personalidad; &uacute;selo como puerta de entrada conversacional.</p>",
        "<p>En peritajes, declare expl&iacute;citamente formaci&oacute;n en el m&eacute;todo proyectivo utilizado y sus l&iacute;mites conocidos.</p>",
        "<p>Almacene dibujos en sobre cerrado dentro de expediente si el paciente lo solicita; respete material simb&oacute;lico sensible.</p>",
        "<p>Si el evaluado pregunta qu&eacute; significa su dibujo, devuelva con preguntas abiertas antes de ofrecer hip&oacute;tesis cl&iacute;nicas tentativas.</p>",
    ],
    "historia-clinica-psicologica-paso-a-paso": [
        "<p>Verifique identidad del paciente al abrir expediente, especialmente en teleconsulta, para evitar mezclar historias cl&iacute;nicas.</p>",
        "<p>En antecedentes, pregunte por violencia de pareja con protocolo seguro; registre solo lo necesario para plan de protecci&oacute;n.</p>",
        "<p>La exploraci&oacute;n mental puede hacerse de forma conversacional; no todo debe sonar a interrogatorio psiqui&aacute;trico r&iacute;gido.</p>",
        "<p>Archivo de consentimientos firmados (digital o f&iacute;sico) debe ser recuperable en minutos ante auditor&iacute;a &eacute;tica.</p>",
        "<p>El plan terap&eacute;utico inicial puede revisarse a las cuatro semanas; documente cambios sin borrar versiones previas.</p>",
        "<p>Notas SOAP excesivamente largas dificultan lectura futura; priorice datos que influyeron decisiones cl&iacute;nicas ese d&iacute;a.</p>",
        "<p>Programe revisi&oacute;n anual de plantillas para incorporar cambios normativos o de modalidad de atenci&oacute;n en su consultorio.</p>",
    ],
}

FAQ_PADS: dict[str, list[str]] = {
    "escalas-ansiedad-psicologia-clinica": [
        " In menores, considere entrevista con cuidadores seg&uacute;n edad y consentimiento.",
        " Compare con observaci&oacute;n cl&iacute;nica de inquietud motora o evitaci&oacute;n.",
        " Ajuste intervalo si hay cambio de medicaci&oacute;n ansiol&iacute;tica reciente.",
        " Documente versi&oacute;n en espa&ntilde;ol utilizada si existen variantes regionales.",
        " Si hay trauma no explorado, posponga interpretaci&oacute;n final del puntaje.",
    ],
    "escalas-depresion-validadas-espanol": [
        " Descarte man&iacute;a o hipoman&iacute;a antes de iniciar antidepresivo solo por puntaje.",
        " En dolor cr&oacute;nico, valore &iacute;tems som&aacute;ticos con cautela cl&iacute;nica.",
        " Repita tras intervenci&oacute;n m&iacute;nima de cuatro semanas para tendencia.",
        " En informes, explique que escalas no miden funcionamiento global.",
        " Ante empeoramiento s&uacute;bito, reeval&uacute;e riesgo aunque puntaje previo fuera bajo.",
    ],
    "evaluacion-cognitiva-moca-mmse": [
        " Considere escolaridad al explicar resultados a la familia.",
        " Repita tras corregir deficiencia auditiva si sospecha subestimaci&oacute;n.",
        " No use tamizaje como &uacute;nica base de incapacidad laboral.",
        " En TEPT, cognici&oacute;n puede mejorar al estabilizar sue&ntilde;o.",
        " Derive si hay ca&iacute;das recientes no explicadas por otro factor. Documente idioma y duraci&oacute;n total de la sesi&oacute;n de evaluaci&oacute;n.",
    ],
    "tests-proyectivos-rorschach-htp": [
        " Busque supervisi&oacute;n peri&oacute;dica si usa proyectivos con frecuencia.",
        " Evite interpretaciones culturales estereotipadas en poblaci&oacute;n ind&iacute;gena.",
        " En laboral, combine con entrevista y pruebas objetivas si procede.",
        " Respete si el paciente rechaza dibujar por verg&uuml;enza; no fuerce.",
        " Informe al paciente c&oacute;mo se resguardar&aacute;n dibujos o respuestas. Separe claramente hip&oacute;tesis cl&iacute;nicas de especulaci&oacute;n simb&oacute;lica.",
    ],
    "historia-clinica-psicologica-paso-a-paso": [
        " Puede completar antecedentes en segunda sesi&oacute;n si la primera fue de crisis.",
        " Revise c&oacute;digo de &eacute;tica estatal sobre plazos de conservaci&oacute;n.",
        " En menores, registre qui&eacute;n autoriz&oacute; tratamiento y contacto de emergencia.",
        " Las notas deben permitir continuidad si otro colega cubre la sesi&oacute;n.",
        " Ofrezca copia de plan terap&eacute;utico en lenguaje comprensible al paciente. Incluya fecha y modalidad en cada nota de evoluci&oacute;n subsiguiente.",
    ],
}

for _article in ARTICLES:
    _slug = _article["slug"]
    _pads = SECTION_PADS.get(_slug, [])
    for _sec, _pad in zip(_article["sections"], _pads):
        _sec["html"] += _pad
    if len(_pads) > len(_article["sections"]):
        _article["sections"][-1]["html"] += "".join(_pads[len(_article["sections"]) :])
    _faq_pads = FAQ_PADS.get(_slug, [])
    for _i, _faq in enumerate(_article.get("faqs", [])):
        if _i < len(_faq_pads):
            _faq["a"] = _faq["a"] + _faq_pads[_i]

CLOSING_BLOCKS: dict[str, str] = {
    "escalas-depresion-validadas-espanol": "<p>En consulta comunitaria o institucional, acuerde con el equipo un protocolo m&iacute;nimo: PHQ-9 en admisi&oacute;n, exploraci&oacute;n de riesgo en cada contacto y BDI-II o CES-D solo cuando el caso lo requiera. Evite que el paciente perciba burocracia sin devoluci&oacute;n cl&iacute;nica. Capacite a recepci&oacute;n para no prometer diagn&oacute;sticos a partir de cuestionarios completados en sala de espera. La calidad del expediente mejora cuando cada puntaje va acompa&ntilde;ado de una nota breve sobre contexto y decisi&oacute;n tomada ese d&iacute;a.</p>",
    "evaluacion-cognitiva-moca-mmse": "<p>La <strong>evaluaci&oacute;n cognitiva</strong> breve cobra sentido cuando forma parte de un plan: queja espec&iacute;fica, l&iacute;nea base, intervenci&oacute;n y reevaluaci&oacute;n. Sin plan, el paciente sale con etiqueta de olvido y miedo a demencia sin orientaci&oacute;n clara. Dedique tiempo a devoluci&oacute;n: explique qu&eacute; mide el tamizaje, qu&eacute; no mide y cu&aacute;les ser&aacute;n los siguientes pasos si persisten preocupaciones. En familias con alto conflicto por cuidados, el tamizaje puede ser detonante; modere expectativas y ofrezca recursos de apoyo al cuidador cuando proceda. Si coordina con m&eacute;dico familiar, env&iacute;e resumen objetivo con puntajes seriados y observaciones conductuales, no solo un n&uacute;mero aislado del &uacute;ltimo MoCA o MMSE aplicado. Recuerde que la queja cognitiva en depresi&oacute;n tratada a menudo mejora antes que el paciente internalice recuperaci&oacute;n global. Programe la pr&oacute;xima reevaluaci&oacute;n antes de cerrar la sesi&oacute;n para reducir ansiedad anticipatoria en la familia. Anote en expediente si hubo interrupciones durante la prueba o uso de lentes no habituales.</p>",
    "tests-proyectivos-rorschach-htp": "<p>La reputaci&oacute;n de los <strong>tests proyectivos</strong> depende de c&oacute;mo los usamos: con formaci&oacute;n, supervisi&oacute;n e integraci&oacute;n multim&eacute;todo pueden enriquecer la comprensi&oacute;n cl&iacute;nica; usados como atajo interpretativo generan informes fr&aacute;giles. En M&eacute;xico, donde peritajes psicol&oacute;gicos enfrentan escrutinio judicial, la prudencia redactando conclusiones protege al paciente y al profesional. Mantenga archivo de respuestas, tiempos y condiciones de aplicaci&oacute;n. Si el paciente rechaza t&eacute;cnicas gr&aacute;ficas por verg&uuml;enza cultural o religiosa, registre la negativa y ofrezca alternativas v&aacute;lidas sin presi&oacute;n. La psicoterapia puede usar dibujos o asociaciones libres sin convertir cada sesi&oacute;n en evaluaci&oacute;n formal; distinga objetivos terap&eacute;uticos de objetivos periciales en su documentaci&oacute;n. Ante dudas interpretativas, consulte supervisi&oacute;n antes de cerrar informe definitivo. La formaci&oacute;n continua en un solo sistema proyectivo vale m&aacute;s que aplicar muchos instrumentos sin profundidad. Reserve tiempo suficiente; la prisa invalida la calidad del material obtenido y aumenta respuestas perfunctorias. Explique al evaluado que no hay respuestas correctas o incorrectas en sentido absoluto durante la aplicaci&oacute;n cl&iacute;nica estandarizada formal.</p>",
    "historia-clinica-psicologica-paso-a-paso": "<p>Una <strong>historia cl&iacute;nica psicol&oacute;gica paso a paso</strong> bien construida ahorra tiempo a largo plazo: menos repetici&oacute;n de preguntas, menos errores de medicaci&oacute;n documentada y mejor coordinaci&oacute;n si el paciente cambia de terapeuta. Revise cada seis meses si su plantilla sigue cumpliendo lo que usted necesita en su modelo de pr&aacute;ctica (presencial, h&iacute;brido, pericial). Invierta en respaldo digital cifrado y contrase&ntilde;as &uacute;nicas; la historia cl&iacute;nica es activo cl&iacute;nico y legal. Capacite a practicantes o asistentes sobre confidencialidad antes de delegar captura administrativa de datos identificables. Cuando el paciente retorna tras pausa prolongada, actualice motivo de consulta y antecedentes antes de asumir continuidad del plan previo. Una l&iacute;nea de tiempo clara de eventos vitales facilita formulaci&oacute;n en casos complejos con m&uacute;ltiples derivaciones. Dedique los &uacute;ltimos minutos de la evaluaci&oacute;n inicial a verificar que el paciente entendi&oacute; el plan y sus dudas quedaron registradas. Firme o autentique cada nota seg&uacute;n su modalidad de expediente.</p>",
}

for _article in ARTICLES:
    _closing = CLOSING_BLOCKS.get(_article["slug"])
    if _closing and _article["sections"]:
        _article["sections"][-1]["html"] += _closing


if __name__ == "__main__":
    for spec in ARTICLES:
        slug = spec["slug"]
        tl = len(spec["title"].replace("&iacute;", "í").replace("&oacute;", "ó")
                    .replace("&aacute;", "á").replace("&eacute;", "é")
                    .replace("&uacute;", "ú").replace("&ntilde;", "ñ")
                    .replace("&uuml;", "ü"))
        dl = len(spec["description"].replace("&iacute;", "í").replace("&oacute;", "ó")
                    .replace("&aacute;", "á").replace("&eacute;", "é")
                    .replace("&uacute;", "ú").replace("&ntilde;", "ñ"))
        qw = wc(spec["quick_answer"])
        iw = wc(spec["intro_long"])
        bw = body_words(spec)
        links = sum(
            1 for s in spec["sections"]
            if "/articulos/" in s["html"]
        )
        print(f"{slug}: title~{tl} desc~{dl} quick={qw} intro={iw} body={bw} sections_w_links={links}")
