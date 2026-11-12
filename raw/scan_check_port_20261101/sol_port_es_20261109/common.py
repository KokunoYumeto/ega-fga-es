"""Shared setup for carrying the French EGA fixes into the Spanish EGA (ega-fga-es) with GPT-6.1 Sol, as for the
English (sol_bulk_20261109). Two Spanish editions: 'current' (the corrected French's fixes, FIXLOG_CURRENT) and
'diplomatic' (the diplomatic French's fixes); the items are the hand items the script port of 5 Nov left
(PORT_ES_CURRENT_HAND.json, PORT_ES_DIPLOMATIC_HAND.json)."""
import collections
import json
import pathlib
import re

BS = chr(92)
HERE = pathlib.Path(__file__).parent
E = HERE.parent
ED = E / "ega-fga-es" / "editions"
TREES = {"current": ["II_CURRENT", "III1_CURRENT", "III2", "IV1_CURRENT", "IV3", "IV4"],
         "diplomatic": ["II_DIPLOMATIC", "III1_DIPLOMATIC", "IV1_DIPLOMATIC"]}
HAND = {"current": "PORT_ES_CURRENT_HAND.json", "diplomatic": "PORT_ES_DIPLOMATIC_HAND.json"}
MARK = re.compile(re.escape(BS) + r"oldpage\[([^\]]+)\]\{(\d+)\}")


def load_tree(edition):
    """{file: (text, {(part, page): [(start, end)]})} for every .tex file with page markers in the edition's trees."""
    out = {}
    for d in TREES[edition]:
        for f in sorted((ED / d).rglob("*.tex")):
            t = f.read_text(encoding="utf-8", errors="replace")
            ms = list(MARK.finditer(t))
            if not ms:
                continue
            segs = collections.defaultdict(list)
            segs[(ms[0].group(1), int(ms[0].group(2)) - 1)].append((0, ms[0].start()))
            for i, m in enumerate(ms):
                segs[(m.group(1), int(m.group(2)))].append((m.start(), ms[i + 1].start() if i + 1 < len(ms) else len(t)))
            out[f] = (t, segs)
    return out


def rel(f):
    return str(f.relative_to(ED)).replace(BS, "/")


def iii_half(x):
    """EGA III-1 and III-2 share the page numbers 136-167 under the one part label "III"; the French file of the item
    tells them apart (ega3-1-fr.tex: III-1, ega3-6-fr.tex and ega3-7-fr.tex: III-2)."""
    if x.get("part") != "III":
        return None
    name = str(x.get("file", "")).replace(BS, "/").rsplit("/", 1)[-1]
    return "III2" if name.startswith(("ega3-6", "ega3-7")) else "III1"


def target_ok(f, x):
    """May the Spanish file f receive the fix x? For part III, only the tree of the same half of EGA III."""
    half = iii_half(x)
    if half is None:
        return True
    top = rel(f).split("/")[0]
    return top == "III2" if half == "III2" else top.startswith("III1_")


def has_target(edition, x):
    """The Spanish has EGA III-2 in one edition only (tree III2, with the corrected edition)."""
    return not (iii_half(x) == "III2" and "III2" not in TREES[edition])


def items(edition):
    return {x["entry"]: x for x in json.loads((E / HAND[edition]).read_text(encoding="utf-8"))}
