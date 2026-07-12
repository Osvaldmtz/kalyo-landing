import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const OUTPUT_PATH = path.join(__dirname, 'doi-alternatives-round2.csv');
const VERIFY_TIMEOUT_MS = 8000;
const PERPLEXITY_URL = 'https://api.perplexity.ai/chat/completions';

const BROKEN_URLS = [
  ['pass-sensibilidad-ansiedad', 'https://doi.org/10.1007/s00737-015-0498-9'],
  ['test-beck-ansiedad-bai', 'https://doi.org/10.1016/j.acp.2020.01.001'],
  ['tests-psicologicos-digitales', 'https://doi.org/10.1016/j.rpe.2019.02.004'],
  ['faces-iv-escala-adaptabilidad-familiar', 'https://doi.org/10.1016/j.salm.2015.03.002'],
  ['mdq-trastorno-bipolar-tamizaje', 'https://doi.org/10.1016/S0301-0081(05)70012-3'],
  ['ecr-cuestionario-apego-adultos', 'https://doi.org/10.4067/s0718-50652020000300080'],
  ['core-om-medida-resultados-clinicos', 'https://doi.org/10.1016/j.revaluar.2024.05.003'],
  ['oq-45-resultados-terapia', 'https://doi.org/10.1080/08039481.2012.679150'],
  ['scared-ansiedad-infantil', 'https://doi.org/10.5093/rpccna2011a6'],
  ['audit-test-alcoholismo', 'https://adicciones.es/index.php/adicciones/article/download/613/602/1170'],
  ['que-es-el-phq-9', 'https://investigacion.upb.edu.co/es/publications/construct-validity-of-the-phq-9-in-university-students-in-colombi/'],
  ['ley-1581-proteccion-datos-psicologia', 'https://www.sic.gov.co/resoluciones/2797-2013'],
  ['assist-evaluacion-sustancias-oms', 'https://adicciones.es/index.php/adicciones/article/download/1496/1232/5103'],
  ['ley-1090-psicologia-colombia', 'https://www.colpsic.org.co/normatividad/'],
  ['asrs-tdah-adultos', 'https://www.adicciones.es/index.php/adicciones/article/download/298/298/577'],
  ['adhd-rs-5-tdah-ninos', 'https://www.sciencedirect.com/science/article/pii/S0213485317302244'],
  ['raads-r-autismo-adultos', 'https://novopsych.com/es-us/evaluaciones/diagnostico/escala-diagnostica-del-espectro-autista-de-ritvo-revisada-raads-r/'],
  ['consentimiento-informado-psicologia', 'https://www.colpsic.org.co/wp-content/uploads/2020/12/Doctrina-No.-3-CONSENTIMIENTO-INFORMADO-dic-5-2018.pdf'],
  ['audit-c-tamizaje-alcohol-breve', 'https://www.adicciones.es/index.php/adicciones/article/viewFile/775/730'],
  ['test-reloj-dibujo-cognicion', 'https://revecuatneurol.com/'],
  ['ftnd-test-nicotina-dependencia', 'https://revistasdigitales.uniboyaca.edu.co/index.php/rs/article/download/185/200/527'],
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

async function findAlternativeUrl(brokenUrl, apiKey) {
  const prompt = `Find the correct working URL for this academic paper or resource: ${brokenUrl}.
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
      return extractUrl(content);
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

async function processEntry([article, brokenUrl], index, total, apiKey) {
  console.log(`[${index + 1}/${total}] ${article} — ${brokenUrl}`);

  let alternativeUrl = 'NOT_FOUND';
  let statusCode = '';
  let verified = 'NO';

  try {
    const foundUrl = await findAlternativeUrl(brokenUrl, apiKey);
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
    broken_url: brokenUrl,
    alternative_url: alternativeUrl,
    status_code: statusCode,
    verified,
  };
}

function writeCsv(rows) {
  const header = ['article', 'broken_url', 'alternative_url', 'status_code', 'verified'];
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

  console.log(`Processing ${BROKEN_URLS.length} broken URLs...`);
  const rows = [];

  for (let i = 0; i < BROKEN_URLS.length; i += 1) {
    const row = await processEntry(BROKEN_URLS[i], i, BROKEN_URLS.length, apiKey);
    rows.push(row);
    if (i < BROKEN_URLS.length - 1) {
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

// Run: PERPLEXITY_API_KEY=$(grep PERPLEXITY_API_KEY .env.local | cut -d '=' -f2) node scripts/fix-broken-dois-round2.mjs
