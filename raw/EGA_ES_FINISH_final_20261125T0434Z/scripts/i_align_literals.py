"""Align the same source formula within each I unit, allowing Spanish word order."""
import re,json,collections,difflib
from corpus import RESULT,FR,write_tsv
from audit_i_ch1 import texts,i_units,mask_notes
from tex_tools import math_spans,math_loose_key,retain_translated_text

def main():
 edits=collections.defaultdict(list);changes=[];gaps=[];stats=[]
 for layer in ['CURRENT','DIPLOMATIC']:
  p,t=texts(layer);su=i_units(t)
  for fp in sorted((FR/layer.lower()/'BASE/native/ega1').glob('ega1-*-fr.tex')):
   for num,fu in i_units(fp.read_text()).items():
    eu=su[num];ff=math_spans(mask_notes(fu.text));ss=math_spans(mask_notes(eu.text));fk=[math_loose_key(x.text) for x in ff];sk=[math_loose_key(x.text) for x in ss]
    pairs=[];usedf=set();useds=set()
    for block in difflib.SequenceMatcher(None,fk,sk,autojunk=False).get_matching_blocks():
     for i in range(block.size):pairs.append((block.a+i,block.b+i));usedf.add(block.a+i);useds.add(block.b+i)
    for a,k in enumerate(fk):
     if a in usedf:continue
     candidates=[i for i,x in enumerate(sk) if i not in useds and x==k]
     if candidates:
      b=min(candidates,key=lambda b:abs(a-b));pairs.append((a,b));usedf.add(a);useds.add(b)
    for a,b in pairs:
     f,s=ff[a],ss[b];new=retain_translated_text(f.text,s.text)
     if new is None:continue
     # Whitespace differences alone carry no content and need no edit.
     if re.sub(r'\s+','',new)==re.sub(r'\s+','',s.text):continue
     after=re.match(r'\s*([.,;:!?])',fu.text[f.end:]);oldafter=re.match(r'\s*([.,;:!?])',eu.text[s.end:])
     if f.kind=='inline' and s.kind!='inline' and after and not oldafter:new+=after[1]
     edits[p].append((eu.start+s.start,eu.start+s.end,new));changes.append([str(p.relative_to(RESULT)),num,s.text,new,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/'+layer.lower()+'/'+str(fp.relative_to(FR/layer.lower()))+': '+num+'; same formula in source/translation'])
    uf=[i for i in range(len(ff)) if i not in usedf];us=[i for i in range(len(ss)) if i not in useds]
    if uf or us:gaps.append({'layer':layer,'source':str(fp.relative_to(FR/layer.lower())),'place':num,'fr':[ff[i].text for i in uf],'es':[ss[i].text for i in us],'fpos':[(ff[i].start,ff[i].end) for i in uf],'epos':[(ss[i].start,ss[i].end) for i in us],'fr_contexts':[fu.text[max(0,ff[i].start-130):min(len(fu.text),ff[i].end+180)] for i in uf],'es_contexts':[eu.text[max(0,ss[i].start-130):min(len(eu.text),ss[i].end+180)] for i in us]})
    stats.append([layer,fp.name,num,len(ff),len(ss),len(pairs)])
 for p,ee in edits.items():
  t=p.read_text()
  for a,b,new in sorted(ee,reverse=True):t=t[:a]+new+t[b:]
  p.write_text(t)
 log=RESULT/'records/CAMBIOS_i_aligned_literal.tsv';counter=1
 while log.exists():counter+=1;log=RESULT/f'records/CAMBIOS_i_aligned_literal_{counter}.tsv'
 write_tsv(log,['file','place','before','after','kind','source'],changes)
 write_tsv(RESULT/'records/I_CH1_FORMULA_COVERAGE.tsv',['edition','source','unit','french_math','spanish_core_math','aligned'],stats)
 (RESULT.parent/'tmp/i/gaps_by_unit.json').write_text(json.dumps(gaps,ensure_ascii=False,indent=2))
 print('literal changes',len(changes),'units with unmatched formulas',len(gaps))
 for i,g in enumerate(gaps):
  if g['layer']=='CURRENT':print(i,g['place'],str(g['fr'])[:300],str(g['es'])[:300])
if __name__=='__main__':main()
