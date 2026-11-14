#!/usr/bin/env python3
"""Generate 7 AEO compliance/practice articles for Kalyo."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from publish_aeo_helpers import (  # noqa: E402
    bump_counts,
    insert_card,
    insert_sitemap,
    verify,
    word_count as helper_word_count,
)
from render_aeo_article import render  # noqa: E402

SPECS_DIR = ROOT / "scripts" / "article-batch" / "specs"
ART = ROOT / "articulos"
ASSETS = ROOT / "assets" / "blog"

SPECS = [
    # 1 NOM-024 vs NOM-004
    {
        "slug": "nom-024-nom-004-psicologos-mexico",
        "title": "NOM-024 vs NOM-004: diferencias para psicólogos | Kalyo",
        "description": "NOM-024 vs NOM-004 para psicólogos en México: diferencias clave, tabla comparativa, expediente electrónico y checklist de cumplimiento en consulta privada.",
        "keywords": "NOM-024 vs NOM-004, diferencias NOM-024 NOM-004, expediente clínico electrónico, psicólogos México, NOM-004 historia clínica",
        "h1": "NOM-024 vs NOM-004: diferencias para psicólogos en México",
        "breadcrumb_short": "NOM-024 vs NOM-004",
        "hero_alt": "Comparativa NOM-024 y NOM-004 para expediente clínico de psicólogos",
        "inline_alt": "Tabla NOM-024 vs NOM-004 en consultorio psicológico",
        "meta_label": "Cumplimiento legal &middot; M&eacute;xico 2026",
        "date_published": "2026-11-14",
        "date_modified": "2026-11-14",
        "quick_answer": "La <strong>NOM-004</strong> define el <em>contenido, manejo y conservaci&oacute;n</em> del expediente cl&iacute;nico (historia, notas, consentimientos). La <strong>NOM-024</strong> orienta los <em>sistemas electr&oacute;nicos</em> de informaci&oacute;n en salud: seguridad, integridad, interoperabilidad y trazabilidad cuando el expediente es digital. Para psic&oacute;logos en consulta privada: cumpla el contenido cl&iacute;nico (NOM-004) y, si usa ECE, exija autenticaci&oacute;n, bit&aacute;cora y respaldos (esp&iacute;ritu NOM-024 + <a href=\"/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html\">LFPDPPP</a>).",
        "intro_long": "Confundir <strong>NOM-024</strong> con <strong>NOM-004</strong> lleva a comprar software sin estructura cl&iacute;nica o a digitalizar PDFs sin seguridad. Esta gu&iacute;a compara ambas normas para psic&oacute;logos en M&eacute;xico, con tabla clara para featured snippets y un checklist accionable. Complementa <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> y el <a href=\"/articulos/expediente-clinico-electronico-psicologos.html\">expediente electr&oacute;nico</a> con foco en consulta privada.",
        "cta_h2": "Cumple NOM-004 en expediente digital con Kalyo",
        "cta_p": "Historia, notas, consentimientos y control de acceso &mdash; kalyo.io",
        "card_title": "NOM-024 vs NOM-004 para psicólogos",
        "card_p": "Tabla comparativa, diferencias clave y checklist para expediente electrónico en México.",
        "after_href": "/articulos/nom-004-historia-clinica-mexico.html",
        "after_loc": "https://kalyo.io/articulos/nom-004-historia-clinica-mexico.html",
        "asset_from": "nom-004-historia-clinica-mexico",
        "sections": [
            {
                "h2": "Tabla comparativa NOM-004 vs NOM-024",
                "html": """<table class="items-table">
<thead><tr><th>Aspecto</th><th>NOM-004</th><th>NOM-024</th></tr></thead>
<tbody>
<tr><td>Enfoque</td><td>Contenido y manejo del expediente cl&iacute;nico</td><td>Sistemas electr&oacute;nicos de informaci&oacute;n en salud</td></tr>
<tr><td>Pregunta clave</td><td>&iquest;Qu&eacute; debe documentarse?</td><td>&iquest;C&oacute;mo debe protegerse e intercambiarse lo digital?</td></tr>
<tr><td>Aplica a</td><td>Establecimientos y consultorios que integran expediente</td><td>Sistemas de expediente electr&oacute;nico / informaci&oacute;n en salud</td></tr>
<tr><td>Para el psic&oacute;logo</td><td>Historia, notas, consentimientos, conservaci&oacute;n</td><td>Accesos, integridad, respaldos, trazabilidad</td></tr>
<tr><td>Formato</td><td>F&iacute;sico o electr&oacute;nico</td><td>Electr&oacute;nico (cuando el sistema es digital)</td></tr>
</tbody></table>
<p>En una frase: <strong>NOM-004 = qu&eacute; registrar</strong>; <strong>NOM-024 = c&oacute;mo el sistema electr&oacute;nico lo sostiene</strong>.</p>"""
            },
            {
                "h2": "Qu&eacute; exige la NOM-004 en consulta psicol&oacute;gica",
                "html": """<p>La NOM-004-SSA3-2012 establece c&oacute;mo integrar, archivar y proteger el expediente. En psicolog&iacute;a eso se traduce en identificaci&oacute;n del paciente, motivo de consulta, antecedentes, exploraci&oacute;n propia de la disciplina, impresiones, plan, evoluci&oacute;n y consentimientos, con identificaci&oacute;n del profesional. Detalle pr&aacute;ctico en <a href="/articulos/nom-004-historia-clinica-mexico.html">historia cl&iacute;nica seg&uacute;n NOM-004</a>.</p>
<p>Conservaci&oacute;n habitual de referencia: al menos cinco a&ntilde;os desde la &uacute;ltima atenci&oacute;n. El papel ordenado puede cumplir contenido; el problema aparece al migrar a digital sin controles.</p>
<ul>
<li>Contenido m&iacute;nimo por encuentro relevante.</li>
<li>Confidencialidad y acceso restringido.</li>
<li>Firma o equivalente del responsable.</li>
</ul>"""
            },
            {
                "h2": "Qu&eacute; aporta la NOM-024 al expediente electr&oacute;nico",
                "html": """<p>Cuando el expediente deja el papel, la NOM-024 orienta requisitos de sistemas: autenticaci&oacute;n de usuarios, integridad de registros, disponibilidad, respaldos y posibilidades de intercambio seguro. No sustituye la cl&iacute;nica; eleva el est&aacute;ndar t&eacute;cnico del <a href="/articulos/expediente-clinico-electronico-psicologos.html">expediente cl&iacute;nico electr&oacute;nico</a>.</p>
<p>Se&ntilde;ales de que su &laquo;Drive de PDFs&raquo; no alcanza el esp&iacute;ritu NOM-024:</p>
<ol>
<li>Una sola contrase&ntilde;a compartida.</li>
<li>Sin bit&aacute;cora de qui&eacute;n abri&oacute; o edit&oacute;.</li>
<li>Sin prueba de restauraci&oacute;n de respaldos.</li>
<li>Notas editables sin rastro de cambios.</li>
</ol>
<p>Combine con <a href="/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html">LFPDPPP</a>: la NOM habla de sistemas de salud; la ley de datos exige aviso, ARCO y seguridad del tratamiento.</p>"""
            },
            {
                "h2": "Checklist para psic&oacute;logos en consulta privada",
                "html": """<ol>
<li>Plantilla de historia y nota alineada a NOM-004.</li>
<li>Consentimiento informado archivado y recuperable.</li>
<li>Usuarios individuales en el software (sin cuentas gen&eacute;ricas).</li>
<li>Respaldo verificado en el &uacute;ltimo trimestre.</li>
<li>Pol&iacute;tica de retenci&oacute;n escrita (cl&iacute;nica + fiscal).</li>
<li>Aviso de privacidad LFPDPPP actualizado.</li>
</ol>
<p>Si busca un ECE orientado a psicolog&iacute;a con control de acceso y notas estructuradas, pruebe <a href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=nom-024-nom-004-psicologos-mexico">Kalyo</a> y contraste con su flujo actual durante dos semanas.</p>
<p>Recuerde: cumplir NOM-004 en papel y fallar seguridad digital, o tener software &laquo;bonito&raquo; sin contenido cl&iacute;nico, son dos extremos del mismo error. La respuesta correcta es contenido + sistema.</p>"""
            },
        ],
        "faqs": [
            {"q": "&iquest;La NOM-024 reemplaza a la NOM-004?", "a": "No. La NOM-004 sigue regulando el expediente cl&iacute;nico. La NOM-024 complementa el marco cuando el sistema es electr&oacute;nico. Ambas se leen juntas en digitalizaci&oacute;n."},
            {"q": "&iquest;Debo cumplir NOM-024 si solo uso papel?", "a": "El foco de NOM-024 es sistemas electr&oacute;nicos. En papel priorice NOM-004, confidencialidad y conservaci&oacute;n. Al digitalizar, eleve seguridad y trazabilidad."},
            {"q": "&iquest;Google Drive cumple NOM-024?", "a": "Como repositorio de PDFs suele carecer de bit&aacute;cora cl&iacute;nica, roles finos e integridad de notas. No equivale a un expediente electr&oacute;nico dise&ntilde;ado para salud."},
            {"q": "&iquest;Qu&eacute; norma cita un auditor primero?", "a": "En contenido cl&iacute;nico, NOM-004. Si el sistema es electr&oacute;nico, tambi&eacute;n se revisar&aacute;n accesos, respaldos e integridad alineados al esp&iacute;ritu NOM-024 y a LFPDPPP."},
            {"q": "&iquest;Kalyo sustituye asesor&iacute;a legal?", "a": "No. Es una herramienta de expediente y pr&aacute;ctica. Use esta gu&iacute;a como orientaci&oacute;n y consulte asesor&iacute;a para su caso espec&iacute;fico."},
        ],
        "related": [
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004 historia cl&iacute;nica"},
            {"href": "/articulos/expediente-clinico-electronico-psicologos.html", "label": "Expediente electr&oacute;nico"},
            {"href": "/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html", "label": "LFPDPPP psic&oacute;logos"},
            {"href": "/articulos/historia-clinica-psicologica-paso-a-paso.html", "label": "Historia cl&iacute;nica paso a paso"},
        ],
    },
    # 2 Nota evoluciÃ³n SOAP
    {
        "slug": "nota-evolucion-soap-psicologia",
        "title": "Nota de evolución psicología: guía formato SOAP | Kalyo",
        "description": "Nota de evolución psicología con formato SOAP: ejemplos reales, estructura clínica y buenas prácticas para documentar sesiones en el expediente digital.",
        "keywords": "nota de evolución psicología, nota SOAP psicología, formato SOAP, expediente clínico, documentación psicológica",
        "h1": "Nota de evolución psicología: formato SOAP con ejemplos",
        "breadcrumb_short": "Nota de evolución SOAP",
        "hero_alt": "Psicólogo redactando nota de evolución SOAP en expediente digital",
        "inline_alt": "Ejemplo de nota SOAP en psicología clínica",
        "meta_label": "Pr&aacute;ctica cl&iacute;nica &middot; Documentaci&oacute;n 2026",
        "date_published": "2026-11-14",
        "date_modified": "2026-11-14",
        "quick_answer": "La <strong>nota de evoluci&oacute;n en psicolog&iacute;a</strong> documenta cada sesi&oacute;n: qu&eacute; report&oacute; el paciente, qu&eacute; observ&oacute; el terapeuta, c&oacute;mo se interpreta y qu&eacute; plan sigue. El formato <strong>SOAP</strong> (Subjetivo, Objetivo, An&aacute;lisis, Plan) ordena esa informaci&oacute;n sin transcribir la sesi&oacute;n entera. Debe ser &uacute;til para continuidad, auditor&iacute;a y riesgo; no un diario &iacute;ntimo. En M&eacute;xico alinee con <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> y archive en un <a href=\"/articulos/expediente-clinico-electronico-psicologos.html\">expediente electr&oacute;nico</a> con autor&iacute;a clara.",
        "intro_long": "Muchas notas fallan por ser demasiado largas, vagas o tard&iacute;as. Esta gu&iacute;a muestra c&oacute;mo escribir una <strong>nota de evoluci&oacute;n psicolog&iacute;a</strong> con formato SOAP, ejemplos reales de seguimiento y errores frecuentes a evitar en consultorio. Complementa <a href=\"/articulos/nota-evolucion-psicologica.html\">la gu&iacute;a base de nota de evoluci&oacute;n</a> con un &aacute;ngulo operativo listo para el expediente digital diario.",
        "cta_h2": "Escribe notas SOAP en el expediente Kalyo",
        "cta_p": "Plantillas, historial y trazabilidad por sesi&oacute;n &mdash; kalyo.io",
        "card_title": "Nota de evolución SOAP en psicología",
        "card_p": "Formato SOAP, ejemplos reales y buenas prácticas para documentar sesiones.",
        "after_href": "/articulos/nota-evolucion-psicologica.html",
        "after_loc": "https://kalyo.io/articulos/nota-evolucion-psicologica.html",
        "asset_from": "nota-evolucion-psicologica",
        "sections": [
            {
                "h2": "Estructura SOAP aplicada a psicolog&iacute;a",
                "html": """<ul>
<li><strong>S &mdash; Subjetivo:</strong> lo que el paciente reporta (estado de &aacute;nimo, eventos, tareas).</li>
<li><strong>O &mdash; Objetivo:</strong> lo que usted observa (afecto, discurso, asistencia, escalas).</li>
<li><strong>A &mdash; An&aacute;lisis:</strong> formulaci&oacute;n breve, hip&oacute;tesis, riesgo, respuesta a intervenci&oacute;n.</li>
<li><strong>P &mdash; Plan:</strong> t&eacute;cnicas, tareas, pr&oacute;xima cita, derivaciones.</li>
</ul>
<p>Priorice datos que cambian decisiones cl&iacute;nicas. Evite copiar di&aacute;logos &iacute;ntimos innecesarios: protege privacidad y hace la nota legible meses despu&eacute;s.</p>"""
            },
            {
                "h2": "Ejemplo de nota SOAP (sesi&oacute;n de seguimiento)",
                "html": """<p><strong>S:</strong> Refiere ansiedad ante presentaci&oacute;n laboral; durmi&oacute; 5 h; practic&oacute; respiraci&oacute;n 3/7 d&iacute;as. Niega ideaci&oacute;n suicida actual.</p>
<p><strong>O:</strong> Contacto visual adecuado, habla r&aacute;pida al inicio, se calma al estructurar agenda. GAD-7 hoy: 11 (previo 14).</p>
<p><strong>A:</strong> Ansiedad anticipatoria laboral en descenso parcial; adherencia irregular a tarea. Sin indicadores de riesgo agudo. Mantiene metas de exposici&oacute;n gradual.</p>
<p><strong>P:</strong> Continuar TCC breve; tarea: ensayo de presentaci&oacute;n 2 veces; reevaluar GAD-7 en 2 semanas; cita 7 d&iacute;as.</p>
<p>Adapte el nivel de detalle a crisis o evaluaci&oacute;n de riesgo: ah&iacute; el apartado A y P deben ser m&aacute;s expl&iacute;citos.</p>"""
            },
            {
                "h2": "Errores frecuentes y c&oacute;mo corregirlos",
                "html": """<ol>
<li><strong>Nota al mes:</strong> escriba el mismo d&iacute;a; la memoria distorsiona.</li>
<li><strong>Solo &laquo;se trabaj&oacute; ansiedad&raquo;:</strong> diga qu&eacute; t&eacute;cnica y qu&eacute; respuesta observ&oacute;.</li>
<li><strong>Copiar chat de WhatsApp:</strong> use expediente con control de acceso.</li>
<li><strong>Omitir riesgo:</strong> registre exploraci&oacute;n aunque sea negativa.</li>
<li><strong>Plan gen&eacute;rico:</strong> una tarea observable supera tres intenciones vagas.</li>
</ol>
<p>Si usa IA para borradores, revise cl&iacute;nica y confidencialidad del proveedor; el profesional sigue siendo autor responsable. Vea tambi&eacute;n <a href="/articulos/notas-clinicas-inteligencia-artificial-psicologos.html">notas cl&iacute;nicas con IA</a>.</p>"""
            },
            {
                "h2": "Frecuencia, longitud y archivo digital",
                "html": """<p>En psicoterapia ambulatoria, una nota por sesi&oacute;n es el est&aacute;ndar. Longitud t&iacute;pica: medio p&aacute;rrafo por bloque SOAP en rutina; m&aacute;s en crisis. Firmela o autent&iacute;quela en el ECE. Conserve plazos legales/&eacute;ticos (en MX, referencia NOM-004 de cinco a&ntilde;os).</p>
<p>Un sistema como <a href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=nota-evolucion-soap-psicologia">Kalyo</a> permite plantillas SOAP, historial por paciente y menos notas perdidas en libretas o chats. La mejor nota es la que otro colega podr&iacute;a continuar ma&ntilde;ana sin llamarlo.</p>
<p>Revise trimestralmente si sus plantillas siguen sirviendo a su modelo (presencial, tele, pareja). Elimine campos decorativos que nunca completa: la nota debe ser sostenible.</p>"""
            },
        ],
        "faqs": [
            {"q": "&iquest;SOAP es obligatorio en psicolog&iacute;a?", "a": "No es el &uacute;nico formato v&aacute;lido, pero es un est&aacute;ndar claro y ense&ntilde;able. Lo obligatorio es documentar evoluci&oacute;n &uacute;til y conforme a su marco normativo/&eacute;tico."},
            {"q": "&iquest;Cu&aacute;nto debe medir la nota?", "a": "La suficiente para continuidad y riesgo. En rutina, breve y estructurada; en crisis, m&aacute;s detalle en an&aacute;lisis y plan. Evite transcripciones literales innecesarias."},
            {"q": "&iquest;Debo incluir puntajes de tests?", "a": "S&iacute;, cuando se aplicaron: instrumento, fecha y resultado orientativo. Ayuda a monitorear respuesta y respalda decisiones."},
            {"q": "&iquest;Puedo dictar la nota con el paciente presente?", "a": "Algunos lo hacen con consentimiento y cuidado de lenguaje. Otros prefieren minutos al cierre. Elija el m&eacute;todo que no degrade la alianza ni la calidad del registro."},
            {"q": "&iquest;Qu&eacute; hago si olvid&eacute; una sesi&oacute;n?", "a": "Documente lo recordable con honestidad y fecha real de registro. No invente. Ajuste el h&aacute;bito para que no se repita."},
        ],
        "related": [
            {"href": "/articulos/nota-evolucion-psicologica.html", "label": "Nota de evoluci&oacute;n (gu&iacute;a base)"},
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004"},
            {"href": "/articulos/firma-electronica-notas-clinicas-colombia.html", "label": "Firma electr&oacute;nica en notas"},
            {"href": "/articulos/expediente-clinico-electronico-psicologos.html", "label": "Expediente electr&oacute;nico"},
        ],
    },
    # 3 Historial clÃ­nico
    {
        "slug": "historial-clinico-psicologico-estructura",
        "title": "Historial clínico psicológico: estructura y guía | Kalyo",
        "description": "Historial clínico psicológico: estructura completa con secciones obligatorias, menores, teleconsulta, consentimiento y checklist para psicólogos en LATAM.",
        "keywords": "historial clínico psicológico, estructura historial clínico, historia clínica psicología, expediente psicológico, teleconsulta",
        "h1": "Historial clínico psicológico: estructura completa para consulta",
        "breadcrumb_short": "Historial clínico psicológico",
        "hero_alt": "Estructura de historial clínico psicológico en expediente digital",
        "inline_alt": "Secciones del historial clínico psicológico",
        "meta_label": "Pr&aacute;ctica cl&iacute;nica &middot; Expediente 2026",
        "date_published": "2026-11-14",
        "date_modified": "2026-11-14",
        "quick_answer": "El <strong>historial cl&iacute;nico psicol&oacute;gico</strong> integra identificaci&oacute;n, motivo de consulta, antecedentes, exploraci&oacute;n, formulaci&oacute;n, plan, consentimientos y evoluci&oacute;n. No es un formulario est&aacute;tico: se actualiza con el tratamiento. En M&eacute;xico alinee contenidos a <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a>; en menores documente tutores y asentimiento; en teleconsulta registre modalidad e identidad. Un <a href=\"/expediente-clinico-psicologico/\">expediente digital</a> facilita estructura y recuperaci&oacute;n.",
        "intro_long": "Abrir consulta con plantillas incompletas genera huecos legales y cl&iacute;nicos desde el primer mes. Esta gu&iacute;a detalla la <strong>estructura del historial cl&iacute;nico psicol&oacute;gico</strong>: secciones esenciales, menores de edad, teleconsulta y un checklist de auditor&iacute;a interna muy usable. Complementa <a href=\"/articulos/historia-clinica-psicologica-paso-a-paso.html\">historia paso a paso</a> con &eacute;nfasis en la arquitectura completa del expediente.",
        "cta_h2": "Estructura tu historial en Kalyo",
        "cta_p": "Secciones, consentimientos y evoluci&oacute;n en un solo expediente &mdash; kalyo.io",
        "card_title": "Historial clínico psicológico: estructura",
        "card_p": "Secciones, menores, teleconsulta y checklist para armar el expediente.",
        "after_href": "/articulos/historia-clinica-psicologica-paso-a-paso.html",
        "after_loc": "https://kalyo.io/articulos/historia-clinica-psicologica-paso-a-paso.html",
        "asset_from": "historia-clinica-psicologica-paso-a-paso",
        "sections": [
            {
                "h2": "Secciones esenciales del historial",
                "html": """<ol>
<li>Identificaci&oacute;n y contacto de emergencia.</li>
<li>Motivo de consulta (palabras del paciente).</li>
<li>Antecedentes personales, familiares y de tratamiento.</li>
<li>Exploraci&oacute;n del estado mental / evaluaci&oacute;n inicial.</li>
<li>Riesgo (suicida/heteroagresivo) cuando proceda.</li>
<li>Instrumentos aplicados y resultados orientativos.</li>
<li>Formulaci&oacute;n y plan terap&eacute;utico.</li>
<li>Consentimientos e informaci&oacute;n de privacidad.</li>
<li>Notas de evoluci&oacute;n (p. ej. <a href="/articulos/nota-evolucion-soap-psicologia.html">SOAP</a>).</li>
<li>Alta, referencias e informes a terceros autorizados.</li>
</ol>
<p>No todas las secciones se completan en la primera hora; s&iacute; debe quedar trazado el riesgo y el consentimiento b&aacute;sico desde el inicio.</p>"""
            },
            {
                "h2": "Menores de edad: tutores y asentimiento",
                "html": """<p>Documente qui&eacute;n autoriza el tratamiento, parentesco, custodia relevante y contacto. Explique l&iacute;mites de confidencialidad al menor seg&uacute;n edad y marco local. Conserve autorizaciones para informes escolares. Si hay conflicto entre cuidadores, registre qu&eacute; informaci&oacute;n se comparti&oacute; y con qu&eacute; base.</p>
<p>Evite mezclar en un solo archivo datos de hermanos sin necesidad. Separe expedientes aunque la familia comparta agenda.</p>"""
            },
            {
                "h2": "Teleconsulta: qu&eacute; agregar al historial",
                "html": """<p>Registre modalidad (video/audio), plataforma, verificaci&oacute;n de identidad y ubicaci&oacute;n aproximada del paciente si su protocolo lo pide. Anote limitaciones t&eacute;cnicas que afectaron la sesi&oacute;n. El contenido cl&iacute;nico (SOAP) no cambia; cambia el contexto de seguridad y consentimiento remoto.</p>
<p>Enlace &uacute;til: <a href="/articulos/telepsicologia-etica-mexico-colombia.html">telepsicolog&iacute;a &eacute;tica MX/CO</a>. Guarde consentimientos espec&iacute;ficos de modalidad a distancia cuando aplique.</p>"""
            },
            {
                "h2": "Checklist de apertura y auditor&iacute;a interna",
                "html": """<ul>
<li>Ficha completa antes de la tercera sesi&oacute;n (salvo crisis).</li>
<li>Consentimiento firmado o equivalente digital.</li>
<li>Plantilla de nota lista y usada el mismo d&iacute;a.</li>
<li>Pruebas con fecha, versi&oacute;n y puntaje.</li>
<li>Plan visible para el paciente en lenguaje claro.</li>
<li>Retenci&oacute;n y respaldo definidos.</li>
</ul>
<p>Centralice el historial en <a href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=historial-clinico-psicologico-estructura">Kalyo</a> para evitar versiones dispersas en papel, Drive y WhatsApp. Un historial &uacute;nico es m&aacute;s f&aacute;cil de defender y de continuar.</p>
<p>Revise anualmente si la estructura sigue cubriendo su poblaci&oacute;n (adultos, adolescentes, pareja). Quite campos muertos; agregue solo lo que usa.</p>"""
            },
        ],
        "faqs": [
            {"q": "&iquest;Historial e historia cl&iacute;nica son lo mismo?", "a": "En la pr&aacute;ctica se usan como sin&oacute;nimos del registro integral. Algunos reservan &laquo;historia&raquo; para la evaluaci&oacute;n inicial y &laquo;historial/expediente&raquo; para el conjunto con evoluci&oacute;n."},
            {"q": "&iquest;Cu&aacute;ntas sesiones lleva completar el historial?", "a": "Una a tres seg&uacute;n complejidad. Lo no negociable desde el d&iacute;a uno: riesgo, consentimiento e identificaci&oacute;n."},
            {"q": "&iquest;Debo incluir todo lo que el paciente cuenta?", "a": "No. Registre lo cl&iacute;nicamente pertinente. Evite detalles &iacute;ntimos superfluos que aumentan riesgo de filtraci&oacute;n sin aportar a la formulaci&oacute;n."},
            {"q": "&iquest;Qu&eacute; cambia en teleconsulta?", "a": "Modalidad, identidad, consentimiento remoto y limitaciones t&eacute;cnicas. El resto de la estructura cl&iacute;nica se mantiene."},
            {"q": "&iquest;Puedo usar plantillas de internet?", "a": "S&iacute;, si las adapta a su norma local, &eacute;tica y tipo de paciente. Revise menores, riesgo y consentimientos."},
        ],
        "related": [
            {"href": "/articulos/historia-clinica-psicologica-paso-a-paso.html", "label": "Historia cl&iacute;nica paso a paso"},
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004"},
            {"href": "/articulos/nota-evolucion-soap-psicologia.html", "label": "Nota SOAP"},
            {"href": "/articulos/consentimiento-informado-psicologia.html", "label": "Consentimiento informado"},
        ],
    },
    # 4 Factura DIAN
    {
        "slug": "factura-electronica-dian-psicologos-colombia",
        "title": "Factura electrónica DIAN para psicólogos clínicos | Kalyo",
        "description": "Factura electrónica DIAN para psicólogos en Colombia: requisitos, RIPS, consulta particular y checklist para facturar servicios de salud mental en 2026.",
        "keywords": "factura electrónica DIAN, factura electrónica psicólogos Colombia, RIPS, consulta particular, facturación salud mental",
        "h1": "Factura electrónica DIAN para psicólogos en Colombia",
        "breadcrumb_short": "Factura electrónica DIAN",
        "hero_alt": "Psicólogo colombiano emitiendo factura electrónica DIAN",
        "inline_alt": "Flujo factura electrónica DIAN y RIPS en psicología",
        "meta_label": "Cumplimiento legal &middot; Colombia 2026",
        "date_published": "2026-11-14",
        "date_modified": "2026-11-14",
        "quick_answer": "La <strong>factura electr&oacute;nica DIAN</strong> es el comprobante fiscal electr&oacute;nico obligatorio para quienes est&aacute;n obligados a facturar en Colombia. Los psic&oacute;logos en consulta particular suelen emitirla a personas naturales; si prestan servicios al sistema de salud, adem&aacute;s deben alinear <strong>RIPS</strong> y validaciones (p. ej. marco de la <a href=\"/articulos/resolucion-2275-rips-psicologos-colombia.html\">Resoluci&oacute;n 2275</a>). La regla pr&aacute;ctica: la factura cuenta lo cobrado; el expediente prueba lo atendido.",
        "intro_long": "Mezclar facturaci&oacute;n con notas incompletas genera glosas y mucho m&aacute;s estr&eacute;s fiscal al cierre de mes. Esta gu&iacute;a explica la <strong>factura electr&oacute;nica DIAN para psic&oacute;logos</strong> en Colombia: consulta particular versus sistema de salud, v&iacute;nculo con RIPS y checklist operativo concreto. Complementa <a href=\"/articulos/rips-registros-individuales-colombia.html\">RIPS</a> y la <a href=\"/articulos/resolucion-2275-rips-psicologos-colombia.html\">Resoluci&oacute;n 2275</a> con foco pr&aacute;ctico diario.",
        "cta_h2": "Documenta sesiones listas para facturar con Kalyo",
        "cta_p": "Expediente y agenda alineados a tu cierre de mes &mdash; kalyo.io",
        "card_title": "Factura electrónica DIAN para psicólogos",
        "card_p": "DIAN, RIPS, consulta particular y checklist de facturación en Colombia.",
        "after_href": "/articulos/resolucion-2275-rips-psicologos-colombia.html",
        "after_loc": "https://kalyo.io/articulos/resolucion-2275-rips-psicologos-colombia.html",
        "asset_from": "rips-registros-individuales-colombia",
        "sections": [
            {
                "h2": "Qui&eacute;n debe emitir factura electr&oacute;nica",
                "html": """<p>Depende de su calidad tributaria y del tipo de operaci&oacute;n. Muchos psic&oacute;logos independientes ya facturan electr&oacute;nicamente a trav&eacute;s de un software autorizado por la DIAN. Verifique con su contador si es responsable de IVA, no responsable, o si aplica documento equivalente en alg&uacute;n escenario espec&iacute;fico.</p>
<p>No improvise: el r&eacute;gimen cambia y las sanciones por no facturar cuando corresponde son costosas. Esta gu&iacute;a no sustituye asesor&iacute;a tributaria; ordena el lado cl&iacute;nico-operativo.</p>"""
            },
            {
                "h2": "Consulta particular vs servicios al sistema de salud",
                "html": """<ul>
<li><strong>Particular:</strong> factura al paciente; el expediente respalda la prestaci&oacute;n; RIPS puede no aplicar.</li>
<li><strong>EPS/IPS/convenio:</strong> factura + RIPS JSON/validaci&oacute;n seg&uacute;n reglas vigentes; el expediente debe cuadrar fechas, CUPS y diagn&oacute;sticos.</li>
</ul>
<p>Detalle normativo de RIPS en <a href="/articulos/rips-registros-individuales-colombia.html">RIPS Colombia</a> y <a href="/articulos/resolucion-2275-rips-psicologos-colombia.html">Resoluci&oacute;n 2275</a>. Separe agendas si atiende ambos mundos.</p>"""
            },
            {
                "h2": "Datos cl&iacute;nicos que debe cuadrar la factura",
                "html": """<p>Antes de emitir:</p>
<ol>
<li>Fecha de atenci&oacute;n = fecha en nota.</li>
<li>Concepto claro (consulta psicol&oacute;gica / evaluaci&oacute;n).</li>
<li>Identificaci&oacute;n correcta del adquirente.</li>
<li>Si hay RIPS: mismos servicios facturados que reportados.</li>
</ol>
<p>El error cl&aacute;sico es facturar un paquete de sesiones sin notas suficientes. Su contador emite el XML; usted aporta la verdad cl&iacute;nica.</p>"""
            },
            {
                "h2": "Checklist de cierre de mes para psic&oacute;logos",
                "html": """<ul>
<li>Notas de todas las sesiones cobradas.</li>
<li>Facturas emitidas y aceptadas.</li>
<li>CUV/soportes RIPS si aplica.</li>
<li>Conciliaci&oacute;n agenda &harr; cobranza &harr; expediente.</li>
<li>Resguardo de XML/PDF fiscales.</li>
</ul>
<p>Use <a href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=factura-electronica-dian-psicologos-colombia">Kalyo</a> para mantener expediente y citas ordenados mientras su facturador DIAN genera los comprobantes. Menos fricci&oacute;n entre cl&iacute;nica y contabilidad.</p>
<p>Capacite a quien factura en c&oacute;digos de psicolog&iacute;a; no asuma que el mismo flujo de medicina general aplica sin ajustes.</p>"""
            },
        ],
        "faqs": [
            {"q": "&iquest;Todo psic&oacute;logo en Colombia debe facturar electr&oacute;nicamente?", "a": "Depende de su obligaci&oacute;n tributaria. Consulte a su contador. Si est&aacute; obligado a facturar, el canal vigente es electr&oacute;nico v&iacute;a proveedor autorizado DIAN."},
            {"q": "&iquest;La factura reemplaza la historia cl&iacute;nica?", "a": "No. La factura es soporte fiscal/comercial; la historia documenta la atenci&oacute;n. Ambas deben ser coherentes en fechas y servicios."},
            {"q": "&iquest;Necesito RIPS si solo atiendo particulares?", "a": "Generalmente no para el d&iacute;a a d&iacute;a particular. S&iacute; cuando reporta al sistema de salud o convenios que lo exigen."},
            {"q": "&iquest;Puedo facturar sin software cl&iacute;nico?", "a": "S&iacute;, pero el riesgo de desalineaci&oacute;n agenda-nota-factura sube. Un expediente digital reduce glosas y omisiones."},
            {"q": "&iquest;Qu&eacute; guardo por cada factura?", "a": "XML/PDF, evidencia de aceptaci&oacute;n y, si aplica, CUV/RIPS del periodo, m&aacute;s la nota cl&iacute;nica correspondiente."},
        ],
        "related": [
            {"href": "/articulos/resolucion-2275-rips-psicologos-colombia.html", "label": "Resoluci&oacute;n 2275 RIPS"},
            {"href": "/articulos/rips-registros-individuales-colombia.html", "label": "RIPS Colombia"},
            {"href": "/articulos/como-abrir-consulta-privada-colombia.html", "label": "Abrir consulta en Colombia"},
            {"href": "/articulos/ley-1581-proteccion-datos-psicologia.html", "label": "Ley 1581"},
        ],
    },
    # 5 Firma electrÃ³nica
    {
        "slug": "firma-electronica-notas-clinicas-colombia",
        "title": "Firma electrónica en notas clínicas psicológicas | Kalyo",
        "description": "Firma electrónica en notas clínicas: validez legal, autoría, bitácora del expediente electrónico y buenas prácticas para psicólogos en Colombia y LATAM.",
        "keywords": "firma electrónica notas clínicas, firma electrónica Colombia, autoría expediente, bitácora ECE, notas psicológicas",
        "h1": "Firma electrónica en notas clínicas: validez y autoría",
        "breadcrumb_short": "Firma electrónica en notas",
        "hero_alt": "Firma electrónica de nota clínica en expediente psicológico",
        "inline_alt": "Bitácora y autoría en notas clínicas electrónicas",
        "meta_label": "Cumplimiento legal &middot; Colombia / LATAM 2026",
        "date_published": "2026-11-14",
        "date_modified": "2026-11-14",
        "quick_answer": "La <strong>firma electr&oacute;nica en notas cl&iacute;nicas</strong> busca demostrar <em>autor&iacute;a e integridad</em>: qui&eacute;n registr&oacute; la atenci&oacute;n y que el texto no se alter&oacute; sin rastro. En un expediente electr&oacute;nico esto suele lograrse con autenticaci&oacute;n fuerte, sello de tiempo y bit&aacute;cora de cambios; no siempre requiere firma digital certificada de alto nivel. En Colombia, alinee pr&aacute;ctica con historia cl&iacute;nica, <a href=\"/articulos/ley-1581-proteccion-datos-psicologia.html\">Ley 1581</a> y pol&iacute;ticas institucionales. Evite &laquo;firmar&raquo; pegando una imagen PNG en un Word compartido.",
        "intro_long": "Sin autor&iacute;a clara, la nota pierde valor ante auditor&iacute;a, glosa o cualquier tipo de disputa legal. Esta gu&iacute;a explica la <strong>firma electr&oacute;nica en notas cl&iacute;nicas</strong> para psic&oacute;logos cl&iacute;nicos: niveles de firma, bit&aacute;cora del ECE y checklist de implementaci&oacute;n en consulta privada. Complementa <a href=\"/articulos/expediente-clinico-electronico-psicologos.html\">expediente electr&oacute;nico</a> y <a href=\"/articulos/nota-evolucion-soap-psicologia.html\">notas SOAP</a> con foco en integridad.",
        "cta_h2": "Autenticidad de notas en Kalyo",
        "cta_p": "Usuarios individuales, historial y expediente trazable &mdash; kalyo.io",
        "card_title": "Firma electrónica en notas clínicas",
        "card_p": "Validez, autoría, bitácora y buenas prácticas en expediente electrónico.",
        "after_href": "/articulos/expediente-clinico-electronico-psicologos.html",
        "after_loc": "https://kalyo.io/articulos/expediente-clinico-electronico-psicologos.html",
        "asset_from": "expediente-clinico-electronico-psicologos",
        "sections": [
            {
                "h2": "Qu&eacute; problema resuelve la firma electr&oacute;nica",
                "html": """<p>Tres riesgos t&iacute;picos:</p>
<ul>
<li>No saber qui&eacute;n escribi&oacute; la nota.</li>
<li>Notas editadas despu&eacute;s sin dejar rastro.</li>
<li>Cuentas compartidas (&laquo;consultorio1&raquo;) que anulan responsabilidad.</li>
</ul>
<p>La firma/autenticaci&oacute;n vincula persona &rarr; registro &rarr; momento. Es tan importante como el contenido SOAP.</p>"""
            },
            {
                "h2": "Niveles: simple, avanzada y certificada",
                "html": """<p>En t&eacute;rminos pr&aacute;cticos para consultorio:</p>
<ol>
<li><strong>Simple:</strong> login + registro de usuario/fecha (m&iacute;nimo en ECE serio).</li>
<li><strong>Avanzada:</strong> factores adicionales (MFA), control de integridad, pol&iacute;ticas de no repudio mejoradas.</li>
<li><strong>Certificada / cualificada:</strong> certificados emitidos por entidades de certificaci&oacute;n; suele pedirse en contextos institucionales espec&iacute;ficos.</li>
</ol>
<p>No compre el nivel m&aacute;s caro sin requisito: primero cierre el m&iacute;nimo (usuario &uacute;nico + bit&aacute;cora). Consulte a su IPS o asesor si un pagador exige un tipo particular.</p>"""
            },
            {
                "h2": "Bit&aacute;cora del ECE: el complemento imprescindible",
                "html": """<p>Una firma sin log es d&eacute;bil. El sistema debe registrar altas, ediciones y accesos relevantes. Las correcciones se hacen con addendum, no borrando la historia. Eso protege al paciente y al profesional.</p>
<p>Combine con <a href="/articulos/nota-evolucion-soap-psicologia.html">buena nota SOAP</a>: firmar basura sigue siendo basura. La calidad cl&iacute;nica y la autor&iacute;a van juntas.</p>"""
            },
            {
                "h2": "Checklist de implementaci&oacute;n en consulta",
                "html": """<ul>
<li>Usuario individual por profesional y asistente.</li>
<li>Prohibido compartir contrase&ntilde;as.</li>
<li>MFA si el software lo permite.</li>
<li>Pol&iacute;tica de correcci&oacute;n/addendum escrita.</li>
<li>Prueba anual de exportaci&oacute;n e integridad.</li>
</ul>
<p><a href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=firma-electronica-notas-clinicas-colombia">Kalyo</a> ayuda a mantener notas ligadas a usuarios y expediente &uacute;nico, base de cualquier esquema de firma electr&oacute;nica cre&iacute;ble en consultorio.</p>
<p>En Colombia, alinear tambi&eacute;n protecci&oacute;n de datos (<a href="/articulos/ley-1581-proteccion-datos-psicologia.html">Ley 1581</a>) y, si factura a salud, coherencia con RIPS.</p>"""
            },
        ],
        "faqs": [
            {"q": "&iquest;Pegar una imagen de firma en PDF es suficiente?", "a": "Suele ser d&eacute;bil: no prueba identidad ni integridad. Prefiera autenticaci&oacute;n de usuario + registro inmutable o mecanismos del ECE."},
            {"q": "&iquest;Necesito certificado digital siempre?", "a": "No siempre. Muchas consultas privadas inician con autenticaci&oacute;n robusta y bit&aacute;cora. Verifique requisitos de su instituci&oacute;n o pagador."},
            {"q": "&iquest;Puedo editar una nota ya firmada?", "a": "Corrija con addendum o nueva entrada fechada. Evite reescribir silenciosamente el pasado."},
            {"q": "&iquest;Qu&eacute; pasa con practicantes?", "a": "Cada uno con usuario propio; supervisiones documentadas. No use la cuenta del titular para notas ajenas."},
            {"q": "&iquest;La firma electr&oacute;nica reemplaza el consentimiento?", "a": "No. Son actos distintos: uno autentica la nota; el otro documenta aceptaci&oacute;n del tratamiento/datos."},
        ],
        "related": [
            {"href": "/articulos/expediente-clinico-electronico-psicologos.html", "label": "Expediente electr&oacute;nico"},
            {"href": "/articulos/nota-evolucion-soap-psicologia.html", "label": "Nota SOAP"},
            {"href": "/articulos/ley-1581-proteccion-datos-psicologia.html", "label": "Ley 1581"},
            {"href": "/articulos/nom-024-nom-004-psicologos-mexico.html", "label": "NOM-024 vs NOM-004"},
        ],
    },
    # 6 Tiempo conservar
    {
        "slug": "tiempo-conservar-expediente-clinico",
        "title": "¿Cuánto tiempo conservar el expediente clínico? | Kalyo",
        "description": "Cuánto tiempo conservar el expediente clínico en México, Colombia y Chile: plazos numéricos por país, ARCO frente a retención y checklist de archivo seguro.",
        "keywords": "tiempo conservar expediente clínico, cuánto tiempo se guarda el expediente, NOM-004, retención historia clínica, México Colombia Chile",
        "h1": "Cuánto tiempo conservar el expediente clínico (MX, CO, CL)",
        "breadcrumb_short": "Tiempo conservar expediente",
        "hero_alt": "Plazos de conservación del expediente clínico en LATAM",
        "inline_alt": "Tabla de plazos de retención de expediente clínico",
        "meta_label": "Cumplimiento legal &middot; MX / CO / CL 2026",
        "date_published": "2026-11-14",
        "date_modified": "2026-11-14",
        "quick_answer": "<strong>M&eacute;xico:</strong> referencia habitual de la NOM-004 &mdash; m&iacute;nimo <strong>5 a&ntilde;os</strong> desde la &uacute;ltima atenci&oacute;n. <strong>Colombia:</strong> conserve seg&uacute;n normas de historia cl&iacute;nica e institucionales (con frecuencia plazos largos en salud; verifique su IPS/c&oacute;digo &eacute;tico) y no borre solo por petici&oacute;n ARCO si hay deber de retenci&oacute;n. <strong>Chile:</strong> aplique normativa sanitaria y &eacute;tica del colegio/entidad; documente su pol&iacute;tica interna. Respuesta corta: <em>defina un m&iacute;nimo escrito &ge;5 a&ntilde;os y no destruya antes sin revisi&oacute;n legal</em>.",
        "intro_long": "La pregunta &laquo;&iquest;cu&aacute;nto tiempo guardar el expediente?&raquo; busca un n&uacute;mero usable y defendible ante el paciente. Esta gu&iacute;a da plazos de referencia claros para <strong>M&eacute;xico, Colombia y Chile</strong>, la tensi&oacute;n con derechos ARCO o Habeas Data, y un checklist de archivo seguro. Enlaza <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> y <a href=\"/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html\">LFPDPPP</a> para el d&iacute;a a d&iacute;a.",
        "cta_h2": "Archiva y reten con Kalyo",
        "cta_p": "Expediente digital con respaldos y control de acceso &mdash; kalyo.io",
        "card_title": "Tiempo de conservar el expediente clínico",
        "card_p": "Plazos MX/CO/CL, ARCO vs retención y checklist de archivo seguro.",
        "after_href": "/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html",
        "after_loc": "https://kalyo.io/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html",
        "asset_from": "lfpdppp-proteccion-datos-psicologos-mexico",
        "sections": [
            {
                "h2": "Plazos de referencia por pa&iacute;s",
                "html": """<table class="items-table">
<thead><tr><th>Pa&iacute;s</th><th>Referencia pr&aacute;ctica</th><th>Notas</th></tr></thead>
<tbody>
<tr><td>M&eacute;xico</td><td><strong>5 a&ntilde;os</strong> m&iacute;nimo (NOM-004)</td><td>Desde &uacute;ltima atenci&oacute;n; confirme su contexto</td></tr>
<tr><td>Colombia</td><td>Seg&uacute;n historia cl&iacute;nica / entidad</td><td>No asuma borrado inmediato por Habeas Data</td></tr>
<tr><td>Chile</td><td>Norma sanitaria + &eacute;tica profesional</td><td>Documente pol&iacute;tica interna del consultorio</td></tr>
</tbody></table>
<p>Si atiende menores o hay litigio, consulte plazos m&aacute;s largos antes de destruir.</p>"""
            },
            {
                "h2": "ARCO / Habeas Data vs deber de conservaci&oacute;n",
                "html": """<p>El paciente puede pedir acceso o cancelaci&oacute;n de datos, pero el deber de conservar historia cl&iacute;nica puede prevalecer durante el plazo legal. Explique la tensi&oacute;n, ofrezca copia y limite usos secundarios. Gu&iacute;a MX: <a href="/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html">LFPDPPP</a>; CO: <a href="/articulos/ley-1581-proteccion-datos-psicologia.html">Ley 1581</a>.</p>"""
            },
            {
                "h2": "Qu&eacute; conservar (y qu&eacute; no mezclar)",
                "html": """<ul>
<li>Historia, notas, consentimientos, tests, informes emitidos.</li>
<li>Evidencias de entrega de avisos/consentimientos.</li>
<li>Separar archivo fiscal (facturas) del cl&iacute;nico si es viable.</li>
</ul>
<p>No guarde chats personales como &laquo;expediente&raquo;. Migre a ECE con retenci&oacute;n definida.</p>"""
            },
            {
                "h2": "Checklist de retenci&oacute;n y destrucci&oacute;n segura",
                "html": """<ol>
<li>Pol&iacute;tica escrita con plazo por tipo de registro.</li>
<li>Inventario de d&oacute;nde viven los datos.</li>
<li>Respaldo cifrado y prueba de restauraci&oacute;n.</li>
<li>Calendario de revisi&oacute;n anual de archivos vencidos.</li>
<li>Destrucci&oacute;n segura (digital y papel) con registro.</li>
</ol>
<p>Un <a href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=tiempo-conservar-expediente-clinico">expediente en Kalyo</a> facilita saber qu&eacute; pacientes est&aacute;n activos y cu&aacute;les llevan a&ntilde;os sin atenci&oacute;n, base para aplicar retenci&oacute;n sin caos.</p>
<p>Cuando dude entre borrar o guardar, conserve y documente la consulta legal: destruir temprano es irreversible.</p>"""
            },
        ],
        "faqs": [
            {"q": "&iquest;Cu&aacute;ntos a&ntilde;os debo guardar el expediente en M&eacute;xico?", "a": "La referencia habitual de NOM-004 es m&iacute;nimo cinco a&ntilde;os desde la &uacute;ltima atenci&oacute;n. Confirme su contexto y otros plazos aplicables."},
            {"q": "&iquest;Si el paciente pide borrar todo, debo hacerlo ya?", "a": "No autom&aacute;ticamente. Puede haber deber de conservaci&oacute;n cl&iacute;nica. Explique, ofrezca copia y limite usos no esenciales."},
            {"q": "&iquest;El plazo es igual en Colombia y Chile?", "a": "No copie el n&uacute;mero de M&eacute;xico sin revisar. Use tabla de referencia y valide con norma local / entidad."},
            {"q": "&iquest;Debo guardar tambi&eacute;n facturas cinco a&ntilde;os?", "a": "Los plazos fiscales pueden diferir de los cl&iacute;nicos. Consulte a su contador y documente ambas pol&iacute;ticas."},
            {"q": "&iquest;C&oacute;mo destruyo un expediente digital?", "a": "Con procedimiento documentado: baja l&oacute;gica/f&iacute;sica seg&uacute;n el sistema, sin dejar copias en correos o discos personales."},
        ],
        "related": [
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004"},
            {"href": "/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html", "label": "LFPDPPP"},
            {"href": "/articulos/ley-1581-proteccion-datos-psicologia.html", "label": "Ley 1581"},
            {"href": "/articulos/expediente-clinico-electronico-psicologos.html", "label": "Expediente electr&oacute;nico"},
        ],
    },
    # 7 CancelaciÃ³n / no-shows
    {
        "slug": "politica-cancelacion-no-show-psicologia",
        "title": "Política de cancelación y no-shows del psicólogo | Kalyo",
        "description": "Política de cancelación y no-shows en psicología: honorarios, recordatorios, agenda y cláusulas claras para reducir inasistencias en consulta privada.",
        "keywords": "política de cancelación psicólogo, no-show psicología, inasistencias consulta, honorarios cancelación, agenda psicólogos",
        "h1": "Política de cancelación y no-shows en psicología",
        "breadcrumb_short": "Cancelación y no-shows",
        "hero_alt": "Agenda psicológica con política de cancelación y recordatorios",
        "inline_alt": "Ejemplo de política de cancelación en consulta psicológica",
        "meta_label": "Pr&aacute;ctica privada &middot; Operaciones 2026",
        "date_published": "2026-11-14",
        "date_modified": "2026-11-14",
        "quick_answer": "Una <strong>pol&iacute;tica de cancelaci&oacute;n y no-shows</strong> define con cu&aacute;nta anticipaci&oacute;n se puede cancelar o reprogramar, qu&eacute; ocurre si el paciente no asiste y c&oacute;mo se cobran honorarios. Debe comunicarse en el encuadre y consentimiento, aplicarse con consistencia &eacute;tica y acompa&ntilde;arse de recordatorios de agenda. Reduce vac&iacute;os en la agenda sin castigar crisis reales. Comb&iacute;nela con una <a href=\"/articulos/agenda-para-psicologos.html\">agenda profesional</a> y recordatorios automatizados.",
        "intro_long": "Los no-shows erosionan ingresos y continuidad terap&eacute;utica en consulta privada cada mes. Esta gu&iacute;a propone una <strong>pol&iacute;tica de cancelaci&oacute;n</strong> clara y muy aplicable: plazos exactos, cobros &eacute;ticos, excepciones humanas y recordatorios de agenda. Complementa <a href=\"/articulos/reducir-inasistencias-consulta-psicologica.html\">c&oacute;mo reducir inasistencias</a> con plantilla de cl&aacute;usulas listas para el encuadre y el consentimiento informado.",
        "cta_h2": "Agenda y recordatorios con Kalyo",
        "cta_p": "Menos no-shows con citas y expediente en un solo lugar &mdash; kalyo.io",
        "card_title": "Política de cancelación y no-shows",
        "card_p": "Honorarios, recordatorios, agenda y cláusulas para consulta privada.",
        "after_href": "/articulos/reducir-inasistencias-consulta-psicologica.html",
        "after_loc": "https://kalyo.io/articulos/reducir-inasistencias-consulta-psicologica.html",
        "asset_from": "reducir-inasistencias-consulta-psicologica",
        "sections": [
            {
                "h2": "Elementos m&iacute;nimos de la pol&iacute;tica",
                "html": """<ol>
<li>Plazo de cancelaci&oacute;n/reprogramaci&oacute;n (p. ej. 24 o 48 h).</li>
<li>Consecuencia del no-show (cobro total, parcial o p&eacute;rdida de se&ntilde;a).</li>
<li>Excepciones (emergencia m&eacute;dica, duelo, fuerza mayor) y c&oacute;mo se acreditan.</li>
<li>Canal oficial para avisar (no solo stories de WhatsApp).</li>
<li>Cu&aacute;ndo se cobra anticipado o se pide tarjeta en archivo.</li>
</ol>
<p>Escr&iacute;bala en lenguaje claro y rev&iacute;sela en la primera sesi&oacute;n. Incl&uacute;yala en el <a href="/articulos/consentimiento-informado-psicologia.html">consentimiento informado</a>.</p>"""
            },
            {
                "h2": "Honorarios: cobro &eacute;tico vs castigo",
                "html": """<p>El cobro por cancelaci&oacute;n tard&iacute;a compensa el tiempo reservado, no &laquo;castiga&raquo; al paciente. Aplique la misma regla a todos, con margen humano en crisis. Evite renegociar caso por caso sin criterio: genera resentimiento y excepciones opacas.</p>
<p>Ejemplo de cl&aacute;usula corta: &laquo;Cancelaciones con menos de 24 h o inasistencias se cobran al 100% de la sesi&oacute;n, salvo emergencia documentada.&raquo; Ad&aacute;ptela a su contexto legal y de mercado (MX/CO/CL).</p>"""
            },
            {
                "h2": "Recordatorios y agenda: prevenci&oacute;n del no-show",
                "html": """<p>La mejor pol&iacute;tica es la que casi no se usa. Implemente:</p>
<ul>
<li>Confirmaci&oacute;n 48 h y recordatorio 2&ndash;3 h antes.</li>
<li>Enlace f&aacute;cil para reprogramar.</li>
<li>Lista de espera para huecos.</li>
<li>L&iacute;mite de no-shows antes de revisar el encuadre.</li>
</ul>
<p>M&aacute;s t&aacute;cticas en <a href="/articulos/reducir-inasistencias-consulta-psicologica.html">reducir inasistencias</a>. Una <a href="/articulos/agenda-para-psicologos.html">agenda para psic&oacute;logos</a> centralizada evita dobles reservas y olvidos del propio terapeuta.</p>"""
            },
            {
                "h2": "Plantilla breve para consentimientos",
                "html": """<p>Incluya en su documento de encuadre:</p>
<ul>
<li>Duraci&oacute;n y honorario de la sesi&oacute;n.</li>
<li>Plazo de cancelaci&oacute;n.</li>
<li>Pol&iacute;tica de no-show.</li>
<li>Medio de aviso v&aacute;lido.</li>
<li>Excepciones y c&oacute;mo solicitarlas.</li>
</ul>
<p>Con <a href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=politica-cancelacion-no-show-psicologia">Kalyo</a> puede unir agenda, recordatorios y expediente para que la pol&iacute;tica no viva solo en un PDF olvidado. Mida tasa de no-show mensual y ajuste plazos si su poblaci&oacute;n lo requiere.</p>
<p>Revise la pol&iacute;tica cada a&ntilde;o o al cambiar de modalidad (presencial a h&iacute;brida). Lo que funciona en terapia semanal puede fallar en evaluaciones &uacute;nicas.</p>"""
            },
        ],
        "faqs": [
            {"q": "&iquest;Es &eacute;tico cobrar un no-show?", "a": "S&iacute;, si se inform&oacute; con claridad, se aplica con consistencia y hay margen para emergencias reales. El objetivo es cuidar el encuadre y la agenda, no castigar."},
            {"q": "&iquest;24 o 48 horas de anticipaci&oacute;n?", "a": "Ambas son comunes. Elija seg&uacute;n su demanda y comun&iacute;quelo. Lo cr&iacute;tico es la claridad, no el n&uacute;mero exacto."},
            {"q": "&iquest;Qu&eacute; hago con pacientes en crisis que cancelan tarde?", "a": "Priorice seguridad y contenci&oacute;n. Puede exceptuar el cobro y documentar el criterio. Ofrezca reprogramaci&oacute;n pronta."},
            {"q": "&iquest;Los recordatorios por WhatsApp bastan?", "a": "Ayudan, pero conviene canal predecible y registro. Automatizar desde la agenda reduce olvidos del terapeuta."},
            {"q": "&iquest;Debo pedirlo firmado?", "a": "S&iacute;: incl&uacute;yalo en consentimiento/encuadre. La firma o aceptaci&oacute;n digital evita malentendidos posteriores."},
        ],
        "related": [
            {"href": "/articulos/reducir-inasistencias-consulta-psicologica.html", "label": "Reducir inasistencias"},
            {"href": "/articulos/agenda-para-psicologos.html", "label": "Agenda para psic&oacute;logos"},
            {"href": "/articulos/consentimiento-informado-psicologia.html", "label": "Consentimiento informado"},
            {"href": "/articulos/encuadre-terapeutico.html", "label": "Encuadre terap&eacute;utico"},
        ],
    },
]


def copy_assets(slug: str, src_slug: str) -> None:
    for kind in ("hero", "inline"):
        for ext in ("jpg", "webp"):
            src = ASSETS / f"{src_slug}-{kind}.{ext}"
            dst = ASSETS / f"{slug}-{kind}.{ext}"
            if not src.exists():
                # try alternate common assets
                continue
            if not dst.exists():
                shutil.copy2(src, dst)


def ensure_assets(slug: str, src_slug: str) -> None:
    copy_assets(slug, src_slug)
    # fallbacks if source missing
    for fb in (
        "nom-004-historia-clinica-mexico",
        "nota-evolucion-psicologica",
        "rips-registros-individuales-colombia",
        "expediente-clinico-electronico-psicologos",
        "lfpdppp-proteccion-datos-psicologos-mexico",
        "consentimiento-informado-psicologia",
        "agenda-para-psicologos",
    ):
        missing = any(
            not (ASSETS / f"{slug}-{kind}.{ext}").exists()
            for kind in ("hero", "inline")
            for ext in ("jpg", "webp")
        )
        if missing:
            copy_assets(slug, fb)


def publish(spec: dict) -> dict:
    slug = spec["slug"]
    SPECS_DIR.mkdir(parents=True, exist_ok=True)
    render_spec = {
        k: v
        for k, v in spec.items()
        if k not in {"card_title", "card_p", "after_href", "after_loc", "asset_from"}
    }
    (SPECS_DIR / f"{slug}.json").write_text(
        json.dumps(render_spec, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    html = render(render_spec)
    (ART / f"{slug}.html").write_text(html, encoding="utf-8")
    ensure_assets(slug, spec["asset_from"])

    info = verify(slug)
    print(json.dumps(info, ensure_ascii=False))

    if f'href="/articulos/{slug}.html"' not in (ART / "index.html").read_text(encoding="utf-8"):
        card = (
            f'      <a href="/articulos/{slug}.html" class="blog-card">\n'
            f'        <span class="blog-card-tag">Gu&iacute;a normativa</span>\n'
            f'        <h3>{spec["card_title"]}</h3>\n'
            f'        <p>{spec["card_p"]}</p>\n'
            f"      </a>\n"
        )
        insert_card(spec["after_href"], card)
        bump_counts(1)
    else:
        print("card exists, skip bump")

    insert_sitemap(spec["after_loc"], f"https://kalyo.io/articulos/{slug}.html", lastmod="2026-11-14")
    print("UPDATED", slug)
    return info


def main() -> None:
    # Prefer existing assets for nota/historial if slug assets exist under different names
    asset_aliases = {
        "nota-evolucion-psicologica": [
            "nota-evolucion-psicologica",
            "notas-de-sesion-psicologica",
        ],
        "historia-clinica-psicologica-paso-a-paso": [
            "historia-clinica-psicologica-paso-a-paso",
            "expediente-psicologico-estructura",
            "nom-004-historia-clinica-mexico",
        ],
        "reducir-inasistencias-consulta-psicologica": [
            "reducir-inasistencias-consulta-psicologica",
            "agenda-para-psicologos",
            "agenda-online-psicologos",
        ],
    }
    for spec in SPECS:
        intro_w = helper_word_count(spec["intro_long"])
        print(
            f"PRECHECK {spec['slug']}: title={len(spec['title'])} "
            f"desc={len(spec['description'])} intro={intro_w}"
        )
        if not (55 <= len(spec["title"]) <= 60):
            raise SystemExit(f"title length {len(spec['title'])}: {spec['title']}")
        if not (150 <= len(spec["description"]) <= 160):
            raise SystemExit(f"desc length {len(spec['description'])}")
        if not (50 <= intro_w <= 60):
            raise SystemExit(f"intro words {intro_w}")
        # resolve asset_from aliases
        src = spec["asset_from"]
        for cand in asset_aliases.get(src, [src]):
            if (ASSETS / f"{cand}-hero.jpg").exists():
                spec["asset_from"] = cand
                break
        publish(spec)


if __name__ == "__main__":
    main()
