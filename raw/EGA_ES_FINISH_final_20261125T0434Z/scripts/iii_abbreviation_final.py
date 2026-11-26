#!/usr/bin/env python3
"""Close source-bound abbreviation and explicitly observed duplication residues."""
from iii_register_candidates import *
import hashlib

F=re.compile(r'\bresp\.|\brespectivement\b',re.I)
E=re.compile(r'\bresp\.|\brespectivamente\b',re.I)
OVERRIDE={
 ('1','11.4.2',19):'.\n  \\item[(ii)] Para cada ',
 ('1','2.2.3',8):' el núcleo, la imagen y el conúcleo de ',
 ('1','4.6.3',2):'.\n\\end{corollary}\n\n\\begin{proof}\nSe puede limitar al caso en que ',
 ('7','7.7.9',19):', hay que reemplazar\n',
 ('1','11.4.3',8):' existe\n(cf. \\hyperref[0.11.3.1-fr]{11.3.1}); entonces las dos sucesiones espectrales\n',
}

def run():
 logs=[];counts=collections.Counter()
 for ed,part in [('current','1'),('diplomatic','1'),('current','6'),('current','7')]:
  f,e,b,p,g=compare(ed,part);assert not g;edits=[]
  for x in segments(ed,part):
   new=x['e'];why=[];key=(part,x['place'],int(x['id'].rsplit(':',1)[1]))
   if key in OVERRIDE:
    new=OVERRIDE[key];why.append('source abbreviation, punctuation or duplicated prose residue')
   else:
    ff=list(F.finditer(x['f']));ee=list(E.finditer(new))
    if len(ff)==len(ee):
     for a,z in reversed(list(zip(ff,ee))):
      if a[0].lower()=='resp.' and z[0].lower()!='resp.':
       stop=z.end()
       if new[stop:stop+1]==',' and not x['f'][a.end():].lstrip().startswith(','):stop+=1
       new=new[:z.start()]+'resp.'+new[stop:];counts['respectivamente_to_resp']+=1
       why.append('source resp. retained as abbreviation')
   if part=='1' and x['place']=='11.9.3' and key[2]==9:
    old=r'(Bourbaki, \emph{Alg\`ebre commutative}, cap.~I, \S2, ejerc.~6).'
    assert old in new
    new=new.replace(old,r'(cf. Bourbaki, \emph{Alg. comm.}, cap.~I, \S~2, ejerc.~6).')
    why.append('restore source cf. and abbreviated publication title')
   if part=='1' and x['place']=='13.7.6' and key[2]==12:
    if 'decimos' in new:
     assert re.search(r'nous\s+dirons',x['f'],re.I)
     new=new.replace('decimos','diremos');why.append('source author future retained')
   if new==x['e']:continue
   if any(q[0]<=x['estart'] and x['eend']<=q[1] for q in b):
    edits.append((x['estart'],x['eend'],new,x['place'],x['e']))
   else:
    for tag,i,j,k,l in difflib.SequenceMatcher(None,x['e'],new,autojunk=False).get_opcodes():
     if tag!='equal':edits.append((x['estart']+i,x['estart']+j,new[k:l],x['place'],x['e'][i:j]))
   counts['changed_segments']+=1
   logs.append(dict(id=x['id'],edition=ed,part=part,place=x['place'],source_sha256=hashlib.sha256(x['f'].encode()).hexdigest(),before=x['e'],after=new,reason='; '.join(why)))
  if edits:apply_edits(ed,part,edits,b)
  print(ed,part,len(edits))
 (ROOT/'records/III_ABBREVIATION_DECISIONS.json').write_text(json.dumps(dict(counts=counts,decisions=logs),ensure_ascii=False,indent=2)+'\n')
 print(dict(counts))

if __name__=='__main__':run()
