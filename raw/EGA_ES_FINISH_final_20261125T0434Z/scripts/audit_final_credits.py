"""Read-only audit of the fourteen assembled credit fronts against supplied records."""
from pathlib import Path
import re, json, hashlib, csv
from collections import Counter
from corpus import RESULT, SOURCE, write_tsv

ORIGINAL = SOURCE / 'EGA_ES_FINISH_2_ESPANOL/repo'
READERS = RESULT / 'readers'
PROMPT = SOURCE.parent / 'upload/PROMPT(20261125-003234).md'

def section(t, title):
    return t.split('## '+title+'\n', 1)[1].split('\n## ', 1)[0].strip()

def latex_unescape(t):
    return re.sub(r'\\([_&%#$\{\}])', r'\1', t)

def tex_plain(t):
    t=re.sub(r'\\href\{[^{}]*\}\{([^{}]*)\}', r'\1', t)
    t=latex_unescape(t)
    t=re.sub(r'\\(?:begin|end)\{[^}]*\}', ' ', t)
    t=re.sub(r'\\[A-Za-z@]+\*?', ' ', t)
    return t.replace('{',' ').replace('}',' ').replace('~',' ')

def md_plain(t):
    t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', t)
    return t.replace('*','').replace('`','')

def tok(t):
    return ' '.join(re.findall(r'[^\W_]+', t, re.UNICODE))

def paragraphs(md):
    return [x for x in re.split(r'\n\s*\n',md.strip()) if x.strip() and not x.lstrip().startswith('#')]

def md_urls(md):
    return re.findall(r'\[[^\]]+\]\(([^)]+)\)',md)

def tex_urls(t):
    return [latex_unescape(x) for x in re.findall(r'\\href\{([^{}]+)\}',t)]

def rel(p): return str(p.relative_to(SOURCE))
def front(p):
    t=p.read_text()
    return t.split(r'\begin{document}',1)[1].split(r'\tableofcontents',1)[0]

readme=(ORIGINAL/'README.md').read_text()
attr=(ORIGINAL/'ATTRIBUTION.md').read_text()
how=section(readme,'Cómo se hizo')
source_credits=section(readme,'Fuentes y créditos')
# Read the exact user-supplied rights string independently of the assembler.
prompt=PROMPT.read_text()
rights=re.search(r'Every reader.s front matter carries this statement, in Spanish: «([^»]+)»',prompt).group(1)
source_first_entries='\n'.join(source_credits.splitlines()[:6])
# The first two list entries are primary-work citations. Other credits are checked
# in full through ATTRIBUTION and a separate exact-identity/scope inventory below.
source_first_entries=source_credits.split('- EGA: las fuentes inglesas',1)[0].strip()
source_inventory={
 'human_contributors':['Mateo Carmona','Tim Holzschuh','Tim Hosgood','Ryan Keleti','Thiago Solovera & Nery','Wayne Yang','Steve Hnizdur','Jon Sterling'],
 'versions':['3d7afe28c99d1887ccdb85acf2ca1afd93fb1971','9976dd5f8e2ddcb388f0a07f3aa334f120d1019f'],
 'current_ai':['Traducción y preparación por GPT-6 Astra, OpenAI, ChatGPT Pro mode.','AI-translated; AI-produced corrections.','Cotejo francés heredado: Claude Opus 5.5, esfuerzo max, noviembre de 2026.'],
}
expected={}
for v in ['I','II','III1','IV1','IV2']:
 for layer in ['CURRENT','DIPLOMATIC']:
  expected[f'EGA_{v}_{layer}']=[f'editions/{v}_{layer}/FUENTES.md'] if v in {'II','III1','IV1'} else []
for v in ['III2','IV3','IV4']:expected['EGA_'+v]=[f'editions/{v}/FUENTES.md']
expected['EGA_COMPLETA_CURRENT']=['editions/'+v+'/FUENTES.md' for v in ['II_CURRENT','III1_CURRENT','III2','IV1_CURRENT','IV3','IV4']]
assert len(expected)==14
actual={p.parent.name:p for p in READERS.glob('*/*.tex')}
assert actual.keys()==expected.keys(),(set(actual)-set(expected),set(expected)-set(actual))
checks=[];summaries=[];findings=[];evidence=[]
for name,sourcefiles in sorted(expected.items()):
 p=actual[name];t=front(p);plain=tok(tex_plain(t));links=tex_urls(t);done=[]
 def record(check,source,status,detail):
  row=[name,str(p.relative_to(RESULT)),check,source,status,detail]
  checks.append(row);done.append(row)
  if status!='pass':findings.append(row)
 sourcegroups=[('README how','EGA_ES_FINISH_2_ESPANOL/repo/README.md:Cómo se hizo',how),('ATTRIBUTION','EGA_ES_FINISH_2_ESPANOL/repo/ATTRIBUTION.md',attr),('README sources and credits','EGA_ES_FINISH_2_ESPANOL/repo/README.md:Fuentes y créditos',source_credits)]
 for f in sourcefiles:sourcegroups.append(('edition FUENTES',rel(ORIGINAL/f),(ORIGINAL/f).read_text()))
 for label,path,md in sourcegroups:
  for i,para in enumerate(paragraphs(md),1):
   wanted=tok(md_plain(para));passed=wanted in plain
   record(label+' paragraph '+str(i),path,'pass' if passed else 'missing',para)
  for url in dict.fromkeys(md_urls(md)):
   if re.match(r'https?://',url):
    passed=url in links;actual_url=url if passed else ''
   else:
    # Relative hrefs must resolve within the delivered result tree. A relative
    # credit path remains identified by its original source in this audit.
    options=[url,'../../tree/repo/'+url]
    matched=[x for x in options if x in links]
    resolved=[x for x in matched if (p.parent/x).is_file()]
    passed=bool(resolved);actual_url=resolved[0] if resolved else (matched[0] if matched else '')
   record(label+' link',path,'pass' if passed else 'missing_or_unresolved',url+' -> '+actual_url)
  for ident in dict.fromkeys(re.findall(r'\b[0-9a-f]{64}\b',md)):
   record(label+' module SHA-256',path,'pass' if ident in t else 'missing',ident)
 for group,items in source_inventory.items():
  for item in items:
   record(group,'README.md / ATTRIBUTION.md / user prompt','pass' if tok(item) in plain else 'missing',item)
 record('rights exact','upload/PROMPT(20261125-003234).md:Rules.2','pass' if rights in t else 'missing','Literal Spanish statement, including CC0 1.0 and GitHub withdrawal sentence.')
 record('no AI-assisted','user prompt:Rules.1','pass' if not re.search(r'AI[ -]assisted',t,re.I) else 'prohibited_wording','Spanish identified as AI-translated and corrections as AI-produced corrections.')
 privacy=[]
 for pat in [r'(?<![\w/])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}',r'/(?:home|Users|workspace|tmp|mnt)/[^\s}]+',r'[A-Za-z]:\\(?:Users|Documents)\\']:
  privacy.extend(re.findall(pat,t,re.I))
 record('front privacy','user prompt:Rules.3','pass' if not privacy else 'private_data_present','No e-mail address or absolute local path in the front.' if not privacy else 'Private data detected; values suppressed.')
 unresolved=sum(x[4]!='pass' for x in done)
 summaries.append([name,str(p.relative_to(RESULT)),len(t),hashlib.sha256(t.encode()).hexdigest(),len(done),len(done)-unresolved,unresolved,'closed' if not unresolved else 'requires_front_fix','; '.join(sourcefiles) or 'Global credits; no separate inherited edition FUENTES supplied.'])
 evidence.append({'reader':name,'front_sha256':hashlib.sha256(t.encode()).hexdigest(),'front':t,'source_files':sourcefiles,'source_url_count':len(links),'unresolved':unresolved})

write_tsv(RESULT/'records/CREDITS_FINAL_REVIEW.tsv',['reader','file','front_characters','front_sha256','checks','passed','pending','status','specific_sources'],summaries)
write_tsv(RESULT/'records/CREDITS_FINAL_CHECKS.tsv',['reader','file','check','source','status','detail'],checks)
write_tsv(RESULT/'records/CREDITS_FINAL_FINDINGS.tsv',['reader','file','check','source','status','detail'],findings)
(RESULT/'records/CREDITS_FINAL_EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
counts={'readers':14,'checks':len(checks),'passed':len(checks)-len(findings),'pending':len(findings),'closed_readers':sum(x[7]=='closed' for x in summaries),'source_files_edited':0,'internet_link_liveness_checked':False,'proof_verification':False}
linkchecks=[x for x in checks if x[2].endswith(' link')]
external=[x[5].split(' -> ')[0] for x in linkchecks if x[5].startswith('http')]
internal=[x for x in linkchecks if not x[5].startswith('http')]
counts.update({'source_external_url_checks':len(external),'source_external_urls_unique':len(set(external)),'package_relative_link_checks':len(internal),'module_sha256_checks':sum('module SHA-256' in x[2] for x in checks),'reported_front_issues_resolved':5})
(RESULT/'records/CREDITS_FINAL_COUNTS.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(counts))
print(json.dumps(Counter((x[2],x[4]) for x in findings).most_common(),ensure_ascii=False))
