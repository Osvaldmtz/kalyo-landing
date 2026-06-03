export type KalyCategory = "agenda" | "pacientes" | "notas";

export type KalyVideo = {
  slug: string;
  command: string;       // texto mostrado como "comando de voz"
  category: KalyCategory;
  loop: boolean;         // true para clips cortos (<=25s)
  featured?: boolean;
};

export const kalyCategories: { id: KalyCategory; label: string }[] = [
  { id: "agenda",    label: "Agenda y citas" },
  { id: "pacientes", label: "Pacientes y expedientes" },
  { id: "notas",     label: "Notas y reportes" },
];

export const kalyVideos: KalyVideo[] = [
  { slug: "cuantas-citas-tengo-programadas", command: "¿Cuántas citas tengo programadas?", category: "agenda",    loop: true },
  { slug: "cual-es-mi-siguiente-cita",       command: "¿Cuál es mi siguiente cita?",      category: "agenda",    loop: true },
  { slug: "agendamiento-de-citas",          command: "Agenda una cita",                  category: "agenda",    loop: false },
  { slug: "agendamiento-multiple-de-citas",  command: "Agenda varias citas",              category: "agenda",    loop: true },
  { slug: "reagendamiento-de-citas",        command: "Reagenda esta cita",               category: "agenda",    loop: false },
  { slug: "cancelacion-de-citas",           command: "Cancela la cita",                  category: "agenda",    loop: true },
  { slug: "abre-expediente",                command: "Abre el expediente",               category: "pacientes", loop: true },
  { slug: "cuantos-pacientes-activos",      command: "¿Cuántos pacientes activos tengo?", category: "pacientes", loop: true },
  { slug: "resumen-ultima-sesion",          command: "Resumen de la última sesión",      category: "pacientes", loop: false },
  { slug: "haz-notas-clinicas",             command: "Haz las notas clínicas",           category: "notas",     loop: false },
  { slug: "leer-ultimas-notas-paciente",    command: "Lee las últimas notas del paciente", category: "notas",   loop: false },
  { slug: "enviar-tests-whatsapp",          command: "Envía los tests por WhatsApp",     category: "notas",     loop: false },
  { slug: "resumen-proceso-paciente",       command: "Resume el proceso del paciente",   category: "notas",     loop: false, featured: true },
];

export function videoSrc(slug: string): string {
  return `videos/kaly/${slug}.mp4`;
}

export function posterSrc(slug: string): string {
  return `videos/kaly/posters/${slug}.jpg`;
}
