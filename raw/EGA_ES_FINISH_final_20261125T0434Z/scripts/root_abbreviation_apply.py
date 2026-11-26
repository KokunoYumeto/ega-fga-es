"""Apply source-bound abbreviation decisions after bilingual context review."""
import json,re,collections
from corpus import RESULT,write_tsv
R=json.loads((RESULT/'records/ROOT_ABBREVIATION_REVIEW.json').read_text());edits=collections.defaultdict(list);rows=[];dec=[]
for r in R:
 skip=r['scope']=='I' or (r['scope']=='IV4' and r['place']=='19.1.8')
 dec.append([r['file'],r['place'],r['before'],'retained: source respectivement/voir' if skip else 'restored '+r['after']])
 if skip:continue
 p=RESULT/r['file'];t=p.read_text();a,b=r['position'],r['end'];assert t[a:b]==r['before']
 if r['after']=='resp.' and t[b:b+1]==',' and not re.search(r'resp\.\s*,',r['fr']):b+=1
 edits[p].append((a,b,r['after']));rows.append([r['file'],r['place'],t[a:b],r['after'],'standard','STANDARDS_20261119b.md register; '+r['edition']+'/'+r['source']+': abbreviation retained from source'])
for p,ee in edits.items():
 t=p.read_text()
 for a,b,new in sorted(ee,reverse=True):t=t[:a]+new+t[b:]
 p.write_text(t)
write_tsv(RESULT/'records/CAMBIOS_root_abbreviations.tsv',['file','place','before','after','kind','source'],rows)
write_tsv(RESULT/'records/ROOT_ABBREVIATION_DECISIONS.tsv',['file','place','before','decision'],dec)
print('restored abbreviations',len(rows),'retained',len(R)-len(rows))
