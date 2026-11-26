#!/usr/bin/env python3
"""Apply settled recouvrement terminology in the 34 residual III2 intervals."""
from iii_segment_decisions import *

def run():
 S={}
 for x in segments('current','6'):
  mm=list(re.finditer(r'\bcubrimientos?\b',x['e']))
  if not mm:continue
  assert len(mm)==len(re.findall(r'\brecouvrements?\b',x['f']))
  S[x['id'].split(':',1)[1]]=[('cubrimiento','recubrimiento')]
 assert len(S)==34,len(S)
 apply_decisions({},S,name='recouvrement -> recubrimiento; STANDARDS_20261119b settled Spanish term; aligned French checked')

if __name__=='__main__':run()
