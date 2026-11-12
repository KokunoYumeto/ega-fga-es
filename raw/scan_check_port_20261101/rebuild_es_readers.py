"""Rebuild the Spanish EGA readers (readers/<dir>/: flattened TeX, PDF, sources ZIP) from the edition sources, the way
the published ones were made: the master flattened (flatten_tex.py), \\bibliography{the} replaced by the inlined
bibliography of the published reader (the bibliography is unchanged), the line endings of the published file kept,
two LaTeX runs, and the ZIP rebuilt with the same members (FUENTES.md, README.md, RIGHTS_NOTICE.md, direct/<reader>.tex,
native/<edition files>).

usage: python -I rebuild_es_readers.py WORKDIR [EDITION ...]"""
import io
import os
import pathlib
import re
import shutil
import subprocess
import sys
import zipfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from flatten_tex import flatten  # noqa: E402

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
G = E / "ega-fga-es"
# edition -> (master, reader dir, reader name, engine)
EDS = {
    "II_CURRENT": ("EGA_II_es_current.tex", "EGA_II", "EGA_II_es_current", "xelatex"),
    "II_DIPLOMATIC": ("EGA_II_es_diplomatic.tex", "EGA_II", "EGA_II_es_diplomatic", "xelatex"),
    "III1_CURRENT": ("EGA_III1_ES_CURRENT_READER.tex", "III1_CURRENT", "EGA_III1_ES_CURRENT_READER", "pdflatex"),
    "III1_DIPLOMATIC": ("EGA_III1_ES_DIPLOMATIC_READER.tex", "III1_DIPLOMATIC", "EGA_III1_ES_DIPLOMATIC_READER", "pdflatex"),
    "III2": ("EGA_III2_ES.tex", "III2", "EGA_III2_ES", "pdflatex"),
    "IV1_CURRENT": ("EGA_IV1_ES.tex", "IV1_CURRENT", "EGA_IV1_ES", "pdflatex"),
    "IV1_DIPLOMATIC": ("EGA_IV1_ES.tex", "IV1_DIPLOMATIC", "EGA_IV1_ES", "pdflatex"),
    "IV3": ("reader-es.tex", "IV3", "reader-es", "pdflatex"),
    "IV4": ("EGA_IV4_ES.tex", "IV4", "EGA_IV4_ES", "pdflatex"),
}
work = pathlib.Path(sys.argv[1])
which = sys.argv[2:] or list(EDS)
for ed in which:
    master, rdir, rname, engine = EDS[ed]
    src = G / "editions" / ed
    out = G / "readers" / rdir
    old_tex = (out / f"{rname}.tex").read_bytes().decode("utf-8")
    crlf = "\r\n" in old_tex
    flat = flatten(src / master, src)
    if "\\bibliography{the}" in flat:
        o = old_tex.replace("\r\n", "\n")
        a = o.find("\\providecommand{\\bysame}")
        b = o.find("\\end{thebibliography}", a)
        assert a >= 0 and b > a, ed
        flat = flat.replace("\\bibliography{the}", o[a:b + len("\\end{thebibliography}")], 1)
    flat = flat.replace("\r\n", "\n")
    if crlf:
        flat = flat.replace("\n", "\r\n")
    (out / f"{rname}.tex").write_bytes(flat.encode("utf-8"))
    # two LaTeX runs in a scratch folder
    d = work / ed
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    shutil.copy(out / f"{rname}.tex", d / f"{rname}.tex")
    env = dict(os.environ, TEXINPUTS=str(src).replace("\\", "/") + "//;")
    for _ in range(2):
        subprocess.run([engine, "-interaction=nonstopmode", f"{rname}.tex"], cwd=d, env=env, capture_output=True,
                       timeout=3000)
    log = (d / f"{rname}.log").read_text(encoding="latin-1", errors="replace")
    errs = len(re.findall(r"^! ", log, re.M))
    pages = re.search(r"Output written on .*?\((\d+) pages", log.replace("\n", ""))
    if errs == 0 and pages:
        shutil.copy(d / f"{rname}.pdf", out / f"{rname}.pdf")
    # sources ZIP with the same members as the published one
    zpath = out / f"{rname}_sources.zip"
    if zpath.exists():
        with zipfile.ZipFile(zpath) as z:
            names = z.namelist()
            old_members = {n: z.read(n) for n in names}
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
            for n in names:
                if n.startswith("direct/"):
                    data = (out / f"{rname}.tex").read_bytes()
                elif n.startswith("native/") and (src / n[len("native/"):]).exists():
                    data = (src / n[len("native/"):]).read_bytes()
                elif (src / n).exists():
                    data = (src / n).read_bytes()
                else:  # a member with no source file in the edition (e.g. a build script): keep it as published
                    data = old_members[n]
                info = zipfile.ZipInfo(n, date_time=(2026, 11, 5, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, data)
        zpath.write_bytes(buf.getvalue())
    print(ed, "errors", errs, "pages", pages.group(1) if pages else None, "| pdf", "updated" if errs == 0 and pages else
          "NOT updated", "| zip", "rebuilt" if zpath.exists() else "none")
