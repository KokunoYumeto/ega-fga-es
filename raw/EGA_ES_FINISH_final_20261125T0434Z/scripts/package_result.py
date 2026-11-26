"""Create a deliverable ZIP, excluding supplied archives and transient extracts."""
from pathlib import Path
import zipfile,hashlib,json,argparse,time,csv,io
from corpus import RESULT, write_tsv

EXCLUDED_DIRS={'tree/release_v2026-11-15-ega-i','tree/repo/readers'}
EXCLUDED_FILES={'records/I_DIPLOMATIC_PENDING.tsv','records/STANDARD_MODEL_REVIEW_CONTEXTS.json','records/STANDARD_MODEL_BOUND.json'}
def wanted(p):
    rel=p.relative_to(RESULT).as_posix()
    if any(rel==d or rel.startswith(d+'/') for d in EXCLUDED_DIRS):return False
    if rel in EXCLUDED_FILES or '/__pycache__/' in '/'+rel:return False
    return p.suffix not in {'.pyc','.aux','.toc','.out','.synctex','.gz'} and not p.name.endswith('.zip')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--checkpoint',type=int);ap.add_argument('--destination',type=Path);a=ap.parse_args()
    if a.checkpoint is not None:
        timer=json.loads((RESULT.parent/'task_started.json').read_text())
        elapsed=time.time()-timer['started_epoch']
        if elapsed<a.checkpoint*45*60:raise SystemExit('The next 45-minute checkpoint time has not arrived.')
        name=f'EGA_ES_FINISH_checkpoint_{a.checkpoint:02d}.zip'
    else:name='EGA_ES_FINISH_RESULT.zip'
    dest=a.destination or RESULT.parent;dest.mkdir(parents=True,exist_ok=True)
    out=dest/name
    if out.exists():raise SystemExit('A deliverable of this name already exists; it will not be overwritten.')
    files=sorted(p for p in RESULT.rglob('*') if p.is_file() and wanted(p) and p.name!='OUTPUT_MANIFEST.tsv')
    manifest=[]
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in files:
            payload=p.read_bytes();rel=p.relative_to(RESULT).as_posix()
            manifest.append([rel,len(payload),hashlib.sha256(payload).hexdigest()])
            z.writestr(rel,payload)
        buffer=io.StringIO();w=csv.writer(buffer,delimiter='\t',lineterminator='\n')
        w.writerow(['path','bytes','sha256']);w.writerows(manifest)
        z.writestr('OUTPUT_MANIFEST.tsv',buffer.getvalue())
    (RESULT/'OUTPUT_MANIFEST.tsv').write_text(buffer.getvalue())
    print(json.dumps({'file':out.name,'bytes':out.stat().st_size,'files':len(files)+1,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
if __name__=='__main__':main()
