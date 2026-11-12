"""Check Sol's decisions for one Spanish edition before they are applied (the mechanical checks of
sol_bulk_20261109/audit_bulk.py, on the Spanish trees). For every id of decisions_<edition>_*.json, with the French fix
OLD -> NEW from the edition's hand items:
- apply: en_old must occur exactly once on the Spanish pages p-1..p+1 (as apply.py requires);
- already: en_old (the Spanish that "already says it") must occur there and carry the markup the fix adds: \\emph for
  an added emphasis, no \\emph for a removed one, upright markup (or a place outside every italic statement) for an
  added \\textup;
- not_applicable: doubtful when the fix adds or removes \\emph or \\textup (those normally carry over);
- unclear: doubtful.
Writes AUDIT_<edition>.md, doubtful_<edition>.json and clean_<edition>.json (the decisions that passed, for apply.py).
usage: python -I audit.py current|diplomatic"""
import collections
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import BS, HERE, has_target, items, load_tree, rel, target_ok  # noqa: E402

edition = sys.argv[1]
UPRIGHT_REF_TREES = {"II_CURRENT", "II_DIPLOMATIC", "III1_CURRENT", "III1_DIPLOMATIC", "IV3", "IV4"}
ITALIC = ("theorem", "proposition", "corollary", "lemma", "conjecture", "env", "statement", "teorema", "proposicion",
          "corolario", "lema")
meta = items(edition)
tree = load_tree(edition)
text = {f: t for f, (t, _) in tree.items()}
segs = {f: s for f, (_, s) in tree.items()}


def find(part, page, s, x=None):
    hits = []
    for f in text:
        if x is not None and not target_ok(f, x):
            continue
        for p in (page - 1, page, page + 1):
            for a, b in segs[f].get((part, p), []):
                k = text[f].find(s, a)
                while k >= 0 and k + len(s) <= b:
                    hits.append((f, k))
                    k = text[f].find(s, k + 1)
    return sorted(set(hits))


def in_italic(f, k):
    depth = collections.Counter()
    for m in re.finditer(r"\\(begin|end)\{([A-Za-z*]+)\}", text[f][:k]):
        env = m.group(2).rstrip("*")
        if any(env.startswith(x) for x in ITALIC):
            depth[env] += 1 if m.group(1) == "begin" else -1
    return any(v > 0 for v in depth.values())


def upright_labels(f, k):
    t = text[f]
    b = t.rfind("\\begin{enumerate}", 0, k)
    if b < 0 or t.rfind("\\end{enumerate}", b, k) >= 0:
        return False
    opts = re.match(r"\\begin\{enumerate\}\s*(\[[^\n]*\])?", t[b:b + 200])
    return bool(opts and opts.group(1) and re.search(r"\\(rm|textup|upshape|normalfont)", opts.group(1)))


def kind(old, new):
    e_old, e_new = old.count(BS + "emph"), new.count(BS + "emph")
    u_old, u_new = old.count(BS + "textup"), new.count(BS + "textup")
    if u_new > u_old:
        return "textup+"
    if e_new > e_old:
        return "emph+"
    if e_new < e_old:
        return "emph-"
    if e_new == e_old and e_new > 0 and old != new:
        return "emph~"
    return "other"


paths = sorted(HERE.glob(f"decisions_{edition}_*.json"))
alldec = {}
for path in paths:
    for d in json.loads(path.read_text(encoding="utf-8")):
        alldec[int(d["id"])] = d
doubt, clean, stats = [], [], collections.Counter()
for path in paths:
    for d in json.loads(path.read_text(encoding="utf-8")):
        i = int(d["id"])
        x = meta.get(i)
        if not x:
            stats["unknown id"] += 1
            continue
        if not has_target(edition, x):
            stats["no target (EGA III-2)"] += 1
            continue
        part, page = x["part"], int(x["page"])
        k = kind(x["old"], x["new"])
        dec = d.get("decision")
        why = None
        old = (d.get("en_old") or "").replace("\r\n", "\n")
        if dec == "apply":
            if len(find(part, page, old, x)) != 1:
                why = "apply: en_old not found exactly once on pages p-1..p+1"
        elif dec == "already":
            hits = find(part, page, old, x) if old else []
            cov = re.search(r"covered by (\d+)", d.get("note") or "")
            if cov and (alldec.get(int(cov.group(1))) or {}).get("decision") == "apply":
                why = None
            elif not hits:
                why = "already: en_old missing or not found"
            elif k == "emph+" and BS + "emph" not in old:
                why = "already: the fix adds an emphasis but the quoted Spanish has none"
            elif k == "emph-" and BS + "emph" in old:
                why = "already: the fix removes an emphasis but the quoted Spanish has one"
            elif k == "textup+" and not re.search(r"\\(textup|rm\b|upshape|emph)", old):
                f0, k0 = hits[0]
                # \sref and \eref print upright (\normalfont) in II, III1, IV3 and IV4, not in III2 and IV1
                upright_ref = re.search(r"\\[se]ref\b", old) and rel(f0).split("/")[0] in UPRIGHT_REF_TREES
                if not upright_ref and in_italic(f0, k0) and not upright_labels(f0, k0):
                    why = "already: the fix sets text upright, the quoted Spanish has no upright markup and is inside an italic statement"
        elif dec == "not_applicable":
            if k in ("emph+", "emph-", "textup+", "emph~"):
                why = f"not_applicable for a {k} fix"
        else:
            why = f"decision {dec!r}"
        stats[(dec, "doubtful" if why else "ok")] += 1
        if why:
            doubt.append({"id": i, "batch": path.stem, "part": part, "page": page, "kind": k, "fr_old": x["old"],
                          "fr_new": x["new"], "decision": dec, "en_file": d.get("en_file"), "en_old": d.get("en_old"),
                          "en_new": d.get("en_new"), "note": d.get("note"), "why": why})
        else:
            clean.append(d)
(HERE / f"doubtful_{edition}.json").write_text(json.dumps(doubt, ensure_ascii=False, indent=1), encoding="utf-8")
(HERE / f"clean_{edition}.json").write_text(json.dumps(clean, ensure_ascii=False, indent=1), encoding="utf-8")
L = [f"# Audit of Sol's decisions, Spanish EGA ({edition})", "", f"{len(paths)} decision files", "",
     "| decision | ok | doubtful |", "|---|---:|---:|"]
for dec in ("apply", "already", "not_applicable", "unclear", None):
    L.append(f"| {dec} | {stats[(dec, 'ok')]} | {stats[(dec, 'doubtful')]} |")
L += ["", f"Skipped, no Spanish target (EGA III-2 in the diplomatic edition): {stats['no target (EGA III-2)']}",
      f"Doubtful by reason: {dict(collections.Counter(d['why'] for d in doubt))}", ""]
for d in doubt:
    L += [f"## {d['id']} ({d['part']} {d['page']}, {d['kind']}, {d['batch']}): {d['why']}",
          f"FR: {d['fr_old']!r} -> {d['fr_new']!r}", f"Sol: {d['decision']} | es_old {d['en_old']!r} | es_new "
          f"{d['en_new']!r} | note {d['note']!r}", ""]
(HERE / f"AUDIT_{edition}.md").write_text("\n".join(L), encoding="utf-8")
print("\n".join(L[:12]))
