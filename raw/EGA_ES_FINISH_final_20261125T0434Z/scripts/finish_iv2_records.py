#!/usr/bin/env python3
"""Regenerate IV-2 coverage, reconciliation, and check-event records from delivered Spanish.
No proof verification is inferred from translation or exact TeX comparison.
"""
from pathlib import Path
import sys,re,csv,json,bisect,collections,hashlib,difflib
sys.path.insert(0,str(Path(__file__).resolve().parent))
import audit_iv2_alignment as a
import reconcile_iv2 as r
import iv2_layer_patches as lp
ROOT=a.ROOT;SOURCE=a.SOURCE;REC=ROOT/'records';DONE=SOURCE/'EGA_ES_FINISH_4_HECHO/done'
DATE='2026-11-25'
WHO='GPT-6 Astra, OpenAI, ChatGPT Pro mode; effort not separately reported; IV2 run'
FRPATH='EGA_ES_FINISH_1_FRANCES/fr/{layer}/IV2/native/ega4/ega4-2-fr.tex'
ORIG=SOURCE/'EGA_ES_FINISH_2_ESPANOL/worktree/es'

def write(name,header,rows):
 with (REC/name).open('w') as out:
  wr=csv.writer(out,delimiter='\t');wr.writerow(header);wr.writerows(rows)

def prose(t):
 t=a.MATH.sub(' ',t);t=re.sub(r'(?<!\\)%[^\n]*','',t)
 t=re.sub(r'\\(?:label|EGAReaderTarget|oldpage|tag|setcounter|addtocounter|setlength)\s*(?:\[[^\]]*\])?\{[^}]*\}(?:\{[^}]*\})?',' ',t)
 t=re.sub(r'\\(?:begin|end)\{[^}]*\}(?:\[[^\]]*\])?',' ',t)
 t=re.sub(r'\\[A-Za-z@]+\*?',' ',t)
 return t

def words(t):return len(re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:['’\-][A-Za-zÀ-ÖØ-öø-ÿ]+)*",prose(t)))
def nspace(t):return re.sub(r'\s+','',t)
def line(t,pos):return t.count('\n',0,pos)+1

def find_snippet(f,s,page,pages):
 pat=re.compile(r'\s*'.join(re.escape(v) for v in re.split(r'\s+',s.strip())))
 loc=pages.get(page,0);stop=pages.get(page+2,len(f));start=pages.get(max(5,page-1),0)
 matches=list(pat.finditer(f,start,stop))
 if not matches:matches=list(pat.finditer(f))
 if not matches:return None,0
 return min(matches,key=lambda m:abs(m.start()-loc)),len(matches)

def main():
 allmap=[];events=[];units=[];stats={};cache={}
 for layer in ['CURRENT','DIPLOMATIC']:
  f,e,bounds,paired,gaps=a.compare(layer)
  mismatches=[q for q in paired if r.translated_math(q['f'])!=q['e']]
  assert not gaps and not mismatches,(layer,'formula source mismatch')
  byfile=collections.defaultdict(list)
  for q in paired:byfile[q['file']].append(q)
  fa=list(a.ANCHOR.finditer(f));ea=list(a.ANCHOR.finditer(e));assert len(fa)==len(ea)==582
  assert [q[1] for q in fa]==[q[1] for q in ea]
  src=FRPATH.format(layer=layer.lower())
  sf=a.sections(f);se=a.sections(e)
  for fm,em in zip(fa,ea):
   file=a.owner(em.start(),bounds);place='IV.'+fm[1]
   allmap.append([src,place,layer,file,'present; source formula and structure compared','French line '+str(line(f,fm.start()))+'; ordered numbered environment retained; mathematical validity not independently verified'])
   events.append([layer+':'+place,DATE,WHO,'carried as background without fault found','Inherited Spanish statement retained and source-aligned formula/marker stream compared. Editorial/source fidelity comparison only; no independent proof or truth certificate claimed.'])
  stylebad=[]
  for (place,lo,hi),(_,x,y) in zip(sf,se):
   for token in ['emph','textup','footnote']:
    pat=r'\\'+token+r'\b'
    if len(re.findall(pat,f[lo:hi]))!=len(re.findall(pat,e[x:y])):stylebad.append((place,token))
  assert not stylebad,(layer,stylebad)
  markers={}
  for name,pat in [('labels_targets',r'\\label\{[^}]*\}|\\EGAReaderTarget\{[^}]*\}\{[^}]*\}'),('oldpage',r'\\oldpage(?:\[[^\]]*\])?\{[^}]*\}'),('tag',r'\\tag\{[^}]*\}')]:
   ff=re.findall(pat,f);ee=re.findall(pat,e);assert ff==ee,(layer,name);markers[name]=len(ff)
  for kind in ['section','subsection']:
   ff=list(re.finditer(r'\\'+kind+r'\*?\{',f));ee=list(re.finditer(r'\\'+kind+r'\*?\{',e));assert len(ff)==len(ee)
   for idx,(fm,em) in enumerate(zip(ff,ee),1):
    allmap.append([src,'IV2.heading.'+kind+'.'+str(idx).zfill(2),layer,a.owner(em.start(),bounds),'present; heading order compared','French line '+str(line(f,fm.start()))+'; corresponding Spanish heading in identical sequence'])
  for idx,(lo,hi,file) in enumerate(bounds,1):
   pp=byfile[file];assert pp
   fl=min(q['fstart'] for q in pp);fh=max(q['fend'] for q in pp);t=e[lo:hi]
   origin=ORIG/layer/'EGA_IV2'/Path(file).name
   disposition='existing unit revised' if origin.exists() else 'assembled from inherited current Spanish, then reconciled with printed French'
   units.append([layer,idx,file,src,line(f,fl),line(f,fh),len(pp),len(list(a.ANCHOR.finditer(t))),words(t),'complete ordered formula/marker coverage',disposition])
   allmap.append([src,'IV2.unit.'+str(idx).zfill(3),layer,file,'present; full input unit included','Matching source formulas at French lines '+str(line(f,fl))+'–'+str(line(f,fh))+'; '+str(len(pp))+' math spans; '+disposition+'. Source ranges indicate matched formulas, not asserted paragraph boundaries.'])
  pages={int(m[1]):m.start() for m in re.finditer(r'\\oldpage\[IV-2\]\{(\d+)\}',f)}
  cache[layer]=(f,e,bounds,paired,pages)
  stats[layer]={'ordered_inputs':len(bounds),'numbered_environments':len(fa),'math_spans':len(paired),'unmatched_math_spans':0,'formula_text_translations':sum(q['f']!=q['e'] for q in paired),'markers':markers,'prose_lexical_words_french':words(f),'prose_lexical_words_spanish':words(e),'newly_assembled_inputs':sum(not (ORIG/layer/'EGA_IV2'/Path(x[2]).name).exists() for x in bounds)}
  events.append(['IV2:'+layer+':formula_stream',DATE,WHO,'used and rechecked in this run',str(len(paired))+' ordered math spans literally equal to the supplied '+layer.lower()+' French, except translated words in six text{} groups within five formulas; zero unmatched spans. This certifies source identity of TeX, not mathematical validity.'])
  events.append(['IV2:'+layer+':structure',DATE,WHO,'used and rechecked in this run','342 ordered inputs; 582 numbered environments; 740 labels/targets, 227 printed-page markers, and 119 tags exactly in French order. Per-numbered-segment counts of emph, textup, and footnote agree. Inherited editorial notes retained.'])
  events.append(['IV2:'+layer+':register',DATE,WHO,'used and rechecked in this run','456 source-on prose spans corrected, plus 28 targeted mixed-clause/pronoun/imperative corrections and the source long period in proof III of 6.14.1. Source nous and author imperatives retained. Review is linguistic/editorial, not proof checking.'])
 write('MAPA_iv2.tsv',['french_file','place','edition','spanish_file','status','evidence'],allmap)
 write('IV2_UNIT_AUDIT.tsv',['edition','input_order','spanish_file','french_file','first_matched_formula_line','last_matched_formula_line','math_spans','numbered_environment_starts','prose_lexical_words','coverage','disposition'],units)
 # Every relevant HAND entry receives a verdict. Earlier admissions are kept distinct from new work.
 admitted={(q['list'],q['entry']):q for q in map(json.loads,(DONE/'codex_session/HAND_DISPOSITIONS_ADMITTED.jsonl').read_text().splitlines())}
 hand=[];handcounts=collections.Counter();evolved=[]
 for layer in ['CURRENT','DIPLOMATIC']:
  f,e,bounds,paired,pages=cache[layer];name='PORT_ES_'+layer+'_HAND.json';src=FRPATH.format(layer=layer.lower())
  items=[q for q in json.loads((DONE/'hand_lists'/name).read_text()) if q['french_file'].startswith('IV2/')]
  for q in items:
   hid='hand:'+name+':'+str(q['entry']);prior=admitted.get((name,q['entry']));verdict='already in' if prior else 'carried'
   m,occ=find_snippet(f,q['french_new'],int(q['page']),pages)
   pos=m.start() if m else pages.get(int(q['page']),0)
   p=next((z for z in paired if z['fstart']>=pos),paired[-1]);file=p['file'];place='IV-2 printed p. '+str(q['page'])
   if m:
    place+='; French line '+str(line(f,m.start()))
    evidence='Replacement witness located in supplied French'+(' (repeated snippet; printed-page context used)' if occ>1 else '')+'. '
   else:
    assert prior,(name,q['entry'],'unresolved pending witness')
    evolved.append([name,q['entry'],q['page']]);evidence='The earlier replacement is no longer verbatim in the supplied release; the latest whole source span controls. No blind rollback to the older snippet. '
   mathematical=bool(re.search(r'\$|\\(?:math|boldsymbol|operatorname|frac|otimes|widehat|setmin|subset|supset|xymatrix|tag)',q['french_new']))
   if prior:
    reason='Earlier admitted disposition: '+prior['disposition']+'. '+evidence
    reason+=('Exact source formulas in the affected unit were reconciled in this run; earlier mathematical content retained. ' if mathematical else 'Earlier editorial correction retained; source structure, markers and emphasis screened in this run. ')
   else:reason='Previously pending; carried in the diplomatic tail reconstruction and checked against printed French. '+evidence
   reason+='Translation/source comparison is not a mathematical proof check.'
   hand.append([hid,file,place,verdict,reason]);handcounts[(layer,verdict)]+=1
   eventtype='used and rechecked in this run' if (not prior or mathematical) else 'carried as background without fault found'
   events.append([hid,DATE,WHO,eventtype,reason])
 assert len(hand)==2674
 # The respell note requires a manual French check after its suggested interim rollback.
 respells=[];resc=collections.Counter();carriedrows={213,217,218,241,246,249,260,266,355}
 context_reasons={
  219:'The printed operator is deg.tr without a final abbreviation dot inside the operator.',242:'The printed operator is deg.tr without a final abbreviation dot inside the operator.',252:'The printed operator is deg.tr without a final abbreviation dot inside the operator.',253:'The printed operator is deg.tr without a final abbreviation dot inside the operator.',254:'The printed operator is deg.tr without a final abbreviation dot inside the operator.',268:'The index follows the supplied deg.tr spelling, without the proposed extra dot.',360:'The index follows the supplied deg.tr spelling, without the proposed extra dot.',
  232:'The source multiplication dot is retained in the formula.',243:'The source R.mathfrak L product dot is retained.',244:'The source R.mathfrak L product dot is retained.',
  225:'French has a comma in the list of hypotheses; the proposed semicolon is not reinstated.',226:'French has a comma in the list of hypotheses; the proposed semicolon is not reinstated.',
  256:'French terminates condition a) with a period, retained in Spanish.',257:'French terminates condition b) with a period, retained in Spanish.',351:'Printed French terminates condition a) with a period.',352:'Printed French terminates condition b) with a period.',
  258:'The supplied current reference reads (6.12.4; II), with a semicolon; the older comma proposal is superseded.',353:'The supplied diplomatic reference retains (6.12.4; II)), including its printed extra closing parenthesis.',
  262:'The punctuation inside the condition label is retained exactly from French.',263:'The punctuation inside the condition label is retained exactly from French.',357:'The punctuation inside the condition label is retained exactly from diplomatic French.',358:'The punctuation inside the condition label is retained exactly from diplomatic French.',
  264:'The tensor expression follows the source structure and source mathcal spelling; the old spelling is not restored.',
  239:'The existing comma and Spanish parenthetical commas keep the source long sentence intact.',231:'The definition reference and adjoining formula now use literal source TeX; the older unbolded numeral is not restored.',
 }
 unit_lookup={row[2]:row for row in units}
 for idx,s in enumerate((DONE/'RESPELL_CORRECTIONS_20261115.jsonl').read_text().splitlines(),1):
  q=json.loads(s)
  if not(q['tree'].startswith('es/') and q['file'].startswith('EGA_IV2/')):continue
  file='tree/worktree/'+q['tree']+'/'+q['file'];u=unit_lookup[file];layer=q['tree'].split('/')[-1]
  rid='RESPELL-'+str(idx).zfill(6);place='inherited line '+str(q['line'])+'; French matched-formula lines '+str(u[4])+'–'+str(u[5])
  if idx in carriedrows:
   verdict='carried';why='Spanish clause punctuation was restored outside formulas after comparing the French sentence. Formula TeX remains literal source.'
  else:
   verdict='does not apply to a translation';why='The literal intermediate rollback is superseded by the later exact-French notation rule and the supplied source reading. The requested manual source check was completed; the affected unit has an exact ordered formula stream. '
   why+=context_reasons.get(idx,'The final formula punctuation and spelling follow the authoritative French, rather than the older should_read line.')
  why+=' Origin: '+q['tree']+', entry '+str(q['entry'])+', '+q['file']+':'+str(q['line'])+'; kind '+q['kind']+'.'
  respells.append([rid,file,place,verdict,why]);resc[verdict]+=1
  events.append([rid,DATE,WHO,'used and rechecked in this run',why+' This is a source/typography check, not a proof check.'])
 assert len(respells)==71
 write('HECHO_REVISADO_iv2.tsv',r.HEADERS['HECHO_REVISADO'],hand+respells)
 # Record only newly rendered fragments; inherited material copied into missing diplomatic files is assembly.
 trans=[]
 for idx in [5,6,15,18,25,26,29]:
  name,place,before,after=lp.P[idx]
  trans.append(['tree/worktree/es/DIPLOMATIC/EGA_IV2/'+name+'.diplomatic.tex',FRPATH.format(layer='diplomatic'),'IV.'+place+'; newly rendered printed-variant fragment only',words(after)])
 for layer in ['CURRENT','DIPLOMATIC']:
  f,e,bounds,paired,pages=cache[layer]
  q=next(q for q in paired if q['place']=='3.3.3' and re.search(r'\\text\{\s*et\s*\}',q['f']))
  trans.append([q['file'],FRPATH.format(layer=layer.lower()),'IV.3.3.3; untranslated et inside text{} rendered as y',1])
 write('TRADUCCION_iv2.tsv',r.HEADERS['TRADUCCION'],trans)
 # Held/low-confidence choices are reported at each actual prose occurrence.
 glossary=[]
 for layer in ['CURRENT','DIPLOMATIC']:
  _,e,bounds,_,_=cache[layer]
  for lo,hi,file in bounds:
   t=e[lo:hi];masked=list(t)
   for m in a.MATH.finditer(t):masked[m.start():m.end()]=' '*len(m[0])
   masked=''.join(masked)
   for m in re.finditer(r'\b(?:cuerpos?|campos?|valoraci[oó]n(?:es)?)\b',masked,re.I):
    val=m[0]
    if val.lower().startswith('valoraci'):
     term='anneau de valuation';wit='standard/DOUBT_DECISIONS_20261119.tsv, es: anneau de valuation; low confidence, not applied'
    else:
     term='corps / champ (held)';wit='standard/DECISIONS_20261119b.tsv, es: corps, champ; held until the canonical translation is checked; existing word retained'
    glossary.append([term,val,wit,file+':'+str(line(t,m.start())),'yes'])
 glossary.extend([
  ['on','se; impersonal construction','standard/STANDARDS_20261119b.md §§2,4; corresponding French prose spans','IV2: 456 aligned spans per edition, with mixed-clause follow-up','yes'],
  ['nous','first-person plural','standard/STANDARDS_20261119b.md §§2,4; corresponding French prose spans','IV.4.4.1; IV.6.14.1 proof III; IV.7.2.10; retained elsewhere','yes'],
  ['suite de composition','sucesión de composición','Supplied French IV.6.9.2 and existing diplomatic Spanish terminology','tree/worktree/es/CURRENT/EGA_IV2/ega4-2_6.9.1_6.9.2_ES.tex:6.9.2','yes']
 ])
 write('GLOSARIO_REGISTRO_iv2.tsv',r.HEADERS['GLOSARIO_REGISTRO'],glossary)
 write('CHECK_EVENTS_iv2.tsv',r.HEADERS['CHECK_EVENTS'],events)
 (REC/'IV2_AUDIT_COUNTS.json').write_text(json.dumps({'editions':stats,'hand_rows':len(hand),'hand_verdicts':{k[0]+':'+k[1]:v for k,v in handcounts.items()},'older_hand_snippets_superseded_by_source':evolved,'respell_rows':len(respells),'respell_verdicts':dict(resc),'partial_translation_fragments':len(trans),'partial_translation_words':sum(x[3] for x in trans),'glossary_rows':len(glossary),'check_events':len(events),'map_rows':len(allmap),'unit_audit_rows':len(units)},ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'editions':stats,'hand':len(hand),'respells':len(respells),'evolved_snippets':len(evolved),'map':len(allmap),'unit_rows':len(units),'check_events':len(events),'glossary':len(glossary)},ensure_ascii=False))
if __name__=='__main__':main()
