"""Restore authorial first person and finish boundary-sensitive prose clauses."""
from ii_tools import *
rows=[]
for ed in ['current','diplomatic']:
 path=espath(ed);t=path.read_text();edits=[]
 for part,ps in parts(t).items():
  su=units(ps.text)
  for unit,f in units(frpath(ed,part).read_text()).items():
   s=su[unit];fm=math_spans(f.text);sm=math_spans(s.text);assert len(fm)==len(sm)
   fb=[(0,0)]+[(m.start,m.end) for m in fm]+[(len(f.text),len(f.text))];sb=[(0,0)]+[(m.start,m.end) for m in sm]+[(len(s.text),len(s.text))]
   for i in range(len(fb)-1):
    fg=f.text[fb[i][1]:fb[i+1][0]];a,b=sb[i][1],sb[i+1][0];old=s.text[a:b];new=old
    if re.search(r'notre (?:assertion|conclusion)',fg,re.I):
     if unit=='3.2.9' and part=='errata':new=new.replace('la afirmación se obtiene por pegado','de donde nuestra afirmación')
     else:
      new=re.sub(r'\bla (afirmación|aserción|conclusión)\b',r'nuestra \1',new)
      new=new.replace('La afirmación','Nuestra afirmación')
    if re.search(r'Nous dirons',fg):new=new.replace('Se dice','Diremos')
    if 'nous dirons' in fg:new=new.replace('se dice','diremos')
    if 'nous écrivons' in fg:new=new.replace('se escribe','escribimos')
    if re.search(r'nous (?:le )?(?:noterons|désignerons)',fg):
     new=new.replace('y se denota por','y lo denotaremos por').replace('que se denota por','que denotaremos por')
    if 'nous appellerons' in fg:new=new.replace('; se llaman',', que llamaremos')
    if re.search(r'\bposons\b',fg,re.I) and not re.search(r'\b(?:pongamos|ponemos)\b',new,re.I):
     new=re.sub(r'\bsea(?:n)?\b','pongamos',new);new=re.sub(r'\bSea(?:n)?\b','Pongamos',new)
    if 'Prenons' in fg:
     new=new.replace('Tómese entonces','Tomemos entonces')
     if unit=='8.6.1':new=new.replace('Sea ','Tomemos por ')
     else:new=new.replace('Sea ','Tomemos ')
    if 'considérons' in fg.lower():
     new=new.replace('considérese','consideremos').replace('Considérese','Consideremos').replace('Considérense','Consideremos')
    if 'supposons que' in fg:new=new.replace('supóngase que','supongamos que')
    if 'Notons' in fg:new=new.replace('Obsérvese','Observemos')
    if unit=='1.6.4' and "nous n'avons" in fg:new=new.replace('solo hay que demostrar','solo tenemos que demostrar')
    if unit=='6.7.1.1' and 'nous considérons' in fg:new=new.replace('el caso considerado','el caso que consideramos')
    if unit=='7.3.7' and 'Nous pouvons caractériser' in fg:
     new=new.replace('Los morfismos universalmente cerrados (resp. los morfismos propios) pueden caracterizarse mediante','Podemos caracterizar los morfismos universalmente cerrados (resp. propios) mediante')
    if unit=='7.3.9' and 'nous permettront' in fg:new=new.replace('estos criterios permitirán','estos criterios nos permitirán')
    if part=='errata' and unit=='1.8.4' and "notons d'autre part" in fg:
     new=new.replace('. Para todo abierto','; observemos, por otra parte, que para todo abierto')
    if new!=old:
     edits.append((ps.start+s.start+a,ps.start+s.start+b,new));rows.append([str(path.relative_to(ROOT)),part+':'+unit+': gap '+str(i),old,new,'standard',source_note(ed,part,unit)+'; restore authorial nous/imperative; bilingual clause reviewed.'])
 path.write_text(apply_edits(t,edits))
write('II_CHANGES_register2.tsv',HEADER,rows)
print('authorial gaps restored',len(rows))
