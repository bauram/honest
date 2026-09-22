import re,os
p=os.path.expanduser('~/mnt/honest-web/web/index.html');s=open(p,encoding='utf-8').read()
B=lambda t,x:f'<p><b>{t}</b>{x}</p>'
D={
'fundacio-tutelar-dema':('Nova web per a la Fundació Tutelar Demà, fruit d’un conveni de col·laboració: una fundació que acompanya persones amb discapacitat intel·lectual i que tenia una web de 2004.',
 B('Un conveni','El projecte neix d’un conveni de col·laboració signat entre la fundació i Honest.')+B('De 2004 a avui','La web anterior era de l’any 2004 i s’havia quedat molt desactualitzada. N’hem fet una de nova, clara i actual, que explica millor la feina de la fundació.')+B('Accessible per a tothom','Hem treballat amb criteris d’accessibilitat perquè qualsevol persona hi pugui navegar sense barreres.'),
 'Conveni · Disseny web · Desenvolupament · Accessibilitat','Nova web accessible per a la fundació, fruit d’un conveni: de la web de 2004 a una web clara i actual.'),
'balcons-per-palestina':('Un projecte d’activació social: grups de persones es reuneixen per teixir banderes de Palestina i omplir els balcons de solidaritat.',
 B('Teixir juntes','Vam organitzar cinc tallers a Mallorca on grups de dones es trobaven per cosir i teixir banderes de Palestina per penjar als balcons.')+B('Mobilització comunitària','El teixir es va convertir en una excusa per trobar-se, conversar i activar el barri. Juntament amb Balcons per la Pau.')+B('L’excedent, solidari','Les banderes sobrants es van vendre i el projecte va créixer de manera comunitària.'),
 'Activació social · Tallers · Campanya · Comunitat','Cinc tallers per teixir banderes de Palestina i omplir els balcons: activació social i comunitària amb Balcons per la Pau.'),
'revista-lestel':('Redisseny de L’Estel, una revista amb 40 anys d’història que s’havia quedat desactualitzada.',
 B('Noves retícules','Vam dissenyar noves graelles i un redisseny complet de la maquetació per donar-li una lectura més actual.')+B('Set números d’acompanyament','Durant set números vam fer consultoria i acompanyament a l’equip; després ells han continuat amb el sistema que vam construir plegats.')+B('Més que paper','Vam actualitzar els continguts i la línia editorial, i vam començar a treballar l’Instagram i la web.'),
 'Redisseny editorial · Consultoria · Línia editorial · Xarxes','Redisseny d’una revista amb 40 anys d’història: noves retícules, línia editorial i set números d’acompanyament.'),
'regenera-deia':('Suport en comunicació, web i xarxes socials a Regenera Deià, un projecte de regeneració comunitària amb conveni de col·laboració.',
 B('Comunicació','Acompanyam el projecte en la comunicació i en com explica la seva feina.')+B('Web i xarxes','Hem desenvolupat la web i portam les xarxes socials del projecte.'),
 'Conveni · Comunicació · Web · Xarxes socials','Suport en comunicació, web i xarxes socials per a un projecte de regeneració comunitària a Deià.'),
'fundacio-mediterrani':('Nova web i nova imatge per a la Fundació Iniciatives del Mediterrani, amb conveni de col·laboració.',
 B('Una imatge nova','Hem actualitzat tot el branding: logotip i imatge gràfica, que s’havien quedat antics.')+B('Una web moderna','Una web de disseny actual que connecta amb els públics més joves i amb el públic objectiu de la fundació.'),
 'Conveni · Branding · Logotip · Disseny web','Nou branding, logotip i una web moderna que connecta amb els públics joves de la fundació.'),
'mapa-de-ruido':('Comunicació, xarxes i organització del festival d’art sonor Mapa de Ruido, on participam en la direcció com a part associada.',
 B('Direcció del festival','Formam part de la direcció del festival com a entitat associada.')+B('Comunicació i xarxes','Hem portat la comunicació, el seguiment i les xarxes socials.')+B('Esdeveniments i càpsules','Organització del festival i de les càpsules, com Alta Intensitat i Síntesi Modular, a l’Espacio Pulpo.')+'<p><b>També hi vam fer un taller</b>Dins el festival vam impartir un taller de live coding i mapping. <a class="u" href="#/projectes/taller-live-coding">Veure el taller</a></p>',
 'Direcció · Comunicació · Xarxes · Producció d’esdeveniments','Direcció associada, comunicació, xarxes i organització de càpsules del festival d’art sonor.'),
'taller-live-coding':('Un taller de noves tecnologies perquè la gent aprengués a fer art a través del codi de programació, dins el festival Mapa de Ruido.',
 B('Art amb codi','El live coding converteix el codi en un instrument: s’escriu en directe per crear so i imatge.')+B('Mapping i vectors','Vam treballar la generació de formes i vectors amb codi i la seva projecció sobre l’espai.')+'<p><b>Dins el festival</b>El taller formava part de <a class="u" href="#/projectes/mapa-de-ruido">Mapa de Ruido</a>.</p>',
 'Formació · Live coding · Mapping · Codi creatiu','Aprendre a fer art amb codi de programació: live coding i mapping dins el festival Mapa de Ruido.'),
'cube':('Una galeria efímera al centre de Palma durant el darrer trimestre de 2025, amb exposicions d’artistes al voltant del turisme de masses.',
 B('Dels marges al centre','CUBE portava al centre de Palma mirades crítiques sobre el turisme de masses.')+B('Un cub blanc','L’espai era literalment un white cube, el cub blanc típic de les galeries d’art, i a dins s’hi feien intervencions artístiques.')+B('Tornarà','Actualment l’espai és en obres; en un futur el tornarem a obrir.'),
 'Galeria · Comissariat · Exposicions · Producció','Galeria efímera al centre de Palma: un cub blanc amb exposicions sobre el turisme de masses.'),
'saufausreden':('Programa de residències artístiques a Corall 12, a la Platja de Palma, que convida artistes de tot el món a dialogar amb el turisme de masses.',
 B('Residències a la Platja de Palma','Convidam artistes de tot el món a viure i treballar a Corall 12, a la zona del Ballermann.')+B('Transitar el paisatge','Els artistes recorren el paisatge de la Platja de Palma, el transformen i dialoguen amb el turisme de masses.')+B('2025','Dues edicions: Margarito de la Guetto i Llorenç Garrit.'),
 'Residències · Art contemporani · Territori','Residències a la Platja de Palma: artistes de tot el món transformen el paisatge i dialoguen amb el turisme de masses.'),
'nit-de-lart-santanyi':('Instal·lació d’art interactiu per a la Nit de l’Art de Santanyí: projeccions amb intel·ligència artificial i reconeixement facial de la gent que hi passava.',
 B('Art d’interacció','Muntam diferents sistemes amb què el públic interactuava i es veia transformat en directe.')+B('Art, tecnologia i nous mitjans','Una peça que uneix intel·ligència artificial, visió per computador i espai públic. Per a l’Ajuntament de Santanyí.'),
 'Instal·lació · IA · Reconeixement facial · Nous mitjans','Projeccions amb IA i reconeixement facial: art d’interacció a l’espai públic de Santanyí.'),
'can-costa':('Nova direcció de marca i direcció creativa de Can Costa, el centre cultural de la casa natal de Miquel Costa i Llobera, a Pollença.',
 B('Marca','Hem definit la nova direcció de marca del centre cultural.')+B('Direcció creativa','Portam la direcció creativa, la web i la comunicació de la seva programació, com el festival de música.'),
 'Direcció de marca · Direcció creativa · Web · Comunicació','Nova direcció de marca i creativa del centre cultural de la casa natal de Miquel Costa i Llobera.'),
'creativitats-que-sumen':('Una jornada creativa organitzada amb la Fundación Aldaba per apoderar persones en situació d’exclusió social a través de l’art.',
 B('Art per apoderar','Dibuixàvem i cream plegats: l’art com a eina per donar veu i confiança a les persones.')+B('Amb la Fundación Aldaba','Un esdeveniment coorganitzat amb la fundació, obert i participatiu.'),
 'Esdeveniment · Tallers · Art participatiu','Jornada amb la Fundación Aldaba per apoderar persones en exclusió social a través de l’art.'),
'aina-losange':('Col·laboració en l’escenografia del videoclip d’Aina Losange, on apareix una de les nostres obres d’art.',
 B('Escenografia','Una obra d’Honest, Hello God, forma part del fons del videoclip i s’integra en la narrativa visual.')+B('Presentació','El videoclip es va presentar a Honest amb una instal·lació de televisors.'),
 'Escenografia · Art · Vídeo','Escenografia del videoclip d’Aina Losange amb una de les nostres obres d’art.'),
'data-to-design':('Transformam dades climàtiques en gràfics vectorials per fer disseny en temps real: el disseny canvia quan canvien les dades meteorològiques.',
 B('Real time design','Els gràfics es generen a partir de dades climàtiques i es transformen contínuament segons el temps que fa.')+B('Aplicat a l’Acadèmia del Clima','S’ha aplicat principalment a la web de l’Acadèmia del Clima i a peces de comunicació sobre temàtiques climàtiques. <a class="u" href="#/projectes/academia-del-clima">Veure el projecte</a>'),
 'Recerca · Dades · Disseny generatiu · Temps real','Dades climàtiques convertides en gràfics vectorials: un disseny que canvia amb el temps meteorològic.'),
'academia-del-clima':('Conveni de col·laboració amb l’Acadèmia del Clima: comunicació gràfica de tot l’any, consultoria de sistemes informàtics i web.',
 B('Comunicació gràfica','Vam dissenyar tots els cartells i la comunicació gràfica de l’any.')+B('Sistemes i web','Consultoria de sistemes informàtics i desenvolupament de la web, on apliquem el projecte <a class="u" href="#/projectes/data-to-design">Data to Design</a>.'),
 'Conveni · Comunicació gràfica · Consultoria · Web','Conveni amb l’Acadèmia del Clima: cartells de tot l’any, consultoria de sistemes i web.'),
'premi-benet-ams':('Guanyadors del Premi Benet Ams de Ceràmica amb una instal·lació d’art i tecnologia amb ceràmiques interactives.',
 B('Ceràmica d’aquí a 30 anys','La instal·lació imaginava com serà el món de la ceràmica d’aquí a trenta anys, barrejat amb intel·ligència artificial i robòtica.')+B('Peces interactives','Ceràmiques que responen al públic: un diàleg entre l’ofici més antic i la tecnologia més nova.'),
 'Instal·lació · Ceràmica · IA · Robòtica · Premi','Premi de ceràmica per una instal·lació amb ceràmiques interactives, IA i robòtica.'),
'corall-12':('El nostre estudi creatiu a la Platja de Palma: tallers de pintura, fusteria i ceràmica, residències artístiques i cowork.',
 B('Tallers','Un espai amb taller de pintura, de fusteria i de ceràmica, on es poden desenvolupar les disciplines artístiques.')+'<p><b>Residències</b>Aquí es fan les residències artístiques, com <a class="u" href="#/projectes/saufausreden">Saufausreden</a>.</p>'+B('Cowork','També és un cowork creatiu on es pot venir a treballar.'),
 'Estudi · Tallers · Residències · Cowork','Estudi creatiu amb tallers de pintura, fusteria i ceràmica, residències i cowork a la Platja de Palma.'),
'mater-ariany':('Web de l’hotel de Mater a Ariany, pensada des de l’accessibilitat.',
 B('Accessibilitat','Vam aplicar principis d’accessibilitat i funcionalitat perquè persones amb discapacitat física, auditiva o visual hi puguin navegar sense problemes.')+B('Manteniment','Acompanyament i manteniment anual de la web.'),
 'Disseny web · Accessibilitat · Manteniment','Web accessible de l’hotel de Mater a Ariany, pensada per a persones amb discapacitat.'),
'possessio-muntanya':('Web de Possessió Muntanya, una explotació agrícola que vol reactivar la possessió a través de la producció d’oli.',
 B('Reactivar la terra','Una web que explica el projecte de recuperació agrícola de la possessió.')+B('Manteniment','Acompanyament i manteniment anual.'),
 'Disseny web · Desenvolupament · Manteniment','Web d’una explotació agrícola que reactiva la possessió a través de l’oli.'),
'packaging-noma':('Tot el packaging de la línia de cosmètica de cànem de la Cooperativa NOMA, un projecte de reactivació de l’agricultura balear.',
 B('Cosmètica de cànem','Vam dissenyar el packaging de tota la línia de productes.')+B('Agricultura balear','La cooperativa impulsa la reactivació agrícola de les Illes, i el projecte neix del conveni de col·laboració amb Honest.'),
 'Conveni · Packaging · Disseny gràfic','Packaging de la línia de cosmètica de cànem d’una cooperativa que reactiva l’agricultura balear.'),
'dbalears-dijous-bo':('Direcció d’art i editorial de l’edició impresa del diari dBalears per al Dijous Bo, amb més de 20.000 exemplars.',
 B('En paper','Vam dissenyar el diari imprès del qual es van fer més de 20.000 còpies.')+B('Direcció d’art','La direcció d’art i editorial es va portar des d’Honest.'),
 'Direcció d’art · Disseny editorial · Premsa','Direcció d’art i editorial d’un diari imprès de més de 20.000 exemplars.'),
'taller-polaroid':('Taller de fotografia social amb l’artista Margarito de la Guetto, amb càmeres i carrets Polaroid pels carrers de Palma.',
 B('Fotografia social','Un taller per acostar la fotografia social a les persones.')+B('Pel barri','Dinàmiques amb càmeres i carrets Polaroid pel barri de Pere Garau, a Palma.'),
 'Formació · Fotografia · Taller','Fotografia social amb Polaroid pels carrers de Palma amb Margarito de la Guetto.'),
'lens-festival':('Instal·lació per al Lens Festival sobre la interacció entre humans i màquines: com, a través de la càmera, l’ésser humà es veu a si mateix.',
 B('Humà i màquina','Una peça que explora la relació entre les persones i la tecnologia a través de la imatge.')+B('Intel·ligència artificial','La instal·lació utilitzava IA per transformar la mirada del públic sobre si mateix.'),
 'Instal·lació · IA · Nous mitjans','Instal·lació sobre la interacció humà-màquina: la càmera com a mirall, amb IA.'),
}
def upd(slug,lede,body,what,wd):
  global s
  a=s.index(f'<div class="page" data-route="/projectes/{slug}"'); b=s.index('<div class="page"',a+10)
  seg=s[a:b]
  seg=re.sub(r'<p class="lede">.*?</p></section>',f'<p class="lede">{lede}</p></section>',seg,count=1,flags=re.S)
  seg=re.sub(r'<div class="two"><div>.*?</div>\n<div><p class="m">Què hi vam fer</p><p>[^<]*</p>',f'<div class="two"><div>{body}</div>\n<div><p class="m">Què hi vam fer</p><p>{what}</p>',seg,count=1,flags=re.S)
  s=s[:a]+seg+s[b:]
  s,n=re.subn(r'(<a class="card work"[^>]*href="#/projectes/'+slug+r'".*?<p class="wd">)[^<]*(</p></a>)',lambda m:m.group(1)+wd+m.group(2),s,flags=re.S)
  return n
for k,(l,b,w,wd) in D.items(): print(k,upd(k,l,b,w,wd))
# replace nits-classiques with hello-god-campos
a=s.index('<div class="page" data-route="/projectes/nits-classiques-can-costa"'); b=s.index('<div class="page"',a+10) if '<div class="page"' in s[a+10:] else s.index('</main>',a)
nx=re.search(r'<a class="next" href="([^"]+)">([^<]*)</a>',s[a:b])
new=f'''<div class="page" data-route="/projectes/hello-god-campos" data-title="Hello God · Nit de l’Art de Campos · Honest" hidden>
<section class="pt"><p class="m"><a class="u" href="#/projectes">Projectes</a> · <i class="dot d-red"></i>Creativitat + Tecnologia · Instal·lació</p><h1>Hello God · Nit de l’Art de Campos</h1><p class="lede">Una instal·lació que presenta la tecnologia com a substitució de les necessitats espirituals de l’ésser humà. La van veure més de 10.000 persones.</p></section>
<section class="s"><div class="two"><div><p><b>Una nova fe</b>Hello God planteja com la tecnologia ocupa el lloc que abans tenia l’espiritualitat, i a quines noves dependències ens porta.</p><p><b>Nit de l’Art de Campos</b>Instal·lació presentada a la Nit de l’Art de Campos, amb més de 10.000 visitants.</p></div>
<div><p class="m">Què hi vam fer</p><p>Instal·lació · Art i tecnologia · Producció</p></div></div></section>
<section class="s"><div class="h"><span>Següent</span><span></span></div><a class="next" href="{nx.group(1)}">{nx.group(2)}</a></section></div>
'''
s=s[:a]+new+s[b:]
s=re.sub(r'<a class="card work"[^>]*href="#/projectes/nits-classiques-can-costa".*?</a>','<a class="card work" data-cat="art esdeveniments" href="#/projectes/hello-god-campos"><div class="ph d-red noimg"><span class="blank"><i class="s-circle"></i></span></div><p class="k">Instal·lació · Art i tecnologia</p><h3>Hello God · Nit de l’Art de Campos</h3><p class="wd">La tecnologia com a substitució de les necessitats espirituals: una instal·lació vista per més de 10.000 persones.</p></a>',s,count=1,flags=re.S)
s=s.replace('<a class="next" href="#/projectes/nits-classiques-can-costa">Nits Clàssiques a Can Costa →</a>','<a class="next" href="#/projectes/hello-god-campos">Hello God · Nit de l’Art de Campos →</a>')
open(p,'w',encoding='utf-8').write(s)
print('nits left',s.count('nits-classiques'))
