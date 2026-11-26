"""Build standalone Spanish EGA TeX readers from the maintained source tree.

The generated files inline their project inputs and the authoritative French
CC0 notation preamble. The only required external inputs are TeX Live packages.
"""
from pathlib import Path
import re,json,csv,argparse,posixpath
from corpus import RESULT, ES, FR, write_tsv
from tex_tools import balanced_end

RIGHTS='Los derechos sobre las obras originales pertenecen a sus autores o a los representantes o herederos de estos. Nuestras traducciones, correcciones y composición tipográfica fueron producidas por IA. No tienen autor humano y, según nuestro entender, no están protegidas por derechos de autor; si aun así existiera algún derecho nuestro, se dedica al dominio público bajo CC0 1.0. Todo este trabajo reproduce o traduce las obras originales, por lo que nada de lo que aquí se publica concede licencia ni autoriza reproducción, traducción u otro uso de ellas. Estas ediciones se publican con fines educativos y sin ánimo de lucro, y no reclamamos ningún derecho que no poseamos. Si usted es titular de derechos sobre alguna de estas obras y se opone a su publicación aquí, abra una incidencia en GitHub y la retiraremos.'

def tex_escape(s):
    return ''.join({'&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}'}.get(c,c) for c in s)

def md_inline(s):
    tokens=[]
    def save(x):tokens.append(x);return f'ZZTOKEN{len(tokens)-1}ZZ'
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:save(r'\href{'+m[2].replace('_',r'\_')+'}{'+tex_escape(m[1])+'}'),s)
    s=re.sub(r'`([^`]+)`',lambda m:save(r'\texttt{'+tex_escape(m[1])+'}'),s)
    s=tex_escape(s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'\\textbf{\1}',s)
    s=re.sub(r'\*([^*]+)\*',r'\\emph{\1}',s)
    for i,t in enumerate(tokens):s=s.replace(f'ZZTOKEN{i}ZZ',t)
    return s

def markdown_credit(text):
    out=[];inlist=False
    for line in text.splitlines():
        if line.startswith('#'):
            if inlist:out.append(r'\end{itemize}');inlist=False
            out.append(r'\subsection*{'+md_inline(line.lstrip('# '))+'}')
        elif line.startswith('- '):
            if not inlist:out.append(r'\begin{itemize}');inlist=True
            out.append(r'\item '+md_inline(line[2:]))
        else:
            if inlist and not line.strip():out.append(r'\end{itemize}');inlist=False
            out.append(md_inline(line))
    if inlist:out.append(r'\end{itemize}')
    return '\n'.join(out)

def credit_links(text,source_folder):
    """Relocate inherited relative links to the standalone-reader ZIP layout."""
    def link(m):
        target=m[2]
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'):return m[0]
        destination=(source_folder/target).resolve()
        relative=posixpath.relpath(destination,RESULT/'readers'/'reader-folder')
        return '['+m[1]+']('+relative+')'
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,text)

def shared_front(title,edition,volume_sources=()):
    readme=(ES/'repo/README.md').read_text();how=readme.split('## Cómo se hizo\n',1)[1].split('\n## ',1)[0]
    sources=readme.split('## Fuentes y créditos\n',1)[1].split('\n## ',1)[0]
    attr=(ES/'repo/ATTRIBUTION.md').read_text()
    front=r'''\begin{titlepage}\centering\vspace*{20mm}
{\Huge\bfseries Elementos de geometría algebraica\par}\vspace{14mm}
{\LARGE '''+tex_escape(title)+r'''\par}\vspace{10mm}
{\large Alexander Grothendieck\\con la colaboración de Jean Dieudonné\par}
\vfill{\Large Edición española '''+tex_escape(edition)+r'''\par}
\vspace{8mm}{\large 25 de noviembre de 2026\par}\end{titlepage}
\chapter*{Créditos y derechos}
\addcontentsline{toc}{chapter}{Créditos y derechos}
\noindent\textbf{Trabajo de esta ejecución.} Traducción y preparación por GPT-6 Astra, OpenAI, ChatGPT Pro mode. AI-translated; AI-produced corrections. Cotejo francés heredado: Claude Opus 5.5, esfuerzo max, noviembre de 2026.

'''+markdown_credit(credit_links('## Créditos previos conservados\n'+how+'\n## Fuentes y créditos del repositorio\n'+sources+'\n'+attr,ES/'repo'))
    for p in volume_sources:
        if p.exists():front+='\n'+markdown_credit(credit_links(p.read_text(),p.parent))
    front+='\n'+r'\subsection*{Declaración de derechos de esta edición}'+'\n'+RIGHTS+'\n'+r'\clearpage\tableofcontents\clearpage'+'\n'
    return front

def flatten_text(t,project,seen=()):
    def repl(m):
        name=m.group(1);q=project/name
        if q.suffix!='.tex':q=Path(str(q)+'.tex')
        if not q.exists():raise FileNotFoundError(str(q.relative_to(RESULT)))
        if q in seen:raise ValueError('Input cycle')
        return '\n% BEGIN '+str(q.relative_to(RESULT))+'\n'+flatten_text(q.read_text(),project,seen+(q,))+'\n% END '+str(q.relative_to(RESULT))+'\n'
    return re.sub(r'(?m)^[ \t]*\\input\{([^}]+)\}[^\n]*',repl,t)

def body(wrapper):
    t=wrapper.read_text();t=t.split(r'\begin{document}',1)[1].rsplit(r'\end{document}',1)[0]
    t=re.sub(r'% BEGIN RIGHTS AND AI (?:TRANSLATION|AUTHORSHIP) NOTICE[\s\S]*?% END RIGHTS AND AI (?:TRANSLATION|AUTHORSHIP) NOTICE','',t)
    t=t.replace(r'\tableofcontents','')
    return flatten_text(t,wrapper.parent)

def extract_bbl(reader):
    t=reader.read_text();a=t.rfind(r'\begin{thebibliography}');b=t.rfind(r'\end{thebibliography}')
    return t[a:b+len(r'\end{thebibliography}')]+ '\n' if a>=0 and b>a else ''

def ordered_json(path,layer):
    x=json.loads(path.read_text())
    if isinstance(x,list):return x
    return x.get(layer,x.get(layer.lower(),x.get('input_order',[])))

def source_join(paths):
    return '\n'.join('% BEGIN '+str(p.relative_to(RESULT))+'\n'+p.read_text()+'\n% END '+str(p.relative_to(RESULT)) for p in paths)

def volume_i(layer):
    d=ES/f'worktree/es/{layer}';ch0=d/'EGA_I_ch0'
    # Content filenames encode the French decimal order; notes remain appended as supplied.
    units=sorted(ch0.glob('ega0_i_*.tex'),key=lambda p:[int(x) for x in re.findall(r'\d+',p.stem)])
    t=source_join([d/'EGA_I_front/frontmatter-es.tex',d/'EGA_I_front/INTRODUCTION_ES_R570.tex'])
    t+='\n'+r'\setcounter{section}{0}'+'\n'+source_join(units)
    notes=sorted(ch0.glob('*SOURCE_NOTE*.tex'))
    if notes:t+='\n'+source_join(notes)
    ch1=(d/'EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex').read_text()
    a=ch1.index(r'\section*{Sumario}');b=ch1.rfind(r'\nocite{*}')
    ch1=ch1[a:b]
    t+='\n'+r'\chapter*{CAPÍTULO I\\EL LENGUAJE DE LOS ESQUEMAS}\addcontentsline{toc}{chapter}{Capítulo I: El lenguaje de los esquemas}'+'\n'+ch1
    # Bibliographical titles stay in their original publication language.
    bib=(d/'EGA_I_apparatus/ega1_bibliography_es.tex').read_text()
    t+='\n'+bib
    for name in ['ega1_errata_list1_preface_notices_ES.tex','ega1_errata_list1_tate_1_8_1_to_1_8_6_ES.tex','ega1_errata_list1_1_8_7_to_end_ES.tex']:
        p=d/'EGA_I_apparatus'/name
        if p.exists():t+='\n'+p.read_text()
    return t

def volume_ii(layer):
    p=ES/f'repo/editions/II_{layer}/EGA_II_es_{layer.lower()}.tex';t=body(p)
    if layer=='DIPLOMATIC':
        # The printed bibliography continues volume I and does not reprint its
        # entries. Retain those printed citation numbers without a broken link.
        external={'I-1':'1','I-9':'9','I-11':'11','I-13':'13'}
        def cite(m):
            keys=[k.strip() for k in m[2].split(',')]
            return r'\textup{['+', '.join(external[k] for k in keys)+(', '+m[1] if m[1] else '')+']}' if all(k in external for k in keys) else m[0]
        t=re.sub(r'\\cite(?:\[([^\]]*)\])?\{([^}]+)\}',cite,t)
    return t

def volume_iii1(layer):
    p=ES/f'repo/editions/III1_{layer}/EGA_III1_ES_{layer}_READER.tex';t=body(p)
    # book does not accept the amsart running-title optional argument.
    t=re.sub(r'\\title\[[^\]]*\]',r'\\title',t)
    t=t.replace(r'\bibliography{the}',extract_bbl(ES/f'repo/readers/III1_{layer}/EGA_III1_ES_{layer}_READER.tex'))
    t=re.sub(r'\\bibliographystyle\{[^}]*\}','',t)
    return t

def volume_iii2():
    p=ES/'repo/editions/III2/EGA_III2_ES.tex';t=body(p)
    t=re.sub(r'\\EGAUnit\{([^}]+)\}',lambda m:(p.parent/'units'/(m[1]+'.es.tex')).read_text(),t)
    return t

def volume_iv1(layer):
    p=ES/f'worktree/es/PORTED_20261109/IV1_{layer}/EGA_IV1_ES.tex';t=body(p)
    order=ordered_json(RESULT/'records/IV1_CH4_INPUT_ORDER.json',layer)
    paths=[]
    for name in order:
        q=RESULT/name
        if not q.exists():q=ES/f'worktree/es/{layer}/EGA_IV1_ch4'/Path(name).name
        paths.append(q)
    return t+'\n'+source_join(paths)

def volume_iv2(layer):
    order=ordered_json(RESULT/'records/IV2_INPUT_ORDER.json',layer)
    paths=[]
    for name in order:
        q=RESULT/name
        if not q.exists():q=ES/f'worktree/es/{layer}/EGA_IV2'/Path(name).name
        paths.append(q)
    return source_join(paths)

def volume_iv3():
    p=ES/'worktree/es/PORTED_20261109/IV3/reader-es.tex';t=body(p)
    t=re.sub(r'\\title\[[^\]]*\]',r'\\title',t)
    t=t.replace(r'\bibliography{the}',extract_bbl(ES/'repo/readers/IV3/reader-es.tex'))
    t=re.sub(r'\\bibliographystyle\{[^}]*\}','',t)
    return t

def volume_iv4():return body(ES/'worktree/es/PORTED_20261109/IV4/EGA_IV4_ES.tex')

def cleanup_body(t):
    # Definitions inherited in the body can occur in more than one volume.
    t=t.replace(r'\newcommand{\shHom}',r'\providecommand{\shHom}')
    t=re.sub(r'\\newcommand\{(\\EGA(?:IndexLine|TermIndexLine|IVcontentsline|IVidxref|IVterm|IVthreeContents|IVthreeTerm))\}',r'\\providecommand{\1}',t)
    # The full-width introductory table must not inherit a paragraph indent.
    t=t.replace(r'\begin{tabular}{@{}p{0.22\linewidth}p{0.74\linewidth}@{}}',r'\noindent\begin{tabular}{@{}p{0.22\linewidth}p{0.74\linewidth}@{}}')
    # Historic IV3 stable destinations are represented by ordinary source labels
    # in the assembled reader. Keep the visible reference and link that label.
    t=re.sub(r'\\hyperlink\{ega4\.c04\.[^.{}]+\.(\d+(?:-\d+)*)\}',
             lambda m:r'\EGAReadLink{IV.'+m[1].replace('-','.')+'}',t)
    return t

def source_aliases(t):
    """Bind inherited French/Spanish reference suffixes to the same local target."""
    targets=re.findall(r'\\EGAReaderTarget\{([^}]+)\}\{([^}]+)\}',t)
    have=set(re.findall(r'\\label\{([^}]+)\}',t))|{a for a,b in targets}
    added=set()
    bindings=[]
    def bind(raw,actual):
        if '#' in raw:return
        key=re.sub(r'(?:-fr|-es|\.fr|\.es)$','',raw)
        core=re.sub(r'\.eq$','',key.removeprefix('eq:'))
        cores={key,core,re.sub(r'^IV\.2\.s','IV.',core),re.sub(r'^(?:section|subsection|chapter):','',core)}
        candidates=[a for k in sorted(cores) for a in [k,k+'-fr',k+'-es',k+'.fr',k+'.es',k+'.eq','eq:'+k]]
        for a in candidates:
            if a not in have and a not in added:
                bindings.append(r'\EGAReferenceAlias{'+a+'}{'+actual+'}');added.add(a)
    def aliases(m):
        bind(m[1],m[1])
        return m[0]
    re.sub(r'\\label\{([^}]+)\}',aliases,t)
    for actual,numbered in targets:bind(numbered,actual)
    return '\n'.join(bindings)+'\n'+t

def cumulative_bibliography(t,volume):
    """Give repeated bibliography keys their volume scope; preserve printed text."""
    prefix=volume+':'
    t=re.sub(r'(\\bibitem(?:\[[^\]]*\])?\{)([^}]+)(\})',lambda m:m[1]+prefix+m[2]+m[3],t)
    t=re.sub(r'(\\(?:cite|nocite)(?:\[[^\]]*\])?\{)([^}]+)(\})',lambda m:m[1]+','.join(prefix+k.strip() if k.strip()!='*' else '*' for k in m[2].split(','))+m[3],t)
    t=re.sub(r'(\\EGAIVFourExternalCitation\{)([^}]+)(\})',lambda m:m[1]+prefix+m[2]+m[3],t)
    # EGA I reprints the II addendum. Its labels get the reprint scope here.
    if volume=='EGA_I_CURRENT':t=t.replace('ega2:addendum:','ega1:reprinted-addendum:')
    return t

def main(only=None):
    specs=[]
    for layer in ['CURRENT','DIPLOMATIC']:
        specs.extend([(f'EGA_I_{layer}','EGA I',layer,lambda layer=layer:volume_i(layer),[]),
                      (f'EGA_II_{layer}','EGA II',layer,lambda layer=layer:volume_ii(layer),[ES/f'repo/editions/II_{layer}/FUENTES.md']),
                      (f'EGA_III1_{layer}','EGA III, primera parte',layer,lambda layer=layer:volume_iii1(layer),[ES/f'repo/editions/III1_{layer}/FUENTES.md']),
                      (f'EGA_IV1_{layer}','EGA IV, primera parte',layer,lambda layer=layer:volume_iv1(layer),[ES/f'repo/editions/IV1_{layer}/FUENTES.md']),
                      (f'EGA_IV2_{layer}','EGA IV, segunda parte',layer,lambda layer=layer:volume_iv2(layer),[])])
    specs.extend([('EGA_III2','EGA III, segunda parte','CURRENT',volume_iii2,[ES/'repo/editions/III2/FUENTES.md']),
                  ('EGA_IV3','EGA IV, tercera parte','CURRENT',volume_iv3,[ES/'repo/editions/IV3/FUENTES.md']),
                  ('EGA_IV4','EGA IV, cuarta parte','CURRENT',volume_iv4,[ES/'repo/editions/IV4/FUENTES.md'])])
    pre=(RESULT/'scripts/common_preamble.tex').read_text()+'\n% BEGIN authoritative French CC0 preamble-base.tex\n'+(FR/'current/BASE/native/preamble-base.tex').read_text()+'\n% END authoritative preamble-base.tex\n'
    bodies={};summary=[]
    for name,title,layer,make,sources in specs:
        if only and name!=only:continue
        try:t=cleanup_body(make())
        except (FileNotFoundError,KeyError,TypeError) as e:print(name,'NOT READY',str(e));continue
        bodies[name]=t
        folder=RESULT/'readers'/name;folder.mkdir(parents=True,exist_ok=True)
        full=pre+'\n'+r'\hypersetup{pdftitle={'+title+r'},pdfauthor={Alexander Grothendieck y Jean Dieudonné}}'+'\n'+r'\begin{document}'+'\n'+shared_front(title,'actual' if layer=='CURRENT' else 'diplomática',sources)+source_aliases(t)+'\n'+r'\end{document}'+'\n'
        (folder/(name+'.tex')).write_text(full)
        summary.append([name,len(full.encode()),len(re.findall(r'\\label\{',t)),len(re.findall(r'\\oldpage',t))])
    if not only:
        order=['EGA_I_CURRENT','EGA_II_CURRENT','EGA_III1_CURRENT','EGA_III2','EGA_IV1_CURRENT','EGA_IV2_CURRENT','EGA_IV3','EGA_IV4']
        if all(n in bodies for n in order):
            name='EGA_COMPLETA_CURRENT';folder=RESULT/'readers'/name;folder.mkdir(parents=True,exist_ok=True)
            titles={n:title for n,title,_,_,_ in specs}
            t='\n'.join(r'\clearpage\EGAResetVolumeCounters\part{'+titles[n]+r'}'+'\n'+cumulative_bibliography(bodies[n],n) for n in order)
            sources=[p for _,_,layer,_,ps in specs if layer=='CURRENT' for p in ps]
            full=pre+'\n'+r'\begin{document}'+'\n'+shared_front('Edición acumulativa','actual',sources)+source_aliases(t)+'\n'+r'\end{document}'+'\n'
            (folder/(name+'.tex')).write_text(full);summary.append([name,len(full.encode()),len(re.findall(r'\\label\{',t)),len(re.findall(r'\\oldpage',t))])
    assembly=RESULT/'records/READER_ASSEMBLY.tsv'
    if only and assembly.exists():
        prior=list(csv.reader(assembly.open(),delimiter='\t'))[1:]
        summary=[r for r in prior if r[0]!=only]+summary
    write_tsv(assembly,['reader','tex_bytes','labels','page_markers'],summary)
    for r in summary:print('\t'.join(map(str,r)))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--only');args=ap.parse_args();main(args.only)
