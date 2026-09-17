#!/usr/bin/env python3
"""PreToolUse hook — Lab 5, Step 2.

Enforces CLAUDE.md rule 4 (the human-review gate) independently of whatever
the agent believes the rule is. Covers two send paths:

1. Bash calls to scripts/send_reply.py (the placeholder used before Gmail
   was connected) — ticket ID and draft file come from the command text.
2. The real Gmail MCP send_message / create_draft tools — ticket ID is
   read from a "[FW-nnnn]" tag that must be present in the subject line.

If the ticket should be gated, it stamps "HOLD: HUMAN REVIEW" on the draft
(file, or the email subject/body) and denies the tool call outright.
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def load_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def find_ticket(ticket_id):
    for row in load_csv(ROOT / "tickets_raw.csv"):
        if row["ticket_id"] == ticket_id:
            return row
    return None


def find_account(company):
    for row in load_csv(ROOT / "accounts.csv"):
        if row["company"] == company:
            return row
    return None


def gate_reasons(ticket):
    reasons = []

    if "refund" in (ticket.get("category") or "").lower():
        reasons.append("refund request [CLAUDE.md rule 4]")

    if (ticket.get("severity") or "").strip().lower() == "critical":
        reasons.append("severity is Critical [CLAUDE.md rule 4]")

    account = find_account(ticket.get("company", ""))
    real_plan = (account["plan"] if account else "").strip()
    if real_plan.lower() == "enterprise":
        reasons.append("account is Enterprise per accounts.csv [CLAUDE.md rule 4]")

    if not (ticket.get("description") or "").strip():
        reasons.append("required information (description) missing from ticket [CLAUDE.md rule 4]")

    return reasons


TICKET_ID_RE = re.compile(r"FW-\d{3,5}")


def deny(reasons):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": f"Gated: {'; '.join(reasons)}. Draft stamped HOLD: HUMAN REVIEW, send blocked.",
        }
    }))


def check_bash(tool_input):
    command = tool_input.get("command", "")
    if "send_reply.py" not in command:
        return 0

    match = re.search(r"send_reply\.py\s+(\S+)\s+(\S+)", command)
    if not match:
        return 0  # can't parse args, let normal permission flow handle it

    ticket_id, draft_file = match.group(1), match.group(2)
    ticket = find_ticket(ticket_id)
    if ticket is None:
        return 0  # unknown ticket id, nothing this hook can check

    reasons = gate_reasons(ticket)
    if not reasons:
        return 0  # clean ticket, allow the send

    draft_path = Path(draft_file)
    if draft_path.exists():
        original = draft_path.read_text()
        draft_path.write_text(f"HOLD: HUMAN REVIEW ({'; '.join(reasons)})\n\n{original}")

    deny(reasons)
    return 0


def allow_stamped(tool_input, reasons, subject, body):
    """Allow the call through (create_draft only) but inject the HOLD stamp
    into what actually gets created, so a human reviewing Gmail drafts sees
    it flagged rather than looking like an ordinary ready-to-send draft."""
    stamped_input = dict(tool_input)
    stamped_input["subject"] = f"HOLD: HUMAN REVIEW — {subject}"
    stamped_input["body"] = f"HOLD: HUMAN REVIEW ({'; '.join(reasons)})\n\n{body}"
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "permissionDecisionReason": f"Gated: {'; '.join(reasons)}. Draft stamped HOLD: HUMAN REVIEW for human review; not sent.",
            "updatedInput": stamped_input,
        }
    }))


def check_gmail(tool_name, tool_input):
    subject = tool_input.get("subject", "") or ""
    body = tool_input.get("body", "") or ""
    is_draft = tool_name.endswith("__create_draft")

    id_match = TICKET_ID_RE.search(subject) or TICKET_ID_RE.search(body)
    if not id_match:
        # No ticket ID tag at all — treat as a non-ticket send (e.g. a
        # connectivity test) and allow it. KNOWN GAP: this also means an
        # actual ticket reply sent without its [FW-nnnn] tag slips through
        # ungated. Tagging is the only signal this hook has; it is not a
        # substitute for the send path itself carrying a ticket ID.
        return 0

    ticket = find_ticket(id_match.group(0))
    if ticket is None:
        # Looks like a ticket reference but doesn't match a known ticket —
        # still deny/flag, since something is off and a human should look.
        reasons = [f"ticket ID {id_match.group(0)} not found in tickets_raw.csv — cannot verify against the gate"]
        if is_draft:
            allow_stamped(tool_input, reasons, subject, body)
        else:
            deny(reasons)
        return 0

    reasons = gate_reasons(ticket)
    if not reasons:
        return 0  # clean ticket, allow through unchanged

    if is_draft:
        # Drafts are meant to exist for human review — stamp and allow.
        allow_stamped(tool_input, reasons, subject, body)
    else:
        # A real send is never allowed for a gated ticket.
        deny(reasons)
    return 0


def main():
    payload = json.load(sys.stdin)
    tool_name = payload.get("tool_name", "")
    tool_input = payload.get("tool_input") or {}

    if tool_name == "Bash":
        return check_bash(tool_input)
    if tool_name.endswith("__send_message") or tool_name.endswith("__create_draft"):
        return check_gmail(tool_name, tool_input)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
