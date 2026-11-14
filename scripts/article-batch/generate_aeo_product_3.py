#!/usr/bin/env python3
"""Generate 3 high-AEO product/compliance articles for Kalyo."""
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
    {
        "slug": "lfpdppp-proteccion-datos-psicologos-mexico",
        "title": "LFPDPPP para psicólogos: guía de datos clínicos | Kalyo",
        "description": "LFPDPPP para psicólogos en México: avisos de privacidad, consentimiento, seguridad del expediente clínico y checklist de cumplimiento en consulta privada.",
        "keywords": "LFPDPPP, protección de datos psicólogos México, aviso de privacidad consulta psicológica, expediente clínico datos personales, ARCO psicólogos",
        "h1": "LFPDPPP para psicólogos: cómo proteger datos clínicos en consulta",
        "breadcrumb_short": "LFPDPPP para psicólogos",
        "hero_alt": "Psicólogo revisando aviso de privacidad y expediente clínico digital en México",
        "inline_alt": "Checklist LFPDPPP para consultorio psicológico privado",
        "meta_label": "Cumplimiento legal &middot; M&eacute;xico 2026",
        "date_published": "2026-11-14",
        "date_modified": "2026-11-14",
        "quick_answer": "La <strong>LFPDPPP</strong> (Ley Federal de Protecci&oacute;n de Datos Personales en Posesi&oacute;n de los Particulares) obliga a todo psic&oacute;logo en consulta privada en M&eacute;xico a tratar datos de pacientes con base legal, aviso de privacidad, medidas de seguridad y canales ARCO. El expediente cl&iacute;nico concentra datos sensibles de salud: no basta con &laquo;ser &eacute;tico&raquo;; debe documentar finalidades, consentimientos, accesos y retenci&oacute;n. Un <a href=\"/expediente-clinico-psicologico/\">expediente digital con control de acceso</a> facilita demostrar cumplimiento ante el paciente o la autoridad.",
        "intro_long": "Muchos psic&oacute;logos en M&eacute;xico creen que la confidencialidad &eacute;tica basta ante la ley de datos. No: la <strong>LFPDPPP</strong> exige aviso de privacidad, seguridad y canal ARCO. Esta gu&iacute;a traduce la norma al consultorio: qu&eacute; recolectar, c&oacute;mo consentir el expediente digital y c&oacute;mo responder solicitudes del paciente. Incluye checklist y enlaces a <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> y <a href=\"/articulos/consentimiento-informado-psicologia-mexico.html\">consentimiento</a>.",
        "cta_h2": "Protege el expediente de tus pacientes con Kalyo",
        "cta_p": "Control de acceso, respaldos y consentimiento digital en una sola plataforma &mdash; kalyo.io",
        "card_title": "LFPDPPP para psicólogos en México",
        "card_p": "Aviso de privacidad, ARCO, seguridad del expediente y checklist LFPDPPP para consulta privada.",
        "after_href": "/articulos/ley-1581-proteccion-datos-psicologia.html",
        "after_loc": "https://kalyo.io/articulos/ley-1581-proteccion-datos-psicologia.html",
        "asset_from": "ley-1581-proteccion-datos-psicologia",
        "sections": [
            {
                "h2": "Qu&eacute; es la LFPDPPP y por qu&eacute; aplica a psic&oacute;logos",
                "html": """<p>La <strong>LFPDPPP</strong> regula c&oacute;mo particulares (personas f&iacute;sicas o morales) tratan datos personales en M&eacute;xico. Un psic&oacute;logo en pr&aacute;ctica privada es responsable del tratamiento: identifica pacientes, guarda notas, resultados de tests, datos de contacto, facturaci&oacute;n y, a menudo, informaci&oacute;n de familiares. Los datos de salud son <em>datos personales sensibles</em>: el est&aacute;ndar de cuidado es m&aacute;s alto que para un correo de marketing.</p>
<p>La ley no sustituye el secreto profesional ni la <a href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a>; se suma a ellos. La NOM-004 define contenido y conservaci&oacute;n del expediente; la LFPDPPP define c&oacute;mo informar, proteger y atender derechos del titular. En telepsicolog&iacute;a o plataformas en la nube, adem&aacute;s debe revisar d&oacute;nde se alojan los datos y con qui&eacute;n se comparten (proveedores, pasarelas de pago, herramientas de videollamada).</p>
<ul>
<li><strong>Responsable:</strong> el psic&oacute;logo o el consultorio que decide sobre el tratamiento.</li>
<li><strong>Encargado:</strong> un software o contador que trata datos por instrucci&oacute;n (con contrato).</li>
<li><strong>Titular:</strong> el paciente (o tutor) cuyos datos se tratan.</li>
</ul>
<p>Si trabaja en instituci&oacute;n p&uacute;blica, puede aplicar el r&eacute;gimen de datos en posesi&oacute;n de sujetos obligados; esta gu&iacute;a se centra en consulta privada y consultorios particulares.</p>"""
            },
            {
                "h2": "Aviso de privacidad: qu&eacute; debe decir en consulta",
                "html": """<p>Antes o al inicio del tratamiento, entregue un <strong>aviso de privacidad</strong> comprensible. No es el mismo documento que el <a href="/articulos/consentimiento-informado-psicologia-mexico.html">consentimiento informado cl&iacute;nico</a>, aunque pueden firmarse juntos. El aviso debe explicar, como m&iacute;nimo:</p>
<ol>
<li>Identidad y domicilio del responsable.</li>
<li>Finalidades primarias (atenci&oacute;n cl&iacute;nica, expediente, facturaci&oacute;n, recordatorios de cita).</li>
<li>Finalidades secundarias, si las hay (investigaci&oacute;n, marketing, supervisi&oacute;n con datos identificables), con opci&oacute;n de negarse.</li>
<li>Transferencias a terceros (psiquiatra co-tratante, laboratorio, aseguradora, software en la nube).</li>
<li>Medios para ejercer derechos ARCO y revocar consentimiento.</li>
</ol>
<p>Use lenguaje claro. Evite copiar avisos de e-commerce: el paciente necesita saber qu&eacute; pasa con sus notas, tests y grabaciones de sesi&oacute;n (si existen). Conserve evidencia de que el aviso fue puesto a disposici&oacute;n (firma, checkbox digital con marca de tiempo, o acuse en expediente).</p>
<p>En menores de edad, el tutor ejerce derechos; documente parentesco y autoridad. En teleconsulta, confirme identidad y env&iacute;e el aviso por el mismo canal seguro donde gestiona el <a href="/articulos/agenda-para-psicologos.html">agendamiento</a>.</p>"""
            },
            {
                "h2": "Datos sensibles, consentimiento y l&iacute;mites &eacute;ticos",
                "html": """<p>Los datos de salud mental suelen requerir <strong>consentimiento expreso</strong> para su tratamiento, salvo excepciones legales (riesgo vital, orden judicial, obligaci&oacute;n de reportar abuso a menores seg&uacute;n marco aplicable). Explique esos l&iacute;mites en el consentimiento cl&iacute;nico y al&iacute;neelos con el aviso de privacidad para no contradecirse.</p>
<p>Buenas pr&aacute;cticas en consultorio:</p>
<ul>
<li>Recolecte solo lo necesario para el fin cl&iacute;nico (principio de proporcionalidad).</li>
<li>Separe datos administrativos (RFC, factura) de notas &iacute;ntimas cuando sea posible.</li>
<li>No publique casos en redes ni en supervisiones sin anonimizar o sin autorizaci&oacute;n espec&iacute;fica.</li>
<li>Si usa inteligencia artificial para borradores de notas, verifique que el proveedor no entrene modelos con su contenido cl&iacute;nico; documente el flujo en el aviso.</li>
</ul>
<p>La confidencialidad &eacute;tica y la LFPDPPP convergen: ambas exigen control de acceso, no divulgaci&oacute;n indebida y registro de qui&eacute;n consulta el expediente. Un sistema como <a href="/plataforma-psicologos-mexico/">Kalyo para psic&oacute;logos en M&eacute;xico</a> ayuda a centralizar consentimientos, notas y permisos sin hojas sueltas en WhatsApp.</p>"""
            },
            {
                "h2": "Derechos ARCO y retenci&oacute;n del expediente",
                "html": """<p>El paciente puede solicitar <strong>Acceso, Rectificaci&oacute;n, Cancelaci&oacute;n u Oposici&oacute;n</strong> (ARCO). Defina un canal (correo dedicado, formulario) y un plazo interno de respuesta. No elimine de inmediato un expediente solo porque el paciente lo pida: la <a href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a> exige conservaci&oacute;n m&iacute;nima (t&iacute;picamente cinco a&ntilde;os desde la &uacute;ltima atenci&oacute;n en muchos contextos cl&iacute;nicos). Explique la tensi&oacute;n entre derecho de cancelaci&oacute;n y obligaci&oacute;n de conservar historia cl&iacute;nica; ofrezca copia, correcci&oacute;n de datos administrativos y limitaci&oacute;n de usos secundarios.</p>
<p>Checklist operativo:</p>
<ol>
<li>Registro de solicitudes ARCO (fecha, medio, respuesta).</li>
<li>Pol&iacute;tica de retenci&oacute;n escrita (cl&iacute;nica + fiscal).</li>
<li>Procedimiento de respaldo y destrucci&oacute;n segura al vencimiento.</li>
<li>Inventario de sistemas donde viven datos (agenda, drive, correo, app cl&iacute;nica, contabilidad).</li>
</ol>
<p>Si un tercero pide informaci&oacute;n (escuela, RH, pareja), exija autorizaci&oacute;n escrita del titular salvo excepci&oacute;n legal. Documente qu&eacute; se entreg&oacute; y en qu&eacute; fecha.</p>"""
            },
            {
                "h2": "Medidas de seguridad y expediente digital",
                "html": """<p>La LFPDPPP exige <strong>medidas de seguridad administrativas, t&eacute;cnicas y f&iacute;sicas</strong> acordes al riesgo. Para un consultorio psicol&oacute;gico eso implica, como m&iacute;nimo:</p>
<ul>
<li>Contrase&ntilde;as &uacute;nicas, autenticaci&oacute;n robusta y cierre de sesi&oacute;n en dispositivos compartidos.</li>
<li>Cifrado en tr&aacute;nsito (HTTPS) y proveedor con respaldos.</li>
<li>Control de qui&eacute;n accede al expediente (sin cuentas gen&eacute;ricas &laquo;consultorio1&raquo;).</li>
<li>Evitar notas cl&iacute;nicas en chats personales o hojas visibles en sala de espera.</li>
<li>Procedimiento ante incidente (p&eacute;rdida de laptop, acceso indebido): contener, evaluar, notificar si corresponde.</li>
</ul>
<p>Digitalizar no es escanear PDFs a un Drive abierto. Un <a href="/articulos/software-expedientes-psicologicos.html">software de expedientes psicol&oacute;gicos</a> con roles, bit&aacute;cora y consentimientos integrados reduce el riesgo frente a carpetas locales sin respaldo. Combine seguridad t&eacute;cnica con h&aacute;bitos: no deje la sesi&oacute;n abierta, no reenv&iacute;e tests por correo sin cifrar, y capacite a asistentes administrativos solo en lo necesario.</p>
<p>Si usa facturaci&oacute;n CFDI, el contador es encargado o receptor de datos fiscales: firme acuerdos de confidencialidad y limite el acceso a notas cl&iacute;nicas. Separe el expediente cl&iacute;nico del archivo contable siempre que sea viable.</p>"""
            },
            {
                "h2": "Checklist LFPDPPP para abrir o auditar tu consulta",
                "html": """<p>Use esta lista antes de recibir pacientes nuevos o al migrar a expediente electr&oacute;nico:</p>
<ol>
<li>Aviso de privacidad actualizado y evidencia de entrega.</li>
<li>Consentimiento informado cl&iacute;nico alineado (l&iacute;mites de confidencialidad).</li>
<li>Inventario de tratamientos y proveedores (agenda, video, pago, nube).</li>
<li>Contratos o cl&aacute;usulas con encargados de tratamiento.</li>
<li>Pol&iacute;tica ARCO y retenci&oacute;n documentada.</li>
<li>Control de acceso y respaldos verificados en el &uacute;ltimo trimestre.</li>
<li>Capacitaci&oacute;n breve a quien toque datos del paciente.</li>
<li>Revisi&oacute;n anual o al cambiar de software / modalidad (presencial a h&iacute;brida).</li>
</ol>
<p>Completar el checklist no reemplaza asesor&iacute;a legal personalizada, pero s&iacute; eleva el est&aacute;ndar de un consultorio que hoy guarda historias en cuadernos o WhatsApp. La combinaci&oacute;n LFPDPPP + NOM-004 + &eacute;tica profesional es el marco m&iacute;nimo cre&iacute;ble ante pacientes cada vez m&aacute;s informados y ante auditor&iacute;as.</p>
<p>Para implementar el marco en la pr&aacute;ctica diaria, muchos colegas centralizan expediente, consentimientos y agenda en <a href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=lfpdppp-proteccion-datos-psicologos-mexico">Kalyo</a>, de modo que el cumplimiento deje de depender de la memoria del terapeuta al final del d&iacute;a.</p>"""
            },
        ],
        "faqs": [
            {
                "q": "&iquest;La LFPDPPP aplica si solo atiendo de forma privada y no tengo empresa?",
                "a": "S&iacute;. Como persona f&iacute;sica que trata datos de pacientes usted es responsable del tratamiento. Debe contar con aviso de privacidad, medidas de seguridad y canal para derechos ARCO, aunque no tenga marca comercial registrada.",
            },
            {
                "q": "&iquest;El consentimiento informado sustituye al aviso de privacidad?",
                "a": "No. El consentimiento informado cubre el acto cl&iacute;nico (naturaleza del servicio, riesgos, confidencialidad terap&eacute;utica). El aviso de privacidad informa el tratamiento de datos personales bajo la LFPDPPP. Pueden firmarse juntos, pero no deben confundirse.",
            },
            {
                "q": "&iquest;Puedo borrar el expediente si el paciente ejerce cancelaci&oacute;n ARCO?",
                "a": "No de forma autom&aacute;tica. La conservaci&oacute;n del expediente cl&iacute;nico tiene plazos m&iacute;nimos (p. ej. NOM-004). Explique la obligaci&oacute;n legal, ofrezca copia y limite usos secundarios. Consulte asesor&iacute;a si hay conflicto entre normas.",
            },
            {
                "q": "&iquest;WhatsApp es compatible con la LFPDPPP para notas cl&iacute;nicas?",
                "a": "Usar chats personales para notas o tests eleva el riesgo: dispositivos sin control, respaldos opacos y filtraciones. Prefiera canales con control de acceso y registro. WhatsApp puede servir para recordatorios breves si est&aacute; descrito en el aviso y el paciente acepta.",
            },
            {
                "q": "&iquest;Qu&eacute; debo hacer si se filtra un expediente?",
                "a": "Contenga el acceso, documente el incidente, eval&uacute;e alcance y riesgo para titulares, refuerce credenciales y notifique seg&uacute;n gravedad y asesor&iacute;a legal. Revise proveedores y bit&aacute;coras. Prevenga con MFA, m&iacute;nimo privilegio y sin carpetas compartidas abiertas.",
            },
        ],
        "related": [
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004 e historia cl&iacute;nica"},
            {"href": "/articulos/consentimiento-informado-psicologia-mexico.html", "label": "Consentimiento informado M&eacute;xico"},
            {"href": "/articulos/ley-1581-proteccion-datos-psicologia.html", "label": "Ley 1581 (Colombia)"},
            {"href": "/articulos/software-expedientes-psicologicos.html", "label": "Software de expedientes"},
        ],
    },
    {
        "slug": "resolucion-2275-rips-psicologos-colombia",
        "title": "Resolución 2275 RIPS JSON: guía para psicólogos | Kalyo",
        "description": "Resolución 2275 de 2023: RIPS en JSON, CUV y MUV para psicólogos en Colombia. Checklist de facturación electrónica en salud mental y consulta privada.",
        "keywords": "Resolución 2275, RIPS JSON, CUV, MUV, psicólogos Colombia, facturación electrónica salud, FEV-RIPS",
        "h1": "Resolución 2275 RIPS JSON: qué debe hacer el psicólogo en Colombia",
        "breadcrumb_short": "Resolución 2275 RIPS",
        "hero_alt": "Psicólogo colombiano revisando RIPS JSON y facturación electrónica en salud",
        "inline_alt": "Flujo Resolución 2275: RIPS, FEV, MUV y CUV",
        "meta_label": "Cumplimiento legal &middot; Colombia 2026",
        "date_published": "2026-11-14",
        "date_modified": "2026-11-14",
        "quick_answer": "La <strong>Resoluci&oacute;n 2275 de 2023</strong> del Ministerio de Salud de Colombia exige integrar los <strong>RIPS en formato JSON</strong> con la factura electr&oacute;nica de venta (FEV) y validarlos en el Mecanismo &Uacute;nico de Validaci&oacute;n (MUV) para obtener el <strong>CUV</strong>. Para psic&oacute;logos que facturan al sistema de salud o a aseguradoras, el expediente cl&iacute;nico debe respaldar cada consulta o procedimiento reportado. Si atiende solo particulares sin reporte a EPS, el impacto es menor; si glosa o factura institucional, es cr&iacute;tico. Vea tambi&eacute;n la gu&iacute;a base de <a href=\"/articulos/rips-registros-individuales-colombia.html\">RIPS en Colombia</a>.",
        "intro_long": "Desde la <strong>Resoluci&oacute;n 2275</strong>, muchos psic&oacute;logos en Colombia enfrentan rechazos por RIPS mal estructurados o factura desalineada con la historia. Esta gu&iacute;a explica qu&eacute; cambia con el JSON, el CUV y el MUV, qu&eacute; archivos importan en salud mental y qu&eacute; errores generan glosa. Ordena el flujo m&iacute;nimo de cierre de mes y complementa <a href=\"/articulos/rips-registros-individuales-colombia.html\">RIPS</a> y <a href=\"/articulos/ley-1090-psicologia-colombia.html\">Ley 1090</a>.",
        "cta_h2": "Documenta sesiones listas para RIPS con Kalyo",
        "cta_p": "Expediente, notas y trazabilidad cl&iacute;nica para respaldar facturaci&oacute;n en Colombia &mdash; kalyo.io",
        "card_title": "Resolución 2275 RIPS para psicólogos",
        "card_p": "RIPS JSON, CUV, MUV y checklist práctico para psicólogos que facturan en Colombia.",
        "after_href": "/articulos/rips-registros-individuales-colombia.html",
        "after_loc": "https://kalyo.io/articulos/rips-registros-individuales-colombia.html",
        "asset_from": "rips-registros-individuales-colombia",
        "sections": [
            {
                "h2": "Qu&eacute; cambia con la Resoluci&oacute;n 2275",
                "html": """<p>La <strong>Resoluci&oacute;n 2275 de 2023</strong> actualiza el modelo de reporte: los RIPS dejan de pensarse solo como archivos planos aislados y pasan a integrarse con la <strong>factura electr&oacute;nica de venta</strong> bajo validaci&oacute;n unificada. El prestador genera RIPS en <strong>JSON</strong>, los env&iacute;a al mecanismo de validaci&oacute;n y recibe un <strong>C&oacute;digo &Uacute;nico de Validaci&oacute;n (CUV)</strong> cuando el paquete es aceptado.</p>
<p>Implicaciones pr&aacute;cticas para psicolog&iacute;a:</p>
<ul>
<li>La atenci&oacute;n reportada debe existir en historia cl&iacute;nica con fecha, profesional, diagn&oacute;stico y tipo de servicio coherentes.</li>
<li>Errores de c&oacute;digo CUPS, CIE o identificaci&oacute;n del usuario rebotan antes del pago.</li>
<li>La factura y los RIPS deben contar la misma historia: no se factura un control si el expediente dice primera vez, o viceversa.</li>
</ul>
<p>Si su pr&aacute;ctica es 100% particular sin contrato con EPS/IPS, puede no generar RIPS cotidianamente; a&uacute;n as&iacute; conviene entender el est&aacute;ndar si planea convenios o trabaja en instituciones. Detalle base en <a href="/articulos/rips-registros-individuales-colombia.html">RIPS: qu&eacute; son y c&oacute;mo funcionan</a>.</p>"""
            },
            {
                "h2": "RIPS relevantes en salud mental: AC y AP",
                "html": """<p>En consulta psicol&oacute;gica el archivo m&aacute;s usado es el de <strong>consultas (AC)</strong>: primera vez y control/seguimiento con CUPS vigentes seg&uacute;n manual de la aseguradora. Las <strong>evaluaciones con bater&iacute;a</strong> pueden ir como <strong>procedimientos (AP)</strong> cuando el tarifario lo contempla. Cada registro necesita diagn&oacute;stico principal (CIE) alineado a la formulaci&oacute;n cl&iacute;nica documentada.</p>
<p>Errores frecuentes en psicolog&iacute;a:</p>
<ol>
<li>Usar un CIE gen&eacute;rico que no corresponde a lo evaluado esa sesi&oacute;n.</li>
<li>Duplicar la misma consulta en dos env&iacute;os.</li>
<li>Facturar sin nota de evoluci&oacute;n ni firma/autenticaci&oacute;n del profesional.</li>
<li>Omitir autorizaci&oacute;n previa cuando la EPS la exige para evaluaci&oacute;n.</li>
</ol>
<p>Antes de cerrar el mes, cruce agenda, notas y borrador de RIPS. Un <a href="/plataforma-psicologos-colombia/">software cl&iacute;nico para Colombia</a> que ordene expediente y citas reduce discrepancias frente a planillas manuales.</p>"""
            },
            {
                "h2": "Flujo FEV + RIPS + MUV + CUV",
                "html": """<p>Piense el flujo en cuatro pasos:</p>
<ol>
<li><strong>Atenci&oacute;n y documento cl&iacute;nico:</strong> sesi&oacute;n registrada (motivo, intervenci&oacute;n, plan, diagn&oacute;stico de trabajo).</li>
<li><strong>Armado RIPS JSON:</strong> campos estructurados seg&uacute;n especificaci&oacute;n vigente del Ministerio.</li>
<li><strong>Factura electr&oacute;nica (FEV):</strong> montos y conceptos coherentes con lo reportado.</li>
<li><strong>Validaci&oacute;n MUV:</strong> el sistema acepta o rechaza; si acepta, conserva el <strong>CUV</strong> como evidencia.</li>
</ol>
<p>Sin CUV v&aacute;lido, el riesgo de glosa o rechazo administrativo sube. Guarde el CUV junto al expediente del periodo facturado, no solo en el correo del contador. Coordine con facturaci&oacute;n: el psic&oacute;logo aporta la verdad cl&iacute;nica; el facturador aporta la t&eacute;cnica DIAN/FEV, pero ambos deben hablar el mismo idioma de fechas y c&oacute;digos.</p>
<p>Actualice plantillas cuando el Ministerio publique versiones nuevas del mecanismo FEV-RIPS; los n&uacute;meros de versi&oacute;n de validaci&oacute;n cambian y lo que pas&oacute; hace seis meses puede rechazarse hoy.</p>"""
            },
            {
                "h2": "Checklist para psic&oacute;logos antes de enviar RIPS",
                "html": """<p>Use esta lista el d&iacute;a de cierre:</p>
<ul>
<li>Identificaci&oacute;n del usuario y tipo de documento correctos.</li>
<li>Fecha de atenci&oacute;n = fecha en nota de evoluci&oacute;n.</li>
<li>CUPS de psicolog&iacute;a vigente para el contrato.</li>
<li>CIE-10/CIE aplicable coherente con la sesi&oacute;n.</li>
<li>Modalidad (presencial/telemedicina) seg&uacute;n reglas del pagador.</li>
<li>Autorizaci&oacute;n cargada si aplica.</li>
<li>Sin duplicados del mismo encuentro.</li>
<li>Factura y RIPS cuadran en cantidad de servicios.</li>
</ul>
<p>Si el rechazo menciona estructura JSON, no &laquo;invente&raquo; campos: corrija con la especificaci&oacute;n o con su proveedor tecnol&oacute;gico. Si el rechazo es cl&iacute;nico-administrativo (diagn&oacute;stico, CUPS), revise el expediente antes de reenviar. La velocidad de reintento sin corregir la causa multiplica glosas.</p>"""
            },
            {
                "h2": "Consulta privada vs IPS: &iquest;qui&eacute;n debe cumplir?",
                "html": """<p>El alcance depende de c&oacute;mo cobra:</p>
<ul>
<li><strong>Particular puro:</strong> factura a persona natural sin reporte a EPS; la 2275 no es su operaci&oacute;n diaria, pero s&iacute; debe cumplir <a href="/articulos/ley-1581-proteccion-datos-psicologia.html">Ley 1581</a> y &eacute;tica (Ley 1090).</li>
<li><strong>Convenio / IPS / talento humano en salud:</strong> casi seguro genera RIPS y FEV bajo reglas institucionales; usted aporta documentaci&oacute;n cl&iacute;nica impecable.</li>
<li><strong>Mixto:</strong> separe claramente agendas y expedientes para no mezclar reglas de pagadores.</li>
</ul>
<p>En todos los casos, la calidad del expediente es el activo: sin nota, no hay defensa ante auditor&iacute;a. Digitalizar notas SOAP y consentimientos en una plataforma &uacute;nica evita el cl&aacute;sico &laquo;la facturaci&oacute;n pide un RIPS que la historia no soporta&raquo;.</p>"""
            },
            {
                "h2": "C&oacute;mo prepararse sin improvisar el &uacute;ltimo d&iacute;a",
                "html": """<p>Recomendaci&oacute;n operativa semanal:</p>
<ol>
<li>Cierre notas el mismo d&iacute;a de la sesi&oacute;n.</li>
<li>Revise diagn&oacute;sticos de trabajo cada 4&ndash;6 encuentros.</li>
<li>Capacite a quien factura en c&oacute;digos de psicolog&iacute;a (no solo medicina general).</li>
<li>Guarde CUV y soportes por periodo.</li>
<li>Haga una prueba de validaci&oacute;n cuando cambie de software o de contrato.</li>
</ol>
<p>La Resoluci&oacute;n 2275 no es un tr&aacute;mite cosm&eacute;tico: es el puente entre lo que usted documenta en sesi&oacute;n y lo que el sistema de salud reconoce como prestado. Ordenar expediente + facturaci&oacute;n es la forma m&aacute;s barata de reducir glosas. Si busca centralizar la parte cl&iacute;nica (agenda, notas, historia) mientras su operador de facturaci&oacute;n genera el JSON, <a href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=resolucion-2275-rips-psicologos-colombia">Kalyo</a> cubre el lado del expediente para que el RIPS no se arme a ciegas.</p>"""
            },
        ],
        "faqs": [
            {
                "q": "&iquest;La Resoluci&oacute;n 2275 obliga a todos los psic&oacute;logos en Colombia?",
                "a": "Obliga a quienes deben reportar RIPS e integrarlos a la factura electr&oacute;nica de salud seg&uacute;n su rol de prestador. La consulta particular sin convenio EPS puede no generar RIPS diarios, pero s&iacute; debe cumplir &eacute;tica y protecci&oacute;n de datos.",
            },
            {
                "q": "&iquest;Qu&eacute; es el CUV y por qu&eacute; importa?",
                "a": "El C&oacute;digo &Uacute;nico de Validaci&oacute;n acredita que el paquete RIPS/FEV pas&oacute; el Mecanismo &Uacute;nico de Validaci&oacute;n. Sin CUV v&aacute;lido, aumenta el riesgo de rechazo o glosa. Cons&eacute;rvelo con el soporte del periodo facturado.",
            },
            {
                "q": "&iquest;Puedo seguir enviando RIPS en archivos planos antiguos?",
                "a": "El modelo impulsado por la 2275 apunta a JSON integrado con FEV y validaci&oacute;n unificada. Verifique la fecha y el canal que exige su EPS o su software; no asuma que el formato de hace a&ntilde;os sigue acept&aacute;ndose.",
            },
            {
                "q": "&iquest;Qu&eacute; CUPS uso en psicolog&iacute;a?",
                "a": "Depende del manual tarifario y del contrato. Lo habitual es distinguir primera vez y control, y procedimientos de evaluaci&oacute;n cuando apliquen. Confirme siempre con facturaci&oacute;n/EPS antes de cerrar el mes.",
            },
            {
                "q": "&iquest;C&oacute;mo evito glosas por diagn&oacute;stico?",
                "a": "Alinee el CIE con lo documentado en la nota de esa fecha, evite c&oacute;digos decorativos y actualice la formulaci&oacute;n cuando el cuadro cambie. La inconsistencia entre nota y RIPS es causa cl&aacute;sica de rechazo.",
            },
        ],
        "related": [
            {"href": "/articulos/rips-registros-individuales-colombia.html", "label": "RIPS en Colombia (gu&iacute;a base)"},
            {"href": "/articulos/ley-1090-psicologia-colombia.html", "label": "Ley 1090"},
            {"href": "/articulos/ley-1581-proteccion-datos-psicologia.html", "label": "Ley 1581 datos"},
            {"href": "/articulos/como-abrir-consulta-privada-colombia.html", "label": "Abrir consulta en Colombia"},
        ],
    },
    {
        "slug": "expediente-clinico-electronico-psicologos",
        "title": "Expediente clínico electrónico: guía psicólogos | Kalyo",
        "description": "Expediente clínico electrónico para psicólogos: requisitos NOM-004 y NOM-024, seguridad, respaldos y checklist para digitalizar el consultorio en México.",
        "keywords": "expediente clínico electrónico, NOM-024, NOM-004, psicólogos, historia clínica digital, software expediente psicológico",
        "h1": "Expediente clínico electrónico para psicólogos: requisitos y checklist",
        "breadcrumb_short": "Expediente clínico electrónico",
        "hero_alt": "Expediente clínico electrónico en laptop de consultorio psicológico",
        "inline_alt": "Elementos del expediente clínico electrónico: acceso, firma, respaldo",
        "meta_label": "Pr&aacute;ctica cl&iacute;nica &middot; Digitalizaci&oacute;n 2026",
        "date_published": "2026-11-14",
        "date_modified": "2026-11-14",
        "quick_answer": "Un <strong>expediente cl&iacute;nico electr&oacute;nico</strong> para psic&oacute;logos es el conjunto de registros digitales de atenci&oacute;n (identificaci&oacute;n, historia, notas, consentimientos, pruebas) con autenticaci&oacute;n, trazabilidad y respaldo. En M&eacute;xico, el contenido m&iacute;nimo se alinea a la <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a>; cuando el expediente es electr&oacute;nico, la <strong>NOM-024</strong> orienta interoperabilidad, seguridad e integridad. No basta escanear hojas a un Drive: necesita control de acceso, conservaci&oacute;n y firma o equivalente. En Colombia y Chile el principio es el mismo: confidencialidad + historia &uacute;til + evidencia de qui&eacute;n registr&oacute; qu&eacute;.",
        "intro_long": "Digitalizar el consultorio sin criterio genera PDFs ca&oacute;ticos y riesgos de filtraci&oacute;n. Esta gu&iacute;a define un <strong>expediente cl&iacute;nico electr&oacute;nico</strong> serio para psicolog&iacute;a, c&oacute;mo se relacionan NOM-004 y NOM-024 en M&eacute;xico, qu&eacute; exigir a un software y c&oacute;mo migrar sin perder historia. Incluye checklist de seguridad y enlaces a <a href=\"/articulos/nota-evolucion-psicologica.html\">notas</a> y <a href=\"/digitalizar-consulta-psicologica/\">digitalizaci&oacute;n</a>.",
        "cta_h2": "Pasa tu expediente a digital con Kalyo",
        "cta_p": "Historia cl&iacute;nica, notas, tests y consentimientos en un solo lugar &mdash; kalyo.io",
        "card_title": "Expediente clínico electrónico",
        "card_p": "NOM-004, NOM-024, seguridad y checklist para digitalizar el expediente psicológico.",
        "after_href": "/articulos/nom-004-historia-clinica-mexico.html",
        "after_loc": "https://kalyo.io/articulos/nom-004-historia-clinica-mexico.html",
        "asset_from": "nom-004-historia-clinica-mexico",
        "sections": [
            {
                "h2": "Expediente electr&oacute;nico vs carpeta digital improvisada",
                "html": """<p>Escanear notas a Google Drive <em>no</em> es un expediente cl&iacute;nico electr&oacute;nico. Un ECE serio permite:</p>
<ul>
<li>Identificar al paciente de forma un&iacute;voca.</li>
<li>Registrar historia, evoluci&oacute;n, consentimientos y anexos con fecha.</li>
<li>Saber <strong>qui&eacute;n</strong> cre&oacute; o modific&oacute; un registro (trazabilidad).</li>
<li>Restringir accesos y generar respaldos recuperables.</li>
<li>Conservar el contenido el tiempo legal/&eacute;tico exigible.</li>
</ul>
<p>La carpeta improvisada falla en auditor&iacute;a, en cambio de dispositivo y en confidencialidad. El ECE, bien implementado, acelera continuidad asistencial y reduce p&eacute;rdida de informaci&oacute;n entre sesiones. Compare enfoques en <a href="/articulos/software-expedientes-psicologicos.html">software de expedientes psicol&oacute;gicos</a>.</p>"""
            },
            {
                "h2": "NOM-004 y NOM-024: c&oacute;mo se complementan",
                "html": """<p>En M&eacute;xico, la <strong>NOM-004-SSA3-2012</strong> define el <em>qu&eacute;</em> del expediente: integraci&oacute;n, contenidos m&iacute;nimos, confidencialidad y conservaci&oacute;n. La <strong>NOM-024</strong> orienta el <em>c&oacute;mo electr&oacute;nico</em>: sistemas de informaci&oacute;n de salud, intercambio, seguridad e integridad de registros electr&oacute;nicos. Para el psic&oacute;logo en consulta privada, la lectura pr&aacute;ctica es:</p>
<ol>
<li>Cumpla el contenido cl&iacute;nico (NOM-004 / buenas pr&aacute;cticas equivalentes).</li>
<li>Si el sistema es electr&oacute;nico, exija autenticaci&oacute;n, bit&aacute;cora, respaldos y protecci&oacute;n de datos (esp&iacute;ritu NOM-024 + <a href="/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html">LFPDPPP</a>).</li>
</ol>
<p>No necesita memorizar cada numeral; s&iacute; necesita un proveedor que no borre historial sin rastro y que permita exportar informaci&oacute;n del paciente cuando corresponda. En Colombia el paralelo conceptual es historia cl&iacute;nica + <a href="/articulos/ley-1581-proteccion-datos-psicologia.html">Ley 1581</a>; en Chile, confidencialidad y normativa sanitaria aplicable al tipo de prestador.</p>"""
            },
            {
                "h2": "Qu&eacute; debe contener el ECE en psicolog&iacute;a",
                "html": """<p>M&iacute;nimo recomendado:</p>
<ul>
<li>Ficha de identificaci&oacute;n y contacto de emergencia.</li>
<li>Motivo de consulta y antecedentes relevantes.</li>
<li>Consentimiento informado (y aviso de privacidad donde aplique).</li>
<li>Notas de evoluci&oacute;n (p. ej. SOAP) por sesi&oacute;n.</li>
<li>Resultados e interpretaci&oacute;n de tests aplicados.</li>
<li>Plan terap&eacute;utico y reformulaciones.</li>
<li>Registro de riesgo suicida cuando proceda.</li>
<li>Interconsultas / informes entregados a terceros con autorizaci&oacute;n.</li>
</ul>
<p>Gu&iacute;as &uacute;tiles: <a href="/articulos/historia-clinica-psicologica-paso-a-paso.html">historia cl&iacute;nica paso a paso</a> y <a href="/articulos/nota-evolucion-psicologica.html">nota de evoluci&oacute;n</a>. El ECE no escribe por usted: estructura y protege lo que usted documenta.</p>"""
            },
            {
                "h2": "Seguridad, firma y respaldos",
                "html": """<p>Pregunte a cualquier software o a su propia infraestructura:</p>
<ol>
<li>&iquest;Hay usuarios individuales con permisos?</li>
<li>&iquest;Queda registro de accesos y cambios?</li>
<li>&iquest;Los respaldos se prueban (no solo se asumen)?</li>
<li>&iquest;Puedo cerrar sesi&oacute;n remota si pierdo el tel&eacute;fono?</li>
<li>&iquest;D&oacute;nde est&aacute;n los servidores y bajo qu&eacute; contrato de encargado?</li>
</ol>
<p>La &laquo;firma electr&oacute;nica&raquo; en notas puede ser autenticaci&oacute;n fuerte + sello de tiempo + inalterabilidad del registro; no siempre requiere e.firma SAT. Lo cr&iacute;tico es demostrar autor&iacute;a e integridad. Evite compartir una sola contrase&ntilde;a con recepci&oacute;n y terapeutas. Separe roles administrativos (agenda, cobro) de lectura cl&iacute;nica completa.</p>"""
            },
            {
                "h2": "Migraci&oacute;n desde papel o Drive: plan en 4 pasos",
                "html": """<p>Plan realista:</p>
<ol>
<li><strong>Inventario:</strong> d&oacute;nde est&aacute; cada historia hoy (cajones, PDF, WhatsApp).</li>
<li><strong>Plantilla:</strong> defina campos m&iacute;nimos y nota tipo antes de cargar pacientes.</li>
<li><strong>Carga priorizada:</strong> pacientes activos primero; archivo hist&oacute;rico despu&eacute;s.</li>
<li><strong>Corte:</strong> elija una fecha desde la cual solo se escribe en el ECE.</li>
</ol>
<p>No pretenda digitalizar diez a&ntilde;os en un fin de semana. Capacite h&aacute;bitos: nota el mismo d&iacute;a, consentimiento firmado antes de la tercera sesi&oacute;n, sin fotos de notas en el rollo del tel&eacute;fono. Gu&iacute;a ampliada: <a href="/digitalizar-consulta-psicologica/">c&oacute;mo digitalizar tu consulta</a>.</p>
<p>Durante la migraci&oacute;n, evite doble escritura prolongada: si papel y digital coexisten m&aacute;s de tres o cuatro semanas, aumentan omisiones y contradicciones. Asigne un bloque semanal solo para cargar activos (por ejemplo, los que tienen cita en los pr&oacute;ximos quince d&iacute;as). Los casos en pausa pueden esperar con una carpeta de &laquo;archivo hist&oacute;rico de solo lectura&raquo; claramente etiquetada.</p>
<p>Comunique al paciente, cuando proceda, que su historia pasa a un sistema digital con medidas de seguridad; eso refuerza confianza y alinea el <a href="/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html">aviso de privacidad</a>. Si hay practicantes o recepci&oacute;n, delimite qu&eacute; pueden ver: agenda s&iacute;, notas &iacute;ntimas no.</p>"""
            },
            {
                "h2": "Checklist de compra o auditor&iacute;a de software",
                "html": """<p>Antes de pagar una suscripci&oacute;n:</p>
<ul>
<li>Cumple contenido cl&iacute;nico que usted necesita (no solo CRM de citas).</li>
<li>Exportaci&oacute;n de datos del paciente.</li>
<li>Consentimientos y tests integrables.</li>
<li>Soporte en espa&ntilde;ol y residencia de datos clara.</li>
<li>Precio transparente vs alternativas gen&eacute;ricas de medicina.</li>
</ul>
<p>Un ECE pensado para psicolog&iacute;a evita forzar plantillas de hospital quir&uacute;rgico. Si busca una opci&oacute;n orientada a consultorio LATAM con expediente, agenda y evaluaciones, pruebe <a href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=expediente-clinico-electronico-psicologos">Kalyo</a> y compare con su flujo actual durante dos semanas de pacientes reales.</p>
<p>Recuerde: la herramienta no reemplaza juicio cl&iacute;nico ni cumplimiento legal; solo hace m&aacute;s dif&iacute;cil perder, filtrar o contradecir lo documentado. El mejor expediente electr&oacute;nico es el que usted efectivamente completa despu&eacute;s de cada sesi&oacute;n.</p>
<p>Audite cada seis meses: &iquest;siguen activos usuarios que ya no colaboran?, &iquest;los respaldos se restauraron al menos una vez en un entorno de prueba?, &iquest;las plantillas de nota siguen sirviendo a su modelo (presencial, teleconsulta, pareja)? Un ECE abandonado a medias es peor que papel ordenado: da falsa seguridad. Trate la digitalizaci&oacute;n como proceso cl&iacute;nico continuo, no como compra &uacute;nica de software.</p>
<p>En Colombia o Chile el checklist es an&aacute;logo: confidencialidad, retenci&oacute;n, autor&iacute;a de la nota y capacidad de entregar copia al paciente. Ajuste nombres normativos locales, pero no baje el est&aacute;ndar t&eacute;cnico de acceso y respaldo. Si factura a aseguradoras, confirme que el ECE facilita cruzar fecha de sesi&oacute;n con lo reportado en RIPS u hom&oacute;logos.</p>"""
            },
        ],
        "faqs": [
            {
                "q": "&iquest;El expediente electr&oacute;nico es obligatorio para psic&oacute;logos en M&eacute;xico?",
                "a": "La NOM-004 regula el expediente cl&iacute;nico; puede existir en medios f&iacute;sicos o electr&oacute;nicos. Si opta por electr&oacute;nico, debe garantizar integridad, confidencialidad y conservaci&oacute;n. Muchos colegas digitalizan por seguridad y continuidad, no solo por mandato puntual.",
            },
            {
                "q": "&iquest;Qu&eacute; diferencia hay entre NOM-004 y NOM-024?",
                "a": "NOM-004 se centra en contenido, manejo y conservaci&oacute;n del expediente. NOM-024 orienta sistemas electr&oacute;nicos de informaci&oacute;n en salud (seguridad, intercambio, integridad). En la pr&aacute;ctica privada se leen juntas: contenido cl&iacute;nico + sistema confiable.",
            },
            {
                "q": "&iquest;Puedo usar Google Drive como expediente?",
                "a": "Como archivo de respaldo de PDFs, con riesgos altos si no hay control fino de accesos ni bit&aacute;cora cl&iacute;nica. No sustituye un ECE con autenticaci&oacute;n, estructura de notas y trazabilidad de cambios.",
            },
            {
                "q": "&iquest;Cu&aacute;nto tiempo debo conservar el expediente digital?",
                "a": "En M&eacute;xico, la referencia habitual de NOM-004 es m&iacute;nimo cinco a&ntilde;os desde la &uacute;ltima atenci&oacute;n, sin perjuicio de otros plazos. En Colombia y Chile verifique normas locales y c&oacute;digos &eacute;ticos. Defina retenci&oacute;n por escrito.",
            },
            {
                "q": "&iquest;C&oacute;mo migro pacientes activos sin caos?",
                "a": "Priorice activos, cargue ficha + &uacute;ltimas notas + consentimientos, fije fecha de corte y deje el archivo hist&oacute;rico en solo lectura. No duplique escritura papel/digital m&aacute;s de unas semanas.",
            },
        ],
        "related": [
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004 historia cl&iacute;nica"},
            {"href": "/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html", "label": "LFPDPPP para psic&oacute;logos"},
            {"href": "/articulos/software-expedientes-psicologicos.html", "label": "Software de expedientes"},
            {"href": "/articulos/historia-clinica-psicologica-paso-a-paso.html", "label": "Historia cl&iacute;nica paso a paso"},
        ],
    },
]


def copy_assets(slug: str, src_slug: str) -> None:
    for kind in ("hero", "inline"):
        for ext in ("jpg", "webp"):
            src = ASSETS / f"{src_slug}-{kind}.{ext}"
            dst = ASSETS / f"{slug}-{kind}.{ext}"
            if src.exists() and not dst.exists():
                shutil.copy2(src, dst)


def publish(spec: dict) -> dict:
    slug = spec["slug"]
    SPECS_DIR.mkdir(parents=True, exist_ok=True)
    # Strip publish-only keys from stored spec used by renderer
    render_spec = {k: v for k, v in spec.items() if k not in {"card_title", "card_p", "after_href", "after_loc", "asset_from"}}
    (SPECS_DIR / f"{slug}.json").write_text(json.dumps(render_spec, ensure_ascii=False, indent=2), encoding="utf-8")

    html = render(render_spec)
    (ART / f"{slug}.html").write_text(html, encoding="utf-8")
    copy_assets(slug, spec["asset_from"])

    info = verify(slug)
    print(json.dumps(info, ensure_ascii=False))

    if f'href="/articulos/{slug}.html"' not in (ART / "index.html").read_text(encoding="utf-8"):
        card = (
            f'      <a href="/articulos/{slug}.html" class="blog-card">\n'
            f'        <span class="blog-card-tag">Gu&iacute;a normativa</span>\n'
            f'        <h3>{spec["card_title"]}</h3>\n'
            f'        <p>{spec["card_p"]}</p>\n'
            f'      </a>\n'
        )
        insert_card(spec["after_href"], card)
        bump_counts(1)
    else:
        print("card exists, skip bump")

    insert_sitemap(spec["after_loc"], f"https://kalyo.io/articulos/{slug}.html", lastmod="2026-11-14")
    print("UPDATED", slug)
    print("intro_long words", helper_word_count(spec["intro_long"]))
    return info


def main() -> None:
    for spec in SPECS:
        intro_w = helper_word_count(spec["intro_long"])
        print(f"PRECHECK {spec['slug']}: title={len(spec['title'])} desc={len(spec['description'])} intro={intro_w}")
        if not (55 <= len(spec["title"]) <= 60):
            raise SystemExit(f"title length {len(spec['title'])}")
        if not (150 <= len(spec["description"]) <= 160):
            raise SystemExit(f"desc length {len(spec['description'])}")
        if not (50 <= intro_w <= 60):
            raise SystemExit(f"intro words {intro_w}")
        publish(spec)


if __name__ == "__main__":
    main()
