# When something doesn't work

| What you see | What's usually wrong | Fix |
|---|---|---|
| Agent invents a policy number | It's answering from training, not from `docs/` | Add the rule "cite a `[REF-xx]` ID for every policy claim, or say you cannot find it" to `CLAUDE.md` and run again |
| Agent ignores your `CLAUDE.md` | File is in the wrong folder, or you opened a different folder | `CLAUDE.md` must sit at the top of `fernway-triage`. Ask: "what rules are you operating under?" |
| `/triage` doesn't appear | Skill is in the wrong place | It must be `.claude/skills/triage/SKILL.md` — a **folder** called `triage` with a file called `SKILL.md` inside. Not `.claude/skills/triage.md` |
| Skill still doesn't show | Frontmatter missing | The first lines of `SKILL.md` must be `---`, `name: triage`, `description: ...`, `---` |
| Agent processes 10 tickets then stops | No stopping condition | Add: "do not stop until every row has a status" |
| Agent routes everything to human review | Gate is written too broadly | Only four conditions should trigger it. Re-read your rule 4 |
| Everything comes back "Needs Human Review" and you can't tell why | You're not asking it to show its reasoning | Ask it to state which rule fired, by ID, for each ticket |
| Gmail send fails: "username and password not accepted" | Using your Gmail password, not the app password | Use the 16-character app password with no spaces |
| Gmail send fails on an institute account | Admin has app passwords disabled | Use a personal Gmail account |
| Agent is slow and vague late in the day | Context window is full | Run `/context` to check, then `/compact` |
| You broke something and want to go back | — | `/rewind` |
