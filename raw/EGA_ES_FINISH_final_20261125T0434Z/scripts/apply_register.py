"""Source-bound register corrections; mathematical text and notes are untouched."""
import re,json,collections
from corpus import RESULT,write_tsv
from audit_i_ch1 import i_units
from tex_tools import numbered_units,math_spans
R=json.loads((RESULT.parent/'tmp/register_review.json').read_text())
IMP=r'\b(?:nous|supposons|montrons|prouvons|démontrons|considérons|prenons|posons|notons|remarquons|rappelons|choisissons|utilisons|appliquons|définissons|désignons|écrivons|distinguons|cherchons|raisonnons|représentons|observons)\b'
BASE={'podemos':'se puede','podremos':'se podrá','tenemos':'se tiene','tendremos':'se tendrá','vemos':'se ve','veremos':'se verá','sabemos':'se sabe','sabremos':'se sabrá','obtenemos':'se obtiene','obtendremos':'se obtendrá','concluimos':'se concluye','concluiremos':'se concluirá','deducimos':'se deduce','deduciremos':'se deducirá','decimos':'se dice','diremos':'se dirá','denotamos':'se denota','denotaremos':'se denotará','designamos':'se designa','designaremos':'se designará','llamamos':'se llama','llamaremos':'se llamará','consideramos':'se considera','consideraremos':'se considerará','observamos':'se observa','observaremos':'se observará','notamos':'se nota','notaremos':'se notará','suponemos':'se supone','supondremos':'se supondrá','ponemos':'se pone','pondremos':'se pondrá','tomamos':'se toma','tomaremos':'se tomará','definimos':'se define','definiremos':'se definirá','comprobamos':'se comprueba','comprobaremos':'se comprobará','aplicamos':'se aplica','aplicaremos':'se aplicará','encontramos':'se encuentra','encontraremos':'se encontrará','identificamos':'se identifica','identificaremos':'se identificará','escribimos':'se escribe','escribiremos':'se escribirá','mostramos':'se muestra','mostraremos':'se mostrará','demostramos':'se demuestra','demostraremos':'se demostrará','utilizamos':'se utiliza','utilizaremos':'se utilizará','debemos':'se debe','deberemos':'se deberá','queremos':'se quiere','buscamos':'se busca','haremos':'se hará','hacemos':'se hace','supóngase':'se supone','considérese':'se considera','obsérvese':'se observará','elíjase':'se elige','tómese':'se toma','póngase':'se pone','nos reducimos':'se reduce','nos restringimos':'se restringe','nos limitamos':'se limita'}
for p in ['visto','demostrado','probado','definido','señalado']:BASE['hemos '+p]='se ha '+p
# Ambiguous fragments read individually: keep the author's nous/imperative clause.
MANUAL={3:'se supondrá',44:'se pone',93:'se observará',216:'se pone',233:'se puede',343:'se puede',755:'se puede',779:'se reduce',782:'se puede',791:'se puede',843:'se puede',896:'se puede',897:'se puede',915:'se ha probado',925:'se puede',927:'se puede',930:'se puede',937:'se puede',1014:'se sabe',1016:'se observará',1077:'se puede',1091:'se puede',1147:'se puede',1152:'se puede'}
# Map the same reviewed mixed fragment to the diplomatic layer when identical.
manualkeys={(R[i]['scope'],R[i]['place'],R[i]['before'].lower(),R[i]['fr']):v for i,v in MANUAL.items()}
# Direct phrase choices reviewed above.
OVERRIDES={69:'se ha obtenido',117:'se escribirá',146:'se consideran',150:'se observará',152:'se observará',153:'se escribirá',155:'se definen',168:'se tomará',228:'se dice',716:'se dice',826:'se tienen',1062:'se tomarán'}
overridekeys={(R[i]['scope'],R[i]['place'],R[i]['before'].lower(),R[i]['fr']):v for i,v in OVERRIDES.items()}
edits=collections.defaultdict(list);changes=[];decisions=[]
for i,r in enumerate(R):
 key=(r['scope'],r['place'],r['before'].lower(),r['fr']);pure=re.search(r'\bon\b',r['fr'],re.I) and not re.search(IMP,r['fr'],re.I) and len(r['fr'])<700
 new=manualkeys.get(key) or (overridekeys.get(key,BASE.get(r['before'].lower())) if pure else None)
 decisions.append([str(i),r['file'],r['place'],r['before'],'impersonal source: change' if new else 'review or retain authors plural',re.sub(r'\s+',' ',r['fr'])])
 if new is None:continue
 p=RESULT/r['file'];t=p.read_text();u=(i_units(t) if r['scope']=='I' else numbered_units(t))[r['place']];a=r['unit_position'];b=r['unit_end'];assert u.text[a:b]==r['before'],(i,r['place'])
 if r['before'][0].isupper():new=new[0].upper()+new[1:]
 # Clitics precede the finite verb in the edition: move them after se.
 cm=re.search(r'\b(lo|la|los|las)\s+$',u.text[:a])
 if cm:
  a=cm.start();clitic=cm[1];new=re.sub(r'^[Ss]e ',lambda m:m[0]+clitic+' ',new)
 old=u.text[a:b];edits[p].append((u.start+a,u.start+b,new));changes.append([r['file'],r['place'],old,new,'standard','STANDARDS_20261119b.md register; '+r['source']+': '+r['place']+' ('+r['layer']+')'])
 # Source on peut se ...: the Spanish infinitive must no longer refer to nosotros.
 if r['before'].lower() in ['podemos','podremos','debemos']:
  tail=u.text[b:b+240];stop=re.search(r'[.!?;]\s',tail)
  if stop:tail=tail[:stop.start()]
  rm=re.search(r'\b(reducir|limitar|restringir|referir|remitir|contentar|servir|valer|atener)nos\b',tail)
  if rm:
   ra=b+rm.start();rb=b+rm.end();replacement=rm[1];edits[p].append((u.start+ra,u.start+rb,replacement));changes.append([r['file'],r['place'],rm[0],replacement,'standard','STANDARDS_20261119b.md register; clitic concordance with impersonal on'])
for p,ee in edits.items():
 t=p.read_text();original=t
 ee=sorted(set(ee),reverse=True)
 for j,(a,b,new) in enumerate(ee):
  if j and b>ee[j-1][0]:raise ValueError('Overlapping register edits')
  t=t[:a]+new+t[b:]
 assert [s.text for s in math_spans(t)]==[s.text for s in math_spans(original)],str(p)
 p.write_text(t)
write_tsv(RESULT/'records/CAMBIOS_register_I_IV4.tsv',['file','place','before','after','kind','source'],changes)
write_tsv(RESULT/'records/REGISTER_I_IV4_REVIEW.tsv',['id','file','place','before','decision','source_fragment'],decisions)
print('Edits',len(changes),'files',len(edits))
