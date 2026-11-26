"""Source-supported IV4 prose and equation-structure repairs."""
from pathlib import Path
import re,json
from corpus import RESULT,FR,ES,write_tsv
from tex_tools import numbered_units,math_spans,balanced_end

ROOT=ES/'worktree/es/PORTED_20261109/IV4/ega4'
changes=[]
def file_for(num):
    found=[p for p in ROOT.rglob('*.tex') if num in numbered_units(p.read_text())]
    assert len(found)==1,(num,found)
    return found[0]
def edit(num,old,new,source):
    p=file_for(num);t=p.read_text();u=numbered_units(t)[num];assert u.text.count(old)==1,(num,old[:100],u.text.count(old))
    text=u.text.replace(old,new);p.write_text(t[:u.start]+text+t[u.end:])
    changes.append([str(p.relative_to(RESULT)),num,old,new,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/current/IV4/native/ega4/'+source+': '+num])

def main():
    # These three labels are source equation numbers, not extra statements.
    for num,source in [('19.5.5.5','ega4-18-fr.tex'),('19.7.1.3','ega4-18-fr.tex'),('19.7.1.6','ega4-18-fr.tex')]:
        p=file_for(num);t=p.read_text();m=re.search(r'\\begin\{env\}\['+re.escape(num)+r'\]',t);end=t.index(r'\end{env}',m.end())+len(r'\end{env}');old=t[m.start():end]
        fm=next(s.text for s in math_spans((FR/'current/IV4/native/ega4'/source).read_text()) if r'\label{IV.'+num+'}' in s.text)
        new=old[m.end()-m.start():-len(r'\end{env}')];new=new.replace(r'\label{IV.'+num+'}','',1)
        s=math_spans(new)[0];new=new[:s.start]+fm+new[s.end:]
        p.write_text(t[:m.start()]+new+t[end:]);changes.append([str(p.relative_to(RESULT)),num,old,new,'own comparison','French equation environment and tag'])

    p=file_for('16.8.8');u=numbered_units(p.read_text())['16.8.8'];a=u.text.index('donde $a_i\\in B$');b=u.text.index('Demostremos ahora',a);old=u.text[a:b]
    fm=re.search(r'\\footnote\{',old);fe=balanced_end(old,fm.end()-1);note=old[fm.start():fe]
    new=r'''donde $a_i\in B$ y $t\in M$. Ahora bien, este elemento se escribe
$\sum_{H\subset I_{n+1}}(\setmin 1)^{n+1-\operatorname{Card}(H)}(\prod_{i\in H}a_i)\otimes((\prod_{i\notin H}a_i)t)$'''+note+r''',
y el valor de $D'$ para este elemento no es otro que el primer miembro de
(16.8.8.2), lo que demuestra la equivalencia de \emph{a)} y \emph{c)}.

'''
    edit('16.8.8',old,new,'ega4-16-fr.tex')
    edit('19.4.6',r'la equivalencia de \emph{a)} y \emph{b)}:',r'la equivalencia de $a)$ y $b)$:','ega4-18-fr.tex')
    edit('19.4.6','Podemos trabajar en el caso afín','Se puede trabajar en el caso afín','ega4-18-fr.tex')
    edit('21.10.16','nos reducimos inmediatamente al caso','se reduce inmediatamente al caso','ega4-21b-fr.tex')
    edit('21.10.4','podemos limitarnos al caso','se puede limitar al caso','ega4-21b-fr.tex')
    edit('21.10.4','hemos visto que los puntos','se ha visto que los puntos','ega4-21b-fr.tex')
    edit('21.10.4',r'''del $\sh{O}_{X',x'}$-módulo
$\sh{O}_{X',x'}/t'_{x'}\sh{O}_{X',x'}=(\sh{O}_{X,y}/t_y\sh{O}_{X,y})\otimes_{\sh{O}_{X,y}}\sh{O}_{X',x'}$
como de \sref{IV.4.7.1} resulta que''',r'''del $\sh{O}_{X',x'}$-módulo $\sh{O}_{X',x'}/t'_{x'}\sh{O}_{X',x'}$;
como $\sh{O}_{X',x'}/t'_{x'}\sh{O}_{X',x'}=(\sh{O}_{X,y}/t_y\sh{O}_{X,y})\otimes_{\sh{O}_{X,y}}\sh{O}_{X',x'}$, resulta de \sref{IV.4.7.1} que se tiene''','ega4-21b-fr.tex')
    edit('21.13.10',r'$X-\overline{\{y\}}$',r'$V\setmin(V\cap\overline{\{y\}})$','ega4-21c-fr.tex')
    write_tsv(RESULT/'records/CAMBIOS_iv4_manual.tsv',['file','place','before','after','kind','source'],changes)
    print(json.dumps({'changes':len(changes)}))

if __name__=='__main__':main()
