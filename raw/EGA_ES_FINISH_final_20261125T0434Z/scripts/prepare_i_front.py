"""Translate missing title matter and retain the complete inherited introduction."""
import re, csv
from corpus import RESULT, ES, FR, write_tsv

TITLE = r'''\begin{titlepage}
\centering
{\Large INSTITUTO\par}
\vspace{0.4em}
{\Large DE ALTOS ESTUDIOS\par}
\vspace{0.4em}
{\Large CIENTÍFICOS\par}
\vfill
{\Large\bfseries ELEMENTOS DE GEOMETRÍA ALGEBRAICA\par}
\vspace{1.5em}
{\large\itshape por A. GROTHENDIECK\par}
\vspace{0.7em}
{\itshape Redactados con la colaboración de J. DIEUDONNÉ\par}
\vspace{2em}
I
\vspace{1.5em}
{\Large\bfseries EL LENGUAJE DE LOS ESQUEMAS\par}
\vfill
{\Large 1960\par}
\vspace{1.2em}
{\Large PUBLICACIONES MATEMÁTICAS, N.\textsuperscript{o} 4\par}
\vspace{0.5em}
{\large 5, ROND-POINT BUGEAUD --- PARÍS (XVI)\par}
\end{titlepage}
\thispagestyle{empty}
\vspace*{\fill}
\begin{center}
\fbox{%
  \begin{minipage}{0.50\textwidth}
  \centering
  DEPÓSITO LEGAL
  \smallskip
  1.\textsuperscript{a} edición \dotfill 3.\textsuperscript{er} trimestre de 1960
  \smallskip
  TODOS LOS DERECHOS
  reservados para todos los países
  \smallskip
  \copyright\ 1960, \emph{Institut des Hautes Études Scientifiques}
  \end{minipage}%
}
\end{center}
\vspace*{\fill}
\clearpage
'''

def main():
    changes=[];tr=[]
    for layer in ['CURRENT','DIPLOMATIC']:
        d=ES/f'worktree/es/{layer}/EGA_I_front';d.mkdir(exist_ok=True,parents=True)
        p=d/'frontmatter-es.tex';p.write_text(TITLE)
        tr.append([str(p.relative_to(RESULT)),'EGA_ES_FINISH_1_FRANCES/fr/current/BASE/native/ega1/frontmatter-fr.tex','whole file; current and diplomatic identical',len(re.findall(r'\b[^\W\d_]+\b',TITLE))])
        if layer=='DIPLOMATIC':
            p=d/'INTRODUCTION_ES_R570.tex';p.write_text((ES/'worktree/es/CURRENT/EGA_I_front/INTRODUCTION_ES_R570.tex').read_text())
        p=ES/f'worktree/es/{layer}/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex'
        if p.exists():
            t=p.read_text();old=r'\oldpage[I]{79}'
            if r'\label{chapter:I-fr}' not in t:
                new=old+'\n'+r'\phantomsection\label{chapter:I-fr}'
                t=t.replace(old,new,1);p.write_text(t)
                changes.append([str(p.relative_to(RESULT)),'chapter:I',old,new,'assembly','EGA_ES_FINISH_1_FRANCES/fr/current/BASE/native/ega1/chapter1-frontmatter-fr.tex'])
    write_tsv(RESULT/'records/TRADUCCION_i_front.tsv',['file','french_source','range','words'],tr)
    write_tsv(RESULT/'records/CAMBIOS_i_front.tsv',['file','place','before','after','kind','source'],changes)
if __name__=='__main__':main()
