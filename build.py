#!/usr/bin/env python3
"""Genera una web estatica multi-pagina a partir de web/index.html (SPA amb rutes #/).
Sortida: dist/  ->  index.html, /qui-som/index.html, ... + assets/styles.css + assets/app.js
Cada pagina te el seu <title>, descripcio, canonical i nomes el seu contingut."""
import os, re, shutil, html

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'web', 'index.html')
WEB = os.path.dirname(SRC)
OUT = os.path.join(os.path.dirname(SRC), '..', 'dist')
BASE = 'https://honestpg.com'

src = open(SRC, encoding='utf-8').read()

# ---------- 1. trossejar el document ----------
head_start = src.index('<head>')
head_end = src.index('</head>')
head = src[head_start+len('<head>'):head_end]

style = re.search(r'<style>(.*?)</style>', src, re.S).group(1)

scripts = re.findall(r'<script>(.*?)</script>', src, re.S)          # sense el JSON-LD (te type)
jsonld = re.search(r'<script type="application/ld\+json">(.*?)</script>', src, re.S).group(0)

# el 1r script es el router de hash i el 4t la recarrega local: fora de la build
router_js = scripts[0]
scripts_out = [sc for sc in scripts if 'Recàrrega automàtica' not in sc and sc is not router_js]

header_html = re.search(r'(<header class="top">.*?</header>)', src, re.S).group(1)
drawer_html = re.search(r'(<div class="drawer" id="drawer".*?</div></div>)', src, re.S)
drawer_html = re.search(r'(<div class="drawer" id="drawer".*?</nav></div>)', src, re.S).group(1)
footer_html = re.search(r'(<footer class="site-foot">.*?</footer>)', src, re.S).group(1)

# ---------- 2. extreure cada pagina ----------
def pages(text):
    out = []
    for m in re.finditer(r'<div class="page" data-route="([^"]+)" data-title="([^"]*)"[^>]*>', text):
        start = m.start()
        i = m.end(); depth = 1
        for t in re.finditer(r'<(/?)div\b[^>]*>', text[m.end():]):
            if t.group(1): depth -= 1
            else: depth += 1
            if depth == 0:
                i = m.end() + t.end(); break
        inner = text[m.end():i-len('</div>')]
        out.append({'route': m.group(1), 'title': html.unescape(m.group(2)), 'html': inner})
    return out

PAGES = pages(src)
print('pagines trobades:', len(PAGES))

def slug(route):
    return '' if route == '/' else route.strip('/') + '/'

def desc(page):
    m = re.search(r'<p class="lede">(.*?)</p>', page['html'], re.S)
    if not m:
        m = re.search(r'<p>(.*?)</p>', page['html'], re.S)
    t = re.sub(r'<[^>]+>', '', m.group(1)) if m else 'Associació Honest, estudi creatiu sense ànim de lucre de Palma.'
    t = re.sub(r'\s+', ' ', t).strip()
    return (t[:157] + '…') if len(t) > 158 else t

def img_of(page):
    m = re.search(r'<img src="(img/[^"]+)"', page['html'])
    return BASE + '/' + m.group(1) if m else BASE + '/img/egl-card.jpg'

# ---------- 3. reescriure enllaços #/x -> /x/ ----------
def rewrite(t):
    def _h(m):
        path, sep, query = m.group(1).partition('?')
        return 'href="/' + (path + '/' if path else '') + (('?' + query) if query else '') + '"'
    t = re.sub(r'href="#/([^"]*)"', _h, t)
    # rutes relatives d'actius -> absolutes (si no, es trenquen a /projectes/x/)
    t = re.sub(r'(src|href|poster)="(?!https?:|//|/|#|data:|mailto:|tel:)([^"]+)"',
               lambda m: m.group(1) + '="/' + m.group(2) + '"', t)
    return t

# ---------- 4. escriure ----------
os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
open(os.path.join(OUT, 'assets', 'styles.css'), 'w', encoding='utf-8').write(style)

nav_js = """
/* estat actiu del menu segons la URL */
(function(){
  var p = location.pathname.replace(/\\/index\\.html$/, '');
  if (p.length > 1) p = p.replace(/\\/$/, '');
  [].forEach.call(document.querySelectorAll('[data-nav]'), function(a){
    var n = a.getAttribute('data-nav');
    if (p === n || (n !== '/' && p.indexOf(n + '/') === 0)) a.setAttribute('aria-current', 'page');
    else a.removeAttribute('aria-current');
  });
  var f = /[?&]f=([^&]+)/.exec(location.search);
  if (f) { var c = document.querySelector('.chip[data-filter="' + decodeURIComponent(f[1]) + '"]'); if (c) c.click(); }
})();
"""
# llista de projectes per a les cards aleatories de cada fitxa (a la web d'un sol
# fitxer es llegeix del DOM; aqui cada pagina va sola i cal injectar-la)
import json as _json
_proj = []
for _pg in PAGES:
    if _pg['route'] != '/projectes':
        continue
    for _m in re.finditer(r'<a class="card work" data-cat="[^"]*" href="#/projectes/([^"]+)">'
                          r'<div class="ph ([^"]*)">'
                          r'(?:<img[^>]*?src="([^"]+)"[^>]*?alt="([^"]*)"[^>]*>)?.*?'
                          r'<p class="k">(.*?)</p><h3>(.*?)</h3>'
                          r'(?:<p class="wd">(.*?)</p>)?', _pg['html'], re.S):
        _proj.append({'h': '/projectes/' + _m.group(1) + '/',
                      'c': _m.group(2).strip(),
                      'i': ('/' + _m.group(3)) if _m.group(3) else '',
                      'a': _m.group(4) or '',
                      'k': re.sub(r'<[^>]+>', '', _m.group(5)),
                      't': re.sub(r'<[^>]+>', '', _m.group(6)),
                      'w': re.sub(r'<[^>]+>', '', _m.group(7) or '')})
proj_js = 'window.__PROJ=' + _json.dumps(_proj, ensure_ascii=False) + ';\n'
print('projectes per a les cards:', len(_proj))

open(os.path.join(OUT, 'assets', 'app.js'), 'w', encoding='utf-8').write(proj_js + '\n'.join(scripts_out) + '\n' + nav_js)

hash_redirect = ('<script>/* Enllacos antics de la web antiga amb la ruta al hash (#/contacte) cap a la pagina real */\n'
  '(function(){var h=location.hash;if(h.indexOf("#/")!==0)return;var p=h.slice(1);\n'
  'if(p.charAt(1)==="/")return;if(!/^\\/[a-z0-9\\-\\/]*$/i.test(p))return;\n'
  'if(p.slice(-1)!=="/")p+="/";if(p==="/")return;location.replace(p);})();</script>')

head_base = re.sub(r'<style>.*?</style>', '', head, flags=re.S)
head_base = re.sub(r'<title>.*?</title>', '', head_base, flags=re.S)
head_base = re.sub(r'<script type="application/ld\+json">.*?</script>', '', head_base, flags=re.S)
head_base = re.sub(r'<meta name="description"[^>]*>', '', head_base)
head_base = re.sub(r'<meta property="og:(title|description|image|url)"[^>]*>', '', head_base)
head_base = re.sub(r'<meta name="twitter:(title|description|image)"[^>]*>', '', head_base)
head_base = re.sub(r'<link rel="canonical"[^>]*>', '', head_base)
head_base = re.sub(r'\n{2,}', '\n', head_base).strip()



for pg in PAGES:
    url = BASE + '/' + slug(pg['route'])
    d = desc(pg); im = img_of(pg)
    body = rewrite(pg['html'])
    hb = head_base.replace('viewport-fit=cover">', 'viewport-fit=cover">\n' + hash_redirect, 1) if pg['route'] == '/' else head_base
    doc = ('<!doctype html>\n<html lang="ca">\n<head>\n' + hb + '\n'
        '<title>' + html.escape(pg['title']) + '</title>\n'
        '<meta name="description" content="' + html.escape(d) + '">\n'
        '<link rel="canonical" href="' + url + '">\n'
        '<meta property="og:title" content="' + html.escape(pg['title']) + '">\n'
        '<meta property="og:description" content="' + html.escape(d) + '">\n'
        '<meta property="og:image" content="' + im + '">\n'
        '<meta property="og:url" content="' + url + '">\n'
        '<meta name="twitter:title" content="' + html.escape(pg['title']) + '">\n'
        '<meta name="twitter:description" content="' + html.escape(d) + '">\n'
        '<meta name="twitter:image" content="' + im + '">\n'
        + (jsonld + '\n' if pg['route'] == '/' else '')
        + '<link rel="stylesheet" href="/assets/styles.css">\n</head>\n<body>\n'
        + rewrite(header_html) + '\n' + rewrite(drawer_html) + '\n'
        + '<main><div class="page" data-route="' + pg['route'] + '">' + body + '</div></main>\n'
        + rewrite(footer_html) + '\n'
        + '<script defer src="/assets/app.js"></script>\n</body>\n</html>\n')
    dest = os.path.join(OUT, slug(pg['route']), 'index.html')
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, 'w', encoding='utf-8').write(doc)

# assets estatics
for name in ('img', 'docs'):
    shutil.copytree(os.path.join(WEB, name), os.path.join(OUT, name), dirs_exist_ok=True)
for name in ('netlify.toml', 'robots.txt'):
    shutil.copy(os.path.join(WEB, name), os.path.join(OUT, name))

# sitemap
urls = ''.join('  <url><loc>%s</loc></url>\n' % (BASE + '/' + slug(p['route'])) for p in PAGES)
open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write(
  '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')

print('dist generat amb', len(PAGES), 'pagines a', os.path.normpath(OUT))
