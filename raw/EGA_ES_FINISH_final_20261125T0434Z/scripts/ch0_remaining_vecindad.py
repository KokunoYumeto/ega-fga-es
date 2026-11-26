"""Fourteen source-voisinage contexts per layer, read with agreement restored."""
import re
from corpus import ES,RESULT,write_tsv,labels
from tex_tools import prose_segments,math_spans
changes=[];gloss=[]
for layer in ['CURRENT','DIPLOMATIC']:
 for p in (ES/f'worktree/es/{layer}/EGA_I_ch0').glob('*.tex'):
  t=p.read_text();original=t;edits=[]
  for a,b,s in prose_segments(t):
   if not re.search(r'\bentornos?\b',s):continue
   n=s
   for old,new in [('los entornos abiertos','las vecindades abiertas'),('los entornos','las vecindades'),('todo entorno abierto','toda vecindad abierta'),('un entorno abierto','una vecindad abierta'),('un entorno','una vecindad'),('entorno abierto','vecindad abierta')]:n=n.replace(old,new)
   if n!=s:edits.append((a,b,n));place=labels(t[:a]);place=place[-1][0] if place else 'front';changes.append([str(p.relative_to(RESULT)),place,s,n,'standard','DECISIONS_20261119b.tsv: es-voisinage; French 0 §§2–3 context reviewed'])
  for a,b,n in reversed(edits):t=t[:a]+n+t[b:]
  old=r'vecindad de $x$ contenido en';new=r'vecindad de $x$ contenida en'
  if old in t:
   changes.append([str(p.relative_to(RESULT)),'0.3.7.1',old,new,'standard','es-voisinage agreement']);t=t.replace(old,new)
  assert [x.text for x in math_spans(t)]==[x.text for x in math_spans(original)]
  if t!=original:p.write_text(t)
  for m in re.finditer(r'\bvecindades?\b',t):
   ll=labels(t[:m.start()]);place=ll[-1][0] if ll else 'front';gloss.append(['voisinage',m[0],'standard/DECISIONS_20261119b.tsv; source French 0 §§2–3 reviewed',str(p.relative_to(RESULT))+':'+place,'yes'])
write_tsv(RESULT/'records/CAMBIOS_ch0_remaining_vecindad.tsv',['file','place','before','after','kind','source'],changes)
# Name avoids the consolidated ch0 fragment exclusion in the merger.
(RESULT/'records/CAMBIOS_ch0_remaining_vecindad.tsv').rename(RESULT/'records/CAMBIOS_root_ch0_vecindad.tsv')
write_tsv(RESULT/'records/GLOSARIO_REGISTRO_root_ch0_vecindad.tsv',['french_term','spanish_rendering','witness','places','reversible'],gloss)
print('Changed contexts',len(changes))
