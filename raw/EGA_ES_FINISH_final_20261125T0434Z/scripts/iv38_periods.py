from iv38_tools import *
rows=json.loads((ROOT/'records/IV38_PERIOD_CANDIDATES.json').read_text())
new={
0:'\nforman un sistema inductivo de homomorfismos de haces de anillos; como se puede escribir\n',
1:r' en virtud de \sref{IV.8.2.12}, existe, por tanto, un homomorfismo único'+'\n',
2:' es cuasicoherente y de tipo finito; sean ',
3:'; en virtud de la exactitud por la derecha de ',
4:' son también sobreyectivos; además, si existe un homomorfismo ',
5:'; está claro que ',
6:r'; se deduce de \sref{IV.8.5.2}, (i), que existen ',
7:r'); es inducido en un abierto (resp. es cerrado) si ',
8:'.\n'+r'\end{corollary}'+'\n\n'+r'\begin{proof}'+'\nLa condición es evidentemente suficiente; recíprocamente, si existe un ',
9:'; pero, como ',
10:' es cuasicompacto y cuasiseparado; como ',
11:'; el anillo ',
12:'; además, como ',
13:'; se deduce inmediatamente de las definiciones que ',
14:r', son cuasicompactas, de modo que \sref{IV.1.6.3} ',
15:' son disjuntos dos a dos; además, los ',
16:'; como la inmersión canónica ',
17:'; el morfismo primera proyección ',
18:r' lo es \sref{IV.1.6.2}; basta, pues, en virtud de \sref{IV.1.8.7.1}, aplicar el caso (vi) del teorema al morfismo diagonal'+'\n',
19:' una multiplicación asociativa y conmutativa; de igual manera se ve que se puede suponer ',
20:r' es una inmersión abierta. Las propiedades del enunciado se deducen entonces de la invariancia de las propiedades anteriores por cambio de base \sref[II]{II.5.5.5}, (iii), \sref[I]{I.3.5.2} y \sref[I]{I.4.3.2}.'+'\n'+r'\end{proof}'+'\n\n'+r'\begin{proof}[Continuación de la demostración de \sref{IV.8.10.5}]'+'\n'+r'\emph{Caso} (xii): Apliquemos al morfismo ',
21:r' la prop. \sref{IV.8.10.5.1}: se tiene, pues, un diagrama conmutativo'+'\n',
22:' es una inmersión abierta; se deduce para cada ',
23:r'-preesquemas de presentación finita \sref{IV.8.10.5.1} y \sref{IV.1.6.2}), se ve que existe ',
24:r' es propio \sref[II]{II.5.5.3} y \sref[II]{II.5.4.2}, y como ',
25:' es propio.\n\n'+r'\emph{Casos} (xiii) \emph{y} (xiv): En virtud de (xii) y de \sref[II]{II.5.5.3}, que se aplica porque los ',
26:'-amplio; como ',
27:r' \sref{IV.8.5.2}, (ii); además, en virtud de \sref{IV.8.5.5}, se puede suponer ',
28:r' \emph{invertible}. El teorema en este caso es entonces consecuencia del lema más preciso siguiente:'+'\n\n',
29:r' \sref{IV.1.6.1}, \sref{IV.1.2.6}, \sref[II]{II.5.1.1}, \sref[II]{II.5.4.1} y \sref[II]{II.6.2.2}, de modo que se puede suponer ',
30:'-preádica; se sabe que ',
31:r' es de tipo finito \sref{IV.1.5.4}; además, una factorización ',
32:'; ',
33:' y, por consiguiente, si ',
34:r' \sref{IV.8.8.2}, (ii); además, existe un morfismo ',
35:'; la comprobación de que se pueden tomar estos conjuntos como conjuntos de morfismos es inmediata, pues la composición de sistemas de morfismos ',
36:r', lo que es un caso particular de \sref{IV.8.13.2}: en efecto, los morfismos estructurales ',
37:'; se tiene, por tanto, ',
38:'; si ',
39:'-morfismo; por hipótesis, existen un índice ',
}
st=SP.read_text();su=units(st);edits=[]
for i,r in enumerate(rows):
 un,gap,_,_,fr,old=r;u=su[un];ms=core_spans(u.text);a=ms[gap-1].end if gap else 0;b=ms[gap].start if gap<len(ms) else len(u.text);assert u.text[a:b]==old,(i,un)
 edits.append((u.start+a,u.start+b,new[i],un,'Source long sentence restored after bilingual reading of the whole gap; reference and clause order retained.'))
apply(edits,'periods')

from iv38_patchlib import Patches
p=Patches('periods_context')
p.replace('8.5.2.1',r'Ahora $S_\lambda$',r'Observemos ahora que $S_\lambda$')
p.replace('8.8.2.3',r'Sea, pues, un $X$-morfismo',r'Supongamos, pues, dado un $X$-morfismo')
p.replace('8.8.2.5',r'$S_\rho$ \sref{IV.1.6.3}. C.Q.F.D.',r'$S_\rho$. C.Q.F.D.')
p.replace('8.10.5.1',r'$j$, observando que',r'$j$ (observando que')
p.replace('8.10.5.1',r'$\mathcal L$ que es amplio para $f$',r'$\mathcal L$ que sea $f$')
p.replace('8.11.4',r'$\widehat A$ es local noetheriano y',r'$\widehat A$ es un anillo local noetheriano y que el morfismo')
p.replace('8.13.5',r'$X_\mu\to S$ son de presentación finita,',r'$X_\mu\to S$, por ser de presentación finita,')
p.replace('8.14.2.2',r'$\mathfrak J_\mu/\mathfrak J_\lambda$ ($(1\leqslant i\leqslant n)$',r'$\mathfrak J_\mu/\mathfrak J_\lambda$ $(1\leqslant i\leqslant n)$')
p.save()
