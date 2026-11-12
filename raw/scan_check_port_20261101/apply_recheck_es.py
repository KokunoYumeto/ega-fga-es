"""Carry the two corrections of apply_french_recheck.py (0_IV 15.1.15: n+1 twice; proof of 17.3.4: (16.4.6, (ii)))
into the Spanish corrected edition IV1_CURRENT (the diplomatic Spanish keeps the print). Log PORT_ES_LOG.jsonl style.
usage: python -I apply_recheck_es.py [--apply]"""
import json
import pathlib
import sys

E = pathlib.Path(__file__).parent
S = E / "ega-fga-es" / "editions" / "IV1_CURRENT" / "ega4"
BS = chr(92)
ITEMS = [
    ("ega0-15-es.tex", "M/" + BS + "left(" + BS + "sum_{j=1}^{i-1}f_jM" + BS + "right)" + BS + "quad(1" + BS + "leq i"
     + BS + "leq n)", "(1" + BS + "leq i" + BS + "leq n)", "(1" + BS + "leq i" + BS + "leq n+1)"),
    ("ega0-15-es.tex", "M'/" + BS + "left(" + BS + "sum_{j=1}^{i-1}f'_jM'" + BS + "right)" + BS + "quad(1" + BS
     + "leq i" + BS + "leq n)", "(1" + BS + "leq i" + BS + "leq n)", "(1" + BS + "leq i" + BS + "leq n+1)"),
    ("ega0-17-es.tex", "se sabe entonces (16.4.6, (i)) que se tiene", "(16.4.6, (i))", "(16.4.6, (ii))"),
]
apply = "--apply" in sys.argv
for fname, window, a, b in ITEMS:
    f = S / fname
    t = f.read_text(encoding="utf-8")
    n = t.count(window)
    print(fname, "occurrences", n)
    if n == 1 and apply:
        t = t.replace(window, window.replace(a, b))
        f.write_text(t, encoding="utf-8", newline="")
        with open(E / "PORT_ES_CURRENT_LOG.jsonl", "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"file": str(f), "old": window, "new": window.replace(a, b),
                                 "source": "french_recheck"}, ensure_ascii=False) + "\n")
