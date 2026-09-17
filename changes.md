# Change log — tickets_raw.csv -> tickets_clean.csv

## Summary of what was done

- **Dates** — all `created` values normalized to `DD-MM-YYYY` (three input formats existed: ISO,
  `M/D/YY`, and `DD-Mon-YYYY`).
- **Plan** — overwritten on every row from `accounts.csv`, matched by company name. This applies
  regardless of whether the ticket's own `plan` value was blank, differently cased, or actively
  disagreed with the account record — per `CLAUDE.md` rule 2, the ticket is never trusted for plan.
- **Category** — wording/casing normalized to a fixed set: Billing, Refund, Technical, Login,
  Integration, Feature Request, General, SSO, Outage.
- **Severity** — only the 12 rows that arrived with no severity at all were filled in, each
  assigned `Low` per `[REF-SLA-01]` (all 12 were feature requests or "how do I" questions —
  nothing broken). Severity values that already existed on a ticket were left untouched; no
  re-judging of what the helpdesk already set.
- **Duplicate ticket** — the two `FW-1002` rows (same customer, same request, second one's
  subject literally read "Duplicate of FW-1002") were merged into a single row, keeping the
  earlier `created` date and the original description.

## Left unchanged — flagged, not fixed

- **`contact_email`** — blank on 9 rows, all from two companies (Northfield Analytics, Tidewell
  Health Partners — every ticket from each has no email on file). `accounts.csv` has no email
  column, so this cannot be filled from it. Left blank.
- **`description`** — blank on 4 rows (FW-1015, FW-1030, FW-1040, FW-1046) even though `subject`
  is present. Nothing in `accounts.csv` can fill this either. Left as-is.

## Row-level detail

Format: ticket_id | field | before -> after | reason

- FW-1002 | duplicate rows merged | two rows existed (created 1/6/26 and 2026-01-07, second one's subject read 'Duplicate of FW-1002') | kept as a single row using the earlier created date and the original description | reason: same ticket resubmitted by the customer, not two distinct issues
- FW-1001 | created | '2026-01-05' -> '05-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1002 | created | '1/6/26' -> '06-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1002 | plan | 'starter' -> 'Starter' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1002 | category | 'refund request' -> 'Refund' | reason: normalized wording/casing to fixed category set
- FW-1002 | severity | '' -> 'Low' | reason: assigned per [REF-SLA-01] — ticket is a feature request or how-do-I question, nothing broken
- FW-1003 | created | '2026-01-06' -> '06-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1003 | plan | '' -> 'Growth' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1003 | category | 'technical issue' -> 'Technical' | reason: normalized wording/casing to fixed category set
- FW-1004 | created | '06-Jan-2026' -> '06-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1005 | created | '2026-01-07' -> '07-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1006 | created | '1/7/26' -> '07-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1006 | plan | '' -> 'Enterprise' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1008 | created | '08-Jan-2026' -> '08-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1008 | plan | 'GROWTH' -> 'Growth' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1009 | created | '2026-01-08' -> '08-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1009 | category | 'feature request' -> 'Feature Request' | reason: normalized wording/casing to fixed category set
- FW-1009 | severity | '' -> 'Low' | reason: assigned per [REF-SLA-01] — ticket is a feature request or how-do-I question, nothing broken
- FW-1010 | created | '08-Jan-2026' -> '08-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1011 | created | '2026-01-09' -> '09-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1011 | plan | 'Enterprise' -> 'Growth' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1011 | category | 'billing' -> 'Billing' | reason: normalized wording/casing to fixed category set
- FW-1012 | created | '1/9/26' -> '09-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1012 | category | 'refund' -> 'Refund' | reason: normalized wording/casing to fixed category set
- FW-1013 | created | '2026-01-09' -> '09-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1013 | plan | '' -> 'Growth' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1014 | created | '09-Jan-2026' -> '09-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1015 | created | '2026-01-10' -> '10-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1015 | plan | 'starter' -> 'Starter' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1015 | severity | '' -> 'Low' | reason: assigned per [REF-SLA-01] — ticket is a feature request or how-do-I question, nothing broken
- FW-1016 | created | '10-Jan-2026' -> '10-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1017 | created | '2026-01-10' -> '10-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1017 | plan | '' -> 'Enterprise' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1018 | created | '1/11/26' -> '11-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1019 | created | '2026-01-11' -> '11-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1020 | created | '11-Jan-2026' -> '11-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1020 | plan | '' -> 'Enterprise' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1021 | created | '2026-01-12' -> '12-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1022 | created | '12-Jan-2026' -> '12-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1022 | plan | 'Growth' -> 'Starter' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1023 | created | '2026-01-12' -> '12-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1024 | created | '12-Jan-2026' -> '12-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1024 | plan | 'Growth' -> 'Starter' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1024 | severity | '' -> 'Low' | reason: assigned per [REF-SLA-01] — ticket is a feature request or how-do-I question, nothing broken
- FW-1025 | created | '2026-01-13' -> '13-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1026 | created | '13-Jan-2026' -> '13-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1027 | created | '2026-01-13' -> '13-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1027 | plan | '' -> 'Growth' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1028 | created | '14-Jan-2026' -> '14-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1028 | plan | '' -> 'Enterprise' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1029 | created | '2026-01-14' -> '14-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1030 | created | '14-Jan-2026' -> '14-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1030 | severity | '' -> 'Low' | reason: assigned per [REF-SLA-01] — ticket is a feature request or how-do-I question, nothing broken
- FW-1031 | created | '2026-01-15' -> '15-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1031 | plan | '' -> 'Starter' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1032 | created | '15-Jan-2026' -> '15-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1032 | severity | '' -> 'Low' | reason: assigned per [REF-SLA-01] — ticket is a feature request or how-do-I question, nothing broken
- FW-1033 | created | '2026-01-15' -> '15-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1034 | created | '15-Jan-2026' -> '15-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1035 | created | '2026-01-16' -> '16-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1035 | plan | '' -> 'Enterprise' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1036 | created | '16-Jan-2026' -> '16-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1036 | plan | '' -> 'Growth' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1037 | created | '2026-01-16' -> '16-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1038 | created | '16-Jan-2026' -> '16-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1038 | severity | '' -> 'Low' | reason: assigned per [REF-SLA-01] — ticket is a feature request or how-do-I question, nothing broken
- FW-1039 | created | '2026-01-17' -> '17-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1040 | created | '17-Jan-2026' -> '17-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1040 | severity | '' -> 'Low' | reason: assigned per [REF-SLA-01] — ticket is a feature request or how-do-I question, nothing broken
- FW-1041 | created | '2026-01-17' -> '17-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1041 | plan | '' -> 'Enterprise' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1042 | created | '17-Jan-2026' -> '17-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1043 | created | '2026-01-18' -> '18-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1044 | created | '18-Jan-2026' -> '18-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1044 | plan | '' -> 'Enterprise' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1044 | severity | '' -> 'Low' | reason: assigned per [REF-SLA-01] — ticket is a feature request or how-do-I question, nothing broken
- FW-1045 | created | '2026-01-18' -> '18-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1045 | plan | 'Enterprise' -> 'Growth' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1046 | created | '18-Jan-2026' -> '18-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1046 | severity | '' -> 'Low' | reason: assigned per [REF-SLA-01] — ticket is a feature request or how-do-I question, nothing broken
- FW-1047 | created | '2026-01-19' -> '19-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1048 | created | '19-Jan-2026' -> '19-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1049 | created | '2026-01-19' -> '19-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1049 | plan | 'Growth' -> 'Starter' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1050 | created | '19-Jan-2026' -> '19-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1050 | plan | '' -> 'Enterprise' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1051 | created | '2026-01-20' -> '20-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1051 | severity | '' -> 'Low' | reason: assigned per [REF-SLA-01] — ticket is a feature request or how-do-I question, nothing broken
- FW-1052 | created | '20-Jan-2026' -> '20-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1053 | created | '2026-01-20' -> '20-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1053 | plan | '' -> 'Enterprise' | reason: looked up in accounts.csv by company name (accounts.csv is the source of truth, not the ticket) [CLAUDE.md rule 2]
- FW-1054 | created | '20-Jan-2026' -> '20-01-2026' | reason: normalized to DD-MM-YYYY
- FW-1055 | created | '2026-01-21' -> '21-01-2026' | reason: normalized to DD-MM-YYYY
