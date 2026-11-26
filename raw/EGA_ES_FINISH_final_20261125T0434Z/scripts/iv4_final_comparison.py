"""Resolve the remaining reviewed IV4 text/notation disagreements."""
import re,json,csv
from corpus import RESULT,write_tsv
from tex_tools import numbered_units,math_spans,balanced_end
from audit_iv4 import mask_footnotes,PROJECT
from iv4_manual import file_for

record=RESULT/'records/CAMBIOS_iv4_final_comparison.tsv'
changes=list(csv.reader(record.open(),delimiter='\t'))[1:] if record.exists() else []
def save():write_tsv(record,['file','place','before','after','kind','source'],changes)
def patch(num,old,new,all=False):
    if any(r[1]==num and re.sub(r'\s+',' ',r[2])==re.sub(r'\s+',' ',old) and r[3]==new for r in changes):return
    p=file_for(num);t=p.read_text();u=numbered_units(t)[num]
    n=u.text.count(old)
    if n==0:
        matches=list(re.finditer(r'\s+'.join(re.escape(x) for x in re.split(r'\s+',old)),u.text))
        if len(matches)==1:old=matches[0][0];n=1
    assert n>0 and (all or n==1),(num,n,old[:90])
    v=u.text.replace(old,new) if all else u.text.replace(old,new,1)
    p.write_text(t[:u.start]+v+t[u.end:]);changes.append([str(p.relative_to(RESULT)),num,old,new,'own comparison','Supplied current French IV4: '+num+'; source reading retained; inherited notes preserved']);save()
def replace_math(num,old,new):
    if any(r[1]==num and r[2]==old and r[3]==new for r in changes):return
    p=file_for(num);t=p.read_text();u=numbered_units(t)[num];clean=mask_footnotes(u.text)
    places=[m.start() for m in re.finditer(re.escape(old),clean)];assert len(places)==1,(num,old,places)
    a=places[0];v=u.text[:a]+new+u.text[a+len(old):]
    p.write_text(t[:u.start]+v+t[u.end:]);changes.append([str(p.relative_to(RESULT)),num,old,new,'own comparison','Supplied current French IV4: '+num+'; outside editorial footnotes']);save()

def main():
    gaps=json.loads((RESULT.parent/'tmp/iv4/gaps.json').read_text())
    for i in [4,6,7,11,29]:
        g=gaps[i]
        for old,new in zip(g['es'],g['fr']):replace_math(g['place'],old,new)
    patch('18.11.12.1',r"es separable sobre $k'$ (4.6.1)",r'es separable sobre $k$ (4.6.1)')
    patch('20.2.12',r'elementos regulares de $A$\footnote',r'elementos regulares de $X$\footnote')
    patch('21.5.6',r'$f^*(D)$ está definido\footnote',r'$f_*(D)$ está definido\footnote')
    patch('21.15.9',r"\emph{regular con respecto a $S'$}\footnote",r'\emph{regular con respecto a $S$}\footnote')
    patch('16.7.10',r"(estando definida en ($\mathbf{0}_{\mathrm I}$, 3.7.1) la imagen inversa de un haz de conjuntos por $p_2^{(n)}$)",r"(estando definida la imagen inversa de un haz de conjuntos por $p_2^{(n)}$ en ($\mathbf{0}_{\mathrm I}$, 3.7.1))")
    patch('16.9.6',r'''para que la sucesión
  $(f_i)$ engendre $\mathscr J$ no basta con que los $(\bar f_i)_y$ formen
  una base del $(\mathcal{O}_y/\mathscr{J}_y)$-módulo
  $\mathscr{J}_y/\mathscr{J}_y^2$ para \emph{todo} $y\in X$''',r'''no basta con que los $(\bar f_i)_y$ formen
  una base del $(\mathcal{O}_y/\mathscr{J}_y)$-módulo
  $\mathscr{J}_y/\mathscr{J}_y^2$ para \emph{todo} $y\in X$ para que la sucesión
  $(f_i)$ engendre $\mathscr{J}$''')
    patch('18.11.3.5',r'Si localizamos en $\mathfrak p$ la sucesión exacta (18.11.3.6) (aplicada a $A_0$ y $A$), obtenemos por tanto',r'Si se localiza la sucesión exacta (18.11.3.6) (aplicada a $A_0$ y $A$) en $\mathfrak p$, se obtiene por tanto')
    patch('20.3.3','a este pseudomorfismo',r'a este pseudo-$S$-morfismo',all=True)
    patch('20.4.6',r"Pongamos $y=h'_x(x)$. Para todo $x'\in U$, $y$ es una especialización de $h(x')$.",r"Notemos que, para todo $x'\in U$, $h(x')$ es una especialización de $h'_x(x)=y$.")
    patch('20.4.6',r"Como, para todo $x'\in X\cap U$, $y$ es una especialización de $h(x')$",r"Puesto que, para $x'\in X\cap U$, $h(x')$ es una especialización de $y$")
    patch('20.4.8',r' definido en todas partes y que prolonga $h$,',r' definido en todas partes,')
    patch('20.4.8','nos reducimos, pues, al caso','se reduce, pues, al caso')
    patch('20.4.11',r'Sean $X$ un $S$-preesquema localmente noetheriano,',r'Sean $X$ un preesquema localmente noetheriano,')
    patch('20.5.8',r'un preesquema $Y$ sobre $S$ relativamente a $S$',r'un $S$-preesquema $Y$ relativamente a $S$')
    patch('20.6.4',r'cuyo germen en el punto $x$ sea $t_x$',r'del que $t_x$ sea el germen en el punto $x$')
    patch('20.6.4','podemos suponer','se puede suponer')
    patch('21.13.9',"$b_i'/1$ es un elemento no nulo","$b_i'/1$ es un elemento $\\neq0$")
    p=file_for('21.13.9');u=numbered_units(p.read_text())['21.13.9']
    old=re.search(r"b_i'/1\$[^\n]{0,100}",u.text)
    if old:print('21.13.9 remaining text:',old[0])
    patch('21.4.9','Además, la planitud y la desigualdad',r'Por otra parte, puesto que $f$ es plano, la relación')
    patch('21.4.9','implican\n'+r'$\operatorname{prof}(\sh{O}_{X,x})\geq2$', 'implica\n'+r'$\operatorname{prof}(\sh{O}_{X,x})\geq2$')
    patch('21.4.9',r'Si $D$ denota su valor'+'\n'+r'común',r'Si $D$ es el valor común de los $D_\alpha$')
    patch('21.4.10',r'''los gérmenes de estos dos divisores en todo punto de $X_\eta$ son
cero por la condición 1\textdegree{}. Sus gérmenes en todo punto maximal
de $X_y$ son iguales por la condición 2\textdegree{}.''',r'''los gérmenes de $D'$ y de $\operatorname{div}(t^n\circ f)$ en un punto cualquiera de $X_\eta$ son ambos
nulos en virtud de 1\textdegree{}. Del mismo modo, los gérmenes de $D'$ y de $\operatorname{div}(t^n\circ f)$ en un punto maximal
de $X_y$ son iguales por la condición 2\textdegree{}.''')
    patch('21.4.10','La\nigualdad buscada resulta de',r"Se tiene, pues, $D'=\operatorname{div}(t^n\circ f)$ en virtud de")
    patch('21.4.13',r'''Sea $U$ una vecindad abierta
afín en $X$ de un punto $x\in X_\eta$, y sea $s$ una sección
de $\sh{L}$ sobre $U$ con el mismo germen en $x$ que $s_\eta$.''',r'''Sean $U$ una vecindad abierta
afín de un punto $x\in X_\eta$ en $X$ y $s$ una sección
de $\sh{L}$ sobre $U$ con el mismo germen que $s_\eta$ en el punto $x$.''')
    patch('21.4.13','que esta sección induce sobre',r'que $s$ induce sobre')
    p=PROJECT/'ega4/ega4-16-es/components/11_component.tex';t=p.read_text();old='Operadores diferenciales sobre un $S$-preesquema diferencialmente\nsuave';new='Operadores diferenciales sobre un preesquema diferencialmente suave'
    assert old in t;p.write_text(t.replace(old,new));changes.append([str(p.relative_to(RESULT)),'16.11 heading',old,new,'own comparison','French IV4 §16.11 heading'])
    p=PROJECT/'ega4/ega4-errata-addenda-list3-es.tex';t=p.read_text()
    pat=re.compile(r'\\paragraph\{\(Err\\textsubscript\{IV\}, (\d+)\)\.\}')
    def repl(m):
        new=r'\paragraph{($\mathbf{Err}_{\mathrm{IV}}$, '+m[1]+')}'
        changes.append([str(p.relative_to(RESULT)),'Err_IV '+m[1],m[0],new,'own comparison','French erratum heading']);return new
    t=pat.sub(repl,t);p.write_text(t)
    write_tsv(RESULT/'records/CAMBIOS_iv4_final_comparison.tsv',['file','place','before','after','kind','source'],changes)
    print('changes',len(changes))
if __name__=='__main__':main()
