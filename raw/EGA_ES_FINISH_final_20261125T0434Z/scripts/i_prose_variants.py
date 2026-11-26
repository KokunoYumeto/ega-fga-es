"""Explicit Spanish readings of EGA I's current/diplomatic prose differences."""
import re,json,csv
from corpus import RESULT, ES, write_tsv
from tex_tools import numbered_units, balanced_end, math_spans

OVERRIDES={
'5.3.9':r'''\begin{proposition}[5.3.9]
\label{I.5.3.9-fr}
El morfismo diagonal $\Delta_X$ es una inmersión de $X$ en
$X\times_S X$.
\end{proposition}

En efecto, como las aplicaciones continuas $p_1$ y $\Delta_X$ de los espacios
subyacentes son tales que $p_1\circ\Delta_X$ es la identidad, $\Delta_X$
es un homeomorfismo de $X$ sobre $\Delta_X(X)$. Asimismo, siendo la identidad el homomorfismo
compuesto
$\mathscr{O}_x\to\mathscr{O}_{\Delta_X(x)}\to\mathscr{O}_x$ de los
homomorfismos correspondientes a $p_1$ y a $\Delta_X$,
el homomorfismo correspondiente a $\Delta_X$ es sobreyectivo; la proposición
resulta, pues, de (\hyperref[I.4.2.2-fr]{4.2.2}).

Se dice que el subpreesquema de $X\times_S X$ asociado a la inmersión
$\Delta_X$ (\hyperref[I.4.2.1-fr]{4.2.1}) es \emph{la diagonal} de
$X\times_S X$.

''',
'7.3.8':r'''\begin{env}[7.3.8]
\label{I.7.3.8-fr}
Sean $X$, $Y$ dos preesquemas que tienen cada uno un número finito de componentes
irreducibles, y sea $f:X\to Y$ un morfismo cuya restricción al
conjunto de los puntos genéricos de las componentes irreducibles de $X$ sea una
\emph{sobreyeción} sobre el conjunto de los puntos genéricos de las componentes irreducibles
de $Y$. Entonces se tiene
\[
  f^*(\mathscr{R}(Y))=\mathscr{R}(X).
  \tag{7.3.8.1}\label{I.7.3.8.1-fr}
\]
\end{env}

En efecto, se está reducido (en virtud de
(\hyperref[I.7.3.3-fr]{7.3.3})) al caso en que $X$ e $Y$ son irreducibles, de
puntos genéricos $x$, $y$, con $f(x)=y$; por tanto,
\[
  (f^*(\mathscr{R}(Y)))_x
  =\mathscr{O}_y\otimes_{\mathscr{O}_y}\mathscr{O}_x
  =\mathscr{O}_x
\]
(\hyperref[0.4.3.1-fr]{\textbf{0}, 4.3.1}), lo que demuestra (7.3.8.1) en virtud de
(\hyperref[I.7.3.5-fr]{7.3.5}).

\subsection{Haces de torsión y haces sin torsión.}
\label{subsection:I.7.4-fr}

''',
'9.4.6':r'''\begin{lemma}[9.4.6]
\label{I.9.4.6-fr}
Sean $X$ un preesquema, $L$ un conjunto bien ordenado,
$(V_\lambda)_{\lambda\in L}$ un recubrimiento de $X$ por abiertos afines,
$U$ un abierto de $X$; para todo $\lambda\in L$, se pone
$W_\lambda=\bigcup_{\mu<\lambda}V_\mu$. Se supone que:
\begin{enumerate}
  \item[\textup{1\textsuperscript{o}}] Para todo $\lambda\in L$,
    $V_\lambda\cap W_\lambda$ es cuasicompacto:
  \item[\textup{2\textsuperscript{o}}] El morfismo de inmersión $U\to X$ es
    cuasicompacto.
\end{enumerate}
Entonces, para todo $\mathscr{O}_X$-módulo cuasicoherente $\mathscr{F}$ y todo
sub-$(\mathscr{O}_X|U)$-módulo cuasicoherente \textup{de tipo finito} $\mathscr{G}$ de
$\mathscr{F}|U$, existe un sub-$\mathscr{O}_X$-módulo cuasicoherente \textup{de
tipo finito} $\mathscr{G}'$ de $\mathscr{F}$ tal que
$\mathscr{G}'|U=\mathscr{G}$.
\end{lemma}

\begin{proof}
Pongamos $U_\lambda=U\cup W_\lambda$; se va a definir por recurrencia transfinita
una familia $(\mathscr{G}'_\lambda)$, donde $\mathscr{G}'_\lambda$ es un
sub-$(\mathscr{O}_X|U_\lambda)$-módulo cuasicoherente de tipo finito de
$\mathscr{F}|U_\lambda$, tal que
$\mathscr{G}'_\lambda|U_\mu=\mathscr{G}'_\mu$ para $\mu<\lambda$ y
$\mathscr{G}'_\lambda|U=\mathscr{G}$. El único sub-$\mathscr{O}_X$-módulo
$\mathscr{G}'$ de $\mathscr{F}$ tal que
$\mathscr{G}'|U_\lambda=\mathscr{G}'$ para todo $\lambda\in L$
(\hyperref[0.3.3.1-fr]{\textbf{0}, 3.3.1}) responderá a la cuestión. Supongamos, pues, los
$\mathscr{G}'_\mu$ definidos y con las propiedades precedentes para
$\mu<\lambda$; si $\lambda$ no tiene predecesor, se tomará para
$\mathscr{G}'_\lambda$ el único sub-$(\mathscr{O}_X|U_\lambda)$-módulo de
$\mathscr{F}|U_\lambda$ tal que
$\mathscr{G}'_\lambda|U_\mu=\mathscr{G}'_\mu$ para todo $\mu<\lambda$, lo
que es lícito puesto que los $U_\mu$ con $\mu<\lambda$ forman entonces un
recubrimiento de $U_\lambda$. Si, por el contrario, $\lambda=\mu+1$, se tiene
$U_\lambda=U_\mu\cup V_\mu$, y bastará definir un
sub-$(\mathscr{O}_X|V_\mu)$-módulo cuasicoherente de tipo finito
$\mathscr{G}''_\mu$ de $\mathscr{F}|V_\mu$ tal que
\[
  \mathscr{G}''_\mu|(U_\mu\cap V_\mu)
  =\mathscr{G}'_\mu|(U_\mu\cap V_\mu)~;
\]
se tomará después para $\mathscr{G}'_\lambda$ el
sub-$(\mathscr{O}_X|U_\lambda)$-módulo de $\mathscr{F}|U_\lambda$ tal que
$\mathscr{G}'_\lambda|U_\mu=\mathscr{G}'_\mu$ y
$\mathscr{G}'_\lambda|V_\mu=\mathscr{G}''_\mu$
(\hyperref[0.3.3.1-fr]{\textbf{0}, 3.3.1}). Ahora bien, como $V_\mu$ es afín, la existencia
de $\mathscr{G}''_\mu$ está asegurada por (9.4.3) una vez que se haya demostrado que
$U_\mu\cap V_\mu$ es cuasicompacto; pero $U_\mu\cap V_\mu$ es unión de
$U\cap V_\mu$ y de $W_\mu\cap V_\mu$, que son ambos cuasicompactos en
virtud de la hipótesis.
\end{proof}

''',
}

def notes(t):
    out=[]
    for m in re.finditer(r'\\footnote\{',t):
        end=balanced_end(t,m.end()-1);out.append(t[m.end():end-1])
    return out

def main():
    p=ES/'worktree/es/DIPLOMATIC/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex'
    text=p.read_text();initial=numbered_units(text);units={k:s.text for k,s in initial.items()};changes=[];failed=[];tr=[]
    def rep(num,old,new,count=1):
        if old not in units[num]:failed.append([num,old,new]);return
        units[num]=units[num].replace(old,new,count)
        changes.append([str(p.relative_to(RESULT)),num,old,new,'assembly',f'French diplomatic EGA I, {num}; explicit comparison of both French layers'])
    for num,new in OVERRIDES.items():
        old=units[num]
        nn=notes(old)
        if nn:
            new+='\n'+''.join(r'\par\noindent\textit{Nota de la edición heredada.}\footnote{'+s+'}\par\n' for s in nn)
        units[num]=new
        changes.append([str(p.relative_to(RESULT)),num,old,new,'assembly',f'EGA_ES_FINISH_1_FRANCES/fr/diplomatic/BASE/native/ega1/ega1-{num.split(".")[0]}-fr.tex: {num}'])
        prose=new
        for s in reversed(math_spans(prose)):prose=prose[:s.start]+' '+prose[s.end:]
        prose=re.sub(r'\\[A-Za-z]+',' ',prose)
        tr.append([str(p.relative_to(RESULT)),f'EGA_ES_FINISH_1_FRANCES/fr/diplomatic/BASE/native/ega1/ega1-{num.split(".")[0]}-fr.tex',num,len(re.findall(r'\b[^\W\d_]+\b',prose))])
    rep('10.3.2',r'es un homeomorfismo sobre el subespacio cerrado $V(\mathfrak{J})$ de $\mathfrak{X}$',r'es, por lo demás, el homeomorfismo identidad de $\mathfrak{X}$ sobre sí mismo')
    rep('10.3.6','la conclusión se sigue','el corolario se sigue')
    rep('10.4.1',r'\begin{env}[10.4.1]',r'\begin{env}[10.4.1.]')
    rep('10.9.9',"el preesquema formal $X_{/X'}$","el preesquema $X_{/X'}$")
    rep('10.14.2',r'\erratum[II]{ideal coherente de $\sh{O}_\mathfrak{X}$}',r'$\mathscr{O}_{\mathfrak{X}}$-módulo coherente')
    rep('10.14.2',r'los \erratum[II]{ideales coherentes de $\sh{O}_\mathfrak{X}$}',r'los $\mathscr{O}_{\mathfrak{X}}$-módulos coherentes')
    rep('10.14.4',r'$\mathscr{A}$ igual a $\sh{O}_\mathfrak{X}$ en el complemento',r'$\mathscr{A}$ nulo en el complemento')
    rep('10.14.4',r'el soporte del cociente $\bigl(\sh{O}_\mathfrak{X}|U_\alpha\bigr)/\mathfrak{a}_\alpha^\Delta$',r'el soporte de $\mathfrak{a}_\alpha^\Delta$')
    rep('10.14.6',r'se toma como $u$ el homomorfismo que corresponde por esta adjunción a $f_*(\rho)$',r'tomaremos $u=f_*(\rho)$')
    rep('2.5.4',"para todo $S'-preesquema $X$,","para todo $S'-preesquema,")
    rep('2.5.5',r'Si $X$ es un $S$-preesquema,',r'Si $X$ es un $S$-morfismo,')
    rep('3.3.1',r'''\sref{I.3.3.13}, \sref{I.3.3.15} y la afirmación sobre las sumas de la última frase
de \sref{I.3.3.10}''',r'\sref{I.3.3.13} y \sref{I.3.3.15}')
    rep('3.4.5',r'\emph{situado sobre $\mathrm{s}$}',r'\emph{situado sobre} $\mathrm{s}$')
    rep('3.4.9',r'un $\boldsymbol{k}(s)$-homomorfismo\footnote',r'un $\boldsymbol{k}(s)$-monomorfismo\footnote')
    rep('4.2.2',r'un isomorfismo de $\psi^*(\mathscr{O}_X)$ sobre $\mathscr{O}_Y$',r'un isomorfismo de $\mathscr{O}_Y$ sobre $\psi^*(\mathscr{O}_X)$')
    rep('4.2.3',r'el homomorfismo $\Gamma(\theta)$',r'el homomorfismo $\Gamma(\psi)$')
    rep('4.3.1',r'''$\operatorname{Im}(\mathfrak{b}\otimes_A C\to B\otimes_A C)+\operatorname{Im}(B\otimes_A\mathfrak{c}\to B\otimes_A C)$,
o, equivalentemente, la suma de los ideales engendrados por $u(\mathfrak{b})$ y $v(\mathfrak{c})$''',r'$u(\mathfrak{b})+v(\mathfrak{c})$')
    rep('4.4.5',r'\erratum[II]{$A$ es una $B$-álgebra}',r'$B$ es una $A$-álgebra')
    # Keep the inherited note, but move it after the printed introductory clause.
    num='4.5.5';s=units[num]
    m=re.search(r'Para demostrar \(ii\), sea .*?sean \$p\$ y \$q\$',s,re.S)
    if m:
        n=notes(m.group(0));rep(num,m.group(0),r'Para demostrar (ii), sean $p$ y $q$'+''.join(r'\footnote{'+x+'}' for x in n))
    else:failed.append([num,'proof introduction',''])
    rep('5.3.8',r'$X(Z)_Y$ tiene a lo sumo un elemento',r'lo mismo ocurre con $X(Z)_Y$')
    rep('6.1.8',r'la intersección con $U$ del complemento (en $X$)',r'el complemento (en $X$)')
    rep('6.1.12',r'$X$ sea conexo y no vacío',r'$X$ sea conexo')
    rep('7.1.2',r'coinciden en un abierto de $U\cap V\cap W$, que es denso',r'coinciden en $U\cap V\cap W$, que es denso')
    rep('7.1.15',r'se identifican con los puntos de',r'se identifican con los puntos geométricos de')
    rep('7.1.16',r'se identifican con los puntos de',r'se identifican con los puntos geométricos de')
    rep('7.4.3',r'-submódulo cuasicoherente no nulo de',r'-submódulo de')
    rep('7.4.4',r'son espacios vectoriales sobre el cuerpo',r'se identifican con sub-$\mathscr{O}_x$-módulos del cuerpo')
    rep('7.4.7',r', a condición de sustituir c) por la condición de que $\operatorname{Supp}(\mathscr{F})$ no contenga ninguna componente irreducible de $X$','')
    rep('9.5.1','existe un subpreesquema cerrado más pequeño','existe un subpreesquema más pequeño')
    for num,old,new in [('10.5.1','10.3.7','10.3.6'),('2.3.1','0.4.1.7','0.4.1.6'),('4.5.5','I.4.2.5','I.4.2.4'),('5.1.4','I.2.1.8','I.2.1.7'),('5.3.13','I.4.2.5','I.4.2.4'),('5.4.8','I.5.4.4','I.5.4.5'),('5.5.1','I.4.2.5','I.4.2.4'),('5.5.4','I.2.1.8','I.2.1.7'),('5.5.5','I.5.5.5','I.5.5.4'),('5.5.9','I.5.5.5','I.5.5.4'),('9.6.5','0.4.1.3','0.4.1.4')]:
        rep(num,old,new,2 if num=='5.5.9' else 1)
    for num,old,new in [('1.6.5',r'(A_x)_{[\vphi_x]}',r'(A_x)_{[\varphi_{x\'}]}'),('10.6.2',r'\sh{O}_{X_\lambda}=',r'\mathscr{O}_{X_i}='),('10.6.3',r'$(U,\sh{O}_\mathfrak{X}|U)$',r'$(U,\mathscr{O}_X|U)$'),('10.10.5',r'$(M\otimes_A A_n)^\Delta=(M\otimes_A A_n)\supertilde$',r'$(M\otimes_A A_n)^\Delta=(M\otimes_n A_n)^{\sim}$'),('10.15.4',r'los abiertos $U\times_\mathfrak{S} V$',r'los abiertos $U\times_{S}V$'),('5.1.2',r'$\mathfrak{I}\subset\mathfrak{j}_x$',r'$\mathfrak{J}_x\subset\mathfrak{j}_x$'),('6.6.3',r'un entorno $W_1(x)\subset W(x)$ de $y=f(x)$',r'un entorno $W_1(x)\subset W(x)$ de $x$')]:rep(num,old,new)
    for num,span in sorted(initial.items(),key=lambda kv:kv[1].start,reverse=True):
        if units[num]!=span.text:text=text[:span.start]+units[num]+text[span.end:]
    p.write_text(text)
    write_tsv(RESULT/'records/CAMBIOS_i_diplomatic_prose.tsv',['file','place','before','after','kind','source'],changes)
    write_tsv(RESULT/'records/TRADUCCION_i_diplomatic_prose.tsv',['file','french_source','range','words'],tr)
    write_tsv(RESULT/'records/I_DIPLOMATIC_MANUAL_REMAINING.tsv',['place','before','after'],failed)
    print(json.dumps({'changes':len(changes),'newly_translated_units':len(tr),'failed':failed},ensure_ascii=False))
if __name__=='__main__':main()
