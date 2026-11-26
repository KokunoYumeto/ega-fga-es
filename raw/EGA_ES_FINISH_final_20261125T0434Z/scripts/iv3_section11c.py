"""Source omissions and clause repairs in IV3 §§11.4–11.6."""
from iv3_manual import patch
patch('11.4.1.1',r'''\]
y, por tanto,
\[
\operatorname{gr}_{\mathfrak J}^0(N_\lambda)
\otimes''',r'''\]
pues este último producto tensorial es igual a
\[
(M\otimes_A B_\lambda)\Big/
\big(\operatorname{Im}(M\otimes_A\mathfrak JB_\lambda)
 +\operatorname{Im}(\mathfrak J_1M\otimes_A B_\lambda)\big)
\]
y se tiene
$\operatorname{Im}(\mathfrak J_1M\otimes_A B_\lambda)
=\operatorname{Im}(M\otimes_A\mathfrak J_1B_\lambda)
\subset\operatorname{Im}(M\otimes_A\mathfrak JB_\lambda)$ puesto que
$\mathfrak J_1B_\lambda\subset\mathfrak JB_\lambda$ por definición; finalmente,
la relación $\mathfrak J_1B_\lambda\subset\mathfrak JB_\lambda$ muestra que también
se tiene
\[
(M/\mathfrak J_1M)\otimes_A(B_\lambda/\mathfrak JB_\lambda)
=(M/\mathfrak J_1M)\otimes_{A/\mathfrak J_1}
 (B_\lambda/\mathfrak JB_\lambda)
\]
de modo que finalmente se tiene
\[
\operatorname{gr}_{\mathfrak J}^0(N_\lambda)
=M_0\otimes_{A_0}(B_\lambda/\mathfrak JB_\lambda)
\]
y, por consiguiente,
\[
\operatorname{gr}_{\mathfrak J}^0(N_\lambda)
\otimes''')
patch('11.4.1.1',r'concluimos que',r'se concluye que')
patch('11.4.1.1',r'denotemos por $\mathfrak J_n$',r'denotaremos por $\mathfrak J_n$')
patch('11.4.1.1',r'Provistamos',r'Proveamos')
patch('11.4.1.1',r'provistamos',r'proveamos')
patch('11.4.1.1',r'vemos inmediatamente que',r'se ve inmediatamente que')
patch('11.4.5',r'(\textbf{I},~$1.2.7$)',r'$(\mathbf I,1.2.7)$')
patch('11.4.5',r'''sean $U_1$ y $\mathrm{Z}_1$ el abierto de $Y_1$
y el subpreesquema cerrado de $U_1$''',r'''sean $U_1$ el abierto de $Y_1$ y $Z_1$ el
subesquema cerrado de $U_1$''')
patch('11.4.7',r'potencia simbólica (es decir, el núcleo',r'potencia simbólica de $\mathfrak p_i$ (núcleo')
patch('11.4.11',r'Se deduce, pues, de \sref{IV.11.2.6} que, poniendo',r'Existe, por tanto, \sref{IV.11.2.6} un índice $\lambda$ tal que, poniendo')
patch('11.4.11',r"un punto $t'_0$ de $V$ cerrado en $V$",r"en $V$ un punto $t'_0$ cerrado en $V$")
patch('11.4.11',r'(\textbf{I},~$6.4.2$)',r'(\textbf I, 6.4.2)')
patch('11.4.11',r'(\textbf{II},~$6.1.5$)',r'(\textbf{II}, 6.1.5)')
patch('11.4.11',r'(\textbf{II},~$6.1.10$)',r'(\textbf{II}, 6.1.10)')
patch('11.5.1',r'(\textbf{I},~$2.4.4$)',r'(\textbf I, 2.4.4)')
patch('11.5.1',r'(\textbf{I},~$3.6.1$)',r'(\textbf I, 3.6.1)')
patch('11.5.1',r'vemos que nos reducimos',r'se ve que se reduce')
patch('11.5.2',r'$(\mathbf{0}_\mathrm{I},~7.3.5)$',r'($\mathbf 0_{\mathrm I},7.3.5$)')
patch('11.5.3',r'(\textbf{I},~$3.6.5$)',r'(\textbf I, 3.6.5)')
patch('11.5.3',r'(\textbf{II},~$5.4.2$)',r'(\textbf{II}, 5.4.2)',all=True)
patch('11.5.3',r"$h=g_{(\mathfrak{m})}:\mathrm{Z}'\to\mathrm{Z}$",r"$h=g_{(Z)}:Z'\to Z$")
patch('11.5.3',r"es la imagen inversa de $\mathfrak{m}_{y'}^n$ en $A$",r"es la imagen inversa en $A$ de $\mathfrak m_{y'}^n$")
patch('11.5.3',r'''$Y$ es un preesquema local
y $y$ es su punto cerrado, de modo que $\mathrm{V}=\mathrm{Y}$ y, en consecuencia,''',r'''$Y$ es un esquema local, por tanto la única
vecindad del punto cerrado $y$ de $Y$ es $Y$ entero, dicho de otro modo''')
patch('11.5.3',r'En estas condiciones demostraremos que',r'En estas condiciones se va a probar que')
patch('11.5.3',r'será útil en el cap.~V',r'nos será útil en el cap.~V')
patch('11.5.5',r'(\textbf{II},~$6.1.11$)',r'(\textbf{II}, 6.1.11)')
patch('11.5.5.2',r"en todo punto $x'\in\mathrm{X}'_\lambda$ situado sobre $x$",r"en todos los puntos de $X'_{\lambda}$ sobre $x$")
patch('11.5.5.2',r"$\mathrm{V}'=g'^{-1}(\mathrm{U}')=\bigcup w_\lambda^{-1}(\mathrm{V}'_\lambda)$",r"$V'=g'^{-1}(U')=\bigcup_{\lambda}w_{\lambda}^{-1}(V'_{\lambda})$")
patch('11.5.5.2',r'(\textbf{I},~$3.6.1$)',r'(\textbf I, 3.6.1)')
patch('11.6.1',r'para algún $i$ existe un anillo',r'hay un')
print('Reviewed §§11.4–11.6 source clauses complete')

