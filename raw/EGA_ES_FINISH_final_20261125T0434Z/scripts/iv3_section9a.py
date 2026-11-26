from iv3_manual import patch
patch('9.1.4',r'$X_{(K)}\xrightarrow{\sim} Y_{(K)}$',r'$X_{(K)}\xrightarrow{\sim}Y_{(K)}$')
patch('9.1.5',r'$X_{(K)}\to\mathbf{P}_K^n=\mathbf{P}_k^n\otimes_k K$',r'$X_{(K)}\to\mathbf P_K^r=\mathbf P_k^r\otimes_k K$')
patch('9.1.5',r"$X_{(k')}\to\mathbf{P}_{k'}^n$",r"$X_{(k')}\to\mathbf P_{k'}^r$")
patch('9.2.2',r'la condición~$2^\circ$',r'la condición $2^{\mathrm o}$')
patch('9.2.3',r'es una vecindad de $\eta$ \textnormal{(resp.}',r'es una vecindad de $\eta$ en $S$ \textnormal{(resp.}')
patch('9.2.6.2',r'$\dim(X_s)=\sup_i\dim((X_i)_s)$',r'$\dim(X_s)=\sup_i(\dim((X_i)_s))$')
patch('9.3.2',r'Sea $\boldsymbol{P}$ una de las propiedades siguientes de un $k$-morfismo $f:X\to Y$ de preesquemas algebraicos:',r'Denotemos por $\boldsymbol{P}$ una de las propiedades siguientes de un $k$-morfismo $f:X\to Y$ de $k$-preesquemas algebraicos:')
patch('9.4.4',r'en $S$ tal que $\operatorname{Ker}(w_s)=\mathcal N_s$',r'en $S$ tal que, para $s\in U$, $\operatorname{Ker}(w_s)=\mathcal N_s$')
for n in ['9.4.4','9.4.7','9.4.7.1']:
 patch(n,r'~\sref{IV.8.1.2},~$a$))',r' (8.1.2, \emph{a)})')
patch('9.4.4',r'un complejo de tres términos,',r'un complejo de tres términos $\mathcal L^\bullet$,')
patch('9.4.4',r'existe una vecindad $U$ de $\eta$ tal que $w|f^{-1}(U)=0$',r'existe una vecindad abierta $U$ de $\eta$ tal que $w|f^{-1}(U)=0$')
patch('9.4.7',r'existe una vecindad $U$ de $\eta$ en $S$ tal que $\mathcal F|f^{-1}(U)$',r'existe una vecindad abierta $U$ de $\eta$ en $S$ tal que $\mathcal F|f^{-1}(U)$')
patch('9.4.7',r'del lema más general siguiente:',r'del lema más general siguiente (aplicado al caso en que $g$ es la identidad):')
patch('9.4.7.1',r'existe una vecindad $U_0$ de $\eta$ en $S$',r'existe una vecindad abierta $U_0$ de $\eta$ en $S$')
patch('9.4.7.1',r'podemos por tanto tomar $U_0$ de modo que $u_s:\sh{G}_s\to\sh{H}_s$ sea inyectivo para todo $s\in U_0$',r'se puede, por tanto, suponer $U_0$ elegido de modo que, para $s\in U_0$, $u_s:\mathcal G_s\to\mathcal H_s$ sea inyectivo')
patch('9.4.9',r'podemos suponer que es isomorfo a un submódulo',r'se puede suponer que $(\mathcal F_0)_{s_0}$ es isomorfo a un submódulo')

