import re,os
p=os.path.expanduser('~/mnt/honest-web/web/index.html');s=open(p,encoding='utf-8').read()
IG='https://www.instagram.com/honest_playground/'; MEM='docs/memoria-honest-2025.pdf'
L={
'fundacio-tutelar-dema':[('Veure la web','https://fundaciotutelardema.honestpg.com/')],
'balcons-per-palestina':[('Notícia a dBalears','https://www.dbalears.cat/balears/balears/2025/09/11/410577/tallers-confeccio-banderes-palestines-balcons-per-pau.html'),('Memòria 2025 (PDF)',MEM)],
'revista-lestel':[('Veure la revista','https://www.revistalestel.cat/')],
'regenera-deia':[('Veure la web','https://regeneradeia.com/'),('Agenda a l’Ajuntament de Deià','https://ajdeia.net/ca/agenda/regenera-deia-0')],
'fundacio-mediterrani':[('Veure la web','https://www.fim.eco/')],
'mapa-de-ruido':[('Instagram del festival','https://www.instagram.com/mapaderuido/'),('Web del festival','https://mapaderuido.neocities.org/')],
'taller-live-coding':[('Instagram de Mapa de Ruido','https://www.instagram.com/mapaderuido/'),('Memòria 2025 (PDF)',MEM)],
'cube':[('Instagram d’Honest',IG),('Memòria 2025 (PDF)',MEM)],
'saufausreden':[('Instagram d’Honest',IG),('Memòria 2025 (PDF)',MEM)],
'nit-de-lart-santanyi':[('Nit de l’Art a l’Ajuntament de Santanyí','https://ajsantanyi.net/en/node/9985')],
'can-costa':[('Veure la web','https://www.cancosta.art/')],
'creativitats-que-sumen':[('Fundación Aldaba','https://aldaba.ong/'),('Memòria 2025 (PDF)',MEM)],
'aina-losange':[('Canal de YouTube d’Aina Losange','https://www.youtube.com/@ainalosange2917'),('Web d’Aina Losange','https://www.ainalosange.com/')],
'data-to-design':[('Veure-ho a la web de l’Acadèmia del Clima','https://academiadelclima.org/')],
'academia-del-clima':[('Veure la web','https://academiadelclima.org/')],
'premi-benet-ams':[('Instagram d’Honest',IG)],
'corall-12':[('Instagram d’Honest',IG),('Memòria 2025 (PDF)',MEM)],
'mater-ariany':[('Veure la web','https://materariany.com/')],
'possessio-muntanya':[('Memòria 2025 (PDF)',MEM)],
'packaging-noma':[('Web de NOMA','https://nomaoriginal.com/'),('Productes Canem','https://www.canem.es/')],
'dbalears-dijous-bo':[('dBalears','https://www.dbalears.cat/'),('Memòria 2025 (PDF)',MEM)],
'taller-polaroid':[('Instagram d’Honest',IG),('Memòria 2025 (PDF)',MEM)],
'lens-festival':[('Memòria 2025 (PDF)',MEM)],
'hello-god-campos':[('Instagram d’Honest',IG)],
}
def a(t,u):
  ext=u.startswith('http'); dl=u.endswith('.pdf')
  attrs=' target="_blank" rel="noopener"' if ext or dl else ''
  arr='↓' if dl else '↗'
  return f'<a class="plink" href="{u}"{attrs}><span>{t}</span><span class="arr" aria-hidden="true">{arr}</span></a>'
n=0
for slug,links in L.items():
  i=s.index(f'<div class="page" data-route="/projectes/{slug}"')
  j=s.index('<section class="s"><div class="h"><span>Següent</span>',i)
  if 'class="plinks"' in s[i:j]: continue
  blk='<section class="s"><div class="h"><span>Veure més</span><span></span></div><div class="plinks">'+''.join(a(t,u) for t,u in links)+'</div></section>\n'
  s=s[:j]+blk+s[j:]; n+=1
css='''
/* enllaços de projecte */
.plinks{display:flex;flex-wrap:wrap;gap:14px 40px}
.plink{display:inline-flex;align-items:baseline;gap:10px;font-size:clamp(17px,1.5vw,20px);font-weight:700;color:var(--ink);border-bottom:1px solid var(--ink);padding-bottom:6px}
.plink .arr{display:inline-block;transition:transform .25s}
.plink:hover{color:var(--g);border-color:var(--g)}
.plink:hover .arr{transform:translate(3px,-3px)}
'''
k=s.index('</style>'); s=s[:k]+css+s[k:]
open(p,'w',encoding='utf-8').write(s); print(n)
