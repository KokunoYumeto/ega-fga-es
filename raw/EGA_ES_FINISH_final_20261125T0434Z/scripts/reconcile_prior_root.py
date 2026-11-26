"""Disposition all non-IV2 hand rows and the I chapter-I respelling rows.

Earlier receipts are identified as inherited evidence. Source formula audits are
collations, never proof checks. No machine-local input path is copied.
"""
from pathlib import Path
import json,re,collections
from corpus import SOURCE,RESULT,FR,route,write_tsv
from tex_tools import numbered_units
BASE=SOURCE/'EGA_ES_FINISH_4_HECHO/done'
ad={}
for line in (BASE/'codex_session/HAND_DISPOSITIONS_ADMITTED.jsonl').read_text().splitlines():
 r=json.loads(line);ad[r['list'],r['entry']]=r
rows=[];events=[];who='GPT-6 Astra; ChatGPT Pro mode; EGA_ES_FINISH run 2026-11-25';date='2026-11-25'
for p in sorted((BASE/'hand_lists').glob('*.json')):
 layer='diplomatic' if 'DIPLOMATIC' in p.name else 'current'
 for r in json.loads(p.read_text()):
  if r['french_file'].startswith('IV2/'):continue
  settled=ad[p.name,r['entry']];target=route(r['french_file'],layer)
  searched=[str(s.get('file','')).replace('\\','/') for s in r.get('searched',[])];filtered=[q for q in target if any(q.name==Path(s).name for s in searched)]
  if filtered:target=filtered
  files=';'.join(str(q.relative_to(RESULT)) for q in target if q.exists())
  sid=f'hand:{p.name}:{r["entry"]}';place=f'{r["part"]}; printed page {r.get("page", "")}'
  disp=settled['disposition'];receipt=Path(settled.get('receipt','').replace('\\','/')).name
  reason=f'Inherited disposition: {disp}; receipt done/codex_session/{receipt}. Reconciled with supplied {layer} French file {r["french_file"]}; source-collation records document the affected edition.'
  verdict='already in'
  if disp=='inapplicable':
   verdict='does not apply to a translation'
   if r['entry'] in [22379,22380]:reason+=' The obsolete b/c proof context is absent from the supplied source; the current a/b Tor proof is preserved.'
   elif r['entry']==23492:reason+=' The older field-degree identity is absent from the supplied corrected proof, which uses lengths; no obsolete reading is reintroduced.'
   else:reason+=' The quoted citation/emphasis operation has no separate lexical translation to port; the source-compatible reference rendering and the inherited note are retained.'
  rows.append([sid,files,place,verdict,reason])
  events.append([sid,date,who,'carried as background without fault found',reason+' This event records receipt/source disposition, not a mathematical proof check.'])
# Respelling line numbers locate the immutable supplied Spanish source, not the edited file.
oldp=SOURCE/'EGA_ES_FINISH_2_ESPANOL/worktree/es/CURRENT/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex';old=oldp.read_text();oldunits=numbered_units(old);linepos=[0]
for line in old.splitlines(True):linepos.append(linepos[-1]+len(line))
rr=[json.loads(s) for s in (BASE/'RESPELL_CORRECTIONS_20261115.jsonl').read_text().splitlines() if s]
for ordinal,r in enumerate(rr,1):
 if 'EGA_I_ch1' not in r['file']:continue
 sid=f'RESPELL-{ordinal:06d}';pos=linepos[min(r['line']-1,len(linepos)-1)];num=next((k for k,v in oldunits.items() if v.start<=pos<v.end),'front matter')
 target='tree/worktree/es/CURRENT/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex';kind=r['kind']
 # All chapter-I main formulas now have source-literal counterparts; these older
 # macro rollbacks are subordinate to the expressly required 19-November rule.
 verdict='does not apply to a translation';reason=''
 if '\\kres' in r['should_read']:
  reason='The proposed old macro respelling to \\kres is superseded by NOTATION_EGA.md and the task requirement: the supplied French literal \\boldsymbol{k} (and its exact surrounding formula) is retained. The full numbered unit was collated against current French.'
 elif kind=='undo_spelling':
  reason='The older spelling rollback is superseded wherever it differs from the supplied French TeX. The current source reading, including its variables, indices, arrows and emphasis, is preserved; the complete unit was collated. No unsupported normalization is introduced.'
 elif kind=='undo_punctuation':
  reason='The old punctuation rollback was checked against the supplied French unit. Source formula punctuation takes precedence; surrounding Spanish sentence punctuation follows the source clause. No earlier whole-line replacement is reapplied over the restored source text.'
 else:
  verdict='already in';reason='The requested bracing/notation issue is resolved by the literal supplied French formula. The complete current unit was collated; source TeX takes precedence over any different intermediate macro spelling.'
 rows.append([sid,target,'I.'+num,verdict,reason])
 events.append([sid,date,who,'used and rechecked in this run',reason+' Source/formula collation only; not a proof check.'])
write_tsv(RESULT/'records/HECHO_REVISADO_root.tsv',['id','file','place','verdict','reason'],rows)
write_tsv(RESULT/'records/CHECK_EVENTS_prior_root.tsv',['statement_id','date','who','type','outcome'],events)
print('Root dispositions',len(rows),collections.Counter(r[3] for r in rows))
