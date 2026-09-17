# Fernway SLA Terms (Internal Reference)

For support agents — human or AI. Use this to determine correct severity, correct response-time commitment, and whether an outage triggers a service credit.

## [REF-SLA-01] Severity definitions

| Severity | Definition | Examples |
|---|---|---|
| **Critical** | Production-blocking for the whole company, or a total outage / total inability to log in / data loss risk | Entire workspace down; SSO broken for the whole company; all task completions blocked |
| **High** | A major feature is broken with no workaround, affecting a team's ability to work, but not a total outage | Integration completely stopped working; payment method declined putting the account at suspension risk; a subset of users locked out |
| **Medium** | A feature is broken or behaving incorrectly, but a workaround exists or the impact is contained | Duplicate task sync; slow board loading; an individual billing discrepancy |
| **Low** | A question, a minor inconvenience, or a feature request — nothing is broken | "How do I..." questions, feature requests, cosmetic issues |

**Note for support agents:** many incoming tickets arrive with no severity tag at all (see `tickets_raw.csv`). Assigning the correct severity from the definitions above — not copying whatever the customer wrote as the ticket subject, if anything — is part of the triage job.

## [REF-SLA-02] Response time commitments, by plan and severity

| Severity | Starter | Growth | Enterprise |
|---|---|---|---|
| Critical | Next business day | 4 hours | **1 hour** |
| High | Next business day | 4 hours | 4 hours |
| Medium | Next business day | Next business day | 4 hours |
| Low | Next business day | Next business day | Next business day |

Response time is measured from when the ticket is received to when a first substantive response is sent — an automated "we got your ticket" acknowledgment does not count.

## [REF-SLA-03] Uptime commitment and service credits

Fernway commits to **99.9% uptime** measured monthly for Growth and Enterprise plans (Starter has no formal uptime commitment). If uptime in a given month falls below the commitment:

| Uptime in the month | Growth credit | Enterprise credit |
|---|---|---|
| 99.0%–99.9% | 5% of that month's invoice | 10% of that month's invoice |
| 95.0%–99.0% | 10% of that month's invoice | 25% of that month's invoice |
| Below 95.0% | 25% of that month's invoice | 50% of that month's invoice |

**This calculation requires the actual measured uptime for the month, which support agents do not have direct access to.** Never draft a specific credit percentage in a customer-facing response — flag the request for a human to calculate against the actual uptime figures, per `refund-policy.md` rule 6.

## [REF-SLA-04] Escalation path

- **Technical issue that looks like a genuine product bug** (not user error, not a documented known issue) → escalate to Engineering.
- **Anything involving a refund or service credit** → escalate to a human support lead, per `refund-policy.md`.
- **Enterprise contract terms** → escalate to Enterprise Success.
- **Critical severity, regardless of category** → escalate to a human immediately, even if a good draft response can be written — Critical tickets are never auto-sent.
