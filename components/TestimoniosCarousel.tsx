import { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import { AnimatePresence, motion } from "framer-motion";

type Avatar =
  | { type: "photo"; src: string; alt: string }
  | { type: "initials"; initials: string };

type Testimonial = {
  id: string;
  avatar: Avatar;
  quote: string;
  author: string;
  authorHref?: string;
  role?: string;
  location: string;
};

const TESTIMONIALS: Testimonial[] = [
  {
    id: "rosa",
    avatar: {
      type: "photo",
      src: "assets/images/testimonios/rosa-isela-salazar.webp",
      alt: "Rosa Isela Salazar, psicóloga e hipnoterapeuta clínica",
    },
    quote:
      "Kalyo me ayuda a eficientizar la aplicación y evaluación psicométrica de mis pacientes.",
    author: "Rosa Isela Salazar",
    authorHref: "https://www.verticebienestar.mx/",
    role: "Fundadora · Psicóloga e Hipnoterapeuta Clínica",
    location: "Monterrey, México",
  },
  {
    id: "carlos",
    avatar: { type: "initials", initials: "CM" },
    quote:
      "Kaly me agenda citas por voz y la confirmación por WhatsApp bajó mis inasistencias. Los tests digitales son un plus.",
    author: "Ps. Carlos Mendoza",
    location: "Bogotá",
  },
  {
    id: "monica",
    avatar: {
      type: "photo",
      src: "assets/images/testimonios/monica-paez.webp",
      alt: "Mónica Páez, psicóloga cognitivo-conductual",
    },
    quote:
      "Los instrumentos de evaluación han reducido significativamente el tiempo dedicado a las valoraciones. Además, la transcripción automática de las sesiones me permite estar plenamente presente con el paciente, sin distraerme tomando notas",
    author: "Mónica Páez",
    authorHref: "https://psicognitual.com/",
    role: "Psicóloga Cognitivo-Conductual",
    location: "Mexicali, México",
  },
];

function AvatarEl({ avatar }: { avatar: Avatar }) {
  if (avatar.type === "photo") {
    return (
      <img
        className="testimonio-avatar testimonio-avatar--photo"
        src={avatar.src}
        alt={avatar.alt}
        width={56}
        height={56}
        loading="lazy"
      />
    );
  }
  return <div className="testimonio-avatar">{avatar.initials}</div>;
}

function TestimonialCard({
  item,
  isCenter,
}: {
  item: Testimonial;
  isCenter: boolean;
}) {
  return (
    <motion.article
      className={`testimonio-card${isCenter ? " testimonio-card--center" : " testimonio-card--side"}`}
      layout
      animate={{
        scale: isCenter ? 1 : 0.94,
        opacity: isCenter ? 1 : 0.72,
      }}
      transition={{ duration: 0.45, ease: [0.4, 0, 0.2, 1] }}
    >
      <AvatarEl avatar={item.avatar} />
      <div className="testimonio-stars" aria-hidden="true">
        ★★★★★
      </div>
      <p className="testimonio-text">&ldquo;{item.quote}&rdquo;</p>
      <div className="testimonio-author">
        {item.authorHref ? (
          <a href={item.authorHref} target="_blank" rel="noopener noreferrer">
            {item.author}
          </a>
        ) : (
          item.author
        )}
      </div>
      {item.role && <div className="testimonio-role">{item.role}</div>}
      <div className="testimonio-location">{item.location}</div>
    </motion.article>
  );
}

function TestimoniosCarousel() {
  const [active, setActive] = useState(0);
  const [paused, setPaused] = useState(false);
  const [isMobile, setIsMobile] = useState(
    () => typeof window !== "undefined" && window.matchMedia("(max-width: 960px)").matches
  );

  useEffect(() => {
    const mq = window.matchMedia("(max-width: 960px)");
    const sync = () => setIsMobile(mq.matches);
    sync();
    mq.addEventListener("change", sync);
    return () => mq.removeEventListener("change", sync);
  }, []);

  useEffect(() => {
    if (paused) return;
    const timer = window.setInterval(
      () => setActive((i) => (i + 1) % TESTIMONIALS.length),
      4000
    );
    return () => window.clearInterval(timer);
  }, [paused]);

  const n = TESTIMONIALS.length;
  const slots = isMobile
    ? [{ index: active, position: "center" as const }]
    : [
        { index: (active - 1 + n) % n, position: "left" as const },
        { index: active, position: "center" as const },
        { index: (active + 1) % n, position: "right" as const },
      ];

  return (
    <div
      className="testimonios-carousel"
      onMouseEnter={() => setPaused(true)}
      onMouseLeave={() => setPaused(false)}
      onFocus={() => setPaused(true)}
      onBlur={(e) => {
        if (!e.currentTarget.contains(e.relatedTarget as Node | null)) {
          setPaused(false);
        }
      }}
    >
      <div
        className={`testimonios-track${isMobile ? " testimonios-track--mobile" : ""}`}
        aria-live="polite"
        aria-atomic="true"
      >
        <AnimatePresence mode="popLayout" initial={false}>
          {slots.map(({ index, position }) => (
            <motion.div
              key={`${position}-${index}`}
              className={`testimonios-slide testimonios-slide--${position}`}
              initial={{
                opacity: 0,
                x: isMobile ? 40 : position === "left" ? -24 : position === "right" ? 24 : 0,
              }}
              animate={{ opacity: 1, x: 0 }}
              exit={{
                opacity: 0,
                x: isMobile ? -40 : position === "left" ? -24 : position === "right" ? 24 : 0,
              }}
              transition={{ duration: 0.45, ease: [0.4, 0, 0.2, 1] }}
            >
              <TestimonialCard
                item={TESTIMONIALS[index]}
                isCenter={position === "center"}
              />
            </motion.div>
          ))}
        </AnimatePresence>
      </div>

      <div
        className="testimonios-dots"
        role="tablist"
        aria-label="Navegación de testimonios"
      >
        {TESTIMONIALS.map((item, i) => (
          <button
            key={item.id}
            type="button"
            role="tab"
            className={`testimonios-dot${i === active ? " is-active" : ""}`}
            aria-selected={i === active}
            aria-label={`Testimonio ${i + 1}: ${item.author}`}
            onClick={() => setActive(i)}
          />
        ))}
      </div>
    </div>
  );
}

const rootEl = document.getElementById("testimonios-carousel-root");
if (rootEl) {
  createRoot(rootEl).render(<TestimoniosCarousel />);
}
