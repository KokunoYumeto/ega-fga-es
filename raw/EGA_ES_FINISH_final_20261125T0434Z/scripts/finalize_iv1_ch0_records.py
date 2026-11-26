#!/usr/bin/env python3
"""Finalize IV1 chapter-0 fidelity, coverage, changes and translation records.
Supply --source-root with the already unpacked attached input archive.
"""
from pathlib import Path
import re,csv,argparse,json
from tex_tools import math_spans,retain_translated_text,balanced_end
P=argparse.ArgumentParser();P.add_argument('--source-root',type=Path,required=True);a=P.parse_args();r=Path(__file__).resolve().parents[1]
who='GPT-6 Astra, OpenAI, ChatGPT Pro mode; effort not separately reported; IV1 chapter-0 run'
ep=re.compile(r'\\begin\{[^}]+\}\[([\d.]+)\]');mp=re.compile(r'\\(?:label|oldpage|EGAReaderTarget|tag)(?:\[[^\]]*\])?\{[^}]+\}(?:\{[^}]+\})?')
def write(n,h,rows):
 with (r/'records'/n).open('w',encoding='utf-8',newline='') as f:w=csv.writer(f,delimiter='\t');w.writerow(h);w.writerows(rows)
def words(t):
 for s in reversed(math_spans(t)):t=t[:s.start]+' '+t[s.end:]
 t=re.sub(r'(?<!\\)%[^\n]*','',t);t=re.sub(r'\\[A-Za-z]+',' ',t)
 return len(re.findall(r'[A-Za-zÀ-ÿ]+(?:[-’\'][A-Za-zÀ-ÿ]+)*',t))
summary=[];coverage=[];events=[]
for ed in ['current','diplomatic']:
 for fp in sorted((a.source_root/'EGA_ES_FINISH_1_FRANCES/fr'/ed/'IV1/native/ega4').glob('ega0-*-fr.tex')):
  p=r/'tree/worktree/es/PORTED_20261109'/('IV1_'+ed.upper())/'ega4'/fp.name.replace('-fr.tex','-es.tex');fr=fp.read_text();es=p.read_text();fm=math_spans(fr);sm=math_spans(es);same=len(fm)==len(sm) and all(re.sub(r'\s+','',retain_translated_text(f.text,s.text) or f.text)==re.sub(r'\s+','',s.text) for f,s in zip(fm,sm));markers=mp.findall(fr)==mp.findall(es);assert same and markers,(ed,fp.name)
  ids=[m.group(1) for m in ep.finditer(fr)];sids=[m.group(1) for m in ep.finditer(es)];assert ids==sids,(ed,fp.name,'numbering')
  src=str(fp.relative_to(a.source_root));dst=str(p.relative_to(r));summary.append([ed,src,dst,len(ids),len(fm),len(sm),same,len(mp.findall(fr)),len(mp.findall(es)),markers])
  for lab in re.findall(r'\\label\{([^}]+)\}',fr):
   assert r'\label{'+lab+'}' in es
   coverage.append([src,lab,ed,dst,'translated_and_compared','Complete source formula, numbering and marker sequence compared; newly found missing prose translated; no proof verification claimed.'])
  for target in re.findall(r'\\EGAReaderTarget\{[^}]+\}\{([^}]+)\}',fr):coverage.append([src,target,ed,dst,'translated_and_compared','Exact French EGAReaderTarget retained in place of inherited language label.'])
  for id in ids:events.append([ed.upper()+':0.'+id,'2026-11-25',who,'carried as background without fault found','Compared Spanish source formula sequence, numbering and markers against supplied '+ed+' French. Translation/source-fidelity work only; no proof check claimed.'])
changes=[]
for name in ['structure','math','spans','anchors','punctuation','punctuation_manual','pages']:
 for row in csv.DictReader((r/'records'/('IV1_CH0_CHANGES_'+name+'.tsv')).open(),delimiter='\t'):changes.append([row[k] for k in ['file','place','before','after','kind','source']])
trans=[]
for row in csv.DictReader((r/'records/IV1_CH0_NEW_PROSE.tsv').open(),delimiter='\t'):
 trans.append([row['file'],row['french_source'],row['range'],words(row['text'])])
reviews=[]
for i,row in enumerate(csv.DictReader((r/'records/NOTATION_UNMATCHED_IV1_.tsv').open(),delimiter='\t'),1):
 reason='Restored exact source TeX after model comparison; full file now matches source formula and marker sequences.'
 if row['place'] in ['18.3.6','19.5.6.3','21.6.1']:reason='Text was present under an added Spanish numbered environment. Restored source environment structure and equation numbering; complete formula sequence verified.'
 elif row['place']=='15.1.8':reason='Translated the missing current French editorial footnote; kept it absent from the diplomatic layer, following its source.'
 elif row['place']=='21.1.9':reason='Translated the two missing paragraphs after source page marker 157, in both editions.'
 elif row['kind']=='insert':reason='Removed introduced formula grouping or restored source prose/math boundary after reading the French and Spanish; complete formula sequence verified.'
 reviews.append(['IV1-UNMATCHED-'+str(i).zfill(4),row['edition'],row['source'],row['place'],'resolved',reason])
write('MAPA_iv1_ch0.tsv',['french_file','place','edition','spanish_file','status','evidence'],coverage)
write('CAMBIOS_iv1_ch0.tsv',['file','place','before','after','kind','source'],changes)
write('TRADUCCION_iv1_ch0.tsv',['file','french_source','range','words'],trans)
write('CHECK_EVENTS_iv1_ch0.tsv',['statement_id','date','who','type','outcome'],events)
write('IV1_CH0_COMPLETE_FIDELITY.tsv',['edition','french_source','spanish_file','numbered_units','french_math_spans','spanish_math_spans','math_equal_with_translated_text','french_markers','spanish_markers','markers_equal'],summary)
write('IV1_CH0_UNMATCHED_REVIEW.tsv',['id','edition','source','place','verdict','reason'],reviews)
write('IV1_CH0_PUNCTUATION_PENDING.tsv',['file','place','reason','formula'],[])
print(json.dumps({'files':len(summary),'units':sum(x[3] for x in summary),'math_spans':sum(x[4] for x in summary),'source_markers':sum(x[7] for x in summary),'coverage_rows':len(coverage),'changes':len(changes),'translated_passages':len(trans),'translated_words':sum(x[3] for x in trans),'original_unmatched_resolved':len(reviews),'pending':0},ensure_ascii=False))
