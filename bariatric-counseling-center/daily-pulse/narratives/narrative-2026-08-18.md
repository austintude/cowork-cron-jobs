# Morning Briefing -- 2026-08-16

_Generated 2026-08-18T08:03:26.007692Z_

### Headline
- Sessions UP 2,405% vs 28d median (476 vs baseline 19) -- and YoY UP 5,850% (vs 8 sessions this day last year). This is not normal organic growth.
- Avg session duration DOWN 82% (22s vs 122s median) -- strongly suggests this spike is not real human engagement.

### What happened
- **Direct traffic**: jumped from baseline 6.5 to 470 sessions -- nearly the entire lift came through Direct, which is a classic bot, scraper, or misconfigured UTM pattern.
- **Engagement quality**: 476 sessions, 971 pageviews, 22s avg duration -- roughly 2 pages per visit but people are barely stopping, which points away from genuine patient interest.
- **GSC**: zeros across impressions, clicks, and position -- standard 1-3 day reporting lag, not a drop.
- **5 pages modified Aug 13**: binge eating cycle page, post-bariatric support, and three variants of "Professional Weight Loss Therapy" (including a `-fb` landing page) -- worth confirming if a paid campaign launched that day and is attribution-stripping to Direct.

### Efficacy
- **30d window**: 3 pages launched, 125 modified, 472K GSC impressions and 2,057 clicks attributed -- solid organic presence holding.
- **Top launches in data**: all git-commit entries, no page URLs surfaced -- no individual page standouts to report today.
- **Ranking**: 0 pages in top 3 or top 10 per rollup -- this needs a closer look in the weekly briefing.

### Today (do these)
1. **Check the Aug 13 `-fb` page and any associated ad account**: confirm whether a Facebook or paid campaign launched that day and is firing without UTM tags, which would explain 470 Direct sessions landing Aug 16.
2. **Audit the three "Professional Weight Loss Therapy" page variants**: `/professional-weight-loss-therapy-2/` and `/professional-weight-loss-therapy-fb/` may be duplicate or staging pages that shouldn't be publicly indexed -- verify canonical tags and robots settings.
3. **Flag this spike for Todd**: bring a one-line note that Aug 16 sessions look inflated by a traffic anomaly, likely paid or bot, not organic growth -- so the number doesn't mislead the weekly conversation.
