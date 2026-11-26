"""Apply reviewed prose patches with exact surrounding-text preconditions."""
import json,hashlib,collections,argparse,re
from corpus import RESULT, write_tsv
from tex_tools import math_spans

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--include-iv1',action='store_true');a=ap.parse_args()
    data=json.loads((RESULT/'records/STANDARD_MODEL_PATCHES.json').read_text())
    receipt=RESULT/'records/STANDARD_MODEL_APPLIED_IDS.json'
    applied=set(json.loads(receipt.read_text()) if receipt.exists() else [])
    groups=collections.defaultdict(list)
    for i,p in enumerate(data['patches']):
        if i not in applied:groups[p['file']].append((i,p))
    changes=[];pending=[];bindings=[]
    for file,patches in groups.items():
        if not a.include_iv1 and '/PORTED_20261109/IV1_' in file:
            pending.extend([i,file,','.join(p['places']),'owned by the IV1 source-fidelity pass'] for i,p in patches);continue
        path=RESULT/file;t=path.read_text();edits=[]
        samehash=hashlib.sha256(t.encode()).hexdigest()==data['file_sha256'][file]
        for i,p in patches:
            start=None;mode=''
            if samehash and t[p['start']:p['end']]==p['before']:
                start=p['start'];mode='matching original SHA256'
            else:
                # Only complete exact contexts (never the changed word alone)
                # may rebind a patch after independent formula restoration.
                for n in [120,80,48,32,24]:
                    pre=p['prefix'][-n:];post=p['suffix'][:n];needle=pre+p['before']+post
                    if len(pre)+len(post)<30:continue
                    if t.count(needle)==1:
                        start=t.index(needle)+len(pre);mode=f'exact unique context {n}+{n}';break
            if start is None:
                pending.append([i,file,','.join(p['places']),'changed context; explicit rebinding required']);continue
            end=start+len(p['before'])
            assert t[start:end]==p['before']
            edits.append((start,end,p['after'],i,p));bindings.append([i,file,','.join(p['places']),mode])
        new=t;last=len(t)+1
        for start,end,after,i,p in sorted(edits,reverse=True):
            if end>last:raise ValueError('overlapping reviewed patches in '+file)
            new=new[:start]+after+new[end:];last=start
            changes.append([file,','.join(p['places']),p['before'],after,'standard','standard/DECISIONS_20261119b.tsv: '+','.join(p['standard_rows'])+'; '+'; '.join(p['sources'])])
            applied.add(i)
        if [s.text for s in math_spans(new)] != [s.text for s in math_spans(t)]:raise ValueError('prose patch changed math in '+file)
        if new!=t:path.write_text(new)
    receipt.write_text(json.dumps(sorted(applied))+'\n')
    old=RESULT/'records/CAMBIOS_standard_model.tsv'
    if old.exists():old.rename(RESULT/'records/STANDARD_MODEL_PROPOSED_CHANGES.tsv')
    seq=len(list((RESULT/'records').glob('CAMBIOS_standard_model_applied_*.tsv')))+1
    write_tsv(RESULT/f'records/CAMBIOS_standard_model_applied_{seq:02}.tsv',['file','place','before','after','kind','source'],changes)
    write_tsv(RESULT/'records/STANDARD_MODEL_PENDING.tsv',['patch_id','file','place','reason'],pending)
    write_tsv(RESULT/f'records/STANDARD_MODEL_BINDINGS_{seq:02}.tsv',['patch_id','file','place','binding'],bindings)
    print(json.dumps({'applied_now':len(changes),'applied_total':len(applied),'pending':len(pending)}))

if __name__=='__main__':main()
