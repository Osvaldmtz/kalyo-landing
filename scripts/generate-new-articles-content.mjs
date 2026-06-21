function p(text) {
  return `<p>\n      ${text}\n    </p>`;
}

function paras(...texts) {
  return texts.map((t) => p(t)).join('\n\n    ');
}

function section(title, paragraphs, extra = '') {
  return `<h2>${title}</h2>\n    ${paras(...paragraphs)}${extra}`;
}

function makeArticle(base, sections) {
  return {
    ...base,
    bodyHtml: sections.map((s) => section(s.title, s.paragraphs, s.extra || '')).join('\n\n    '),
  };
}

const CLINICAL_META = 'Psicometr&iacute;a cl&iacute;nica &middot; Actualizaci&oacute;n 2026';
const PERINATAL_META = 'Psicometr&iacute;a perinatal &middot; Actualizaci&oacute;n 2026';
const NORM_MX = 'Normativa cl&iacute;nica &middot; Actualizaci&oacute;n 2026';
const NORM_CO = 'Normativa Colombia &middot; Actualizaci&oacute;n 2026';

export const REMAINING_ARTICLES = [
  makeArticle(
    {
      slug: 'isi-indice-severidad-insomnio',
      filename: 'isi-indice-severidad-insomnio.html',
      title: 'ISI: Índice de Severidad del Insomnio — guía clínica para psicólogos | Kalyo',
      description:
        'Guía completa del ISI (0-28): interpretación de puntuaciones, niveles de severidad del insomnio y uso en consulta. Aplica el ISI digitalmente en Kalyo.',
      keywords: 'ISI, insomnio, índice severidad insomnio, psicología clínica, sueño, evaluación del sueño',
      metaLabel: CLINICAL_META,
      h1: 'ISI: &Iacute;ndice de Severidad del Insomnio',
      intro:
        'El Insomnia Severity Index (ISI) es un cuestionario breve de siete &iacute;tems dise&ntilde;ado para evaluar la naturaleza, la severidad y el impacto del insomnio. Ampliamente utilizado en psicolog&iacute;a cl&iacute;nica y medicina del sue&ntilde;o, el ISI permite cuantificar la gravedad del insomnio en una escala de 0 a 28 y monitorizar la respuesta a intervenciones cognitivo-conductuales para el insomnio (TCC-I).',
      heroAlt: 'ISI índice de severidad del insomnio en tablet con interfaz clínica púrpura',
      inlineAlt: 'Gráfico de interpretación ISI escala 0-28, psicología clínica púrpura',
      ctaTitle: 'Aplica el ISI digitalmente en Kalyo',
      ctaText: 'Eval&uacute;a el insomnio con el ISI y lleva el seguimiento de tus pacientes con gr&aacute;ficas de evoluci&oacute;n autom&aacute;ticas.',
      ctaButton: 'Prueba gratis 14 d&iacute;as &rarr;',
      related: [
        ['escala-dass-21', 'DASS-21: Depresi&oacute;n, Ansiedad y Estr&eacute;s'],
        ['que-es-el-gad-7', '&iquest;Qu&eacute; es el GAD-7?'],
        ['que-es-el-phq-9', '&iquest;Qu&eacute; es el PHQ-9?'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; es el ISI?',
        paragraphs: [
          'El ISI fue desarrollado por Charles M. Morin y colaboradores como un instrumento breve y validado para evaluar la percepci&oacute;n subjetiva del insomnio. Consta de siete &iacute;tems que exploran la severidad de los problemas para conciliar el sue&ntilde;o, mantenerlo y despertar demasiado pronto, el grado de satisfacci&oacute;n con el patr&oacute;n de sue&oacute; actual, el impacto diurno del insomnio, la preocupaci&oacute;n por el problema del sue&ntilde;o y la interferencia con la calidad de vida.',
          'A diferencia de registros polisomnogr&aacute;ficos o actigraf&iacute;a, el ISI captura la experiencia subjetiva del paciente, que es el criterio diagn&oacute;stico central del insomnio seg&uacute;ng el DSM-5 y la CIE-11. Esto lo convierte en una herramienta pr&aacute;ctica para la consulta psicol&oacute;gica, donde la queja subjetiva de sue&ntilde;o insuficiente o no reparador es el punto de partida cl&iacute;nico.',
          'El cuestionario puede completarse en menos de cinco minutos y est&aacute; disponible en espa&ntilde;ol con propiedades psicom&eacute;tricas adecuadas en poblaciones latinoamericanas. Su brevedad lo hace ideal para evaluaciones peri&oacute;dicas durante el tratamiento del insomnio y para investigaci&oacute;n cl&iacute;nica.',
          'En la pr&aacute;ctica cl&iacute;nica contempor&aacute;nea, el ISI se ha convertido en el est&aacute;ndar de referencia para cuantificar la severidad del insomnio antes y despu&eacute;s de intervenciones, especialmente la terapia cognitivo-conductual para el insomnio (TCC-I), considerada el tratamiento de primera l&iacute;nea por las gu&iacute;as internacionales.',
        ],
      },
      {
        title: 'C&oacute;mo se aplica',
        paragraphs: [
          'Cada uno de los siete &iacute;tems del ISI se responde en una escala Likert de cinco puntos (0 a 4), con anclajes espec&iacute;ficos para cada pregunta. Los &iacute;tems 1 a 3 eval&uacute;an la severidad de las dificultades de sue&oacute;o; el &iacute;tem 4 mide la satisfacci&oacute;n con el patr&oacute;n actual; el &iacute;tem 5 eval&uacute;a el impacto diurno; el &iacute;tem 6 explora la preocupaci&oacute;n; y el &iacute;tem 7 valora la interferencia con la calidad de vida.',
          'El puntaje total se obtiene sumando las respuestas de los siete &iacute;tems, con un rango posible de 0 a 28. No existen subescalas: el ISI produce una puntuaci&oacute;n global de severidad del insomnio. La administraci&oacute;n puede ser presencial, telef&oacute;nica o digital; en plataformas como Kalyo, la puntuaci&oacute;n y la interpretaci&oacute;n se generan autom&aacute;ticamente.',
          'Se recomienda aplicar el ISI con referencia a las &uacute;ltimas dos semanas, aline&aacute;ndose con los criterios temporales del DSM-5 para el trastorno de insomnio. Si el paciente presenta comorbilidades m&eacute;dicas que afectan el sue&ntilde;o (apnea, dolor cr&oacute;nico, trastornos del movimiento), conviene documentarlas en la historia cl&iacute;nica para contextualizar los resultados.',
          'En el seguimiento terap&eacute;utico, readministrar el ISI cada dos a cuatro semanas permite evaluar la respuesta a la TCC-I. Una reducci&oacute;n de al menos seis puntos se considera cl&iacute;nicamente significativa en estudios de validaci&oacute;n del instrumento.',
        ],
      },
      {
        title: 'Interpretaci&oacute;n de puntuaciones (0&ndash;28)',
        paragraphs: [
          'La interpretaci&oacute;n del ISI se basa en rangos de severidad establecidos por los autores y confirmados en m&uacute;ltiples estudios. Estos rangos orientan la toma de decisiones cl&iacute;nicas, aunque siempre deben complementarse con la entrevista cl&iacute;nica y la evaluaci&oacute;n de comorbilidades.',
          'El insomnio frecuentemente coexiste con ansiedad y depresi&oacute;n. Cuando el ISI indica severidad cl&iacute;nica, conviene administrar el <a href="/articulos/que-es-el-gad-7.html">GAD-7</a> para ansiedad y el <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a> para depresi&oacute;n, o utilizar el <a href="/articulos/escala-dass-21.html">DASS-21</a> para obtener un perfil integrado de las tres dimensiones emocionales.',
        ],
        extra: `
    <table class="severity-table">
      <thead>
        <tr>
          <th>Puntuaci&oacute;n</th>
          <th>Severidad</th>
          <th>Acci&oacute;n cl&iacute;nica</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="score-badge">0 &ndash; 7</span></td>
          <td><strong>Sin insomnio cl&iacute;nico</strong></td>
          <td>Monitoreo; psicoeducaci&oacute;n sobre higiene del sue&ntilde;o si hay quejas leves.</td>
        </tr>
        <tr>
          <td><span class="score-badge">8 &ndash; 14</span></td>
          <td><strong>Insomnio subcl&iacute;nico</strong></td>
          <td>Intervenci&oacute;n breve; considerar TCC-I si persiste.</td>
        </tr>
        <tr>
          <td><span class="score-badge">15 &ndash; 21</span></td>
          <td><strong>Insomnio cl&iacute;nico moderado</strong></td>
          <td>TCC-I estructurada; evaluar comorbilidades.</td>
        </tr>
        <tr>
          <td><span class="score-badge">22 &ndash; 28</span></td>
          <td><strong>Insomnio cl&iacute;nico severo</strong></td>
          <td>TCC-I intensiva; valorar derivaci&oacute;n a unidad del sue&ntilde;o o psiquiatr&iacute;a.</td>
        </tr>
      </tbody>
    </table>`,
      },
      {
        title: 'Relaci&oacute;n con ansiedad, depresi&oacute;n y estr&eacute;s',
        paragraphs: [
          'El insomnio mantiene una relaci&oacute;n bidireccional con la ansiedad y la depresi&oacute;n: los trastornos del sue&ntilde;o pueden ser causa, consecuencia o factor de mantenimiento de la sintomatolog&iacute;a emocional. Por ello, un ISI elevado debe motivar la evaluaci&oacute;n de comorbilidades con instrumentos como el <a href="/articulos/escala-dass-21.html">DASS-21</a>, que diferencia depresi&oacute;n, ansiedad y estr&eacute;s en una sola bater&iacute;a.',
          'La hiperactivaci&oacute;n cognitiva nocturna, caracter&iacute;stica de la ansiedad generalizada, frecuentemente se refleja en puntuaciones altas del ISI en los &iacute;tems de preocupaci&oacute;n e impacto diurno. El <a href="/articulos/que-es-el-gad-7.html">GAD-7</a> ayuda a determinar si el insomnio es secundario a un trastorno de ansiedad que requiere tratamiento espec&iacute;fico.',
          'En depresi&oacute;n, la insomnia de conciliaci&oacute;n y las vigilias nocturnas son s&iacute;ntomas nucleares. Un paciente con ISI elevado y <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a> positivo puede beneficiarse de un plan integrado que aborde ambas dimensiones simult&aacute;neamente, en lugar de tratar el sue&ntilde;o de forma aislada.',
          'El estr&eacute;s cr&oacute;nico laboral o familiar tambi&eacute;n eleva las puntuaciones del ISI. En estos casos, intervenciones de manejo del estr&eacute;s combinadas con t&eacute;cnicas de higiene del sue&ntilde;o y restricci&oacute;n del sue&ntilde;o suelen ser el primer escal&oacute;n terap&eacute;utico antes de derivar a un especialista del sue&ntilde;o.',
        ],
      },
      {
        title: '&iquest;Cu&aacute;ndo usar el ISI?',
        paragraphs: [
          'El ISI es la herramienta de elecci&oacute;n para: evaluaci&oacute;n inicial de quejas de insomnio en consulta psicol&oacute;gica, monitorizaci&oacute;n de respuesta a TCC-I, investigaci&oacute;n cl&iacute;nica sobre trastornos del sue&ntilde;o, tamizaje en pacientes con trastornos de ansiedad o depresi&oacute;n com&oacute;rbe, y evaluaci&oacute;n de resultados en programas de salud mental digital.',
          'En telepsicolog&iacute;a, el ISI es especialmente &uacute;til porque el paciente puede completarlo antes de la sesi&oacute;n, permitiendo al cl&iacute;nico revisar la severidad del insomnio y ajustar el plan terap&eacute;utico. Las plataformas digitales facilitan la visualizaci&oacute;n de tendencias a lo largo del tratamiento.',
          'Tambi&eacute;n se recomienda en evaluaciones pre y post intervenci&oacute;n para documentar objetivamente la eficacia del tratamiento, cumpliendo con est&aacute;ndares de registro cl&iacute;nico y evidencia de resultados terap&eacute;uticos.',
          'En pacientes que reciben farmacoterapia para el insomnio (hipn&oacute;ticos), el ISI permite monitorizar si la medicaci&oacute;n est&aacute; produciendo mejor&iacute;a cl&iacute;nicamente significativa o si es necesario transitar hacia TCC-I como tratamiento de mantenimiento.',
        ],
      },
      {
        title: 'Limitaciones',
        paragraphs: [
          'El ISI eval&uacute;a exclusivamente la percepci&oacute;n subjetiva del insomnio y no detecta trastornos del sue&ntilde;o org&aacute;nicos como apnea obstructiva del sue&ntilde;o, narcolepsia o trastornos del movimiento. Ante ISI elevado con sospecha de apnea (ronquidos, pausas respiratorias reportadas), se requiere derivaci&oacute;n a medicina del sue&ntilde;o.',
          'Como instrumento de autoinforme, est&aacute; sujeto a sesgos de deseabilidad social y a la capacidad del paciente para estimar con precisi&oacute;n sus dificultades de sue&ntilde;o. Algunos pacientes sobreestiman o subestiman la severidad en comparaci&oacute;n con medidas objetivas.',
          'El ISI no diferencia entre insomnio primario e insomnio inducido por sustancias o medicamentos. Una anamnesis detallada sobre consumo de cafe&iacute;na, alcohol, cannabis y medicamentos psicotr&oacute;picos es indispensable para interpretar correctamente los resultados.',
          'Finalmente, los puntos de corte del ISI fueron validados principalmente en poblaciones occidentales. En contextos latinoamericanos, conviene complementar la interpretaci&oacute;n num&eacute;rica con la exploraci&oacute;n cultural de c&oacute;mo el paciente describe y vive sus dificultades de sue&ntilde;o.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'epds-depresion-postnatal-edimburgo',
      filename: 'epds-depresion-postnatal-edimburgo.html',
      title: 'EPDS: Escala de Depresión Postnatal de Edimburgo — guía clínica | Kalyo',
      description:
        'Guía del EPDS: interpretación de puntuaciones, tamizaje de depresión postnatal y protocolos clínicos. Escala de Edimburgo disponible digitalmente en Kalyo.',
      keywords: 'EPDS, depresión postnatal, escala Edimburgo, psicología perinatal, tamizaje posparto, salud mental materna',
      metaLabel: PERINATAL_META,
      h1: 'EPDS: Escala de Depresi&oacute;n Postnatal de Edimburgo',
      intro:
        'La Edinburgh Postnatal Depression Scale (EPDS) es el instrumento de tamizaje m&aacute;s utilizado en el mundo para detectar depresi&oacute;n postnatal y depresi&oacute;n perinatal. Desarrollada en 1987 por Cox, Holden y Sagovsky, consta de diez &iacute;tems que eval&uacute;an s&iacute;ntomas depresivos durante la &uacute;ltima semana, con especial atenci&oacute;n al afecto y la ansiedad materna.',
      heroAlt: 'EPDS escala depresión postnatal en tablet con interfaz clínica púrpura',
      inlineAlt: 'Gráfico de interpretación EPDS escala 0-30, psicología perinatal púrpura',
      ctaTitle: 'Aplica el EPDS digitalmente en Kalyo',
      ctaText: 'Tamiza depresi&oacute;n postnatal con el EPDS y documenta el seguimiento perinatal de tus pacientes en una plataforma segura.',
      ctaButton: 'Prueba gratis 14 d&iacute;as &rarr;',
      related: [
        ['que-es-el-phq-9', '&iquest;Qu&eacute; es el PHQ-9?'],
        ['evaluacion-riesgo-suicida', 'Evaluaci&oacute;n de Riesgo Suicida'],
        ['escala-dass-21', 'DASS-21: Depresi&oacute;n, Ansiedad y Estr&eacute;s'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; es el EPDS?',
        paragraphs: [
          'El EPDS fue dise&ntilde;ado espec&iacute;ficamente para detectar depresi&oacute;n en el periodo perinatal, incluyendo el embarazo y las primeras semanas del posparto. A diferencia de escalas generales de depresi&oacute;n, sus &iacute;tems fueron seleccionados para capturar la experiencia emocional de madres (y padres) sin confundir s&iacute;ntomas depresivos con molestias fisiol&oacute;gicas normales del posparto, como fatiga o cambios del apetito.',
          'Consta de diez reactivos de autoinforme que eval&uacute;an el estado emocional durante los &uacute;ltimos siete d&iacute;as. Los &iacute;tems exploran la capacidad de experimentar placer, autol&aacute;stima, miedo, ansiedad, desesperanza y, de forma cr&iacute;tica, pensamientos de autolesi&oacute;n. El &iacute;tem 10 aborda directamente la posibilidad de autolesionarse y requiere evaluaci&oacute;n cl&iacute;nica inmediata si se punt&uacute;a distinto de cero.',
          'El EPDS ha sido traducido y validado en decenas de idiomas, incluido el espa&ntilde;ol, con buenas propiedades psicom&eacute;tricas en poblaciones latinoamericanas. Su brevedad (menos de cinco minutos) lo hace viable para aplicaci&oacute;n en consultas de ginecolog&iacute;a, pediatr&iacute;a y psicolog&iacute;a perinatal.',
          'Es importante se&ntilde;alar que el EPDS es un instrumento de tamizaje, no un diagn&oacute;stico. Un puntaje elevado indica probable depresi&oacute;n postnatal y requiere evaluaci&oacute;n cl&iacute;nica confirmatoria mediante entrevista estructurada y exploraci&oacute;n psicopatol&oacute;gica completa.',
        ],
      },
      {
        title: 'C&oacute;mo se aplica',
        paragraphs: [
          'Cada &iacute;tem del EPDS se responde en una escala de cuatro puntos (0 a 3), con opciones de respuesta espec&iacute;ficas para cada pregunta. El puntaje total var&iacute;a de 0 a 30. La instrucci&oacute;n est&aacute;ndar es: &laquo;En los &uacute;ltimos siete d&iacute;as, &iquest;con qu&eacute; frecuencia te has sentido as&iacute;?&raquo;',
          'El EPDS puede administrarse durante el embarazo (idealmente en el segundo y tercer trimestre) y en el posparto (semanas 6 a 12 como m&iacute;nimo, aunque puede aplicarse antes si hay indicadores de riesgo). Algunos protocolos recomiendan tamizaje rutinario en la primera consulta posparto y a las 6 semanas.',
          'La aplicaci&oacute;n puede ser presencial, con el cl&iacute;nico presente para resolver dudas, o digital a trav&eacute;s de plataformas como Kalyo. En contextos digitales, es fundamental garantizar privacidad y ofrecer seguimiento inmediato si el &iacute;tem 10 es positivo.',
          'El EPDS tambi&eacute;n puede aplicarse a padres, pues la depresi&oacute;n paterna posparto es un fen&oacute;meno reconocido con implicaciones para el v&iacute;nculo padre-hijo y el apoyo a la pareja. Las puntuaciones se interpretan con los mismos puntos de corte.',
        ],
      },
      {
        title: 'Interpretaci&oacute;n de puntuaciones',
        paragraphs: [
          'Los puntos de corte m&aacute;s utilizados para el EPDS son: 0&ndash;9 sin depresi&oacute;n probable, 10&ndash;12 posible depresi&oacute;n (requiere reevaluaci&oacute;n), y 13 o m&aacute;s depresi&oacute;n probable. Algunos protocolos utilizan un punto de corte de 10 para maximizar la sensibilidad del tamizaje en poblaci&oacute;n general.',
          'El &iacute;tem 10 merece atenci&oacute;n independiente del puntaje total. Cualquier respuesta distinta de cero activa un protocolo de evaluaci&oacute;n de riesgo suicida, tal como se describe en nuestra gu&iacute;a de <a href="/articulos/evaluacion-riesgo-suicida.html">evaluaci&oacute;n de riesgo suicida</a>. La depresi&oacute;n postnatal con ideaci&oacute;n suicida es una emergencia cl&iacute;nica que requiere intervenci&oacute;n inmediata.',
        ],
        extra: `
    <table class="severity-table">
      <thead>
        <tr>
          <th>Puntuaci&oacute;n</th>
          <th>Interpretaci&oacute;n</th>
          <th>Acci&oacute;n cl&iacute;nica</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="score-badge">0 &ndash; 9</span></td>
          <td><strong>Sin depresi&oacute;n probable</strong></td>
          <td>Monitoreo rutinario; psicoeducaci&oacute;n perinatal.</td>
        </tr>
        <tr>
          <td><span class="score-badge">10 &ndash; 12</span></td>
          <td><strong>Posible depresi&oacute;n</strong></td>
          <td>Reevaluaci&oacute;n en 2 semanas; entrevista cl&iacute;nica.</td>
        </tr>
        <tr>
          <td><span class="score-badge">13 &ndash; 30</span></td>
          <td><strong>Depresi&oacute;n probable</strong></td>
          <td>Evaluaci&oacute;n cl&iacute;nica completa; plan de tratamiento; evaluar riesgo.</td>
        </tr>
      </tbody>
    </table>`,
      },
      {
        title: 'EPDS vs PHQ-9 en el periodo perinatal',
        paragraphs: [
          'El <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a> es ampliamente utilizado para tamizaje de depresi&oacute;n en general, pero el EPDS fue dise&ntilde;ado espec&iacute;ficamente para el contexto perinatal. Sus &iacute;tems evitan confundir s&iacute;ntomas depresivos con experiencias normales del posparto, como cansancio extremo por cuidado nocturno del beb&eacute;.',
          'En embarazo y posparto, el EPDS es preferible como tamizaje rutinario. El PHQ-9 puede complementarlo cuando se confirma depresi&oacute;n y se necesita monitorizar la severidad sintom&aacute;tica con mayor granularidad durante el tratamiento.',
          'Para evaluar ansiedad com&oacute;rbe, el <a href="/articulos/escala-dass-21.html">DASS-21</a> ofrece subescalas diferenciadas de depresi&oacute;n, ansiedad y estr&eacute;s, &uacute;til en madres con preocupaciones intensas sobre el cuidado del beb&eacute; o con s&iacute;ntomas de ansiedad perinatal.',
          'La combinaci&oacute;n EPDS + evaluaci&oacute;n de v&iacute;nculo materno-infantil + exploraci&oacute;n de factores de riesgo (historia de depresi&oacute;n, falta de apoyo social, complicaciones del parto) conforma una evaluaci&oacute;n perinatal integral.',
        ],
      },
      {
        title: '&iquest;Cu&aacute;ndo usar el EPDS?',
        paragraphs: [
          'El EPDS debe aplicarse rutinariamente en: consultas de control prenatal (segundo y tercer trimestre), visitas posparto en pediatr&iacute;a y ginecolog&iacute;a, consultas de psicolog&iacute;a perinatal, y programas de salud materno-infantil. La OMS y m&uacute;ltiples sociedades m&eacute;dicas recomiendan tamizaje universal.',
          'Tambi&eacute;n es indicado ante se&ntilde;ales cl&iacute;nicas de alerta: llanto persistente, dificultad para vincularse con el beb&eacute;, aislamiento social, p&eacute;rdida de apetito extrema, insomnio incluso cuando el beb&eacute; duerme, o expresiones de culpa e inadecuaci&oacute;n materna.',
          'En el seguimiento terap&eacute;utico, readministrar el EPDS cada 2 a 4 semanas permite documentar la respuesta al tratamiento. Una reducci&oacute;n de al menos 5 puntos suele considerarse mejora cl&iacute;nicamente significativa.',
          'En telepsicolog&iacute;a perinatal, el EPDS digital facilita el tamizaje entre sesiones y permite al cl&iacute;nico priorizar casos con puntuaciones elevadas o &iacute;tem 10 positivo.',
        ],
      },
      {
        title: 'Limitaciones',
        paragraphs: [
          'El EPDS no detecta depresi&oacute;n posparto psic&oacute;tica, una condici&oacute;n rara pero grave que requiere evaluaci&oacute;n psiqui&aacute;trica urgente. Ante s&iacute;ntomas psic&oacute;ticos (delirios, alucinaciones), el EPDS no es suficiente.',
          'En poblaciones con bajo nivel educativo, algunos &iacute;tems pueden requerir clarificaci&oacute;n. Se recomienda aplicar el EPDS con apoyo del cl&iacute;nico cuando sea necesario, sin invalidar la autonom&iacute;a de la respuesta.',
          'Los puntos de corte pueden variar seg&uacute;n la poblaci&oacute;n. Estudios en Latinoam&eacute;rica han sugerido que un corte de 10 mantiene buen balance entre sensibilidad y especificidad, pero el cl&iacute;nico debe ajustar seg&uacute;n el contexto.',
          'El EPDS no eval&uacute;a directamente la calidad del v&iacute;nculo materno-infantil ni factores psicosociales como violencia de pareja o apoyo social insuficiente, que son determinantes cr&iacute;ticos de la salud mental perinatal.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'pss-10-escala-estres-percibido',
      filename: 'pss-10-escala-estres-percibido.html',
      title: 'PSS-10: Escala de Estrés Percibido — guía clínica para psicólogos | Kalyo',
      description:
        'Guía del PSS-10: interpretación de puntuaciones, estrés percibido y uso clínico. Escala de estrés disponible digitalmente en Kalyo para psicólogos.',
      keywords: 'PSS-10, estrés percibido, escala estrés, psicología clínica, evaluación estrés, Cohen',
      metaLabel: CLINICAL_META,
      h1: 'PSS-10: Escala de Estr&eacute;s Percibido',
      intro:
        'La Perceived Stress Scale (PSS-10) es un instrumento de diez &iacute;tems desarrollado por Sheldon Cohen y colaboradores para medir el grado en que las situaciones de la vida se perciben como estresantes. A diferencia de inventarios que listan eventos vitales espec&iacute;ficos, el PSS-10 eval&uacute;a la experiencia subjetiva global de estr&eacute;s durante el &uacute;ltimo mes.',
      heroAlt: 'PSS-10 escala de estrés percibido en tablet con interfaz clínica púrpura',
      inlineAlt: 'Gráfico de interpretación PSS-10 escala 0-40, psicología clínica púrpura',
      ctaTitle: 'Aplica el PSS-10 digitalmente en Kalyo',
      ctaText: 'Mide el estr&eacute;s percibido de tus pacientes y visualiza su evoluci&oacute;n con gr&aacute;ficas autom&aacute;ticas en Kalyo.',
      ctaButton: 'Prueba gratis 14 d&iacute;as &rarr;',
      related: [
        ['escala-dass-21', 'DASS-21: Depresi&oacute;n, Ansiedad y Estr&eacute;s'],
        ['que-es-el-gad-7', '&iquest;Qu&eacute; es el GAD-7?'],
        ['inventario-burnout-mbi', 'Inventario de Burnout de Maslach (MBI)'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; es el PSS-10?',
        paragraphs: [
          'El PSS-10 mide el estr&eacute;s percibido como evaluaci&oacute;n global de cu&aacute;n impredecibles, incontrolables y sobrecargadas las personas encuentran sus vidas. No pregunta por eventos estresantes espec&iacute;ficos, sino por la experiencia subjetiva de no poder afrontar las demandas del entorno.',
          'Fue desarrollado en 1983 y la versi&oacute; de 10 &iacute;tems (PSS-10) es la m&aacute;s utilizada por su equilibrio entre brevedad y fiabilidad. Los &iacute;tems incluyen afirmaciones positivas (capacidad de afrontamiento) y negativas (sentirse abrumado), lo que captura tanto la percepci&oacute;n de control como la de desbordamiento.',
          'El PSS-10 ha sido validado en m&uacute;ltiples culturas y est&aacute; disponible en espa&ntilde;ol. Se utiliza en psicolog&iacute;a cl&iacute;nica, medicina, investigaci&oacute;n en salud p&uacute;blica y evaluaciones organizacionales de bienestar laboral.',
          'Su relevancia cl&iacute;nica radica en que el estr&eacute;s percibido act&uacute;a como mediador entre eventos vitales y desenlaces de salud mental y f&iacute;sica. Medir el PSS-10 permite identificar pacientes cuya percepci&oacute;n de estr&eacute;s puede estar contribuyendo a s&iacute;ntomas de ansiedad, depresi&oacute;n o agotamiento.',
        ],
      },
      {
        title: 'C&oacute;mo se aplica',
        paragraphs: [
          'Los diez &iacute;tems del PSS-10 se responden en una escala Likert de cinco puntos (0 = nunca, 4 = muy a menudo), con referencia al &uacute;ltimo mes. Cuatro &iacute;tems est&aacute;n formulados en sentido negativo (2, 4, 5, 10) y seis en sentido positivo (1, 3, 6, 7, 8, 9); los positivos se invierten al puntuar.',
          'El puntaje total var&iacute;a de 0 a 40, donde puntuaciones m&aacute;s altas indican mayor estr&eacute;s percibido. La puntuaci&oacute;n se calcula sumando todos los &iacute;tems despu&eacute;s de invertir los positivos (restar la respuesta de 4). En plataformas digitales como Kalyo, este c&aacute;lculo es autom&aacute;tico.',
          'La administraci&oacute;n tarda aproximadamente tres minutos. Puede aplicarse presencialmente, por escrito o digitalmente. Se recomienda leer las instrucciones en voz alta cuando el paciente tenga dificultades de comprensi&oacute;n.',
          'Para seguimiento longitudinal, aplicar el PSS-10 mensualmente permite detectar cambios en la percepci&oacute;n de estr&eacute;s asociados a intervenciones de manejo del estr&eacute;s, cambios vitales o estacionalidad.',
        ],
      },
      {
        title: 'Interpretaci&oacute;n de puntuaciones',
        paragraphs: [
          'No existen puntos de corte universalmente consensuados para el PSS-10, pero la literatura suele utilizar terciles o cuartiles poblacionales. En la pr&aacute;ctica cl&iacute;nica, puntuaciones superiores a 20 indican estr&eacute;s percibido elevado que merece intervenci&oacute;n.',
          'El PSS-10 se interpreta mejor en combinaci&oacute;n con otras medidas. El <a href="/articulos/escala-dass-21.html">DASS-21</a> diferencia estr&eacute;s, depresi&oacute;n y ansiedad; el <a href="/articulos/que-es-el-gad-7.html">GAD-7</a> eval&uacute;a ansiedad generalizada; y el <a href="/articulos/inventario-burnout-mbi.html">MBI</a> detecta agotamiento profesional en contextos laborales.',
        ],
        extra: `
    <table class="severity-table">
      <thead>
        <tr>
          <th>Puntuaci&oacute;n</th>
          <th>Nivel</th>
          <th>Acci&oacute;n cl&iacute;nica</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="score-badge">0 &ndash; 13</span></td>
          <td><strong>Estr&eacute;s bajo</strong></td>
          <td>Monitoreo; reforzar estrategias de afrontamiento existentes.</td>
        </tr>
        <tr>
          <td><span class="score-badge">14 &ndash; 26</span></td>
          <td><strong>Estr&eacute;s moderado</strong></td>
          <td>Intervenci&oacute;n psicoeducativa; t&eacute;cnicas de relajaci&oacute;n y reestructuraci&oacute;n.</td>
        </tr>
        <tr>
          <td><span class="score-badge">27 &ndash; 40</span></td>
          <td><strong>Estr&eacute;s alto</strong></td>
          <td>Intervenci&oacute;n estructurada; evaluar comorbilidades; considerar derivaci&oacute;n.</td>
        </tr>
      </tbody>
    </table>`,
      },
      {
        title: 'Relaci&oacute;n con burnout, ansiedad y depresi&oacute;n',
        paragraphs: [
          'El estr&eacute;s percibido cr&oacute;nico es un predictor de burnout en profesionales de la salud y otros sectores de alto demanda. Cuando el PSS-10 es elevado en contexto laboral, conviene administrar el <a href="/articulos/inventario-burnout-mbi.html">Inventario de Burnout de Maslach (MBI)</a> para evaluar agotamiento emocional, despersonalizaci&oacute;n y baja realizaci&oacute;n personal.',
          'La relaci&oacute;n entre estr&eacute;s percibido y ansiedad es bidireccional. El <a href="/articulos/que-es-el-gad-7.html">GAD-7</a> complementa al PSS-10 cuando el paciente presenta preocupaci&oacute;n excesiva adem&aacute;s de sensaci&oacute;n general de desbordamiento.',
          'El <a href="/articulos/escala-dass-21.html">DASS-21</a> incluye una subescala de estr&eacute;s con &iacute;tems espec&iacute;ficos (tensi&oacute;n, irritabilidad, dificultad para relajarse) que puede diferenciarse del constructo m&aacute;s global del PSS-10. Usar ambos proporciona una visi&oacute;n m&aacute;s rica del perfil emocional.',
          'En pacientes con estr&eacute;s cr&oacute;nico, evaluar tambi&eacute;n s&iacute;ntomas depresivos es esencial, ya que el estr&eacute;s sostenido es uno de los principales factores de riesgo para episodios depresivos.',
        ],
      },
      {
        title: '&iquest;Cu&aacute;ndo usar el PSS-10?',
        paragraphs: [
          'El PSS-10 es &uacute;til en evaluaci&oacute;n inicial de pacientes con quejas de agobio, irritabilidad o sensaci&oacute;n de p&eacute;rdida de control; seguimiento de intervenciones de manejo del estr&eacute;s; evaluaciones organizacionales de bienestar; investigaci&oacute;n sobre factores psicosociales de salud; y complemento de evaluaciones de burnout o ansiedad.',
          'En psicoterapia, el PSS-10 puede servir como medida de resultado (outcome measure) para documentar cambios en la percepci&oacute;n global de estr&eacute;s a lo largo del tratamiento.',
          'En contextos de telepsicolog&iacute;a, su brevedad lo hace ideal para aplicaciones peri&oacute;dicas entre sesiones, permitiendo al cl&iacute;nico ajustar intervenciones seg&uacute;n la evoluci&oacute;n del estr&eacute;s percibido.',
          'Tambi&eacute;n se recomienda en evaluaciones de pacientes con enfermedades cr&oacute;nicas, donde el estr&eacute;s percibido influye significativamente en la adherencia al tratamiento y la calidad de vida.',
        ],
      },
      {
        title: 'Limitaciones',
        paragraphs: [
          'El PSS-10 mide percepci&oacute;n global de estr&eacute;s, no eventos estresantes espec&iacute;ficos ni estrategias de afrontamiento concretas. Complementarlo con entrevista cl&iacute;nica enriquece la evaluaci&oacute;n.',
          'Los puntos de corte var&iacute;an seg&uacute;n la poblaci&oacute;n de referencia. Baremos locales son preferibles cuando est&aacute;n disponibles.',
          'Como autoinforme, est&aacute; sujeto a sesgos de deseabilidad social y estado de &aacute;nimo moment&aacute;neo. Aplicarlo en un momento de crisis aguda puede inflar transitoriamente la puntuaci&oacute;n.',
          'No eval&uacute;a estr&eacute;s postraum&aacute;tico ni estr&eacute;s asociado a eventos vitales concretos. Para trauma, se requieren instrumentos espec&iacute;ficos como el PCL-5.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'nom-004-historia-clinica-mexico',
      filename: 'nom-004-historia-clinica-mexico.html',
      title: 'NOM-004: Historia Clínica en México — guía para psicólogos | Kalyo',
      description:
        'Guía de la NOM-004-SSA3-2012 para psicólogos: requisitos de historia clínica, expediente y documentación. Cumple la normativa mexicana con Kalyo.',
      keywords: 'NOM-004, historia clínica, psicología México, normativa clínica, expediente clínico, documentación psicólogos',
      metaLabel: NORM_MX,
      h1: 'NOM-004: Historia Cl&iacute;nica en M&eacute;xico',
      intro:
        'La Norma Oficial Mexicana NOM-004-SSA3-2012 establece los criterios m&iacute;nimos para la integraci&oacute;n, uso, manejo y archivo del expediente cl&iacute;nico en M&eacute;xico. Para los psic&oacute;logos que ejercen en el pa&iacute;s, comprender esta normativa es esencial para garantizar la calidad asistencial, la trazabilidad de la atenci&oacute;n y el cumplimiento legal de su pr&aacute;ctica cl&iacute;nica.',
      heroAlt: 'NOM-004 historia clínica en tablet con interfaz clínica púrpura',
      inlineAlt: 'Diagrama de requisitos NOM-004 expediente clínico, normativa México púrpura',
      ctaTitle: 'Cumple la NOM-004 con Kalyo',
      ctaText: 'Gestiona historias cl&iacute;nicas digitales conforme a la NOM-004 con plantillas, firma y almacenamiento seguro.',
      ctaButton: 'Prueba gratis 14 d&iacute;as &rarr;',
      related: [
        ['consentimiento-informado-psicologia', 'Consentimiento Informado en Psicolog&iacute;a'],
        ['como-documentar-sesion-clinica', 'C&oacute;mo Documentar una Sesi&oacute;n Cl&iacute;nica'],
        ['software-para-psicologos-clinicos', 'Software para Psic&oacute;logos Cl&iacute;nicos'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; es la NOM-004?',
        paragraphs: [
          'La NOM-004-SSA3-2012 del expediente cl&iacute;nico fue publicada por la Secretar&iacute;a de Salud de M&eacute;xico y es de observancia obligatoria para todos los establecimientos de atenci&oacute;n m&eacute;dica del Sistema Nacional de Salud, incluyendo consultorios privados de psicolog&iacute;a que formen parte de la red de servicios de salud o que opten por acreditar est&aacute;ndares de calidad.',
          'La norma define el expediente cl&iacute;nico como el conjunto de documentos &uacute;nicos, ordenados y sistematizados que contienen los datos, antecedentes e informaci&oacute;n generada durante la atenci&oacute;n de una persona. Para el psic&oacute;logo, esto incluye la historia cl&iacute;nica psicol&oacute;gica, las notas de evoluci&oacute;n, los resultados de evaluaciones psicom&eacute;tricas y la documentaci&oacute;n de consentimiento informado.',
          'La NOM-004 establece requisitos sobre contenido m&iacute;nimo, formato, confidencialidad, conservaci&oacute;n, acceso y transferencia del expediente. Su cumplimiento protege tanto al paciente como al profesional ante auditor&iacute;as, quejas y procedimientos legales.',
          'Aunque la norma fue dise&ntilde;ada principalmente para la atenci&oacute;n m&eacute;dica, sus principios de documentaci&oacute;n cl&iacute;nica son aplicables y exigibles en la pr&aacute;ctica psicol&oacute;gica, especialmente cuando el psic&oacute;logo trabaja en instituciones de salud o presta servicios a aseguradoras.',
        ],
      },
      {
        title: 'Contenido m&iacute;nimo del expediente cl&iacute;nico',
        paragraphs: [
          'La NOM-004 exige que el expediente cl&iacute;nico contenga, como m&iacute;nimo: datos de identificaci&oacute;n del paciente, motivo de consulta, antecedentes personales y familiares relevantes, exploraci&oacute;n f&iacute;sica o psicol&oacute;gica seg&uacute;n corresponda, diagn&oacute;sticos o impresiones cl&iacute;nicas, plan de tratamiento, evoluci&oacute;n y notas de cada consulta.',
          'Para psic&oacute;logos, la &laquo;exploraci&oacute;n&raquo; equivale a la evaluaci&oacute;n psicol&oacute;gica inicial: entrevista cl&iacute;nica, aplicaci&oacute;n de tests, observaci&oacute;n conductual y formulaci&oacute;n del caso. Los resultados de instrumentos como el PHQ-9, GAD-7 o cualquier test psicom&eacute;trico deben registrarse en el expediente con fecha, puntuaci&oacute;n e interpretaci&oacute;n.',
          'Las notas de evoluci&oacute;n deben documentar cada sesi&oacute;n con fecha, intervenciones realizadas, respuesta del paciente y plan para la siguiente consulta. El formato SOAP es ampliamente recomendado y se describe en detalle en nuestra gu&iacute;a sobre <a href="/articulos/como-documentar-sesion-clinica.html">c&oacute;mo documentar una sesi&oacute;n cl&iacute;nica</a>.',
          'El <a href="/articulos/consentimiento-informado-psicologia.html">consentimiento informado</a> firmado debe formar parte integral del expediente antes de iniciar cualquier intervenci&oacute;n psicol&oacute;gica, conforme a los principios &eacute;ticos y legales de la pr&aacute;ctica cl&iacute;nica en M&eacute;xico.',
        ],
      },
      {
        title: 'Requisitos de conservaci&oacute;n y confidencialidad',
        paragraphs: [
          'La NOM-004 establece que el expediente cl&iacute;nico debe conservarse por un m&iacute;nimo de cinco a&ntilde;os a partir de la &uacute;ltima nota de evoluci&oacute;n, aunque para menores de edad el plazo se extiende hasta que cumplan la mayor&iacute;a de edad m&aacute;s cinco a&ntilde;os adicionales.',
          'La confidencialidad es un principio central: solo el paciente, el personal autorizado del establecimiento y las autoridades sanitarias competentes pueden acceder al expediente. El psic&oacute;logo debe implementar medidas de seguridad f&iacute;sica o digitales para proteger la informaci&oacute;n cl&iacute;nica.',
          'En el contexto digital, la NOM-024-SSA3-2012 complementa a la NOM-004 al regular los sistemas de informaci&oacute;n en salud, incluyendo requisitos de respaldo, trazabilidad, autenticaci&oacute;n y cifrado de datos cl&iacute;nicos electr&oacute;nicos.',
          'El incumplimiento de los requisitos de confidencialidad puede derivar en sanciones administrativas y responsabilidad civil o penal, especialmente en casos de filtraci&oacute;n de informaci&oacute;n sensible de salud mental.',
        ],
      },
      {
        title: 'Historia cl&iacute;nica digital y cumplimiento normativo',
        paragraphs: [
          'La digitalizaci&oacute;n del expediente cl&iacute;nico es cada vez m&aacute;s com&uacute;n en consultorios privados de psicolog&iacute;a en M&eacute;xico. Sin embargo, no basta con usar cualquier aplicaci&oacute;n: el sistema debe cumplir con los requisitos de la NOM-004 y, cuando aplique, la NOM-024 para expedientes electr&oacute;nicos.',
          'Un <a href="/articulos/software-para-psicologos-clinicos.html">software para psic&oacute;logos cl&iacute;nicos</a> adecuado debe ofrecer: plantillas de historia cl&iacute;nica conformes a la normativa, registro de notas de evoluci&oacute;n con fecha y hora, almacenamiento seguro con respaldo, gesti&oacute;n de consentimiento informado, y exportaci&oacute;n del expediente cuando el paciente lo solicite.',
          'Kalyo est&aacute; dise&ntilde;ado para psic&oacute;logos en Latinoam&eacute;rica y facilita el cumplimiento de est&aacute;ndares de documentaci&oacute;n cl&iacute;nica, incluyendo la integraci&oacute;n de evaluaciones psicom&eacute;tricas digitales directamente en el expediente del paciente.',
          'Al migrar de expedientes en papel a digitales, el psic&oacute;logo debe garantizar que los expedientes hist&oacute;ricos se digitalicen con la misma calidad y que se mantenga la cadena de custodia de la informaci&oacute;n cl&iacute;nica.',
        ],
      },
      {
        title: 'Implicaciones pr&aacute;cticas para psic&oacute;logos',
        paragraphs: [
          'Todo psic&oacute;logo que ejerza en M&eacute;xico, ya sea en consulta privada o institucional, debe integrar un expediente cl&iacute;nico para cada paciente desde la primera consulta. La ausencia de documentaci&oacute;n adecuada es una de las principales vulnerabilidades en procedimientos &eacute;ticos y legales.',
          'Se recomienda revisar peri&oacute;dicamente que el expediente contenga todos los elementos exigidos por la NOM-004, especialmente antes de auditor&iacute;as de colegios profesionales o acreditaciones de calidad.',
          'La documentaci&oacute;n no es un tr&aacute;mite burocr&aacute;tico: es una herramienta cl&iacute;nica que permite continuidad de la atenci&oacute;n, evaluaci&oacute;n de la efectividad del tratamiento y protecci&oacute;n legal del profesional y del paciente.',
          'Ante la transferencia de un paciente a otro profesional, la NOM-004 regula el procedimiento de entrega del expediente o de un resumen cl&iacute;nico, siempre con autorizaci&oacute;n del paciente y preservando la confidencialidad.',
        ],
      },
      {
        title: 'Limitaciones y consideraciones adicionales',
        paragraphs: [
          'La NOM-004 fue dise&ntilde;ada con un enfoque m&eacute;dico-biol&oacute;gico. Algunos requisitos (como exploraci&oacute;n f&iacute;sica) deben adaptarse al contexto psicol&oacute;gico sin perder el esp&iacute;ritu de la norma: documentar de forma completa, ordenada y trazable la atenci&oacute;n prestada.',
          'La normativa no especifica formatos detallados para la pr&aacute;ctica psicol&oacute;gica, lo que genera variabilidad entre profesionales. Los colegios de psic&oacute;logos y las asociaciones profesionales emiten gu&iacute;as complementarias que conviene consultar.',
          'La NOM-004 no aborda directamente la telepsicolog&iacute;a ni el almacenamiento en la nube, temas que requieren considerar tambi&eacute;n la NOM-024 y la Ley Federal de Protecci&oacute;n de Datos Personales (LFPDPPP).',
          'Mantenerse actualizado sobre reformas normativas es responsabilidad del profesional. Las plataformas digitales especializadas, como Kalyo, actualizan sus plantillas conforme evolucionan los est&aacute;ndares de documentaci&oacute;n cl&iacute;nica en la regi&oacute;n.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'ley-1090-psicologia-colombia',
      filename: 'ley-1090-psicologia-colombia.html',
      title: 'Ley 1090 de 2006: Psicología en Colombia — guía para profesionales | Kalyo',
      description:
        'Guía de la Ley 1090 de 2006 para psicólogos en Colombia: ejercicio profesional, ética, competencias y deberes. Cumple la normativa con Kalyo.',
      keywords: 'Ley 1090, psicología Colombia, ejercicio profesional, ética psicólogos, normativa Colombia',
      metaLabel: NORM_CO,
      h1: 'Ley 1090 de 2006: Marco Legal de la Psicolog&iacute;a en Colombia',
      intro:
        'La Ley 1090 de 2006 es la norma que regula el ejercicio profesional de la psicolog&iacute;a en Colombia. Establece los requisitos para el ejercicio, los deberes y derechos de los psic&oacute;logos, el r&eacute;gimen sancionatorio y las competencias profesionales. Todo psic&oacute;logo colombiano debe conocer esta ley para ejercer de forma legal, &eacute;tica y competente.',
      heroAlt: 'Ley 1090 psicología Colombia en tablet con interfaz clínica púrpura',
      inlineAlt: 'Diagrama marco legal Ley 1090 psicología Colombia púrpura',
      ctaTitle: 'Ejerce con respaldo legal en Kalyo',
      ctaText: 'Documenta tu pr&aacute;ctica conforme a la Ley 1090 con historias cl&iacute;nicas, consentimiento y evaluaciones digitales.',
      ctaButton: 'Prueba gratis 14 d&iacute;as &rarr;',
      related: [
        ['consentimiento-informado-psicologia', 'Consentimiento Informado en Psicolog&iacute;a'],
        ['como-documentar-sesion-clinica', 'C&oacute;mo Documentar una Sesi&oacute;n Cl&iacute;nica'],
        ['evaluacion-riesgo-suicida', 'Evaluaci&oacute;n de Riesgo Suicida'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; establece la Ley 1090?',
        paragraphs: [
          'La Ley 1090 de 2006, reglamentada parcialmente por el Decreto 1047 de 2014, define la psicolog&iacute;a como una disciplina cient&iacute;fica y profesi&oacute;n con responsabilidad social. Regula qui&eacute;n puede ejercer la profesi&oacute;n (titulados con tarjeta profesional vigente), d&oacute;nde puede ejercerse y bajo qu&eacute; condiciones &eacute;ticas y legales.',
          'La ley crea el marco para las competencias profesionales del psic&oacute;logo colombiano, organizadas en &aacute;mbitos como evaluaci&oacute;n e intervenci&oacute;n psicol&oacute;gica, investigaci&oacute;n, docencia, consultor&iacute;a y administraci&oacute;n. Cada psic&oacute;logo debe ejercer dentro de sus competencias declaradas y acreditadas.',
          'Establece el deber de mantener actualizaci&oacute;n profesional continua, respetar la dignidad y autonom&iacute;a de las personas atendidas, garantizar la confidencialidad de la informaci&oacute;n y actuar con integridad en todas las relaciones profesionales.',
          'El incumplimiento de la Ley 1090 puede derivar en procesos &eacute;tico-profesionales ante los colegios de psic&oacute;logos y sanciones que van desde amonestaciones hasta la suspensi&oacute;n del ejercicio profesional.',
        ],
      },
      {
        title: 'Deberes del psic&oacute;logo seg&uacute;n la Ley 1090',
        paragraphs: [
          'Entre los deberes fundamentales se encuentran: obtener el consentimiento informado antes de cualquier evaluaci&oacute;n o intervenci&oacute;n, documentar adecuadamente la atenci&oacute;n prestada, mantener la confidencialidad de la informaci&oacute;n (salvo excepciones legales como riesgo suicida), derivar al paciente cuando el caso exceda las competencias del profesional, y reportar situaciones de abuso o violencia seg&uacute;n la ley.',
          'El deber de documentaci&oacute;n est&aacute; estrechamente vinculado con la pr&aacute;ctica cl&iacute;nica responsable. Nuestra gu&iacute;a sobre <a href="/articulos/como-documentar-sesion-clinica.html">c&oacute;mo documentar una sesi&oacute;n cl&iacute;nica</a> ofrece formatos pr&aacute;cticos alineados con estos requisitos.',
          'El <a href="/articulos/consentimiento-informado-psicologia.html">consentimiento informado</a> no es opcional: la Ley 1090 y el C&oacute;digo Deontol&oacute;gico y Bio&eacute;tico exigen que el paciente conozca los objetivos, procedimientos, riesgos y beneficios de la intervenci&oacute;n psicol&oacute;gica antes de aceptarla.',
          'En situaciones de riesgo suicida, la ley y la bio&eacute;tica permiten (y en ocasiones exigen) romper la confidencialidad para proteger la vida del paciente. Los protocolos de <a href="/articulos/evaluacion-riesgo-suicida.html">evaluaci&oacute;n de riesgo suicida</a> deben formar parte de la competencia cl&iacute;nica de todo psic&oacute;logo.',
        ],
      },
      {
        title: 'Competencias profesionales y l&iacute;mites del ejercicio',
        paragraphs: [
          'La Ley 1090 define competencias espec&iacute;ficas para la evaluaci&oacute;n psicol&oacute;gica, que incluyen seleccionar instrumentos validados, administrarlos correctamente, interpretar resultados dentro de baremos apropiados y comunicar hallazgos de forma comprensible al paciente y, cuando corresponda, a otros profesionales.',
          'El psic&oacute;logo no puede emitir diagn&uacute;sticos m&eacute;dicos ni prescribir medicamentos. Cuando identifica sintomatolog&iacute;a que sugiere un trastorno que requiere evaluaci&oacute;n psiqui&aacute;trica, debe derivar oportunamente.',
          'La evaluaci&oacute;n psicol&oacute;gica con fines laborales, forenses o educativos requiere competencias adicionales y, en algunos casos, certificaciones espec&iacute;ficas. Ejercer fuera del &aacute;mbito de competencia es una falta &eacute;tica sancionable.',
          'La ley tambi&eacute;n regula la publicidad de servicios psicol&oacute;gicos, prohibiendo promesas de curaci&oacute;n, denigraci&oacute;n de colegas y uso de t&iacute;tulos o especializaciones no acreditadas.',
        ],
      },
      {
        title: 'R&eacute;gimen sancionatorio y colegios profesionales',
        paragraphs: [
          'Los Colegios Colombianos de Psic&oacute;logos son las entidades encargadas de vigilar el cumplimiento de la Ley 1090 y del C&oacute;digo Deontol&oacute;gico. Pueden iniciar procesos &eacute;tico-profesionales ante quejas de pacientes, colegas o autoridades.',
          'Las sanciones incluyen amonestaciones privadas o p&uacute;blicas, multas, suspensi&oacute;n temporal del ejercicio y cancelaci&oacute;n de la tarjeta profesional en casos graves de incompetencia, negligencia o conducta contraria a la &eacute;tica.',
          'La afiliaci&oacute;n al colegio profesional es obligatoria para ejercer la psicolog&iacute;a en Colombia. Adem&aacute;s de la vigilancia &eacute;tica, los colegios ofrecen formaci&oacute;n continua, asesor&iacute;a legal y representaci&oacute;n gremial.',
          'Ante un procedimiento sancionatorio, contar con documentaci&oacute;n cl&iacute;nica completa y consentimientos firmados es la principal defensa del psic&oacute;logo que ha actuado conforme a la ley y a la buena pr&aacute;ctica cl&iacute;nica.',
        ],
      },
      {
        title: 'Implicaciones para la pr&aacute;ctica cl&iacute;nica digital',
        paragraphs: [
          'La Ley 1090 no fue redactada pensando en la telepsicolog&iacute;a, pero sus principios son plenamente aplicables al ejercicio digital. El consentimiento informado debe incluir los riesgos y beneficios de la atenci&oacute;n a distancia, y la documentaci&oacute;n cl&iacute;nica debe mantener los mismos est&aacute;ndares de calidad.',
          'La confidencialidad en plataformas digitales requiere medidas adicionales: conexiones cifradas, almacenamiento seguro, pol&iacute;ticas de acceso y cumplimiento de la Ley 1581 de 2012 de protecci&oacute;n de datos personales.',
          'Kalyo facilita el cumplimiento de los deberes de documentaci&oacute;n y consentimiento establecidos por la Ley 1090, permitiendo al psic&oacute;logo colombiano ejercer con respaldo legal en entornos presenciales y digitales.',
          'Los psic&oacute;logos que trabajan con aseguradoras o instituciones de salud en Colombia deben adem&aacute;s cumplir con la Resoluci&oacute;n 1888 de salud mental y los requisitos de reporte del sistema RIPS.',
        ],
      },
      {
        title: 'Limitaciones y actualizaciones normativas',
        paragraphs: [
          'La Ley 1090 requiere actualizaci&oacute;n para abordar expl&iacute;citamente la telepsicolog&iacute;a, la inteligencia artificial en evaluaci&oacute;n psicol&oacute;gica y las nuevas modalidades de intervenci&oacute;n digital. Proyectos de ley en discusi&oacute;n buscan llenar estos vac&iacute;os.',
          'La ley establece principios generales pero no detalla formatos espec&iacute;ficos de historia cl&iacute;nica. Los psic&oacute;logos deben complementar su conocimiento con resoluciones del Ministerio de Salud y gu&iacute;as de los colegios profesionales.',
          'En casos de conflicto entre la Ley 1090 y normas m&aacute;s espec&iacute;ficas (como la Resoluci&oacute;n 1888 para salud mental), prevalece la norma especial, siempre respetando los principios &eacute;ticos fundamentales de la profesi&oacute;n.',
          'Mantenerse informado sobre reformas legales y participar en la formaci&oacute;n continua ofrecida por colegios y asociaciones profesionales es un deber impl&iacute;cito de todo psic&oacute;logo colombiano comprometido con la calidad de la atenci&oacute;n.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'rips-registros-individuales-colombia',
      filename: 'rips-registros-individuales-colombia.html',
      title: 'RIPS en Colombia: Registros Individuales de Prestación de Servicios | Kalyo',
      description:
        'Guía de RIPS para psicólogos en Colombia: consultas, procedimientos y facturación en salud. Cumple los requisitos de reporte con Kalyo.',
      keywords: 'RIPS, Colombia, psicología clínica, facturación salud, registros prestación servicios, normativa Colombia',
      metaLabel: NORM_CO,
      h1: 'RIPS: Registros Individuales de Prestaci&oacute;n de Servicios en Colombia',
      intro:
        'Los Registros Individuales de Prestaci&oacute;n de Servicios de Salud (RIPS) son el sistema est&aacute;ndar de reporte de actividades en el sector salud colombiano. Para psic&oacute;logos que prestan servicios a trav&eacute;s de EPS, IPS o de forma privada con facturaci&oacute;n a aseguradoras, comprender y generar correctamente los RIPS es indispensable para el reconocimiento de servicios y el cumplimiento normativo.',
      heroAlt: 'RIPS registros prestación servicios en tablet con interfaz clínica púrpura',
      inlineAlt: 'Diagrama estructura RIPS Colombia psicología clínica púrpura',
      ctaTitle: 'Gestiona RIPS y consulta en Kalyo',
      ctaText: 'Integra documentaci&oacute;n cl&iacute;nica y c&oacute;digos de consulta psicol&oacute;gica en una plataforma dise&ntilde;ada para psic&oacute;logos en Colombia.',
      ctaButton: 'Prueba gratis 14 d&iacute;as &rarr;',
      related: [
        ['evaluacion-psicologica-colombia-mexico', 'Evaluaci&oacute;n Psicol&oacute;gica en Colombia y M&eacute;xico'],
        ['como-documentar-sesion-clinica', 'C&oacute;mo Documentar una Sesi&oacute;n Cl&iacute;nica'],
        ['software-para-psicologos-clinicos', 'Software para Psic&oacute;logos Cl&iacute;nicos'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; son los RIPS?',
        paragraphs: [
          'Los RIPS son un conjunto de registros estandarizados que documentan las actividades de prestaci&oacute;n de servicios de salud en Colombia. Fueron establecidos por el Ministerio de Salud y Protecci&oacute;n Social para garantizar la trazabilidad de la atenci&oacute;n, facilitar la auditor&iacute;a y permitir la facturaci&oacute;n de servicios ante EPS y aseguradoras.',
          'El sistema RIPS comprende varios archivos planos: consultas (AC), procedimientos (AP), medicamentos (AM), hospitalizaci&oacute;n (AH), reci&eacute;n nacidos (AN), urgencias (AU) y otros. Para psic&oacute;logos, los m&aacute;s relevantes son el registro de consultas (AC) y, cuando aplique, el de procedimientos (AP) para evaluaciones psicol&oacute;gicas.',
          'Cada registro contiene campos obligatorios como tipo de documento del paciente, n&uacute;mero de identificaci&oacute;n, c&oacute;digo del servicio (CUPS), diagn&oacute;stico (CIE-10), valor del servicio y datos del profesional que presta la atenci&oacute;n.',
          'La correcta generaci&oacute;n de RIPS es condici&oacute;n para la glosa y el pago de servicios prestados a trav&eacute;s del sistema de salud colombiano.',
        ],
      },
      {
        title: 'RIPS para consulta psicol&oacute;gica',
        paragraphs: [
          'La consulta psicol&oacute;gica se registra en el archivo AC (Consultas) con el c&oacute;digo CUPS correspondiente. Los c&oacute;digos m&aacute;s utilizados incluyen la consulta de primera vez por psicolog&iacute;a (890208) y consulta de control o seguimiento (890308), aunque pueden variar seg&uacute;n el manual tarifario de cada aseguradora.',
          'Cada registro de consulta debe incluir el diagn&oacute;stico principal en c&oacute;digo CIE-10. Para psicolog&iacute;a cl&iacute;nica, los diagn&oacute;sticos m&aacute;s frecuentes incluyen c&oacute;digos de la categor&iacute;a F (trastornos mentales y del comportamiento), como F32 (episodio depresivo), F41 (otros trastornos de ansiedad) o F43 (reacciones al estr&eacute;s grave).',
          'La documentaci&oacute;n cl&iacute;nica que respalda cada registro RIPS debe estar completa en la historia cl&iacute;nica del paciente. Nuestra gu&iacute;a de <a href="/articulos/como-documentar-sesion-clinica.html">documentaci&oacute;n de sesiones cl&iacute;nicas</a> describe formatos alineados con estos requisitos.',
          'Errores comunes en RIPS incluyen c&oacute;digos CUPS incorrectos, diagn&oacute;sticos CIE-10 que no corresponden a la atenci&oacute;n prestada, duplicidad de registros y discrepancias entre la factura y los RIPS reportados.',
        ],
      },
      {
        title: 'Evaluaciones psicol&oacute;gicas y procedimientos',
        paragraphs: [
          'Las evaluaciones psicol&oacute;gicas con tests estandarizados pueden registrarse como procedimientos (AP) con c&oacute;digos CUPS espec&iacute;ficos para evaluaci&oacute;n psicol&oacute;gica. Es fundamental que el informe de evaluaci&oacute;n forme parte del expediente cl&iacute;nico y respalde el procedimiento facturado.',
          'La gu&iacute;a de <a href="/articulos/evaluacion-psicologica-colombia-mexico.html">evaluaci&oacute;n psicol&oacute;gica en Colombia y M&eacute;xico</a> detalla los est&aacute;ndares de calidad para la aplicaci&oacute;n e interpretaci&oacute;n de tests en el contexto latinoamericano.',
          'Algunas EPS requieren autorizaci&oacute;n previa para ciertos procedimientos de evaluaci&oacute;n psicol&oacute;gica. El psic&oacute;logo debe verificar los requisitos de cada aseguradora antes de prestar el servicio.',
          'La Resoluci&oacute;n 1888 de salud mental establece criterios adicionales para la atenci&oacute;n en salud mental que complementan los requisitos de reporte RIPS.',
        ],
      },
      {
        title: 'Facturaci&oacute;n electr&oacute;nica y validaci&oacute;n',
        paragraphs: [
          'Desde la implementaci&oacute;n de la facturaci&oacute;n electr&oacute;nica en salud (Resoluci&oacute;n 2275 de 2023 y normas complementarias), los RIPS se env&iacute;an junto con la factura electr&oacute;nica al Ministerio de Salud para validaci&oacute;n. El sistema verifica la coherencia entre los servicios facturados y los registros reportados.',
          'Los rechazos por inconsistencias en RIPS son una de las principales causas de glosas (negaci&oacute;n de pago) en servicios de salud mental. Mantener registros precisos y actualizados reduce significativamente este riesgo.',
          'Un <a href="/articulos/software-para-psicologos-clinicos.html">software cl&iacute;nico adecuado</a> puede automatizar la generaci&oacute;n de c&oacute;digos CUPS, vincular diagn&oacute;sticos CIE-10 con las sesiones documentadas y exportar archivos RIPS conformes.',
          'Los psic&oacute;logos en consulta privada que no facturan a EPS tambi&eacute;n se benefician de mantener registros organizados, especialmente si en el futuro incorporan convenios con aseguradoras.',
        ],
      },
      {
        title: 'Buenas pr&aacute;cticas para psic&oacute;logos',
        paragraphs: [
          'Registre cada consulta el mismo d&iacute;a de la atenci&oacute;n, con el c&oacute;digo CUPS y diagn&oacute;stico CIE-10 correctos. La demora en el registro aumenta errores y riesgo de glosas.',
          'Mantenga la historia cl&iacute;nica actualizada como respaldo de cada registro RIPS. En auditor&iacute;as, la EPS puede solicitar el expediente completo para verificar que el servicio facturado fue efectivamente prestado.',
          'Capac&iacute;tese peri&oacute;dicamente sobre actualizaciones en c&oacute;digos CUPS, CIE-10 y normativa de facturaci&oacute;n electr&oacute;nica. El Ministerio de Salud publica resoluciones frecuentes que modifican requisitos.',
          'Considere integrar la gesti&oacute;n cl&iacute;nica y administrativa en una sola plataforma para reducir la carga burocr&aacute;tica y minimizar errores de transcripci&oacute;n entre la nota cl&iacute;nica y el registro RIPS.',
        ],
      },
      {
        title: 'Limitaciones y perspectiva futura',
        paragraphs: [
          'El sistema RIPS fue dise&ntilde;ado con un enfoque m&eacute;dico-asistencial que no siempre captura la riqueza de la intervenci&oacute;n psicol&oacute;gica. Una sesi&oacute;n de psicoterapia se registra igual que una consulta m&eacute;dica breve, lo que puede subestimar la complejidad del servicio prestado.',
          'La transici&oacute;n hacia la facturaci&oacute;n electr&oacute;nica y los nuevos modelos de pago por valor agregado en salud mental plantean desaf&iacute;os para documentar resultados terap&eacute;uticos vinculados a la facturaci&oacute;n.',
          'Los psic&oacute;logos que solo atienden en consulta privada directa (sin EPS) no est&aacute;n obligados a generar RIPS, pero deben mantener registros de atenci&oacute;n conforme a la Ley 1090 y est&aacute;ndares de documentaci&oacute;n cl&iacute;nica.',
          'La digitalizaci&oacute;n progresiva del sistema de salud colombiano favorece plataformas integradas que conecten documentaci&oacute;n cl&iacute;nica, evaluaciones psicom&eacute;tricas y generaci&oacute;n de reportes administrativos.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'ley-1581-proteccion-datos-psicologia',
      filename: 'ley-1581-proteccion-datos-psicologia.html',
      title: 'Ley 1581: Protección de Datos en Psicología — guía Colombia | Kalyo',
      description:
        'Guía de la Ley 1581 de 2012 para psicólogos: datos sensibles, consentimiento, Habeas Data y confidencialidad clínica. Protege a tus pacientes con Kalyo.',
      keywords: 'Ley 1581, protección datos, Habeas Data, psicología Colombia, datos sensibles, confidencialidad clínica',
      metaLabel: NORM_CO,
      h1: 'Ley 1581: Protecci&oacute;n de Datos Personales en Psicolog&iacute;a',
      intro:
        'La Ley 1581 de 2012 y el Decreto 1377 de 2013 establecen el r&eacute;gimen general de protecci&oacute;n de datos personales en Colombia. Para psic&oacute;logos, que manejan datos especialmente sensibles (salud mental, historias cl&iacute;nicas, resultados de tests), el cumplimiento de esta normativa es tanto una obligaci&oacute;n legal como un imperativo &eacute;tico fundamental.',
      heroAlt: 'Ley 1581 protección de datos en tablet con interfaz clínica púrpura',
      inlineAlt: 'Diagrama Ley 1581 datos sensibles psicología clínica púrpura',
      ctaTitle: 'Protege los datos de tus pacientes con Kalyo',
      ctaText: 'Plataforma con cifrado, control de acceso y pol&iacute;ticas de privacidad alineadas con la Ley 1581 de Colombia.',
      ctaButton: 'Prueba gratis 14 d&iacute;as &rarr;',
      related: [
        ['consentimiento-informado-psicologia', 'Consentimiento Informado en Psicolog&iacute;a'],
        ['como-documentar-sesion-clinica', 'C&oacute;mo Documentar una Sesi&oacute;n Cl&iacute;nica'],
        ['ley-1090-psicologia-colombia', 'Ley 1090: Psicolog&iacute;a en Colombia'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; es la Ley 1581?',
        paragraphs: [
          'La Ley 1581 de 2012 regula el tratamiento de datos personales en Colombia, garantizando el derecho fundamental de las personas a conocer, actualizar, rectificar y suprimir la informaci&oacute;n que sobre ellas reposa en bases de datos. Establece principios de legalidad, finalidad, libertad, veracidad, transparencia, acceso y circulaci&oacute;n restringida, seguridad y confidencialidad.',
          'Los datos de salud mental son considerados datos sensibles seg&uacute;n la ley, lo que implica requisitos reforzados para su tratamiento: se requiere autorizaci&oacute;n expl&iacute;cita del titular (paciente), medidas de seguridad adicionales y restricciones sobre la finalidad del uso.',
          'El psic&oacute;logo act&uacute;a como responsable del tratamiento de datos personales cuando administra historias cl&iacute;nicas, resultados de evaluaciones y notas de sesi&oacute;n. Si utiliza plataformas digitales, debe verificar que el proveedor cumpla tambi&eacute;n con la normativa como encargado del tratamiento.',
          'El incumplimiento puede derivar en sanciones de la Superintendencia de Industria y Comercio (SIC), incluyendo multas, suspensi&oacute;n de la base de datos y responsabilidad civil por da&ntilde;os a los titulares.',
        ],
      },
      {
        title: 'Datos sensibles en la pr&aacute;ctica psicol&oacute;gica',
        paragraphs: [
          'En psicolog&iacute;a cl&iacute;nica se tratan datos sensibles de forma rutinaria: diagn&oacute;sticos, historias de abuso, ideaci&oacute;n suicida, orientaci&oacute;n sexual, creencias religiosas y resultados de tests psicom&eacute;tricos. Todos requieren protecci&oacute;n reforzada bajo la Ley 1581.',
          'La autorizaci&oacute;n para el tratamiento de datos sensibles debe ser previa, expresa e informada. El <a href="/articulos/consentimiento-informado-psicologia.html">consentimiento informado</a> cl&iacute;nico y la autorizaci&oacute;n de datos personales pueden integrarse en un solo documento, pero deben cubrir ambas dimensiones: la intervenci&oacute;n terap&eacute;utica y el tratamiento de la informaci&oacute;n.',
          'El principio de finalidad exige que los datos solo se utilicen para los fines para los cuales fueron recolectados. Usar informaci&oacute;n cl&iacute;nica con fines de investigaci&oacute;n, docencia o publicaci&oacute;n requiere autorizaci&oacute;n adicional y, en investigaci&oacute;n, anonimizaci&oacute;n adecuada.',
          'La documentaci&oacute;n cl&iacute;nica detallada en nuestra gu&iacute;a de <a href="/articulos/como-documentar-sesion-clinica.html">c&oacute;mo documentar sesiones</a> debe almacenarse en sistemas que garanticen confidencialidad conforme a la Ley 1581.',
        ],
      },
      {
        title: 'Derechos del paciente (Habeas Data)',
        paragraphs: [
          'Los pacientes tienen derecho a conocer qu&eacute; datos personales tiene el psic&oacute;logo sobre ellos, solicitar prueba de la autorizaci&oacute;n otorgada, ser informados sobre el uso dado a sus datos, presentar quejas ante la SIC, revocar la autorizaci&oacute;n y solicitar supresi&oacute;n cuando no exista deber legal de conservaci&oacute;n.',
          'El psic&oacute;logo debe establecer canales para atender solicitudes de Habeas Data (consulta, actualizaci&oacute;n, rectificaci&oacute;n y supresi&oacute;n) y responder dentro de los plazos legales (m&aacute;ximo 10 d&iacute;as h&aacute;biles para consultas, 15 para reclamos).',
          'La revocaci&oacute;n de autorizaci&oacute;n para tratamiento de datos no implica necesariamente la terminaci&oacute;n del proceso terap&eacute;utico, pero s&iacute; obliga al psic&oacute;logo a evaluar c&oacute;mo continuar la atenci&oacute;n sin tratar datos adicionales o proceder al cierre del caso.',
          'Existen excepciones a la supresi&oacute;n: cuando exista deber legal de conservaci&oacute;n (historia cl&iacute;nica por plazos m&iacute;nimos), mandato judicial o de autoridad competente, o cuando los datos sean necesarios para defensa en procesos judiciales.',
        ],
      },
      {
        title: 'Medidas de seguridad en consultorios y plataformas digitales',
        paragraphs: [
          'La Ley 1581 exige implementar medidas t&eacute;cnicas, humanas y administrativas para proteger los datos personales. En consultorio f&iacute;sico: archivos bajo llave, acceso restringido, destrucci&oacute;n segura de documentos obsoletos y pol&iacute;ticas de acceso para personal administrativo.',
          'En entornos digitales: contrase&ntilde;as robustas, autenticaci&oacute;n de dos factores, cifrado de datos en tr&aacute;nsito y en reposo, respaldos cifrados, pol&iacute;ticas de acceso por roles y registros de auditor&iacute;a de accesos a la informaci&oacute;n cl&iacute;nica.',
          'Al seleccionar una plataforma de gesti&oacute;n cl&iacute;nica, verifique que el proveedor tenga pol&iacute;tica de privacidad clara, acuerdo de tratamiento de datos (como encargado), servidores seguros y cumplimiento de la <a href="/articulos/ley-1090-psicologia-colombia.html">Ley 1090</a> y normativa de salud.',
          'La telepsicolog&iacute;a a&ntilde;ade riesgos adicionales: conexiones no cifradas, plataformas de videollamada generales (no dise&ntilde;adas para salud) y almacenamiento local en dispositivos personales. El psic&oacute;logo es responsable de evaluar y mitigar estos riesgos.',
        ],
      },
      {
        title: 'Pol&iacute;tica de tratamiento de datos para psic&oacute;logos',
        paragraphs: [
          'Todo responsable del tratamiento de datos personales debe registrar su base de datos ante el Registro Nacional de Bases de Datos (RNBD) de la SIC y disponer de una pol&iacute;tica de tratamiento de datos accesible al p&uacute;blico.',
          'La pol&iacute;tica debe describir: identificaci&oacute;n del responsable, finalidad del tratamiento, derechos de los titulares, procedimiento para ejercer derechos, fecha de vigencia y medidas de seguridad implementadas.',
          'Para psic&oacute;logos en consulta privada, la pol&iacute;tica puede publicarse en el sitio web del consultorio o entregarse f&iacute;sicamente al paciente. Debe actualizarse cuando cambien las finalidades o medidas de seguridad.',
          'El registro en el RNBD es gratuito y se realiza en l&iacute;nea. Omitir este registro es una infracci&oacute;n sancionable, aunque muchos psic&oacute;logos en consulta privada a&uacute;n desconocen esta obligaci&oacute;n.',
        ],
      },
      {
        title: 'Limitaciones y relaci&oacute;n con otras normas',
        paragraphs: [
          'La Ley 1581 convive con normas sectoriales de salud que establecen plazos de conservaci&oacute;n de historias cl&iacute;nicas m&aacute;s largos que los plazos generales de retenci&oacute;n de datos. En caso de conflicto, prevalecen las normas especiales del sector salud.',
          'La ley no regula espec&iacute;ficamente la transferencia internacional de datos (pacientes en telepsicolog&iacute;a transfronteriza). Se aplican principios generales de autorizaci&oacute;n y medidas de seguridad reforzadas.',
          'El secreto profesional &eacute;tico del psic&oacute;logo (Ley 1090) complementa pero no sustituye las obligaciones de la Ley 1581. Ambos marcos deben cumplirse simult&aacute;neamente.',
          'Ante una filtraci&oacute;n de datos cl&iacute;nicos, el psic&oacute;logo debe notificar a la SIC y a los titulares afectados, implementar medidas correctivas y documentar el incidente. Contar con plataformas seguras reduce dr&aacute;sticamente este riesgo.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'sivigila-psicologia-colombia',
      filename: 'sivigila-psicologia-colombia.html',
      title: 'SIVIGILA y Psicología en Colombia: notificación de eventos de salud pública | Kalyo',
      description:
        'Guía de SIVIGILA para psicólogos en Colombia: eventos de salud mental, violencia, suicidio y notificación obligatoria. Protocolos clínicos en Kalyo.',
      keywords: 'SIVIGILA, salud pública Colombia, psicología clínica, notificación obligatoria, salud mental, vigilancia epidemiológica',
      metaLabel: NORM_CO,
      h1: 'SIVIGILA: Vigilancia en Salud P&uacute;blica y Psicolog&iacute;a en Colombia',
      intro:
        'El Sistema Nacional de Vigilancia en Salud P&uacute;blica (SIVIGILA) es la plataforma de Colombia para la detecci&oacute;n, notificaci&oacute;n y seguimiento de eventos de inter&eacute;s en salud p&uacute;blica. Los psic&oacute;logos que detectan eventos como intento de suicidio, violencia intrafamiliar o trastornos mentales de notificaci&oacute;n obligatoria deben conocer sus responsabilidades dentro de este sistema.',
      heroAlt: 'SIVIGILA vigilancia salud pública en tablet con interfaz clínica púrpura',
      inlineAlt: 'Diagrama SIVIGILA eventos salud mental Colombia púrpura',
      ctaTitle: 'Documenta y reporta con respaldo cl&iacute;nico en Kalyo',
      ctaText: 'Registra evaluaciones de riesgo y eventos cl&iacute;nicos con trazabilidad conforme a protocolos de salud p&uacute;blica.',
      ctaButton: 'Prueba gratis 14 d&iacute;as &rarr;',
      related: [
        ['evaluacion-riesgo-suicida', 'Evaluaci&oacute;n de Riesgo Suicida'],
        ['ley-1090-psicologia-colombia', 'Ley 1090: Psicolog&iacute;a en Colombia'],
        ['como-documentar-sesion-clinica', 'C&oacute;mo Documentar una Sesi&oacute;n Cl&iacute;nica'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; es SIVIGILA?',
        paragraphs: [
          'SIVIGILA es el sistema oficial de vigilancia epidemiol&oacute;gica de Colombia, operado por el Instituto Nacional de Salud (INS) y las Secretar&iacute;as de Salud departamentales y municipales. Recopila informaci&oacute;n sobre eventos de salud p&uacute;blica para detectar brotes, tendencias y orientar pol&iacute;ticas de prevenci&oacute;n.',
          'El sistema clasifica eventos en dos grupos: eventos de notificaci&oacute;n inmediata (dentro de las 24 horas siguientes al diagn&oacute;stico) y eventos de notificaci&oacute;n rutinaria (semanal). Para psicolog&iacute;a cl&iacute;nica, los eventos m&aacute;s relevantes incluyen intento de suicidio, violencia de g&eacute;nero, maltrato infantil y ciertos trastornos mentales.',
          'La notificaci&oacute;n en SIVIGILA no es responsabilidad exclusiva del m&eacute;dico: cualquier profesional de salud que detecte un evento de notificaci&oacute;n obligatoria debe reportarlo a trav&eacute;s de los canales establecidos por su IPS o directamente a la Secretar&iacute;a de Salud local.',
          'El incumplimiento de la notificaci&oacute;n puede derivar en sanciones administrativas y, en casos graves, responsabilidad por omisi&oacute;n de denuncia de eventos que representan riesgo para la vida o la integridad de las personas.',
        ],
      },
      {
        title: 'Eventos de salud mental de notificaci&oacute;n obligatoria',
        paragraphs: [
          'Entre los eventos de salud mental de notificaci&oacute;n en SIVIGILA se incluyen: intento de suicidio (notificaci&oacute;n inmediata), lesiones por causa externa incluyendo violencia interpersonal, maltrato infantil y violencia de g&eacute;nero. La lista se actualiza peri&oacute;dicamente por el Ministerio de Salud.',
          'Cuando un psic&oacute;logo detecta ideaci&oacute;n suicida activa con plan o intento reciente, debe activar simult&aacute;neamente el protocolo cl&iacute;nico de <a href="/articulos/evaluacion-riesgo-suicida.html">evaluaci&oacute;n de riesgo suicida</a> y el procedimiento de notificaci&oacute;n a SIVIGILA a trav&eacute;s de su instituci&oacute;n.',
          'La notificaci&oacute;n epidemiol&oacute;gica no viola el secreto profesional cuando est&aacute; mandatada por ley. Sin embargo, el psic&oacute;logo debe informar al paciente sobre la obligaci&oacute;n legal de reporte cuando sea cl&iacute;nicamente apropiado, sin comprometer la seguridad.',
          'En consulta privada, el psic&oacute;logo debe conocer el canal de notificaci&oacute;n de su municipio o departamento. Muchas Secretar&iacute;as de Salud ofrecen formularios en l&iacute;nea o l&iacute;neas telef&oacute;nicas para reporte de eventos.',
        ],
      },
      {
        title: 'Protocolo de actuaci&oacute;n del psic&oacute;logo',
        paragraphs: [
          'Ante un evento de notificaci&oacute;n obligatoria, el psic&oacute;logo debe: (1) garantizar la seguridad inmediata del paciente, (2) documentar la evaluaci&oacute;n cl&iacute;nica completa, (3) notificar al sistema de salud seg&uacute;n protocolo institucional o municipal, (4) coordinar con la red de apoyo del paciente.',
          'La documentaci&oacute;n debe ser exhaustiva y oportuna. Nuestra gu&iacute;a de <a href="/articulos/como-documentar-sesion-clinica.html">documentaci&oacute;n de sesiones cl&iacute;nicas</a> proporciona formatos para registrar evaluaciones de riesgo y decisiones cl&iacute;nicas.',
          'En instituciones de salud, el psic&oacute;logo reporta al comit&eacute; epidemiol&oacute;gico o al responsable de SIVIGILA de la IPS, quien formaliza la notificaci&oacute;n en el sistema. En consulta privada, el psic&oacute;logo puede ser directamente responsable de la notificaci&oacute;n.',
          'La <a href="/articulos/ley-1090-psicologia-colombia.html">Ley 1090</a> establece el deber del psic&oacute;logo de reportar situaciones que pongan en riesgo la integridad de personas vulnerables, lo cual se alinea con las obligaciones de SIVIGILA.',
        ],
      },
      {
        title: 'Violencia, maltrato y protecci&oacute;n de vulnerables',
        paragraphs: [
          'La violencia de g&eacute;nero, el maltrato infantil y el abuso en adultos mayores son eventos de notificaci&oacute;n obligatoria. El psic&oacute;logo frecuentemente es el primer profesional en detectar estas situaciones durante la evaluaci&oacute;n o el proceso terap&eacute;utico.',
          'En menores de edad, la Ley 1098 de 2006 (C&oacute;digo de la Infancia) establece la obligaci&oacute;n de denuncia ante Comisar&iacute;as de Familia, ICBF o Fiscal&iacute;a. SIVIGILA complementa este reporte con la dimensi&oacute;n epidemiol&oacute;gica.',
          'El psic&oacute;logo debe conocer la ruta de atenci&oacute;n para v&iacute;ctimas de violencia en su territorio: comisar&iacute;as de familia, casas de justicia, l&iacute;neas de emergencia (123, 155) y servicios especializados de salud mental.',
          'Documentar de forma precisa y objetiva (hechos observados, declaraciones del paciente, evaluaci&oacute;n de riesgo) es esencial tanto para la protecci&oacute;n del paciente como para respaldo legal del profesional.',
        ],
      },
      {
        title: 'Rol del psic&oacute;logo en la vigilancia epidemiol&oacute;gica',
        paragraphs: [
          'M&aacute;s all&aacute; de la notificaci&oacute;n obligatoria, los psic&oacute;logos contribuyen a la salud p&uacute;blica al identificar patrones de riesgo en poblaciones atendidas: incremento de intentos suicidas en adolescentes, violencia intrafamiliar en contextos de confinamiento, o deterioro de salud mental en comunidades expuestas a desastres.',
          'Participar en comit&eacute;s epidemiol&oacute;gicos institucionales, capacitarse en detecci&oacute;n temprana y mantener registros cl&iacute;nicos estandarizados son formas activas de contribuir al sistema de vigilancia.',
          'La Resoluci&oacute;n 4886 de 2018 incluye indicadores de salud mental que las IPS deben reportar, vinculando la pr&aacute;ctica cl&iacute;nica psicol&oacute;gica con metas del sistema de salud.',
          'Plataformas digitales como Kalyo facilitan la trazabilidad de evaluaciones de riesgo y eventos cl&iacute;nicos, apoyando tanto la pr&aacute;ctica cl&iacute;nica como los requerimientos de reporte institucional.',
        ],
      },
      {
        title: 'Limitaciones y desaf&iacute;os pr&aacute;cticos',
        paragraphs: [
          'Muchos psic&oacute;logos en consulta privada desconocen sus obligaciones de notificaci&oacute;n en SIVIGILA, lo que genera subregistro de eventos de salud mental en el pa&iacute;s y dificulta la planificaci&oacute;n de pol&iacute;ticas p&uacute;blicas.',
          'El sistema SIVIGILA fue dise&ntilde;ado principalmente para enfermedades transmisibles; la integraci&oacute;n de eventos de salud mental ha sido progresiva pero a&uacute;n presenta vac&iacute;os en estandarizaci&oacute;n y capacitaci&oacute;n.',
          'La tensi&oacute;n entre confidencialidad terap&eacute;utica y notificaci&oacute;n obligatoria puede generar dilemas &eacute;ticos. El psic&oacute;logo debe priorizar siempre la seguridad del paciente y de terceros, fundamentando sus decisiones en protocolos y supervisi&oacute;n.',
          'La capacitaci&oacute;n en SIVIGILA deber&iacute;a formar parte de la formaci&oacute;n continuada obligatoria de todo psic&oacute;logo cl&iacute;nico en Colombia, especialmente quienes atienden poblaciones de alto riesgo.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'resolucion-1888-salud-mental-colombia',
      filename: 'resolucion-1888-salud-mental-colombia.html',
      title: 'Resolución 1888: Salud Mental en Colombia — guía para psicólogos | Kalyo',
      description:
        'Guía de la Resolución 1888 de 2025 para psicólogos: rutas de atención, criterios de hospitalización y salud mental en Colombia. Cumple con Kalyo.',
      keywords: 'Resolución 1888, salud mental Colombia, psicología clínica, ruta de atención, normativa salud mental',
      metaLabel: NORM_CO,
      h1: 'Resoluci&oacute;n 1888: Pol&iacute;tica de Salud Mental en Colombia',
      intro:
        'La Resoluci&oacute;n 1888 de 2025 del Ministerio de Salud y Protecci&oacute;n Social de Colombia establece la pol&iacute;tica de atenci&oacute;n integral en salud mental, definiendo rutas de atenci&oacute;n, criterios de referencia y contrarreferencia, y est&aacute;ndares de calidad. Es la norma de referencia para psic&oacute;logos que prestan servicios de salud mental en el sistema colombiano.',
      heroAlt: 'Resolución 1888 salud mental en tablet con interfaz clínica púrpura',
      inlineAlt: 'Diagrama ruta atención salud mental Resolución 1888 púrpura',
      ctaTitle: 'Atiende salud mental con respaldo normativo en Kalyo',
      ctaText: 'Documenta evaluaciones, rutas de atenci&oacute;n y seguimiento conforme a est&aacute;ndares de salud mental en Colombia.',
      ctaButton: 'Prueba gratis 14 d&iacute;as &rarr;',
      related: [
        ['ley-1090-psicologia-colombia', 'Ley 1090: Psicolog&iacute;a en Colombia'],
        ['sivigila-psicologia-colombia', 'SIVIGILA y Psicolog&iacute;a en Colombia'],
        ['consentimiento-informado-psicologia', 'Consentimiento Informado en Psicolog&iacute;a'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; establece la Resoluci&oacute;n 1888?',
        paragraphs: [
          'La Resoluci&oacute;n 1888 de 2025 actualiza y fortalece la pol&iacute;tica de salud mental en Colombia, promoviendo un enfoque de atenci&oacute;n integral basado en la comunidad, con &eacute;nfasis en la atenci&oacute;n primaria, la reducci&oacute;n de la hospitalizaci&oacute;n innecesaria y la integraci&oacute;n de servicios de salud mental en el primer nivel de atenci&oacute;n.',
          'Define las rutas integrales de atenci&oacute;n en salud mental (RIAS) para trastornos mentales comunes, trastornos por consumo de sustancias, trastornos mentales severos y suicidio. Cada ruta especifica niveles de atenci&oacute;n, profesionales responsables y criterios de referencia.',
          'Establece que la atenci&oacute;n en salud mental debe ser accesible, oportuna, equitativa, continua, integral, pertinente y con calidad. Estos principios orientan la pr&aacute;ctica del psic&oacute;logo en cualquier nivel del sistema de salud.',
          'La resoluci&oacute;n reconoce expresamente el rol del psic&oacute;logo cl&iacute;nico en la evaluaci&oacute;n, intervenci&oacute;n y seguimiento de trastornos mentales, tanto en atenci&oacute;n primaria como en servicios especializados.',
        ],
      },
      {
        title: 'Rutas de atenci&oacute;n en salud mental',
        paragraphs: [
          'Las RIAS organizan la atenci&oacute;n en niveles: primario (consulta psicol&oacute;gica en EPS, psicoeducaci&oacute;n, tamizaje), secundario (psicoterapia estructurada, evaluaci&oacute;n psicol&oacute;gica especializada) y terciario (hospitalizaci&oacute;n, unidades de salud mental, rehabilitaci&oacute;n psicosocial).',
          'El psic&oacute;logo en atenci&oacute;n primaria realiza tamizaje (PHQ-9, GAD-7, AUDIT), intervenciones breves y derivaci&oacute;n oportuna cuando el caso excede su complejidad. La resoluci&oacute;n enfatiza que la mayor&iacute;a de trastornos mentales comunes deben resolverse en el primer nivel.',
          'Los criterios de referencia incluyen: ausencia de respuesta a intervenciones en primario despu&eacute;s de un n&uacute;mero definido de sesiones, presencia de riesgo suicida moderado a alto, trastornos severos, comorbilidad psiqui&aacute;trica que requiera farmacoterapia, y necesidad de hospitalizaci&oacute;n.',
          'La contrarreferencia exige que el especialista devuelva al paciente al primario con un plan de seguimiento claro, evitando la &laquo;perdida&raquo; del paciente en el sistema.',
        ],
      },
      {
        title: 'Rol del psic&oacute;logo en la Resoluci&oacute;n 1888',
        paragraphs: [
          'La resoluci&oacute;n posiciona al psic&oacute;logo como actor central en la atenci&oacute;n primaria en salud mental: tamizaje, psicoeducaci&oacute;n, intervenciones breves basadas en evidencia (TCC, activaci&oacute;n conductual, manejo de estr&eacute;s) y seguimiento longitudinal.',
          'En el nivel secundario, el psic&oacute;logo realiza psicoterapia estructurada, evaluaciones psicol&oacute;gicas completas e intervenciones especializadas (EMDR, DBT, terapia de pareja, intervenciones perinatales).',
          'El psic&oacute;logo debe documentar cada intervenci&oacute;n conforme a est&aacute;ndares de calidad, incluyendo evaluaci&oacute;n inicial, plan de tratamiento, notas de evoluci&oacute;n y evaluaci&oacute;n de resultados. El <a href="/articulos/consentimiento-informado-psicologia.html">consentimiento informado</a> es requisito previo a cualquier intervenci&oacute;n.',
          'La resoluci&oacute;n promueve la interdisciplinariedad: el psic&oacute;logo trabaja coordinadamente con m&eacute;dicos generales, psiquiatras, trabajadores sociales y equipos de apoyo comunitario.',
        ],
      },
      {
        title: 'Suicidio y urgencias en salud mental',
        paragraphs: [
          'La Resoluci&oacute;n 1888 incluye una ruta espec&iacute;fica para la atenci&oacute;n del riesgo suicida, alineada con protocolos de <a href="/articulos/evaluacion-riesgo-suicida.html">evaluaci&oacute;n de riesgo suicida</a>. Establece que todo servicio de salud debe contar con protocolos para identificaci&oacute;n, evaluaci&oacute;n y manejo del riesgo.',
          'El psic&oacute;logo debe estar capacitado en evaluaci&oacute;n de riesgo suicida y conocer la ruta de derivaci&oacute;n a urgencias cuando el riesgo es inminente. La notificaci&oacute;n en <a href="/articulos/sivigila-psicologia-colombia.html">SIVIGILA</a> es complementaria a la atenci&oacute;n cl&iacute;nica urgente.',
          'Se promueve la reducci&oacute;n de acceso a medios letales, el seguimiento post-alta y la continuidad de la atenci&oacute;n en el nivel primario como estrategias de prevenci&oacute;n del suicidio.',
          'La resoluci&oacute;n desestigmatiza la atenci&oacute;n en salud mental de urgencia, reconociendo que la crisis suicida requiere respuesta inmediata y no puede esperar citas programadas.',
        ],
      },
      {
        title: 'Est&aacute;ndares de calidad y documentaci&oacute;n',
        paragraphs: [
          'La Resoluci&oacute;n 1888 exige que las IPS implementen est&aacute;ndares de calidad en salud mental, incluyendo tiempos m&aacute;ximos de espera para primera consulta, n&uacute;mero m&iacute;nimo de sesiones cubiertas por la EPS y evaluaci&oacute;n peri&oacute;dica de resultados terap&eacute;uticos.',
          'La documentaci&oacute;n cl&iacute;nica es un componente central de la calidad: historias cl&iacute;nicas completas, registros de evaluaciones psicom&eacute;tricas, planes de tratamiento individualizados y evidencia de seguimiento conforme a la <a href="/articulos/ley-1090-psicologia-colombia.html">Ley 1090</a>.',
          'Los indicadores de salud mental reportados a trav&eacute;s de SIVIGILA y los sistemas de informaci&oacute;n de las EPS deben reflejar la calidad real de la atenci&oacute;n, no solo volumen de consultas.',
          'Plataformas digitales como Kalyo apoyan el cumplimiento de est&aacute;ndares al integrar evaluaciones, documentaci&oacute;n y seguimiento longitudinal en un solo sistema trazable.',
        ],
      },
      {
        title: 'Limitaciones y perspectiva de implementaci&oacute;n',
        paragraphs: [
          'La implementaci&oacute;n de la Resoluci&oacute;n 1888 enfrenta desaf&iacute;os estructurales: escasez de psic&oacute;logos en atenci&oacute;n primaria, barreras de acceso en zonas rurales, insuficiente cobertura de psicoterapia por parte de las EPS y resistencia cultural al cuidado de salud mental.',
          'Muchas EPS a&uacute;n no han actualizado sus protocolos internos conforme a la resoluci&oacute;n, generando discrepancias entre la norma nacional y la pr&aacute;ctica real de autorizaci&oacute;n de servicios.',
          'El psic&oacute;logo en consulta privada, aunque no est&eacute; directamente sujeto a las RIAS institucionales, se beneficia de conocer las rutas para orientar a pacientes sobre sus derechos de acceso a servicios de salud mental en el sistema.',
          'La participaci&oacute;n activa de psic&oacute;logos en la implementaci&oacute;n de la resoluci&oacute;n, a trav&eacute;s de colegios profesionales y mesas de salud mental, es clave para que la pol&iacute;tica se traduzca en mejor atenci&oacute;n real para la poblaci&oacute;n colombiana.',
        ],
      },
    ],
  ),
];
