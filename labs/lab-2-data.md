# Lab 2 — Data work as an agent task

**25 minutes · teams of three**

> **To start this lab, type in the chat box:**
> `run the lab in labs/lab-2-data.md`

---

## AGENT — read this before doing anything

You are coaching a team of three MBA students through Lab 2. Rules for the lab:

1. **Step 1 is a hunt, not a handout.** When they ask you to profile the data,
   report what you actually find. Do **not** tell them there are five planted
   problems and do not list them as "the five". Let them count.
2. **Do not clean anything during Step 1.** Profiling only.
3. In Step 2, clean exactly what they ask you to clean. If their instruction is
   ambiguous — for example they say "fix the plans" without saying what to do
   with the blank ones — stop and ask. The ambiguity is the lesson.
4. **Log every change.** Never silently fix something you weren't asked to fix.
5. Close by checking the DONE WHEN list honestly.

---

## Why this lab exists

You do not clean the data. You describe what clean means, and the agent does it.
Then you check the log.

The change log is the deliverable — not the clean file. The clean file is what
you use; the log is what you show an auditor when someone asks why a customer
got the answer they got.

## Step 1 — Profile, don't fix

Type:

```
profile tickets_raw.csv and list every data quality problem you find. Do not fix anything yet.
```

Read the report and count the distinct problems. Then push:

```
for each problem, how many rows are affected, and which ticket IDs?
```

> **Five problems are planted in this file on purpose.** They are the same five
> every real support or operations team carries. If you've found three, look
> harder — particularly at the columns you'd normally skim past, and at whether
> every row is really a different ticket.

## Step 2 — Clean it

Now tell the agent what clean means. Be specific — vague instructions produce
vague data:

```
clean the file and save it as tickets_clean.csv
```
```
write a change log to changes.md: every row you changed, what it was before, what it is now, and why
```

Where a fix isn't obvious, the agent should stop and ask you. If it doesn't
ask and you weren't sure either, that's a silent assumption now baked into
your data.

## Step 3 — Verify

Don't trust the summary. Check the file:

```
compare tickets_raw.csv and tickets_clean.csv. How many rows changed, and how many are unchanged?
```

An agent that says "done" is not the same as an agent that finished correctly.

## Step 4 — Surface the assumptions

```
list every assumption you made where information was missing, and what you would need in order to stop guessing
```

Then ask the team the question that matters:

> What would you have done differently if a missing plan tier meant the
> customer gets nothing?

That answer tells you where your rules need to be tighter — and it's the
question a real support lead will ask you in week one.

---

## DONE WHEN

- [ ] `tickets_clean.csv` exists
- [ ] `changes.md` lists at least 5 changed rows with a reason for each
- [ ] Your assumptions are written out, not just made
- [ ] You can name all five planted problems out loud
