"""Source-bound proposals for IV3 §§8–9; applying owner checks context binding."""
import json,re
from corpus import FR,ES,RESULT
from tex_tools import numbered_units
from register_review import contexts
from register_forms import BASE
IMP=r'\b(?:nous|supposons|montrons|prouvons|démontrons|considérons|prenons|posons|notons|remarquons|rappelons|choisissons|utilisons|appliquons|définissons|désignons|écrivons|distinguons|cherchons|raisonnons|représentons|observons)\b'
rows=[]
for n in ['8','9']:
 fp=FR/'current/IV3/native/ega4'/f'ega4-{n}-fr.tex';p=ES/'worktree/es/PORTED_20261109/IV3/sections'/f'ega4-{n}.tex';st=p.read_text();su=numbered_units(st)
 for num,fu in numbered_units(fp.read_text()).items():
  if num not in su:continue
  u=su[num]
  for a,b,word,fc,sc in contexts(fu.text,u.text):
   pure=re.search(r'\bon\b',fc,re.I) and not re.search(IMP,fc,re.I) and len(fc)<700
   new=BASE.get(word.lower()) if pure else None
   if new and word[0].isupper():new=new[0].upper()+new[1:]
   if new:
    cm=re.search(r'\b(lo|la|los|las)\s+$',u.text[:a])
    if cm:a=cm.start();new=re.sub(r'^[Ss]e ',lambda m:m[0]+cm[1]+' ',new)
   rows.append({'file':str(p.relative_to(RESULT)),'place':num,'source':str(fp.relative_to(FR/'current')),'before':u.text[a:b],'after':new,'prefix':u.text[max(0,a-100):a],'suffix':u.text[b:min(len(u.text),b+150)],'source_context':fc,'spanish_context':sc,'decision':'source on: provisional impersonal form' if new else 'model review: authors nous/imperative or unaligned prose'})
path=RESULT/'records/IV3_REGISTER_89_PROPOSALS.json';path.write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('Candidates',len(rows),'proposed',sum(bool(r['after']) for r in rows))
for i,r in enumerate(rows):
 if not r['after']:print(i,r['place'],r['before'],'FR',re.sub(r'\s+',' ',r['source_context'])[:400],'ES',re.sub(r'\s+',' ',r['spanish_context'])[:180])
