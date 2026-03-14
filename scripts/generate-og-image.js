const { createCanvas } = require('canvas');
const fs = require('fs');

const canvas = createCanvas(1200, 630);
const ctx = canvas.getContext('2d');

// Fondo degradado morado
const gradient = ctx.createLinearGradient(0, 0, 1200, 630);
gradient.addColorStop(0, '#7C3AED');
gradient.addColorStop(1, '#4C1D95');
ctx.fillStyle = gradient;
ctx.fillRect(0, 0, 1200, 630);

// Círculo decorativo
ctx.beginPath();
ctx.arc(1050, 100, 180, 0, Math.PI * 2);
ctx.fillStyle = 'rgba(167, 139, 250, 0.2)';
ctx.fill();

// Logo kalyo
ctx.fillStyle = '#FFFFFF';
ctx.font = 'bold 96px Arial';
ctx.fillText('kalyo', 80, 240);

// Punto decorativo sobre la o
ctx.beginPath();
ctx.arc(375, 155, 12, 0, Math.PI * 2);
ctx.fillStyle = '#C4B5FD';
ctx.fill();

// Tagline
ctx.fillStyle = '#DDD6FE';
ctx.font = '36px Arial';
ctx.fillText('Evaluación clínica inteligente para psicólogos', 80, 310);

// Stats
ctx.fillStyle = '#FFFFFF';
ctx.font = 'bold 28px Arial';
ctx.fillText('91 tests validados  ·  IA  ·  DSM-5-TR  ·  desde $29 USD/mes', 80, 420);

// URL
ctx.fillStyle = '#A78BFA';
ctx.font = '24px Arial';
ctx.fillText('kalyo.io', 80, 560);

// Guardar
const buffer = canvas.toBuffer('image/jpeg', { quality: 0.95 });
fs.writeFileSync('og-image.jpg', buffer);
console.log('og-image.jpg generado correctamente');
