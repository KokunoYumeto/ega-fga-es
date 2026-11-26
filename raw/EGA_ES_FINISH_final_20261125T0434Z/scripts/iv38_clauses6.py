from iv38_patchlib import *
p=Patches('clauses6')
p.replace('8.5.2.1',r'de modo que el homomorfismo \sref{IV.8.5.2.2}',r'\oldpage[IV-3]{21}'+'\n'+r'de modo que el homomorfismo \sref{IV.8.5.2.2}')
p.replace('8.1.2',r'Este ejemplo muestra, en particular,',r'Este ejemplo nos muestra, en particular,')
p.replace('8.2.14',r'lo que demuestra la afirmación.',r'lo que demuestra nuestra afirmación.')
p.replace('8.5.2.1',r'Ahora $p_{\lambda\mu}$',r'Observemos ahora que $p_{\lambda\mu}$')
p.replace('8.5.5',r'$S_0$ es cuasicompacto y que',r'$S_0$ es cuasicompacto, y supongamos que')
p.replace('8.8.2.3',r'Sea dado un homomorfismo de',r'Supongamos dado un homomorfismo de')
p.replace('8.8.2.3',r'Sean, pues, dos $X_\alpha$-morfismos',r'Supongamos, pues, dados dos $X_\alpha$-morfismos')
p.replace('8.8.2.3',r'Sea, pues, un $S$-morfismo',r'Supongamos, pues, dado un $S$-morfismo')
p.replace('8.12.6',r"Ahora bien, $u^{-1}(a)$",r"Observemos ahora que $u^{-1}(a)$")
p.replace('8.12.6',r"El morfismo $f'$ es separado y cuasifinito",r"Observemos ahora que $f'$ es un morfismo separado y cuasifinito")
for un in ['8.2.9','8.3.12','8.6.3']:
 p.replace(un,'se puede restringirnos','se puede restringir')
for un in ['8.10.4','8.11.3','8.11.4','8.14.2']:
 p.replace(un,'se puede reducirnos','se puede reducir')
p.replace('8.10.5','se puede limitarnos','se puede limitar')
# The volume of each citation has been checked against its French context.
for un,old,new in [
 ('8.1.3',r'\sref[I]{I.10.4.8}',r'\sref{IV.10.4.8}'),
 ('8.6.3.1',r'\sref{I.1.8.4}',r'\sref{IV.1.8.4}'),
 ('8.6.3.1',r'\sref{I.1.6.1}',r'\sref{IV.1.6.1}'),
 ('8.8.2.3',r'\sref{I.1.3.4}',r'\sref{IV.1.3.4}'),
 ('8.8.2.3',r'\sref{I.1.2.3}',r'\sref{IV.1.2.3}'),
 ('8.8.3',r'\sref{I.1.6.2}',r'\sref{IV.1.6.2}'),
 ('8.9.1',r'\sref{I.1.6.1}',r'\sref{IV.1.6.1}'),
 ('8.9.1',r'\sref{I.1.6.2}',r'\sref{IV.1.6.2}'),
 ('8.9.1',r'\sref{I.1.8.2}',r'\sref{IV.1.8.2}'),
 ('8.10.4',r'\sref{I.1.4.3}',r'\sref{IV.1.4.3}'),
 ('8.10.4',r'\sref{I.1.5.4}',r'\sref{IV.1.5.4}'),
 ('8.10.5',r'\sref[II]{III.6.2.2}',r'\sref[II]{II.6.2.2}'),
 ('8.10.5',r'\sref[II]{III.6.2.3}',r'\sref[II]{II.6.2.3}')]:p.replace(un,old,new)
# Remove inherited surplus closing parentheses while retaining actual source pairs.
p.replace('8.1.3',r'\sref{IV.9.6.1},~(iv))).',r'\sref{IV.9.6.1}, (iv)).')
p.replace('8.7.2',r'en el caso b),',r'en el caso \emph{b)},')
p.replace('8.7.2',r'$\mathcal O_s$ es el mismo',r'$\mathcal O_s$ es \emph{el mismo}')
for old,new in [(r'\sref{IV.8.1.2},~\emph{c)})',r'\sref{IV.8.1.2}, \emph{c)}'),(r'\sref{IV.8.10.5},~(v),~(xi) y (xii))',r'\sref{IV.8.10.5}, (v), (xi) y (xii)'),(r'\sref{IV.8.1.2},~\emph{a)})',r'\sref{IV.8.1.2}, \emph{a)}'),(r'\sref{IV.8.10.5},~(v),~(ix),~(x),~(xi) y (xii))',r'\sref{IV.8.10.5}, (v), (ix), (x), (xi) y (xii)'),(r'\sref[II]{II.5.1.10},~(ii))',r'\sref[II]{II.5.1.10}, (ii)'),(r"\sref[II]{II.5.1.2},~\emph{c')})",r"\sref[II]{II.5.1.2}, \emph{c')}")]:p.replace('8.11.4',old,new)
p.replace('8.11.6',r'\sref{IV.2.4.5},~(i)))}',r'\sref{IV.2.4.5}, (i))}')
for un,refs in [('8.12.7',[r'\sref{IV.8.12.6}',r'\sref{IV.8.12.6.1}',r'\sref{IV.1.6.2}']),('8.12.9',[r'\sref{IV.8.12.8}']),('8.12.10',[r'\sref[I]{I.8.2.8}',r'\sref[I]{I.5.2.3}']),('8.12.11',[r'\sref[II]{II.6.3.4}',r'\sref[II]{II.6.3.9}',r'\sref[I]{I.5.5.1}',r'\sref{IV.8.12.10}'])]:
 for ref in refs:p.replace(un,ref+')',ref)
p.replace('8.12.7',r'\emph{esquema} afín',r'\emph{esquema afín}')
p.replace('8.12.11',r'\sref[II]{II.6.2.4},~(v)),',r'\sref[II]{II.6.2.4}, (v),')
p.save()
