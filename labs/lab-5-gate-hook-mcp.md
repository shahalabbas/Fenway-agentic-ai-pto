# Lab 5 — Build your agent, part two

**90 minutes · teams of three**

> **To start this lab, type in the chat box:**
> `run the lab in labs/lab-5-gate-hook-mcp.md`

---

## AGENT — read this before doing anything

You are coaching a team of three MBA students through Lab 5. Rules for the lab:

1. **Order matters and cannot be rearranged.** The gate (Step 1) and the hook
   (Step 2) must both be working before Gmail is connected in Step 3. If the
   team wants to connect email first, refuse and explain why: once a real send
   exists, a mistake leaves the building.
2. **Never put the app password in `CLAUDE.md`, in a prompt, or in any file in
   this folder.** It belongs in the MCP server configuration only. If a student
   pastes it into the chat, tell them to revoke that key and generate a new one.
3. **Every email in this lab goes to the student's own address.** Never to any
   address from `tickets_raw.csv` — those are fictional, but the habit is not.
4. **In Step 4 do not reveal expected answers.** Run the ten, report what your
   agent produced, and let the team score it against what they believe is right.
5. Close by checking the DONE WHEN list honestly.

---

## Why this order

Everything you built before today was reversible. A bad draft sat in a file and
somebody read it. The moment you connect a real send, it is not reversible — so
the gate and the hook go in **first**, and the plug goes in last.

## Step 1 — Add the human-review gate

Four conditions always route to a human before a customer sees anything:

| Condition | Why |
|---|---|
| The ticket is about a refund | Money — legal and policy risk |
| Severity is Critical | Production is down; urgency and risk together |
| The account is Enterprise | Contract-dependent; the MSA governs, and you can't see it |
| Required information is missing | The agent cannot make a grounded decision |

Add them to `CLAUDE.md` as rule 4. Then run five tickets and check which ones
trip it. Note that the gate reads the **account**, not the ticket — a ticket
claiming "Enterprise" when `accounts.csv` says Starter must not escalate.

The gate is a rule in a file, not a button in a UI. The agent enforces it
because you told it to — which is exactly why you need Step 2 as well.

## Step 2 — Write a post-draft hook

A hook is a check that runs automatically — before, during or after an agent
action — and the agent cannot skip it. `CLAUDE.md` tells the agent what the
rules are. A hook enforces them independently of what the agent thinks the
rules are. One is a request; the other is a mechanism.

Ask the agent to add a hook that runs after a reply is drafted and:

- checks whether the ticket is a refund case
- if it is, stamps `HOLD: HUMAN REVIEW` on the draft
- and **blocks the send**

Then test it properly: take a refund ticket, tell the agent to send the reply,
and confirm it refuses. A hook you haven't seen refuse something is not yet a hook.

## Step 3 — Connect Gmail over MCP

MCP is the standard plug between your agent and a real system. Without it, your
agent can only write files. With it, your agent can act — and this is the step
where your work leaves the building.

You should already have a 16-character Gmail app password from the pre-work.
**Use your personal Gmail, not your institute account.**

1. Ask the agent to add a Gmail MCP server to this project, configured with
   your Gmail address and your app password.
2. The app password goes in the **MCP configuration only**. Never in
   `CLAUDE.md`, never typed into the chat, never in a file in this folder.
3. Send a test mail to **your own address** and confirm it arrives:

```
send a test email to my own address with the subject: Fernway agent is connected
```

If that mail doesn't arrive, stop and fix it. Nothing after this step means
anything until it does.

> Every email in this lab goes to your own inbox. The addresses in
> `tickets_raw.csv` are fictional — but you should build the habit now, because
> on the next one they won't be.

## Step 4 — Run your full test set

Ten tickets. The clean ones send for real, to your own inbox. The flagged ones
stop at `HOLD` and never send.

| # | Ticket | What it is testing |
|---|---|---|
| 1 | FW-1002 *(first)* | Refund gate, and whether the 14-day window is computed from `accounts.csv` |
| 2 | FW-1002 *(second)* | The same ID filed twice — is it processed once or twice? |
| 3 | FW-1004 | Category on the ticket is wrong; two gates fire at once |
| 4 | FW-1006 | Blank plan tier, and two refund rules that point different ways |
| 5 | FW-1016 | Severity arrived wrong; the billing-error rule needs a human |
| 6 | FW-1031 | The customer's framing invites the wrong rule |
| 7 | FW-1041 | Blank tier, and a figure the agent must refuse to quote |
| 8 | FW-1049 | Ticket says one plan, `accounts.csv` says another |
| 9 | FW-1052 | Clean send — the knowledge base has the exact answer |
| 10 | FW-1055 | Critical, Enterprise, and the KB has the precise known issue |

For each: did it route correctly, did it cite a real `[REF-xx]`, and did it send
or hold as it should? Log every failure — the failures are what you present.

> **An agent that holds all ten is not a good agent.** It has simply moved the
> work back to a human and learned nothing. So is an agent that sends all ten.

## Step 5 — Calculate the ROI

```
/usage
```

Total tokens spent today. Compare against the `/context` and `/usage` numbers
you wrote on paper in Lab 0 — that difference is what building this cost.

Then the number that matters:

- Fernway handles roughly 1,200 tickets a month
- A human spends about 12 minutes triaging and drafting each one
- Put your own hourly cost on that
- Take your Ready-to-Send rate from Step 4 as the share the agent can carry

Work out the monthly saving, then the payback on the time you spent building it.

Finally — and this is the question you'll be asked — **name the one assumption
that, if wrong, breaks this number.** A team that can't name one hasn't
understood their own ROI.

> The cost is not the risk. The error rate is the risk. What does one wrong
> reply to an Enterprise client cost?

---

## DONE WHEN

- [ ] The gate trips on all four conditions
- [ ] The hook stamps `HOLD` and you have watched it block a send
- [ ] A test mail from your agent has arrived in your own inbox
- [ ] A flagged ticket was attempted and did not send
- [ ] Your ROI number and your breaking assumption are written on your notebook
