#!/usr/bin/env python3
"""Batch 9 part 3: clinical SEO article specs (articles 31-35)."""
from __future__ import annotations

import json
import re

KALYO = '<a href="https://app.kalyo.io/register">Kalyo</a>'


def wc(text: str) -> int:
    t = re.sub(r"<[^>]+>", " ", text)
    return len(re.sub(r"\s+", " ", t).strip().split())


def body_words(spec: dict) -> int:
    parts = [spec.get("intro_long") or spec.get("intro", "")]
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
    qw = wc(spec["quick_answer"])
    if not (40 <= qw <= 60):
        raise ValueError(f"{slug} quick_answer words {qw}")
    bw = body_words(spec)
    if bw < 1200:
        raise ValueError(f"{slug} body words {bw} < 1200")
    if kalyo_count(spec) != 1:
        raise ValueError(f"{slug} kalyo links {kalyo_count(spec)}")
    if len(spec["sections"]) != 6:
        raise ValueError(f"{slug} sections {len(spec['sections'])}")
    if len(spec["faqs"]) != 5:
        raise ValueError(f"{slug} faqs {len(spec['faqs'])}")
    if len(spec["related"]) != 4:
        raise ValueError(f"{slug} related {len(spec['related'])}")


CTA_H2 = "Gestiona el expediente de tus pacientes con Kalyo"
CTA_P = (
    "Centraliza consentimientos, notas de evoluci&oacute;n, planes de tratamiento "
    "y resultados psicom&eacute;tricos en un expediente cl&iacute;nico seguro. "
    "Conoce m&aacute;s en <a href=\"https://kalyo.io\">kalyo.io</a>."
)

ARTICLES: list[dict] = []

# --- 31 consentimiento-informado-psicologia-mexico ---
ARTICLES.append(
    {
        "slug": "consentimiento-informado-psicologia-mexico",
        "title": "Consentimiento informado psicolog\u00eda cl\u00ednica M\u00e9xico | Kalyo",
        "description": "Consentimiento informado psicolog\u00eda M\u00e9xico: NOM-004, C\u00f3digo de \u00c9tica, menores, teleconsulta y registro en expediente cl\u00ednico para psic\u00f3logos en consulta.",
        "keywords": "consentimiento informado psicolog\u00eda M\u00e9xico, NOM-004, C\u00f3digo de \u00c9tica, expediente cl\u00ednico, teleconsulta, LFPDPPP, psicolog\u00eda cl\u00ednica",
        "h1": "Consentimiento informado en psicolog\u00eda M\u00e9xico: gu\u00eda cl\u00ednica y legal",
        "breadcrumb_short": "Consentimiento informado M\u00e9xico",
        "hero_alt": "Psic\u00f3logo explicando consentimiento informado a paciente en consulta privada en M\u00e9xico",
        "inline_alt": "Elementos esenciales del consentimiento informado seg\u00fan NOM-004 y \u00e9tica profesional",
        "quick_answer": "El consentimiento informado en psicolog\u00eda M\u00e9xico es el acuerdo libre, previo y documentado mediante el cual el paciente autoriza la evaluaci\u00f3n o tratamiento psicol\u00f3gico tras conocer finalidad, riesgos, beneficios, alternativas, confidencialidad y derecho a revocar. Debe registrarse en el expediente cl\u00ednico conforme a la NOM-004 y al C\u00f3digo de \u00c9tica.",
        "intro_long": "El <strong>consentimiento informado psicolog\u00eda M\u00e9xico</strong> no es un tr\u00e1mite burocr\u00e1tico: es el fundamento \u00e9tico y legal de toda intervenci\u00f3n cl\u00ednica. La <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> exige que el expediente documente la aceptaci\u00f3n del paciente para actos de atenci\u00f3n; el C\u00f3digo de \u00c9tica del psic\u00f3logo mexicano refuerza autonom\u00eda, veracidad y confidencialidad. En consulta privada, institucional o <a href=\"/articulos/teleconsulta-psicologos.html\">teleconsulta</a>, el documento debe ser comprensible, adaptado al nivel educativo del consultante y actualizable cuando cambien procedimientos, honorarios o modalidad. Este art\u00edculo orienta qu\u00e9 incluir, c\u00f3mo obtenerlo en menores o situaciones de riesgo y c\u00f3mo archivarlo junto con la historia cl\u00ednica sin confundirlo con un contrato comercial.",
        "meta_label": "Documentaci&oacute;n cl&iacute;nica &middot; M&eacute;xico &middot; Actualizaci&oacute;n 2026",
        "sections": [
            {
                "h2": "Qu\u00e9 es el consentimiento informado en psicolog\u00eda M\u00e9xico",
                "html": p(
                    "El consentimiento informado es el proceso mediante el cual una persona, con capacidad jur\u00eddica y tras recibir informaci\u00f3n adecuada, autoriza de forma libre la evaluaci\u00f3n psicol\u00f3gica, el tratamiento o procedimientos espec\u00edficos (aplicaci\u00f3n de pruebas, grabaci\u00f3n de sesi\u00f3n, contacto con terceros). Implica <strong>informaci\u00f3n</strong>, <strong>comprensi\u00f3n</strong>, <strong>voluntariedad</strong> y <strong>documentaci\u00f3n</strong>. En psicolog\u00eda cl\u00ednica no se trata solo de firmar un papel: incluye resolver dudas, verificar que el paciente entiende l\u00edmites de confidencialidad y confirmar que no hay coerci\u00f3n.",
                    "En M\u00e9xico, la pr\u00e1ctica psicol\u00f3gica se rige por la Ley General de Salud, la NOM-004-SSA3-2012 sobre expediente cl\u00ednico, la LFPDPPP cuando se tratan datos personales sensibles, y el C\u00f3digo de \u00c9tica profesional. El consentimiento respalda la relaci\u00f3n terap\u00e9utica y protege al profesional ante auditor\u00edas, quejas o litigios, siempre que refleje un proceso real y no una firma obtenida apresuradamente al final de la primera cita.",
                    "Diferencie consentimiento general para el proceso psicoterap\u00e9utico de consentimientos espec\u00edficos: evaluaci\u00f3n psicom\u00e9trica, informes periciales, participaci\u00f3n en investigaci\u00f3n, comunicaci\u00f3n con escuela o empleador, o uso de inteligencia artificial para transcripci\u00f3n de notas. Cada uno requiere explicaci\u00f3n propia porque implica riesgos y usos distintos de la informaci\u00f3n.",
                )
                + """
<ul>
<li><strong>Evaluaci&oacute;n inicial:</strong> autoriza entrevista, pruebas y contacto con informantes si aplica.</li>
<li><strong>Tratamiento:</strong> modalidad, frecuencia, honorarios, pol&iacute;tica de cancelaci&oacute;n.</li>
<li><strong>Procedimientos espec&iacute;ficos:</strong> grabaci&oacute;n, teleconsulta, informes a terceros.</li>
</ul>""",
            },
            {
                "h2": "Marco legal: NOM-004, C\u00f3digo de \u00c9tica y protecci\u00f3n de datos",
                "html": p(
                    "La <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> establece que el expediente cl\u00ednico debe contener documentos que acrediten la relaci\u00f3n m\u00e9dica o de atenci\u00f3n a la salud, incluida la aceptaci\u00f3n del paciente para procedimientos cuando la norma o la pr\u00e1ctica cl\u00ednica lo requieran. Para psicolog\u00eda, esto se traduce en conservar el consentimiento firmado o aceptado digitalmente, con fecha, identificaci\u00f3n del profesional y descripci\u00f3n clara del servicio.",
                    "El C\u00f3digo de \u00c9tica del psic\u00f3logo obliga a respetar la autonom\u00eda del consultante, proporcionar informaci\u00f3n veraz sobre la naturaleza de la intervenci\u00f3n y mantener confidencialidad salvo excepciones legales (riesgo grave para la vida, abuso a menores, orden judicial). La LFPDPPP exige aviso de privacidad cuando se recaban datos personales; en consultorios privados suele integrarse al consentimiento o presentarse como documento complementario.",
                    "No confunda el consentimiento cl\u00ednico con contratos civiles de prestaci\u00f3n de servicios. Ambos pueden coexistir, pero el primero enfatiza derechos del paciente y naturaleza de la intervenci\u00f3n; el segundo, obligaciones comerciales. En instituciones p\u00fablicas, revisar tambi\u00e9n manuales internos y lineamientos de la Secretar\u00eda de Salud estatal.",
                ),
            },
            {
                "h2": "Elementos obligatorios del documento de consentimiento",
                "html": p(
                    "Un consentimiento informado psicol\u00f3gico completo en M\u00e9xico suele incluir: identificaci\u00f3n del profesional (nombre, c\u00e9dula profesional, domicilio del consultorio); descripci\u00f3n del servicio (evaluaci\u00f3n, psicoterapia individual, familiar, etc.); finalidad y alcance; duraci\u00f3n estimada o criterios de alta; honorarios y forma de pago; pol\u00edtica de cancelaci\u00f3n; confidencialidad y <strong>l\u00edmites legales</strong> (menores en riesgo, violencia, mandato judicial); riesgos razonables (malestar emocional al explorar temas dif\u00edciles, no cura garantizada); beneficios esperados; alternativas (otro enfoque terap\u00e9utico, no tratamiento, derivaci\u00f3n); derecho a revocar consentimiento y consecuencias pr\u00e1cticas; contacto de emergencia.",
                    "Redacte en lenguaje claro, evitando jerga innecesaria. Si el paciente no domina el espa\u00f1ol, use int\u00e9rprete calificado y documente el idioma utilizado. Para procedimientos de evaluaci\u00f3n, mencione qu\u00e9 pruebas se aplicar\u00e1n, para qu\u00e9 se usar\u00e1n los resultados y qui\u00e9n tendr\u00e1 acceso. Vincule con la gu\u00eda general de <a href=\"/articulos/consentimiento-informado-psicologia.html\">consentimiento informado en psicolog\u00eda</a> si necesita plantillas base adaptables.",
                    "Incluya espacio para firma del paciente o representante legal, firma del psic\u00f3logo y fecha. En formato digital, registro de aceptaci\u00f3n con timestamp, IP o verificaci\u00f3n de identidad seg\u00fan el nivel de riesgo del servicio.",
                )
                + """
<ol>
<li>Identificaci&oacute;n del profesional y del consultante.</li>
<li>Descripci&oacute;n comprensible del procedimiento o tratamiento.</li>
<li>Riesgos, beneficios, alternativas y l&iacute;mites de confidencialidad.</li>
<li>Derecho a preguntar, negarse o revocar autorizaci&oacute;n.</li>
<li>Firmas, fecha y copia para el paciente cuando lo solicite.</li>
</ol>""",
            },
            {
                "h2": "Menores, tutores y situaciones con capacidad reducida",
                "html": p(
                    "En menores de edad, quien otorga el consentimiento suele ser el padre, madre o tutor con patria potestad, seg\u00fan el C\u00f3digo Civil y la legislaci\u00f3n de salud aplicable. Adem\u00e1s, conforme a la madurez del menor, conviene obtener su <strong>asentimiento</strong> (assent) explicando en t\u00e9rminos adecuados a su edad qu\u00e9 ocurrir\u00e1 en la consulta. En adolescentes, forzar procesos sin escucha activa da\u00f1a la alianza terap\u00e9utica.",
                    "Si hay discrepancia entre custodios, documente intentos de coordinaci\u00f3n y consulte asesor\u00eda legal antes de iniciar tratamiento sin acuerdo. En adultos con discapacidad intelectual o demencia, eval\u00fae capacidad para consentir el procedimiento espec\u00edfico; puede requerirse representante legal. En emergencias psiqui\u00e1tricas con riesgo vital, la normativa permite actuaci\u00f3n sin consentimiento previo, pero debe documentarse la justificaci\u00f3n y obtener ratificaci\u00f3n posterior cuando sea posible.",
                    "Situaciones de violencia intrafamiliar exigen cuidado: obtener consentimiento del agresor para tratar a la v\u00edctima puede poner en riesgo a la persona. Priorice protocolos de seguridad, derivaci\u00f3n a redes especializadas y cumplimiento del deber de reporte cuando la ley lo exija.",
                ),
            },
            {
                "h2": "Consentimiento en teleconsulta y formato digital",
                "html": p(
                    "La <a href=\"/articulos/teleconsulta-psicologos.html\">teleconsulta psicol\u00f3gica</a> requiere consentimiento espec\u00edfico: modalidad a distancia, plataforma utilizada, medidas de confidencialidad (conexi\u00f3n privada, uso de auriculares), riesgos de interceptaci\u00f3n t\u00e9cnica, ubicaci\u00f3n del paciente en caso de emergencia y plan si se pierde la conexi\u00f3n. Informe si las sesiones se graban (por defecto no deber\u00edan sin consentimiento aparte).",
                    "La firma electr\u00f3nica o aceptaci\u00f3n mediante checkbox en plataforma v\u00e1lida debe archivarse en el expediente junto con el aviso de privacidad. Verifique identidad del consultante en primera sesi\u00f3n (identificaci\u00f3n oficial, c\u00f3digo enviado al correo registrado). Revise t\u00e9rminos del proveedor de videollamada respecto a almacenamiento de datos.",
                    "Si utiliza herramientas de transcripci\u00f3n o IA para notas cl\u00ednicas, el paciente debe autorizar expresamente el procesamiento de su voz o contenido de sesi\u00f3n, con opci\u00f3n de rechazar sin que ello impida la atenci\u00f3n presencial convencional cuando est\u00e9 disponible.",
                ),
            },
            {
                "h2": "Registro, actualizaci\u00f3n y archivo en el expediente cl\u00ednico",
                "html": p(
                    "Archive el consentimiento en el expediente desde la primera sesi\u00f3n. Actualice cuando cambien honorarios sustancialmente, se incorporen pruebas psicom\u00e9tricas, se solicite informe pericial o se pase de presencial a teleconsulta. La revocaci\u00f3n del consentimiento para tratamiento implica cesar la intervenci\u00f3n salvo obligaci\u00f3n legal; documente fecha y motivo.",
                    "Conserve originales o copias certificadas seg\u00fan pol\u00edtica del consultorio; la NOM-004 define tiempos de conservaci\u00f3n del expediente. Facilite al paciente copia del consentimiento si la solicita. En auditor\u00edas o quejas ante el colegio profesional, un expediente ordenado con consentimientos fechados demuestra diligencia \u00e9tica.",
                    "Plataformas como {kalyo} permiten almacenar consentimientos firmados digitalmente, vincularlos a la ficha del paciente y recibir aceptaci\u00f3n antes de la primera cita en l\u00ednea, reduciendo omisiones administrativas sin sustituir la explicaci\u00f3n cl\u00ednica cara a cara.".format(
                        kalyo=KALYO
                    ),
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfEl consentimiento informado es obligatorio en psicolog\u00eda privada en M\u00e9xico?",
                "a": "S\u00ed. Es exigencia \u00e9tica del C\u00f3digo de \u00c9tica y buena pr\u00e1ctica cl\u00ednica respaldada por la NOM-004 para documentar la relaci\u00f3n de atenci\u00f3n. Operar sin consentimiento expone a sanciones profesionales y dificulta la defensa ante quejas.",
            },
            {
                "q": "\u00bfPuede firmar un solo padre si hay custodia compartida?",
                "a": "Idealmente ambos titulares de la patria potestad deben autorizar tratamiento en menores. Si solo uno firma, documente el intento de contacto con el otro progenitor y eval\u00fce riesgos legales antes de iniciar.",
            },
            {
                "q": "\u00bfEl consentimiento cubre compartir informes con terceros?",
                "a": "No autom\u00e1ticamente. Emitir informes a escuela, empresa o juzgado requiere autorizaci\u00f3n espec\u00edfica que indique destinatario, alcance y prop\u00f3sito, salvo mandato judicial.",
            },
            {
                "q": "\u00bfC\u00f3mo revocar el consentimiento un paciente?",
                "a": "Por escrito o declaraci\u00f3n expresa en sesi\u00f3n, documentada en nota de evoluci\u00f3n. Cese procedimientos no urgentes; conserve el expediente seg\u00fan plazos legales de conservaci\u00f3n.",
            },
            {
                "q": "\u00bfEs v\u00e1lido el consentimiento por WhatsApp o correo?",
                "a": "Puede servir como evidencia complementaria si incluye identificaci\u00f3n verificable y texto claro, pero se recomienda formato estructurado firmado o aceptaci\u00f3n en plataforma cl\u00ednica que registre fecha y versi\u00f3n del documento.",
            },
        ],
        "related": [
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004: historia cl\u00ednica en M\u00e9xico"},
            {"href": "/articulos/consentimiento-informado-psicologia.html", "label": "Consentimiento informado en psicolog\u00eda"},
            {"href": "/articulos/teleconsulta-psicologos.html", "label": "Teleconsulta para psic\u00f3logos"},
            {"href": "/articulos/software-para-psicologos-clinicos.html", "label": "Software para psic\u00f3logos cl\u00ednicos"},
        ],
        "cta_h2": CTA_H2,
        "cta_p": CTA_P,
    }
)

# --- 32 nota-evolucion-psicologica ---
ARTICLES.append(
    {
        "slug": "nota-evolucion-psicologica",
        "title": "Nota evoluci\u00f3n psicol\u00f3gica: gu\u00eda cl\u00ednica y formato | Kalyo",
        "description": "Nota de evoluci\u00f3n psicol\u00f3gica: estructura SOAP, redacci\u00f3n objetiva, NOM-004, frecuencia de registro y buenas pr\u00e1cticas para psic\u00f3logos en M\u00e9xico y LATAM hoy.",
        "keywords": "nota de evoluci\u00f3n psicol\u00f3gica, SOAP, expediente cl\u00ednico, NOM-004, historia cl\u00ednica, documentaci\u00f3n psicol\u00f3gica, psicolog\u00eda cl\u00ednica",
        "h1": "Nota de evoluci\u00f3n psicol\u00f3gica: c\u00f3mo redactarla en la pr\u00e1ctica cl\u00ednica",
        "breadcrumb_short": "Nota de evoluci\u00f3n psicol\u00f3gica",
        "hero_alt": "Psic\u00f3logo redactando nota de evoluci\u00f3n psicol\u00f3gica tras sesi\u00f3n cl\u00ednica",
        "inline_alt": "Estructura SOAP aplicada a la nota de evoluci\u00f3n en psicolog\u00eda cl\u00ednica",
        "quick_answer": "La nota de evoluci\u00f3n psicol\u00f3gica es el registro peri\u00f3dico de cada sesi\u00f3n o contacto cl\u00ednico: motivo de consulta del d\u00eda, intervenciones realizadas, respuesta del paciente, evaluaci\u00f3n cl\u00ednica y plan. Debe ser objetiva, fechada, firmada y conservarse en el expediente conforme a la NOM-004 y est\u00e1ndares \u00e9ticos.",
        "intro_long": "La <strong>nota de evoluci\u00f3n psicol\u00f3gica</strong> es el hilo conductor del tratamiento: documenta qu\u00e9 ocurri\u00f3 en cada encuentro, permite continuidad entre profesionales y sustenta decisiones cl\u00ednicas futuras. En M\u00e9xico, la <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> exige registros cronol\u00f3gicos en el expediente; en Colombia y otros pa\u00edses de LATAM existen requisitos similares de trazabilidad. Una nota bien escrita equilibra brevedad y contenido cl\u00ednico \u00fatil, evita juicios morales y protege al paciente y al psic\u00f3logo. Este art\u00edculo describe estructura SOAP adaptada, diferencias con la nota de primera vez, criterios de calidad y c\u00f3mo integrar la documentaci\u00f3n en un flujo digital con <a href=\"/articulos/software-para-psicologos-clinicos.html\">software cl\u00ednico</a>.",
        "meta_label": "Documentaci&oacute;n cl&iacute;nica &middot; Gu&iacute;a pr&aacute;ctica &middot; 2026",
        "sections": [
            {
                "h2": "Qu\u00e9 es una nota de evoluci\u00f3n psicol\u00f3gica",
                "html": p(
                    "La nota de evoluci\u00f3n psicol\u00f3gica registra un contacto asistencial puntual: sesi\u00f3n individual, familiar, entrevista breve telef\u00f3nica cl\u00ednicamente relevante o intervenci\u00f3n en crisis documentada. A diferencia del informe psicol\u00f3gico integral, no sintetiza todo el caso; captura el estado y los eventos del d\u00eda. Debe incluir fecha, hora, modalidad (presencial o teleconsulta), identificaci\u00f3n del paciente, n\u00famero de sesi\u00f3n si aplica, contenido cl\u00ednico esencial y firma del profesional.",
                    "Funciones cl\u00ednicas: memoria del proceso terap\u00e9utico, comunicaci\u00f3n con otros integrantes del equipo (psiquiatr\u00eda, trabajo social), base para supervisi\u00f3n y evidencia de diligencia ante auditor\u00edas. Una nota incompleta o gen\u00e9rica (\u00abse trabaj\u00f3 ansiedad\u00bb) dificulta evaluar avance, justificar cambios de plan o responder a solicitudes legales.",
                    "En instituciones, suelen existir formatos institucionales; en consulta privada, el psic\u00f3logo define plantilla propia siempre que cumpla elementos m\u00ednimos legales y \u00e9ticos. La consistencia entre sesiones mejora la calidad del expediente m\u00e1s que la extensi\u00f3n excesiva.",
                ),
            },
            {
                "h2": "Diferencia con nota de primera vez, interconsulta e informe",
                "html": p(
                    "La <strong>nota de primera vez</strong> o historia cl\u00ednica inicial recoge motivo de consulta, antecedentes, exploraci\u00f3n ps\u00edquica completa, hip\u00f3tesis diagn\u00f3stica preliminar, plan de tratamiento y consentimiento. Es m\u00e1s extensa y se elabora una vez (con actualizaciones puntuales). La nota de evoluci\u00f3n es sucesiva y m\u00e1s breve.",
                    "La <strong>nota de interconsulta</strong> documenta contacto con otro profesional o servicio: motivo de derivaci\u00f3n, informaci\u00f3n compartida con consentimiento, respuesta recibida. El <strong>informe psicol\u00f3gico</strong>, descrito en <a href=\"/articulos/como-redactar-informe-psicologico.html\">c\u00f3mo redactar informe psicol\u00f3gico</a>, sintetiza evaluaci\u00f3n o trayectoria para un destinatario espec\u00edfico (escuela, juzgado, aseguradora). No confunda evoluci\u00f3n con informe: la primera es registro interno de sesi\u00f3n; el segundo, producto formal con estructura propia.",
                    "En urgencias psicol\u00f3gicas, puede existir nota de ingreso o de egreso; la evoluci\u00f3n diaria sigue la misma l\u00f3gica cronol\u00f3gica pero en contexto hospitalario.",
                )
                + """
<ul>
<li><strong>Primera vez:</strong> panorama completo e hip&oacute;tesis inicial.</li>
<li><strong>Evoluci&oacute;n:</strong> sesi&oacute;n concreta y plan inmediato.</li>
<li><strong>Informe:</strong> s&iacute;ntesis para tercero autorizado.</li>
</ul>""",
            },
            {
                "h2": "Estructura SOAP y campos cl\u00ednicos esenciales",
                "html": p(
                    "El formato SOAP (Subjetivo, Objetivo, An\u00e1lisis, Plan) se adapta bien a psicolog\u00eda cl\u00ednica. <strong>Subjetivo:</strong> motivo de la sesi\u00f3n en palabras del paciente, eventos relevantes desde la \u00faltima cita, estado de \u00e1nimo referido. <strong>Objetivo:</strong> observaciones del terapeuta (apariencia, contacto, afecto, pensamiento, conducta en sesi\u00f3n), resultados de escalas aplicadas ese d\u00eda si las hubo. <strong>An\u00e1lisis:</strong> formulaci\u00f3n breve, progreso respecto a objetivos del plan de tratamiento, factores que facilitan o obstaculizan. <strong>Plan:</strong> intervenciones acordadas, tareas para casa, pr\u00f3xima cita, derivaciones o ajustes de frecuencia.",
                    "Evite copiar literalmente horas de conversaci\u00f3n; registre contenido cl\u00ednicamente significativo. Si se abordaron temas de riesgo (ideaci\u00f3n suicida, violencia), documente evaluaci\u00f3n, acuerdos de seguridad y contactos de emergencia activados. En menores, indique qui\u00e9n asisti\u00f3 y si hubo segmento individual.",
                    "Para teleconsulta, anote modalidad, confirmaci\u00f3n de ubicaci\u00f3n del paciente y cualquier limitaci\u00f3n t\u00e9cnica que haya afectado la evaluaci\u00f3n (conexi\u00f3n inestable, interrupciones).",
                ),
            },
            {
                "h2": "Criterios de calidad y redacci\u00f3n objetiva",
                "html": p(
                    "Use lenguaje descriptivo, no interpretativo prematuro: \u00abel paciente report\u00f3 insomnio de cinco d\u00edas\u00bb en lugar de \u00abmanipula para llamar atenci\u00f3n\u00bb. Evite estigmatizar, juzgar o incluir datos irrelevantes (opiniones pol\u00edticas del paciente sin nexo cl\u00ednico). Corrija errores sin borrar notas previas: en sistemas digitales, use addendum fechado; en papel, tachaduras legibles con firma y fecha.",
                    "Cada nota debe permitir responder: \u00bfQu\u00e9 se hizo hoy? \u00bfCu\u00e1l fue la respuesta del paciente? \u00bfQu\u00e9 sigue? Incluya n\u00famero de sesi\u00f3n cuando el tratamiento es por paquete o protocolo. Si no asisti\u00f3, registre inasistencia, si hubo aviso, pol\u00edtica aplicada y intento de contacto (sin violar privacidad en mensajes).",
                    "La calidad mejora con revisi\u00f3n peri\u00f3dica en supervisi\u00f3n cl\u00ednica: \u00bfLas notas reflejan el plan de tratamiento? \u00bfHay lagunas en evaluaci\u00f3n de riesgo? \u00bfSe documentan contactos con otros profesionales?",
                ),
            },
            {
                "h2": "Frecuencia, NOM-004 y continuidad asistencial",
                "html": p(
                    "Registre una nota de evoluci\u00f3n por cada sesi\u00f3n cl\u00ednica atendida, idealmente el mismo d\u00eda o dentro de las 24 horas siguientes mientras el recuerdo es fresco. Retrasos prolongados producen notas vagas y vulneran est\u00e1ndares institucionales. La <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> exige que las notas sean cronol\u00f3gicas, legibles, identificadas y conservadas durante el plazo establecido.",
                    "En tratamientos semanales, la sucesi\u00f3n de notas muestra curso del cuadro, adherencia a tareas, respuesta a intervenciones y eventos cr\u00edticos (p\u00e9rdida laboral, reca\u00edda en consumo, hospitalizaci\u00f3n). Facilita transiciones cuando otro colega cubre vacaciones o el paciente cambia de terapeuta con consentimiento.",
                    "Si aplica escalas repetidas (PHQ-9, GAD-7), registre puntaje del d\u00eda y comente tendencia en el apartado de an\u00e1lisis, vinculando con objetivos terap\u00e9uticos medibles.",
                ),
            },
            {
                "h2": "Documentaci\u00f3n digital, trazabilidad y expediente cl\u00ednico",
                "html": p(
                    "Los expedientes digitales permiten plantillas SOAP, bloqueo tras firma, historial de cambios y b\u00fasqueda por fechas. Asegure respaldo, control de acceso y cifrado conforme a aviso de privacidad. En <a href=\"/articulos/teleconsulta-psicologos.html\">teleconsulta</a>, la nota debe indicar que la sesi\u00f3n fue a distancia y cumpli\u00f3 consentimiento vigente.",
                    "Vincule cada nota al plan de tratamiento activo: objetivos, t\u00e9cnicas pactadas, criterios de alta. Cuando el caso requiera informe externo, las evoluciones ser\u00e1n la fuente primaria para redactarlo con precisi\u00f3n.",
                    "Herramientas como {kalyo} agilizan la redacci\u00f3n con plantillas cl\u00ednicas, registro de sesiones y vinculaci\u00f3n al expediente completo, manteniendo trazabilidad sin sustituir el criterio profesional del contenido.".format(
                        kalyo=KALYO
                    ),
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfCu\u00e1nto debe medir una nota de evoluci\u00f3n psicol\u00f3gica?",
                "a": "Suele ocupar medio parrafo por apartado SOAP en casos rutinarios; sesiones de crisis o evaluaci\u00f3n de riesgo requieren m\u00e1s detalle. Priorice contenido cl\u00ednico \u00fatil sobre extensi\u00f3n fija.",
            },
            {
                "q": "\u00bfDebo registrar verbatim lo que dice el paciente?",
                "a": "No es obligatorio ni recomendable en sesiones rutinarias. Capture citas breves cuando sean cl\u00ednicamente decisivas; por lo dem\u00e1s, parafrasee con fidelidad.",
            },
            {
                "q": "\u00bfQu\u00e9 pasa si olvid\u00e9 documentar una sesi\u00f3n?",
                "a": "Redacte la nota tan pronto como detecte el error, indicando fecha real de la sesi\u00f3n y fecha de registro. Evite inventar detalles; documente solo lo que recuerde con certeza.",
            },
            {
                "q": "\u00bfLa nota de evoluci\u00f3n sustituye al plan de tratamiento?",
                "a": "No. El plan establece objetivos e intervenciones globales; la evoluci\u00f3n registra el avance sesi\u00f3n a sesi\u00f3n. Ambos deben ser coherentes.",
            },
            {
                "q": "\u00bfPuedo usar IA para generar notas de evoluci\u00f3n?",
                "a": "Solo con consentimiento informado del paciente, revisi\u00f3n y firma del psic\u00f3logo responsable. Usted es accountable del contenido cl\u00ednico registrado.",
            },
        ],
        "related": [
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004: historia cl\u00ednica en M\u00e9xico"},
            {"href": "/articulos/como-redactar-informe-psicologico.html", "label": "C\u00f3mo redactar informe psicol\u00f3gico"},
            {"href": "/articulos/consentimiento-informado-psicologia.html", "label": "Consentimiento informado en psicolog\u00eda"},
            {"href": "/articulos/software-para-psicologos-clinicos.html", "label": "Software para psic\u00f3logos cl\u00ednicos"},
        ],
        "cta_h2": CTA_H2,
        "cta_p": CTA_P,
    }
)

# --- 33 plan-tratamiento-psicologico ---
ARTICLES.append(
    {
        "slug": "plan-tratamiento-psicologico",
        "title": "Plan tratamiento psicol\u00f3gico: objetivos y registro | Kalyo",
        "description": "Plan de tratamiento psicol\u00f3gico: objetivos SMART, intervenciones, revisi\u00f3n peri\u00f3dica, NOM-004 y registro en expediente cl\u00ednico para psic\u00f3logos en M\u00e9xico.",
        "keywords": "plan de tratamiento psicol\u00f3gico, objetivos SMART, formulaci\u00f3n de caso, psicoterapia, NOM-004, expediente cl\u00ednico, psicolog\u00eda cl\u00ednica",
        "h1": "Plan de tratamiento psicol\u00f3gico: c\u00f3mo estructurarlo en consulta cl\u00ednica",
        "breadcrumb_short": "Plan de tratamiento psicol\u00f3gico",
        "hero_alt": "Psic\u00f3logo elaborando plan de tratamiento psicol\u00f3gico con paciente en consulta",
        "inline_alt": "Componentes del plan de tratamiento: diagn\u00f3stico funcional, objetivos e intervenciones",
        "quick_answer": "El plan de tratamiento psicol\u00f3gico es el documento que traduce la evaluaci\u00f3n inicial en objetivos medibles, intervenciones acordadas, frecuencia de sesiones, criterios de alta y responsables. Debe elaborarse con participaci\u00f3n del paciente, revisarse peri\u00f3dicamente y archivarse en el expediente cl\u00ednico seg\u00fan la NOM-004 y la \u00e9tica profesional.",
        "intro_long": "El <strong>plan de tratamiento psicol\u00f3gico</strong> orienta cada sesi\u00f3n: sin \u00e9l, la psicoterapia puede volverse improvisada y dif\u00edcil de evaluar. Tras la evaluaci\u00f3n inicial, el psic\u00f3logo formula hip\u00f3tesis cl\u00ednicas, define metas realistas con el consultante y selecciona t\u00e9cnicas acordes al modelo te\u00f3rico y al contexto (presencial, <a href=\"/articulos/teleconsulta-psicologos.html\">teleconsulta</a>, recursos disponibles). En M\u00e9xico, integrar el plan al expediente exigido por la <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> es buena pr\u00e1ctica; en salud mental comunitaria, alinea expectativas con familiares y equipo interdisciplinario. Esta gu\u00eda explica componentes esenciales, objetivos SMART, revisi\u00f3n peri\u00f3dica y c\u00f3mo vincular el plan con notas de evoluci\u00f3n e informes. Un plan visible para el paciente (versi\u00f3n resumida sin jerga) refuerza transparencia y reduce conflictos por expectativas no alineadas sobre duraci\u00f3n o resultados del proceso.",
        "meta_label": "Pr&aacute;ctica cl&iacute;nica &middot; Planificaci&oacute;n terap&eacute;utica &middot; 2026",
        "sections": [
            {
                "h2": "Qu\u00e9 es un plan de tratamiento psicol\u00f3gico",
                "html": p(
                    "El plan de tratamiento psicol\u00f3gico es un acuerdo cl\u00ednico estructurado que describe el problema principal (formulaci\u00f3n), objetivos terap\u00e9uticos, estrategias e intervenciones previstas, frecuencia y duraci\u00f3n estimada, roles del paciente y del terapeuta, indicadores de progreso y criterios de alta o derivaci\u00f3n. No es un contrato comercial, aunque puede complementarse con acuerdos de honorarios.",
                    "Se elabora tras la evaluaci\u00f3n inicial suficiente (entrevista, pruebas si indicadas, exploraci\u00f3n de riesgo). En crisis aguda, puede iniciarse un plan de estabilizaci\u00f3n provisional y refinarse en las primeras semanas. Debe ser comprensible para el paciente: evite jerga te\u00f3rica sin explicaci\u00f3n.",
                    "El plan conecta diagn\u00f3stico o formulaci\u00f3n con acci\u00f3n: transforma \u00abdepresi\u00f3n moderada con aislamiento social\u00bb en metas como \u00abreintegrar una actividad social semanal en ocho semanas\u00bb con tareas concretas.",
                ),
            },
            {
                "h2": "Formulaci\u00f3n del caso y objetivos SMART",
                "html": p(
                    "Antes de fijar metas, sintetice <strong>formulaci\u00f3n biopsicosocial</strong>: factores predisponentes, precipitantes, mantenedores y protectores. Incluya fortalezas del paciente. Los objetivos SMART son Espec\u00edficos, Medibles, Alcanzables, Relevantes y Temporales: \u00abreducir frecuencia de ataques de p\u00e1nico de cinco a dos por semana en seis semanas\u00bb es m\u00e1s \u00fatil que \u00abmejorar ansiedad\u00bb.",
                    "Combine objetivos de s\u00edntoma (reducir insomnio), funcionales (retomar clases), relacionales (comunicar l\u00edmites con pareja) y de proceso (identificar pensamientos autom\u00e1ticos). Priorice dos o tres metas activas para no dispersar la terapia. Acuerde con el paciente cu\u00e1les son negociables y cu\u00e1les urgentes (p. ej., seguridad en riesgo suicida).",
                    "Documente baseline: puntaje en escalas, frecuencia conductual, d\u00edas de inasistencia laboral. Permite comparar en revisiones trimestrales.",
                )
                + """
<ul>
<li><strong>Espec&iacute;fico:</strong> conducta o s&iacute;ntoma concreto.</li>
<li><strong>Medible:</strong> escala, frecuencia o duraci&oacute;n registrable.</li>
<li><strong>Temporal:</strong> plazo realista seg&uacute;n gravedad y recursos.</li>
</ul>""",
            },
            {
                "h2": "Intervenciones, t\u00e9cnicas y criterios de alta",
                "html": p(
                    "Describa el enfoque principal (TCC, ACT, sist\u00e9mica, humanista integrativo) y t\u00e9cnicas planeadas: reestructuraci\u00f3n cognitiva, exposici\u00f3n gradual, entrenamiento en habilidades sociales, psicoeducaci\u00f3n, mindfulness. Indique si habr\u00e1 tareas entre sesiones y material de apoyo. Si prev\u00e9 evaluaci\u00f3n psicom\u00e9trica repetida, mencione instrumentos y calendario, alineado con <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">c\u00f3mo interpretar tests psicol\u00f3gicos</a>.",
                    "Defina <strong>criterios de alta</strong>: metas alcanzadas, remisi\u00f3n de s\u00edntomas cl\u00ednicamente significativa, paciente aut\u00f3nomo en manejo de reca\u00eddas, o derivaci\u00f3n a otro nivel de atenci\u00f3n. Incluya plan de prevenci\u00f3n de reca\u00edda y opciones de sesiones de seguimiento espaciadas.",
                    "Si el paciente interrumpe antes de cumplir objetivos, registre motivo (econ\u00f3mico, mudanza, insatisfacci\u00f3n, mejor\u00eda parcial) y recomendaciones de continuidad.",
                ),
            },
            {
                "h2": "Revisi\u00f3n peri\u00f3dica y medici\u00f3n de avance",
                "html": p(
                    "Revise el plan cada cuatro a ocho sesiones o ante eventos cr\u00edticos (reca\u00edda, cambio laboral, nueva comorbilidad m\u00e9dica). Eval\u00fae progreso con datos: escalas, cumplimiento de tareas, observaciones en sesi\u00f3n. Si no hay avance, reformule hip\u00f3tesis: \u00bfBarrera de adherencia? \u00bfDiagn\u00f3stico incompleto? \u00bfEnfoque mal ajustado?",
                    "Involucre al paciente en la revisi\u00f3n: \u00bfQu\u00e9 ha funcionado? \u00bfQu\u00e9 ajustar? La participaci\u00f3n activa mejora compromiso. En terapia familiar o de pareja, actualice acuerdos y reglas observables.",
                    "Las notas de evoluci\u00f3n deben referir objetivos del plan; si cambia el plan, documente versi\u00f3n nueva con fecha y motivo, conservando la anterior en el historial.",
                ),
            },
            {
                "h2": "Plan de tratamiento en contextos legales y de salud mental",
                "html": p(
                    "En M\u00e9xico, el plan forma parte del expediente regulado por la NOM-004. En procesos judiciales o periciales, puede solicitarse justificar intervenci\u00f3n y resultados; un plan claro protege al profesional. En Colombia, la <a href=\"/articulos/ley-1616-2013-salud-mental-colombia.html\">Ley 1616 de salud mental</a> enfatiza enfoque integral y derechos; el plan debe respetar autonom\u00eda y no imponer metas ajenas al consultante.",
                    "En instituciones, alinee el plan con protocolos institucionales (violencia de g\u00e9nero, adicciones, duelo). En menores, incluya metas educativas y coordinaci\u00f3n con tutores con <a href=\"/articulos/consentimiento-informado-psicologia.html\">consentimiento informado</a> vigente.",
                    "Ante riesgo suicida activo, el plan prioriza seguridad: reducci\u00f3n de medios letales, red de apoyo, contacto de emergencia, frecuencia intensiva temporal y coordinaci\u00f3n con psiquiatr\u00eda.",
                ),
            },
            {
                "h2": "Integraci\u00f3n con expediente cl\u00ednico y equipo interdisciplinario",
                "html": p(
                    "Archive el plan en el expediente digital o f\u00edsico, accesible para usted y, con autorizaci\u00f3n, para otros profesionales del equipo. Comparta versi\u00f3n resumida con el paciente (metas y tareas) para reforzar transparencia.",
                    "Cuando redacte un informe externo, el plan y su evoluci\u00f3n sustentan recomendaciones; consulte <a href=\"/articulos/como-redactar-informe-psicologico.html\">c\u00f3mo redactar informe psicol\u00f3gico</a> para coherencia.",
                    "Plataformas como {kalyo} permiten vincular objetivos del plan con sesiones, escalas repetidas y recordatorios de revisi\u00f3n, facilitando continuidad en consultorios con alta carga cl\u00ednica.".format(
                        kalyo=KALYO
                    ),
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfCu\u00e1ndo elaborar el plan de tratamiento psicol\u00f3gico?",
                "a": "Tras la evaluaci\u00f3n inicial, cuando tenga hip\u00f3tesis cl\u00ednica suficiente y acuerdo con el paciente sobre metas. En crisis, use un plan breve de estabilizaci\u00f3n y compl\u00e9telo en dos o tres sesiones.",
            },
            {
                "q": "\u00bfDebe firmarlo el paciente?",
                "a": "Se recomienda acuerdo documentado: firma o aceptaci\u00f3n digital del paciente y del psic\u00f3logo. Refuerza alianza y claridad de expectativas.",
            },
            {
                "q": "\u00bfPuedo cambiar el enfoque terap\u00e9utico a mitad del tratamiento?",
                "a": "S\u00ed, si lo cl\u00ednico lo justifica. Registre motivo del cambio, nuevo plan y discusi\u00f3n con el paciente; no borre versiones anteriores.",
            },
            {
                "q": "\u00bfEl plan es lo mismo que las notas de evoluci\u00f3n?",
                "a": "No. El plan es el mapa; las notas de evoluci\u00f3n registran cada sesi\u00f3n. Ambos deben ser coherentes y complementarios.",
            },
            {
                "q": "\u00bfQu\u00e9 hacer si el paciente rechaza un objetivo del plan?",
                "a": "Negocie metas alternativas alcanzables. Sin acuerdo m\u00ednimo sobre objetivos o riesgo no manejable, eval\u00fae derivaci\u00f3n o alta con recomendaciones.",
            },
        ],
        "related": [
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004: historia cl\u00ednica en M\u00e9xico"},
            {"href": "/articulos/como-redactar-informe-psicologico.html", "label": "C\u00f3mo redactar informe psicol\u00f3gico"},
            {"href": "/articulos/consentimiento-informado-psicologia.html", "label": "Consentimiento informado en psicolog\u00eda"},
            {"href": "/articulos/ley-1616-2013-salud-mental-colombia.html", "label": "Ley 1616: salud mental Colombia"},
        ],
        "cta_h2": CTA_H2,
        "cta_p": CTA_P,
    }
)

# --- 34 psicometria-que-es ---
ARTICLES.append(
    {
        "slug": "psicometria-que-es",
        "title": "Psicometr\u00eda qu\u00e9 es: tests, validez y uso cl\u00ednico MX | Kalyo",
        "description": "Psicometr\u00eda qu\u00e9 es: validez, fiabilidad, tipos de tests, interpretaci\u00f3n cl\u00ednica \u00e9tica y registro en expediente para psic\u00f3logos en M\u00e9xico y Latinoam\u00e9rica.",
        "keywords": "psicometr\u00eda qu\u00e9 es, tests psicol\u00f3gicos, validez, fiabilidad, evaluaci\u00f3n psicol\u00f3gica, interpretaci\u00f3n cl\u00ednica, psicolog\u00eda M\u00e9xico",
        "h1": "Psicometr\u00eda qu\u00e9 es: fundamentos para la pr\u00e1ctica cl\u00ednica",
        "breadcrumb_short": "Psicometr\u00eda qu\u00e9 es",
        "hero_alt": "Aplicaci\u00f3n de test psicol\u00f3gico en consulta cl\u00ednica con interpretaci\u00f3n profesional",
        "inline_alt": "Conceptos de validez, fiabilidad y estandarizaci\u00f3n en psicometr\u00eda cl\u00ednica",
        "quick_answer": "La psicometr\u00eda es la disciplina que desarrolla, adapta y valida instrumentos para medir constructos psicol\u00f3gicos con rigor estad\u00edstico. En cl\u00ednica, permite aplicar tests y escalas con validez, fiabilidad y normas adecuadas, siempre integrados con entrevista, observaci\u00f3n y juicio profesional informado por el C\u00f3digo de \u00c9tica.",
        "intro_long": "Cuando colegas o pacientes preguntan <strong>psicometr\u00eda qu\u00e9 es</strong>, conviene ir m\u00e1s all\u00e1 del \u00abtest de personalidad\u00bb: es el conjunto de m\u00e9todos que hacen medible lo psicol\u00f3gico con criterios cient\u00edficos. El psic\u00f3logo cl\u00ednico usa pruebas proyectivas, escalas de s\u00edntomas, bater\u00edas cognitivas e inventarios de personalidad dentro de una evaluaci\u00f3n integral. Comprender validez, fiabilidad y limitaciones evita sobreinterpretar puntajes. Esta gu\u00eda conecta fundamentos psicom\u00e9tricos con pr\u00e1ctica en M\u00e9xico: consentimiento, registro en expediente seg\u00fan la <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> e interpretaci\u00f3n responsable descrita en <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">c\u00f3mo interpretar tests psicol\u00f3gicos</a>. La formaci\u00f3n continua en evaluaci\u00f3n psicol\u00f3gica protege al profesional de usar instrumentos obsoletos o aplicaciones comerciales sin respaldo t\u00e9cnico adecuado.",
        "meta_label": "Psicometr&iacute;a cl&iacute;nica &middot; Fundamentos &middot; Actualizaci&oacute;n 2026",
        "sections": [
            {
                "h2": "Psicometr\u00eda qu\u00e9 es: definici\u00f3n y alcance",
                "html": p(
                    "La psicometr\u00eda estudia c\u00f3mo medir atributos psicol\u00f3gicos (inteligencia, personalidad, s\u00edntomas, aptitudes) mediante instrumentos estandarizados. Incluye dise\u00f1o de \u00edtems, pilotaje, an\u00e1lisis de validez y fiabilidad, normas por poblaci\u00f3n y manual de aplicaci\u00f3n. No se reduce a \u00abcalificar cuestionarios\u00bb: implica decidir si un instrumento mide lo que afirma medir y si los resultados son reproducibles y \u00fatiles para decisiones cl\u00ednicas.",
                    "En la formaci\u00f3n del psic\u00f3logo cl\u00ednico, la psicometr\u00eda sustenta evaluaci\u00f3n diagn\u00f3stica, selecci\u00f3n de tratamiento, informes periciales y seguimiento de cambio. Un test sin respaldo psicom\u00e9trico adecuado para la poblaci\u00f3n evaluada puede inducir error cl\u00ednico y da\u00f1o (sobrediagn\u00f3stico, estigmatizaci\u00f3n, decisiones escolares o laborales incorrectas).",
                    "Diferencie psicometr\u00eda de psicodiagn\u00f3stico: el segundo es el proceso cl\u00ednico integral; la psicometr\u00eda aporta herramientas medidas dentro de ese proceso.",
                ),
            },
            {
                "h2": "Tests psicol\u00f3gicos: tipos y aplicaciones cl\u00ednicas",
                "html": p(
                    "Los <strong>tests psicol\u00f3gicos</strong> se clasifican seg\u00fan constructo y formato: escalas de s\u00edntomas (PHQ-9, GAD-7), inventarios de personalidad (MMPI-2, NEO), pruebas cognitivas (WAIS, WISC), tests proyectivos (Rorschach, TAT, seg\u00fan formaci\u00f3n), evaluaciones neuropsicol\u00f3gicas breves o completas, y bater\u00edas vocacionales u ocupacionales.",
                    "En consulta privada mexicana, los tests m\u00e1s frecuentes son escalas breves de tamizaje, cuestionarios de personalidad con normas latinas cuando existen, y pruebas cognitivas para sospecha de deterioro o TDAH. Seleccione instrumentos acordes a la pregunta cl\u00ednica: \u00bfTamizaje de depresi\u00f3n? \u00bfPerfil cognitivo? \u00bfAptitud para cierto puesto con consentimiento laboral?",
                    "Evite aplicar bater\u00edas extensas sin indicaci\u00f3n; respete fatiga del paciente y costo. Documente cu\u00e1les pruebas se aplicaron, en qu\u00e9 idioma y bajo qu\u00e9 condiciones (presencial, supervisado, autoadministrado en casa con instrucciones).",
                )
                + """
<table class="items-table">
<thead><tr><th>Tipo</th><th>Ejemplo de uso</th><th>Nota cl&iacute;nica</th></tr></thead>
<tbody>
<tr><td>Tamizaje</td><td>PHQ-9, AUDIT</td><td>Orienta; no diagnostica solo</td></tr>
<tr><td>Personalidad</td><td>Inventarios multiscala</td><td>Requiere formaci&oacute;n en interpretaci&oacute;n</td></tr>
<tr><td>Cognitivo</td><td>WAIS/WISC</td><td>Certificaci&oacute;n del aplicador</td></tr>
</tbody>
</table>""",
            },
            {
                "h2": "Validez, fiabilidad y estandarizaci\u00f3n",
                "html": p(
                    "<strong>Fiabilidad</strong> indica consistencia del instrumento (test-retest, alpha de Cronbach, equivalencia entre formas). <strong>Validez</strong> indica si mide el constructo pretendido: validez de contenido, criterio (convergente con otros instrumentos o diagn\u00f3stico cl\u00ednico), constructo (an\u00e1lisis factorial). Un test fiable no es necesariamente v\u00e1lido para su pregunta cl\u00ednica.",
                    "La <strong>estandarizaci\u00f3n</strong> define procedimiento uniforme de aplicaci\u00f3n y calificaci\u00f3n; las <strong>normas</strong> permiten comparar al individuo con una muestra de referencia. Cuidado al usar normas norteamericanas en poblaci\u00f3n mexicana sin estudios de equivalencia: interpretaciones pueden sesgarse. Prefiera manuales con datos latinos o interprete con cautela cl\u00ednica.",
                    "Revise validez ecol\u00f3gica: \u00bfEl resultado predice funcionamiento real? Integre siempre entrevista y observaci\u00f3n.",
                ),
            },
            {
                "h2": "Administraci\u00f3n \u00e9tica y consentimiento informado",
                "html": p(
                    "Aplicar tests requiere <a href=\"/articulos/consentimiento-informado-psicologia.html\">consentimiento informado</a> espec\u00edfico: para qu\u00e9 se usan resultados, qui\u00e9n acceder\u00e1, si habr\u00e1 informe a terceros. En menores, autorizaci\u00f3n de tutores y explicaci\u00f3n adecuada al ni\u00f1o seg\u00fan edad.",
                    "Mantenga confidencialidad de protocolos restringidos (material de prueba, respuestas). No divulgue puntajes en redes ni permita que el paciente se autoetiquete sin contexto cl\u00ednico (\u00absaqu\u00e9 alto en narcisismo\u00bb en Instagram). En contextos laborales o legales, aclare limitaciones de validez incremental y posible simulaci\u00f3n o disimulaci\u00f3n.",
                    "Si aplica pruebas en <a href=\"/articulos/teleconsulta-psicologos.html\">teleconsulta</a>, verifique supervisi\u00f3n, identidad y condiciones que el manual autorice para modalidad remota.",
                ),
            },
            {
                "h2": "Interpretaci\u00f3n cl\u00ednica integrada",
                "html": p(
                    "La interpretaci\u00f3n psicom\u00e9trica no es lectura autom\u00e1tica de puntajes: integra perfil multiscala, consistencia de respuestas (\u00edndices de validez en inventarios), contexto vital, medicaci\u00f3n, sue\u00f1o, cultura y motivaci\u00f3n del evaluado. Consulte la gu\u00eda <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">c\u00f3mo interpretar tests psicol\u00f3gicos</a> para estructurar informes.",
                    "Evite lenguaje determinista (\u00abel test dice que es borderline\u00bb). Reporte hip\u00f3tesis, nivel de confianza y recomendaciones. En discrepancia entre test y entrevista, priorice formulaci\u00f3n cl\u00ednica y considere reevaluaci\u00f3n o fuentes m\u00faltiples.",
                    "Para seguimiento terap\u00e9utico, repita la misma escala en intervalos definidos y grafique cambio; un punto aislado no define respuesta al tratamiento.",
                ),
            },
            {
                "h2": "Registro de resultados en el expediente cl\u00ednico",
                "html": p(
                    "Archive protocolos, hojas de respuesta o registros digitales en el expediente conforme a la <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a>. Incluya fecha, instrumentos, puntajes clave, interpretaci\u00f3n resumida y recomendaciones. Si emite informe formal, siga estructura profesional en <a href=\"/articulos/como-redactar-informe-psicologico.html\">c\u00f3mo redactar informe psicol\u00f3gico</a>.",
                    "Conserve materiales seg\u00fan pol\u00edtica del editor del test ( algunos exigen almacenamiento bajo llave). En plataformas digitales, asegure que solo personal autorizado accede a resultados sensibles.",
                    "Herramientas como {kalyo} permiten aplicar decenas de escalas, calificar autom\u00e1ticamente y vincular resultados al expediente, ahorrando tiempo administrativo sin reemplazar su juicio cl\u00ednico en la interpretaci\u00f3n.".format(
                        kalyo=KALYO
                    ),
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfPsicometr\u00eda y evaluaci\u00f3n psicol\u00f3gica son lo mismo?",
                "a": "La evaluaci\u00f3n psicol\u00f3gica es el proceso cl\u00ednico completo; la psicometr\u00eda aporta la base cient\u00edfica y los instrumentos medidos que pueden formar parte de aquella.",
            },
            {
                "q": "\u00bfPuedo usar tests sin normas mexicanas?",
                "a": "Puede hacerlo con cautela documentada, explicando limitaciones al paciente y destinatarios del informe. Prefiera instrumentos con evidencia en poblaci\u00f3n similar cuando exista.",
            },
            {
                "q": "\u00bfUn puntaje alto en depresi\u00f3n confirma diagn\u00f3stico?",
                "a": "No por s\u00ed solo. Confirma con entrevista cl\u00ednica, criterios DSM-5 o CIE-11, duraci\u00f3n, deterioro funcional y exclusi\u00f3n de otras causas.",
            },
            {
                "q": "\u00bfLos tests en l\u00ednea gratuitos son v\u00e1lidos cl\u00ednicamente?",
                "a": "La mayor\u00eda carece de control estandarizado y confidencialidad adecuada. No sustituyen instrumentos cl\u00ednicos validados aplicados por profesional.",
            },
            {
                "q": "\u00bfDebo guardar las hojas de respuesta?",
                "a": "S\u00ed, seg\u00fan manual del test y normativa del expediente. Facilitan reevaluaci\u00f3n, auditor\u00eda y defensa de su interpretaci\u00f3n.",
            },
        ],
        "related": [
            {"href": "/articulos/como-interpretar-tests-psicologicos.html", "label": "C\u00f3mo interpretar tests psicol\u00f3gicos"},
            {"href": "/articulos/como-redactar-informe-psicologico.html", "label": "C\u00f3mo redactar informe psicol\u00f3gico"},
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004: historia cl\u00ednica en M\u00e9xico"},
            {"href": "/articulos/software-para-psicologos-clinicos.html", "label": "Software para psic\u00f3logos cl\u00ednicos"},
        ],
        "cta_h2": CTA_H2,
        "cta_p": CTA_P,
    }
)

# --- 35 etica-psicologo-mexico ---
ARTICLES.append(
    {
        "slug": "etica-psicologo-mexico",
        "title": "\u00c9tica profesional psic\u00f3logo M\u00e9xico: gu\u00eda cl\u00ednica | Kalyo",
        "description": "\u00c9tica profesional psic\u00f3logo M\u00e9xico: C\u00f3digo de \u00c9tica, confidencialidad, teleconsulta, l\u00edmites terap\u00e9uticos y documentaci\u00f3n cl\u00ednica responsable en consulta.",
        "keywords": "\u00e9tica profesional psic\u00f3logo M\u00e9xico, C\u00f3digo de \u00c9tica, confidencialidad, psicolog\u00eda cl\u00ednica, NOM-004, teleconsulta, colegio de psic\u00f3logos",
        "h1": "\u00c9tica profesional del psic\u00f3logo en M\u00e9xico: principios y pr\u00e1ctica",
        "breadcrumb_short": "\u00c9tica profesional M\u00e9xico",
        "hero_alt": "Psic\u00f3logo revisando principios \u00e9ticos y documentaci\u00f3n cl\u00ednica en consulta mexicana",
        "inline_alt": "Pilares de la \u00e9tica profesional: autonom\u00eda, confidencialidad y competencia",
        "quick_answer": "La \u00e9tica profesional del psic\u00f3logo en M\u00e9xico se sustenta en el C\u00f3digo de \u00c9tica, la legislaci\u00f3n sanitaria y la NOM-004: beneficencia, no maleficencia, autonom\u00eda, confidencialidad y competencia. Implica l\u00edmites claros en la relaci\u00f3n terap\u00e9utica, consentimiento informado, manejo responsable de datos y derivaci\u00f3n cuando el caso excede su formaci\u00f3n.",
        "intro_long": "La <strong>\u00e9tica profesional psic\u00f3logo M\u00e9xico</strong> no es un ap\u00e9ndice acad\u00e9mico: es la br\u00fajula diaria del consultorio. Colegios profesionales, la Ley General de Salud, la <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> y el C\u00f3digo de \u00c9tica definen deberes hacia pacientes, colegas e instituciones. Violaciones \u00e9ticas pueden implicar sanciones colegiales, demandas civiles o p\u00e9rdida de confianza p\u00fablica. Este art\u00edculo repasa confidencialidad y sus l\u00edmites, relaci\u00f3n dual, publicidad responsable, <a href=\"/articulos/teleconsulta-psicologos.html\">teleconsulta</a> y documentaci\u00f3n cl\u00ednica alineada con <a href=\"/articulos/consentimiento-informado-psicologia-mexico.html\">consentimiento informado en psicolog\u00eda M\u00e9xico</a> y buenas pr\u00e1cticas de expediente digital. Revisar el c\u00f3digo al menos una vez al a\u00f1o actualiza criterios ante nuevas tecnolog\u00edas y modalidades de atenci\u00f3n.",
        "meta_label": "&Eacute;tica profesional &middot; M&eacute;xico &middot; Actualizaci&oacute;n 2026",
        "sections": [
            {
                "h2": "\u00c9tica profesional del psic\u00f3logo en M\u00e9xico: marco normativo",
                "html": p(
                    "El ejercicio psicol\u00f3gico en M\u00e9xico se regula por la Ley General de Salud, reglamentos estatales, c\u00e9dula profesional expedida por la SEP, normas oficiales como la NOM-004 para expediente cl\u00ednico, la LFPDPPP para datos personales, y el C\u00f3digo de \u00c9tica promulgado por el Colegio Nacional de Psic\u00f3logos de M\u00e9xico y colegios estatales. Estos documentos convergen en proteger al paciente y garantizar competencia profesional.",
                    "Principios centrales: <strong>beneficencia</strong> (actuar en beneficio del consultante), <strong>no maleficencia</strong> (evitar da\u00f1o), <strong>autonom\u00eda</strong> (respetar decisiones informadas), <strong>justicia</strong> (acceso equitativo, no discriminaci\u00f3n) y <strong>fidelidad</strong> (lealtad y veracidad en la relaci\u00f3n profesional).",
                    "La \u00e9tica tambi\u00e9n obliga a reconocer l\u00edmites de competencia: no todo psic\u00f3logo est\u00e1 capacitado para neuropsicolog\u00eda forense, psicoterapia de pareja compleja o adicciones severas sin formaci\u00f3n espec\u00edfica y supervisi\u00f3n.",
                ),
            },
            {
                "h2": "C\u00f3digo de \u00c9tica: deberes hacia el paciente",
                "html": p(
                    "Hacia el paciente, el psic\u00f3logo debe ofrecer servicios con diligencia, mantener confidencialidad, obtener consentimiento informado, evitar explotaci\u00f3n (sexual, econ\u00f3mica, laboral), respetar diversidad cultural, de g\u00e9nero y orientaci\u00f3n, y proporcionar informaci\u00f3n clara sobre su formaci\u00f3n y modalidad de trabajo.",
                    "Debe explicar honorarios, pol\u00edtica de cancelaci\u00f3n y duraci\u00f3n estimada del proceso cuando sea posible. No garantice curas ni resultados milagrosos. En investigaci\u00f3n o uso de datos, transparencia adicional y aprobaci\u00f3n \u00e9tica cuando corresponda.",
                    "El paciente tiene derecho a acceder a su expediente seg\u00fan la ley, solicitar copias, corregir datos err\u00f3neos en aviso de privacidad y terminar la relaci\u00f3n terap\u00e9utica, salvo obligaciones legales pendientes.",
                ),
            },
            {
                "h2": "Confidencialidad, l\u00edmites y deber de reporte",
                "html": p(
                    "La confidencialidad es pilar de la psicoterapia, pero no es absoluta. Excepciones t\u00edpicas en M\u00e9xico incluyen: riesgo grave e inminente para la vida del paciente o terceros; sospecha fundada de abuso o negligencia contra menores o personas vulnerables; mandato judicial; algunas situaciones de notificaci\u00f3n epidemiol\u00f3gica. Conozca la ley estatal aplicable y documente la raz\u00f3n de cualquier ruptura de confidencialidad.",
                    "Explique estos l\u00edmites en el <a href=\"/articulos/consentimiento-informado-psicologia.html\">consentimiento informado</a> desde la primera sesi\u00f3n. Ante dilemas, consulte supervisi\u00f3n, asesor\u00eda legal y, si el paciente no est\u00e1 en peligro inmediato, busque minimizar divulgaci\u00f3n (informar solo lo necesario).",
                    "En pareja o familia, acuerde qu\u00e9 contenido individual permanece confidencial y qu\u00e9 se comparte en sesi\u00f3n conjunta. En informes periciales, recuerde que el destinatario es quien contrat\u00f3 la evaluaci\u00f3n dentro del marco legal, no necesariamente el paciente como en terapia cl\u00ednica.",
                ),
            },
            {
                "h2": "Relaci\u00f3n terap\u00e9utica, dualidad y conflictos de inter\u00e9s",
                "html": p(
                    "Evite relaciones duales: tratar a familiares cercanos, empleados, parejas rom\u00e1nticas o personas con las que tenga intereses financieros compartidos. Si la dualidad es inevitable en comunidades peque\u00f1as, documente medidas de manejo (derivaci\u00f3n, l\u00edmites estrictos, supervisi\u00f3n).",
                    "No acepte regalos sustanciales ni favores que comprometan imparcialidad. En publicidad, evite comparaciones denigrantes con colegas, promesas de resultados garantizados o uso de testimonios identificables sin consentimiento escrito.",
                    "Mantenga l\u00edmites temporales y econ\u00f3micos: cobrar tarifas razonables, no prolongar terapia innecesariamente por beneficio econ\u00f3mico, ofrecer derivaci\u00f3n cuando el paciente no progresa y otro enfoque es indicado.",
                ),
            },
            {
                "h2": "Teleconsulta, redes sociales y presencia digital \u00e9tica",
                "html": p(
                    "La <a href=\"/articulos/teleconsulta-psicologos.html\">teleconsulta</a> exige las mismas obligaciones \u00e9ticas que la presencial m\u00e1s consideraciones t\u00e9cnicas: verificar identidad, asegurar entorno privado del terapeuta, usar plataformas con confidencialidad razonable, plan de emergencias si el paciente est\u00e1 en otra ciudad, y consentimiento espec\u00edfico para modalidad remota.",
                    "En redes sociales, separe vida personal de identidad profesional cuando sea posible. No diagnostique en comentarios p\u00fablicos. Si educa en contenido cl\u00ednico, evite que pacientes actuales interact\u00faen de forma que erosione confidencialidad. No publique fragmentos de sesiones reconocibles.",
                    "El uso de IA para notas o transcripci\u00f3n requiere consentimiento, revisi\u00f3n humana y pol\u00edtica de privacidad del proveedor tecnol\u00f3gico.",
                ),
            },
            {
                "h2": "Supervisi\u00f3n, formaci\u00f3n continua y documentaci\u00f3n \u00e9tica",
                "html": p(
                    "La competencia exige formaci\u00f3n continua, supervisi\u00f3n cl\u00ednica en casos complejos y adherencia a la NOM-004 en documentaci\u00f3n: historia cl\u00ednica, notas de evoluci\u00f3n, planes de tratamiento, consentimientos. Un expediente incompleto dificulta defensa \u00e9tica ante quejas.",
                    "Ante errores cl\u00ednicos o \u00e9ticos, priorice reparaci\u00f3n al paciente, consulta colegial y transparencia institucional cuando aplique. El encubrimiento agrava sanciones colegiales.",
                    "Para organizar expediente, consentimientos y trazabilidad sin sacrificar confidencialidad, muchos consultorios usan {kalyo}, alineado con flujos cl\u00ednicos digitales descritos en <a href=\"/articulos/software-para-psicologos-clinicos.html\">software para psic\u00f3logos cl\u00ednicos</a>.".format(
                        kalyo=KALYO
                    ),
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfPuedo tener relaci\u00f3n de pareja con un ex paciente?",
                "a": "La mayor\u00eda de c\u00f3digos \u00e9ticos desaconsejan o proh\u00edben relaciones rom\u00e1nticas con ex pacientes por periodos prolongados o de forma permanente, por el desequilibrio de poder inherente.",
            },
            {
                "q": "\u00bfDebo reportar abuso infantil aunque el paciente adulto pida secreto?",
                "a": "Cuando la ley exige reporte de abuso actual contra menores o personas vulnerables, el deber legal prevalece. Documente y, cuando sea seguro, informe al paciente sobre su obligaci\u00f3n.",
            },
            {
                "q": "\u00bfPuedo negarme a entregar el expediente al paciente?",
                "a": "En general no, salvo excepciones legales (riesgo para terceros si se divulgan ciertos datos, materiales de terceros). Consulte normativa vigente y asesor\u00eda legal.",
            },
            {
                "q": "\u00bfLa \u00e9tica difiere en sector p\u00fablico y privado?",
                "a": "Los principios son los mismos; el sector p\u00fablico a\u00f1ade protocolos institucionales y posibles obligaciones de reporte epidemiol\u00f3gico o administrativo.",
            },
            {
                "q": "\u00bfQu\u00e9 hacer si un colega act\u00faa anti\u00e9ticamente?",
                "a": "Seg\u00fan gravedad, aborde directamente, documente hechos objetivos y acuda al colegio profesional o autoridad competente si hay da\u00f1o al paciente.",
            },
        ],
        "related": [
            {"href": "/articulos/consentimiento-informado-psicologia-mexico.html", "label": "Consentimiento informado psicolog\u00eda M\u00e9xico"},
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004: historia cl\u00ednica en M\u00e9xico"},
            {"href": "/articulos/teleconsulta-psicologos.html", "label": "Teleconsulta para psic\u00f3logos"},
            {"href": "/articulos/software-para-psicologos-clinicos.html", "label": "Software para psic\u00f3logos cl\u00ednicos"},
        ],
        "cta_h2": CTA_H2,
        "cta_p": CTA_P,
    }
)


SECTION_PADS: dict[str, list[str]] = {
    "nota-evolucion-psicologica": [
        "<p>En la pr\u00e1ctica diaria, reserve cinco a diez minutos tras cada sesi\u00f3n para redactar la evoluci\u00f3n mientras el intercambio est\u00e1 fresco. Si atiende varios pacientes seguidos, una plantilla SOAP preconfigurada reduce omisiones de evaluaci\u00f3n de riesgo o tareas acordadas. Evite registrar datos sensibles innecesarios (n\u00fameros de cuenta, contrase\u00f1as) que no aporten valor cl\u00ednico.</p>",
        "<p>Ante solicitudes de terceros, recuerde que la nota de evoluci\u00f3n es parte del expediente protegido; compartir extractos requiere consentimiento espec\u00edfico o mandato legal. En peritajes, el perito redacta informe aparte aunque consulte las evoluciones internas.</p>",
        "<p>El apartado Subjetivo debe reflejar la voz del paciente sin sarcasmo ni juicio. Si cita preocupaciones centrales (\u00abno quiero seguir con medicaci\u00f3n\u00bb), facilitan decisiones compartidas con psiquiatr\u00eda en casos con tratamiento combinado.</p>",
        "<p>En Objetivo, describa conductas observables: contacto visual, latencia de respuesta, llanto, agitaci\u00f3n psicomotriz. Estas observaciones complementan autoinforme y son \u00fatiles en seguimiento de trastornos afectivos o psic\u00f3ticos.</p>",
        "<p>El An\u00e1lisis vincula sesi\u00f3n con objetivos del plan de tratamiento: \u00bfSe cumpli\u00f3 la tarea? \u00bfQu\u00e9 barrera apareci\u00f3? Sin este puente, las notas se vuelven lista de eventos sin direcci\u00f3n terap\u00e9utica.</p>",
        "<p>En instituciones con rotaci\u00f3n de residentes, una evoluci\u00f3n clara evita repetir preguntas traumatizantes y mejora continuidad. Digitalizar con respaldo cifrado cumple aviso de privacidad y agiliza auditor\u00edas internas.</p>",
    ],
    "plan-tratamiento-psicologico": [
        "<p>Involucre al paciente en la redacci\u00f3n del plan: pregunte qu\u00e9 meta le importar\u00eda ver cumplida en tres meses. La participaci\u00f3n activa predice mejor adherencia que planes impuestos unilateralmente desde el escritorio del terapeuta.</p>",
        "<p>Documente factores culturales: en algunos contextos familiares mexicanos, metas individuales deben negociarse con expectativas de cuidado de parientes mayores o hijos. Ignorar el sistema familiar genera abandono precoz.</p>",
        "<p>Para trastornos cr\u00f3nicos (TEPT, TLP, trastornos alimentarios), el plan puede priorizar metas de calidad de vida y reducci\u00f3n de da\u00f1o cuando remisi\u00f3n total no es realista a corto plazo. Revise expectativas en cada trimestre.</p>",
        "<p>Describa indicadores observables: n\u00famero de ataques de p\u00e1nico semanales, d\u00edas de asistencia escolar, horas de sue\u00f1o, consumo de alcohol por semana. Los indicadores deben ser recogibles sin equipamiento costoso.</p>",
        "<p>Ante falta de progreso, documente hip\u00f3tesis alternativas: comorbilidad m\u00e9dica no detectada, ambiente laboral t\u00f3xico, efectos adversos de medicaci\u00f3n. El plan debe permitir derivaci\u00f3n a psiquiatr\u00eda o medicina sin culpar al paciente.</p>",
        "<p>En equipos interdisciplinarios, comparta versi\u00f3n resumida del plan (objetivos y frecuencia) con nutrici\u00f3n, psiquiatr\u00eda o trabajo social, siempre con consentimiento. Evite correos con datos identificables sin cifrado.</p><p>Si el paciente pertenece a programa de salud mental comunitario, alinee metas con recursos reales del territorio: grupos de apoyo, medicaci\u00f3n p\u00fablica, tr\u00e1mites de discapacidad. Un plan desconectado del contexto fracasa por falta de viabilidad, no por falta de motivaci\u00f3n.</p>",
        "<p>El plan escrito debe incluir nombre del profesional, fecha, diagn\u00f3stico o formulaci\u00f3n, n\u00famero de sesiones estimadas y criterios expl\u00edcitos de reevaluaci\u00f3n. Sin fecha de revisi\u00f3n, el documento envejece y pierde utilidad cl\u00ednica.</p>",
    ],
    "psicometria-que-es": [
        "<p>La psicometr\u00eda moderna incluye modelos de respuesta al \u00edtem (IRT) que permiten bancos de preguntas adaptativos en plataformas digitales. Conocer el nivel b\u00e1sico ayuda a evaluar si un software cl\u00ednico calibra bien las escalas que administra.</p><p>En M\u00e9xico, muchos psic\u00f3logos cl\u00ednicos combinan escalas libres (PHQ-9, GAD-7) con pruebas comerciales; verifique licencia de uso y formaci\u00f3n requerida antes de facturar evaluaciones completas.</p>",
        "<p>Diferencie test normativo (compara con poblaci\u00f3n) e ipsativo (compara rasgos dentro del individuo, com\u00fan en intereses vocacionales). Confundir ambos lleva a interpretaciones err\u00f3neas en orientaci\u00f3n vocacional o selecci\u00f3n de personal.</p>",
        "<p>La validez de criterio concurrente correlaciona el test con un gold standard cl\u00ednico; validez predictiva estima desempe\u00f1o futuro. En cl\u00ednica, la validez de constructo importa para confirmar que PHQ-9 mide depresi\u00f3n y no ansiedad solamente.</p>",
        "<p>Registre condiciones de aplicaci\u00f3n: ruido ambiental, interrupciones, uso de lentes, horas de sue\u00f1o previas. Factores contextuales explican discrepancias entre prueba y funci\u00f3n real sin invalidar la evaluaci\u00f3n.</p>",
        "<p>Ante perfiles inconsistentes (elevaci\u00f3n en escalas de validez), reentreviste antes de concluir simulaci\u00f3n. Estr\u00e9s extremo, baja lectura o impulsividad tambi\u00e9n distorsionan perfiles.</p>",
        "<p>Integre resultados psicom\u00e9tricos en formulaci\u00f3n escrita: el perfil sugiere elevaci\u00f3n en ansiedad som\u00e1tica, coherente con quejas corporales; recomiende enfoque cognitivo-conductual con componente de relajaci\u00f3n.</p><p>En informes para escuela o trabajo, traduzca puntajes a recomendaciones concretas (pausas sensoriales, flexibilidad de entregas) en lugar de exponer n\u00fameros crudos que estigmatizan sin orientar.</p>",
        "<p>Consulte manuales actualizados del editor del test: versiones revisadas pueden cambiar baremos o \u00edtems. Aplicar manual obsoleto es error \u00e9tico y cl\u00ednico evitable.</p><p>Si administra pruebas en poblaciones no incluidas en la estandarizaci\u00f3n original, declare la limitaci\u00f3n en el informe y evite conclusiones definitivas sobre capacidad intelectual o aptitud.</p>",
    ],
    "etica-psicologo-mexico": [
        "<p>El psic\u00f3logo debe mantener formaci\u00f3n continua acreditada y registrar cursos en curr\u00edculum disponible para pacientes que pregunten por su preparaci\u00f3n en trauma, infancia o neuropsicolog\u00eda. La competencia es obligaci\u00f3n \u00e9tica, no solo comercial.</p><p>Si detecta incompetencia propia en un caso (p. ej., trastorno alimentario severo sin supervisi\u00f3n), la \u00e9tica exige derivar antes de improvisar intervenciones que pongan en riesgo al paciente.</p>",
        "<p>Ante conflictos \u00e9ticos (paciente pide mentir en informe, familiar exige datos sin consentimiento), documente la petici\u00f3n y su respuesta basada en c\u00f3digo. Consulte al colegio profesional antes de actuar en zona gris.</p><p>En situaciones de violencia de g\u00e9nero, priorice seguridad de la v\u00edctima sobre confidencialidad absoluta cuando la ley lo exija y coordine con redes especializadas.</p>",
        "<p>La publicidad en redes debe evitar antes/despu\u00e9s identificables, promesas de cura r\u00e1pida o descuentos que presionen vulnerabilidad econ\u00f3mica. Informe tarifas con transparencia en consentimiento inicial.</p>",
        "<p>En investigaci\u00f3n cl\u00ednica privada, obtenga consentimiento informado ampliado, comit\u00e9 \u00e9tico cuando corresponda y posibilidad real de retirarse sin perder tratamiento base.</p>",
        "<p>La contratransferencia intensa (enojo, atracci\u00f3n, aburrimiento) se aborda en supervisi\u00f3n, no en redes sociales. El paciente nunca debe enterarse de procesos emocionales del terapeuta v\u00eda internet.</p>",
        "<p>Ante queja formal en colegio, coopere con procedimientos, aporte expediente ordenado y evite contactar al quejoso de forma intimidatoria. La documentaci\u00f3n cl\u00ednica oportuna es su mejor defensa si actu\u00f3 conforme a est\u00e1ndares.</p><p>Mantenga l\u00edmites de horario: responder mensajes de pacientes a deshoras puede erosionar marco terap\u00e9utico y generar dependencia. Defina pol\u00edtica de contacto fuera de sesi\u00f3n en consentimiento inicial.</p>",
        "<p>Respete diversidad: evite conversion therapy, patologizar identidades LGBTQ+ o imponer valores religiosos del terapeuta. La neutralidad \u00e9tica no impide psicoeducaci\u00f3n basada en evidencia sobre salud mental.</p><p>En peritajes judiciales, aclare su rol evaluador frente a rol terapeuta; no mezcle dualidad de funciones con el mismo evaluado sin marco legal claro.</p>",
    ],
}


def apply_section_pads() -> None:
    for article in ARTICLES:
        pads = SECTION_PADS.get(article["slug"], [])
        for section, pad in zip(article["sections"], pads):
            section["html"] += pad
        extra = FAQ_PADS.get(article["slug"], [])
        for faq, add in zip(article["faqs"], extra):
            faq["a"] = faq["a"] + " " + add


FAQ_PADS: dict[str, list[str]] = {
    "plan-tratamiento-psicologico": [
        "Incluya fecha tentativa de primera revisi\u00f3n en el documento firmado y programe recordatorio en agenda cl\u00ednica.",
        "La firma del paciente no sustituye comprensi\u00f3n verbal previa de metas, riesgos y alternativas.",
        "Registre en nota de evoluci\u00f3n la discusi\u00f3n cl\u00ednica que motiv\u00f3 el cambio de enfoque.",
        "Las notas deben referir qu\u00e9 objetivo del plan se trabaj\u00f3 en cada sesi\u00f3n cl\u00ednica.",
        "Documente derivaci\u00f3n y comparta plan resumido con nuevo profesional si hay transferencia, incluyendo objetivos pendientes y alertas de riesgo.",
    ],
    "psicometria-que-es": [
        "Consulte al editor si existen normas locales para su regi\u00f3n antes de interpretar percentiles o clasificaciones diagn\u00f3sticas autom\u00e1ticas del software usado.",
        "El diagn\u00f3stico requiere entrevista cl\u00ednica estructurada adem\u00e1s del puntaje, con exploraci\u00f3n de duraci\u00f3n, curso temporal y deterioro funcional en m\u00faltiples \u00e1reas.",
        "Prefiera aplicaci\u00f3n supervisada en evaluaciones de alto impacto legal, laboral o escolar con consecuencias significativas para el evaluado.",
        "Conserve protocolos seg\u00fan pol\u00edtica del editor y tiempo de retenci\u00f3n legal del expediente cl\u00ednico vigente en su consultorio.",
        "La calificaci\u00f3n autom\u00e1tica exige verificaci\u00f3n de respuestas omitidas, dobles marcas o patrones de respuesta aleatoria antes de interpretar.",
    ],
    "etica-psicologo-mexico": [
        "Consulte asesor\u00eda legal local porque plazos y excepciones de confidencialidad var\u00edan por entidad federativa.",
        "Documente evaluaci\u00f3n de riesgo y contactos activados en la misma sesi\u00f3n, con hora y personas notificadas.",
        "Ofrezca copia certificada del expediente cuando la normativa lo permita y el paciente la solicite por escrito.",
        "Revise manuales institucionales adem\u00e1s del c\u00f3digo profesional general si trabaja en sector p\u00fablico.",
        "Priorice bienestar del paciente y evidencia objetiva sobre lealtad a colegas en conflictos \u00e9ticos complejos.",
    ],
}


apply_section_pads()


if __name__ == "__main__":
    for spec in ARTICLES:
        validate(spec)
        print(f"OK {spec['slug']}: title={len(spec['title'])} desc={len(spec['description'])} "
              f"quick={wc(spec['quick_answer'])} body={body_words(spec)} kalyo={kalyo_count(spec)}")
