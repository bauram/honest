# Honest — com treballar en aquest projecte

Web de l'**Associació Honest** (honestpg.com), estudi creatiu sense ànim de lucre de Palma
que posa creativitat i tecnologia al servei del tercer sector.

Abans de tocar res de disseny, copy o qualsevol peça de marca, aplica la skill
**honest-art-direction** (paleta, tipografia, retícula, to de veu). Aquest document explica
com està muntat el projecte i com s'hi treballa; la skill explica com ha de quedar.

---

## 1. Estructura

```
honest-web/
├─ web/index.html      ← L'ÚNIC fitxer que s'edita. Tota la web: CSS, JS i les 39 pàgines.
├─ web/img/            imatges, vídeos (.mp4 + .webm), logos a img/entitats/
├─ web/docs/           PDFs públics (estatuts, memòries, convenis)
├─ web/_no-usats/      fitxers retirats, pendents d'esborrar a mà
├─ build.py            genera dist/ (una URL real per pàgina)
├─ dist/               sortida del build — NO s'edita mai a mà
├─ deploy.sh           build + push a github.com/bauram/honest + desplegament a Netlify
└─ README-build.md     resum del build i el desplegament
```

`web/index.html` és una SPA amb encaminador de hash: cada pàgina és un
`<div class="page" data-route="/…">` i el CSS viu tot dins un sol `<style>`.

---

## 2. Com editar

- **Sempre amb un script de python que llegeix i reescriu el fitxer** (`str.replace` sobre
  una cadena única), o amb `sed -i`. Mai reescrivint el fitxer sencer a partir del que
  s'ha llegit: es perd contingut i el fitxer fa ~210 KB.
- El CSS nou s'afegeix **just abans de `</style>`**, en un bloc amb comentari que digui què fa.
  Les regles del final guanyen; si una regla antiga s'hi resisteix, cal `!important`.
- Una regla nova no ha de canviar l'escriptori si el canvi és de mòbil: envolta-la amb
  `@media(max-width:860px)` (o 620px per a les fotos de fitxa).
- `data-route` i `data-title` han d'existir a cada pàgina nova: el build els fa servir per
  generar `<title>`, descripció i canonical.

## 3. Verificar abans de donar res per fet

1. Còpia del fitxer a un servidor local i obre'l amb Chromium/Playwright.
2. Comprova, com a mínim: consola sense errors, `scrollWidth === clientWidth` (cap
   desbordament horitzontal) a **390, 768 i 1440 px**, i que les imatges i vídeos carreguen.
3. Per a canvis visuals, fes captura i mira-la. No et refiïs del codi.

## 4. Build i desplegament

```bash
python3 build.py                  # genera dist/ (39 pàgines + assets + sitemap)
bash deploy.sh "missatge"         # build + GitHub + desplegament de prova
bash deploy.sh "missatge" prod    # publica a honestpg.com
```

- A Netlify el **directori de publicació ha de ser `dist`**, no `web`.
- Després de qualsevol canvi a `web/index.html`, torna a executar `build.py`.
- Previsualització local: `python3 -m http.server 8000` dins de `web/`.

## 5. Imatges i vídeos

- Fitxa de projecte: la imatge **horitzontal és la card**; les altres van dins la fitxa.
- Cards en 4:5, vídeos i finestres de web en 16:9.
- Tot vídeo va en **dos formats**: `.webm` (VP9) i `.mp4` (H.264), `muted loop playsinline`,
  amb `preload="none"` i `data-lazyvid="1"` — un IntersectionObserver els arrenca quan són
  visibles i els atura quan surten de pantalla. No afegeixis `autoplay` a mà.
- Vídeos de YouTube: `youtube-nocookie.com/embed/ID`, sense controls, en bucle i **amb so
  activat per defecte**; el botó de silenci ja existeix (`.ytsound`).
- Les webs de clients es mostren com un vídeo de scroll dins una finestra de navegador
  dibuixada. Es generen capturant la pàgina real amb el navegador (roda del ratolí, no
  `scrollTop`: moltes webs porten scroll suau i no responen), enganxant les captures amb
  correlació d'imatge i renderitzant el paneig a 1800×1124.
- Si es reemplaça una imatge, **fes servir un nom de fitxer nou**: escriure damunt el mateix
  nom de vegades no es propaga i queda la versió antiga.

## 6. Mòbil

L'escriptori està tancat i **no s'ha de tocar**. A mòbil:

- Menú hamburguesa a la capçalera, sense botó de col·laborar.
- Els blocs de text llargs s'amaguen (`.mhide`) i es substitueixen per un acordió
  `Més informació` amb l'avís en vermell que la informació completa és a l'escriptori.
- Franja de color a Qui som (vermell) i Què feim (blau).
- A les fitxes amb fotos, si hi ha un vídeo només es mostra el vídeo.
- El castell del peu no es veu.

## 7. Llengua i contingut

- **Català de Mallorca** (formes balears: feim, col·laboram). Cap llenguatge comercial:
  Honest no ven serveis, col·labora. Res de "clients", "solucions" ni superlatius.
- Vocabulari: **escletxa**, no "bretxa" (castellanisme).
- Als convenis que es pengen, **tapa en negre les dades sensibles**: DNI/NIF, adreces
  particulars i signatures. Els noms de persona i les dades de l'entitat es mantenen.
  La redacció ha de ser irreversible (rasteritzar el PDF, no només dibuixar un rectangle).

## 8. Limitacions conegudes de l'entorn

- **No es poden esborrar fitxers** de la carpeta: si cal treure'n, mou-los a `web/_no-usats/`
  i avisa. Tampoc es pot sobreescriure un `.zip` existent: crea'l amb un nom nou (o munta'l
  fora de la carpeta i copia'l).
- Ni el contenidor ni el shell local arriben a les webs de clients; només el navegador de
  l'usuari. Les captures de webs externes s'han de fer des d'allà.
- Els PDFs de `web/docs/` pesen ~44 MB i són la major part del pes del repositori.

## 9. Enllaços

- Producció: https://honestpg.com · Repositori: github.com/bauram/honest
- Netlify site id: `06afaf32-06b9-4100-b554-337f06d5dcd1`
- Instagram: @honest_playground · hola@honest.cat
