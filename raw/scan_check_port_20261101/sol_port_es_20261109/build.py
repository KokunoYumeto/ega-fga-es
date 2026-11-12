"""Write the Spanish port batches for one edition: per printed page, the Spanish text of the page and its neighbours,
then the French fixes of that page (OLD, NEW, the corrected French context). Items whose page has no Spanish text in
the edition's trees are left out (listed in no_target_<edition>.json). Pages are never split across batches.
usage: python -I build.py current|diplomatic [ITEMS_PER_BATCH=150]"""
import collections
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from common import BS, E, HERE, load_tree, rel, items  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith("--")]
opts = dict(a[2:].split("=", 1) for a in sys.argv[1:] if a.startswith("--") and "=" in a)
edition = args[0]
per = int(args[1]) if len(args) > 1 else 150
# second look (9 Nov): --only=doubtful_<edition>.json restricts the items and shows each first answer and why it
# was questioned; --tag=NAME names the batch folder (batches_NAME) and the batches (NAME_001, ...)
ONLY = {int(d["id"]): d for d in json.load(open(HERE / opts["only"], encoding="utf-8"))} if "only" in opts else None
TAG = opts.get("tag", edition)
tree = load_tree(edition)
FR = E / "ega-fr" / "editions" / "2026-10-24-r20" / ("current" if edition == "current" else "diplomatic") / "packages"
fr = {}
for f in sorted(FR.glob("*/native/**/*.tex")):
    fr[f] = f.read_text(encoding="utf-8", errors="replace")


def es_page(part, page):
    res = []
    for f, (t, segs) in tree.items():
        for s, e in segs.get((part, page), []):
            res.append((rel(f), t[s:e]))
    return res


def fr_context(new, width=260):
    if not new.strip():
        return None
    for f, t in fr.items():
        k = t.find(new)
        if k >= 0:
            return t[max(0, k - width):k + len(new) + width]
    return None


its = items(edition)
bypage = collections.defaultdict(list)
no_target = []
for x in its.values():
    if ONLY is not None and x["entry"] not in ONLY:
        continue
    p = (x["part"], int(x["page"]))
    if any(es_page(p[0], q) for q in (p[1] - 1, p[1], p[1] + 1)):
        bypage[p].append(x)
    else:
        no_target.append(x["entry"])
PARTS = ["0" + BS + "textsubscript{I}", "I", "II", "0" + BS + "textsubscript{III}", "III", "IV",
         "0" + BS + "textsubscript{IV-1}", "IV-1", "IV-2", "IV-3", "IV-4"]
keys = sorted(bypage, key=lambda k: (PARTS.index(k[0]) if k[0] in PARTS else 99, k[1]))
batches, cur, n = [], [], 0
for k in keys:
    if cur and n + len(bypage[k]) > per:
        batches.append(cur)
        cur, n = [], 0
    cur.append(k)
    n += len(bypage[k])
if cur:
    batches.append(cur)
out = HERE / f"batches_{TAG}"
out.mkdir(exist_ok=True)
index = []
for b, ks in enumerate(batches, 1):
    name = f"{TAG}_{b:03d}"
    lines = [f"# Spanish hand pass, {name}: {sum(len(bypage[k]) for k in ks)} items on {len(ks)} printed pages", ""]
    shown, ids = set(), []
    for part, page in ks:
        lines.append(f"=================== PAGE {part} {page} ===================")
        for p in (page - 1, page, page + 1):
            if (part, p) in shown:
                lines.append(f"----- (Spanish page {part} {p}: shown above in this file) -----")
                continue
            shown.add((part, p))
            for fname, txt in es_page(part, p):
                lines.append(f"----- Spanish, {fname}, page {part} {p} -----")
                lines.append(txt.rstrip("\n"))
        lines.append(f"----- French corrections on page {part} {page} -----")
        for x in bypage[(part, page)]:
            ids.append(x["entry"])
            lines += [f"[id {x['entry']}]", "OLD: " + x["old"], "NEW: " + x["new"]]
            ctx = fr_context(x["new"])
            if ctx:
                lines.append("FRENCH CONTEXT (corrected): " + ctx)
            if ONLY is not None:
                d = ONLY[x["entry"]]
                lines.append(f"FIRST ANSWER: {d.get('decision')}; es_old {d.get('en_old')!r}; es_new {d.get('en_new')!r}; "
                             f"note {d.get('note')!r}. QUESTIONED BECAUSE: {d.get('why')}")
            lines.append("")
    (out / f"{name}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="")
    index.append(dict(batch=name, items=len(ids), ids=ids))
(out / "BATCHES.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
(HERE / f"no_target_{TAG}.json").write_text(json.dumps(no_target), encoding="utf-8")
sizes = [(out / f"{x['batch']}.txt").stat().st_size for x in index]
print(edition, len(index), "batches;", sum(x["items"] for x in index), "items;", len(no_target), "without Spanish text;",
      "KB min/max/mean", min(sizes) // 1024, max(sizes) // 1024, sum(sizes) // len(sizes) // 1024)
