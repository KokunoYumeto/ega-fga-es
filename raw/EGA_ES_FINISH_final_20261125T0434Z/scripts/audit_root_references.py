"""Compare citation targets in already-aligned source/Spanish numbered units."""
import re,json,collections,difflib
from corpus import FR,RESULT,ES,canonical
from audit_i_ch1 import texts,i_units,mask_notes
from audit_iv4 import pairs as iv4pairs
from tex_tools import numbered_units
PAT=re.compile(r'\\hyperref\[([^]]+)\]|\\(?:sref|eref)(?:\[[^]]*\])?\{([^}]+)\}')
def refs(t):
 return [(canonical(m[1] or m[2]),m.start(),m.end(),m[1] or m[2]) for m in PAT.finditer(mask_notes(t))]
out=[]
for layer in ['CURRENT','DIPLOMATIC']:
 p,t=texts(layer);su=i_units(t)
 for fp in (FR/layer.lower()/'BASE/native/ega1').glob('ega1-*-fr.tex'):
  for n,fu in i_units(fp.read_text()).items():
   s=su[n];ff=refs(fu.text);ss=refs(s.text)
   for op,a,b,c,d in difflib.SequenceMatcher(None,[x[0] for x in ff],[x[0] for x in ss],autojunk=False).get_opcodes():
    if op=='equal':continue
    out.append({'layer':layer,'file':str(p.relative_to(RESULT)),'source':str(fp.relative_to(FR/layer.lower())),'place':n,'op':op,'fr':[x[3] for x in ff[a:b]],'es':[x[3] for x in ss[c:d]],'frpos':[x[1:3] for x in ff[a:b]],'espos':[x[1:3] for x in ss[c:d]],'fr_context':fu.text[max(0,ff[a][1]-80):ff[b-1][2]+100] if a<b else '', 'es_context':s.text[max(0,ss[c][1]-80):ss[d-1][2]+100] if c<d else ''})
(RESULT/'records/ROOT_REFERENCE_REVIEW.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('reference mismatch blocks',len(out))
for i,r in enumerate(out):
 if r['layer']=='CURRENT':print(i,r['place'],r['op'],r['fr'],r['es'])
