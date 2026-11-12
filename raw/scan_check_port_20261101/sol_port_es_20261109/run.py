"""Carry the French EGA fixes into the Spanish EGA with OpenAI GPT-6.1 Sol (effort high, Flex tier), batch by batch,
at most CONCURRENCY at a time; answers in answer_<batch>.md and decisions_<batch>.json; each decisions file is
dry-run with apply.py. The prompt is the English hand-pass prompt (PORT_EN_AGENT_PROMPT.txt, as run for the English
on 9 Nov) rewritten for the Spanish edition, with the italic-statement rule and en_old for "already".
usage: python -I run.py current|diplomatic [CONCURRENCY=4]
The API key is read from the user's note at run time by enr_pilot.key() and never printed or stored."""
import json
import os
import re
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"user\Documents\enriques_api_pilot_20261106")
import enr_pilot as P  # noqa: E402

PROMPT = r"""You carry corrections from the French EGA into the Spanish EGA.

The French EGA was checked page by page against the printed original (Publ. Math. IHÉS); every correction is an
exact edit OLD -> NEW of the French LaTeX. The Spanish EGA is a translation of the French, made before these
corrections. The corrections in your batch could not be carried over by a script, mostly because the French wording
differs from the Spanish.

Your batch is below, between BEGIN BATCH and END BATCH. It has one block per printed page: "=== PAGE <part> <page>
===", then the Spanish text of that page and of its neighbours ("----- Spanish, <file>, page <part> <p> -----": the
translation's page breaks fall a few lines differently, so the passage can sit on the page before or after), then the
French corrections of that page: "[id N]", OLD, NEW and, where found, FRENCH CONTEXT (the corrected French around the
edit).

For each id decide:
- "apply": the Spanish has the error that the French fix corrects. Give an exact Spanish edit: "en_file" (as named
  in the block), "en_old" (an exact substring of that Spanish text, long enough to occur only once in the Spanish
  pages of the block) and "en_new" (the corrected Spanish). Carry over the meaning of the fix: a corrected formula,
  index, sign, reference, number or letter; a missing or wrong word (translated into Spanish, never pasted in French);
  an italic emphasis \emph{...} restored on a defined term or an emphasized phrase (put it on the Spanish words that
  translate the French ones); an upright parenthesis \textup{(...)} inside an italic statement (proposition, theorem,
  corollary, lemma) where the Spanish has the same parenthesis; a missing or wrong parenthesis, bracket or punctuation
  mark that belongs to the mathematics or the meaning.
- "already": the Spanish already says what the corrected French says.
- "not_applicable": the fix concerns only the French: spelling, accents, French punctuation or spacing (spaces
  before ; : ! ?, guillemets), grammar, a French line or page break, blank lines, a display set inline or the reverse,
  or another layout choice of the French print that the Spanish does not follow.
- "unclear": you cannot find the passage or are not sure; say why in "note".

Rules:
- Mathematics must end up identical to the corrected French: same symbols, indices, references and numbering.
- Keep the Spanish edition's conventions and macros where they render the same as the French, and its spelling and
  typography (Spanish quotation marks, decimal commas, etc., as the file uses).
- If the Spanish writes references with its own macros and they already render the corrected French typography (bold
  chapter numbers, upright references), the fix is "already".
- Never change \oldpage markers, \label or \hyperref/\sref keys, or file structure.
- If one Spanish edit covers several ids, put it in the first and give the others "already" with note
  "covered by <id>". No two "apply" edits may overlap.
- Italic statements: everything inside a proposition, theorem, corollary or lemma environment is italic, including its
  enumerate items and the parentheses that contain references; \sref and \hyperref make only the reference itself
  upright, not the text around it. When the French fix sets a parenthesis or label upright there, the Spanish needs
  \textup{...} on the same parenthesis or label, unless the Spanish already prints it upright (\textup, \rm, \upshape,
  or \emph inside the italic statement).
- Use LF line breaks (\n) in en_old and en_new, exactly as in the Spanish text shown.

Answer with one fenced block ```json containing one JSON list, one object per id, in the batch's order:
  {"id": N, "decision": "apply"|"already"|"not_applicable"|"unclear", "en_file": ..., "en_old": ..., "en_new": ...,
   "note": "..."}
("en_file" and "en_old" for "apply" and "already", "en_new" only for "apply"; "note" short, and only where useful).
Every id of the batch gets exactly one object. For "already", "en_old" is the exact Spanish text (occurring once in
the Spanish pages of the block) that already says what the corrected French says, so that the decision can be checked.
After the block, one line each: any place where the Spanish translation itself is wrong in a way the French fix does
not cover (do not fix those). Nothing else.
"""


SECOND = ("\nSECOND LOOK. Every id in this batch was answered once already, and a mechanical check questioned that "
          "answer: each id shows FIRST ANSWER and QUESTIONED BECAUSE. Read the French fix and the Spanish again and "
          "decide afresh (the first answer may still be right; say why in the note).\n")


def submit(edition, name, tag=None, effort="high"):
    text = open(os.path.join(HERE, f"batches_{tag or edition}", name + ".txt"), encoding="utf-8").read()
    body = {"model": "gpt-6.1-sol", "input": PROMPT + (SECOND if tag else "") + "\nBEGIN BATCH\n" + text + "\nEND BATCH\n",
            "reasoning": {"effort": effort}, "max_output_tokens": 128000, "background": True, "service_tier": "flex"}
    code, r = P.call("POST", P.API, body)
    return code, r.get("id"), r.get("error")


def finish(edition, name, r):
    text = "".join(c.get("text", "") for o in r.get("output", []) if o.get("type") == "message"
                   for c in o.get("content", []))
    open(os.path.join(HERE, f"answer_{name}.md"), "w", encoding="utf-8").write(text)
    m = re.search(r"```json\s*\n(.*?)```", text, re.S)
    ok = False
    if m:
        try:
            lst = json.loads(m.group(1))
            json.dump(lst, open(os.path.join(HERE, f"decisions_{name}.json"), "w", encoding="utf-8"), ensure_ascii=False,
                      indent=1)
            ok = True
        except ValueError as e:
            print(name, "JSON error", e, flush=True)
    u = r.get("usage") or {}
    usd = (u.get("input_tokens", 0) * 2 + u.get("output_tokens", 0) * 10) / 1e6 / 2
    dry = ""
    if ok:
        res = subprocess.run([sys.executable, "-I", os.path.join(HERE, "apply.py"), edition,
                              os.path.join(HERE, f"decisions_{name}.json"), "--dry"], capture_output=True, text=True,
                             encoding="utf-8")
        dry = (res.stdout.strip().splitlines() or [res.stderr.strip()[-300:]])[0]
    return ok, round(usd, 4), dry


def run(edition, conc, tag=None, effort="high"):
    sp = os.path.join(HERE, f"state_{tag or edition}.json")
    st = json.load(open(sp, encoding="utf-8")) if os.path.exists(sp) else {}
    index = json.load(open(os.path.join(HERE, f"batches_{tag or edition}", "BATCHES.json"), encoding="utf-8"))
    todo = [b["batch"] for b in index if not os.path.exists(os.path.join(HERE, f"decisions_{b['batch']}.json"))]
    flying = {n: v["id"] for n, v in st.items() if v.get("status") == "submitted" and n in todo}
    queue = [n for n in todo if n not in flying]
    while queue or flying:
        while queue and len(flying) < conc:
            n = queue.pop(0)
            code, rid, err = submit(edition, n, tag, effort)
            if code >= 300 or not rid:
                print(n, "submit failed", code, json.dumps(err)[:200], flush=True)
                time.sleep(30)
                queue.append(n)
                continue
            flying[n] = rid
            st[n] = {"status": "submitted", "id": rid, "t": time.time(), "tries": st.get(n, {}).get("tries", 0) + 1}
            json.dump(st, open(sp, "w", encoding="utf-8"), indent=1)
        time.sleep(45)
        for n, rid in list(flying.items()):
            code, r = P.call("GET", f"{P.API}/{rid}")
            s = r.get("status")
            if s in ("queued", "in_progress"):
                continue
            del flying[n]
            if s == "completed":
                ok, usd, dry = finish(edition, n, r)
                st[n].update(status="done" if ok else "bad_answer", usd=usd, dry=dry,
                             minutes=round((time.time() - st[n]["t"]) / 60, 1))
                print(n, st[n]["status"], f"${usd}", st[n]["minutes"], "min |", dry, flush=True)
            else:
                st[n].update(status=s)
                print(n, s, flush=True)
                if st[n]["tries"] < 3:
                    queue.append(n)
            json.dump(st, open(sp, "w", encoding="utf-8"), indent=1)
    cost = sum(v.get("usd") or 0 for v in st.values())
    print(edition, "done; cost", f"${cost:.2f}", flush=True)


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    o = dict(x[2:].split("=", 1) for x in sys.argv[1:] if x.startswith("--") and "=" in x)
    # second look (9 Nov): python -I run.py current 4 --tag=second_current --effort=max
    run(a[0], int(a[1]) if len(a) > 1 else 4, o.get("tag"), o.get("effort", "high"))
