from ii_patchlib import *
p=Patches('clauses13')
p.replace('8.11.7',r'Se supone además que $q$ es propio',r'Se supone que $q$ es propio',editions=('current',),note='Keep the source order of the two hypotheses; only the second source clause says en outre.')
p.save()
