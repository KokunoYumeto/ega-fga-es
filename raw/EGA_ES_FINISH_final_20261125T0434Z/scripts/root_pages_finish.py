"""Restore reviewed source-page positions without changing prose or formulas."""
import re,json,collections
from corpus import RESULT,ES,write_tsv
from audit_i_ch1 import texts
from audit_iv4 import pairs,PROJECT
R=json.loads((RESULT/'records/ROOT_PAGE_POSITION_REVIEW.json').read_text())
flat={('IV4','current',str(fp.relative_to(__import__('corpus').FR/'current'))):(st,PROJECT/'ega4'/fp.name.replace('-fr.tex','-es.tex')) for fp,ft,st in pairs()}
for ed in ['current','diplomatic']:
 p,t=texts(ed.upper());flat[('I',ed)]=(t,p)
Ianchors={'80':r'\begin{env}[1.1.1]','81':r'\begin{env}[1.1.3]','82':r'\begin{proposition}[1.1.10]','201':r'\begin{remark}[10.9.10]','98':r'\begin{proposition}[2.1.3]','101':r'\subsection{Pegado de preesquemas}','102':r'\begin{proposition}[2.4.2]','103':r'\begin{corollary}[2.4.6]','104':r'\begin{env}[2.5.3]','107':r'\begin{lemma}[3.2.6.3]','130':r'\begin{proposition}[5.1.9]'}
Vanchors={'69':r'\begin{enumerate}','83':r'\begin{enumerate}','93':'considerar','129':'afines','167':'fielmente','168':'para todo','176':'como por','182':'tal que','187':'para que','208':'para una','222':r'\subsection','223':'se puede aplicar','224':'que ','251':'se llama','271':'lo mismo','273':'Se deduce','276':'Entonces','277':'de ','285':'para todo','289':'considerar','290':'de modo','291':'necesariamente','292':r'de \sref','309':'sobre','311':'que se tiene','319':'elemento','324':'su topología','326':'se pone','327':'grande'}
edits=collections.defaultdict(list);changes=[];review=[]
def resolve(st,pos,fallback):
 stack=[]
 for m in re.finditer(r'(?m)^% (BEGIN|END) (tree/[^\n]+)\n?',st[:pos+1]):
  if m[1]=='BEGIN':stack.append((RESULT/m[2],m.end()))
  elif stack:stack.pop()
 if stack:
  p,start=stack[-1];off=pos-start
  assert p.read_text()[max(0,off-30):off+30]==st[max(start,pos-30):pos+30],(p.name,off)
  return p,off
 return fallback,pos
for r in R:
 if r['status']!='review':continue
 sc,ed,page=r['scope'],r['layer'],r['page'];st,p=flat[(sc,ed)] if sc=='I' else flat[(sc,ed,r['source'])]
 if (sc,page) in [('I','122'),('IV4','58')]:
  review.append([sc,ed,page,'retained','Source and translation have the same clause; Spanish noun-adjective order or the source line-break inside morphisme accounts for the formula-interval difference.']);continue
 gap=r['expected_es_interval'];pos=r['hi']
 if sc=='I' and page in Ianchors:pos=st.index(Ianchors[page])
 elif sc=='IV4' and page in Vanchors:
  a=Vanchors[page];assert gap.count(a)==1,(page,a,repr(gap));pos=r['lo']+gap.index(a)
 mm=[m for m in re.finditer(r'\\oldpage(?:\[[^\]]*\])?\{'+re.escape(page)+r'\}',st)];assert len(mm)==1,(sc,page,len(mm));m=mm[0]
 oldp,oldpos=resolve(st,m.start(),p);newp,newpos=resolve(st,pos,p)
 marker=m.group();assert oldp.read_text()[oldpos:oldpos+len(marker)]==marker
 edits[oldp].append((oldpos,oldpos+len(marker),''));edits[newp].append((newpos,newpos,'\n'+marker+'\n'))
 changes.append([str(oldp.relative_to(RESULT)),f'{sc} printed page {page}',marker,'','own comparison',r['source']+': source page position moved to corresponding translated clause'])
 changes.append([str(newp.relative_to(RESULT)),f'{sc} printed page {page}','','\n'+marker+'\n','own comparison',r['source']+': source page position restored'])
 review.append([sc,ed,page,'moved','French and Spanish clauses read side by side; marker positioned at the translated clause or statement boundary.'])
for p,ee in edits.items():
 t=p.read_text()
 for a,b,new in sorted(ee,reverse=True):t=t[:a]+new+t[b:]
 p.write_text(t)
write_tsv(RESULT/'records/CAMBIOS_root_page_positions.tsv',['file','place','before','after','kind','source'],changes)
write_tsv(RESULT/'records/ROOT_PAGE_POSITION_DECISIONS.tsv',['scope','edition','page','decision','reason'],review)
print('page movements',len(changes)//2,'retained reviewed',sum(x[3]=='retained' for x in review))
