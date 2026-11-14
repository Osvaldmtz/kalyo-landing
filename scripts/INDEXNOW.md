# IndexNow (Bing) — kalyo-landing

Notifica a Bing (y motores compatibles con IndexNow) cuando se publican o actualizan URLs en [kalyo.io](https://kalyo.io).

## API key

| Campo | Valor |
|-------|--------|
| **Key** | `bf63cc655f454739808db18cfbb65d70` |
| **Archivo de verificación** | `/bf63cc655f454739808db18cfbb65d70.txt` (raíz del sitio) |
| **URL pública** | https://kalyo.io/bf63cc655f454739808db18cfbb65d70.txt |
| **Host** | `kalyo.io` |
| **Endpoint** | `https://api.indexnow.org/indexnow` |

La key es pública por diseño (el archivo `.txt` debe ser accesible en la raíz). No la trates como secreto de servidor; sí conviene no rotarla sin actualizar el archivo desplegado.

## Uso

```bash
# Ping de URLs sueltas
./scripts/indexnow-ping.sh \
  https://kalyo.io/articulos/phq-9-escala-depresion.html \
  https://kalyo.io/articulos/gad-7-escala-ansiedad-generalizada.html

# Desde un archivo (una URL por línea)
./scripts/indexnow-ping.sh --file scripts/indexnow-article-urls.txt

# Todos los artículos en articulos/*.html (excepto index.html)
./scripts/indexnow-ping.sh --articles
```

Respuestas esperadas: `200` OK o `202` Accepted. `403` suele indicar que el `.txt` de verificación aún no está en producción.

## Regenerar lista de artículos

```bash
./scripts/indexnow-ping.sh --write-urls scripts/indexnow-article-urls.txt
```
