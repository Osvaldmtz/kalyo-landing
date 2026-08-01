#!/usr/bin/env python3
"""Batch 9 part 2: clinical SEO article specs (articles 26-30)."""
from __future__ import annotations

import re

KALYO = '<a href="https://app.kalyo.io/register">Kalyo</a>'


def wc(text: str) -> int:
    t = re.sub(r"<[^>]+>", " ", text)
    return len(re.sub(r"\s+", " ", t).strip().split())


def body_words(spec: dict) -> int:
    parts = [spec["quick_answer"], spec["intro_long"]]
    for s in spec["sections"]:
        parts.append(s["html"])
    for f in spec["faqs"]:
        parts.append(f["q"] + " " + f["a"])
    return sum(wc(p) for p in parts)


def p(*paras: str) -> str:
    return "".join(f"<p>{x}</p>" for x in paras)


CTA_H2 = "Gestiona el expediente de tus pacientes con Kalyo"
CTA_P = "Expediente cl&iacute;nico, tests y notas en una sola plataforma &mdash; kalyo.io"

ARTICLES: list[dict] = []

# --- 26 test-inteligencia-ninos-guia ---
ARTICLES.append(
    {
        "slug": "test-inteligencia-ninos-guia",
        "title": "Test de inteligencia ni\u00f1os: gu\u00eda cl\u00ednica y WISC-V | Kalyo",
        "description": "Test de inteligencia ni\u00f1os: cu\u00e1ndo solicitarlo, WISC-V y WPPSI, interpretaci\u00f3n cl\u00ednica, informes escolares, neuropsicolog\u00eda infantil y coordinaci\u00f3n en M\u00e9xico.",
        "keywords": "test de inteligencia ni\u00f1os, WISC-V, WPPSI, evaluaci\u00f3n cognitiva infantil, CI, neuropsicolog\u00eda, psicolog\u00eda cl\u00ednica, M\u00e9xico",
        "h1": "Test de inteligencia en ni\u00f1os: gu\u00eda cl\u00ednica para psic\u00f3logos",
        "breadcrumb_short": "Test inteligencia ni\u00f1os",
        "hero_alt": "Evaluaci\u00f3n cognitiva infantil con test de inteligencia en consultorio psicol\u00f3gico",
        "inline_alt": "Perfil de \u00edndices WISC-V y \u00e1reas cognitivas en evaluaci\u00f3n infantil",
        "quick_answer": "Un <strong>test de inteligencia en ni\u00f1os</strong> mide funciones cognitivas con bater&iacute;as estandarizadas como el <a href=\"/articulos/wisc-v-test-inteligencia-ninos.html\">WISC-V</a> (6 a 16 a\u00f1os) o WPPSI-IV (2 a 7 a\u00f1os). No define valor humano: orienta apoyos escolares, diagn&oacute;stico diferencial y planificaci&oacute;n cl&iacute;nica con informe contextualizado.",
        "intro_long": "Las familias y escuelas en M&eacute;xico solicitan con frecuencia un <strong>test de inteligencia para ni&ntilde;os</strong> ante rezago acad&eacute;mico, sospecha de altas capacidades o evaluaci&oacute;n integral previa a derivaci&oacute;n especializada. El psic&oacute;logo debe distinguir medici&oacute;n cognitiva de juicios morales sobre el desempe&ntilde;o, elegir instrumento acorde a edad y nivel ling&uuml;&iacute;stico, integrar datos conductuales y escolares, y redactar informes &uacute;tiles para maestros y padres sin reducir al ni&ntilde;o a un n&uacute;mero. Esta gu&iacute;a resume indicaciones, administraci&oacute;n responsable e interpretaci&oacute;n cl&iacute;nica basada en manuales t&eacute;cnicos y buenas pr&aacute;cticas de evaluaci&oacute;n infantil.",
        "meta_label": "Neuropsicolog&iacute;a infantil &middot; Evaluaci&oacute;n cognitiva &middot; 2026",
        "cta_h2": CTA_H2,
        "cta_p": CTA_P,
        "sections": [
            {
                "h2": "Cu\u00e1ndo solicitar un test de inteligencia en ni\u00f1os",
                "html": p(
                    "Un <strong>test de inteligencia en ni&ntilde;os</strong> est&aacute; indicado cuando hay discrepancia persistente entre capacidad aparente y rendimiento escolar, sospecha de discapacidad intelectual, necesidad de documentar perfil cognitivo para apoyos educativos (CONAFE, USAER, adecuaciones curriculares), evaluaci&oacute;n de altas capacidades con evidencia conductual, o como parte de bater&iacute;a en sospecha de TDAH, TEA o trastorno espec&iacute;fico del aprendizaje. No es tamizaje universal ni prueba de entrada escolar sin marco &eacute;tico claro.",
                    "Explore motivo de consulta con padres y docentes: &iquest;buscan etiqueta, beca, cambio de grupo o comprensi&oacute;n de dificultades? Documente consentimiento informado, ventana reciente de sue&ntilde;o, medicaci&oacute;n (estimulantes, anticonvulsivos) y contexto sociocultural (biling&uuml;ismo, migraci&oacute;n reciente, trauma). Postergue evaluaci&oacute;n est&aacute;ndar si hay crisis familiar aguda, privaci&oacute;n extrema de sue&ntilde;o o enfermedad febril; reprograme para evitar sesgo por estado f&iacute;sico.",
                    "En M&eacute;xico, la SEP reconoce evaluaciones externas como insumo para adecuaciones cuando est&aacute;n bien fundadas; el psic&oacute;logo debe redactar recomendaciones funcionales, no prescripciones pedag&oacute;gicas fuera de su competencia. Derive a neuropsicolog&iacute;a si hay sospecha de lesi&oacute;n cerebral, epilepsia no controlada o perfil complejo con m&uacute;ltiples comorbilidades.",
                    "Registre en expediente qui&eacute;n solicit&oacute; la evaluaci&oacute;n, qu&eacute; decisiones dependen del informe (cambio de escuela, beca, terapia) y qu&eacute; expectativas tiene el menor sobre la prueba. Ajustar el marco previo reduce ansiedad de rendimiento y mejora validez de la sesi&oacute;n.",
                ),
            },
            {
                "h2": "Instrumentos: WISC-V, WPPSI-IV y selecci\u00f3n por edad",
                "html": p(
                    "El <a href=\"/articulos/wisc-v-test-inteligencia-ninos.html\">WISC-V</a> es la escala Wechsler m&aacute;s usada entre 6 a&ntilde;os y 16 a&ntilde;os 11 meses; incluye &iacute;ndices verbales, visoespaciales, fluido razonamiento, memoria de trabajo y velocidad de procesamiento, adem&aacute;s de CI total. Para menores de 6 a&ntilde;os, la WPPSI-IV cubre 2 a 7 a&ntilde;os 7 meses con subpruebas adaptadas al desarrollo. Elegir prueba seg&uacute;n edad cronol&oacute;gica, no solo escolar; un ni&ntilde;o con retraso madurativo puede requerir interpretaci&oacute;n cautelosa de &iacute;ndices.",
                    "Otras bater&iacute;as (Stanford-Binet, Kaufman KABC-II) existen en consultorios especializados; la elecci&oacute;n depende de formaci&oacute;n del evaluador, normas disponibles para la poblaci&oacute;n y objetivo cl&iacute;nico. No mezcle puntuaciones de escalas distintas en un mismo informe sin explicar incompatibilidad m&eacute;trica. Verifique vigencia de normas mexicanas o latinoamericanas cuando el manual lo permita; de lo contrario, declare limitaciones en generalizaci&oacute;n.",
                    "La administraci&oacute;n exige ambiente estandarizado: iluminaci&oacute;n adecuada, m&iacute;nimas interrupciones, material completo y cronometraje preciso. Sesiones largas se fraccionan seg&uacute;n manual y tolerancia del ni&ntilde;o; registre fatiga o frustraci&oacute;n que obligue a suspender subpruebas y reagendar.",
                )
                + """
<table class="items-table">
<thead><tr><th>Instrumento</th><th>Rango de edad</th><th>Uso cl\u00ednico</th></tr></thead>
<tbody>
<tr><td>WPPSI-IV</td><td>2:6 a 7:7 a\u00f1os</td><td>Primera evaluaci\u00f3n cognitiva temprana</td></tr>
<tr><td>WISC-V</td><td>6:0 a 16:11 a\u00f1os</td><td>Perfil \u00edndices escolar y cl\u00ednico</td></tr>
<tr><td>WAIS-IV</td><td>16+ a\u00f1os</td><td>Adolescentes mayores seg\u00fan manual</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "Administraci\u00f3n estandarizada y consideraciones culturales",
                "html": p(
                    "Siga el manual de aplicaci&oacute;n: orden de subpruebas, l&iacute;mites de tiempo, criterios de discontinuaci&oacute;n y puntuaciones de proceso cuando est&eacute;n disponibles. Anote comportamientos observados (evitaci&oacute;n visual, impulsividad motora, solicitud excesiva de aprobaci&oacute;n) porque enriquecen interpretaci&oacute;n m&aacute;s all&aacute; del CI. En ni&ntilde;os biling&uuml;es, eval&uacute;e dominio del idioma de aplicaci&oacute;n; si el espa&ntilde;ol es segundo idioma reciente, un CI verbal puede subestimar capacidad y requerir pruebas no verbales o evaluaci&oacute;n adicional.",
                    "Evite sesgos: no entrenar subpruebas antes de la evaluaci&oacute;n oficial, no dar pistas extra, no reinterpretar respuestas para inflar puntuaciones. Si el ni&ntilde;o tiene discapacidad motora o visual, consulte manual sobre pruebas alternativas permitidas. Documente adaptaciones no est&aacute;ndar porque invalidan comparaci&oacute;n normativa.",
                    "La relaci&oacute;n evaluador-ni&ntilde;o influye en motivaci&oacute;n: rapport breve sin sobre-familiaridad. Explique al menor que realizar&aacute; juegos y acertijos; no use t&eacute;rmino &laquo;examen&raquo; si aumenta ansiedad. Padres observan desde sala de espera salvo indicaci&oacute;n cl&iacute;nica contraria.",
                ),
            },
            {
                "h2": "Interpretaci\u00f3n cl\u00ednica del perfil cognitivo",
                "html": p(
                    "El CI total resume rendimiento global pero la cl&iacute;nica valora <strong>dispersi&oacute;n entre &iacute;ndices</strong>: diferencias &ge;15 puntos entre verbal y visoespacial sugieren perfil heterog&eacute;neo (p. ej., fortaleza no verbal con dificultad ling&uuml;&iacute;stica). Memoria de trabajo baja con razonamiento fluido preservado orienta a estrategias de apoyo en tareas multi-paso. Velocidad de procesamiento reducida puede reflejar TDAH, ansiedad o fatiga, no necesariamente capacidad intelectual limitada.",
                    "Compare con historial escolar, pruebas de lectura-escritura y observaci&oacute;n cl&iacute;nica. Un CI promedio no excluye trastorno espec&iacute;fico del aprendizaje; un CI bajo requiere explorar habilidades adaptativas y causas org&aacute;nicas antes de concluir discapacidad intelectual. Reporte intervalos de confianza e incertidumbre de medici&oacute;n; evite lenguaje determinista (&laquo;nunca podr&aacute;&raquo;).",
                    "En altas capacidades, un CI &ge;130 debe complementarse con creatividad, motivaci&oacute;n y funcionamiento social; algunos ni&ntilde;os con CI alto tienen TEA o TDAH com&oacute;rbidos. La evaluaci&oacute;n neuropsicol&oacute;gica ampliada (<a href=\"/articulos/evaluacion-neuropsicologica-guia-clinica.html\">gu&iacute;a cl&iacute;nica</a>) integra atenci&oacute;n, funciones ejecutivas y lenguaje cuando el perfil escolar no cuadra con CI global.",
                ),
            },
            {
                "h2": "Informe psicol&oacute;gico y comunicaci&oacute;n con escuela y familia",
                "html": p(
                    "El informe describe instrumentos aplicados, validez de la sesi&oacute;n, puntuaciones con escala adecuada (escalar, compuesto), fortalezas, debilidades y recomendaciones concretas: tiempo extra en evaluaciones, material visual, reducci&oacute;n de distractores, tutor&iacute;as espec&iacute;ficas. Evite jerga estad&iacute;stica sin traducci&oacute;n funcional. Incluya limitaciones (fatiga, un solo d&iacute;a de evaluaci&oacute;n, idioma).",
                    "En devoluci&oacute;n a padres, enfatice que el CI es una fotograf&iacute;a de rendimiento en tareas estandarizadas, no destino. Ofrezca estrategias de estimulaci&oacute;n en casa alineadas con fortalezas. Con escuelas, sugiera adecuaciones observables y medibles; no diagnostique necesidades educativas fuera de marco legal local sin datos suficientes.",
                    "Para continuidad de evaluaciones repetidas (reevaluaci&oacute;n cada 2-3 a&ntilde;os en algunos contextos), centralizar protocolos, puntuaciones brutas y observaciones en {kalyo} facilita comparaci&oacute;n longitudinal sin p&eacute;rdida de datos entre profesionales.".format(
                        kalyo=KALYO
                    ),
                ),
            },
            {
                "h2": "Errores frecuentes y derivaci\u00f3n especializada",
                "html": p(
                    "Errores comunes: evaluar solo para satisfacer presi&oacute;n escolar sin hip&oacute;tesis cl&iacute;nica; interpretar un &iacute;ndice aislado ignorando validez; omitir exploraci&oacute;n emocional cuando hay ansiedad de rendimiento extrema; prometer cambio de escuela o diagn&oacute;stico m&eacute;dico. Otro error es usar versiones pirata o incompletas sin normas v&aacute;lidas.",
                    "Derive a neurolog&iacute;a pedi&aacute;trica si hay convulsiones, regresi&oacute;n de habilidades, macrocefalia o historia perinatal de riesgo. Derive a psiquiatr&iacute;a infantil si hay psicosis, man&iacute;a o autolesiones. Derive a fonoaudiolog&iacute;a si el perfil sugiere trastorno del lenguaje primario. Coordinaci&oacute;n interdisciplinaria enriquece el <strong>test de inteligencia ni&ntilde;os</strong> dentro de evaluaci&oacute;n integral.",
                    "Mantenga formaci&oacute;n continua en pruebas Wechsler y supervisi&oacute;n de casos complejos. En poblaciones rurales o ind&iacute;genas, considere limitaciones normativas y valore evaluaci&oacute;n cualitativa complementaria con respeto cultural.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfA qu\u00e9 edad conviene aplicar el primer test de inteligencia?",
                "a": "Depende de la pregunta cl\u00ednica. WPPSI-IV puede aplicarse desde los 2 a\u00f1os y medio con interpretaci\u00f3n cautelosa; WISC-V desde los 6 a\u00f1os. Antes de los 4 a\u00f1os, priorice evaluaci\u00f3n del desarrollo global y observaci\u00f3n cl\u00ednica salvo indicaci\u00f3n espec\u00edfica.",
            },
            {
                "q": "\u00bfUn CI bajo confirma discapacidad intelectual?",
                "a": "No por s\u00ed solo. Se requieren d\u00e9ficits en funcionamiento adaptativo, inicio en el periodo de desarrollo y exclusi\u00f3n de causas alternativas. El test cognitivo es un pilar, no el criterio \u00fanico.",
            },
            {
                "q": "\u00bfPuedo evaluar a un ni\u00f1o biling\u00fce solo en espa\u00f1ol?",
                "a": "Si el espa\u00f1ol no es su idioma dominante, el \u00edndice verbal puede estar sesgado. Documente dominio ling\u00fc\u00edstico y considere subpruebas no verbales o evaluaci\u00f3n por profesional biling\u00fce.",
            },
            {
                "q": "\u00bfCon qu\u00e9 frecuencia se repite el WISC-V?",
                "a": "Los manuales recomiendan intervalos m\u00ednimos (t\u00edpicamente 12 meses) para evitar efecto pr\u00e1ctica. Reeval\u00fae cuando cambie el plan educativo o haya intervenci\u00f3n que altere el perfil esperado.",
            },
            {
                "q": "\u00bfEl test de inteligencia diagnostica TDAH o autismo?",
                "a": "No. Puede mostrar perfil compatible (p. ej., memoria de trabajo baja), pero el diagn\u00f3stico requiere criterios espec\u00edficos, historia del desarrollo y herramientas adicionales.",
            },
        ],
        "related": [
            {"href": "/articulos/wisc-v-test-inteligencia-ninos.html", "label": "WISC-V: test de inteligencia infantil"},
            {"href": "/articulos/evaluacion-neuropsicologica-guia-clinica.html", "label": "Evaluaci\u00f3n neuropsicol\u00f3gica: gu\u00eda cl\u00ednica"},
            {"href": "/articulos/tdah-adultos.html", "label": "TDAH en adultos: evaluaci\u00f3n y tratamiento"},
            {"href": "/articulos/que-es-el-dsm-5.html", "label": "Qu\u00e9 es el DSM-5: manual diagn\u00f3stico"},
        ],
    }
)

# --- 27 sindrome-burnout-evaluacion ---
ARTICLES.append(
    {
        "slug": "sindrome-burnout-evaluacion",
        "title": "S\u00edndrome de burnout: evaluaci\u00f3n cl\u00ednica con MBI | Kalyo",
        "description": "S\u00edndrome de burnout evaluaci\u00f3n: tr\u00edada Maslach, MBI y MBI-HSS, diferencial con depresi\u00f3n, intervenci\u00f3n psicol\u00f3gica y prevenci\u00f3n en profesionales de salud.",
        "keywords": "s\u00edndrome de burnout evaluaci\u00f3n, MBI, Maslach, agotamiento emocional, despersonalizaci\u00f3n, salud laboral, psicolog\u00eda cl\u00ednica, M\u00e9xico",
        "h1": "S\u00edndrome de burnout: evaluaci\u00f3n cl\u00ednica para psic\u00f3logos",
        "breadcrumb_short": "Burnout: evaluaci\u00f3n",
        "hero_alt": "Evaluaci\u00f3n del s\u00edndrome de burnout con inventario MBI en consulta cl\u00ednica",
        "inline_alt": "Tr\u00edada del burnout: agotamiento, despersonalizaci\u00f3n y realizaci\u00f3n personal",
        "quick_answer": "La <strong>evaluaci&oacute;n del s&iacute;ndrome de burnout</strong> mide agotamiento emocional, despersonalizaci&oacute;n y baja realizaci&oacute;n personal, t&iacute;picamente con el <a href=\"/articulos/inventario-burnout-mbi.html\">Inventario de Burnout de Maslach (MBI)</a>. No es diagn&oacute;stico DSM-5; orienta intervenci&oacute;n laboral, cl&iacute;nica y prevenci&oacute;n en profesionales de salud mental y docentes.",
        "intro_long": "El <strong>s&iacute;ndrome de burnout</strong> afecta de forma creciente a psic&oacute;logos, m&eacute;dicos, enfermeras y docentes en M&eacute;xico, donde jornadas largas, carga administrativa y exposici&oacute;n emocional intensa erosionan la salud mental. La evaluaci&oacute;n cl&iacute;nica rigurosa distingue burnout de depresi&oacute;n mayor, trastorno de ansiedad o agotamiento f&iacute;sico por otras causas. Este art&iacute;culo describe la tr&iacute;ada de Maslach, uso responsable del MBI y MBI-HSS, interpretaci&oacute;n por subescalas, factores organizacionales y recomendaciones basadas en evidencia para consultorios privados, hospitales, escuelas p&uacute;blicas y servicios comunitarios de salud.",
        "meta_label": "Salud laboral &middot; Psicometr&iacute;a cl&iacute;nica &middot; 2026",
        "cta_h2": CTA_H2,
        "cta_p": CTA_P,
        "sections": [
            {
                "h2": "Qu\u00e9 es el s\u00edndrome de burnout en contexto cl\u00ednico",
                "html": p(
                    "El burnout se define operativamente como s&iacute;ndrome de agotamiento laboral cr&oacute;nico con tres dimensiones: <strong>agotamiento emocional</strong> (fatiga extrema por demanda interpersonal), <strong>despersonalizaci&oacute;n</strong> (actitudes c&iacute;nicas o distantes hacia usuarios o pacientes) y <strong>baja realizaci&oacute;n personal</strong> (sentimiento de incompetencia o falta de logro). La OMS lo incluy&oacute; en la CIE-11 como fen&oacute;meno ocupacional, no como trastorno mental independiente, lo que no resta gravedad cl&iacute;nica.",
                    "En psic&oacute;logos cl&iacute;nicos, el burnout surge de acumulaci&oacute;n de sesiones traum&aacute;ticas, falta de supervisi&oacute;n, listas de espera interminables y conflicto rol persona-profesional. En M&eacute;xico, muchos profesionales combinan consulta privada, instituci&oacute;n p&uacute;blica y docencia, multiplicando factores de riesgo. La evaluaci&oacute;n debe contextualizar el puesto, antig&uuml;edad y cambios organizacionales recientes (p. ej., telemedicina masiva post-pandemia).",
                    "Diferencie burnout de &laquo;estar cansado&raquo;: el burnout implica deterioro sostenido en actitud y funcionamiento laboral, con riesgo de errores cl&iacute;nicos, absentismo y abandono de la profesi&oacute;n. Identificarlo temprano protege al profesional y a los pacientes.",
                ),
            },
            {
                "h2": "Indicaciones para evaluar burnout en consulta",
                "html": p(
                    "Eval&uacute;e cuando el profesional reporta fatiga que no mejora con descanso, cinismo hacia pacientes, dificultad para empatizar, insomnio de conciliaci&oacute;n por rumiaciones laborales, aumento de errores administrativos o deseo de dejar la cl&iacute;nica pese a formaci&oacute;n previa entusiasta. Instituciones de salud pueden solicitar evaluaci&oacute;n grupal tras rotaci&oacute;n en urgencias o programas de residencia.",
                    "La <strong>evaluaci&oacute;n del s&iacute;ndrome de burnout</strong> tambi&eacute;n es &uacute;til en investigaci&oacute;n organizacional y dise&oacute;o de intervenciones, siempre con consentimiento y confidencialidad. No use MBI como filtro contrataci&oacute;n sin base &eacute;tica y legal s&oacute;lida. Combine autorreporte con entrevista cl&iacute;nica: algunos profesionales minimizan despersonalizaci&oacute;n por verg&uuml;enza.",
                    "Identifique burnout de relaciones interpersonales ca&oacute;ticas, falta de supervisi&oacute;n cl&iacute;nica, ausencia de l&iacute;mites entre vida personal y consulta, y exposici&oacute;n repetida a material traum&aacute;tico sin espacios de procesamiento. En servicios p&uacute;blicos mexicanos, la sobrecarga de pacientes por plaza aumenta despersonalizaci&oacute;n medible en MBI.",
                    "Explore comorbilidades: depresi&oacute;n mayor, trastorno de ansiedad generalizada, insomnio cr&oacute;nico, consumo de alcohol para &laquo;desconectar&raquo; y trastornos som&aacute;ticos. El burnout frecuentemente coexiste con ellos; el plan terap&eacute;utico debe abordar ambos niveles.",
                ),
            },
            {
                "h2": "MBI y MBI-HSS: administraci\u00f3n e interpretaci\u00f3n",
                "html": p(
                    "El <a href=\"/articulos/inventario-burnout-mbi.html\">Maslach Burnout Inventory (MBI)</a> existe en versiones para servicios humanos (MBI-HSS), educaci&oacute;n (MBI-ES) y general (MBI-GS). MBI-HSS es la m&aacute;s usada en psic&oacute;logos y personal sanitario. Consta de 22 &iacute;tems en tres subescalas; cada una se punt&uacute;a por separado, no hay total &uacute;nico oficial en todos los contextos.",
                    "Agotamiento emocional alto sugiere sobrecarga de demanda afectiva; despersonalizaci&oacute;n elevada se asocia a distanciamiento defensivo; baja realizaci&oacute;n personal indica percepci&oacute;n de ineficacia. Consulte puntos de corte publicados en manuales y revisiones meta-anal&iacute;ticas para su versi&oacute;n; evite inventar categor&iacute;as. Repita medici&oacute;n cada 3-6 meses si hay intervenci&oacute;n institucional.",
                    "Administre en condiciones privadas, explique que no hay respuestas correctas y aclare uso de resultados (individual vs agregado institucional). En grupos peque&ntilde;os, garantice anonimato si los datos van a direcci&oacute;n.",
                    "Compare puntuaciones con normas publicadas para la versi&oacute;n en espa&ntilde;ol cuando existan; si usa puntos de corte de la literatura internacional, ind&iacute;quelo en el informe. Evite etiquetar &laquo;burnout severo&raquo; sin entrevista cl&iacute;nica que confirme deterioro funcional.",
                )
                + """
<table class="items-table">
<thead><tr><th>Subescala MBI-HSS</th><th>Contenido</th><th>Interpretaci\u00f3n cl\u00ednica</th></tr></thead>
<tbody>
<tr><td>Agotamiento emocional</td><td>9 \u00edtems</td><td>Exhausti\u00f3n por carga laboral emocional</td></tr>
<tr><td>Despersonalizaci\u00f3n</td><td>5 \u00edtems</td><td>Actitudes fr\u00edas o c\u00ednicas hacia usuarios</td></tr>
<tr><td>Realizaci\u00f3n personal</td><td>8 \u00edtems</td><td>Competencia y logro (puntuaci\u00f3n baja = riesgo)</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "Diferencial con depresi\u00f3n, ansiedad y estr\u00e9s agudo",
                "html": p(
                    "El burnout comparte fatiga y anhedonia con <strong>depresi&oacute;n mayor</strong>, pero suele estar m&aacute;s ligado al contexto laboral: s&iacute;ntomas mejoran parcialmente en vacaciones prolongadas (aunque no siempre desaparecen). La depresi&oacute;n afecta m&aacute;ltiples dominios vitales sin anclaje exclusivo al trabajo. Aplique PHQ-9 o entrevista estructurada cuando haya duda.",
                    "La ansiedad generalizada incluye preocupaci&oacute;n difusa; el burnout incluye cinismo espec&iacute;fico hacia destinatarios del servicio. El estr&eacute;s agudo post-evento cr&iacute;tico (p. ej., muerte de paciente en sesi&oacute;n) puede simular pico de agotamiento; explore temporalidad y evento desencadenante. <a href=\"/articulos/que-es-el-dsm-5.html\">DSM-5</a> no codifica burnout como trastorno; documente diagn&oacute;sticos com&oacute;rbidos cuando cumplan criterios.",
                    "Regla pr&aacute;ctica: si al cambiar de rol o reducir carga no hay mejor&iacute;a en 2-3 meses y aparecen ideaci&oacute;n suicida o culpa global, priorice evaluaci&oacute;n de depresi&oacute;n y derive psiquiatr&iacute;a si corresponde.",
                    "En devoluci&oacute;n, explique al profesional que el MBI describe estado actual relacionado con el trabajo, no un rasgo permanente. Esto reduce verg&uuml;enza y facilita b&uacute;squeda de apoyo institucional o cambio de rol.",
                ),
            },
            {
                "h2": "Intervenci\u00f3n psicol\u00f3gica y cambios organizacionales",
                "html": p(
                    "Intervenciones individuales: TCC para manejo de estr&eacute;s, entrenamiento en mindfulness basado en evidencia, l&iacute;mites de sesiones diarias, t&eacute;cnicas de recuperaci&oacute;n entre consultas (micro-pausas, ejercicio), psicoeducaci&oacute;n sobre compasi&oacute;n y autocr&iacute;tica. Trabaje creencias de invulnerabilidad (&laquo;debo aguantar todo&raquo;) frecuentes en profesionales de salud mental.",
                    "Intervenciones organizacionales (cuando hay acceso a direcci&oacute;n): reducir carga administrativa, grupos de apoyo entre pares, supervisi&oacute;n cl&iacute;nica obligatoria, rotaci&oacute;n de tareas de alto impacto emocional, pol&iacute;ticas de licencia. La evidencia sugiere que solo intervenciones individuales son insuficientes si el entorno laboral permanece t&oacute;xico.",
                    "Proponga acuerdos de autocuidado verificables: l&iacute;mite de sesiones diarias, d&iacute;a libre semanal sin consulta, actividad f&iacute;sica programada y revisi&oacute;n trimestral del MBI para objetivar cambio.",
                    "Para seguimiento de MBI repetido, notas de sesi&oacute;n y acuerdos de autocuidado, {kalyo} ayuda a visualizar tendencias sin mezclar datos institucionales agregados con expediente cl&iacute;nico individual.".format(
                        kalyo=KALYO
                    ),
                ),
            },
            {
                "h2": "Prevenci\u00f3n, supervisi\u00f3n y \u00e9tica profesional",
                "html": p(
                    "Prevenci&oacute;n primaria incluye formaci&oacute;n en l&iacute;mites terap&eacute;uticos desde pregrado, pr&aacute;ctica supervisada con carga realista y cultura que normalice pedir ayuda. Psic&oacute;logos en pr&aacute;ctica privada deben programar supervisi&oacute;n externa peri&oacute;dica aunque no sea obligatoria legalmente.",
                    "Si el profesional evaluado muestra despersonalizaci&oacute;n severa, eval&uacute;e riesgo para pacientes (sesiones apresuradas, falta de empat&iacute;a documentada) y considere reducci&oacute;n temporal de carga. El deber de cuidado al usuario prevalece. Documente recomendaciones y seguimiento.",
                    "En informes institucionales agregados, reporte medias y percentiles sin identificar individuos. Respete propiedad del MBI: use versiones autorizadas y cite manual en informes de investigaci&oacute;n.",
                    "Incluya en notas de evoluci&oacute;n factores protectores identificados (red de colegas, hobbies, supervisi&oacute;n activa) para equilibrar el enfoque cl&iacute;nico y sostener motivaci&oacute;n al cambio.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfEl burnout es un diagn\u00f3stico DSM-5?",
                "a": "No tiene categor\u00eda propia en DSM-5. Se conceptualiza como fen\u00f3meno relacionado con el trabajo (CIE-11). Puede coexistir con depresi\u00f3n o ansiedad, que s\u00ed tienen criterios DSM-5.",
            },
            {
                "q": "\u00bfQu\u00e9 versi\u00f3n del MBI uso con psic\u00f3logos cl\u00ednicos?",
                "a": "La MBI-HSS (Human Services Survey) est\u00e1 dise\u00f1ada para profesionales que atienden personas en servicios de salud, educaci\u00f3n y trabajo social cl\u00ednico.",
            },
            {
                "q": "\u00bfUn puntaje alto en agotamiento basta para concluir burnout?",
                "a": "La interpretaci\u00f3n cl\u00ednica integra las tres subescalas y la entrevista. Perfiles mixtos son comunes; no reduzca el s\u00edndrome a un solo n\u00famero ni a una subescala aislada.",
            },
            {
                "q": "\u00bfPuedo aplicar MBI en l\u00ednea sin supervisi\u00f3n?",
                "a": "S\u00ed en contextos autorizados, pero explique prop\u00f3sito, confidencialidad y limitaciones. Resultados no sustituyen evaluaci\u00f3n cl\u00ednica completa si hay deterioro grave o ideaci\u00f3n suicida.",
            },
            {
                "q": "\u00bfCu\u00e1ndo derivar a psiquiatr\u00eda por burnout?",
                "a": "Ante depresi\u00f3n mayor, insomnio severo refractario, ideaci\u00f3n suicida, consumo de sustancias para afrontar jornada o incapacidad funcional persistente pese a cambios laborales razonables. Coordine licencia temporal si el profesional sigue atendiendo en deterioro.",
            },
        ],
        "related": [
            {"href": "/articulos/inventario-burnout-mbi.html", "label": "Inventario MBI: tr\u00edada del burnout"},
            {"href": "/articulos/burnout-laboral.html", "label": "Burnout laboral: s\u00edntomas y manejo"},
            {"href": "/articulos/pss-10-escala-estres-percibido.html", "label": "PSS-10: estr\u00e9s percibido"},
            {"href": "/articulos/que-es-el-dsm-5.html", "label": "Qu\u00e9 es el DSM-5"},
        ],
    }
)

# --- 28 tdah-adultos-evaluacion-diagnostico ---
ARTICLES.append(
    {
        "slug": "tdah-adultos-evaluacion-diagnostico",
        "title": "TDAH adultos: evaluaci\u00f3n, diagn\u00f3stico y ASRS cl\u00ednico | Kalyo",
        "description": "TDAH adultos evaluaci\u00f3n: criterios DSM-5, ASRS, WURS, entrevista DIVA, diagn\u00f3stico diferencial e informes cl\u00ednicos con psiquiatr\u00eda en consulta mexicana.",
        "keywords": "TDAH adultos evaluaci\u00f3n, ASRS, WURS, DIVA, DSM-5, CAARS, diagn\u00f3stico diferencial, psicolog\u00eda cl\u00ednica, M\u00e9xico",
        "h1": "TDAH en adultos: evaluaci\u00f3n y diagn\u00f3stico cl\u00ednico",
        "breadcrumb_short": "TDAH adultos: evaluaci\u00f3n",
        "hero_alt": "Evaluaci\u00f3n de TDAH en adultos con escalas ASRS y entrevista cl\u00ednica",
        "inline_alt": "Proceso de evaluaci\u00f3n del TDAH en adultos: infancia, escalas y entrevista",
        "quick_answer": "La <strong>evaluaci&oacute;n de TDAH en adultos</strong> exige s&iacute;ntomas de inatenci&oacute;n y/o hiperactividad desde antes de los 12 a&ntilde;os, deterioro en dos o m&aacute;s contextos y exclusi&oacute;n de cuadros alternativos. El <a href=\"/articulos/asrs-tdah-adultos.html\">ASRS</a> tamiza; la entrevista estructurada (p. ej. DIVA) y datos de infancia confirman.",
        "intro_long": "El TDAH no desaparece necesariamente en la adultez: muchos pacientes en M&eacute;xico llegan a consulta tras d&eacute;cadas de fracaso acad&eacute;mico mal interpretado, inestabilidad laboral o conflictos de pareja atribuidos a &laquo;flojera&raquo;. La <strong>evaluaci&oacute;n de TDAH en adultos</strong> requiere evidencia longitudinal, informantes cuando sea posible y diagn&oacute;stico diferencial riguroso con ansiedad, trastorno bipolar, TEA y efectos de sustancias. Este art&iacute;culo orienta al psic&oacute;logo cl&iacute;nico en protocolo de evaluaci&oacute;n, uso de ASRS y WURS, entrevista DIVA, redacci&oacute;n de informes &uacute;tiles para psiquiatr&iacute;a y criterios para ajustes razonables en el entorno laboral.",
        "meta_label": "Neurodesarrollo &middot; Evaluaci&oacute;n cl&iacute;nica &middot; 2026",
        "cta_h2": CTA_H2,
        "cta_p": CTA_P,
        "sections": [
            {
                "h2": "Presentaci\u00f3n cl\u00ednica del TDAH en adultos",
                "html": p(
                    "En adultos, la hiperactividad motora suele convertirse en <strong>inquietud interna</strong>, impulsividad verbal, cambios de trabajo frecuentes o sensaci&oacute;n de motor encendido. La inatenci&oacute;n se manifiesta en olvidos cr&oacute;nicos de citas, dificultad para completar proyectos, desorganizaci&oacute;n dom&eacute;stica, procrastinaci&oacute;n paralizante y errores por falta de detalle en tareas administrativas. Mujeres a menudo presentan subtipo predominantemente inatento con diagn&oacute;stico tard&iacute;o.",
                    "Comorbilidades frecuentes: trastornos de ansiedad, depresi&oacute;n, consumo de cannabis o alcohol para autorregular, trastornos de personalidad cuando hubo invalidaci&oacute;n cr&oacute;nica. Explore impacto en autoestima y creencias nucleares (&laquo;soy incapaz&raquo;). En M&eacute;xico, acceso limitado a evaluaci&oacute;n infantil incrementa solicitudes de diagn&oacute;stico retrospectivo en la treinta&ntilde;era y cuarenta&ntilde;era.",
                    "Documente &aacute;reas funcionales: educaci&oacute;n, trabajo, pareja, manejo financiero, manejo de salud (olvidos de medicaci&oacute;n). El DSM-5 exige evidencia de deterioro en al menos dos dominios.",
                    "Pregunte por compensaciones desarrolladas (listas exhaustivas, alarmas m&uacute;ltiples, delegaci&oacute;n extrema) que enmascaran s&iacute;ntomas en entrevista breve. La historia de &laquo;funcionar bien un mes y colapsar despu&eacute;s&raquo; sugiere d&eacute;ficit ejecutivo m&aacute;s que falta de inter&eacute;s.",
                ),
            },
            {
                "h2": "Criterios DSM-5 y evidencia de inicio en la infancia",
                "html": p(
                    "Confirme al menos cinco s&iacute;ntomas de inatenci&oacute;n y/o cinco de hiperactividad-impulsividad (seis si menor de 17 a&ntilde;os) presentes &ge;6 meses, inconsistentes con nivel de desarrollo, con inicio antes de los 12 a&ntilde;os y ocurrencia en dos o m&aacute;s entornos. S&iacute;ntomas no deben explicarse mejor por otro trastorno mental.",
                    "La evidencia de infancia puede obtenerse de informes escolares, boletas con comentarios de maestros, entrevista a padres o hermanos, &aacute;lbumes que muestren proyectos incompletos, y cuestionarios retrospectivos como el <a href=\"/articulos/wurs-tdah-infancia-adultos.html\">WURS</a>. La amnesia autobiogr&aacute;fica es com&uacute;n; no concluya negativamente por falta de recuerdo v&iacute;vido sin fuentes alternativas.",
                    "Consulte criterios completos en la gu&iacute;a <a href=\"/articulos/tdah-adultos.html\">TDAH en adultos</a> para alinear evaluaci&oacute;n con especificadores (presentaci&oacute;n combinada, inatenta, hiperactiva) y severidad.",
                    "Registre edad de inicio aproximada por dominio (escuela primaria vs secundaria) y si hubo periodos de relativa compensaci&oacute;n en contextos altamente estructurados o de alto inter&eacute;s.",
                ),
            },
            {
                "h2": "Protocolo de evaluaci\u00f3n: ASRS, WURS y entrevista DIVA",
                "html": p(
                    "Flujo recomendado: (1) entrevista cl&iacute;nica inicial con motivo y comorbilidades; (2) tamizaje <a href=\"/articulos/asrs-tdah-adultos.html\">ASRS v1.1</a> (6 o 18 &iacute;tems); (3) WURS u otro cuestionario retrospectivo de infancia; (4) entrevista estructurada DIVA-5 o equivalente que eval&uacute;a criterios en infancia y adultez con ejemplos concretos; (5) escalas complementarias CAARS, BRIEF-A para funciones ejecutivas si hay formaci&oacute;n; (6) prueba cognitiva breve si hay duda de discapacidad intelectual.",
                    "ASRS positivo no diagnostica; orienta profundizaci&oacute;n. Parte de ASRS est&aacute; en dominio p&uacute;blico; mantenga estandarizaci&oacute;n de aplicaci&oacute;n. DIVA requiere capacitaci&oacute;n; documente ejemplos conductuales por criterio en cada etapa vital.",
                    "Solicite permiso para contactar pareja o familiar informante; compare relatos. Discrepancias no invalidan diagn&oacute;stico pero requieren exploraci&oacute;n (camuflaje, compensaci&oacute;n alta, sesgo del informante).",
                    "Reserve sesi&oacute;n dedicada solo a infancia con preguntas concretas por entorno (aula, casa, juegos). Evite preguntas cerradas del tipo &laquo;&iquest;era desordenado?&raquo; que invitan respuesta socialmente deseable.",
                )
                + """
<ol>
<li>Entrevista cl\u00ednica y consentimiento informado.</li>
<li>ASRS v1.1 y cuestionario retrospectivo de infancia (WURS).</li>
<li>Entrevista estructurada DIVA-5 o similar.</li>
<li>Diagn\u00f3stico diferencial y pruebas complementarias si indicado.</li>
<li>Informe integrado y plan de tratamiento o derivaci\u00f3n.</li>
</ol>""",
            },
            {
                "h2": "Diagn\u00f3stico diferencial en adultos",
                "html": p(
                    "Diferencie TDAH de <strong>trastorno de ansiedad generalizada</strong> (preocupaci&oacute;n difusa vs desorganizaci&oacute;n por inatenci&oacute;n), <strong>trastorno bipolar</strong> (s&iacute;ntomas epis&oacute;dicos con inicio adulto vs curso cr&oacute;nico desde infancia), <strong>TEA</strong> (d&eacute;ficits sociales primarios, rigidez), <strong>trastornos de personalidad</strong> (especialmente l&iacute;mite si impulsividad interpersonal extrema), <strong>apnea del sue&ntilde;o</strong> e <strong>hipotiroidismo</strong> (somnolencia diurna).",
                    "Consumo de estimulantes no prescritos complica evaluaci&oacute;n; indague sustancias con tacto. Trastorno por consumo de cannabis puede empeorar motivaci&oacute;n y mimetizar inatenci&oacute;n. Eval&uacute;e durante periodo de abstinencia cuando sea seguro.",
                    "Depresi&oacute;n mayor puede causar pseudo-inatenci&oacute;n; si s&iacute;ntomas remiten con tratamiento del &aacute;nimo y nunca hubo historia infantil, TDAH es menos probable. Documente razonamiento diferencial en informe.",
                    "Solicite estudios m&eacute;dicos b&aacute;sicos (TSH, hemograma) cuando la somnolencia diurna o fatiga cognitive no cuadren con patr&oacute;n cl&aacute;sico de TDAH.",
                ),
            },
            {
                "h2": "Informe cl\u00ednico, psiquiatr\u00eda y ajustes laborales",
                "html": p(
                    "El informe resume fuentes, cumplimiento criterio por criterio, especificador, severidad, comorbilidades y recomendaciones: psicoeducaci&oacute;n, TCC para TDAH adultos, coaching de organizaci&oacute;n, evaluaci&oacute;n psiqui&aacute;trica para farmacoterapia si el paciente lo desea. No garantice acceso a medicamento; es decisi&oacute;n m&eacute;dica.",
                    "Cartas para empleador o escuela deben ser breves, describir ajustes funcionales (tiempo extra en tareas, recordatorios escritos, reducci&oacute;n de interrupciones) sin divulgar diagn&oacute;stico si el paciente prefiere confidencialidad limitada. En M&eacute;xico, la NOM-035 refuerza evaluaci&oacute;n de riesgo psicosocial laboral; TDAH puede interactuar con entornos de alta demanda.",
                    "Centralizar ASRS, notas DIVA y objetivos terap&eacute;uticos en {kalyo} mejora continuidad cuando el paciente alterna psicolog&iacute;a y psiquiatr&iacute;a.".format(
                        kalyo=KALYO
                    ),
                    "Incluya en informe secci&oacute;n de recomendaciones no farmacol&oacute;gicas priorizadas: rutinas externas, fragmentaci&oacute;n de tareas, entrenamiento en estimaci&oacute;n temporal y manejo de distracciones digitales.",
                ),
            },
            {
                "h2": "Errores frecuentes y buenas pr\u00e1cticas",
                "html": p(
                    "Errores: diagnosticar solo con ASRS positivo; omitir historia infantil; no evaluar comorbilidades; confundir TDAH con alta capacidad no reconocida; medicalizar estr&eacute;s vital agudo. Otro error es iniciar evaluaci&oacute;n durante crisis (duelo, divorcio) sin posponer conclusi&oacute;n diagn&oacute;stica.",
                    "Buenas pr&aacute;cticas: reservar al menos dos sesiones de evaluaci&oacute;n; usar ejemplos conductuales escritos; ofrecer psicoeducaci&oacute;n sobre neurodesarrollo para reducir verg&uuml;enza; derivar cuando perfil sugiere TEA o bipolaridad; reevaluar si tratamiento espec&iacute;fico TDAH no produce mejor&iacute;a funcional en 3-6 meses.",
                    "Mantenga formaci&oacute;n en evaluaci&oacute;n de adultos; supervisi&oacute;n en casos con simulaci&oacute;n o beneficio secundario (acceso a estimulantes). Documente base de evidencia para cada criterio DSM-5.",
                    "Si tras evaluaci&oacute;n completa no se confirma TDAH, ofrezca devoluci&oacute;n compasiva con hip&oacute;tesis alternativas y plan de seguimiento; evite dejar al paciente con sensaci&oacute;n de consulta fallida.",
                    "Considere evaluaci&oacute;n neuropsicol&oacute;gica breve de funciones ejecutivas cuando hay queja de olvido pero ASRS y DIVA no aclaran el cuadro; la integraci&oacute;n multimodal fortalece conclusiones diagn&oacute;sticas y orienta tratamiento.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfEl ASRS basta para diagnosticar TDAH en adultos?",
                "a": "No. Es tamizaje validado para detectar probable TDAH. El diagn\u00f3stico requiere entrevista cl\u00ednica, evidencia de infancia, integraci\u00f3n con WURS o DIVA y exclusi\u00f3n de otras condiciones m\u00e9dicas o psiqui\u00e1tricas que expliquen mejor el cuadro.",
            },
            {
                "q": "\u00bfQu\u00e9 hago si no hay informantes de la infancia?",
                "a": "Use informes escolares archivados, WURS y entrevista detallada. La ausencia de informantes complica pero no impide evaluaci\u00f3n si hay evidencia documental o retrospectiva consistente en varios dominios de la infancia.",
            },
            {
                "q": "\u00bfPuede diagnosticarse TDAH por primera vez a los 40 a\u00f1os?",
                "a": "S\u00ed, si los s\u00edntomas existieron desde antes de los 12 a\u00f1os aunque no fueron reconocidos. Debe diferenciarse de inicio adulto por otra patolog\u00eda. Solicite ejemplos concretos por etapa escolar y laboral temprana.",
            },
            {
                "q": "\u00bfQui\u00e9n prescribe metilfenidato en M\u00e9xico?",
                "a": "M\u00e9dicos con capacidad legal para prescribir psicof\u00e1rmacos controlados, usualmente psiquiatr\u00eda o medicina familiar seg\u00fan contexto. El psic\u00f3logo eval\u00faa, documenta criterios y coordina; no prescribe estimulantes.",
            },
            {
                "q": "\u00bfWURS reemplaza a DIVA?",
                "a": "No. WURS es cuestionario retrospectivo; DIVA es entrevista estructurada que eval\u00faa cada criterio con ejemplos en infancia y adultez. Se complementan en la evaluaci\u00f3n integral de TDAH adultos en consulta cl\u00ednica.",
            },
        ],
        "related": [
            {"href": "/articulos/tdah-adultos.html", "label": "TDAH en adultos: gu\u00eda cl\u00ednica"},
            {"href": "/articulos/asrs-tdah-adultos.html", "label": "ASRS: tamizaje TDAH adultos"},
            {"href": "/articulos/wurs-tdah-infancia-adultos.html", "label": "WURS: s\u00edntomas retrospectivos"},
            {"href": "/articulos/que-es-el-dsm-5.html", "label": "Qu\u00e9 es el DSM-5"},
        ],
    }
)

# --- 29 evaluacion-neuropsicologica-instrumentos ---
ARTICLES.append(
    {
        "slug": "evaluacion-neuropsicologica-instrumentos",
        "title": "Evaluaci\u00f3n neuropsicol\u00f3gica: instrumentos y bater\u00eda | Kalyo",
        "description": "Evaluaci\u00f3n neuropsicol\u00f3gica: dominios cognitivos, selecci\u00f3n de pruebas, bater\u00eda flexible, informes cl\u00ednicos y coordinaci\u00f3n m\u00e9dica para psic\u00f3logos en M\u00e9xico.",
        "keywords": "evaluaci\u00f3n neuropsicol\u00f3gica, instrumentos neuropsicol\u00f3gicos, funciones ejecutivas, memoria, atenci\u00f3n, bater\u00eda cognitiva, neuropsicolog\u00eda cl\u00ednica",
        "h1": "Evaluaci\u00f3n neuropsicol\u00f3gica: instrumentos y bater\u00eda cl\u00ednica",
        "breadcrumb_short": "Evaluaci\u00f3n neuropsicol\u00f3gica",
        "hero_alt": "Bater\u00eda de evaluaci\u00f3n neuropsicol\u00f3gica con pruebas cognitivas en consultorio",
        "inline_alt": "Dominios cognitivos evaluados en una bater\u00eda neuropsicol\u00f3gica cl\u00ednica",
        "quick_answer": "La <strong>evaluaci&oacute;n neuropsicol&oacute;gica</strong> integra pruebas estandarizadas de atenci&oacute;n, memoria, lenguaje, funciones ejecutivas y visuoespacial seg&uacute;n la pregunta cl&iacute;nica. No existe bater&iacute;a &uacute;nica: se seleccionan instrumentos validados, como describe la <a href=\"/articulos/evaluacion-neuropsicologica-guia-clinica.html\">gu&iacute;a cl&iacute;nica</a>, e interpretan en contexto m&eacute;dico, funcional y educativo.",
        "intro_long": "La <strong>evaluaci&oacute;n neuropsicol&oacute;gica</strong> va m&aacute;s all&aacute; de un test de CI: caracteriza fortalezas y d&eacute;ficits cognitivos con implicaciones para diagn&oacute;stico diferencial, rehabilitaci&oacute;n y pron&oacute;stico funcional a mediano plazo. En M&eacute;xico, neuropsic&oacute;logos cl&iacute;nicos eval&uacute;an secuelas de TEC, demencias incipientes, epilepsia, TDAH complejo, esclerosis m&uacute;ltiple y efectos cognitivos de tratamientos oncol&oacute;gicos. Este art&iacute;culo resume dominios a evaluar, criterios para elegir instrumentos, modelos de bater&iacute;a fija vs flexible, validez de la evaluaci&oacute;n e integraci&oacute;n con neurolog&iacute;a y psiquiatr&iacute;a sin inventar datos normativos no publicados.",
        "meta_label": "Neuropsicolog&iacute;a cl&iacute;nica &middot; Instrumentos &middot; 2026",
        "cta_h2": CTA_H2,
        "cta_p": CTA_P,
        "sections": [
            {
                "h2": "Objetivos de la evaluaci\u00f3n neuropsicol\u00f3gica",
                "html": p(
                    "La evaluaci&oacute;n responde preguntas cl&iacute;nicas concretas: &iquest;Hay deterioro cognitivo objetivo m&aacute;s all&aacute; del queja subjetiva? &iquest;Cu&aacute;l es el perfil de funciones ejecutivas en TDAH adulto? &iquest;Existen secuelas atencionales post-TEC compatibles con restricciones laborales? &iquest;El cuadro sugiere demencia tipo Alzheimer vs depresi&oacute;n pseudodemencia? Formule hip&oacute;tesis antes de elegir pruebas.",
                    "Los objetivos gu&iacute;an extensi&oacute;n de bater&iacute;a: evaluaci&oacute;n breve de cribado (1-2 horas) vs bater&iacute;a completa (varias sesiones). Documente motivo de referencia (neur&oacute;logo, onc&oacute;logo, escuela, juzgado) y expectativas del paciente para alinear devoluci&oacute;n.",
                    "La evaluaci&oacute;n neuropsicol&oacute;gica es proceso din&aacute;mico: observaciones conductuales (fatiga, perseveraci&oacute;n, impulsividad) complementan puntuaciones. Incluya entrevista cl&iacute;nica sobre antecedentes m&eacute;dicos, medicaci&oacute;n psicoactiva, sue&ntilde;o, consumo de alcohol y educaci&oacute;n prem&oacute;rbida.",
                    "Acuerde con el paciente si desea que el informe se comparta con empleador, escuela o familiar; adapte nivel de detalle t&eacute;cnico del lenguaje a cada destinatario autorizado.",
                    "En evaluaciones medicolegales, acuerde por escrito alcance, pruebas incluidas y plazos; evite ampliar bater&iacute;a sin autorizaci&oacute;n porque incrementa costo y fatiga del evaluado.",
                ),
            },
            {
                "h2": "Dominios cognitivos e instrumentos representativos",
                "html": p(
                    "Dominios t&iacute;picos: <strong>atenci&oacute;n</strong> (sostenida, selectiva, dividida), <strong>memoria</strong> (verbal, visual, working memory), <strong>lenguaje</strong> (fluencias, comprensi&oacute;n, denominaci&oacute;n), <strong>funciones visuoespaciales y visuoconstructivas</strong>, <strong>funciones ejecutivas</strong> (flexibilidad, inhibici&oacute;n, planificaci&oacute;n), <strong>velocidad de procesamiento</strong> y <strong>funcionamiento intelectual global</strong> (WISC-V, WAIS-IV seg&uacute;n edad).",
                    "Instrumentos frecuentes en consultorios formados incluyen Stroop, Trail Making Test, Wisconsin Card Sorting (o versiones alternativas), Rey-Osterrieth, HVLT, digit span de escalas Wechsler, fluencias FAS/animales, Clock Drawing Test. Seleccione seg&uacute;n manual disponible, normas y competencia del evaluador; no liste pruebas que no domine.",
                    "Consulte la <a href=\"/articulos/evaluacion-neuropsicologica-guia-clinica.html\">gu&iacute;a cl&iacute;nica de evaluaci&oacute;n neuropsicol&oacute;gica</a> para alinear dominios con patolog&iacute;as frecuentes (TEC, demencia, esclerosis m&uacute;ltiple).",
                    "Documente nivel educativo formal y ocupaci&oacute;n previa para estimar reserva cognitiva; un profesional con altos a&ntilde;os de escolaridad puede compensar d&eacute;ficits leves en pruebas breves.",
                    "Integre prueba de inteligencia (WAIS-IV) cuando la pregunta cl&iacute;nica incluye discapacidad intelectual, deterioro global o discrepancia entre queja subjetiva y rendimiento aparente en entrevista.",
                )
                + """
<table class="items-table">
<thead><tr><th>Dominio</th><th>Ejemplos de tareas</th><th>Relevancia cl\u00ednica</th></tr></thead>
<tbody>
<tr><td>Atenci\u00f3n / psicomotricidad</td><td>TMT-A, s\u00edmbolos WAIS</td><td>TDAH, TEC leve, envejecimiento</td></tr>
<tr><td>Memoria verbal</td><td>HVLT, lista de palabras</td><td>Demencia, epilepsia temporal</td></tr>
<tr><td>Funciones ejecutivas</td><td>TMT-B, Stroop, WCST</td><td>TEC frontal, esclerosis m\u00faltiple</td></tr>
<tr><td>Visuoespacial</td><td>Rey copia, bloques WAIS</td><td>ICTUS derecho, demencia</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "Bater\u00eda fija versus bater\u00eda flexible",
                "html": p(
                    "Las <strong>bater&iacute;as fijas</strong> (p. ej., protocolos institucionales predefinidos) estandarizan comparaci&oacute;n entre pacientes del mismo servicio pero pueden incluir pruebas irrelevantes para el caso. Las <strong>bater&iacute;as flexibles</strong>, recomendadas en gu&iacute;as actuales, eligen pruebas seg&uacute;n hip&oacute;tesis, edad, educaci&oacute;n y capacidad f&iacute;sica, documentando justificaci&oacute;n de cada elecci&oacute;n.",
                    "Ventaja flexible: eficiencia y tolerancia del paciente (menos fatiga en demencia moderada). Riesgo: selecci&oacute;n sesgada si el cl&iacute;nico solo aplica pruebas confirmatorias. Mitigue con lista de comprobaci&oacute;n de dominios m&iacute;nimos seg&uacute;n pregunta cl&iacute;nica.",
                    "En M&eacute;xico, acceso desigual a materiales impone adaptaciones; declare limitaciones cuando falten normas locales o cuando se usen versiones abreviadas no est&aacute;ndar.",
                    "Revise lista de dominios cubiertos antes de cerrar evaluaci&oacute;n: omitir memoria en queja de olvidos post-TEC debilita validez cl&iacute;nica del informe final.",
                    "Documente por escrito cada prueba omitida y el motivo (fatiga, d&eacute;ficit sensorial, negativa del paciente) para defender conclusiones ante terceros.",
                ),
            },
            {
                "h2": "Validez, sesgos y consideraciones m\u00e9dicas",
                "html": p(
                    "Eval&uacute;e validez del rendimiento: esfuerzo, comprensi&oacute;n de instrucciones, visi&oacute;n/audici&oacute;n, dolor, ansiedad, somnolencia por medicaci&oacute;n. Pruebas de validez de esfuerzo existen para contextos medicolegales; &uacute;selas solo con formaci&oacute;n. Fatiga intra-evaluaci&oacute;n invalida comparaciones si no se registran pausas.",
                    "Factores demogr&aacute;ficos: escolaridad y alfabetizaci&oacute;n influyen en fluencias y memoria verbal; interprete con cautela sin caer en determinismo. Biling&uuml;ismo puede alterar tiempos en tareas verbales. Ajuste expectativas a l&iacute;nea base educativa, no solo edad.",
                    "Coordine con neurolog&iacute;a para correlacionar hallazgos con neuroimagen (RM estructural, EEG). Discrepancia imagen-cognici&oacute;n es com&uacute;n; expl&iacute;quela en informe. Postergue evaluaci&oacute;n aguda post-TEC hasta estabilizaci&oacute;n m&eacute;dica salvo urgencia forense.",
                    "Registre hora del d&iacute;a y medicaci&oacute;n reciente (sedantes, antiepil&eacute;pticos) que pueden deprimir temporalmente atenci&oacute;n y memoria inmediata.",
                    "En adultos mayores, descarte delirium intercurrente antes de atribuir bajo rendimiento a demencia neurodegenerativa; repita cribado cognitivo breve tras estabilizaci&oacute;n m&eacute;dica.",
                ),
            },
            {
                "h2": "Informe neuropsicol\u00f3gico e implicaciones funcionales",
                "html": p(
                    "El informe integra historia, observaci&oacute;n, puntuaciones (preferible con equivalentes a percentiles o clasificaciones cl&iacute;nicas del manual), comparaci&oacute;n intra-individual (fortalezas vs debilidades) y conclusiones vinculadas a pregunta de referencia. Evite listas de n&uacute;meros sin s&iacute;ntesis narrativa.",
                    "Recomendaciones funcionales: apoyos en trabajo (listas, ambientes silenciosos), rehabilitaci&oacute;n cognitiva, derivaci&oacute;n a logopedia, seguimiento anual en demencia. Para escuelas, traduzca d&eacute;ficits en estrategias pedag&oacute;gicas concretas.",
                    "Registre protocolo aplicado, fechas, duraci&oacute;n de sesiones y validez percibida. {kalyo} facilita archivar bater&iacute;as repetidas y comparar curvas longitudinales en enfermedades neurodegenerativas.".format(
                        kalyo=KALYO
                    ),
                    "Incluya secci&oacute;n de recomendaciones de rehabilitaci&oacute;n cognitiva o estrategias compensatorias concretas (agenda externa, rutinas de memoria, simplificaci&oacute;n de entorno) vinculadas a d&eacute;ficits medidos.",
                    "En seguimiento de demencia leve, compare no solo puntuaciones sino tambi&eacute;n capacidad para actividades instrumentales (manejo de finanzas, medicaci&oacute;n) reportada por cuidador con consentimiento.",
                ),
            },
            {
                "h2": "Formaci\u00f3n, \u00e9tica y derivaci\u00f3n",
                "html": p(
                    "La evaluaci&oacute;n neuropsicol&oacute;gica especializada requiere posgrado o supervisi&oacute;n prolongada; psic&oacute;logos generales deben acotar alcance o co-evaluar. No extrapole conclusiones m&eacute;dicas (localizaci&oacute;n de lesi&oacute;n) m&aacute;s all&aacute; de correlaciones inferenciales prudentes.",
                    "Derive a neurolog&iacute;a ante inicio agudo de d&eacute;ficits focales, crisis convulsivas nuevas o deterioro r&aacute;pido. Derive a psiquiatr&iacute;a si predominio afectivo compromete validez o requiere hospitalizaci&oacute;n. En menores, coordine con neuropsicolog&iacute;a infantil y <a href=\"/articulos/wisc-v-test-inteligencia-ninos.html\">evaluaci&oacute;n cognitiva infantil</a> cuando corresponda.",
                    "Respete propiedad intelectual de bater&iacute;as comerciales. Mantenga confidencialidad en informes para aseguradoras o procesos legales; el paciente autoriza divulgaci&oacute;n por escrito.",
                    "Ofrezca devoluci&oacute;n oral antes de entregar informe escrito; muchos pacientes necesitan psicoeducaci&oacute;n sobre variabilidad cognitiva normal vs deterioro patol&oacute;gico.",
                    "Planifique reevaluaci&oacute;n en demencias leves cada 6-12 meses para documentar curso; en TEC, la primera evaluaci&oacute;n post-aguda suele repetirse tras tres a seis meses por recuperaci&oacute;n espont&aacute;nea parcial.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfCu\u00e1nto dura una evaluaci\u00f3n neuropsicol\u00f3gica completa?",
                "a": "Var\u00eda seg\u00fan bater\u00eda y fatiga del paciente, t\u00edpicamente entre 4 y 8 horas divididas en 2-3 sesiones. Evaluaciones breves de un dominio pueden completarse en 1-2 horas. Pacientes geri\u00e1tricos o post-TEC agudo suelen tolerar menos tiempo por sesi\u00f3n y requieren m\u00e1s d\u00edas de aplicaci\u00f3n.",
            },
            {
                "q": "\u00bfSe necesita RM cerebral siempre?",
                "a": "No siempre, pero es recomendable ante inicio s\u00fabito, d\u00e9ficits focales, cefalea nueva o sospecha de causa org\u00e1nica. La decisi\u00f3n m\u00e9dica complementa la evaluaci\u00f3n cognitiva. En demencia, la neuroimagen ayuda a descartar causas tratables como hidrocefalia normotensiva.",
            },
            {
                "q": "\u00bfPuedo usar solo cuestionarios de funciones ejecutivas?",
                "a": "Los cuestionarios (p. ej., autorreporte) aportan percepci\u00f3n subjetiva pero no sustituyen pruebas performance-based para diagn\u00f3stico diferencial riguroso. Discrepancia entre queja subjetiva y prueba objetiva es dato cl\u00ednico relevante.",
            },
            {
                "q": "\u00bfC\u00f3mo evaluar pacientes con baja escolaridad?",
                "a": "Elija pruebas con menor carga verbal cuando sea posible, use normas que estratifican educaci\u00f3n y complemente con observaci\u00f3n funcional en actividades cotidianas. Evite conclusiones sobre demencia sin repetir evaluaci\u00f3n o incluir informante.",
            },
            {
                "q": "\u00bfLa evaluaci\u00f3n neuropsicol\u00f3gica diagnostica demencia?",
                "a": "Aporta evidencia de deterioro cognitivo y perfil compatible, pero el diagn\u00f3stico etiol\u00f3gico requiere integraci\u00f3n cl\u00ednica, imagen y laboratorios seg\u00fan neurolog\u00eda. El psic\u00f3logo describe patr\u00f3n cognitivo, no tipo exacto de demencia sin datos m\u00e9dicos.",
            },
        ],
        "related": [
            {"href": "/articulos/evaluacion-neuropsicologica-guia-clinica.html", "label": "Evaluaci\u00f3n neuropsicol\u00f3gica: gu\u00eda"},
            {"href": "/articulos/wisc-v-test-inteligencia-ninos.html", "label": "WISC-V: inteligencia infantil"},
            {"href": "/articulos/tdah-adultos.html", "label": "TDAH en adultos"},
            {"href": "/articulos/que-es-el-dsm-5.html", "label": "Qu\u00e9 es el DSM-5"},
        ],
    }
)

# --- 30 trastornos-personalidad-dsm5 ---
ARTICLES.append(
    {
        "slug": "trastornos-personalidad-dsm5",
        "title": "Trastornos de personalidad DSM-5: evaluaci\u00f3n cl\u00ednica | Kalyo",
        "description": "Trastornos de personalidad DSM-5: Cl\u00faster A/B/C, PID-5, SCID-5-PD, entrevista cl\u00ednica, diagn\u00f3stico diferencial y tratamiento para psic\u00f3logos en M\u00e9xico.",
        "keywords": "trastornos de personalidad DSM-5, PID-5, SCID-5, TLP, Cl\u00faster B, evaluaci\u00f3n personalidad, psicolog\u00eda cl\u00ednica, Criterios DSM-5",
        "h1": "Trastornos de personalidad en DSM-5: evaluaci\u00f3n cl\u00ednica",
        "breadcrumb_short": "Trastornos personalidad DSM-5",
        "hero_alt": "Evaluaci\u00f3n de trastornos de personalidad con entrevista cl\u00ednica y escalas DSM-5",
        "inline_alt": "Cl\u00fasteres A, B y C de trastornos de personalidad seg\u00fan DSM-5",
        "quick_answer": "Los <strong>trastornos de personalidad DSM-5</strong> son patrones persistentes de experiencia interna y conducta desviados, inflexibles y con malestar o deterioro, agrupados en Cl&uacute;ster A, B y C. La evaluaci&oacute;n combina entrevista estructurada (SCID-5-PD), medidas dimensionales como <a href=\"/articulos/pid-5-bf-personalidad-dsm5.html\">PID-5</a> e historia longitudinal.",
        "intro_long": "Los <strong>trastornos de personalidad</strong> generan consultas complejas: relaciones interpersonales ca&oacute;ticas, impulsividad, vac&iacute;o cr&oacute;nico o evitaci&oacute;n social extrema. El DSM-5 mantiene categor&iacute;as cl&iacute;nicas y propone alternativa dimensional basada en rasgos (Modelo de rasgos de personalidad patol&oacute;gica). En M&eacute;xico, el psic&oacute;logo debe evaluar con cautela, evitar etiquetas estigmatizantes prematuras y distinguir personalidad de cuadros epis&oacute;dicos (psicosis, man&iacute;a, TEPT). Esta gu&iacute;a resume Cl&uacute;steres A/B/C, instrumentos PID-5 y SCID-5, diferencial con trastorno l&iacute;mite y enfoques terap&eacute;uticos basados en evidencia para la pr&aacute;ctica cl&iacute;nica privada.",
        "meta_label": "Personalidad &middot; DSM-5 &middot; Evaluaci&oacute;n cl&iacute;nica &middot; 2026",
        "cta_h2": CTA_H2,
        "cta_p": CTA_P,
        "sections": [
            {
                "h2": "Modelo categ\u00f3rico DSM-5: Cl\u00faster A, B y C",
                "html": p(
                    "El DSM-5 describe diez trastornos espec&iacute;ficos agrupados en tres cl&uacute;steres. <strong>Cl&uacute;ster A</strong> (exc&eacute;ntrico): paranoide, esquizoide, esquizot&iacute;pico &mdash; patr&oacute;n de distanciamiento social y cogniciones/percepciones peculiares. <strong>Cl&uacute;ster B</strong> (dram&aacute;tico): antisocial, l&iacute;mite (<a href=\"/articulos/tlp-trastorno-limite.html\">TLP</a>), histri&oacute;nico, narcisista &mdash; impulsividad, labilidad emocional, inestabilidad relacional. <strong>Cl&uacute;ster C</strong> (ansioso): evitativo, dependiente, obsesivo-compulsivo de personalidad &mdash; miedo al rechazo, necesidad de cuidado o perfeccionismo r&iacute;gido.",
                    "Criterios generales exigen patr&oacute;n persistente (inicio adolescencia/adultez temprana), permeabilidad en m&uacute;ltiples contextos, malestar o deterioro y no atribuible a sustancias o condici&oacute;n m&eacute;dica. La evaluaci&oacute;n requiere historia longitudinal, no solo crisis actual.",
                    "Consulte el marco general en <a href=\"/articulos/que-es-el-dsm-5.html\">qu&eacute; es el DSM-5</a> para ubicar trastornos de personalidad respecto a otros cap&iacute;tulos diagn&oacute;sticos.",
                    "Explique al paciente que el diagn&oacute;stico describe patrones duraderos, no un veredicto sobre su car&aacute;cter; esto reduce resistencia en entrevistas largas de personalidad.",
                    "Al explicar Cl&uacute;ster B, enfatice que impulsividad o inestabilidad relacional pueden modificarse con tratamiento especializado; el diagn&oacute;stico abre acceso a intervenciones, no cierra posibilidades de cambio.",
                ),
            },
            {
                "h2": "Enfoque dimensional: rasgos PID-5 y AMPD",
                "html": p(
                    "El DSM-5 incluye en Secci&oacute;n III el <strong>Modelo Alternativo de Trastornos de Personalidad (AMPD)</strong> con criterios generales de personalidad patol&oacute;gica y cinco dominios de rasgos: afectividad negativa, desapego, antagonismo, desinhibici&oacute;n y psicoticismo. El <a href=\"/articulos/pid-5-bf-personalidad-dsm5.html\">PID-5-BF</a> (Inventario de Personalidad para el DSM-5, forma breve) mide estos rasgos dimensionalmente.",
                    "Ventaja dimensional: captura gradaciones y comorbilidad entre categor&iacute;as. Limitaci&oacute;n: normas y uso cl&iacute;nico requieren formaci&oacute;n; no reemplace entrevista. En investigaci&oacute;n y consultorios especializados, combinar PID-5 con SCID-5-PD enriquece perfil.",
                    "Interprete rasgos elevados en contexto cultural: antagonismo alto no equivale autom&aacute;ticamente a trastorno antisocial; explore funcionalidad y flexibilidad del patr&oacute;n.",
                    "El <a href=\"/articulos/pid-5-bf-personalidad-dsm5.html\">PID-5-BF</a> puede repetirse en seguimiento terap&eacute;utico para documentar cambio dimensional, no solo alivio sintom&aacute;tico epis&oacute;dico de depresi&oacute;n o ansiedad com&oacute;rbida.",
                )
                + """
<table class="items-table">
<thead><tr><th>Cl\u00faster</th><th>Trastornos</th><th>Tem\u00e1tica central</th></tr></thead>
<tbody>
<tr><td>A</td><td>Paranoide, esquizoide, esquizot\u00edpico</td><td>Extra\u00f1eza, aislamiento</td></tr>
<tr><td>B</td><td>Antisocial, l\u00edmite, histri\u00f3nico, narcisista</td><td>Impulsividad, dramatismo</td></tr>
<tr><td>C</td><td>Evitativo, dependiente, obsesivo-compulsivo</td><td>Miedo, rigidez</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "Evaluaci\u00f3n cl\u00ednica: entrevista SCID-5-PD y fuentes",
                "html": p(
                    "La entrevista semiestructurada <strong>SCID-5-PD</strong> eval&uacute;a criterios por trastorno con preguntas estandarizadas y probes cl&iacute;nicos. Requiere capacitaci&oacute;n. Complemente con historia desarrollo, relaciones significativas, patrones laborales, antecedentes legales (Cl&uacute;ster B) y respuesta previa a tratamientos.",
                    "Use informantes con consentimiento cuando el paciente minimiza conductas interpersonales. Compare autoimagen con relatos de pareja o familiares. Documente ejemplos conductuales concretos por criterio, no impresiones globales (&laquo;es dif&iacute;cil&raquo;).",
                    "Eval&uacute;e comorbilidades: depresi&oacute;n, TLP con consumo de sustancias, TEPT complejo, trastornos alimentarios. Diagn&oacute;sticos m&uacute;ltiples de personalidad son posibles si criterios completos y cl&iacute;nicamente relevantes.",
                    "Reserve tiempo suficiente: entrevistas SCID-5-PD fragmentadas en dos sesiones reducen fatiga del paciente y mejoran calidad de ejemplos conductuales.",
                    "Revise historial de hospitalizaciones psiqui&aacute;tricas, intentos suicidas y tratamientos previos antes de cerrar diagn&oacute;stico de personalidad; estos datos contextualizan severidad actual.",
                ),
            },
            {
                "h2": "Diagn\u00f3stico diferencial y timing diagn\u00f3stico",
                "html": p(
                    "No diagnostique trastorno de personalidad en episodio depresivo mayor agudo, intoxicaci&oacute;n, psicosis activa o TEPT no estabilizado sin historia previa clara. Adolescentes requieren cautela: rasgos normativos pueden simular trastorno; espere persistencia m&aacute;s all&aacute; de desarrollo esperado.",
                    "Diferencie TLP de trastorno bipolar (episodios definidos con remisi&oacute;n), TEA (d&eacute;ficits sociales desde infancia temprana), trastorno por estr&eacute;s agudo y personalidad evitativa de fobia social severa. Narcisismo patol&oacute;gico vs rasgos adaptativos de liderazgo exige evaluaci&oacute;n de fragilidad del yo y respuesta a cr&iacute;tica.",
                    "Documente nivel de funcionamiento global (escala WHODAS o equivalente) para planificar intensidad de tratamiento.",
                    "En <a href=\"/articulos/tlp-trastorno-limite.html\">trastorno l&iacute;mite</a>, eval&uacute;e siempre riesgo suicida y autolesiones antes de profundizar en historia de apego.",
                    "Considere evaluaci&oacute;n de rasgos con <a href=\"/articulos/pid-5-bf-personalidad-dsm5.html\">PID-5-BF</a> cuando el perfil categ&oacute;rico resulte mixto o subcl&iacute;nico pero funcionalmente relevante.",
                ),
            },
            {
                "h2": "Tratamiento psicol\u00f3gico basado en evidencia",
                "html": p(
                    "TLP: DBT, TFP, MBT seg&uacute;n acceso. Trastorno evitativo: TCC con exposici&oacute;n gradual social. Obsesivo-compulsivo de personalidad: TCC enfocada en flexibilidad y perfeccionismo, distinto de TOC. Antisocial: intervenciones limitadas en insight; enfoque en reducci&oacute;n de daño y contenci&oacute;n legal cuando aplique.",
                    "En Cl&uacute;ster C, psicoeducaci&oacute;n sobre tolerancia a la incertidumbre reduce evitaci&oacute;n laboral. En Cl&uacute;ster A, metas graduales de interacci&oacute;n social suelen ser m&aacute;s &uacute;tiles que confrontar creencias paranoides de forma directa.",
                    "Psicoterapias de personalidad son de largo plazo; acuerde metas realistas (reducir autolesiones, mejorar relaciones laborales estables). Farmacoterapia no cura personalidad pero psiquiatr&iacute;a puede tratar comorbilidades (ISRS para ansiedad en evitativo).",
                    "Supervisi&oacute;n cl&iacute;nica obligatoria por intensidad contratransferencial. Registre planes de seguridad en TLP con riesgo suicida. {kalyo} ayuda a documentar objetivos terap&eacute;uticos, escalas PID-5 repetidas y acuerdos de l&iacute;mites entre sesiones.".format(
                        kalyo=KALYO
                    ),
                    "Acuerde metas conductuales observables (frecuencia de conflictos laborales, episodios de autolesi&oacute;n, d&iacute;as de aislamiento) adem&aacute;s de metas subjetivas de bienestar.",
                    "Coordine con psiquiatr&iacute;a cuando hay indicaci&oacute;n de psicof&aacute;rmacos para comorbilidad afectiva; el psic&oacute;logo monitoriza adherencia, efectos sobre impulsividad y continuidad de psicoterapia de personalidad.",
                ),
            },
            {
                "h2": "\u00c9tica, estigma e informes cl\u00ednicos",
                "html": p(
                    "Evite usar diagn&oacute;sticos de personalidad como descalificaci&oacute;n moral. En informes periciales, describa conductas observables y criterios cumplidos, impacto funcional y recomendaciones de tratamiento. Informe al paciente diagn&oacute;stico con lenguaje comprensible y enfoque en posibilidades de cambio (plasticidad en rasgos con intervención sostenida).",
                    "Confidencialidad reforzada: etiquetas mal interpretadas da&ntilde;an empleo o custodia. Divulgue solo con consentimiento o mandato legal. En M&eacute;xico, respete marco de salud mental y derechos del paciente en instituciones p&uacute;blicas con recursos limitados.",
                    "Actualice diagn&oacute;stico si tras a&ntilde;os de tratamiento el patr&oacute;n ya no causa deterioro significativo; algunos pacientes ya no cumplen criterios plenos aunque mantengan rasgos subcl&iacute;nicos.",
                    "En peritajes, distinga rasgos de personalidad de conductas puntuales ligadas a intoxicaci&oacute;n o situaci&oacute;n legal estresante; evite conclusiones definitivas con una sola entrevista.",
                    "Forme al paciente en lectura de resultados PID-5 cuando se use seguimiento dimensional; comprender rasgos facilita adherencia a metas terap&eacute;uticas espec&iacute;ficas por dominio.",
                    "En instituciones p&uacute;blicas mexicanas con alta rotaci&oacute;n de terapeutas, un expediente estructurado con diagn&oacute;stico de personalidad bien documentado reduce reevaluaciones redundantes y protege continuidad asistencial del paciente.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfCu\u00e1ntos trastornos de personalidad hay en DSM-5?",
                "a": "Diez trastornos espec\u00edficos en el modelo categ\u00f3rico (paranoide, esquizoide, esquizot\u00edpico, antisocial, l\u00edmite, histri\u00f3nico, narcisista, evitativo, dependiente y obsesivo-compulsivo de personalidad). El modelo alternativo en Secci\u00f3n III usa rasgos transdiagn\u00f3sticos que pueden complementar, no reemplazar, la entrevista cl\u00ednica.",
            },
            {
                "q": "\u00bfPID-5 diagnostica trastorno de personalidad solo?",
                "a": "No. PID-5 mide rasgos dimensionales compatibles con el modelo alternativo DSM-5. El diagn\u00f3stico categ\u00f3rico requiere entrevista cl\u00ednica estructurada, historia longitudinal e integraci\u00f3n de impacto funcional.",
            },
            {
                "q": "\u00bfSe puede diagnosticar TLP antes de los 18 a\u00f1os?",
                "a": "DSM-5 permite TLP antes de 18 a\u00f1os si s\u00edntomas son persistentes al menos un a\u00f1o y cl\u00ednicamente significativos, con cautela diagn\u00f3stica. Diferencie inestabilidad evolutiva normativa de patr\u00f3n persistente.",
            },
            {
                "q": "\u00bfLos trastornos de personalidad son tratables?",
                "a": "S\u00ed, parcialmente. Evidencia robusta para DBT en TLP y TCC en otros cuadros. Cambio requiere tiempo, alianza terap\u00e9utica estable y a menudo tratamiento especializado de varios a\u00f1os; las metas deben ser funcionales y revisables trimestralmente con el paciente.",
            },
            {
                "q": "\u00bfSCID-5-PD est\u00e1 disponible en espa\u00f1ol?",
                "a": "Existen versiones traducidas y adaptaciones; verifique edici\u00f3n autorizada y capacitaci\u00f3n del aplicador antes de uso cl\u00ednico o pericial. Documente versi\u00f3n, fecha y duraci\u00f3n de la entrevista en el informe psicol\u00f3gico final.",
            },
        ],
        "related": [
            {"href": "/articulos/pid-5-bf-personalidad-dsm5.html", "label": "PID-5: rasgos de personalidad DSM-5"},
            {"href": "/articulos/tlp-trastorno-limite.html", "label": "TLP: trastorno l\u00edmite de personalidad"},
            {"href": "/articulos/scid-5-entrevista-clinica.html", "label": "SCID-5: entrevista cl\u00ednica estructurada"},
            {"href": "/articulos/que-es-el-dsm-5.html", "label": "Qu\u00e9 es el DSM-5"},
        ],
    }
)

if __name__ == "__main__":
    for spec in ARTICLES:
        tl = len(spec["title"])
        dl = len(spec["description"])
        qa_w = wc(spec["quick_answer"])
        il_w = wc(spec["intro_long"])
        bw = body_words(spec)
        print(
            f"{spec['slug']}: title={tl} desc={dl} quick={qa_w} intro={il_w} body={bw}"
        )
