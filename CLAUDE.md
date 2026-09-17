# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is not a software project — there is no code to build, lint, or test. It is a workshop
dataset and lab-instruction folder for "Fernway Support Triage," a hands-on exercise where the
agent is built up over a series of labs into a support-ticket triage assistant for a fictional
B2B SaaS company (Fernway).

## Running a lab

Labs live in `labs/lab-N-*.md` and are meant to be handed to the agent, not read and followed
by hand. When a user says "run the lab in labs/lab-N-*.md", open that file and follow the
"AGENT" instructions at the top of it exactly — these typically require going one step at a
time, waiting for the team's input at decision points, and not doing the team's thinking for
them. Each lab file's own instructions to the agent take precedence over general helpfulness
instincts (e.g. don't skip ahead or auto-complete steps even if the answer is obvious).

## Triage rules

These six rules govern any ticket-triage work in this repository. They apply every time,
regardless of which lab is active:

1. **Cite your sources.** Every claim about Fernway policy must carry the document ID it came
   from (e.g. `[REF-SLA-02]`). No ID, no claim.
2. **Trust `accounts.csv`, not the ticket.** Always look up the plan tier there. Never trust
   what the ticket itself says the plan is.
3. **Don't estimate.** If `docs/` doesn't answer the question, say so explicitly. Never produce
   a plausible-sounding number or policy in its place.
4. **The gate.** Route a ticket to human review if any of the following is true: it's a refund
   request, its severity is Critical, the account is on the Enterprise plan, or required
   information is missing from the ticket. **The Enterprise condition reads the account in
   `accounts.csv`, never the ticket's own `plan` field** — a ticket that claims "Enterprise"
   while `accounts.csv` says otherwise must not escalate on that basis alone.
5. **The output.** For each ticket, produce one row in `tickets_processed.csv` with columns:
   ticket ID, category, severity, draft reply, citation, and status.
6. **Stopping condition.** Processing is finished when every row in `tickets_processed.csv` has
   a status. Don't stop partway through the ticket set.

## Data model

- `tickets_raw.csv` — 55 support tickets exactly as exported from the helpdesk. Deliberately
  messy (inconsistent date formats, inconsistent casing/values, missing fields).
- `accounts.csv` — the 11 real customer accounts. This is the source of truth for plan/billing
  details; the ticket data often disagrees with it and the ticket is wrong when it does.
- `docs/refund-policy.md`, `docs/sla-terms.md`, `docs/product-knowledge-base.md` — policy
  references, each rule tagged with a stable ID (`[REF-RP-xx]`, `[REF-SLA-xx]`, `[REF-KB-xx]`).

**Grounding rule:** any policy claim the agent makes must cite one of these `[REF-xx]` IDs. If
no matching rule exists in `docs/`, the correct answer is "I cannot find this in policy," not a
plausible-sounding guess. Fernway is fictional — never source answers from general knowledge or
the web.

**Known issue:** five problems are intentionally planted in the ticket/account data (this is a
Lab 2 exercise). Do not silently "fix" data inconsistencies unless the active lab step asks for
it — finding them is the point.

## Later-lab artifacts

Subsequent labs cause the agent to create its own tooling in this repo; when working in a later
lab, expect and respect:
- `.claude/skills/<name>/SKILL.md` — skills such as `/triage` (Lab 3), each a folder containing
  a `SKILL.md` with `---`-delimited frontmatter (`name`, `description`).
- `.claude/agents/` — subagents (Lab 4), created by request rather than a slash command.
- Hooks and an MCP server wiring (Lab 5), plus a real Gmail send using an app password.
