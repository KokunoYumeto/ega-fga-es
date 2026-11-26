from pathlib import Path
import csv
new=r'''
\begin{flushright}
\textit{(Continuará.)}
\end{flushright}

\clearpage
\oldpage[0\textsubscript{III}]{80}
\thispagestyle{empty}
\null
\clearpage
\thispagestyle{plain}
\markboth{ESTUDIO COHOMOLÓGICO DE LOS HACES COHERENTES}{CAPÍTULO III}
\oldpage[III]{81}
\phantomsection
\label{chapter:III-fr}

\begin{center}
{\large CAPÍTULO III\par}
\vspace{1.5em}
{\Large\bfseries ESTUDIO COHOMOLÓGICO\par}
{\Large\bfseries DE LOS HACES COHERENTES\par}
\vspace{1.8em}
{\bfseries Sumario\par}
\end{center}

\medskip
\begin{tabular}{@{}r@{\ }p{0.82\textwidth}@{}}
\S~1. & Cohomología de los esquemas afines.\\
\S~2. & Estudio cohomológico de los morfismos proyectivos.\\
\S~3. & El teorema de finitud para los morfismos propios.\\
\S~4. & El teorema fundamental de los morfismos propios; aplicaciones.\\
\S~5. & Un teorema de existencia de haces algebraicos coherentes.\\
\S~6. & Funtores Tor y Ext locales y globales; fórmula de Künneth.\\
\S~7. & Estudio del cambio de base en los funtores cohomológicos covariantes de Módulos.\\
\S~8. & El teorema de dualidad sobre los fibrados proyectivos.\\
\S~9. & Cohomología relativa y cohomología local; dualidad local.\\
\S~10. & Relaciones entre cohomología proyectiva y cohomología local. Técnica de compleción formal a lo largo de un divisor.\\
\S~11. & Grupos de Picard globales y locales\footnotemark.
\end{tabular}

\medskip
Este capítulo da los teoremas fundamentales sobre la cohomología de los haces algebraicos coherentes, con excepción de los que se deducen de la teoría de residuos (teoremas de dualidad), que serán objeto de un capítulo posterior. Entre los primeros, hay esencialmente seis teoremas fundamentales, que constituyen el objeto de los seis primeros parágrafos del presente capítulo. Estos resultados serán en lo sucesivo herramientas esenciales, incluso en cuestiones que no son de naturaleza propiamente cohomológica; el lector verá sus primeros ejemplos ya en el \S~4. El \S~7 da resultados de naturaleza más técnica, pero de uso constante en las aplicaciones. Finalmente, en los \S\S~8 a 11, desarrollaremos ciertos resultados, ligados a la dualidad de los haces coherentes, particularmente importantes para las aplicaciones, y que pueden exponerse antes de la teoría general de residuos.

\footnotetext{El capítulo IV no depende de los \S\S~8 a 11, y sin duda se publicará antes que estos últimos.}

\oldpage[III]{82}
El contenido de los \S\S~1 y 2 se debe a J.-P. Serre, y el lector constatará que solo hemos tenido que seguir la exposición de (FAC). Los \S\S~8 y 9 están igualmente inspirados por (FAC) (siendo, sin embargo, menos evidentes las transposiciones exigidas por los diferentes contextos). Finalmente, como hemos dicho en la Introducción, el \S~4 debe considerarse como la formulación, en lenguaje moderno, del «teorema de invariancia» fundamental de la «teoría de las funciones holomorfas» de Zariski.

Señalemos finalmente que los resultados del n\textsuperscript{o}~3.4 (y las proposiciones preliminares de (\textbf{0}, 13.4 a 13.7)) no se utilizarán en lo que sigue del cap.~III y pueden, por tanto, omitirse en una primera lectura.

\setcounter{section}{0}
'''
with Path('result/records/CAMBIOS_iii_manual.tsv').open('a') as o:
 wr=csv.writer(o,delimiter='\t')
 for layer in ['CURRENT','DIPLOMATIC']:
  p=Path(f'result/tree/repo/editions/III1_{layer}/EGA_III1_ES_{layer}_READER.tex');t=p.read_text();lo=t.index(r'\input{ega0/ega0-13}')+len(r'\input{ega0/ega0-13}');hi=t.index(r'\input{ega3/ega3-1}');old=t[lo:hi];p.write_text(t[:lo]+new+'\n'+t[hi:]);wr.writerow([str(p.relative_to('result')),'chapter III opening',old,new,'source fidelity; omitted §§6–7 headings and introductory sentences restored; inherited translator aside absent from source retained only in before record',f'EGA_ES_FINISH_1_FRANCES/fr/{layer.lower()}/BASE/native/ega3/ega3-1-fr.tex:chapter:III-fr'])
