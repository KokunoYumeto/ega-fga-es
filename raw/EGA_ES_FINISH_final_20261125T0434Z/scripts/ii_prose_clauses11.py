from ii_patchlib import *
p=Patches('clauses11')
p.replace('1.6.2',r'Por \sref[I]{I.5.5.12-fr}',r'En virtud \textbf{de} \sref[I]{I.5.5.12-fr}',editions=('diplomatic',),note='Preserve the source diplomatic emphasis.')
p.replace('3.5.6',r'$G(u^\sharp)$ es un subconjunto abierto',r'$G(u^\sharp)$ \textbf{es} un subconjunto abierto',editions=('diplomatic',),note='Preserve the source diplomatic emphasis.')
p.replace('4.6.18','morfismos cuasiproyectivos; morfismos propios','morfismos cuasiproyectivos morfismos propios',editions=('diplomatic',),note='Preserve the source diplomatic heading separator reading.')
p.save()
