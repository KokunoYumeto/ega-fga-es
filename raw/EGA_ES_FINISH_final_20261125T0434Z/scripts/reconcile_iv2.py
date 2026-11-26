#!/usr/bin/env python3
"""Reproducible IV-2 corrections and source-formula reconciliation.
Run after expanding the supplied archives in ../source. The source layers are read only.
"""
from pathlib import Path
import sys,re,csv,json,collections,difflib
sys.path.insert(0,str(Path(__file__).resolve().parent))
import audit_iv2_alignment as a
ROOT=a.ROOT;SRC=a.SOURCE;ES=a.ES
HEADERS={'CAMBIOS':['file','place','before','after','kind','source'], 'TRADUCCION':['file','french_source','range','words'], 'CHECK_EVENTS':['statement_id','date','who','type','outcome'], 'HECHO_REVISADO':['id','file','place','verdict','reason'], 'GLOSARIO_REGISTRO':['french_term','spanish_rendering','witness','places','reversible']}
for kind,header in HEADERS.items():
 p=ROOT/'records'/f'{kind}_iv2.tsv'
 if not p.exists():
  with p.open('w') as out: csv.writer(out,delimiter='\t').writerow(header)

def log(kind,row):
 with (ROOT/'records'/f'{kind}_iv2.tsv').open('a') as out:csv.writer(out,delimiter='\t').writerow(row)

def change(file,place,before,after,kind='own comparison',source=None):
 p=ROOT/file;txt=p.read_text()
 if before==after:return False
 n=txt.count(before)
 if n!=1:
  if after in txt:return False
  raise ValueError(f'Expected single preimage in {file}, {place}: {n}')
 p.write_text(txt.replace(before,after,1))
 log('CAMBIOS',[file,place,before,after,kind,source or 'EGA_ES_FINISH_1_FRANCES/fr/current/IV2/native/ega4/ega4-2-fr.tex, IV.'+place])
 return True

MANUAL=[
('ega4-2_opening_through_2.1.3_ES.tex','2.1.2',r'el morfismo correspondiente y $M$',r'el morfismo correspondiente a $\varphi$ y $M$'),
('ega4-2_opening_through_2.1.3_ES.tex','2.1.3',r'\sref[0\textsubscript{I}]{0.6.3.3}',r'$(\mathbf{0}_{\mathrm I},6.3.3)$'),
('ega4-2_4.8.1_4.8.4_ES.tex','4.8.4',r'del conjunto de partida de $\varepsilon_{K_1,K}$',r'del conjunto de llegada de $\varepsilon_{K,K\prime}$'),
('ega4-2_6.7.5_ES.tex','6.7.5','y $a$, $b$ dos elementos\nde $k$ que forman una familia $p$-libre', 'y $a$, $b$ que forman una familia $p$-libre'),
('ega4-2_6.14.4_proof_III_ES.tex','6.14.4','dominios enteros integralmente cerrados $A\'_i$, cuyos cuerpos de\nfracciones $K\'_i$ son extensiones', 'dominios enteros integralmente cerrados $A\'_i$, siendo los cuerpos de\nfracciones $K\'_i$ de los $A\'_i$ extensiones'),
('ega4-2_6.14.4_proof_IV_ES.tex','6.14.4','noetheriana geométricamente normal y, por tanto, un producto directo\nde dominios enteros.', "noetheriana geométricamente normal y, por tanto, $B'$ es un producto directo\nde dominios enteros."),
('ega4-2_6.15.2_example_ES.tex','6.15.2','la clausura integral de $A$;\npor tanto, $A$ es unirramoso', 'la clausura integral de $A$,\nque es, por tanto, unirramoso'),
('ega4-2_7.2.5_proof_step_I_ES.tex','7.2.5',r'dos etapas, con $n\geqslant1$.',r'dos etapas, siendo $n$ $\geqslant1$.'),
('ega4-2_7.2.5_proof_step_II_ES.tex','7.2.5',"La imagen recíproca de la fibra $u^{-1}(x)$ por la proyección\n$X'_1\\to X'$", "La imagen recíproca por la proyección\n$X'_1\\to X'$ de la fibra $u^{-1}(x)$"),
]

def manual():
 for name,place,before,after in MANUAL:change('tree/worktree/es/CURRENT/EGA_IV2/'+name,place,before,after)
 # The exact-source formula will replace this temporary lexical spelling in the next pass.
 change('tree/worktree/es/CURRENT/EGA_IV2/ega4-2_4.8.1_4.8.4_ES.tex','4.8.4',r'$\varepsilon_{K,K\prime}$',"$\\varepsilon_{K,K'}$")

TEXT_MAP={' et ':' y ','avec ':'con ','pour ':'para ','et':'y'}
def translated_math(f):
 return re.sub(r'\\text\{([^{}]*)\}',lambda m:r'\text{'+TEXT_MAP.get(m[1],m[1])+'}',f)

def apply_span_edits(layer,edits,bounds):
 grouped=collections.defaultdict(list)
 for lo,hi,new,place,old,source in edits:
  owner=next((z for z in bounds if z[0]<=lo and hi<=z[1]),None)
  if not owner:raise ValueError('Edit crosses input-unit boundary')
  start,end,path=owner;grouped[path].append((lo-start,hi-start,new,place,old,source))
 for file,items in grouped.items():
  path=ROOT/file;text=path.read_text()
  last=len(text)+1
  for lo,hi,new,place,old,source in sorted(items,reverse=True):
   assert hi<=last,(file,place,'overlap')
   assert text[lo:hi]==old,(file,place,'preimage')
   text=text[:lo]+new+text[hi:];last=lo
   log('CAMBIOS',[file,place,old,new,'own comparison',source])
  path.write_text(text)
 return sum(map(len,grouped.values()))

def restore_math(layer='CURRENT',include_gaps=True):
 f,e,bounds,paired,gaps=a.compare(layer)
 edits=[]
 src='EGA_ES_FINISH_1_FRANCES/fr/'+layer.lower()+'/IV2/native/ega4/ega4-2-fr.tex'
 for q in paired:
  expected=translated_math(q['f'])
  if expected!=q['e']:
   new=expected
   if expected.startswith('$') and q['e'].startswith('\\['):
    # A display inserted by the earlier build moved the sentence punctuation inside it.
    after=re.match(r'\s*([,.;:])',f[q['fend']:])
    already=re.match(r'\s*([,.;:])',e[q['eend']:])
    if after and not already:new+=after[1]
   edits.append((q['estart'],q['eend'],new,q['place'],q['e'],src+', IV.'+q['place']))
 if include_gaps:
  for q in gaps:
   if q['fcount']==q['ecount']:
    for fm,em,fp,ep in zip(q['f'],q['e'],q['fpos'],q['epos']):
     new=translated_math(fm)
     if fm.startswith('$') and em.startswith('\\['):
      after=re.match(r'\s*([,.;:])',f[fp[1]:]);already=re.match(r'\s*([,.;:])',e[ep[1]:])
      if after and not already:new+=after[1]
     edits.append((ep[0],ep[1],new,q['place'],em,src+', IV.'+q['place']))
   elif q['fcount']==0 and all(re.fullmatch(r'\$[012]\$',s) for s in q['e']):
    # French prints these isolated prose numerals outside math mode.
    for em,ep in zip(q['e'],q['epos']):edits.append((ep[0],ep[1],em[1:-1],q['place'],em,src+', IV.'+q['place']+'; prose numeral'))
 print(layer,'math edits',apply_span_edits(layer,edits,bounds))

def restore_structural(layer='CURRENT'):
 f=(a.FR/layer.lower()/'IV2/native/ega4/ega4-2-fr.tex').read_text();e,bounds=a.aggregate(layer)
 edits=[]
 for name,pattern in [('label',r'\\label\{[^}]*\}'),('EGAReaderTarget',r'\\EGAReaderTarget\{[^}]*\}\{[^}]*\}')]:
  fm=list(re.finditer(pattern,f));em=list(re.finditer(pattern,e));assert len(fm)==len(em),(layer,name,len(fm),len(em))
  for u,v in zip(fm,em):
   if u[0]!=v[0]:edits.append((v.start(),v.end(),u[0],name,v[0],'standard/NOTATION_EGA.md §6; French IV2 '+name))
 print(layer,'label edits',apply_span_edits(layer,edits,bounds))
 if layer=='CURRENT':
  name='tree/worktree/es/CURRENT/EGA_IV2/ega4-2_opening_through_2.1.3_ES.tex'
  change(name,'2.1',r'\subsection{Módulos planos sobre los preesquemas.}',r'\setcounter{subsection}{0}'+'\n'+r'\subsection{Módulos planos sobre los preesquemas.}','standard','standard/NOTATION_EGA.md §6')

if __name__=='__main__':
 task=sys.argv[1] if len(sys.argv)>1 else 'current'
 if task=='current':manual();restore_math();restore_structural()
 elif task=='diplomatic':restore_math('DIPLOMATIC');restore_structural('DIPLOMATIC')
