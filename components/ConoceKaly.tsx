"use client";

import { Fragment, useCallback, useEffect, useRef, useState } from "react";
import { Mic } from "lucide-react";
import {
  kalyCategories,
  kalyVideos,
  posterSrc,
  videoSrc,
  type KalyVideo,
} from "@/lib/kaly-videos";

const reducedMotionQuery = "(prefers-reduced-motion: reduce)";

function PhoneVideo({
  video,
  size = "card",
  onOpenLightbox,
}: {
  video: KalyVideo;
  size?: "card" | "lightbox";
  onOpenLightbox?: (v: KalyVideo) => void;
}) {
  const wrapRef = useRef<HTMLDivElement>(null);
  const videoRef = useRef<HTMLVideoElement>(null);
  const [playing, setPlaying] = useState(false);
  const [reducedMotion, setReducedMotion] = useState(false);
  const showCover = size === "card";

  useEffect(() => {
    const mq = window.matchMedia(reducedMotionQuery);
    setReducedMotion(mq.matches);
    const fn = () => setReducedMotion(mq.matches);
    mq.addEventListener("change", fn);
    return () => mq.removeEventListener("change", fn);
  }, []);

  const useAutoplay = video.loop && !reducedMotion;

  const loadSrc = useCallback(() => {
    const el = videoRef.current;
    if (el && !el.src) el.src = videoSrc(video.slug);
  }, [video.slug]);

  useEffect(() => {
    const v = videoRef.current;
    if (!v || useAutoplay) return;
    const sync = () => setPlaying(!v.paused && !v.ended);
    sync();
    v.addEventListener("play", sync);
    v.addEventListener("pause", sync);
    v.addEventListener("ended", sync);
    return () => {
      v.removeEventListener("play", sync);
      v.removeEventListener("pause", sync);
      v.removeEventListener("ended", sync);
    };
  }, [useAutoplay]);

  useEffect(() => {
    if (!useAutoplay || !wrapRef.current) return;
    const el = wrapRef.current;
    const obs = new IntersectionObserver(
      ([entry]) => {
        const v = videoRef.current;
        if (!v) return;
        if (entry.isIntersecting) {
          loadSrc();
          v.play().catch(() => {});
        } else {
          v.pause();
        }
      },
      { rootMargin: "80px", threshold: 0.35 }
    );
    obs.observe(el);
    return () => obs.disconnect();
  }, [useAutoplay, loadSrc]);

  const playManual = () => {
    loadSrc();
    const v = videoRef.current;
    if (!v) return;
    v.controls = true;
    v.muted = false;
    setPlaying(true);
    v.play().catch(() => {});
  };

  const handleWrapClick = () => {
    const v = videoRef.current;
    if (useAutoplay) {
      onOpenLightbox?.(video);
      return;
    }
    if (!v?.src || v.paused) playManual();
    else onOpenLightbox?.(video);
  };

  return (
    <div
      ref={wrapRef}
      className={`kaly-phone-wrap${size === "lightbox" ? " kaly-phone-wrap--lightbox" : ""}`}
      onClick={handleWrapClick}
      role="presentation"
    >
      <div className="kaly-phone">
        <div className="kaly-phone-bezel">
          <div className="kaly-phone-notch" />
          <div className="kaly-phone-screen">
            <video
              ref={videoRef}
              preload="none"
              playsInline
              poster={posterSrc(video.slug)}
              aria-label={video.command}
              muted={video.loop}
              loop={video.loop}
            />
            {showCover && (
              <div className="kaly-video-cover" aria-hidden>
                <div className="kaly-cover-inner">
                  <Mic className="kaly-cmd-icon" size={20} strokeWidth={2} aria-hidden />
                  <p className="kaly-cover-command">{video.command}</p>
                </div>
              </div>
            )}
            {!useAutoplay && !playing && (
              <button
                type="button"
                className="kaly-play-btn"
                aria-label={`Reproducir: ${video.command}`}
                onClick={(e) => {
                  e.stopPropagation();
                  playManual();
                }}
              >
                <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden>
                  <path d="M8 5v14l11-7z" />
                </svg>
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default function ConoceKaly() {
  const [lightbox, setLightbox] = useState<KalyVideo | null>(null);

  return (
    <section className="section-conoce-kaly" id="conoce-kaly">
      <div style={{ maxWidth: 1100, margin: "0 auto" }}>
        <div className="conoce-kaly-header">
          <div className="section-label">Asistente por voz</div>
          <h2 className="section-headline">Conoce a Kaly</h2>
          <p className="section-sub">Tu asistente clínico por voz. Háblale, y Kalyo lo hace.</p>
          <span className="kaly-plan-badge">Incluido en el plan Max</span>
        </div>

        <div className="kaly-intro">
          <h3>Tu asistente en consulta</h3>
          <p>
            Kaly escucha tus comandos y ejecuta tareas en Kalyo: agenda, expedientes y notas,
            sin dejar de atender. Todo por voz, sin tocar la pantalla.
          </p>
          <p className="kaly-intro-voces">6 voces de México, Colombia, España y Argentina.</p>
          <ul>
            <li>Agendar, reagendar y consultar tu agenda</li>
            <li>Documentar sesiones, asignar pruebas y enviar material al paciente</li>
            <li>Consultar expedientes y resúmenes clínicos</li>
          </ul>
        </div>

        <div id="kaly-demos">
          <div className="kaly-grid" aria-label="Demos de comandos de voz con Kaly">
            {kalyCategories.map((cat, index) => (
              <Fragment key={cat.id}>
                <h3
                  className={`kaly-category-title${index === 0 ? " kaly-category-title--first" : ""}`}
                  id={`kaly-cat-${cat.id}`}
                >
                  {cat.label}
                </h3>
                {kalyVideos
                  .filter((v) => v.category === cat.id)
                  .map((item) => (
                    <article key={item.slug} className="kaly-grid-card">
                      <span className="kaly-card-category">{cat.label}</span>
                      <PhoneVideo video={item} onOpenLightbox={setLightbox} />
                    </article>
                  ))}
              </Fragment>
            ))}
          </div>
        </div>
      </div>

      {lightbox && (
        <div className="kaly-lightbox is-open" role="presentation">
          <div className="kaly-lightbox-backdrop" onClick={() => setLightbox(null)} />
          <div
            className="kaly-lightbox-dialog"
            role="dialog"
            aria-modal
            aria-label="Demo de Kaly"
          >
            <button
              type="button"
              className="kaly-lightbox-close"
              aria-label="Cerrar"
              onClick={() => setLightbox(null)}
            >
              &times;
            </button>
            <PhoneVideo video={lightbox} size="lightbox" />
            <p className="kaly-lightbox-cmd">{lightbox.command}</p>
          </div>
        </div>
      )}
    </section>
  );
}
