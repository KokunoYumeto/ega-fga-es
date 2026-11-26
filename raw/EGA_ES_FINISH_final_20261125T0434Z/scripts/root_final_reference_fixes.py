"""Reviewed source reference targets and mathematical text arguments."""
import re,collections
from corpus import RESULT,ES,write_tsv
from audit_i_ch1 import texts,i_units
from tex_tools import balanced_end
changes=[]
for layer in ['CURRENT','DIPLOMATIC']:
 p,t=texts(layer);full=p.read_text();edits=[]
 for n,old,new in [('1.2.5',r'\sref{I.1.1.11}',r'\sref{I.1.1.12-fr}'),('5.3.8',r'\hyperref[I.3.4.3]{(3.4.3.1)}',r'\hyperref[I.3.4.3.1-fr]{(3.4.3.1)}')]:
  u=i_units(full)[n];assert old in u.text;pos=u.start+u.text.index(old);edits.append((pos,pos+len(old),new));changes.append([str(p.relative_to(RESULT)),n,old,new,'own comparison',f'BASE/native/ega1/ega1-{n.split(".")[0]}-fr.tex ({layer.lower()}): cited source target'])
 if layer=='DIPLOMATIC':
  for n,old,new in [('5.5.5',r'La Proposición~\sref{I.5.5.5}',r'La Proposición~\sref{I.5.5.4}'),('5.5.9',r'la suficiencia se deduce de \sref{I.5.5.5}',r'la suficiencia se deduce de \sref{I.5.5.4}')]:
   u=i_units(full)[n];assert old in u.text;pos=u.start+u.text.index(old);edits.append((pos,pos+len(old),new));changes.append([str(p.relative_to(RESULT)),n,old,new,'own comparison','BASE/native/ega1/ega1-5-fr.tex (diplomatic): printed citation retained; inherited correcting note retained'])
 u=i_units(full)['10.10.5'];m=re.search(r'donde \$v\$ es un homomorfismo \$A\^[pm]\\to A\^[qn]\$',u.text);assert m
 a=u.start+m.end();new=r' \sref{I.10.10.2-fr}';edits.append((a,a,new));changes.append([str(p.relative_to(RESULT)),'10.10.5','',new,'own comparison','BASE/native/ega1/ega1-10-fr.tex: omitted citation after the presentation morphism'])
 for a,b,new in sorted(edits,reverse=True):full=full[:a]+new+full[b:]
 p.write_text(full)
for p in (ES/'worktree/es/PORTED_20261109/IV4/ega4').rglob('*.tex'):
 t=p.read_text();old=t
 for a,b in [(r'\text{pour $\mathbf{p},\mathbf{q}$ dans $\mathbb{N}^{(L)}$,',r'\text{para $\mathbf{p},\mathbf{q}$ en $\mathbb{N}^{(L)}$,'),(r'\textup{pour }',r'\textup{para }'),(r'\text{pour }',r'\text{para }'),(r'\text{et}',r'\text{y}'),(r'\textup{et}',r'\textup{y}'),(r'\mbox{et}',r'\mbox{y}')]:
  if a in t:changes.append([str(p.relative_to(RESULT)),'mathematical text argument',a,b,'own comparison','IV4 source formula text: French connective translated, mathematical tokens retained']);t=t.replace(a,b)
 if t!=old:p.write_text(t)
write_tsv(RESULT/'records/CAMBIOS_root_final_references.tsv',['file','place','before','after','kind','source'],changes)
print('reviewed reference/text changes',len(changes))
