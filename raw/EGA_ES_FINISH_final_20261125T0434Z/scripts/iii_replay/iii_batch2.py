import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iii_bridge_patch import apply
D={
'current:1:10.3.1:0':r''' es \emph{noetheriano} (\hyperref[0.6.5.2-fr]{§0§, 6.5.2}), lo que concluirá la demostración del lema.

Se tiene ''',
'current:1:10.3.1:1':r'''. Resulta, pues, de (\hyperref[0.7.2.12-fr]{§0§, 7.2.12}) y (\hyperref[0.7.2.8-fr]{§1§, 7.2.8}) que ''',
'current:1:10.3.1:2':r'''-módulo plano (\hyperref[0.6.2.1-fr]{§0§, 6.2.1}); el criterio (\hyperref[0.10.2.2-fr]{10.2.2}) es, pues, aplicable a la ''',
'current:1:10.3.1:3':r''', tales que: §0§ Para todo ''',
'current:1:10.3.1:4':r''' generada por un solo elemento; §0§ Para todo ordinal ''',
'current:1:10.3.1:5':r'''; §0§ ''',
'current:1:10.3.1:6':r''' no tiene predecesor, y, si ''',
'current:1:10.3.1:7':r''', como §0§, donde ''',
'current:1:10.3.1:8':r''' satisface el enunciado de (\hyperref[0.10.3.1-fr]{10.3.1}).
\end{env}

Se observará que, en virtud de (\hyperref[0.10.2.1-fr]{10.2.1, §0§}), se tiene un isomorfismo canónico
''',
'current:1:10.3.1:9':r'''-módulo plano (\hyperref[0.7.3.3-fr]{§0§, 7.3.3}), por tanto un ''',
'current:1:10.3.1:10':r'''-módulo plano (\hyperref[0.6.2.1-fr]{§0§, 6.2.1}).

Se ha demostrado además el

''',
'current:1:11.1.1:0':r''' a un sistema E formado por los elementos siguientes:
\begin{enumerate}
  \item[§0§] Una familia ''',
'current:1:11.1.1:1':r''' definidos para §0§, §1§ y ''',
'current:1:11.1.1:2':r'''.
  \item[§0§] Una familia de morfismos
''',
'current:1:11.1.1:3':r'''
  \item[§0§] Una familia de isomorfismos
''',
'current:1:11.1.1:4':r'''

Los demás elementos del dato de E son entonces:
\begin{enumerate}
  \item[§0§] Dos subobjetos ''',
'current:1:11.1.1:5':r'''
  \item[§0§]
    \oldpage[0\textsubscript{III}]{24}
    Una familia ''',
'current:1:11.1.1:6':r'''.
  \item[§0§] Para todo par ''',
'current:1:11.1.1:7':r''', sin las filtraciones, se llama el \emph{término límite} de la sucesión espectral E.

Supongamos que la categoría ''',
'current:1:11.1.2:0':r'''} de una sucesión espectral E en una sucesión espectral ''',
'current:1:11.1.3:0':r''' están determinados por los datos \emph{a)} a \emph{c)} de la sucesión espectral E). Diremos que la sucesión espectral E es \emph{regular} si es débilmente convergente y si además:
\begin{enumerate}
  \item[''',
'current:1:11.1.3:1':r''' es \emph{estable}; la hipótesis de que E es débilmente convergente implica entonces
''',
'current:1:11.1.3:2':r''' es \emph{discreta} y \emph{exhaustiva}.
\end{enumerate}

Se dice que la sucesión espectral E es \emph{corregular} si es débilmente convergente y si además:
\begin{enumerate}
  \item[''',
'current:1:11.1.3:3':r''' es \emph{codiscreta}.
\end{enumerate}

Finalmente, se dice que E es \emph{birregular} si es a la vez regular y corregular, es decir, si se tienen las condiciones siguientes:
\begin{enumerate}
  \item[\textit{a)}] Para todo par ''',
'current:1:11.1.4:0':r'''. Si una sucesión espectral E es débilmente convergente, se tiene
''',
'current:1:11.1.4:1':r''' es un morfismo de E en una sucesión espectral débilmente convergente ''',
'current:1:11.1.5:0':r'''
\oldpage[0\textsubscript{III}]{26}
la hipótesis de que E y ''',
'current:1:11.1.6:0':r'''\begin{env}[11.1.6]
\label{0.11.1.6-fr}
Resulta de (\hyperref[0.11.1.1.2-fr]{11.1.1.2}) y de la definición (\hyperref[0.11.1.1.3-fr]{11.1.1.3}) que si, en una sucesión espectral E, se tiene
''',
'current:1:11.1.6:1':r'''; si E es \emph{débilmente convergente}, se tiene, pues, también
''',
'current:1:11.1.6:2':r''' es \emph{discreta} y \emph{exhaustiva}, la sucesión E es \emph{regular} y se tiene
''',
'current:1:11.1.9:0':r'''\begin{env}[11.1.9]
\label{0.11.1.9-fr}
Habremos de considerar condiciones que aseguren que una sucesión espectral E sea birregular de manera «uniforme» en ''',
'current:1:11.2.1:0':r''' se utilizará también para \emph{objetos graduados} de ''',
'current:1:11.2.1:1':r''', de tipo §0§, que no son necesariamente complejos (o que se pueden considerar como tales para operadores de derivación \emph{nulos}); por ejemplo, escribiremos
''',
'current:1:11.3.1:0':r''' se suponen, pues, \emph{permutables}. Supongamos satisfecha \emph{una} de las dos condiciones siguientes: §0§ Las \emph{sumas directas infinitas} existen en ''',
'current:1:11.3.1:1':r'''; §0§ Para todo ''',
'current:1:11.4.1:0':r''', provisto de una aumentación §0§, de modo que la sucesión
''',
'current:1:11.4.2:0':r'''
    son exactas, es decir, §0§, §1§, §2§ y
''',
'current:1:11.4.2:1':r''' son, respectivamente, \emph{resoluciones} de §0§, §1§, §2§ y ''',
'current:1:11.4.2:2':r''' (la condición (ii) anterior implica entonces que los §0§, §1§ y
''',
'current:1:11.4.4:0':r''' existen y son \emph{birregulares} en cada uno de los dos casos siguientes:
\begin{enumerate}
  \item[§0§] ''',
'current:1:11.4.4:1':r''' está acotado inferiormente;
  \item[§0§] Todo objeto de ''',
'current:1:11.4.4:2':r''' admite una resolución inyectiva de longitud a lo sumo igual a un entero ''',
'current:1:11.4.5:0':r''', se tienen isomorfismos funtoriales
§0§
\end{proposition}

\begin{proof}
En efecto, los únicos términos ''',
'current:1:11.5.1:1':r''', del que §0§ es evidentemente el límite inductivo cuando ''',
'current:1:11.5.1:2':r'''; por la permutabilidad de las sumas directas y de los límites inductivos, el complejo simple asociado a ''',
'current:1:11.5.2:0':r''' que tienen las
\oldpage[0\textsubscript{III}]{37}
propiedades siguientes: §0§ Todo ''',
'current:1:11.5.2:1':r'''; §0§ Para todo ''',
'current:1:11.5.2:2':r''' y tales además que: §0§ ''',
'current:1:11.5.2:3':r'''; §0§ Si se pone ''',
'current:1:11.5.2:6':r''' y con §0§ en ''',
'current:1:11.5.2:7':r'''. Pongamos entonces §0§ para §1§, §2§ y §3§ para §4§, con el operador de derivación evidente. Pongamos
''',
'current:1:11.5.2:8':r''' para todo §0§ (con ''',
'current:1:11.5.2:9':r''' es inyectivo para todo §0§, y que los ''',
'current:1:11.5.2:10':r''' compatible con las aumentaciones, y dos tales morfismos §0§, §1§ son homótopos.
\end{corollary}

\begin{proof}
Esto no es sino (M, V, 1.1 \emph{a)}) aplicado a la categoría abeliana
''',
'current:1:11.5.2:11':r''', o también que §0§ es igual a §1§; como ''',
}
apply(D)
