"""Compile the standalone readers and retain portable, privacy-clean reports.

Run after assemble_readers.py. Standard TeX Live installations use pdflatex
directly. The optional local bootstrap repairs missing format/font-map caches
in the execution environment without changing any reader content.
"""
from pathlib import Path
import os, re, json, csv, argparse, subprocess, concurrent.futures, collections
from corpus import RESULT, write_tsv

TEMP = RESULT.parent / 'tmp' / 'build'

def clean_log(text):
    # TeX wraps embedded font paths across physical lines, sometimes even inside
    # /usr. Consume the whole angle-bracket asset record before line-based
    # redaction, and also clean continuations from earlier redacted logs.
    def font_asset(match):
        compact=re.sub(r'\s+','',match.group(1))
        if compact.startswith(('/', '[TeX-installation-file]')):
            return '<[TeX-installation-file]>'
        return match.group(0)
    text=re.sub(r'<([^>]*)>',font_asset,text,flags=re.S)
    text=text.replace(str(RESULT.parent)+'/', '')
    text=re.sub(r'tmp/\s*build/', 'readers/', text)
    # Installed package paths have no bearing on the editorial record.
    text=re.sub(r'/(?:usr|opt|home|var|tmp)/[^\s()<>\n]*', '[TeX-installation-file]', text)
    text=re.sub(r'</\s*(?:usr|opt|home|var|tmp)/[^>]*>', '<[TeX-installation-file]>', text)
    text=re.sub(r'(?<![@\w])[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?![\w@])','[contact address omitted]',text)
    return text

def environment():
    TEMP.mkdir(parents=True,exist_ok=True)
    env=os.environ.copy()
    fmt=subprocess.run(['kpsewhich','pdflatex.fmt'],capture_output=True,text=True).stdout.strip()
    if fmt:
        env['TEXFORMATS']=str(Path(fmt).resolve().parent)+os.pathsep
    if not fmt:
        fmt_dir=TEMP/'formats';fmt_dir.mkdir(exist_ok=True)
        if not (fmt_dir/'pdflatex.fmt').exists():
            p=subprocess.run(['pdftex','-etex','-ini','--jobname=pdflatex','--progname=pdflatex','pdflatex.ini'],cwd=fmt_dir,capture_output=True,text=True)
            if p.returncode:raise RuntimeError('Cannot initialize the installed LaTeX format: '+clean_log(p.stdout[-1000:]))
        env['TEXFORMATS']=str(fmt_dir)+os.pathsep
    fontmap=subprocess.run(['kpsewhich','pdftex.map'],capture_output=True,text=True).stdout.strip()
    if not fontmap:
        names=['lm.map','cm.map','cmextra.map','latxfont.map','symbols.map','euler.map','rsfs.map','xypic.map']
        maps=[]
        for name in names:
            p=subprocess.run(['kpsewhich',name],capture_output=True,text=True).stdout.strip()
            if p:maps.append(Path(p).read_text())
        (TEMP/'pdftex.map').write_text('\n'.join(maps))
        env['TEXFONTMAPS']=str(TEMP)+os.pathsep
    return env

def parse_log(text):
    over=[]
    # TeX reports a box on the page following the latest shipout page number.
    page=1
    for m in re.finditer(r'\[(\d+)(?:\{|\]|\s)|Overfull \\([hv])box \(([-\d.]+)pt too (?:wide|high)\)',text):
        if m[1]:page=int(m[1])+1
        else:
            tail=text[m.end():m.end()+180]
            line=re.search(r'(?:at lines?|in paragraph at lines?)\s+(\d+)(?:--(\d+))?',tail)
            over.append([page,m[2],float(m[3]),line[1] if line else '',line[2] if line and line[2] else ''])
    warnings=[]
    for m in re.finditer(r'(?:LaTeX(?: Font)?|Package [^\n]+?|Class [^\n]+?) Warning:[\s\S]*?(?:\n\n|$)|pdfTeX warning[^\n]*(?:\n(?!\s*\n|\[|\(|!)[^\n]*)*',text):
        warnings.append(re.sub(r'\s+',' ',m[0]).strip())
    def warning_kind(w):
        if 'Font Warning' in w:return 'font substitution'
        if 'undefined' in w.lower():return 'undefined reference or citation'
        if 'multiply defined' in w.lower() or 'duplicate' in w.lower() or 'same identifier' in w.lower():return 'duplicate label or destination'
        if 'pdf string' in w.lower():return 'PDF bookmark string'
        if 'changed' in w.lower() or 'rerun' in w.lower():return 'rerun request'
        if w.startswith('pdfTeX'):return 'pdfTeX destination or resource'
        return 'other package warning'
    pages=re.search(r'Output written on [\s\S]*?\((\d+) pages?',text)
    return {'pages':int(pages[1]) if pages else 0,'overfull':over,'warnings':warnings,
            'warning_counts':dict(collections.Counter(warning_kind(w) for w in warnings))}

def compile_one(name,env,passes,stage):
    folder=RESULT/'readers'/name
    out=TEMP/name;out.mkdir(exist_ok=True)
    tex=folder/(name+'.tex')
    rc=0;details={};done=0
    for run in range(1,passes+1):
        p=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',f'-output-directory={out}',str(tex)],cwd=folder,env=env,capture_output=True,text=True)
        (out/f'{stage}-console-{run}.txt').write_text(p.stdout+p.stderr)
        raw=(out/(name+'.log')).read_text(errors='replace') if (out/(name+'.log')).exists() else p.stdout+p.stderr
        details=parse_log(raw);rc=p.returncode;done=run
        if rc:break
    (folder/'build.log').write_text(clean_log(raw))
    if not rc and (out/(name+'.pdf')).exists():
        import shutil
        shutil.copy2(out/(name+'.pdf'),folder/(name+'.pdf'))
        if stage=='baseline':shutil.copy2(out/(name+'.pdf'),out/'baseline.pdf')
    for old in folder.iterdir():
        if old.suffix in {'.aux','.toc','.log','.out'} and old.name!='build.log':old.unlink()
        if old.name=='build-console.txt':old.unlink()
    result={'reader':name,'stage':stage,'returncode':rc,'passes':done,**details}
    (RESULT/'records'/f'BUILD_{stage}_{name}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'reader':name,'stage':stage,'returncode':rc,'pages':details['pages'],'overfull':len(details['overfull']),'max_pt':max([x[2] for x in details['overfull']],default=0)},ensure_ascii=False),flush=True)
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--only',nargs='*');ap.add_argument('--passes',type=int,default=3);ap.add_argument('--stage',default='final');ap.add_argument('--jobs',type=int,default=3);a=ap.parse_args()
    names=a.only or sorted(p.name for p in (RESULT/'readers').iterdir() if (p/(p.name+'.tex')).exists())
    env=environment()
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        results=list(ex.map(lambda n:compile_one(n,env,a.passes,a.stage),names))
    # A targeted rebuild updates one report, but the stage summary must retain
    # the other completed readers instead of silently shrinking to --only.
    if a.only:
        results=[json.loads(p.read_text()) for p in sorted((RESULT/'records').glob(f'BUILD_{a.stage}_EGA*.json'))]
    write_tsv(RESULT/'records'/f'BUILD_{a.stage}_SUMMARY.tsv',['reader','returncode','passes','pages','overfull_boxes','maximum_pt','warnings'],[[r['reader'],r['returncode'],r['passes'],r['pages'],len(r['overfull']),max([b[2] for b in r['overfull']],default=0),len(r['warnings'])] for r in results])

if __name__=='__main__':main()
