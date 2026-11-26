#!/usr/bin/env python3
"""Restore schéma/préschéma in one-to-one source-aligned prose intervals.

Formulas must first be in identical French order. Intervals are the prose
between two consecutive matched formulas within one numbered source unit.
Only equal-count term streams are paired; unequal counts are held for reading.
"""
from iii_register_candidates import *
import hashlib,csv
F=re.compile(r'\b(?:sous-)?(?:pré)?schémas?\b',re.I)
E=re.compile(r'\b(?:sub)?(?:pre)?esquemas?\b',re.I)
def render(s):
 t=('sub' if s.lower().startswith('sous-') else '')+('pre' if 'pré' in s.lower() else '')+'esquema'+('s' if s.lower().endswith('s') else '')
 return t
def run():
 records=[];held=[]
 for ed,part in [('current','1'),('diplomatic','1'),('current','6'),('current','7')]:
  f,e,b,p,g=compare(ed,part);assert not g;changes=[]
  for x in segments(ed,part):
   fm=list(F.finditer(x['f']));em=list(E.finditer(x['e']))
   if len(fm)!=len(em):
    if fm or em:held.append(dict(id=x['id'],f=x['f'],e=x['e'],f_terms=[m[0] for m in fm],e_terms=[m[0] for m in em]))
    continue
   new=x['e']
   for a,z in reversed(list(zip(fm,em))):
    term=render(a[0]);term=term.capitalize() if z[0][0].isupper() else term
    if term==z[0]:continue
    new=new[:z.start()]+term+new[z.end():]
    records.append(dict(id=x['id'],french_term=a[0],before=z[0],after=term,source_sha256=hashlib.sha256(x['f'].encode()).hexdigest(),reason='Same-count ordered term occurrences between identical French formulas; prefix and number follow source'))
   if new!=x['e']:changes.append((x['estart'],x['eend'],new,x['place'],x['e']))
  if changes:apply_edits(ed,part,changes,b)
  print(ed,part,'changes',len(changes))
 (ROOT/'records/III_SCHEMA_DECISIONS.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'records/III_SCHEMA_HELD.json').write_text(json.dumps(held,ensure_ascii=False,indent=2)+'\n')
 print('term occurrences changed',len(records),'held intervals',len(held))
if __name__=='__main__':run()
