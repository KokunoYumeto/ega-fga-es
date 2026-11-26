"""Record reviewed inherited-note differences; never edit edition sources."""
import re,json,csv,difflib,collections,hashlib
from pathlib import Path
from corpus import RESULT,SOURCE,FR,write_tsv
from tex_tools import balanced_end,math_spans,ENV_RE,numbered_units

def notes(t):
 out=[]
 for m in re.finditer(r'\\footnote(?:text)?(?:\[[^]]*\])?\{',t):
  b=balanced_end(t,m.end()-1);out.append((m.start(),b,t[m.start():b]))
 return out
def norm(t):return re.sub(r'\s+','',t)
def mathseq(t):return [norm(x.text) for x in math_spans(t)]
def pick(p,needle):
 t=p.read_text();nn=[x for x in notes(t) if needle in re.sub(r'\s+',' ',x[2])]
 assert len(nn)==1,(p.name,needle,len(nn));a,b,s=nn[0]
 return {'source':str(p.relative_to(SOURCE)),'source_line':t.count('\n',0,a)+1,'source_note':s}
def original_file(file):
 p=SOURCE/'EGA_ES_FINISH_2_ESPANOL'/file.removeprefix('tree/')
 if not p.exists():p=Path(str(p).replace('DIPLOMATIC','CURRENT').replace('.diplomatic.tex','.tex'))
 assert p.is_file();return p

raw=json.loads((RESULT/'records/INHERITED_NOTE_DIFFERENCES.json').read_text())
assert len(raw)==20
specs={
 0:('BASE/native/ega3/ega3-1-fr.tex','Le chapitre IV'),
 1:('BASE/native/ega3/ega3-1-fr.tex','La démonstration qui suit'),
 2:('BASE/native/ega3/ega3-1-fr.tex','La dernière expression'),
 3:('BASE/native/ega3/ega3-1-fr.tex','Le chapitre IV'),
 4:('BASE/native/ega3/ega3-1-fr.tex','La démonstration qui suit'),
 5:('BASE/native/ega3/ega3-1-fr.tex','La dernière expression'),
 6:('BASE/native/ega3/ega3-7-fr.tex','Hironaka'),
 7:('BASE/native/ega1/ega0-1-fr.tex','solution du problème universel'),
 8:('BASE/native/ega1/ega1-3-fr.tex',r'La notation $\operatorname{Hom}_A'),
 10:('BASE/native/ega1/ega1-3-fr.tex',r'La notation $\operatorname{Hom}_A'),
 12:('IV3/native/ega4/ega4-11-fr.tex','Bourbaki'),
 13:('IV3/native/ega4/ega4-8-fr.tex','purement'),
 14:('IV3/native/ega4/ega4-8-fr.tex','corollaires (8.12.8)'),
 17:('IV4/native/ega4/ega4-18-fr.tex','18.10.16'),
 19:('IV4/native/ega4/ega4-21c-fr.tex','Seshadri suppose'),
}
reasons={
0:'Nota mixta: la frase autoral se traduce según el francés; la apóstilla [Trad.] Estos cuatro últimos capítulos nunca se publicaron se conserva literalmente, con su marcado. La capa diplomática original carece de esta apóstilla y no se la añade.',
1:'Nota autoral de agradecimiento a Serre. La redacción y H^n(X,mathcal F) siguen el francés; se conserva íntegramente la atribución y el complemento sobre la filtración.',
2:'Nota autoral que define el conjunto de homomorfismos de álgebras. Designa traduce désigne y las fórmulas restauran las macros literales francesas; el objeto no cambia.',
3:'Nota autoral de la introducción del capítulo III. Capítulo IV, §§8 a 11 y la previsión de publicación corresponden al francés. No existía apóstilla [Trad.] en esta capa.',
4:'Nota autoral de agradecimiento a Serre. La redacción y H^n(X,mathcal F) siguen el francés; se conserva íntegramente la atribución y el complemento sobre la filtración.',
5:'Nota autoral que define el conjunto de homomorfismos de álgebras. Designa traduce désigne y las fórmulas restauran las macros literales francesas; el objeto no cambia.',
6:'Nota autoral de atribución a Hironaka. Principio de demostración traduce principe de démonstration; se conserva oralmente, la reducción indicada y la terminología heredada valuación.',
7:'Nota autoral: la cláusula definido por la condición que reproduce défini par la condition que del francés corregido. Se retira la especificación de componentes añadida en la traducción antigua, que no figura en esta nota francesa. Las fórmulas finales coinciden con la fuente; no se valida el argumento matemático.',
8:'Nota autoral: footnote pasa a footnotetext como en la fuente y Hom_A adopta operatorname{Hom}_A; se conserva íntegro el sentido de homomorfismos de álgebras.',
9:'Nota editorial española íntegra con normalización terminológica exigida para toda la edición: un entorno pasa a una vecindad. Fórmulas y afirmación editorial se conservan. La mención de de x describe la lectura impresa, confirmada por la capa francesa diplomática; el francés corregido ya dice de y.',
10:'Nota autoral: footnote pasa a footnotetext como en la fuente y Hom_A adopta operatorname{Hom}_A; se conserva íntegro el sentido de homomorfismos de álgebras.',
11:'Nota editorial española íntegra con normalización terminológica exigida para toda la edición: un entorno pasa a una vecindad. Fórmulas y afirmación editorial se conservan. La lectura de x de la capa francesa diplomática confirma su referencia al impreso.',
12:'Falso missing del emparejamiento por similitud. La nota autoral de Bourbaki está íntegra. Se cotejó su texto completo; M,N,P,Q,R,A,B y las referencias recuperan la notación francesa, se conserva la cadena completa de afirmaciones y la atribución. La baja similitud proviene principalmente de las antiguas macros mathrm. Cotejo textual, no comprobación de la demostración.',
13:'Nota autoral: On notera pasa a Se observará; la frase sobre los espacios subyacentes a los espacios analíticos reproduce el francés y sustituye la formulación española menos precisa. X,Y y C recuperan la notación fuente.',
14:'Nota autoral preservada: footnotetext con marca manual pasa a footnote como en francés; se elimina solo la marca manual redundante y se conserva la afirmación sobre los corolarios 8.12.8–8.12.11 y §9.',
16:'Nota editorial española íntegra con normalización terminológica exigida para toda la edición: liso pasa a suave. Las fórmulas y la explicación heredada del punto Delta(x)=(x,x) no cambian; la frase francesa conserva lisse sur S en x.',
17:'Nota autoral preservada; cuasi-proyectivo pasa a cuasiproyectivo por el estándar. Todas las referencias y las hipótesis coinciden con la nota francesa.',
18:'Nota editorial española íntegra con normalización terminológica exigida para toda la edición: al entorno pasa a a la vecindad. Las fórmulas y el comentario heredado sobre V y X no cambian; no se convierte dicho comentario en una corrección silenciosa del texto francés.',
}
reasons[15]='Nota editorial española íntegra con normalización terminológica exigida para toda la edición: lisura pasa a suavidad. Se conservan literalmente las referencias (17.5.9) y (17.5.1) y la afirmación editorial heredada. La fuente francesa confirma la cita impresa (17.5.9); esta revisión no comprueba el criterio matemático.'
reasons[19]='Nota autoral de Seshadri conservada íntegramente. Obsérvese también que pasa a Observemos también que para preservar el plural autoral Notons aussi que. Ninguna otra palabra ni fórmula cambia. Se cotejó la nota francesa completa; no se verifica su demostración.'
places={0:'III front',1:'III.4.1.7',2:'III.4.8.8',3:'III front',4:'III.4.1.7',5:'III.4.8.8',6:'III.7.6.9',7:'0.3.2.2',8:'I.3.2.2',9:'I.6.6.3',10:'I.3.2.2',11:'I.6.6.3',12:'IV.11.1.2',13:'IV.8.1.3',14:'IV.8.12.8',15:'IV.17.13.4',16:'IV.17.13.5',17:'IV.18.10.16',18:'IV.21.13.10',19:'IV.21.14.4'}
review=[];evidence=[];snapshots={}
for i,r in enumerate(raw):
 p=RESULT/r['file'];t=p.read_text();q=original_file(r['file']);old=q.read_text()
 assert r['before'] in old,(i,'original note not found')
 after=r['after']
 if after is None:
  ns=[x for x in notes(t) if 'Bourbaki' in x[2]];assert len(ns)==1;pos,end,after=ns[0]
 else:
  ns=[x for x in notes(t) if x[2]==after];assert len(ns)==1;(pos,end,_)=ns[0]
 if i==15: assert r['before'].replace('lisura','suavidad')==after
 if i==19: assert r['before'].replace('Obsérvese','Observemos')==after
 edition='diplomatic' if 'DIPLOMATIC' in r['file'] else 'current'
 category='editorial_original_with_standard_normalization' if i in {9,11,15,16,18} else 'mixed_author_and_editorial' if i==0 else 'author_note_source_translation'
 if i in specs:
  rel,needle=specs[i];z=pick(FR/edition/rel,needle)
  source_math=mathseq(z['source_note']);target_math=mathseq(after)
  assert source_math==target_math,(i,'source note math mismatch',source_math,target_math)
  integrity=f'{len(source_math)} ordered mathematical spans agree with French, whitespace ignored'
  relation='direct French note'
 else:
  if i in {9,11}:rel='BASE/native/ega1/ega1-6-fr.tex';source_ed='diplomatic';unit='6.6.3';needle='W_1(x)'
  elif i==15:rel='IV4/native/ega4/ega4-17-fr.tex';source_ed='current';unit='17.13.4';needle='(17.5.9)'
  elif i==16:rel='IV4/native/ega4/ega4-17-fr.tex';source_ed='current';unit='17.13.5';needle='lisse'
  else:rel='IV4/native/ega4/ega4-21c-fr.tex';source_ed='current';unit='21.13.10';needle=r'à $V\setmin'
  fp=FR/source_ed/rel;ft=fp.read_text();u=numbered_units(ft)[unit];a=u.text.find(needle);assert a>=0
  context=u.text[max(0,a-180):min(len(u.text),a+420)]
  z={'source':str(fp.relative_to(SOURCE)),'source_line':ft.count('\n',0,u.start+a)+1,'source_note':context}
  assert mathseq(r['before'])==mathseq(after),(i,'editorial formula altered')
  integrity=f'{len(mathseq(after))} ordered mathematical spans identical to inherited note'
  relation='inherited Spanish editorial note; French body is contextual witness, not a source note'
 if i==0:
  apost=r'\emph{[Trad.] Estos cuatro últimos capítulos nunca se publicaron.}'
  assert apost in r['before'] and apost in after
  integrity+='; editorial apostilla byte-identical'
 verdict='retained_complete_source_faithful' if category!='editorial_original_with_standard_normalization' else 'retained_complete_terminology_normalized'
 if i==12:verdict='false_missing_resolved_complete'
 risk='No unauthorized semantic alteration detected in this textual comparison; no mathematical proof verification.'
 source=z['source']+':line '+str(z['source_line'])
 review.append([i,r['file'],places[i],str(q.relative_to(SOURCE)),category,verdict,r['before'],after,source,relation,reasons[i],integrity,risk,'closed'])
 evidence.append({'id':i,'file':r['file'],'place':places[i],'original_source':str(q.relative_to(SOURCE)),'before':r['before'],'after':after,'source_witness':z,'source_relation':relation,'reason':reasons[i],'math_integrity':integrity,'target_line':t.count('\n',0,pos)+1,'status':'closed'})
 snapshots[r['file']]=hashlib.sha256(t.encode()).hexdigest()

write_tsv(RESULT/'records/INHERITED_NOTE_FINAL_REVIEW.tsv',['id','file','place','original_spanish_source','note_class','verdict','before','after','french_witness','source_relation','reason','integrity','risk','status'],review)
(RESULT/'records/INHERITED_NOTE_FINAL_EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
(RESULT/'records/INHERITED_NOTE_REVIEW_SOURCE_HASHES.json').write_text(json.dumps(snapshots,ensure_ascii=False,indent=2)+'\n')

# Explain the four-note increase in comparable files as well as preservation.
added=[]
for ed in ['current','diplomatic']:
 layer=ed.upper();file=f'tree/repo/editions/III1_{layer}/EGA_III1_ES_{layer}_READER.tex'
 p=RESULT/file;t=p.read_text();a,b,s=next(x for x in notes(t) if 'Para facilitar la búsqueda' in x[2])
 z=pick(FR/ed/'BASE/native/ega3/ega3-1-fr.tex','Pour faciliter la recherche')
 assert mathseq(s)==mathseq(z['source_note'])
 added.append([file,'III1 chapter 0 front','authorial source note newly translated','',s,z['source']+':line '+str(z['source_line']),z['source_note'],'Nota autoral francesa antes ausente, ahora traducida íntegramente; sus fórmulas coinciden con la fuente.','closed'])
file='tree/worktree/es/CURRENT/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex';p=RESULT/file;t=p.read_text()
a,b,s=next(x for x in notes(t) if 'La demostración impresa en la fuente francesa es insuficiente' in x[2]);body=s[s.index('{')+1:-1]
q=original_file(file);assert body in q.read_text()
added.append([file,'I.5.3.9','inherited editorial prose moved to a footnote',body,s,str(q.relative_to(SOURCE))+':I.5.3.9',body,'La frase editorial ya existía literalmente en el cuerpo español. Se preserva como nota al restituir el cuerpo francés; no se ha introducido una nueva evaluación matemática.','closed'])
file='tree/worktree/es/PORTED_20261109/IV1_CURRENT/ega4/ega0-15-es.tex';p=RESULT/file;t=p.read_text()
a,b,s=next(x for x in notes(t) if 'Precisión editorial' in x[2])
z=pick(FR/'current/IV1/native/ega4/ega0-15-fr.tex','Précision éditoriale')
assert mathseq(s)==mathseq(z['source_note'])
added.append([file,'0.15.1.8','corrected French editorial note newly translated','',s,z['source']+':line '+str(z['source_line']),z['source_note'],'Nota editorial presente en el francés corregido, antes ausente de la traducción. Se traslada íntegra con sus fórmulas; no se afirma haber comprobado su argumento.','closed'])
write_tsv(RESULT/'records/INHERITED_NOTE_ADDITIONS_REVIEW.tsv',['file','place','note_class','before','after','source','source_text','reason','status'],added)
assert len(added)==4
audit=list(csv.DictReader((RESULT/'records/INHERITED_NOTE_AUDIT.tsv').open(),delimiter='\t'))
counts={k:sum(int(x[k]) for x in audit) for k in ['original_notes','current_notes','verbatim_retained','modified_candidates','unmatched_original_notes']}
assert counts=={'original_notes':264,'current_notes':268,'verbatim_retained':244,'modified_candidates':19,'unmatched_original_notes':1}
counts.update({'reviewed_differences':20,'authorial_source_notes':14,'mixed_authorial_editorial':1,'editorial_terminology_normalizations':5,'false_missing_resolved':1,'added_or_relocated_notes_explained':4,'unresolved':0,'unauthorized_semantic_changes_detected':0,'source_files_modified_by_this_audit':0,'mathematical_proof_verification':False})
(RESULT/'records/INHERITED_NOTE_FINAL_COUNTS.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
(RESULT/'records/INHERITED_NOTE_FINAL_REVIEW.md').write_text('''# Revisión final de notas heredadas\n\n## Resultado\n\nSe cerraron los 20 avisos del cotejo de notas: **cero notas heredadas perdidas, cero alteraciones semánticas no autorizadas detectadas y cero pendientes de esta revisión**. No se modificó ningún archivo de la edición. El cotejo es textual y editorial; no comprueba demostraciones ni valida las afirmaciones matemáticas de las notas.\n\nEl script `audit_editorial_notes.py --all` encontró, en los archivos que tienen un antecedente español comparable, 264 notas originales y 268 actuales: 244 conservadas salvo espacios, 19 candidatas modificadas y una supuesta ausencia. Se leyeron íntegramente los 20 avisos contra el español original y el francés correspondiente. El recuento describe esas notas codificadas mediante footnote/footnotetext; no es un censo de todas las anotaciones de cualquier clase de la edición.\n\n## Clasificación de las diferencias\n\n| Clase | Casos | Resultado |\n|---|---:|---|\n| Notas autorales francesas | 14 | Traducción fiel a la fuente y conservación de atribuciones, condiciones y referencias. Las fórmulas de cada nota coinciden con el francés, salvo espacios. |\n| Nota mixta autoral y editorial | 1 | La parte autoral de III1 CURRENT sigue el francés; la apóstilla del traductor se conserva literalmente con su marcado. |\n| Notas editoriales españolas con normalización terminológica | 5 | Texto original íntegro y fórmulas idénticas; solo se aplican vecindad, suave o suavidad, conforme al estándar de toda la edición. |\n\nLas cinco normalizaciones editoriales son: I.6.6.3 en CURRENT y DIPLOMATIC, «un entorno» → «una vecindad»; IV.17.13.4, «lisura» → «suavidad»; IV.17.13.5, «liso» → «suave»; IV.21.13.10, «al entorno» → «a la vecindad». Se registran como conservación íntegra con normalización terminológica, no como identidad byte a byte. Sus afirmaciones editoriales heredadas no se han convertido en nuevas conclusiones de esta revisión. La mención «de x» de la nota I.6.6.3 se cotejó con el francés diplomático; el francés corregido ya lee «de y».\n\nLa nota de Bourbaki en IV.11.1.2 es el **falso faltante**: está completa. La similitud textual baja se debe principalmente al restablecimiento de la notación francesa M, N, P, Q, R, A y B frente a las macros antiguas. Se cotejaron la nota completa, su secuencia de afirmaciones y todas sus fórmulas; no se verificó la demostración matemática.\n\nEn I.0.3.2.2 se distingue expresamente la antigua traducción de una nota autoral de una nota editorial española: la cláusula sobre los componentes añadida por la traducción anterior no está en el francés corregido. El texto actual traduce la condición que la fuente enuncia. En IV.8.1.3, «On notera» se traduce por «Se observará», y la relación entre espacios subyacentes y espacios analíticos sigue el francés. En IV.21.14.4 se conserva el plural autoral de «Notons aussi»: «Obsérvese también» pasa a «Observemos también», sin cambiar ninguna otra palabra ni fórmula de la nota. Los cambios de macros de nota y de marcas manuales de I.3.2.2 e IV.8.12.8 no suprimen contenido.\n\n## Las cuatro notas adicionales del recuento\n\nTambién se documentó el aumento de 264 a 268 notas en esos archivos comparables:\n\n- III1 CURRENT y DIPLOMATIC: dos traducciones de la nota autoral inicial sobre la referencia al capítulo 0 publicado con I.\n- I CURRENT, 5.3.9: una frase editorial heredada del cuerpo español se conserva literalmente como nota al restituir el cuerpo francés.\n- IV1 CURRENT, 0.15.1.8: una nota editorial del francés corregido, antes ausente, se tradujo íntegramente.\n\n## Evidencia\n\n`INHERITED_NOTE_FINAL_REVIEW.tsv` contiene los 20 casos con before/after completos, clase de nota, fuente española de origen, testigo francés, motivo, control de fórmulas, riesgo y cierre. `INHERITED_NOTE_FINAL_EVIDENCE.json` conserva los pasajes franceses exactos y la ubicación de cada nota actual. `INHERITED_NOTE_ADDITIONS_REVIEW.tsv` documenta las cuatro adiciones o reubicaciones. `INHERITED_NOTE_FINAL_COUNTS.json` contiene los recuentos. El registro bruto del script no se alteró: su supuesto missing se resuelve en esta revisión documentada.\n''')
write_tsv(RESULT/'records/CHECK_EVENTS_inherited_notes_final.tsv',['statement_id','date','who','type','outcome'],[
 ['inherited-notes-final','2026-11-25','IA','editorial_source_comparison','20 inherited-note alerts read against original Spanish and French: 14 authorial, one mixed, five editorial terminology normalizations; zero lost notes or unauthorized semantic changes detected. Four added/relocated notes explained. No proof verification; no edition-source edits.'],
 ['inherited-notes-math','2026-11-25','script','structural_comparison','Ordered math spans of 15 source-based notes match French ignoring whitespace; five Spanish editorial notes preserve inherited math. Mixed-note translator apostilla is byte-identical.']])
print(json.dumps(counts))

# Preserve the documented limitation when this differential review is rerun.
if (RESULT/'records/INHERITED_NOTE_SOURCE_CONFLICTS.tsv').exists():
 p=RESULT/'records/INHERITED_NOTE_FINAL_REVIEW.md'
 p.write_text(p.read_text()+'\n## Discordancia heredada documentada por separado\n\nUna nota conservada literalmente en IV1 CURRENT, 0.23.2.8(ii), presenta una contradicción interna y una discordancia con la referencia francesa diplomática. Se conserva intacta; los testigos y el riesgo se documentan en INHERITED_NOTE_SOURCE_CONFLICTS.tsv y su resumen Markdown. No es uno de los 20 cambios comparados ni una alteración introducida por esta ejecución.\n')
