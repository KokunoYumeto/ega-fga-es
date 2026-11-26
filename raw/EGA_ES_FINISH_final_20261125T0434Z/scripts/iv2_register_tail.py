#!/usr/bin/env python3
"""Source-context corrections for mixed register clauses and remaining pronouns in IV-2."""
import re
import audit_iv2_alignment as a
import reconcile_iv2 as r
# place at the following formula, a unique French prose witness, Spanish pattern, replacement
RULES=[
('2.1.5','autrement dit, on est ramené à prouver',r'quedamos\s+reducidos','la cuestión se reduce'),
('2.4.2','de la même manière, on pose les définitions suivantes',r'damos\s+las\s+definiciones\s+siguientes','se dan las definiciones siguientes'),
('2.4.3','on sait que (iv) découle',r'sabemos que','se sabe que'),
('6.13.7.1','On remarque d\'abord que l\'on peut supposer',r'Observamos primero que podemos','Se observa primero que se puede'),
('6.13.7.1','on passe au cas général',r'pasamos al caso general','se pasa al caso general'),
('6.13.7.1','on voit cette fois que',r'vemos esta vez que','se ve esta vez que'),
('7.3.17','on obtient l\'énoncé',r'obtenemos\s+el\s+enunciado','se obtiene el enunciado'),
('7.4.4.1','montrons d\'abord que l\'on peut raisonner',r'podemos razonar','se puede razonar'),
('7.4.4.2',r"Montrons qu'\emph{on peut se ramener au cas où}",r'podemos reducirnos','es posible reducirse'),
('2.2.7','on peut (en remplaçant',r'se puede','es posible'),
('2.2.7',') se ramener au cas où',r'reducirnos','reducirse'),
('4.6.21','après réduction au cas où',r'reducirnos','reducir la cuestión'),
('6.10.6','cela permet de se borner',r'limitarnos','limitarse'),
('6.11.9','En se restreignant à des voisinages ouverts affines',r'Restringiéndonos','Al restringirse'),
('6.14.1.1','le procédé du début permet de se borner',r'limitarnos','limitarse'),
('4.4.1','ce qui précède nous montre déjà',r'lo anterior muestra ya','lo anterior nos muestra ya'),
('6.14.1.4','dans le cas où nous nous sommes placés',r'En el caso considerado,','En el caso en que nos hemos situado,'),
('6.7.4.1','Distinguons deux cas',r'Distinguimos','Distingamos'),
('6.11.6.1','Distinguons alors deux cas',r'Distinguimos','Distingamos'),
('6.12.4','Distinguons maintenant deux cas',r'Distinguimos','Distingamos'),
('6.12.7','Distinguons deux cas',r'Distinguimos','Distingamos'),
('4.7.3','autrement dit, supposer que',r'podemos','se puede'),
('6.10.6',', supposer que',r'podemos','se puede'),
('6.11.6.1',', supposer que',r'podemos','se puede'),
('6.12.4.1',', supposer que',r'podemos','se puede'),
('7.4.4.2','La conclusion à prouver',r'que debemos demostrar','que hay que demostrar'),
('7.4.4.2',"L'assertion à démontrer",r'que debemos demostrar','que hay que demostrar'),
('7.5.7.1','Le raisonnement de I) ramène encore',r'nos reduce de nuevo','reduce de nuevo la cuestión'),
]
def run(layer):
 f,e,bounds,paired,gaps=a.compare(layer);assert not gaps
 paired.sort(key=lambda v:v['fstart']);edits=[];counts=[0]*len(RULES)
 for prev,nxt in zip(paired,paired[1:]):
  fr=' '.join(f[prev['fend']:nxt['fstart']].split());es=e[prev['eend']:nxt['estart']]
  for idx,(place,witness,pattern,replacement) in enumerate(RULES):
   if nxt['place']!=place or witness not in fr:continue
   matches=list(re.finditer(pattern,es))
   for m in matches:
    edits.append((prev['eend']+m.start(),prev['eend']+m.end(),replacement,place,m[0],'standard/STANDARDS_20261119b.md register; EGA_ES_FINISH_1_FRANCES/fr/'+layer.lower()+'/IV2/native/ega4/ega4-2-fr.tex, IV.'+place));counts[idx]+=1
 r.apply_span_edits(layer,edits,bounds)
 print(layer,'tail register edits',len(edits),'rules with no preimage',[i+1 for i,n in enumerate(counts) if n==0])
 # Both French layers retain suite de composition; restore this terminology in the current text.
 if layer=='CURRENT':
  r.change('tree/worktree/es/CURRENT/EGA_IV2/ega4-2_6.9.1_6.9.2_ES.tex','6.9.2','Se sabe que existe una filtración finita','Se sabe que existe una sucesión de composición','own comparison','EGA_ES_FINISH_1_FRANCES/fr/current/IV2/native/ega4/ega4-2-fr.tex, IV.6.9.2')
if __name__=='__main__':
 for layer in ['CURRENT','DIPLOMATIC']:run(layer)
