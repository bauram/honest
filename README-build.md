# Web d'Honest — com funciona

## Fonts
- `web/index.html` — **el fitxer que s'edita**. Conté tota la web (CSS, JS i totes les pàgines)
  i funciona sol amb rutes `#/…`. És el que es veu a `localhost:8000`.
- `web/img/`, `web/docs/` — imatges i PDFs.

## Build per a producció
`python3 build.py` genera `dist/`: una **pàgina HTML per ruta** (39 URLs reals com
`/qui-som/` o `/projectes/cube/`), amb el seu `<title>`, descripció, canonical i Open Graph,
el CSS i el JS a part (`dist/assets/`) perquè es cachegin entre pàgines, i el `sitemap.xml`
amb totes les URLs. És el que llegeix bé Google.

## Desplegament
`bash deploy.sh "missatge"` → build + push a github.com/bauram/honest + desplegament de prova.
`bash deploy.sh "missatge" prod` → el mateix, però publica a honestpg.com (demana confirmació).

> Netlify ha de publicar la carpeta `dist` (Site settings → Build & deploy → Publish directory).

## Previsualització local
- Fitxer d'edició: `cd web && python3 -m http.server 8000` → http://localhost:8000
- Resultat de la build: `cd dist && python3 -m http.server 8001` → http://localhost:8001
