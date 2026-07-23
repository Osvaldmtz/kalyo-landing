# Content guidelines — kalyo.io artículos

## REGLA CONTENIDO: imágenes por artículo

Todo artículo nuevo debe tener:

- **1 imagen hero** (jpg + webp) en `/assets/blog/{slug}-hero.{jpg,webp}`
- **2 imágenes en el body** (jpg + webp) en `/assets/blog/{slug}-1.*` y `{slug}-2.*`
- **OG image específica** del artículo (normalmente el hero: `/assets/blog/{slug}-hero.jpg`)
- **Alt text descriptivo** con keyword principal
- **Formato responsive** con `<picture>` (webp + jpg fallback)

### Markup body (mínimo)

```html
<figure class="article-inline-img">
  <picture>
    <source srcset="/assets/blog/{slug}-1.webp" type="image/webp">
    <img src="/assets/blog/{slug}-1.jpg" alt="… keyword …" width="1200" height="675" loading="lazy">
  </picture>
</figure>
```

### Posición sugerida

1. Body image 1: después de la intro (`article-intro`)
2. Body image 2: mitad del artículo (antes de FAQ o conclusión)
3. Hero: arriba, `loading="eager"` + `fetchpriority="high"`

### Requisitos técnicos

- Width/height explícitos (evitar CLS)
- Body images: `loading="lazy"`
- No usar el `og-image` genérico del sitio como única imagen social del artículo
- Preferir assets propios o mockups de marca; evitar stock genérico sin contexto clínico/producto

### Checklist al publicar

- [ ] Hero jpg + webp
- [ ] Body `-1` y `-2` jpg + webp
- [ ] Alt con keyword en las 3 imágenes
- [ ] `og:image` / `twitter:image` → hero del artículo
- [ ] Entrada en `sitemap.xml`
- [ ] CTAs con UTM (`utm_campaign={slug}`)
