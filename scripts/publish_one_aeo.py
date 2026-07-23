import json, sys
from pathlib import Path
from scripts.render_aeo_article import render
from scripts.publish_aeo_helpers import verify, bump_counts, insert_card, insert_sitemap

slug = sys.argv[1]
spec = json.loads(Path(f"scripts/article-batch/specs/{slug}.json").read_text())
Path(f"articulos/{slug}.html").write_text(render(spec))
info = verify(slug)
print(json.dumps(info, ensure_ascii=False))
if f'href="/articulos/{slug}.html"' not in Path("articulos/index.html").read_text():
    card = f'''      <a href="/articulos/{slug}.html" class="blog-card">
        <span class="blog-card-tag">Gu&iacute;a cl&iacute;nica</span>
        <h3>{spec["card_title"]}</h3>
        <p>{spec["card_p"]}</p>
      </a>
'''
    insert_card(spec["after_href"], card)
    bump_counts(1)
else:
    print("card exists, skip bump")
insert_sitemap(spec["after_loc"], f"https://kalyo.io/articulos/{slug}.html")
print("UPDATED", slug)
