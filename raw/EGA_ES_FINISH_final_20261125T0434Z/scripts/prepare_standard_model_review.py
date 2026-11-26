"""Produce relative-path source/target contexts for the terminology model pass."""
from pathlib import Path
import re,csv,json,collections,bisect
from corpus import RESULT,FR,canonical,labels
from tex_tools import ENV_RE

queue=list(csv.DictReader((RESULT/'records/ESTANDAR_MODEL_QUEUE.tsv').open(),delimiter='\t'))
indexes={}
for edition in ('current','diplomatic'):
    idx=collections.defaultdict(list)
    for p in (FR/edition).rglob('*.tex'):
        if p.name.startswith(('EGA_','preamble')): continue
        text=p.read_text()
        envstarts=[m.start() for m in ENV_RE.finditer(text)]
        anchors=labels(text)
        anchors.extend((canonical(m.group(1)),m.start(),m.end(),m.group(1)) for m in re.finditer(r'\\EGAReaderTarget\{[^{}]*\}\{([^{}]+)\}',text))
        chapter=next((v for k,v in [('ega0','0'),('ega1','I'),('ega2','II'),('ega3','III'),('ega4','IV')] if k in p.parts),None)
        if chapter:
            # Several III2 statements have printed numbers but no label.
            for m in re.finditer(r'\\begin\{[^{}]+\}\[([0-9]+(?:\.[0-9]+)+)\]',text):
                key=chapter+'.'+m.group(1)
                if not any(a[0]==key for a in anchors):anchors.append((key,m.start(),m.end(),key))
        for key,a,b,raw in anchors:
            j=bisect.bisect_right(envstarts,a)-1
            start=envstarts[j] if j>=0 else 0
            end=envstarts[j+1] if j+1<len(envstarts) else len(text)
            # A unit may end with a substantial unnumbered next section. Keep
            # it available for semantic alignment; excerpts below stay local.
            idx[key].append((p,text,start,end))
    indexes[edition]=idx

output=[]
for i,r in enumerate(queue):
    edition='diplomatic' if 'DIPLOMATIC' in r['file'] else 'current'
    key=re.sub(r'-proof$','',canonical(r['place']))
    matches=indexes[edition].get(key,[])
    while not matches and '.' in key:
        key=key.rsplit('.',1)[0]
        matches=indexes[edition].get(key,[])
    if len(matches)>1:
        # Chapter zero numbers overlap only through bibliographical anchors;
        # retain all candidates in the review evidence instead of guessing.
        names=[x[0].name for x in matches]
    term={'es-voisinage':r'voisinages?', 'es-stalk':r'fibr[ée]s?|germes?',
          'es-filtrant':r'(?:co)?filtr[a-zéèê]+'}[r['row']]
    snippets=[]
    for p,t,a,b in matches:
        unit=t[a:b]
        hits=list(re.finditer(term,unit,re.I))
        for h in hits:
            lo=max(0,h.start()-110);hi=min(len(unit),h.end()+220)
            snippets.append({'file':str(p.relative_to(FR.parent.parent)), 'anchor':key,
                             'term':h.group(),'context':re.sub(r'\s+',' ',unit[lo:hi])})
    r={**r,'id':i,'french':snippets}
    output.append(r)
(RESULT/'records/STANDARD_MODEL_REVIEW_CONTEXTS.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'rows':len(output),'without_french_term_context':sum(not r['french'] for r in output)},ensure_ascii=False))
