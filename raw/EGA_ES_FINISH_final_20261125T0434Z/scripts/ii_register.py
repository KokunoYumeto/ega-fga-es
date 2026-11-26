"""Source-anchored register restoration after bilingual clause review.

The French pronoun and imperative are tested within the aligned prose gap;
mixed-authorial passages are treated explicitly rather than blanket-replaced.
"""
from ii_tools import *
AUTH=re.compile(r'\b(?:nous|notre|nos|supposons|posons|montrons|démontrons|prouvons|considérons|prenons|reprenons|rappelons|notons|voyons|revenons|désignons|écrivons|conservons|définissons|interprétons|recouvrons|commençons|terminons|partons|faisons|indiquons|adoptons|appelons|donnons|passons|gardons|remarquons|observons|explicitons|couvrons|formons)\b',re.I)
VERBS={'podemos':'se puede','podremos':'se podrá','tenemos':'se tiene','tendremos':'se tendrá','sabemos':'se sabe','vemos':'se ve','veremos':'se verá','suponemos':'se supone','supongamos':'se supone','ponemos':'se pone','pongamos':'se pone','pondremos':'se pondrá','denotamos':'se denota','denotemos':'se denota','denotaremos':'se denotará','designamos':'se designa','designemos':'se designa','designaremos':'se designará','decimos':'se dice','diremos':'se dirá','llamaremos':'se llamará','definimos':'se define','definamos':'se define','escribimos':'se escribe','escribiremos':'se escribirá','consideramos':'se considera','consideremos':'se considera','tomamos':'se toma','tomemos':'se toma','tomaremos':'se tomará','obtenemos':'se obtiene','deducimos':'se deduce','concluimos':'se concluye','concluiremos':'se concluirá','concluiríamos':'se concluiría','observamos':'se observa','observemos':'se observa','observaremos':'se observará','señalemos':'se señala','recordemos':'se recuerda','recordamos':'se recuerda','hemos':'se ha','debemos':'se debe','acabamos':'se acaba','hacemos':'se hace','aplicamos':'se aplica','terminamos':'se termina','estamos':'se está','componemos':'se compone','mostremos':'se muestra','identificaremos':'se identificará','hablemos':'se hable','probamos':'se prueba'}
def subcase(t,old,new):
 return re.sub(r'\b'+re.escape(old)+r'\b',lambda m:new[0].upper()+new[1:] if m.group()[0].isupper() else new,t,flags=re.I)
def convert(t,allowed=None):
 if allowed is None:
  for a,b in [('nos vemos reducidos','se reduce'),('nos reducimos','se reduce'),('quedamos reducidos','se reduce'),('nos encontramos','se está'),('nos remitimos','se remite'),('nos guardaremos de creer','se evitará creer')]:t=subcase(t,a,b)
 for a,b in VERBS.items():
  if allowed is None or a in allowed:t=subcase(t,a,b)
 # These pronominal infinitives had the same subject as the converted verb.
 for a,b in [('reducirnos','reducir'),('limitarnos','limitar'),('restringirnos','restringir'),('remitiéndonos','remitiéndose'),('reduciéndonos','reduciéndose')]:t=subcase(t,a,b)
 return t
mixed={
 ('1.4.3',14):{'denotamos'},('4.2.5',5):{'vemos'},('4.2.6',49):{'observamos'},
 ('4.5.9',9):{'decimos'},('4.5.13',21):{'podemos'},
 ('4.6.13.1',35):{'podemos'},('4.6.13.1',45):{'podemos'},
 ('5.2.1',30):{'sabemos'},('7.3.12',20):{'designamos'},
 ('8.2.1',1):{'pondremos'},('8.8.5',10):{'suponemos'},
 ('8.8.6',0):{'escribimos'},('8.10.7',3):{'tomamos'},
 ('8.12.5',0):{'tomamos'},
}
rows=[];review=[]
for ed in ['current','diplomatic']:
 path=espath(ed);t=path.read_text();edits=[]
 for part,ps in parts(t).items():
  for unit,f in units(frpath(ed,part).read_text()).items():
   s=units(ps.text)[unit];fm=math_spans(f.text);sm=math_spans(s.text);assert len(fm)==len(sm)
   fb=[(0,0)]+[(m.start,m.end) for m in fm]+[(len(f.text),len(f.text))];sb=[(0,0)]+[(m.start,m.end) for m in sm]+[(len(s.text),len(s.text))]
   for i in range(len(fb)-1):
    fg=f.text[fb[i][1]:fb[i+1][0]];a,b=sb[i][1],sb[i+1][0];sg=s.text[a:b];new=sg
    if re.search(r'\bon\b',fg,re.I) and not AUTH.search(fg):new=convert(sg)
    elif (unit,i) in mixed:new=convert(sg,mixed[unit,i])
    if unit=='8.3.1' and 'Par abus de langage, nous dirons' in fg:
     new=new.replace('también diremos','también se dirá')
    if unit=='4.2.6' and 'nous obtenons' in fg:new=new.replace('obtenida de este modo','que obtenemos así')
    if unit=='8.10.7' and 'indiquons' in fg:new=new.replace('indicamos brevemente','indiquemos brevemente')
    if unit=='8.11.5' and 'le lemme sera démontré' in fg:
     new=convert(sg).replace('habremos demostrado el lema si se prueba','el lema quedará demostrado si se prueba')
    if unit=='8.14.5' and 'on a défini' in fg:
     new=new.replace('se ha definido','se han definido')
    if unit=='8.9.3' and 'deux homomorphismes canoniques' in fg:
     new=new.replace('se tiene así homomorfismos canónicos','se tienen así dos homomorfismos canónicos')
    if unit=='8.7.2' and 'les formules analogues' in fg:new=new.replace('Se deduce','Se deducen')
    if unit=='8.10.3' and 'on est ramené' in fg:new=new.replace('nos reduce','reduce')
    if unit=='3.6.1' and 'on ramène' in fg:new=new.replace('reducimos el estudio','se reduce el estudio')
    if unit=='8.7.2' and 'On est donc dans' in fg:new=new.replace('lo que nos lleva','lo que lleva')
    if unit=='8.12.6' and 'avec les notations de cette dernière' in fg:
     new=new.replace('(cuyas notaciones adoptamos); reduciéndose','; con las notaciones de esta última, y reduciéndose')
    if new!=sg:
     edits.append((ps.start+s.start+a,ps.start+s.start+b,new));rows.append([str(path.relative_to(ROOT)),part+':'+unit+': gap '+str(i),sg,new,'standard',source_note(ed,part,unit)+'; STANDARDS_20261119b register: impersonal on, authorial nous/imperative retained; French clause: '+re.sub(r'\s+',' ',fg)])
     review.append([ed,part,unit,i,fg,sg,new])
 path.write_text(apply_edits(t,edits))
write('II_CHANGES_register.tsv',HEADER,rows)
write('II_REGISTER_APPLIED_REVIEW.tsv',['edition','part','unit','gap','french','before','after'],review)
print('source-anchored register gaps',len(rows))
