"""EGA II source-fidelity helpers; source files are supplied separately."""
from pathlib import Path
import re,csv,difflib
from tex_tools import Span,math_spans,math_loose_key,balanced_end,retain_translated_text
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT.parent/'source/EGA_ES_FINISH_1_FRANCES/fr'
NAMES={'front':'front-fr.tex','main':'ega2-1-fr.tex','bibliography':'ega2-bibliography-fr.tex','indexes':'ega2-indexes-and-contents-fr.tex','errata':'ega2-errata-addenda-fr.tex'}
def espath(ed):return ROOT/'tree/repo/editions'/('II_'+ed.upper())/('EGA_II_es_'+ed+'.tex')
def frpath(ed,part):return SRC/ed/'BASE/native/ega2'/NAMES[part]
def parts(t):
 a=t.index('% EGA II SOURCE FRONT MATTER') if '% EGA II SOURCE FRONT MATTER' in t else t.index(r'\section*{Sumario}');b=t.index(r'\section{Morfismos afines}')
 c=t.index(r'\clearpage',t.index(r'\begin{proposition}[8.14.14]'))
 d=t.index(r'\clearpage',t.index(r'\end{thebibliography}',c))
 e=t.index(r'\oldpage[II]{217}',d)
 # Include errata page-setup controls, but no preceding index prose.
 f=t.index(r'\end{document}',e)
 return {k:Span(i,j,t[i:j],k) for k,i,j in [('front',a,b),('main',b,c),('bibliography',c,d),('indexes',d,e),('errata',e,f)]}
UNIT_RE=re.compile(r'\\begin\{([^}]+)\}\[([\d.]+)\]|\\par\\medskip\\noindent\\textit\{(?:Remarques|Observaciones) \(([\d.]+)\)\. ---\\ \}')
def units(t):
 ms=list(UNIT_RE.finditer(t));out={}
 if not ms:return {'PRE':Span(0,len(t),t,'unnumbered')}
 if ms[0].start():out['PRE']=Span(0,ms[0].start(),t[:ms[0].start()],'unnumbered')
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else len(t)
  out[m.group(2) or m.group(3)]=Span(m.start(),end,t[m.start():end],m.group(1) or 'manualremarks')
 return out
def write(name,header,rows):
 with (ROOT/'records'/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(header);w.writerows(rows)
def read(name):return list(csv.DictReader((ROOT/'records'/name).open(),delimiter='\t'))
HEADER=['file','place','before','after','kind','source']
def apply_edits(t,edits):
 last=len(t)+1
 for a,b,z in sorted(edits,reverse=True):
  assert b<=last,(a,b,last);t=t[:a]+z+t[b:];last=a
 return t
def source_note(ed,part,key):return 'EGA_ES_FINISH_1_FRANCES/fr/'+ed+'/BASE/native/ega2/'+NAMES[part]+': '+key
def key(t):
 # Alignment-only: recognize inherited TeX aliases before stripping whitespace.
 t=t.replace(r'\dots',r'\ldots').replace(r'\cdots',r'\ldots').replace(r'\leqslant',r'\leq').replace(r'\geqslant',r'\geq').replace(r'\ne ',r'\neq ')
 t=re.sub(r'\\supertilde(?![A-Za-z])',r'^{\\sim}',t)
 t=re.sub(r'\\dual\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}',r'\\check{\1}',t)
 return math_loose_key(t)
def stripmath(t):
 for s in reversed(math_spans(t)):t=t[:s.start]+' '+t[s.end:]
 t=re.sub(r'(?<!\\)%[^\n]*','',t)
 return t
def words(t):return len(re.findall(r'[A-Za-zÀ-ÿ]+(?:[-’\'][A-Za-zÀ-ÿ]+)*',re.sub(r'\\[A-Za-z]+',' ',stripmath(t))))
