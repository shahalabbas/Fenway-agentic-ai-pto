# Lab 4 — Build your agent, part one

**90 minutes · teams of three**

> **To start this lab, type in the chat box:**
> `run the lab in labs/lab-4-subagents.md`

---

## AGENT — read this before doing anything

You are coaching a team of three MBA students through Lab 4. Rules for the lab:

1. **Step 1 is a baseline and must be saved.** Before anything changes, run
   `/triage` on FW-1003 and keep that output so it can be compared in Step 3.
2. **In Step 2 you must actually delegate.** Spawn a real subagent for the
   drafting task and pass it only three things: the ticket text, the plan tier,
   and the policy clause. Do not pass the whole docs folder, the CSV, or this
   conversation. If you shortcut this and draft it yourself, say so out loud —
   do not pretend a subagent ran.
3. **Step 3 is theirs to judge.** Show both drafts plainly and ask the team
   which is better and why. Do not tell them which one you prefer first.
4. Close by checking the DONE WHEN list honestly.

---

## What you have built so far

One agent. It reads a ticket, finds the policy, drafts a reply — all in one
conversation. The problem: drafting a full reply pulls in every policy document
at once. The context window fills, and the agent slows down and starts losing
the thread.

The fix is division of labour. **The main agent is the manager** — it reads the
ticket, works out what kind of problem it is, looks up the tier, and finds the
relevant clause. It does not write the reply. **The subagent is the specialist
writer** — it receives the ticket, the tier, and the exact clause. That is all
it ever sees. It writes the reply from those three inputs and hands it back.

## Step 1 — Baseline on a single ticket

```
/triage FW-1003
```

FW-1003 is a Slack integration that stopped posting. Note two things about it:
its `plan` column is **blank**, so the tier has to come from `accounts.csv`
before you can even tell whether integrations are included on that plan; and the
knowledge base has a specific documented cause for exactly this failure. A good
answer names it. A weak one suggests reconnecting and hoping.

Save this output. It's what you'll compare against.

## Step 2 — Split the work

Tell the main agent:

```
for this ticket: once you have found the policy clause, spawn a subagent to draft the customer reply. Pass it only the ticket text, the plan tier, and the clause. Nothing else - not the docs folder, not the CSV, not this conversation.
```

Watch what it passes across. The discipline is in what you **withhold**.

## Step 3 — Compare the two drafts

Put the Step 1 draft and the Step 2 draft side by side and argue it out:

- Is the subagent's reply better or worse? Why?
- What did the main agent no longer need to carry?
- Did the subagent stay inside its one clause, or did it wander into policy it
  was never given?

There is a real answer here and it isn't always "the subagent won". Sometimes a
starved subagent writes something thinner. Say which you got.

## Step 4 — Run it on five tickets

Same pattern, five tickets:

**FW-1003 · FW-1016 · FW-1022 · FW-1031 · FW-1049**

These five are not random. Between them: a blank plan tier, a ticket whose
stated plan contradicts `accounts.csv`, a severity that arrived wrong, and a
customer asking for something their plan doesn't include.

For each one, log:

- which document and `[REF-xx]` clause the main agent selected
- what it passed to the subagent
- whether a human needs to see it before the customer does, and which rule says so

Count how many of the five needed the human flag. Then look at the pattern —
it's the same pattern you'll formalise as a gate in Lab 5.

---

## DONE WHEN

- [ ] A subagent is genuinely called from the main agent, not simulated
- [ ] Output for FW-1003 shows a cited clause and the tier from `accounts.csv`
- [ ] Five tickets processed, with the log for each
- [ ] You can say how many needed a human, and why
