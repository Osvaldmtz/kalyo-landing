/** Runtime mirror of kaly-videos.ts for static landing */
export const kalyCategories = [
  { id: "agenda", label: "Agenda y citas" },
  { id: "pacientes", label: "Pacientes y expedientes" },
  { id: "notas", label: "Notas y reportes" },
];

export const kalyVideos = [
  { slug: "cuantas-citas-tengo", command: "¿Cuántas citas tengo?", category: "agenda", loop: true },
  { slug: "cuantas-citas-tengo-hoy", command: "¿Cuántas citas tengo hoy?", category: "agenda", loop: true },
  { slug: "cual-es-mi-siguiente-cita", command: "¿Cuál es mi siguiente cita?", category: "agenda", loop: true },
  { slug: "agendamiento-de-citas", command: "Agenda una cita", category: "agenda", loop: true },
  { slug: "reagendamiento-de-citas", command: "Reagenda esta cita", category: "agenda", loop: false },
  { slug: "cancelacion-de-citas", command: "Cancela la cita", category: "agenda", loop: true },
  { slug: "abre-expediente", command: "Abre el expediente", category: "pacientes", loop: true },
  { slug: "cuantos-pacientes-activos", command: "¿Cuántos pacientes activos tengo?", category: "pacientes", loop: true },
  { slug: "recordatorio-sesion-anterior", command: "Recuérdame la sesión anterior", category: "pacientes", loop: false },
  { slug: "haz-notas-clinicas", command: "Haz las notas clínicas", category: "notas", loop: true },
  { slug: "enviar-tests-whatsapp", command: "Envía los tests por WhatsApp", category: "notas", loop: false },
  { slug: "resumen-proceso-paciente", command: "Resume el proceso del paciente", category: "notas", loop: false, featured: true },
];

export function videoSrc(slug) {
  return `videos/kaly/${slug}.mp4`;
}

export function posterSrc(slug) {
  return `videos/kaly/posters/${slug}.jpg`;
}
