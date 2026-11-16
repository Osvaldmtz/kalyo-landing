#!/usr/bin/env python3
"""Generate 7 comparative AEO articles for Kalyo."""
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

SPECS = [{'slug': 'psicologo-vs-psiquiatra-diferencias',
  'title': 'Psicólogo vs psiquiatra: diferencias clave 2026 | Kalyo',
  'description': 'Psicólogo vs psiquiatra: diferencias de formación, enfoque, medicación y cuándo '
                 'ir con cada uno en México y Colombia. Incluye tabla comparativa clara.',
  'keywords': 'psicólogo vs psiquiatra, diferencia entre psicologo y psiquiatra, medicación, '
              'derivación México Colombia',
  'h1': 'Psicólogo vs psiquiatra: diferencias clave en México y Colombia',
  'breadcrumb_short': 'Psicólogo vs psiquiatra',
  'hero_alt': 'Comparativa psicólogo y psiquiatra en salud mental',
  'inline_alt': 'Tabla psicólogo vs psiquiatra formación y medicación',
  'meta_label': 'Pr&aacute;ctica cl&iacute;nica &middot; Comparativa 2026',
  'date_published': '2026-11-16',
  'date_modified': '2026-11-16',
  'quick_answer': 'El <strong>psic&oacute;logo</strong> es profesional de psicolog&iacute;a: '
                  'eval&uacute;a, formula y hace psicoterapia; <strong>no prescribe</strong> '
                  'psicof&aacute;rmacos. El <strong>psiquiatra</strong> es m&eacute;dico '
                  'especializado: diagnostica desde el modelo m&eacute;dico, puede prescribir y '
                  'monitoriza medicaci&oacute;n. En la mayor&iacute;a de casos conviene '
                  'combinaci&oacute;n cuando hay severidad, riesgo o indicaci&oacute;n '
                  'farmacol&oacute;gica. Use clasificaci&oacute;n alineada a <a '
                  'href="/articulos/cie-11-vs-dsm-5-diferencias.html">CIE-11/DSM</a> y documente '
                  'derivaciones.',
  'intro_long': 'La <strong>diferencia entre psic&oacute;logo y psiquiatra</strong> confunde a '
                'pacientes y derivaciones en consulta diaria. Esta gu&iacute;a compara '
                'formaci&oacute;n, medicaci&oacute;n, evaluaci&oacute;n y cu&aacute;ndo acudir a '
                'cada profesional en M&eacute;xico y Colombia, con tabla para respuestas directas. '
                'Complementa <a href="/articulos/cie-11-vs-dsm-5-diferencias.html">CIE-11 vs '
                'DSM-5</a> y la pr&aacute;ctica interdisciplinar sin mezclar roles '
                'cl&iacute;nicos, legales ni de prescripci&oacute;n.',
  'cta_h2': 'Documenta derivaciones y seguimiento con Kalyo',
  'cta_p': 'Expediente, notas y trazabilidad del plan terap&eacute;utico &mdash; kalyo.io',
  'card_title': 'Psicólogo vs psiquiatra',
  'card_p': 'Formación, medicación y cuándo derivar en México y Colombia.',
  'after_href': '/articulos/cie-11-vs-dsm-5-diferencias.html',
  'after_loc': 'https://kalyo.io/articulos/cie-11-vs-dsm-5-diferencias.html',
  'asset_from': 'cie-11-vs-dsm-5-diferencias',
  'sections': [{'h2': 'Tabla comparativa psic&oacute;logo vs psiquiatra',
                'html': '<table class="items-table">\n'
                        '<thead><tr><th>Aspecto</th><th>Psic&oacute;logo</th><th>Psiquiatra</th></tr></thead>\n'
                        '<tbody>\n'
                        '<tr><td>Formaci&oacute;n</td><td>Psicolog&iacute;a + pr&aacute;ctica '
                        'cl&iacute;nica</td><td>Medicina + psiquiatr&iacute;a</td></tr>\n'
                        '<tr><td>Medicaci&oacute;n</td><td>No prescribe</td><td>Prescribe y '
                        'monitoriza</td></tr>\n'
                        '<tr><td>Intervenci&oacute;n principal</td><td>Psicoterapia y '
                        'evaluaci&oacute;n</td><td>Farmacoterapia y '
                        'estabilizaci&oacute;n</td></tr>\n'
                        '<tr><td>Riesgo / psicosis</td><td>Detecta y deriva</td><td>Manejo '
                        'm&eacute;dico urgente</td></tr>\n'
                        '<tr><td>Documentaci&oacute;n</td><td>Formulaci&oacute;n y notas '
                        'SOAP</td><td>Diagn&oacute;stico m&eacute;dico y recetas</td></tr>\n'
                        '</tbody></table>\n'
                        '<p>La tabla orienta respuestas r&aacute;pidas; los apartados siguientes '
                        'detallan matices cl&iacute;nicos y de pr&aacute;ctica.</p>'},
               {'h2': 'Formaci&oacute;n y marco legal en LATAM',
                'html': '<p>En M&eacute;xico el psic&oacute;logo ejerce con t&iacute;tulo y '
                        'c&eacute;dula; el psiquiatra con licencia m&eacute;dica. En Colombia el '
                        'psic&oacute;logo se ampara en la <a '
                        'href="/articulos/ley-1090-psicologia-colombia.html">Ley 1090</a>. '
                        'Ning&uacute;n psic&oacute;logo debe prescribir ni presentarse como '
                        'm&eacute;dico.</p>\n'
                        '<p>La colaboraci&oacute;n eficiente reparte tareas: estabilizaci&oacute;n '
                        'y farmacolog&iacute;a del lado m&eacute;dico; habilidades, adherencia y '
                        'psicoterapia del lado psicol&oacute;gico.</p>\n'
                        '<p>Registre en expediente consentimiento para intercambio entre '
                        'profesionales y resumen cl&iacute;nico sin exponer datos '
                        'innecesarios.</p>\n'},
               {'h2': 'Cu&aacute;ndo combinar medicaci&oacute;n y terapia',
                'html': '<p>Depresi&oacute;n moderada-grave, trastorno bipolar, esquizofrenia, '
                        'TEPT severo y muchos TDAH en adultos suelen requerir evaluaci&oacute;n '
                        'combinada. El psic&oacute;logo monitorea adherencia, efectos en conducta '
                        'y se&ntilde;ales de empeoramiento.</p>\n'
                        '<p>Derive con nota clara: motivo, riesgo, tratamiento actual y objetivos '
                        'terap&eacute;uticos. Vea <a '
                        'href="/articulos/nota-evolucion-soap-psicologia.html">nota SOAP</a> para '
                        'estructurar.</p>\n'
                        '<p>Evite culpar al paciente por &laquo;no mejorar solo con '
                        'pastillas&raquo;: explique el modelo biopsicosocial con evidencia.</p>\n'},
               {'h2': 'Orientaci&oacute;n al paciente y continuidad',
                'html': '<p>Sin psicosis ni riesgo vital, muchas personas inician con '
                        'psicolog&iacute;a; con alucinaciones, man&iacute;a, abstinencia grave o '
                        'crisis suicida activa, priorice valoraci&oacute;n '
                        'psiqui&aacute;trica.</p>\n'
                        '<p>Explique que ver a ambos no duplica tratamiento: integra '
                        'intervenciones con distintos objetivos.</p>\n'
                        '<p><a '
                        'href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=psicologo-vs-psiquiatra-diferencias">Kalyo</a> '
                        'ayuda a sostener continuidad cuando el paciente alterna citas entre '
                        'profesionales.</p>\n'
                        '<p>Revise peri&oacute;dicamente su protocolo con supervisi&oacute;n y '
                        'normativa vigente; documente decisiones en el expediente y mantenga '
                        'canales seguros con el paciente. La comparativa resume tendencias; cada '
                        'caso requiere juicio cl&iacute;nico individual.</p><p>Revise '
                        'peri&oacute;dicamente su protocolo con supervisi&oacute;n y normativa '
                        'vigente; documente decisiones en el expediente y mantenga canales seguros '
                        'con el paciente. La comparativa resume tendencias; cada caso requiere '
                        'juicio cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p>'}],
  'faqs': [{'q': '&iquest;Un psic&oacute;logo puede diagnosticar?',
            'a': 'Formula cl&iacute;nicamente para guiar psicoterapia; diagn&oacute;stico '
                 'm&eacute;dico y prescripci&oacute;n son del psiquiatra seg&uacute;n marco '
                 'local.'},
           {'q': '&iquest;El psiquiatra hace terapia?',
            'a': 'Algunos s&iacute;, breve; muchos derivan psicoterapia prolongada al '
                 'psic&oacute;logo.'},
           {'q': '&iquest;Qui&eacute;n atiende depresi&oacute;n?',
            'a': 'Frecuentemente ambos: medicaci&oacute;n si hay indicaci&oacute;n y psicoterapia '
                 'para sintomas y prevenci&oacute;n.'},
           {'q': '&iquest;Puede solo medicarse?',
            'a': 'A veces en casos leves; cl&iacute;nicamente suele acompa&ntilde;arse con '
                 'psicoterapia para adherencia y habilidades.'},
           {'q': '&iquest;C&oacute;mo compartir informaci&oacute;n?',
            'a': 'Consentimiento informado, canal seguro y resumen cl&iacute;nico; no env&iacute;e '
                 'expediente por mensajer&iacute;a informal.'}],
  'related': [{'href': '/articulos/cie-11-vs-dsm-5-diferencias.html', 'label': 'CIE-11 vs DSM-5'},
              {'href': '/articulos/como-interpretar-tests-psicologicos.html',
               'label': 'Interpretar tests'},
              {'href': '/articulos/alianza-terapeutica.html',
               'label': 'Alianza terap&eacute;utica'},
              {'href': '/articulos/encuadre-terapeutico.html',
               'label': 'Encuadre terap&eacute;utico'}]},
 {'slug': 'terapia-cognitivo-conductual-vs-psicoanalitica',
  'title': 'TCC vs terapia psicoanalítica: diferencias clave | Kalyo',
  'description': 'TCC vs terapia psicoanalítica: diferencias de enfoque, duración, evidencia y '
                 'cuándo usar cada una en la práctica clínica. Incluye tabla comparativa clara.',
  'keywords': 'terapia cognitivo conductual vs psicoanalisis, TCC vs psicoanalítica, evidencia '
              'psicoterapia',
  'h1': 'TCC vs terapia psicoanalítica: diferencias clave en clínica',
  'breadcrumb_short': 'TCC vs psicoanalítica',
  'hero_alt': 'Comparativa TCC y terapia psicoanalítica',
  'inline_alt': 'Tabla TCC versus psicoanálisis',
  'meta_label': 'Psicoterapia &middot; Comparativa 2026',
  'date_published': '2026-11-16',
  'date_modified': '2026-11-16',
  'quick_answer': 'La <strong>TCC</strong> es breve, estructurada y orientada a metas conductuales '
                  'y cognitivas con fuerte respaldo en ensayos controlados. La <strong>terapia '
                  'psicoanal&iacute;tica</strong> explora conflicto, transferencia e inconsciente '
                  'en proceso m&aacute;s largo. Elija seg&uacute;n presentaci&oacute;n, '
                  'motivaci&oacute;n, tiempo y preferencia del paciente &mdash; no por moda. La <a '
                  'href="/articulos/alianza-terapeutica.html">alianza terap&eacute;utica</a> '
                  'predice resultado en ambos modelos.',
  'intro_long': 'Comparar <strong>terapia cognitivo conductual vs psicoan&aacute;lisis</strong> '
                'evita elegir por reputaci&oacute;n y no por encaje cl&iacute;nico real. Esta '
                'gu&iacute;a contrasta duraci&oacute;n, evidencia, t&eacute;cnicas y criterios de '
                'derivaci&oacute;n en consultorio latinoamericano, con tabla para respuestas '
                'directas. Complementa la <a '
                'href="/articulos/terapia-cognitivo-conductual-guia.html">gu&iacute;a de TCC</a> y '
                'el trabajo sobre <a href="/articulos/alianza-terapeutica.html">alianza '
                'terap&eacute;utica</a> sin recomendar un modelo &uacute;nico para todos los '
                'pacientes.',
  'cta_h2': 'Registra objetivos terapéuticos en Kalyo',
  'cta_p': 'Notas, plan y seguimiento por sesión &mdash; kalyo.io',
  'card_title': 'TCC vs terapia psicoanalítica',
  'card_p': 'Enfoque, duración, evidencia y cuándo usar cada modelo.',
  'after_href': '/articulos/alianza-terapeutica.html',
  'after_loc': 'https://kalyo.io/articulos/alianza-terapeutica.html',
  'asset_from': 'alianza-terapeutica',
  'sections': [{'h2': 'Tabla comparativa TCC vs terapia psicoanal&iacute;tica',
                'html': '<table class="items-table">\n'
                        '<thead><tr><th>Aspecto</th><th>TCC</th><th>Psicoan&aacute;lisis</th></tr></thead>\n'
                        '<tbody>\n'
                        '<tr><td>Objetivo</td><td>S&iacute;ntomas actuales y '
                        'habilidades</td><td>Comprensi&oacute;n profunda y patr&oacute;n '
                        'relacional</td></tr>\n'
                        '<tr><td>Duraci&oacute;n</td><td>Breve a media '
                        '(semanas-meses)</td><td>Larga (a&ntilde;os posible)</td></tr>\n'
                        '<tr><td>Estructura</td><td>Agenda, tareas, '
                        'psicoeducaci&oacute;n</td><td>Asociaci&oacute;n libre, '
                        'interpretaci&oacute;n</td></tr>\n'
                        '<tr><td>Evidencia RCT</td><td>Alta en depresi&oacute;n, TAG, '
                        'TOC</td><td>Evidencia creciente; heterog&eacute;nea por '
                        'indicaci&oacute;n</td></tr>\n'
                        '<tr><td>Ideal si</td><td>Meta concreta, tiempo '
                        'limitado</td><td>Exploraci&oacute;n de personalidad y '
                        'conflicto</td></tr>\n'
                        '</tbody></table>\n'
                        '<p>La tabla orienta respuestas r&aacute;pidas; los apartados siguientes '
                        'detallan matices cl&iacute;nicos y de pr&aacute;ctica.</p>'},
               {'h2': 'Modelo de cambio: conducta vs significado',
                'html': '<p>La TCC asume que pensamientos, conductas y sensaciones se influyen '
                        'mutuamente; interviene con reestructuraci&oacute;n, exposici&oacute;n y '
                        'experimentos conductuales. El psicoan&aacute;lisis enfatiza material '
                        'inconsciente, defensas y repetici&oacute;n en la relaci&oacute;n '
                        'terap&eacute;utica.</p>\n'
                        '<p>Ning&uacute;n modelo es superior en abstracto: un paciente con '
                        'p&aacute;nico agorafobia puede preferir TCC con exposici&oacute;n; otro '
                        'con duelo complejo y patrones relacionales cr&oacute;nicos puede buscar '
                        'profundidad anal&iacute;tica.</p>\n'
                        '<p>Documente hip&oacute;tesis de cambio y revisiones de plan; use <a '
                        'href="/articulos/terapia-cognitivo-conductual-guia.html">gu&iacute;a '
                        'TCC</a> como referencia de t&eacute;cnicas.</p>\n'},
               {'h2': 'Evidencia y expectativas realistas',
                'html': '<p>Para depresi&oacute;n, TAG, TOC e insomnio, la TCC tiene amplia base '
                        'emp&iacute;rica. Psicoterapias psicodin&aacute;micas breves muestran '
                        'efectos en algunos trastornos; psicoan&aacute;lisis abierto requiere '
                        'conversar honestamente sobre tiempos y costos.</p>\n'
                        '<p>No prometa &laquo;cura r&aacute;pida&raquo; con TCC ni '
                        '&laquo;reconfiguraci&oacute;n total&raquo; con an&aacute;lisis sin '
                        'revisar avances en sesi&oacute;n.</p>\n'
                        '<p>Escala breve cada pocas semanas (PHQ-9, GAD-7) si usa TCC; en '
                        'an&aacute;lisis, revise objetivos impl&iacute;citos del paciente.</p>\n'},
               {'h2': 'Integraci&oacute;n en la práctica diaria',
                'html': '<p>Muchos cl&iacute;nicos eclectas usan t&eacute;cnicas cognitivas dentro '
                        'de marco psicodin&aacute;mico o viceversa; lo importante es coherencia y '
                        'competencia entrenada.</p>\n'
                        '<p>Si el paciente no progresa en un modelo tras tiempo razonable, '
                        'renegociar o derivar es &eacute;tico.</p>\n'
                        '<p><a '
                        'href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=terapia-cognitivo-conductual-vs-psicoanalitica">Kalyo</a> '
                        'ayuda a registrar tareas, objetivos y notas por modelo '
                        'terap&eacute;utico.</p>\n'
                        '<p>Revise peri&oacute;dicamente su protocolo con supervisi&oacute;n y '
                        'normativa vigente; documente decisiones en el expediente y mantenga '
                        'canales seguros con el paciente. La comparativa resume tendencias; cada '
                        'caso requiere juicio cl&iacute;nico individual.</p><p>Revise '
                        'peri&oacute;dicamente su protocolo con supervisi&oacute;n y normativa '
                        'vigente; documente decisiones en el expediente y mantenga canales seguros '
                        'con el paciente. La comparativa resume tendencias; cada caso requiere '
                        'juicio cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p>'}],
  'faqs': [{'q': '&iquest;La TCC sirve solo para trastornos leves?',
            'a': 'No; hay protocolos para depresi&oacute;n grave, TEPT y otros con adecuaciones. '
                 'La severidad gu&iacute;a intensidad y equipo.'},
           {'q': '&iquest;El psicoan&aacute;lisis ya no se usa?',
            'a': 'S&iacute; se usa; demanda formaci&oacute;n espec&iacute;fica y encaje '
                 'paciente-terapeuta. No es obsoleto, es distinto.'},
           {'q': '&iquest;Puedo mezclar modelos sin formación?',
            'a': 'Mezclar t&eacute;cnicas sin formaci&oacute;n diluye ambos. Prefiera un modelo '
                 'principal o supervise eclecticismo.'},
           {'q': '&iquest;Cu&aacute;l tiene mejor alianza?',
            'a': 'La alianza depende m&aacute;s del terapeuta que del modelo; mida rupturas y '
                 'reparaciones.'},
           {'q': '&iquest;C&oacute;mo explicarlo al paciente?',
            'a': 'Use la tabla: metas, tiempo y estilo de trabajo. Deje que elija con '
                 'informaci&oacute;n, no presi&oacute;n.'}],
  'related': [{'href': '/articulos/terapia-cognitivo-conductual-guia.html', 'label': 'Guía TCC'},
              {'href': '/articulos/alianza-terapeutica.html',
               'label': 'Alianza terap&eacute;utica'},
              {'href': '/articulos/encuadre-terapeutico.html', 'label': 'Encuadre'},
              {'href': '/articulos/wai-sr-alianza-terapeutica.html', 'label': 'WAI-SR alianza'}]},
 {'slug': 'expediente-clinico-papel-vs-digital',
  'title': 'Expediente clínico papel vs digital: diferencias | Kalyo',
  'description': 'Expediente clínico en papel vs digital: ventajas, riesgos, normativa MX/CO y '
                 'cuándo migrar al expediente electrónico. Incluye tabla comparativa clara.',
  'keywords': 'expediente clinico digital, expediente clínico papel vs digital, NOM-004, ECE',
  'h1': 'Expediente clínico en papel vs digital: guía comparativa',
  'breadcrumb_short': 'Papel vs digital',
  'hero_alt': 'Expediente clínico en papel versus digital',
  'inline_alt': 'Comparativa expediente papel y electrónico',
  'meta_label': 'Expediente &middot; MX / CO 2026',
  'date_published': '2026-11-16',
  'date_modified': '2026-11-16',
  'quick_answer': 'El expediente en <strong>papel</strong> puede cumplir contenido si est&aacute; '
                  'ordenado, legible y resguardado, pero falla en b&uacute;squeda, respaldo y '
                  'trazabilidad. El <strong>digital</strong> exige software con accesos, '
                  'bit&aacute;cora y respaldos &mdash; alineado a <a '
                  'href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a> (MX) y '
                  'buenas pr&aacute;cticas de historia cl&iacute;nica (CO). No digitalice PDFs '
                  'sueltos en Drive: eso no es expediente cl&iacute;nico electr&oacute;nico.',
  'intro_long': 'Elegir entre <strong>expediente cl&iacute;nico en papel y digital</strong> no es '
                'est&eacute;tica: es cumplimiento, seguridad y continuidad asistencial en el '
                'consultorio. Esta gu&iacute;a compara ventajas, riesgos y se&ntilde;ales de '
                'migraci&oacute;n en M&eacute;xico y Colombia con tabla directa. Complementa <a '
                'href="/articulos/expediente-clinico-electronico-psicologos.html">expediente '
                'electr&oacute;nico para psic&oacute;logos</a> y <a '
                'href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a> sin sustituir '
                'asesor&iacute;a legal puntual ni auditor&iacute;a externa.',
  'cta_h2': 'Migra con estructura clínica en Kalyo',
  'cta_p': 'Historia, notas SOAP, consentimientos y control de acceso &mdash; kalyo.io',
  'card_title': 'Expediente clínico papel vs digital',
  'card_p': 'Ventajas, riesgos y cuándo migrar al ECE en MX/CO.',
  'after_href': '/articulos/expediente-clinico-electronico-psicologos.html',
  'after_loc': 'https://kalyo.io/articulos/expediente-clinico-electronico-psicologos.html',
  'asset_from': 'expediente-clinico-electronico-psicologos',
  'sections': [{'h2': 'Tabla comparativa expediente papel vs digital',
                'html': '<table class="items-table">\n'
                        '<thead><tr><th>Aspecto</th><th>Papel</th><th>Digital '
                        '(ECE)</th></tr></thead>\n'
                        '<tbody>\n'
                        '<tr><td>Acceso</td><td>F&iacute;sico, riesgo de '
                        'p&eacute;rdida</td><td>Remoto con autenticaci&oacute;n</td></tr>\n'
                        '<tr><td>B&uacute;squeda</td><td>Lenta, depende de '
                        '&iacute;ndice</td><td>Por paciente, fecha, tipo de nota</td></tr>\n'
                        '<tr><td>Respaldo</td><td>Fotocopias/archivo</td><td>Copias '
                        'autom&aacute;ticas verificadas</td></tr>\n'
                        '<tr><td>Integridad</td><td>Borrado manual dif&iacute;cil de '
                        'auditar</td><td>Bit&aacute;cora y versiones</td></tr>\n'
                        '<tr><td>Normativa</td><td>NOM-004 contenido (MX)</td><td>Contenido + '
                        'seguridad / LFPDPPP / Ley 1581</td></tr>\n'
                        '</tbody></table>\n'
                        '<p>La tabla orienta respuestas r&aacute;pidas; los apartados siguientes '
                        'detallan matices cl&iacute;nicos y de pr&aacute;ctica.</p>'},
               {'h2': 'Cuándo el papel aún es defendible',
                'html': '<p>Consultas muy bajas, sin telemedicina y con archivo f&iacute;sico '
                        'ordenado pueden cumplir contenido cl&iacute;nico. El riesgo aparece al '
                        'crecer volumen, mezclar modales o perder legibilidad.</p>\n'
                        '<p>Si usa papel, defina: carpeta por paciente, orden cronol&oacute;gico, '
                        'custodia, plazos de conservaci&oacute;n y pol&iacute;tica ARCO. Vea <a '
                        'href="/articulos/tiempo-conservar-expediente-clinico.html">tiempo de '
                        'conservaci&oacute;n</a>.</p>\n'
                        '<p>El paso a digital debe planearse; no escanee todo un fin de semana sin '
                        'controles.</p>\n'},
               {'h2': 'Riesgos del &laquo;pseudo-digital&raquo;',
                'html': '<p>Word, Excel y carpetas compartidas carecen de trazabilidad '
                        'cl&iacute;nica, roles finos y bit&aacute;cora. Un PDF en WhatsApp no es '
                        'expediente.</p>\n'
                        '<p>Compare con <a '
                        'href="/articulos/nom-024-nom-004-psicologos-mexico.html">NOM-024 vs '
                        'NOM-004</a>: el contenido cl&iacute;nico y la seguridad del sistema son '
                        'distintos pero complementarios.</p>\n'
                        '<p>En Colombia, historia cl&iacute;nica continua y protecci&oacute;n de '
                        'datos exigen retenci&oacute;n responsable.</p>\n'},
               {'h2': 'Plan de migración en tres fases',
                'html': '<p>Fase 1: plantillas de historia y SOAP homog&eacute;neas. Fase 2: ECE '
                        'con usuarios individuales y respaldo probado. Fase 3: cierre de archivo '
                        'papel con inventario.</p>\n'
                        '<p>Capacite al equipo en login, correcciones por addendum y '
                        'exportaci&oacute;n anual de prueba.</p>\n'
                        '<p><a '
                        'href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=expediente-clinico-papel-vs-digital">Kalyo</a> '
                        'centraliza historia, notas y consentimientos pensados para '
                        'psicolog&iacute;a.</p>\n'
                        '<p>Revise peri&oacute;dicamente su protocolo con supervisi&oacute;n y '
                        'normativa vigente; documente decisiones en el expediente y mantenga '
                        'canales seguros con el paciente. La comparativa resume tendencias; cada '
                        'caso requiere juicio cl&iacute;nico individual.</p><p>Revise '
                        'peri&oacute;dicamente su protocolo con supervisi&oacute;n y normativa '
                        'vigente; documente decisiones en el expediente y mantenga canales seguros '
                        'con el paciente. La comparativa resume tendencias; cada caso requiere '
                        'juicio cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p>'}],
  'faqs': [{'q': '&iquest;El papel es ilegal?',
            'a': 'No necesariamente si cumple contenido y conservaci&oacute;n; el digital mejora '
                 'control y continuidad.'},
           {'q': '&iquest;Drive basta como ECE?',
            'a': 'Suele no alcanzar bit&aacute;cora cl&iacute;nica ni roles; no equivale a '
                 'software de salud dise&ntilde;ado.'},
           {'q': '&iquest;Debo escanear todo?',
            'a': 'Priorice pacientes activos; hist&oacute;rico seg&uacute;n plazo legal y '
                 'capacidad.'},
           {'q': '&iquest;Qu&eacute; pasa con firmas?',
            'a': 'ECE con autenticaci&oacute;n; vea notas y firma en Colombia si aplica.'},
           {'q': '&iquest;Costo de migraci&oacute;n?',
            'a': 'Incluya licencias, tiempo de carga y formaci&oacute;n; el costo de '
                 'p&eacute;rdida de expediente suele ser mayor.'}],
  'related': [{'href': '/articulos/expediente-clinico-electronico-psicologos.html',
               'label': 'ECE psicólogos'},
              {'href': '/articulos/nom-004-historia-clinica-mexico.html', 'label': 'NOM-004'},
              {'href': '/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html',
               'label': 'LFPDPPP'},
              {'href': '/articulos/tiempo-conservar-expediente-clinico.html',
               'label': 'Conservación expediente'}]},
 {'slug': 'consulta-presencial-vs-telepsicologia',
  'title': 'Presencial vs telepsicología: diferencias clave | Kalyo',
  'description': 'Consulta presencial vs telepsicología: diferencias clínicas, legales y éticas en '
                 'México y Colombia para psicólogos. Guía práctica con tabla comparativa.',
  'keywords': 'telepsicologia, consulta presencial vs online, telesalud psicología',
  'h1': 'Consulta presencial vs telepsicología para psicólogos',
  'breadcrumb_short': 'Presencial vs telepsicología',
  'hero_alt': 'Comparativa consulta presencial y telepsicología',
  'inline_alt': 'Tabla presencial versus telepsicología',
  'meta_label': 'Teleconsulta &middot; MX / CO 2026',
  'date_published': '2026-11-16',
  'date_modified': '2026-11-16',
  'quick_answer': 'La consulta <strong>presencial</strong> favorece observaci&oacute;n presencial '
                  'completa y contenci&oacute;n en mismo espacio. La '
                  '<strong>telepsicolog&iacute;a</strong> ampl&iacute;a acceso pero exige '
                  'consentimiento de modalidad, identidad, canal seguro y plan de crisis a '
                  'distancia. En MX y CO revise <a '
                  'href="/articulos/telepsicologia-requisitos-legales-mx-co.html">requisitos '
                  'legales</a> y <a '
                  'href="/articulos/telepsicologia-etica-mexico-colombia.html">&eacute;tica</a>. '
                  'No todo caso es apto remoto.',
  'intro_long': 'La comparaci&oacute;n <strong>presencial vs telepsicolog&iacute;a</strong> define '
                'protocolos de consultorio h&iacute;brido en Latinoam&eacute;rica hoy. Esta '
                'gu&iacute;a contrasta aspectos cl&iacute;nicos, legales y de encuadre con tabla '
                'para decisiones r&aacute;pidas en la pr&aacute;ctica diaria. Complementa <a '
                'href="/articulos/telepsicologia-requisitos-legales-mx-co.html">requisitos '
                'MX/CO</a> y documentaci&oacute;n en expediente sin sustituir el criterio '
                'cl&iacute;nico individual ni el juicio de riesgo.',
  'cta_h2': 'Telepsicología con expediente en Kalyo',
  'cta_p': 'Agenda, notas y consentimientos en un solo flujo &mdash; kalyo.io',
  'card_title': 'Presencial vs telepsicología',
  'card_p': 'Diferencias clínicas, legales y éticas para psicólogos.',
  'after_href': '/articulos/telepsicologia-requisitos-legales-mx-co.html',
  'after_loc': 'https://kalyo.io/articulos/telepsicologia-requisitos-legales-mx-co.html',
  'asset_from': 'telepsicologia-etica-mexico-colombia',
  'sections': [{'h2': 'Tabla comparativa presencial vs telepsicolog&iacute;a',
                'html': '<table class="items-table">\n'
                        '<thead><tr><th>Aspecto</th><th>Presencial</th><th>Telepsicolog&iacute;a</th></tr></thead>\n'
                        '<tbody>\n'
                        '<tr><td>Observaci&oacute;n</td><td>Lenguaje no verbal '
                        'completo</td><td>Depende de c&aacute;mara y conexi&oacute;n</td></tr>\n'
                        '<tr><td>Acceso</td><td>Barrera geogr&aacute;fica</td><td>Mayor alcance '
                        'regional</td></tr>\n'
                        '<tr><td>Encuadre</td><td>Consultorio f&iacute;sico</td><td>Privacidad '
                        'domiciliaria del paciente</td></tr>\n'
                        '<tr><td>Crisis</td><td>Protocolo in situ</td><td>Plan de emergencia local '
                        'y contacto</td></tr>\n'
                        '<tr><td>Registro</td><td>Modalidad presencial en '
                        'nota</td><td>Consentimiento remoto + datos t&eacute;cnicos</td></tr>\n'
                        '</tbody></table>\n'
                        '<p>La tabla orienta respuestas r&aacute;pidas; los apartados siguientes '
                        'detallan matices cl&iacute;nicos y de pr&aacute;ctica.</p>'},
               {'h2': 'Criterios clínicos de idoneidad',
                'html': '<p>Telepsicolog&iacute;a suele ser adecuada para seguimiento '
                        'psicoterap&eacute;utico estable, psicoeducaci&oacute;n y muchas '
                        'evaluaciones con apoyo digital. Precaución en psicosis activa, crisis '
                        'suicida sin red, TEA con necesidad de observaci&oacute;n presencial o '
                        'evaluaciones que requieren test presencial estandarizado.</p>\n'
                        '<p>Documente motivo de modalidad y reeval&uacute;e si cambian condiciones '
                        '(mudanza, violencia dom&eacute;stica audible en llamada).</p>\n'
                        '<p>Vea consentimiento y elementos MX/CO en <a '
                        'href="/articulos/consentimiento-informado-elementos-mx-co.html">consentimiento '
                        'informado</a>.</p>\n'},
               {'h2': 'Aspectos legales y de datos',
                'html': '<p>Registre c&eacute;dula profesional, ubicaci&oacute;n del '
                        'psic&oacute;logo, ubicaci&oacute;n del paciente si aplica, plataforma, '
                        'consentimiento y limitaciones de confidencialidad en red.</p>\n'
                        '<p>No grabe sesiones sin base legal y consentimiento expl&iacute;cito. '
                        'Proteja datos seg&uacute;n <a '
                        'href="/articulos/lfpdppp-proteccion-datos-psicologos-mexico.html">LFPDPPP</a> '
                        'o Ley 1581.</p>\n'
                        '<p>Tenga protocolo si se cae la llamada: contacto alterno y '
                        'reagenda.</p>\n'},
               {'h2': 'Híbrido y calidad de sesión',
                'html': '<p>Alternar presencial y remoto es com&uacute;n; mantenga est&aacute;ndar '
                        'de nota en ambos. Revise calidad de audio, iluminaci&oacute;n y '
                        'distracciones.</p>\n'
                        '<p>Ofrezca presencial cuando la alianza o el riesgo lo exijan.</p>\n'
                        '<p><a '
                        'href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=consulta-presencial-vs-telepsicologia">Kalyo</a> '
                        'unifica agenda, expediente y trazabilidad de modalidad.</p>\n'
                        '<p>Revise peri&oacute;dicamente su protocolo con supervisi&oacute;n y '
                        'normativa vigente; documente decisiones en el expediente y mantenga '
                        'canales seguros con el paciente. La comparativa resume tendencias; cada '
                        'caso requiere juicio cl&iacute;nico individual.</p><p>Revise '
                        'peri&oacute;dicamente su protocolo con supervisi&oacute;n y normativa '
                        'vigente; documente decisiones en el expediente y mantenga canales seguros '
                        'con el paciente. La comparativa resume tendencias; cada caso requiere '
                        'juicio cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p>'}],
  'faqs': [{'q': '&iquest;La telepsicolog&iacute;a es tan efectiva?',
            'a': 'Meta-an&aacute;lisis muestran resultados comparables en muchos trastornos; '
                 'depende del caso y del encuadre.'},
           {'q': '&iquest;Puedo atender paciente en otro pa&iacute;s?',
            'a': 'Revise habilitaci&oacute;n profesional y regulaci&oacute;n del lugar del '
                 'paciente; no asuma libre circulaci&oacute;n.'},
           {'q': '&iquest;WhatsApp video es suficiente?',
            'a': 'Suele ser insuficiente para confidencialidad y registro; prefiera plataforma '
                 'pensada para salud.'},
           {'q': '&iquest;C&oacute;mo manejar crisis remota?',
            'a': 'Plan escrito: contacto emergencia local, derivaci&oacute;n, l&iacute;mites de lo '
                 'que puede hacer a distancia.'},
           {'q': '&iquest;Debo cobrar distinto?',
            'a': 'Defina en encuadre; pol&iacute;tica clara evita conflictos.'}],
  'related': [{'href': '/articulos/telepsicologia-requisitos-legales-mx-co.html',
               'label': 'Requisitos legales'},
              {'href': '/articulos/telepsicologia-etica-mexico-colombia.html',
               'label': 'Ética telepsicología'},
              {'href': '/articulos/consentimiento-informado-elementos-mx-co.html',
               'label': 'Consentimiento MX/CO'},
              {'href': '/articulos/expediente-clinico-electronico-psicologos.html',
               'label': 'Expediente digital'}]},
 {'slug': 'nota-soap-vs-nota-evolucion-libre',
  'title': 'Nota SOAP vs evolución libre: guía clínica 2026 | Kalyo',
  'description': 'Nota SOAP vs nota de evolución libre: cuándo usar cada formato en psicología, '
                 'con ejemplos y criterios de calidad. Guía práctica con tabla comparativa.',
  'keywords': 'nota soap, nota de evolución libre, documentación psicología',
  'h1': 'Nota SOAP vs nota de evolución libre en psicología',
  'breadcrumb_short': 'SOAP vs evolución libre',
  'hero_alt': 'Comparativa nota SOAP y evolución libre',
  'inline_alt': 'Tabla SOAP versus nota libre',
  'meta_label': 'Documentaci&oacute;n &middot; 2026',
  'date_published': '2026-11-16',
  'date_modified': '2026-11-16',
  'quick_answer': 'La <strong>nota SOAP</strong> ordena Subjetivo, Objetivo, An&aacute;lisis y '
                  'Plan para continuidad y auditor&iacute;a. La <strong>nota de evoluci&oacute;n '
                  'libre</strong> permite narrativa flexible pero riesga omisiones si no hay '
                  'plantilla m&iacute;nima. En psicolog&iacute;a, SOAP no es obligatorio pero '
                  'mejora claridad. Alinee a <a '
                  'href="/articulos/nom-004-historia-clinica-mexico.html">NOM-004</a> y vea '
                  'ejemplos en <a '
                  'href="/articulos/nota-evolucion-soap-psicologia.html">gu&iacute;a SOAP</a>.',
  'intro_long': 'Elegir entre <strong>nota SOAP y nota de evoluci&oacute;n libre</strong> afecta '
                'calidad del expediente y defensibilidad cl&iacute;nica ante terceros. Esta '
                'gu&iacute;a compara cu&aacute;ndo usar cada formato, errores comunes y criterios '
                'de calidad con tabla directa. Complementa <a '
                'href="/articulos/nota-evolucion-soap-psicologia.html">nota SOAP en '
                'psicolog&iacute;a</a> y <a href="/articulos/nota-evolucion-psicologica.html">nota '
                'de evoluci&oacute;n base</a> para consultorios que estandarizan '
                'documentaci&oacute;n por sesi&oacute;n.',
  'cta_h2': 'Plantillas SOAP en Kalyo',
  'cta_p': 'Notas estructuradas, historial y trazabilidad &mdash; kalyo.io',
  'card_title': 'Nota SOAP vs evolución libre',
  'card_p': 'Cuándo usar cada formato y criterios de calidad.',
  'after_href': '/articulos/nota-evolucion-soap-psicologia.html',
  'after_loc': 'https://kalyo.io/articulos/nota-evolucion-soap-psicologia.html',
  'asset_from': 'nota-evolucion-soap-psicologia',
  'sections': [{'h2': 'Tabla comparativa nota SOAP vs evoluci&oacute;n libre',
                'html': '<table class="items-table">\n'
                        '<thead><tr><th>Aspecto</th><th>SOAP</th><th>Evoluci&oacute;n '
                        'libre</th></tr></thead>\n'
                        '<tbody>\n'
                        '<tr><td>Estructura</td><td>Cuatro bloques fijos</td><td>Narrativa '
                        'flexible</td></tr>\n'
                        '<tr><td>Legibilidad</td><td>Alta para terceros</td><td>Variable '
                        'seg&uacute;n autor</td></tr>\n'
                        '<tr><td>Tiempo</td><td>R&aacute;pida con plantilla</td><td>Puede '
                        'alargarse si es diario</td></tr>\n'
                        '<tr><td>Auditor&iacute;a</td><td>Facilita revisi&oacute;n de '
                        'plan</td><td>Riesgo de omitir riesgo/plan</td></tr>\n'
                        '<tr><td>Uso ideal</td><td>Rutina y equipo</td><td>Proceso muy '
                        'din&aacute;mico o institucional</td></tr>\n'
                        '</tbody></table>\n'
                        '<p>La tabla orienta respuestas r&aacute;pidas; los apartados siguientes '
                        'detallan matices cl&iacute;nicos y de pr&aacute;ctica.</p>'},
               {'h2': 'Ejemplos de cuándo priorizar SOAP',
                'html': '<p>Seguimiento ambulatorio semanal, equipos con cobertura de colegas, '
                        'facturaci&oacute;n a aseguradoras y casos con riesgo intermitente: SOAP '
                        'obliga a revisar plan y exploraci&oacute;n de riesgo.</p>\n'
                        '<p>Incluya escalas cuando aplican y tareas concretas en Plan.</p>\n'
                        '<p>Evite transcripciones literales en Subjetivo: sintetice con '
                        'precisi&oacute;n cl&iacute;nica.</p>\n'},
               {'h2': 'Cuándo la nota libre aún funciona',
                'html': '<p>Algunos modelos psicodin&aacute;micos usan narrativa extensa; aun '
                        'as&iacute;, debe constar formulaci&oacute;n, intervenci&oacute;n y plan '
                        'impl&iacute;cito. Un checklist interno (riesgo, alianza, tarea) reduce '
                        'vac&iacute;os.</p>\n'
                        '<p>Si la nota libre supera tres p&aacute;ginas sin plan, probablemente '
                        'necesita estructura.</p>\n'
                        '<p>Compare con <a '
                        'href="/articulos/nota-evolucion-psicologica.html">gu&iacute;a base de '
                        'evoluci&oacute;n</a>.</p>\n'},
               {'h2': 'Calidad y expediente digital',
                'html': '<p>Defina plantilla predeterminada SOAP en ECE; permita addendum para '
                        'correcciones sin borrar historial.</p>\n'
                        '<p>Revise muestras trimestrales: &iquest;hay plan en cada nota? '
                        '&iquest;riesgo documentado?</p>\n'
                        '<p><a '
                        'href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=nota-soap-vs-nota-evolucion-libre">Kalyo</a> '
                        'ofrece plantillas SOAP y historial por paciente.</p>\n'
                        '<p>Revise peri&oacute;dicamente su protocolo con supervisi&oacute;n y '
                        'normativa vigente; documente decisiones en el expediente y mantenga '
                        'canales seguros con el paciente. La comparativa resume tendencias; cada '
                        'caso requiere juicio cl&iacute;nico individual.</p><p>Revise '
                        'peri&oacute;dicamente su protocolo con supervisi&oacute;n y normativa '
                        'vigente; documente decisiones en el expediente y mantenga canales seguros '
                        'con el paciente. La comparativa resume tendencias; cada caso requiere '
                        'juicio cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p>'}],
  'faqs': [{'q': '&iquest;SOAP es obligatorio?',
            'a': 'No universalmente; es est&aacute;ndar &uacute;til. Lo obligatorio es documentar '
                 'evoluci&oacute;n cl&iacute;nicamente relevante.'},
           {'q': '&iquest;Puedo mezclar formatos?',
            'a': 'S&iacute;, pero unifique criterio por servicio para no confundir al equipo.'},
           {'q': '&iquest;La libre es menos profesional?',
            'a': 'No; es menos auditable si no hay disciplina.'},
           {'q': '&iquest;IA para redactar?',
            'a': 'Revise contenido y confidencialidad; el profesional responde.'},
           {'q': '&iquest;Longitud ideal?',
            'a': 'La suficiente para continuidad; breve en rutina, ampliada en crisis.'}],
  'related': [{'href': '/articulos/nota-evolucion-soap-psicologia.html', 'label': 'Guía SOAP'},
              {'href': '/articulos/nota-evolucion-psicologica.html', 'label': 'Nota de evolución'},
              {'href': '/articulos/nom-004-historia-clinica-mexico.html', 'label': 'NOM-004'},
              {'href': '/articulos/firma-electronica-notas-clinicas-colombia.html',
               'label': 'Firma electrónica'}]},
 {'slug': 'evaluacion-psicologica-vs-diagnostico-psiquiatrico',
  'title': 'Evaluación psicológica vs diagnóstico: guía 2026 | Kalyo',
  'description': 'Evaluación psicológica vs diagnóstico psiquiátrico: alcances, métodos, límites '
                 'legales y colaboración interdisciplinar. Incluye tabla comparativa clara.',
  'keywords': 'evaluacion psicologica, evaluación psicológica vs diagnóstico psiquiátrico',
  'h1': 'Evaluación psicológica vs diagnóstico psiquiátrico',
  'breadcrumb_short': 'Evaluación vs diagnóstico',
  'hero_alt': 'Comparativa evaluación psicológica y diagnóstico psiquiátrico',
  'inline_alt': 'Tabla evaluación versus diagnóstico',
  'meta_label': 'Evaluaci&oacute;n &middot; Comparativa 2026',
  'date_published': '2026-11-16',
  'date_modified': '2026-11-16',
  'quick_answer': 'La <strong>evaluaci&oacute;n psicol&oacute;gica</strong> integra entrevista, '
                  'tests, observaci&oacute;n y formulaci&oacute;n para orientar '
                  'intervenci&oacute;n psicol&oacute;gica. El <strong>diagn&oacute;stico '
                  'psiqui&aacute;trico</strong> es juicio m&eacute;dico que clasifica para '
                  'tratamiento, pron&oacute;stico y prescripci&oacute;n. Pueden coincidir en '
                  'etiquetas (CIE/DSM) pero el rol y la responsabilidad legal difieren. Apoye con '
                  '<a '
                  'href="/articulos/como-interpretar-tests-psicologicos.html">interpretaci&oacute;n '
                  'de tests</a> y derivaci&oacute;n oportuna.',
  'intro_long': 'Confundir <strong>evaluaci&oacute;n psicol&oacute;gica y diagn&oacute;stico '
                'psiqui&aacute;trico</strong> genera expectativas err&oacute;neas, reclamos y '
                'riesgo legal para el consultorio privado. Esta gu&iacute;a compara alcances, '
                'instrumentos y colaboraci&oacute;n interdisciplinar con tabla clara y criterios '
                'de derivaci&oacute;n. Complementa <a '
                'href="/articulos/como-interpretar-tests-psicologicos.html">c&oacute;mo '
                'interpretar tests</a> y clasificaci&oacute;n en <a '
                'href="/articulos/cie-11-vs-dsm-5-diferencias.html">CIE-11 vs DSM-5</a> sin '
                'convertir la evaluaci&oacute;n en prescripci&oacute;n indirecta.',
  'cta_h2': 'Registra evaluaciones en Kalyo',
  'cta_p': 'Tests, conclusiones y seguimiento en expediente &mdash; kalyo.io',
  'card_title': 'Evaluación psicológica vs diagnóstico',
  'card_p': 'Alcances, métodos y límites legales comparados.',
  'after_href': '/articulos/como-interpretar-tests-psicologicos.html',
  'after_loc': 'https://kalyo.io/articulos/como-interpretar-tests-psicologicos.html',
  'asset_from': 'como-interpretar-tests-psicologicos',
  'sections': [{'h2': 'Tabla comparativa evaluaci&oacute;n vs diagn&oacute;stico',
                'html': '<table class="items-table">\n'
                        '<thead><tr><th>Aspecto</th><th>Evaluaci&oacute;n '
                        'psicol&oacute;gica</th><th>Diagn&oacute;stico '
                        'psiqui&aacute;trico</th></tr></thead>\n'
                        '<tbody>\n'
                        '<tr><td>Profesional</td><td>Psic&oacute;logo</td><td>Psiquiatra</td></tr>\n'
                        '<tr><td>M&eacute;todos</td><td>Tests, entrevistas, '
                        'observaci&oacute;n</td><td>Examen m&eacute;dico, historia, '
                        'estudios</td></tr>\n'
                        '<tr><td>Salida</td><td>Informe y '
                        'formulaci&oacute;n</td><td>Diagn&oacute;stico m&eacute;dico y '
                        'tratamiento</td></tr>\n'
                        '<tr><td>Medicaci&oacute;n</td><td>No prescribe</td><td>Indica y ajusta '
                        'f&aacute;rmacos</td></tr>\n'
                        '<tr><td>Colaboraci&oacute;n</td><td>Aporta funcionamiento y '
                        'cognici&oacute;n</td><td>Aporta comorbilidad m&eacute;dica</td></tr>\n'
                        '</tbody></table>\n'
                        '<p>La tabla orienta respuestas r&aacute;pidas; los apartados siguientes '
                        'detallan matices cl&iacute;nicos y de pr&aacute;ctica.</p>'},
               {'h2': 'Instrumentos y límites de interpretación',
                'html': '<p>El psic&oacute;logo selecciona bater&iacute;as con validez y validez '
                        'local; interpreta en contexto, no como verdad absoluta. El psiquiatra '
                        'integra hallazgos m&eacute;dicos, laboratorio y examen neurol&oacute;gico '
                        'cuando corresponde.</p>\n'
                        '<p>No entregue al paciente etiquetas diagn&oacute;sticas como sentencia; '
                        'explique hip&oacute;tesis y pasos siguientes.</p>\n'
                        '<p>Revise <a href="/articulos/phq-9-escala-depresion.html">PHQ-9</a> y '
                        'otras escalas como apoyo, no reemplazo cl&iacute;nico.</p>\n'},
               {'h2': 'Informes y comunicación con referentes',
                'html': '<p>El informe psicol&oacute;gico describe procedimiento, resultados, '
                        'fortalezas, limitaciones y recomendaciones. El informe '
                        'psiqui&aacute;trico documenta diagn&oacute;stico m&eacute;dico y plan '
                        'farmacol&oacute;gico.</p>\n'
                        '<p>Al compartir con escuelas o empleadores, minimice datos sensibles y '
                        'obtenga consentimiento.</p>\n'
                        '<p>Use lenguaje comprensible para paciente y t&eacute;cnico para '
                        'colegas.</p>\n'},
               {'h2': 'Derivación y trabajo en equipo',
                'html': '<p>Derive cuando haya indicio de psicosis, man&iacute;a, riesgo vital o '
                        'necesidad de medicaci&oacute;n. Reunir evaluaci&oacute;n '
                        'psicol&oacute;gica reciente acelera consulta psiqui&aacute;trica.</p>\n'
                        '<p>Evite duplicar evaluaciones costosas sin coordinaci&oacute;n.</p>\n'
                        '<p><a '
                        'href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=evaluacion-psicologica-vs-diagnostico-psiquiatrico">Kalyo</a> '
                        'almacena resultados de tests y evoluci&oacute;n en un solo '
                        'expediente.</p>\n'
                        '<p>Revise peri&oacute;dicamente su protocolo con supervisi&oacute;n y '
                        'normativa vigente; documente decisiones en el expediente y mantenga '
                        'canales seguros con el paciente. La comparativa resume tendencias; cada '
                        'caso requiere juicio cl&iacute;nico individual.</p><p>Revise '
                        'peri&oacute;dicamente su protocolo con supervisi&oacute;n y normativa '
                        'vigente; documente decisiones en el expediente y mantenga canales seguros '
                        'con el paciente. La comparativa resume tendencias; cada caso requiere '
                        'juicio cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p>'}],
  'faqs': [{'q': '&iquest;El psic&oacute;logo da diagnóstico?',
            'a': 'Formula y clasifica para psicoterapia; diagn&oacute;stico m&eacute;dico es del '
                 'psiquiatra.'},
           {'q': '&iquest;Los tests diagnostican solos?',
            'a': 'No; son herramientas que requieren integraci&oacute;n cl&iacute;nica.'},
           {'q': '&iquest;Debo usar CIE o DSM?', 'a': 'Sea consistente y documente sistema usado.'},
           {'q': '&iquest;Informe verbal basta?',
            'a': 'Para continuidad interna a veces; formalice por escrito ante terceros.'},
           {'q': '&iquest;Cu&aacute;ndo reevaluar?',
            'a': 'Seg&uacute;n motivo: seguimiento, cambio marcado o solicitud institucional.'}],
  'related': [{'href': '/articulos/como-interpretar-tests-psicologicos.html',
               'label': 'Interpretar tests'},
              {'href': '/articulos/cie-11-vs-dsm-5-diferencias.html', 'label': 'CIE-11 vs DSM-5'},
              {'href': '/articulos/psicologo-vs-psiquiatra-diferencias.html',
               'label': 'Psicólogo vs psiquiatra'},
              {'href': '/articulos/historia-clinica-psicologica-paso-a-paso.html',
               'label': 'Historia clínica'}]},
 {'slug': 'software-psicologos-vs-excel-google-drive',
  'title': 'Software para psicólogos vs Excel y Drive: guía | Kalyo',
  'description': 'Software para psicólogos vs Excel/Google Drive: por qué migrar, riesgos de hojas '
                 'sueltas y beneficios del ECE digital. Incluye tabla comparativa clara.',
  'keywords': 'software para psicologos, Excel Google Drive psicología, expediente digital',
  'h1': 'Software para psicólogos vs Excel y Google Drive',
  'breadcrumb_short': 'Software vs Excel/Drive',
  'hero_alt': 'Software para psicólogos versus Excel y Google Drive',
  'inline_alt': 'Comparativa software clínico y hojas de cálculo',
  'meta_label': 'Herramientas &middot; Consultorio 2026',
  'date_published': '2026-11-16',
  'date_modified': '2026-11-16',
  'quick_answer': '<strong>Excel y Google Drive</strong> sirven para listas sueltas, pero fracasan '
                  'en expediente cl&iacute;nico: sin historia integrada, bit&aacute;cora ni '
                  'control fino de acceso. Un <strong>software para psic&oacute;logos</strong> une '
                  'agenda, expediente, notas y consentimientos con trazabilidad. Migrar reduce '
                  'errores de archivo y libera tiempo cl&iacute;nico. Compare con <a '
                  'href="/articulos/expediente-clinico-electronico-psicologos.html">ECE</a> y '
                  'evite carpetas compartidas sin pol&iacute;tica.',
  'intro_long': 'Muchos consultorios inician en <strong>Excel y Drive</strong> y se quedan '
                'ah&iacute; por costumbre o por precio aparente bajo cada mes. Esta gu&iacute;a '
                'compara hojas sueltas versus <strong>software para psic&oacute;logos</strong>: '
                'riesgos, costos ocultos y beneficios del expediente digital con tabla clara. '
                'Complementa <a href="/articulos/agenda-para-psicologos.html">agenda para '
                'psic&oacute;logos</a> y <a '
                'href="/articulos/expediente-clinico-papel-vs-digital.html">papel vs digital</a> '
                'con puente directo al producto Kalyo para migrar sin fricci&oacute;n.',
  'cta_h2': 'De Excel a expediente clínico con Kalyo',
  'cta_p': 'Agenda, historia, SOAP y permisos en un solo lugar &mdash; kalyo.io',
  'card_title': 'Software vs Excel y Drive',
  'card_p': 'Por qué migrar y qué gana el consultorio.',
  'after_href': '/articulos/software-para-psicologos-comparativa.html',
  'after_loc': 'https://kalyo.io/articulos/agenda-para-psicologos.html',
  'asset_from': 'agenda-para-psicologos',
  'sections': [{'h2': 'Tabla comparativa software vs Excel y Drive',
                'html': '<table class="items-table">\n'
                        '<thead><tr><th>Aspecto</th><th>Excel / Drive</th><th>Software '
                        '(Kalyo)</th></tr></thead>\n'
                        '<tbody>\n'
                        '<tr><td>Paciente</td><td>Filas duplicadas / archivos '
                        'sueltos</td><td>Expediente &uacute;nico por persona</td></tr>\n'
                        '<tr><td>Agenda</td><td>Manual o calendario aparte</td><td>Citas ligadas '
                        'al expediente</td></tr>\n'
                        '<tr><td>Notas</td><td>Documentos dispersos</td><td>SOAP con historial y '
                        'autor&iacute;a</td></tr>\n'
                        '<tr><td>Seguridad</td><td>Cuentas compartidas</td><td>Usuarios '
                        'individuales y roles</td></tr>\n'
                        '<tr><td>Cumplimiento</td><td>Dif&iacute;cil auditar</td><td>Orientado a '
                        'pr&aacute;ctica cl&iacute;nica documentada</td></tr>\n'
                        '</tbody></table>\n'
                        '<p>La tabla orienta respuestas r&aacute;pidas; los apartados siguientes '
                        'detallan matices cl&iacute;nicos y de pr&aacute;ctica.</p>'},
               {'h2': 'Costos ocultos de las hojas de cálculo',
                'html': '<p>Tiempo buscando archivos, versiones &laquo;final_v3&raquo;, notas '
                        'fuera del expediente y citas sin documentar son costos reales. Un no-show '
                        'sin registro tambi&eacute;n cuenta.</p>\n'
                        '<p>Drive no reemplaza bit&aacute;cora cl&iacute;nica ni consentimientos '
                        'integrados.</p>\n'
                        '<p>Vea <a '
                        'href="/articulos/reducir-inasistencias-consulta-psicologica.html">reducir '
                        'inasistencias</a> al centralizar agenda.</p>\n'},
               {'h2': 'Qué debe tener software clínico',
                'html': '<p>Historia estructurada, notas por sesi&oacute;n, consentimientos, '
                        'exportaci&oacute;n, respaldo y soporte. Opcional: tests y teleconsulta '
                        'seg&uacute;n su modelo.</p>\n'
                        '<p>Compare opciones en <a '
                        'href="/articulos/software-para-psicologos-comparativa.html">comparativa '
                        'de software</a>.</p>\n'
                        '<p>Pruebe dos semanas con pacientes piloto antes de migrar todo el '
                        'archivo.</p>\n'},
               {'h2': 'Migración gradual hacia Kalyo',
                'html': '<p>Empiece con pacientes nuevos; cargue activos; mantenga lectura del '
                        'archivo antiguo hasta cerrar plazos legales.</p>\n'
                        '<p>Capacite en una plantilla SOAP &uacute;nica y no vuelva a Excel para '
                        'notas nuevas.</p>\n'
                        '<p><a '
                        'href="https://app.kalyo.io/register?utm_source=blog&utm_medium=article&utm_campaign=software-psicologos-vs-excel-google-drive">Kalyo</a> '
                        'integra agenda, expediente y registro orientado a psicolog&iacute;a: '
                        'menos fricci&oacute;n que mantener hoja, carpeta y calendario '
                        'separados.</p>\n'
                        '<p>Revise peri&oacute;dicamente su protocolo con supervisi&oacute;n y '
                        'normativa vigente; documente decisiones en el expediente y mantenga '
                        'canales seguros con el paciente. La comparativa resume tendencias; cada '
                        'caso requiere juicio cl&iacute;nico individual.</p><p>Revise '
                        'peri&oacute;dicamente su protocolo con supervisi&oacute;n y normativa '
                        'vigente; documente decisiones en el expediente y mantenga canales seguros '
                        'con el paciente. La comparativa resume tendencias; cada caso requiere '
                        'juicio cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p><p>Revise peri&oacute;dicamente su '
                        'protocolo con supervisi&oacute;n y normativa vigente; documente '
                        'decisiones en el expediente y mantenga canales seguros con el paciente. '
                        'La comparativa resume tendencias; cada caso requiere juicio '
                        'cl&iacute;nico individual.</p>'}],
  'faqs': [{'q': '&iquest;Excel es ilegal para expediente?',
            'a': 'No si cumple contenido; es fr&aacute;gil para seguridad y continuidad.'},
           {'q': '&iquest;Puedo seguir con Drive para respaldo?',
            'a': 'S&iacute; como copia si est&aacute; cifrado y es secundario al ECE principal.'},
           {'q': '&iquest;Cu&aacute;nto tarda migrar?',
            'a': 'Semanas seg&uacute;n volumen; planifique cargas por lotes.'},
           {'q': '&iquest;Kalyo exporta datos?',
            'a': 'Revise exportaci&oacute;n en prueba; evite dependencia sin salida.'},
           {'q': '&iquest;Vale la pena si soy solo?',
            'a': 'A menudo s&iacute;: el tiempo recuperado en documentaci&oacute;n paga la '
                 'licencia.'}],
  'related': [{'href': '/articulos/agenda-para-psicologos.html', 'label': 'Agenda para psicólogos'},
              {'href': '/articulos/expediente-clinico-electronico-psicologos.html',
               'label': 'ECE psicólogos'},
              {'href': '/articulos/software-para-psicologos-comparativa.html',
               'label': 'Comparativa software'},
              {'href': '/articulos/reducir-inasistencias-consulta-psicologica.html',
               'label': 'Reducir inasistencias'}]}]

def copy_assets(slug: str, src_slug: str) -> None:
    for kind in ("hero", "inline"):
        for ext in ("jpg", "webp"):
            src = ASSETS / f"{src_slug}-{kind}.{ext}"
            dst = ASSETS / f"{slug}-{kind}.{ext}"
            if not src.exists():
                continue
            if not dst.exists():
                shutil.copy2(src, dst)


def ensure_assets(slug: str, src_slug: str) -> None:
    copy_assets(slug, src_slug)
    for fb in (
        "nom-004-historia-clinica-mexico",
        "nota-evolucion-psicologica",
        "rips-registros-individuales-colombia",
        "expediente-clinico-electronico-psicologos",
        "lfpdppp-proteccion-datos-psicologos-mexico",
        "consentimiento-informado-psicologia",
        "agenda-para-psicologos",
        "alianza-terapeutica",
        "cie-11-vs-dsm-5-diferencias",
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
            f'        <span class="blog-card-tag">Gu&iacute;a comparativa</span>\n'
            f'        <h3>{spec["card_title"]}</h3>\n'
            f'        <p>{spec["card_p"]}</p>\n'
            f"      </a>\n"
        )
        insert_card(spec["after_href"], card)
        bump_counts(1)
    else:
        print("card exists, skip bump")

    insert_sitemap(spec["after_loc"], f"https://kalyo.io/articulos/{slug}.html", lastmod="2026-11-16")
    print("UPDATED", slug)
    return info


def main() -> None:
    asset_aliases = {
        "cie-11-vs-dsm-5-diferencias": ["cie-11-vs-dsm-5-diferencias", "cie-11-trastornos-mentales-psicologos"],
        "telepsicologia-etica-mexico-colombia": [
            "telepsicologia-etica-mexico-colombia",
            "telepsicologia-requisitos-legales-mx-co",
        ],
        "como-interpretar-tests-psicologicos": ["como-interpretar-tests-psicologicos", "phq-9-escala-depresion"],
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
        src = spec["asset_from"]
        for cand in asset_aliases.get(src, [src]):
            if (ASSETS / f"{cand}-hero.jpg").exists():
                spec["asset_from"] = cand
                break
        publish(spec)


if __name__ == "__main__":
    main()
