"""Section-8-only alignment; leaves global IV3 reports/journals untouched."""
from iv38_tools import *
import argparse,collections
ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');ap.add_argument('--suffix',default='');args=ap.parse_args()
ft=FP.read_text();st=SP.read_text();fu=units(ft);su=units(st);edits=[];blocks=[];stats=[]
for un,f in fu.items():
 s=su[un];fm=core_spans(f.text);sm=core_spans(s.text);aligned=0
 for op,a,b,c,d in difflib.SequenceMatcher(None,[key(x.text) for x in fm],[key(x.text) for x in sm],autojunk=False).get_opcodes():
  if op=='equal' or op=='replace' and b-a==d-c==1:
   for i,j in zip(range(a,b),range(c,d)):
    new=retain_translated_text(fm[i].text,sm[j].text)
    if new is None:new=fm[i].text
    if new!=sm[j].text:
     if new.startswith('$') and not new.startswith('$$') and not sm[j].text.startswith('$'):
      fp=re.match(r'\s*([.,;:!?])',f.text[fm[i].end:]);sp=re.match(r'\s*([.,;:!?])',s.text[sm[j].end:])
      if fp and not sp:new+=fp.group(1)
     edits.append((s.start+sm[j].start,s.start+sm[j].end,new,un,'Literal supplied French formula restored after comparison; printed source takes precedence over inherited mathematical alteration.'))
    aligned+=1
  else:
   fa=fm[a].start if a<len(fm) else len(f.text);fb=fm[b-1].end if b>a else fa;sa=sm[c].start if c<len(sm) else len(s.text);sb=sm[d-1].end if d>c else sa
   blocks.append({'id':len(blocks),'place':un,'kind':op,'f_range':[f.start+fa,f.start+fb],'s_range':[s.start+sa,s.start+sb], 'french_math':' | '.join(x.text for x in fm[a:b]),'spanish_math':' | '.join(x.text for x in sm[c:d]),'french':f.text[max(0,fa-240):min(len(f.text),fb+240)],'spanish':s.text[max(0,sa-240):min(len(s.text),sb+240)]})
 stats.append([un,len(fm),len(sm),aligned])
if args.apply:apply(edits,'math'+args.suffix)
write('IV38_MATH_STATS'+args.suffix+'.tsv',['place','french_math','spanish_math','aligned'],stats)
(ROOT/('records/IV38_BLOCKS'+args.suffix+'.json')).write_text(json.dumps(blocks,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'source_spans':sum(x[1] for x in stats),'aligned':sum(x[3] for x in stats),'literal_changes':len(edits),'remaining_blocks':len(blocks),'kinds':dict(collections.Counter(x['kind'] for x in blocks))}))
