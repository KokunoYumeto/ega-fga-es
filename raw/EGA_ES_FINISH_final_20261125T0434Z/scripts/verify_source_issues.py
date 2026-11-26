"""Small exact counterexample certificates, not a proof check of EGA as a whole."""
import json
from corpus import RESULT
# IV.1.9.10: the spectrum of F_2 is the one-point space.
X=frozenset({'x'});E=frozenset();opens={frozenset(),X}
constructible_empty=True  # the empty locally closed subset itself
neighborhood_of_x=any('x' in U and U<=E for U in opens)
assert constructible_empty and not neighborhood_of_x
# IV.16.8.8 proof evaluation: n=0, B=Q[x], M=N=B, D=d/dx, a=x,t=1.
# D'(b tensor t)=b D(t): D'(x tensor1-1 tensor x)=x*0-1*1.
dprime=-1;first_member=1
assert dprime==-first_member and dprime!=first_member
out={'IV.1.9.10':{'X':'Spec(F_2)','E':'empty','E_constructible':True,'E_is_neighborhood_of_x':False},'IV.16.8.8.proof.evaluation':{'n':0,'D':'d/dx','a':'x','t':'1','Dprime_value':dprime,'first_member_16_8_8_2':first_member,'general_factor':'(-1)^(n+1)'}}
(RESULT/'records/SOURCE_ISSUES_CERTIFICATE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Two exact counterexample checks passed.')
