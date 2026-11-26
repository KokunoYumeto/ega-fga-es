"""Prepare model-review contexts for register; never infer a proof check."""
import re,json,difflib,collections
from corpus import FR,RESULT,ES,route
from tex_tools import numbered_units,math_spans,prose_segments,math_loose_key
from audit_i_ch1 import i_units,texts,mask_notes
from audit_iv4 import pairs as iv4_pairs
PAT=re.compile(r'\b(?:no[s]?\s+(?:reducimos|reduciremos|limitamos|limitaremos|restringimos|restringiremos)|hemos\s+(?:visto|demostrado|probado|definido|señalado)|podemos|podremos|tenemos|tendremos|vemos|veremos|sabemos|sabremos|obtenemos|obtendremos|concluimos|concluiremos|deducimos|deduciremos|decimos|diremos|denotamos|denotaremos|designamos|designaremos|llamamos|llamaremos|consideramos|consideraremos|observamos|observaremos|notamos|notaremos|suponemos|supondremos|ponemos|pondremos|tomamos|tomaremos|definimos|definiremos|comprobamos|comprobaremos|aplicamos|aplicaremos|encontramos|encontraremos|identificamos|identificaremos|escribimos|escribiremos|mostramos|mostraremos|demostramos|demostraremos|utilizamos|utilizaremos|debemos|deberemos|queremos|buscamos|haremos|hacemos|supóngase|considérese|obsérvese|elíjase|tómese|póngase)\b',re.I)

def contexts(ft,st):
 ff=math_spans(mask_notes(ft));ss=math_spans(mask_notes(st));links={}
 for block in difflib.SequenceMatcher(None,[math_loose_key(x.text) for x in ff],[math_loose_key(x.text) for x in ss],autojunk=False).get_matching_blocks():
  for j in range(block.size):links[block.b+j]=block.a+j
 for a,b,prose in prose_segments(mask_notes(st)):
  for m in PAT.finditer(prose):
   start=a+m.start();end=a+m.end();before=[i for i in links if ss[i].end<=start];after=[i for i in links if ss[i].start>=end]
   prev=max(before,default=None);nxt=min(after,default=None)
   fs=ff[links[prev]].end if prev is not None else 0;fe=ff[links[nxt]].start if nxt is not None else len(ft)
   fc=ft[fs:fe]
   yield start,end,m.group(),fc,st[max(0,start-90):min(len(st),end+140)]

def main():
 out=[]
 for layer in ['CURRENT','DIPLOMATIC']:
  p,t=texts(layer);su=i_units(t)
  for fp in sorted((FR/layer.lower()/'BASE/native/ega1').glob('ega1-*-fr.tex')):
   for num,fu in i_units(fp.read_text()).items():
    if num not in su:continue
    for a,b,word,fc,sc in contexts(fu.text,su[num].text):out.append({'scope':'I','layer':layer,'file':str(p.relative_to(RESULT)),'source':str(fp.relative_to(FR/layer.lower())),'place':num,'before':word,'fr':fc,'es':sc,'unit_position':a,'unit_end':b})
 idx=collections.defaultdict(list)
 for p in (ES/'worktree/es/PORTED_20261109/IV4/ega4').rglob('*.tex'):
  t=p.read_text()
  for n,u in numbered_units(t).items():idx[n].append((p,u))
 for fp,ft,st in iv4_pairs():
  for num,fu in numbered_units(ft).items():
   cand=idx.get(num,[])
   if 'errata' in fp.name:cand=[(p,u) for p,u in cand if 'errata' in p.name]
   else:cand=[(p,u) for p,u in cand if 'errata' not in p.name]
   if len(cand)!=1:continue
   p,su=cand[0]
   for a,b,word,fc,sc in contexts(fu.text,su.text):out.append({'scope':'IV4','layer':'CURRENT','file':str(p.relative_to(RESULT)),'source':str(fp.relative_to(FR/'current')),'place':num,'before':word,'fr':fc,'es':sc,'unit_position':a,'unit_end':b})
 (RESULT.parent/'tmp/register_review.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
 print('Total',len(out),collections.Counter(x['scope'] for x in out))
 for i,x in enumerate(out):
  if x['scope']=='I' and x['layer']=='DIPLOMATIC':continue
  if re.search(r'\bon\b',x['fr'],re.I) and not re.search(r'\bnous\b',x['fr'],re.I):print(i,x['scope'],x['place'],x['before'],'FR:',re.sub(r'\s+',' ',x['fr'])[:230],'ES:',re.sub(r'\s+',' ',x['es'])[:170])
if __name__=='__main__':main()
