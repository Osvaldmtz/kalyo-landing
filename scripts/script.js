const imgMap = {
  ss1:`assets/dashboard.jpg`,ss2:`assets/evaluaciones.jpg`,ss3:`assets/tendencia.jpg`,ss4:`assets/hero-tablet.jpg`
};
const featureItems = document.querySelectorAll('.feature-item');
const featureImg = document.getElementById('featureImg');
featureItems.forEach(item => {
  item.addEventListener('click', () => {
    featureItems.forEach(el => el.classList.remove('active'));
    item.classList.add('active');
    featureImg.style.opacity='0';
    setTimeout(() => { featureImg.src=imgMap[item.getAttribute('data-img')]; featureImg.style.opacity='1'; }, 200);
  });
});
let idx=0;
setInterval(() => { idx=(idx+1)%featureItems.length; featureItems[idx].click(); }, 4000);

const obs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if(e.isIntersecting) {
      e.target.style.opacity

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

  // Append UTMs to all outbound links (app.kalyo.io and calendly)
  function appendUtms(href){
    try {
      const url = new URL(href);
      Object.entries(utmData).forEach(([k,v]) => url.searchParams.set(k,v));
      return url.toString();
    } catch(e){ return href; }
  }

  document.querySelectorAll('a[href*="app.kalyo.io"], a[href*="calendly.com"]').forEach(a => {
    a.href = appendUtms(a.href);
  });

  // Also append to Calendly iframe
  const calIframe = document.querySelector('.calendly-embed-wrap iframe');
  if(calIframe){
    calIframe.src = appendUtms(calIframe.src);
  }
})();
