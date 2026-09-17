# Reply-drafter subagent brief

Used by the main triage agent to spin up a subagent for **drafting the
customer-facing reply only**, once the main agent has already looked up the
account tier and selected the policy/KB clause. This is the pattern run in
Lab 4, Step 2 and Step 4.

## Division of labour

- **Main agent** reads the ticket, looks up the real plan tier in
  `accounts.csv` (never trusts the ticket's own `plan` field), decides what
  kind of problem it is, and selects the exact `[REF-xx]` clause that
  applies.
- **Subagent** never sees any of that process. It receives three inputs and
  writes the reply.

## What to pass the subagent — exactly these three things

1. **Ticket text** — subject + description only. Not the raw CSV row, not
   the ticket ID's history, not other tickets from the same customer.
2. **Plan tier** — the value from `accounts.csv`, as a plain string (e.g.
   `Growth`, `Starter (monthly)`). Never the ticket's own `plan` field.
3. **The clause** — the exact `[REF-xx]` text the main agent selected,
   quoted in full. One clause (or the small set that together answer the
   ticket) — not the whole doc it came from.

Do **not** pass: the docs folder, `accounts.csv`, `tickets_raw.csv`, this
conversation, or any other ticket. If a shortcut means drafting it yourself
instead of actually spawning a subagent, say so out loud — never present a
self-drafted reply as if a subagent produced it.

## Subagent prompt template

```
You are a customer support reply writer. You have exactly three inputs
below and nothing else — no other policy documents, no CSV files, no other
context. Write a short, warm, professional customer-facing reply. Cite the
clause ID given wherever you state a policy or documented fact. Do not
invent any other policy or fact.

TICKET TEXT:
Subject: <subject>
Description: <description>

PLAN TIER: <tier from accounts.csv>

POLICY/KB CLAUSE:
[REF-xx] <full clause text>

Write the draft reply now.
```

## After the draft comes back

The subagent's draft is not automatically final. Run it through the gate
(CLAUDE.md rule 4) before it reaches a customer:

- Refund request → human review, always, regardless of how clean the
  drafted answer is.
- Severity Critical → human review.
- Account is Enterprise → human review.
- Required information missing from the ticket → human review.

A ticket can clear all four literal gate checks and still deserve a human
look — e.g. a plan/tier mismatch between the ticket and `accounts.csv`, or a
customer using a feature their real plan doesn't include. The gate catches
refund asks reliably; it does not yet catch every case where the customer is
outside their entitlements without asking for money back. Flag these
explicitly rather than letting a clean gate pass stand in for "safe to
send."

## Known good / known bad from Lab 4

- Good: a subagent given only REF-KB-03 wrote about Slack token refresh and
  reconnect order, and did not wander into refund policy or other
  integrations it wasn't given.
- Good: subagents given a refund clause requiring human confirmation
  (REF-RP-04) correctly wrote the reply as pending, not final, without being
  told to.
- Watch for: a tighter, more clause-faithful draft can still be a *worse*
  reply if the main agent needed something in the reply that wasn't in the
  three inputs (e.g. a clarifying question) — brevity from constrained
  context isn't automatically better.
