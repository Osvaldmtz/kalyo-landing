import { kalyCategories, kalyVideos, videoSrc, posterSrc } from '../lib/kaly-videos.js';

const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function micIcon() {
  return `<svg class="kaly-cmd-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/></svg>`;
}

function playIcon() {
  return `<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>`;
}

function createPhoneVideo({ slug, command, loop, size = 'card' }) {
  const wrap = document.createElement('div');
  wrap.className = `kaly-phone-wrap kaly-phone-wrap--${size}`;
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
        <button type="button" class="kaly-play-btn" ${useAutoplay ? 'hidden' : ''} aria-label="Reproducir: ${command.replace(/"/g, '&quot;')}">${playIcon()}</button>
      </div>
    </div>
  `;

  const video = phone.querySelector('video');
  video.dataset.src = videoSrc(slug);
  if (loop) {
    video.muted = true;
    video.loop = true;
  }

  wrap.appendChild(phone);
  if (size !== 'lightbox') wireVideoBehavior(wrap, { loop, useAutoplay });
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

  const startPlayback = (withSound = true) => {
    loadVideoSrc(video);
    if (withSound) {
      video.controls = true;
      video.muted = false;
    }
    if (btn) btn.hidden = true;
    video.play().catch(() => {});
  };

  if (btn) {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      startPlayback(true);
    });
  }

  wrap.addEventListener('click', () => {
    if (!video.src || video.paused) startPlayback(true);
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
  const lbWrap = createPhoneVideo({ ...meta, size: 'lightbox' });
  phoneHost.appendChild(lbWrap);
  cmdEl.textContent = label || meta.command;

  const lbVideo = lbWrap.querySelector('video');
  const lbBtn = lbWrap.querySelector('.kaly-play-btn');
  loadVideoSrc(lbVideo);
  lbVideo.controls = true;
  lbVideo.muted = false;
  if (lbBtn) lbBtn.hidden = true;
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
  document.querySelectorAll('.kaly-phone-wrap').forEach((wrap) => {
    const video = wrap.querySelector('video');
    if (video?.loop && !reducedMotion && wrap.closest('#kaly-grid')) {
      loopObserver.observe(wrap);
    }
  });
}

function buildHero(featured) {
  const host = document.getElementById('kaly-hero-phone');
  if (!host) return;
  host.innerHTML = '';
  host.appendChild(createPhoneVideo({ ...featured, size: 'hero' }));
}

function buildTabs(activeId) {
  const tablist = document.getElementById('kaly-tabs');
  if (!tablist) return;
  tablist.innerHTML = '';
  tablist.setAttribute('role', 'tablist');
  tablist.setAttribute('aria-label', 'Categorías de demos de Kaly');

  kalyCategories.forEach((cat, i) => {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'kaly-tab' + (cat.id === activeId ? ' is-active' : '');
    btn.setAttribute('role', 'tab');
    btn.id = `kaly-tab-${cat.id}`;
    btn.setAttribute('aria-selected', cat.id === activeId ? 'true' : 'false');
    btn.setAttribute('aria-controls', `kaly-panel-${cat.id}`);
    btn.tabIndex = cat.id === activeId ? 0 : -1;
    btn.textContent = cat.label;
    btn.addEventListener('click', () => selectTab(cat.id));
    btn.addEventListener('keydown', (e) => onTabKeydown(e, i));
    tablist.appendChild(btn);
  });
}

function onTabKeydown(e, index) {
  const tabs = [...document.querySelectorAll('.kaly-tab')];
  let next = index;
  if (e.key === 'ArrowRight') next = (index + 1) % tabs.length;
  else if (e.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
  else if (e.key === 'Home') next = 0;
  else if (e.key === 'End') next = tabs.length - 1;
  else return;
  e.preventDefault();
  tabs[next].click();
  tabs[next].focus();
}

function selectTab(categoryId) {
  buildTabs(categoryId);
  renderGrid(categoryId);
}

function renderGrid(categoryId) {
  const grid = document.getElementById('kaly-grid');
  const panel = document.getElementById('kaly-grid-panel');
  if (!grid || !panel) return;

  panel.id = `kaly-panel-${categoryId}`;
  panel.setAttribute('role', 'tabpanel');
  panel.setAttribute('aria-labelledby', `kaly-tab-${categoryId}`);

  grid.innerHTML = '';
  kalyVideos
    .filter((v) => !v.featured && v.category === categoryId)
    .forEach((item) => {
      const card = document.createElement('article');
      card.className = 'kaly-grid-card';
      card.innerHTML = `<div class="kaly-cmd-bubble">${micIcon()}<span>${item.command}</span></div>`;
      const wrap = createPhoneVideo(item);
      if (item.loop && !reducedMotion) wrap.dataset.autoplay = 'true';
      card.appendChild(wrap);
      grid.appendChild(card);
    });
}

function init() {
  const featured = kalyVideos.find((v) => v.featured);
  if (featured) buildHero(featured);
  selectTab(kalyCategories[0].id);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
