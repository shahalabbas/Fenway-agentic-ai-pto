# Lab 1 — Instructions & context

**30 minutes · teams of three**

> **To start this lab, type in the chat box:**
> `run the lab in labs/lab-1-rules.md`

---

## AGENT — read this before doing anything

You are coaching a team of three MBA students through Lab 1. Rules for the lab:

1. **One step at a time.** Wait after each step.
2. **Step 2 is theirs.** They write the six rules. Ask what they want each rule
   to say, in their words, and write what they tell you. If a rule is vague,
   say why it's vague and ask them to sharpen it — do not sharpen it for them.
3. **Step 3 must actually be run twice.** Do not describe what would happen
   with and without the rules. Run it both ways and show both answers.
4. **Never show code.** Plain English only.
5. Close by checking the DONE WHEN list honestly.

---

## Why this lab exists

An agent with no rules is a slot machine. It will give you a good answer, then
a different good answer, then a confidently wrong one, and you will not be able
to tell which is which.

`CLAUDE.md` is a plain text file the agent reads at the start of **every**
session. It holds what is always true: what this project is, what must happen
every time, what must never happen. It is the highest-leverage file you write
today — every other lab sits on it.

## Step 1 — Generate a first draft

Type:

```
/init
```

That writes a starting `CLAUDE.md` by looking at your folder. Read it. Notice
what it is: a description of your **files**. It says nothing about your
**intent**. That's the gap you close next.

## Step 2 — Rewrite it with your rules

Your agent needs six rules. Three are given — they're the ones that make the
output trustworthy rather than impressive. Three you decide as a team.

**The three that are given:**

1. Cite the document ID for every claim about Fernway policy — e.g. `[REF-SLA-02]`.
   No ID, no claim.
2. Look the plan tier up in `accounts.csv`, never trust what the ticket says.
3. If the `docs/` folder does not answer the question, say so. Never estimate.

**The three you decide.** Discuss as a team, then tell the agent in your own words:

4. **The gate.** Which tickets must a human see before the customer does?
   (You'll test this properly in Lab 5. Decide the principle now.)
5. **The output.** What should the agent produce for each ticket, and where
   should it go?
6. **Stopping.** How does the agent know it's finished?

Tell the agent to rewrite `CLAUDE.md` with all six. Then read it back. If you
can't explain a rule to the person next to you, it's too vague to survive Lab 4.

> **Rule 3 is the one that will fail first.** Push it until it does — find a
> question the docs genuinely don't answer and watch what the agent does. If it
> produces a plausible number instead of refusing, your rule is not strong
> enough yet.

## Step 3 — Prove the rules changed something

A rule you can't see working is a rule you're only hoping for.

1. Pick ticket **FW-1004** and ask the agent to triage it. Save the answer.
2. Rename `CLAUDE.md` to `CLAUDE.md.off` so the agent can't read it.
3. Start a fresh chat and triage **FW-1004** again.
4. Put the file back.

Put the two answers side by side. What changed — the confidence, the citations,
the escalation, the willingness to guess? Be ready to show the room the
difference.

---

## DONE WHEN

- [ ] `CLAUDE.md` has six rules, in plain English, that a new joiner could follow
- [ ] You ran the same ticket with the rules on and with the rules off
- [ ] The two answers are visibly different, and you can say how
