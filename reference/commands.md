# The commands you'll use

Type `/` in the chat box to see the whole list. Your own skills appear in the
same list — after Lab 3, `/triage` sits right next to `/context`.

*(There's a printable version of this in `commands.png`.)*

## The context window
| | |
|---|---|
| `/context` | What's in the window right now |
| `/compact` | Summarise it and free up room |
| `/clear` | Start clean; the old session is still saved |
| `/resume` | Pick up a previous conversation |

## Setting the agent up
| | |
|---|---|
| `/init` | Writes your first `CLAUDE.md` — Lab 1 |
| `/memory` | Edit `CLAUDE.md` and what it remembers |
| `/mcp` | Connect and manage MCP servers — Lab 5 |
| `/hooks` | See the checks wired to tool events — Lab 5 |

## When it goes wrong
| | |
|---|---|
| `/rewind` | Undo back to an earlier checkpoint |
| `/permissions` | What the agent may and may not do |
| `/status` | Version, model, account, connection |
| `/help` | Every command, including your own |

## What it cost
| | |
|---|---|
| `/usage` | Session cost and plan usage — Lab 0 and Lab 5 |
| `/model` | Switch the model you're running |
| `/export` | Save the conversation to a file |
| `/tasks` | Everything running in the background |

> **Subagents are not a slash command.** Ask the agent to create one, or add a
> file in `.claude/agents/`. Lab 4 does this by asking.
