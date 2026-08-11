# Honest — Web

Web corporativa de **Associació Honest**, estudi creatiu sense ànim de lucre (Palma, Mallorca).
Creativitat i tecnologia per al tercer sector.

Lloc estàtic (HTML + CSS + JS), sense build ni dependències. Tipografies via Google Fonts.

## Pàgines
- `index.html` — Inici (hero a pantalla completa, estil honestpg)
- `nosotros.html` — Qui som
- `servicios.html` — Serveis
- `proyectos.html` — Projectes
- `honest-lab.html` — Honest.Lab
- `contacto.html` — Contacte

## Desenvolupament local
Obre `index.html` al navegador, o serveix la carpeta:

```bash
python3 -m http.server 8000
# després obre http://localhost:8000
```

## Publicar amb GitHub Pages
1. Crea un repositori nou a GitHub i puja aquests fitxers a l'arrel:
   ```bash
   git init
   git add .
   git commit -m "Honest web"
   git branch -M main
   git remote add origin https://github.com/USUARI/REPO.git
   git push -u origin main
   ```
2. Al repo: **Settings → Pages → Build and deployment → Source: Deploy from a branch**,
   branca `main`, carpeta `/ (root)`. Desa.
3. En un minut la web estarà a `https://USUARI.github.io/REPO/`.

> Consell: si vols un domini propi (p. ex. honest.cat), afegeix-lo a Settings → Pages → Custom domain.

## Notes
- El formulari de contacte és una demo sense backend. Per activar-lo, connecta'l a
  Formspree, Netlify Forms o un endpoint propi.
- Les imatges són il·lustracions SVG de marca (a `assets/img/`); substitueix-les per
  fotos i pòsters reals quan els tinguis.
- Alguns textos de projectes estan marcats com a provisionals: revisa'ls.

© Associació Honest · CIF G22446975
