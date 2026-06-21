import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import sharp from 'sharp';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const blogDir = path.join(__dirname, '..', 'assets', 'blog');

function kb(bytes) {
  return (bytes / 1024).toFixed(1);
}

const jpgFiles = fs.readdirSync(blogDir).filter((f) => f.endsWith('.jpg')).sort();

if (jpgFiles.length === 0) {
  console.error('No JPG files found in assets/blog/');
  process.exit(1);
}

console.log(`Optimizing ${jpgFiles.length} images...\n`);

let totalBefore = 0;
let totalJpgAfter = 0;
let totalWebpAfter = 0;

for (const file of jpgFiles) {
  const inputPath = path.join(blogDir, file);
  const base = file.replace(/\.jpg$/, '');
  const webpPath = path.join(blogDir, `${base}.webp`);

  const before = fs.statSync(inputPath).size;
  totalBefore += before;

  await sharp(inputPath)
    .jpeg({ quality: 75, mozjpeg: true })
    .toFile(inputPath + '.tmp');
  fs.renameSync(inputPath + '.tmp', inputPath);

  await sharp(inputPath)
    .webp({ quality: 82 })
    .toFile(webpPath);

  const jpgAfter = fs.statSync(inputPath).size;
  const webpAfter = fs.statSync(webpPath).size;
  totalJpgAfter += jpgAfter;
  totalWebpAfter += webpAfter;

  console.log(`${file}`);
  console.log(`  JPG:  ${kb(before)} KB → ${kb(jpgAfter)} KB`);
  console.log(`  WebP: ${kb(webpAfter)} KB (${base}.webp)\n`);
}

console.log('--- Totals ---');
console.log(`Original JPG:  ${kb(totalBefore)} KB`);
console.log(`Compressed JPG: ${kb(totalJpgAfter)} KB (${Math.round((1 - totalJpgAfter / totalBefore) * 100)}% smaller)`);
console.log(`WebP total:    ${kb(totalWebpAfter)} KB (${Math.round((1 - totalWebpAfter / totalBefore) * 100)}% vs original JPG)`);
