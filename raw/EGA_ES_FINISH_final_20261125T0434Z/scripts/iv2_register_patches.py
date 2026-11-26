#!/usr/bin/env python3
"""Apply the reviewed, source-aligned IV-2 impersonal-register patches.
The accompanying patch data contains only Spanish edits and relative witnesses.
File digests prevent replay at an unintended revision; already-applied files are skipped.
"""
import csv,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=Path(__file__).with_suffix('.json')
def digest(t):return hashlib.sha256(t.encode()).hexdigest()
def main():
 data=json.loads(DATA.read_text());done=0
 for rec in data:
  path=ROOT/rec['file'];text=path.read_text()
  if digest(text)==rec['after_sha256']:continue
  if digest(text)!=rec['before_sha256']:raise ValueError('Unexpected file revision: '+rec['file'])
  for edit in sorted(rec['edits'],key=lambda v:v['start'],reverse=True):
   assert text[edit['start']:edit['end']]==edit['before']
   text=text[:edit['start']]+edit['after']+text[edit['end']:]
  assert digest(text)==rec['after_sha256'];path.write_text(text)
  with (ROOT/'records/CAMBIOS_iv2.tsv').open('a') as out:
   wr=csv.writer(out,delimiter='\t')
   for edit in rec['edits']:wr.writerow([rec['file'],edit['place'],edit['before'],edit['after'],'standard','standard/STANDARDS_20261119b.md §§2,4; '+edit['source']])
  done+=len(rec['edits'])
 print('Reviewed register edits applied:',done)
if __name__=='__main__':main()
