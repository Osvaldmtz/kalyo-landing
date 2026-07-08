const imgMap = {
  ss1: { webp: 'assets/dashboard.webp', jpg: 'assets/dashboard.jpg' },
  ss2: { webp: 'assets/evaluaciones.webp', jpg: 'assets/evaluaciones.jpg' },
  ss3: { webp: 'assets/tendencia.webp', jpg: 'assets/tendencia.jpg' },
  ss4: { webp: 'assets/hero-tablet.webp', jpg: 'assets/hero-tablet.jpg' },
};
const featureItems = document.querySelectorAll('.feature-item');
const featureImg = document.getElementById('featureImg');
const featureSource = document.getElementById('featureSource');
featureItems.forEach(item => {
  item.addEventListener('click', () => {
    featureItems.forEach(el => el.classList.remove('active'));
    item.classList.add('active');
    featureImg.style.opacity='0';
    setTimeout(() => {
      const img = imgMap[item.getAttribute('data-img')];
      if (featureSource) featureSource.srcset = img.webp;
      featureImg.src = img.jpg;
      featureImg.style.opacity='1';
    }, 200);
  });
});
let idx=0;
setInterval(() => { idx=(idx+1)%featureItems.length; featureItems[idx].click(); }, 4000);

const obs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if(e.isIntersecting) {
      e.target.style.opacity = '1';
      e.target.style.transform = 'translateY(0)';
      obs.unobserve(e.target);
    }
  });
}, { threshold: 0.1 });
document.querySelectorAll('.problema-card, .paso, .screenshot-card, .precio-card').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(28px)';
  el.style.transition = 'opacity .6s ease, transform .6s ease';
  obs.observe(el);
});

const h=document.getElementById('hamburger');
const n=document.getElementById('main-nav');
const c=document.querySelector('.hctas');
h.addEventListener('click',()=>{
  n.classList.toggle('open');
  c.classList.toggle('open');
});

(function(){
  const params = new URLSearchParams(window.location.search);
  const utmKeys = ['utm_source','utm_medium','utm_campaign','utm_content','utm_term','fbclid'];
  const utmData = {};
  utmKeys.forEach(k => { if(params.get(k)) utmData[k] = params.get(k); });
  if(Object.keys(utmData).length === 0) return;

  // Store UTMs in sessionStorage for persistence across page interactions
  sessionStorage.setItem('kalyo_utm', JSON.stringify(utmData));

  function appendUtms(href){
    try {
      const url = new URL(href);
      Object.entries(utmData).forEach(([k,v]) => url.searchParams.set(k,v));
      return url.toString();
    } catch(e){ return href; }
  }

  // Append UTMs to outbound app links
  document.querySelectorAll('a[href*="app.kalyo.io"]').forEach(a => {
    a.href = appendUtms(a.href);
  });
})();
