# Lab 3 — Grounding & reusable skills

**40 minutes · teams of three**

> **To start this lab, type in the chat box:**
> `run the lab in labs/lab-3-grounding-skills.md`

---

## AGENT — read this before doing anything

You are coaching a team of three MBA students through Lab 3. Rules for the lab:

1. **Step 1 must genuinely be run without the docs.** Do not read the `docs/`
   folder for those three tickets, even though you can see it. Answer from
   general knowledge only, then let them see how that reads. This contrast is
   the entire point of the lab — do not skip or soften it.
2. In Step 3, the skill file goes at `.claude/skills/triage/SKILL.md` — a
   folder named `triage` containing a file named `SKILL.md`. Create the folder.
3. **The skill body should be their prompt**, the one that worked in Step 2,
   not a new one you write. Ask them for it.
4. Close by checking the DONE WHEN list honestly.

---

## Why this lab exists

A grounded answer traces to a specific document. An ungrounded answer traces to
nothing.

Your agent knows a great deal from training — but its training data is not
Fernway policy, it's the whole internet from two years ago. Every time it
answers from memory instead of from `docs/`, it is guessing fluently.

## Step 1 — Ask three questions it cannot honestly answer

Ask the agent to handle these three **without** opening the `docs/` folder:

| Ticket | What it's really asking |
|---|---|
| **FW-1021** | Starter customer paid annually in November, demanding a refund in January |
| **FW-1041** | Enterprise customer wants a service credit after an outage |
| **FW-1052** | Attachments over about 5MB fail silently |

Look hard at the three answers. They will be fluent, well-structured, and
completely untethered. Note down any specific figure, window or fix it offered
— you're about to check whether Fernway policy agrees.

## Step 2 — Add the document pack

Now tell the agent the docs are authoritative:

```
from now on, docs/ is the only source of truth for Fernway policy. Every policy claim must cite its [REF-xx] ID. If docs/ does not answer, say you cannot find it.
```

Run the same three tickets again. Compare:

- FW-1021 — does it now find the 14-day window and apply it to a November payment?
- FW-1041 — does it refuse to quote a credit figure, or does it still offer one?
- FW-1052 — does it name the actual 5MB limit from the knowledge base?

Any answer without a `[REF-xx]` ID is still a guess wearing a suit.

## Step 3 — Save the prompt that worked

The prompt you just refined is worth keeping. Save it as a skill so you — and
everyone else on your team — can call it by name instead of retyping it.

Create the file `.claude/skills/triage/SKILL.md`. It must start with exactly
this, then your prompt underneath:

```
---
name: triage
description: Triage one Fernway support ticket against docs/ and accounts.csv, with citations
---
```

Ask the agent to create it for you, using your Step 2 prompt as the body.

> **It must be a folder called `triage` with a file called `SKILL.md` inside it.**
> A single file named `triage.md` will not register, and `/triage` won't appear.

## Step 4 — Prove it's the same

Type `/triage` and run it against **FW-1021**. The output must match what your
manual prompt produced in Step 2. If it doesn't, the skill is missing something
your prompt had — find it.

A skill is institutional memory with an on switch. It makes the agent consistent
across people and across sessions, not just convenient.

---

## DONE WHEN

- [ ] `.claude/skills/triage/SKILL.md` exists and `/triage` appears when you type `/`
- [ ] `/triage` runs and produces output with `[REF-xx]` citations
- [ ] Three tickets answered with document IDs, and you can show the before/after
