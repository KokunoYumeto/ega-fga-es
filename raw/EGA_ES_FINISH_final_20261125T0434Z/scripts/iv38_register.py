from iv38_tools import *
rows=json.loads((ROOT/'records/IV3_REGISTER_89_PROPOSALS.json').read_text());t=SP.read_text();edits=[];review=[]
for i,r in enumerate(rows):
 if not r['file'].endswith('ega4-8.tex'):continue
 if r['after'] is None:review.append([i,r['place'],'retained',r['decision']]);continue
 exact=r['prefix']+r['before']+r['suffix'];matches=[m.start()+len(r['prefix']) for m in re.finditer(re.escape(exact),t)]
 if len(matches)!=1:review.append([i,r['place'],'requires refreshed context',str(len(matches))+' exact matches: '+r['before']]);continue
 a=matches[0];edits.append((a,a+len(r['before']),r['after'],r['place'],'STANDARDS_20261119b register; root-reviewed proposal '+str(i)+': '+r['decision']));review.append([i,r['place'],'applied',r['decision']])
apply(edits,'register','standard');write('IV38_REGISTER_REVIEW.tsv',['proposal_id','place','verdict','reason'],review)
print('requiring refreshed context',[r for r in review if r[2]=='requires refreshed context'])
