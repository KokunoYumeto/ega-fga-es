#!/usr/bin/env python3
"""Source-aligned register decisions. Run once against the audited III state."""
from iii_register_candidates import *
import csv

# Each replacement was read against the source fragment bounded by consecutive
# source-identical formulas. These are editorial checks, not proof checks.
OVERRIDE={
'1:8.1.3:24':'; si se designa por ',
'1:8.1.3:28':',\n',
'1:8.2.6:3':r" con las propiedades del \emph{inverso} en un grupo; como para todo morfismo ",
'1:10.2.8:32':'\n',
'1:10.3.1:102':', se tenga ',
'1:10.3.1:166':',\n',
'1:10.3.1:241':';\n',
'1:11.1.1:54':' están definidos, y designando por ',
'1:11.2.2:33':'. Se definen también los ',
'1:11.2.2:40':' deducido como arriba de una sucesión exacta de cohomología. Se toma como ',
'1:11.5.2:13':r'; forman evidentemente una \emph{categoría abeliana} ',
'1:11.9.1:63':', los objetos ',
'1:12.1.7:45':r', y al pasar a la cohomología, se obtiene por tanto el \emph{mismo} homomorfismo; en otros términos, se ha mostrado que el homomorfismo de borde (\hyperref[0.12.1.7.5-fr]{12.1.7.5}), que se escribe ',
'1:12.2.5:13':r", se ve que, componiendo (\hyperref[0.12.2.5.4-fr]{12.2.5.4}) y (\hyperref[0.12.2.5.3-fr]{12.2.5.3}), se obtiene un homomorfismo de prehaces, que proporciona el homomorfismo de haces (\hyperref[0.12.2.5.1-fr]{12.2.5.1})."+'\n\n'+r'La definición de (\hyperref[0.12.2.5.2-fr]{12.2.5.2}) es aún más simple; por definición, ',
'1:12.3.5:11':' puesto que ',
'1:13.4.1:6':r' una \emph{filtración} ',
'1:13.7.2:10':', la resolución inyectiva de ',
'1:13.7.6:28':'. Se denotará también por ',
'1:2.2.3:18':' es exacta; por consiguiente, se puede suponer que ',
'1:2.2.4:19':'; se puede pues limitar al caso en que ',
'1:2.2.4:21':r' (\textbf{II}, 4.6.11), y por consiguiente se puede identificar ',
'1:2.2.4:61':'. Dicho esto, se ve, como al comienzo de la demostración de (2.2.2), que se puede limitar al caso en que ',
'1:3.4.1:46':r' un morfismo \emph{de tipo finito} (\textbf{I}, 10.13.3); siendo las notaciones las mismas que arriba, se dice que una parte ',
'1:3.4.4:38':', y se puede pues suponer, para tratarla, que ',
'1:4.1.2:3':r' (\textbf{I}, 5.2.1); se sabe (\textbf{I}, 4.4.5) que ',
'1:4.1.2:21':r'-Módulo (\textbf{0}, 12.2.1) y se deduce por tanto de (\hyperref[III.4.1.2.1-fr]{4.1.2.1}) un homomorfismo ',
'1:4.1.3:1':r' el morfismo canónico de espacios anillados definido en (\textbf{I}, 10.8.7), de modo que se tiene el diagrama conmutativo ',
'1:4.1.3:9':r' (\textbf{I}, 10.8.8) salvo isomorfismo canónico. Se sabe que se tiene ',
'1:4.1.3:18':r', se tienen, teniendo en cuenta (\hyperref[III.1.4.11-fr]{1.4.11}), homomorfismos ',
'1:4.1.4:3':r'-Módulo coherente (\hyperref[III.3.2.1-fr]{3.2.1}), se tiene ',
'1:4.1.4:6':r' es \emph{conmutativo}. Basta evidentemente probar la conmutatividad del diagrama correspondiente de homomorfismos de prehaces, luego se puede limitar al caso en que ',
'1:4.2.2:15':'-preádica es nulo, y como esta topología es separada, se tiene también ',
'1:4.2.3:1':'; se obtiene pues el corolario siguiente:\n'+r'\end{env}'+'\n\n',
'1:4.3.4:6':', la fibra ',
'1:4.3.10:8':') es geométricamente conexa.\n'+r'\end{corollary}'+'\n\n'+r'\begin{proof}'+'\nSe puede limitar al caso en que ',
'1:4.4.1:19':'; se puede pues limitar al caso en que ',
'1:4.4.3:16':r' (\textbf{II}, 5.3.2 y 5.5.1). Se reduce pues a demostrar el teorema cuando ',
'1:4.4.9:17':r' tienen el mismo cuerpo de fracciones (\textbf{I}, 7.1.5). Se puede pues aplicar (\hyperref[III.4.4.8-fr]{4.4.8}), y si ',
'1:4.8.8:12':r' es la misma que en (\textbf{II}, 1.1.2), y para ver que es biyectiva, se reduce inmediatamente al caso en que ',
'6:6.4.3:6':' como complejos de Módulos, se denotará por ',
'6:6.5.1:20':', (siendo nulos los demás), se escribirá ',
'6:6.5.6:6':', se puede suponer ',
'6:6.5.11:17':'-Módulos cuasicoherentes (6.5.1); se reduce fácilmente al caso en que ',
'6:6.6.2:23':' su hipertor. Se designará por ',
'6:6.6.8:27':'. Se denotará por ',
'7:7.6.8:15':r' sea reducido, se puede, en virtud de (7.6.7), limitar al caso en que ',
'7:7.6.9:25':r' (\textbf{II}, 7.1.9). En virtud de la fórmula (7.6.7.1), se ve que se reduce a demostrar la desigualdad ',
'7:7.9.10:12':'.\n'+r'\end{lemma}'+'\n\n'+r'\begin{proof}'+'\nEn efecto, se puede limitar al caso en que ',
# Mixed author/impersonal spans and source futures/imperatives.
'1:8.1.6:0':r'\begin{env}[8.1.6]'+'\n'+r'\label{0.8.1.6-fr}'+'\n'+r'Apliquemos la prop. (\hyperref[0.8.1.4-fr]{8.1.4}) al caso en que el funtor ',
'1:11.4.4:22':', lo que establece nuestras aserciones. Cuando se supone que en ',
'1:11.7.1:6':', y es lo que haremos en adelante. Se puede considerar ',
'1:12.1.7:1':r'; vamos a ver que el dihomomorfismo definido en (\hyperref[0.12.1.3-fr]{12.1.3}) ',
'1:4.1.8:0':r'\begin{env}[4.1.8]'+'\n'+r'\label{III.4.1.8-fr}'+'\n'+r'Pasemos finalmente a la demostración de (\hyperref[III.4.1.5-fr]{4.1.5}): para todo abierto afín ',
'6:6.3.8:8':'. Vamos a ver que se puede definir un ',
'6:6.10.6:7':'; veremos más adelante (7.7.12, (i)) que se puede entonces suponer que ',
'7:7.6.9:27':r"; pero esto no es sino la desigualdad (7.6.5.1)\footnote{El principio de demostración de (i) por reducción al caso de un anillo de valuación discreta nos fue comunicado oralmente por Hironaka.}."+'\n'+r'\item[(ii)] La primera aserción ya ha sido demostrada (7.3.4). Para demostrar la recíproca, utilicemos el criterio valuativo (7.6.2); teniendo en cuenta la fórmula (7.6.7.1), se reduce pues al caso en que ',
'7:7.8.10:16':r' (es lo que llamaremos un \emph{revestimiento étale} de ',
}
SUBS={
'1:8.1.1:0': [('Denotamos','Denotaremos')],
'1:8.1.1:5': [('ponemos','pondremos')],
'1:8.1.1:8': [('denotamos','denotaremos')],
'1:8.1.2:5': [('denotamos','designemos')],
'1:8.2.1:17':[('llamamos','llamaremos')],
'1:9.3.2:16':[('aplicamos','apliquemos')],
'1:10.1.1:8':[('Denotamos','Denotaremos')],
'1:11.1.1:0':[('utilizamos','utilizaremos'),('llamamos','llamaremos')],
'1:11.2.1:16':[('Denotamos','Denotaremos')],
'1:11.2.1:48':[('denotamos','denotaremos')],
'1:11.3.1:35':[('denotamos','denotaremos')],
'1:11.3.2:5':[('denotamos','denotaremos')],
'1:12.4.5:10':[('Llamamos','Llamaremos')],
'1:12.4.5:12':[('denotamos','denotaremos')],
'1:13.6.4:17':[('llamamos','llamaremos')],
'1:2.1.7:0':[('Aplicamos ahora','Vamos a aplicar')],
'1:3.4.5:18':[('hemos demostrado','se ha demostrado'),('Demostremos ahora','Probemos después')],
'6:6.7.10:31':[('consideramos','consideraremos'),('cubrimientos','recubrimientos')],
'6:6.7.10:35':[('consideramos','consideraremos'),('cubrimientos','recubrimientos')],
}

def preserve_case(s,new):return new[0].upper()+new[1:] if s[0].isupper() else new
def impersonal(t):
 t=re.sub(r'\bnos reducimos\b',lambda m:preserve_case(m[0],'se reduce'),t,flags=re.I)
 t=PATT.sub(lambda m:preserve_case(m[0],VERBS[m[0].lower()]),t)
 t=re.sub(r'\b(limit|reduc|restring)irnos\b',lambda m:m[1]+'irse',t) if False else t
 t=t.replace('limitarnos','limitar').replace('reducirnos','reducir').replace('restringirnos','restringir')
 for x,y in [('se define de manera análoga los','se definen de manera análoga los'),('Se define de manera análoga los','Se definen de manera análoga los'),('Se define análogamente los','Se definen análogamente los'),('se define los','se definen los'),('se tiene las implicaciones','se tienen las implicaciones'),('se tiene notaciones','se tienen notaciones'),('Adoptamos las convenciones análogas','Se adoptarán convenciones análogas')]:t=t.replace(x,y)
 return t

def run():
 sets={};resolved={};decisions=[]
 for ed,part in [('current','1'),('diplomatic','1'),('current','6'),('current','7')]:
  f,e,b,p,g=compare(ed,part);assert not g;sets[ed,part]=(b,list(segments(ed,part)))
 for (ed,part),(b,ss) in sets.items():
  if ed!='current':continue
  for x in ss:
   k=x['id'].split(':',1)[1]
   if k in OVERRIDE:resolved[part,x['place'],x['f']]=OVERRIDE[k]
   elif k in SUBS:
    t=x['e']
    for a,z in SUBS[k]:assert a in t,(k,a);t=t.replace(a,z)
    resolved[part,x['place'],x['f']]=t
 for (ed,part),(b,ss) in sets.items():
  edits=[]
  for x in ss:
   k=x['id'].split(':',1)[1];key=(part,x['place'],x['f'])
   candidate=bool(PATT.search(x['e']))
   if key in resolved:new=resolved[key];reason='Source clause, author tense or source punctuation restored after contextual reading'
   elif ed=='diplomatic' and k=='1:12.2.5:13':new=OVERRIDE[k];reason='Printed spelling homcmorphisme has no Spanish consequence; source reference order restored'
   elif candidate and not x['author']:new=impersonal(x['e']);reason='French on/non-author clause rendered impersonally after reading the aligned span'
   elif candidate:new=x['e'];reason='Authors’ first plural retained after checking the French clause'
   else:continue
   if new!=x['e']:
    # A long introductory segment may cross a reader/input boundary. Here all
    # replacements are local; source-adjacent only changes are split if needed.
    if any(q[0]<=x['estart'] and x['eend']<=q[1] for q in b):edits.append((x['estart'],x['eend'],new,x['place'],x['e']))
    else:
     for tag,i,j,k,l in difflib.SequenceMatcher(None,x['e'],new,autojunk=False).get_opcodes():
      if tag!='equal':edits.append((x['estart']+i,x['estart']+j,new[k:l],x['place'],x['e'][i:j]))
   decisions.append(dict(id=x['id'],edition=ed,part=part,place=x['place'],source_sha256=__import__('hashlib').sha256(x['f'].encode()).hexdigest(),before=x['e'],after=new,changed=new!=x['e'],reason=reason))
  if edits:apply_edits(ed,part,edits,b)
  print(ed,part,len(edits))
 (ROOT/'records/III_REGISTER_DECISIONS.json').write_text(json.dumps(decisions,ensure_ascii=False,indent=2)+'\n')
 print('decisions',len(decisions),'changed',sum(x['changed'] for x in decisions))
if __name__=='__main__':run()
