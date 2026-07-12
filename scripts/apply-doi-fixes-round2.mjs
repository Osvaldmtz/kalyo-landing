import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ARTICULOS_DIR = path.join(__dirname, '..', 'articulos');
const REL = 'nofollow noopener noreferrer';

const RULE1 = [
  ['audit-test-alcoholismo.html', 'https://adicciones.es/index.php/adicciones/article/download/613/602/1170', 'https://www.adicciones.es/index.php/adicciones/article/view/613'],
  ['assist-evaluacion-sustancias-oms.html', 'https://adicciones.es/index.php/adicciones/article/download/1496/1232/5103', 'https://adicciones.es/index.php/adicciones/article/view/1496'],
  ['asrs-tdah-adultos.html', 'https://www.adicciones.es/index.php/adicciones/article/download/298/298/577', 'https://www.adicciones.es/index.php/adicciones/article/view/298'],
  ['raads-r-autismo-adultos.html', 'https://novopsych.com/es-us/evaluaciones/diagnostico/escala-diagnostica-del-espectro-autista-de-ritvo-revisada-raads-r/', 'https://pubmed.ncbi.nlm.nih.gov/21086033/'],
  ['consentimiento-informado-psicologia.html', 'https://www.colpsic.org.co/wp-content/uploads/2020/12/Doctrina-No.-3-CONSENTIMIENTO-INFORMADO-dic-5-2018.pdf', 'https://eticapsicologica.org/index.php/documentos/lineamientos/item/44-doctrina-no-03-consentimiento-informado-en-el-ejercicio-de-la-psicologia-en-colombia'],
  ['audit-c-tamizaje-alcohol-breve.html', 'https://www.adicciones.es/index.php/adicciones/article/viewFile/775/730', 'https://www.adicciones.es/index.php/adicciones/article/viewFile/775/730'],
];

const RULE2 = [
  ['ley-1090-psicologia-colombia.html', 'https://www.colpsic.org.co/normatividad/'],
  ['test-reloj-dibujo-cognicion.html', 'https://revecuatneurol.com/'],
];

const RULE3 = [
  ['pass-sensibilidad-ansiedad.html', 'https://doi.org/10.1007/s00737-015-0498-9'],
  ['test-beck-ansiedad-bai.html', 'https://doi.org/10.1016/j.acp.2020.01.001'],
  ['tests-psicologicos-digitales.html', 'https://doi.org/10.1016/j.rpe.2019.02.004'],
  ['faces-iv-escala-adaptabilidad-familiar.html', 'https://doi.org/10.1016/j.salm.2015.03.002'],
  ['mdq-trastorno-bipolar-tamizaje.html', 'https://doi.org/10.1016/S0301-0081(05)70012-3'],
  ['ecr-cuestionario-apego-adultos.html', 'https://doi.org/10.4067/s0718-50652020000300080'],
  ['core-om-medida-resultados-clinicos.html', 'https://doi.org/10.1016/j.revaluar.2024.05.003'],
  ['oq-45-resultados-terapia.html', 'https://doi.org/10.1080/08039481.2012.679150'],
  ['scared-ansiedad-infantil.html', 'https://doi.org/10.5093/rpccna2011a6'],
  ['que-es-el-phq-9.html', 'https://investigacion.upb.edu.co/es/publications/construct-validity-of-the-phq-9-in-university-students-in-colombi/'],
  ['ley-1581-proteccion-datos-psicologia.html', 'https://www.sic.gov.co/resoluciones/2797-2013'],
  ['adhd-rs-5-tdah-ninos.html', 'https://www.sciencedirect.com/science/article/pii/S0213485317302244'],
  ['ftnd-test-nicotina-dependencia.html', 'https://revistasdigitales.uniboyaca.edu.co/index.php/rs/article/download/185/200/527'],
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

function countMatches(html, href) {
  return (html.match(anchorRegex(href)) || []).length;
}

function replaceHrefWithRel(html, brokenHref, newHref) {
  const re = anchorRegex(brokenHref);
  return html.replace(re, (_match, inner) => {
    return `<a href="${newHref}" target="_blank" rel="${REL}">${inner}</a>`;
  });
}

function ensureRel(html, href) {
  const re = anchorRegex(href);
  return html.replace(re, (match) => {
    if (match.includes(`rel="${REL}"`)) return match;
    if (/rel="([^"]*)"/.test(match)) {
      return match.replace(/rel="[^"]*"/, `rel="${REL}"`);
    }
    return match.replace(/<a\s+/, `<a rel="${REL}" `);
  });
}

function stripAnchor(html, href) {
  const re = anchorRegex(href);
  return html.replace(re, (_match, inner) => inner);
}

const stats = { rule1: 0, rule2: 0, rule3: 0, files: 0 };

for (const [file, broken, replacement] of RULE1) {
  const filePath = path.join(ARTICULOS_DIR, file);
  let html = fs.readFileSync(filePath, 'utf8');
  const before = html;
  const count = countMatches(html, broken);
  html = replaceHrefWithRel(html, broken, replacement);
  if (html !== before) {
    fs.writeFileSync(filePath, html, 'utf8');
    stats.rule1 += count;
    stats.files += 1;
    console.log(`Rule1 ${file}: ${count}`);
  }
}

for (const [file, href] of RULE2) {
  const filePath = path.join(ARTICULOS_DIR, file);
  let html = fs.readFileSync(filePath, 'utf8');
  const before = html;
  const count = countMatches(html, href);
  html = ensureRel(html, href);
  if (html !== before) {
    fs.writeFileSync(filePath, html, 'utf8');
    stats.rule2 += count;
    stats.files += 1;
    console.log(`Rule2 ${file}: ${count}`);
  }
}

for (const [file, href] of RULE3) {
  const filePath = path.join(ARTICULOS_DIR, file);
  let html = fs.readFileSync(filePath, 'utf8');
  const before = html;
  const count = countMatches(html, href);
  html = stripAnchor(html, href);
  if (html !== before) {
    fs.writeFileSync(filePath, html, 'utf8');
    stats.rule3 += count;
    stats.files += 1;
    console.log(`Rule3 ${file}: ${count}`);
  }
}

console.log(`\nRule 1: ${stats.rule1} | Rule 2: ${stats.rule2} | Rule 3: ${stats.rule3}`);
