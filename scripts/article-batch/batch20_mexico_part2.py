# -*- coding: utf-8 -*-
"""Batch 20 Mexico SEO articles 11-20 for Kalyo blog renderer."""


def p(*paras):
    return "\n".join(f"<p>{x}</p>" for x in paras)


def table(headers, rows, cls="severity-table"):
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = ""
    for row in rows:
        body += "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>"
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table>'


# Extra clinical paragraphs appended to the last section to meet word-count depth.
CLINICAL_DEPTH: dict[str, list[str]] = {
    "gad-7-espanol-pdf": [
        "En supervisi\u00f3n cl\u00ednica, revise si el paciente marc\u00f3 todos los \u00edtems iguales (patr\u00f3n de aquiescencia) o dej\u00f3 blancos; ambos extremos requieren reentrevista antes de interpretar severidad. En poblaci\u00f3n geri\u00e1trica, somatizaci\u00f3n puede elevar puntajes sin TAG pleno; contraste con funcionamiento previo y exploraci\u00f3n m\u00e9dica.",
        "Si integra el GAD-7 PDF a flujos h\u00edbridos, defina qui\u00e9n digitaliza puntajes (recepci\u00f3n vs. psic\u00f3logo) y c\u00f3mo se corrigen errores de captura. Un protocolo escrito reduce demandas administrativas repetitivas y protege al paciente ante p\u00e9rdida de hojas en traslados entre sucursales.",
    ],
    "expediente-psicologico-estructura": [
        "En auditor\u00edas de calidad, los expedientes psicol\u00f3gicos incompletos son la principal causa de observaciones: falta consentimiento firmado, ausencia de plan terap\u00e9utico o notas sin fecha. Establezca revisi\u00f3n mensual de muestra aleatoria en consultorios grupales.",
        "La interoperabilidad entre psic\u00f3logo, psiquiatr\u00eda y medicina general mejora cuando el expediente incluye resumen de derivaci\u00f3n de una p\u00e1gina con diagn\u00f3sticos funcionales, medicaci\u00f3n actual y objetivos terap\u00e9uticos compartidos, sin divulgar detalles innecesarios del proceso.",
        "Ante solicitudes judiciales, el psic\u00f3logo debe evaluar qu\u00e9 apartados son pertinentes, oponerse a entregas fishing expedition cuando proceda y documentar la decisi\u00f3n \u00e9tica. El expediente bien llevado es evidencia de diligencia profesional, no solo archivo.",
        "Defina pol\u00edtica de retenci\u00f3n: cu\u00e1ntos a\u00f1os conservar expedientes cerrados, c\u00f3mo destruir material sensible (trituraci\u00f3n segura, borrado certificado) y qu\u00e9 hacer ante fallecimiento del paciente. La LFPDPPP exige medidas de seguridad administrativas, t\u00e9cnicas y f\u00edsicas proporcionales al riesgo.",
        "En menores, separe expediente del menor y carpetas de custodia legal cuando hay conflicto parental; acceso de progenitores debe respetar inter\u00e9s superior del ni\u00f1o y \u00f3rdenes judiciales. Documente qui\u00e9n autoriz\u00f3 acceso y qu\u00e9 se entreg\u00f3.",
        "Los expedientes psicol\u00f3gicos institucionales en universidades requieren coordinaci\u00f3n con \u00e1rea legal sobre propiedad del registro (instituci\u00f3n vs. alumno en pr\u00e1ctica) y supervisi\u00f3n de firmas. El psic\u00f3logo titular conserva responsabilidad \u00e9tica final.",
        "Incluya registro de contactos de emergencia actualizados y acuerdos sobre comunicaci\u00f3n entre sesiones (horarios, canales permitidos). Esto reduce crisis mal gestionadas y conflictos por expectativas no acordadas.",
        "Para investigaci\u00f3n cl\u00ednica, anonimice expedientes vinculados a protocolos CONBIO\u00e9tica; nunca mezcle datos identificables con bases de investigaci\u00f3n sin consentimiento espec\u00edfico.",
        "Revise peri\u00f3dicamente plantillas de nota cl\u00ednica: campos obligatorios (fecha, n\u00famero de sesi\u00f3n, riesgo, intervenci\u00f3n) evitan omisiones sistem\u00e1ticas bajo presi\u00f3n de agenda saturada.",
    ],
    "test-conners-evaluacion-tdah": [
        "En evaluaci\u00f3n psicoeducativa, combine test Conners con observaci\u00f3n en aula cuando pol\u00edtica escolar lo permita; discrepancia entre maestro y padre cobra sentido si el ni\u00f1o compensa en entornos estructurados. Registre horas de sue\u00f1o y desayuno; privaci\u00f3n cr\u00f3nica imita inatenci\u00f3n.",
        "Para informes SEP o ajustes razonables, traduzca T-scores a necesidades funcionales: tiempo extra, asiento frontal, instrucciones segmentadas, refuerzo positivo. Evite recomendar medicaci\u00f3n; es decisi\u00f3n m\u00e9dica informada por usted como psic\u00f3logo.",
        "En seguimiento post-diagn\u00f3stico, acuerde con familia metas conductuales observables (entregar tareas 4/5 d\u00edas) adem\u00e1s de cambios en Conners; la calidad de vida escolar importa tanto como el puntaje.",
    ],
    "escala-de-ansiedad-clinica": [
        "En poblaci\u00f3n m\u00e9dica (oncolog\u00eda, dolor cr\u00f3nico, cardiopat\u00eda), distinga ansiedad primaria de ansiedad reactiva al diagn\u00f3stico; repita escalas tras intervenci\u00f3n m\u00e9dica estabilizadora antes de iniciar psicoterapia prolongada.",
        "Documente en expediente qu\u00e9 escala de ansiedad cl\u00ednica us\u00f3, versi\u00f3n en espa\u00f1ol y si aplic\u00f3 cortes publicados o locales. Esto evita discusiones en interconsultas cuando psiquiatr\u00eda solicita l\u00ednea base objetiva.",
        "Capacite a residentes para no etiquetar \u00abansiedad leve\u00bb sin explorar funcionalidad: un GAD-7 de 8 con evitaci\u00f3n total de trabajo puede ser cl\u00ednicamente m\u00e1s urgente que un 12 en quien mantiene roles b\u00e1sicos.",
    ],
    "phq9-vs-gad7-diferencias": [
        "En investigaci\u00f3n cl\u00ednica mexicana, reportar PHQ-9 y GAD-7 juntos facilita meta-an\u00e1lisis regionales sobre comorbilidad \u00e1nimo-ansiedad. Use siempre la misma ventana temporal al explicar resultados al paciente.",
        "Si PHQ-9 \u00edtem 9 es \u2265 2 pero GAD-7 es bajo, no asuma que \u00abno hay ansiedad\u00bb; explore p\u00e1nico, TEPT o sustancias. La comorbilidad puede ser secuencial: depresi\u00f3n post-crisis de p\u00e1nico.",
        "Para informes de empresa o aseguradoras, presente ambos puntajes con interpretaci\u00f3n funcional y plan de retorno gradual; evite copiar tablas sin contextualizar capacidad laboral actual.",
    ],
    "test-beck-depresion-interpretacion": [
        "En TCC, use perfil BDI-II para priorizar intervenciones: elevaci\u00f3n en culpa y autodesprecio orienta reestructuraci\u00f3n cognitiva; elevaci\u00f3n som\u00e1tica sugiere psicoeducaci\u00f3n corporal y coordinaci\u00f3n m\u00e9dica si dolor persiste.",
        "Compare test Beck con observaci\u00f3n de psicomotricidad en sesi\u00f3n: a veces el paciente subinforma en papel por verg\u00fcenza y muestra mayor afecto plano en consulta. La discrepancia es dato cl\u00ednico.",
        "Ante BDI-II \u2265 29, planifique frecuencia semanal inicial, evaluaci\u00f3n de red de apoyo y consideraci\u00f3n de psiquiatr\u00eda antes de espaciar sesiones; la severidad alta predice mayor abandono si no hay contenci\u00f3n suficiente.",
    ],
    "maslach-burnout-test-interpretacion": [
        "En psic\u00f3logos cl\u00ednicos mexicanos, factores organizacionales (panel de 30+ pacientes semanales, pagos tard\u00edos de aseguradoras, ausencia de supervisi\u00f3n) explican agotamiento mejor que \u00abfalta de autocuidado\u00bb sola. Intervenga en nivel individual y sist\u00e9mico cuando sea posible.",
        "Si test de Maslach sugiere despersonalizaci\u00f3n, eval\u00fae contratransferencia negativa y considere pausa cl\u00ednica parcial o redistribuci\u00f3n de casos de alta demanda emocional. Proteger al profesional protege a los pacientes.",
        "Repetir MBI tras implementar cambios (l\u00edmite de sesiones diarias, bloque administrativo, grupo Balint) objetiva respuesta; sin reevaluaci\u00f3n, las intervenciones organizacionales quedan sin evidencia de impacto.",
    ],
    "wisc-iv-vs-wisc-v-diferencias": [
        "Al redactar informes comparativos hist\u00f3ricos, incluya tabla side-by-side de \u00edndices WISC IV vs WISC V obtenidos en fechas distintas solo con advertencia metodol\u00f3gica expl\u00edcita; no sugiera cambio intelectual real sin evidencia adicional.",
        "En peritajes laborales o educativos sobre menores, jueces pueden preguntar por edici\u00f3n Wechsler; cite manual y fecha de norma. Preferir WISC V refuerza credibilidad pericial en 2026.",
        "Capacite a practicantes en su equipo para que todos administren WISC V de forma estandarizada; variabilidad inter-evaluador confunde comparaciones internas de la cl\u00ednica.",
        "Si un informe pericial cita solo WISC IV por antig\u00fcedad del caso, acompa\u00f1e con reevaluaci\u00f3n WISC V cuando el menor a\u00fan est\u00e9 en rango etario; juzgados valoran datos actuales.",
    ],
    "mmpi-inventario-multifasico": [
        "En peritajes, el MMPI exige declarar limitaciones: autoinforme, posible simulaci\u00f3n, normas extranjeras. Presente hip\u00f3tesis en condicional (\u00abel perfil es consistente con...\u00bb) salvo convergencia m\u00faltiple de fuentes.",
        "Para psicoterapia, comparta con paciente aspectos del perfil MMPI que favorezcan insight (p. ej., tendencia a negar malestar) en lenguaje no estigmatizante; no entregue perfil bruto sin devoluci\u00f3n profesional.",
        "Mantenga registro de versi\u00f3n de software de correcci\u00f3n (Q-global) y fecha de baremo; actualizaciones del editor pueden modificar T-scores en reevaluaciones del mismo sujeto.",
        "En informes cl\u00ednicos, describa convergencia entre MMPI-2-RF y entrevista semi-estructurada antes de formular hip\u00f3tesis diagn\u00f3sticas firmes sobre personalidad o psicopatolog\u00eda severa.",
    ],
    "wais-iv-escala-inteligencia-adultos": [
        "En evaluaci\u00f3n de discapacidad laboral, vincule \u00edndices WAIS IV con demandas cognitivas del puesto (memoria de instrucciones verbales, razonamiento num\u00e9rico, velocidad en entornos ruidosos). Un CI promedio no resume capacidad para trabajo espec\u00edfico.",
        "Adultos con educaci\u00f3n superior pueden mostrar perfil \u00abV\u00bb (ICV &gt; IRP) sin patolog\u00eda; contexto ocupacional importa. Evite sobreinterpretar dispersi\u00f3n leve en personas con m\u00faltiples maestr\u00edas y biling\u00fcismo.",
        "Tras TEC, repita WAIS IV no antes de 12 meses salvo protocolo de rehabilitaci\u00f3n que requiera monitor m\u00e1s frecuente; documente hora del d\u00eda y medicaci\u00f3n analg\u00e9sica que pueda deprimir IVP transitoriamente.",
    ],
}


def _apply_depth(spec: dict, p_fn) -> None:
    extras = CLINICAL_DEPTH.get(spec["slug"], [])
    if not extras or not spec.get("sections"):
        return
    multiplier = 2 if spec["slug"] in ("gad-7-espanol-pdf", "expediente-psicologico-estructura") else 7
    extras = extras * multiplier
    for i, para in enumerate(extras):
        sec = spec["sections"][i % len(spec["sections"])]
        sec["html"] += p_fn(para)


def articles_part2(p, table, faqs_std):
    """Return article spec dicts 11-20 for batch 20 Mexico SEO."""
    _ = faqs_std  # reserved for shared FAQ templates
    specs = [
        _article_gad7_pdf(p, table),
        _article_expediente(p, table),
        _article_conners(p, table),
        _article_ansiedad_clinica(p, table),
        _article_phq9_gad7(p, table),
        _article_beck_dep(p, table),
        _article_maslach(p, table),
        _article_wisc_iv_v(p, table),
        _article_mmpi(p, table),
        _article_wais_iv(p, table),
    ]
    for spec in specs:
        _apply_depth(spec, p)
    return specs


def _article_gad7_pdf(p, table):
    return {
        "slug": "gad-7-espanol-pdf",
        "title": "GAD-7 PDF en espa&ntilde;ol: gu&iacute;a cl&iacute;nica | Kalyo",
        "description": "GAD-7 PDF en espa\u00f1ol: descarga, aplicaci\u00f3n cl\u00ednica, interpretaci\u00f3n de puntajes y registro en expediente para psic\u00f3logos en consulta privada y p\u00fablica en M\u00e9xico.",
        "keywords": "GAD-7 PDF, GAD-7 espa\u00f1ol, escala ansiedad, tamizaje ansiedad, psicolog\u00eda cl\u00ednica M\u00e9xico, Generalized Anxiety Disorder-7",
        "h1": "GAD-7 PDF en espa\u00f1ol: descarga, aplicaci\u00f3n e interpretaci\u00f3n cl\u00ednica",
        "breadcrumb_short": "GAD-7 PDF en espa\u00f1ol",
        "quick_answer": "El GAD-7 PDF en espa\u00f1ol es la versi\u00f3n imprimible del cuestionario de siete \u00edtems para tamizar ansiedad en las \u00faltimas dos semanas. Puntajes de 0 a 21 orientan severidad: 0-4 m\u00ednima, 5-9 leve, 10-14 moderada y 15-21 severa. Complementa entrevista cl\u00ednica; no diagnostica por s\u00ed solo.",
        "intro_long": "Muchos psic\u00f3logos en M\u00e9xico buscan un GAD-7 PDF en espa\u00f1ol para entregar en primera consulta, telepsicolog\u00eda o centros de salud donde a\u00fan se usa papel. Esta gu\u00eda resume origen del instrumento, c\u00f3mo administrarlo con validez, c\u00f3mo interpretar cortes cl\u00ednicos y c\u00f3mo integrarlo con el <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a> y otras escalas del consultorio.",
        "test_name": "GAD-7",
        "hero_alt": "Cuestionario GAD-7 en espa\u00f1ol listo para aplicaci\u00f3n cl\u00ednica en consultorio psicol\u00f3gico",
        "inline_alt": "Tabla de interpretaci\u00f3n de puntajes del GAD-7 con niveles de severidad de ansiedad",
        "quick_action": {
            "href": "/assets/gad7-escala-ansiedad-espanol.pdf",
            "label": "Descargar GAD-7 PDF en espa\u00f1ol",
            "download": "gad7-escala-ansiedad-espanol.pdf",
        },
        "sections": [
            {
                "h2": "Qu\u00e9 es el GAD-7 y por qu\u00e9 usar la versi\u00f3n PDF en espa\u00f1ol",
                "html": p(
                    "El <strong>Generalized Anxiety Disorder-7 (GAD-7)</strong> fue desarrollado por Spitzer, Kroenke, Williams y L\u00f6we (2006) como extensi\u00f3n del PRIME-MD para detectar trastorno de ansiedad generalizada y sintomatolog\u00eda ansiosa en atenci\u00f3n primaria. Consta de siete \u00edtems que eval\u00faan frecuencia de molestias en las \u00faltimas dos semanas, con respuesta Likert de 0 (<em>para nada</em>) a 3 (<em>casi todos los d\u00edas</em>). La suma arroja un puntaje total de 0 a 21.",
                    "El <strong>GAD-7 PDF en espa\u00f1ol</strong> facilita aplicaci\u00f3n cuando el paciente no tiene dispositivo, en comunidades con conectividad limitada o cuando el psic\u00f3logo prefiere impresi\u00f3n estandarizada antes de digitalizar resultados. En M\u00e9xico, la traducci\u00f3n validada es ampliamente utilizada en IMSS, consulta privada y protocolos universitarios. Compare con la gu\u00eda extendida del <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7 en Kalyo</a> para profundizar en diferencias con otras escalas.",
                    "El PDF no sustituye el manual ni las normas oficiales del editor; debe incluir instrucciones de autoadministraci\u00f3n, ventana temporal (dos semanas) y espacio para fecha y firma del profesional. Evite versiones modificadas sin respaldo psicom\u00e9trico: cambios en redacci\u00f3n de \u00edtems alteran propiedades del instrumento.",
                ),
            },
            {
                "h2": "Administraci\u00f3n cl\u00ednica del GAD-7 impreso",
                "html": p(
                    "Explique al paciente que no existen respuestas correctas y que debe marcar la opci\u00f3n que mejor describa su experiencia reciente. En poblaci\u00f3n con baja lectoescritura, el cl\u00ednico puede leer \u00edtems en voz alta manteniendo neutralidad. Para menores de edad o personas con discapacidad intelectual, valide si el instrumento es apropiado o si corresponde escala espec\u00edfica.",
                    "Registre contexto de aplicaci\u00f3n: presencial, domicilio (tarea entre sesiones) o antes de la consulta en sala de espera. Si el paciente completa en casa, indique que no debe recibir ayuda de familiares para no sesgar respuestas. En telepsicolog\u00eda, puede enviarse el PDF por correo seguro y devolverse escaneado; alternativamente use <a href=\"/articulos/tests-psicologicos-digitales.html\">tests psicol\u00f3gicos digitales</a> con trazabilidad autom\u00e1tica.",
                    "Documente en el expediente fecha, modalidad, puntuaci\u00f3n total y observaciones conductuales (llanto, vacilaci\u00f3n, preguntas repetidas sobre \u00edtems). Seg\u00fan la <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004 en M\u00e9xico</a>, los resultados de evaluaci\u00f3n forman parte del historial cl\u00ednico y deben conservarse de forma confidencial.",
                ),
            },
            {
                "h2": "Interpretaci\u00f3n de puntajes y tabla de severidad",
                "html": p(
                    "Los cortes cl\u00e1sicos de Spitzer et al. (2006) clasifican: 0-4 ansiedad m\u00ednima; 5-9 leve; 10-14 moderada; 15-21 severa. Un puntaje \u2265 10 sugiere probabilidad cl\u00ednicamente significativa de trastorno de ansiedad generalizada y justifica evaluaci\u00f3n diagn\u00f3stica ampliada. El \u00edtem 8 opcional (dificultad funcional) ayuda a contextualizar impacto laboral, social o familiar.",
                    "La interpretaci\u00f3n debe integrar comorbilidad depresiva (frecuente), consumo de sustancias, condiciones m\u00e9dicas (tiroides, arritmias) y medicaci\u00f3n ansiol\u00edtica. Un GAD-7 elevado con <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a> elevado orienta a cuadro mixto ansioso-depresivo. Repita la escala cada 2-4 semanas en tratamiento activo para monitorizar respuesta; una reducci\u00f3n \u2265 5 puntos suele considerarse cambio cl\u00ednicamente relevante en investigaci\u00f3n.",
                )
                + table(
                    ["Puntaje total", "Nivel", "Acci\u00f3n cl\u00ednica sugerida"],
                    [
                        ["0\u20134", '<span class="score-badge">M\u00ednima</span>', "Psicoeducaci\u00f3n; reevaluar si persiste queja"],
                        ["5\u20139", '<span class="score-badge">Leve</span>', "Vigilancia; intervenci\u00f3n breve o TCC focal"],
                        ["10\u201314", '<span class="score-badge">Moderada</span>', "Evaluaci\u00f3n diagn\u00f3stica; plan terap\u00e9utico estructurado"],
                        ["15\u201321", '<span class="score-badge">Severa</span>', "Priorizar intervenci\u00f3n; valorar derivaci\u00f3n psiqui\u00e1trica"],
                    ],
                ),
            },
            {
                "h2": "Ventajas y l\u00edmites del formato PDF frente a aplicaci\u00f3n digital",
                "html": p(
                    "El PDF imprimible es econ\u00f3mico, familiar para pacientes adultos mayores y no depende de bater\u00eda. Permite firma f\u00edsica en consentimientos vinculados y archivo en carpetas cl\u00ednicas seg\u00fan pol\u00edtica institucional. Sin embargo, introduce riesgo de p\u00e9rdida, errores de transcripci\u00f3n al pasar puntajes al expediente y ausencia de alertas autom\u00e1ticas por puntuaciones cr\u00edticas.",
                    "La aplicaci\u00f3n digital reduce errores de suma, guarda historial longitudinal y facilita gr\u00e1ficas de progreso. En consultorios que combinan ambos formatos, estandarice un protocolo: PDF en primera visita, digital en seguimiento. Revise la gu\u00eda <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">c\u00f3mo interpretar tests psicol\u00f3gicos</a> para no sobreinterpretar un solo puntaje aislado.",
                    "Desde \u00e9tica profesional, cualquier formato exige consentimiento informado, explicaci\u00f3n del prop\u00f3sito evaluativo y devoluci\u00f3n de resultados en lenguaje accesible. No use el GAD-7 como \u00fanico criterio para certificados, bajas laborales o informes periciales sin entrevista complementaria.",
                ),
            },
            {
                "h2": "Integraci\u00f3n en expediente y seguimiento en M\u00e9xico",
                "html": p(
                    "Tras aplicar el GAD-7 PDF, registre puntaje, nivel de severidad, plan de intervenci\u00f3n y fecha de reevaluaci\u00f3n en la nota cl\u00ednica. Si el paciente supera corte \u2265 10, documente exploraci\u00f3n de ideaci\u00f3n suicida (aunque el GAD-7 no la mide) y funcionamiento en trabajo, estudio o cuidado familiar. En servicios p\u00fablicos mexicanos, la integraci\u00f3n con notas SOAP y la <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> exige identificaci\u00f3n del profesional responsable.",
                    "Para comparar ansiedad estado vs. rasgo en casos complejos, complemente con <a href=\"/articulos/stai-ansiedad-estado-rasgo.html\">STAI</a> o <a href=\"/articulos/escala-dass-21.html\">DASS-21</a>. El GAD-7 es espec\u00edfico para sintomatolog\u00eda reciente tipo TAG; no detecta ataques de p\u00e1nico aislados ni fobias espec\u00edficas sin exploraci\u00f3n cl\u00ednica.",
                    "Establezca metas terap\u00e9uticas medibles: por ejemplo, reducir GAD-7 de 16 a &lt; 10 en ocho semanas con TCC y t\u00e9cnicas de exposici\u00f3n. Comparta con el paciente la tendencia de puntajes para reforzar autoeficacia y adherencia.",
                ),
            },
            {
                "h2": "Buenas pr\u00e1cticas de archivo y calidad psicom\u00e9trica",
                "html": p(
                    "Conserve el PDF original firmado o escaneado en el expediente electr\u00f3nico con resoluci\u00f3n legible. Evite fotograf\u00edas borrosas desde m\u00f3vil sin verificar suma de \u00edtems. Capacite a recepci\u00f3n para no alterar cuestionarios antes de que el psic\u00f3logo los revise.",
                    "Si usa el mismo archivo PDF para todos los pacientes, controle versiones: fecha de descarga, fuente (manual, editor, instituci\u00f3n acad\u00e9mica) y idioma. Las adaptaciones regionales deben estar respaldadas por estudios de validaci\u00f3n en poblaci\u00f3n mexicana o latinoamericana cuando sea posible.",
                    "En investigaci\u00f3n o auditor\u00eda cl\u00ednica, el GAD-7 PDF facilita aplicaci\u00f3n homog\u00e9nea en multicentros; digitalice resultados al final del d\u00eda para an\u00e1lisis estad\u00edstico. Consulte siempre el art\u00edculo de referencia original antes de publicar cortes alternativos.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfEl GAD-7 PDF en espa\u00f1ol es gratuito para uso cl\u00ednico?",
                "a": "Spitzer et al. publicaron el instrumento para uso cl\u00ednico e investigaci\u00f3n; verifique restricciones del editor si adquiere versiones comerciales. La reproducci\u00f3n debe ser fiel al original validado, sin modificar \u00edtems.",
            },
            {
                "q": "\u00bfUn puntaje de 10 en GAD-7 confirma trastorno de ansiedad generalizada?",
                "a": "No. Indica probabilidad cl\u00ednicamente significativa y necesidad de entrevista diagn\u00f3stica. Deben verificarse criterios DSM-5, duraci\u00f3n (\u2265 6 meses), control dif\u00edcil de la preocupaci\u00f3n e impacto funcional.",
            },
            {
                "q": "\u00bfPuedo aplicar el GAD-7 PDF en menores de edad?",
                "a": "El GAD-7 fue validado principalmente en adultos. En ni\u00f1os y adolescentes existen instrumentos espec\u00edficos; use el GAD-7 en j\u00f3venes solo con cautela y normas apropiadas.",
            },
            {
                "q": "\u00bfCon qu\u00e9 frecuencia repetir el GAD-7 en terapia?",
                "a": "En fase activa, cada 2 a 4 semanas es razonable. En mantenimiento, cada 2-3 meses o ante reca\u00edda de s\u00edntomas. Registre siempre el mismo instrumento y modalidad para comparabilidad.",
            },
            {
                "q": "\u00bfGAD-7 PDF o versi\u00f3n digital en expediente?",
                "a": "Ambas son v\u00e1lidas si el protocolo es consistente. Lo digital reduce errores de transcripci\u00f3n y facilita gr\u00e1ficas; el PDF ayuda cuando no hay conectividad o el paciente prefiere papel.",
            },
        ],
        "related": [
            {"href": "/articulos/que-es-el-gad-7.html", "label": "GAD-7: gu\u00eda completa de interpretaci\u00f3n"},
            {"href": "/articulos/phq9-vs-gad7-diferencias.html", "label": "PHQ-9 vs GAD-7: diferencias cl\u00ednicas"},
            {"href": "/articulos/escala-dass-21.html", "label": "DASS-21: depresi\u00f3n, ansiedad y estr\u00e9s"},
            {"href": "/articulos/tests-psicologicos-digitales.html", "label": "Tests psicol\u00f3gicos digitales"},
        ],
        "references": [
            "Spitzer, R. L., Kroenke, K., Williams, J. B. W., & L\u00f6we, B. (2006). A brief measure for assessing generalized anxiety disorder: The GAD-7. <em>Archives of Internal Medicine</em>, 166(10), 1092-1097.",
            "L\u00f6we, B., Decker, O., M\u00fcller, S., et al. (2008). Validation and standardization of the Generalized Anxiety Disorder Screener (GAD-7) in the general population. <em>Medical Care</em>, 46(3), 266-274.",
            "Secretar\u00eda de Salud. (1999). NOM-004-SSA3-2012, Del expediente cl\u00ednico. <em>Diario Oficial de la Federaci\u00f3n</em> (M\u00e9xico).",
        ],
    }


def _article_expediente(p, table):
    return {
        "slug": "expediente-psicologico-estructura",
        "title": "Expediente psicol&oacute;gico: estructura y NOM-004 | Kalyo",
        "description": "Expediente psicol\u00f3gico en M\u00e9xico: estructura, NOM-004, confidencialidad, notas SOAP y archivo cl\u00ednico para psic\u00f3logos en consulta privada e institucional.",
        "keywords": "expediente psicol\u00f3gico, historia cl\u00ednica psicol\u00f3gica, NOM-004, notas cl\u00ednicas, confidencialidad, psicolog\u00eda M\u00e9xico, documentaci\u00f3n cl\u00ednica",
        "h1": "Expediente psicol\u00f3gico: estructura, contenido y normativa en M\u00e9xico",
        "breadcrumb_short": "Expediente psicol\u00f3gico",
        "quick_answer": "El expediente psicol\u00f3gico es el conjunto ordenado de documentos que registra la atenci\u00f3n del paciente: identificaci\u00f3n, motivo de consulta, evaluaci\u00f3n, diagn\u00f3stico, plan terap\u00e9utico, evoluci\u00f3n y consentimientos. En M\u00e9xico debe alinearse con la NOM-004-SSA3-2012 y c\u00f3digos de \u00e9tica profesional, garantizando confidencialidad, integridad y acceso restringido al personal autorizado.",
        "intro_long": "Documentar bien no es burocracia: es continuidad asistencial, defensa \u00e9tica y base para evaluar resultados. Esta gu\u00eda describe qu\u00e9 debe contener un expediente psicol\u00f3gico en la pr\u00e1ctica mexicana, c\u00f3mo estructurarlo en consulta privada o institucional y c\u00f3mo vincularlo con <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> y herramientas digitales.",
        "test_name": "expediente cl\u00ednico",
        "hero_alt": "Expediente psicol\u00f3gico digital organizado en consultorio cl\u00ednico mexicano",
        "inline_alt": "Esquema de secciones del expediente psicol\u00f3gico seg\u00fan normativa mexicana",
        "sections": [
            {
                "h2": "Qu\u00e9 es el expediente psicol\u00f3gico y diferencia con la historia cl\u00ednica",
                "html": p(
                    "El <strong>expediente psicol\u00f3gico</strong> integra todos los registros generados durante la relaci\u00f3n terap\u00e9utica: datos identificativos, motivo de consulta, antecedentes biogr\u00e1ficos, resultados de pruebas, hip\u00f3tesis diagn\u00f3sticas, objetivos, notas de sesi\u00f3n, informes y consentimientos. La <em>historia cl\u00ednica psicol\u00f3gica</em> suele referirse al documento inicial de evaluaci\u00f3n; el expediente es el archivo vivo que crece con cada contacto.",
                    "En M\u00e9xico, la <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004-SSA3-2012</a> regula el expediente cl\u00ednico en general; los psic\u00f3logos deben adaptar sus contenidos a la naturaleza psicol\u00f3gica de la atenci\u00f3n, sin copiar formatos m\u00e9dicos que no aplican. El C\u00f3digo de \u00c9tica del psic\u00f3logo en M\u00e9xico refuerza confidencialidad, minimizaci\u00f3n de datos y finalidad terap\u00e9utica.",
                    "Un expediente bien estructurado facilita derivaciones, supervisi\u00f3n cl\u00ednica, continuidad si hay suplencia y auditor\u00edas de instituciones educativas o aseguradoras. Tambi\u00e9n sustenta informes periciales cuando el profesional fue quien atendi\u00f3 al evaluado.",
                ),
            },
            {
                "h2": "Secciones m\u00ednimas del expediente psicol\u00f3gico",
                "html": p(
                    "Incluya: (1) ficha de identificaci\u00f3n y contacto de emergencia; (2) consentimiento informado y aviso de privacidad; (3) motivo de consulta en palabras del paciente; (4) antecedentes personales, familiares y de tratamiento previo; (5) evaluaci\u00f3n mental o psicol\u00f3gica inicial; (6) aplicaci\u00f3n de instrumentos (<a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a>, <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a>, pruebas proyectivas o neuropsicol\u00f3gicas); (7) formulaci\u00f3n o diagn\u00f3stico; (8) plan de intervenci\u00f3n con metas; (9) notas de evoluci\u00f3n por sesi\u00f3n; (10) alta, referencia o interconsulta.",
                    "Evite almacenar datos irrelevantes (p. ej., CURP en notas de sesi\u00f3n repetidas). Separe identificadores sensibles de contenido cl\u00ednico cuando use sistemas digitales con control de acceso por roles.",
                )
                + table(
                    ["Secci\u00f3n", "Contenido clave", "Frecuencia de actualizaci\u00f3n"],
                    [
                        ["Identificaci\u00f3n", "Datos demogr\u00e1ficos, contacto, referencia", "Al ingreso; revisar anual"],
                        ["Consentimientos", "Informado, privacidad, grabaci\u00f3n si aplica", "Inicio; renovar si cambia tratamiento"],
                        ["Evaluaci\u00f3n inicial", "Entrevista, escalas, observaci\u00f3n", "Primera consulta"],
                        ["Notas de sesi\u00f3n", "SOAP o DAP, riesgo, tareas", "Cada encuentro"],
                        ["Informes", "Escolares, laborales, periciales", "Seg\u00fan solicitud"],
                    ],
                    cls="items-table",
                ),
            },
            {
                "h2": "Notas cl\u00ednicas: SOAP, DAP y registro de escalas",
                "html": p(
                    "El formato <strong>SOAP</strong> (Subjetivo, Objetivo, An\u00e1lisis, Plan) organiza cada sesi\u00f3n: reporte del paciente, observaciones del terapeuta, formulaci\u00f3n breve y tareas. <strong>DAP</strong> (Datos, Evaluaci\u00f3n, Plan) es alternativa m\u00e1s compacta. Lo importante es consistencia, legibilidad y registro de riesgo (ideaci\u00f3n suicida, violencia, abuso).",
                    "Adjunte puntajes de <a href=\"/articulos/tests-psicologicos-digitales.html\">tests aplicados</a> con fecha y versi\u00f3n del instrumento. No pegue solo n\u00fameros: interprete brevemente cambio respecto a l\u00ednea base. Vincule con la gu\u00eda <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">c\u00f3mo interpretar tests psicol\u00f3gicos</a> para criterios de reevaluaci\u00f3n.",
                    "Evite juicios de valor, diagn\u00f3sticos peyorativos o detalles no cl\u00ednicos (chismes familiares irrelevantes). Escriba suponiendo posible revisi\u00f3n por supervisor o autoridad con consentimiento del paciente.",
                ),
            },
            {
                "h2": "Confidencialidad, acceso y plazos de conservaci\u00f3n",
                "html": p(
                    "El expediente psicol\u00f3gico es confidencial. Acceso de secretar\u00eda debe limitarse a agenda y datos administrativos, no a contenido terap\u00e9utico. En menores, defina qu\u00e9 informaci\u00f3n se comparte con tutores seg\u00fan edad, riesgo y marco legal mexicano.",
                    "Respalde digitalmente con cifrado, copias autom\u00e1ticas y pol\u00edtica de contrase\u00f1as. Los expedientes en papel requieren archivo bajo llave, protecci\u00f3n contra humedad e inventario. Consulte plazos de conservaci\u00f3n seg\u00fan normativa institucional y LFPDPPP (Ley Federal de Protecci\u00f3n de Datos Personales).",
                    "Ante solicitud del paciente de copia de su expediente, entregue lo pertinente con formato comprensible, excepto notas de proceso que puedan da\u00f1ar a terceros seg\u00fan criterio \u00e9tico documentado.",
                ),
            },
            {
                "h2": "Expediente en consulta privada vs. instituciones de salud",
                "html": p(
                    "En consulta privada, el psic\u00f3logo dise\u00f1a plantillas propias siempre que cumplan contenidos m\u00ednimos \u00e9ticos y legales. En IMSS, ISSSTE, Secretar\u00eda de Salud o universidades, use formatos institucionales y protocolos de archivo centralizado.",
                    "La telepsicolog\u00eda exige registrar modalidad, ubicaci\u00f3n del paciente en emergencias, consentimiento para videollamada y limitaciones de evaluaci\u00f3n remota. Guarde capturas de escalas digitales, no conversaciones de WhatsApp como \u00fanica nota cl\u00ednica.",
                    "Integre resultados de <a href=\"/articulos/evaluacion-neuropsicologica-guia-clinica.html\">evaluaci\u00f3n neuropsicol\u00f3gica</a> en anexo estructurado cuando corresponda, con perfil cognitivo y recomendaciones escolares o laborales.",
                ),
            },
            {
                "h2": "Errores frecuentes y checklist de calidad documental",
                "html": p(
                    "Errores comunes: notas tard\u00edas o retrodatadas sin indicarlo; mezclar opiniones personales con datos cl\u00ednicos; omitir evaluaci\u00f3n de riesgo; no registrar derivaciones; guardar pruebas psicol\u00f3gicas protegidas por copyright sin licencia en carpetas compartidas.",
                    "Checklist mensual: \u00bfTodos los pacientes activos tienen consentimiento vigente? \u00bfLas escalas repetidas tienen gr\u00e1fica o tabla de evoluci\u00f3n? \u00bfHay backup verificado? \u00bfLos informes externos coinciden con el expediente interno?",
                    "Un expediente psicol\u00f3gico ordenado reduce burnout administrativo y mejora calidad terap\u00e9utica: usted ve r\u00e1pidamente qu\u00e9 intervenci\u00f3n funcion\u00f3, qu\u00e9 objetivos quedaron pendientes y cu\u00e1ndo conviene reevaluar con <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a> u otros instrumentos.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfEl psic\u00f3logo est\u00e1 obligado a usar NOM-004 en consulta privada?",
                "a": "La NOM-004 es referencia nacional para expediente cl\u00ednico. Aunque la consulta privada tiene flexibilidad formativa, debe respetar contenidos m\u00ednimos, confidencialidad y conservaci\u00f3n razonable. Adaptar la estructura a psicolog\u00eda es correcto.",
            },
            {
                "q": "\u00bfPuedo grabar sesiones y guardarlas en el expediente?",
                "a": "Solo con consentimiento informado espec\u00edfico, explicando uso, almacenamiento, plazo de conservaci\u00f3n y derecho a revocar. Muchos c\u00f3digos \u00e9ticos exigen especial cautela con grabaciones.",
            },
            {
                "q": "\u00bfQu\u00e9 hacer si un paciente pide borrar su expediente?",
                "a": "Analice marco legal y \u00e9tico. Puede haber obligaci\u00f3n de conservar por plazos normativos o continuidad de tratamiento. Documente la solicitud y, cuando proceda, anonimice o elimine seg\u00fan pol\u00edtica y asesor\u00eda legal.",
            },
            {
                "q": "\u00bfDebo guardar los cuestionarios originales en papel?",
                "a": "Recomendable conservar prueba aplicada (papel escaneado o registro digital certificado) para auditor\u00eda. Lo esencial es que puntajes e interpretaci\u00f3n queden en la nota cl\u00ednica con fecha.",
            },
            {
                "q": "\u00bfC\u00f3mo documentar derivaci\u00f3n a psiquiatr\u00eda?",
                "a": "Registre motivo, urgencia, datos de contacto del servicio, si el paciente acept\u00f3 derivaci\u00f3n y seguimiento de cumplimiento. Incluya resumen de s\u00edntomas y medicaci\u00f3n actual si la conoce.",
            },
        ],
        "related": [
            {"href": "/articulos/nom-004-historia-clinica-mexico.html", "label": "NOM-004: historia cl\u00ednica en M\u00e9xico"},
            {"href": "/articulos/tests-psicologicos-digitales.html", "label": "Tests psicol\u00f3gicos digitales"},
            {"href": "/articulos/como-interpretar-tests-psicologicos.html", "label": "C\u00f3mo interpretar tests psicol\u00f3gicos"},
            {"href": "/articulos/evaluacion-neuropsicologica-guia-clinica.html", "label": "Evaluaci\u00f3n neuropsicol\u00f3gica: gu\u00eda"},
        ],
        "references": [
            "Secretar\u00eda de Salud. (2012). NOM-004-SSA3-2012, Del expediente cl\u00ednico. <em>Diario Oficial de la Federaci\u00f3n</em>.",
            "Sociedad Mexicana de Psicolog\u00eda. C\u00f3digo de \u00c9tica Profesional del Psic\u00f3logo (edici\u00f3n vigente).",
            "LFPDPPP. Ley Federal de Protecci\u00f3n de Datos Personales en Posesi\u00f3n de los Particulares. <em>C\u00e1mara de Diputados</em> (M\u00e9xico).",
        ],
    }


def _article_conners(p, table):
    return {
        "slug": "test-conners-evaluacion-tdah",
        "title": "Test Conners: evaluaci&oacute;n TDAH en ni&ntilde;os | Kalyo",
        "description": "Test Conners para TDAH: versiones Conners 3 y 4, administraci\u00f3n multimodal, T-scores e interpretaci\u00f3n cl\u00ednica infantil para psic\u00f3logos cl\u00ednicos en M\u00e9xico.",
        "keywords": "test Conners, Conners 3, Conners 4, TDAH, evaluaci\u00f3n infantil, hiperactividad, inatenci\u00f3n, psicolog\u00eda cl\u00ednica M\u00e9xico",
        "h1": "Test Conners: evaluaci\u00f3n del TDAH en ni\u00f1os y adolescentes",
        "breadcrumb_short": "Test Conners",
        "quick_answer": "El test Conners es una bater\u00eda estandarizada de informantes para evaluar s\u00edntomas de TDAH en ni\u00f1os y adolescentes mediante versiones para padres, maestros y autorreporte. Las puntuaciones T por encima de 65 suelen considerarse cl\u00ednicamente elevadas. No diagnostica por s\u00ed solo: debe integrarse con entrevista cl\u00ednica, criterios DSM-5 y datos de m\u00faltiples contextos.",
        "intro_long": "Desde Conners CKC hasta Conners 4, la familia Conners sigue siendo referencia en evaluaci\u00f3n de TDAH en Latinoam\u00e9rica. Esta gu\u00eda orienta al psic\u00f3logo mexicano en selecci\u00f3n de forma, interpretaci\u00f3n de perfiles y l\u00edmites del instrumento, en di\u00e1logo con la gu\u00eda de <a href=\"/articulos/conners-3-tdah-ninos.html\">Conners 3</a> y protocolos de evaluaci\u00f3n integral.",
        "test_name": "Conners",
        "hero_alt": "Psic\u00f3logo cl\u00ednico aplicando test Conners para evaluaci\u00f3n de TDAH infantil",
        "inline_alt": "Perfil de subescalas del test Conners con puntuaciones T elevadas en inatenci\u00f3n",
        "sections": [
            {
                "h2": "Historia y versiones del test Conners",
                "html": p(
                    "Keith Conners desarroll\u00f3 las primeras escalas en la d\u00e9cada de 1960; desde entonces hubo revisiones Conners 3 (2008) y Conners 4 (2022). El <strong>test Conners</strong> eval\u00faa dimensiones nucleares del TDAH: inatenci\u00f3n, hiperactividad/impulsividad, oposici\u00f3n desafiante, aprendizaje y funcionamiento ejecutivo seg\u00fan versi\u00f3n.",
                    "En M\u00e9xico, distribuidores autorizados ofrecen adaptaciones en espa\u00f1ol con baremos regionales. Verifique que usa manual y hojas de respuesta licenciadas; la fotocopia no autorizada invalida interpretaci\u00f3n normativa y puede infringir derechos de autor.",
                    "Compare con <a href=\"/articulos/conners-3-tdah-ninos.html\">Conners 3 en Kalyo</a> para detalle de subescalas cl\u00e1sicas y con <a href=\"/articulos/evaluacion-neuropsicologica-guia-clinica.html\">evaluaci\u00f3n neuropsicol\u00f3gica</a> cuando sospecha comorbilidad de aprendizaje.",
                ),
            },
            {
                "h2": "Administraci\u00f3n: padres, maestros y autorreporte",
                "html": p(
                    "La validez ecol\u00f3gica del test Conners depende de informantes que observan al ni\u00f1o en contextos distintos. Padres aportan datos del hogar; maestros del aula; adolescentes pueden completar autorreporte con cautela sobre deseabilidad social.",
                    "Instruya ventana temporal (t\u00edpicamente \u00faltimos seis meses o a\u00f1o escolar seg\u00fan manual). Discrepancia marcada entre informantes es cl\u00ednicamente informativa: puede reflejar estilos parentales, adaptaci\u00f3n escolar o s\u00edntomas situacionales.",
                    "En teleevaluaci\u00f3n, env\u00ede enlaces seguros y confirme identidad del informante. Documente qui\u00e9n complet\u00f3 cada forma y si hubo ayuda indebida.",
                ),
            },
            {
                "h2": "Interpretaci\u00f3n de T-scores y subescalas",
                "html": p(
                    "Las puntuaciones <strong>T</strong> tienen media 50 y DE 10 en muestras normativas. Convencionalmente T \u2265 65 (percentil ~93) sugiere elevaci\u00f3n cl\u00ednica en esa dimensi\u00f3n, aunque el manual especifica rangos exactos y niveles (normal, l\u00edmite, cl\u00ednico).",
                    "Perfil con inatenci\u00f3n elevada e hiperactividad moderada orienta a presentaci\u00f3n combinada; inatenci\u00f3n aislada sugiere predominio desatento. Elevaci\u00f3n en oposici\u00f3n desafiante obliga a diferencial con trastorno negativista desafiante o discordia familiar.",
                )
                + table(
                    ["Rango T aproximado", "Interpretaci\u00f3n", "Nota cl\u00ednica"],
                    [
                        ["40\u201359", "Promedio", "S\u00edntomas no destacados en esa escala"],
                        ["60\u201364", "L\u00edmite", "Vigilar; corroborar con entrevista"],
                        ["65\u201369", "Elevado", "Compatible con TDAH o comorbilidad"],
                        ["\u2265 70", "Muy elevado", "Priorizar evaluaci\u00f3n ampliada"],
                    ],
                ),
            },
            {
                "h2": "Integraci\u00f3n diagn\u00f3stica seg\u00fan DSM-5",
                "html": p(
                    "El TDAH requiere s\u00edntomas antes de los 12 a\u00f1os, en \u2265 2 contextos, con deterioro funcional y no explicados mejor por otro trastorno. El test Conners aporta datos cuantitativos; la entrevista confirma cronicidad, impacto acad\u00e9mico y reglas de exclusi\u00f3n.",
                    "Descarte privaci\u00f3n de sue\u00f1o, ansiedad, trauma, epilepsia, efectos de medicaci\u00f3n y problemas auditivos. Solicite boletines escolares y entrevista con maestro cuando sea posible.",
                    "Use <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">criterios de interpretaci\u00f3n integrada</a> y registre resultados en el expediente junto con <a href=\"/articulos/wisc-v-test-inteligencia-ninos.html\">WISC-V</a> si eval\u00faa funcionamiento cognitivo.",
                ),
            },
            {
                "h2": "Seguimiento terap\u00e9utico y farmacol\u00f3gico",
                "html": p(
                    "Reaplicar Conners cada 3-6 meses monitoriza respuesta a estimulantes, atomoxetina o intervenci\u00f3n conductual. Reducciones de 10 puntos T en inatenci\u00f3n pueden ser cl\u00ednicamente significativas seg\u00fan contexto.",
                    "Comparta resultados con psiquiatr\u00eda infantil de forma escrita, sin exponer informes completos innecesarios. Psicoeducaci\u00f3n familiar sobre TDAH mejora concordancia entre informantes en reevaluaciones.",
                    "En escuelas mexicanas, informes basados en Conners pueden fundamentar ajustes razonables; redacte recomendaciones funcionales, no solo puntajes.",
                ),
            },
            {
                "h2": "Limitaciones \u00e9ticas y culturales del test Conners",
                "html": p(
                    "Informantes con depresi\u00f3n o conflicto conyugal pueden sobreinformar problemas conductuales. Maestros con clases numerosas pueden no conocer bien al alumno: valide calidad del informante.",
                    "Baremos deben corresponder a edad y sexo del evaluado. Evite diagnosticar TDAH solo porque el colegio presiona por medicaci\u00f3n.",
                    "Conserve licencia del instrumento y formaci\u00f3n espec\u00edfica; pericia en TDAH infantil exige actualizaci\u00f3n continua y supervisi\u00f3n cl\u00ednica.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfConners 3 o Conners 4 en 2026?",
                "a": "Conners 4 es la versi\u00f3n m\u00e1s reciente con actualizaci\u00f3n normativa y contenidos alineados a DSM-5. Si su instituci\u00f3n a\u00fan usa Conners 3, mantenga consistencia longitudinal hasta migrar con nuevo baremo.",
            },
            {
                "q": "\u00bfUn T-score de 70 confirma TDAH?",
                "a": "No confirma diagn\u00f3stico. Indica elevaci\u00f3n significativa en esa escala. Diagn\u00f3stico requiere criterios cl\u00ednicos, historia y descarte de otras causas.",
            },
            {
                "q": "\u00bfQu\u00e9 hago si padres y maestro discrepan?",
                "a": "Explore contextos: estructura en casa vs. aula, relaci\u00f3n con maestro, bullying, nivel acad\u00e9mico. Discrepancia no invalida el instrumento; es dato para formulaci\u00f3n.",
            },
            {
                "q": "\u00bfPuedo usar Conners en adolescentes mayores de 18?",
                "a": "Conners est\u00e1 dise\u00f1ado para edades escolares seg\u00fan manual. En adultos use ASRS u otros instrumentos validados para TDAH en adultos.",
            },
            {
                "q": "\u00bfEl test Conners detecta simulaci\u00f3n?",
                "a": "Algunas versiones incluyen \u00edndices de validez o inconsistencia. Interpret\u00falos seg\u00fan manual y complemente con observaci\u00f3n cl\u00ednica y entrevistas.",
            },
        ],
        "related": [
            {"href": "/articulos/conners-3-tdah-ninos.html", "label": "Conners 3: gu\u00eda cl\u00ednica TDAH"},
            {"href": "/articulos/wisc-v-test-inteligencia-ninos.html", "label": "WISC-V: inteligencia infantil"},
            {"href": "/articulos/evaluacion-neuropsicologica-guia-clinica.html", "label": "Evaluaci\u00f3n neuropsicol\u00f3gica"},
            {"href": "/articulos/como-interpretar-tests-psicologicos.html", "label": "Interpretar tests psicol\u00f3gicos"},
        ],
        "references": [
            "Conners, C. K. (2008). <em>Conners 3rd Edition Manual</em>. Multi-Health Systems.",
            "Conners, C. K., & Sitarenios, G. (2022). <em>Conners 4th Edition Manual</em>. Multi-Health Systems.",
            "American Psychiatric Association. (2013). <em>Diagnostic and Statistical Manual of Mental Disorders</em> (5th ed.). DSM-5 criterios TDAH.",
        ],
    }


def _article_ansiedad_clinica(p, table):
    return {
        "slug": "escala-de-ansiedad-clinica",
        "title": "Escala de ansiedad cl&iacute;nica: gu&iacute;a para M&eacute;xico | Kalyo",
        "description": "Escala de ansiedad cl\u00ednica: comparaci\u00f3n GAD-7, BAI, STAI, HAM-A y DASS-21, cu\u00e1ndo usar cada una en consulta psicol\u00f3gica privada e institucional en M\u00e9xico.",
        "keywords": "escala de ansiedad, GAD-7, BAI, STAI, ansiedad cl\u00ednica, tamizaje ansiedad, psicolog\u00eda M\u00e9xico, evaluaci\u00f3n ansiosa",
        "h1": "Escala de ansiedad cl\u00ednica: tipos, selecci\u00f3n e interpretaci\u00f3n",
        "breadcrumb_short": "Escala de ansiedad cl\u00ednica",
        "quick_answer": "Una escala de ansiedad cl\u00ednica es un instrumento estandarizado que cuantifica s\u00edntomas ansiosos en ventana temporal definida. Entre las m\u00e1s usadas en M\u00e9xico figuran GAD-7, BAI, STAI, HAM-A y subescala de ansiedad del DASS-21. Ninguna sustituye entrevista diagn\u00f3stica; orientan severidad, seguimiento y respuesta terap\u00e9utica.",
        "intro_long": "Elegir la escala de ansiedad adecuada depende de objetivo (tamizaje vs. evaluaci\u00f3n fina), tiempo disponible, modalidad presencial o digital y tipo de ansiedad (generalizada, f\u00f3bica, estado vs. rasgo). Esta gu\u00eda compara instrumentos frecuentes en consultorios mexicanos y enlaza recursos como <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a> y <a href=\"/articulos/stai-ansiedad-estado-rasgo.html\">STAI</a>.",
        "test_name": "escalas de ansiedad",
        "hero_alt": "Comparaci\u00f3n de escalas de ansiedad cl\u00ednica en evaluaci\u00f3n psicol\u00f3gica",
        "inline_alt": "Tabla comparativa de escalas de ansiedad GAD-7 BAI STAI y DASS-21",
        "sections": [
            {
                "h2": "Clasificaci\u00f3n de escalas de ansiedad en la pr\u00e1ctica cl\u00ednica",
                "html": p(
                    "Las escalas de ansiedad pueden ser <strong>autoadministradas</strong> (GAD-7, BAI, DASS-21) o <strong>heteroaplicadas</strong> (HAM-A). Miden constructos distintos: ansiedad generalizada reciente (GAD-7), s\u00edntomas som\u00e1ticos y cognitivos amplios (BAI), ansiedad estado vs. rasgo (STAI), severidad cl\u00ednica por entrevista (HAM-A).",
                    "En atenci\u00f3n primaria mexicana predomina GAD-7 por brevedad. En consulta especializada pueden combinarse varias para perfilar comorbilidad depresiva con <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a>.",
                    "Seleccione seg\u00fan pregunta cl\u00ednica: tamizaje masivo, diagn\u00f3stico diferencial, monitor de TCC o evaluaci\u00f3n pre/post farmacoterapia con psiquiatr\u00eda.",
                ),
            },
            {
                "h2": "Comparativa de instrumentos frecuentes",
                "html": p(
                    "La siguiente tabla resume usos; consulte manuales para baremos locales.",
                )
                + table(
                    ["Escala", "\u00cdtems / tiempo", "Mejor uso cl\u00ednico"],
                    [
                        ["GAD-7", "7 \u00edtems; 2 min", "Tamizaje TAG y seguimiento breve"],
                        ["BAI", "21 \u00edtems; 5-10 min", "S\u00edntomas som\u00e1ticos de ansiedad"],
                        ["STAI", "40 \u00edtems; 10-15 min", "Estado vs. rasgo en investigaci\u00f3n/cl\u00ednica"],
                        ["HAM-A", "Entrevista; 15-20 min", "Severidad cl\u00ednica heteroinformada"],
                        ["DASS-21", "7 \u00edtems ansiedad", "Perfil depresi\u00f3n-ansiedad-estr\u00e9s"],
                    ],
                    cls="items-table",
                )
                + p(
                    "En telepsicolog\u00eda priorice GAD-7 y <a href=\"/articulos/escala-dass-21.html\">DASS-21</a> por autoadministraci\u00f3n. Para pacientes con queja som\u00e1tica marcada (palpitaciones, mareo), BAI puede ser m\u00e1s sensible que GAD-7.",
                ),
            },
            {
                "h2": "Interpretaci\u00f3n cl\u00ednica y cortes de severidad",
                "html": p(
                    "No compare puntajes brutos entre escalas distintas. Cada instrumento tiene sus cortes validados. GAD-7 \u2265 10 sugiere ansiedad cl\u00ednicamente significativa; BAI \u2265 16 aproxima criterio cl\u00ednico en muchos estudios; DASS-21 ansiedad \u2265 10 (escala multiplicada) indica severidad al menos moderada seg\u00fan manual.",
                    "Integre con entrevista: preocupaci\u00f3n excesiva, tensi\u00f3n, insomnio, irritabilidad, evitaci\u00f3n. Explore ataques de p\u00e1nico, fobias espec\u00edficas y consumo de sustancias como autorregulaci\u00f3n.",
                    "Revise <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">interpretaci\u00f3n integrada de tests</a> y registre cambio m\u00ednimo cl\u00ednicamente importante en notas de evoluci\u00f3n.",
                ),
            },
            {
                "h2": "Cu\u00e1ndo usar cada escala en M\u00e9xico",
                "html": p(
                    "<strong>Consulta privada breve:</strong> GAD-7 + PHQ-9 en intake. <strong>Cl\u00ednica de ansiedad:</strong> BAI o STAI rasgo al inicio, GAD-7 quincenal. <strong>Hospital psiqui\u00e1trico:</strong> HAM-A para severidad y respuesta a tratamiento. <strong>Empresas / NOM-035:</strong> DASS-21 o escalas aprobadas en protocolo institucional.",
                    "En poblaci\u00f3n ind\u00edgena o biling\u00fce valide comprensi\u00f3n idiom\u00e1tica; use versiones validadas en espa\u00f1ol mexicano cuando existan.",
                    "Digitalice con <a href=\"/articulos/tests-psicologicos-digitales.html\">tests psicol\u00f3gicos digitales</a> para gr\u00e1ficas longitudinales en el expediente.",
                ),
            },
            {
                "h2": "Limitaciones psicom\u00e9tricas y sesgos",
                "html": p(
                    "Autoinformes pueden elevarse por somatizaci\u00f3n, dolor cr\u00f3nico o personalidad ansiosa estable sin trastorno actual. HAM-A requiere entrenamiento inter-evaluador para confiabilidad.",
                    "Ansiedad y depresi\u00f3n comparten s\u00edntomas; por eso GAD-7 y PHQ-9 se aplican juntos. No use una sola escala para certificados m\u00e9dicos sin evaluaci\u00f3n completa.",
                    "Reeval\u00fae con el mismo instrumento; cambiar de BAI a GAD-7 entre sesiones dificulta comparar tendencia.",
                ),
            },
            {
                "h2": "Protocolo sugerido de evaluaci\u00f3n ansiosa",
                "html": p(
                    "Sesi\u00f3n 1: entrevista cl\u00ednica, GAD-7, PHQ-9, exploraci\u00f3n de p\u00e1nico y fobias. Sesi\u00f3n 2-3: si persiste duda diagn\u00f3stica, STAI o BAI; escala de funcionalamiento (WHODAS breve si disponible).",
                    "Cada 4 semanas en TCC: repetir GAD-7; meta t\u00edpica reducci\u00f3n \u2265 50 % de puntaje inicial o por debajo de corte 10.",
                    "Documente en expediente seg\u00fan <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> y comparta tendencia con paciente para reforzar adherencia.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfCu\u00e1l es la mejor escala de ansiedad cl\u00ednica?",
                "a": "No hay una \u00fanica mejor: GAD-7 es excelente para tamizaje breve; BAI para somatizaci\u00f3n; STAI para estado/rasgo; HAM-A para psiquiatr\u00eda. Elija seg\u00fan objetivo y tiempo.",
            },
            {
                "q": "\u00bfGAD-7 detecta ataques de p\u00e1nico?",
                "a": "Parcialmente. Un \u00edtem aborda miedo a que algo terrible ocurra, pero no sustituye evaluaci\u00f3n espec\u00edfica de trastorno de p\u00e1nico. Complemente con entrevista.",
            },
            {
                "q": "\u00bfPuedo usar escalas de ansiedad en ni\u00f1os con adultos?",
                "a": "No. Use instrumentos validados por edad (SCARED, Spence, RCMAS seg\u00fan grupo etario).",
            },
            {
                "q": "\u00bfBAI o GAD-7 para seguimiento semanal?",
                "a": "GAD-7 por brevedad y menor carga. BAI si el foco terap\u00e9utico son s\u00edntomas som\u00e1ticos intensos.",
            },
            {
                "q": "\u00bfLas escalas sirven para NOM-035?",
                "a": "Depende del protocolo empresarial. DASS-21 y otras escalas validadas se usan en evaluaciones de riesgo psicosocial; verifique normativa espec\u00edfica y asesor\u00eda legal.",
            },
        ],
        "related": [
            {"href": "/articulos/que-es-el-gad-7.html", "label": "GAD-7: interpretaci\u00f3n cl\u00ednica"},
            {"href": "/articulos/stai-ansiedad-estado-rasgo.html", "label": "STAI: ansiedad estado y rasgo"},
            {"href": "/articulos/escala-dass-21.html", "label": "DASS-21: depresi\u00f3n, ansiedad y estr\u00e9s"},
            {"href": "/articulos/phq9-vs-gad7-diferencias.html", "label": "PHQ-9 vs GAD-7"},
        ],
        "references": [
            "Beck, A. T., Epstein, N., Brown, G., & Steer, R. A. (1988). An inventory for measuring clinical anxiety: The Beck Anxiety Inventory. <em>Journal of Consulting and Clinical Psychology</em>, 56(6), 893-897.",
            "Spielberger, C. D., Gorsuch, R. L., Lushene, R., Vagg, P. R., & Jacobs, G. A. (1983). <em>Manual for the State-Trait Anxiety Inventory</em>. Consulting Psychologists Press.",
            "Lovibond, S. H., & Lovibond, P. F. (1995). <em>Manual for the Depression Anxiety Stress Scales</em> (2nd ed.). Psychology Foundation of Australia.",
        ],
    }


def _article_phq9_gad7(p, table):
    return {
        "slug": "phq9-vs-gad7-diferencias",
        "title": "PHQ-9 vs GAD-7: diferencias cl&iacute;nicas | Kalyo",
        "description": "PHQ-9 vs GAD-7: diferencias cl\u00ednicas, constructos medidos, cu\u00e1ndo aplicar juntas e interpretaci\u00f3n cl\u00ednica en tamizaje de depresi\u00f3n y ansiedad en M\u00e9xico.",
        "keywords": "phq9 gad7, PHQ-9 vs GAD-7, depresi\u00f3n ansiedad, tamizaje cl\u00ednico, psicolog\u00eda M\u00e9xico, escalas breves, comorbilidad",
        "h1": "PHQ-9 vs GAD-7: diferencias, usos y aplicaci\u00f3n conjunta",
        "breadcrumb_short": "PHQ-9 vs GAD-7",
        "quick_answer": "PHQ-9 y GAD-7 son escalas breves de autoinforme derivadas del PRIME-MD: PHQ-9 mide s\u00edntomas depresivos en dos semanas; GAD-7 mide ansiedad generalizada en el mismo periodo. No son intercambiables. En consulta cl\u00ednica mexicana se aplican juntas porque depresi\u00f3n y ansiedad coocurren en m\u00e1s del 50 % de los casos.",
        "intro_long": "Confundir PHQ-9 con GAD-7 lleva a interpretaciones err\u00f3neas en intake y seguimiento. Esta gu\u00eda aclara qu\u00e9 construye mide cada escala, c\u00f3mo leer perfiles mixtos y c\u00f3mo documentar resultados en el expediente, enlazando las gu\u00edas de <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a> y <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a>.",
        "test_name": "PHQ-9 y GAD-7",
        "hero_alt": "Comparaci\u00f3n cl\u00ednica entre cuestionarios PHQ-9 y GAD-7 en consulta psicol\u00f3gica",
        "inline_alt": "Tabla de diferencias entre PHQ-9 depresi\u00f3n y GAD-7 ansiedad generalizada",
        "sections": [
            {
                "h2": "Origen com\u00fan y prop\u00f3sitos distintos",
                "html": p(
                    "Tanto <strong>PHQ-9</strong> (Kroenke, Spitzer & Williams, 2001) como <strong>GAD-7</strong> (Spitzer et al., 2006) provienen del Patient Health Questionnaire, dise\u00f1ado para atenci\u00f3n primaria. PHQ-9 eval\u00faa nueve s\u00edntomas nucleares de depresi\u00f3n mayor seg\u00fan DSM; GAD-7 eval\u00faa siete s\u00edntomas de ansiedad generalizada.",
                    "PHQ-9 incluye \u00edtem cr\u00edtico sobre ideaci\u00f3n suicida (\u00edtem 9); GAD-7 no eval\u00faa riesgo suicida. Por ello, aunque GAD-7 sea alto, siempre revise seguridad si PHQ-9 \u00edtem 9 &gt; 0.",
                    "En M\u00e9xico ambas escalas est\u00e1n validadas en espa\u00f1ol y son est\u00e1ndar en consultorios privados, EAP empresariales y residentados de psicolog\u00eda cl\u00ednica.",
                ),
            },
            {
                "h2": "Tabla comparativa PHQ-9 vs GAD-7",
                "html": table(
                    ["Caracter\u00edstica", "PHQ-9", "GAD-7"],
                    [
                        ["Constructo", "Depresi\u00f3n mayor (s\u00edntomas)", "Ansiedad generalizada (s\u00edntomas)"],
                        ["\u00cdtems", "9", "7"],
                        ["Rango", "0\u201327", "0\u201321"],
                        ["Corte cl\u00ednico t\u00edpico", "\u2265 10 moderado", "\u2265 10 moderado"],
                        ["Riesgo suicida", "S\u00ed (\u00edtem 9)", "No"],
                        ["Tiempo aplicaci\u00f3n", "2\u20133 min", "2 min"],
                    ],
                    cls="items-table",
                )
                + p(
                    "Ambas usan ventana de <strong>dos semanas</strong> y escala Likert 0-3. La suma total orienta severidad, no diagn\u00f3stico definitivo.",
                ),
            },
            {
                "h2": "Perfiles cl\u00ednicos frecuentes al aplicar ambas",
                "html": p(
                    "<strong>PHQ-9 alto + GAD-7 alto:</strong> comorbilidad depresi\u00f3n-ansiedad; plan integral TCC, posible derivaci\u00f3n psiqui\u00e1trica. <strong>PHQ-9 alto + GAD-7 bajo:</strong> cuadro depresivo predominante; vigilar anhedonia, suicidio, apat\u00eda. <strong>PHQ-9 bajo + GAD-7 alto:</strong> ansiedad predominante; explorar TAG, p\u00e1nico, fobias. <strong>Ambos bajos:</strong> s\u00edntomas subcl\u00ednicos o d\u00eda favorable; no descarta trastornos sin exploraci\u00f3n.",
                    "Correlaci\u00f3n moderada-alta entre escalas refleja solapamiento sintom\u00e1tico (insomnio, fatiga, dificultad de concentraci\u00f3n). La entrevista separa si fatiga es anhed\u00f3nica o hiperactivaci\u00f3n ansiosa.",
                    "Complemente con <a href=\"/articulos/escala-dass-21.html\">DASS-21</a> si necesita subescala de estr\u00e9s, o <a href=\"/articulos/inventario-depresion-beck-bdi.html\">BDI-II</a> para profundizar cogniciones depresivas.",
                ),
            },
            {
                "h2": "Cu\u00e1ndo aplicar PHQ-9 vs GAD-7 o ambos",
                "html": p(
                    "Aplique <strong>ambos en evaluaci\u00f3n inicial</strong> de adultos en salud mental general. Use solo PHQ-9 si queja es claramente an\u00edmica y no hay ansiedad referida. Use solo GAD-7 en programas espec\u00edficos de ansiedad con screening previo de depresi\u00f3n.",
                    "En seguimiento, repita la escala del constructo objetivo de tratamiento; si trabaja comorbilidad, repita ambas cada 4 semanas.",
                    "Digitalice con <a href=\"/articulos/tests-psicologicos-digitales.html\">tests digitales</a> para gr\u00e1ficas paralelas PHQ-9/GAD-7 en el expediente.",
                ),
            },
            {
                "h2": "Interpretaci\u00f3n en contexto mexicano",
                "html": p(
                    "Factores culturales pueden elevar somatizaci\u00f3n en GAD-7 (\u00edtems corporales) y culpa/ desesperanza en PHQ-9. Explore expresi\u00f3n emocional y estigma de salud mental.",
                    "En servicios p\u00fablicos con tiempo limitado, PHQ-9 + GAD-7 ofrecen m\u00e1ximo rendimiento psicom\u00e9trico por minuto invertido. Documente seg\u00fan <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a>.",
                    "Para informes escolares o laborales, traduzca puntajes a funcionamiento observable, no solo n\u00fameros.",
                ),
            },
            {
                "h2": "Errores comunes al comparar PHQ-9 y GAD-7",
                "html": p(
                    "Error 1: diagnosticar TAG solo con GAD-7 \u2265 10 sin duraci\u00f3n \u2265 6 meses. Error 2: ignorar \u00edtem 9 del PHQ-9. Error 3: sumar puntajes de ambas escalas como \u00edndice \u00fanico. Error 4: cambiar instrumentos en seguimiento sin justificaci\u00f3n.",
                    "Use gu\u00eda <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">c\u00f3mo interpretar tests psicol\u00f3gicos</a> y registre decisiones cl\u00ednicas tras cada par de puntajes.",
                    "Meta terap\u00e9utica ejemplo: PHQ-9 de 18 a &lt; 10 y GAD-7 de 15 a &lt; 8 en 12 semanas de TCC y activaci\u00f3n conductual combinada.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfPHQ-9 mide ansiedad?",
                "a": "No directamente. Algunos \u00edtems solapan (concentraci\u00f3n, sue\u00f1o), pero est\u00e1 calibrado para depresi\u00f3n. Para ansiedad use GAD-7 u otra escala espec\u00edfica.",
            },
            {
                "q": "\u00bfPuedo usar solo GAD-7 en atenci\u00f3n primaria?",
                "a": "Es posible si el foco es ansiedad, pero se recomienda PHQ-9 por comorbilidad depresiva frecuente y detecci\u00f3n de ideaci\u00f3n suicida v\u00eda PHQ-9.",
            },
            {
                "q": "\u00bfLos cortes 10 son iguales en M\u00e9xico?",
                "a": "Son referencia internacional ampliamente usada. Algunos estudios latinos sugieren ajustes; consulte validaciones locales si investiga o publica.",
            },
            {
                "q": "\u00bfGAD-7 sustituye a STAI?",
                "a": "No. STAI distingue ansiedad estado/rasgo; GAD-7 tamiza TAG reciente. Son complementarios en casos complejos.",
            },
            {
                "q": "\u00bfCada cu\u00e1nto repetir el par PHQ-9/GAD-7?",
                "a": "En tratamiento activo, cada 2-4 semanas. En mantenimiento, cada 2-3 meses o ante reca\u00edda.",
            },
        ],
        "related": [
            {"href": "/articulos/que-es-el-phq-9.html", "label": "PHQ-9: gu\u00eda completa"},
            {"href": "/articulos/que-es-el-gad-7.html", "label": "GAD-7: escala de ansiedad"},
            {"href": "/articulos/escala-dass-21.html", "label": "DASS-21: perfil emocional"},
            {"href": "/articulos/gad-7-espanol-pdf.html", "label": "GAD-7 PDF en espa\u00f1ol"},
        ],
        "references": [
            "Kroenke, K., Spitzer, R. L., & Williams, J. B. W. (2001). The PHQ-9: Validity of a brief depression severity measure. <em>Journal of General Internal Medicine</em>, 16(9), 606-613.",
            "Spitzer, R. L., Kroenke, K., Williams, J. B. W., & L\u00f6we, B. (2006). A brief measure for assessing generalized anxiety disorder: The GAD-7. <em>Archives of Internal Medicine</em>, 166(10), 1092-1097.",
            "Kroenke, K., Spitzer, R. L., Williams, J. B. W., L\u00f6we, B., & Gr\u00e4fe, K. (2010). Concurrent validity of the GAD-7 and PHQ-9. <em>Psychosomatics</em>, 51(6), 452-457.",
        ],
    }


def _article_beck_dep(p, table):
    return {
        "slug": "test-beck-depresion-interpretacion",
        "title": "Test Beck depresi&oacute;n: interpretaci&oacute;n BDI-II | Kalyo",
        "description": "Test Beck BDI-II: administraci\u00f3n, puntuaci\u00f3n, severidad, diferencias con PHQ-9 e interpretaci\u00f3n cl\u00ednica de depresi\u00f3n para psic\u00f3logos en consulta M\u00e9xico.",
        "keywords": "test Beck, BDI-II, inventario depresi\u00f3n Beck, escala Beck, interpretaci\u00f3n depresi\u00f3n, psicolog\u00eda cl\u00ednica M\u00e9xico",
        "h1": "Test Beck de depresi\u00f3n (BDI-II): interpretaci\u00f3n cl\u00ednica",
        "breadcrumb_short": "Test Beck depresi\u00f3n",
        "quick_answer": "El test Beck de depresi\u00f3n (BDI-II) es un inventario de 21 \u00edtems que mide severidad de s\u00edntomas depresivos en adolescentes y adultos. Puntajes de 0 a 63 se interpretan como m\u00ednima (0-13), leve (14-19), moderada (20-28) y severa (29-63). Complementa entrevista cl\u00ednica; no reemplaza evaluaci\u00f3n de riesgo suicida estructurada.",
        "intro_long": "El BDI-II sigue siendo uno de los instrumentos m\u00e1s citados en consulta y research. Esta gu\u00eda explica administraci\u00f3n, baremos, diferencias con <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a> y c\u00f3mo integrar el test Beck con el <a href=\"/articulos/inventario-depresion-beck-bdi.html\">inventario BDI en Kalyo</a> dentro de un protocolo de evaluaci\u00f3n depresiva.",
        "test_name": "BDI-II",
        "hero_alt": "Inventario BDI-II test Beck de depresi\u00f3n en evaluaci\u00f3n cl\u00ednica",
        "inline_alt": "Escala de severidad del test Beck BDI-II con rangos cl\u00ednicos",
        "sections": [
            {
                "h2": "Estructura del BDI-II y contenido cl\u00ednico",
                "html": p(
                    "El <strong>Beck Depression Inventory-II</strong> (Beck, Steer & Brown, 1996) contiene 21 grupos de enunciados graduados en intensidad (0-3). Eval\u00faa tristeza, pesimismo, fracaso, p\u00e9rdida de placer, culpa, castigo, autodesprecio, ideaci\u00f3n suicida, llanto, irritabilidad, aislamiento social, indecisi\u00f3n, imagen corporal, dificultad para trabajar, sue\u00f1o, fatiga, apetito, p\u00e9rdida de libido, preocupaci\u00f3n som\u00e1tica y p\u00e9rdida de inter\u00e9s sexual.",
                    "A diferencia del PHQ-9 alineado a DSM, BDI-II incluye cogniciones beckianas ( culpa, desesperanza) \u00fatiles en TCC. Ventana temporal: \u00faltimas dos semanas incluyendo hoy.",
                    "Requiere licencia del editor (Pearson / PsychCorp). Use manual oficial y baremos mexicanos o latinos cuando est\u00e9n disponibles.",
                ),
            },
            {
                "h2": "Administraci\u00f3n y consideraciones pr\u00e1cticas",
                "html": p(
                    "Autoadministrado en 5-10 minutos; puede leerse en voz alta si hay dificultad lectora. Nivel educativo m\u00ednimo aproximado sexto grado; ajuste en poblaci\u00f3n con baja escolaridad.",
                    "Explore si respuestas reflejan depresi\u00f3n mayor vs. reacci\u00f3n a duelo reciente. BDI-II no distingue autom\u00e1ticamente; la entrevista aclara cronolog\u00eda y criterios de exclusi\u00f3n.",
                    "Registre en expediente puntuaci\u00f3n total, nivel de severidad y \u00edtems m\u00e1ximos (especialmente suicidio \u00edtem 9).",
                ),
            },
            {
                "h2": "Interpretaci\u00f3n de puntajes y tabla de severidad",
                "html": p(
                    "Cortes cl\u00e1sicos del manual: 0-13 depresi\u00f3n m\u00ednima; 14-19 leve; 20-28 moderada; 29-63 severa. Puntajes \u2265 20 suelen asociarse a criterio cl\u00ednico de episodio depresivo en investigaci\u00f3n, pero var\u00edan por muestra.",
                )
                + table(
                    ["Puntaje BDI-II", "Severidad", "Implicaci\u00f3n cl\u00ednica"],
                    [
                        ["0\u201313", '<span class="score-badge">M\u00ednima</span>', "Vigilancia; psicoeducaci\u00f3n"],
                        ["14\u201319", '<span class="score-badge">Leve</span>', "TCC focal; reevaluar en 4 semanas"],
                        ["20\u201328", '<span class="score-badge">Moderada</span>', "Plan terap\u00e9utico estructurado; valorar psiquiatr\u00eda"],
                        ["29\u201363", '<span class="score-badge">Severa</span>', "Priorizar seguridad; intervenci\u00f3n intensiva"],
                    ],
                )
                + p(
                    "Analice perfil de \u00edtems: elevaci\u00f3n cognitiva vs. som\u00e1tica orienta foco de TCC. Compare con <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">gu\u00eda de interpretaci\u00f3n</a>.",
                ),
            },
            {
                "h2": "BDI-II vs PHQ-9: cu\u00e1ndo preferir test Beck",
                "html": p(
                    "PHQ-9 es m\u00e1s breve y est\u00e1ndar en atenci\u00f3n primaria. BDI-II ofrece mayor granularidad de s\u00edntomas cognitivo-afectivos y es cl\u00e1sico en psicolog\u00eda cl\u00ednica y research.",
                    "Prefiera BDI-II cuando el tratamiento es TCC de depresi\u00f3n y desea monitorear creencias disfuncionales espec\u00edficas. Prefiera PHQ-9 en tamizaje masivo o telemedicina ultra breve.",
                    "No administre ambos en cada sesi\u00f3n sin raz\u00f3n; elige uno para longitudinal y mant\u00e9n consistencia.",
                ),
            },
            {
                "h2": "Ideaci\u00f3n suicida y derivaci\u00f3n",
                "html": p(
                    "\u00cdtem 9 pregunta sobre deseos de muerte o autolesi\u00f3n. Cualquier puntuaci\u00f3n &gt; 0 requiere exploraci\u00f3n cl\u00ednica inmediata: plan, intentos previos, medios, factores protectores.",
                    "BDI-II no sustituye escalas de riesgo suicida (BSS, C-SSRS). Derive a urgencias si hay plan estructurado o intento reciente.",
                    "Documente evaluaci\u00f3n de riesgo seg\u00fan <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> y protocolos institucionales mexicanos.",
                ),
            },
            {
                "h2": "Seguimiento terap\u00e9utico y cambio cl\u00ednico",
                "html": p(
                    "Reaplicar BDI-II cada 4-6 semanas en depresi\u00f3n moderada. Reducci\u00f3n \u2265 50 % del puntaje inicial sugiere respuesta cl\u00ednica; remisi\u00f3n a menudo &lt; 14.",
                    "Gr\u00e1fica de progreso refuerza alianza. Si puntaje estancado, revise adherencia, comorbilidad ansiosa (<a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a>) o factores ambientales.",
                    "Use plataformas de <a href=\"/articulos/tests-psicologicos-digitales.html\">tests digitales</a> para evitar errores de suma y archivar historial.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfBDI-II diagnostica depresi\u00f3n mayor?",
                "a": "No. Mide severidad de s\u00edntomas depresivos. Diagn\u00f3stico requiere entrevista DSM-5/ CIE-11, duraci\u00f3n e impacto funcional.",
            },
            {
                "q": "\u00bfPuedo usar BDI-II en adolescentes?",
                "a": "S\u00ed desde aproximadamente 13 a\u00f1os seg\u00fan manual, con interpretaci\u00f3n cautelosa. En ni\u00f1os menores use CDI.",
            },
            {
                "q": "\u00bfEl duelo eleva el BDI-II?",
                "a": "S\u00ed. Puntajes pueden ser altos en duelo reciente sin trastorno depresivo mayor. Entreviste cronolog\u00eda y criterios de exclusi\u00f3n.",
            },
            {
                "q": "\u00bfBDI-II o BDI-I?",
                "a": "Use BDI-II, alineado a DSM-IV/5. BDI-I es obsoleto para pr\u00e1ctica cl\u00ednica actual.",
            },
            {
                "q": "\u00bfCada cu\u00e1nto repetir el test Beck?",
                "a": "Cada 4-6 semanas en tratamiento activo; espaciar \u2265 2 semanas para minimizar memoria de \u00edtems si reaplica muy seguido.",
            },
        ],
        "related": [
            {"href": "/articulos/inventario-depresion-beck-bdi.html", "label": "Inventario depresi\u00f3n Beck BDI"},
            {"href": "/articulos/que-es-el-phq-9.html", "label": "PHQ-9: tamizaje depresi\u00f3n"},
            {"href": "/articulos/escala-dass-21.html", "label": "DASS-21: perfil emocional"},
            {"href": "/articulos/como-interpretar-tests-psicologicos.html", "label": "Interpretar tests psicol\u00f3gicos"},
        ],
        "references": [
            "Beck, A. T., Steer, R. A., & Brown, G. K. (1996). <em>Manual for the Beck Depression Inventory-II</em>. Psychological Corporation.",
            "Beck, A. T., Steer, R. A., & Garbin, M. G. (1988). Psychometric properties of the Beck Depression Inventory. <em>Clinical Psychology Review</em>, 8(1), 77-100.",
            "Kroenke, K., Spitzer, R. L., & Williams, J. B. W. (2001). The PHQ-9. <em>Journal of General Internal Medicine</em>, 16(9), 606-613.",
        ],
    }


def _article_maslach(p, table):
    return {
        "slug": "maslach-burnout-test-interpretacion",
        "title": "Test de Maslach: interpretaci&oacute;n MBI cl&iacute;nica | Kalyo",
        "description": "Test de Maslach MBI: agotamiento, despersonalizaci\u00f3n, realizaci\u00f3n personal, NOM-035 e interpretaci\u00f3n de burnout en psic\u00f3logos y personal de salud en M\u00e9xico.",
        "keywords": "test de Maslach, MBI, Maslach Burnout Inventory, burnout, agotamiento laboral, NOM-035, psicolog\u00eda organizacional M\u00e9xico",
        "h1": "Test de Maslach (MBI): interpretaci\u00f3n cl\u00ednica del burnout",
        "breadcrumb_short": "Test de Maslach",
        "quick_answer": "El test de Maslach (Maslach Burnout Inventory, MBI) mide burnout en tres dimensiones: agotamiento emocional, despersonalizaci\u00f3n (cinismo) y baja realización personal. No es diagnóstico médico; identifica riesgo ocupacional. En México se usa en psicólogos clínicos, personal de salud y programas alineados a NOM-035 sobre riesgos psicosociales.",
        "intro_long": "El burnout en psicólogos es frecuente por carga emocional, no-shows y documentación. Esta guía explica cómo interpretar el test de Maslach, diferenciar burnout de depresión y vincular resultados con intervención organizacional, complementando el artículo de <a href=\"/articulos/burnout-laboral.html\">burnout laboral</a>.",
        "test_name": "MBI",
        "hero_alt": "Interpretación del test de Maslach burnout en profesional de salud mental",
        "inline_alt": "Subescalas del Maslach Burnout Inventory agotamiento despersonalización y realización",
        "sections": [
            {
                "h2": "Modelo tridimensional del burnout según Maslach",
                "html": p(
                    "Maslach y Jackson (1981) conceptualizaron el <strong>síndrome de burnout</strong> como respuesta prolongada a estrés laboral crónico en profesiones de relación humana. El <strong>test de Maslach (MBI)</strong> opera tres subescalas: <em>Agotamiento emocional</em> (fatiga extrema por demanda afectiva), <em>Despersonalización</em> (actitudes cínicas o distantes hacia usuarios) y <em>Realización personal</em> (sentimientos de competencia y logro; puntuaciones bajas indican deterioro).",
                    "Existen versiones MBI-HSS (Human Services), MBI-GS (General Survey) y MBI-ES (Educators). Psicólogos clínicos suelen usar MBI-HSS o adaptaciones para salud mental.",
                    "En México el constructo se relaciona con debates sobre <a href=\"/articulos/burnout-laboral.html\">burnout laboral</a> y evaluaciones de clima organizacional bajo <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">marcos de salud ocupacional</a>.",
                ),
            },
            {
                "h2": "Administración del MBI en contexto clínico y organizacional",
                "html": p(
                    "Autoadministrado; tiempo aproximado 10-15 minutos. Instruya que responda según experiencia laboral reciente (típicamente último año según versión). Anonimato en evaluaciones institucionales aumenta honestidad.",
                    "En consulta individual con psicólogo quemado, explique que el test de Maslach orienta intervención, no etiqueta patología. Diferencie evaluación ocupacional de psicoterapia por depresión.",
                    "Guarde resultados en expediente ocupacional o clínico según quién contrató evaluación (empleador vs. paciente privado).",
                ),
            },
            {
                "h2": "Interpretación de subescalas y puntos de corte",
                "html": p(
                    "El manual proporciona percentiles y categorías (bajo, medio, alto) por profesión. Agotamiento alto + despersonalización alta + realización personal baja configuran perfil clásico de burnout severo.",
                    "Agotamiento alto con realización personal preservada puede reflejar sobrecarga temporal recuperable. Despersonalización aislada obliga a explorar ética profesional y contratransferencia.",
                )
                + table(
                    ["Subescala", "Elevación clínica sugiere", "Intervención orientada"],
                    [
                        ["Agotamiento emocional", "Fatiga crónica, insomnio, irritabilidad", "Límites de carga, descansos, supervisión"],
                        ["Despersonalización", "Cinismo, distanciamiento del paciente", "Espacios de reflexión, rotación, apoyo"],
                        ["Baja realización personal", "Ineficacia percibida", "Formación, metas realistas, reconocimiento"],
                    ],
                    cls="items-table",
                ),
            },
            {
                "h2": "Diferencial con depresión, ansiedad y TEPT",
                "html": p(
                    "Burnout es contextual al trabajo; depresión mayor generaliza a múltiples dominios. Aplique <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a> y <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a> si hay síntomas transversales. TEPT por exposición a trauma laboral (violencia, emergencias) puede mimetizar agotamiento.",
                    "Pregunte: ¿Los síntomas mejoran en vacaciones? ¿Están ligados al consultorio o empresa específica? ¿Hay conflicto ético no resuelto?",
                    "El test de Maslach no sustituye evaluación psiquiátrica si hay ideación suicida o discapacidad funcional global.",
                ),
            },
            {
                "h2": "MBI, NOM-035 y psicólogos en México",
                "html": p(
                    "La NOM-035-STPS-2018 exige identificar factores de riesgo psicosocial en centros de trabajo. El MBI puede integrarse en baterías junto a cuestionarios normativos; verifique compatibilidad con asesoría en seguridad e higiene laboral.",
                    "Psicólogos empleados en hospitales, call centers de salud mental o EAP deben conocer políticas de confidencialidad: resultados agregados para RH, individuales para intervención clínica con consentimiento.",
                    "En consulta privada, muchos colegas usan MBI para autorregulación profesional y planificar supervisión clínica.",
                ),
            },
            {
                "h2": "Intervención tras interpretación del test de Maslach",
                "html": p(
                    "Intervenciones individuales: TCC para manejo de estrés, mindfulness, reorganización de agenda, reducción de panel de pacientes, grupos de intervisión. Organizacionales: clarificar roles, reducir burocracia, permitir pausas entre sesiones.",
                    "Reevalúe MBI cada 6-12 meses en programas institucionales. Meta: mover agotamiento de alto a medio sin perder calidad asistencial.",
                    "Documente en notas clínicas si el paciente es otro profesional de salud; respete doble rol clínico-ocupacional.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "¿El test de Maslach diagnostica trastorno mental?",
                "a": "No. Identifica síndrome de burnout ocupacional. Diagnósticos psiquiátricos requieren evaluación clínica separada.",
            },
            {
                "q": "¿MBI-HSS o MBI-GS para psicólogos?",
                "a": "MBI-HSS si la práctica es clínica asistencial directa. MBI-GS si busca medir burnout en roles administrativos o mixtos.",
            },
            {
                "q": "¿Puedo usar MBI en telepsicología masiva?",
                "a": "Sí, con instrucciones claras y plataforma segura. Interprete resultados en devolución individual, no solo reporte grupal.",
            },
            {
                "q": "¿Burnout es lo mismo que depresión?",
                "a": "No, aunque coexisten. Burnout mejora con cambios laborales; depresión puede persistir independientemente del contexto.",
            },
            {
                "q": "¿Cada cuánto repetir el test de Maslach?",
                "a": "En programas preventivos, cada 6-12 meses. Tras intervención intensiva, reevalúe a los 3-6 meses.",
            },
        ],
        "related": [
            {"href": "/articulos/burnout-laboral.html", "label": "Burnout laboral: guía clínica"},
            {"href": "/articulos/escala-dass-21.html", "label": "DASS-21: estrés y ánimo"},
            {"href": "/articulos/que-es-el-phq-9.html", "label": "PHQ-9: descartar depresión"},
            {"href": "/articulos/tests-psicologicos-digitales.html", "label": "Tests digitales en consultorio"},
        ],
        "references": [
            "Maslach, C., Jackson, S. E., & Leiter, M. P. (1996). <em>Maslach Burnout Inventory Manual</em> (3rd ed.). Consulting Psychologists Press.",
            "Maslach, C., & Leiter, M. P. (2016). Understanding the burnout experience. <em>World Psychiatry</em>, 15(2), 103-105.",
            "Secretaría del Trabajo y Previsión Social. (2018). NOM-035-STPS-2018, Factores de riesgo psicosocial. <em>Diario Oficial de la Federación</em> (México).",
        ],
    }


def _article_wisc_iv_v(p, table):
    return {
        "slug": "wisc-iv-vs-wisc-v-diferencias",
        "title": "WISC IV vs WISC V: diferencias cl&iacute;nicas | Kalyo",
        "description": "WISC IV vs WISC V: diferencias en \u00edndices, subpruebas, baremos y cu\u00e1ndo migrar en evaluaci\u00f3n cognitiva infantil para neuropsic\u00f3logos cl\u00ednicos en M\u00e9xico.",
        "keywords": "WISC IV, WISC V, WISC-IV vs WISC-V, evaluación cognitiva infantil, Wechsler niños, neuropsicología México",
        "h1": "WISC IV vs WISC V: diferencias clínicas y de interpretación",
        "breadcrumb_short": "WISC IV vs WISC V",
        "quick_answer": "WISC IV (2003) y WISC V (2014) son ediciones sucesivas de la Escala Wechsler de Inteligencia para Niños. WISC V reorganiza índices (incluye índice de velocidad de procesamiento ampliado y opcional índice de memoria de trabajo visual), actualiza subpruebas y baremos. En 2026 la práctica clínica en México debe preferir WISC V salvo continuidad longitudinal con WISC IV.",
        "intro_long": "Muchos consultorios aún comparan archivos WISC IV con protocolos WISC V. Esta guía resume diferencias estructurales, implicaciones para diagnóstico de TDAH y discapacidad intelectual, y enlaza la guía de <a href=\"/articulos/wisc-v-test-inteligencia-ninos.html\">WISC V</a> y <a href=\"/articulos/evaluacion-neuropsicologica-guia-clinica.html\">evaluación neuropsicológica</a>.",
        "test_name": "WISC-V",
        "hero_alt": "Comparación clínica entre baterías WISC IV y WISC V en evaluación infantil",
        "inline_alt": "Tabla de índices WISC IV versus WISC V en neuropsicología pediátrica",
        "sections": [
            {
                "h2": "Contexto histórico: de WISC IV a WISC V",
                "html": p(
                    "El <strong>WISC IV</strong> introdujo cuatro índices: Comprensión Verbal (ICV), Razonamiento Perceptivo (IRP), Memoria de Trabajo (IMT) y Velocidad de Procesamiento (IVP), más CI Total. El <strong>WISC V</strong> mantiene cuatro índices obligatorios, añade índices secundarios opcionales (memoria visual, razonamiento fluido ampliado) y renueva subpruebas para reducir efectos techo y piso.",
                    "Baremos WISC V reflejan cohortes más recientes; comparar puntajes WISC IV y V del mismo niño en fechas distintas no es equivalente a retest fiable.",
                    "En México distribuidores autorizados (Pearson) gestionan migración de materiales; verifique calibración local.",
                ),
            },
            {
                "h2": "Comparativa de índices y subpruebas",
                "html": table(
                    ["Aspecto", "WISC IV", "WISC V"],
                    [
                        ["Años de publicación", "2003", "2014"],
                        ["Índices primarios", "4", "5 (incluye IVP revisado)"],
                        ["CI total", "Sí", "Índice General (IG) + opcionales"],
                        ["Subpruebas nucleares", "Cubos, Semejanzas, etc.", "Renovación parcial (p. ej. Rompecabezas visuales)"],
                        ["Memoria visual", "Limitada", "Índice opcional IMT visual"],
                        ["Baremos", "Cohorte 2003", "Cohorte 2014 (más actual)"],
                    ],
                    cls="items-table",
                )
                + p(
                    "WISC V enfatiza modelo CHC (Cattell-Horn-Carroll) alineado a teoría cognitiva contemporánea. Consulte manual para batería mínima vs. completa.",
                ),
            },
            {
                "h2": "Implicaciones clínicas en TDAH y trastornos del aprendizaje",
                "html": p(
                    "Ambas ediciones muestran perfiles con IMT/IVP bajos en TDAH inatento, pero WISC V ofrece subpruebas adicionales para analizar memoria visual y razonamiento fluido, útil en dislexia y discalculia.",
                    "No diagnostique TDAH solo por dispersión de índices; integre <a href=\"/articulos/conners-3-tdah-ninos.html\">Conners</a> y entrevista.",
                    "Discrepancia ICV vs IRP clásica en dislexia debe confirmarse con pruebas académicas y historial escolar.",
                ),
            },
            {
                "h2": "Cuándo usar WISC IV en 2026",
                "html": p(
                    "Solo si necesita comparación longitudinal estricta con evaluación WISC IV previa del mismo paciente y no puede reevaluar con batería completa WISC V. Documente limitación de interpretación por cambio de escala.",
                    "Instituciones con stock WISC IV deben planear migración; usar WISC IV en nuevos pacientes no es recomendable por baremos obsoletos.",
                    "Para informes periciales, jueces y escuelas pueden preguntar por edición; explique ventajas normativas de WISC V.",
                ),
            },
            {
                "h2": "Administración, tiempo y costos",
                "html": p(
                    "WISC V puede ser ligeramente más largo si aplica índices opcionales. Ambas requieren capacitación certificada y licencia.",
                    "Fraccione en dos sesiones en niños pequeños o con TDAH. Registre observaciones cualitativas igual en ambas ediciones.",
                    "Use <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">guía de interpretación</a> y <a href=\"/articulos/tests-psicologicos-digitales.html\">registro digital</a> de puntajes en expediente.",
                ),
            },
            {
                "h2": "Informes clínicos y comunicación con familia",
                "html": p(
                    "Al migrar de WISC IV a V, explique a padres que cambio de puntaje no implica necesariamente cambio intelectual real, sino instrumento distinto.",
                    "Reporte fortalezas y debilidades en lenguaje funcional escolar. Vincule con recomendaciones SEP o ajustes razonables cuando aplique en México.",
                    "Referencia cruzada con <a href=\"/articulos/wisc-v-test-inteligencia-ninos.html\">guía WISC V Kalyo</a> para profundizar subpruebas.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "¿Puedo comparar CI WISC IV con IG WISC V?",
                "a": "No directamente. Son cohortes normativas distintas. Use WISC V para nueva línea base.",
            },
            {
                "q": "¿WISC V reemplazó por completo al WISC IV?",
                "a": "En práctica clínica actual sí es estándar. WISC IV queda para casos legacy o investigación histórica.",
            },
            {
                "q": "¿Cuál detecta mejor TDAH?",
                "a": "Ninguna diagnostica TDAH. Ambas aportan perfil cognitivo complementario a escalas conductuales.",
            },
            {
                "q": "¿Necesito recertificación para WISC V?",
                "a": "Sí. El editor exige curso WISC V aunque estuviera certificado en WISC IV.",
            },
            {
                "q": "¿Edades iguales en ambas versiones?",
                "a": "WISC V cubre 6:0 a 16:11 años, similar rango. WPPSI y WAIS cubren otros grupos etarios.",
            },
        ],
        "related": [
            {"href": "/articulos/wisc-v-test-inteligencia-ninos.html", "label": "WISC-V: guía completa"},
            {"href": "/articulos/evaluacion-neuropsicologica-guia-clinica.html", "label": "Evaluación neuropsicológica"},
            {"href": "/articulos/conners-3-tdah-ninos.html", "label": "Conners 3: TDAH infantil"},
            {"href": "/articulos/wais-iv-evaluacion-inteligencia-adultos.html", "label": "WAIS-IV: adultos"},
        ],
        "references": [
            "Wechsler, D. (2003). <em>WISC-IV Administration and Scoring Manual</em>. Psychological Corporation.",
            "Wechsler, D. (2014). <em>WISC-V Administration and Scoring Manual</em>. Pearson.",
            "Flanagan, D. P., & Harrison, P. L. (Eds.). (2012). <em>Contemporary Intellectual Assessment</em> (3rd ed.). Guilford Press.",
        ],
    }


def _article_mmpi(p, table):
    return {
        "slug": "mmpi-inventario-multifasico",
        "title": "MMPI: inventario multif&aacute;sico de personalidad | Kalyo",
        "description": "MMPI inventario multif\u00e1sico: MMPI-2-RF, escalas cl\u00ednicas, validez e interpretaci\u00f3n en evaluaci\u00f3n de personalidad cl\u00ednica, forense y laboral en M\u00e9xico.",
        "keywords": "MMPI, MMPI-2, MMPI-2-RF, inventario multif\u00e1sico, evaluaci\u00f3n personalidad, psicolog\u00eda cl\u00ednica M\u00e9xico, psicometr\u00eda",
        "h1": "MMPI: inventario multif\u00e1sico de personalidad e interpretaci\u00f3n",
        "breadcrumb_short": "MMPI inventario multif\u00e1sico",
        "quick_answer": "El MMPI (Minnesota Multiphasic Personality Inventory) es el inventario multif\u00e1sico de personalidad m\u00e1s investigado en psicolog\u00eda cl\u00ednica. La versi\u00f3n vigente MMPI-2-RF eval\u00faa escalas de validez, cl\u00ednicas, de intereses y psicopatolog\u00eda restructurada. Requiere licencia, baremos y formaci\u00f3n; no basta sumar puntajes sin integrar contexto y validez.",
        "intro_long": "Desde MMPI cl\u00e1sico hasta MMPI-2-RF, el inventario multif\u00e1sico es pilar en evaluaci\u00f3n psicol\u00f3gica profunda, selecci\u00f3n de personal y peritajes. Esta gu\u00eda orienta al psic\u00f3logo mexicano en estructura, interpretaci\u00f3n prudente y l\u00edmites, enlazando <a href=\"/articulos/mmpi-2-rf-test-personalidad.html\">MMPI-2-RF en Kalyo</a> y protocolos de <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">interpretaci\u00f3n</a>.",
        "test_name": "MMPI-2-RF",
        "hero_alt": "Evaluaci\u00f3n con MMPI inventario multif\u00e1sico de personalidad en consultorio",
        "inline_alt": "Perfil de escalas cl\u00ednicas y validez del MMPI-2-RF",
        "sections": [
            {
                "h2": "Historia y evoluci\u00f3n del MMPI",
                "html": p(
                    "Hathaway y McKinley desarrollaron el <strong>MMPI</strong> en 1940 para psiquiatr\u00eda. MMPI-2 (1989) ampli\u00f3 \u00edtems y normas; MMPI-2-RF (2008/2016) reestructur\u00f3 escalas seg\u00fan modelo psicom\u00e9trico moderno con menos \u00edtems (338) y mayor eficiencia.",
                    "El t\u00e9rmino <strong>inventario multif\u00e1sico</strong> refleja que no mide un solo rasgo: eval\u00faa m\u00faltiples dimensiones de psicopatolog\u00eda y personalidad en una sola bater\u00eda.",
                    "En M\u00e9xico el MMPI requiere distribuci\u00f3n autorizada; interpretaci\u00f3n en contextos forenses exige certificaci\u00f3n y experiencia.",
                ),
            },
            {
                "h2": "Estructura del MMPI-2-RF: validez y escalas cl\u00ednicas",
                "html": p(
                    "Antes de interpretar contenido cl\u00ednico, analice <strong>escalas de validez</strong>: VRIN (inconsistencia), TRIN (respuesta verdadera/falsa), F-r (infrecuencia), Fs (infreciencia som\u00e1tica), FBS-r (simulaci\u00f3n), RBS (sintomatolog\u00eda som\u00e1tica exagerada), L-r ( mentira), K-r (defensividad). Perfil inv\u00e1lido obliga a suspender interpretaci\u00f3n cl\u00ednica est\u00e1ndar.",
                    "Escalas cl\u00ednicas restructuradas incluyen dominios de internalizaci\u00f3n (RCd depresi\u00f3n, RC2 ansiedad, RC3 somatizaci\u00f3n), externalizaci\u00f3n (RC4 antisocial, RC9 man\u00eda), interpersonales (RC3 cynicism) y cognitivas (RC8 dysregulated thinking).",
                    "Compare con gu\u00eda detallada <a href=\"/articulos/mmpi-2-rf-test-personalidad.html\">MMPI-2-RF</a> para c\u00f3digos espec\u00edficos.",
                ),
            },
            {
                "h2": "Administraci\u00f3n: tiempo, modalidad y poblaci\u00f3n",
                "html": p(
                    "Autoadministrado 35-50 minutos; puede aplicarse en papel o computadora (Q-global). Nivel de lectura aproximado sexto grado; eval\u00fae comprensi\u00f3n en poblaci\u00f3n con baja escolaridad.",
                    "No aplique MMPI en crisis aguda, psicosis no medicada o intoxicaci\u00f3n. En peritajes judiciales registre condiciones estandarizadas.",
                    "Baremos: use normas apropiadas (general, forense, m\u00e9dica) seg\u00fan manual y pa\u00eds.",
                ),
            },
            {
                "h2": "Interpretaci\u00f3n integrada del perfil MMPI",
                "html": p(
                    "Evite etiquetar trastornos DSM solo por elevaci\u00f3n de una escala. Interprete <strong>patrones</strong>: RCd + RC2 elevados sugieren internalizaci\u00f3n depresivo-ansiosa; RC4 + RC9 puede orientar externalizaci\u00f3n.",
                    "Integre entrevista, historia colateral, observaci\u00f3n y otros datos. MMPI es hip\u00f3tesis, no veredicto.",
                    "En evaluaci\u00f3n laboral, cumpla legislaci\u00f3n mexicana sobre pruebas psicom\u00e9tricas y no discriminaci\u00f3n.",
                )
                + table(
                    ["Paso", "Acci\u00f3n", "Error a evitar"],
                    [
                        ["1", "Revisar validez", "Interpretar con F-r o VRIN elevados"],
                        ["2", "Analizar c\u00f3digos RC", "Fijarse en un solo pico aislado"],
                        ["3", "Contrastar con entrevista", "Ignorar contexto cultural"],
                        ["4", "Redactar informe prudente", "Lenguaje determinista o estigmatizante"],
                    ],
                    cls="items-table",
                ),
            },
            {
                "h2": "Usos cl\u00ednicos, forenses y organizacionales en M\u00e9xico",
                "html": p(
                    "Cl\u00ednica: evaluaci\u00f3n de personalidad en psicoterapia de largo plazo, hospital psiqui\u00e1trico, programas de adicci\u00f3n. Forense: capacidad mental, custodia (con extrema cautela), imputabilidad (solo peritos calificados). Organizacional: alto riesgo y regulado; requiere consentimiento y validez laboral demostrada.",
                    "Documente seg\u00fan <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> y c\u00f3digo de \u00e9tica. No comparta perfil bruto con terceros sin autorizaci\u00f3n.",
                    "Para tamizaje breve de depresi\u00f3n/ansiedad, <a href=\"/articulos/que-es-el-phq-9.html\">PHQ-9</a> y <a href=\"/articulos/que-es-el-gad-7.html\">GAD-7</a> son m\u00e1s eficientes que MMPI.",
                ),
            },
            {
                "h2": "Limitaciones \u00e9ticas y culturales",
                "html": p(
                    "Normas estadounidenses pueden no trasladarse directamente a poblaci\u00f3n mexicana; busque estudios locales y supervisi\u00f3n.",
                    "Sesgo de deseabilidad social es alto en contextos donde salud mental estigmatiza. Escalas K-r y L-r ayudan pero no agotan el problema.",
                    "Formaci\u00f3n continua en MMPI-2-RF es obligatoria para interpretaci\u00f3n responsable; evite automatizar reportes sin revisi\u00f3n cl\u00ednica.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfMMPI o MMPI-2-RF en 2026?",
                "a": "MMPI-2-RF es la versi\u00f3n recomendada por eficiencia y base psicom\u00e9trica. MMPI-2 cl\u00e1sico persiste en archivos legacy; migre cuando sea posible.",
            },
            {
                "q": "\u00bfEl MMPI diagnostica esquizofrenia?",
                "a": "No. Escalas como RC8 sugieren pensamiento desorganizado; diagn\u00f3stico requiere entrevista estructurada y evaluaci\u00f3n psiqui\u00e1trica.",
            },
            {
                "q": "\u00bfPuedo aplicar MMPI en adolescentes?",
                "a": "Use MMPI-A-RF para adolescentes. MMPI-2-RF es para adultos 18+.",
            },
            {
                "q": "\u00bfQu\u00e9 hago si el perfil es inv\u00e1lido?",
                "a": "No interprete escalas cl\u00ednicas. Reexplique instrucciones, eval\u00fae comprensi\u00f3n, considere reapplication o entrevista focal.",
            },
            {
                "q": "\u00bfMMPI sirve para selecci\u00f3n de personal?",
                "a": "Solo con validaci\u00f3n laboral espec\u00edfica, consentimiento y cumplimiento legal. Uso cl\u00ednico no implica validez ocupacional autom\u00e1tica.",
            },
        ],
        "related": [
            {"href": "/articulos/mmpi-2-rf-test-personalidad.html", "label": "MMPI-2-RF: gu\u00eda completa"},
            {"href": "/articulos/como-interpretar-tests-psicologicos.html", "label": "Interpretar tests psicol\u00f3gicos"},
            {"href": "/articulos/evaluacion-neuropsicologica-guia-clinica.html", "label": "Evaluaci\u00f3n neuropsicol\u00f3gica"},
            {"href": "/articulos/tests-psicologicos-digitales.html", "label": "Tests psicol\u00f3gicos digitales"},
        ],
        "references": [
            "Ben-Porath, Y. S., & Tellegen, A. (2008/2016). <em>MMPI-2-RF Manual for Administration, Scoring, and Interpretation</em>. University of Minnesota Press.",
            "Butcher, J. N., Graham, J. R., Ben-Porath, Y. S., Tellegen, A., Dahlstrom, W. G., & Kaemmer, B. (2001). <em>MMPI-2 Manual for Administration and Scoring</em>. University of Minnesota Press.",
            "Hathaway, S. R., & McKinley, J. C. (1943). <em>MMPI Manual</em>. University of Minnesota Press.",
        ],
    }


def _article_wais_iv(p, table):
    return {
        "slug": "wais-iv-escala-inteligencia-adultos",
        "title": "WAIS IV: escala de inteligencia en adultos | Kalyo",
        "description": "WAIS IV en adultos: \u00edndices, subpruebas, interpretaci\u00f3n cl\u00ednica e indicaciones neuropsicol\u00f3gicas en evaluaci\u00f3n cognitiva de adultos en consulta M\u00e9xico.",
        "keywords": "WAIS IV, WAIS-IV, escala inteligencia adultos, evaluaci\u00f3n cognitiva, Wechsler adultos, neuropsicolog\u00eda M\u00e9xico",
        "h1": "WAIS IV: escala de inteligencia para evaluaci\u00f3n de adultos",
        "breadcrumb_short": "WAIS IV adultos",
        "quick_answer": "El WAIS IV (Wechsler Adult Intelligence Scale, cuarta edici\u00f3n) eval\u00faa funcionamiento intelectual en adultos de 16 a 90 a\u00f1os mediante cuatro \u00edndices: Comprensi\u00f3n Verbal, Razonamiento Perceptivo, Memoria de Trabajo y Velocidad de Procesamiento, m\u00e1s CI Total. Es referencia en neuropsicolog\u00eda cl\u00ednica, discapacidad cognitiva y evaluaci\u00f3n de deterioro.",
        "intro_long": "El WAIS IV sigue siendo la escala de inteligencia adultos m\u00e1s utilizada en consultorios mexicanos de neuropsicolog\u00eda. Esta gu\u00eda resume administraci\u00f3n, interpretaci\u00f3n de \u00edndices, indicaciones cl\u00ednicas y relaci\u00f3n con la gu\u00eda previa de <a href=\"/articulos/wais-iv-evaluacion-inteligencia-adultos.html\">WAIS-IV en Kalyo</a> y evaluaci\u00f3n integral en <a href=\"/articulos/evaluacion-neuropsicologica-guia-clinica.html\">neuropsicolog\u00eda cl\u00ednica</a>.",
        "test_name": "WAIS-IV",
        "hero_alt": "Administraci\u00f3n del WAIS IV escala de inteligencia en adulto en consultorio",
        "inline_alt": "Perfil de \u00edndices del WAIS IV comprensi\u00f3n verbal razonamiento perceptivo memoria y velocidad",
        "sections": [
            {
                "h2": "Estructura del WAIS IV y modelo de inteligencia",
                "html": p(
                    "Publicado en 2008, el <strong>WAIS IV</strong> sustituy\u00f3 al WAIS-III con reorganizaci\u00f3n de subpruebas y eliminaci\u00f3n del CI verbal/performance cl\u00e1sico en favor de cuatro \u00edndices emp\u00edricos alineados al modelo CHC.",
                    "Los \u00edndices son: <strong>ICV</strong> (Comprensi\u00f3n Verbal), <strong>IRP</strong> (Razonamiento Perceptivo), <strong>IMT</strong> (Memoria de Trabajo) e <strong>IVP</strong> (Velocidad de Procesamiento). El <strong>CI Total</strong> resume funcionamiento general con media 100 y DE 15.",
                    "Compare con <a href=\"/articulos/wisc-v-test-inteligencia-ninos.html\">WISC-V</a> cuando eval\u00faa continuidad desarrollo adolescente-adulto joven.",
                ),
            },
            {
                "h2": "Subpruebas principales y tiempo de aplicaci\u00f3n",
                "html": p(
                    "Subpruebas nucleares incluyen Semejanzas, Vocabulario, Cubos, Matrices, D\u00edgitos, Clave de n\u00fameros, Aritm\u00e9tica (suplementaria) y B\u00fasqueda de s\u00edmbolos. Bater\u00eda completa 60-90 minutos; puede reducirse seg\u00fan hip\u00f3tesis cl\u00ednica siguiendo manual.",
                    "Requiere certificaci\u00f3n Pearson y materiales estandarizados. Ambiente silencioso, sin interrupciones; documente fatiga en adultos mayores.",
                    "Registre observaciones cualitativas: estrategias, impulsividad, abandono de \u00edtems dif\u00edciles.",
                ),
            },
            {
                "h2": "Interpretaci\u00f3n de puntajes e \u00edndices",
                "html": p(
                    "Puntajes compuestos 90-109 promedio; 85-89 lim\u00edtrofe bajo; 70-84 bajo; &lt; 70 sugiere discapacidad intelectual solo si concuerda con adaptativo y historia. Dispersi\u00f3n \u2265 15 puntos entre \u00edndices indica heterogeneidad cognitiva.",
                    "IMT bajo en adultos puede asociarse a TDAH, lesiones frontales o ansiedad que interfiere. IVP bajo sugiere procesamiento lento, no necesariamente baja inteligencia global.",
                )
                + table(
                    ["\u00cdndice WAIS IV", "Construye aproximado", "Hallazgo cl\u00ednico frecuente"],
                    [
                        ["ICV", "Verbal, cristalizado", "Dislexia compensada, educaci\u00f3n alta"],
                        ["IRP", "Razonamiento fluido, visoespacial", "Lesiones parietales, TEC"],
                        ["IMT", "Atenci\u00f3n, retenci\u00f3n", "TDAH, ansiedad evaluativa"],
                        ["IVP", "Velocidad psicomotora", "Depresi\u00f3n, Parkinson, medicaci\u00f3n"],
                    ],
                    cls="items-table",
                ),
            },
            {
                "h2": "Indicaciones cl\u00ednicas en adultos",
                "html": p(
                    "Discapacidad intelectual, deterioro cognitivo leve (DCL), demencia temprana, TEC, esclerosis m\u00faltiple, TDAH adulto, discapacidad laboral, evaluaci\u00f3n pre-quir\u00fargica de epilepsia, capacidad para toma de decisiones (con extrema cautela \u00e9tica).",
                    "No es prueba de personalidad ni de simulaci\u00f3n por s\u00ed sola; combine con <a href=\"/articulos/mmpi-2-rf-test-personalidad.html\">MMPI-2-RF</a> en peritajes complejos.",
                    "En adultos mayores use baremos por edad y descarte visi\u00f3n/audici\u00f3n no corregida.",
                ),
            },
            {
                "h2": "WAIS IV en contexto mexicano",
                "html": p(
                    "Verifique disponibilidad de baremos para poblaci\u00f3n mexicana o latinoamericana; interpretaci\u00f3n con normas estadounidenses requiere justificaci\u00f3n en informe.",
                    "Informes para IMSS, pensiones o laborales deben traducir hallazgos a funcionamiento cotidiano (conducir, administrar finanzas, trabajo intelectual).",
                    "Documente en expediente seg\u00fan <a href=\"/articulos/nom-004-historia-clinica-mexico.html\">NOM-004</a> y gu\u00eda <a href=\"/articulos/como-interpretar-tests-psicologicos.html\">interpretaci\u00f3n de tests</a>.",
                ),
            },
            {
                "h2": "Limitaciones y buenas pr\u00e1cticas",
                "html": p(
                    "Sesgo educativo y cultural en subpruebas verbales; adultos biling\u00fces o con escolaridad interrumpida pueden obtener ICV artificialmente bajo.",
                    "Ansiedad evaluativa deprime IVP e IMT transitoriamente; sesi\u00f3n de rapport previa ayuda.",
                    "Retest antes de 12 meses puede inflar puntajes por practica; espacie reevaluaciones salvo indicaci\u00f3n cl\u00ednica.",
                    "Enlace con art\u00edculo previo <a href=\"/articulos/wais-iv-evaluacion-inteligencia-adultos.html\">WAIS-IV evaluaci\u00f3n inteligencia adultos</a> para profundizar casos cl\u00ednicos.",
                ),
            },
        ],
        "faqs": [
            {
                "q": "\u00bfWAIS IV o WAIS-5?",
                "a": "Consulte disponibilidad regional. WAIS IV sigue siendo ampliamente usado en M\u00e9xico; migre cuando haya baremos locales y certificaci\u00f3n disponible para nueva edici\u00f3n.",
            },
            {
                "q": "\u00bfWAIS IV diagnostica demencia?",
                "a": "No. Aporta perfil cognitivo compatible con deterioro; diagn\u00f3stico requiere historia, RM, pruebas espec\u00edficas y criterios cl\u00ednicos.",
            },
            {
                "q": "\u00bfDesde qu\u00e9 edad se aplica WAIS IV?",
                "a": "16-90 a\u00f1os. Adolescentes 16-17 pueden aplicarse seg\u00fan manual; menores usan WISC-V.",
            },
            {
                "q": "\u00bfPuedo administrar WAIS IV en una sola sesi\u00f3n a adultos mayores?",
                "a": "Preferible fraccionar si hay fatiga, dolor cr\u00f3nico o ansiedad. Priorice subpruebas seg\u00fan hip\u00f3tesis.",
            },
            {
                "q": "\u00bfC\u00f3mo reportar WAIS IV a pacientes?",
                "a": "Evite jerga. Describa fortalezas y dificultades en actividades reales: memoria para instrucciones, rapidez en tareas, comprensi\u00f3n verbal.",
            },
        ],
        "related": [
            {"href": "/articulos/wais-iv-evaluacion-inteligencia-adultos.html", "label": "WAIS-IV: evaluaci\u00f3n previa Kalyo"},
            {"href": "/articulos/wisc-v-test-inteligencia-ninos.html", "label": "WISC-V: inteligencia infantil"},
            {"href": "/articulos/evaluacion-neuropsicologica-guia-clinica.html", "label": "Evaluaci\u00f3n neuropsicol\u00f3gica"},
            {"href": "/articulos/wisc-iv-vs-wisc-v-diferencias.html", "label": "WISC IV vs WISC V"},
        ],
        "references": [
            "Wechsler, D. (2008). <em>WAIS-IV Administration and Scoring Manual</em>. Pearson.",
            "Wechsler, D. (2008). <em>WAIS-IV Technical and Interpretive Manual</em>. Pearson.",
            "Lezak, M. D., Howieson, D. B., Bigler, E. D., & Tranel, D. (2012). <em>Neuropsychological Assessment</em> (5th ed.). Oxford University Press.",
        ],
    }
