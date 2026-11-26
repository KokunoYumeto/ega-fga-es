"""Apply the two reviewed source distinctions; retain 26 explained lexical alerts."""
import json,re,collections,hashlib
from corpus import RESULT,write_tsv
from tex_tools import math_spans
rows=json.loads((RESULT/'records/OTHER_SCHEME_REVIEW_initial.json').read_text())
assert len(rows)==28
reasons={
0:'La traducción explicita el referente de partout dense: X es el preesquema del mismo párrafo. Se conserva preesquema.',
1:'La fuente completa dice sous-$Y$-schéma; la fórmula divide el compuesto francés. $Y$-subesquema conserva ambos componentes.',
2:'De esquemas afines precede al morfismo escrito en español y sigue a esa misma fórmula en francés. El sustantivo está conservado con el mismo sentido.',
3:'De esquemas afines precede al morfismo escrito en español y sigue a esa misma fórmula en francés. El sustantivo está conservado con el mismo sentido.',
4:'La fuente completa dice sous-$Y$-schéma; la fórmula divide el compuesto francés. $Y$-subesquema conserva ambos componentes.',
5:'La fuente completa dice sous-$Y$-schéma fermé; la fórmula divide el compuesto francés. $Y$-subesquema cerrado conserva el sentido.',
6:'La fuente llama préschéma a U\u2032 y dice que est induit par X\u2032 sur l\u2019ouvert U\u2032. La traducción explicita subpreesquema inducido, conforme al objeto ya definido.',
7:'La fuente llama préschéma a U\u2032_k y dice que est induit par X\u2032. La traducción explicita subpreesquema inducido, conforme al objeto ya definido.',
8:'El título fuente Préschémas entiers sur un autre deja el segundo sustantivo elíptico. Preesquemas enteros sobre otro preesquema conserva ese referente.',
9:'De la base refiere al preesquema S del enunciado. La traducción explicita del preesquema de base sin cambiar el objeto.',
10:'Deux S-morphismes finis se traduce como morfismos finitos de S-preesquemas. La prosa contigua conserva finitud e integralidad y el mismo referente.',
11:'El índice fuente de II, 2.9 dice Sous-préschémas fermés, no sous-schémas. Se restaura Subpreesquemas cerrados.',
12:'En el índice, Préschémas entiers sur un autre se explicita como Preesquemas enteros sobre otro preesquema. Los demás sustantivos del intervalo corresponden uno a uno.',
13:'El español explicita El preesquema ante Z=Spec(B\u2297_A C); la misma frase francesa lo sitúa en la categoría des S-préschémas. Se conserva preesquema.'
}
verdicts=[];changes=[];gloss=[];checks=[];byfile=collections.defaultdict(list)
for r in rows:
 k=r['id']%14;decision='change' if k==11 else 'retain';reason=reasons[k]
 r['decision']=decision;r['reason']=reason
 verdicts.append([r['id'],r['scope'],r['edition'],r['source'],r['place'],r['source_line'],r['class'],decision,reason,r['french'],r['spanish']])
 if decision=='change':
  assert r['source_terms']==['Sous-préschémas','schéma'] and r['target_terms']==['Subesquemas','esquema']
  m=r['spanish_matches'][0];byfile[m['file']].append((m['start'],m['end'],'Subpreesquemas',r))
for file,edits in byfile.items():
 p=RESULT/file;t=p.read_text();out=t
 for a,b,new,r in sorted(edits,reverse=True):
  assert t[a:b]=='Subesquemas'
  out=out[:a]+new+out[b:]
  source=r['source']+':index II.2.9:line '+str(r['source_line'])
  changes.append([file,'II index:2.9',t[a:b],new,'terminology_source_correction',source+'; Sous-préschémas fermés'])
  gloss.append(['sous-préschéma','subpreesquema',source+'; '+r['reason'],file+':index II.2.9','yes'])
 assert [s.text for s in math_spans(t)]==[s.text for s in math_spans(out)]
 for pat in [r'\\label\{[^}]*\}',r'\\tag\{[^}]*\}',r'\\oldpage(?:\[[^\]]*\])?\{[^}]*\}']:
  assert re.findall(pat,t)==re.findall(pat,out)
 p.write_text(out)
 checks.append([file,len(edits),len(math_spans(t)),'unchanged','unchanged',hashlib.sha256(t.encode()).hexdigest(),hashlib.sha256(out.encode()).hexdigest()])
write_tsv(RESULT/'records/OTHER_SCHEME_DECISIONS.tsv',['id','scope','edition','source','place','source_line','screen_class','decision','reason','french','spanish'],verdicts)
write_tsv(RESULT/'records/CAMBIOS_scheme_final_other.tsv',['file','place','before','after','kind','source'],changes)
write_tsv(RESULT/'records/GLOSARIO_REGISTRO_scheme_final_other.tsv',['french_term','spanish_rendering','witness','places','reversible'],gloss)
write_tsv(RESULT/'records/OTHER_SCHEME_STRUCTURE.tsv',['file','atomic_edits','math_spans','math_sequence','labels_tags_pages','before_sha256','after_sha256'],checks)
write_tsv(RESULT/'records/CHECK_EVENTS_scheme_final_other.tsv',['statement_id','date','who','type','outcome'],[
 ['scheme-other','2026-11-25','IA','terminology_source_comparison','3172 source nouns in 121974 formula-bounded intervals screened; 28 alerts read in context. Two Sous-préschémas entries restored in II contents; 26 lexical alerts retained after expanded-context review. Editorial notes and bibliographic titles excluded. No proof verification.'],
 ['scheme-other-structure','2026-11-25','script','structural_comparison','Two changed II monoliths preserve ordered mathematical spans, labels, tags and original-page markers exactly.']])
(RESULT/'records/OTHER_SCHEME_REVIEW_RESOLVED.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'alerts_reviewed':len(rows),'changed':len(changes),'retained':len(rows)-len(changes),'files_changed':len(checks)}))
