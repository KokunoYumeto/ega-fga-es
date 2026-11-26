"""Finalize author preliminaries, errata copies, and inherited editorial notes."""
import re,collections,difflib
from corpus import RESULT,ES,FR,write_tsv
from tex_tools import math_spans,math_loose_key,numbered_units,retain_translated_text
from ii_tools import parts,espath
changes=[];tr=[];events=[]
# The I appendix repeats the fully collated list1 supplied with II.
for layer in ['current','diplomatic']:
 t=parts(espath(layer).read_text())['errata'].text
 a=t.index(r'\paragraph{(I, 1.7.3)');b=t.index(r'\begin{corollary}[1.8.7]')
 for name,new in zip(['ega1_errata_list1_preface_notices_ES.tex','ega1_errata_list1_tate_1_8_1_to_1_8_6_ES.tex','ega1_errata_list1_1_8_7_to_end_ES.tex'],[t[:a],t[a:b],t[b:]]):
  p=ES/f'worktree/es/{layer.upper()}/EGA_I_apparatus'/name;old=p.read_text();assert r'\footnote' not in old
  for op,i,j,k,l in difflib.SequenceMatcher(None,old.splitlines(keepends=True),new.splitlines(keepends=True),autojunk=False).get_opcodes():
   if op!='equal':changes.append([str(p.relative_to(RESULT)),'Errata List1',''.join(old.splitlines(keepends=True)[i:j]),''.join(new.splitlines(keepends=True)[k:l]),'own comparison','EGA_ES_FINISH_1_FRANCES/fr/'+layer+'/BASE/native/ega2/ega2-errata-addenda-fr.tex; synchronized with fully collated II errata'])
  p.write_text(new)
  events.append(['I.apparatus.'+name+':'+layer,'2026-11-25','GPT-6 Astra; ChatGPT Pro; root','carried as background without fault found','Spanish appendix synchronized with the fully source-collated II List1; inherited appendix has no footnotes. Formula order/count compared; no proof check.'])
# Restore the exact inherited editorial mathematical reading in the note.
for layer in ['CURRENT','DIPLOMATIC']:
 p=ES/f'worktree/es/{layer}/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex';t=p.read_text()
 old=r'esquemas $X\to\mathbf{Z}[T]$.}}';new=r'esquemas $X\to\bb{Z}[T]$.}}'
 if old in t:t=t.replace(old,new);p.write_text(t);changes.append([str(p.relative_to(RESULT)),'I.3.3.15 editorial note',old,new,'own comparison','EGA_ES_FINISH_2_ESPANOL/worktree/es/CURRENT/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex: inherited note preserved verbatim'])
# All unnumbered prefixes use the same formula order, checked separately.
base=ES/'worktree/es/PORTED_20261109/IV4/ega4'
for fname,src in [('ega4-16-es/components/00_intro.tex','ega4-16-fr.tex'),('ega4-20-es/components/01_component.tex','ega4-20-fr.tex'),('ega4-errata-addenda-list3-es.tex','ega4-errata-addenda-list3-fr.tex')]:
 p=base/fname;t=p.read_text();ft=(FR/'current/IV4/native/ega4'/src).read_text();fu=numbered_units(ft);ft=ft[:min(x.start for x in fu.values())];su=numbered_units(t);end=min((x.start for x in su.values()),default=len(t));st=t[:end]
 ff=math_spans(ft);ss=math_spans(st);assert len(ff)==len(ss),(fname,len(ff),len(ss));assert [math_loose_key(x.text) for x in ff]==[math_loose_key(x.text) for x in ss]
 for f,s in reversed(list(zip(ff,ss))):
  new=retain_translated_text(f.text,s.text);assert new is not None
  if re.sub(r'\s+','',new)!=re.sub(r'\s+','',s.text):
   changes.append([str(p.relative_to(RESULT)),'unnumbered prelude',s.text,new,'own comparison','IV4/native/ega4/'+src+': literal source formula']);t=t[:s.start]+new+t[s.end:]
 p.write_text(t);events.append(['IV4.'+src+':prelude','2026-11-25','GPT-6 Astra; ChatGPT Pro; root','carried as background without fault found',f'Full unnumbered prelude collated; {len(ff)} formula spans in source order. Textual comparison only.'])
patches={
 'ega4-20-es/components/01_component.tex':[(r'\subsection{Introduction.}',r'\subsection{Introducción.}'),('Veremos en','Se verá en')],
 'ega4-21a-es/components/00_intro.tex':[('remitimos al lector a la sección que se les dedica','el lector consultará la sección que se les dedica')],
 'ega4-errata-addenda-list3-es.tex':[
 ('« en outre si » por « si en\noutre »','« además si » por « si\nademás »'),('chap.~','cap.~'),('$A$-module por $B$-module','$A$-módulo por $B$-módulo'),('ramifiée por ramifié','ramificada por ramificado'),('« première » y « seconde »','« primera » y « segunda »'),('vérifiant','que verifica'),('(ii) et (iii)','(ii) y (iii)'),('2\\textsuperscript{e} Partie, Bibliographie','2\\textsuperscript{a} parte, Bibliografía'),('$\\alpha$) et $\\beta$)','$\\alpha$) y $\\beta$)'),('simple por lisse','simple por suave'),('obsérvese que la relación','se observará que la relación'),('podemos limitarnos al caso','se puede limitar al caso'),('« di-homomorphismes de modules (relatif à $u$) » por homomorphisme\nde $B$-modules','« dihomomorfismos de módulos (relativo a $u$) » por homomorfismo\nde $B$-módulos')]
}
for name,pp in patches.items():
 p=base/name;t=p.read_text()
 for old,new in pp:
  assert old in t,(name,old)
  changes.append([str(p.relative_to(RESULT)),name,old,new,'own comparison','IV4 source corresponding prelude or errata entry; untranslated words/register restored'])
  if any(w in old for w in ['Introduction','en outre','module','ramifi','première','vérifiant','Partie','lisse','di-homomorphismes']):tr.append([str(p.relative_to(RESULT)),'EGA_ES_FINISH_1_FRANCES/fr/current/IV4/native/ega4/'+('ega4-20-fr.tex' if '20-es' in name else 'ega4-errata-addenda-list3-fr.tex'),'unnumbered heading or quoted errata phrase: '+old,len(re.findall(r'\b[A-Za-zÀ-ÿ]+\b',re.sub(r'\\[A-Za-z]+','',new)))])
  t=t.replace(old,new)
 p.write_text(t)
write_tsv(RESULT/'records/CAMBIOS_root_front_apparatus.tsv',['file','place','before','after','kind','source'],changes)
write_tsv(RESULT/'records/TRADUCCION_root_front_apparatus.tsv',['file','french_source','range','words'],tr)
write_tsv(RESULT/'records/CHECK_EVENTS_root_front_apparatus.tsv',['statement_id','date','who','type','outcome'],events)
print('changes',len(changes),'translated snippets',len(tr))
