"""Apply reviewed decided glossary equivalents, preserving entier and integral closure."""
import re,collections
from corpus import RESULT,ES,FR,write_tsv
from standardize import canonical_files,place_for
from tex_tools import prose_segments
rows=[];gl=[];dry=[];edits=collections.defaultdict(list)
for p in canonical_files():
 if any(x in str(p) for x in ['/III1_','/III2/','/IV3/']):continue
 t=p.read_text()
 for a,b,s in prose_segments(t):
  for m in re.finditer(r'\bespacio(s)? anillado(s)? en anillos locales(?: noetherianos)?\b',s):
   old=m[0];new='espacios localmente anillados' if m[1] else 'espacio localmente anillado'
   if old.endswith(' noetherianos'):new+=' cuyos anillos locales son noetherianos'
   pos=a+m.start();end=a+m.end();place=place_for(t,pos)
   edits[p].append((pos,end,new));dry.append([str(p.relative_to(RESULT)),place,old,new]);rows.append([str(p.relative_to(RESULT)),place,old,new,'standard','GLOSARIO_es_20261119/GLOSSARY_es.tsv row 11; same locally ringed-space concept, with noetherian qualification retained where present'])
   gl.append(['espace localement annelé / espace annelé en anneaux locaux',new,'GLOSARIO_es_20261119/GLOSSARY_es.tsv row 11 decided',str(p.relative_to(RESULT))+':'+place,'yes'])
for ed in ['CURRENT','DIPLOMATIC']:
 p=ES/f'worktree/es/{ed}/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex';t=p.read_text();old=r'\emph{integral}';new=r'\emph{íntegro}';assert t.count(old)==1
 fp=FR/ed.lower()/'BASE/native/ega1/ega1-7-fr.tex';ft=fp.read_text();assert r'\emph{intègre}' in ft
 pos=t.index(old);edits[p].append((pos,pos+len(old),new));dry.append([str(p.relative_to(RESULT)),'I.7.2.8',old,new]);rows.append([str(p.relative_to(RESULT)),'I.7.2.8',old,new,'standard','GLOSARIO_es_20261119/GLOSSARY_es.tsv row 106; French I.7.2.8 intègre'])
 gl.append(['intègre','íntegro','GLOSARIO_es_20261119/GLOSSARY_es.tsv row 106 decided; French I.7.2.8',str(p.relative_to(RESULT))+':I.7.2.8','yes'])
write_tsv(RESULT/'records/GLOSSARY_FINAL_ROOT_DRY_RUN.tsv',['file','place','before','after'],dry)
for p,ee in edits.items():
 t=p.read_text()
 for a,b,s in sorted(ee,reverse=True):t=t[:a]+s+t[b:]
 p.write_text(t)
write_tsv(RESULT/'records/CAMBIOS_glossary_final_root.tsv',['file','place','before','after','kind','source'],rows)
write_tsv(RESULT/'records/GLOSARIO_REGISTRO_glossary_final_root.tsv',['french_term','spanish_rendering','witness','places','reversible'],gl)
print('glossary changes',len(rows))
