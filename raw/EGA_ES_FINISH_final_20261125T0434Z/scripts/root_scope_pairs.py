"""Read-only source/Spanish pairings and source-file offsets for released scopes."""
import re,json
from corpus import RESULT,ES,FR
from tex_tools import numbered_units,Span
from audit_i_ch1 import texts,i_units
from audit_iv4 import pairs as iv4pairs,PROJECT
from assemble_readers import source_join

def scoped_units(t,fn=numbered_units):
 u=fn(t)
 if not u:return {'whole':Span(0,len(t),t,'whole')}
 a=min(x.start for x in u.values())
 if a:u={'prelude':Span(0,a,t[:a],'prelude'),**u}
 return u

def pairs():
 for ed in ['current','diplomatic']:
  layer=ed.upper();p,t=texts(layer)
  for fp in sorted((FR/ed/'BASE/native/ega1').glob('ega1-*-fr.tex')):yield 'I',ed,fp,fp.read_text(),t,p,0,i_units
  fp=FR/ed/'BASE/native/ega1/ega0-1-fr.tex';files=sorted((ES/f'worktree/es/{layer}/EGA_I_ch0').glob('ega0_i_*.tex'),key=lambda p:list(map(int,re.findall(r'\d+',p.stem))))
  yield 'I0',ed,fp,fp.read_text(),source_join(files),None,0,numbered_units
  for fp in sorted((FR/ed/'IV1/native/ega4').glob('ega0-*-fr.tex')):
   p=ES/f'worktree/es/PORTED_20261109/IV1_{layer}/ega4'/fp.name.replace('-fr.tex','-es.tex');yield 'IV1_0',ed,fp,fp.read_text(),p.read_text(),p,0,numbered_units
  for scope,src,orderfile in [('IV1_1','IV1/native/ega4/ega4-1-fr.tex','IV1_CH4_INPUT_ORDER.json'),('IV2','IV2/native/ega4/ega4-2-fr.tex','IV2_INPUT_ORDER.json')]:
   o=json.load(open(RESULT/'records'/orderfile));o=o if isinstance(o,list) else o[layer];fp=FR/ed/src
   yield scope,ed,fp,fp.read_text(),source_join([RESULT/x for x in o]),None,0,numbered_units
  from ii_tools import parts,units,espath,frpath
  p=espath(ed)
  for name,sp in parts(p.read_text()).items():
   if name=='bibliography':continue
   fp=frpath(ed,name);yield 'II:'+name,ed,fp,fp.read_text(),sp.text,p,sp.start,units
 for fp,ft,st in iv4pairs():yield 'IV4','current',fp,ft,st,PROJECT/'ega4'/fp.name.replace('-fr.tex','-es.tex'),0,numbered_units

def resolve(st,pos,fallback,offset=0):
 stack=[]
 for m in re.finditer(r'(?m)^% (BEGIN|END) (tree/[^\n]+)\n?',st[:pos+1]):
  if m[1]=='BEGIN':stack.append((RESULT/m[2],m.end()))
  elif stack:stack.pop()
 if stack:
  p,start=stack[-1];off=pos-start
  assert p.read_text()[max(0,off-30):off+30]==st[max(start,pos-30):pos+30],(p.name,off)
  return p,off
 assert fallback is not None
 return fallback,pos+offset
