"""Compile the Spanish EGA editions touched by the port (one pdflatex pass each, in a scratch folder) and report the
errors with their source lines.  usage: python -I compile_es.py OUTDIR [EDITION ...]"""
import pathlib
import re
import subprocess
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
ROOT = E / "ega-fga-es" / "editions"
MASTERS = {"II_CURRENT": "EGA_II_es_current.tex", "III1_CURRENT": "EGA_III1_ES_CURRENT_READER.tex",
           "III2": "EGA_III2_ES.tex", "IV1_CURRENT": "EGA_IV1_ES.tex", "IV3": "reader-es.tex", "IV4": "EGA_IV4_ES.tex",
           "III1_DIPLOMATIC": "EGA_III1_ES_DIPLOMATIC_READER.tex", "IV1_DIPLOMATIC": "EGA_IV1_ES.tex",
           "II_DIPLOMATIC": "EGA_II_es_diplomatic.tex"}
out = pathlib.Path(sys.argv[1])
which = sys.argv[2:] or list(MASTERS)
for ed in which:
    d = out / ed
    d.mkdir(parents=True, exist_ok=True)
    src = ROOT / ed
    env = dict(__import__("os").environ, TEXINPUTS=str(src).replace("\\", "/") + "//;")
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-output-directory", str(d), MASTERS[ed]], cwd=src,
                       env=env, capture_output=True, text=True, encoding="latin-1", timeout=3000)
    log = (d / (pathlib.Path(MASTERS[ed]).stem + ".log")).read_text(encoding="latin-1", errors="replace")
    errs = re.findall(r"^! .*$", log, re.M)
    pages = re.search(r"Output written on .*?\((\d+) pages", log.replace("\n", ""))
    print(ed, "errors", len(errs), "pages", pages.group(1) if pages else None)
    for m in list(re.finditer(r"^! (.*)$\n(?:.*\n){0,6}?l\.(\d+) (.*)$", log, re.M))[:6]:
        print("   ", m.group(1)[:70], "| l." + m.group(2), m.group(3)[:80])
