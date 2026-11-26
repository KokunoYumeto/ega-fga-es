"""Restore source wording and formula grouping in reviewed I passages.

Existing editorial notes are retained, including where they discuss a different
reading from the supplied French source layer.
"""
import re,csv
from corpus import RESULT,write_tsv
from audit_i_ch1 import texts,i_units
from tex_tools import balanced_end
LOG=RESULT/'records/CAMBIOS_i_source_clauses.tsv'
H=['file','place','before','after','kind','source']
rows=list(csv.DictReader(LOG.open(),delimiter='\t')) if LOG.exists() else []

def replace(num,old,new,layers=('CURRENT','DIPLOMATIC')):
 for layer in layers:
  p,t=texts(layer);whole=p.read_text();u=i_units(t)[num]
  if old not in u.text and new in u.text:continue
  pat=re.escape(old);pat=re.sub(r'(?:\\\s)+',r'\\s+',pat)
  # Literal first, then whitespace-only rebinding for editions with reflowed lines.
  if old in u.text:a=u.text.index(old);b=a+len(old)
  else:
   pat=r'\s+'.join(re.escape(z) for z in old.split());mm=list(re.finditer(pat,u.text))
   if len(mm)!=1:raise ValueError((layer,num,'not unique',old[:100],len(mm)))
   a,b=mm[0].span()
  before=u.text[a:b];whole=whole[:u.start+a]+new+whole[u.start+b:];p.write_text(whole)
  rows.append(dict(zip(H,[str(p.relative_to(RESULT)),num,before,new,'own comparison',f'EGA_ES_FINISH_1_FRANCES/fr/{layer.lower()}/BASE/native/ega1/ega1-{num.split(".")[0]}-fr.tex: {num}; source prose/formula grouping'])))
  write_tsv(LOG,H,[[r[k] for k in H] for r in rows])

