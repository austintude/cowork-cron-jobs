# Hand-off: approved items waiting to be placed on staging13

Generated 2026-09-19 00:23 by queue_apply.py. Daniel approved these on the dashboard. Nothing below is on any site yet.

## Rules

- staging13 only. Production is read-only. Never push; the push is its own day with its own runbook (wp-production-push skill).
- Content blocks go through the block process: `build_content_spec.py` then `build_from_spec.js` in a live editor tab (gb-kadence-blocks skill). Do not paste HTML into the editor by hand.
- Follow the brand wording kit (`bcc-brand-wording-kit.md`). Fix obvious typos in a draft; do not rewrite it, Daniel approved this wording.
- After each item is on staging13 and you have looked at the page: `cd seo-tools && python queue_apply.py --placed <id> "<staging url or short note>"`.
- When all are done: `python scoreboard-build.py`, then post one summary line on DRB-1247 (`node drbtix.js note DRB-1247 ...` from _project-manager).
- Redirects: import `review-queue/approved-redirects.csv` into Rank Math > Redirections on staging13 (or add each one by hand), test each source URL, then mark each placed.
- Link asks: the queue item is only a starting angle. For each one: (1) open their site; find the exact page we want the link on (a resources, partners, providers or links page, or the article that mentions us) and record its URL; if no such page exists, name the page where a link would fit and say so. (2) Find the right person and role from their about, team or contact page; use an email address ONLY if it is published on their site, otherwise say 'contact form: <url>'. Never guess or look up personal addresses. (3) Pick the one BCC page they should link to (a service page matching their specialty, the psychological evaluation page, or the Texas demand asset) and suggested anchor text. (4) Write the email as Todd, in the brand kit voice: subject; greeting by first name; one specific line that shows we know their site or the referral relationship; the ask with their exact page and our exact URL; what we give back (a listing on our partners page, the demand-asset data, a co-branded patient handout); a plain sign-off. No SEO jargon, no dashes, under 170 words. (5) Put every finished ask into ONE Gmail draft from daniel@drbdig.com to tmccord@bccsanantonio.com (gmail-clean-drafts skill: htmlBody with anchors; subject 'Link notes to send this week: N'), each as To / Subject / body ready to paste plus one line of why, and a request that Todd reply 'sent' per note. (6) `python queue_apply.py --packet <id> "<gmail draft subject or url>"` for each. Daniel reviews the draft and sends it to Todd; when Todd sends a note, Daniel presses Mark sent.

## Content blocks (8)

- id `f72187a483`: **Demand asset: Texas food addiction search trends (2026-Q3)**
  - target: NEW: /texas-food-addiction-search-trends/
  - draft file: `C:\Users\danie\Documents\Claude\Projects\cron-jobs\bariatric-counseling-center\review-queue\approved-content\f72187a483-demand-asset-texas-food-addiction-search-trends-2026-q3.md`
  - approved: 2026-09-19. Why: 37,440 Texas searches a month across 80 terms; a citeable page that earns links from media and directories.
- id `045b092524`: **AI Overview answer for "bariatric surgery counseling" on /bariatric-surgery-counseling-in-**
  - target: https://www.bariatriccounselingcenter.com/bariatric-surgery-counseling-in-san-antonio-tx/
  - draft file: `C:\Users\danie\Documents\Claude\Projects\cron-jobs\bariatric-counseling-center\review-queue\approved-content\045b092524-ai-overview-answer-for-bariatric-surgery-counseling-on-baria.md`
  - approved: 2026-09-19. Why: AI Overview shows for "bariatric surgery counseling" (volume not on file) and cites no named source, not BCC.
- id `a26b6ab355`: **AI Overview answer for "bariatric counseling" on /bariatric-counseling-near-me/**
  - target: https://www.bariatriccounselingcenter.com/bariatric-counseling-near-me/
  - draft file: `C:\Users\danie\Documents\Claude\Projects\cron-jobs\bariatric-counseling-center\review-queue\approved-content\a26b6ab355-ai-overview-answer-for-bariatric-counseling-on-bariatric-cou.md`
  - approved: 2026-09-19. Why: AI Overview shows for "bariatric counseling" (volume not on file) and cites no named source, not BCC.
- id `c9c45d4ec5`: **FAQ block for /bariatric-surgery-counseling-in-san-antonio-tx/ (3 questions)**
  - target: https://www.bariatriccounselingcenter.com/bariatric-surgery-counseling-in-san-antonio-tx/
  - draft file: `C:\Users\danie\Documents\Claude\Projects\cron-jobs\bariatric-counseling-center\review-queue\approved-content\c9c45d4ec5-faq-block-for-bariatric-surgery-counseling-in-san-antonio-tx.md`
  - approved: 2026-09-19. Why: 3 People Also Ask questions across 2 tracked terms (best BCC position 1).
- id `195eefae28`: **FAQ block for /bariatric-therapy-in-san-antonio-tx/ (4 questions)**
  - target: https://www.bariatriccounselingcenter.com/bariatric-therapy-in-san-antonio-tx/
  - draft file: `C:\Users\danie\Documents\Claude\Projects\cron-jobs\bariatric-counseling-center\review-queue\approved-content\195eefae28-faq-block-for-bariatric-therapy-in-san-antonio-tx-4-question.md`
  - approved: 2026-09-19. Why: 4 People Also Ask questions across 3 tracked terms (best BCC position 1).
- id `1f2b7c8adf`: **New page brief: san antonio weight loss clinic**
  - target: NEW: /san-antonio-weight-loss-clinic/
  - draft file: `C:\Users\danie\Documents\Claude\Projects\cron-jobs\bariatric-counseling-center\review-queue\approved-content\1f2b7c8adf-new-page-brief-san-antonio-weight-loss-clinic.md`
  - approved: 2026-09-19. Why: 880/mo Texas (880/mo US); sagebariatric.com ranks #10 and no BCC page targets "weight loss clinic".
- id `50546ad909`: **AI Overview answer for "nutrition counseling" on /nutritional-counseling-in-san-antonio-tx**
  - target: https://www.bariatriccounselingcenter.com/nutritional-counseling-in-san-antonio-tx/
  - draft file: `C:\Users\danie\Documents\Claude\Projects\cron-jobs\bariatric-counseling-center\review-queue\approved-content\50546ad909-ai-overview-answer-for-nutrition-counseling-on-nutritional-c.md`
  - approved: 2026-09-19. Why: AI Overview shows for "nutrition counseling" (260/mo Texas) and cites ncoa.org, ucsfhealth.org, nutritioncounselingcenter.com, not BCC.
- id `482a5526a7`: **FAQ block for /bariatric-counseling-near-me/ (5 questions)**
  - target: https://www.bariatriccounselingcenter.com/bariatric-counseling-near-me/
  - draft file: `C:\Users\danie\Documents\Claude\Projects\cron-jobs\bariatric-counseling-center\review-queue\approved-content\482a5526a7-faq-block-for-bariatric-counseling-near-me-5-questions.md`
  - approved: 2026-09-19. Why: 5 People Also Ask questions across 2 tracked terms (best BCC position 1).

## Link asks to research and write (6)

- id `82358a5dc0`: **Partner link note: texasdigestive.com** (domain texasdigestive.com, channel guess email)
  - why it was queued: 1 person from texasdigestive.com on the referral list, and the site links to a local competitor but not to BCC.
  - starting angle (rewrite it, do not send as is): Hi [first name],  Thank you for the patients you refer for bariatric evaluations and the eating work that comes after surgery. It means a lot to me and the team, and we send a detailed progress summary on each one when they finish the program.  If you keep a page of trusted providers on your site, w
- id `5d38b158f3`: **Partner link note: vitalitylifecounselingsa.com** (domain vitalitylifecounselingsa.com, channel guess email)
  - why it was queued: 1 person from vitalitylifecounselingsa.com on the referral list, and the site links to a local competitor but not to BCC.
  - starting angle (rewrite it, do not send as is): Hi [first name],  Thank you for the clients you send us when food and eating are the heart of the problem. It means a lot to me and the team, and we send a short progress note back so you stay in the loop.  If you keep a page of trusted providers on your site, we would be grateful for a spot on it, 
- id `dce3479216`: **Partner link note: gastroconsa.com** (domain gastroconsa.com, channel guess email)
  - why it was queued: 20 people from gastroconsa.com on the referral list, and the site has never linked to BCC.
  - starting angle (rewrite it, do not send as is): Hi [first name],  A quick thank you for the patients you refer for bariatric evaluations and the eating work that comes after surgery. It matters to us, and we always send a detailed progress summary on each one when they finish the program.  Would you be open to adding us to the resources or referr
- id `bbd7b1a44e`: **Partner link note: dgdclinic.com** (domain dgdclinic.com, channel guess email)
  - why it was queued: 13 people from dgdclinic.com on the referral list, and the site has never linked to BCC.
  - starting angle (rewrite it, do not send as is): Hi [first name],  I wanted to say thank you for the patients you refer for weight, eating and food-related concerns. We do not take it for granted, and we make a point of sending a progress summary back to you when each one finishes.  If you keep a page of trusted providers on your site, we would be
- id `ba77ef834d`: **Partner link note: tddctx.com** (domain tddctx.com, channel guess email)
  - why it was queued: 12 people from tddctx.com on the referral list, and the site has never linked to BCC.
  - starting angle (rewrite it, do not send as is): Hi [first name],  A quick thank you for the patients you have sent our way. It matters to us, and we always send a progress summary back to you when each one finishes the program.  If you keep a page of trusted providers on your site, we would be grateful for a spot on it, and we will do the same fo
- id `56b776c512`: **Partner link note: rfamilymedicalgroup.com** (domain rfamilymedicalgroup.com, channel guess email)
  - why it was queued: 11 people from rfamilymedicalgroup.com on the referral list, and the site has never linked to BCC.
  - starting angle (rewrite it, do not send as is): Hi [first name],  Thank you for the patients you refer for weight, eating and food-related concerns. It means a lot to me and the team, and we send a progress summary back to you when each one finishes.  Would you be open to adding us to the resources or referrals page on your website? We would happ
