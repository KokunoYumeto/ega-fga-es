"""Final literal restoration for source-aligned IV4 core formulas."""
import re,json,difflib,collections
from corpus import RESULT,ES,FR,write_tsv
from tex_tools import numbered_units,math_spans,math_loose_key,retain_translated_text
from audit_iv4 import FILES,mask_footnotes

def main():
 sources={};idx=collections.defaultdict(list)
 for n in FILES:
  fp=FR/'current/IV4/native/ega4'/f'ega4-{n}-fr.tex'
  for num,fu in numbered_units(fp.read_text()).items():sources[('errata' in fp.name,num)]=(fp,fu)
 edits=collections.defaultdict(list);changes=[];unmatched=[]
 for p in (ES/'worktree/es/PORTED_20261109/IV4/ega4').rglob('*.tex'):
  t=p.read_text()
  for num,su in numbered_units(t).items():
   key=('errata' in p.name,num)
   if key not in sources:continue
   fp,fu=sources[key];ff=math_spans(mask_footnotes(fu.text));ss=math_spans(mask_footnotes(su.text))
   for block in difflib.SequenceMatcher(None,[math_loose_key(x.text) for x in ff],[math_loose_key(x.text) for x in ss],autojunk=False).get_matching_blocks():
    for j in range(block.size):
     f,s=ff[block.a+j],ss[block.b+j];new=retain_translated_text(f.text,s.text)
     if new is None:unmatched.append([p.name,num,f.text,s.text]);continue
     if re.sub(r'\s+','',new)==re.sub(r'\s+','',s.text):continue
     after=re.match(r'\s*([.,;:!?])',fu.text[f.end:]);oldafter=re.match(r'\s*([.,;:!?])',su.text[s.end:])
     if f.kind=='inline' and s.kind!='inline' and after and not oldafter:new+=after[1]
     edits[p].append((su.start+s.start,su.start+s.end,new));changes.append([str(p.relative_to(RESULT)),num,s.text,new,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/current/'+str(fp.relative_to(FR/'current'))+': '+num+'; exact source formula'])
 for p,ee in edits.items():
  t=p.read_text()
  for a,b,new in sorted(ee,reverse=True):t=t[:a]+new+t[b:]
  p.write_text(t)
 write_tsv(RESULT/'records/CAMBIOS_iv4_final_literals.tsv',['file','place','before','after','kind','source'],changes)
 write_tsv(RESULT/'records/IV4_FORMULA_TEXT_PENDING.tsv',['file','place','french','spanish'],unmatched)
 print('Restored',len(changes),'text-pending',len(unmatched))
if __name__=='__main__':main()
