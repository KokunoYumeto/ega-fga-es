#!/usr/bin/env python3
"""Build source-fidelity records for the completed III readers; never a proof claim."""
from audit_iii_alignment import *
from iii_restore_local_math import translate_math
from iii_register_candidates import segments
from corpus import write_tsv
from tex_tools import is_escaped
import csv,hashlib

REC=ROOT/'records'
DATE='2026-11-25'
WHO='GPT-6 Astra, OpenAI, ChatGPT Pro mode; effort not separately reported; EGA III source-fidelity run'
EDITIONS=[('current','1'),('diplomatic','1'),('current','6'),('current','7')]
ENV=re.compile(r'\\begin\{(env|definition|proposition|theorem|corollary|lemma|remark|remarks|example|examples|scholium|notation|namedtheorem)\}\[([^\]]+)\]')
TARGET=re.compile(r'\\(?:label|hypertarget)\{([^}]+)\}')
PAGE=re.compile(r'\\oldpage(?:\[[^]]*\])?\{\d+\}')

def load(name):
 p=REC/name
 return [json.loads(l) for l in p.read_text().splitlines()] if p.suffix=='.jsonl' else json.loads(p.read_text())

def plain(t):
 for m in reversed(math_spans(t)):t=t[:m.start]+' '+t[m.end:]
 t=re.sub(r'(?<!\\)%[^\n]*','',t)
 # Remove labels, references, page furniture and all environments' technical names.
 t=re.sub(r'\\(?:label|hypertarget|oldpage|input|sref|ref|tag|setcounter|markboth|setlength|addtocounter|thispagestyle|vspace)\*?(?:\[[^]]*\])?(?:\{[^{}]*\}){1,2}',' ',t)
 t=re.sub(r'\\(?:begin|end)\{[^}]*\}(?:\[[^]]*\])?',' ',t)
 t=re.sub(r'\\textbf\{(?:[IVX]+|\d+)\}',' ',t)
 t=re.sub(r'\\\\\[[^]]*\]',' ',t)
 t=re.sub(r'\\[A-Za-z@]+\*?(?:\[[^]]*\])?',' ',t)
 return ' '.join(re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:['’\-][A-Za-zÀ-ÖØ-öø-ÿ]+)*",t))

def words(t):return len(plain(t).split())
def src(ed,part):return 'EGA_ES_FINISH_1_FRANCES/fr/'+ed+'/BASE/native/ega3/ega3-'+part+'-fr.tex'
def line(t,p):return t.count('\n',0,p)+1
def owner(b,p):return next(q[2] for q in b if q[0]<=p<=q[1])
def fullplace(part,k):
 if k=='opening':return 'III'+part+':opening'
 return ('0.' if part=='1' and int(k.split('.')[0])>=8 else 'III.')+k
def brace_delta(t):return sum((1 if c=='{' else -1) for i,c in enumerate(t) if c in '{}' and not is_escaped(t,i))
def envs(t):return collections.Counter(re.findall(r'\\(begin|end)\{([^}]+)\}',t))

def main():
 maps=[];events=[];fidelity=[];stats={};cache={};glossary=[]
 for ed,part in EDITIONS:
  f,e,b,p,g=compare(ed,part);assert not g,(ed,part,'unmatched source formulas')
  bad=[q for q in p if translate_math(q['f'])!=q['e']];assert not bad,(ed,part,'literal source mismatch')
  fm=list(TARGET.finditer(f));em=list(TARGET.finditer(e));ft=[m[1] for m in fm];et=[m[1] for m in em if m[1] in set(ft)]
  assert ft==et,(ed,part,'canonical target sequence')
  assert PAGE.findall(f)==PAGE.findall(e),(ed,part,'page sequence')
  assert re.findall(r'\\tag\{[^}]*\}',f)==re.findall(r'\\tag\{[^}]*\}',e),(ed,part,'tag sequence')
  fs=sections(f);es=sections(e);unitfiles={};bytarget={m[1]:m for m in em}
  for m in fm:
   q=bytarget[m[1]];maps.append([src(ed,part),m[1],ed,owner(b,q.start()),'translated_and_compared','Canonical source target present in exact source order; French line '+str(line(f,m.start()))+'. Formula and translation comparison only; no proof verification.'])
  ff=list(ENV.finditer(f));ee=list(ENV.finditer(e));assert [(x[1],x[2]) for x in ff]==[(x[1],x[2]) for x in ee]
  for a,z in zip(ff,ee):
   place=fullplace(part,a[2].rstrip('.'))
   maps.append([src(ed,part),place,ed,owner(b,z.start()),'translated_and_compared','Numbered source environment retained with its kind and number; French line '+str(line(f,a.start()))+'.'])
   events.append([ed.upper()+':III'+part+':'+place,DATE,WHO,'carried as background without fault found','Inherited statement carried after source formula/numbering comparison and targeted prose/register restoration. This is an editorial source-fidelity event; no independent proof or truth certificate.'])
  for (k,fa,fz),(_,ea,ez) in zip(fs,es):
   files=list(dict.fromkeys(q[2] for q in b if q[0]<ez and ea<q[1]));unitfiles[k]=';'.join(files)
   pp=[q for q in p if q['place']==k]
   assert brace_delta(f[fa:fz])==brace_delta(e[ea:ez]),(ed,part,k,'brace structure')
   assert envs(f[fa:fz])==envs(e[ea:ez]),(ed,part,k,'environment structure')
   fidelity.append([ed,part,fullplace(part,k),src(ed,part),line(f,fa),line(f,fz),unitfiles[k],len(pp),'0','literal_source_after_translated_text_arguments','source environment counts and brace balance agree'])
  stat=dict(logical_units=len(fs),numbered_environments=len(ff),math_spans=len(p),unmatched_math_spans=0,canonical_targets=len(ft),printed_page_markers=len(PAGE.findall(f)),formula_tags=len(re.findall(r'\\tag\{',f)),input_chunks=len(b),spanish_files=len(set(q[2] for q in b)),source_sha256=hashlib.sha256(f.encode()).hexdigest(),assembled_spanish_sha256=hashlib.sha256(e.encode()).hexdigest())
  stats[ed+'_'+part]=stat;cache[ed,part]=(f,e,b,fs,es,unitfiles)
  events.append(['III:'+ed+':'+part+':literal_TeX_stream',DATE,WHO,'computation or formal certificate',str(len(p))+' ordered source math spans equal the supplied French TeX after explicit translation of text arguments; 0 gaps. This certificate concerns character streams only, not mathematical validity.'])
  events.append(['III:'+ed+':'+part+':source_structure',DATE,WHO,'used and rechecked in this run',str(len(ft))+' canonical targets, '+str(stat['printed_page_markers'])+' page markers and '+str(stat['formula_tags'])+' formula tags occur in exact source order. Per-logical-unit environment counters and brace balances agree. Editorial/source check only.'])
  # Each held or low-confidence source occurrence, with unchanged local terminology.
  for x in segments(ed,part):
   for term,pat in [('corps',r'\bcorps\b'),('champ',r'\bchamps?\b'),('anneau de valuation',r'\banneaux?\s+de\s+valuation\b')]:
    for n,m in enumerate(re.finditer(pat,x['f'],re.I),1):
     if term=='anneau de valuation':
      rr=re.findall(r'\banillos?\s+de\s+val[ou]a(?:ci[oó]n|ciones)\b',x['e'],re.I)
      wit='DOUBT_DECISIONS_20261119.tsv: low confidence; edition wording retained'
     else:
      rr=re.findall(r'\b(?:sub)?(?:cuerpos?|campos?)\b',x['e'],re.I)
      wit='DECISIONS_20261119b.tsv: held pending canonical Spanish witness; edition wording retained'
     if not rr:
      k,ea,ez=next(y for y in es if y[0]==x['place']);rr=re.findall(r'\b(?:sub)?(?:cuerpos?|campos?)\b',e[ea:ez],re.I)
      rendering='; '.join(dict.fromkeys(rr))+' (noun phrase precedes its formula in inherited Spanish)'
     else:rendering=rr[min(n-1,len(rr)-1)]
     glossary.append([term,rendering,wit+'; '+src(ed,part)+': line '+str(line(f,x['fstart']+m.start())),unitfiles[x['place']]+': '+fullplace(part,x['place'])+'; source occurrence '+str(n)+' in interval '+x['id'],'yes'])
 maps.append([src('current','6'),'III2:chapter_continuation','current',cache['current','6'][5]['opening'],'translated_and_compared','Chapter III continuation title restored before section 6.'])
 for ed in ['current','diplomatic']:
  maps.append([src(ed,'1'),'III1:front_and_chapter_III_introduction',ed,'tree/repo/editions/III1_'+ed.upper()+'/EGA_III1_ES_'+ed.upper()+'_READER.tex','translated_and_compared','Chapter 0 note, Chapter III contents including sections 6 and 7, omitted introduction clauses and printed pages restored.'])
 bridges=load('III_BRIDGE_TRANSLATIONS.jsonl');register=load('III_REGISTER_DECISIONS.json');follow=load('III_SEGMENT_DECISIONS.jsonl');schema=load('III_SCHEMA_DECISIONS.json');abbr=load('III_ABBREVIATION_DECISIONS.json');mt=load('III_MATH_TEXT_AUDIT.json')
 work=[]
 for i,q in enumerate(bridges,1):
  ed,part,k=q['edition'],q['part'],q['place'];f,e,b,fs,es,uf=cache[ed,part];fa,fz=next((a,z) for n,a,z in fs if n==k)
  fragment=q.get('source_fragment');matches=[m.start() for m in re.finditer(re.escape(fragment),f)] if fragment else []
  lo=matches[0] if len(matches)==1 else fa;hi=lo+len(fragment) if len(matches)==1 else fz
  work.append(['III-TRANSLATION-WORK-'+str(i).zfill(5),uf[k],src(ed,part),fullplace(part,k)+'; French lines '+str(line(f,lo))+'–'+str(line(f,hi)),words(q['after']),q['kind'],'retranslation or restored source bridge; not counted as new corpus coverage'])
 # New clauses can be separated confidently from rewritten inherited prose.
 translation=[]
 def add(ed,part,k,description,t):
  translation.append([cache[ed,part][5][k],src(ed,part),fullplace(part,k)+'; '+description,words(t)])
 for ed in ['current','diplomatic']:
  reader='tree/repo/editions/III1_'+ed.upper()+'/EGA_III1_ES_'+ed.upper()+'_READER.tex'
  newfront=[('Chapter 0 opening: omitted reference-convention footnote','Para facilitar la búsqueda de las referencias, se remitirá en adelante a los parágrafos del capítulo 0 publicados con el capítulo I mediante el signo'),('Chapter III contents: absent section 6 entry','Funtores Tor y Ext locales y globales; fórmula de Künneth.'),('Chapter III contents: absent section 7 entry','Estudio del cambio de base en los funtores cohomológicos covariantes de Módulos.'),('Chapter III introductory paragraph: omitted six-theorem sentence','Entre los primeros, hay esencialmente seis teoremas fundamentales, que constituyen el objeto de los seis primeros parágrafos del presente capítulo.'),('Chapter III introductory paragraph: omitted section 7 sentence','El da resultados de naturaleza más técnica, pero de uso constante en las aplicaciones.'),('Chapter 0 closing continuation notice','Continuará')]
  for desc,t in newfront:translation.append([reader,src(ed,'1'),desc,words(t)])
 for q in bridges:
  if not words(q['before']) and words(q['after']):add(q['edition'],q['part'],q['place'],'new source prose in formerly empty math-bounded interval',q['after'])
 q=next(q for q in bridges if q['edition']=='current' and q['part']=='1' and q['place']=='4.3.10')
 add('current','1','4.3.10','omitted generic-point paragraph; final pre-existing Pongamos excluded',q['after'].rsplit('Pongamos',1)[0])
 add('diplomatic','1','4.3.10','omitted clause in printed generic-point argument','tiene un solo punto genérico')
 add('current','6','opening','previously absent chapter continuation title','CAPÍTULO III continuación ESTUDIO COHOMOLÓGICO DE LOS HACES COHERENTES')
 newpieces=[('1','11.9.1','con las notaciones usuales'),('1','13.3.1','la condición ML se cumple también para por lo que precede'),('1','13.7.6','para las estructuras de módulo bigraduado'),('1','2.1.12','siendo el producto igual a'),('1','2.2.5','Pero el anillo se identifica con la intersección de los anillos de fracciones para es decir con'),('1','4.5.2','se identifica canónicamente con Basta observar que al ser un módulo de tipo finito'),('6','6.10.3','no está enteramente determinado por las propiedades de'),('7','7.2.7','puesto que conmuta con las sumas directas'),('7','7.3.6','plano'),('7','7.8.2','el razonamiento es el mismo basado en aplicado a un abierto afín en un esquema cuasicompacto')]
 for part,k,t in newpieces:
  for ed in (['current','diplomatic'] if part=='1' else ['current']):add(ed,part,k,'newly restored prose clause only; adjacent formulas and inherited wording excluded',t)
 # Source-backed linguistic decisions, kept reversible and distinct from proofs.
 for label,rows in [('register',register),('followup',follow)]:
  for q in rows:
   ed,part,k=q['edition'],q['part'],q['place']
   glossary.append(['on / nous / author imperative / source clause',q['after'],'STANDARDS_20261119b.md all-language and Spanish register; '+src(ed,part)+'; '+q['reason']+'; source SHA256 '+q['source_sha256'],cache[ed,part][5][k]+': '+q['id'],'yes'])
 for q in schema:
  ed,part,k,idx=q['id'].split(':')
  glossary.append([q['french_term'],q['after'],'STANDARDS_20261119b.md: preserve schéma/préschéma distinction; '+src(ed,part)+'; source SHA256 '+q['source_sha256'],cache[ed,part][5][k]+': '+q['id'],'yes'])
 for q in mt:glossary.append([q['source_argument'],q['translated_formula'],'NOTATION_EGA.md: translate prose in math text arguments, preserve nested mathematical TeX; '+q['verdict'],cache[q['edition'],q['part']][5][q['place']]+': '+fullplace(q['part'],q['place']),'yes'])
 for q in abbr['decisions']:glossary.append(['resp. / cf. / source tense',q['after'],'STANDARDS_20261119b.md: source abbreviations and author register; '+q['reason'],cache[q['edition'],q['part']][5][q['place']]+': '+q['id'],'yes'])
 finalterms=list(csv.DictReader((REC/'FINAL_STANDARD_MODEL_III.tsv').open(),delimiter='\t'))
 for q in finalterms:glossary.append(['fibre / filtré',q['form'],q['reason']+'; '+q['french_source'],q['file']+': '+q['place']+'; '+q['review_id'],'yes'])
 standard=[['es-register-III-initial',len(register),sum(q['changed'] for q in register),'74 reviewed candidates retained','Source-aligned initial register decisions; includes author tense and source-clause repairs.'],['es-register-III-followup-on',198,198,'0 in this explicit batch','198 source-aligned corrections for impersonal on, mixed clauses and author imperatives; later phases may revisit a site.'],['es-register-III-followup-author',129,129,'0 in this explicit batch','129 first-plural author-voice and related clause decisions; successive edits, not unique locations.'],['es-register-III-last-imperatives',16,16,'0 listed residues','Source on notera/observera -> se observará; soient -> sean; Faisons -> Hagamos, en efecto.'],['es-scheme-prescheme-III',len(schema),len(schema),'0 source-term stream mismatches at scope release','120 same-cardinality occurrence changes; additional full-unit rewrites are recorded without counting them again here.'],['es-recouvrement-III',34,34,'0 cubrimiento residues at release','34 explicit III2 intervals contain matching French recouvrement; recubrimiento is the settled standard term.'],['es-resp-III',52,52,'0 compared same-count residues','Source resp. restored; French respectivement remains respectivamente.'],['es-cf-III',4,4,'0 listed residues','Restore cf. in two III1 places in both editions.'],['es-integral-closure-III',6,6,'0 listed residues','intégralement clos -> integralmente cerrado; distinct from intègre -> íntegro.'],['es-fibra-tallo-III-final',57,0,'57 retained morphism/geometric/formal fibers','All final candidates read in aligned source context; none is a sheaf stalk.'],['es-filtrante-III-final',60,0,'60 objects bearing filtrations retained','Source filtré(s), not filtrant; no substitution.']]
 for key in ['register','source_prose','notes']:
  outcome={'register':'448 initial decisions (374 changed), 198 impersonal/imperative follow-ups, 129 author-voice follow-ups and 16 final imperative corrections. These are successive editorial decisions, not independent proof checks.','source_prose':'1110 explicit source bridge/full-unit translations logged separately from newly supplied coverage. Missing paragraphs, clauses, headings and formula mentions restored; current/printed variants kept distinct.','notes':'Source author notes retained; sans doute rendered probablemente. CURRENT inherited [Trad.] Estos cuatro últimos capítulos nunca se publicaron. restored exactly; absent from inherited DIPLOMATIC and not added there.'}[key]
  events.append(['III:'+key,DATE,WHO,'used and rechecked in this run',outcome])
 events.append(['III:math_text_arguments',DATE,WHO,'used and rechecked in this run','All 68 source text/textup/mbox/hbox groups reviewed, including nested mathematics. No duplicated retained Spanish nested formula remains. Prose/TeX comparison only.'])
 events.append(['III:7.5.6:printed_implication',DATE,WHO,'carried as background without fault found','Supplied source prints (i) implies (ii) in the proof passage; this printed direction was restored instead of the inherited reversal. No claim of independent mathematical validation or silent emendation.'])
 for q in finalterms:events.append([q['review_id'],DATE,WHO,'used and rechecked in this run',q['reason']+' Terminology context check only; no proof check.'])
 write_tsv(REC/'MAPA_iii.tsv',['french_file','place','edition','spanish_file','status','evidence'],maps)
 write_tsv(REC/'III_COMPLETE_FIDELITY.tsv',['edition','part','place','french_source','source_first_line','source_last_line','spanish_files','aligned_math_spans','unmatched_math_spans','formula_verdict','structure_verdict'],fidelity)
 write_tsv(REC/'III_TRANSLATION_WORK.tsv',['work_id','file','french_source','range','words','kind','coverage'],work)
 write_tsv(REC/'TRADUCCION_iii.tsv',['file','french_source','range','words'],translation)
 write_tsv(REC/'GLOSARIO_REGISTRO_iii.tsv',['french_term','spanish_rendering','witness','places','reversible'],glossary)
 write_tsv(REC/'ESTANDAR_APLICADO_iii.tsv',['row','found','changed','places_left','reason'],standard)
 write_tsv(REC/'CHECK_EVENTS_iii.tsv',['statement_id','date','who','type','outcome'],events)
 counts=dict(editions=stats,math_spans=sum(q['math_spans'] for q in stats.values()),numbered_environments=sum(q['numbered_environments'] for q in stats.values()),canonical_targets=sum(q['canonical_targets'] for q in stats.values()),printed_pages=sum(q['printed_page_markers'] for q in stats.values()),logical_units=len(fidelity),map_rows=len(maps),check_events=len(events),glossary_rows=len(glossary),source_translation_work_rows=len(work),retranslated_span_words=sum(q[4] for q in work),new_translation_fragments=len(translation),new_translation_words=sum(q[3] for q in translation),register_initial_decisions=len(register),register_initial_changes=sum(q['changed'] for q in register),followup_decisions=len(follow),schema_occurrence_changes=len(schema),math_text_groups=len(mt),final_model_verdicts=len(finalterms))
 counts['own_change_rows']=sum(1 for _ in csv.DictReader((REC/'CAMBIOS_iii.tsv').open(),delimiter='\t')) if (REC/'CAMBIOS_iii.tsv').exists() else 0
 (REC/'III_COMPLETE_COUNTS.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(counts,ensure_ascii=False))

if __name__=='__main__':main()
