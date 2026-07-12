import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const OUTPUT_PATH = path.join(__dirname, 'doi-alternatives.csv');
const VERIFY_TIMEOUT_MS = 8000;
const PERPLEXITY_URL = 'https://api.perplexity.ai/chat/completions';

const BROKEN_DOIS = [
  ['vineland-3-conducta-adaptativa', 'https://doi.org/10.1186/s13229-017-0137-7'],
  ['aces-adversidad-infantil', 'https://doi.org/10.1017/S0033291716003550'],
  ['test-beck-ansiedad-bai', 'https://doi.org/10.1016/j.acp.2020.01.001'],
  ['tests-psicologicos-digitales', 'https://doi.org/10.1016/j.rpe.2019.02.004'],
  ['gds-15-depresion-geriatrica', 'https://doi.org/10.11111/rcp.2020.59511493'],
  ['mchat-rf-autismo-infantil', 'https://doi.org/10.1016/j.rchped.2023.0703'],
  ['scared-ansiedad-infantil', 'https://doi.org/10.1016/j.anest.2011.03.002'],
  ['eat-26-trastornos-alimentarios', 'https://doi.org/10.31239/actamedicacol.44.2.2019'],
  ['adhd-rs-5-tdah-ninos', 'https://doi.org/10.1016/S0022-4405(97)00012-3'],
  ['faces-iv-escala-adaptabilidad-familiar', 'https://doi.org/10.1016/j.salm.2015.03.002'],
  ['mdq-trastorno-bipolar-tamizaje', 'https://doi.org/10.1016/S0301-0081(05)70012-3'],
  ['test-vocacional-riasec', 'https://doi.org/10.1016/j.jvb.2016.03.005'],
  ['aces-adversidad-infantil', 'https://doi.org/10.1016/S0749-3792(97)00291-7'],
  ['mdq-trastorno-bipolar-tamizaje', 'https://doi.org/10.1097/00129333-200002000-00003'],
  ['inventario-depresion-beck-bdi', 'https://doi.org/10.5093/clinsal2003a14'],
  ['wisc-v-test-inteligencia-ninos', 'https://doi.org/10.1177/073805704022002003'],
  ['vineland-3-conducta-adaptativa', 'https://doi.org/10.1007/s10803-013-1876-9'],
  ['inventario-burnout-mbi', 'https://doi.org/10.1080/cesp.v9n1.v9n1a02'],
  ['mchat-rf-autismo-infantil', 'https://doi.org/10.1097/DBP.0b013e3181a5b8d0'],
  ['raads-r-autismo-adultos', 'https://doi.org/10.1007/s10803-011-0286-5'],
  ['scl-90-r-lista-sintomas-revisada', 'https://doi.org/10.4321/S0212-97232002000000000'],
  ['escala-hamilton-ansiedad-ham-a', 'https://doi.org/10.1080/13651502.2020.1756342'],
  ['mmpi-2-rf-test-personalidad', 'https://doi.org/10.1080/07356666.2011.567890'],
  ['lsas-ansiedad-social-liebowitz', 'https://doi.org/10.1016/S0005-7967(99)00029-5'],
  ['raads-r-autismo-adultos', 'https://doi.org/10.1007/s10803-025-0312-9'],
  ['test-moca-evaluacion-cognitiva', 'https://doi.org/10.1016/S0185-3325(14)70010-0'],
  ['evaluacion-psicologica-colombia-mexico', 'https://doi.org/10.2183-6051.2024.67b62b984c5cd64deffbedf3'],
  ['enrich-inventario-relacion-pareja', 'https://doi.org/10.1037/1999-IPRS'],
  ['escala-pcl-5-estres-postraumatico', 'https://doi.org/10.1016/j.anyes.2014.01.002'],
  ['mmpi-2-rf-test-personalidad', 'https://doi.org/10.7334/psicothema2012.234'],
  ['test-moca-evaluacion-cognitiva', 'https://doi.org/10.1016/j.neuroci.2016.03.005'],
  ['vineland-3-conducta-adaptativa', 'https://doi.org/10.1007/s10803-006-0055-9'],
  ['y-bocs-escala-yale-brown-toc', 'https://doi.org/10.1016/j.psychres.2018.116456'],
  ['phq-15-sintomas-somaticos', 'https://doi.org/10.1111/j.1468-0148.2011.00746.x'],
  ['lsas-ansiedad-social-liebowitz', 'https://doi.org/10.1016/S0749-3797(02)00530-9'],
  ['rips-registros-individuales-colombia', 'https://doi.org/10.1186/s12873-024-01098-7'],
  ['ecr-cuestionario-apego-adultos', 'https://doi.org/10.4067/s0718-50652020000300080'],
  ['vineland-3-conducta-adaptativa', 'https://doi.org/10.1007/s10803-011-0299-9'],
  ['who-5-bienestar-psicologico', 'https://doi.org/10.5281/cyrev.2024.525'],
  ['mini-entrevista-diagnostica-estructurada', 'https://doi.org/10.18845/revmedhjca.v88.n80.147'],
  ['c-ssrs-escala-columbia-suicidio', 'https://doi.org/10.1176/appi.ajp.2010.10050776'],
  ['faces-iv-escala-adaptabilidad-familiar', 'https://doi.org/10.18800/2013000200002'],
  ['como-interpretar-tests-psicologicos', 'https://doi.org/10.1001/archinternmed.166.10.1092'],
  ['wais-iv-evaluacion-inteligencia-adultos', 'https://doi.org/10.7334/psicothema2011.102'],
  ['evaluacion-psicologica-colombia-mexico', 'https://doi.org/10.1093-psicologiaysalud.udenar.2024.QBLG'],
  ['tests-psicologicos-digitales', 'https://doi.org/10.11144/rip.14.102'],
  ['scl-90-r-lista-sintomas-revisada', 'https://doi.org/10.1016/S0022-3999(02)00000-0'],
  ['diagnostico-tea-adultos-colombia', 'https://doi.org/10.1007/s10803-006-0056-9'],
  ['que-es-el-gad-7', 'https://doi.org/10.1016/j.jcp.2020.03.005'],
  ['test-beck-ansiedad-bai', 'https://doi.org/10.1016/S0214-987X(03)70001-2'],
  ['adir-r-entrevista-autismo', 'https://doi.org/10.1002/9780470547038.ch12'],
  ['mini-entrevista-diagnostica-estructurada', 'https://doi.org/10.1111/j.1600-0447.1998.tb10997.x'],
  ['escala-hamilton-ansiedad-ham-a', 'https://doi.org/10.1016/0165-0327(88)90027-3'],
  ['gds-15-depresion-geriatrica', 'https://doi.org/10.33999/rpsy.2021.9606717'],
  ['ados-2-evaluacion-tea', 'https://doi.org/10.1007/s10803-023-05892-x'],
  ['adir-r-entrevista-autismo', 'https://doi.org/10.31829/vertex.941.730'],
  ['ados-2-evaluacion-tea', 'https://doi.org/10.1176/appi.ajp.166.5.589'],
  ['core-om-medida-resultados-clinicos', 'https://doi.org/10.1007/s41234-025-00001-x'],
  ['diagnostico-tea-adultos-colombia', 'https://doi.org/10.18273/revmeduis.v32n2-201916096'],
  ['lsas-ansiedad-social-liebowitz', 'https://doi.org/10.1016/S0887-618X(02)00129-5'],
  ['core-om-medida-resultados-clinicos', 'https://doi.org/10.1016/j.revaluar.2024.05.003'],
  ['lsas-ansiedad-social-liebowitz', 'https://doi.org/10.1097/0146-8244-42-9-1076'],
  ['evaluacion-psicologica-colombia-mexico', 'https://doi.org/10.1688-4221.2024.0001.01212'],
  ['ecr-cuestionario-apego-adultos', 'https://doi.org/10.4067/s0718-50652007000300080'],
  ['test-beck-ansiedad-bai', 'https://doi.org/10.1037/1072-524X.1.1.1'],
  ['scl-90-r-lista-sintomas-revisada', 'https://doi.org/10.1080/14650120500185332'],
  ['oq-45-resultados-terapia', 'https://doi.org/10.1080/08039481.2012.679150'],
  ['escala-hamilton-ansiedad-ham-a', 'https://doi.org/10.1111/j.2044-8341.1959.tb00907.x'],
  ['isi-indice-severidad-insomnio', 'https://doi.org/10.1002/jclp.4990530405'],
  ['isi-indice-severidad-insomnio', 'https://doi.org/10.13140/RG.2.2.39472.1'],
  ['ess-escala-somnolencia-epworth', 'https://doi.org/10.1093/sleep/17.2.123'],
  ['scared-ansiedad-infantil', 'https://doi.org/10.5093/rpccna2011a6'],
];

function csvEscape(value) {
  const text = String(value ?? '');
  if (/[",\n\r]/.test(text)) {
    return `"${text.replace(/"/g, '""')}"`;
  }
  return text;
}

function extractUrl(text) {
  if (!text) return null;
  const cleaned = text.trim().replace(/^```(?:\w+)?\s*/i, '').replace(/\s*```$/, '');
  const match = cleaned.match(/https?:\/\/[^\s<>"')\]]+/i);
  if (!match) return null;
  return match[0].replace(/[.,;]+$/, '');
}

async function findAlternativeUrl(doi, apiKey) {
  const prompt = `Find the correct working URL for this academic paper DOI: ${doi}.
Look for the paper on PubMed, PsycINFO, ResearchGate, Semantic Scholar, or the journal's official site.
Return ONLY the URL, nothing else.`;

  let lastError = null;
  for (let attempt = 0; attempt < 3; attempt += 1) {
    try {
      const response = await fetch(PERPLEXITY_URL, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${apiKey}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'sonar',
          messages: [{ role: 'user', content: prompt }],
          temperature: 0.1,
        }),
      });

      if (!response.ok) {
        throw new Error(`Perplexity HTTP ${response.status}: ${await response.text()}`);
      }

      const data = await response.json();
      const content = data?.choices?.[0]?.message?.content?.trim() ?? '';
      const url = extractUrl(content);
      return url;
    } catch (error) {
      lastError = error;
      if (attempt < 2) {
        await new Promise((resolve) => setTimeout(resolve, 2000 * (attempt + 1)));
      }
    }
  }

  throw lastError ?? new Error('Perplexity request failed');
}

async function verifyUrl(url) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), VERIFY_TIMEOUT_MS);

  try {
    const response = await fetch(url, {
      method: 'HEAD',
      redirect: 'follow',
      signal: controller.signal,
      headers: {
        'User-Agent': 'KalyoDOIFixer/1.0',
      },
    });

    return {
      statusCode: response.status,
      verified: response.status >= 200 && response.status < 400 ? 'YES' : 'NO',
    };
  } catch (error) {
    const isTimeout = error?.name === 'AbortError';
    return {
      statusCode: isTimeout ? 'TIMEOUT' : 'ERROR',
      verified: 'NO',
    };
  } finally {
    clearTimeout(timer);
  }
}

async function processEntry([article, brokenDoi], index, total, apiKey) {
  console.log(`[${index + 1}/${total}] ${article} — ${brokenDoi}`);

  let alternativeUrl = 'NOT_FOUND';
  let statusCode = '';
  let verified = 'NO';

  try {
    const foundUrl = await findAlternativeUrl(brokenDoi, apiKey);
    if (foundUrl) {
      alternativeUrl = foundUrl;
      const check = await verifyUrl(foundUrl);
      statusCode = check.statusCode;
      verified = check.verified;
      console.log(`  -> ${alternativeUrl} (${statusCode}, ${verified})`);
    } else {
      console.log('  -> NOT_FOUND');
    }
  } catch (error) {
    console.log(`  -> ERROR: ${error.message}`);
    alternativeUrl = 'NOT_FOUND';
    statusCode = 'ERROR';
    verified = 'NO';
  }

  return {
    article,
    broken_doi: brokenDoi,
    alternative_url: alternativeUrl,
    status_code: statusCode,
    verified,
  };
}

function writeCsv(rows) {
  const header = ['article', 'broken_doi', 'alternative_url', 'status_code', 'verified'];
  const lines = [
    header.join(','),
    ...rows.map((row) => header.map((key) => csvEscape(row[key])).join(',')),
  ];
  fs.writeFileSync(OUTPUT_PATH, `${lines.join('\n')}\n`, 'utf8');
}

async function main() {
  const apiKey = process.env.PERPLEXITY_API_KEY;
  if (!apiKey) {
    console.error('Missing PERPLEXITY_API_KEY environment variable.');
    process.exit(1);
  }

  console.log(`Processing ${BROKEN_DOIS.length} broken DOIs...`);
  const rows = [];

  for (let i = 0; i < BROKEN_DOIS.length; i += 1) {
    const row = await processEntry(BROKEN_DOIS[i], i, BROKEN_DOIS.length, apiKey);
    rows.push(row);
    if (i < BROKEN_DOIS.length - 1) {
      await new Promise((resolve) => setTimeout(resolve, 1000));
    }
  }

  writeCsv(rows);

  const verifiedCount = rows.filter((row) => row.verified === 'YES').length;
  const notFoundCount = rows.filter((row) => row.alternative_url === 'NOT_FOUND').length;
  console.log(`\nWrote ${OUTPUT_PATH}`);
  console.log(`Verified: ${verifiedCount}/${rows.length}`);
  console.log(`Not found: ${notFoundCount}/${rows.length}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});

// Run: PERPLEXITY_API_KEY=xxx node scripts/fix-broken-dois.mjs
