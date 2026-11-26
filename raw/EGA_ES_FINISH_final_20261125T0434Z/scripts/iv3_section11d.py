"""Reviewed source clauses and mathematical statements in IV3 §§11.7–11.10."""
import re
from iv3_manual import patch,source_unit
from tex_tools import math_spans
patch('11.7.1',r'sea $\Gamma$ su grupo de Galois',r'denotemos por $\Gamma$ el grupo de Galois de $k^\prime$')
# Use the source's literal spelling of the field.
patch('11.7.1',r'$k^\prime$',r"$k'$")
patch('11.7.1',r'''\[
\mathrm{B}\otimes_\mathrm{A}\mathrm{B}
=\frac{\mathrm{A}'\otimes_\mathrm{A}\mathrm{A}'}
{\operatorname{Im}(\mathfrak{J}\otimes_\mathrm{A}\mathrm{A}')+\operatorname{Im}(\mathrm{A}'\otimes_\mathrm{A}\mathfrak{J})}.
\]''',r'''$B\otimes_A B=(A'\otimes_A A')/(\operatorname{Im}(\mathfrak J\otimes_A A')+\operatorname{Im}(A'\otimes_A\mathfrak J))$.''')
patch('11.7.2',r'''sea $\mathrm{A}_0=k[\mathrm{S},\mathrm{T}]$ y sea $\mathrm{A}=\mathrm{A}_0/\mathrm{A}_0\mathrm{S}\mathrm{T}$''',r'''$A_0$ el anillo de polinomios $k[S,T]$, $A$ el anillo cociente $A_0/A_0ST$''')
patch('11.7.2',r'''Sea $X$ el subpreesquema de $Z$ inducido en el complementario de $z_2$.''',r'''Denotaremos por $X$ el subpreesquema de $Z$ inducido en el complementario de $z_2$ en $Z$.''')
patch('11.7.2',r'\emph{a fortiori}, $f$ no es propio',r'\emph{a fortiori}, no es propio')
patch('11.7.3',r'obtenido restringiendo $g$',r'restricción de $g$ a $X$')
patch('11.7.5',r'\sref{IV.6.15.11}',r'\sref{IV.6.5.11}')
patch('11.7.5',r'$\mathbf{C}[[\mathrm{U},\mathrm{V}]]/((\mathrm{U}+i\mathrm{V})(\mathrm{U}\setmin i\mathrm{V}))$',r'$\mathbf C[[U,V]]/(U+iV)(U\setmin iV)$')
patch('11.7.5',r'$;\ es el producto directo',r'$;\ $\overline B$ es el producto directo') if False else None
patch('11.7.5',r'$\overline B=\overline A\otimes_{\mathbf R}\mathbf C$; es el producto directo',r'$\overline B=\overline A\otimes_{\mathbf R}\mathbf C$; $\overline B$ es el producto directo')
patch('11.8.1',r"cuya contracción a $\mathrm{A}$ es $\mathfrak m=\mathfrak i_y$",r"del que $\mathfrak m=\mathfrak i_y$ es la traza sobre $A$")
patch('11.8.1',r'($1\leq i\leq m$)',r'$(1\leq i\leq m)$')
patch('11.9.3',r'$v_{\lambda\mu}:\sh{G}_\lambda\to(j_{\lambda\mu})_*(j_{\lambda\mu}^*(\sh{G}_\lambda))=(j_{\lambda\mu})_*(\sh{H}_{\lambda\mu})$',r'''$v_{\lambda\mu}=\rho_{\mathcal G_\lambda}:\mathcal G_\lambda\to
(j_{\lambda\mu})_*(j_{\lambda\mu}^*(\mathcal G_\lambda))
=(j_{\lambda\mu})_*(\mathcal H_{\lambda\mu})$''')
patch('11.9.3',r'donde los $f_\lambda$ son \emph{afines}',r'dicho de otro modo, se reduce al caso en que los $Z_\lambda$ son \emph{afines}')
patch('11.9.4',r'''\[
  \bigcap_{\lambda\in\mathrm{L}}\operatorname{Ker}((\varphi_\lambda)_s)
  =\left(\bigcap_{\lambda\in\mathrm{L}}\operatorname{Ker}(\varphi_\lambda)\right)_s
  \quad \sref[0]{0.1.3.2}.
\]''',r'''$\bigcap_{\lambda\in L}\operatorname{Ker}((\varphi_\lambda)_s)
=(\bigcap_{\lambda\in L}\operatorname{Ker}(\varphi_\lambda))_s$
$(\mathbf 0_{\mathrm I},1.3.2)$.''')
patch('11.9.6',r'sean cero es ella misma cero',r'sean nulas, entonces $t^\prime$ sea ella misma nula')
patch('11.9.6',r'$t^\prime$',r"$t'$")
patch('11.9.7.1',r'$u_\lambda\otimes 1$ es la restricción',r'$u_\lambda\otimes 1:M\otimes_A N\to M_\lambda\otimes_A N$ es la restricción')
patch('11.9.8',r'de rango $2$',r'de rango 2')
patch('11.9.10',r'sean cero es ella misma cero',r'sean nulas, entonces $z^\prime$ sea ella misma nula')
patch('11.9.10',r'$z^\prime$',r"$z'$")
patch('11.9.10',r'$Z_\lambda=X$ para todo $\lambda\in\mathrm{L}$',r'$Z_\lambda=X$ para todo $\lambda$')
patch('11.9.10',r'''$\mathrm{B}_h=\mathrm{A}_{s_h}/\mathfrak{J}'_{h-1}\mathrm{A}_{s_h}$, para que
  $\mathrm{A}_h=\mathrm{B}_h/((\mathfrak{J}_{h-1}/\mathfrak{J}'_{h-1})\mathrm{B}_h)$''',r'''$A_{s_h}/\mathfrak J'_{h-1}A_{s_h}=B_h$, de modo que
  $A_h=B_h/(\mathfrak J_{h-1}/\mathfrak J'_{h-1})B_h$''')
patch('11.9.11',r'se reduzca a $0$',r'se reduzca a 0')
patch('11.9.11',r'se tiene inmediatamente $t_x=0$ para todo punto cerrado $x\in U$',r'resulta inmediatamente que para todo punto cerrado $x\in U$, se tiene $t_x=0$')
patch('11.9.11',r'es un punto \emph{no cerrado}, se tiene',r'es un punto \emph{no cerrado} de $X$, se tiene')
patch('11.9.12',r'''se puede suponer que $t'$ es la imagen canónica de una sección $t''_\alpha$ de $\mathcal F''_\alpha$ sobre $U''_\alpha$''',r'''se puede suponer que hay una sección $t''_\alpha$ de $\mathcal F''_\alpha$ sobre $U''_\alpha$ tal que $t'$ sea la imagen canónica de $t''_\alpha$''')
patch('11.9.15',r'obtenida de $(u_\lambda)$ por el cambio de base',r'obtenida a partir del cambio de base')
patch('11.9.15',r"$\sh{G}'_\lambda=\sh{G}_\lambda\otimes_{\sh{O}_\mathrm{S}}\sh{O}_{\mathrm{S}'}$",r"$\mathcal G'_\lambda=\mathcal G_\lambda\otimes_S S'$")
patch('11.9.15',r'''$\mathfrak{J}^n\otimes_{(\mathrm{A}/\mathfrak{J})}(\mathrm{N}_\lambda/\mathfrak{J}\mathrm{N}_\lambda)$ se identifica con $\mathfrak J^nN_\lambda$''',r'''$\mathfrak J^nN_\lambda$ se identifica con
$\mathfrak J^n\otimes_{(A/\mathfrak J)}(N_\lambda/\mathfrak JN_\lambda)$''')
patch('11.9.15',r'$t^0_\alpha=0$ para todo $\alpha$ y, por tanto, $t=0$',r'$t^0_\alpha=0$ para todo $\alpha$ puesto que la familia $(u_{\lambda0})$ es separante, y, por consiguiente, $t=0$')
patch('11.9.16',r'''basta probar que la imagen $t_\mathfrak p$ de $t$ en $M_\mathfrak p$ es nula para todo ideal maximal $\mathfrak{p}$ de $\mathrm{B}$''',r'''basta probar que para todo ideal maximal $\mathfrak p$ de $B$, la imagen $t_\mathfrak p$ de $t$ en $M_\mathfrak p$ es nula''')
patch('11.9.16',r'se reduce a $0$',r'se reduce a 0',all=True)
patch('11.9.16',r'''que la familia $(u'_\lambda)_{s'}$ es separante para todo $s'\in S'$''',r'''que, para todo $s'\in S'$, la familia $(u'_\lambda)_{s'}$ es separante''')
patch('11.9.17.1',r', aplicado a $u_\lambda$,',r'')
patch('11.10.1',r'''todo par $u$, $v$ de $\mathrm{S}$-morfismos''',r'''todo par de $S$-morfismos $u$, $v$''')
patch('11.10.1',r'''con la restricción de $f_\lambda$ a $f_\lambda^{-1}(\mathrm{U})$''',r'''con el morfismo $f_\lambda^{-1}(U)\to U$, restricción de $f_\lambda$,''')
patch('11.10.1',r'tiene imagen $0$',r'tiene imagen 0')
patch('11.10.1',r'''que es la imagen inversa, por $(u,v)_\mathrm{S}$, de la diagonal de $\mathrm{X}'$ en $X'\times_SX'$''',r'''imagen inversa de la diagonal de $X'\times_SX'$ por $(u,v)_S$''')
patch('11.10.3',r'''La noción de familia esquemáticamente dominante sobre $\mathrm{X}$, como resulta, por ejemplo, de una condición de la forma \emph{b)} de \sref{IV.11.10.1}, es \emph{local} sobre $X$''',r'''La noción de familia esquemáticamente dominante es \emph{local} sobre
$X$, como resulta, por ejemplo, de la forma \emph{b)} de \sref{IV.11.10.1}''')
print('Reviewed §§11.7–11.10 source clauses complete')

