# Audit of Sol's decisions, Spanish EGA (current)

82 decision files

| decision | ok | doubtful |
|---|---:|---:|
| apply | 5793 | 14 |
| already | 3820 | 98 |
| not_applicable | 1744 | 52 |
| unclear | 0 | 106 |
| None | 0 | 0 |

Skipped, no Spanish target (EGA III-2 in the diplomatic edition): 0
Doubtful by reason: {"decision 'unclear'": 106, 'apply: en_old not found exactly once on pages p-1..p+1': 14, 'already: en_old missing or not found': 12, 'not_applicable for a textup+ fix': 13, 'already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement': 81, 'already: the fix adds an emphasis but the quoted Spanish has none': 5, 'not_applicable for a emph~ fix': 21, 'not_applicable for a emph- fix': 15, 'not_applicable for a emph+ fix': 3}

## 1967 (II 10, other, decisions_current_001): decision 'unclear'
FR: '{I, 9.6.2}' -> '{\\textbf{I}, 9.6.2}'
Sol: unclear | es_old None | es_new None | note 'La referencia a I, 9.6.2 que corresponde aquí a la prueba de 1.4.5 no figura en el pasaje español.'

## 2003 (II 12, other, decisions_current_001): apply: en_old not found exactly once on pages p-1..p+1
FR: '\\operatorname{Spec}(k(s))' -> '\\operatorname{Spec}(\\boldsymbol{k}(s))'
Sol: apply | es_old "$S'=\\Spec(\\kres(s))$" | es_new "$S'=\\Spec(\\boldsymbol{\\kres}(s))$" | note None

## 1554 (II 23, emph+, decisions_current_001): already: en_old missing or not found
FR: 'est un idéal gradué~: en passant' -> 'est un idéal \\emph{gradué}~: en passant'
Sol: already | es_old 'es un ideal \\emph{gradué}' | es_new None | note ''

## 1800 (II 44, other, decisions_current_002): already: en_old missing or not found
FR: "\\widetilde{M_{[\\varphi]}}|D_+(f'g')" -> "(M_{[\\varphi]})\\supertilde|D_+(f'g')"
Sol: already | es_old "$(M_{[\\vphi]})\\supertilde|D_+(f'g') \\simto (\\Phi_{fg})_*(\\widetilde{M}|D_+(fg))$" | es_new None | note None

## 2052 (II 54, other, decisions_current_003): already: en_old missing or not found
FR: '$\\widetilde{\\Gamma(U,\\mathcal{M})}$~;' -> '$(\\Gamma(U,\\mathcal{M}))\\supertilde$~;'
Sol: already | es_old 'el $\\sh{O}_{X_U}$-módulo cuasi-coherente $(\\Gamma(U,\\sh{M}))\\supertilde;' | es_new None | note None

## 2576 (II 75, other, decisions_current_004): already: en_old missing or not found
FR: '\\otimes_{k(y)}K$.' -> '\\otimes_{\\boldsymbol{k}(y)}K$.'
Sol: already | es_old 'el \\emph{dual} del espacio vectorial sobre $K$ $\\sh{E}^y\\otimes_{\\kres(y)}K$.' | es_new None | note None

## 5507 (II 75, other, decisions_current_004): decision 'unclear'
FR: '[III.2.1.14-fr]{III,' -> '[III.2.1.14-fr]{\\textbf{III},'
Sol: unclear | es_old None | es_new None | note 'No aparece ninguna referencia a III.2.1.14 en las páginas españolas del bloque.'

## 2598 (II 76, other, decisions_current_004): already: en_old missing or not found
FR: '[I.1.3.12-fr]{I,' -> '[I.1.3.12-fr]{\\textbf{I},'
Sol: already | es_old '$(E\\otimes_A F)^\\sim$ \\sref[I]{I.1.3.12}' | es_new None | note None

## 3157 (II 80, other, decisions_current_004): decision 'unclear'
FR: '{I, 9.5.11}' -> '{\\textbf{I}, 9.5.11}'
Sol: unclear | es_old None | es_new None | note 'No aparece I.9.5.11; en la demostración de 4.4.7 se cita I.9.5.10.'

## 5509 (II 80, textup+, decisions_current_004): decision 'unclear'
FR: 'Module cohérent de type\n  fini $\\mathcal{E}$ de' -> 'Module cohérent \\textup{de type\n  fini} $\\mathcal{E}$ de'
Sol: unclear | es_old None | es_new None | note "Sin contexto no se identifica un módulo coherente de tipo finito en estas páginas; el de 4.4.6 (b') dice cuasi-coherente y ya lleva énfasis."

## 2948 (II 93, other, decisions_current_006): decision 'unclear'
FR: '3.7.1}) et\n(\\hyperref[II.4.4.1-fr]{4.4.1}))' -> '3.7.1} et\n\\hyperref[0.4.4.1-fr]{4.4.1})'
Sol: unclear | es_old None | es_new None | note 'La referencia debe pasar de II.4.4.1 a 0.4.4.1, pero se prohíbe cambiar las claves de \\sref.'

## 2421 (II 96, textup+, decisions_current_006): not_applicable for a textup+ fix
FR: '(\\hyperref[II.1.2.7-fr]{1.2.7})' -> '\\textup{(\\hyperref[II.1.2.7-fr]{1.2.7})}'
Sol: not_applicable | es_old None | es_new None | note 'En 5.1.9 el español omite esta referencia; no hay paréntesis que poner en recta.'

## 5511 (II 130, textup+, decisions_current_009): decision 'unclear'
FR: '(\\hyperref[II.6.5.5.1-fr]{6.5.5.1})' -> '\\textup{(\\hyperref[II.6.5.5.1-fr]{6.5.5.1})}'
Sol: unclear | es_old None | es_new None | note 'No aparece una referencia a (6.5.5.1) en las páginas españolas del bloque.'

## 3255 (II 132, textup+, decisions_current_009): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '($1\\leq i\\leq n$)' -> '\\textup{($1\\leq i\\leq n$)}'
Sol: already | es_old '\\qquad(1\\leq i\\leq n)' | es_new None | note 'Los paréntesis ya son rectos en modo matemático.'

## 3578 (II 178, emph+, decisions_current_012): already: the fix adds an emphasis but the quoted Spanish has none
FR: '9.2.2, a)}' -> '9.2.2, \\emph{a)}}'
Sol: already | es_old 'que es cuasicoherente \\sref[I]{I.9.2.2}[a].' | es_new None | note 'Se conserva la macro española para la referencia al apartado.'

## 3590 (II 179, emph~, decisions_current_012): not_applicable for a emph~ fix
FR: "\\emph{l'image réciproque}" -> "l'\\emph{image réciproque}"
Sol: not_applicable | es_old None | es_new None | note 'Ajuste del artículo elidido francés; el artículo español ya queda fuera del énfasis.'

## 3698 (II 183, emph~, decisions_current_012): not_applicable for a emph~ fix
FR: '\\emph{produit}\n\\[\n  \\prod_{n\\geqslant 1}\\mathcal{L}^{\\otimes n}\n  =\\varprojlim_n\\pi_*(\\mathcal{J}/\\mathcal{J}^{n+1})\n\\]\n(puisque' -> '\\emph{produit}\n$\\prod_{n\\geqslant 1}\\mathcal{L}^{\\otimes n}=\\varprojlim_n\\pi_*(\\mathcal{J}/\\mathcal{J}^{n+1})$\n(puisque'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de fórmula desplegada a fórmula en línea.'

## 3377 (II 188, emph+, decisions_current_012): already: the fix adds an emphasis but the quoted Spanish has none
FR: '{4.5.2, a)}' -> '{4.5.2, \\emph{a)}}'
Sol: already | es_old 'En virtud del criterio~\\sref{II.4.5.2}[a],' | es_new None | note 'Se conserva la macro española para la referencia al apartado.'

## 3962 (II 199, emph+, decisions_current_013): already: the fix adds an emphasis but the quoted Spanish has none
FR: '9.2.2, b)}' -> '9.2.2, \\emph{b)}}'
Sol: already | es_old '\\sref[I]{I.9.2.2}[b]' | es_new None | note 'El inciso se compone mediante el macro español de referencias.'

## 5514 (II 221, textup+, decisions_current_014): decision 'unclear'
FR: 'canonique (1.8.8.1) soit' -> 'canonique \\textup{(1.8.8.1)} soit'
Sol: unclear | es_old None | es_new None | note 'No aparece «aplicación canónica (1.8.8.1)» en el pasaje; el corolario remite a (1.8.9.1), ya tratado en 5513.'

## 4050 (0\textsubscript{III} 5, other, decisions_current_015): decision 'unclear'
FR: 'signe $0_{\\mathrm I}$' -> 'signe $\\mathbf{0}_{\\mathrm I}$'
Sol: unclear | es_old None | es_new None | note 'The introductory footnote containing this notation is absent from the supplied Spanish text.'

## 4130 (0\textsubscript{III} 9, other, decisions_current_015): already: en_old missing or not found
FR: 'dans\n$C$, on pose' -> 'dans\n$\\boldsymbol{C}$, on pose'
Sol: already | es_old "para todo morfismo $u:Y\\to Y'$ de $\\C$, ponemos $(F\\times F')(u)$" | es_new None | note None

## 4305 (0\textsubscript{III} 18, emph+, decisions_current_015): decision 'unclear'
FR: "vérifiée l'une des" -> "vérifiée l'\\emph{une} des"
Sol: unclear | es_old None | es_new None | note 'The Spanish text of page 18, including 10.1.2, was not supplied.'

## 4306 (0\textsubscript{III} 18, emph~, decisions_current_015): decision 'unclear'
FR: 'anneau local\n    \\emph{noethérien}' -> 'anneau \\emph{local\n    noethérien}'
Sol: unclear | es_old None | es_new None | note 'The corresponding Spanish passage in section 10 was not supplied.'

## 4308 (0\textsubscript{III} 18, emph+, decisions_current_015): decision 'unclear'
FR: '$M$ un $B$-module de type fini' -> '$M$ un $B$-\\emph{module} de type fini'
Sol: unclear | es_old None | es_new None | note 'The Spanish text of 10.2.2 was not supplied.'

## 4309 (0\textsubscript{III} 18, emph+, decisions_current_015): decision 'unclear'
FR: 'comme $A$-module, les conditions' -> 'comme $A$-\\emph{module}, les conditions'
Sol: unclear | es_old None | es_new None | note 'The Spanish text of 10.2.2 was not supplied.'

## 4310 (0\textsubscript{III} 18, emph+, decisions_current_015): decision 'unclear'
FR: '{10.2.1}) sont équivalentes.' -> '{10.2.1}) sont \\emph{équivalentes}.'
Sol: unclear | es_old None | es_new None | note 'The Spanish text of 10.2.2 was not supplied.'

## 24594 (0\textsubscript{III} 18, emph~, decisions_current_015): not_applicable for a emph~ fix
FR: 'et en outre si $M$ est \\emph{idéalement séparé}' -> 'et si en outre $M$ est \\emph{idéalement séparé}'
Sol: not_applicable | es_old None | es_new None | note 'French word order only.'

## 4335 (0\textsubscript{III} 22, other, decisions_current_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 6.2.3}' -> '{$\\mathbf{0}_{\\mathrm I}$, 6.2.3}'
Sol: unclear | es_old None | es_new None | note 'El pasaje de 10.3.1 no figura en las páginas españolas proporcionadas.'

## 4336 (0\textsubscript{III} 22, other, decisions_current_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 6.6.2}' -> '{$\\mathbf{0}_{\\mathrm I}$, 6.6.2}'
Sol: unclear | es_old None | es_new None | note 'El pasaje de 10.3.1 no figura en las páginas españolas proporcionadas.'

## 4337 (0\textsubscript{III} 22, other, decisions_current_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 6.5.2}' -> '{$\\mathbf{0}_{\\mathrm I}$, 6.5.2}'
Sol: unclear | es_old None | es_new None | note 'El pasaje de 10.3.1 no figura en las páginas españolas proporcionadas.'

## 4338 (0\textsubscript{III} 22, other, decisions_current_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 7.2.12}' -> '{$\\mathbf{0}_{\\mathrm I}$, 7.2.12}'
Sol: unclear | es_old None | es_new None | note 'El pasaje de 10.3.1 no figura en las páginas españolas proporcionadas.'

## 4339 (0\textsubscript{III} 22, other, decisions_current_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 7.2.8}' -> '{$\\mathbf{0}_{\\mathrm I}$, 7.2.8}'
Sol: unclear | es_old None | es_new None | note 'El pasaje de 10.3.1 no figura en las páginas españolas proporcionadas.'

## 4340 (0\textsubscript{III} 22, emph+, decisions_current_016): decision 'unclear'
FR: 'noethérien. On sait' -> '\\emph{noethérien}. On sait'
Sol: unclear | es_old None | es_new None | note 'El pasaje de 10.3.1 no figura en las páginas españolas proporcionadas.'

## 4341 (0\textsubscript{III} 22, other, decisions_current_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 6.2.1}' -> '{$\\mathbf{0}_{\\mathrm I}$, 6.2.1}'
Sol: unclear | es_old None | es_new None | note 'El pasaje de 10.3.1 no figura en las páginas españolas proporcionadas.'

## 4342 (0\textsubscript{III} 22, emph+, decisions_current_016): decision 'unclear'
FR: 'est $A_\\lambda$-plat. C.Q.F.D.' -> 'est $A_\\lambda$-\\emph{plat}. C.Q.F.D.'
Sol: unclear | es_old None | es_new None | note 'El pasaje de 10.3.1 no figura en las páginas españolas proporcionadas.'

## 4343 (0\textsubscript{III} 22, other, decisions_current_016): decision 'unclear'
FR: '\\xi\\mapsto t_\\xi' -> '\\xi\\to t_\\xi'
Sol: unclear | es_old None | es_new None | note 'El pasaje de 10.3.1 no figura en las páginas españolas proporcionadas.'

## 4344 (0\textsubscript{III} 23, other, decisions_current_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 7.3.3}' -> '{$\\mathbf{0}_{\\mathrm I}$, 7.3.3}'
Sol: unclear | es_old None | es_new None | note 'El pasaje de 10.3.1 no figura en las páginas españolas proporcionadas.'

## 4345 (0\textsubscript{III} 23, other, decisions_current_016): decision 'unclear'
FR: '{$0_{\\mathrm I}$, 6.2.1}' -> '{$\\mathbf{0}_{\\mathrm I}$, 6.2.1}'
Sol: unclear | es_old None | es_new None | note 'El pasaje de 10.3.1 no figura en las páginas españolas proporcionadas.'

## 4374 (0\textsubscript{III} 25, textup+, decisions_current_016): not_applicable for a textup+ fix
FR: "exactes, E, $E'$" -> "exactes, \\textup{E}, $E'$"
Sol: not_applicable | es_old None | es_new None | note 'El francés corrige una E escrita como texto dentro del enunciado; el español utiliza la notación matemática $E$.'

## 4410 (0\textsubscript{III} 28, emph+, decisions_current_016): already: en_old missing or not found
FR: 'objets gradués de $K^\\bullet$' -> 'objets \\emph{gradués} de $K^\\bullet$'
Sol: already | es_old 'formada por subobjetos \\emph{graduados}\n\\oldpage[0\\textsubscript{III}]{28}\nde $K^\\bullet$' | es_new None | note None

## 4493 (0\textsubscript{III} 34, emph~, decisions_current_017): not_applicable for a emph~ fix
FR: 'le $p$-ième \\emph{foncteur' -> 'le $p$\\textsuperscript{e} \\emph{foncteur'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de la forma del ordinal francés; el español dice «de grado p».'

## 4505 (0\textsubscript{III} 34, emph~, decisions_current_017): already: en_old missing or not found
FR: '\\emph{bifoncteur covariant}' -> '\\emph{bifoncteur} covariant'
Sol: already | es_old 'un \\emph{bifuntor} covariante $(M, N) \\rightarrow T(M, N)$' | es_new None | note None

## 4927 (0\textsubscript{III} 42, emph-, decisions_current_018): not_applicable for a emph- fix
FR: '\\begin{env}[11.7.3]\n\\label{0.11.7.3-fr}\n\\emph{Remarques}.\n' -> '\\begin{remarks}[11.7.3]\n\\label{0.11.7.3-fr}\n\\upshape\n'
Sol: not_applicable | es_old None | es_new None | note 'Cambio del entorno francés; se conserva la estructura española, ya en redonda.'

## 5522 (0\textsubscript{III} 43, emph+, decisions_current_018): decision 'unclear'
FR: "rangés dans l'ordre croissant dans" -> "rangés \\emph{dans l'ordre croissant} dans"
Sol: unclear | es_old None | es_new None | note 'No se identifica otra aparición de la frase; podría ser una variante de 5521.'

## 5439 (0\textsubscript{III} 67, emph~, decisions_current_020): not_applicable for a emph~ fix
FR: '\\emph{Remarques} (13.2.4).' -> '\\emph{Remarques} (13.2.4). ---'
Sol: not_applicable | es_old None | es_new None | note 'Raya de separación en la presentación francesa.'

## 5471 (0\textsubscript{III} 68, emph-, decisions_current_020): not_applicable for a emph- fix
FR: "montrons qu'il satisfait aux conditions de\n\\emph{a)}.\n" -> 'montrons\n'
Sol: not_applicable | es_old None | es_new None | note 'Redistribución de la frase alrededor del salto de página francés.'

## 5487 (0\textsubscript{III} 69, emph~, decisions_current_020): not_applicable for a emph~ fix
FR: '\\emph{Remarques} (13.3.2).' -> '\\emph{Remarques} (13.3.2). ---'
Sol: not_applicable | es_old None | es_new None | note 'Raya de separación en la presentación francesa.'

## 5154 (0\textsubscript{III} 72, textup+, decisions_current_021): not_applicable for a textup+ fix
FR: '(la flèche verticale de droite provenant du\nmorphisme $X_{p+s-1}^\\bullet\\to X_{p+r-1}^\\bullet$)' -> '\\textup{(la flèche verticale de droite provenant du\nmorphisme $X_{p+s-1}^\\bullet\\to X_{p+r-1}^\\bullet$)}'
Sol: not_applicable | es_old None | es_new None | note 'La traducción sustituye el inciso entre paréntesis por una oración con «donde».'

## 5230 (0\textsubscript{III} 76, emph-, decisions_current_021): not_applicable for a emph- fix
FR: '\\qquad\\emph{pour tout $p\\in\\mathbb Z$.}\n\\end{equation}\n\\end{proposition}' -> '\\qquad\\textit{pour tout $p\\in\\mathbb Z$.}\n\\end{equation}\n\\end{proposition}'
Sol: not_applicable | es_old None | es_new None | note 'La traducción emplea una condición puramente matemática, no la frase francesa con \\emph.'

## 5239 (0\textsubscript{III} 76, emph-, decisions_current_021): not_applicable for a emph- fix
FR: '\\qquad\\emph{pour tout $p\\in\\mathbb Z$.}\n\\end{equation}\n\\end{corollary}' -> '\\qquad\\textit{pour tout $p\\in\\mathbb Z$.}\n\\end{equation}\n\\end{corollary}'
Sol: not_applicable | es_old None | es_new None | note 'La traducción emplea una condición puramente matemática, no la frase francesa con \\emph.'

## 6011 (III 96, other, decisions_current_022): decision 'unclear'
FR: '\\providecommand{\\shProj}{\\mathcal{P}\\mathrm{roj}}' -> '\\providecommand{\\shProj}{\\mathcal{P}\\mathit{roj}}'
Sol: unclear | es_old None | es_new None | note 'La definición de \\shProj no aparece en los fragmentos españoles; no se puede comprobar la tipografía de la macro.'

## 5392 (III 99, textup+, decisions_current_022): not_applicable for a textup+ fix
FR: '$i=r$ et $n\\leq-(r+1)$.' -> '$i=r$ \\textup{et} $n\\leq-(r+1)$.'
Sol: not_applicable | es_old None | es_new None | note 'La conjunción afectada no aparece en español: las dos condiciones del par se separan por una coma.'

## 14440 (III 102, textup+, decisions_current_023): decision 'unclear'
FR: 'propres sur $Y$ (II, 5.4.10)' -> 'propres sur $Y$ \\textup{(\\textbf{II}, 5.4.10)}'
Sol: unclear | es_old None | es_new None | note 'No aparece otra referencia a II, 5.4.10 vinculada a «propios sobre Y»; la del enunciado de 2.2.4 queda corregida por 14439.'

## 5941 (III 104, other, decisions_current_023): decision 'unclear'
FR: '\\text{dans }K_{\\mathcal S}' -> '\\text{dans }\\boldsymbol{K}_{\\mathcal S}'
Sol: unclear | es_old None | es_new None | note 'El español omite la indicación «en K_S» junto al primer funtor; no hay una letra correspondiente que poner en negrita.'

## 5944 (III 104, other, decisions_current_023): decision 'unclear'
FR: '\\text{dans }K_X' -> '\\text{dans }\\boldsymbol{K}_X'
Sol: unclear | es_old None | es_new None | note 'El español omite la indicación «en K_X» junto al segundo funtor; no hay una letra correspondiente que poner en negrita.'

## 5621 (III 113, other, decisions_current_024): decision 'unclear'
FR: '(\\hyperref[III.2.6.2.1-fr]{2.6.2.1}))' -> '(\\hyperref[III.2.6.2.2-fr]{2.6.2.2}))'
Sol: unclear | es_old None | es_new None | note 'La referencia debe ser 2.6.2.2, pero corregirla exige cambiar la clave de \\sref, prohibido por las instrucciones.'

## 5671 (III 115, emph-, decisions_current_024): not_applicable for a emph- fix
FR: '\\begin{env}[2.6.3]\n\\label{III.2.6.3-fr}\n\\emph{Remarque.}' -> '\\begin{remark}[2.6.3]\n\\label{III.2.6.3-fr}\n\\upshape'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de entorno de la edición francesa; se conserva la estructura española.'

## 5535 (III 117, other, decisions_current_025): already: en_old missing or not found
FR: "$K'$, tel que" -> "$\\boldsymbol{K}'$, tel que"
Sol: already | es_old "un $\\sh{O}_X$-módulo coherente $\\sh{F}$ perteneciente a $\\C'$ tal que $\\sh{F}_x\\neq 0$" | es_new None | note None

## 5550 (III 119, emph+, decisions_current_025): already: the fix adds an emphasis but the quoted Spanish has none
FR: '(I, 10.5.6) est propre.' -> '(\\textbf{I}, 10.5.6) \\emph{est propre}.'
Sol: already | es_old 'entonces el morfismo $f_0:X_0\\to S_0$ inducido por $f$~\\sref[I]{I.10.5.6} es propio}.' | es_new None | note 'El texto ya está dentro de \\emph y la referencia usa \\sref.'

## 14431 (III 119, emph+, decisions_current_025): already: the fix adds an emphasis but the quoted Spanish has none
FR: 'le morphisme\n$f_0:X_0\\to S_0$ déduit de' -> '\\emph{le morphisme}\n$f_0:X_0\\to S_0$ \\emph{déduit de}'
Sol: already | es_old 'entonces el morfismo $f_0:X_0\\to S_0$ inducido por $f$~\\sref[I]{I.10.5.6} es propio}.' | es_new None | note 'La frase completa ya está dentro de \\emph.'

## 14432 (III 119, emph+, decisions_current_025): decision 'unclear'
FR: 'le morphisme\n$f_0:X_0\\to Y_0$ déduit de' -> '\\emph{le morphisme}\n$f_0:X_0\\to Y_0$ \\emph{déduit de}'
Sol: unclear | es_old None | es_new None | note 'No aparece el pasaje con f_0:X_0\\to Y_0; la definición mostrada usa S_0 y ya tiene el énfasis.'

## 14435 (III 121, other, decisions_current_025): decision 'unclear'
FR: "\\widetilde{S'}" -> "\\widetilde{S}'"
Sol: unclear | es_old None | es_new None | note "No aparece \\widetilde{S'} ni una expresión equivalente con tilde en las páginas españolas del bloque."

## 14436 (III 121, other, decisions_current_025): decision 'unclear'
FR: "\\widetilde{M'}" -> "\\widetilde{M}'"
Sol: unclear | es_old None | es_new None | note "No aparece \\widetilde{M'} ni una expresión equivalente con tilde en las páginas españolas del bloque."

## 6246 (III 125, textup+, decisions_current_026): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'diagramme\n(\\hyperref[III.4.1.4.2-fr]{4.1.4.2}) sont' -> 'diagramme\n\\textup{(\\hyperref[III.4.1.4.2-fr]{4.1.4.2})} sont'
Sol: already | es_old '$\\vphi_n$, $\\psi_n$ y $\\rho_n$ del diagrama\n\\eqref{III.4.1.4.2} son isomorfismos topológicos.' | es_new None | note '\\eqref ya imprime la referencia y sus paréntesis en redonda.'

## 6250 (III 125, emph-, decisions_current_026): not_applicable for a emph- fix
FR: '\\begin{env}[4.1.6]\n\\label{III.4.1.6-fr}\n\\emph{Remarques.}\n' -> '\\begin{remarks}[4.1.6]\n\\label{III.4.1.6-fr}\n\\upshape\n'
Sol: not_applicable | es_old None | es_new None | note 'Cambio del entorno francés; se conserva la estructura española.'

## 6143 (III 129, emph-, decisions_current_026): not_applicable for a emph- fix
FR: '\\begin{env}[4.1.10]\n\\label{III.4.1.10-fr}\n\\emph{Remarque.}\n' -> '\\begin{remark}[4.1.10]\n\\label{III.4.1.10-fr}\n\\upshape\n'
Sol: not_applicable | es_old None | es_new None | note 'Cambio del entorno francés; se conserva la estructura española.'

## 6052 (III 133, other, decisions_current_026): decision 'unclear'
FR: '(0\\textsubscript{I}, 2.1.8)~; cela' -> '(\\textbf{0}\\textsubscript{I}, 2.1.8)~; cela'
Sol: unclear | es_old None | es_new None | note 'La referencia a 0, 2.1.8 no aparece en el párrafo español posterior a 4.3.9; la aparición posterior pertenece a otra parte de la demostración.'

## 6819 (III 137, emph+, decisions_current_027): not_applicable for a emph+ fix
FR: 'CHAPITRE III (suite)' -> 'CHAPITRE III \\emph{(suite)}'
Sol: not_applicable | es_old None | es_new None | note 'El encabezado de continuación del capítulo no aparece en esta estructura española.'

## 6541 (III 139, textup+, decisions_current_027): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'de (\\hyperref[III.4.2.1.1-fr]{4.2.1.1}) est surjectif.' -> '\\textup{(\\hyperref[III.4.2.1.1-fr]{4.2.1.1})} est surjectif.'
Sol: already | es_old '\\eqref{III.4.2.1.1} es sobreyectivo.' | es_new None | note '\\eqref ya compone en redonda la referencia con sus paréntesis.'

## 6764 (III 139, emph+, decisions_current_027): apply: en_old not found exactly once on pages p-1..p+1
FR: 'est un isomorphisme et que' -> 'est un \\emph{isomorphisme} et que'
Sol: apply | es_old "$\\mathscr H^\\bullet(\\mathscr K'^\\bullet)$ es un isomorfismo y que" | es_new "$\\mathscr H^\\bullet(\\mathscr K'^\\bullet)$ es un \\emph{isomorfismo} y que" | note None

## 6827 (III 142, textup+, decisions_current_028): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'où, dans (6.3.2.1),' -> 'où, dans \\textup{(6.3.2.1)},'
Sol: already | es_old 'donde, en \\sref{III.6.3.2.1},' | es_new None | note 'La referencia se compone mediante \\sref.'

## 6828 (III 142, textup+, decisions_current_028): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'spectrale (6.3.2.2) est' -> 'spectrale \\textup{(6.3.2.2)} est'
Sol: already | es_old 'sucesión espectral \\sref{III.6.3.2.2} es siempre regular;' | es_new None | note 'La referencia se compone mediante \\sref.'

## 6829 (III 142, textup+, decisions_current_028): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'spectrales (6.3.2.1) et (6.3.2.2) sont' -> 'spectrales \\textup{(6.3.2.1)} et \\textup{(6.3.2.2)} sont'
Sol: already | es_old 'las dos sucesiones espectrales \\sref{III.6.3.2.1} y\n\\sref{III.6.3.2.2} son birregulares.' | es_new None | note 'Las referencias se componen mediante \\sref.'

## 6898 (III 146, textup+, decisions_current_029): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'Avec les notations de (6.4.1), supposons' -> 'Avec les notations de \\textup{(6.4.1)}, supposons'
Sol: already | es_old 'Con las notaciones de \\sref{III.6.4.1}, supongamos que' | es_new None | note None

## 7065 (III 147, textup+, decisions_current_029): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'Avec les notations de (6.4.4), supposons' -> 'Avec les notations de \\textup{(6.4.4)}, supposons'
Sol: already | es_old 'Con las notaciones de \\sref{III.6.4.4}, si $u$ y $v$ son' | es_new None | note None

## 7066 (III 147, textup+, decisions_current_029): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '(6.4.4.2) est bijectif' -> '\\textup{(6.4.4.2)} est bijectif'
Sol: already | es_old 'inmersiones abiertas, entonces \\sref{III.6.4.4.2} es biyectivo.' | es_new None | note None

## 6276 (III 148, other, decisions_current_029): decision 'unclear'
FR: 'et II, 10.12.3.1)' -> 'et \\textbf{II}, 10.12.3.1)'
Sol: unclear | es_old None | es_new None | note 'El francés conserva II, 10.12.3.1; el español tiene \\sref[I]{I.10.12.3.1}. La negrita ya la proporciona la macro, pero no se puede igualar el capítulo sin alterar la referencia.'

## 6359 (III 150, emph-, decisions_current_030): not_applicable for a emph- fix
FR: '\\begin{env}[5.1.7]\n\\label{III.5.1.7-fr}\n\\emph{Scholie.}\n' -> '\\begin{scholium}[5.1.7]\n\\label{III.5.1.7-fr}\n'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de entorno y presentación del escolio; se conserva la estructura española.'

## 7129 (III 150, other, decisions_current_030): decision 'unclear'
FR: '$\\mathscr{T}\\!or_\\bullet^S(\\mathscr P_\\bullet,\\mathscr Q_\\bullet)$ se' -> '$\\boldsymbol{\\mathscr{T}\\!or}_\\bullet^S(\\mathscr P_\\bullet,\\mathscr Q_\\bullet)$ se'
Sol: unclear | es_old None | es_new None | note 'Se localiza el pasaje, pero falta la definición de \\shTor para comprobar si ya imprime el hipertor en negrita.'

## 7130 (III 150, other, decisions_current_030): decision 'unclear'
FR: '$\\mathscr{T}\\!or_\\bullet^S(\\mathscr Q_\\bullet,\\mathscr P_\\bullet)$' -> '$\\boldsymbol{\\mathscr{T}\\!or}_\\bullet^S(\\mathscr Q_\\bullet,\\mathscr P_\\bullet)$'
Sol: unclear | es_old None | es_new None | note 'No se proporciona la definición de \\shTor; no puedo comprobar su negrita.'

## 7131 (III 150, other, decisions_current_030): decision 'unclear'
FR: '\\varinjlim_\\alpha\n  \\mathscr{T}\\!or_\\bullet^S\n  (\\mathscr P_{\\alpha\\bullet},\\mathscr Q_\\bullet)\n' -> '\\varinjlim\n  (\\boldsymbol{\\mathscr{T}\\!or}_\\bullet^S\n  (\\mathscr P_{\\alpha\\bullet},\\mathscr Q_\\bullet))\n'
Sol: unclear | es_old None | es_new None | note 'Hay que quitar el subíndice explícito de varinjlim y añadir paréntesis; falta además comprobar si \\shTor ya incluye la negrita.'

## 7132 (III 150, other, decisions_current_030): decision 'unclear'
FR: '\\xrightarrow{\\sim}\n  \\mathscr{T}\\!or_\\bullet^S' -> '\\xrightarrow{\\sim}\n  \\boldsymbol{\\mathscr{T}\\!or}_\\bullet^S'
Sol: unclear | es_old None | es_new None | note 'No se proporciona la definición de \\shTor; no puedo comprobar su negrita.'

## 7134 (III 150, other, decisions_current_030): decision 'unclear'
FR: '$\\mathscr{T}\\!or_n^S(\\mathscr P_\\bullet,\\mathscr Q_\\bullet)$ sont' -> '$\\boldsymbol{\\mathscr{T}\\!or}_n^S(\\mathscr P_\\bullet,\\mathscr Q_\\bullet)$ sont'
Sol: unclear | es_old None | es_new None | note 'No se proporciona la definición de \\shTor; no puedo comprobar su negrita.'

## 7135 (III 150, other, decisions_current_030): decision 'unclear'
FR: '\\bigl(\\mathscr{T}\\!or_n^S' -> '\\bigl(\\boldsymbol{\\mathscr{T}\\!or}_n^S'
Sol: unclear | es_old None | es_new None | note 'No se proporciona la definición de \\shTor; no puedo comprobar su negrita.'

## 7140 (III 150, other, decisions_current_030): decision 'unclear'
FR: '$\\mathscr{T}\\!or_n^X' -> '$\\boldsymbol{\\mathscr{T}\\!or}_n^X'
Sol: unclear | es_old None | es_new None | note 'No se proporciona la definición de \\shTor; no puedo comprobar su negrita.'

## 7150 (III 151, other, decisions_current_030): decision 'unclear'
FR: '  \\mathscr{T}\\!or_\\bullet^S(\\mathscr P_\\bullet,\\mathscr Q_\\bullet)\n  \\xrightarrow' -> '  \\boldsymbol{\\mathscr{T}\\!or}_\\bullet^S(\\mathscr P_\\bullet,\\mathscr Q_\\bullet)\n  \\xrightarrow'
Sol: unclear | es_old None | es_new None | note 'No se proporciona la definición de \\shTor; no puedo comprobar su negrita.'

## 7151 (III 151, textup+, decisions_current_030): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '($0_{\\mathrm I}$, 6.7.1), que' -> '\\textup{($\\mathbf{0}_{\\mathrm I}$, 6.7.1)}, que'
Sol: already | es_old 'Supongamos que $X$ es plano sobre $S$ (\\sref[0]{0.6.7.1}), que' | es_new None | note 'El entorno español env no es cursivo; los paréntesis ya son rectos.'

## 7152 (III 151, textup+, decisions_current_030): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: "l'homomorphisme (6.5.9.1) est" -> "l'homomorphisme \\textup{(6.5.9.1)} est"
Sol: already | es_old 'Entonces el homomorfismo\n\\sref{III.6.5.9.1} es biyectivo.' | es_new None | note None

## 7154 (III 151, textup+, decisions_current_030): not_applicable for a textup+ fix
FR: 'Soit $\\mathscr P_\\bullet$ (resp.\n$\\mathscr Q_\\bullet$) un complexe' -> 'Soit $\\mathscr P_\\bullet$ \\textup{(resp.}\n$\\mathscr Q_\\bullet$\\textup{)} un complexe'
Sol: not_applicable | es_old None | es_new None | note 'La traducción desarrolla los dos complejos sin usar el paréntesis «respectivamente».'

## 7155 (III 151, textup+, decisions_current_030): not_applicable for a textup+ fix
FR: '-Modules (resp. de\n$\\mathscr O_Y$-Modules) quasi-cohérents; on a' -> '-Modules \\textup{(resp.} de\n$\\mathscr O_Y$-Modules\\textup{)} quasi-cohérents; on a'
Sol: not_applicable | es_old None | es_new None | note 'La traducción desarrolla los dos tipos de módulos sin ese paréntesis.'

## 7156 (III 151, other, decisions_current_030): decision 'unclear'
FR: '(f\\times_S g)_*\n  \\bigl(\\mathscr{T}\\!or' -> '(f\\times_S g)_*\n  \\bigl(\\boldsymbol{\\mathscr{T}\\!or}'
Sol: unclear | es_old None | es_new None | note 'No se proporciona la definición de \\shTor; no puedo comprobar su negrita.'

## 7157 (III 151, other, decisions_current_030): decision 'unclear'
FR: '\\mathscr{T}\\!or_\\bullet^S\n  (f_*' -> '\\boldsymbol{\\mathscr{T}\\!or}_\\bullet^S\n  (f_*'
Sol: unclear | es_old None | es_new None | note 'No se proporciona la definición de \\shTor; no puedo comprobar su negrita.'

## 6335 (III 152, other, decisions_current_030): decision 'unclear'
FR: '(I, 1.3.1)' -> '(1.3.1)'
Sol: unclear | es_old None | es_new None | note 'La referencia debe pasar de I, 1.3.1 a III, 1.3.1, pero hacerlo mediante la macro exigiría cambiar la clave \\sref, expresamente prohibido.'

## 6586 (III 153, emph-, decisions_current_031): not_applicable for a emph- fix
FR: "\\emph{Démonstration du théorème d'existence : cas projectif.}" -> "\\textbf{Démonstration du théorème d'existence : cas projectif.}"
Sol: not_applicable | es_old None | es_new None | note 'Cambio de estilo del encabezamiento.'

## 6597 (III 153, emph-, decisions_current_031): not_applicable for a emph- fix
FR: "\\emph{Démonstration du théorème d'existence; cas quasi-projectif.}" -> "\\textbf{Démonstration du théorème d'existence; cas quasi-projectif.}"
Sol: not_applicable | es_old None | es_new None | note 'Cambio de estilo del encabezamiento.'

## 6691 (III 157, emph-, decisions_current_032): not_applicable for a emph- fix
FR: '\\begin{env}[5.4.2]\n\\label{III.5.4.2-fr}\n\\emph{Scholie.}\n' -> '\\begin{scholium}[5.4.2]\n\\label{III.5.4.2-fr}\n'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de entorno y presentación del escolio.'

## 7504 (III 159, emph~, decisions_current_032): not_applicable for a emph~ fix
FR: "\\]\nOn dit que les suites spectrales $(a)$ et $(b)$ sont les \\emph{suites\nspectrales de Künneth}.\n\nOn notera que les suites spectrales $(a)$ et $(a')$ (resp. $(b)$ et $(b')$)\nsont identiques lorsque $\\mathscr P_\\bullet^{(1)}$ et\n$\\mathscr P_\\bullet^{(2)}$ se réduisent à leurs termes de degré 0; dans ce cas,\nles suites $(c)$ et $(d)$ sont dégénérées et sont donc sans intérêt.\n\\end{theorem}" -> "\\]\n\\end{theorem}\n\\noindent On dit que les suites spectrales $(a)$ et $(b)$ sont les \\emph{suites\nspectrales de Künneth}.\n\nOn notera que les suites spectrales $(a)$ et $(a')$ (resp. $(b)$ et $(b')$)\nsont identiques lorsque $\\mathscr P_\\bullet^{(1)}$ et\n$\\mathscr P_\\bullet^{(2)}$ se réduisent à leurs termes de degré 0; dans ce cas,\nles suites $(c)$ et $(d)$ sont dégénérées et sont donc sans intérêt."
Sol: not_applicable | es_old None | es_new None | note 'Cambio del límite del entorno y de la presentación; no se altera la estructura española.'

## 7526 (III 160, other, decisions_current_032): apply: en_old not found exactly once on pages p-1..p+1
FR: '$E_2$\n($0_{\\mathrm I}$, 11.1.5)' -> '$E_2$\n(\\textbf{0}, 11.1.5)'
Sol: apply | es_old 'términos $E_2$ ($0_{\\mathrm I}$, 11.1.5).' | es_new 'términos $E_2$ (\\textbf{0}, 11.1.5).' | note None

## 6405 (III 162, other, decisions_current_032): decision 'unclear'
FR: '$\\mathbf{Ens}$' -> '$\\boldsymbol{\\mathit{Ens}}$'
Sol: unclear | es_old None | es_new None | note 'La notación española es \\Set; falta su definición para comprobar la negrita cursiva.'

## 6407 (III 162, other, decisions_current_032): decision 'unclear'
FR: 'catégorie $C$, $u$ morphisme de\n$C$)' -> 'catégorie $\\boldsymbol{C}$, $u$ morphisme de\n$\\boldsymbol{C}$)'
Sol: unclear | es_old None | es_new None | note 'Se usa \\C; falta su definición para comprobar si ya imprime C en negrita.'

## 6421 (III 162, other, decisions_current_032): decision 'unclear'
FR: '$\\mathrm R^\\bullet T(K^\\bullet)$' -> '$\\mathbf R^\\bullet T(K^\\bullet)$'
Sol: unclear | es_old None | es_new None | note 'Se usa \\RR; falta su definición para comprobar si ya imprime R en negrita.'

## 6423 (III 162, other, decisions_current_032): decision 'unclear'
FR: "$\\mathrm R^\\bullet T(K^\\bullet,K'^{\\bullet})$" -> "$\\mathbf R^\\bullet T(K^\\bullet,K'^{\\bullet})$"
Sol: unclear | es_old None | es_new None | note 'Se usa \\RR; falta su definición para comprobar si ya imprime R en negrita.'

## 6425 (III 162, other, decisions_current_032): decision 'unclear'
FR: '$\\mathrm L_\\bullet T(K_\\bullet)$' -> '$\\mathbf L_\\bullet T(K_\\bullet)$'
Sol: unclear | es_old None | es_new None | note 'Se usa \\LL; falta su definición para comprobar si ya imprime L en negrita.'

## 6427 (III 162, other, decisions_current_032): decision 'unclear'
FR: "$\\mathrm L_\\bullet T(K_\\bullet,K'_\\bullet)$" -> "$\\mathbf L_\\bullet T(K_\\bullet,K'_\\bullet)$"
Sol: unclear | es_old None | es_new None | note 'Se usa \\LL; falta su definición para comprobar si ya imprime L en negrita.'

## 6429 (III 162, other, decisions_current_032): decision 'unclear'
FR: '$\\mathrm L_\\bullet T(K_{\\bullet\\bullet})$' -> '$\\mathbf L_\\bullet T(K_{\\bullet\\bullet})$'
Sol: unclear | es_old None | es_new None | note 'Se usa \\LL; falta su definición para comprobar si ya imprime L en negrita.'

## 6440 (III 162, other, decisions_current_032): decision 'unclear'
FR: '$\\mathcal H^p(f,\\mathcal K^\\bullet)$' -> '$\\mathscr H^p(f,\\mathcal K^\\bullet)$'
Sol: unclear | es_old None | es_new None | note 'Se usa \\sh{H}; falta la definición de \\sh para comprobar si coincide con \\mathscr H.'

## 6441 (III 162, other, decisions_current_032): decision 'unclear'
FR: '$\\mathcal H_f^p(\\mathcal K^\\bullet)$' -> '$\\mathscr H_f^p(\\mathcal K^\\bullet)$'
Sol: unclear | es_old None | es_new None | note 'Se usa \\sh{H}; falta la definición de \\sh para comprobar si coincide con \\mathscr H.'

## 14445 (III 162, other, decisions_current_032): decision 'unclear'
FR: '($Y$ objet de $C$, $w$ morphisme de $C$)' -> '($Y$ objet de $\\boldsymbol{C}$, $w$ morphisme de $\\boldsymbol{C}$)'
Sol: unclear | es_old None | es_new None | note 'La entrada h_w(Y) usa \\C; falta su definición para comprobar la negrita.'

## 14446 (III 162, other, decisions_current_032): decision 'unclear'
FR: 'morphismes de $C$)' -> 'morphismes de $\\boldsymbol{C}$)'
Sol: unclear | es_old None | es_new None | note 'No se identifica una ocurrencia distinta de «morphismes de C)» en las páginas españolas.'

## 6480 (III 163, other, decisions_current_032): decision 'unclear'
FR: '$C\\to\\operatorname{Hom}(C^o,\\mathbf{Ens})$' -> '$\\boldsymbol{C}\\to\\boldsymbol{\\mathit{Hom}}(\\boldsymbol{C}^0,\\boldsymbol{\\mathit{Ens}})$'
Sol: unclear | es_old None | es_new None | note 'La fórmula usa \\C, \\CHom, \\op y \\Set; faltan sus definiciones para comprobar la tipografía corregida.'

## 6929 (III 165, textup+, decisions_current_033): not_applicable for a textup+ fix
FR: "(dit « foncteur spectral\nd'associativité »)" -> "\\textup{(dit « foncteur spectral\nd'associativité »)}"
Sol: not_applicable | es_old None | es_new None | note 'El español no conserva el paréntesis; usa «denominado» y el término ya lleva \\emph.'

## 6930 (III 165, textup+, decisions_current_033): not_applicable for a textup+ fix
FR: '\\mathscr P_\\bullet^{(m)})\n\\]\n(ou simplement ${}^{(e)}\\mathscr E(f_1,\\ldots,f_m;\n\\mathscr P_\\bullet^{(1)},\\ldots,\\mathscr P_\\bullet^{(m)})$) dont' -> '\\mathscr P_\\bullet^{(m)})\n  \\qquad\\textup{(ou simplement ${}^{(e)}\\mathscr E(f_1,\\ldots,f_m;\n\\mathscr P_\\bullet^{(1)},\\ldots,\\mathscr P_\\bullet^{(m)})$)}\n\\]\ndont'
Sol: not_applicable | es_old None | es_new None | note 'El español no conserva el inciso parentético; el resto del cambio es de disposición.'

## 7739 (III 168, textup+, decisions_current_033): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'Sous les conditions de (6.9.1), supposons que' -> 'Sous les conditions de \\textup{(6.9.1)}, supposons que'
Sol: already | es_old 'Bajo las condiciones de \\sref{III.6.9.1}, supongamos que:\n\\begin{enumerate}' | es_new None | note 'La referencia usa \\sref, sin paréntesis exterior en cursiva.'

## 7745 (III 169, other, decisions_current_033): decision 'unclear'
FR: "(0, 11.1.6); d'où" -> "(\\textbf{0}, 11.1.6); d'où"
Sol: unclear | es_old None | es_new None | note 'La frase correspondiente dice «es biyectivo; combinando…», pero omite por completo la referencia cuyo 0 se corrige.'

## 7746 (III 169, textup+, decisions_current_033): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'Sous les conditions de (6.9.1), supposons' -> 'Sous les conditions de \\textup{(6.9.1)}, supposons'
Sol: already | es_old "Bajo las condiciones de \\sref{III.6.9.1}, supongamos que $S$ y $S'$ son\nafines," | es_new None | note 'La referencia usa \\sref, sin paréntesis exterior en cursiva.'

## 7747 (III 169, textup+, decisions_current_033): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '(6.9.6.3) pour $n' -> '\\textup{(6.9.6.3)} pour $n'
Sol: already | es_old 'entero $n_0$, se tienen los isomorfismos canónicos \\sref{III.6.9.6.3} para\n$n\\leq n_0$' | es_new None | note 'La referencia usa \\sref, sin paréntesis exterior en cursiva.'

## 7763 (III 170, textup+, decisions_current_033): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'Sous les conditions de (6.9.8), supposons' -> 'Sous les conditions de \\textup{(6.9.8)}, supposons'
Sol: already | es_old 'Bajo las condiciones de \\sref{III.6.9.8}, supongamos que el complejo' | es_new None | note 'La referencia usa \\sref, sin paréntesis exterior en cursiva.'

## 7775 (III 171, textup+, decisions_current_033): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'définis dans (6.7.10))' -> 'définis dans \\textup{(6.7.10)})'
Sol: already | es_old 'definidos en\n\\sref{III.6.7.10}.' | es_new None | note 'La referencia usa \\sref, sin paréntesis exterior en cursiva.'

## 7781 (III 172, other, decisions_current_033): decision 'unclear'
FR: "isomorphe à\n\\[\n  \\mathscr H_\\bullet\n  (M_{\\bullet\\bullet\\bullet}\\otimes_A Q'_\\bullet),\n\\]\noù" -> "isomorphe à\n$\\mathrm H_\\bullet(M_{\\bullet\\bullet\\bullet}\\otimes_A Q'_\\bullet)$, où"
Sol: unclear | es_old None | es_new None | note 'El español usa \\HH_\\bullet. Sin la definición de \\HH no puedo verificar si ya imprime la H ordinaria recta o requiere sustituirse por \\mathrm H.'

## 7841 (III 176, textup+, decisions_current_034): not_applicable for a textup+ fix
FR: '(resp. exact à droite, exact) pour' -> '\\textup{(resp.} exact à droite, exact) pour'
Sol: not_applicable | es_old None | es_new None | note 'El español no usa el paréntesis: integra las alternativas en la oración.'

## 7842 (III 176, textup+, decisions_current_034): not_applicable for a textup+ fix
FR: '(resp. exact à droite, exact).' -> '\\textup{(resp.} exact à droite, exact).'
Sol: not_applicable | es_old None | es_new None | note 'El español no usa el paréntesis: integra las alternativas en la oración.'

## 7308 (III 178, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '$t_L$ (7.2.2.1)' -> '$t_L$ \\textup{(7.2.2.1)}'
Sol: already | es_old 'homomorfismo canónico $t_L$ de \\eqref{III.7.2.2.1.eq}' | es_new None | note '\\eqref ya imprime el paréntesis y la referencia en redonda.'

## 7314 (III 178, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '$t_M$ (7.2.2.1)' -> '$t_M$ \\textup{(7.2.2.1)}'
Sol: already | es_old '\\item[(b)] el homomorfismo canónico $t_M$ de\n    \\eqref{III.7.2.2.1.eq}' | es_new None | note '\\eqref ya imprime el paréntesis y la referencia en redonda.'

## 7333 (III 179, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'conditions de (7.2.5) sont' -> 'conditions de \\textup{(7.2.5)} sont'
Sol: already | es_old 'Las condiciones de \\sref{III.7.2.5} son\ntambién equivalentes' | es_new None | note 'La macro de referencia ya imprime en redonda.'

## 7340 (III 181, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'canonique (7.2.2.1)' -> 'canonique \\textup{(7.2.2.1)}'
Sol: already | es_old 'canónico y funtorial \\eqref{III.7.2.2.1.eq}' | es_new None | note '\\eqref ya imprime el paréntesis y la referencia en redonda.'

## 7341 (III 181, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: "l'homomorphisme (7.3.1.1)" -> "l'homomorphisme \\textup{(7.3.1.1)}"
Sol: already | es_old '\\eqref{III.7.3.1.1.eq} es un epimorfismo;' | es_new None | note '\\eqref ya imprime el paréntesis y la referencia en redonda.'

## 7344 (III 181, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'conditions de (7.2.7) sur' -> 'conditions de \\textup{(7.2.7)} sur'
Sol: already | es_old 'Si, además, se verifican las condiciones de \\sref{III.7.2.7} sobre' | es_new None | note 'La macro de referencia ya imprime en redonda.'

## 7348 (III 181, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'notations de (7.3.1)' -> 'notations de \\textup{(7.3.1)}'
Sol: already | es_old 'Sea $A$ un anillo conmutativo. Con las notaciones de\n\\sref{III.7.3.1}, supongamos' | es_new None | note 'La macro de referencia ya imprime en redonda.'

## 7351 (III 181, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'canoniques\n    (7.3.3.1)' -> 'canoniques\n    \\textup{(7.3.3.1)}'
Sol: already | es_old 'homomorfismos \\eqref{III.7.3.3.1.eq} son epimorfismos para\n    $i=p$ e $i=p+1$;' | es_new None | note '\\eqref ya imprime el paréntesis y la referencia en redonda.'

## 7352 (III 181, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: "l'homomorphisme (7.3.3.1) est un\n    isomorphisme" -> "l'homomorphisme \\textup{(7.3.3.1)} est un\n    isomorphisme"
Sol: already | es_old '\\eqref{III.7.3.3.1.eq} es un isomorfismo para $i=p$, y' | es_new None | note '\\eqref ya imprime el paréntesis y la referencia en redonda.'

## 7353 (III 181, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: "l'homomorphisme (7.3.3.1) est un\n    épimorphisme" -> "l'homomorphisme \\textup{(7.3.3.1)} est un\n    épimorphisme"
Sol: already | es_old 'homomorfismo \\eqref{III.7.3.3.1.eq} es un epimorfismo para\n    $i=p$, y' | es_new None | note '\\eqref ya imprime el paréntesis y la referencia en redonda.'

## 7625 (III 182, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'les conditions de (7.3.3) sont' -> 'les conditions de \\textup{(7.3.3)} sont'
Sol: already | es_old '\\sref{III.7.3.3} son también equivalentes a cada una de las\nsiguientes:' | es_new None | note 'La macro de referencia ya imprime en redonda.'

## 7635 (III 182, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'membres de (7.3.5.4) soient' -> 'membres de \\textup{(7.3.5.4)} soient'
Sol: already | es_old 'y se da la igualdad en \\eqref{III.7.3.5.4.eq} si y solo si' | es_new None | note '\\eqref ya imprime el paréntesis y la referencia en redonda.'

## 7653 (III 184, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'de (7.3.7) et\ncommute aux limites inductives, et' -> 'de \\textup{(7.3.7)} et\ncommute aux limites inductives, et'
Sol: already | es_old '\\sref{III.7.3.7} y conmuta con los límites inductivos. Supongamos' | es_new None | note 'La macro de referencia ya imprime en redonda.'

## 7661 (III 184, textup+, decisions_current_034): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'de (7.3.7) et\ncommute aux limites inductives, que' -> 'de \\textup{(7.3.7)} et\ncommute aux limites inductives, que'
Sol: already | es_old '\\sref{III.7.3.7} y conmuta con los límites inductivos, que $A$ es' | es_new None | note 'La macro de referencia ya imprime en redonda.'

## 7675 (III 185, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '(7.3.7) impliquent les deux' -> '\\textup{(7.3.7)} impliquent les deux'
Sol: already | es_old 'Las condiciones\nequivalentes (a), (b) y (c) de \\sref{III.7.3.7} implican las dos' | es_new None | note 'La referencia ya se imprime derecha mediante \\sref.'

## 7696 (III 186, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'générales de (7.4.1), et pour' -> 'générales de \\textup{(7.4.1)}, et pour'
Sol: already | es_old 'Bajo las condiciones generales de \\sref{III.7.4.1}, y para un entero dado' | es_new None | note 'La referencia ya se imprime derecha mediante \\sref.'

## 7370 (III 187, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'par (7.4.1.1).' -> 'par \\textup{(7.4.1.1)}.'
Sol: already | es_old '\\eqref{III.7.4.1.1.eq}. Entonces, el conjunto $U$ de los' | es_new None | note 'La referencia ya se imprime derecha mediante \\eqref.'

## 7371 (III 187, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '$(T_p)_y$ (7.1.4)' -> '$(T_p)_y$ \\textup{(7.1.4)}'
Sol: already | es_old 'tales que $(T_p)_y$ \\sref{III.7.1.4} sea exacto por la derecha' | es_new None | note 'La referencia ya se imprime derecha mediante \\sref.'

## 7378 (III 188, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'Sous les hypothèses de (7.4.4), supposons' -> 'Sous les hypothèses de \\textup{(7.4.4)}, supposons'
Sol: already | es_old 'Bajo las hipótesis de \\sref{III.7.4.4}, supongamos además que $A$ es un' | es_new None | note 'La referencia ya se imprime derecha mediante \\sref.'

## 7381 (III 188, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'générales de (7.4.4), les conditions' -> 'générales de \\textup{(7.4.4)}, les conditions'
Sol: already | es_old 'Bajo las hipótesis generales de \\sref{III.7.4.4}, las condiciones (a), (b) y' | es_new None | note 'La referencia ya se imprime derecha mediante \\sref.'

## 7392 (III 189, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'générales de (7.4.4). Alors' -> 'générales de \\textup{(7.4.4)}. Alors'
Sol: already | es_old 'Supongamos verificadas las condiciones generales de \\sref{III.7.4.4}. Entonces,' | es_new None | note 'La referencia ya se imprime derecha mediante \\sref.'

## 7412 (III 190, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '(7.5.1.1) est un isomorphisme' -> '\\textup{(7.5.1.1)} est un isomorphisme'
Sol: already | es_old 'homomorfismo canónico \\eqref{III.7.5.1.1.eq} es un isomorfismo.' | es_new None | note 'La referencia ya se imprime derecha mediante \\eqref.'

## 7435 (III 190, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'générales de (7.5.2), si' -> 'générales de \\textup{(7.5.2)}, si'
Sol: already | es_old 'Bajo las hipótesis generales de \\sref{III.7.5.2}, si $T(k)=0$,' | es_new None | note 'La referencia ya se imprime derecha mediante \\sref.'

## 7452 (III 191, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'conditions générales de (7.5.4).' -> 'conditions générales de \\textup{(7.5.4)}.'
Sol: already | es_old 'Supongamos verificadas las hipótesis generales de\n\\sref{III.7.5.4}.' | es_new None | note 'La referencia ya se imprime derecha mediante \\sref.'

## 7455 (III 191, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'hypothèses générales de (7.5.4), et' -> 'hypothèses générales de \\textup{(7.5.4)}, et'
Sol: already | es_old '\\sref{III.7.5.4}, y supongamos además que $A$ es un anillo de\nvaluación discreta.' | es_new None | note 'La referencia ya se imprime derecha mediante \\sref.'

## 7558 (III 192, textup+, decisions_current_035): already: en_old missing or not found
FR: 'de (7.4.1), soit $B$' -> 'de \\textup{(7.4.1)}, soit $B$'
Sol: already | es_old 'Bajo las hipótesis de \\sref{III.7.4.1}, sea $B$ una $A$-álgebra' | es_new None | note 'Pasaje en la página española 196 suministrada; \\sref ya imprime la referencia derecha.'

## 7559 (III 192, textup+, decisions_current_035): apply: en_old not found exactly once on pages p-1..p+1
FR: '(resp. exact à gauche, exact) il en' -> '\\textup{(resp.} exact à gauche, exact) il en'
Sol: apply | es_old 'conmutativa. Si $T_p$ es exacto por la derecha (respectivamente,\nexacto por la izquierda, exacto),' | es_new 'conmutativa. Si $T_p$ es exacto por la derecha \\textup{(respectivamente,}\nexacto por la izquierda, exacto),' | note 'Pasaje en la página española 196 suministrada.'

## 7560 (III 192, emph+, decisions_current_035): apply: en_old not found exactly once on pages p-1..p+1
FR: '$A$-module plat. On a' -> '$A$-module \\emph{plat}. On a'
Sol: apply | es_old '$A$-módulo plano. Entonces, para todo $A$-módulo $M$,' | es_new '$A$-módulo \\emph{plano}. Entonces, para todo $A$-módulo $M$,' | note 'Pasaje en la página española 196 suministrada.'

## 7562 (III 192, other, decisions_current_035): apply: en_old not found exactly once on pages p-1..p+1
FR: '$M\\mapsto M_{(B)}$' -> '$M\\leadsto M_{(B)}$'
Sol: apply | es_old '$M\\mapsto M_{(B)}$' | es_new '$M\\leadsto M_{(B)}$' | note 'Pasaje en la página española 196 suministrada.'

## 7563 (III 192, other, decisions_current_035): already: en_old missing or not found
FR: '($0_{\\mathrm I}$, 6.4.1)' -> '($\\mathbf{0}_{\\mathrm I}$, 6.4.1)'
Sol: already | es_old 'propiedad de exactitud \\sref[0]{0.6.4.1}.' | es_new None | note 'Pasaje en la página española 196 suministrada; la macro ya da la tipografía del capítulo.'

## 7564 (III 192, textup+, decisions_current_035): decision 'unclear'
FR: 'de (7.4.1), on suppose' -> 'de \\textup{(7.4.1)}, on suppose'
Sol: unclear | es_old None | es_new None | note 'No se suministra el enunciado español de 7.6.2; solo aparece la continuación de su demostración.'

## 7565 (III 192, textup+, decisions_current_035): decision 'unclear'
FR: '(resp. exact à gauche, exact), il faut' -> '\\textup{(resp.} exact à gauche, exact), il faut'
Sol: unclear | es_old None | es_new None | note 'No se suministra el enunciado español de 7.6.2, que contiene este paréntesis.'

## 7566 (III 192, other, decisions_current_035): decision 'unclear'
FR: '($0$, 10.2.8)' -> '($\\mathbf{0}$, 10.2.8)'
Sol: unclear | es_old None | es_new None | note 'No se suministra el comienzo de la demostración española de 7.6.2, donde estaría esta referencia.'

## 7569 (III 193, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'de (7.4.1), supposons' -> 'de \\textup{(7.4.1)}, supposons'
Sol: already | es_old 'Bajo las hipótesis de \\sref{III.7.4.1}, supongamos que $A$ es un\nanillo noetheriano regular de dimensión $1$' | es_new None | note 'La referencia ya se imprime derecha mediante \\sref.'

## 7578 (III 194, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'de (7.4.1), supposons' -> 'de \\textup{(7.4.1)}, supposons'
Sol: already | es_old 'Bajo las hipótesis de \\sref{III.7.4.1}, supongamos que $A$ es un\nanillo de valuación discreta,' | es_new None | note 'La referencia ya se imprime derecha mediante \\sref.'

## 7585 (III 194, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '(I, 1.2.1)' -> '\\textup{(\\textbf{I}, 1.2.1)}'
Sol: already | es_old 'la aplicación correspondiente \\sref[I]{I.1.2.1}. Si' | es_new None | note 'La macro ya imprime la referencia derecha y el capítulo con su tipografía propia.'

## 7586 (III 194, textup+, decisions_current_035): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '(7.1.3), on a' -> '\\textup{(7.1.3)}, on a'
Sol: already | es_old "$T'_\\bullet=T_\\bullet^{(A')}$ \\sref{III.7.1.3}, entonces" | es_new None | note 'La referencia ya se imprime derecha mediante \\sref.'

## 7995 (III 201, textup+, decisions_current_036): not_applicable for a textup+ fix
FR: "(d'où un isomorphisme de foncteurs" -> "\\textup{(d'où un isomorphisme de foncteurs}"
Sol: not_applicable | es_old None | es_new None | note 'Spanish uses a separate sentence, not the French parenthesis.'

## 8011 (III 202, textup+, decisions_current_036): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'hypothèses de (7.7.6) relatives' -> 'hypothèses de \\textup{(7.7.6)} relatives'
Sol: already | es_old 'Bajo las hipótesis de \\sref{III.7.7.6} relativas a $X$, $Y$ y $f$,' | es_new None | note 'The reference macro already prints the complete reference upright.'

## 8031 (III 203, textup+, decisions_current_036): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'générales de (7.7.5),' -> 'générales de \\textup{(7.7.5)},'
Sol: already | es_old 'condiciones generales de \\sref{III.7.7.5}, sean $y$ un punto de $Y$ y $p$ un' | es_new None | note 'The reference macro already prints the complete reference upright.'

## 8069 (III 205, textup+, decisions_current_036): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'celles de (7.8.1),' -> 'celles de \\textup{(7.8.1)},'
Sol: already | es_old 'Con las notaciones e hipótesis de \\sref{III.7.8.1}, las condiciones' | es_new None | note 'The reference macro already prints the complete reference upright.'

## 8075 (III 205, textup+, decisions_current_036): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'défini par (7.7.1.1).\nPour' -> 'défini par \\textup{(7.7.1.1)}.\nPour'
Sol: already | es_old '$Y$, y $\\mathscr T_\\bullet$ el funtor definido por\n\\eqref{III.7.7.1.1}. Para todo $y\\in Y$, las condiciones siguientes' | es_new None | note 'The equation-reference macro already prints the reference upright.'

## 8089 (III 205, textup+, decisions_current_036): not_applicable for a textup+ fix
FR: '(définie dans (7.7.5.1))' -> '\\textup{(définie dans (7.7.5.1))}'
Sol: not_applicable | es_old None | es_new None | note 'Spanish uses a comma-delimited clause, not the French parenthesis.'

## 8092 (III 205, textup+, decisions_current_036): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '($0_{\\mathrm I}$, 4.1.4)' -> '\\textup{($\\mathbf{0}_{\\mathrm I}$, 4.1.4)}'
Sol: already | es_old '\\sref[0]{0.4.1.4}' | es_new None | note 'The reference macro supplies both the corrected chapter typography and the upright parenthesis.'

## 8104 (III 206, textup+, decisions_current_037): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'hypothèses de (7.8.4), les' -> 'hypothèses de \\textup{(7.8.4)}, les'
Sol: already | es_old 'Bajo las hipótesis de \\sref{III.7.8.4}, las condiciones siguientes\nson equivalentes:' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 8307 (III 207, textup+, decisions_current_037): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '[7.8.7]\nSous les hypothèses de (7.8.6)' -> '[7.8.7]\nSous les hypothèses de \\textup{(7.8.6)}'
Sol: already | es_old 'Bajo las hipótesis de \\sref{III.7.8.6}, existe un entorno abierto\n$U$ de $y$ tal que:' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 8311 (III 207, textup+, decisions_current_037): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'conditions de (7.8.6) et en outre' -> 'conditions de \\textup{(7.8.6)} et en outre'
Sol: already | es_old 'Supongamos que se cumplen las hipótesis de \\sref{III.7.8.6} y,\nademás, que' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 8313 (III 207, textup+, decisions_current_037): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '[7.8.9]\nSous les hypothèses de (7.8.6)' -> '[7.8.9]\nSous les hypothèses de \\textup{(7.8.6)}'
Sol: already | es_old 'Bajo las hipótesis de \\sref{III.7.8.6}, existen un entorno abierto\n$U$ de $y$, un $\\mathscr O_U$-módulo coherente' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 8356 (III 210, textup+, decisions_current_037): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'Sous les hypothèses de (7.9.4), soient' -> 'Sous les hypothèses de \\textup{(7.9.4)}, soient'
Sol: already | es_old "Bajo las hipótesis de \\sref{III.7.9.4}, sean $Y'$ un preesquema" | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 8361 (III 210, textup+, decisions_current_037): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'hypothèses de (7.9.4) et en outre' -> 'hypothèses de \\textup{(7.9.4)} et en outre'
Sol: already | es_old 'Supongamos que se cumplen las hipótesis de \\sref{III.7.9.4} y,\nademás, que existe un entero' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 8372 (III 210, textup+, decisions_current_037): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'préliminaires de (7.9.9)' -> 'préliminaires de \\textup{(7.9.9)}'
Sol: already | es_old 'Bajo las hipótesis preliminares de \\sref{III.7.9.9} relativas a' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 8373 (III 210, textup+, decisions_current_037): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'hypothèses de (7.9.10)' -> 'hypothèses de \\textup{(7.9.10)}'
Sol: already | es_old 'Bajo las hipótesis de \\sref{III.7.9.10}, se tiene' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 8377 (III 211, textup+, decisions_current_037): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'celles de (7.9.4), soit' -> 'celles de \\textup{(7.9.4)}, soit'
Sol: already | es_old 'Bajo las hipótesis de \\sref{III.7.9.4}, sea $\\mathscr L$ un' | es_new None | note 'La referencia ya se imprime en redonda mediante \\sref.'

## 8626 (III 222, emph~, decisions_current_038): not_applicable for a emph~ fix
FR: '« \\emph{quasi-cohérent de type fini} ». Dans la\ndémonstration, on se ramène au cas où\n\n' -> '« \\emph{quasi-}%\n'
Sol: not_applicable | es_old None | es_new None | note 'Partición de palabra y salto de página franceses.'

## 24023 (IV 345, emph+, decisions_current_038): not_applicable for a emph+ fix
FR: '\\subsection*{A) Erreurs typographiques}' -> '\\begin{center}\nA) \\emph{Erreurs typographiques}\n\\end{center}'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de presentación de un encabezado.'

## 24129 (IV 347, emph+, decisions_current_038): not_applicable for a emph+ fix
FR: '\\subsection*{B) Modifications de texte}' -> '\\begin{center}\nB) \\emph{Modifications de texte}\n\\end{center}'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de presentación de un encabezado.'

## 24372 (IV 358, emph+, decisions_current_040): decision 'unclear'
FR: '« ou si la condition $\\beta$) de\n({\\hyperref[canon-index.ega4.c04.prop.15-6-6]{15.6.6}}, (iii)) est vérifiée »' -> '« \\emph{ou si la condition} $\\beta$) \\emph{de}\n({\\hyperref[canon-index.ega4.c04.prop.15-6-6]{15.6.6}}, (iii)) \\emph{est vérifiée} »'
Sol: unclear | es_old None | es_new None | note 'La inserción citada está en francés, no en español; no hay palabras españolas sobre las que restituir el énfasis sin traducir además la cita.'

## 24397 (IV 358, textup+, decisions_current_040): not_applicable for a textup+ fix
FR: 'en outre, soit que' -> 'en outre, \\textup{soit} que'
Sol: not_applicable | es_old None | es_new None | note 'La traducción no tiene un primer término correlativo equivalente al primer « soit ».'

## 24014 (IV 361, textup+, decisions_current_040): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '{\\hyperlink{ega4.c04.cor.21-4-11}{(21.4.11)}}. Pour tout' -> '\\textup{\\hyperlink{ega4.c04.cor.21-4-11}{(21.4.11)}}. Pour tout'
Sol: already | es_old 'Supongamos las hipótesis de {\\EGAReadLink{IV.21.4.11}{(21.4.11)}}. Para todo' | es_new None | note 'La macro de referencia incluye los paréntesis en redonda.'

## 8816 (0\textsubscript{IV-1} 5, other, decisions_current_040): decision 'unclear'
FR: 'CHAPITRE 0 (suite)' -> 'CHAPITRE 0 \\textit{(suite)}'
Sol: unclear | es_old None | es_new None | note 'No se muestra la página española 5 ni su encabezamiento; el texto proporcionado comienza en la página 6.'

## 8817 (0\textsubscript{IV-1} 5, other, decisions_current_040): decision 'unclear'
FR: 'symbole $0' -> 'symbole $\\mathbf{0}'
Sol: unclear | es_old None | es_new None | note 'No se muestra la nota de la página española 5.'

## 8818 (0\textsubscript{IV-1} 5, other, decisions_current_040): decision 'unclear'
FR: '_N$ (resp.' -> '_{\\mathrm N}$ (resp.'
Sol: unclear | es_old None | es_new None | note 'No se muestra la nota de la página española 5.'

## 8819 (0\textsubscript{IV-1} 5, other, decisions_current_040): decision 'unclear'
FR: '$\\operatorname{Err}_N$' -> '$\\mathbf{Err}_{\\mathrm N}$'
Sol: unclear | es_old None | es_new None | note 'No se muestra el pasaje español con la notación Err_N.'

## 8820 (0\textsubscript{IV-1} 5, other, decisions_current_040): decision 'unclear'
FR: 'chapitre 0 (resp.' -> 'chapitre \\textbf{0} (resp.'
Sol: unclear | es_old None | es_new None | note 'No se muestra la nota de la página española 5.'

## 8821 (0\textsubscript{IV-1} 5, other, decisions_current_040): decision 'unclear'
FR: 'jointe au chapitre\n$N$.}' -> 'jointe au chapitre\nN.}'
Sol: unclear | es_old None | es_new None | note 'No se muestra la nota de la página española 5.'

## 8458 (0\textsubscript{IV-1} 40, textup+, decisions_current_042): apply: en_old not found exactly once on pages p-1..p+1
FR: '(17.1.1) est' -> '\\textup{(17.1.1)} est'
Sol: apply | es_old '(17.1.1) es' | es_new '\\textup{(17.1.1)} es' | note None

## 8970 (0\textsubscript{IV-1} 61, emph~, decisions_current_042): not_applicable for a emph~ fix
FR: '\\emph{homomorphisme de groupes}.\n\\end{env}' -> '\\emph{homomorphisme de groupes}.'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de estructura de entornos, que debe conservarse en la edición española.'

## 8971 (0\textsubscript{IV-1} 62, other, decisions_current_042): decision 'unclear'
FR: "\\begin{env}[18.3.6.4]\n\\label{0.18.3.6.4-fr}\nEnfin, l'application $(u,1_B,1_L)_*$ est l'application\n\\[\n  u^*:\\operatorname{Exan}_A(B,L)\\longrightarrow\n  \\operatorname{Exan}_{A'}(B,L)\n\\]" -> "Enfin, l'application $(u,1_B,1_L)_*$ est l'application\n\\begin{equation}\n\\label{0.18.3.6.4-fr}\n\\tag{18.3.6.4}\n  u^*:\\operatorname{Exan}_A(B,L)\\longrightarrow\n  \\operatorname{Exan}_{A'}(B,L)\n\\end{equation}"
Sol: unclear | es_old None | es_new None | note 'El pasaje está localizado, pero trasladar la numeración al display exige sustituir el entorno y mover su \\label, cambios prohibidos por las reglas.'

## 9772 (0\textsubscript{IV-1} 120, textup+, decisions_current_045): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'suite exacte \\sref{0.20.2.2.1-fr}' -> 'suite exacte \\textup{\\sref{0.20.2.2.1-fr}}'
Sol: already | es_old 'Además, la sucesión exacta \\sref{0.20.2.2.1-es} es' | es_new None | note '\\sref ya imprime la referencia en redonda.'

## 10171 (0\textsubscript{IV-1} 130, textup+, decisions_current_045): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'canonique \\sref{0.20.5.4.1-fr}' -> 'canonique \\textup{\\sref{0.20.5.4.1-fr}}'
Sol: already | es_old 'el homomorfismo canónico \\sref{0.20.5.4.1-es}' | es_new None | note '\\sref ya imprime la referencia en redonda.'

## 10090 (0\textsubscript{IV-1} 146, textup+, decisions_current_045): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'Sous les hypothèses de \\sref{0.20.6.22-fr}, supposons' -> 'Sous les hypothèses de \\textup{\\sref{0.20.6.22-fr}}, supposons'
Sol: already | es_old 'Bajo las hipótesis de \\sref{0.20.6.22-es}, supongamos además' | es_new None | note '\\sref ya imprime la referencia en redonda.'

## 10096 (0\textsubscript{IV-1} 146, textup+, decisions_current_045): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'comme dans \\sref{0.20.2.2-fr}.' -> 'comme dans \\textup{\\sref{0.20.2.2-fr}}.'
Sol: already | es_old 'se define como en \\sref{0.20.2.2-es}.' | es_new None | note '\\sref ya imprime la referencia en redonda.'

## 10110 (0\textsubscript{IV-1} 148, textup+, decisions_current_045): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '\\sref{0.19.10.2-fr}' -> '\\textup{\\sref{0.19.10.2-fr}}'
Sol: already | es_old '$B$ sea formalmente no ramificada \\sref{0.19.10.2-es}' | es_new None | note '\\sref ya imprime la referencia en redonda.'

## 10117 (0\textsubscript{IV-1} 148, textup+, decisions_current_045): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'bimorphisme formel \\sref{0.19.1.2-fr}' -> 'bimorphisme formel \\textup{\\sref{0.19.1.2-fr}}'
Sol: already | es_old 'bimorfismo formal \\sref{0.19.1.2-es}.\n\\end{proposition}' | es_new None | note '\\sref ya imprime la referencia en redonda.'

## 10119 (0\textsubscript{IV-1} 149, textup+, decisions_current_045): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: "l'homomorphisme \\sref{0.20.7.3.1-fr} est" -> "l'homomorphisme \\textup{\\sref{0.20.7.3.1-fr}} est"
Sol: already | es_old '$\\mathfrak K_\\lambda$ de $C$, el homomorfismo \\sref{0.20.7.3.1-es} es' | es_new None | note '\\sref ya imprime la referencia en redonda.'

## 10123 (0\textsubscript{IV-1} 149, textup+, decisions_current_045): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'gauche \\sref{0.19.1.5-fr}, il faut' -> 'gauche \\textup{\\sref{0.19.1.5-fr}}, il faut'
Sol: already | es_old 'izquierda \\sref{0.19.1.5-es}, es necesario' | es_new None | note '\\sref ya imprime la referencia en redonda.'

## 10285 (0\textsubscript{IV-1} 153, textup+, decisions_current_046): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '\\sref{0.20.7.18-fr}, si' -> '\\textup{\\sref{0.20.7.18-fr}}, si'
Sol: already | es_old 'Bajo las hipótesis de \\sref{0.20.7.18-es}, supongamos además' | es_new None | note '\\sref ya imprime la referencia derecha.'

## 15801 (IV-3 13, textup+, decisions_current_049): apply: en_old not found exactly once on pages p-1..p+1
FR: '(et alors on a\n$u_\\mu^{-1}(E_\\mu)\\subset u_\\mu^{-1}(F_\\mu)$ pour $\\mu\\geq\\lambda$)' -> '\\textup{(et alors on a\n$u_\\mu^{-1}(E_\\mu)\\subset u_\\mu^{-1}(F_\\mu)$ pour $\\mu\\geq\\lambda$)}'
Sol: apply | es_old '(y entonces también se tiene $u_\\mu^{-1}(\\mathrm{E}_\\mu)\\subset u_\\mu^{-1}(\\mathrm{F}_\\mu)$ para\n\\oldpage[IV-3]{13}\n$\\mu\\geqslant\\lambda$)' | es_new '\\textup{(y entonces también se tiene $u_\\mu^{-1}(\\mathrm{E}_\\mu)\\subset u_\\mu^{-1}(\\mathrm{F}_\\mu)$ para\n\\oldpage[IV-3]{13}\n$\\mu\\geqslant\\lambda$)}' | note None

## 15908 (IV-3 25, textup+, decisions_current_050): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'canonique (8.5.10.1) est' -> 'canonique \\textup{(8.5.10.1)} est'
Sol: already | es_old 'la aplicación canónica \\eqref{IV.8.5.10.1} es inyectiva' | es_new None | note '\\eqref ya imprime la referencia en redonda.'

## 15919 (IV-3 26, textup+, decisions_current_050): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'applications (8.6.2.1), (8.6.2.2), (8.6.2.3) sont' -> 'applications \\textup{(8.6.2.1), (8.6.2.2), (8.6.2.3)} sont'
Sol: already | es_old 'Entonces las aplicaciones \\eqref{IV.8.6.2.1}, \\eqref{IV.8.6.2.2} y \\eqref{IV.8.6.2.3}' | es_new None | note '\\eqref ya imprime las referencias en redonda.'

## 15923 (IV-3 26, other, decisions_current_050): decision 'unclear'
FR: '(I, 1.8.4)' -> '(1.8.4)'
Sol: unclear | es_old None | es_new None | note 'El pasaje tiene \\sref[I]{I.1.8.4}; remitir a IV, 1.8.4 requiere cambiar una clave \\sref, prohibido por las reglas.'

## 15924 (IV-3 26, other, decisions_current_050): decision 'unclear'
FR: '(I, 1.6.1)' -> '(1.6.1)'
Sol: unclear | es_old None | es_new None | note 'El pasaje tiene \\sref[I]{I.1.6.1}; remitir a IV, 1.6.1 requiere cambiar una clave \\sref, prohibido por las reglas.'

## 15939 (IV-3 28, textup+, decisions_current_050): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: "l'application (8.8.1.1) est" -> "l'application \\textup{(8.8.1.1)} est"
Sol: already | es_old 'Entonces la aplicación \\eqref{IV.8.8.1.1} es' | es_new None | note '\\eqref ya imprime la referencia en redonda.'

## 15951 (IV-3 30, other, decisions_current_050): decision 'unclear'
FR: '(compte tenu de (I, 3.4))' -> '(compte tenu de (1.3.4))'
Sol: unclear | es_old None | es_new None | note 'El pasaje tiene \\sref[I]{I.1.3.4}; remitir a IV, 1.3.4 requiere cambiar una clave \\sref, prohibido por las reglas.'

## 15954 (IV-3 31, other, decisions_current_050): decision 'unclear'
FR: 'quasi-séparé (I, 1.2.3)' -> 'quasi-séparé (1.2.3)'
Sol: unclear | es_old None | es_new None | note 'El pasaje tiene \\sref[I]{I.1.2.3}; remitir a IV, 1.2.3 requiere cambiar una clave \\sref, prohibido por las reglas.'

## 15961 (IV-3 33, other, decisions_current_050): decision 'unclear'
FR: 'donc (I, 1.6.3) $X_\\rho$' -> 'donc (1.6.3) $X_\\rho$'
Sol: unclear | es_old None | es_new None | note 'El pasaje tiene \\sref[I]{I.1.6.3}; remitir a IV, 1.6.3 requiere cambiar una clave \\sref, prohibido por las reglas.'

## 15964 (IV-3 33, other, decisions_current_050): decision 'unclear'
FR: 'présentation finie (I, 1.6.2). Alors' -> 'présentation finie (1.6.2). Alors'
Sol: unclear | es_old None | es_new None | note 'El pasaje tiene \\sref[I]{I.1.6.2}; remitir a IV, 1.6.2 requiere cambiar una clave \\sref, prohibido por las reglas.'

## 15973 (IV-3 34, other, decisions_current_050): decision 'unclear'
FR: 'présentation finie (I, 1.6.1)' -> 'présentation finie (1.6.1)'
Sol: unclear | es_old None | es_new None | note 'El pasaje tiene \\sref[I]{I.1.6.1}; remitir a IV, 1.6.1 requiere cambiar una clave \\sref, prohibido por las reglas.'

## 15974 (IV-3 34, other, decisions_current_050): decision 'unclear'
FR: '(I, 1.6.2, (iii))' -> '(1.6.2, (iii))'
Sol: unclear | es_old None | es_new None | note 'El pasaje tiene \\sref[I]{I.1.6.2},~(iii); remitir a IV, 1.6.2 requiere cambiar una clave \\sref, prohibido por las reglas.'

## 15975 (IV-3 34, other, decisions_current_050): decision 'unclear'
FR: '(I, 1.8.2)' -> '(1.8.2)'
Sol: unclear | es_old None | es_new None | note 'El pasaje tiene \\sref[I]{I.1.8.2}; remitir a IV, 1.8.2 requiere cambiar una clave \\sref, prohibido por las reglas.'

## 16060 (IV-3 37, other, decisions_current_051): decision 'unclear'
FR: '(I, 4.3 et I, 5.4, (iii))' -> '(1.4.3 et 1.5.4, (iii))'
Sol: unclear | es_old None | es_new None | note 'El español cita I.1.4.3 e I.1.5.4, no IV.1.4.3 e IV.1.5.4. Corregir los destinos exigiría cambiar claves de \\sref, lo que está prohibido.'

## 16087 (IV-3 38, other, decisions_current_051): decision 'unclear'
FR: '(III, 6.2.2' -> '(\\textbf{II}, 6.2.2'
Sol: unclear | es_old None | es_new None | note 'Las referencias españolas son \\sref[III]{III.6.2.2} y \\sref[III]{III.6.2.3}; el francés corregido remite al capítulo II. Corregir los destinos exigiría cambiar claves prohibidas.'

## 16101 (IV-3 40, textup+, decisions_current_051): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '1\\textsuperscript{o} $p$' -> '\\textup{1\\textsuperscript{o}} $p$'
Sol: already | es_old '$1^\\circ$ $p$ es proyectivo' | es_new None | note 'La etiqueta matemática ya se imprime en redonda.'

## 16102 (IV-3 40, textup+, decisions_current_051): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '2\\textsuperscript{o} $g$' -> '\\textup{2\\textsuperscript{o}} $g$'
Sol: already | es_old '$2^\\circ$ $g$ es proyectivo y sobreyectivo' | es_new None | note 'La etiqueta matemática ya se imprime en redonda.'

## 16103 (IV-3 40, textup+, decisions_current_051): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '3\\textsuperscript{o} $j$' -> '\\textup{3\\textsuperscript{o}} $j$'
Sol: already | es_old '$3^\\circ$ $j$ es una inmersión abierta' | es_new None | note 'La etiqueta matemática ya se imprime en redonda.'

## 16158 (IV-3 42, other, decisions_current_051): decision 'unclear'
FR: '(I, 3.3.12)' -> '(\\textbf{I}, 3.3.12)'
Sol: unclear | es_old None | es_new None | note 'En este pasaje el español cita I.5.3.8, mientras que el francés cita I.3.3.12. La macro ya da la tipografía corregida, pero las referencias no coinciden y no se pueden cambiar las claves.'

## 16187 (IV-3 44, textup+, decisions_current_051): decision 'unclear'
FR: '(II, 1.2.7)' -> '\\textup{(\\textbf{II}, 1.2.7)}'
Sol: unclear | es_old None | es_new None | note 'En la proposición 8.12.3 falta la referencia a II, 1.2.7 después de la inyección; no hay referencia cuya tipografía corregir.'

## 16188 (IV-3 44, textup+, decisions_current_051): decision 'unclear'
FR: '((I, 9.6.6)' -> '\\textup{((\\textbf{I}, 9.6.6)}'
Sol: unclear | es_old None | es_new None | note 'La proposición 8.12.3 omite la definición de la familia (C_lambda) y su referencia a I, 9.6.6. El pasaje análogo del lema 8.12.2 corresponde a 16177.'

## 16189 (IV-3 44, textup+, decisions_current_051): decision 'unclear'
FR: '(1.7.9)))' -> '\\textup{(1.7.9)))}'
Sol: unclear | es_old None | es_new None | note 'La proposición 8.12.3 omite la cláusula con la referencia a 1.7.9. El pasaje análogo del lema 8.12.2 corresponde a 16178.'

## 16225 (IV-3 51, other, decisions_current_052): decision 'unclear'
FR: "dans $\\mathcal C'$, ce" -> "dans $\\boldsymbol{C}'$, ce"
Sol: unclear | es_old None | es_new None | note "La traducción omite la frase «quels que soient X, X' dans C'»; no hay aquí una aparición de C' que corregir."

## 16486 (IV-3 78, emph~, decisions_current_054): not_applicable for a emph~ fix
FR: '\\emph{irrédondant}' -> '\\emph{irredondant}'
Sol: not_applicable | es_old None | es_new None | note 'Ortografía francesa.'

## 16394 (IV-3 82, emph~, decisions_current_054): apply: en_old not found exactly once on pages p-1..p+1
FR: '(resp. \\emph{géométriquement connexes})' -> '(resp. \\emph{géométriquement} connexes)'
Sol: apply | es_old 'sean geométricamente irreducibles (resp.\\ geométricamente conexas).' | es_new 'sean geométricamente irreducibles (resp.\\ \\emph{geométricamente} conexas).' | note None

## 17422 (IV-3 131, emph~, decisions_current_057): not_applicable for a emph~ fix
FR: "nous allons d'abord prouver que~:\n\\begin{equation}\n\\text{\\emph{Pour $\\lambda$ assez grand, l'homomorphisme canonique\n$v_\\lambda:N_\\lambda\\otimes_{A_\\lambda}A\\to N$ est bijectif.}}\n\\label{IV.11.2.9.9-fr}\n\\tag{11.2.9.9}\n\\end{equation}\nComme les" -> "nous allons d'abord prouver que~:\n\n\\begin{env}[11.2.9.9]\n\\label{IV.11.2.9.9-fr}\n\\emph{Pour $\\lambda$ assez grand, l'homomorphisme canonique\n$v_\\lambda:N_\\lambda\\otimes_{A_\\lambda}A\\to N$ est bijectif.}\n\\end{env}\n\nComme les"
Sol: not_applicable | es_old None | es_new None | note 'Cambio del entorno de presentación, sin cambio de contenido ni énfasis.'

## 17799 (IV-3 133, other, decisions_current_057): decision 'unclear'
FR: '$\\mathcal F=\\widetilde{\\mathbf M}$, où $M$ est' -> '$\\mathcal F=\\widetilde M$, où $M$ est'
Sol: unclear | es_old None | es_new None | note 'El contexto francés trata de una resolución graduada sobre S y no aparece en las páginas españolas mostradas; además, el cambio invierte 17456.'

## 17478 (IV-3 134, textup+, decisions_current_057): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'celles de (8.5.1) et' -> 'celles de \\textup{(8.5.1)} et'
Sol: already | es_old 'Con las notaciones de $(8.5.1)$ y $(8.8.1)$,' | es_new None | note 'Los números y paréntesis ya son erguidos en modo matemático.'

## 17479 (IV-3 134, textup+, decisions_current_057): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'et (8.8.1), on suppose' -> 'et \\textup{(8.8.1)}, on suppose'
Sol: already | es_old 'Con las notaciones de $(8.5.1)$ y $(8.8.1)$,' | es_new None | note 'Los números y paréntesis ya son erguidos en modo matemático.'

## 17298 (IV-3 136, textup+, decisions_current_057): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'celles de (8.5.1)' -> 'celles de \\textup{(8.5.1)}'
Sol: already | es_old 'Con las notaciones y las hipótesis generales de $(8.5.1)$ y $(8.8.1)$,' | es_new None | note 'Los números y paréntesis ya son erguidos en modo matemático.'

## 17299 (IV-3 136, textup+, decisions_current_057): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: '(8.8.1),\nsupposons' -> '\\textup{(8.8.1)},\nsupposons'
Sol: already | es_old 'Con las notaciones y las hipótesis generales de $(8.5.1)$ y $(8.8.1)$,' | es_new None | note 'Los números y paréntesis ya son erguidos en modo matemático.'

## 17329 (IV-3 138, textup+, decisions_current_057): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: 'notations de (9.4.1)' -> 'notations de \\textup{(9.4.1)}'
Sol: already | es_old 'Entonces, con las notaciones de $(9.4.1)$,' | es_new None | note 'Los números y paréntesis ya son erguidos en modo matemático.'

## 17550 (IV-3 163, other, decisions_current_059): already: en_old missing or not found
FR: "((j'_{\\lambda\\mu})^*(\\mathcal G'_\\lambda))$" -> "(j'^*_{\\lambda\\mu}(\\mathcal G'_\\lambda))$"
Sol: already | es_old "$(j'_{\\lambda\\mu})_*(j_{\\lambda\\mu}'^*(\\sh{G}'_\\lambda))$" | es_new None | note None

## 17855 (IV-3 204, other, decisions_current_061): decision 'unclear'
FR: "ouvert au point $x'$.\n\\end{enumerate}\n\\end{remarks}\n\n" -> "ouvert au point $x'$.\n"
Sol: unclear | es_old None | es_new None | note 'El español también cierra prematuramente enumerate y remarks antes de la continuación de la página 205. Suprimir esos cierres sin reinsertarlos dejaría los entornos abiertos; trasladarlos exigiría una edición estructural.'

## 17857 (IV-3 205, other, decisions_current_062): decision 'unclear'
FR: '$f^{-1}(y)$.\n\n\\begin{proposition}[14.3.4]' -> '$f^{-1}(y)$.\n\\end{enumerate}\n\\end{remarks}\n\n\\begin{proposition}[14.3.4]'
Sol: unclear | es_old None | es_new None | note 'Los cierres ya existen al final de la página 204, pero dejan fuera el párrafo de continuación de la página 205; corregirlo exigiría trasladar cierres de entornos.'

## 18426 (IV-3 230, other, decisions_current_063): apply: en_old not found exactly once on pages p-1..p+1
FR: '$\\mathbf{k}(y)$-préschéma' -> '$\\boldsymbol{k}(y)$-préschéma'
Sol: apply | es_old "el $\\mathbf{k}(y)$-preesquema $\\mathrm{Y}_y'$" | es_new "el $\\boldsymbol{k}(y)$-preesquema $\\mathrm{Y}_y'$" | note None

## 18443 (IV-3 231, textup+, decisions_current_063): already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement
FR: "tels que~:\n\\begin{enumerate}[label=\\emph{\\arabic*\\textsuperscript{\\textdegree}}]\n  \\item $g(z)=y$, $g(z')=y'$~;\n  \\item si l'on pose $f'=f_{(Z)}$, $n(y)$ est le nombre de points de $f'^{-1}(z)$ et $n(y')$ est le nombre de points de $f'^{-1}(z')$.\n\\end{enumerate}" -> "tels que~: \\textup{1\\textsuperscript{\\textdegree}} $g(z)=y$, $g(z')=y'$~; \\textup{2\\textsuperscript{\\textdegree}} si l'on pose $f'=f_{(Z)}$, $n(y)$ est le nombre de points de $f'^{-1}(z)$ et $n(y')$ est le nombre de points de $f'^{-1}(z')$."
Sol: already | es_old "$1^\\circ$ $g(z)=y$, $g(z')=y'$;\n$2^\\circ$ si se pone $f'=f_{(Z)}$, $n(y)$ es el número de puntos de $f'^{-1}(z)$ y $n(y')$ es el número de puntos de $f'^{-1}(z')$." | es_new None | note 'Ya está en línea y los rótulos matemáticos son derechos.'

## 24750 (IV-4 8, emph~, decisions_current_065): not_applicable for a emph~ fix
FR: "appelé l'\\emph{invariant normal d'ordre infini} de $f$, et parfois noté" -> "appelée l'\\emph{invariant normal d'ordre infini} de $f$, et parfois notée"
Sol: not_applicable | es_old None | es_new None | note 'Concordancia gramatical exclusivamente francesa.'

## 18903 (IV-4 22, emph~, decisions_current_065): not_applicable for a emph~ fix
FR: "d'une \\emph{section universelle} pour" -> "d'une «\\emph{section universelle}» pour"
Sol: not_applicable | es_old None | es_new None | note 'Adición de comillas francesas.'

## 19964 (IV-4 79, emph+, decisions_current_069): decision 'unclear'
FR: '(17.4.1, $d$))' -> '(17.4.1, \\emph{d)})'
Sol: unclear | es_old None | es_new None | note 'El pasaje de 17.8.1 no aparece en las páginas españolas proporcionadas; falta toda la subsección 17.8 en este extracto.'

## 19965 (IV-4 79, textup+, decisions_current_069): decision 'unclear'
FR: '$h$ est plat. Pour' -> '$h$ est \\textup{plat}. Pour'
Sol: unclear | es_old None | es_new None | note 'La proposición 17.8.2 no aparece en las páginas españolas proporcionadas.'

## 19966 (IV-4 79, textup+, decisions_current_069): decision 'unclear'
FR: '(resp. étale), il faut' -> '\\textup{(resp.}\\ étale\\textup{)}, il faut'
Sol: unclear | es_old None | es_new None | note 'La proposición 17.8.2 no aparece en las páginas españolas proporcionadas.'

## 19968 (IV-4 79, textup+, decisions_current_069): decision 'unclear'
FR: "(resp. étale). Lorsqu'il" -> "\\textup{(resp.}\\ étale\\textup{)}. Lorsqu'il"
Sol: unclear | es_old None | es_new None | note 'La proposición 17.8.2 no aparece en las páginas españolas proporcionadas.'

## 19969 (IV-4 79, emph+, decisions_current_069): decision 'unclear'
FR: 'propriété des fibres de ce' -> 'propriété des \\emph{fibres} de ce'
Sol: unclear | es_old None | es_new None | note 'La demostración de 17.8.1 no aparece en las páginas españolas proporcionadas.'

## 19970 (IV-4 79, emph+, decisions_current_069): decision 'unclear'
FR: '(17.5.1, $b$))' -> '(17.5.1, \\emph{b)})'
Sol: unclear | es_old None | es_new None | note 'No aparece la referencia (17.5.1, b)) ni el pasaje correspondiente en las páginas españolas proporcionadas.'

## 20184 (IV-4 88, other, decisions_current_069): decision 'unclear'
FR: '\\begin{examples}[17.12.7]' -> '\\begin{example}[17.12.7]'
Sol: unclear | es_old None | es_new None | note 'El español usa el entorno examples; no se proporciona su definición ni consta que exista example. El cambio a singular requiere comprobar los entornos españoles, sin alterar la estructura a ciegas.'

## 20185 (IV-4 89, other, decisions_current_069): decision 'unclear'
FR: '$S$-isomorphisme du préschéma $G$, la « translation à gauche » $\\tau_s$, transformant les points de la section unité de $G$ en les points de $s(S)$; on en conclut que $G$ est lisse sur $S$ aux points de $s(S)$.\n\\end{examples}' -> '$S$-isomorphisme du préschéma $G$, la « translation à gauche » $\\tau_s$, transformant les points de la section unité de $G$ en les points de $s(S)$; on en conclut que $G$ est lisse sur $S$ aux points de $s(S)$.\n\\end{example}'
Sol: unclear | es_old None | es_new None | note 'Depende del cambio de entorno de 20184 y de la disponibilidad de example en la edición española.'

## 20378 (IV-4 98, textup+, decisions_current_070): apply: en_old not found exactly once on pages p-1..p+1
FR: 'Pour tout schéma local' -> 'Pour tout \\textup{schéma local}'
Sol: apply | es_old "Para todo esquema local $Y'$" | es_new "Para todo \\textup{esquema local} $Y'$" | note None

## 20494 (IV-4 108, textup+, decisions_current_071): apply: en_old not found exactly once on pages p-1..p+1
FR: 'surjectif, localement de présentation finie et localement quasi-fini' -> 'surjectif, localement de présentation finie et \\textup{localement quasi-fini}'
Sol: apply | es_old 'sobre\xadyectivo, localmente de presentación finita y localmente cuasi-finito' | es_new 'sobre\xadyectivo, localmente de presentación finita y \\textup{localmente cuasi-finito}' | note 'La edición debe usar el substring sin guion discrecional: «sobreyectivo, localmente de presentación finita y localmente cuasi-finito».'

## 20705 (IV-4 117, emph-, decisions_current_071): not_applicable for a emph- fix
FR: '\\begin{env}[18.3.3]\n\\label{IV.18.3.3}\n\\emph{Exemple.} --- La prop.' -> '\\begin{example}[18.3.3]\n\\label{IV.18.3.3}\nLa prop.'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de entorno de presentación; el español ya identifica el pasaje como ejemplo.'

## 20869 (IV-4 123, emph-, decisions_current_072): not_applicable for a emph- fix
FR: '\\begin{env}[18.4.11]\n\\label{IV.18.4.11}\n\\emph{Exemples.} --- On peut' -> '\\begin{examples}[18.4.11]\n\\label{IV.18.4.11}\nOn peut'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de entorno del francés; el español ya tiene el encabezado «Ejemplos».'

## 21759 (IV-4 178, textup+, decisions_current_075): apply: en_old not found exactly once on pages p-1..p+1
FR: "la condition $d)$ est équivalente à $a)$, $a')$ et $b)$." -> "la condition \\textup{d)} est équivalente à \\textup{a), a$'$)} et \\textup{b)}."
Sol: apply | es_old "la condición $d)$ es equivalente a $a)$, $a')$ y $b)$)." | es_new "la condición \\textup{d)} es equivalente a \\textup{a), a$'$)} y \\textup{b)}." | note None

## 21955 (IV-4 185, emph+, decisions_current_075): decision 'unclear'
FR: 'étude des immersions régulières (16.9.2)' -> 'étude des \\emph{immersions régulières} (16.9.2)'
Sol: unclear | es_old None | es_new None | note 'La introducción de la sección 19 no aparece en los textos españoles proporcionados.'

## 22376 (IV-4 191, other, decisions_current_076): decision 'unclear'
FR: "d'appliquer ($0$, 15.1.6)" -> "d'appliquer (\\textbf{0}, 15.1.6)"
Sol: unclear | es_old None | es_new None | note 'No aparece una referencia a (0, 15.1.6); las dos referencias a (0, 15.1.16) corresponden a 22066 y 22115.'

## 22379 (IV-4 199, emph+, decisions_current_076): decision 'unclear'
FR: "l'équivalence de $b)$ et $c)$," -> "l'équivalence de \\emph{b)} et \\emph{c)},"
Sol: unclear | es_old None | es_new None | note 'La demostración española está reformulada y no contiene una afirmación de equivalencia de b) y c); no se identifica el pasaje exacto.'

## 22380 (IV-4 199, emph+, decisions_current_076): decision 'unclear'
FR: 'la condition $c)$ implique' -> 'la condition \\emph{c)} implique'
Sol: unclear | es_old None | es_new None | note 'La demostración española está reformulada y no contiene «la condición c) implica»; no se identifica con seguridad el pasaje exacto.'

## 22566 (IV-4 216, other, decisions_current_077): decision 'unclear'
FR: '($0$, 15.1.7)' -> '(\\textbf{0}, 15.1.7)'
Sol: unclear | es_old None | es_new None | note 'No aparece una referencia independiente (0, 15.1.7) en estas páginas. El contexto francés corresponde a la página 206, ya tratada en 22311; la referencia conjunta de la nota se trata en 22660.'

## 22658 (IV-4 216, other, decisions_current_077): decision 'unclear'
FR: '\\mathfrak R' -> '\\mathfrak K'
Sol: unclear | es_old None | es_new None | note 'El contexto francés pertenece a otro pasaje no mostrado. Las dos R restantes de la página 216 se corrigen en 22552 y 22556; no se puede identificar otra ocurrencia para este id.'

## 22666 (IV-4 216, other, decisions_current_077): decision 'unclear'
FR: '($0$, 15.1.9)' -> '(\\textbf{0}, 15.1.9)'
Sol: unclear | es_old None | es_new None | note 'El contexto francés no está en las páginas mostradas y no aparece una referencia independiente (0, 15.1.9). La referencia conjunta de la nota se trata en 22660.'

## 22840 (IV-4 225, other, decisions_current_078): apply: en_old not found exactly once on pages p-1..p+1
FR: '\\Gamma(X-Z,\\sh H)' -> '\\Gamma(X\\setmin Z,\\sh H)'
Sol: apply | es_old '\\longrightarrow\\Gamma(X-Z,\\sh H)' | es_new '\\longrightarrow\\Gamma(X\\setmin Z,\\sh H)' | note None

## 22859 (IV-4 226, emph~, decisions_current_078): not_applicable for a emph~ fix
FR: '$\\sh{O}_X$-module \\emph{plat}' -> '$\\sh{O}_X$-Module \\emph{plat}'
Sol: not_applicable | es_old None | es_new None | note 'Mayúscula de «Module» propia del francés.'

## 22898 (IV-4 241, emph~, decisions_current_079): not_applicable for a emph~ fix
FR: '\\emph{20.3.8.5. Fin de la démonstration de \\sref{IV.20.3.8.2}.}' -> '\\textbf{(20.3.8.5)} \\emph{Fin de la démonstration de \\sref{IV.20.3.8.2}.} ---'
Sol: not_applicable | es_old None | es_new None | note 'Formato del encabezamiento; no cambia su número ni su contenido.'

## 22899 (IV-4 241, emph~, decisions_current_079): not_applicable for a emph~ fix
FR: '\\emph{20.3.8.6. Fin de la démonstration de \\sref{IV.20.3.8}.}' -> '\\textbf{(20.3.8.6)} \\emph{Fin de la démonstration de \\sref{IV.20.3.8}.} ---'
Sol: not_applicable | es_old None | es_new None | note 'Formato del encabezamiento; no cambia su número ni su contenido.'

## 23000 (IV-4 254, emph~, decisions_current_079): not_applicable for a emph~ fix
FR: 'qui est \\emph{régulière relativement à $S$}' -> 'qui est \\emph{régulière relative à $S$}'
Sol: not_applicable | es_old None | es_new None | note 'Ajuste gramatical francés sin cambio de sentido.'

## 23187 (IV-4 271, emph~, decisions_current_080): not_applicable for a emph~ fix
FR: 'On appelle \\emph{multiplicité' -> 'on appelle \\emph{multiplicité'
Sol: not_applicable | es_old None | es_new None | note 'Mayúscula de inicio de frase francesa.'

## 23203 (IV-4 272, emph~, decisions_current_080): not_applicable for a emph~ fix
FR: 'un homomorphisme de faisceaux de \\emph{monoïdes}' -> 'un homomorphisme de faisceau de \\emph{monoïdes}'
Sol: not_applicable | es_old None | es_new None | note 'Cambio gramatical francés de plural a singular.'

## 23204 (IV-4 272, emph~, decisions_current_080): not_applicable for a emph~ fix
FR: '\\emph{faisceaux de monoïdes}' -> '\\emph{faisceau de monoïdes}'
Sol: not_applicable | es_old None | es_new None | note 'Cambio gramatical francés de plural a singular.'

## 23492 (IV-4 297, other, decisions_current_081): decision 'unclear'
FR: "[\\boldsymbol{k}(x'_1):\\boldsymbol{k}(x')]\\cdot[\\boldsymbol{k}(x'):\\boldsymbol{k}(x)]\n  =[\\boldsymbol{k}(x'_1):\\boldsymbol{k}(x_1)]\\cdot[\\boldsymbol{k}(x_1):\\boldsymbol{k}(x)],\n" -> "[\\boldsymbol{k}(x'_1):\\boldsymbol{k}(x')].[\\boldsymbol{k}(x'):\\boldsymbol{k}(x)]\n  =[\\boldsymbol{k}(x'_1):\\boldsymbol{k}(x_1)].[\\boldsymbol{k}(x_1):\\boldsymbol{k}(x)]\n"
Sol: unclear | es_old None | es_new None | note 'La identidad de grados de cuerpos indicada no aparece en las páginas españolas del bloque; la demostración española usa longitudes.'

## 23564 (IV-4 308, emph-, decisions_current_081): not_applicable for a emph- fix
FR: '\\begin{env}[21.12.9]\n\\label{IV.21.12.9}\n\\emph{Exemples}. ---\nSi $A$' -> '\\begin{examples}[21.12.9]\n\\label{IV.21.12.9}\nSi $A$'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de entorno de presentación; el español ya tiene el encabezamiento «Ejemplos».'

## 23886 (IV-4 317, emph-, decisions_current_081): not_applicable for a emph- fix
FR: '\\begin{env}[21.13.9]\n\\label{IV.21.13.9}\n\\emph{Exemples}. ---\n\n(i) Un anneau' -> '\\begin{examples}[21.13.9]\n\\label{IV.21.13.9}\n(i) Un anneau'
Sol: not_applicable | es_old None | es_new None | note 'Cambio de entorno de presentación; el español ya tiene el encabezamiento «Ejemplos».'

## 23917 (IV-4 319, emph~, decisions_current_081): not_applicable for a emph~ fix
FR: '\\emph{régulier}.\n\\end{env}' -> '\\emph{régulier}.\n\\end{examples}'
Sol: not_applicable | es_old None | es_new None | note 'Cierre del cambio de entorno francés de 23886.'
