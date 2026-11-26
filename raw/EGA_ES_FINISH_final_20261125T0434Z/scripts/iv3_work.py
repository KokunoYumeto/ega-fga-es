"""Source-fidelity edits for IV3; every exact edit is recorded."""
from pathlib import Path
import json,re
from corpus import RESULT,FR,write_tsv
DIR=RESULT/'tree/worktree/es/PORTED_20261109/IV3'
JOURNAL=RESULT/'records/IV3_FIDELITY_PATCH_LOG.json'

def save_rows(rows):
 JOURNAL.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 write_tsv(RESULT/'records/CAMBIOS_iv3_fidelity.tsv',['file','place','before','after','kind','source'],
           [[r[k] for k in ['file','place','before','after','kind','source']] for r in rows])

def replace(q,before,after,place,source,expected=1):
 t=q.read_text();count=t.count(before)
 assert count==expected,(str(q.relative_to(RESULT)),place,count,expected,before[:100])
 if before==after:return
 q.write_text(t.replace(before,after))
 rows=json.loads(JOURNAL.read_text()) if JOURNAL.exists() else []
 rows.append({'file':str(q.relative_to(RESULT)),'place':place,'before':before,'after':after,
              'kind':'own comparison','source':'EGA_ES_FINISH_1_FRANCES/fr/current/IV3/native/ega4/'+source+': '+place})
 save_rows(rows)

def apply_edits(q,edits,source):
 t=q.read_text();out=t;rows=json.loads(JOURNAL.read_text()) if JOURNAL.exists() else []
 last=len(t)+1
 for a,b,new,place in sorted(edits,reverse=True):
  assert b<=last,('Overlapping IV3 edits',q.name,a,b,last)
  last=a
  if t[a:b]==new:continue
  rows.append({'file':str(q.relative_to(RESULT)),'place':place,'before':t[a:b],'after':new,
    'kind':'own comparison','source':'EGA_ES_FINISH_1_FRANCES/fr/current/IV3/native/ega4/'+source+': '+place})
  out=out[:a]+new+out[b:]
 q.write_text(out);save_rows(rows)

if __name__=='__main__':
 q=DIR/'sections/ega4-11.tex';t=q.read_text()
 before='\\phantomsection\\label{IV.11.1.1.1}\n\\noindent\\textbf{(11.1.1.1)}'
 after='\\begin{env}[11.1.1.1]\n\\label{IV.11.1.1.1}'
 replace(q,before,after,'11.1.1.1','ega4-11-fr.tex')
 t=q.read_text();a=t.index('\\begin{env}[11.1.1.1]');b=t.index('\\medskip',a)
 before=t[a:b];after=before.rstrip()+'\n\\end{env}\n'
 replace(q,before,after,'11.1.1.1','ega4-11-fr.tex')
 t=q.read_text();m=re.search(r'\\begin\{equation\}\s*\\label\{IV\.11\.2\.9\.9\}.*?\\end\{equation\}',t,re.S);assert m
 after='\\begin{env}[11.2.9.9]\n\\label{IV.11.2.9.9}\n\\emph{Para $\\lambda$ suficientemente grande, el homomorfismo canónico\n$v_\\lambda:N_\\lambda\\otimes_{A_\\lambda}A\\to N$ es biyectivo.}\n\\end{env}'
 replace(q,m.group(),after,'11.2.9.9','ega4-11-fr.tex')
 print('Restored two numbered source wrappers')
