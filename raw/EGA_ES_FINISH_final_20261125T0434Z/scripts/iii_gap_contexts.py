#!/usr/bin/env python3
from audit_iii_alignment import *

def bridge(edition,part):
 f,e,b,p,g=compare(edition,part);ss=sections(f);tt=sections(e);by={k:(lo,hi) for k,lo,hi in tt};all=[]
 for place,lo,hi in ss:
  x,y=by[place];ps=[q for q in p if q['place']==place];gs=[q for q in g if q['place']==place]
  for i,q in enumerate(gs):
   if q['fpos']:fa,fb=q['fpos'][0][0],q['fpos'][-1][1];left=next((z for z in reversed(ps) if z['fend']<=fa),None);right=next((z for z in ps if z['fstart']>=fb),None)
   else:
    ea,eb=q['epos'][0][0],q['epos'][-1][1];left=next((z for z in reversed(ps) if z['eend']<=ea),None);right=next((z for z in ps if z['estart']>=eb),None)
   fs=left['fend'] if left else lo;fe=right['fstart'] if right else hi
   es=left['eend'] if left else x;ee=right['estart'] if right else y
   all.append(dict(id=f'{edition}:{part}:{place}:{i}',edition=edition,part=part,place=place,fstart=fs,fend=fe,estart=es,eend=ee,f=f[fs:fe],e=e[es:ee],left=left['f'] if left else '',right=right['f'] if right else '',gap=q))
 return f,e,b,all
if __name__=='__main__':
 for ed,p in [('current','1'),('diplomatic','1'),('current','6'),('current','7')]:
  f,e,b,all=bridge(ed,p);(ROOT/'records'/f'III_BRIDGES_{ed}_{p}.json').write_text(json.dumps(all,ensure_ascii=False,indent=2)+'\n');print(ed,p,len(all),sum(len(x['f']) for x in all),sum(len(x['e']) for x in all))
