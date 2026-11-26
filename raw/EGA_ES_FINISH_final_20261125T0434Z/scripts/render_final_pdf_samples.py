"""Render a dispersed sample of every completed final reader for visual review.

The TSV identifies physical PDF pages and binds the review to the PDF SHA-256.
Rendering alone is not recorded as visual inspection; human/model dispositions
are written separately after the sheets have been viewed.
"""
from pathlib import Path
import argparse,json,hashlib,math
import fitz
from PIL import Image,ImageDraw,ImageFont
from corpus import RESULT,write_tsv

ap=argparse.ArgumentParser();ap.add_argument('--only',nargs='*');a=ap.parse_args()
out=RESULT/'qa/final';out.mkdir(parents=True,exist_ok=True)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',15)
for folder in sorted((RESULT/'readers').iterdir()):
    name=folder.name
    if a.only and name not in a.only:continue
    report=RESULT/'records'/f'BUILD_final_{name}.json'
    if not report.exists() or json.loads(report.read_text())['returncode']:continue
    p=folder/(name+'.pdf');doc=fitz.open(p);n=len(doc)
    pages=sorted(set([1,min(n,5),max(1,round(n*.2)),max(1,round(n*.5)),max(1,round(n*.8)),n]))
    if name=='EGA_COMPLETA_CURRENT':
        parts=[x[2] for x in doc.get_toc() if x[0]==1 and x[1].startswith('EGA ')]
        if len(parts)==8:
            pages=sorted(set([1,8]+[min(n,(x+y)//2) for x,y in zip(parts,parts[1:]+[n])]+[n]))
        else:pages=sorted(set([1,8]+[max(1,round(n*i/10)) for i in range(1,10)]+[n]))
    sha=hashlib.sha256(p.read_bytes()).hexdigest();rr=[]
    for chunk in range(math.ceil(len(pages)/6)):
        chosen=pages[chunk*6:chunk*6+6];canvas=Image.new('RGB',(1512,1488),'#d9dde2');draw=ImageDraw.Draw(canvas)
        for j,page in enumerate(chosen):
            pg=doc[page-1];pix=pg.get_pixmap(matrix=fitz.Matrix(500/pg.rect.width,500/pg.rect.width),alpha=False)
            im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);x=(j%3)*504+2;y=(j//3)*744+28
            canvas.paste(im,(x,y));draw.text((x,y-24),f'{name} · p. {page}/{n}',fill='black',font=font)
            rr.append([name,page,n,str((out/f'{name}_{chunk+1}.png').relative_to(RESULT)),sha,'rendered; awaiting visual review'])
        canvas.save(out/f'{name}_{chunk+1}.png')
    write_tsv(RESULT/'records'/f'PDF_SAMPLE_{name}.tsv',['reader','physical_page','total_pages','contact_sheet','pdf_sha256','status'],rr)
    print(name,pages,flush=True)
