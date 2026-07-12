import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ARTICULOS_DIR = path.join(__dirname, '..', 'articulos');

const RULE1 = [
  ['scared-ansiedad-infantil.html', 'https://doi.org/10.1016/j.anest.2011.03.002', 'https://pubmed.ncbi.nlm.nih.gov/22050799/'],
  ['aces-adversidad-infantil.html', 'https://doi.org/10.1016/S0749-3792(97)00291-7', 'https://pubmed.ncbi.nlm.nih.gov/9563278/'],
  ['inventario-burnout-mbi.html', 'https://doi.org/10.1080/cesp.v9n1.v9n1a02', 'http://www.scielo.org.co/pdf/cesp/v9n1/v9n1a02.pdf'],
  ['mmpi-2-rf-test-personalidad.html', 'https://doi.org/10.7334/psicothema2012.234', 'https://www.psicothema.com/pdf/4088.pdf'],
  ['test-moca-evaluacion-cognitiva.html', 'https://doi.org/10.1016/j.neuroci.2016.03.005', 'https://pubmed.ncbi.nlm.nih.gov/27242063/'],
  ['faces-iv-escala-adaptabilidad-familiar.html', 'https://doi.org/10.18800/2013000200002', 'https://revistas.pucp.edu.pe/index.php/revistapsicologia/article/view/20002'],
  ['como-interpretar-tests-psicologicos.html', 'https://doi.org/10.1001/archinternmed.166.10.1092', 'https://pubmed.ncbi.nlm.nih.gov/16717171/'],
  ['wais-iv-evaluacion-inteligencia-adultos.html', 'https://doi.org/10.7334/psicothema2011.102', 'https://www.psicothema.com/pi?pii=4090'],
];

const RULE2_URLS = [
  'https://www.sciencedirect.com/science/article/pii/S2210271X20000013',
  'https://www.sciencedirect.com/science/article/pii/S0039625719300463',
  'https://www.sciencedirect.com/science/article/pii/S2214509815000028',
  'https://www.sciencedirect.com/science/article/pii/S221128551400002X',
  'https://www.sciencedirect.com/science/article/pii/S0021999120301699',
  'https://www.cambridge.org/core/journals/psychological-medicine/article/abs/10.1017/S0033291716003550',
  'https://www.tandfonline.com/doi/full/10.1080/13651502.2020.1756342',
  'https://www.tandfonline.com/doi/10.1080/08039481.2012.679150',
  'https://www.scielo.cl/scielo.php?script=sci_arttext&pid=S0718-50652020000300080',
  'https://www.scielo.cl/scielo.php?script=sci_arttext&pid=S0718-50652007000300080',
  'https://adicciones.es/index.php/adicciones/article/download/613/602/1170',
  'https://www.adicciones.es/index.php/adicciones/article/download/298/298/577',
  'https://adicciones.es/index.php/adicciones/article/download/1496/1232/5103',
  'https://www.sciencedirect.com/science/article/pii/S0213485317302244',
  'https://investigacion.upb.edu.co/es/publications/construct-validity-of-the-phq-9-in-university-students-in-colombi/',
  'https://www.colpsic.org.co/normatividad/',
  'https://www.sic.gov.co/resoluciones/2797-2013',
  'https://novopsych.com/es-us/evaluaciones/diagnostico/escala-diagnostica-del-espectro-autista-de-ritvo-revisada-raads-r/',
];

const RULE3_DOIS = [
  'https://doi.org/10.1186/s13229-017-0137-7',
  'https://doi.org/10.1017/S0033291716003550',
  'https://doi.org/10.11111/rcp.2020.59511493',
  'https://doi.org/10.1016/j.rchped.2023.0703',
  'https://doi.org/10.31239/actamedicacol.44.2.2019',
  'https://doi.org/10.1016/S0022-4405(97)00012-3',
  'https://doi.org/10.1097/00129333-200002000-00003',
  'https://doi.org/10.5093/clinsal2003a14',
  'https://doi.org/10.1177/073805704022002003',
  'https://doi.org/10.1007/s10803-013-1876-9',
  'https://doi.org/10.1097/DBP.0b013e3181a5b8d0',
  'https://doi.org/10.1007/s10803-011-0286-5',
  'https://doi.org/10.4321/S0212-97232002000000000',
  'https://doi.org/10.1080/07356666.2011.567890',
  'https://doi.org/10.1016/S0005-7967(99)00029-5',
  'https://doi.org/10.1007/s10803-025-0312-9',
  'https://doi.org/10.1016/S0185-3325(14)70010-0',
  'https://doi.org/10.2183-6051.2024.67b62b984c5cd64deffbedf3',
  'https://doi.org/10.1037/1999-IPRS',
  'https://doi.org/10.1016/j.anyes.2014.01.002',
  'https://doi.org/10.1007/s10803-006-0055-9',
  'https://doi.org/10.1016/j.psychres.2018.116456',
  'https://doi.org/10.1111/j.1468-0148.2011.00746.x',
  'https://doi.org/10.1016/S0749-3797(02)00530-9',
  'https://doi.org/10.1186/s12873-024-01098-7',
  'https://doi.org/10.1007/s10803-011-0299-9',
  'https://doi.org/10.5281/cyrev.2024.525',
  'https://doi.org/10.18845/revmedhjca.v88.n80.147',
  'https://doi.org/10.1176/appi.ajp.2010.10050776',
  'https://doi.org/10.1093-psicologiaysalud.udenar.2024.QBLG',
  'https://doi.org/10.11144/rip.14.102',
  'https://doi.org/10.1016/S0022-3999(02)00000-0',
  'https://doi.org/10.1007/s10803-006-0056-9',
  'https://doi.org/10.1016/j.jcp.2020.03.005',
  'https://doi.org/10.1016/S0214-987X(03)70001-2',
  'https://doi.org/10.1002/9780470547038.ch12',
  'https://doi.org/10.1111/j.1600-0447.1998.tb10997.x',
  'https://doi.org/10.1016/0165-0327(88)90027-3',
  'https://doi.org/10.33999/rpsy.2021.9606717',
  'https://doi.org/10.1007/s10803-023-05892-x',
  'https://doi.org/10.31829/vertex.941.730',
  'https://doi.org/10.1176/appi.ajp.166.5.589',
  'https://doi.org/10.1007/s41234-025-00001-x',
  'https://doi.org/10.18273/revmeduis.v32n2-201916096',
  'https://doi.org/10.1016/S0887-618X(02)00129-5',
  'https://doi.org/10.1688-4221.2024.0001.01212',
  'https://doi.org/10.4067/s0718-50652007000300080',
  'https://doi.org/10.1037/1072-524X.1.1.1',
  'https://doi.org/10.1080/14650120500185332',
  'https://doi.org/10.1111/j.2044-8341.1959.tb00907.x',
  'https://doi.org/10.1002/jclp.4990530405',
  'https://doi.org/10.13140/RG.2.2.39472.1',
  'https://doi.org/10.1093/sleep/17.2.123',
  'https://doi.org/10.1016/j.jvb.2016.03.005',
  'https://doi.org/10.1080/13651502.2020.1756342',
  'https://doi.org/10.1097/0146-8244-42-9-1076',
];

function escapeRegex(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function anchorRegex(href) {
  return new RegExp(
    `<a\\s+[^>]*href="${escapeRegex(href)}"[^>]*>([\\s\\S]*?)<\\/a>`,
    'g',
  );
}

function replaceHrefWithNofollow(html, brokenHref, newHref) {
  const re = anchorRegex(brokenHref);
  return html.replace(re, (_match, inner) => {
    return `<a href="${newHref}" target="_blank" rel="nofollow noopener noreferrer">${inner}</a>`;
  });
}

function addNofollow(html, href) {
  const re = anchorRegex(href);
  return html.replace(re, (match) => {
    if (/\bnofollow\b/.test(match)) return match;
    if (/rel="([^"]*)"/.test(match)) {
      return match.replace(/rel="([^"]*)"/, (_m, rel) => {
        const parts = rel.split(/\s+/).filter(Boolean);
        if (!parts.includes('nofollow')) parts.unshift('nofollow');
        return `rel="${parts.join(' ')}"`;
      });
    }
    return match.replace(/<a\s+/, '<a rel="nofollow" ');
  });
}

function stripAnchor(html, href) {
  const re = anchorRegex(href);
  return html.replace(re, (_match, inner) => inner);
}

const stats = { rule1: 0, rule2: 0, rule3: 0, files: 0 };

for (const file of fs.readdirSync(ARTICULOS_DIR).filter((f) => f.endsWith('.html') && f !== 'index.html')) {
  const filePath = path.join(ARTICULOS_DIR, file);
  let html = fs.readFileSync(filePath, 'utf8');
  const original = html;

  for (const [targetFile, broken, replacement] of RULE1) {
    if (file !== targetFile) continue;
    const before = html;
    html = replaceHrefWithNofollow(html, broken, replacement);
    const count = (before.match(anchorRegex(broken)) || []).length;
    if (count > 0) stats.rule1 += count;
  }

  for (const url of RULE2_URLS) {
    const before = html;
    html = addNofollow(html, url);
    const count = (before.match(anchorRegex(url)) || []).length;
    if (count > 0) stats.rule2 += count;
  }

  for (const doi of RULE3_DOIS) {
    const before = html;
    html = stripAnchor(html, doi);
    const count = (before.match(anchorRegex(doi)) || []).length;
    if (count > 0) stats.rule3 += count;
  }

  if (html !== original) {
    fs.writeFileSync(filePath, html, 'utf8');
    stats.files += 1;
  }
}

console.log(`Modified ${stats.files} files`);
console.log(`Rule 1 replacements: ${stats.rule1}`);
console.log(`Rule 2 nofollow added: ${stats.rule2}`);
console.log(`Rule 3 stripped links: ${stats.rule3}`);
