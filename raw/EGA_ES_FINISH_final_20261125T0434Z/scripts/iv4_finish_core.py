"""Final four reviewed IV4 boundary differences and untranslated errata quotes."""
import re,csv
from corpus import RESULT,write_tsv
from tex_tools import numbered_units,balanced_end
from iv4_manual import file_for
from audit_iv4 import PROJECT

changes=[];translations=[]
def change(p,place,old,new,source):
    t=p.read_text();assert t.count(old)==1,(place,old[:80],t.count(old));p.write_text(t.replace(old,new,1))
    changes.append([str(p.relative_to(RESULT)),place,old,new,'own comparison',source])
def main():
    p=file_for('21.10.17.3');change(p,'21.10.17.3',r'$(\mathbf{0},19.8.8)$, (ii)',r'\sref[0]{0.19.8.8}[(ii)]','French IV4 21.10.17.3 reference')
    p=file_for('21.13.14');t=p.read_text();u=numbered_units(t)['21.13.14'];a=u.text.index(r'\end{enumerate}');b=u.text.index('La propiedad',a);old=u.text[a:b]
    new=r'''\oldpage[IV-4]{322}
  \item[\textup{b$'$)}] Para toda parte cerrada $Y$ de $X$ tal que
$\operatorname{codim}(Y,X)\geq2$ y tal que exista $\lambda$ para el cual
$Y\subset X\setmin U_\lambda$, el par $(X,Y)$ es parafactorial.
\end{enumerate}
\end{proposition}

\begin{proof}
'''
    change(p,'21.13.14',old,new,'French IV4 21.13.14: third condition in statement')
    p=file_for('21.14.1');u=numbered_units(p.read_text())['21.14.1'];a=u.text.index(r'ideal primo $\mathfrak q$ de altura');b=u.text.index(r'no contenido en $\mathfrak p$',a)
    old=u.text[a:b];m=re.search(r'\\footnote\{',old);end=balanced_end(old,m.end()-1);note=old[m.start():end]
    new=r'ideal primo $\mathfrak q$ de $B$ de altura $1$'+note+' '
    change(p,'21.14.1',old,new,'French IV4 21.14.1: hypothesis order; note retained unchanged')

    p=PROJECT/'ega4/ega4-errata-addenda-list3-es.tex'
    quoted=[
      (r'\emph{pour} $k\geq1$',r'\emph{para} $k\geq1$','IV.12.1.1'),
      (r'$\alpha$) ou $\beta$)',r'$\alpha$) o $\beta$)','Err_IV'),
      ("Dire que $A$ est caténaire por Dire qu'un anneau \\emph{intègre} $A$ est\ncaténaire",r'Decir que $A$ es catenario por Decir que un anillo \emph{íntegro} $A$ es catenario','Err_IV 5'),
      ('formellement lisses pour les\ntopologies préadiques','formalmente suaves para las topologías preádicas','Err_IV 15'),
      ('formellement lisses','formalmente suaves','Err_IV 15'),
      ('et anneaux strictement locaux','y anillos estrictamente locales','Err_IV 16'),
      ('« comme » por « comme étant »','« como » por « como siendo »','Err_IV 16'),
      (r"tel qu'il existe un"+'\n'+r'$\sh{O}_Y$-Module ample',r'tal que exista un $\sh{O}_Y$-módulo amplio','Err_IV 29'),
      ('et quasi-séparé','y cuasiseparado','Err_IV 29'),
      ("L'hypothèse",'La hipótesis','Err_IV 29'),
      (r'''Il résulte de
{\EGAReadLink{IV.8.12.3}{(8.12.3)}} que l'existence de la
factorisation de l'énoncé est une propriété \emph{locale} sur $Y$; on peut
donc supposer $Y$ \emph{affine}, ce qui''',r'''Resulta de
{\EGAReadLink{IV.8.12.3}{(8.12.3)}} que la existencia de la
factorización del enunciado es una propiedad \emph{local} sobre $Y$; se puede,
pues, suponer $Y$ \emph{afín}, lo que''','Err_IV 29'),
      ('quelconque','cualquiera','Err_IV 43'),
      ("dont l'ensemble des composantes irréductibles est localement fini",'cuyo conjunto de componentes irreducibles es localmente finito','Err_IV 43'),
      ('de type fini','de tipo finito','Err_IV 43'),
      ('de présentation\nfinie','de presentación finita','Err_IV 43'),
      (r'''supposons que
pour tout $y\in Y$''',r'supongamos que para todo $y\in Y$','Err_IV 46'),
      (r'''supposons que $f$ soit localement de
présentation finie et que pour tout $y\in Y$''',r'supongamos que $f$ sea localmente de presentación finita y que para todo $y\in Y$','Err_IV 46'),
    ]
    for old,new,place in quoted:
        t=p.read_text()
        if old not in t:raise ValueError('Unlocated erratum quote: '+old)
        count=t.count(old);p.write_text(t.replace(old,new))
        changes.append([str(p.relative_to(RESULT)),place,old,new,'own comparison','French IV4 errata/addenda list3: quoted correction'])
        translations.append([str(p.relative_to(RESULT)),'EGA_ES_FINISH_1_FRANCES/fr/current/IV4/native/ega4/ega4-errata-addenda-list3-fr.tex',place+' quoted phrase',len(re.findall(r'\b[A-Za-zÀ-ÿ]+\b',new))])
    write_tsv(RESULT/'records/CAMBIOS_iv4_finish_core.tsv',['file','place','before','after','kind','source'],changes)
    write_tsv(RESULT/'records/TRADUCCION_iv4_quotes.tsv',['file','french_source','range','words'],translations)
    print('Changes',len(changes),'translated quotes',len(translations))
if __name__=='__main__':main()
