# Honest — web (refactor sobre base Practice)

Web de **Honest**, estudi creatiu sense ànim de lucre de Mallorca, construïda reescrivint
el contingut de la base clonada de practice.inc. **Només s'ha tocat text** (titulars, cossos,
navegació, metadades, alt, dades tècniques): l'estructura, el CSS i les imatges es mantenen.

## Idioma i to
Català. Veu honesta, càlida i rigorosa, destil·lada del Canon Ramis i de la memòria d'Honest
("l'art i la creativitat com a motor de la transformació social").

## Pàgines (12)
- `index.html` — Inici (qui som + com treballam + amb qui + FAQ + contacte)
- `projectes/` — Projectes (graella)
- `nosaltres/` — Nosaltres
- `metode/` — Mètode
- `projectes/<slug>/` — 8 fitxes de projecte reals: Mapa de Ruido, Fundació Iniciatives del
  Mediterrani, Regenera Deià, Can Costa, Mater Ariany, Cooperativa NOMA, Balcons per Palestina, CUBE.

## Dades reals usades (de la memòria d'Honest)
Contacte: associaciohonest@gmail.com · 670 49 25 91 · C. Sant Llorenç 8, Baixos, Palma · honestpg.com

## Pendent (no fet en aquesta passa)
- **Imatges, logos i vídeos**: encara són els de la base (Practice). Es substitueixen amb la
  skill d'imatges (`refactor-clone-web-imagenes`). El logo de la capçalera és un SVG amb la
  forma "Practice" (el seu text accessible ja diu "Honest").
- Favicon i vídeos encara es serveixen des de dominis de la base (assets a substituir).
- Perfils de xarxes socials: pendents de confirmar (ara apunten a honestpg.com / email).
- Les altres ~21 fitxes de projecte del portfolio original s'han retirat; s'aniran omplint amb
  projectes reals d'Honest.

## Previsualització
cd honest-web && python3 -m http.server 8000  →  http://localhost:8000
