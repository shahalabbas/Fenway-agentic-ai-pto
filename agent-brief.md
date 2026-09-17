# Agent brief — Fernway reply-drafting subagent

Use this brief whenever the main agent spins up a subagent to draft a customer-facing
reply for a Fernway ticket. This is the pattern from Lab 4: the main agent is the
manager (reads the ticket, resolves the plan tier via `accounts.csv`, **re-derives
severity from `[REF-SLA-01]` rather than trusting the ticket's own field**, finds the
policy clause); the subagent is the specialist writer, and sees only what's below.

## Before delegating: verify severity, not just tier

CLAUDE.md rule 2 says never trust the ticket for plan tier — always resolve it via
`accounts.csv`. The same discipline applies to severity, per `sla-terms.md`:
*"Assigning the correct severity from the definitions above — not copying whatever
the customer wrote — is part of the triage job."* The main agent must check the
ticket's stated severity against the `[REF-SLA-01]` definition table before using it
anywhere (drafting, the gate, or an SLA response-time citation).

**Caught in the Lab 4 sample:** FW-1016 ("charged twice this month," a duplicate
charge) arrived tagged **High**, but `[REF-SLA-01]`'s own example table lists "an
individual billing discrepancy" — exactly this case — under **Medium**. The ticket's
own severity tag was wrong. It doesn't change the outcome here (FW-1016 is gated to a
human anyway, as a refund request), but a main agent that skips this check and
blindly trusts ticket severity elsewhere could let a true Critical slip through
mislabeled as something lower, or could over-escalate a Medium mislabeled High.

## What the subagent receives — nothing more

1. **Ticket text** — subject and description only.
2. **Plan tier** — the tier looked up in `accounts.csv`, never copied from the
   ticket's own `plan` field.
3. **The policy clause** — the single `[REF-xx]` clause the main agent selected,
   quoted in full.

Do **not** pass: the `docs/` folder, `tickets_raw.csv` / `tickets_clean.csv` /
`accounts.csv`, the surrounding conversation, or any other `[REF-xx]` clause not
selected as relevant. If the subagent needs more than these three things to do
its job, that's a sign the main agent picked the wrong clause or hasn't finished
triage yet — not a reason to hand over more context.

## Subagent instructions (paste as the task prompt)

```
You are a customer support reply writer. Do not use any tools — do not read any
files, do not explore any folder, do not look anything up. Work only from the
three inputs given below. Write a short, professional customer-facing reply.

TICKET TEXT:
<subject + description>

PLAN TIER: <tier from accounts.csv>

POLICY CLAUSE [REF-xx]: "<clause text>"

Write the customer-facing draft reply now, citing [REF-xx]. Output only the
reply text, nothing else.
```

**If the ticket is a refund request**, add this line to the prompt: *"This is a
refund request, so do NOT state a final approve/deny — state the applicable
policy finding and note it is pending human confirmation."* Per `[REF-RP-08]`,
no refund decision is final until a human confirms it, and the drafted reply
must not imply otherwise.

## Verifying the subagent actually ran clean

Check the returned run for `tool_uses: 0`. If it's nonzero, the subagent read
something beyond what it was handed — that's a discipline failure, not a detail
to wave past.

## The gate, unchanged from CLAUDE.md rule 4

Regardless of how good the draft is, route to human review before it reaches
the customer if any of the following is true:

- it's a refund request
- severity is Critical
- the account is on the Enterprise plan
- required information is missing from the ticket

In the Lab 4 sample (FW-1003, FW-1016, FW-1022, FW-1031, FW-1049), 2 of 5
needed a human — both because they were refund requests, not because of
severity or plan tier.

## Known gap this gate doesn't close

FW-1049 (Zapier auth error) doesn't trip any of the four literal gate
conditions above, but the account is really **Starter** (the ticket said
Growth — another `accounts.csv` contradiction) and Starter has no API access
per `[REF-KB-02]`. Zapier only works over the public API, so this customer
may be relying on something their real plan doesn't include. The gate as
written only reliably catches refund asks; it misses this "using something
outside your entitlements" pattern. Flag cases like this by hand until the
gate is extended — do not let "cleared the four checks" stand in for "safe
to send."
