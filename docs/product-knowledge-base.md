# Fernway Product Knowledge Base

Internal reference for support agents (human or AI). Use this to answer product and troubleshooting questions accurately — do not guess at behavior that isn't documented here.

## [REF-KB-01] What Fernway is

Fernway is a workflow and project management platform for operations and IT teams. Core building blocks:

- **Boards** — a visual workspace of tasks, organized into columns (e.g., To Do / In Progress / Done)
- **Tasks** — individual work items on a board, with assignees, due dates, attachments, and a description field
- **Workflows** — automation rules that act on tasks (e.g., "when a form is submitted, create a task and assign it")
- **Integrations** — connections to external tools that sync data in or out of Fernway

## [REF-KB-02] Plan tiers and what's included

| Feature | Starter | Growth | Enterprise |
|---|---|---|---|
| Boards & tasks | ✓ | ✓ | ✓ |
| Team size | Up to 25 users | Up to 200 users | Unlimited |
| Automations / Workflows | — | ✓ | ✓ |
| Integrations (Slack, Google Workspace) | — | ✓ | ✓ |
| API access | — | ✓ (rate-limited) | ✓ (higher limits) |
| SSO / SAML | — | — | ✓ |
| Custom fields | — | — | ✓ |
| Dedicated CSM | — | — | ✓ |

**Note for support agents:** if a Starter customer reports an issue with automations, integrations, or SSO, the first thing to check is whether the feature is even included in their plan — this is a very common source of confused tickets (see FW-1024, a Starter customer asking for a feature that requires Enterprise).

## [REF-KB-03] Known integrations

- **Slack** — posts board/task updates to a designated channel. Common failure modes: notifications silently stop after a Slack workspace token refresh, or notifications duplicate if the integration is reconnected without first disconnecting the old link.
- **Google Workspace** — two-way sync with Google Calendar for task due dates. Common failure mode: duplicate tasks appear if the same calendar is connected to more than one Fernway board.
- **Zapier** — supported on a best-effort basis via our public API. Not officially covered by SLA response times, since it's a third-party integration path, but agents should still log the issue and escalate to engineering if it looks like our API is at fault.

## Common troubleshooting topics

**[REF-KB-04] SSO / SAML login loops (Enterprise only):** almost always caused by a misconfigured redirect URL on the identity provider (Okta, Azure AD, etc.) side, not a Fernway-side bug. Standard response: ask the customer's IT admin to verify the SAML redirect URL matches exactly what's in their Fernway Enterprise settings, and offer a screen-share with our solutions engineering team if it persists after that check.

**[REF-KB-05] Password reset emails not arriving:** check spam/junk first. If still missing after that, it is sometimes a corporate email filter blocking mail from our sending domain — advise the customer's IT team to allowlist mail from fernway-app.com.

**[REF-KB-06] CSV export showing garbled characters:** almost always a character encoding issue on the customer's end when opening in certain spreadsheet software. Recommend re-opening the exported file with UTF-8 encoding explicitly selected on import.

**[REF-KB-07] Slow board load times:** boards with 250+ tasks and heavy attachment use can load slowly. This is a known scaling limitation, not a bug. Recommend archiving completed tasks older than 90 days to improve load time; a permanent fix is on the roadmap but has no committed date.

**[REF-KB-08] Attachments failing to upload silently:** the per-file upload limit is 5MB. Files over this limit currently fail without a visible error message to the user — this is a known gap the product team is aware of. Confirm file size with the customer as the first troubleshooting step.

**[REF-KB-09] Workflow / automation not triggering:** most common cause is a condition in the workflow rule that no longer matches (e.g., a form field was renamed after the workflow was built). Ask the customer to re-check the trigger condition against the current form fields.

**[REF-KB-10] Approval steps disappearing from a custom workflow (Enterprise):** if a workflow is edited by more than one admin around the same time, the last save can silently overwrite an approval step added by someone else. This is a known conflict-resolution gap in the workflow editor. Advise the customer to have only one admin edit a given workflow at a time until this is fixed, and escalate to engineering if it's actively blocking task completion — this can become a Critical-severity issue if it blocks all task completions company-wide.

## [REF-KB-11] What agents should NOT do

- Do not promise a specific bug-fix date. Say "the team is aware and it's on the roadmap" if there's no committed date.
- Do not confirm SLA credit amounts without checking `sla-terms.md` — the credit calculation depends on the customer's plan tier and the specific outage duration.
- Do not approve or deny a refund in a first-response draft. Refund decisions always require human sign-off — see `refund-policy.md`.
