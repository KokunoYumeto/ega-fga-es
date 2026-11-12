"""Apply Sol's decisions to the Spanish EGA (one edition), as apply_port_decisions.py does for the English: an
"apply" edit is made when en_old occurs exactly once in the Spanish text of pages PAGE-1..PAGE+1 of the item's part
(in en_file, or, if that fails, in exactly one file of the edition's trees); otherwise the item goes to LEFT.
Every decision is logged in PORT_ES_<EDITION>_SOL_LOG.jsonl; items already logged are skipped.
usage: python -I apply.py current|diplomatic DECISIONS.json [...] [--dry]"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import E, MARK, has_target, items, load_tree, rel, target_ok  # noqa: E402

edition = sys.argv[1]
dry = "--dry" in sys.argv
paths = [a for a in sys.argv[2:] if not a.startswith("--")]
meta = items(edition)
tree = load_tree(edition)
text = {f: t for f, (t, _) in tree.items()}
LOG = E / f"PORT_ES_{edition.upper()}_SOL_LOG.jsonl"
LEFT = E / f"PORT_ES_{edition.upper()}_SOL_LEFT.json"
done = set()
if LOG.exists():
    done = {json.loads(l)["entry"] for l in LOG.read_text(encoding="utf-8").splitlines() if l.strip()}


def bal(s):
    """Brace balance, ignoring \\{ \\} and \\\\: an edit must not change it (9 Nov: Sol once wrote \\textup{(resp.\\})."""
    s = s.replace(chr(92) * 2, "").replace(chr(92) + "{", "").replace(chr(92) + "}", "")
    return s.count("{") - s.count("}")


def spans(f, part, page):
    t = text[f]
    ms = list(MARK.finditer(t))
    out = []
    for p in (page - 1, page, page + 1):
        if ms and (part, p) == (ms[0].group(1), int(ms[0].group(2)) - 1):
            out.append((0, ms[0].start()))
        for i, m in enumerate(ms):
            if (m.group(1), int(m.group(2))) == (part, p):
                out.append((m.start(), ms[i + 1].start() if i + 1 < len(ms) else len(t)))
    return out


def occurrences(f, part, page, s):
    hits = []
    for a, b in spans(f, part, page):
        k = text[f].find(s, a)
        while k >= 0 and k + len(s) <= b:
            hits.append(k)
            k = text[f].find(s, k + 1)
    return sorted(set(hits))


stats = {}
left = json.loads(LEFT.read_text(encoding="utf-8")) if LEFT.exists() else []
changed, logrecs = set(), []
for path in paths:
    for d in json.load(open(path, encoding="utf-8")):
        entry = int(d["id"])
        if entry in done or entry not in meta:
            stats["skipped"] = stats.get("skipped", 0) + 1
            continue
        x = meta[entry]
        if not has_target(edition, x):   # EGA III-2 has no Spanish diplomatic edition
            stats["no_target"] = stats.get("no_target", 0) + 1
            continue
        part, page = x["part"], int(x["page"])
        rec = dict(entry=entry, part=part, page=page, decision=d.get("decision"), note=d.get("note"),
                   batch=os.path.basename(path).rsplit(".", 1)[0])
        if d.get("decision") == "apply":
            old = (d.get("en_old") or "").replace("\r\n", "\n")
            new = (d.get("en_new") or "").replace("\r\n", "\n")
            cands = [f for f in text if (rel(f) == (d.get("en_file") or "") or f.name == os.path.basename(d.get("en_file") or ""))
                     and target_ok(f, x)]
            hit = None
            for f in cands:
                occ = occurrences(f, part, page, old) if old else []
                if len(occ) == 1:
                    hit = (f, occ[0])
            if hit is None and old:
                allhits = [(f, k) for f in text if target_ok(f, x) for k in occurrences(f, part, page, old)]
                if len(allhits) == 1:
                    hit = allhits[0]
            if hit is None or MARK.search(old) or MARK.search(new) or old == new or bal(old) != bal(new):
                rec["outcome"] = "left"
                left.append(dict(d, part=part, page=page))
            else:
                f, k = hit
                if not dry:
                    text[f] = text[f][:k] + new + text[f][k + len(old):]
                    changed.add(f)
                rec.update(outcome="applied", en_file=rel(f), en_old=old, en_new=new)
        else:
            rec["outcome"] = d.get("decision")
        stats[rec["outcome"]] = stats.get(rec["outcome"], 0) + 1
        logrecs.append(rec)
if not dry:
    for f in changed:
        f.write_text(text[f], encoding="utf-8", newline="")
    with open(LOG, "a", encoding="utf-8") as fh:
        for r in logrecs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    LEFT.write_text(json.dumps(left, ensure_ascii=False, indent=1), encoding="utf-8")
print(("dry run " if dry else "") + ", ".join(f"{k} {v}" for k, v in sorted(stats.items())), "| files changed", len(changed))
