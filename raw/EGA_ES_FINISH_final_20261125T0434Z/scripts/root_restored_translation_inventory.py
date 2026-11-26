#!/usr/bin/env python3
"""Inventory completed root edits without changing any Spanish source file."""
from pathlib import Path
import csv,re,json
from corpus import RESULT,FR,SOURCE,write_tsv
from audit_i_ch1 import texts,i_units
from finish_iii_records import plain

REC=RESULT/'records'
NAMES=['CAMBIOS_i_prose_restore.tsv','CAMBIOS_i_source_clauses.tsv','CAMBIOS_i_reviewed_literals.tsv','CAMBIOS_i_aligned_literal.tsv','CAMBIOS_i_aligned_literal_2.tsv','CAMBIOS_i_aligned_literal_3.tsv','CAMBIOS_i_aligned_literal_4.tsv','CAMBIOS_i_diplomatic.tsv','CAMBIOS_i_diplomatic_prose.tsv','CAMBIOS_i_front.tsv','CAMBIOS_root_front_apparatus.tsv','CAMBIOS_root_author_voice.tsv','CAMBIOS_iv4_finish_core.tsv']

def main():
 translations=[];inventory=[]
 for ed in ['current','diplomatic']:
  fp=FR/ed/'BASE/native/ega1/ega1-1-fr.tex';f=fp.read_text();u=i_units(f)['1.3.8'];assert 'Considérons en effet' in u.text
  sp,st=texts(ed.upper());su=i_units(st)['1.3.8'];assert 'Consideremos, en efecto,' in su.text
  pos=f.index('Considérons en effet',u.start)
  translations.append([str(sp.relative_to(RESULT)),'EGA_ES_FINISH_1_FRANCES/fr/'+ed+'/BASE/native/ega1/ega1-1-fr.tex','I.1.3.8, French line '+str(f.count('\n',0,pos)+1)+': omitted connective en effet restored as en efecto; only the two new prose words',2])
 ep='tree/worktree/es/PORTED_20261109/IV4/ega4/ega4-errata-addenda-list3-es.tex'
 fs='EGA_ES_FINISH_1_FRANCES/fr/current/IV4/native/ega4/ega4-errata-addenda-list3-fr.tex'
 old=(SOURCE/'EGA_ES_FINISH_2_ESPANOL'/ep.removeprefix('tree/')).read_text();new=(RESULT/ep).read_text();f=(SOURCE/fs).read_text()
 assert old.count('chap.~')==4 and 'chap.~' not in new
 assert old.count('(ii) et (iii)')==1 and '(ii) et (iii)' not in new
 assert old.count(r'$\alpha$) et $\beta$)')==1 and r'$\alpha$) et $\beta$)' not in new
 # The source has two et occurrences in IV.7.8.4; the first was already y in the inherited Spanish.
 for place,needle,words,desc in [
  ('III.4.4.12','chap.~V par : chap.~IV',2,'two previously untranslated chap. abbreviations rendered cap.; Roman chapter numerals excluded'),
  ('III.7.9.11','chap.~V par chap.~VI',2,'two previously untranslated chap. abbreviations rendered cap.; Roman chapter numerals excluded'),
  ('IV.7.8.4','(ii) et (iii)',1,'second quoted conjunction et rendered y; the first conjunction was already Spanish and is excluded'),
  ('IV.15.6.10',r'$\alpha$) et $\beta$)',1,'quoted conjunction et rendered y; formula symbols excluded; ou -> o already recorded in TRADUCCION_iv4_quotes'),
 ]:
  pos=f.rindex(needle) if place=='IV.7.8.4' else f.index(needle)
  translations.append([ep,fs,'Errata List3, '+place+', French line '+str(f.count('\n',0,pos)+1)+': '+desc,words])
 for name in NAMES:
  for i,r in enumerate(csv.DictReader((REC/name).open(),delimiter='\t'),1):
   a=plain(r['before']);b=plain(r['after']);verdict='not new coverage';added=0
   if name=='CAMBIOS_i_prose_restore.tsv' and r['place']=='1.3.8' and 'Consideremos, en efecto,' in r['after']:
    verdict='new connective counted';added=2;reason='The source en effet is absent from before and present as en efecto in after; formula and homomorphism grouping excluded.'
   elif name=='CAMBIOS_root_front_apparatus.tsv' and r['before'] in ['chap.~','(ii) et (iii)',r'$\alpha$) et $\beta$)']:
    verdict='new untranslated wording counted';added=4 if r['before']=='chap.~' else 1;reason='Original Spanish and final source were checked; exact occurrence count excludes already Spanish parallels.'
   elif name=='CAMBIOS_i_prose_restore.tsv' and r['place']=='5.3.9' and r'\begin{proof}' in r['before']:
    reason='The entire affine-local corrected proof was already Spanish in before; source wording was revised and inherited notes moved. No previously absent paragraph; no new-word count.'
   elif name=='CAMBIOS_iv4_finish_core.tsv' and r['place']=='21.13.14':
    reason='Condition b-prime was already translated in the proof in before; it was moved into the statement. Reordering only, no new translation.'
   elif name=='CAMBIOS_i_diplomatic_prose.tsv' and r['place'] in ['5.3.9','7.3.8','9.4.6']:
    verdict='already registered';reason='Covered by TRADUCCION_i_diplomatic_prose.tsv; no duplicate added.'
   elif name=='CAMBIOS_i_front.tsv':
    verdict='already registered';reason='Covered by TRADUCCION_i_front.tsv; no duplicate added.'
   elif name=='CAMBIOS_iv4_finish_core.tsv' and 'quoted correction' in r['source']:
    verdict='already registered';reason='Covered by TRADUCCION_iv4_quotes.tsv, including the ou -> o quote; no duplicate added.'
   elif name=='CAMBIOS_root_front_apparatus.tsv' and r['place']=='Errata List1':
    reason='Assembly/synchronization with source-collated Spanish II List1; inherited Spanish clauses remain Spanish. Not new corpus translation.'
   elif name=='CAMBIOS_root_front_apparatus.tsv' and any(x in r['before'] for x in ['Introduction','en outre','module','ramifi','première','vérifiant','Partie','lisse','di-homomorphismes']):
    verdict='already registered';reason='Covered by TRADUCCION_root_front_apparatus.tsv; bibliography separately covered by TRADUCCION_i_bibliography.tsv.'
   elif a==b:
    reason='No change in prose words after removing mathematical TeX and metadata; literal notation, formula layout or marker restoration only.'
   elif name=='CAMBIOS_root_author_voice.tsv':
    reason='Source author voice or relative-clause wording restored; existing proposition/proof text retained. Register act, not new translated passage.'
   else:
    reason='Existing Spanish rephrased, reordered or reconciled with source; notation mentions and formula-associated connectors are not counted as a new passage.'
   inventory.append([name,i,r['file'],r['place'],verdict,added,reason,r['source']])
 write_tsv(REC/'TRADUCCION_root_restored_passages.tsv',['file','french_source','range','words'],translations)
 write_tsv(REC/'ROOT_TRANSLATION_INVENTORY.tsv',['change_record','data_row','file','place','verdict','new_words','reason','source'],inventory)
 report=dict(records_reviewed=len(inventory),new_translation_rows=len(translations),new_prose_words=sum(r[3] for r in translations),notes=['I.5.3.9 CURRENT had its corrected affine-local proof already translated; no new coverage counted.','IV.21.13.14 condition b-prime was moved from the proof into the statement; no new coverage counted.','III-independent check; no Spanish source files modified.','Existing I front/bibliography/diplomatic and IV4 quotation translation rows were not duplicated.'])
 (REC/'ROOT_TRANSLATION_INVENTORY_COUNTS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':main()
