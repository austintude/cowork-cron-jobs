# Morning Briefing -- 2026-08-22

_Generated 2026-08-24T08:03:23.947994Z_

### Headline
- Sessions DOWN 38% vs 28-day median (15 vs baseline 24) -- and DOWN 74% vs same day last year (57 sessions). Broad softness across every metric.
- Saturday Aug 22 is historically lighter traffic, but YoY gap of -74% is the number to flag for Todd.

### What happened
- **Sessions**: 15 vs median 24 (-38.8%); organic search dropped from baseline 11 to 6 -- the biggest single driver of the shortfall.
- **Pageviews**: 40 vs median 68 (-40.7%); YoY same day was 281, so this is a steep year-over-year gap.
- **Avg session duration**: 37.6s vs median 116s (-67.5%) -- CRITICAL flag; the people who did arrive left fast, suggesting a landing-page or content mismatch worth investigating.
- **GSC**: zeros across impressions, clicks, and position -- standard 1-3 day reporting lag, not a real drop.

### Efficacy
- **30-day window**: 3 pages launched, 105 pages modified, 570,848 GSC impressions and 1,345 GA4 sessions attributed across tracked content.
- **Top launches**: all five Aug 13 page-modify events (binge eating, post-bariatric support, weight loss therapy variants) are 11 days old -- no GSC impression data surfaced yet in top-launches feed; watch for movement this week.
- **Ranking warmup**: DRB-1146 psych-eval BOFU pages (IDs 6530-6532) published on staging 3 days ago -- confirm prod deployment before expecting any index activity.

### Today (do these)
1. **Confirm prod push** for DRB-1146 psych-eval pages 6530-6532 -- git log shows they were republished on staging12 Aug 21 but no prod deployment commit is visible; if they haven't gone live, push today.
2. **Check session-duration drop** on Aug 22 -- pull the GA4 landing-page breakdown for that day and see which page(s) had near-zero engagement time, since a 67% duration drop on an already-light day suggests a specific page issue, not a sitewide one.
3. **Flag the YoY gap for Todd** -- sessions -74% vs same Saturday last year (57 to 15) needs context before the weekly meeting; check whether Aug 22, 2025 had a social post, newsletter, or ad running that inflated last year's number.
