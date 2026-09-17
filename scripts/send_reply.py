#!/usr/bin/env python3
"""Placeholder 'send' action for Lab 5, Step 2 — stands in for the Gmail MCP
send that gets wired up in Step 3. Lets the human-review hook be tested
before any real email integration exists.

Usage: send_reply.py <ticket_id> <draft_file>
"""
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) != 3:
        print("usage: send_reply.py <ticket_id> <draft_file>", file=sys.stderr)
        return 2

    ticket_id, draft_file = sys.argv[1], sys.argv[2]
    draft_path = Path(draft_file)
    if not draft_path.exists():
        print(f"draft file not found: {draft_file}", file=sys.stderr)
        return 2

    draft = draft_path.read_text()
    print(f"SENDING reply for {ticket_id}:\n{draft}")

    log_path = ROOT / "sent_log.csv"
    is_new = not log_path.exists()
    with log_path.open("a", newline="") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["ticket_id", "sent_at", "status"])
        writer.writerow([ticket_id, datetime.now(timezone.utc).isoformat(), "SENT"])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
