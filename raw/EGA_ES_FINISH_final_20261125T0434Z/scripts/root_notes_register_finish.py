"""Preserve inherited notes and close two source-bound register decisions."""
import json,re
from corpus import RESULT,ES,write_tsv
rows=[]
p=ES/'worktree/es/DIPLOMATIC/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex';t=p.read_text()
for old,new in [(r'esquemas $\mathbf{Z}[T]\to X$.}}',r'esquemas $X\to\bb{Z}[T]$.}}'),(r'Proposición~\hyperref[I.5.5.4]{5.5.5}.}}',r'Proposición~\hyperref[I.5.5.5]{5.5.5}.}}')]:
 if old in t:t=t.replace(old,new)
 else:assert new in t
 rows.append([str(p.relative_to(RESULT)),'inherited editorial note',old,new,'own comparison','EGA_ES_FINISH_2_ESPANOL/worktree/es/CURRENT/EGA_I_ch1/EGA_I_ES_CUMULATIVE.tex: exact inherited note restored in derived diplomatic layer'])
p.write_text(t)
for ed in ['CURRENT','DIPLOMATIC']:
 p=ES/f'worktree/es/PORTED_20261109/IV1_{ed}/ega4/ega0-22-es.tex';t=p.read_text();old='En (22.7), vamos a dar, para los anillos locales completos,';new='En (22.7), se va a dar, para los anillos locales completos,'
 assert old in t or new in t;t=t.replace(old,new);p.write_text(t)
 rows.append([str(p.relative_to(RESULT)),'0.22.6.9',old,new,'standard','STANDARDS_20261119b.md register; '+ed.lower()+'/IV1/native/ega4/ega0-22-fr.tex: on va donner'])
 p=ES/f'worktree/es/{ed}/EGA_IV2'/('ega4-2_2.1.8_through_2.1.14_ES'+('.diplomatic' if ed=='DIPLOMATIC' else '')+'.tex');t=p.read_text();old='Obsérvese que la proposición';new='Se observará que la proposición';assert old in t or new in t;t=t.replace(old,new);p.write_text(t)
 rows.append([str(p.relative_to(RESULT)),'IV.2.1.12',old,new,'standard','STANDARDS_20261119b.md register; '+ed.lower()+'/IV2/native/ega4/ega4-2-fr.tex: On notera'])
write_tsv(RESULT/'records/CAMBIOS_root_notes_register_finish.tsv',['file','place','before','after','kind','source'],rows)
print(len(rows))
