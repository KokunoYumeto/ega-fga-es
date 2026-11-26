"""Restore the printed formula across an inherited editorial footnote marker."""
import re
from audit_i_ch1 import texts,i_units
from tex_tools import balanced_end
from i_edit_helper import replace
p,t=texts('DIPLOMATIC');u=i_units(t)['4.2.3'];m=re.search(r'\\footnote\{',u.text);e=balanced_end(u.text,m.end()-1);note=u.text[m.start():e]
old=r'$\Gamma(\psi)$'+note+r'$:\Gamma(\sh{O}_X)\to\Gamma(\sh{O}_Y)$'
if old in u.text:replace('4.2.3',old,r'$\Gamma(\psi):\Gamma(\mathscr{O}_X)\to\Gamma(\mathscr{O}_Y)$'+note,('DIPLOMATIC',))
