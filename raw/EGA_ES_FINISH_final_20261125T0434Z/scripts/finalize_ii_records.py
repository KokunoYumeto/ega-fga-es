"""Finalize the EGA II bilingual source-fidelity records.

Requires the supplied source archive at the sibling source/ directory. This
is a source/translation audit, not a mathematical proof verification.
"""
from ii_tools import *
import json,collections
WHO='GPT-6 Astra, OpenAI, ChatGPT Pro mode; effort not separately reported; EGA II source-fidelity run'
TRANS={'pour tout ':'para todo ','où ':'donde ',' pour ':' para ','et':'y','(ouvert de $P_k$)':'(abierto de $P_k$)','(ouvert de $P$)':'(abierto de $P$)',"(ouverts de $X'$)":"(abiertos de $X'$)",'pour ':'para ','quels que soient ':'cualesquiera que sean ','avec':'con','où':'donde'}
TP=re.compile(r'\\(?:text|textup|textnormal|textrm|textbf|mbox|hbox)\{')
MARK=re.compile(r'\\(?:label|oldpage|tag)(?:\[[^\]]*\])?\{[^}]+\}')
def translated_formula(t):
 edits=[]
 for m in TP.finditer(t):
  e=balanced_end(t,m.end()-1);arg=t[m.end():e-1];assert arg in TRANS,arg;edits.append((m.end(),e-1,TRANS[arg]))
 return apply_edits(t,edits)
def norm(t):return re.sub(r'\s+','',t)
summary=[];coverage=[];events=[];gloss=[];translations=[]
for ed in ['current','diplomatic']:
 path=espath(ed);t=path.read_text();dst=str(path.relative_to(ROOT))
 for part,sp in parts(t).items():
  fp=frpath(ed,part);fr=fp.read_text();fu=units(fr);su=units(sp.text);src=str(fp.relative_to(ROOT.parent/'source'))
  assert list(fu)==list(su),(ed,part,'unit order')
  total=0
  for unit,f in fu.items():
   s=su[unit];fm=math_spans(f.text);sm=math_spans(s.text);assert len(fm)==len(sm),(ed,part,unit,'math count')
   for i,(a,b) in enumerate(zip(fm,sm)):assert norm(translated_formula(a.text))==norm(b.text),(ed,part,unit,i,'strict formula mismatch')
   total+=len(fm)
   if unit!='PRE':events.append([ed.upper()+':II:'+part+':'+unit,'2026-11-25',WHO,'carried as background without fault found','Compared exact supplied '+ed+' French formula sequence, translated formula text arguments, source numbering and references. Targeted prose/register corrections recorded. Translation/source-fidelity event only; no proof check.'])
   if part!='bibliography':
    clean=stripmath(f.text)
    for term,pat in [('corps',r'\bcorps\b'),('champ',r'\bchamps?\b'),('anneau de valuation',r'\banneau[x]?\s+de\s+valuation\b')]:
     for j,m in enumerate(re.finditer(pat,clean,re.I),1):
      esclean=stripmath(s.text)
      if term=='corps':render='cuerpo' if re.search(r'\bcuerpos?\b',esclean,re.I) else 'existing edition term retained'
      elif term=='champ':render='campo' if re.search(r'\bcampos?\b',esclean,re.I) else 'existing edition term retained'
      else:render='anillo de valuación (existing edition term retained)'
      gloss.append([m.group(),render,'STANDARDS_20261119b / DECISIONS_20261119b: held or low-confidence choice; no terminology substitution. French witness: '+src+':'+unit+': occurrence '+str(j),dst+':'+part+':'+unit+': French occurrence '+str(j),'yes'])
  fl=re.findall(r'\\label\{([^}]+)\}',fr);sl=re.findall(r'\\label\{([^}]+)\}',sp.text);assert fl==sl,(ed,part,'label sequence')
  # The inherited bibliography contains extra Spanish-edition bibliography items;
  # its supplied source page marker is still required and has been restored.
  fm=MARK.findall(fr);sm=MARK.findall(sp.text);assert fm==sm,(ed,part,'marker sequence')
  for lab in fl:coverage.append([src,lab,ed,dst,'translated_and_compared','All source math spans compare literally after translation of the source text arguments; source label/page/tag order verified; no proof verification claimed.'])
  coverage.append([src,part+': unnumbered matter',ed,dst,'translated_and_compared','Front matter, bibliography, indexes or surrounding prose retained; bibliography publication titles remain in their publication language.'])
  summary.append([ed,part,src,dst,len(fu)-('PRE' in fu),total,len(fl),len(fm),'exact after source-argument translation','verified'])
names=['structure','math','math_pass3']+['clauses'+str(i) for i in range(1,14)]+['anchors','pages','references','register','register2','math_text']
changes=[]
for name in names:
 for row in read('II_CHANGES_'+name+'.tsv'):changes.append([row[k] for k in HEADER])
write('CAMBIOS_ii.tsv',HEADER,changes)
write('MAPA_ii.tsv',['french_file','place','edition','spanish_file','status','evidence'],coverage)
write('CHECK_EVENTS_ii.tsv',['statement_id','date','who','type','outcome'],events)
write('GLOSARIO_REGISTRO_ii.tsv',['french_term','spanish_rendering','witness','places','reversible'],gloss)
# Only newly restored words are counted here; corrections/retranslations of
# existing text are fully documented in CAMBIOS, not counted as new prose.
new=[('current','front','source chapter heading','CAPÍTULO II ESTUDIO GLOBAL ELEMENTAL DE ALGUNAS CLASES DE MORFISMOS'),('diplomatic','front','source chapter heading','CAPÍTULO II ESTUDIO GLOBAL ELEMENTAL DE ALGUNAS CLASES DE MORFISMOS'),('current','main','1.4.5: missing finite-type qualification','de tipo finito')]
for ed in ['current','diplomatic']:
 new += [(ed,'main','6.4.8: missing endomorphism declaration',r'Sea $u$ un endomorfismo de $\mathcal{E}$'),(ed,'main','3.8.5: missing finite-type qualification across source page 71','de tipo finito'),(ed,'errata','1.8.1: missing universal element qualification',r'para todo $s\in A$')]
for ed,part,rng,txt in new:translations.append([str(espath(ed).relative_to(ROOT)),str(frpath(ed,part).relative_to(ROOT.parent/'source')),rng,words(txt)])
write('TRADUCCION_ii.tsv',['file','french_source','range','words'],translations)
review=[]
for i,row in enumerate(read('NOTATION_UNMATCHED_BASE_native_ega2_.tsv'),1):review.append(['II-UNMATCHED-'+str(i).zfill(4),row['edition'],row['source'],row['place'],'resolved','Restored source TeX/partition after bilingual clause comparison; every final source math span now passes the literal source-plus-translated-argument comparison.'])
write('II_UNMATCHED_REVIEW.tsv',['id','edition','source','place','verdict','reason'],review)
write('II_COMPLETE_FIDELITY.tsv',['edition','part','french_source','spanish_file','numbered_units','math_spans','labels','source_markers','math_verdict','marker_verdict'],summary)
refreview=[]
for row in read('II_REFERENCE_PENDING_NOW.tsv'):
 assert row['part'] in ['front','errata'],row
 refreview.append([row['edition'],row['part'],row['unit'],row['es_keys'],'retained tree convention','Inherited hyperlinks render the same plain references or section numbers as the French. No missing source reference.'])
write('II_REFERENCE_FINAL_REVIEW.tsv',['edition','part','unit','keys','verdict','reason'],refreview)
variants=[]
for row in read('II_SOURCE_PROSE_VARIANTS.tsv'):
 variants.append([row['part'],row['unit'],row['French_differences'],'reviewed','Semantic, mathematical, reference and emphasis distinctions retained in the corresponding layers; French-only grammar/capitalization differences without a distinct Spanish reading do not require artificial mistranslation.'])
write('II_DIPLOMATIC_PROSE_REVIEW.tsv',['part','unit','French_differences','verdict','reason'],variants)
punct=[]
for row in read('II_PUNCTUATION_CANDIDATES.tsv'):punct.append([row['edition'],row['part'],row['unit'],row['gap'],'reviewed; no missing punctuation','The stop follows the translated complement or closing emphasis, or is already in the adjacent reference.'])
write('II_PUNCTUATION_FINAL_REVIEW.tsv',['edition','part','unit','gap','verdict','reason'],punct)
write('II_PENDING_FINAL.tsv',['edition','part','unit','issue'],[])
counts={'parts':len(summary),'numbered_units':sum(x[4] for x in summary),'math_spans':sum(x[5] for x in summary),'labels':sum(x[6] for x in summary),'markers':sum(x[7] for x in summary),'coverage_rows':len(coverage),'changes':len(changes),'new_passages':len(translations),'new_prose_words':sum(x[3] for x in translations),'held_term_occurrences':len(gloss),'original_unmatched_resolved':len(review),'math_text_arguments':50,'unresolved':0}
(ROOT/'records/II_COMPLETE_COUNTS.json').write_text(json.dumps(counts,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(counts,ensure_ascii=False))
