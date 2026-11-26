#!/usr/bin/env python3
"""Targeted typography and register corrections checked against the corresponding French units."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import reconcile_iv2 as r
BOTH=[
('ega4-2_5.13.3_5.13.4_ES','5.13.4',r'unirramosos\textup{)}',r'unirramosos)'),
('ega4-2_5.13.3_5.13.4_ES','5.13.4',r'unirramoso\textup{)}',r'unirramoso)'),
('ega4-2_6.1.3_6.1.4_ES','6.1.3',r'plano\textup{)}',r'plano)'),
('ega4-2_6.7.5_ES','6.7.5',r'en \textup{(i)}',r'en (i)'),
('ega4-2_6.14.1_proof_II_b_ES','6.14.1',r'anillo \emph{local} (evidentemente',r'anillo local (evidentemente'),
('ega4-2_7.2.10_ES','7.2.10','ni, con mayor razón, estrictamente','ni, \\emph{con mayor razón}, estrictamente'),
('ega4-2_7.2.10_ES','7.2.10','Tampoco se sabe si, en las condiciones equivalentes','Ignoramos asimismo si, en las condiciones equivalentes'),
('ega4-2_7.3.16_ES','7.3.16','Supongamos que la propiedad','Se supone que la propiedad'),
('ega4-2_7.3.16_ES','7.3.16','del segundo tipo, suponemos además','del segundo tipo, se supone además'),
]
def main():
 for layer in ['CURRENT','DIPLOMATIC']:
  suff='.tex' if layer=='CURRENT' else '.diplomatic.tex'
  for name,place,before,after in BOTH:
   file='tree/worktree/es/'+layer+'/EGA_IV2/'+name+suff
   text=(r.ROOT/file).read_text()
   if before in text and text.count(before)>1:
    # Restrict identical closing-brace corrections to the full containing line.
    lo=text.index(before);i=text.rfind('\n',0,lo)+1;j=text.find('\n',lo)
    b=text[i:j];r.change(file,place,b,b.replace(before,after,1),'standard','standard/NOTATION_EGA.md §6; French IV.'+place)
   elif before in text:r.change(file,place,before,after,'standard','standard/STANDARDS_20261119b.md: register and emphasis; French IV.'+place)
   elif after not in text:print('NEEDS EXACT PREIMAGE',file,repr(before))
 r.change('tree/worktree/es/CURRENT/EGA_IV2/ega4-2_7.2.7_ES.tex','7.2.7','satisfacen con\nmayor razón','satisfacen \\emph{con\nmayor razón}','standard','standard/NOTATION_EGA.md §6; French IV.7.2.7')
 r.change('tree/worktree/es/CURRENT/EGA_IV2/ega4-2_7.3.16_ES.tex','7.3.16',"$B$ de $A$\n(resp. toda", "$B$ de $A$\n\\textup{(resp.} toda",'standard','standard/NOTATION_EGA.md §6; French IV.7.3.16')
if __name__=='__main__':main()
