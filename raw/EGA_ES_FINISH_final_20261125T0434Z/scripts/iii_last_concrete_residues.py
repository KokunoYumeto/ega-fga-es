#!/usr/bin/env python3
"""Close the explicit final register and integral-closure findings from root QA."""
from iii_segment_decisions import *
S={
 '1:1.1.10:0':[('póngase','sean')],
 '1:1.2.4:14':[('Obsérvese','Se observará')],
 '1:1.4.2:0':[('Obsérvese','Se observará')],
 '1:1.4.6:0':[('Supóngase que se satisfacen','Se supone que se satisfacen'),('y, además, que','y se supone además que')],
 '1:1.4.8:0':[('Obsérvese','Se observará')],
 '6:6.7.3:21':[('Obsérvese','Se observará')],
 '6:6.7.4:14':[('obsérvese','se observará')],
 '6:6.9.2:26':[('Obsérvese','Se observará')],
 '7:7.4.8:1':[('Obsérvese','Se observará')],
 '7:7.6.5:10':[('Tómese','Hagamos, en efecto,')],
 '7:7.7.2:20':[('Obsérvese','Se observará')],
 '1:4.3.10:10':[('íntegramente','integralmente')],
 '1:4.4.8:4':[('íntegramente','integralmente')],
 '1:4.4.9:15':[('íntegramente','integralmente')],
}
if __name__=='__main__':
 apply_decisions({},S,name='final concrete root QA: source on future, soient, Faisons; integral closure distinguished from intègre')
