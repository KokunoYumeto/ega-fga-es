from ii_patchlib import *
p=Patches('clauses12')
for unit in ['3.7.4','7.4.19','8.9.1']:
 p.replace(unit,'Obsérvese que','Se observa que')
for unit in ['8.3.4','8.7.6']:
 p.replace(unit,'obsérvese que','se observa que')
p.replace('7.3.5','supóngase que','se supone que')
p.replace('7.3.6','supóngase que','se supone que')
p.replace('7.3.6','supóngase finalmente que','se supone finalmente que')
p.replace('3.3.3','(Obsérvese que','(')
p.replace('8.7.6',r'obtenido haciendo \emph{explotar} en el cono afín $C$ el',r'obtenido por \emph{explosión} en el cono afín $C$ del',note='Retain the established noun explosión and the exact order of the source mathematical arguments and emphasis.')
p.replace('8.8.3',r'obtenido \emph{haciendo explotar en el cono afín $C$ el',r'obtenido \emph{por explosión en el cono afín $C$ del',note='Retain the established noun explosión and the exact order of the source mathematical arguments and emphasis.')
p.save()
