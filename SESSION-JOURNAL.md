# cron-jobs Session Journal

**Purpose:** Shared ledger of what's been done, what's in flight, what's blocking next — visible to every Claude surface working on this project (Discord bridge, desktop Cowork, local Claude Code CLI). Auto-synced to GitHub like the rest of the project.

**Protocol:**
- Every Claude that does meaningful work on this project appends a journal entry at the BOTTOM.
- The "STATE NOW" section at the top is the current snapshot — updated each session, **replacing** the prior snapshot in place.
- Every Claude reads STATE NOW + the last 5–10 journal entries at session start to orient.
- Keep entries terse — one paragraph per meaningful task. Not a transcript.
- The SessionStart hook at `~/.claude-bridge/hooks/inbox-check.ps1` automatically surfaces this file to every new Claude session.

---

## STATE NOW (last updated 2026-05-30 by seed-bot@WEROCKDM)

**Project:** <one-line description>
**Current goal / target:** <what we're working toward + any deadline>

**Built + verified:**
- <key thing #1 — done, verified>
- <key thing #2>

**In flight / blocking:**
1. <thing being worked on right now>
2. <next thing>

**Open autonomous queue (runner can do without Daniel's hands):**
- <item>

**Open — needs Daniel hands or external party:**
- <item>

---

## JOURNAL

### 2026-05-30 — seed-bot@WEROCKDM — <short title>
<one-paragraph summary, including artifact paths/IDs/cost/duration if relevant>
