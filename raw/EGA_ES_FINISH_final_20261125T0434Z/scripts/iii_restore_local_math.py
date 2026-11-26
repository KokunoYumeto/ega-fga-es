#!/usr/bin/env python3
"""Restore corresponding one-formula source blocks between ordered common anchors.
The similarity score selects locations only; source literal text is restored.
Enum markers, source volume tokens and inequalities restated in words are held.
"""
import sys,re,json,difflib
from pathlib import Path
from audit_iii_alignment import *
TEXT={'pour ':'para ','pour tout ':'para todo ','si ':'si ','dans ':'en ','et':'y','par hypothèse, donc':'por hipótesis, por tanto','(resp. ':'(resp. ',')':')',' et ':' y ','(ou simplement ${}^{(e)}\\mathscr E(f_1,\\ldots,f_m;\n\\mathscr P_\\bullet^{(1)},\\ldots,\\mathscr P_\\bullet^{(m)})$)':'(o simplemente ${}^{(e)}\\mathscr E(f_1,\\ldots,f_m;\n\\mathscr P_\\bullet^{(1)},\\ldots,\\mathscr P_\\bullet^{(m)})$)'}
TEXT['sous-$A$-module de $\\mathrm H$.']='sub-$A$-módulo de $\\mathrm H$.'
TEXT.update({r'\emph{pour tout} ':r'\emph{para todo} ','ou':'o',r'(pour tout $n\in\mathbf Z$)':r'(para todo $n\in\mathbf Z$)','pour':'para','pour tout entier ':'para todo entero '})
def translate_math(s):
 ed=[]
 for m in re.finditer(r'\\(?:text|textup|mbox)\{',s):
  end=balanced_end(s,m.end()-1);t=s[m.end():end-1]
  if re.search('[A-Za-zÀ-ÿ]{2}',t):
   if t not in TEXT:raise ValueError(('unreviewed text',t))
   ed.append((m.end(),end-1,TEXT[t]))
 for a,b,n in reversed(ed):s=s[:a]+n+s[b:]
 return s

def punctuate(new,old,fafter,eafter):
 if new.startswith('$') and not new.startswith('$$') and not old.startswith('$'):
  mark=re.match(r'\s*([,.;:!?])',fafter);already=re.match(r'\s*([,.;:!?])',eafter)
  if mark and not already and re.search(r'[.,;:!?]\s*(?:\\\]|\\end\{[^}]+\})$',old):new+=mark[1]
 return new

def run(apply=False):
 report=[]
 for edition,part in [('current','1'),('diplomatic','1'),('current','6'),('current','7')]:
  f,e,b,p,g=compare(edition,part);ed=[]
  for q in g:
   if len(q['f'])!=1 or len(q['e'])!=1:continue
   a=q['f'][0];z=q['e'][0]
   if r'\mathbf{0}' in a or re.fullmatch(r'\$(?:[a-z]\)|\d\^\\circ)\$',a) or re.fullmatch(r'\$\\(?:leq?|geq?) [^$]+\$',a):continue
   k=weak(a).split('PRIMES')[0];l=weak(z).split('PRIMES')[0];score=difflib.SequenceMatcher(None,k,l,autojunk=False).ratio()
   if score<.60:continue
   if r'\text{' in z and r'\text{' not in a and (r'\sref' in z or r'\eqref' in z):continue
   if r'\text{(resp.' in a:continue
   lo,hi=q['epos'][0];fa,fb=q['fpos'][0];new=punctuate(translate_math(a),z,f[fb:],e[hi:])
   report.append(dict(edition=edition,part=part,place=q['place'],score=score,f=a,e=z,f_context=f[max(0,fa-120):fb+120],e_context=e[max(0,lo-120):hi+120]))
   ed.append((lo,hi,new,q['place'],z))
  if apply:apply_edits(edition,part,ed,b)
  print(edition,part,len(ed))
 (ROOT/'records/III_LOCAL_MATH_RESTORATIONS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':run('--apply' in sys.argv)
