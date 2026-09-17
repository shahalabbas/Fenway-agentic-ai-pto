# Lab 0 — Setup & first loop

**15 minutes · teams of three, one laptop**

> **To start this lab, type in the chat box:**
> `run the lab in labs/lab-0-setup.md`

---

## AGENT — read this before doing anything

You are coaching a team of three MBA students through Lab 0. They are not
developers. Follow these rules for the whole lab:

1. **One step at a time.** Present a step, wait for them to do it, then move on.
   Never run ahead and complete several steps in one reply.
2. **Do not do their thinking.** Where the lab says the team decides something,
   ask them and wait for an answer. Do not suggest one and move on.
3. **Never show code** unless a step explicitly contains it. Plain English only.
4. **Keep replies short.** A few lines per step.
5. At the end, walk the DONE WHEN list item by item and say plainly which ones
   are met and which are not. Do not congratulate them on unmet items.

Start by greeting the team in one line and asking if all three are at the laptop.

---

## Step 1 — Open the folder

You should already be here: this chat has `fernway-triage` open. If the window
title or file list says something else, close it and open this folder.

## Step 2 — Start the meter

Type each of these and write the number down on paper, with the current time:

```
/context
```
```
/usage
```

You'll run both again at the end of the day. The difference is what the whole
build cost — and you can't reconstruct it later if you don't write it down now.

## Step 3 — First loop

Type this:

```
look at the files in this folder and tell me what Fernway is and what problem I am about to solve
```

Read what comes back. The agent went and read files before it answered — you
didn't paste anything in. **It chose which files to open.** That choosing is
what "agentic" means, and you just watched it happen.

## Step 4 — Form your team

Three people, one laptop. Decide now:

- who types for Lab 0
- who reads the outputs and challenges them
- who writes down decisions and surprises

Rotate the typist at each lab. Nobody watches all day.

---

## DONE WHEN

- [ ] Three people are around one folder
- [ ] Both numbers from `/context` and `/usage` are written on paper with a time
- [ ] The agent described this folder correctly — a support triage problem, 55 tickets,
      11 customer accounts, 3 policy documents
