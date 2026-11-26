"""Translate remaining source errata quotations, retaining mathematical TeX."""
import re
from corpus import RESULT,ES,FR,write_tsv
from tex_tools import math_spans
p=ES/'worktree/es/PORTED_20261109/IV4/ega4/ega4-errata-addenda-list3-es.tex';t=p.read_text();oldmath=[x.text for x in math_spans(t)];rows=[];tr=[];edits=[]
repls=[('localement quasi-fini, localement de présentation finie et dominant','localmente cuasifinito, localmente de presentación finita y dominante'),('localement quasi-fini et dominant','localmente cuasifinito y dominante'),('localement de présentation finie','localmente de presentación finita'),('localement de type fini','localmente de tipo finito'),('localement de tipo finito','localmente de tipo finito'),('localement noethérien','localmente noetheriano'),('équidimensionalité locale','equidimensionalidad local'),('équidimensionalité','equidimensionalidad'),('localement équidimensionnelles','localmente equidimensionales'),('localement équidimensionnels','localmente equidimensionales'),('localement équidimensionnel','localmente equidimensional'),('équidimensionnelles','equidimensionales'),('équidimensionnels','equidimensionales'),('équidimensionnel','equidimensional'),('de dimension 2','de dimensión 2'),('intègre','íntegro'),('Soient','Sean'),('strictement','estrictamente'),('localement','localmente'),('noethérien','noetheriano')]
for m in re.finditer(r'«[\s\S]*?»',t):
 old=m[0];new=old
 for a,b in repls:new=re.sub(r'\s+'.join(re.escape(x) for x in a.split()),lambda m:b,new)
 if new==old:continue
 headers=list(re.finditer(r'\\paragraph\{([^\n]+)',t[:m.start()]));place=headers[-1][1][:200] if headers else 'quoted errata phrase'
 edits.append((m.start(),m.end(),new));rows.append([str(p.relative_to(RESULT)),place,old,new,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/current/IV4/native/ega4/ega4-errata-addenda-list3-fr.tex: corresponding quoted errata reading'])
 prose=re.sub(r'\\[A-Za-z]+',' ',new);words=len(re.findall(r'[A-Za-zÀ-ÿ]+',prose));tr.append([str(p.relative_to(RESULT)),'EGA_ES_FINISH_1_FRANCES/fr/current/IV4/native/ega4/ega4-errata-addenda-list3-fr.tex',place+'; quoted phrase: '+old,words])
for a,b,new in reversed(edits):t=t[:a]+new+t[b:]
assert [x.text for x in math_spans(t)]==oldmath
p.write_text(t)
suffix='';counter=1
while (RESULT/('records/CAMBIOS_iv4_remaining_errata_quotes'+suffix+'.tsv')).exists():
 counter+=1;suffix='_'+str(counter)
write_tsv(RESULT/('records/CAMBIOS_iv4_remaining_errata_quotes'+suffix+'.tsv'),['file','place','before','after','kind','source'],rows)
write_tsv(RESULT/('records/TRADUCCION_iv4_remaining_errata_quotes'+suffix+'.tsv'),['file','french_source','range','words'],tr)
print('quoted passages translated',len(rows),'words',sum(r[-1] for r in tr))
