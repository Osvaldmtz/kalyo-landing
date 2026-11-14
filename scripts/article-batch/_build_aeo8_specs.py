# -*- coding: utf-8 -*-
"""Build aeo-batch8-specs.json with 7 full AEO article specs."""
from __future__ import annotations
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from publish_aeo_helpers import word_count as wc

CLOSERS = {
"generic": """
<p>En consultorio real, la diferencia entre cumplir y solo parecer que se cumple est&aacute; en h&aacute;bitos semanales: cerrar notas el mismo d&iacute;a, revisar accesos, conciliar agenda con cobranza y actualizar consentimientos cuando cambia la modalidad. Estos rituales cortos protegen m&aacute;s que documentos largos sin uso. Capacite a practicantes con ejemplos de su propia pr&aacute;ctica, no solo con teor&iacute;a normativa.</p>
<p>Cuando dude entre dos interpretaciones legales o &eacute;ticas, documente la decisi&oacute;n tomada, la fecha y la fuente consultada. Esa trazabilidad es &uacute;til ante auditor&iacute;as y ante su propio yo futuro. Revise esta gu&iacute;a cada vez que cambie de software, de ciudad o de tipo de convenio. El contexto altera prioridades, pero no elimina la necesidad de respuesta clara, expediente &uacute;til y respeto al paciente.</p>
<p>Kalyo puede sostener la parte operativa del expediente, la agenda y los consentimientos digitales; el criterio cl&iacute;nico y el cumplimiento local siguen siendo suyos. Use la plataforma como apoyo, no como sustituto de juicio profesional. Si algo de esta gu&iacute;a entra en tensi&oacute;n con una circular nueva de su EPS, colegio o autoridad, prevalece la norma vigente y actualice su plantilla.</p>
<p>Priorice evidencia recuperable: fechas, autor&iacute;a, versiones de documentos y notas firmadas o equivalentes. Un sistema ordenado reduce ansiedad administrativa y libera atenci&oacute;n para lo cl&iacute;nico. Empiece por el cuello de botella m&aacute;s doloroso de su semana &mdash;consentimiento, alta, cobro, riesgo o supervisi&oacute;n&mdash; y estandar&iacute;celo en catorce d&iacute;as.</p>
<p>Comparta este checklist con colegas de confianza y contrasten pr&aacute;cticas. La mejora colectiva eleva el est&aacute;ndar del gremio. Mantenga actualizadas las referencias a NOM, Ley 1090, LFPDPPP u otras normas locales que toquen su poblaci&oacute;n. La excelencia cl&iacute;nica y la documentaci&oacute;n seria no compiten: se refuerzan.</p>
"""
}

def closer(slug: str) -> str:
    link = f'https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign={slug}'
    return CLOSERS["generic"] + f'<p>Si busca un expediente digital orientado a psicolog&iacute;a, pruebe <a href="{link}">Kalyo</a> y contraste con su flujo actual durante dos semanas.</p>'

SPECS = []

SPECS.append({
"slug":"consentimiento-informado-elementos-mx-co",
"title":"Consentimiento informado psicología: qué incluir | Kalyo",
"description":"Consentimiento informado en psicología MX/CO: qué debe incluir, checklist para menores y teleconsulta, y cómo archivarlo en el expediente clínico digital.",
"keywords":"consentimiento informado psicologia, consentimiento informado psicologo, qué debe incluir, México, Colombia, checklist",
"h1":"Consentimiento informado en psicología: qué debe incluir (MX/CO)",
"breadcrumb_short":"Consentimiento informado MX/CO",
"hero_alt":"Checklist de consentimiento informado psicológico México Colombia",
"inline_alt":"Elementos del consentimiento informado en psicología clínica",
"meta_label":"Cumplimiento &eacute;tico &middot; MX/CO 2026",
"date_published":"2026-11-14","date_modified":"2026-11-14",
"quick_answer":"El <strong>consentimiento informado en psicolog&iacute;a</strong> documenta que la persona comprende el servicio, riesgos, beneficios, alternativas, l&iacute;mites de confidencialidad y derecho a retirarse. En M&eacute;xico y Colombia debe integrarse al <a href=\"/articulos/expediente-clinico-electronico-psicologos.html\">expediente</a> al inicio; en menores se suma autorizaci&oacute;n de tutores. No reemplaza el aviso de privacidad ni el encuadre de honorarios.",
"intro_long":"""Muchos consultorios usan un PDF gen&eacute;rico que omite teleconsulta, riesgo y terceros. Esta gu&iacute;a detalla <strong>qu&eacute; debe incluir el consentimiento informado</strong> en M&eacute;xico y Colombia, con tabla comparativa, menores y archivo digital. Complementa <a href="/articulos/consentimiento-informado-psicologia-mexico.html">la gu&iacute;a M&eacute;xico</a> y el marco Latam con un checklist listo para el consultorio privado. &Uacute;sela en su pr&aacute;ctica diaria.""",
"cta_h2":"Archiva consentimientos firmados en Kalyo","cta_p":"Plantillas, firma y expediente &uacute;nico &mdash; kalyo.io",
"card_title":"Consentimiento informado: qué incluir MX/CO","card_p":"Elementos mínimos, menores, teleconsulta y checklist para el expediente.",
"after_href":"/articulos/consentimiento-informado-psicologia-mexico.html",
"after_loc":"https://kalyo.io/articulos/consentimiento-informado-psicologia-mexico.html",
"asset_from":"consentimiento-informado-psicologia-mexico",
"sections":[
{"h2":"Elementos m&iacute;nimos del consentimiento","html":"""<p>Un consentimiento cl&iacute;nico &uacute;til responde, en lenguaje claro, a qui&eacute;n atiende, qu&eacute; servicio se ofrece, con qu&eacute; modalidad, para qu&eacute; objetivos generales, qu&eacute; riesgos y beneficios existen, qu&eacute; alternativas hay, c&oacute;mo opera la confidencialidad y sus excepciones, c&oacute;mo se manejan honorarios o a qu&eacute; documento remiten, y c&oacute;mo se puede revocar el acuerdo.</p>
<ul>
<li>Identificaci&oacute;n del profesional (nombre, c&eacute;dula o tarjeta profesional) y del paciente o representante.</li>
<li>Descripci&oacute;n del servicio: psicoterapia, evaluaci&oacute;n, orientaci&oacute;n; presencial o teleconsulta.</li>
<li>L&iacute;mites de confidencialidad: riesgo suicida o heteroagresivo, maltrato, mandatos legales.</li>
<li>Uso de pruebas, grabaciones o informes a terceros, si aplica.</li>
<li>Firma o equivalente digital con fecha y copia para el paciente.</li>
</ul>
<p>Separe este acto del <a href="/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html">aviso de privacidad LFPDPPP</a> en M&eacute;xico y de las pol&iacute;ticas de datos en Colombia. Evite promesas de resultado: el consentimiento informa un proceso, no garantiza curaci&oacute;n.</p>"""},
{"h2":"M&eacute;xico y Colombia: diferencias &uacute;tiles","html":"""<table class="items-table"><thead><tr><th>Aspecto</th><th>M&eacute;xico</th><th>Colombia</th></tr></thead><tbody>
<tr><td>Expediente</td><td><a href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a></td><td>Historia cl&iacute;nica y registro continuo</td></tr>
<tr><td>&Eacute;tica</td><td>C&oacute;digo &eacute;tico / deontol&oacute;gico + c&eacute;dula</td><td><a href="/articulos/ley-1090-psicologia-colombia.html">Ley 1090</a></td></tr>
<tr><td>Datos</td><td>LFPDPPP / ARCO</td><td>Ley 1581 / h&aacute;beas data</td></tr>
<tr><td>Teleconsulta</td><td>Consentimiento de modalidad + canal seguro</td><td>Consentimiento remoto + telesalud aplicable</td></tr>
</tbody></table>
<p>Priorice comprensi&oacute;n real. Para detalle M&eacute;xico use <a href="/articulos/consentimiento-informado-psicologia-mexico.html">esta gu&iacute;a</a>; para panorama regional, <a href="/articulos/consentimiento-informado-psicologia-latam.html">Latam</a>. Actualice el texto cuando cambie su poblaci&oacute;n o incorpore evaluaciones periciales.</p>"""},
{"h2":"Menores, pareja e informes a terceros","html":"""<p>Con <strong>menores</strong>, registre qui&eacute;n autoriza, parentesco o custodia, qu&eacute; se comunicar&aacute; a cuidadores y qu&eacute; permanece reservado. Busque asentimiento del adolescente. En <strong>pareja o familia</strong>, defina qui&eacute;n es el paciente del encuadre y reglas sobre secretos entre miembros.</p>
<p>Si emitir&aacute; informes escolares, laborales o legales, anticipe destinatarios y alcance. Sin autorizaci&oacute;n clara, pause el informe. Deje constancia en nota de que se explic&oacute;, se respondieron dudas y se entreg&oacute; copia. Estos matices evitan conflictos &eacute;ticos posteriores.</p>"""},
{"h2":"Teleconsulta, archivo y checklist","html":"""<p>Agregue cl&aacute;usulas de plataforma, riesgos de privacidad en casa, no grabaci&oacute;n sin acuerdo, verificaci&oacute;n de identidad y plan ante crisis a distancia. Vea <a href="/articulos/telepsicologia-requisitos-legales-mx-co.html">requisitos de telepsicolog&iacute;a</a>.</p>
<ol>
<li>Plantilla base + anexos (menores / teleconsulta / informes).</li>
<li>Explicaci&oacute;n verbal con tiempo para preguntas.</li>
<li>Firma o equivalente digital trazable.</li>
<li>Copia al paciente y archivo dentro del expediente.</li>
<li>Adenda si cambia modalidad u honorarios materiales.</li>
</ol>
<p>Revise coherencia con su <a href="/articulos/encuadre-terapeutico.html">encuadre</a>. Capacite a quien entrega el documento: usted responde por el contenido.</p>"""+closer("consentimiento-informado-elementos-mx-co")},
],
"faqs":[
{"q":"&iquest;Basta el consentimiento verbal?","a":"Conviene evidencia escrita o digital. En urgencia documente el verbal en nota y regularice por escrito apenas pueda."},
{"q":"&iquest;Es igual al aviso de privacidad?","a":"No. Uno cubre el acto cl&iacute;nico; el otro, el tratamiento de datos personales."},
{"q":"&iquest;Debo renovarlo cada a&ntilde;o?","a":"Renueve o adende ante cambios materiales. La revisi&oacute;n anual es buena pr&aacute;ctica."},
{"q":"&iquest;Y si el paciente no firma?","a":"Explore dudas. Si el servicio lo requiere y persiste la negativa, no inicie o suspenda, salvo obligaciones de urgencia."},
{"q":"&iquest;Sirven plantillas de internet?","a":"Solo si las adapta a MX/CO, a su identificaci&oacute;n profesional, teleconsulta y menores."},
],
"related":[
{"href":"/articulos/consentimiento-informado-psicologia-mexico.html","label":"Consentimiento M&eacute;xico"},
{"href":"/articulos/consentimiento-informado-psicologia.html","label":"Gu&iacute;a general"},
{"href":"/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html","label":"LFPDPPP"},
{"href":"/articulos/encuadre-terapeutico.html","label":"Encuadre terap&eacute;utico"},
],
})

SPECS.append({
"slug":"codigo-deontologico-psicologo-mexico",
"title":"Código deontológico psicólogo México: ética y NOM | Kalyo",
"description":"Código deontológico del psicólogo en México: ética SMP, cédula profesional, NOM aplicables, confidencialidad, límites duales y checklist práctico 2026.",
"keywords":"codigo de etica del psicologo, codigo deontologico del psicologo, código ético psicólogo México, SMP, NOM",
"h1":"Código deontológico del psicólogo en México: ética y NOM",
"breadcrumb_short":"Código deontológico México",
"hero_alt":"Código deontológico y ético del psicólogo en México",
"inline_alt":"Checklist ético y normativo para psicólogos en México",
"meta_label":"&Eacute;tica profesional &middot; M&eacute;xico 2026",
"date_published":"2026-11-14","date_modified":"2026-11-14",
"quick_answer":"El <strong>c&oacute;digo deontol&oacute;gico / &eacute;tico del psic&oacute;logo en M&eacute;xico</strong> fija deberes de competencia, confidencialidad, consentimiento, integridad y l&iacute;mites de rol. Se articula con c&eacute;dula profesional, lineamientos de la Sociedad Mexicana de Psicolog&iacute;a y normas sanitarias como <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a>. No es un adorno: orienta decisiones diarias y respalda el expediente.",
"intro_long":"""El c&oacute;digo deontol&oacute;gico orienta la pr&aacute;ctica &eacute;tica del psic&oacute;logo m&aacute;s all&aacute; de la intuici&oacute;n personal. Esta gu&iacute;a resume el <strong>c&oacute;digo &eacute;tico del psic&oacute;logo en M&eacute;xico</strong>, su v&iacute;nculo con c&eacute;dula, NOM y l&iacute;mites profesionales, m&aacute;s un checklist aplicable a consulta privada. No sustituye el texto oficial ni asesor&iacute;a colegiada. &Uacute;sela en su pr&aacute;ctica diaria.""",
"cta_h2":"Documenta con criterio ético en Kalyo","cta_p":"Expediente, consentimientos y notas con trazabilidad &mdash; kalyo.io",
"card_title":"Código deontológico del psicólogo en México","card_p":"Ética SMP, cédula, NOM, confidencialidad y checklist de consulta privada.",
"after_href":"/articulos/nom-004-historia-clinica-mexico.html",
"after_loc":"https://kalyo.io/articulos/nom-004-historia-clinica-mexico.html",
"asset_from":"nom-004-historia-clinica-mexico",
"sections":[
{"h2":"Qu&eacute; regula el c&oacute;digo &eacute;tico / deontol&oacute;gico","html":"""<p>En M&eacute;xico, los lineamientos &eacute;ticos del gremio &mdash;incluyendo referencias asociadas a la Sociedad Mexicana de Psicolog&iacute;a y c&oacute;digos de &eacute;tica profesional&mdash; organizan deberes sobre:</p>
<ul>
<li>Competencia y l&iacute;mites de formaci&oacute;n (no practicar lo que no se domina).</li>
<li>Confidencialidad y sus excepciones.</li>
<li>Consentimiento informado y respeto a la autonom&iacute;a.</li>
<li>Integridad, honestidad en publicidad y honorarios.</li>
<li>Relaciones duales y conflictos de inter&eacute;s.</li>
<li>Responsabilidad en investigaci&oacute;n, docencia y supervisi&oacute;n.</li>
</ul>
<p>El c&oacute;digo no reemplaza la ley, pero s&iacute; traduce valores a conductas. L&eacute;alo junto a su c&eacute;dula, al reglamento del establecimiento si labora en instituci&oacute;n, y a las NOM que toquen su expediente.</p>"""},
{"h2":"C&eacute;dula, NOM y otros lineamientos que se cruzan","html":"""<p>La <strong>c&eacute;dula profesional</strong> acredita t&iacute;tulo; el c&oacute;digo orienta c&oacute;mo ejercer. En documentaci&oacute;n cl&iacute;nica, la <a href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a> define contenido y manejo del expediente. Si digitaliza, considere el esp&iacute;ritu de <a href="/articulos/nom-024-nom-004-psicologos-mexico.html">NOM-024 vs NOM-004</a> y la <a href="/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html">LFPDPPP</a>.</p>
<p>En salud laboral aparece <a href="/articulos/nom-035-ssa3-salud-mental-trabajo.html">NOM-035</a>; en atenci&oacute;n psiqui&aacute;trica, referencias a NOM-025. No todo psic&oacute;logo aplica todas las NOM, pero s&iacute; debe saber cu&aacute;les le tocan seg&uacute;n contexto.</p>
<p>Publicidad enga&ntilde;osa, t&iacute;tulos inventados o promesas de cura violan &eacute;tica y pueden tener consecuencias legales. Revise su sitio web y redes con la misma rigurosidad que su nota cl&iacute;nica.</p>"""},
{"h2":"Confidencialidad, roles duales y redes","html":"""<p>La confidencialidad es la regla; las excepciones deben anticiparse en el <a href="/articulos/consentimiento-informado-elementos-mx-co.html">consentimiento</a>. No discuta casos identificables en grupos de WhatsApp sin anonimizar. En redes, evite contenido que exponga pacientes aunque &laquo;no diga el nombre&raquo; si el contexto los hace reconocibles.</p>
<p>Los <strong>roles duales</strong> (amigo, socio, docente y terapeuta a la vez) aumentan riesgo de da&ntilde;o. Si no puede evitarlos, documente mitigaciones, derive cuando proceda y priorice el bienestar del usuario del servicio. En supervisi&oacute;n, mantenga fronteras claras entre ense&ntilde;anza y terapia del supervisado.</p>"""},
{"h2":"Checklist &eacute;tico para consulta privada","html":"""<ol>
<li>C&eacute;dula y datos profesionales visibles y actualizados.</li>
<li>Consentimiento y aviso de privacidad vigentes.</li>
<li>Expediente alineado a NOM-004 con notas oportunas.</li>
<li>Pol&iacute;tica escrita de confidencialidad y crisis.</li>
<li>Publicidad sin promesas enga&ntilde;osas.</li>
<li>Canal de supervisi&oacute;n o interconsulta para casos l&iacute;mite.</li>
<li>Seguro de responsabilidad civil si su riesgo lo amerita.</li>
</ol>
<p>Compare con el marco colombiano (<a href="/articulos/ley-1090-psicologia-colombia.html">Ley 1090</a>) si atiende poblaci&oacute;n binacional. La &eacute;tica local manda; la comparaci&oacute;n solo ilumina.</p>"""+closer("codigo-deontologico-psicologo-mexico")},
],
"faqs":[
{"q":"&iquest;El c&oacute;digo &eacute;tico es ley?","a":"Es normativa profesional deontológica. Se articula con leyes y NOM, pero no las sustituye. Incumplir puede tener consecuencias colegiadas y clínicas."},
{"q":"&iquest;Debo citar NOM-004 en el c&oacute;digo?","a":"El c&oacute;digo habla de deberes; la NOM-004 opera el expediente. Ambos se necesitan en consulta documentada."},
{"q":"&iquest;Puedo atender fuera de mi especialidad?","a":"Solo dentro de su competencia. Forme, supervise o derive. Improvisar técnicas sin entrenamiento viola el principio de competencia."},
{"q":"&iquest;Qu&eacute; hago con un conflicto dual?","a":"Evalúe riesgo de daño, documente, busque supervisión y derive si la dualidad compromete el juicio."},
{"q":"&iquest;Dónde consulto el texto oficial?","a":"En fuentes de la SMP / colegios y documentos éticos vigentes. Esta guía es orientación práctica, no el texto normativo completo."},
],
"related":[
{"href":"/articulos/nom-004-historia-clinica-mexico.html","label":"NOM-004"},
{"href":"/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html","label":"LFPDPPP"},
{"href":"/articulos/consentimiento-informado-elementos-mx-co.html","label":"Consentimiento MX/CO"},
{"href":"/articulos/ley-1090-psicologia-colombia.html","label":"Ley 1090 Colombia"},
],
})

print('built', len(SPECS), 'so far')
for s in SPECS:
    print(s['slug'], 'intro', wc(s['intro_long']), 'title', len(s['title']), 'desc', len(s['description']))
    assert 50<=wc(s['intro_long'])<=60
    assert 55<=len(s['title'])<=60
    assert 150<=len(s['description'])<=160

# Continue remaining 5 in same file - write to partial then append
Path('/tmp/aeo8_specs_part1.json').write_text(json.dumps(SPECS, ensure_ascii=False), encoding='utf-8')
print('part1 saved')
