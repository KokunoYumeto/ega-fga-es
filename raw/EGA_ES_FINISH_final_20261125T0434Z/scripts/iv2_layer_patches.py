#!/usr/bin/env python3
"""Language-dependent printed-layer readings; formula variants are handled separately."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import reconcile_iv2 as r
P=[
('ega4-2_2.4.4_through_2.4.8_ES','2.4.4',r'separado \textup{(1.8.7.1)}',r'separado \textup{(1.7.7.1)}'),
('ega4-2_2.4.4_through_2.4.8_ES','2.4.6',r'\emph{homeomorfismo universal} (2.4.3, (vi))',r'\emph{homeomorfismo universal} (2.4.4, (vi))'),
('ega4-2_2.5.1_through_2.5.3_ES','2.5.2',r'cap.~II, \S~5, núm.~2',r'cap.~\textbf{II}, \S~5, núm.~2'),
('ega4-2_2.5.8_part2_ES','2.5.8.6',"forma con la primera un di-isomorfismo de $C'$-módulos a derecha", "forma con la primera un di-isomorfismo de $C'$-\\emph{módulos} a derecha"),
('ega4-2_2.8.4_ES','2.8.4','el primer miembro de (2.8.4.1)','el primer miembro de (2.8.3.1)'),
('ega4-2_3.4.6_3.4.9_ES','3.4.9',r'las saturaciones de $f^nM$',r'las saturaciones de los $f^nM$'),
('ega4-2_4.2.1_4.2.3_ES','4.2.1','tiene la segunda relación (4.2.1.1); intercambiando los papeles de $K$ y $L$,\nse obtiene la primera relación (4.2.1.1)', 'tiene la primera relación (4.2.1.1); intercambiando los papeles de $K$ y $L$,\nse obtiene la segunda relación (4.2.1.1)'),
('ega4-2_4.4_ES','4.4.5','de donde resulta la primera afirmación de (4.4.5).','de donde resulta la primera afirmación de (4.4.4).'),
('ega4-2_4.6.19_4.6.22_ES','4.6.21',r'en virtud de (\textbf I, 9.1.12), que',r'en virtud de (\textbf I, 9.1.12) que'),
('ega4-2_4.6.19_4.6.22_ES','4.6.22','Las definiciones (4.6.17) y (4.6.19)','Las definiciones (4.6.18) y (4.6.19)'),
('ega4-2_4.6.19_4.6.22_ES','4.6.22',r'\emph{geométricamente reducido} (4.6.13).',r'\emph{geométricamente reducido} (4.6.11).'),
('ega4-2_4.7.11_4.7.13_ES','4.7.12','por la multiplicidad total','por \\textbf{la} multiplicidad total'),
('ega4-2_4.8.5_4.8.7_ES','4.8.7',r'\emph{Alg.}, cap.~II, 3.',r'\emph{Alg.}, cap~\textbf{II}, 3.'),
('ega4-2_5.5.1_5.5.3_ES','5.5.1','Además, en virtud de (5.5.1.1), se','Además, en virtud de (5.5.1.2), se'),
('ega4-2_5.5.4_5.5.7_ES','5.5.7','los dos miembros de (5.5.7.1) son iguales','los dos miembros de (5.5.7) son iguales'),
('ega4-2_5.6.9_5.6.10_ES','5.6.10',r'$B_{\mathfrak n}$ es una extensión algebraica del cuerpo residual de',r'$B_{\mathfrak n}$ es una extensión algebraica del cuerpo de fracciones de'),
('ega4-2_5.7.3_5.7.4_ES','5.7.3','normalidad (cf. (5.8.6)).','normalidad (cf. (5.8.5)).'),
('ega4-2_5.9.2_5.9.4_ES','5.9.4','(5.9.4.1) buscado.','(5.9.1.1) buscado.'),
('ega4-2_5.9.11_ES','5.9.11',r'$Z$-cerrado en $x$, como',r'$Z$-puro en $x$, como'),
('ega4-2_5.10.1_5.10.4_ES','5.10.4',r'\textup{(}con las notaciones de \textup{(5.9.6))}',r'\textup{(}con las notaciones de \textup{(5.9 6))}'),
('ega4-2_5.10.14_5.10.15_ES','5.10.14',r'$\dim(\mathcal F_x)=0$ (3.1.4), es decir',r'$\dim(\mathcal F_x)=0$ (3.1.4) es decir'),
('ega4-2_6.1.5_ES','6.1.5',r'en virtud de (\textbf 0, 16.3.9.2),',r'en virtud de (5.5.1.2),'),
('ega4-2_6.3.5_6.3.7_ES','6.3.5',r'$N=B=\mathcal O_x$.',r'$N=B=\mathcal O_x$'),
('ega4-2_6.5.1_6.5.3_ES','6.5.2',r'Sean $X$, $Y$ dos preesquemas localmente noetherianos, $f:X\to Y$',r'Sean $X$, $Y$ dos preesquemas localmente noetherianos $f:X\to Y$'),
('ega4-2_6.6_ES','6.6.1','(6.5.4, (i)) y (2.1.13)','(6.5.4, (ii)) y (2.1.13)'),
('ega4-2_7.8.3_ES','7.8.3',r'$\mathcal F$ es no nulo y libre',r'$\mathcal F$ es libre'),
('ega4-2_7.8.3_ES','7.8.3',r'es no nulo y libre de torsión, $\operatorname{Ass}',r'es libre de torsión, $\operatorname{Ass}'),
('ega4-2_7.8.4_ES','7.8.4','por «que satisface (7.8.2, (ii) y (iii))».','por «que satisface» (7.8.2, (ii) y (iii)).'),
('ega4-2_7.8.4_ES','7.8.4','de (7.8.3, (iv));','de (7.8.3, (v));'),
('ega4-2_7.9.1_ES','7.9.1','íntegramente cerrados de dimensión a lo sumo $1$, por lo que son cuerpos o anillos de\nvaloración discreta', 'íntegramente cerrados de dimensión $1$, por lo que son anillos de\nvaloración discreta'),
('ega4-2_bibliography_continuation_ES','bibliography.36',r'\textsc{Abhyankar}, Local uniformization on algebraic',r'\textsc{Abhyankhar}, Local uniformization of algebraic'),
('ega4-2_bibliography_continuation_ES','bibliography.36','characteristic $p\\ne0$, \\emph{Ann. of','characteristic $p\\ne0$, \\emph{Amer. J. of'),
('ega4-2_terminology_index_ES','index.3.2.5','\\EGAIVtwoTerm{Descomposición irredundante, descomposición irredundante reducida\nde un módulo}{3.2.5}','Descomposición irredundante, descomposición irredundante reducida\nde un módulo : 3.2.5\\par'),
]

def main():
 for name,place,before,after in P:r.change('tree/worktree/es/DIPLOMATIC/EGA_IV2/'+name+'.diplomatic.tex',place,before,after,'own comparison','EGA_ES_FINISH_1_FRANCES/fr/diplomatic/IV2/native/ega4/ega4-2-fr.tex, IV.'+place)
 # Two inherited citation/prose deviations occur in both languages/layers. Source is controlling.
 for layer in ['CURRENT','DIPLOMATIC']:
  suff='.tex' if layer=='CURRENT' else '.diplomatic.tex'
  r.change('tree/worktree/es/'+layer+'/EGA_IV2/ega4-2_4.6.15_4.6.18_ES'+suff,'4.6.15', 'Como $p$ es abierto (2.4.10) y cerrado', 'Como $p$ es cerrado', 'own comparison','EGA_ES_FINISH_1_FRANCES/fr/'+layer.lower()+'/IV2/native/ega4/ega4-2-fr.tex, IV.4.6.15; remove unmarked expansion absent from source')
 r.change('tree/worktree/es/CURRENT/EGA_IV2/ega4-2_7.8.4_ES.tex','7.8.4',r'$0$ (7.8.3, (iii));',r'$0$ (7.8.3, (ii));')

if __name__=='__main__':main()
