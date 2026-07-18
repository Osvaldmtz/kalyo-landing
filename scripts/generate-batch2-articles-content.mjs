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
const PRACTICE_META = 'Pr&aacute;ctica profesional &middot; Actualizaci&oacute;n 2026';

export const BATCH2_ARTICLES = [
  makeArticle(
    {
      slug: 'ghq-12-cuestionario-salud-general',
      filename: 'ghq-12-cuestionario-salud-general.html',
      title: 'GHQ-12: Cuestionario de Salud General — guía clínica para psicólogos | Kalyo',
      description:
        'Guía completa del GHQ-12: 12 ítems, puntuación Likert y GHQ, punto de corte ≥3 y uso en atención primaria. Aplica el GHQ-12 digitalmente en Kalyo.',
      keywords: 'GHQ-12, cuestionario salud general, Goldberg, tamizaje salud mental, psicología clínica, atención primaria',
      metaLabel: CLINICAL_META,
      h1: 'GHQ-12: Cuestionario de Salud General',
      intro:
        'El General Health Questionnaire de 12 &iacute;tems (GHQ-12) es uno de los instrumentos de tamizaje psicosocial m&aacute;s utilizados en el mundo. Desarrollado por David Goldberg, detecta malestar psicol&oacute;gico no espec&iacute;fico en poblaci&oacute;n general y en atenci&oacute;n primaria. Su brevedad, facilidad de administraci&oacute;n y s&oacute;lida base psicom&eacute;trica lo convierten en una herramienta esencial para psic&oacute;logos que trabajan en contextos comunitarios, m&eacute;dicos y de salud ocupacional.',
      heroAlt: 'GHQ-12 cuestionario salud general en tablet con interfaz clínica púrpura',
      inlineAlt: 'Gráfico interpretación GHQ-12 puntuación Likert y GHQ, psicología clínica púrpura',
      ctaTitle: 'Aplica el GHQ-12 digitalmente en Kalyo',
      ctaText: 'Tamiza malestar psicosocial con el GHQ-12 y vincula los resultados al expediente cl&iacute;nico de tus pacientes con interpretaci&oacute;n autom&aacute;tica.',
      ctaButton: 'Prueba gratis 7 d&iacute;as &rarr;',
      related: [
        ['que-es-el-phq-9', '&iquest;Qu&eacute; es el PHQ-9?'],
        ['escala-dass-21', 'DASS-21: Depresi&oacute;n, Ansiedad y Estr&eacute;s'],
        ['pss-10-escala-estres-percibido', 'PSS-10: Escala de Estr&eacute;s Percibido'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; es el GHQ-12 y qui&eacute;n lo desarroll&oacute;?',
        paragraphs: [
          'El GHQ-12 forma parte de la familia de cuestionarios General Health Questionnaire desarrollados por David P. Goldberg y colaboradores a partir de la d&eacute;cada de 1970 en el Institute of Psychiatry de Londres. La versi&oacute;n de 12 &iacute;tems fue seleccionada por su equilibrio entre sensibilidad, especificidad y brevedad, convirti&eacute;ndose en la m&aacute;s empleada internacionalmente para detectar malestar psicol&oacute;gico en los &uacute;ltimos meses.',
          'A diferencia de escalas que miden trastornos espec&iacute;ficos como depresi&oacute;n o ansiedad, el GHQ-12 eval&uacute;a la salud psicol&oacute;gica general: incapacidad para realizar actividades habituales, s&iacute;ntomas som&aacute;ticos relacionados con el estr&eacute;s, ansiedad, depresi&oacute;n leve y disfunci&oacute;n social. Esto lo hace especialmente &uacute;til como primer filtro antes de aplicar instrumentos m&aacute;s espec&iacute;ficos como el <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a> o el <a href="/articulos/escala-dass-21.html">DASS-21</a>.',
          'El cuestionario ha sido traducido y validado en decenas de idiomas, incluido el espa&ntilde;ol, con estudios en poblaciones cl&iacute;nicas y comunitarias de Am&eacute;rica Latina. Su aplicaci&oacute;n no requiere entrenamiento especializado: puede administrarse de forma aut&oacute;noma, en entrevista o mediante plataformas digitales que calculan autom&aacute;ticamente ambos sistemas de puntuaci&oacute;n.',
          'En la pr&aacute;ctica cl&iacute;nica contempor&aacute;nea, el GHQ-12 se utiliza en programas de salud p&uacute;blica, consultorios de medicina general, evaluaciones ocupacionales y psicolog&iacute;a comunitaria. No sustituye un diagn&oacute;stico cl&iacute;nico, pero orienta la necesidad de evaluaci&oacute;n psicol&oacute;gica m&aacute;s profunda cuando el puntaje supera el punto de corte establecido.',
        ],
      },
      {
        title: 'Los 12 &iacute;tems y c&oacute;mo aplicarlos',
        paragraphs: [
          'Los 12 &iacute;tems del GHQ-12 exploran experiencias recientes relacionadas con la salud mental y el funcionamiento cotidiano. Ejemplos t&iacute;picos incluyen: &laquo;&iquest;Ha podido concentrarse en lo que hace?&raquo;, &laquo;&iquest;Ha perdido mucho sue&ntilde;o por preocupaciones?&raquo;, &laquo;&iquest;Se ha sentido capaz de tomar decisiones?&raquo; y &laquo;&iquest;Ha sentido que no supera sus dificultades?&raquo;. Cada reactivo captura un aspecto del malestar psicosocial.',
          'La instrucci&oacute;n est&aacute;ndar pide al respondiente referirse a c&oacute;mo se ha sentido durante las &uacute;ltimas semanas en comparaci&oacute;n con su estado habitual. Las opciones de respuesta utilizan una escala Likert de cuatro puntos: &laquo;menos que lo habitual&raquo;, &laquo;igual que lo habitual&raquo;, &laquo;m&aacute;s que lo habitual&raquo; y &laquo;mucho m&aacute;s que lo habitual&raquo;, aunque la codificaci&oacute; num&eacute;rica var&iacute;a seg&uacute;n el m&eacute;todo de puntuaci&oacute;n elegido.',
          'La administraci&oacute;n puede ser presencial, telef&oacute;nica o digital. En contextos de atenci&oacute;n primaria, muchos protocolos recomiendan aplicarlo en sala de espera antes de la consulta m&eacute;dica o psicol&oacute;gica. En plataformas como Kalyo, el paciente completa el cuestionario de forma remota y el cl&iacute;nico recibe el puntaje interpretado antes de la sesi&oacute;n.',
          'Es importante aclarar al paciente que no existen respuestas correctas o incorrectas y que el cuestionario eval&uacute;a su bienestar reciente, no un diagn&oacute;stico. Si el paciente presenta dificultades de comprensi&oacute;n lectora, el cl&iacute;nico puede leer los &iacute;tems en voz alta manteniendo la estandarizaci&oacute;n del instrumento.',
        ],
      },
      {
        title: 'Dos formas de puntuaci&oacute;n: Likert (0-1-2-3) y GHQ (0-0-1-1)',
        paragraphs: [
          'El GHQ-12 admite dos sistemas de puntuaci&oacute;n ampliamente documentados en la literatura. El m&eacute;todo Likert asigna 0, 1, 2 y 3 a las cuatro opciones de respuesta respectivamente, produciendo un rango total de 0 a 36. Este m&eacute;todo conserva la gradaci&oacute;n completa de la respuesta y es &uacute;til cuando se busca sensibilidad a cambios graduales en intervenciones comunitarias o de salud p&uacute;blica.',
          'El m&eacute;todo GHQ binario codifica las dos primeras opciones como 0 y las dos &uacute;ltimas como 1, siguiendo la l&oacute;gica de que respuestas en los extremos superiores indican presencia de s&iacute;ntomas. Con este sistema, el puntaje total var&iacute;a de 0 a 12 y es el m&aacute;s utilizado para determinar casos probables de malestar psicol&oacute;gico en investigaci&oacute;n epidemiol&oacute;gica y tamizaje cl&iacute;nico.',
          'La elecci&oacute;n del m&eacute;todo debe ser consistente dentro de un mismo protocolo o estudio. Mezclar ambos sistemas en una misma cohorte invalida la comparabilidad de resultados. Las plataformas digitales deben permitir seleccionar el m&eacute;todo de puntuaci&oacute;n y documentarlo en el informe cl&iacute;nico.',
          'En la pr&aacute;ctica cl&iacute;nica individual, el m&eacute;todo GHQ (0-0-1-1) es el est&aacute;ndar m&aacute;s recomendado por su amplia validaci&oacute;n con el punto de corte &ge;3. El m&eacute;todo Likert puede complementarse cuando se monitoriza evoluci&oacute;n durante intervenciones breves de apoyo psicosocial.',
        ],
      },
      {
        title: 'Punto de corte &ge;3 GHQ',
        paragraphs: [
          'Con el m&eacute;todo de puntuaci&oacute;n GHQ (0-0-1-1), el punto de corte m&aacute;s ampliamente aceptado es &ge;3 para identificar casos probables de malestar psicol&oacute;gico. Este umbral ha demostrado buen equilibrio entre sensibilidad y especificidad en m&uacute;ltiples poblaciones, aunque algunos estudios sugieren ajustes seg&uacute;n contexto cultural o cl&iacute;nico.',
          'Un puntaje de 0 a 2 generalmente indica ausencia de malestar psicol&oacute;gico significativo en el periodo evaluado, aunque no descarta problemas puntuales que requieran exploraci&oacute;n en entrevista. Un puntaje &ge;3 activa la recomendaci&oacute;n de evaluaci&oacute;n cl&iacute;nica m&aacute;s detallada, preferiblemente con instrumentos espec&iacute;ficos de depresi&oacute;n, ansiedad y estr&eacute;s.',
        ],
        extra: `
    <table class="severity-table">
      <thead>
        <tr>
          <th>Puntuaci&oacute;n GHQ</th>
          <th>Interpretaci&oacute;n</th>
          <th>Acci&oacute;n cl&iacute;nica</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="score-badge">0 &ndash; 2</span></td>
          <td><strong>Sin malestar significativo</strong></td>
          <td>Monitoreo; psicoeducaci&oacute;n si hay factores estresores identificados.</td>
        </tr>
        <tr>
          <td><span class="score-badge">&ge; 3</span></td>
          <td><strong>Caso probable de malestar psicol&oacute;gico</strong></td>
          <td>Evaluaci&oacute;n cl&iacute;nica ampliada; aplicar PHQ-9, GAD-7 o DASS-21.</td>
        </tr>
        <tr>
          <td><span class="score-badge">Likert 0 &ndash; 11</span></td>
          <td><strong>Rango bajo (m&eacute;todo Likert)</strong></td>
          <td>Seguimiento rutinario; reevaluar si persisten quejas.</td>
        </tr>
        <tr>
          <td><span class="score-badge">Likert &ge; 12</span></td>
          <td><strong>Rango elevado (m&eacute;todo Likert)</strong></td>
          <td>Derivar a evaluaci&oacute;n psicol&oacute;gica especializada.</td>
        </tr>
      </tbody>
    </table>`,
      },
      {
        title: 'GHQ-12 vs PHQ-9 vs DASS-21',
        paragraphs: [
          'El GHQ-12, el <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a> y el <a href="/articulos/escala-dass-21.html">DASS-21</a> responden a objetivos cl&iacute;nicos distintos aunque puedan complementarse. El GHQ-12 es un tamizaje general de malestar psicosocial no espec&iacute;fico; el PHQ-9 mide severidad de s&iacute;ntomas depresivos seg&uacute;n criterios del DSM; y el DASS-21 diferencia tres dimensiones emocionales: depresi&oacute;n, ansiedad y estr&eacute;s.',
          'En atenci&oacute;n primaria, el GHQ-12 funciona como primer filtro de bajo costo temporal. Si el resultado es positivo (&ge;3), el PHQ-9 permite cuantificar depresi&oacute;n y evaluar ideaci&oacute;n suicida (&iacute;tem 9). El DASS-21 aporta un perfil dimensional cuando el malestar es polisintom&aacute;tico y se necesita orientar la intervenci&oacute;n hacia ansiedad, estado de &aacute;nimo o estr&eacute;s percibido.',
          'El <a href="/articulos/pss-10-escala-estres-percibido.html">PSS-10</a> puede a&ntilde;adirse cuando el GHQ-12 sugiere malestar pero se sospecha que el estr&eacute;s cr&oacute;nico es el factor central, especialmente en contextos laborales o acad&eacute;micos. La combinaci&oacute;n GHQ-12 + PHQ-9 + PSS-10 ofrece un tamizaje breve pero comprehensivo en menos de quince minutos.',
          'Ninguno de estos instrumentos establece diagn&oacute;stico por s&iacute; solo. La entrevista cl&iacute;nica, la historia psicosocial y la formulaci&oacute;n del caso integran los resultados psicom&eacute;tricos con la experiencia subjetiva del paciente y su contexto vital.',
        ],
      },
      {
        title: 'Uso en atenci&oacute;n primaria',
        paragraphs: [
          'En medicina general y atenci&oacute;n primaria, el GHQ-12 se ha consolidado como herramienta de detecci&oacute;n temprana de problemas de salud mental que de otro modo pasar&iacute;an desapercibidos. Estudios demuestran que una proporci&oacute;n significativa de pacientes con malestar psicol&oacute;gico consulta inicialmente por s&iacute;ntomas som&aacute;ticos inespec&iacute;ficos.',
          'Los m&eacute;dicos de familia y enfermeras de atenci&oacute;n primaria pueden aplicar el GHQ-12 en sala de espera. Un resultado positivo activa la derivaci&oacute;n al psic&oacute;logo o psiquiatra del equipo de salud. Este modelo de tamizaje escalonado optimiza recursos y reduce tiempos de espera para intervenciones especializadas.',
          'Para psic&oacute;logos integrados en equipos interdisciplinarios, el GHQ-12 facilita la triage: pacientes con puntajes bajos pueden recibir intervenciones breves de psicoeducaci&oacute;n, mientras que puntajes elevados justifican evaluaci&oacute;n completa con bater&iacute;as espec&iacute;ficas y plan terap&eacute;utico estructurado.',
          'La readministraci&oacute;n peri&oacute;dica del GHQ-12 permite monitorizar respuesta a intervenciones de salud mental en atenci&oacute;n primaria, especialmente programas de activaci&oacute;n conductual, manejo de estr&eacute;s y apoyo psicosocial post-crisis.',
        ],
      },
      {
        title: 'Validaci&oacute;n Colombia/M&eacute;xico',
        paragraphs: [
          'En Colombia, estudios de validaci&oacute;n del GHQ-12 en poblaci&oacute;n general y cl&iacute;nica han confirmado propiedades psicom&eacute;tricas aceptables, con consistencia interna (alfa de Cronbach) generalmente superior a 0.80. El punto de corte &ge;3 se ha replicado con sensibilidad adecuada, aunque se recomienda considerar variables sociodemogr&aacute;ficas en poblaciones rurales o con baja escolaridad.',
          'En M&eacute;xico, investigaciones en contextos urbanos, estudiantiles y de salud ocupacional han documentado la utilidad del GHQ-12 como tamizaje en servicios de salud p&uacute;blica y privada. Algunos estudios sugieren puntos de corte ligeramente diferentes seg&uacute;n la poblaci&oacute;n (3-4 en m&eacute;todo GHQ), por lo que conviene documentar la referencia normativa utilizada.',
          'Al aplicar el GHQ-12 en Colombia o M&eacute;xico, el psic&oacute;logo debe complementar la interpretaci&oacute;n num&eacute;rica con la evaluaci&oacute;n cultural del malestar: expresiones idiom&aacute;ticas de sufrimiento, estigma hacia la salud mental, acceso a servicios y factores socioecon&oacute;micos que modulan la presentaci&oacute;n cl&iacute;nica.',
          'Las plataformas digitales facilitan la estandarizaci&oacute;n del GHQ-12 en contextos multiculturales al garantizar instrucciones uniformes, puntuaci&oacute;n autom&aacute;tica y registro en el expediente cl&iacute;nico conforme a normativas locales como la Ley 1090 en Colombia o la NOM-004 en M&eacute;xico.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'phq-15-sintomas-somaticos',
      filename: 'phq-15-sintomas-somaticos.html',
      title: 'PHQ-15: Síntomas Somáticos — guía clínica para psicólogos | Kalyo',
      description:
        'Guía del PHQ-15: 15 síntomas somáticos, interpretación 0-30, relación con trauma y estrés, y cuándo derivar a medicina. Disponible digitalmente en Kalyo.',
      keywords: 'PHQ-15, síntomas somáticos, somatización, psicología clínica, tamizaje médico, salud mental',
      metaLabel: CLINICAL_META,
      h1: 'PHQ-15: Cuestionario de S&iacute;ntomas Som&aacute;ticos',
      intro:
        'El Patient Health Questionnaire de 15 &iacute;tems (PHQ-15) eval&uacute;a la severidad de s&iacute;ntomas som&aacute;ticos frecuentes en consulta m&eacute;dica y psicol&oacute;gica. Desarrollado por Kroenke, Spitzer y Williams como extensi&oacute;n del PHQ, permite cuantificar malestar f&iacute;sico que frecuentemente acompa&ntilde;a trastornos depresivos, ansiosos y relacionados con estr&eacute;s o trauma, orientando la integraci&oacute;n entre psicolog&iacute;a y medicina.',
      heroAlt: 'PHQ-15 síntomas somáticos en tablet con interfaz clínica púrpura',
      inlineAlt: 'Gráfico interpretación PHQ-15 escala 0-30 somatización púrpura',
      ctaTitle: 'Eval&uacute;a s&iacute;ntomas som&aacute;ticos con el PHQ-15 en Kalyo',
      ctaText: 'Integra el PHQ-15 con el PHQ-9 y el DASS-21 en bater&iacute;as digitales con puntuaci&oacute;n e interpretaci&oacute;n autom&aacute;tica.',
      ctaButton: 'Prueba gratis 7 d&iacute;as &rarr;',
      related: [
        ['que-es-el-phq-9', '&iquest;Qu&eacute; es el PHQ-9?'],
        ['escala-dass-21', 'DASS-21: Depresi&oacute;n, Ansiedad y Estr&eacute;s'],
        ['pss-10-escala-estres-percibido', 'PSS-10: Escala de Estr&eacute;s Percibido'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; mide el PHQ-15?',
        paragraphs: [
          'El PHQ-15 cuantifica la severidad de s&iacute;ntomas som&aacute;ticos que causan malestar funcional significativo. Eval&uacute;a molestias f&iacute;sicas como dolor de est&oacute;mago, dolor de espalda, dolores en extremidades, cefaleas, fatiga, palpitaciones, mareos, dificultad para respirar, indigesti&oacute;n, problemas sexuales, problemas de sue&ntilde;o y sensaci&oacute;n de peso en el pecho.',
          'A diferencia de una lista de s&iacute;ntomas m&eacute;dicos, el PHQ-15 pregunta cu&aacute;nto ha molestado cada s&iacute;ntoma al paciente durante las &uacute;ltimas cuatro semanas, capturando tanto presencia como impacto subjetivo. Esto lo distingue de exploraciones m&eacute;dicas que documentan hallazgos objetivos sin evaluar el sufrimiento asociado.',
          'El instrumento forma parte de la familia PHQ y comparte la l&oacute;gica de tamizaje breve orientado a la pr&aacute;ctica cl&iacute;nica primaria. Su objetivo no es diagnosticar trastorno de somatizaci&oacute;n, sino identificar pacientes con carga som&aacute;tica elevada que requieren evaluaci&oacute;n integrada psicol&oacute;gica y m&eacute;dica.',
          'En psicolog&iacute;a cl&iacute;nica, el PHQ-15 es especialmente valioso cuando el paciente presenta quejas f&iacute;sicas recurrentes sin explicaci&oacute;n m&eacute;dica suficiente, o cuando la somatizaci&oacute;n dificulta el acceso a intervenciones psicoterap&eacute;uticas centradas en emociones y cogniciones.',
        ],
      },
      {
        title: 'Los 15 s&iacute;ntomas',
        paragraphs: [
          'Los 15 &iacute;tems del PHQ-15 cubren las quejas som&aacute;ticas m&aacute;s frecuentes en atenci&oacute;n primaria internacional. Cada &iacute;tem se responde en escala de tres puntos: 0 (&laquo;nada&raquo;), 1 (&laquo;un poco&raquo;) y 2 (&laquo;mucho&raquo;), con un rango total de 0 a 30. La instrucci&oacute;n est&aacute;ndar es referirse a las &uacute;ltimas cuatro semanas.',
          'Los s&iacute;ntomas incluyen dolor estomacal, dolor de espalda, dolor en brazos/piernas/caderas/articulaciones, cefaleas, sensaci&oacute;n de peso en el pecho, mareos, desmayos, palpitaciones, falta de aliento, dolor al tener relaciones sexuales, problemas menstruales (en mujeres), estre&ntilde;imiento/diarrea/indigesti&oacute;n, fatiga/bajo nivel de energ&iacute;a y dificultad para dormir.',
          'Es importante registrar si el paciente ha consultado previamente con m&eacute;dicos por estos s&iacute;ntomas y qu&eacute; estudios se han realizado. La coexistencia de PHQ-15 elevado con evaluaci&oacute;n m&eacute;dica normal orienta hacia componente psicog&eacute;nico que requiere intervenci&oacute;n psicol&oacute;gica, sin descartar seguimiento m&eacute;dico.',
          'En poblaciones con alto estigma hacia la salud mental, los pacientes frecuentemente reportan s&iacute;ntomas som&aacute;ticos como v&iacute;a leg&iacute;tima de expresar sufrimiento. El PHQ-15 permite validar estas experiencias mientras se abre espacio para explorar dimensiones emocionales con instrumentos complementarios.',
        ],
      },
      {
        title: 'Puntuaci&oacute;n 0-4/5-9/10-14/15-30',
        paragraphs: [
          'La interpretaci&oacute;n del PHQ-15 utiliza rangos de severidad establecidos por Kroenke y colaboradores. Estos rangos orientan la intensidad de la intervenci&oacute;n y la necesidad de derivaci&oacute;n, siempre complementados con la entrevista cl&iacute;nica y evaluaci&oacute;n m&eacute;dica cuando corresponda.',
          'Un puntaje elevado en el PHQ-15 frecuentemente coexiste con depresi&oacute;n y ansiedad medidas por el <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a> y el <a href="/articulos/escala-dass-21.html">DASS-21</a>. La evaluaci&oacute;n integrada permite distinguir si la somatizaci&oacute;n es expresi&oacute;n primaria de malestar emocional o complicaci&oacute;n de condici&oacute;n m&eacute;dica org&aacute;nica.',
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
          <td><span class="score-badge">0 &ndash; 4</span></td>
          <td><strong>S&iacute;ntomas som&aacute;ticos m&iacute;nimos</strong></td>
          <td>Monitoreo; psicoeducaci&oacute;n sobre relaci&oacute;n mente-cuerpo.</td>
        </tr>
        <tr>
          <td><span class="score-badge">5 &ndash; 9</span></td>
          <td><strong>S&iacute;ntomas som&aacute;ticos bajos</strong></td>
          <td>Explorar factores estresores; evaluar comorbilidad emocional.</td>
        </tr>
        <tr>
          <td><span class="score-badge">10 &ndash; 14</span></td>
          <td><strong>S&iacute;ntomas som&aacute;ticos moderados</strong></td>
          <td>Intervenci&oacute;n psicol&oacute;gica; valorar derivaci&oacute;n m&eacute;dica.</td>
        </tr>
        <tr>
          <td><span class="score-badge">15 &ndash; 30</span></td>
          <td><strong>S&iacute;ntomas som&aacute;ticos severos</strong></td>
          <td>Evaluaci&oacute;n m&eacute;dica y psicol&oacute;gica integrada; plan multidisciplinario.</td>
        </tr>
      </tbody>
    </table>`,
      },
      {
        title: 'PHQ-15 trauma/estr&eacute;s',
        paragraphs: [
          'La somatizaci&oacute;n tiene una relaci&oacute;n bien documentada con experiencias traum&aacute;ticas y estr&eacute;s cr&oacute;nico. Pacientes con historial de abuso, violencia, accidentes o desastres frecuentemente presentan s&iacute;ntomas som&aacute;ticos persistentes como expresi&oacute;n del trauma no procesado. El PHQ-15 ayuda a cuantificar esta carga som&aacute;tica en la evaluaci&oacute;n inicial.',
          'El estr&eacute;s percibido medido por el <a href="/articulos/pss-10-escala-estres-percibido.html">PSS-10</a> frecuentemente correlaciona con puntuaciones elevadas del PHQ-15. Cuando ambos instrumentos son positivos, conviene explorar mecanismos de afrontamiento, hiperactivaci&oacute;n del sistema nervioso aut&oacute;nomo y posible trastorno por estr&eacute;s postraum&aacute;tico.',
          'En trauma complejo, la somatizaci&oacute;n puede ser el s&iacute;ntoma principal durante a&ntilde;os antes de que el paciente acceda a procesamiento emocional. El PHQ-15 proporciona un lenguaje menos estigmatizante para iniciar la conversaci&oacute;n sobre malestar, facilitando la transici&oacute;n hacia intervenciones psicoterap&eacute;uticas basadas en evidencia.',
          'La intervenci&oacute;n integrada combina psicoterapia (EMDR, TCC, enfoques som&aacute;ticos), manejo del estr&eacute;s y coordinaci&oacute;n con medicina cuando existen s&iacute;ntomas f&iacute;sicos que requieren descarte org&aacute;nico. El seguimiento con PHQ-15 permite documentar reducci&oacute;n de la carga som&aacute;tica a lo largo del tratamiento.',
        ],
      },
      {
        title: 'PHQ-9 vs PHQ-15',
        paragraphs: [
          'El <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a> y el PHQ-15 comparten autor&iacute;a y formato, pero miden constructos diferentes. El PHQ-9 eval&uacute;a s&iacute;ntomas depresivos nucleares (humor bajo, anhedonia, sue&ntilde;o, fatiga, apetito, culpa, concentraci&oacute;n, agitaci&oacute;n/retardo, ideaci&oacute;n suicida). El PHQ-15 se centra en s&iacute;ntomas f&iacute;sicos que causan malestar funcional.',
          'Un paciente puede presentar PHQ-9 elevado con PHQ-15 moderado (depresi&oacute;n con somatizaci&oacute;n leve), PHQ-15 elevado con PHQ-9 normal (somatizaci&oacute;n sin depresi&oacute;n cl&iacute;nica evidente), o ambos elevados (comorbilidad frecuente en consulta primaria). La evaluaci&oacute;n conjunta enriquece la formulaci&oacute;n del caso.',
          'En la pr&aacute;ctica cl&iacute;nica, se recomienda administrar ambos instrumentos cuando el paciente consulta por s&iacute;ntomas f&iacute;sicos inexplicados o depresi&oacute;n con quejas corporales prominentes. Las plataformas digitales permiten aplicar PHQ-9 y PHQ-15 en secuencia con puntuaci&oacute;n integrada.',
          'La interpretaci&oacute;n cruzada orienta el plan terap&eacute;utico: depresi&oacute;n predominante requiere intervenci&oacute;n en estado de &aacute;nimo; somatizaci&oacute;n predominante beneficia de t&eacute;cnicas de atenci&oacute;n plena, reestructuraci&oacute;n de creencias sobre s&iacute;ntomas f&iacute;sicos y psicoeducaci&oacute;n sobre la conexi&oacute;n mente-cuerpo.',
        ],
      },
      {
        title: 'Cu&aacute;ndo derivar m&eacute;dico',
        paragraphs: [
          'La derivaci&oacute;n m&eacute;dica est&aacute; indicada cuando los s&iacute;ntomas som&aacute;ticos del PHQ-15 son severos (15-30), aparecen s&iacute;ntomas de alarma (dolor tor&aacute;cico agudo, p&eacute;rdida de peso involuntaria, fiebre, d&eacute;ficit neurol&oacute;gico), o no se ha realizado evaluaci&oacute;n m&eacute;dica previa adecuada. El psic&oacute;logo no debe asumir origen psicog&eacute;nico sin descarte m&eacute;dico razonable.',
          'Ante PHQ-15 &ge;10 con historia de enfermedad m&eacute;dica conocida, la derivaci&oacute;n permite verificar si los s&iacute;ntomas representan exacerbaci&oacute;n org&aacute;nica o componente psicog&eacute;nico superpuesto. La comunicaci&oacute;n interdisciplinaria mejora la adherencia del paciente a ambos tratamientos.',
          'S&iacute;ntomas como palpitaciones, falta de aliento y dolor tor&aacute;cico requieren evaluaci&oacute;n cardiol&oacute;gica antes de atribuirse exclusivamente a ansiedad. Problemas sexuales y menstruales pueden tener causas endocrinas o ginecol&oacute;gicas que deben descartarse. El PHQ-15 orienta pero no reemplaza el juicio cl&iacute;nico m&eacute;dico.',
          'Cuando la evaluaci&oacute;n m&eacute;dica descarta patolog&iacute;a org&aacute;nica significativa y el PHQ-15 permanece elevado, el psic&oacute;logo puede proceder con intervenci&oacute;n psicoterap&eacute;utica documentando la evaluaci&oacute;n integrada. Este enfoque reduce la iatrogenia de m&uacute;ltiples consultas m&eacute;dicas innecesarias y valida la dimensi&oacute;n psicol&oacute;gica del sufrimiento.',
          'El seguimiento peri&oacute;dico con PHQ-15 cada cuatro a ocho semanas documenta respuesta a intervenciones psicoterap&eacute;uticas centradas en somatizaci&oacute;n, mindfulness som&aacute;tico o procesamiento de trauma. Una reducci&oacute;n sostenida de cinco o m&aacute;s puntos suele indicar mejor&iacute;a cl&iacute;nicamente significativa en consulta ambulatoria.',
        ],
      },
      {
        title: 'Integraci&oacute;n cl&iacute;nica del PHQ-15',
        paragraphs: [
          'El PHQ-15 funciona mejor dentro de una bater&iacute;a integrada que incluya evaluaci&oacute;n emocional, estr&eacute;s y funcionamiento global. En pacientes con quejas som&aacute;ticas cr&oacute;nicas, combinar PHQ-15 con <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a>, <a href="/articulos/escala-dass-21.html">DASS-21</a> y <a href="/articulos/pss-10-escala-estres-percibido.html">PSS-10</a> permite distinguir si el malestar f&iacute;sico se explica principalmente por depresi&oacute;n, ansiedad, estr&eacute;s cr&oacute;nico o una combinaci&oacute;n de factores.',
          'En formulaci&oacute;n de caso, registrar qu&eacute; s&iacute;ntomas som&aacute;ticos tienen mayor puntaje orienta la psicoeducaci&oacute;n: un paciente con cefaleas y tensi&oacute;n muscular dominante puede beneficiarse de t&eacute;cnicas de relajaci&oacute;n; uno con dolor abdominal y gastrointestinal, de intervenciones sobre ansiedad anticipatoria y h&aacute;bitos alimentarios.',
          'Las plataformas digitales permiten visualizar la evoluci&oacute;n de cada s&iacute;ntoma som&aacute;tico por separado, no solo el puntaje total. Esto enriquece la conversaci&oacute;n cl&iacute;nica y ayuda al paciente a reconocer patrones entre estr&eacute;s emocional y manifestaciones corporales.',
          'Finalmente, el PHQ-15 debe interpretarse con sensibilidad cultural: en algunas poblaciones latinoamericanas, la expresi&oacute;n som&aacute;tica del malestar es normativa y no siempre indica patolog&iacute;a. La entrevista cl&iacute;nica contextualiza si los s&iacute;ntomas causan deterioro funcional real o representan variaci&oacute;n cultural de la expresi&oacute;n emocional.',
          'Registrar la fecha, el contexto de aplicaci&oacute;n y la interpretaci&oacute;n integrada con otros instrumentos cumple est&aacute;ndares de buena pr&aacute;ctica cl&iacute;nica y facilita la continuidad cuando el paciente es derivado a medicina o psiquiatr&iacute;a.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'dast-10-deteccion-drogas',
      filename: 'dast-10-deteccion-drogas.html',
      title: 'DAST-10: Detección de Consumo de Drogas — guía clínica | Kalyo',
      description:
        'Guía del DAST-10: 10 ítems, interpretación por rangos, comparación con AUDIT, uso en adicciones y consideraciones éticas. Tamizaje digital en Kalyo.',
      keywords: 'DAST-10, detección drogas, consumo sustancias, adicciones, psicología clínica, tamizaje',
      metaLabel: CLINICAL_META,
      h1: 'DAST-10: Cuestionario de Detecci&oacute;n de Consumo de Drogas',
      intro:
        'El Drug Abuse Screening Test de 10 &iacute;tems (DAST-10) es un instrumento breve de autoinforme dise&ntilde;ado para detectar problemas relacionados con el consumo de drogas (excluyendo alcohol y tabaco). Desarrollado por Skinner y modificado por Gavin y colaboradores, el DAST-10 identifica consecuencias adversas del uso de sustancias y orienta la necesidad de evaluaci&oacute;n especializada en adicciones.',
      heroAlt: 'DAST-10 detección drogas en tablet con interfaz clínica púrpura',
      inlineAlt: 'Gráfico interpretación DAST-10 rangos puntuación adicciones púrpura',
      ctaTitle: 'Tamiza consumo problem&aacute;tico con el DAST-10 en Kalyo',
      ctaText: 'Integra el DAST-10 con el AUDIT y escalas de salud mental en bater&iacute;as de evaluaci&oacute;n cl&iacute;nica digital.',
      ctaButton: 'Prueba gratis 7 d&iacute;as &rarr;',
      related: [
        ['audit-test-alcoholismo', 'AUDIT: Test de Alcoholismo'],
        ['evaluacion-riesgo-suicida', 'Evaluaci&oacute;n de Riesgo Suicida'],
        ['escala-dass-21', 'DASS-21: Depresi&oacute;n, Ansiedad y Estr&eacute;s'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; es el DAST-10?',
        paragraphs: [
          'El DAST-10 es la versi&oacute;n abreviada del Drug Abuse Screening Test original de 28 &iacute;tems. Fue dise&ntilde;ado para uso en atenci&oacute;n primaria, servicios de urgencias y consulta psicol&oacute;gica donde el tiempo de evaluaci&oacute;n es limitado pero la detecci&oacute;n de consumo problem&aacute;tico de sustancias es cl&iacute;nicamente relevante.',
          'El instrumento eval&uacute;a consecuencias del consumo de drogas il&iacute;citas y uso indebido de medicamentos recetados durante los &uacute;ltimos 12 meses. Pregunta sobre culpa, problemas legales, relaciones interpersonales afectadas, incapacidad para dejar de consumir, abandono de actividades y preocupaci&oacute;n de terceros por el consumo.',
          'Es importante aclarar que el DAST-10 no eval&uacute;a alcohol (para ello existe el <a href="/articulos/audit-test-alcoholismo.html">AUDIT</a>) ni tabaco. En la pr&aacute;ctica cl&iacute;nica, se recomienda administrar ambos instrumentos cuando se sospecha policonsumo, dado que alcohol y otras sustancias frecuentemente coexisten.',
          'El DAST-10 es un instrumento de tamizaje, no un diagn&oacute;stico de trastorno por uso de sustancias. Un puntaje elevado indica probable problema que requiere evaluaci&oacute;n cl&iacute;nica estructurada, entrevista motivacional y, cuando corresponda, derivaci&oacute;n a servicios especializados en adicciones.',
        ],
      },
      {
        title: '10 &iacute;tems',
        paragraphs: [
          'Los 10 &iacute;tems del DAST-10 son preguntas de s&iacute;/no sobre experiencias relacionadas con el consumo de drogas en el &uacute;ltimo a&ntilde;o. Ejemplos incluyen: &laquo;&iquest;Ha usado drogas distintas a las necesarias por razones m&eacute;dicas?&raquo;, &laquo;&iquest;Ha sentido culpa por su consumo?&raquo;, &laquo;&iquest;Ha tenido problemas legales por consumo?&raquo; y &laquo;&iquest;Le han criticado familiares o amigos por su consumo?&raquo;',
          'Cada respuesta afirmativa (excepto el &iacute;tem 3, que se punt&uacute;a de forma inversa) suma un punto. El rango total es 0 a 10. La administraci&oacute;n toma menos de cinco minutos y puede realizarse de forma an&oacute;nima en programas de tamizaje comunitario o confidencial en consulta cl&iacute;nica.',
          'El cl&iacute;nico debe crear un ambiente de confidencialidad y no juicio para maximizar la honestidad del paciente. Explicar que las respuestas son confidenciales y que el objetivo es ofrecer ayuda, no castigo, reduce la deseabilidad social en las respuestas.',
          'En adolescentes y adultos j&oacute;venes, conviene complementar el DAST-10 con exploraci&oacute;n de sustancias espec&iacute;ficas consumidas (cannabis, coca&iacute;na, estimulantes, opioides, benzodiacepinas, alucin&oacute;genos) y contexto de consumo (recreativo, automedicaci&oacute;n, presi&oacute;n social).',
        ],
      },
      {
        title: 'Puntuaci&oacute;n 0/1-2/3-5/6-8/9-10',
        paragraphs: [
          'La interpretaci&oacute;n del DAST-10 utiliza rangos progresivos de severidad que orientan el nivel de intervenci&oacute;n requerido. A mayor puntaje, mayor probabilidad de trastorno por uso de sustancias y mayor urgencia de evaluaci&oacute;n especializada.',
          'En puntajes elevados, conviene evaluar comorbilidad psiqui&aacute;trica con el <a href="/articulos/escala-dass-21.html">DASS-21</a> y explorar riesgo suicida seg&uacute;n protocolos de <a href="/articulos/evaluacion-riesgo-suicida.html">evaluaci&oacute;n de riesgo suicida</a>, dado que el consumo de sustancias incrementa significativamente el riesgo de autolesión y suicidio.',
        ],
        extra: `
    <table class="severity-table">
      <thead>
        <tr>
          <th>Puntuaci&oacute;n</th>
          <th>Nivel de problema</th>
          <th>Acci&oacute;n cl&iacute;nica</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="score-badge">0</span></td>
          <td><strong>Sin problemas detectados</strong></td>
          <td>Psicoeducaci&oacute;n preventiva si hay factores de riesgo.</td>
        </tr>
        <tr>
          <td><span class="score-badge">1 &ndash; 2</span></td>
          <td><strong>Nivel bajo</strong></td>
          <td>Intervenci&oacute;n breve; monitoreo del consumo.</td>
        </tr>
        <tr>
          <td><span class="score-badge">3 &ndash; 5</span></td>
          <td><strong>Nivel moderado</strong></td>
          <td>Evaluaci&oacute;n cl&iacute;nica ampliada; entrevista motivacional.</td>
        </tr>
        <tr>
          <td><span class="score-badge">6 &ndash; 8</span></td>
          <td><strong>Nivel sustancial</strong></td>
          <td>Derivaci&oacute;n a servicios de adicciones; plan de tratamiento.</td>
        </tr>
        <tr>
          <td><span class="score-badge">9 &ndash; 10</span></td>
          <td><strong>Nivel severo</strong></td>
          <td>Intervenci&oacute;n intensiva; considerar desintoxicaci&oacute;n hospitalaria.</td>
        </tr>
      </tbody>
    </table>`,
      },
      {
        title: 'DAST vs AUDIT',
        paragraphs: [
          'El DAST-10 y el <a href="/articulos/audit-test-alcoholismo.html">AUDIT</a> son instrumentos complementarios del mismo autor (Skinner/Gavin para DAST; WHO para AUDIT). El AUDIT eval&uacute;a consumo de riesgo, dependencia y consecuencias del alcohol; el DAST-10 eval&uacute;a problemas con otras drogas excluyendo alcohol y tabaco.',
          'En la pr&aacute;ctica cl&iacute;nica latinoamericana, el policonsumo es frecuente: alcohol como gateway y otras sustancias como cannabis, coca&iacute;na o benzodiacepinas. Administrar AUDIT + DAST-10 proporciona un perfil completo de consumo en menos de diez minutos.',
          'Las puntuaciones no son directamente comparables porque utilizan escalas y rangos diferentes. Sin embargo, un AUDIT &ge;8 combinado con DAST-10 &ge;3 sugiere policonsumo problem&aacute;tico que requiere evaluaci&oacute;n especializada y posible tratamiento integrado de adicciones.',
          'En pacientes en tratamiento psiqui&aacute;trico, el DAST-10 detecta uso de sustancias que puede interferir con medicaci&oacute;n psicotr&oacute;pica, comprometer adherencia al tratamiento o enmascarar s&iacute;ntomas psicopatol&oacute;gicos. La evaluaci&oacute;n rutinaria de sustancias debe ser est&aacute;ndar en psicolog&iacute;a cl&iacute;nica.',
        ],
      },
      {
        title: 'Uso cl&iacute;nico adicciones',
        paragraphs: [
          'En servicios especializados de adicciones, el DAST-10 funciona como medida de l&iacute;nea base y seguimiento de respuesta al tratamiento. La reducci&oacute;n del puntaje a lo largo del programa documenta progreso objetivo complementario a indicadores cl&iacute;nicos y de abstinencia.',
          'En consulta psicol&oacute;gica general, el DAST-10 identifica pacientes cuyo consumo de sustancias puede estar manteniendo o exacerbando s&iacute;ntomas depresivos, ansiosos o traum&aacute;ticos. La intervenci&oacute;n psicoterap&eacute;utica sin abordar el consumo frecuentemente produce resultados limitados.',
          'La entrevista motivacional posterior a un DAST-10 positivo explora ambivalencia hacia el cambio, consecuencias percibidas del consumo y recursos de apoyo disponibles. El psic&oacute;logo no debe asumir que un puntaje elevado implica disposici&oacute;n autom&aacute;tica para tratamiento de adicciones.',
          'En contextos forenses y laborales, el DAST-10 puede formar parte de evaluaciones de idoneidad, siempre con consentimiento informado y comprensi&oacute;n de que es tamizaje que requiere confirmaci&oacute;n cl&iacute;nica, no prueba de consumo actual (para ello existen toxicolog&iacute;as).',
        ],
      },
      {
        title: 'Consideraciones &eacute;ticas',
        paragraphs: [
          'La evaluaci&oacute;n de consumo de sustancias conlleva implicaciones &eacute;ticas significativas. El psic&oacute;logo debe informar al paciente sobre los l&iacute;mites de la confidencialidad: situaciones de riesgo grave, mandatos legales y pol&iacute;ticas institucionales que pueden requerir reporte.',
          'En menores de edad, la evaluaci&oacute;n de consumo de sustancias requiere considerar el marco legal local sobre consentimiento, confidencialidad y deber de protecci&oacute;n. En Colombia y M&eacute;xico, las normativas sobre salud de adolescentes permiten confidencialidad en ciertos contextos, pero el consumo de sustancias il&iacute;citas puede activar obligaciones de reporte.',
          'Los resultados del DAST-10 no deben utilizarse para estigmatizar, discriminar o coaccionar al paciente. El enfoque cl&iacute;nico debe ser de salud p&uacute;blica y reducci&oacute;n de da&ntilde;os, reconociendo que el consumo problem&aacute;tico es un problema de salud que responde a intervenci&oacute;n profesional.',
          'Documentar la administraci&oacute;n del DAST-10, su interpretaci&oacute;n y las decisiones cl&iacute;nicas derivadas protege al profesional y al paciente. Las plataformas digitales facilitan el registro confidencial y la trazabilidad de evaluaciones de sustancias en el expediente cl&iacute;nico.',
        ],
      },
      {
        title: 'DAST-10 en poblaciones espec&iacute;ficas',
        paragraphs: [
          'En adolescentes, el DAST-10 debe administrarse con adaptaciones en el lenguaje y consideraci&oacute;n del marco legal sobre confidencialidad. La detecci&oacute;n temprana de consumo problem&aacute;tico en esta poblaci&oacute;n permite intervenci&oacute;n breve antes de que el patr&oacute;n de uso se consolide en dependencia adulta.',
          'En pacientes con trastornos psiqui&aacute;tricos com&oacute;rbiles, el DAST-10 ayuda a identificar automedicaci&oacute;n con benzodiacepinas, cannabis u opioides que puede interferir con el tratamiento psicoterap&eacute;utico o farmacol&oacute;gico. La evaluaci&oacute;n de sustancias debe ser rutina en ingreso a servicios de salud mental.',
          'En contextos perinatales, el consumo de sustancias tiene implicaciones para la salud materna y fetal. Aunque el DAST-10 no fue validado espec&iacute;ficamente en embarazo, puede orientar la necesidad de evaluaci&oacute;n especializada y coordinaci&oacute;n con obstetricia.',
          'En poblaciones privadas de libertad o en tratamiento por delitos relacionados con sustancias, el DAST-10 complementa historias cl&iacute;nicas forenses. Interpretar resultados en contexto evita stigmatizaci&oacute;n y orienta planes de reinserci&oacute;n basados en evidencia.',
        ],
      },
      {
        title: 'Seguimiento y reevaluaci&oacute;n',
        paragraphs: [
          'Readministrar el DAST-10 cada tres a seis meses durante tratamiento de adicciones documenta respuesta objetiva. Una reducci&oacute;n sostenida del puntaje complementa indicadores cl&iacute;nicos de abstinencia, mejor&iacute;a funcional y adherencia terap&eacute;utica.',
          'Si el puntaje aumenta durante el tratamiento, explorar reca&iacute;da, consumo oculto o factores estresores que reactiven el patr&oacute;n de uso. El DAST-10 no detecta consumo reciente directamente, pero s&iacute; consecuencias que suelen acompa&ntilde;ar reca&iacute;das.',
          'Integrar DAST-10 con <a href="/articulos/audit-test-alcoholismo.html">AUDIT</a> en cada evaluaci&oacute;n de seguimiento proporciona perfil completo de consumo. Muchos pacientes reducen drogas il&iacute;citas pero incrementan alcohol, patr&oacute;n que el DAST-10 solo no detectar&iacute;a.',
          'Las plataformas digitales facilitan alertas autom&aacute;ticas cuando el puntaje supera umbrales de riesgo en reevaluaciones, permitiendo intervenci&oacute;n oportuna antes de escalada a consumo severo.',
          'En consulta privada, incluir el DAST-10 como parte del intake estandarizado normaliza la conversaci&oacute;n sobre sustancias y reduce el estigma asociado a preguntas directas sobre drogas en sesiones posteriores.',
        ],
      },
      {
        title: 'Limitaciones del DAST-10',
        paragraphs: [
          'El DAST-10 no detecta consumo reciente ni cuantifica frecuencia o cantidad de sustancias. Un paciente en abstinencia reciente puede puntuar alto por consecuencias pasadas, mientras que un consumidor activo ocasional puede puntuar bajo si a&uacute;n no experimenta problemas.',
          'No eval&uacute;a alcohol ni tabaco: debe complementarse con <a href="/articulos/audit-test-alcoholismo.html">AUDIT</a> y preguntas directas sobre nicotina. El policonsumo requiere bater&iacute;a integrada, no DAST-10 aislado.',
          'En poblaciones donde el consumo de cannabis est&aacute; parcialmente legalizado o normalizado socialmente, interpretar respuestas requiere contextualizaci&oacute;n cl&iacute;nica sobre deterioro funcional, no solo presencia de consumo.',
          'Como todo autoinforme, est&aacute; sujeto a minimizaci&oacute;n por verg&uuml;enza o maximizaci&oacute;n en contextos forenses. La entrevista cl&iacute;nica posterior al tamizaje valida y enriquece los resultados del cuestionario.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'scoff-trastornos-alimentarios',
      filename: 'scoff-trastornos-alimentarios.html',
      title: 'SCOFF: Tamizaje de Trastornos Alimentarios — guía clínica | Kalyo',
      description:
        'Guía del cuestionario SCOFF: 5 ítems, punto de corte ≥2, uso en adolescentes, comparación con EDE-Q y derivación. Tamizaje digital en Kalyo.',
      keywords: 'SCOFF, trastornos alimentarios, anorexia, bulimia, tamizaje adolescentes, psicología clínica',
      metaLabel: CLINICAL_META,
      h1: 'SCOFF: Cuestionario de Tamizaje de Trastornos Alimentarios',
      intro:
        'El cuestionario SCOFF es un instrumento de tamizaje de cinco &iacute;tems dise&ntilde;ado para detectar probable anorexia nerviosa y bulimia nerviosa en atenci&oacute;n primaria. Desarrollado por Morgan, Reid y Lacey, su acr&oacute;nimo (Sick, Control, One stone, Fat, Food) resume las preguntas clave sobre conductas y cogniciones alimentarias de riesgo. Su extrema brevedad lo hace ideal para consulta pedi&aacute;trica, ginecol&oacute;gica y psicol&oacute;gica.',
      heroAlt: 'SCOFF trastornos alimentarios en tablet con interfaz clínica púrpura',
      inlineAlt: 'Gráfico interpretación SCOFF 5 ítems tamizaje alimentario púrpura',
      ctaTitle: 'Tamiza trastornos alimentarios con el SCOFF en Kalyo',
      ctaText: 'Detecta se&ntilde;ales de alerta temprana con el SCOFF y documenta la evaluaci&oacute;n en el expediente cl&iacute;nico digital.',
      ctaButton: 'Prueba gratis 7 d&iacute;as &rarr;',
      related: [
        ['evaluacion-riesgo-suicida', 'Evaluaci&oacute;n de Riesgo Suicida'],
        ['epds-depresion-postnatal-edimburgo', 'EPDS: Depresi&oacute;n Postnatal'],
        ['que-es-el-phq-9', '&iquest;Qu&eacute; es el PHQ-9?'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; es el SCOFF?',
        paragraphs: [
          'El SCOFF fue desarrollado en 1999 como herramienta de tamizaje para m&eacute;dicos de atenci&oacute;n primaria que atienden pacientes con posibles trastornos alimentarios. Consta de cinco preguntas de s&iacute;/no que exploran conductas centrales de anorexia y bulimia: v&oacute;mitos autoinducidos, p&eacute;rdida de control sobre la alimentaci&oacute;n, p&eacute;rdida de peso significativa, imagen corporal distorsionada y preocupaci&oacute;n obsesiva por la comida.',
          'A diferencia de cuestionarios extensos como el EDE-Q (Eating Disorder Examination Questionnaire), el SCOFF prioriza la sensibilidad sobre la especificidad: est&aacute; dise&ntilde;ado para no pasar por alto casos probables, aceptando algunos falsos positivos que se resuelven con evaluaci&oacute;n cl&iacute;nica posterior.',
          'El instrumento ha sido validado en m&uacute;ltiples pa&iacute;ses y poblaciones, incluidos adolescentes y adultos j&oacute;venes. Su administraci&oacute;n toma menos de dos minutos y puede integrarse en evaluaciones rutinarias de salud mental en consulta psicol&oacute;gica, pedi&aacute;trica y de medicina general.',
          'El SCOFF no diagnostica trastornos alimentarios ni eval&uacute;a trastorno por atrac&oacute;n u otros trastornos de la conducta alimentaria del DSM-5. Un resultado positivo activa la necesidad de evaluaci&oacute;n especializada con entrevista cl&iacute;nica estructurada y, cuando corresponda, evaluaci&oacute;n m&eacute;dica de complicaciones f&iacute;sicas.',
        ],
      },
      {
        title: '5 &iacute;tems S-C-O-F-F',
        paragraphs: [
          'Los cinco &iacute;tems del SCOFF corresponden al acr&oacute;nimo: S (&laquo;&iquest;Te haces vomitar porque te sientes inc&oacute;modamente lleno/a?&raquo;), C (&laquo;&iquest;Te preocupa que hayas perdido el control sobre cu&aacute;nto comes?&raquo;), O (&laquo;&iquest;Has perdido m&aacute;s de 6 kg en un periodo de tres meses?&raquo;), F (&laquo;&iquest;Crees que est&aacute;s gordo/a cuando otros dicen que est&aacute;s demasiado delgado/a?&raquo;) y F (&laquo;&iquest;Dir&iacute;as que la comida domina tu vida?&raquo;).',
          'Cada respuesta afirmativa suma un punto. El rango total es 0 a 5. La formulaci&oacute;n exacta de los &iacute;tems puede variar ligeramente seg&uacute;n la traducci&oacute;n validada, pero el contenido sem&aacute;ntico se mantiene: v&oacute;mitos, p&eacute;rdida de control, p&eacute;rdida de peso, imagen corporal y preocupaci&oacute;n alimentaria.',
          'El cl&iacute;nico debe administrar el SCOFF en un contexto privado y de confianza, especialmente con adolescentes que pueden minimizar s&iacute;ntomas por verg&uuml;enza o negaci&oacute;n. Explicar que las preguntas son rutinarias y que buscan ofrecer apoyo, no juzgar, facilita respuestas honestas.',
          'En la pr&aacute;ctica cl&iacute;nica, conviene complementar el SCOFF con exploraci&oacute;n de ejercicio compulsivo, uso de laxantes/diur&eacute;ticos, restricci&oacute;n cal&oacute;rica extrema y se&ntilde;ales f&iacute;sicas (amenorrea, bradicardia, hipotensi&oacute;n ortost&aacute;tica) que no est&aacute;n cubiertas por los cinco &iacute;tems.',
        ],
      },
      {
        title: 'Punto corte &ge;2',
        paragraphs: [
          'El punto de corte m&aacute;s ampliamente utilizado para el SCOFF es &ge;2 respuestas afirmativas para identificar casos probables de trastorno alimentario. Este umbral ha demostrado sensibilidad superior al 90% en estudios de validaci&oacute;n, con especificidad variable seg&uacute;n la poblaci&oacute;n (generalmente 80-90%).',
          'Un puntaje de 0-1 generalmente descarta trastorno alimentario cl&iacute;nico, aunque no excluye preocupaci&oacute;n corporal leve o conductas alimentarias subcl&iacute;nicas que merecen psicoeducaci&oacute;n. Un puntaje &ge;2 activa evaluaci&oacute;n especializada inmediata.',
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
          <td><span class="score-badge">0 &ndash; 1</span></td>
          <td><strong>Probable ausencia de trastorno alimentario</strong></td>
          <td>Monitoreo; psicoeducaci&oacute;n sobre imagen corporal si hay quejas.</td>
        </tr>
        <tr>
          <td><span class="score-badge">&ge; 2</span></td>
          <td><strong>Probable trastorno alimentario</strong></td>
          <td>Evaluaci&oacute;n especializada; valoraci&oacute;n m&eacute;dica; derivaci&oacute;n.</td>
        </tr>
      </tbody>
    </table>`,
      },
      {
        title: 'Adolescentes',
        paragraphs: [
          'Los trastornos alimentarios tienen pico de inicio en la adolescencia y adultez temprana. El SCOFF es especialmente valioso en tamizaje escolar, consulta pedi&aacute;trica y psicolog&iacute;a adolescente, donde la detecci&oacute;n temprana puede prevenir complicaciones m&eacute;dicas graves como desnutrici&oacute;n, osteoporosis, alteraciones electrol&iacute;ticas y riesgo cardiovascular.',
          'En adolescentes, factores de riesgo incluyen bullying por peso, presi&oacute;n sociocultural por delgadez, pr&aacute;cticas deportivas con control de peso extremo, historial de dieta en la familia y comorbilidad con ansiedad o depresi&oacute;n medible con el <a href="/articulos/que-es-el-phq-9.html">PHQ-9</a>.',
          'La administraci&oacute;n del SCOFF a menores requiere considerar el marco legal sobre consentimiento y confidencialidad. En muchos contextos, los adolescentes pueden recibir evaluaci&oacute;n de salud mental con confidencialidad parcial, pero los trastornos alimentarios con riesgo m&eacute;dico pueden requerir involucrar a padres o tutores.',
          'Ante SCOFF positivo en adolescente, la evaluaci&oacute;n m&eacute;dica es prioritaria para descartar complicaciones f&iacute;sicas antes o paralelamente a la intervenci&oacute;n psicol&oacute;gica. La anorexia nerviosa tiene la tasa de mortalidad m&aacute;s alta entre trastornos psiqui&aacute;tricos.',
        ],
      },
      {
        title: 'SCOFF vs EDE-Q',
        paragraphs: [
          'El SCOFF y el Eating Disorder Examination Questionnaire (EDE-Q) responden a necesidades cl&iacute;nicas diferentes. El SCOFF es tamizaje ultrabreve (2 minutos) orientado a detecci&oacute;n s&iacute;/no de casos probables. El EDE-Q es cuestionario extenso (28+ &iacute;tems) que eval&uacute;a frecuencia y severidad de conductas y cogniciones alimentarias espec&iacute;ficas con subescalas.',
          'En atenci&oacute;n primaria y consulta psicol&oacute;gica general, el SCOFF es la herramienta de elecci&oacute;n para tamizaje rutinario. Cuando el SCOFF es positivo (&ge;2), el EDE-Q o entrevista cl&iacute;nica estructurada (EDE) permiten caracterizar el trastorno, evaluar severidad y planificar tratamiento especializado.',
          'El EDE-Q requiere mayor tiempo de administraci&oacute;n y capacitaci&oacute;n para interpretaci&oacute;n. No es viable como tamizaje universal, pero es indispensable en unidades especializadas de trastornos alimentarios para evaluaci&oacute;n diagn&oacute;stica y seguimiento de respuesta al tratamiento.',
          'La secuencia cl&iacute;nica recomendada es: SCOFF (tamizaje) &rarr; evaluaci&oacute;n m&eacute;dica + EDE-Q o entrevista cl&iacute;nica (confirmaci&oacute;n) &rarr; tratamiento multidisciplinario (psicolog&iacute;a, nutrici&oacute;n, psiquiatr&iacute;a, medicina).',
        ],
      },
      {
        title: 'Derivar especialista',
        paragraphs: [
          'Ante SCOFF &ge;2, la derivaci&oacute;n a especialista en trastornos alimentarios est&aacute; indicada de forma urgente, especialmente si coexisten se&ntilde;ales m&eacute;dicas de alarma: p&eacute;rdida de peso &gt;15% en tres meses, bradicardia, hipotensi&oacute;n, amenorrea, alteraciones electrol&iacute;ticas o ideaci&oacute;n suicida evaluada con protocolos de <a href="/articulos/evaluacion-riesgo-suicida.html">riesgo suicida</a>.',
          'La derivaci&oacute;n debe ser caliente (con contacto directo entre profesionales), no fr&iacute;a (simple referencia escrita). Los trastornos alimentarios tienen alta tasa de no adherencia a tratamiento; la coordinaci&oacute;n entre el profesional que detecta y el especialista incrementa la probabilidad de atenci&oacute;n efectiva.',
          'En contextos con escasez de especialistas, el psic&oacute;logo general puede iniciar psicoeducaci&oacute;n, estabilizaci&oacute;n m&eacute;dica b&aacute;sica y monitoreo mientras se gestiona la derivaci&oacute;n. Sin embargo, la anorexia nerviosa con bajo peso significativo requiere manejo multidisciplinario especializado.',
          'Documentar el resultado del SCOFF, las se&ntilde;ales de alarma identificadas, la derivaci&oacute;n realizada y el seguimiento de la referencia es esencial para la continuidad de la atenci&oacute;n y la protecci&oacute;n legal del profesional.',
        ],
      },
      {
        title: 'Marco legal menores',
        paragraphs: [
          'La evaluaci&oacute;n de trastornos alimentarios en menores intersecta con normativas de consentimiento informado, confidencialidad, protecci&oacute;n de la infancia y reporte de maltrato. En Colombia, la Ley 1090 y el C&oacute;digo de Infancia y Adolescencia regulan la atenci&oacute;n a menores; en M&eacute;xico, la Ley General de los Derechos de Ni&ntilde;as, Ni&ntilde;os y Adolescentes establece principios similares.',
          'Cuando el trastorno alimentario pone en riesgo la vida o integridad f&iacute;sica del menor (anorexia con desnutrici&oacute;n severa), el psic&oacute;logo puede estar obligado a involucrar a padres/tutores y, en casos extremos, activar protecci&oacute;n legal o hospitalizaci&oacute;n involuntaria seg&uacute;n la legislaci&oacute;n local.',
          'La confidencialidad del adolescente debe balancearse con el deber de protecci&oacute;n. Se recomienda explicar al menor desde el inicio los l&iacute;mites de la confidencialidad: &laquo;Lo que compartas es confidencial, excepto si hay riesgo grave para tu salud f&iacute;sica o vida&raquo;.',
          'En casos de sospecha de trastorno alimentario inducido por adultos (alimentaci&oacute;n forzada, restricci&oacute;n extrema impuesta) o asociado a abuso, el psic&oacute;logo debe activar protocolos de reporte a autoridades de protecci&oacute;n de menores conforme a la ley vigente en su jurisdicci&oacute;n.',
          'Capacitaci&oacute;n en trastornos alimentarios antes de usar el SCOFF de forma rutinaria mejora la calidad de la derivaci&oacute;n y reduce respuestas cl&iacute;nicas inadecuadas ante pacientes con riesgo m&eacute;dico alto.',
        ],
      },
      {
        title: 'SCOFF en consulta psicol&oacute;gica general',
        paragraphs: [
          'Integrar el SCOFF en la evaluaci&oacute;n inicial de adolescentes y adultos j&oacute;venes con quejas de imagen corporal, ansiedad social o perfeccionismo incrementa la detecci&oacute;n temprana. Muchos pacientes no verbalizan conductas alimentarias patol&oacute;gicas sin preguntas directas.',
          'Cuando el SCOFF es negativo pero persisten se&ntilde;ales cl&iacute;nicas (fluctuaciones de peso, evitaci&oacute;n de comidas sociales, ejercicio compulsivo), profundizar con entrevista cl&iacute;nica. El SCOFF tiene alta sensibilidad pero no especificidad perfecta.',
          'En varones, los trastornos alimentarios est&aacute;n subdiagnosticados. El SCOFF aplica igualmente, aunque la presentaci&oacute;n puede enfatizar musculatura y ejercicio extremo m&aacute;s que restricci&oacute;n cal&oacute;rica cl&aacute;sica.',
          'Documentar SCOFF, exploraci&oacute;n complementaria y decisiones de derivaci&oacute;n en el expediente protege al profesional y mejora continuidad si el paciente es referido a unidad especializada de trastornos alimentarios.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'aces-adversidad-infantil',
      filename: 'aces-adversidad-infantil.html',
      title: 'ACEs: Experiencias Adversas en la Infancia — guía clínica | Kalyo',
      description:
        'Guía de ACEs: 10 categorías de adversidad infantil, puntuación ≥4 riesgo, trauma complejo, entrevista clínica y validación Colombia/México.',
      keywords: 'ACEs, adversidad infantil, trauma infantil, experiencias adversas, psicología clínica, salud mental',
      metaLabel: CLINICAL_META,
      h1: 'ACEs: Cuestionario de Experiencias Adversas en la Infancia',
      intro:
        'El cuestionario de Adverse Childhood Experiences (ACEs) eval&uacute;a la exposici&oacute;n a diez categor&iacute;as de adversidad durante la infancia y adolescencia. Originado en el estudio de Kaiser Permanente y CDC, ha demostrado correlaci&oacute;n robusta entre trauma infantil y riesgo de problemas de salud mental, f&iacute;sica y conductual en la adultez. Para psic&oacute;logos cl&iacute;nicos, los ACEs enriquecen la formulaci&oacute;n del caso con perspectiva traumatol&oacute;gica.',
      heroAlt: 'ACEs adversidad infantil en tablet con interfaz clínica púrpura',
      inlineAlt: 'Gráfico 10 categorías ACEs trauma infantil psicología púrpura',
      ctaTitle: 'Eval&uacute;a historial de adversidad con ACEs en Kalyo',
      ctaText: 'Integra la evaluaci&oacute;n de ACEs con escalas de trauma y depresi&oacute;n en bater&iacute;as cl&iacute;nicas digitales seguras.',
      ctaButton: 'Prueba gratis 7 d&iacute;as &rarr;',
      related: [
        ['evaluacion-riesgo-suicida', 'Evaluaci&oacute;n de Riesgo Suicida'],
        ['escala-pcl-5-estres-postraumatico', 'Escala PCL-5: Estr&eacute;s Postraum&aacute;tico'],
        ['escala-dass-21', 'DASS-21: Depresi&oacute;n, Ansiedad y Estr&eacute;s'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; son los ACEs?',
        paragraphs: [
          'Las Adverse Childhood Experiences (ACEs) son eventos estresantes o traum&aacute;ticos ocurridos antes de los 18 a&ntilde;os que incrementan el riesgo de problemas de salud a lo largo del ciclo vital. El cuestionario ACE eval&uacute;a diez categor&iacute;as agrupadas en tres dominios: abuso (f&iacute;sico, emocional, sexual), neglecto (f&iacute;sico, emocional) y disfunci&oacute;n familiar (violencia dom&eacute;stica, consumo de sustancias, enfermedad mental, separaci&oacute;n, encarcelamiento).',
          'El estudio original de Felitti y colaboradores (1998) demostr&oacute; una relaci&oacute;n dosis-respuesta: a mayor n&uacute;mero de ACEs, mayor riesgo de depresi&oacute;n, ansiedad, consumo de sustancias, enfermedades cr&oacute;nicas, conductas de riesgo y mortalidad prematura. Esta evidencia ha transformado la comprensi&oacute;n de la salud mental desde un modelo biom&eacute;dico hacia un enfoque biopsicosocial integrado.',
          'Para el psic&oacute;logo cl&iacute;nico, los ACEs no diagnostican trastornos, pero proporcionan contexto developmental crucial para comprender s&iacute;ntomas actuales, patrones relacionales, mecanismos de afrontamiento y vulnerabilidad a estr&eacute;s. Un paciente con m&uacute;ltiples ACEs frecuentemente presenta trauma complejo m&aacute;s que un evento traum&aacute;tico &uacute;nico.',
          'El cuestionario ACE es de dominio p&uacute;blico y puede administrarse libremente. Existen versiones abreviadas y adaptaciones culturales, pero la versi&oacute;n est&aacute;ndar de 10 &iacute;tems permanece como referencia internacional.',
        ],
      },
      {
        title: '10 categor&iacute;as',
        paragraphs: [
          'Las diez categor&iacute;as de ACEs eval&uacute;an: (1) abuso emocional (&laquo;&iquest;Un adulto te insult&oacute; o humill&oacute; frecuentemente?&raquo;), (2) abuso f&iacute;sico, (3) abuso sexual, (4) neglecto emocional (&laquo;&iquest;Sentiste que nadie en tu familia te quer&iacute;a?&raquo;), (5) neglecto f&iacute;sico, (6) violencia dom&eacute;stica hacia la madre o figura materna, (7) consumo de alcohol o drogas en el hogar, (8) enfermedad mental de un miembro del hogar, (9) encarcelamiento de un miembro del hogar, y (10) separaci&oacute;n o divorcio de los padres.',
          'Cada categor&iacute;a se responde s&iacute;/no. El puntaje total es la suma de categor&iacute;as afirmativas, con rango de 0 a 10. No se ponderan por severidad: un ACE cuenta igual independientemente de su intensidad o duraci&oacute;n, aunque la exploraci&oacute;n cl&iacute;nica posterior debe profundizar en estos matices.',
          'Es fundamental aclarar al paciente que las preguntas se refieren a experiencias antes de los 18 a&ntilde;os, no a situaciones actuales. Algunos pacientes pueden experimentar reactivaci&oacute;n emocional al responder; el cl&iacute;nico debe estar preparado para contenci&oacute;n y evaluaci&oacute;n de seguridad si es necesario.',
          'Los ACEs no capturan todas las formas de adversidad infantil (pobreza extrema, discriminaci&oacute;n, migraci&oacute;n forzada, violencia comunitaria, bullying severo). Conviene complementar con exploraci&oacute;n abierta de otras experiencias traum&aacute;ticas relevantes para la formulaci&oacute;n del caso.',
        ],
      },
      {
        title: 'Puntuaci&oacute;n &ge;4 riesgo',
        paragraphs: [
          'La investigaci&oacute;n original estableci&oacute; que acumular cuatro o m&aacute;s ACEs incrementa significativamente el riesgo de problemas de salud mental y f&iacute;sica en la adultez. Pacientes con ACE &ge;4 tienen mayor probabilidad de depresi&oacute;n, ansiedad, TEPT, consumo de sustancias, conductas autolesivas y enfermedades cr&oacute;nicas.',
          'Un puntaje de 0-3 no descarta trauma ni problemas actuales, pero indica menor carga acumulada de adversidad infantil. Un puntaje &ge;4 activa evaluaci&oacute;n traumatol&oacute;gica ampliada con instrumentos como el <a href="/articulos/escala-pcl-5-estres-postraumatico.html">PCL-5</a> y el <a href="/articulos/escala-dass-21.html">DASS-21</a>.',
        ],
        extra: `
    <table class="severity-table">
      <thead>
        <tr>
          <th>Puntuaci&oacute;n ACE</th>
          <th>Nivel de riesgo</th>
          <th>Acci&oacute;n cl&iacute;nica</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="score-badge">0</span></td>
          <td><strong>Sin ACEs reportados</strong></td>
          <td>Evaluaci&oacute;n est&aacute;ndar; explorar otras adversidades no capturadas.</td>
        </tr>
        <tr>
          <td><span class="score-badge">1 &ndash; 3</span></td>
          <td><strong>Riesgo moderado</strong></td>
          <td>Explorar impacto developmental; evaluar comorbilidad emocional.</td>
        </tr>
        <tr>
          <td><span class="score-badge">&ge; 4</span></td>
          <td><strong>Alto riesgo</strong></td>
          <td>Evaluaci&oacute;n traumatol&oacute;gica completa; PCL-5; plan de estabilizaci&oacute;n.</td>
        </tr>
      </tbody>
    </table>`,
      },
      {
        title: 'ACEs y trauma complejo',
        paragraphs: [
          'El trauma complejo (C-PTSD) se diferencia del TEPT cl&aacute;sico por su origen en exposici&oacute;n prolongada y repetida a adversidad interpersonal durante el desarrollo, t&iacute;picamente en contextos donde el perpetrador es una figura de apego. Los ACEs &ge;4 son uno de los indicadores m&aacute;s robustos de trauma complejo.',
          'Las secuelas del trauma complejo incluyen dificultades de regulaci&oacute;n emocional, alteraciones en la identidad y autoestima, problemas interpersonales cr&oacute;nicos, somatizaci&oacute;n, disociaci&oacute;n y vulnerabilidad a re-victimizaci&oacute;n. Estos pacientes frecuentemente no responden a protocolos est&aacute;ndar de TEPT dise&ntilde;ados para trauma &uacute;nico.',
          'La intervenci&oacute;n en trauma complejo requiere fases: estabilizaci&oacute;n y seguridad, procesamiento traum&aacute;tico y reintegraci&oacute;n. Enfoques como DBT, EMDR adaptado, terapia centrada en trauma complejo (CPT) y modelos de fase son preferibles a exposici&oacute;n directa prematura.',
          'El <a href="/articulos/escala-pcl-5-estres-postraumatico.html">PCL-5</a> eval&uacute;a s&iacute;ntomas de TEPT seg&uacute;n DSM-5, pero puede subestimar trauma complejo. La evaluaci&oacute;n ACE complementa el PCL-5 con perspectiva developmental que enriquece la formulaci&oacute;n y orienta la selecci&oacute;n de intervenci&oacute;n.',
        ],
      },
      {
        title: 'Introducir en entrevista',
        paragraphs: [
          'Administrar ACEs requiere sensibilidad cl&iacute;nica. Se recomienda introducir el cuestionario despu&eacute;s de establecer rapport, explicando su prop&oacute;sito: &laquo;Estas preguntas nos ayudan a comprender experiencias de tu infancia que pueden estar relacionadas con lo que vives hoy. Puedes responder solo lo que te sientas c&oacute;modo/a compartiendo&raquo;.',
          'El cl&iacute;nico debe monitorear la activaci&oacute;n emocional del paciente durante la administraci&oacute;n. Si el paciente se disocia, llora inconsolablemente o presenta crisis, se pausa la evaluaci&oacute;n para contenci&oacute;n y t&eacute;cnicas de grounding antes de continuar o posponer.',
          'No todos los pacientes con ACEs elevados desean procesar el trauma inmediatamente. Algunos requieren meses de estabilizaci&oacute;n antes de abordar material traum&aacute;tico. Respetar el ritmo del paciente es fundamental en trauma-informed care.',
          'Documentar los ACEs en la historia cl&iacute;nica (con consentimiento) facilita la continuidad de la atenci&oacute;n y evita que el paciente deba repetir narrativas traum&aacute;ticas con cada profesional. Las plataformas digitales permiten registro seguro y acceso controlado a esta informaci&oacute;n sensible.',
        ],
      },
      {
        title: 'Colombia/M&eacute;xico',
        paragraphs: [
          'En Colombia, estudios sobre ACEs en poblaciones urbanas y expuestas a conflicto armado han documentado prevalencias elevadas de adversidad infantil, especialmente en regiones afectadas por violencia. La validaci&oacute;n cultural debe considerar que categor&iacute;as como &laquo;encarcelamiento&raquo; y &laquo;violencia dom&eacute;stica&raquo; pueden tener expresiones contextuales espec&iacute;ficas.',
          'En M&eacute;xico, investigaciones en contextos de pobreza, migraci&oacute;n y violencia comunitaria han adaptado el cuestionario ACE. Algunos estudios a&ntilde;aden categor&iacute;as locales (testigo de homicidio, desplazamiento forzado) que enriquecen la evaluaci&oacute;n pero impiden comparaci&oacute;n directa con baremos internacionales.',
          'El psic&oacute;logo en Colombia debe considerar la Ley 1090 y protocolos de reporte cuando los ACEs revelan abuso sexual actual de menores o situaciones de riesgo inminente. En M&eacute;xico, la NOM-004 y leyes de protecci&oacute;n de menores establecen obligaciones similares.',
          'La evaluaci&oacute;n de ACEs en contextos latinoamericanos debe integrar variables socioculturales: resiliencia comunitaria, apoyo familiar extendido, espiritualidad y factores protectores que modulan el impacto de la adversidad infantil.',
        ],
      },
      {
        title: 'Consideraciones &eacute;ticas',
        paragraphs: [
          'Administrar ACEs puede reactivar trauma no procesado. El psic&oacute;logo debe contar con competencia en evaluaci&oacute;n traumatol&oacute;gica y protocolos de crisis antes de incorporar ACEs rutinariamente en su pr&aacute;ctica. No es un cuestionario para aplicar sin preparaci&oacute;n cl&iacute;nica.',
          'La confidencialidad de la informaci&oacute;n sobre abuso infantil tiene l&iacute;mites legales cuando existe riesgo para menores actuales en el entorno del paciente (p. ej., hijos del paciente en situaci&oacute;n de abuso). El profesional debe conocer sus obligaciones de reporte en su jurisdicci&oacute;n.',
          'Los ACEs no determinismo: muchas personas con puntuaciones altas desarrollan resiliencia y funcionamiento adaptativo. La interpretaci&oacute;n debe evitar mensajes de fatalismo (&laquo;tu infancia conden&oacute; tu futuro&raquo;) y enfatizar posibilidades de sanaci&oacute;n y crecimiento postraum&aacute;tico.',
          'Ante ACE &ge;4 con ideaci&oacute;n suicida o autolesiones, activar protocolos de <a href="/articulos/evaluacion-riesgo-suicida.html">evaluaci&oacute;n de riesgo suicida</a> es prioritario. El trauma infantil incrementa significativamente el riesgo suicida en adultos, especialmente con comorbilidad depresiva.',
          'Formaci&oacute;n en trauma-informed care antes de incorporar ACEs a la pr&aacute;ctica rutinaria es inversi&oacute;n esencial. El cl&iacute;nico debe contar con red de derivaci&oacute;n, supervisi&oacute;n cl&iacute;nica y autocuidado para sostener este tipo de evaluaciones.',
        ],
      },
      {
        title: 'Factores protectores y resiliencia',
        paragraphs: [
          'Los ACEs cuantifican adversidad, pero no miden factores protectores: figuras de apego seguro, apoyo comunitario, acceso a educaci&oacute;n, espiritualidad o intervenciones tempranas que mitigan el impacto del trauma infantil.',
          'En formulaci&oacute;n cl&iacute;nica, integrar ACEs con exploraci&oacute;n de fortalezas y recursos de afrontamiento evita narrativas de victimizaci&oacute;n. Pacientes con ACE elevados y factores protectores robustos pueden tener mejor pron&oacute;stico que puntajes similares sin red de apoyo.',
          'Intervenciones basadas en resiliencia complementan el procesamiento traum&aacute;tico: construcci&oacute;n de habilidades sociales, regulaci&oacute;n emocional, conexi&oacute;n comunitaria y sentido de prop&oacute;sito son objetivos terap&eacute;uticos tan importantes como reducir s&iacute;ntomas.',
          'Readministrar ACEs no es recomendable en seguimiento (experiencias infantiles no cambian), pero s&iacute; monitorizar s&iacute;ntomas actuales con <a href="/articulos/escala-dass-21.html">DASS-21</a> y <a href="/articulos/escala-pcl-5-estres-postraumatico.html">PCL-5</a> para evaluar respuesta terap&eacute;utica.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'c-ssrs-escala-columbia-suicidio',
      filename: 'c-ssrs-escala-columbia-suicidio.html',
      title: 'C-SSRS: Escala Columbia de Riesgo Suicida — guía clínica | Kalyo',
      description:
        'Guía de la C-SSRS: versiones completa y breve, ideación vs conducta, administración, puntuación, protocolo de seguridad y documentación.',
      keywords: 'C-SSRS, Columbia, riesgo suicida, escala suicidio, evaluación clínica, psicología, protocolo seguridad',
      metaLabel: CLINICAL_META,
      h1: 'C-SSRS: Escala Columbia de Severidad del Riesgo Suicida',
      intro:
        'La Columbia-Suicide Severity Rating Scale (C-SSRS) es un instrumento estandarizado para evaluar severidad de ideaci&oacute;n suicida y comportamiento suicida. Desarrollada por investigadores de la Universidad de Columbia con apoyo del NIMH, ha sido adoptada por instituciones de salud mental, servicios de emergencia y programas de prevenci&oacute;n en todo el mundo. Su estructura jer&aacute;rquica permite clasificar el riesgo y activar protocolos de seguridad graduados.',
      heroAlt: 'C-SSRS escala Columbia riesgo suicida en tablet interfaz clínica púrpura',
      inlineAlt: 'Diagrama C-SSRS ideación conducta suicida protocolo seguridad púrpura',
      ctaTitle: 'Eval&uacute;a riesgo suicida con protocolos seguros en Kalyo',
      ctaText: 'Integra evaluaci&oacute;n de riesgo suicida con documentaci&oacute;n cl&iacute;nica y planes de seguridad en plataforma digital.',
      ctaButton: 'Prueba gratis 7 d&iacute;as &rarr;',
      related: [
        ['evaluacion-riesgo-suicida', 'Evaluaci&oacute;n de Riesgo Suicida'],
        ['sivigila-psicologia-colombia', 'SIVIGILA y Psicolog&iacute;a en Colombia'],
        ['escala-pcl-5-estres-postraumatico', 'Escala PCL-5: Estr&eacute;s Postraum&aacute;tico'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; es la C-SSRS?',
        paragraphs: [
          'La C-SSRS fue desarrollada por Posner, Brown y colaboradores en la Columbia University y el New York State Psychiatric Institute como respuesta a la necesidad de un instrumento estandarizado, validado y de dominio p&uacute;blico para evaluar riesgo suicida. A diferencia de preguntas aisladas sobre ideaci&oacute;n, la C-SSRS eval&uacute;a sistem&aacute;ticamente la severidad de pensamientos suicidas y la historia de comportamiento suicida.',
          'El instrumento se basa en la distinci&oacute;n entre ideaci&oacute;n suicida (pensamientos) y comportamiento suicida (intentos, preparaci&oacute;n, conductas). Esta diferenciaci&oacute;n es cl&iacute;nicamente crucial: un paciente puede tener ideaci&oacute;n pasiva sin plan ni intento, o ideaci&oacute;n activa con plan espec&iacute;fico que requiere intervenci&oacute;n inmediata.',
          'La C-SSRS ha sido validada en m&uacute;ltiples poblaciones (adultos, adolescentes, ancianos, pacientes psiqui&aacute;tricos, servicios de emergencia) y est&aacute; disponible en espa&ntilde;ol. Es utilizada por la FDA en ensayos cl&iacute;nicos de psicofarmacolog&iacute;a y por sistemas de salud como herramienta est&aacute;ndar de triage suicida.',
          'Para psic&oacute;logos cl&iacute;nicos, la C-SSRS complementa (no reemplaza) la entrevista cl&iacute;nica de riesgo suicida descrita en nuestra gu&iacute;a de <a href="/articulos/evaluacion-riesgo-suicida.html">evaluaci&oacute;n de riesgo suicida</a>, proporcionando estructura y lenguaje com&uacute;n para documentaci&oacute;n y comunicaci&oacute;n interdisciplinaria.',
        ],
      },
      {
        title: 'Completa vs breve',
        paragraphs: [
          'La C-SSRS existe en versi&oacute;n completa (Full Scale) y versiones abreviadas (Screen Version, Since Last Visit). La versi&oacute;n completa eval&uacute;a ideaci&oacute;n suicida en cinco niveles de severidad, comportamiento suicida (intentos, interrupciones, preparaci&oacute;n, conducta) e intensidad de ideaci&oacute;n cuando est&aacute; presente.',
          'La versi&oacute;n breve (screening) contiene las preguntas esenciales para triage r&aacute;pido en atenci&oacute;n primaria, servicios de urgencias y consulta psicol&oacute;gica rutinaria. Pregunta sobre deseo de morir, pensamientos activos/pasivos, ideaci&oacute;n con m&eacute;todo, ideaci&oacute;n con plan e intentos previos.',
          'En consulta psicol&oacute;gica ambulatoria, la versi&oacute;n breve es generalmente suficiente para evaluaci&oacute;n inicial y seguimiento peri&oacute;dico. La versi&oacute;n completa se reserva para evaluaciones especializadas, hospitalizaci&oacute;n psiqui&aacute;trica o investigaci&oacute;n cl&iacute;nica.',
          'Ambas versiones utilizan la misma l&oacute;gica jer&aacute;rquica: las preguntas se administran en secuencia y algunas solo se activan seg&uacute;n respuestas previas. Esto evita preguntas innecesarias y respeta el ritmo emocional del paciente.',
        ],
      },
      {
        title: 'Ideaci&oacute;n vs conducta',
        paragraphs: [
          'La C-SSRS diferencia cinco niveles de ideaci&oacute;n suicida: (1) deseo de estar muerto, (2) pensamientos suicidas no espec&iacute;ficos activos, (3) pensamientos con m&eacute;todo pero sin plan, (4) pensamientos con plan e intenci&oacute;n, (5) pensamientos con plan, intenci&oacute;n y preparaci&oacute;n. A mayor nivel, mayor riesgo inminente.',
          'El comportamiento suicida incluye: intento actual (acciones para acabar con la vida), intento interrumpido (intervenci&oacute;n de terceros), intento abortado (autointerrupci&oacute;n), preparaci&oacute;n (recolecci&oacute;n de medios, despedidas) y comportamiento suicida no especificado. La presencia de intento previo es el predictor m&aacute;s robusto de riesgo futuro.',
          'Un paciente puede tener ideaci&oacute;n pasiva (nivel 1-2: &laquo;preferir&iacute;a no despertar&raquo;) sin plan ni intento. Esto requiere evaluaci&oacute;n y monitoreo, pero no necesariamente hospitalizaci&oacute;n. Ideaci&oacute;n activa con plan (nivel 4-5) requiere intervenci&oacute;n inmediata y plan de seguridad.',
          'La distinci&oacute;n ideaci&oacute;n/conducta evita dos errores cl&iacute;nicos frecuentes: subestimar riesgo en pacientes con ideaci&oacute;n activa sin intento previo, y sobreestimar riesgo en pacientes con ideaci&oacute;n pasiva transitoria sin factores de riesgo adicionales.',
        ],
      },
      {
        title: 'C&oacute;mo administrar',
        paragraphs: [
          'La C-SSRS se administra preferiblemente en entrevista semiestructurada, aunque existen versiones de autoinforme para investigaci&oacute;n. El cl&iacute;nico lee las preguntas en lenguaje claro, adaptando formulaci&oacute;n sin alterar el contenido sem&aacute;ntico. Se recomienda un tono directo pero emp&aacute;tico: &laquo;Voy a hacerte algunas preguntas importantes sobre c&oacute;mo te has sentido&raquo;.',
          'Las preguntas sobre ideaci&oacute;n deben hacerse sin rodeos. Evitar eufemismos (&laquo;&iquest;Has pensado en hacerte da&ntilde;o?&raquo;) que el paciente puede interpretar como autolesión no suicida. La C-SSRS utiliza lenguaje directo: &laquo;&iquest;Has deseado estar muerto/a?&raquo;, &laquo;&iquest;Has pensado en suicidarte?&raquo;.',
          'Si el paciente responde afirmativamente a cualquier pregunta sobre ideaci&oacute;n o comportamiento, el cl&iacute;nico profundiza con preguntas de seguimiento sobre frecuencia, duraci&oacute;n, controlabilidad, disuasores y acceso a medios letales. Esta exploraci&oacute;n no est&aacute; codificada en la C-SSRS pero es esencial para la formulaci&oacute;n cl&iacute;nica.',
          'En adolescentes, la administraci&oacute;n requiere considerar confidencialidad y presencia de padres. En pacientes con trauma (<a href="/articulos/escala-pcl-5-estres-postraumatico.html">PCL-5</a> elevado), la evaluaci&oacute;n de riesgo suicida es componente obligatorio de la evaluaci&oacute;n inicial.',
        ],
      },
      {
        title: 'Puntuaci&oacute;n e interpretaci&oacute;n',
        paragraphs: [
          'La C-SSRS no produce un puntaje total &uacute;nico como escalas Likert. La interpretaci&oacute;n se basa en el nivel m&aacute;s alto de ideaci&oacute;n reportado y la presencia/ausencia de comportamiento suicida. Esta aproximaci&oacute;n categ&oacute;rica refleja mejor la realidad cl&iacute;nica del riesgo suicida que un n&uacute;mero continuo.',
          'Riesgo bajo: ideaci&oacute;n nivel 1-2 sin plan ni intento previo, con factores protectores (apoyo social, tratamiento adherente, ausencia de sustancias). Riesgo moderado: ideaci&oacute;n nivel 3 o intento remoto (&gt;6 meses) sin factores agudos. Riesgo alto: ideaci&oacute;n nivel 4-5, intento reciente, acceso a medios letales, consumo de sustancias, aislamiento.',
        ],
        extra: `
    <table class="severity-table">
      <thead>
        <tr>
          <th>Nivel ideaci&oacute;n</th>
          <th>Descripci&oacute;n</th>
          <th>Nivel de riesgo</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="score-badge">1</span></td>
          <td><strong>Deseo de estar muerto</strong></td>
          <td>Bajo-moderado; evaluar factores protectores.</td>
        </tr>
        <tr>
          <td><span class="score-badge">2 &ndash; 3</span></td>
          <td><strong>Ideaci&oacute;n activa sin plan</strong></td>
          <td>Moderado; plan de seguridad; seguimiento cercano.</td>
        </tr>
        <tr>
          <td><span class="score-badge">4 &ndash; 5</span></td>
          <td><strong>Ideaci&oacute;n con plan/intenci&oacute;n</strong></td>
          <td>Alto; intervenci&oacute;n inmediata; considerar hospitalizaci&oacute;n.</td>
        </tr>
        <tr>
          <td><span class="score-badge">Conducta</span></td>
          <td><strong>Intento o preparaci&oacute;n</strong></td>
          <td>Muy alto; emergencia psiqui&aacute;trica; no dejar solo al paciente.</td>
        </tr>
      </tbody>
    </table>`,
      },
      {
        title: 'Protocolo seguridad',
        paragraphs: [
          'Ante riesgo moderado-alto en C-SSRS, activar protocolo de seguridad: (1) no dejar solo al paciente, (2) evaluar acceso a medios letales y acordar su retiro seguro, (3) elaborar plan de seguridad escrito con n&uacute;meros de crisis y contactos de apoyo, (4) acordar seguimiento en 24-48 horas, (5) considerar hospitalizaci&oacute;n si riesgo inminente.',
          'El plan de seguridad (Safety Planning Intervention de Stanley & Brown) incluye: se&ntilde;ales de alerta personales, estrategias de afrontamiento internas, personas y lugares de distracci&oacute;n, contactos de apoyo, profesionales de crisis y medio ambiente seguro (retiro de armas, medicamentos, sustancias).',
          'En Colombia, el psic&oacute;logo debe conocer l&iacute;neas de crisis (L&iacute;nea 106, L&iacute;nea de la Vida 018000423456) y protocolos de <a href="/articulos/sivigila-psicologia-colombia.html">SIVIGILA</a> para eventos de inter&eacute;s en salud p&uacute;blica. En M&eacute;xico, la L&iacute;nea de la Vida 800 911 2000 y SAPTEL 55 5259 8121.',
          'La hospitalizaci&oacute;n involuntaria es &uacute;ltimo recurso cuando el paciente no puede mantenerse seguro de forma ambulatoria. Debe cumplir requisitos legales locales y documentarse exhaustivamente la evaluaci&oacute;n de riesgo que la justifica.',
        ],
      },
      {
        title: 'Documentaci&oacute;n',
        paragraphs: [
          'Documentar la evaluaci&oacute;n C-SSRS es obligaci&oacute;n &eacute;tica y legal. El registro debe incluir: fecha y hora, nivel m&aacute;s alto de ideaci&oacute;n, presencia de comportamiento suicida, factores de riesgo y protectores identificados, plan de seguridad acordado, decisiones cl&iacute;nicas (derivaci&oacute;n, hospitalizaci&oacute;n, seguimiento) y firma del profesional.',
          'La documentaci&oacute;n protege al paciente (continuidad de cuidados) y al profesional (evidencia de evaluaci&oacute;n diligente en procedimientos legales o &eacute;ticos). La ausencia de documentaci&oacute;n de riesgo suicida es una de las principales vulnerabilidades en demandas por suicidio de pacientes.',
          'En plataformas digitales, los formularios C-SSRS estructurados facilitan registro estandarizado y alertas autom&aacute;ticas cuando el riesgo es elevado. Kalyo permite integrar evaluaci&oacute;n de riesgo suicida con el expediente cl&iacute;nico y planes de seguimiento.',
          'La reevaluaci&oacute;n peri&oacute;dica con C-SSRS (cada sesi&oacute;n en pacientes de alto riesgo, mensual en riesgo moderado) documenta evoluci&oacute;n del riesgo y respuesta al tratamiento. Una reducci&oacute;n de nivel de ideaci&oacute;n es indicador cl&iacute;nicamente significativo.',
        ],
      },
      {
        title: 'C-SSRS vs SBQ-R',
        paragraphs: [
          'La C-SSRS y la Scale for Suicide Ideation (SSI) o Suicidal Behaviors Questionnaire-Revised (SBQ-R) son instrumentos complementarios. El SBQ-R es cuestionario breve de autoinforme (4 &iacute;tems) que produce puntaje total para tamizaje en poblaci&oacute;n general y estudiantes.',
          'La C-SSRS ofrece mayor granularidad cl&iacute;nica: diferencia niveles de ideaci&oacute;n, eval&uacute;a comportamiento suicida detalladamente y est&aacute; dise&ntilde;ada para entrevista cl&iacute;nica. El SBQ-R es m&aacute;s r&aacute;pido pero menos espec&iacute;fico para decisiones cl&iacute;nicas complejas.',
          'En consulta psicol&oacute;gica, se recomienda C-SSRS como instrumento principal de evaluaci&oacute;n de riesgo suicida. El SBQ-R puede usarse como tamizaje inicial en poblaciones grandes (universidades, empresas) con derivaci&oacute;n a evaluaci&oacute;n C-SSRS cuando es positivo.',
          'Ambos instrumentos deben complementarse con la evaluaci&oacute;n cl&iacute;nica integral descrita en nuestra gu&iacute;a de <a href="/articulos/evaluacion-riesgo-suicida.html">evaluaci&oacute;n de riesgo suicida</a>, que incluye exploraci&oacute;n de factores precipitantes, red de apoyo, funcionamiento psicosocial y plan terap&eacute;utico.',
          'Capacitaci&oacute;n formal en administraci&oacute;n de la C-SSRS, disponible gratuitamente en l&iacute;nea a trav&eacute;s de los desarrolladores, mejora la estandarizaci&oacute;n interprofesional y la calidad de la documentaci&oacute;n de riesgo suicida en equipos de salud mental.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'cage-alcoholismo-test',
      filename: 'cage-alcoholismo-test.html',
      title: 'CAGE: Test de Tamizaje de Alcoholismo — guía clínica | Kalyo',
      description:
        'Guía del CAGE: 4 preguntas, punto de corte ≥2, comparación con AUDIT, ventajas, limitaciones y uso en atención primaria.',
      keywords: 'CAGE, alcoholismo, tamizaje alcohol, test CAGE, psicología clínica, atención primaria',
      metaLabel: CLINICAL_META,
      h1: 'CAGE: Cuestionario de Tamizaje de Alcoholismo',
      intro:
        'El cuestionario CAGE es uno de los instrumentos de tamizaje de consumo problem&aacute;tico de alcohol m&aacute;s utilizados en atenci&oacute;n primaria mundial. Su acr&oacute;nimo (Cut down, Annoyed, Guilty, Eye-opener) resume cuatro preguntas clave sobre consecuencias del consumo de alcohol. Desarrollado por Ewing en 1984, destaca por su extrema brevedad y alta sensibilidad para detectar dependencia alcoh&oacute;lica.',
      heroAlt: 'CAGE test alcoholismo en tablet con interfaz clínica púrpura',
      inlineAlt: 'Gráfico interpretación CAGE 4 preguntas tamizaje alcohol púrpura',
      ctaTitle: 'Tamiza consumo de alcohol con CAGE y AUDIT en Kalyo',
      ctaText: 'Combina el CAGE con el AUDIT y escalas de salud mental en evaluaciones cl&iacute;nicas digitales integradas.',
      ctaButton: 'Prueba gratis 7 d&iacute;as &rarr;',
      related: [
        ['audit-test-alcoholismo', 'AUDIT: Test de Alcoholismo'],
        ['dast-10-deteccion-drogas', 'DAST-10: Detecci&oacute;n de Drogas'],
        ['escala-dass-21', 'DASS-21: Depresi&oacute;n, Ansiedad y Estr&eacute;s'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; es el CAGE?',
        paragraphs: [
          'El CAGE fue desarrollado por John A. Ewing como herramienta de tamizaje r&aacute;pido para detectar dependencia alcoh&oacute;lica en atenci&oacute;n primaria. Consta de cuatro preguntas de s&iacute;/no que exploran: necesidad de reducir el consumo (Cut down), molestia de otros por el consumo (Annoyed), culpa por beber (Guilty) y consumo matutino para aliviar malestar (Eye-opener).',
          'A diferencia de cuestionarios que cuantifican cantidad de consumo, el CAGE eval&uacute;a consecuencias psicosociales y conductas indicativas de dependencia. Esto lo hace especialmente sensible para detectar alcoholismo establecido, aunque menos sensible para consumo de riesgo sin dependencia.',
          'El instrumento ha sido validado en decenas de pa&iacute;ses y poblaciones cl&iacute;nicas. Su administraci&oacute;n toma menos de un minuto y puede integrarse en evaluaciones m&eacute;dicas rutinarias, consulta psicol&oacute;gica y programas de salud ocupacional.',
          'El CAGE es tamizaje, no diagn&oacute;stico. Un resultado positivo (&ge;2) indica probable problema con el alcohol que requiere evaluaci&oacute;n ampliada, preferiblemente con el <a href="/articulos/audit-test-alcoholismo.html">AUDIT</a> y entrevista cl&iacute;nica estructurada.',
        ],
      },
      {
        title: '4 preguntas',
        paragraphs: [
          'Las cuatro preguntas del CAGE en espa&ntilde;ol son: (C) &laquo;&iquest;Alguna vez has sentido que deber&iacute;as reducir tu consumo de alcohol?&raquo;, (A) &laquo;&iquest;Te ha molestado que la gente te critique tu forma de beber?&raquo;, (G) &laquo;&iquest;Alguna vez te has sentido mal o culpable por tu forma de beber?&raquo;, (E) &laquo;Eye-opener: &iquest;Alguna vez has tomado alcohol por la ma&ntilde;ana para calmar los nervios o eliminar la resaca?&raquo;.',
          'Cada respuesta afirmativa suma un punto. El rango total es 0 a 4. La pregunta Eye-opener (consumo matutino) es particularmente espec&iacute;fica de dependencia f&iacute;sica y tiene alto valor predictivo de alcoholismo cl&iacute;nico.',
          'El cl&iacute;nico debe aclarar que las preguntas se refieren a experiencias de por vida (&laquo;alguna vez&raquo;), no solo al &uacute;ltimo mes. Esto diferencia al CAGE del AUDIT, que eval&uacute;a consumo reciente.',
          'En poblaciones con bajo consumo de alcohol por razones culturales o religiosas, el CAGE puede tener menor prevalencia de positivos. En contextos latinoamericanos con alta tolerancia social al consumo, la normalizaci&oacute;n del alcohol puede reducir la honestidad en respuestas.',
        ],
      },
      {
        title: 'Punto corte &ge;2',
        paragraphs: [
          'El punto de corte est&aacute;ndar del CAGE es &ge;2 respuestas afirmativas para identificar probable dependencia alcoh&oacute;lica. Este umbral ha demostrado sensibilidad de 70-90% y especificidad de 70-85% en m&uacute;ltiples estudios, aunque var&iacute;a seg&uacute;n la poblaci&oacute;n.',
          'Un puntaje de 0-1 generalmente descarta dependencia alcoh&oacute;lica, aunque no excluye consumo de riesgo detectable con el AUDIT. Un puntaje &ge;2 activa evaluaci&oacute;n ampliada y exploraci&oacute;n de consecuencias del consumo.',
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
          <td><span class="score-badge">0 &ndash; 1</span></td>
          <td><strong>Dependencia improbable</strong></td>
          <td>Evaluar consumo de riesgo con AUDIT; psicoeducaci&oacute;n.</td>
        </tr>
        <tr>
          <td><span class="score-badge">&ge; 2</span></td>
          <td><strong>Probable dependencia alcoh&oacute;lica</strong></td>
          <td>Evaluaci&oacute;n ampliada; AUDIT; derivaci&oacute;n si necesario.</td>
        </tr>
        <tr>
          <td><span class="score-badge">3 &ndash; 4</span></td>
          <td><strong>Alta probabilidad de dependencia</strong></td>
          <td>Intervenci&oacute;n especializada; evaluar abstinencia/retirada.</td>
        </tr>
      </tbody>
    </table>`,
      },
      {
        title: 'CAGE vs AUDIT',
        paragraphs: [
          'El CAGE y el <a href="/articulos/audit-test-alcoholismo.html">AUDIT</a> son instrumentos complementarios con objetivos distintos. El CAGE detecta dependencia alcoh&oacute;lica establecida con cuatro preguntas de por vida. El AUDIT eval&uacute;a consumo de riesgo, s&iacute;ntomas de dependencia y consecuencias en los &uacute;ltimos 12 meses con diez &iacute;tems.',
          'El AUDIT es m&aacute;s sensible para consumo de riesgo y bebedor social problem&aacute;tico (puntuaci&oacute;n 8-15). El CAGE es m&aacute;s espec&iacute;fico para dependencia cl&iacute;nica. En atenci&oacute;n primaria, la secuencia AUDIT &rarr; CAGE (si AUDIT &ge;8) optimiza detecci&oacute;n sin sobrecargar al paciente.',
          'Un paciente puede tener AUDIT elevado (consumo de riesgo) con CAGE negativo (sin dependencia), o CAGE positivo con AUDIT moderado (dependencia con consumo aparentemente controlado). La evaluaci&oacute;n conjunta enriquece la formulaci&oacute;n cl&iacute;nica.',
          'Para policonsumo, combinar AUDIT + <a href="/articulos/dast-10-deteccion-drogas.html">DAST-10</a> + CAGE proporciona perfil completo de sustancias. El consumo de alcohol frecuentemente coexiste con otras drogas y con sintomatolog&iacute;a depresiva medible con el <a href="/articulos/escala-dass-21.html">DASS-21</a>.',
        ],
      },
      {
        title: 'Ventajas rapidez',
        paragraphs: [
          'La principal ventaja del CAGE es su rapidez: cuatro preguntas de s&iacute;/no administrables en menos de un minuto. Esto lo hace ideal para atenci&oacute;n primaria con alta demanda, consultas m&eacute;dicas breves y evaluaciones de urgencia donde el tiempo es limitado.',
          'El CAGE no requiere capacitaci&oacute;n especializada: m&eacute;dicos generales, enfermeras y psic&oacute;logos pueden administrarlo con m&iacute;nima instrucci&oacute;n. Su simplicidad ha facilitado adopci&oacute;n masiva en sistemas de salud de pa&iacute;ses de ingresos bajos y medios.',
          'Las preguntas del CAGE son f&aacute;cilmente comprensibles para pacientes con baja escolaridad. No requieren calcular unidades de alcohol ni recordar cantidades exactas de consumo, barreras frecuentes en cuestionarios m&aacute;s extensos.',
          'En telemedicina y consulta digital, el CAGE puede administrarse como primer filtro antes de videoconsulta, permitiendo al cl&iacute;nico preparar evaluaci&oacute;n ampliada si el resultado es positivo.',
        ],
      },
      {
        title: 'Limitaciones',
        paragraphs: [
          'El CAGE tiene limitaciones importantes. Su sensibilidad para consumo de riesgo sin dependencia es baja: un paciente con AUDIT &ge;8 puede tener CAGE 0-1. No debe usarse como &uacute;nico instrumento de evaluaci&oacute;n de alcohol.',
          'Las preguntas de &laquo;alguna vez&raquo; no distinguen consumo activo de historia remota. Un paciente abstinente de largo plazo puede responder afirmativamente a preguntas sobre experiencias pasadas, generando falsos positivos si no se contextualiza.',
          'El CAGE fue validado principalmente en poblaciones adultas occidentales. En mujeres embarazadas, adolescentes y ancianos, los puntos de corte pueden requerir ajuste. Algunos estudios sugieren punto de corte &ge;1 en mujeres por menor prevalencia base.',
          'El estigma del alcoholismo puede reducir honestidad en respuestas, especialmente en contextos laborales o forenses. Garantizar confidencialidad y enfoque de salud (no moralizador) mejora la validez de las respuestas.',
        ],
      },
      {
        title: 'Atenci&oacute;n primaria',
        paragraphs: [
          'En atenci&oacute;n primaria, el CAGE es la herramienta de elecci&oacute;n para tamizaje universal de alcoholismo en adultos. Organizaciones como la USPSTF recomiendan tamizaje de consumo de alcohol en todos los adultos, y el CAGE cumple este objetivo con m&iacute;nimo costo temporal.',
          'Los m&eacute;dicos de familia pueden integrar CAGE en evaluaciones anuales de salud, consultas por s&iacute;ntomas som&aacute;ticos inespec&iacute;ficos o antes de prescribir medicamentos que interact&uacute;an con alcohol. Un CAGE positivo activa derivaci&oacute;n al psic&oacute;logo o servicios de adicciones.',
          'Para psic&oacute;logos en atenci&oacute;n primaria integrada, el CAGE identifica pacientes cuyo consumo de alcohol puede estar manteniendo depresi&oacute;n, ansiedad o problemas de pareja. La intervenci&oacute;n breve motivacional posterior a CAGE positivo es efectiva incluso en consultas de 5-10 minutos.',
          'En Colombia y M&eacute;xico, donde el consumo de alcohol es normativo socialmente, el tamizaje rutinario con CAGE en atenci&oacute;n primaria puede detectar casos que de otro modo permanecer&iacute;an ocultos hasta complicaciones m&eacute;dicas o sociales graves.',
          'Documentar el resultado del CAGE, las intervenciones breves realizadas y las derivaciones efectuadas respalda la pr&aacute;ctica basada en evidencia y cumple est&aacute;ndares de registro cl&iacute;nico en consulta privada e institucional.',
        ],
      },
      {
        title: 'Intervenci&oacute;n breve tras CAGE positivo',
        paragraphs: [
          'Ante CAGE &ge;2, la intervenci&oacute;n breve (5-15 minutos) basada en entrevista motivacional es efectiva incluso en consulta primaria. Explorar pros y contras del consumo, feedback personalizado y consejo m&eacute;dico claro incrementan la probabilidad de reducci&oacute;n de consumo.',
          'Proporcionar informaci&oacute;n sobre l&iacute;mites de consumo de bajo riesgo, riesgos hep&aacute;ticos, interacciones con medicamentos psicotr&oacute;picos y recursos de tratamiento disponibles complementa el tamizaje con acci&oacute;n cl&iacute;nica inmediata.',
          'Si el paciente no est&aacute; listo para cambio, mantener puerta abierta (&laquo; cuando quieras hablar de esto, estoy disponible&raquo;) y reevaluar en consultas posteriores. La presi&oacute;n moralizadora reduce adherencia y da&ntilde;a la relaci&oacute;n terap&eacute;utica.',
          'Combinar intervenci&oacute;n breve con evaluaci&oacute;n <a href="/articulos/audit-test-alcoholismo.html">AUDIT</a> completa y <a href="/articulos/dast-10-deteccion-drogas.html">DAST-10</a> cuando se sospecha policonsumo maximiza la utilidad cl&iacute;nica del tamizaje inicial con CAGE.',
          'En telepsicolog&iacute;a, el CAGE puede administrarse digitalmente antes de la sesi&oacute;n. Un resultado positivo permite al cl&iacute;nico preparar evaluaci&oacute;n ampliada y recursos de derivaci&oacute;n sin consumir tiempo valioso de la consulta.',
        ],
      },
      {
        title: 'Limitaciones del CAGE',
        paragraphs: [
          'El CAGE fue dise&ntilde;ado para detectar dependencia alcoh&oacute;lica, no consumo de riesgo moderado. Pacientes con patrones binge drinking pueden tener CAGE negativo y AUDIT elevado, quedando sin detectar si solo se aplica CAGE.',
          'Las preguntas de &laquo;alguna vez en la vida&raquo; no distinguen consumo activo de historia remota resuelta. Contextualizar respuestas en entrevista es indispensable para evitar sobre- o subestimaci&oacute;n del riesgo actual.',
          'En mujeres embarazadas, el umbral de corte puede requerir ajuste a &ge;1 por menor prevalencia base. El consumo de alcohol en embarazo tiene umbral de riesgo esencialmente cero, independientemente del puntaje CAGE.',
          'El CAGE no reemplaza evaluaci&oacute;n cl&iacute;nica completa de trastorno por uso de alcohol ni evaluaci&oacute;n de otras sustancias con <a href="/articulos/dast-10-deteccion-drogas.html">DAST-10</a>. Su valor est&aacute; en la rapidez del tamizaje inicial en atenci&oacute;n primaria, no en la exhaustividad diagn&oacute;stica.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'y-bocs-escala-yale-brown-toc',
      filename: 'y-bocs-escala-yale-brown-toc.html',
      title: 'Y-BOCS: Escala Yale-Brown para TOC — guía clínica | Kalyo',
      description:
        'Guía de la Y-BOCS: obsesiones y compulsiones, 10 ítems 0-4, interpretación por rangos, seguimiento ERP, CY-BOCS y diagnóstico diferencial.',
      keywords: 'Y-BOCS, TOC, trastorno obsesivo compulsivo, Yale-Brown, ERP, psicología clínica',
      metaLabel: CLINICAL_META,
      h1: 'Y-BOCS: Escala Yale-Brown para Trastorno Obsesivo-Compulsivo',
      intro:
        'La Yale-Brown Obsessive Compulsive Scale (Y-BOCS) es el instrumento est&aacute;ndar de referencia para evaluar la severidad del trastorno obsesivo-compulsivo (TOC). Desarrollada por Goodman, Rasmussen y colaboradores, cuantifica obsesiones y compulsiones en diez &iacute;tems con escala de cinco puntos. Es indispensable para diagn&oacute;stico, planificaci&oacute;n de tratamiento con ERP y monitorizaci&oacute;n de respuesta terap&eacute;utica.',
      heroAlt: 'Y-BOCS escala Yale-Brown TOC en tablet interfaz clínica púrpura',
      inlineAlt: 'Gráfico interpretación Y-BOCS obsesiones compulsiones severidad púrpura',
      ctaTitle: 'Eval&uacute;a severidad de TOC con la Y-BOCS en Kalyo',
      ctaText: 'Aplica la Y-BOCS digitalmente y monitoriza la respuesta a ERP con gr&aacute;ficas de evoluci&oacute;n autom&aacute;ticas.',
      ctaButton: 'Prueba gratis 7 d&iacute;as &rarr;',
      related: [
        ['escala-dass-21', 'DASS-21: Depresi&oacute;n, Ansiedad y Estr&eacute;s'],
        ['que-es-el-gad-7', '&iquest;Qu&eacute; es el GAD-7?'],
        ['escala-hamilton-ansiedad-ham-a', 'Escala Hamilton de Ansiedad (HAM-A)'],
      ],
    },
    [
      {
        title: '&iquest;Qu&eacute; es la Y-BOCS?',
        paragraphs: [
          'La Y-BOCS fue desarrollada en la Yale School of Medicine y el Connecticut Mental Health Center como instrumento estandarizado para cuantificar severidad del TOC independientemente del contenido espec&iacute;fico de obsesiones y compulsiones. A diferencia de checklists de s&iacute;ntomas, eval&uacute;a tiempo ocupado, interferencia, distr&eacute;s, resistencia y control.',
          'Consta de diez &iacute;tems divididos en dos subescalas: obsesiones (&iacute;tems 1-5) y compulsiones (&iacute;tems 6-10). Cada &iacute;tem se punt&uacute;a de 0 a 4, con rango total de 0 a 40. La administraci&oacute;n requiere entrevista cl&iacute;nica semiestructurada de 15-30 minutos por un profesional capacitado.',
          'La Y-BOCS es el outcome measure est&aacute;ndar en ensayos cl&iacute;nicos de TOC y en investigaci&oacute;n sobre terapia de exposici&oacute;n con prevenci&oacute;n de respuesta (ERP). Una reducci&oacute;n &ge;35% del puntaje basal se considera respuesta cl&iacute;nicamente significativa al tratamiento.',
          'Existen versiones autoaplicadas (Y-BOCS-SR) para investigaci&oacute;n, pero la versi&oacute;n entrevista cl&iacute;nica permanece como est&aacute;ndar para evaluaci&oacute;n diagn&oacute;stica y decisiones terap&eacute;uticas en consulta especializada.',
        ],
      },
      {
        title: 'Obsesiones y compulsiones',
        paragraphs: [
          'Las obsesiones son pensamientos, impulsos o im&aacute;genes recurrentes e intrusivos que causan ansiedad o malestar. Las compulsiones son conductas o actos mentales repetitivos que el individuo se ve impulsado a realizar en respuesta a obsesiones. La Y-BOCS eval&uacute;a severidad de ambos dominios por separado.',
          'Los cinco &iacute;tems de obsesiones eval&uacute;an: (1) tiempo ocupado por obsesiones, (2) interferencia con funcionamiento, (3) distr&eacute;s causado, (4) resistencia al impulso obsesivo, (5) grado de control sobre obsesiones. Los &iacute;tems 6-10 eval&uacute;an las mismas dimensiones para compulsiones.',
          'La puntuaci&oacute;n de subescalas (0-20 obsesiones, 0-20 compulsiones) orienta el foco terap&eacute;utico. Un paciente con obsesiones predominantes (rumiaciones, dudas) puede requerir ERP adaptado diferente a uno con compulsiones visibles (lavado, revisi&oacute;n).',
          'La Y-BOCS no eval&uacute;a el contenido espec&iacute;fico de obsesiones (contaminaci&oacute;n, simetr&iacute;a, agresividad, tab&uacute;es). Para caracterizaci&oacute;n de subtipos, complementar con entrevista cl&iacute;nica o inventarios como el OCI-R (Obsessive-Compulsive Inventory-Revised).',
        ],
      },
      {
        title: '10 &iacute;tems 0-4',
        paragraphs: [
          'Cada uno de los diez &iacute;tems se punt&uacute;a de 0 (sin s&iacute;ntomas) a 4 (s&iacute;ntomas extremos). Los anclajes var&iacute;an por &iacute;tem: para &laquo;tiempo ocupado&raquo;, 0 = ninguno, 1 = menos de 1 hora/d&iacute;a, 2 = 1-3 horas, 3 = 3-8 horas, 4 = m&aacute;s de 8 horas. Para &laquo;interferencia&raquo;, 0 = ninguna, 4 = incapacitante.',
          'La suma de &iacute;tems 1-5 produce subescala de obsesiones (0-20). La suma de &iacute;tems 6-10 produce subescala de compulsiones (0-20). La suma total (0-40) indica severidad global del TOC.',
          'La administraci&oacute;n debe referirse a la semana previa, capturando s&iacute;ntomas recientes y evitando sesgo de recuerdo de periodos m&aacute;s graves. El cl&iacute;nico debe definir claramente qu&eacute; constituye obsesi&oacute;n vs preocupaci&oacute;n normal antes de puntuar.',
          'En plataformas digitales, la Y-BOCS puede estructurarse con anclajes visuales y c&aacute;lculo autom&aacute;tico de subescalas y total, facilitando el seguimiento longitudinal con gr&aacute;ficas de evoluci&oacute;n.',
        ],
      },
      {
        title: 'Interpretaci&oacute;n 0-7/8-15/16-23/24-31/32-40',
        paragraphs: [
          'La interpretaci&oacute;n de la Y-BOCS utiliza rangos de severidad ampliamente aceptados en la literatura cl&iacute;nica e investigaci&oacute;n. Estos rangos orientan decisiones sobre intensidad de tratamiento y necesidad de derivaci&oacute;n especializada.',
          'Pacientes con Y-BOCS &ge;16 generalmente requieren ERP estructurada con psic&oacute;logo especializado en TOC. Comorbilidad con depresi&oacute;n o ansiedad medible con el <a href="/articulos/escala-dass-21.html">DASS-21</a> o el <a href="/articulos/que-es-el-gad-7.html">GAD-7</a> es frecuente y debe abordarse en el plan terap&eacute;utico integrado.',
        ],
        extra: `
    <table class="severity-table">
      <thead>
        <tr>
          <th>Puntuaci&oacute;n total</th>
          <th>Severidad</th>
          <th>Acci&oacute;n cl&iacute;nica</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="score-badge">0 &ndash; 7</span></td>
          <td><strong>Subcl&iacute;nico</strong></td>
          <td>Psicoeducaci&oacute;n; monitoreo si hay quejas.</td>
        </tr>
        <tr>
          <td><span class="score-badge">8 &ndash; 15</span></td>
          <td><strong>Leve</strong></td>
          <td>Intervenci&oacute;n psicol&oacute;gica; ERP si persiste.</td>
        </tr>
        <tr>
          <td><span class="score-badge">16 &ndash; 23</span></td>
          <td><strong>Moderado</strong></td>
          <td>ERP estructurada; valorar ISRS si comorbilidad.</td>
        </tr>
        <tr>
          <td><span class="score-badge">24 &ndash; 31</span></td>
          <td><strong>Severo</strong></td>
          <td>ERP intensiva; considerar psiquiatr&iacute;a para ISRS.</td>
        </tr>
        <tr>
          <td><span class="score-badge">32 &ndash; 40</span></td>
          <td><strong>Extremo</strong></td>
          <td>Tratamiento intensivo multidisciplinario; posible hospitalizaci&oacute;n.</td>
        </tr>
      </tbody>
    </table>`,
      },
      {
        title: 'Seguimiento ERP',
        paragraphs: [
          'La terapia de exposici&oacute;n con prevenci&oacute;n de respuesta (ERP) es el tratamiento de primera l&iacute;nea para TOC seg&uacute;n gu&iacute;as internacionales. La Y-BOCS es el instrumento est&aacute;ndar para monitorizar respuesta a ERP: se administra al inicio, cada 4-8 sesiones y al finalizar tratamiento.',
          'Una reducci&oacute;n &ge;35% del puntaje basal indica respuesta cl&iacute;nicamente significativa. Reducci&oacute;n &ge;50% indica remisi&oacute;n parcial. Puntaje final &le;12-14 sugiere remisi&oacute;n cl&iacute;nica. Estos criterios orientan decisiones sobre continuar, intensificar o modificar el tratamiento.',
          'Si despu&eacute;s de 12-16 sesiones de ERP bien conducida la Y-BOCS no muestra reducci&oacute;n &ge;35%, considerar: comorbilidad no abordada (depresi&oacute;n, TDAH), ERP mal implementada, resistencia familiar o necesidad de potenciaci&oacute;n farmacol&oacute;gica con ISRS.',
          'Las plataformas digitales facilitan visualizaci&oacute;n de tendencias Y-BOCS a lo largo del tratamiento, permitiendo al cl&iacute;nico y paciente evaluar objetivamente el progreso y mantener motivaci&oacute;n durante ERP, que puede ser emocionalmente exigente.',
        ],
      },
      {
        title: 'CY-BOCS',
        paragraphs: [
          'La Children&rsquo;s Yale-Brown Obsessive Compulsive Scale (CY-BOCS) es la adaptaci&oacute;n pedi&aacute;trica de la Y-BOCS para ni&ntilde;os y adolescentes de 6 a 18 a&ntilde;os. Mantiene la estructura de diez &iacute;tems y rangos de puntuaci&oacute;n, con lenguaje adaptado y entrevista que incluye al menor y, frecuentemente, a los padres.',
          'El TOC pedi&aacute;trico tiene presentaci&oacute;n cl&iacute;nica distinta al adulto: obsesiones de agresividad y simetr&iacute;a son m&aacute;s frecuentes, y las compulsiones pueden ser enmascaradas como rutinas infantiles normales. La CY-BOCS ayuda a distinguir TOC cl&iacute;nico de conductas evolutivamente normales.',
          'Los puntos de corte de severidad en CY-BOCS son similares a la Y-BOCS adulta, aunque algunos estudios sugieren umbrales ligeramente m&aacute;s bajos en preadolescentes. La ERP adaptada a ni&ntilde;os incluye involucraci&oacute;n parental como co-terapeuta.',
          'En adolescentes, puede utilizarse Y-BOCS o CY-BOCS seg&uacute;n madurez cognitiva y preferencia cl&iacute;nica. La consistencia en el instrumento elegido es importante para seguimiento longitudinal.',
        ],
      },
      {
        title: 'Diagn&oacute;stico diferencial',
        paragraphs: [
          'La Y-BOCS eval&uacute;a severidad de TOC, no establece diagn&oacute;stico. Antes de administrarla, el cl&iacute;nico debe confirmar criterios DSM-5/CIE-11 de trastorno obsesivo-compulsivo mediante entrevista cl&iacute;nica. Muchas condiciones pueden simular TOC.',
          'El trastorno de ansiedad generalizada (<a href="/articulos/que-es-el-gad-7.html">GAD-7</a> elevado) presenta preocupaciones excesivas pero generalmente tem&aacute;ticas (finanzas, salud, relaciones), no intrusiones egodist&oacute;nicas espec&iacute;ficas. La ansiedad por enfermedad (hipocondr&iacute;a) puede incluir compulsiones de verificaci&oacute;n m&eacute;dica que simulan TOC de contaminaci&oacute;n.',
          'El trastorno de p&aacute;nico puede incluir miedo a &laquo;perder el control&raquo; o &laquo;volverse loco&raquo; que simula obsesiones de da&ntilde;o. La <a href="/articulos/escala-hamilton-ansiedad-ham-a.html">escala Hamilton de ansiedad</a> ayuda a caracterizar ansiedad generalizada vs ansiedad espec&iacute;fica del TOC.',
          'El trastorno del espectro autista puede incluir rituales y rigidez que simulan compulsiones, pero sin obsesiones egodist&oacute;nicas ni resistencia al ritual. La evaluaci&oacute;n diferencial requiere historia developmental y, cuando corresponda, evaluaci&oacute;n neuropsicol&oacute;gica.',
          'Registrar puntajes Y-BOCS, subescalas de obsesiones y compulsiones, y respuesta terap&eacute;utica en el expediente cl&iacute;nico cumple est&aacute;ndares de documentaci&oacute;n en TOC y facilita coordinaci&oacute;n con psiquiatr&iacute;a cuando se requiere potenciaci&oacute;n farmacol&oacute;gica con ISRS.',
        ],
      },
      {
        title: 'Y-BOCS y comorbilidad cl&iacute;nica',
        paragraphs: [
          'El TOC rara vez ocurre aislado. Depresi&oacute;n com&oacute;rbe, medible con el <a href="/articulos/escala-dass-21.html">DASS-21</a>, afecta hasta el 60% de pacientes con TOC y puede interferir con adherencia a ERP si no se aborda simult&aacute;neamente.',
          'Trastornos de ansiedad generalizada, fobias y trastorno de p&aacute;nico comparten features con TOC. El <a href="/articulos/que-es-el-gad-7.html">GAD-7</a> y la <a href="/articulos/escala-hamilton-ansiedad-ham-a.html">HAM-A</a> ayudan a caracterizar ansiedad com&oacute;rbe que requiere intervenci&oacute;n espec&iacute;fica adem&aacute;s de ERP.',
          'Tics motores y vocales (Tourette) coocurren frecuentemente con TOC en ni&ntilde;os y adolescentes. La evaluaci&oacute;n CY-BOCS debe complementarse con exploraci&oacute;n neurol&oacute;gica cuando se sospecha este cuadro.',
          'El abordaje secuencial recomendado es: estabilizar comorbilidad depresiva o ansiosa severa, iniciar ERP para TOC cuando el paciente tenga capacidad de tolerar ansiedad inducida por exposici&oacute;n, y monitorizar con Y-BOCS en cada fase.',
          'Familiares y parejas de pacientes con TOC severo frecuentemente participan en compulsiones (&laquo;acomodaci&oacute;n&raquo;). La evaluaci&oacute;n Y-BOCS debe acompa&ntilde;arse de psicoeducaci&oacute;n familiar para reducir refuerzo inadvertido de rituales.',
        ],
      },
      {
        title: 'Limitaciones de la Y-BOCS',
        paragraphs: [
          'La Y-BOCS requiere entrenamiento para administraci&oacute;n estandarizada. Variabilidad inter-evaluador es un problema si distintos cl&iacute;nicos punt&uacute;an sin calibraci&oacute;n previa, especialmente en los anclajes de &laquo;tiempo ocupado&raquo; e &laquo;interferencia&raquo;.',
          'No eval&uacute;a insight, funcionalidad global ni comorbilidades. Un paciente con Y-BOCS moderado pero insight pobre y comorbilidad depresiva severa puede requerir intervenci&oacute;n m&aacute;s intensiva de lo que sugiere el puntaje aislado.',
          'Obsesiones puramente mentales (rumiaciones, dudas) pueden subestimarse si el cl&iacute;nico se enfoca en compulsiones visibles. Explorar obsesiones ocultas antes de puntuar mejora la validez de la evaluaci&oacute;n.',
          'Los puntos de corte fueron validados principalmente en poblaciones occidentales. En contextos latinoamericanos, complementar con evaluaci&oacute;n cl&iacute;nica culturalmente informada enriquece la interpretaci&oacute;n m&aacute;s all&aacute; del n&uacute;mero total.',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'como-abrir-consulta-privada-colombia',
      filename: 'como-abrir-consulta-privada-colombia.html',
      title: 'Cómo Abrir Consulta Privada de Psicología en Colombia — guía 2026 | Kalyo',
      description:
        'Guía paso a paso para abrir consulta privada en Colombia: Colpsic, DIAN, Cámara de Comercio, Secretaría de Salud, facturación y herramientas digitales.',
      keywords: 'consulta privada psicología Colombia, Colpsic, DIAN, RUT, facturación psicólogos, emprendimiento psicología',
      metaLabel: PRACTICE_META,
      h1: 'C&oacute;mo Abrir una Consulta Privada de Psicolog&iacute;a en Colombia',
      intro:
        'Abrir una consulta privada de psicolog&iacute;a en Colombia requiere cumplir requisitos legales, tributarios y sanitarios que garantizan el ejercicio profesional &eacute;tico y sostenible. Esta gu&iacute;a recorre paso a paso el proceso desde la tarjeta profesional hasta la facturaci&oacute;n electr&oacute;nica, con referencias actualizadas a 2026 para psic&oacute;logos que desean emprender en consulta independiente.',
      heroAlt: 'Abrir consulta privada psicología Colombia en tablet interfaz clínica púrpura',
      inlineAlt: 'Diagrama pasos abrir consulta privada psicología Colombia púrpura',
      ctaTitle: 'Kalyo te ayuda a gestionar tu consulta desde el primer d&iacute;a',
      ctaText: 'Historias cl&iacute;nicas, consentimiento informado, evaluaciones psicom&eacute;tricas y gesti&oacute;n de pacientes en una plataforma dise&ntilde;ada para psic&oacute;logos colombianos.',
      ctaButton: 'Prueba gratis 7 d&iacute;as &rarr;',
      related: [
        ['ley-1090-psicologia-colombia', 'Ley 1090: Psicolog&iacute;a en Colombia'],
        ['consentimiento-informado-psicologia', 'Consentimiento Informado en Psicolog&iacute;a'],
        ['software-para-psicologos-clinicos', 'Software para Psic&oacute;logos Cl&iacute;nicos'],
      ],
    },
    [
      {
        title: 'Requisitos previos Colpsic',
        paragraphs: [
          'Antes de abrir consulta privada, el psic&oacute;logo debe contar con t&iacute;tulo profesional de psicolog&iacute;a otorgado por universidad reconocida por el Ministerio de Educaci&oacute;n, tarjeta profesional vigente expedida por el Consejo Profesional de Psicolog&iacute;a de Colombia (Colpsic) y afiliaci&oacute;n activa al colegio departamental de psic&oacute;logos correspondiente a su jurisdicci&oacute;n.',
          'La <a href="/articulos/ley-1090-psicologia-colombia.html">Ley 1090 de 2006</a> establece que ejercer psicolog&iacute;a sin tarjeta profesional es delito. Verificar que la tarjeta est&eacute; vigente y registrada en el sistema del Colpsic es el primer paso indispensable antes de cualquier tr&aacute;mite empresarial.',
          'Se recomienda contar con p&oacute;liza de responsabilidad civil profesional antes de atender pacientes. Aunque no es requisito legal universal, protege al psic&oacute;logo ante demandas por mala praxis y es exigida por algunas aseguradoras y arrendadores de consultorios.',
          'Definir el &aacute;mbito de competencia (cl&iacute;nica, organizacional, educativa) y obtener certificaciones de especializaci&oacute;n cuando se anuncien servicios especializados es requisito &eacute;tico del C&oacute;digo Deontol&oacute;gico y Bio&eacute;tico de la profesi&oacute;n.',
        ],
      },
      {
        title: 'Paso 1 Colpsic',
        paragraphs: [
          'El tr&aacute;mite inicial ante Colpsic incluye verificar la inscripci&oacute;n de la tarjeta profesional en el Registro &Uacute;nico Nacional de Profesionales de la Salud (REPS) si se planea facturar a EPS o prestar servicios en el sistema de salud. Para consulta privada directa (sin EPS), el REPS no es obligatorio pero facilita futuros convenios.',
          'Afiliarse al colegio departamental de psic&oacute;logos (Colpsic seccional) es obligatorio seg&uacute;n la Ley 1090. La afiliaci&oacute;n ofrece asesor&iacute;a &eacute;tica y legal, formaci&oacute;n continua, descuentos en seguros y representaci&oacute;n gremial. Las cuotas anuales var&iacute;an por seccional.',
          'Solicitar certificado de vigencia de tarjeta profesional y certificado de antecedentes &eacute;ticos (si est&aacute; disponible) para tr&aacute;mites ante Secretar&iacute;a de Salud y contratos con instituciones. Estos documentos acreditan habilitaci&oacute;n profesional.',
          'Consultar con el colegio sobre requisitos espec&iacute;ficos para telepsicolog&iacute;a y consulta digital, ya que las resoluciones sobre ejercicio a distancia est&aacute;n en evoluci&oacute;n y var&iacute;an por seccional.',
        ],
      },
      {
        title: 'Paso 2 DIAN RUT',
        paragraphs: [
          'Registrar el RUT (Registro &Uacute;nico Tributario) ante la DIAN es obligatorio para facturar servicios profesionales. El psic&oacute;logo puede registrarse como persona natural responsable de IVA (si supera umbrales de facturaci&oacute;n) o como persona natural no responsable de IVA (r&eacute;gimen m&aacute;s com&uacute;n para consultorios peque&ntilde;os).',
          'En el RUT, seleccionar actividad econ&oacute;mica correspondiente a servicios de psicolog&iacute;a (c&oacute;digo CIIU 8699 seg&uacute;n clasificaci&oacute;n vigente). Definir responsabilidades tributarias: retenci&oacute;n en la fuente, r&eacute;gimen simple de tributaci&oacute;n (SIMPLE) si aplica, y obligaci&oacute;n de facturaci&oacute;n electr&oacute;nica.',
          'Desde 2021, la facturaci&oacute;n electr&oacute;nica es obligatoria para personas naturales en Colombia. Se requiere adquirir numeraci&oacute;n de facturaci&oacute;n electr&oacute;nica (rango de numeraci&oacute;n) y contratar proveedor tecnol&oacute;gico autorizado (PTA) o software de facturaci&oacute;n certificado.',
          'Mantener contabilidad b&aacute;sica de ingresos y gastos desde el primer d&iacute;a. Considerar contratar contador para declaraciones bimestrales/anuales, especialmente si se factura a empresas que practican retenci&oacute;n en la fuente.',
        ],
      },
      {
        title: 'Paso 3 C&aacute;mara de comercio',
        paragraphs: [
          'Para consulta privada, el psic&oacute;logo puede operar como persona natural sin constituir empresa. Sin embargo, registrar un establecimiento de comercio en la C&aacute;mara de Comercio del municipio donde se ubica el consultorio es recomendable y exigido por algunas Secretar&iacute;as de Salud para habilitaci&oacute;n sanitaria.',
          'El registro de establecimiento de comercio incluye: matr&iacute;cula mercantil, declaraci&oacute;n de actividad econ&oacute;mica, direcci&oacute;n del consultorio y renovaci&oacute;n anual. El costo var&iacute;a por c&aacute;mara de comercio (aproximadamente $200.000-$400.000 COP anuales en 2026).',
          'Si se planea contratar personal (secretaria, asistente), constituir una sociedad (SAS es la forma m&aacute;s flexible) puede ofrecer ventajas tributarias y de responsabilidad limitada. Consultar con abogado y contador antes de constituir sociedad.',
          'El registro mercantil tambi&eacute;n es requisito para abrir cuenta bancaria empresarial si se desea separar finanzas personales de las de la consulta.',
        ],
      },
      {
        title: 'Paso 4 Secretar&iacute;a de Salud',
        paragraphs: [
          'La habilitaci&oacute;n sanitaria del consultorio ante la Secretar&iacute;a de Salud departamental o distrital es requisito legal para prestar servicios de salud en consulta privada. El tr&aacute;mite eval&uacute;a condiciones f&iacute;sicas del espacio: ventilaci&oacute;n, iluminaci&oacute;n, privacidad, se&ntilde;alizaci&oacute;n, botiqu&iacute;n b&aacute;sico y cumplimiento de normas t&eacute;cnicas de habilitaci&oacute;n.',
          'Documentos requeridos t&iacute;picamente incluyen: tarjeta profesional, RUT, registro mercantil, plano del consultorio, certificado de uso de suelo (si aplica), contrato de arrendamiento o propiedad, y formulario de solicitud de habilitaci&oacute;n. El proceso puede tardar 1-3 meses.',
          'La Resoluci&oacute;n 1449 de 2016 y normas complementarias establecen est&aacute;ndares de habilitaci&oacute;n para consultorios ambulatorios. Verificar requisitos espec&iacute;ficos de la Secretar&iacute;a de Salud de su departamento, ya que existen variaciones locales.',
          'La habilitaci&oacute;n debe renovarse peri&oacute;dicamente (generalmente cada 5 a&ntilde;os). Operar sin habilitaci&oacute;n expone a sanciones de la autoridad sanitaria y puede invalidar contratos con aseguradoras.',
        ],
      },
      {
        title: 'Paso 5 banco/facturaci&oacute;n',
        paragraphs: [
          'Abrir cuenta bancaria para la consulta (personal o empresarial seg&uacute;n estructura legal) facilita la separaci&oacute;n de finanzas y la aceptaci&oacute;n de pagos electr&oacute;nicos. Muchos psic&oacute;logos utilizan cuentas de ahorros personales con RUT registrado para simplicidad inicial.',
          'Implementar facturaci&oacute;n electr&oacute;nica desde el primer paciente. Softwares como Siigo, Alegra, Facturador DIAN gratuito o integraciones en plataformas cl&iacute;nicas permiten emitir facturas conformes. Cada sesi&oacute;n atendida debe facturarse.',
          'Definir pol&iacute;tica de pagos: tarifas por sesi&oacute;n, paquetes, formas de pago aceptadas (efectivo, transferencia, dat&aacute;fono, PSE), pol&iacute;tica de cancelaci&oacute;n y recibos para pacientes que no requieren factura (personas naturales ocasionales).',
          'Considerar integraci&oacute;n de pagos en plataforma digital cl&iacute;nica para automatizar cobros y facturaci&oacute;n. Un <a href="/articulos/software-para-psicologos-clinicos.html">software para psic&oacute;logos cl&iacute;nicos</a> que integre agenda, pagos y facturaci&oacute;n reduce carga administrativa.',
        ],
      },
      {
        title: 'Tarifas 2026',
        paragraphs: [
          'Las tarifas de consulta psicol&oacute;gica privada en Colombia var&iacute;an ampliamente seg&uacute;n ciudad, experiencia, especializaci&oacute;n y modalidad. En 2026, rangos orientativos en ciudades principales son: $80.000-$150.000 COP por sesi&oacute;n individual est&aacute;ndar, $120.000-$250.000 COP para especialistas con posgrado, y $60.000-$100.000 COP para telepsicolog&iacute;a.',
          'Investigar tarifas de colegas en la misma ciudad y segmento antes de fijar precios. Subvalorar servicios afecta sostenibilidad; sobrevalorar sin respaldo de especializaci&oacute;n dificulta captaci&oacute;n de pacientes.',
          'Documentar tarifas en reglamento interno de la consulta y comunicarlas claramente al paciente antes de iniciar tratamiento, incluyendo pol&iacute;tica de incrementos anuales y paquetes promocionales si se ofrecen.',
          'Si se planea facturar a EPS o empresas, consultar manual tarifario de cada aseguradora. Los valores de referencia del POS/SISBEN no aplican directamente a consulta privada fuera del sistema.',
        ],
      },
      {
        title: 'Seguros RC',
        paragraphs: [
          'La p&oacute;liza de responsabilidad civil profesional protege al psic&oacute;logo ante reclamaciones por presunta mala praxis, violaci&oacute;n de confidencialidad o da&ntilde;os derivados de la atenci&oacute;n. Aunque no es requisito legal obligatorio para consulta privada, es altamente recomendable.',
          'Compa&ntilde;&iacute;as como Sura, Bol&iacute;var, Allianz y colectivos del Colpsic ofrecen p&oacute;lizas espec&iacute;ficas para psic&oacute;logos con primas anuales entre $500.000-$2.000.000 COP seg&uacute;n cobertura. Verificar que la p&oacute;liza cubra telepsicolog&iacute;a si se ofrece.',
          'Algunos arrendadores de consultorios y cl&iacute;nicas compartidas exigen p&oacute;liza de RC como condici&oacute;n del contrato. Tener p&oacute;liza activa facilita estos acuerdos y transmite profesionalismo a pacientes.',
          'La RC no sustituye pr&aacute;ctica &eacute;tica ni documentaci&oacute;n cl&iacute;nica adecuada. Ante procedimientos &eacute;tico-profesionales, contar con historias cl&iacute;nicas completas y <a href="/articulos/consentimiento-informado-psicologia.html">consentimientos informados</a> es la mejor protecci&oacute;n.',
        ],
      },
      {
        title: 'Herramientas digitales',
        paragraphs: [
          'Desde el primer d&iacute;a, implementar herramientas digitales reduce errores administrativos y mejora calidad cl&iacute;nica. Elementos esenciales: sistema de agenda con recordatorios, historias cl&iacute;nicas digitales conformes a est&aacute;ndares legales, gesti&oacute;n de consentimiento informado, evaluaciones psicom&eacute;tricas digitales y respaldo seguro de informaci&oacute;n.',
          'Kalyo est&aacute; dise&ntilde;ado para psic&oacute;logos en Latinoam&eacute;rica e integra evaluaciones cl&iacute;nicas (PHQ-9, GAD-7, DASS-21 y decenas m&aacute;s), documentaci&oacute;n de sesiones, consentimiento y seguimiento de pacientes en plataforma segura compatible con telepsicolog&iacute;a.',
          'Seleccionar herramientas que cumplan Ley 1581 de protecci&oacute;n de datos personales: servidores seguros, cifrado, pol&iacute;tica de privacidad clara y acuerdo de tratamiento de datos. Los expedientes cl&iacute;nicos contienen datos sensibles de salud.',
          'Evitar almacenar expedientes en WhatsApp, Gmail personal o documentos sin cifrado. Estas pr&aacute;cticas violan confidencialidad profesional y la Ley 1581, exponiendo al psic&oacute;logo a sanciones legales y &eacute;ticas.',
        ],
      },
      {
        title: 'Errores comunes',
        paragraphs: [
          'Atender pacientes antes de completar habilitaci&oacute;n sanitaria es uno de los errores m&aacute;s frecuentes. Aunque el tr&aacute;mite es lento, operar sin habilitaci&oacute;n es ilegal y puede resultar en clausura del consultorio y multas.',
          'No facturar o facturar incorrectamente genera problemas tributarios con la DIAN. La facturaci&oacute;n electr&oacute;nica obligatoria implica que cada ingreso profesional debe documentarse. Acumular meses sin facturar complica regularizaci&oacute;n posterior.',
          'Descuidar documentaci&oacute;n cl&iacute;nica desde el inicio es un error cr&iacute;tico. Sin historias cl&iacute;nicas, consentimientos y notas de evoluci&oacute;n, el psic&oacute;logo queda indefenso ante quejas &eacute;ticas, demandas o auditor&iacute;as. Implementar sistema de documentaci&oacute;n desde el primer paciente.',
          'Subestimar costos operativos (arriendo, servicios, seguros, software, formaci&oacute;n continua, marketing) lleva a consultorios insostenibles. Elaborar proyecci&oacute;n financiera a 12 meses antes de abrir, considerando periodo de ramp-up de captaci&oacute;n de pacientes (3-6 meses t&iacute;pico).',
        ],
      },
    ],
  ),

  makeArticle(
    {
      slug: 'como-abrir-consulta-privada-mexico',
      filename: 'como-abrir-consulta-privada-mexico.html',
      title: 'Cómo Abrir Consulta Privada de Psicología en México — guía 2026 | Kalyo',
      description:
        'Guía paso a paso para abrir consulta privada en México: cédula SEP, RFC SAT, IMSS, COFEPRIS, CFDI, NOM-004 y herramientas digitales.',
      keywords: 'consulta privada psicología México, cédula SEP, RFC SAT, CFDI, NOM-004, emprendimiento psicología',
      metaLabel: PRACTICE_META,
      h1: 'C&oacute;mo Abrir una Consulta Privada de Psicolog&iacute;a en M&eacute;xico',
      intro:
        'Emprender en consulta privada de psicolog&iacute;a en M&eacute;xico implica navegar requisitos profesionales, fiscales y sanitarios que var&iacute;an por estado. Esta gu&iacute;a integra los pasos esenciales para ejercer legalmente en 2026: desde la c&eacute;dula profesional de la SEP hasta la facturaci&oacute;n CFDI y el cumplimiento de la NOM-004 para historias cl&iacute;nicas.',
      heroAlt: 'Abrir consulta privada psicología México en tablet interfaz clínica púrpura',
      inlineAlt: 'Diagrama pasos abrir consulta privada psicología México púrpura',
      ctaTitle: 'Kalyo cumple con NOM-004 y te ayuda desde el primer d&iacute;a',
      ctaText: 'Expedientes cl&iacute;nicos conformes a NOM-004, consentimiento informado, evaluaciones psicom&eacute;tricas y gesti&oacute;n de pacientes en plataforma segura.',
      ctaButton: 'Prueba gratis 7 d&iacute;as &rarr;',
      related: [
        ['nom-004-historia-clinica-mexico', 'NOM-004: Historia Cl&iacute;nica en M&eacute;xico'],
        ['consentimiento-informado-psicologia', 'Consentimiento Informado en Psicolog&iacute;a'],
        ['software-para-psicologos-clinicos', 'Software para Psic&oacute;logos Cl&iacute;nicos'],
      ],
    },
    [
      {
        title: 'Requisitos SEP/c&eacute;dula',
        paragraphs: [
          'El requisito fundamental para ejercer psicolog&iacute;a en M&eacute;xico es la c&eacute;dula profesional expedida por la Secretar&iacute;a de Educaci&oacute;n P&uacute;blica (SEP), que acredita t&iacute;tulo de licenciatura en psicolog&iacute;a otorgado por universidad incorporada o reconocida. Sin c&eacute;dula profesional, ejercer psicolog&iacute;a es ilegal seg&uacute;n la Ley Reglamentaria del Art&iacute;culo 5&deg; Constitucional.',
          'Verificar que la c&eacute;dula est&eacute; registrada en el Registro Nacional de Profesionales (RNPS) de la SEP. Para consulta privada cl&iacute;nica, se recomienda contar con formaci&oacute;n en psicolog&iacute;a cl&iacute;nica o posgrado en &aacute;rea de intervenci&oacute;n, aunque no es requisito legal para ejercer.',
          'Los colegios estatales de psic&oacute;logos (no existe colegio nacional obligatorio como en Colombia) ofrecen certificaciones voluntarias, formaci&oacute;n continua y asesor&iacute;a &eacute;tica. Afiliarse al colegio estatal es recomendable aunque no siempre obligatorio.',
          'Si se planea atender menores, evaluaciones forenses o neuropsicolog&iacute;a, verificar requisitos adicionales de certificaci&oacute;n o registro ante autoridades estatales de salud o instancias judiciales.',
        ],
      },
      {
        title: 'Paso 1 c&eacute;dula SEP',
        paragraphs: [
          'Si a&uacute;n no se cuenta con c&eacute;dula profesional, el tr&aacute;mite se realiza ante la Direcci&oacute;n General de Profesiones de la SEP con t&iacute;tulo apostillado (si es extranjero), acta de examen profesional y pago de derechos. El proceso puede tardar semanas a meses seg&uacute;n carga administrativa.',
          'Para psic&oacute;logos con t&iacute;tulo extranjero, existe procedimiento de revalidaci&oacute;n o equivalencia de estudios ante la SEP y, en algunos casos, examen &uacute;nico nacional. Consultar requisitos actualizados en gob.mx/sep.',
          'Una vez obtenida, la c&eacute;dula profesional debe exhibirse en el consultorio conforme a la NOM-004 y estar disponible para verificaci&oacute;n de pacientes y autoridades sanitarias. Incluir n&uacute;mero de c&eacute;dula en recibos, facturas y documentos profesionales.',
          'Mantener actualizado el registro ante colegio estatal de psic&oacute;logos si se est&aacute; afiliado, y renovar certificaciones de especializaci&oacute;n cuando se anuncien p&uacute;blicamente.',
        ],
      },
      {
        title: 'Paso 2 SAT RFC',
        paragraphs: [
          'Registrar el RFC (Registro Federal de Contribuyentes) ante el SAT es obligatorio para facturar servicios profesionales. El tr&aacute;mite puede realizarse en l&iacute;nea (sat.gob.mx) o en m&oacute;dulos del SAT con e.firma (Firma Electr&oacute;nica Avanzada).',
          'Seleccionar r&eacute;gimen fiscal adecuado: R&eacute;gimen Simplificado de Confianza (RESICO) para ingresos hasta $3.5 millones MXN anuales (2026), actividad empresarial y profesional con honorarios, o r&eacute;gimen general seg&uacute;n proyecci&oacute;n de ingresos. Consultar contador para optimizaci&oacute;n fiscal legal.',
          'Obtener e.firma (FIEL) es indispensable para facturaci&oacute;n electr&oacute;nica CFDI. Tramitar en SAT con identificaci&oacute;n oficial, comprobante de domicilio y correo electr&oacute;nico. La e.firma tiene vigencia de 4 a&ntilde;os y debe renovarse.',
          'Inscribirse en el RFC con actividad econ&oacute;mica de servicios profesionales de psicolog&iacute;a (c&oacute;digo SCIAN 621330 o equivalente vigente). Actualizar domicilio fiscal si se cambia ubicaci&oacute;n del consultorio.',
        ],
      },
      {
        title: 'Paso 3 IMSS',
        paragraphs: [
          'La inscripci&oacute;n al IMSS como trabajador independiente (modalidad obligatoria o voluntaria) proporciona acceso a seguridad social: atenci&oacute;n m&eacute;dica, pensiones e incapacidades. Aunque no es requisito legal para abrir consulta, es altamente recomendable para psic&oacute;logos independientes.',
          'En modalidad obligatoria, cotizar mensualmente seg&uacute;n ingresos declarados (salario base de cotizaci&oacute;n). En 2026, la cuota aproximada var&iacute;a entre $2.000-$6.000 MXN mensuales seg&uacute;n nivel de ingresos declarado.',
          'El IMSS tambi&eacute;n es relevante si se planea contratar personal: registrar empleados (secretaria, asistente) implica obligaciones patronales de IMSS, INFONAVIT y SAR.',
          'Alternativas privadas (Seguro de Salud para la Familia, seguros m&eacute;dicos privados) complementan o sustituyen IMSS seg&uacute;n preferencia, pero IMSS sigue siendo la opci&oacute;n m&aacute;s accesible para independientes.',
        ],
      },
      {
        title: 'Paso 4 COFEPRIS',
        paragraphs: [
          'COFEPRIS (Comisi&oacute;n Federal para la Protecci&oacute;n contra Riesgos Sanitarios) regula establecimientos de salud en M&eacute;xico. Para consultorios de psicolog&iacute;a privada, los requisitos var&iacute;an por estado: algunos exigen aviso de funcionamiento o licencia sanitaria, otros son m&aacute;s flexibles para consultorios ambulatorios de bajo riesgo.',
          'Consultar la Secretar&iacute;a de Salud estatal o municipal correspondiente. En CDMX, por ejemplo, se requiere aviso de funcionamiento para consultorios. En otros estados, un consultorio individual puede operar con c&eacute;dula profesional y cumplimiento de NOM-004 sin tr&aacute;mite COFEPRIS espec&iacute;fico.',
          'Si se planea usar psicof&aacute;rmacos de muestra o realizar procedimientos invasivos (no aplicable a psicolog&iacute;a cl&iacute;nica est&aacute;ndar), los requisitos COFEPRIS son m&aacute;s estrictos. Para psicoterapia ambulatoria, los requisitos son generalmente m&iacute;nimos.',
          'Verificar normativa local antes de abrir. Operar sin permisos requeridos expone a clausura y multas de la autoridad sanitaria estatal.',
        ],
      },
      {
        title: 'Paso 5 banco/CFDI',
        paragraphs: [
          'Abrir cuenta bancaria para la consulta facilita gesti&oacute;n financiera y aceptaci&oacute;n de transferencias SPEI. Bancos como BBVA, Santander, Banorte y fintechs (Mercado Pago, Clip) ofrecen cuentas para profesionales independientes.',
          'Implementar facturaci&oacute;n electr&oacute;nica CFDI 4.0 desde el primer ingreso. Contratar PAC (Proveedor Autorizado de Certificaci&oacute;n) como Facturama, SW Sapien, o integraciones en software cl&iacute;nico. Cada pago recibido debe emitir CFDI con clave de servicio 85121800 (servicios de psicolog&iacute;a).',
          'Definir pol&iacute;tica de pagos: tarifas, paquetes, formas de pago (efectivo, transferencia, tarjeta), pol&iacute;tica de cancelaci&oacute;n y recibos simples para pacientes que no requieren factura (considerando l&iacute;mite de ingresos en efectivo seg&uacute;n SAT).',
          'Integrar pagos y facturaci&oacute;n en plataforma cl&iacute;nica reduce errores. Un <a href="/articulos/software-para-psicologos-clinicos.html">software para psic&oacute;logos cl&iacute;nicos</a> compatible con NOM-004 facilita operaci&oacute;n diaria.',
        ],
      },
      {
        title: 'Tarifas 2026',
        paragraphs: [
          'Las tarifas de consulta psicol&oacute;gica privada en M&eacute;xico var&iacute;an significativamente por ciudad y especializaci&oacute;n. En 2026, rangos orientativos son: CDMX y Monterrey $800-$2.500 MXN por sesi&oacute;n individual, ciudades medianas $500-$1.200 MXN, telepsicolog&iacute;a $400-$1.000 MXN.',
          'Psic&oacute;logos con posgrado cl&iacute;nico, neuropsicolog&iacute;a o psicoterapia especializada pueden cobrar $1.500-$4.000 MXN en zonas urbanas de alto poder adquisitivo. Investigar mercado local antes de fijar tarifas.',
          'Comunicar tarifas claramente al paciente antes de iniciar tratamiento. Incluir pol&iacute;tica de incrementos, paquetes y descuentos en reglamento interno. La transparencia previene conflictos y es requisito de buena pr&aacute;ctica profesional.',
          'Si se planea facturar a empresas (programas de bienestar laboral, EAP), las tarifas corporativas suelen ser 20-40% superiores a tarifas individuales y requieren contrato y facturaci&oacute;n formal.',
        ],
      },
      {
        title: 'NOM-004',
        paragraphs: [
          'La <a href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004-SSA3-2012</a> establece requisitos para el expediente cl&iacute;nico en consulta privada. Todo psic&oacute;logo debe integrar historia cl&iacute;nica para cada paciente desde la primera consulta, incluyendo identificaci&oacute;n, motivo de consulta, antecedentes, exploraci&oacute;n psicol&oacute;gica, diagn&oacute;stico, plan terap&eacute;utico y notas de evoluci&oacute;n.',
          'La NOM-004 exige conservar expedientes m&iacute;nimo 5 a&ntilde;os desde &uacute;ltima atenci&oacute;n. Los expedientes deben ser legibles, fechados, firmados y protegidos contra acceso no autorizado. La versi&oacute;n electr&oacute;nica debe cumplir NOM-024 si se digitaliza.',
          'Implementar plantillas conformes a NOM-004 desde el inicio evita reconstrucci&oacute;n posterior de expedientes. Kalyo ofrece plantillas adaptadas a psicolog&iacute;a cl&iacute;nica en M&eacute;xico con campos requeridos por la norma.',
          'El incumplimiento de NOM-004 expone a sanciones de la Secretar&iacute;a de Salud estatal y es vulnerabilidad principal en procedimientos &eacute;ticos ante colegios profesionales o demandas de pacientes.',
        ],
      },
      {
        title: 'Seguros RC',
        paragraphs: [
          'El seguro de responsabilidad civil profesional protege al psic&oacute;logo ante reclamaciones por presunta mala praxis. En M&eacute;xico, aunque no es requisito legal obligatorio para consulta privada, es recomendable y exigido por algunos arrendadores de consultorios y programas corporativos.',
          'Aseguradoras como GNP, AXA, Mapfre y colectivos de colegios estatales ofrecen p&oacute;lizas para psic&oacute;logos con primas anuales entre $3.000-$15.000 MXN seg&uacute;n suma asegurada. Verificar cobertura para telepsicolog&iacute;a.',
          'La RC profesional complementa (no sustituye) pr&aacute;ctica &eacute;tica y documentaci&oacute;n conforme a NOM-004. Ante cualquier incidente cl&iacute;nico, contar con expediente completo y <a href="/articulos/consentimiento-informado-psicologia.html">consentimiento informado</a> documentado es esencial.',
          'Algunos colegios estatales de psic&oacute;logos negocian p&oacute;lizas colectivas con descuento. Consultar con el colegio local al iniciar la pr&aacute;ctica privada.',
        ],
      },
      {
        title: 'Herramientas digitales',
        paragraphs: [
          'Desde el primer paciente, implementar sistema digital de gesti&oacute;n cl&iacute;nica conforme a NOM-004: historias cl&iacute;nicas estructuradas, notas de evoluci&oacute;n, consentimiento informado, evaluaciones psicom&eacute;tricas, agenda y respaldo seguro.',
          'Kalyo cumple con est&aacute;ndares de documentaci&oacute;n cl&iacute;nica para psic&oacute;logos en M&eacute;xico, integrando evaluaciones (PHQ-9, GAD-7, DASS-21 y m&aacute;s), expedientes digitales y telepsicolog&iacute;a en plataforma segura.',
          'Seleccionar herramientas que cumplan LFPDPPP (Ley Federal de Protecci&oacute;n de Datos Personales): aviso de privacidad, consentimiento para tratamiento de datos, servidores seguros y posibilidad de que el paciente ejerza derechos ARCO.',
          'Evitar WhatsApp, Gmail personal o notas sin respaldo para expedientes cl&iacute;nicos. Estas pr&aacute;cticas violan NOM-004, LFPDPPP y confidencialidad profesional, generando riesgo legal significativo.',
          'Planificar desde el inicio c&oacute;mo se gestionar&aacute;n cancelaciones, reprogramaciones, paquetes prepagados y facturaci&oacute;n a empresas evita conflictos con pacientes y problemas fiscales con el SAT en los primeros meses de operaci&oacute;n.',
        ],
      },
    ],
  ),
];
