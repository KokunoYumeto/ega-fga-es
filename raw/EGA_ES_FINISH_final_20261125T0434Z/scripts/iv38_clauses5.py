from iv38_patchlib import *
p=Patches('clauses5')
p.replace('8.8.3',r"``preesquema en grupos''",r'«\emph{preesquema en grupos}»')
p.replace('8.11.5',r'observemos \sref[I]{I.5.3.8} que',r'observemos \sref[I]{I.3.3.12} que')
p.replace('8.12.6',r"el morfismo $u:Y'\to Y$ es regular y, en consecuencia,",r"el morfismo $u:Y'\to Y$ es regular y, \emph{a fortiori}, normal, y por consiguiente,")
p.replace('8.12.6',r"$g'$ es, en efecto, una inmersión abierta.",r"$g'$ es, en efecto, una inmersión abierta, C.Q.F.D.")
p.replace('8.13.5',r'(pues es de tipo finito sobre $S$ y $f$ es noetheriano)',r'(pues $S$ lo es y $f$ es de tipo finito)')
# Restore literal reference formulas. They were previously expanded into macros
# with a different mathematical span boundary.
for un,old,new in [
 ('8.2.13',r'\sref[$\mathbf{0}_{\mathrm{I}}$]{0.3.7.1}',r'$(\mathbf{0}_{\mathrm I},3.7.1)$'),
 ('8.2.13',r'\sref[$\mathbf{0}_{\mathrm{I}}$]{0.4.3.1}',r'$(\mathbf{0}_{\mathrm I},4.3.1)$'),
 ('8.3.8',r'\sref[0]{0.6.2.3}',r'$(\mathbf{0}_{\mathrm I},6.2.3)$'),
 ('8.3.11',r'($\mathbf{0}_{\mathrm{III}}$,~9.1.4)',r'$(\mathbf{0}_{\mathrm{III}},9.1.4)$'),
 ('8.3.11',r'($\mathbf{0}_{\mathrm{III}}$,~9.1.8)',r'$(\mathbf{0}_{\mathrm{III}},9.1.8)$'),
 ('8.3.12',r'($\mathbf{0}_{\mathrm{III}}$,~9.1.8)',r'$(\mathbf{0}_{\mathrm{III}},9.1.8)$'),
 ('8.4.2.1',r'\sref[0]{0.2.1.6}',r'$(\mathbf{0}_{\mathrm I},2.1.6)$'),
 ('8.4.2.1',r'\sref[0]{0.2.1.7}',r'$(\mathbf{0}_{\mathrm I},2.1.7)$'),
 ('8.5.1',r'\sref[0]{0.5.1.1}',r'$(\mathbf{0}_{\mathrm I},5.1.1)$'),
 ('8.5.2.1',r'\sref[0]{0.5.2.5}',r'$(\mathbf{0}_{\mathrm I},5.2.5)$'),
 ('8.5.2.5',r'\sref[0]{0.3.3.1}',r'$(\mathbf{0}_{\mathrm I},3.3.1)$'),
 ('8.5.8',r'\sref[0\textsubscript{I}]{0.6.7.2}',r'$(\mathbf{0}_{\mathrm I},6.7.2)$'),
 ('8.8.2.5',r'\sref[0\textsubscript{I}]{0.4.1.7}',r'$(\mathbf{0}_{\mathrm I}, 4.1.7)$'),
 ('8.13.6',r'$(\mathbf{0}_{\text{III}},~8.2.5)$',r'$(\mathbf 0_{\mathrm{III}},8.2.5)$')]:p.replace(un,old,new)
for un,ns in [('8.10.3',range(1,5)),('8.10.5.1',range(1,4))]:
 for n in ns:p.replace(un,'$'+str(n)+r'^\circ$',str(n)+r'\textsuperscript{o}')
# Source page anchors placed at the corresponding phrase / formula boundary.
for un,page in [('8.1.2',6),('8.1.2',7),('8.2.13',12),('8.5.2.1',21),('8.10.5.1',40)]:p.replace(un,r'\oldpage[IV-3]{'+str(page)+'}','')
p.replace('8.1.2',r'en $U_\alpha$ y, por tanto, en $Y$.',r'en $U_\alpha$,'+'\n'+r'\oldpage[IV-3]{6}'+'\n'+r'por tanto, en $Y$.')
p.replace('8.1.2',r'(que a veces se califica de «geometría algebraica absoluta»)',r'(que a veces se califica de'+'\n'+r'\oldpage[IV-3]{7}'+'\n'+r'«geometría algebraica absoluta»)')
p.replace('8.2.12',r'\sref{IV.5.13.3},~(ii).',r'\sref{IV.5.13.3},~(ii).'+'\n\n'+r'\oldpage[IV-3]{12}')
p.replace('8.5.2.1',r'de modo que el homomorfismo \eqref{IV.8.5.2.2}',r'\oldpage[IV-3]{21}'+'\n'+r'de modo que el homomorfismo \eqref{IV.8.5.2.2}')
p.replace('8.10.5.1',r'$f:X\to Y$ un $A$-morfismo separado.',r'$f:X\to Y$'+'\n'+r'\oldpage[IV-3]{40}'+'\n'+r'un $A$-morfismo separado.')
# Close numbered statements at the same mathematical boundary as the source.
p.replace('8.3.2',r'\end{theorem}','')
p.replace('8.3.2',r'Las observaciones entre paréntesis',r'\end{theorem}'+'\n\n'+r'Las observaciones entre paréntesis')
p.replace('8.6.2',r'\end{env}','')
p.replace('8.6.2',r'\end{align}',r'\end{align}'+'\n'+r'\end{env}')
p.replace('8.12.2',r'\end{lemma}','')
p.replace('8.12.2',r'Basta aplicar \sref[II]{II.3.8.4}',r'\end{lemma}'+'\n\n'+r'Basta aplicar \sref[II]{II.3.8.4}')
p.save()
