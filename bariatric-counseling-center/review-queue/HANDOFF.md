# Hand-off: approved items waiting to be placed on staging13

Generated 2026-09-18 19:45 by queue_apply.py. Daniel approved these on the dashboard. Nothing below is on any site yet.

## Rules

- staging13 only. Production is read-only. Never push; the push is its own day with its own runbook (wp-production-push skill).
- Content blocks go through the block process: `build_content_spec.py` then `build_from_spec.js` in a live editor tab (gb-kadence-blocks skill). Do not paste HTML into the editor by hand.
- Follow the brand wording kit (`bcc-brand-wording-kit.md`). Fix obvious typos in a draft; do not rewrite it, Daniel approved this wording.
- After each item is on staging13 and you have looked at the page: `cd seo-tools && python queue_apply.py --placed <id> "<staging url or short note>"`.
- When all are done: `python scoreboard-build.py`, then post one summary line on DRB-1247 (`node drbtix.js note DRB-1247 ...` from _project-manager).
- Redirects: import `review-queue/approved-redirects.csv` into Rank Math > Redirections on staging13 (or add each one by hand), test each source URL, then mark each placed.
- Link asks: the queue item is only a starting angle. For each one: (1) open their site; find the exact page we want the link on (a resources, partners, providers or links page, or the article that mentions us) and record its URL; if no such page exists, name the page where a link would fit and say so. (2) Find the right person and role from their about, team or contact page; use an email address ONLY if it is published on their site, otherwise say 'contact form: <url>'. Never guess or look up personal addresses. (3) Pick the one BCC page they should link to (a service page matching their specialty, the psychological evaluation page, or the Texas demand asset) and suggested anchor text. (4) Write the email as Todd, in the brand kit voice: subject; greeting by first name; one specific line that shows we know their site or the referral relationship; the ask with their exact page and our exact URL; what we give back (a listing on our partners page, the demand-asset data, a co-branded patient handout); a plain sign-off. No SEO jargon, no dashes, under 170 words. (5) Put every finished ask into ONE Gmail draft from daniel@drbdig.com to tmccord@bccsanantonio.com (gmail-clean-drafts skill: htmlBody with anchors; subject 'Link notes to send this week: N'), each as To / Subject / body ready to paste plus one line of why, and a request that Todd reply 'sent' per note. (6) `python queue_apply.py --packet <id> "<gmail draft subject or url>"` for each. Daniel reviews the draft and sends it to Todd; when Todd sends a note, Daniel presses Mark sent.

## Nothing outstanding for a Claude session right now.