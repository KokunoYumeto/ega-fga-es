#!/usr/bin/env python3
from iii_bridge_patch import *
VERBS={
 'tenemos':'se tiene','vemos':'se ve','podemos':'se puede','sabemos':'se sabe','ponemos':'se pone','denotamos':'se denota','designamos':'se designa','deducimos':'se deduce','obtenemos':'se obtiene','concluimos':'se concluye','observamos':'se observa','notamos':'se observa','consideramos':'se considera','definimos':'se define','encontramos':'se encuentra','comprobamos':'se comprueba','verificamos':'se verifica','demostramos':'se demuestra','probamos':'se prueba','recordamos':'se recuerda','tomamos':'se toma','suponemos':'se supone','elegimos':'se elige','aplicamos':'se aplica','identificamos':'se identifica','reducimos':'se reduce','escribimos':'se escribe','llegamos':'se llega','pasamos':'se pasa','llamamos':'se llama','entendemos':'se entiende',
 'podremos':'se podrá','tendremos':'se tendrá','veremos':'se verá','diremos':'se dirá','denotaremos':'se denotará','designaremos':'se designará','obtendremos':'se obtendrá','deduciremos':'se deducirá','concluiremos':'se concluirá','llamaremos':'se llamará',
 'hemos':'se ha','habíamos':'se había','habremos':'se habrá',
 'basta con que demostremos':'basta demostrar',
 'podríamos':'se podría','tendríamos':'se tendría','tendríamos':'se tendría','obtendríamos':'se obtendría',
}
AUTHOR=re.compile(r'\b(?:nous|notre|nos|posons|supposons|montrons|prouvons|désignons|notons|remarquons|considérons|rappelons|passons|revenons|définissons|calculons|appliquons|prenons|donnons|procédons|raisonnons|distinguons|identifions|établissons|vérifions|utilisons|observons|examinons|fixons|bornons)\b',re.I)
PATT=re.compile(r'\b(?:'+ '|'.join(map(re.escape,sorted(VERBS,key=len,reverse=True)))+r')\b',re.I)
def segments(ed,part):
 f,e,b,p,g=compare(ed,part);assert not g
 for (k,fa,fb),(_,ea,eb) in zip(sections(f),sections(e)):
  qq=[q for q in p if q['place']==k];fpos=[fa]+[q['fend'] for q in qq];ePos=[ea]+[q['eend'] for q in qq];fends=[q['fstart'] for q in qq]+[fb];eends=[q['estart'] for q in qq]+[eb]
  for i,(a,z,c,d) in enumerate(zip(fpos,fends,ePos,eends)):
   if a==z and c==d:continue
   yield dict(id=f'{ed}:{part}:{k}:{i}',edition=ed,part=part,place=k,fstart=a,fend=z,estart=c,eend=d,f=f[a:z],e=e[c:d],author=bool(AUTHOR.search(f[a:z])))
def run():
 out=[]
 for ed,part in [('current','1'),('diplomatic','1'),('current','6'),('current','7')]:
  for x in segments(ed,part):
   ms=list(PATT.finditer(x['e']))
   if ms:x['verbs']=[m[0] for m in ms];out.append(x)
 (ROOT/'records/III_REGISTER_CANDIDATES.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print('candidates',len(out),'impersonal',sum(not x['author'] for x in out))
 for x in out:
  if x['edition']=='diplomatic' or x['author']:continue
  print(x['id'],x['verbs'],'FR',repr(x['f']),'ES',repr(x['e']))
if __name__=='__main__':run()
