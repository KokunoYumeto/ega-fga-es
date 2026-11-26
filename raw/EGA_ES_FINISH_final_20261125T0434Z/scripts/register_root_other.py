"""Source-bounded register review for chapter-zero material and front matter."""
import re,json,collections,difflib
from corpus import RESULT,ES,FR,write_tsv
from tex_tools import numbered_units,Span,math_spans
from register_review import contexts
from register_forms import BASE
IMP=r'\b(?:nous|supposons|montrons|prouvons|démontrons|considérons|prenons|posons|notons|remarquons|rappelons|choisissons|utilisons|appliquons|définissons|désignons|écrivons|distinguons|cherchons|raisonnons|représentons|observons|voyons|examinons|traitons|admettons|appelons)\b'
def units(t):
 u=numbered_units(t)
 if u:
  a=min(x.start for x in u.values())
  if a:u={'intro':Span(0,a,t[:a],'intro'),**u}
 else:u={'whole':Span(0,len(t),t,'whole')}
 return u

def generate(target="REGISTER_ROOT_OTHER_REVIEW.json"):
 out=[]
 for layer in ['CURRENT','DIPLOMATIC']:
  fp=FR/layer.lower()/'BASE/native/ega1/ega0-1-fr.tex';fu=units(fp.read_text())
  for p in sorted((ES/f'worktree/es/{layer}/EGA_I_ch0').glob('ega0_i_*.tex')):
   for n,su in units(p.read_text()).items():
    if n not in fu or n=='intro':continue
    for a,b,word,fc,sc in contexts(fu[n].text,su.text):out.append({'scope':'I0','layer':layer,'file':str(p.relative_to(RESULT)),'source':str(fp.relative_to(FR/layer.lower())),'place':n,'before':word,'fr':fc,'es':sc,'position':su.start+a,'end':su.start+b})
  for fp in sorted((FR/layer.lower()/'IV1/native/ega4').glob('ega0-*-fr.tex')):
   p=ES/f'worktree/es/PORTED_20261109/IV1_{layer}/ega4'/fp.name.replace('-fr.tex','-es.tex');su=units(p.read_text())
   for n,fu in units(fp.read_text()).items():
    if n not in su:continue
    for a,b,word,fc,sc in contexts(fu.text,su[n].text):out.append({'scope':'IV1_0','layer':layer,'file':str(p.relative_to(RESULT)),'source':str(fp.relative_to(FR/layer.lower())),'place':n,'before':word,'fr':fc,'es':sc,'position':su[n].start+a,'end':su[n].start+b})
 for r in out:
  pure=re.search(r'\bon\b',r['fr'],re.I) and not re.search(IMP,r['fr'],re.I) and len(r['fr'])<700
  r['after']=BASE.get(r['before'].lower()) if pure else None
 (RESULT/'records'/target).write_text(json.dumps(out,ensure_ascii=False,indent=2))
 print('candidates',len(out),collections.Counter(r['scope'] for r in out),'pure',sum(r['after'] is not None for r in out))
 for i,r in enumerate(out):
  if r['layer']=='DIPLOMATIC':continue
  if r['after'] is not None and r['before'].lower() not in ['podemos','tenemos','nos reducimos','hemos visto','vemos','veremos','podremos']:
   print('PURE',i,r['scope'],r['place'],r['before'],'FR',re.sub(r'\s+',' ',r['fr'])[:270],'ES',re.sub(r'\s+',' ',r['es'])[:220])
  elif r['after'] is None and re.search(r'\bon\b',r['fr'],re.I):
   print('MIXED',i,r['scope'],r['place'],r['before'],'FR',re.sub(r'\s+',' ',r['fr'])[:370],'ES',re.sub(r'\s+',' ',r['es'])[:230])
if __name__=='__main__':generate()
