import { kalyCategories, kalyVideos, videoSrc, posterSrc } from '../lib/kaly-videos.js';

const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function micIcon() {
  return `<svg class="kaly-cmd-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/></svg>`;
}

function playIcon() {
  return `<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>`;
}

function coverMarkup(command) {
  return `
    <div class="kaly-video-cover" aria-hidden="true">
      <div class="kaly-cover-inner">
        ${micIcon()}
        <p class="kaly-cover-command">${command}</p>
      </div>
    </div>
  `;
}

function wirePlayButton(screen, video) {
  const btn = screen.querySelector('.kaly-play-btn');
  if (!btn) return;
  const sync = () => {
    btn.hidden = !video.paused && !video.ended;
  };
  video.addEventListener('play', sync);
  video.addEventListener('pause', sync);
  video.addEventListener('ended', sync);
}

function createPhoneVideo({ slug, command, loop, showCover = true }) {
  const wrap = document.createElement('div');
  wrap.className = 'kaly-phone-wrap';
  wrap.dataset.slug = slug;
  wrap.dataset.command = command;

  const useAutoplay = loop && !reducedMotion;
  const phone = document.createElement('div');
  phone.className = 'kaly-phone';
  phone.innerHTML = `
    <div class="kaly-phone-bezel">
      <div class="kaly-phone-notch"></div>
      <div class="kaly-phone-screen">
        <video
          preload="none"
          playsinline
          poster="${posterSrc(slug)}"
          aria-label="${command.replace(/"/g, '&quot;')}"
        ></video>
        ${showCover ? coverMarkup(command) : ''}
        <button type="button" class="kaly-play-btn" ${useAutoplay ? 'hidden' : ''} aria-label="Reproducir: ${command.replace(/"/g, '&quot;')}">${playIcon()}</button>
      </div>
    </div>
  `;

  const video = phone.querySelector('video');
  const screen = phone.querySelector('.kaly-phone-screen');
  video.dataset.src = videoSrc(slug);
  if (loop) {
    video.muted = true;
    video.loop = true;
  }
  if (showCover && screen && !useAutoplay) wirePlayButton(screen, video);

  wrap.appendChild(phone);
  wireVideoBehavior(wrap, { loop, useAutoplay });
  return wrap;
}

function loadVideoSrc(video) {
  if (!video.src && video.dataset.src) video.src = video.dataset.src;
}

function wireVideoBehavior(wrap, { loop, useAutoplay }) {
  const video = wrap.querySelector('video');
  const btn = wrap.querySelector('.kaly-play-btn');
  const command = wrap.dataset.command;

  const openLb = () => openLightbox(wrap.dataset.slug, command);

  if (useAutoplay) {
    loopObserver.observe(wrap);
    wrap.addEventListener('click', openLb);
    return;
  }

  const startPlayback = () => {
    loadVideoSrc(video);
    video.controls = true;
    video.muted = false;
    if (btn) btn.hidden = true;
    video.play().catch(() => {});
  };

  if (btn) {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      startPlayback();
    });
  }

  wrap.addEventListener('click', () => {
    if (!video.src || video.paused) startPlayback();
    else openLb();
  });
}

const loopObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      const wrap = entry.target;
      const video = wrap.querySelector('video');
      if (!video) return;
      if (entry.isIntersecting) {
        loadVideoSrc(video);
        video.play().catch(() => {});
      } else {
        video.pause();
      }
    });
  },
  { rootMargin: '80px', threshold: 0.35 }
);

let lightboxEl = null;

function openLightbox(slug, label) {
  const meta = kalyVideos.find((v) => v.slug === slug);
  if (!meta) return;

  if (!lightboxEl) {
    lightboxEl = document.createElement('div');
    lightboxEl.className = 'kaly-lightbox';
    lightboxEl.innerHTML = `
      <div class="kaly-lightbox-backdrop" data-close></div>
      <div class="kaly-lightbox-dialog" role="dialog" aria-modal="true" aria-label="Demo de Kaly">
        <button type="button" class="kaly-lightbox-close" aria-label="Cerrar">&times;</button>
        <div class="kaly-lightbox-phone"></div>
        <p class="kaly-lightbox-cmd"></p>
      </div>
    `;
    document.body.appendChild(lightboxEl);
    lightboxEl.querySelector('[data-close]').addEventListener('click', closeLightbox);
    lightboxEl.querySelector('.kaly-lightbox-close').addEventListener('click', closeLightbox);
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && lightboxEl?.classList.contains('is-open')) closeLightbox();
    });
  }

  document.querySelectorAll('.kaly-phone-wrap[data-autoplay]').forEach((w) => {
    w.querySelector('video')?.pause();
  });

  const phoneHost = lightboxEl.querySelector('.kaly-lightbox-phone');
  const cmdEl = lightboxEl.querySelector('.kaly-lightbox-cmd');
  phoneHost.innerHTML = '';

  const lbWrap = document.createElement('div');
  lbWrap.className = 'kaly-phone-wrap kaly-phone-wrap--lightbox';
  lbWrap.innerHTML = `
    <div class="kaly-phone">
      <div class="kaly-phone-bezel">
        <div class="kaly-phone-notch"></div>
        <div class="kaly-phone-screen">
          <video preload="none" playsinline poster="${posterSrc(slug)}" aria-label="${(label || meta.command).replace(/"/g, '&quot;')}"></video>
        </div>
      </div>
    </div>
  `;
  phoneHost.appendChild(lbWrap);
  cmdEl.textContent = label || meta.command;

  const lbVideo = lbWrap.querySelector('video');
  lbVideo.src = videoSrc(slug);
  lbVideo.controls = true;
  lbVideo.muted = false;
  lbVideo.play().catch(() => {});

  lightboxEl.classList.add('is-open');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  if (!lightboxEl) return;
  const v = lightboxEl.querySelector('video');
  if (v) {
    v.pause();
    v.removeAttribute('src');
    v.load();
  }
  lightboxEl.classList.remove('is-open');
  document.body.style.overflow = '';
  document.querySelectorAll('#kaly-demos .kaly-phone-wrap[data-autoplay]').forEach((wrap) => {
    loopObserver.observe(wrap);
  });
}

function categoryLabel(categoryId) {
  return kalyCategories.find((c) => c.id === categoryId)?.label ?? '';
}

function createCard(item) {
  const card = document.createElement('article');
  card.className = 'kaly-grid-card';
  card.innerHTML = `<span class="kaly-card-category">${categoryLabel(item.category)}</span>`;
  const wrap = createPhoneVideo(item);
  if (item.loop && !reducedMotion) wrap.dataset.autoplay = 'true';
  card.appendChild(wrap);
  return card;
}

function renderDemos() {
  const host = document.getElementById('kaly-demos');
  if (!host) return;
  host.innerHTML = '';

  const grid = document.createElement('div');
  grid.className = 'kaly-grid';
  grid.setAttribute('aria-label', 'Demos de comandos de voz con Kaly');

  kalyCategories.forEach((cat) => {
    kalyVideos.filter((v) => v.category === cat.id).forEach((item) => {
      grid.appendChild(createCard(item));
    });
  });

  host.appendChild(grid);
}

function init() {
  renderDemos();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
