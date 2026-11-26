"""Consolidate section-8-only evidence; no mathematical proof check claimed."""
from iv38_tools import *
from collections import Counter
WHO='GPT-6 Astra, OpenAI, ChatGPT Pro mode; effort not separately reported; IV3 section-8 source-fidelity run'
ft=FP.read_text();st=SP.read_text();fu=units(ft);su=units(st)
assert list(fu)==list(su),'numbered unit order'
def norm(t):return re.sub(r'\s+','',t)
def translated_formula(t):return t.replace(r'\text{pour }',r'\text{para }').replace(r'\hbox{et}',r'\hbox{y}')
def stripmath(t):
 for m in reversed(math_spans(t)):t=t[:m.start]+' '+t[m.end:]
 return t
def words(t):return len(re.findall(r'[A-Za-zÀ-ÿ]+(?:[-’\x27][A-Za-zÀ-ÿ]+)*',re.sub(r'\\[A-Za-z]+',' ',stripmath(t))))
def refnums(z):
 for m in reversed(core_spans(z)):z=z[:m.start]+' '*(m.end-m.start)+z[m.end:]
 for pat in [r'\\label\{[^}]*\}',r'\\EGAReaderTarget\{[^}]*\}\{[^}]*\}',r'\\(?:begin|end)\{[^}]*\}(?:\[[^]]*\])?',r'\\oldpage(?:\[[^]]*\])?\{[^}]*\}',r'\\tag\{[^}]*\}']:
  z=re.sub(pat,lambda m:' '*len(m[0]),z)
 return list(re.finditer(r'(?<![0-9])\d+(?:\.\d+){1,4}(?![0-9])',z))
dst=str(SP.relative_to(ROOT));summary=[];events=[];gloss=[];volumes=[]
for un,f in fu.items():
 s=su[un];fm=math_spans(f.text);sm=math_spans(s.text);assert len(fm)==len(sm),(un,'math counts')
 for i,(a,b) in enumerate(zip(fm,sm)):assert norm(translated_formula(a.text))==norm(b.text),(un,i,'literal formula')
 summary.append([un,len(fm),len(core_spans(f.text)),'exact after source text-argument translation'])
 if un!='front':events.append(['CURRENT:IV3:'+un,'2026-11-25',WHO,'carried as background without fault found','Compared all supplied French mathematical spans and markers; corrected missing clauses, references, register and text arguments with source-bounded journals. Translation/source-fidelity event only; no mathematical proof verification claimed.'])
 ff=refnums(f.text);ss=refnums(s.text);assert [m[0] for m in ff]==[m[0].removeprefix('0.') for m in ss],(un,'reference numbers')
 for a,b in zip(ff,ss):
  mm=re.search(r'\\(?:sref|eqref|eref|ref)(?:\[[^]]*\])?\{([^.{}]+)\.$',s.text[max(0,b.start()-85):b.start()])
  if not mm:continue
  sc=mm[1];left=f.text[max(0,a.start()-220):a.start()];left=left[left.rfind('('):]
  hits=list(re.finditer(r'\\(?:textbf|mathbf)\s*\{?([IV]{1,3}|0)\}?',left));fc=hits[-1][1] if hits else 'T' if re.match(r'\(T\s*,',left) else 'IV'
  assert sc==fc,(un,a[0],fc,sc)
  volumes.append([un,a[0],fc,sc,'source chapter and reference number verified'])
 for term,pat in [('corps',r'\bcorps\b'),('champ',r'\bchamps?\b'),('anneau de valuation',r'\banneau[x]?\s+de\s+valuation\b')]:
  for j,m in enumerate(re.finditer(pat,stripmath(f.text),re.I),1):
   render={'corps':'cuerpo','champ':'campo','anneau de valuation':'anillo de valuación'}[term]
   gloss.append([m[0],render,'STANDARDS_20261119b / DECISIONS_20261119b: held or low-confidence choice retained. French witness: '+SOURCE+': '+un+': occurrence '+str(j),dst+': '+un+': occurrence '+str(j),'yes'])

MARK=re.compile(r'\\label\{[^}]*\}|\\EGAReaderTarget\{[^}]*\}\{[^}]*\}|\\oldpage(?:\[[^]]*\])?\{[^}]*\}|\\tag\{[^}]*\}')
assert MARK.findall(ft)==MARK.findall(st),'source marker order'
pagepat=re.compile(r'\\oldpage\[([^]]*)\]\{([^}]+)\}')
def page_positions(us):
 return {m[0]:(un,sum(z.end<=m.start() for z in core_spans(u.text))) for un,u in us.items() for m in pagepat.finditer(u.text)}
assert page_positions(fu)==page_positions(su),'page positions at corresponding mathematical boundary'
assert len(re.findall(r'\\footnote\{',ft))==len(re.findall(r'\\footnote\{',st))==2
assert not re.search(r'\bse puede (?:reducirnos|restringirnos|limitarnos)\b',st)
assert not re.search(r'constructib',stripmath(st),re.I)
labels=re.findall(r'\\label\{([^}]+)\}',ft);readers=re.findall(r'\\EGAReaderTarget\{[^}]+\}\{([^}]+)\}',ft)
coverage=[[SOURCE,k,'current',dst,'translated_and_compared','Exact supplied French math after translation of its text arguments; label/page/tag/reader-target order verified; source-fidelity comparison only.'] for k in labels+readers]
coverage.append([SOURCE,'front and surrounding unnumbered prose','current',dst,'translated_and_compared','Source chapter heading, all 50 original-page markers and both source footnotes present; bibliography titles retain their publication language.'])
initial=ROOT/'records/IV38_INITIAL_MAP.tsv'
if not initial.exists():initial.write_text((ROOT/'records/MAPA_iv3_8.tsv').read_text())
names=['register','math','clauses1','clauses2','clauses3','math_p2','structure','anchors','math_text','clauses4','clauses5','clauses6','periods','periods_context','surface','terminology']
changes=[]
for name in names:
 changes.extend([[r[k] for k in HEADER] for r in read('IV38_CHANGES_'+name+'.tsv')])
write('CAMBIOS_iv3_8.tsv',HEADER,changes)
write('MAPA_iv3_8.tsv',['french_file','place','edition','spanish_file','status','evidence'],coverage)
write('CHECK_EVENTS_iv3_8.tsv',['statement_id','date','who','type','outcome'],events)
for r in read('IV38_TERMINOLOGY_DRY_RUN.tsv'):
 gloss.append(['constructible / related forms','construible / related forms','TERMINOLOGY_DECISIONS.tsv EGAIV3-ES-TERM-0004; Zalamea, Grothendieck: Una guía a la obra matemática, PDF p. 18; supplied source '+SOURCE+': '+r['place'],dst+': '+r['place']+': offset '+r['offset'],'yes'])
write('GLOSARIO_REGISTRO_iv3_8.tsv',['french_term','spanish_rendering','witness','places','reversible'],gloss)
# Count only restored prose, not corrections of wording or formula-only restorations.
new=[
 ('8.2.7: arbitrary ringed space and ordered index set','arbitrario arbitrario'),
 ('8.5.6: explicit later exact sequence','la sucesión'),
 ('8.5.8: omitted surjectivity clause',r'el homomorfismo $\mathcal F\to\operatorname{Ker}g$ es sobreyectivo y'),
 ('8.6.1: presentation base',r'sobre $Y$'),
 ('8.6.2: definition of the order on the direct limit',r'se define una relación de orden en el conjunto $\varinjlim\mathfrak{Spr}(S_\lambda)$'),
 ('8.6.3.1: finite-presentation base',r'sobre $S_\lambda$'),
 ('8.8.1: explicit canonical maps',r'respectivamente iguales a $1_{X_\alpha}\times u_\lambda$ y $1_{Y_\alpha}\times u_\lambda$'),
 ('8.10.5: alternative kinds of subschemes','resp. inducido en un abierto, resp. cerrado'),
 ('8.10.5: properties concerning only fibers','que solo conciernen a las fibras'),
 ('8.10.5: finite-presentation qualification',r'de presentación finita sobre $S_\mu$'),
 ('8.12.1: quasi-compact and quasi-separated intermediate morphism',r'$g$ es un morfismo cuasicompacto y cuasiseparado'),
 ('8.12.1: explicit immersion hypothesis',r'de que $g$ es una inmersión'),
 ('8.12.3: missing filtered family of subalgebras',r'Sea $(\mathcal C_\lambda)$ la familia filtrante creciente de las sub-$\mathcal O_Y$-álgebras cuasicoherentes de tipo finito de $\mathcal C$ (cuya unión es $\mathcal C$)'),
 ('8.12.3: identification of the intermediate spectrum',r'de modo que $Y\prime$ se identifica con $\operatorname{Spec}(\mathcal B\prime)$'),
 ('8.12.6: regular implies normal clause',r'y \emph{a fortiori}, normal'),
 ('8.13.4: category of the essentially affine pro-objects',r'de $\boldsymbol{C}\prime_0$'),
 ('8.14.2.2: ring of the finitely generated ideals',r'de $C$'),
]
translations=[[dst,SOURCE,place,words(txt)] for place,txt in new]
write('TRADUCCION_iv3_8.tsv',['file','french_source','range','words'],translations)
write('IV38_COMPLETE_FIDELITY.tsv',['place','all_math_spans','core_math_spans','verdict'],summary)
write('IV38_REFERENCE_FINAL_REVIEW.tsv',['place','number','french_chapter','spanish_chapter','verdict'],volumes)
initialblocks=json.loads((ROOT/'records/IV38_INITIAL_BLOCKS.json').read_text())
write('IV38_UNMATCHED_REVIEW.tsv',['id','place','verdict','reason'],[['IV38-UNMATCHED-'+str(i+1).zfill(3),r['place'],'resolved','Bilingual clause comparison followed by literal equality of every final source formula, including reference math and translated source text arguments.'] for i,r in enumerate(initialblocks)])
register=[]
for r in read('IV38_REGISTER_CANDIDATES.tsv'):register.append([r['place'],r['gap'],'reviewed','French authors’ nous and imperative retained; source-on changes and clitic repairs logged separately; noun suffixes and shifts across adjacent math gaps excluded.'])
write('IV38_REGISTER_FINAL_REVIEW.tsv',['place','gap','verdict','reason'],register)
write('IV38_PUNCTUATION_FINAL_REVIEW.tsv',['place','gap','verdict','reason'],[[r['place'],r['gap'],'reviewed; stop present','Spanish complement follows the formula before the sentence stop; no missing punctuation.'] for r in read('IV38_PUNCTUATION_CANDIDATES.tsv')])
write('IV38_PENDING_FINAL.tsv',['place','issue'],[])
counts={'numbered_units':len(events),'all_math_spans':sum(x[1] for x in summary),'core_math_spans':sum(x[2] for x in summary),'source_labels':len(labels),'reader_targets':len(readers),'source_markers':len(MARK.findall(ft)),'pages':len(page_positions(fu)),'source_footnotes':2,'math_text_arguments':len(read('IV38_MATH_TEXT_VERIFIED.tsv')),'initial_blocks_resolved':len(initialblocks),'coverage_rows':len(coverage),'changes':len(changes),'new_passages':len(translations),'new_prose_words':sum(x[3] for x in translations),'glossary_rows':len(gloss),'terminology_changed':len(read('IV38_TERMINOLOGY_DRY_RUN.tsv')),'verified_reference_volumes':len(volumes),'unresolved':0}
(ROOT/'records/IV38_COMPLETE_COUNTS.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
(ROOT/'records/IV38_AUDIT.md').write_text('''# EGA IV, tercera parte, §8: cotejo de fuente

Se cotejó el archivo francés corregido con su traducción española. El cotejo es editorial y traductológico: no constituye una comprobación de las demostraciones matemáticas.

La secuencia completa de fórmulas coincide literalmente con el francés, salvo la traducción de los argumentos de texto del propio francés y el espacio en blanco de TeX. Se verificaron también las etiquetas, los destinos EGAReaderTarget, las páginas originales, las etiquetas de ecuaciones y los dos pies de página de la fuente.

Las correcciones restauran cláusulas y condiciones omitidas, el ámbito de tres enunciados, referencias con capítulo equivocado, el registro impersonal de «on», la primera persona de «nous» y de los imperativos originales, y las frases largas de la fuente. Los argumentos text/textup/hbox se leyeron expresamente; no se copiaron a ciegas argumentos españoles que pudieran duplicar matemática adyacente. Se aplicó la grafía «construible» conforme al testigo EGAIV3-ES-TERM-0004; las decisiones terminológicas held y de baja confianza permanecen registradas sin imponer una sustitución.

Los registros consolidados que deben fusionarse son MAPA_iv3_8.tsv, CAMBIOS_iv3_8.tsv, TRADUCCION_iv3_8.tsv, GLOSARIO_REGISTRO_iv3_8.tsv y CHECK_EVENTS_iv3_8.tsv. Los archivos IV38_CHANGES_*.tsv son componentes históricos del mismo registro y no se deben contar otra vez. Los cambios anteriores de otros agentes no se han sobrescrito.

Los informes históricos de patrones no encontrados documentan variantes de búsqueda; la verificación final literal y el archivo IV38_PENDING_FINAL.tsv determinan el estado actual. El script finalize_iv38_records.py verifica nuevamente las condiciones y consolida los registros sin modificar la traducción.
''')
print(json.dumps(counts,ensure_ascii=False))
