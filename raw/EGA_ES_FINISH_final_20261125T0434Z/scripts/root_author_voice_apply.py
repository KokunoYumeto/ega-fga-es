"""Restore reviewed author plurals; retain genuine Spanish enclitic plurals."""
import re,collections,json
from corpus import RESULT,ES,FR,write_tsv
from root_scope_pairs import pairs,scoped_units,resolve
P={
('I','1.7.3'):[('Sean $A=A(X)$, $B=A(Y)$','Pongamos $A=A(X)$, $B=A(Y)$')],
('I','10.4.6'):[('se dejan los detalles al lector','dejamos los detalles al lector')],
('I','10.14.6'):[('se toma como','tomaremos como')],
('I','10.15.3'):[('Se deja al lector el cuidado','Dejamos al lector el cuidado')],
('I','10.15.4'):[('Si se prueba que','Si demostramos que')],
('I','3.2.6.4'):[('y sean $X_i=','y pongamos $X_i=')],
('I','4.1.9'):[('Sea $f=(\\psi,\\theta)$','Pongamos $f=(\\psi,\\theta)$')],
('I','5.3.16'):[(r'Aplicando \sref{I.5.3.15} al morfismo de inyección $f:X\to Y$, se ve que',r'Apliquemos \sref{I.5.3.15} al morfismo de inyección $f:X\to Y$; se sabe entonces que')],
('I','7.1.1'):[('se dice que','diremos que')],
('I','9.5.6'):[(r'Sea $u=g_1\circ f=g_2\circ f$',r'Pongamos $u=g_1\circ f=g_2\circ f$')],
('IV1_0','19.5.2'):[('Nótese que aquí','Observemos que aquí')],
('IV1_0','19.7.2'):[('nótese que los ideales','observemos que los ideales')],
('IV1_0','21.5.2'):[('Por otra parte, \\emph{toda} derivación','Observemos, por otra parte, que \\emph{toda} derivación')],
('IV2','2.3.5'):[('genérico, que $f^{-1}(y)$','genérico, supongamos que $f^{-1}(y)$')],
('IV2','3.4.1.5'):[('Obsérvese que esto','Observemos que esto')],
('IV2','4.7.3'):[('Obsérvese que dos extensiones','Observemos que dos extensiones')],
('IV2','6.15.7'):[('Obsérvese que','Observemos que')],
('IV2','7.9.8'):[('Obsérvese que la condición','Observemos que la condición')],
('II:main','3.1.3'):[('y se denota por','y lo denotaremos por')],
('II:main','6.7.1.1'):[('en el caso considerado tomando','en el caso que consideramos tomando')],
('IV4','16.8.7'):[('que se designará por','que designaremos por')],
('IV4','16.9.7'):[('se dirá que un ideal','diremos que un ideal')],
('IV4','18.7.1'):[('suponiendo además que la propiedad','donde suponemos además que la propiedad')],
('IV4','18.12.12'):[('conservando sus notaciones','cuyas notaciones conservamos')],
('IV4','21.6.7'):[('que se seguirá denotando por','que seguiremos denotando por')],
('IV4:errata','10.4.14'):[('Se ignora si todo endomorfismo','Ignoramos si todo endomorfismo')],
('IV4:errata','21.4.9'):[(r'Sean $i:U\to Y$ y $j:f^{-1}(U)\to X$ las inmersiones canónicas',r'Denotemos por $i:U\to Y$ y $j:f^{-1}(U)\to X$ las inyecciones canónicas')],
('IV4:errata','21.4.13'):[('Los puntos de $\\operatorname{Ass}','Observemos que los puntos de $\\operatorname{Ass}')],
}
R=json.loads((RESULT/'records/ROOT_AUTHOR_VOICE_REVIEW.json').read_text())
candidatekeys={(r['scope']+(':errata' if r['scope']=='IV4' and 'errata' in r['source'] else ''),r['edition'],r['place']) for r in R}
rows=[];edits=collections.defaultdict(list);done=collections.Counter()
for scope,ed,fp,ft,st,p,off,fn in pairs():
 if scope=='IV4' and 'errata' in fp.name:scope='IV4:errata'
 fu=scoped_units(ft,fn);su=scoped_units(st,fn)
 for (sc,n),pp in P.items():
  if scope!=sc or n not in fu or n not in su:continue
  if (sc,ed,n) not in candidatekeys:continue
  u=su[n]
  for old,new in pp:
   pat=r'\s+'.join(re.escape(x) for x in old.split());mm=list(re.finditer(pat,u.text));expected=2 if (sc,n)==('IV2','6.15.7') else 1
   assert len(mm)==expected,(ed,sc,n,old,len(mm))
   for m in mm:
    q,a=resolve(st,u.start+m.start(),p,off);_,b=resolve(st,u.start+m.end(),p,off)
    edits[q].append((a,b,new));rows.append([str(q.relative_to(RESULT)),n,m[0],new,'standard','STANDARDS_20261119b.md register; '+str(fp.relative_to(FR))+' '+n+': French author plural'])
   done[(sc,n)]+=1
assert all(k in done for k in P),(set(P)-set(done))
# The I appendix and II errata carry the same source passage.
old="Sea $\\pi:S\\to S'$ la única aplicación de $S$ en $S'$. Para todo\nabierto $U$ de $S$, la aplicación canónica"
new="Sea $\\pi:S\\to S'$ la única aplicación de $S$ en $S'$; observemos, por otra parte, que para todo\nabierto $U$ de $S$ se tiene una aplicación canónica"
for ed in ['CURRENT','DIPLOMATIC']:
 for p in [ES/f'repo/editions/II_{ed}/EGA_II_es_{ed.lower()}.tex',ES/f'worktree/es/{ed}/EGA_I_apparatus/ega1_errata_list1_tate_1_8_1_to_1_8_6_ES.tex']:
  t=p.read_text();assert old in t,p;a=t.index(old);edits[p].append((a,a+len(old),new));rows.append([str(p.relative_to(RESULT)),'Errata I.1.8.4',old,new,'own comparison','BASE/native/ega2/ega2-errata-addenda-fr.tex I.1.8.4: notons d’autre part que ... on a une application canonique'])
  old2='\ndefine un \\emph{$\\pi$-morfismo}';new2='\nque define un \\emph{$\\pi$-morfismo}';assert t.count(old2)==1;p2=t.index(old2);edits[p].append((p2,p2+len(old2),new2));rows.append([str(p.relative_to(RESULT)),'Errata I.1.8.4',old2,new2,'own comparison','French relative clause following application canonique'])
for p,ee in edits.items():
 t=p.read_text();ee=sorted(set(ee),reverse=True)
 for a,b,new in ee:t=t[:a]+new+t[b:]
 p.write_text(t)
write_tsv(RESULT/'records/CAMBIOS_root_author_voice.tsv',['file','place','before','after','kind','source'],rows)
R=json.loads((RESULT/'records/ROOT_AUTHOR_VOICE_REVIEW.json').read_text());dec=[]
for r in R:
 sc=r['scope']+(':errata' if r['scope']=='IV4' and 'errata' in r['source'] else '');k=(sc,r['place'])
 decision='author plural restored' if k in done or k==('II:errata','1.8.4') else 'retained: first plural in enclitic form, shared clause or following formula interval'
 dec.append([r['scope'],r['edition'],r['place'],r['french_word'],decision])
write_tsv(RESULT/'records/ROOT_AUTHOR_VOICE_DECISIONS.tsv',['scope','edition','place','french_form','decision'],dec)
print('author voice corrections',len(rows))
