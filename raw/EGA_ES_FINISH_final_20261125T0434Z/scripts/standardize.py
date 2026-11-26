"""Terminology dry run and mechanically unambiguous prose replacements.

Revision b supersedes the earlier application plan for suave and vecindad.
Gender-sensitive and sense-sensitive changes are queued for a model pass.
"""
import re,json,csv,collections,argparse
from corpus import RESULT,ES,write_tsv,labels
from tex_tools import prose_segments

RULES=[
 ('es-foncteur',r'\bfunctor(?:es|ial(?:es)?|ialidad)?\b',None),
 ('es-quasi',r'\bcuasi(?:-|\s+)(?=[a-záéíóúñ])','cuasi'),
 ('es-preesquema',r'\bpre-esquema(s)?\b',lambda m:'preesquema'+(m.group(1) or '')),
 ('es-image-reciproque',r'\bimagen\s+recíproca\b','imagen inversa'),
 ('es-images-reciproques',r'\bimágenes\s+recíprocas\b','imágenes inversas'),
 ('es-limite-directe',r'\blímite(s)?\s+directo(s)?\b',lambda m:'límite'+(m.group(1) or '')+' inductivo'+(m.group(2) or '')),
 ('es-limite-inverse',r'\blímite(s)?\s+inverso(s)?\b',lambda m:'límite'+(m.group(1) or '')+' proyectivo'+(m.group(2) or '')),
 ('es-lisse',r'\blis[oa](s)?\b',lambda m:'suave'+(m.group(1) or '')),
 ('es-lissite',r'\b(?:lisitud|lisura)(es|s)?\b',lambda m:'suavidad'+('es' if m.group(1) else '')),
 ('es-iff',r'\bsi\s+y\s+sólo\s+si\b','si y solo si'),
 ('es-objet-final',r'\bobjeto(s)?\s+terminal(es)?\b',lambda m:'objeto'+(m.group(1) or '')+' final'+(m.group(2) or '')),
]
RULES[0]=(RULES[0][0],RULES[0][1],lambda m:m.group(0).replace('funct','funt'))
MODELS=[('es-voisinage',r'\bentornos?\b'),('es-stalk',r'\bfibras?\b'),('es-filtrant',r'\b(?:co)?filtrad[oa]s?\b')]
HELD=[('corps',r'\bcuerpos?\b'),('champ',r'\bcampos?\b'),('anneau de valuation',r'\b(?:valoración|valuación)\b')]

def canonical_files():
    out=[]
    for layer in ['CURRENT','DIPLOMATIC']:
        for d in ['EGA_I_ch0','EGA_I_ch1','EGA_I_front','EGA_I_apparatus','EGA_IV1_ch4','EGA_IV2']:
            out+=list((ES/f'worktree/es/{layer}/{d}').rglob('*.tex'))
    for d in ['IV1_CURRENT','IV1_DIPLOMATIC','IV3','IV4']:
        folder=ES/f'worktree/es/PORTED_20261109/{d}'
        out += [p for p in folder.rglob('*.tex') if not any(s in p.name for s in ['reference','preamble','external'])]
    for d in ['II_CURRENT','II_DIPLOMATIC','III1_CURRENT','III1_DIPLOMATIC','III2','II_NOTES','IV1_NOTES']:
        folder=ES/f'repo/editions/{d}'
        out += [p for p in folder.rglob('*.tex') if 'preamble' not in p.name]
    return sorted(set(out))

def place_for(t,pos):
    ll=labels(t[:pos])
    return ll[-1][0] if ll else 'front matter'

def run(apply=False,exclude_active=True,scope=None,tag=""):
    suffix=("_"+tag) if tag else ""
    dry=[];model=[];held=[];changes=[];count=collections.Counter();changed=collections.Counter()
    for p in canonical_files():
        rp=str(p.relative_to(RESULT));
        if scope and scope not in rp:continue
        t=p.read_text();edits=[]
        if exclude_active and any('/'+d+'/' in rp for d in ['EGA_I_ch0','EGA_IV2','EGA_IV1_ch4']):continue
        for a,b,prose in prose_segments(t):
            for rid,pat,new in RULES:
                for m in re.finditer(pat,prose,re.I):
                    start=a+m.start();end=a+m.end();old=m.group(0)
                    rendered=new(m) if callable(new) else new
                    if old[0].isupper():rendered=rendered[0].upper()+rendered[1:]
                    place=place_for(t,start);context=t[max(0,start-140):min(len(t),end+180)].replace('\n',' ')
                    dry.append([rid,rp,place,t.count('\n',0,start)+1,old,rendered,context]);count[rid]+=1
                    edits.append((start,end,rendered))
                    changes.append([rp,place,old,rendered,'standard',f'EGA_ES_FINISH_3_ESTANDAR/standard/DECISIONS_20261119b.tsv: {rid}'])
                    changed[rid]+=1
            for rid,pat in MODELS:
                for m in re.finditer(pat,prose,re.I):
                    start=a+m.start();end=a+m.end()
                    model.append([rid,rp,place_for(t,start),t.count('\n',0,start)+1,m.group(),t[max(0,start-180):min(len(t),end+260)].replace('\n',' ')])
            for term,pat in HELD:
                for m in re.finditer(pat,prose,re.I):
                    start=a+m.start()
                    held.append([term,m.group(), 'standard/DECISIONS_20261119b.tsv; standard/DOUBT_DECISIONS_20261119.tsv: held or low confidence; present edition term retained',f'{rp}:{place_for(t,start)}:line {t.count(chr(10),0,start)+1}','yes'])
        if apply:
            for a,b,new in sorted(edits,reverse=True):t=t[:a]+new+t[b:]
            p.write_text(t)
    write_tsv(RESULT/('records/ESTANDAR_DRY_RUN'+suffix+'.tsv'),['row','file','place','line','before','after','context'],dry)
    write_tsv(RESULT/('records/ESTANDAR_MODEL_QUEUE'+suffix+'.tsv'),['row','file','place','line','form','context'],model)
    write_tsv(RESULT/('records/GLOSARIO_REGISTRO_held'+suffix+'.tsv'),['french_term','spanish_rendering','witness','places','reversible'],held)
    if apply:write_tsv(RESULT/('records/CAMBIOS_standard_script'+suffix+'.tsv'),['file','place','before','after','kind','source'],changes)
    write_tsv(RESULT/('records/ESTANDAR_APLICADO_script'+suffix+'.tsv'),['row','found','changed','places_left','reason'],[[rid,count[rid],changed[rid] if apply else 0,'','Applied outside math, command identifiers and comments' if apply else 'Dry run only'] for rid,_,_ in RULES])
    print(json.dumps({'apply':apply,'candidates':dict(count),'model_queue':dict(collections.Counter(r[0] for r in model)),'held_occurrences':len(held)},ensure_ascii=False))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');ap.add_argument('--include-active',action='store_true');ap.add_argument('--scope');ap.add_argument('--tag',default='');a=ap.parse_args();run(a.apply,not a.include_active,a.scope,a.tag)
