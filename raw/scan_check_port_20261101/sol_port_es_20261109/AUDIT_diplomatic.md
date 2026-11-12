# Audit of Sol's decisions, Spanish EGA (diplomatic)

45 decision files

| decision | ok | doubtful |
|---|---:|---:|
| apply | 1990 | 4 |
| already | 2830 | 17 |
| not_applicable | 865 | 23 |
| unclear | 0 | 36 |
| None | 0 | 0 |

Skipped, no Spanish target (EGA III-2 in the diplomatic edition): 587
Doubtful by reason: {'already: en_old missing or not found': 2, "decision 'unclear'": 36, 'not_applicable for a textup+ fix': 4, 'apply: en_old not found exactly once on pages p-1..p+1': 4, 'already: the fix adds an emphasis but the quoted Spanish has none': 3, 'not_applicable for a emph~ fix': 6, 'not_applicable for a emph- fix': 13, 'already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement': 12}

## 1938 (II 54, other, decisions_diplomatic_003): already: en_old missing or not found
FR: '$\\widetilde{\\Gamma(U,\\mathcal{M})}$~;' -> '$(\\Gamma(U,\\mathcal{M}))\\supertilde$~;'
Sol: already | es_old 'el $\\sh{O}_{X_U}$-módulo cuasi-coherente $(\\Gamma(U,\\sh{M}))\\supertilde;' | es_new None | note None

## 2498 (II 75, other, decisions_diplomatic_004): decision 'unclear'
FR: '\\operatorname{GL}(n,\\mathcal{O}_Y)' -> '\\mathbf{GL}(n,\\mathcal{O}_Y)'
Sol: unclear | es_old None | es_new None | note 'El pasaje usa $\\GL(n,\\sh{O}_Y)$; sin la definición de \\GL no puedo comprobar si imprime GL en negrita.'

## 2877 (II 93, other, decisions_diplomatic_006): decision 'unclear'
FR: '3.7.1}) et\n(\\hyperref[II.4.4.1-fr]{4.4.1}))' -> '3.7.1} et\n\\hyperref[0.4.4.1-fr]{4.4.1})'
Sol: unclear | es_old None | es_new None | note 'La agrupación ya coincide, pero corregir la referencia de II.4.4.1 a 0.4.4.1 exigiría cambiar una clave de \\sref, prohibido por las instrucciones.'

## 2330 (II 96, textup+, decisions_diplomatic_006): not_applicable for a textup+ fix
FR: '(\\hyperref[II.1.2.7-fr]{1.2.7})' -> '\\textup{(\\hyperref[II.1.2.7-fr]{1.2.7})}'
Sol: not_applicable | es_old None | es_new None | note 'En el corolario 5.1.9 la traducción omite esta referencia; no hay un paréntesis correspondiente que poner en redonda.'

## 2423 (II 106, textup+, decisions_diplomatic_007): apply: en_old not found exactly once on pages p-1..p+1
FR: 'est réduit (resp.' -> 'est réduit \\textup{(resp.}'
Sol: apply | es_old 'Si $X$ es reducido (resp. irreducible, íntegro),' | es_new 'Si $X$ es reducido \\textup{(resp.} irreducible, íntegro),' | note None

## 3537 (II 178, emph+, decisions_diplomatic_012): already: the fix adds an emphasis but the quoted Spanish has none
FR: '9.2.2, a)}' -> '9.2.2, \\emph{a)}}'
Sol: already | es_old 'que es cuasicoherente \\sref[I]{I.9.2.2}[a].' | es_new None | note 'El apartado se expresa mediante la convención de referencias de \\sref.'

## 3663 (II 183, emph~, decisions_diplomatic_012): not_applicable for a emph~ fix
FR: '\\emph{produit}\n\\[\n  \\prod_{n\\geqslant 1}\\mathcal{L}^{\\otimes n}\n  =\\varprojlim_n\\pi_*(\\mathcal{J}/\\mathcal{J}^{n+1})\n\\]\n(puisque' -> '\\emph{produit}\n$\\prod_{n\\geqslant 1}\\mathcal{L}^{\\otimes n}=\\varprojlim_n\\pi_*(\\mathcal{J}/\\mathcal{J}^{n+1})$\n(puisque'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de fórmula desplegada a fórmula en línea.'

## 3328 (II 188, emph+, decisions_diplomatic_012): already: the fix adds an emphasis but the quoted Spanish has none
FR: '{4.5.2, a)}' -> '{4.5.2, \\emph{a)}}'
Sol: already | es_old 'En virtud del criterio~\\sref{II.4.5.2}[a],' | es_new None | note 'El apartado se expresa mediante la convención de referencias de \\sref.'

## 3933 (II 199, emph+, decisions_diplomatic_013): already: the fix adds an emphasis but the quoted Spanish has none
FR: '9.2.2, b)}' -> '9.2.2, \\emph{b)}}'
Sol: already | es_old "$\\sh{O}_{X'}$-módulo cuasi-coherente $\\sh{F}'$ \\sref[I]{I.9.2.2}[b]." | es_new None | note 'La letra se da mediante la macro de referencia de la edición.'

## 4025 (0\textsubscript{III} 5, other, decisions_diplomatic_015): decision 'unclear'
FR: 'signe $0_{\\mathrm I}$' -> 'signe $\\mathbf{0}_{\\mathrm I}$'
Sol: unclear | es_old None | es_new None | note 'La nota al pie que introduce la notación del capítulo 0 no aparece en las páginas españolas proporcionadas.'

## 4286 (0\textsubscript{III} 17, other, decisions_diplomatic_016): decision 'unclear'
FR: '\\operatorname{gr}_0(M)\\otimes' -> '\\operatorname{gr}_{\\mathbf{0}}(M)\\otimes'
Sol: unclear | es_old None | es_new None | note 'No se proporciona el texto español de (10.1.1.2).'

## 4287 (0\textsubscript{III} 17, other, decisions_diplomatic_016): decision 'unclear'
FR: '_{\\operatorname{gr}_0(A)}' -> '_{\\operatorname{gr}_0(A\\boldsymbol{)}}'
Sol: unclear | es_old None | es_new None | note 'No se proporciona el texto español de (10.1.1.2).'

## 4288 (0\textsubscript{III} 18, emph+, decisions_diplomatic_016): decision 'unclear'
FR: "vérifiée l'une des" -> "vérifiée l'\\emph{une} des"
Sol: unclear | es_old None | es_new None | note 'No se proporciona el texto español de (10.1.2).'

## 4289 (0\textsubscript{III} 18, emph~, decisions_diplomatic_016): decision 'unclear'
FR: 'anneau local\n    \\emph{noethérien}' -> 'anneau \\emph{local\n    noethérien}'
Sol: unclear | es_old None | es_new None | note 'Falta el pasaje español sobre los módulos sobre anillos locales noetherianos.'

## 4291 (0\textsubscript{III} 18, emph+, decisions_diplomatic_016): decision 'unclear'
FR: '$M$ un $B$-module de type fini' -> '$M$ un $B$-\\emph{module} de type fini'
Sol: unclear | es_old None | es_new None | note 'No se proporciona el texto español de (10.2.2).'

## 4292 (0\textsubscript{III} 18, emph+, decisions_diplomatic_016): decision 'unclear'
FR: 'comme $A$-module, les conditions' -> 'comme $A$-\\emph{module}, les conditions'
Sol: unclear | es_old None | es_new None | note 'No se proporciona el texto español de (10.2.2).'

## 4293 (0\textsubscript{III} 18, emph+, decisions_diplomatic_016): decision 'unclear'
FR: '{10.2.1}) sont équivalentes.' -> '{10.2.1}) sont \\emph{équivalentes}.'
Sol: unclear | es_old None | es_new None | note 'No se proporciona el texto español de (10.2.2).'

## 4322 (0\textsubscript{III} 22, other, decisions_diplomatic_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 6.2.3}' -> '{$\\mathbf{0}_{\\mathrm I}$, 6.2.3}'
Sol: unclear | es_old None | es_new None | note 'Falta el texto español de la sección 10 que contiene esta referencia.'

## 4323 (0\textsubscript{III} 22, other, decisions_diplomatic_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 6.6.2}' -> '{$\\mathbf{0}_{\\mathrm I}$, 6.6.2}'
Sol: unclear | es_old None | es_new None | note 'Falta el texto español de la sección 10 que contiene esta referencia.'

## 4324 (0\textsubscript{III} 22, other, decisions_diplomatic_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 6.5.2}' -> '{$\\mathbf{0}_{\\mathrm I}$, 6.5.2}'
Sol: unclear | es_old None | es_new None | note 'Falta el texto español de la sección 10 que contiene esta referencia.'

## 4325 (0\textsubscript{III} 22, other, decisions_diplomatic_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 7.2.12}' -> '{$\\mathbf{0}_{\\mathrm I}$, 7.2.12}'
Sol: unclear | es_old None | es_new None | note 'Falta el texto español de la sección 10 que contiene esta referencia.'

## 4326 (0\textsubscript{III} 22, other, decisions_diplomatic_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 7.2.8}' -> '{$\\mathbf{0}_{\\mathrm I}$, 7.2.8}'
Sol: unclear | es_old None | es_new None | note 'Falta el texto español de la sección 10 que contiene esta referencia.'

## 4327 (0\textsubscript{III} 22, emph+, decisions_diplomatic_016): decision 'unclear'
FR: 'noethérien. On sait' -> '\\emph{noethérien}. On sait'
Sol: unclear | es_old None | es_new None | note "Falta el pasaje español sobre el carácter noetheriano de $\\widehat A'$."

## 4328 (0\textsubscript{III} 22, other, decisions_diplomatic_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 6.2.1}' -> '{$\\mathbf{0}_{\\mathrm I}$, 6.2.1}'
Sol: unclear | es_old None | es_new None | note 'Falta el texto español de la sección 10 que contiene esta referencia.'

## 4329 (0\textsubscript{III} 22, emph+, decisions_diplomatic_016): decision 'unclear'
FR: 'est $A_\\lambda$-plat. C.Q.F.D.' -> 'est $A_\\lambda$-\\emph{plat}. C.Q.F.D.'
Sol: unclear | es_old None | es_new None | note "Falta el pasaje español sobre la planitud de $\\widehat A'$."

## 4330 (0\textsubscript{III} 22, other, decisions_diplomatic_016): decision 'unclear'
FR: '\\xi\\mapsto t_\\xi' -> '\\xi\\to t_\\xi'
Sol: unclear | es_old None | es_new None | note 'No se proporciona el texto español de (10.3.1.4).'

## 4331 (0\textsubscript{III} 22, other, decisions_diplomatic_016): decision 'unclear'
FR: "$f_{\\xi\\zeta}$ est l'application canonique" -> "$f_{\\zeta\\xi}$ est l'application canonique"
Sol: unclear | es_old None | es_new None | note 'Falta la construcción española de los morfismos $f_{\\zeta\\xi}$.'

## 4332 (0\textsubscript{III} 23, other, decisions_diplomatic_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 7.3.3}' -> '{$\\mathbf{0}_{\\mathrm I}$, 7.3.3}'
Sol: unclear | es_old None | es_new None | note 'Falta el texto español anterior a la sección 11 que contiene esta referencia.'

## 4333 (0\textsubscript{III} 23, other, decisions_diplomatic_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 6.2.1}' -> '{$\\mathbf{0}_{\\mathrm I}$, 6.2.1}'
Sol: unclear | es_old None | es_new None | note 'Falta el texto español de la sección 10 que contiene esta referencia.'

## 4344 (0\textsubscript{III} 23, other, decisions_diplomatic_016): apply: en_old not found exactly once on pages p-1..p+1
FR: '\\item[(e)]' -> '\\item[$e)$]'
Sol: apply | es_old '  \\item[(e)]\n\\oldpage[0\\textsubscript{III}]{24}\n    Una familia' | es_new '  \\item[$(e)$]\n\\oldpage[0\\textsubscript{III}]{24}\n    Una familia' | note 'Se conserva la forma española de la etiqueta y no se modifica el marcador de página.'

## 4407 (0\textsubscript{III} 28, emph+, decisions_diplomatic_016): already: en_old missing or not found
FR: 'objets gradués de $K^\\bullet$' -> 'objets \\emph{gradués} de $K^\\bullet$'
Sol: already | es_old 'formada por subobjetos \\emph{graduados}\n\\oldpage[0\\textsubscript{III}]{28}\nde $K^\\bullet$' | es_new None | note None

## 4496 (0\textsubscript{III} 34, emph~, decisions_diplomatic_017): not_applicable for a emph~ fix
FR: 'le $p$-ième \\emph{foncteur' -> 'le $p$\\textsuperscript{e} \\emph{foncteur'
Sol: not_applicable | es_old None | es_new None | note 'Forma del ordinal francés; el español dice «de grado p».'

## 4960 (0\textsubscript{III} 42, emph-, decisions_diplomatic_018): not_applicable for a emph- fix
FR: '\\begin{env}[11.7.3]\n\\label{0.11.7.3-fr}\n\\emph{Remarques}.\n' -> '\\begin{remarks}[11.7.3]\n\\label{0.11.7.3-fr}\n\\upshape\n'
Sol: not_applicable | es_old None | es_new None | note 'Cambio del entorno francés; se conserva la estructura editorial española.'

## 5491 (0\textsubscript{III} 67, emph~, decisions_diplomatic_020): not_applicable for a emph~ fix
FR: '\\emph{Remarques} (13.2.4).' -> '\\emph{Remarques} (13.2.4). ---'
Sol: not_applicable | es_old None | es_new None | note 'Separador tipográfico tras el encabezamiento de observaciones.'

## 5523 (0\textsubscript{III} 68, emph-, decisions_diplomatic_021): not_applicable for a emph- fix
FR: "montrons qu'il satisfait aux conditions de\n\\emph{a)}.\n" -> 'montrons\n'
Sol: not_applicable | es_old None | es_new None | note 'Redistribución del texto alrededor del salto de página francés.'

## 5539 (0\textsubscript{III} 69, emph~, decisions_diplomatic_021): not_applicable for a emph~ fix
FR: '\\emph{Remarques} (13.3.2).' -> '\\emph{Remarques} (13.3.2). ---'
Sol: not_applicable | es_old None | es_new None | note 'Separador tipográfico del encabezamiento francés.'

## 5195 (0\textsubscript{III} 72, textup+, decisions_diplomatic_021): not_applicable for a textup+ fix
FR: '(la flèche verticale de droite provenant du\nmorphisme $X_{p+s-1}^\\bullet\\to X_{p+r-1}^\\bullet$)' -> '\\textup{(la flèche verticale de droite provenant du\nmorphisme $X_{p+s-1}^\\bullet\\to X_{p+r-1}^\\bullet$)}'
Sol: not_applicable | es_old None | es_new None | note 'El español integra la explicación con «donde», sin paréntesis.'

## 5272 (0\textsubscript{III} 76, emph-, decisions_diplomatic_021): not_applicable for a emph- fix
FR: '\\qquad\\emph{pour tout $p\\in\\mathbb Z$.}\n\\end{equation}\n\\end{proposition}' -> '\\qquad\\textit{pour tout $p\\in\\mathbb Z$.}\n\\end{equation}\n\\end{proposition}'
Sol: not_applicable | es_old None | es_new None | note 'El español usa únicamente la condición matemática entre paréntesis, sin la frase francesa.'

## 5282 (0\textsubscript{III} 76, emph-, decisions_diplomatic_021): not_applicable for a emph- fix
FR: '\\qquad\\emph{pour tout $p\\in\\mathbb Z$.}\n\\end{equation}\n\\end{corollary}' -> '\\qquad\\textit{pour tout $p\\in\\mathbb Z$.}\n\\end{equation}\n\\end{corollary}'
Sol: not_applicable | es_old None | es_new None | note 'El español usa únicamente la condición matemática entre paréntesis, sin la frase francesa.'

## 5324 (0\textsubscript{III} 79, emph~, decisions_diplomatic_022): not_applicable for a emph~ fix
FR: '\\end{enumerate}\nPour la démonstration, voir Bourbaki, \\emph{Alg. comm.}, chap.~III, \\S~3,\nn\\textsuperscript{o}~1, prop.~3.\n\\end{lemma}' -> '\\end{enumerate}\n\\end{lemma}\nPour la démonstration, voir Bourbaki, \\emph{Alg. comm.}, chap.~III, \\S~3,\nn\\textsuperscript{o}~1, prop.~3.'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de ubicación respecto al entorno lemma; no se altera la estructura española.'

## 6060 (III 96, other, decisions_diplomatic_022): decision 'unclear'
FR: '\\providecommand{\\shProj}{\\mathcal{P}\\mathrm{roj}}' -> '\\providecommand{\\shProj}{\\mathcal{P}\\mathit{roj}}'
Sol: unclear | es_old None | es_new None | note 'No aparece la definición de \\shProj ni un uso correspondiente en los textos españoles suministrados.'

## 5441 (III 99, textup+, decisions_diplomatic_023): not_applicable for a textup+ fix
FR: '$i=r$ et $n\\leq-(r+1)$.' -> '$i=r$ \\textup{et} $n\\leq-(r+1)$.'
Sol: not_applicable | es_old None | es_new None | note 'El español separa los valores mediante comas; no contiene la conjunción francesa que se endereza.'

## 5988 (III 104, other, decisions_diplomatic_023): decision 'unclear'
FR: '\\text{dans }K_{\\mathcal S}' -> '\\text{dans }\\boldsymbol{K}_{\\mathcal S}'
Sol: unclear | es_old None | es_new None | note 'La fórmula española omite la indicación de dominio «en K_S»; no hay allí un símbolo K al que trasladar la negrita.'

## 5991 (III 104, other, decisions_diplomatic_023): decision 'unclear'
FR: '\\text{dans }K_X' -> '\\text{dans }\\boldsymbol{K}_X'
Sol: unclear | es_old None | es_new None | note 'La fórmula española omite la indicación de dominio «en K_X»; no hay allí un símbolo K al que trasladar la negrita.'

## 5705 (III 115, emph-, decisions_diplomatic_025): not_applicable for a emph- fix
FR: '\\begin{env}[2.6.3]\n\\label{III.2.6.3-fr}\n\\emph{Remarque.}' -> '\\begin{remark}[2.6.3]\n\\label{III.2.6.3-fr}\n\\upshape'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de entorno francés; se conserva la estructura española.'

## 6308 (III 125, textup+, decisions_diplomatic_026): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'diagramme\n(\\hyperref[III.4.1.4.2-fr]{4.1.4.2}) sont' -> 'diagramme\n\\textup{(\\hyperref[III.4.1.4.2-fr]{4.1.4.2})} sont'
Sol: already | es_old '\\eqref{III.4.1.4.2} son isomorfismos topológicos.' | es_new None | note '\\eqref imprime la referencia y sus paréntesis en redonda.'

## 6312 (III 125, emph-, decisions_diplomatic_026): not_applicable for a emph- fix
FR: '\\begin{env}[4.1.6]\n\\label{III.4.1.6-fr}\n\\emph{Remarques.}\n' -> '\\begin{remarks}[4.1.6]\n\\label{III.4.1.6-fr}\n\\upshape\n'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de entorno y presentación de las observaciones; no se altera la estructura española.'

## 6338 (III 126, other, decisions_diplomatic_026): decision 'unclear'
FR: '\\mathcal F\\ar[r]_x&\\mathcal F\n}\n\\tag{4.1.7.11}\\label{III.4.1.7.11-fr}\n\\]\n\n' -> '\\mathcal F\\ar[r]_x&\\mathcal F\n}\n\\]\n'
Sol: unclear | es_old None | es_new None | note 'El número 4.1.7.11 debe pasar al diagrama siguiente junto con su etiqueta; trasladar la etiqueta está prohibido por las reglas.'

## 6168 (III 127, other, decisions_diplomatic_026): decision 'unclear'
FR: 'H^n(X,\\mathcal F)\\ar[r]_{\\mu_{x,0}}&H^n(X,\\mathcal F)\n}\n\\]' -> 'H^n(X,\\mathcal F)\\ar[r]_{\\mu_{x,0}}&H^n(X,\\mathcal F)\n}\n\\tag{4.1.7.11}\\label{III.4.1.7.11-fr}\n\\]'
Sol: unclear | es_old None | es_new None | note 'Complementa 6338: trasladar correctamente el número al diagrama cohomológico exige también trasladar la etiqueta, operación prohibida.'

## 6199 (III 129, emph-, decisions_diplomatic_026): not_applicable for a emph- fix
FR: '\\begin{env}[4.1.10]\n\\label{III.4.1.10-fr}\n\\emph{Remarque.}\n' -> '\\begin{remark}[4.1.10]\n\\label{III.4.1.10-fr}\n\\upshape\n'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de entorno y presentación de la observación; no se altera la estructura española.'

## 6085 (III 132, emph-, decisions_diplomatic_027): not_applicable for a emph- fix
FR: '\\emph{unibranche}' -> 'unibranche'
Sol: not_applicable | es_old None | es_new None | note 'La edición española destaca los términos definidos mediante su propia convención tipográfica.'

## 6101 (III 133, emph-, decisions_diplomatic_027): not_applicable for a emph- fix
FR: '\\emph{universellement ouvert}' -> 'universellement ouvert'
Sol: not_applicable | es_old None | es_new None | note 'La edición española destaca los términos definidos mediante su propia convención tipográfica.'

## 6102 (III 133, other, decisions_diplomatic_027): decision 'unclear'
FR: '(0\\textsubscript{I}, 2.1.8)~; cela' -> '(\\textbf{0}\\textsubscript{I}, 2.1.8)~; cela'
Sol: unclear | es_old None | es_new None | note 'El párrafo español correspondiente omite la referencia a 0, 2.1.8; no hay allí una referencia cuya tipografía pueda comprobarse.'

## 6106 (III 133, other, decisions_diplomatic_027): decision 'unclear'
FR: "$X'=X\\times_YY'$, $f'=f\\times1_{Y'}$~; désignons par $\\eta$, $\\eta'$,\n$\\xi$ les points génériques de $Y$, $Y'$ et $X$ respectivement, de sorte\nque $f(\\xi)=\\eta$ et $h^{-1}(\\eta)=\\{\\eta'\\}$~; en outre,\n$k(\\eta)=k(\\eta')=\\mathrm R(Y)$, donc $f'^{-1}(\\eta')$ est isomorphe à\n$f^{-1}(\\eta)$ (I, 3.6.4) et en particulier, puisque $\\xi$ est le point\ngénérique de $f^{-1}(\\eta)$ (0\\textsubscript{I}, 2.1.8),\n$f'^{-1}(\\eta')$ a un seul point générique. Mais par hypothèse, toute\ncomposante irréductible de $X'$ a son point générique dans\n$f'^{-1}(\\eta')$, donc $X'$ est nécessairement irréductible, son point\ngénérique $\\xi'$ est le point générique de $f'^{-1}(\\eta')$ et on a\n$k(\\xi')=k(\\xi)$.\n\n" -> ''
Sol: unclear | es_old None | es_new None | note 'La eliminación afecta a un paso esencial de la prueba, pero el contexto corregido de 6109 conserva su conclusión. No es seguro si se trata de una supresión o de un traslado de página.'

## 6623 (III 139, textup+, decisions_diplomatic_028): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'de (\\hyperref[III.4.2.1.1-fr]{4.2.1.1}) est surjectif.' -> '\\textup{(\\hyperref[III.4.2.1.1-fr]{4.2.1.1})} est surjectif.'
Sol: already | es_old '\\eqref{III.4.2.1.1} es sobreyectivo.' | es_new None | note '\\eqref ya imprime la referencia y sus paréntesis en redonda.'

## 6434 (III 150, emph-, decisions_diplomatic_031): not_applicable for a emph- fix
FR: '\\begin{env}[5.1.7]\n\\label{III.5.1.7-fr}\n\\emph{Scholie.}\n' -> '\\begin{scholium}[5.1.7]\n\\label{III.5.1.7-fr}\n'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de entorno; el español ya identifica el escolio y debe conservar su estructura.'

## 6670 (III 153, emph-, decisions_diplomatic_032): not_applicable for a emph- fix
FR: "\\emph{Démonstration du théorème d'existence : cas projectif.}" -> "\\textbf{Démonstration du théorème d'existence : cas projectif.}"
Sol: not_applicable | es_old None | es_new None | note 'Cambio de estilo tipográfico del encabezado.'

## 6682 (III 153, emph-, decisions_diplomatic_032): not_applicable for a emph- fix
FR: "\\emph{Démonstration du théorème d'existence; cas quasi-projectif.}" -> "\\textbf{Démonstration du théorème d'existence; cas quasi-projectif.}"
Sol: not_applicable | es_old None | es_new None | note 'Cambio de estilo tipográfico del encabezado.'

## 6781 (III 157, emph-, decisions_diplomatic_033): not_applicable for a emph- fix
FR: '\\begin{env}[5.4.2]\n\\label{III.5.4.2-fr}\n\\emph{Scholie.}\n' -> '\\begin{scholium}[5.4.2]\n\\label{III.5.4.2-fr}\n'
Sol: not_applicable | es_old None | es_new None | note 'La edición española ya identifica el escolio; no se cambia su estructura de entornos.'

## 8971 (0\textsubscript{IV-1} 5, other, decisions_diplomatic_035): decision 'unclear'
FR: 'CHAPITRE 0 (suite)' -> 'CHAPITRE 0 \\textit{(suite)}'
Sol: unclear | es_old None | es_new None | note 'The Spanish chapter heading on page 5 is not supplied.'

## 8972 (0\textsubscript{IV-1} 5, other, decisions_diplomatic_035): decision 'unclear'
FR: 'symbole $0' -> 'symbole $\\mathbf{0}'
Sol: unclear | es_old None | es_new None | note 'The Spanish footnote on page 5 is not supplied.'

## 8973 (0\textsubscript{IV-1} 5, other, decisions_diplomatic_035): decision 'unclear'
FR: '_N$ (resp.' -> '_{\\mathrm N}$ (resp.'
Sol: unclear | es_old None | es_new None | note 'The Spanish footnote on page 5 is not supplied.'

## 8974 (0\textsubscript{IV-1} 5, other, decisions_diplomatic_035): decision 'unclear'
FR: '$\\operatorname{Err}_N$' -> '$\\mathbf{Err}_{\\mathrm N}$'
Sol: unclear | es_old None | es_new None | note 'The Spanish footnote on page 5 is not supplied.'

## 8975 (0\textsubscript{IV-1} 5, other, decisions_diplomatic_035): decision 'unclear'
FR: 'chapitre 0 (resp.' -> 'chapitre \\textbf{0} (resp.'
Sol: unclear | es_old None | es_new None | note 'The Spanish footnote on page 5 is not supplied.'

## 8976 (0\textsubscript{IV-1} 5, other, decisions_diplomatic_035): decision 'unclear'
FR: 'jointe au chapitre\n$N$.}' -> 'jointe au chapitre\nN.}'
Sol: unclear | es_old None | es_new None | note 'The Spanish footnote on page 5 is not supplied.'

## 8628 (0\textsubscript{IV-1} 41, textup+, decisions_diplomatic_037): not_applicable for a textup+ fix
FR: 'mod. $\\mathfrak{m}^2$ sont' -> '\\textup{mod.} $\\mathfrak{m}^2$ sont'
Sol: not_applicable | es_old None | es_new None | note 'La redonda afecta a la abreviatura francesa «mod.»; el español escribe «módulo» sin abreviar.'

## 9133 (0\textsubscript{IV-1} 61, emph~, decisions_diplomatic_037): not_applicable for a emph~ fix
FR: '\\emph{homomorphisme de groupes}.\n\\end{env}' -> '\\emph{homomorphisme de groupes}.'
Sol: not_applicable | es_old None | es_new None | note 'Cambio del límite de un entorno; se conserva la estructura española exigida.'

## 9134 (0\textsubscript{IV-1} 62, other, decisions_diplomatic_037): decision 'unclear'
FR: "\\begin{env}[18.3.6.4]\n\\label{0.18.3.6.4-fr}\nEnfin, l'application $(u,1_B,1_L)_*$ est l'application\n\\[\n  u^*:\\operatorname{Exan}_A(B,L)\\longrightarrow\n  \\operatorname{Exan}_{A'}(B,L)\n\\]" -> "Enfin, l'application $(u,1_B,1_L)_*$ est l'application\n\\begin{equation}\n\\label{0.18.3.6.4-fr}\n\\tag{18.3.6.4}\n  u^*:\\operatorname{Exan}_A(B,L)\\longrightarrow\n  \\operatorname{Exan}_{A'}(B,L)\n\\end{equation}"
Sol: unclear | es_old None | es_new None | note 'La fórmula carece de la numeración indicada, pero la corrección completa exige quitar el entorno y trasladar label, cambios prohibidos por las reglas.'

## 9454 (0\textsubscript{IV-1} 105, other, decisions_diplomatic_040): apply: en_old not found exactly once on pages p-1..p+1
FR: "\\varprojlim_j\n  ((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n'{}^j))" -> '\\varprojlim_j\n  ((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n^j))'
Sol: apply | es_old "\\varprojlim_j\n  ((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n'{}^j))\\right)~;\n\\]\n\\oldpage[0\\textsubscript{IV-1}]{106}\n\npero $\\varprojlim_j((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n'{}^j))$ es el" | es_new '\\varprojlim_j\n  ((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n^j))\\right)~;\n\\]\n\\oldpage[0\\textsubscript{IV-1}]{106}\n\npero $\\varprojlim_j((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n^j))$ es el' | note 'La repetición inmediata se ajusta también al contexto francés corregido; el marcador queda intacto.'

## 9954 (0\textsubscript{IV-1} 120, textup+, decisions_diplomatic_040): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'suite exacte \\sref{0.20.2.2.1-fr}' -> 'suite exacte \\textup{\\sref{0.20.2.2.1-fr}}'
Sol: already | es_old 'Además, la sucesión exacta \\sref{0.20.2.2.1-es} es' | es_new None | note '\\sref ya imprime la referencia en redonda.'

## 10370 (0\textsubscript{IV-1} 130, textup+, decisions_diplomatic_040): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'canonique \\sref{0.20.5.4.1-fr}' -> 'canonique \\textup{\\sref{0.20.5.4.1-fr}}'
Sol: already | es_old 'el homomorfismo canónico \\sref{0.20.5.4.1-es}' | es_new None | note '\\sref ya imprime la referencia en redonda.'

## 10283 (0\textsubscript{IV-1} 146, textup+, decisions_diplomatic_041): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'Sous les hypothèses de \\sref{0.20.6.22-fr}, supposons' -> 'Sous les hypothèses de \\textup{\\sref{0.20.6.22-fr}}, supposons'
Sol: already | es_old 'Bajo las hipótesis de \\sref{0.20.6.22-es}, supongamos además que $B$ sea' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 10300 (0\textsubscript{IV-1} 147, textup+, decisions_diplomatic_041): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '\\sref{0.19.9.1-fr}' -> '\\textup{\\sref{0.19.9.1-fr}}'
Sol: already | es_old 'sea una $B$-álgebra formalmente lisa respecto de $A$\n\\sref{0.19.9.1-es}' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 10305 (0\textsubscript{IV-1} 148, textup+, decisions_diplomatic_041): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '\\sref{0.19.10.2-fr}' -> '\\textup{\\sref{0.19.10.2-fr}}'
Sol: already | es_old '$B$ sea formalmente no ramificada \\sref{0.19.10.2-es}, es necesario y suficiente' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 10313 (0\textsubscript{IV-1} 148, textup+, decisions_diplomatic_041): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'bimorphisme formel \\sref{0.19.1.2-fr}' -> 'bimorphisme formel \\textup{\\sref{0.19.1.2-fr}}'
Sol: already | es_old 'bimorfismo formal \\sref{0.19.1.2-es}.' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 10315 (0\textsubscript{IV-1} 149, textup+, decisions_diplomatic_041): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: "l'homomorphisme \\sref{0.20.7.3.1-fr} est" -> "l'homomorphisme \\textup{\\sref{0.20.7.3.1-fr}} est"
Sol: already | es_old '$\\mathfrak K_\\lambda$ de $C$, el homomorfismo \\sref{0.20.7.3.1-es} es' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 10317 (0\textsubscript{IV-1} 149, textup+, decisions_diplomatic_041): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'Dans la suite exacte \\sref{0.20.5.12.1-fr}' -> 'Dans la suite exacte \\textup{\\sref{0.20.5.12.1-fr}}'
Sol: already | es_old 'En la sucesión exacta \\sref{0.20.5.12.1-es}' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 10319 (0\textsubscript{IV-1} 149, textup+, decisions_diplomatic_041): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'gauche \\sref{0.19.1.5-fr}, il faut' -> 'gauche \\textup{\\sref{0.19.1.5-fr}}, il faut'
Sol: already | es_old 'izquierda \\sref{0.19.1.5-es}, es necesario y suficiente' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 10489 (0\textsubscript{IV-1} 153, textup+, decisions_diplomatic_041): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '\\sref{0.20.7.18-fr}, si' -> '\\textup{\\sref{0.20.7.18-fr}}, si'
Sol: already | es_old 'Bajo las hipótesis de \\sref{0.20.7.18-es}, supongamos además que en $B$ y' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 11085 (0\textsubscript{IV-1} 210, other, decisions_diplomatic_045): apply: en_old not found exactly once on pages p-1..p+1
FR: '(\\langle F_i,D_j\\otimes1\\rangle)' -> '(\\mathopen{<}F_i,D_j\\otimes1\\mathclose{>})'
Sol: apply | es_old "$(\\langle F_i,D_j\\otimes1\\rangle)$ es invertible; por tanto, esto implica que los\n$F_i$ son linealmente independientes, y \\emph{a fortiori} que ocurre lo\nmismo con los $f'_i\\otimes1$; pero como estos últimos engendran\n$(\\mathfrak qA_{\\mathfrak p}/\\mathfrak q^2A_{\\mathfrak p})\n\\otimes_{A_{\\mathfrak p}}L$, se concluye que $j$ es inyectivo. Recíprocamente,\nsupongamos $j$ inyectivo, y tomemos los $f_i$ de modo que los $f'_i\\otimes1$\nformen\n\\oldpage[0\\textsubscript{IV-1}]{210}\n\nuna base de\n$(\\mathfrak qA_{\\mathfrak p}/\\mathfrak q^2A_{\\mathfrak p})\n\\otimes_{A_{\\mathfrak p}}L$; entonces los $F_i$ forman una base de la imagen de\n$j$; pero se sabe (21.9.3) que $\\widehat\\Omega^1_{A/k}$ es un $A$-módulo\nlibre de rango $r$ y que las $k$-derivaciones de $A$ en sí mismo engendran su\ndual; el hecho de que los $F_i$ sean linealmente independientes implica, pues,\nla existencia de $k$-derivaciones $D_i$ de $A$ en sí mismo tales que la matriz\n$(\\langle F_i,D_j\\otimes1\\rangle)$ sea invertible, es decir, la condición\nb)." | es_new "$(\\mathopen{<}F_i,D_j\\otimes1\\mathclose{>})$ es invertible; por tanto, esto implica que los\n$F_i$ son linealmente independientes, y \\emph{a fortiori} que ocurre lo\nmismo con los $f'_i\\otimes1$; pero como estos últimos engendran\n$(\\mathfrak qA_{\\mathfrak p}/\\mathfrak q^2A_{\\mathfrak p})\n\\otimes_{A_{\\mathfrak p}}L$, se concluye que $j$ es inyectivo. Recíprocamente,\nsupongamos $j$ inyectivo, y tomemos los $f_i$ de modo que los $f'_i\\otimes1$\nformen\n\\oldpage[0\\textsubscript{IV-1}]{210}\n\nuna base de\n$(\\mathfrak qA_{\\mathfrak p}/\\mathfrak q^2A_{\\mathfrak p})\n\\otimes_{A_{\\mathfrak p}}L$; entonces los $F_i$ forman una base de la imagen de\n$j$; pero se sabe (21.9.3) que $\\widehat\\Omega^1_{A/k}$ es un $A$-módulo\nlibre de rango $r$ y que las $k$-derivaciones de $A$ en sí mismo engendran su\ndual; el hecho de que los $F_i$ sean linealmente independientes implica, pues,\nla existencia de $k$-derivaciones $D_i$ de $A$ en sí mismo tales que la matriz\n$(\\mathopen{<}F_i,D_j\\otimes1\\mathclose{>})$ sea invertible, es decir, la condición\n\\emph{b)}." | note 'Incluye ambas apariciones de la matriz y 11086.'
