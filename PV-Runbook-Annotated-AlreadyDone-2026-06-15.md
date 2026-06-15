# PV Go-Live Runbook — Verification Pass (what's already done)

**Compiled:** 2026-06-15 (evening) · **By:** verification sweep across Shopify (`vjas0d-p7`), live DNS, Gmail, Drive, and the `precision-vision` project repo.
**Purpose:** flag every runbook item that is *already complete* so it can be cut or marked done before this is shared with PV — and surface a few places where the runbook's wording is now out of date and would look wrong to PV's people (Gus, TKD).

> **How to read the tags below**
> ✅ **DONE** — verified complete; safe to strip or mark done before sharing.
> ⬜ **OPEN** — genuinely not done yet; keep it.
> ⚠️ **PARTIAL / NUANCE** — partly done or the runbook's wording needs a fix.
> 🔍 **VERIFY MANUALLY** — couldn't confirm through the API/records; check in admin.

---

## TL;DR — the five things that matter most

1. **`AMAZONPAYTEST-99` is STILL ACTIVE** (99% off entire order). Not deleted. **Keep this item — it's real.** A second test code, **`TEST10`, is also still active.** Both must go before payments go live.
2. **The email-auth section is largely already done and the runbook's framing is wrong.** SPF already includes Shopify, a DMARC record already exists, and M365 DKIM already exists. The runbook says these are "missing" and that's why mail lands in spam — if PV's IT or Gus reads that, it's inaccurate. The **only** truly missing piece is **Shopify's own DKIM** selector. Rewrite this section (details below) before sharing.
3. **TTL is still 600, not 300.** The one DNS prep task that genuinely isn't done. Keep it.
4. **GoDaddy delegate access to access@drbdig.com is EXPIRED** — so the A1 "if delegate access came through, Daniel flips directly" branch is moot. **Gus flips.** Resolve that open question in the doc.
5. **A lot of "night-before" prep is already done:** V3 theme is live, fraud guardrails are active, share-cart is built, the footer broken link is fixed, GTM + HubSpot are deployed, the SEO + Lighthouse baselines were locked weeks ago, and the Gus email + team heads-ups are sent. See the confirmed-done list next.

---

## Confirmed DONE — cut or mark complete before sharing with PV

These were verified complete. Listing them as open to-dos in a PV-facing doc would make the team look behind when they aren't.

- **SPF includes Shopify** — live DNS shows `v=spf1 include:spf.em.secureserver.net include:shops.shopify.com include:_spf-us.ppe-hosted.com include:spf.protection.outlook.com -all`. One record, correctly merged, M365 preserved. Gus confirmed this in his 6/10 reply ("The SPF has been updated to include shopify").
- **DMARC record exists** — `v=DMARC1; p=quarantine; …` is live (note: it's *quarantine*, stricter than the `p=none` the runbook proposes — see nuance below).
- **M365 / GoDaddy DKIM exists** — `selector1`/`selector2._domainkey` resolve with valid keys.
- **`AMAZONPAYTEST-99` is identified** (and confirmed still live — see Open).
- **Fraud guardrails are active** — Shopify Flow workflow **"Capture payment if it is not high fraud risk"** (manual-capture/`uncaptured` tagging) and **"Hold fulfillments based on total order value"** are both live (per the 5/21 Flow audit). Manual capture is on.
- **V3 theme is the published/MAIN theme** ("V3 BUILD — Working Theme"); the old theme ("precision-vision") and a dated backup ("BACKUP — Pre-V3 Build — 2026-04-29") sit unpublished in the library as instant rollback.
- **Share-cart + shipping-estimate message** — built natively in `theme.liquid` (v2, dated 2026-06-12), including the "enter ZIP for estimate" flow and the recipient banner.
- **Footer "About" broken `#` link is fixed** — footer "About" now points to `/pages/about`, not `#`.
- **Legal pages exist** — Privacy Policy, Terms of Service, Shipping Policy, and Returns & Refund Policy all exist as pages; a Shopify Privacy shop-policy is configured (see nuance on footer linking + final copy).
- **GTM deployed** — `GTM-PWMNJNH` is in `theme.liquid` (head + body) and fires (seen even on the password page).
- **HubSpot tracking deployed** — loader `//js.hs-scripts.com/44425657.js` (portal 44425657) is in `theme.liquid`.
- **Continue-selling applied** — every variant checked (Pelli-Robson, ETDRS Original, Sloan, cabinets) is `inventoryPolicy: CONTINUE`; negative-but-orderable stock confirms it.
- **Smoke-test products exist & active** — Pelli-Robson Contrast Sensitivity Chart, ETDRS Original Illuminator Cabinet, Original Series Sloan Letter ETDRS, Sloan flip books, etc.
- **Pre-launch SEO/GSC baseline locked** — `pv-prelaunch-baseline-2026-05-21.md` (89-day GSC window, dated/locked 5/21).
- **Lighthouse baseline captured** — mobile + desktop reports dated 2026-05-13 in `lighthouse-results/`.
- **GSC property already exists** for precision-vision.com and a sitemap is already registered (Google sent a sitemap-indexing notice 6/14; the "Blocked by robots.txt" reason is just the storefront password).
- **Gus DNS coordination email** — sent 6/10, acknowledged; Gus confirmed Tuesday availability and added his teammate Charles.
- **PV team heads-up** — covered multiple times: your 6/11 testing-window email, Paul's 6/15 "we meet at 1, launch tomorrow," and TKD's 6/15 go-live confirmation.

---

## Corrections the runbook needs before it goes to PV

These aren't just "done" — they're places where the current wording is **inaccurate** and would undercut credibility.

**1. Email-auth section (A2 / D1) overstates the problem.**
The runbook says order emails "currently land in spam because these [SPF/DKIM/DMARC] are missing." On live DNS:
- SPF already includes `shops.shopify.com` (merged correctly with M365 `spf.protection.outlook.com` and Proofpoint `_spf-us.ppe-hosted.com`).
- DMARC already exists at `p=quarantine`.
- M365 DKIM (`selector1`/`selector2`) already exists.
The **only** missing element is **Shopify's own DKIM CNAME** (no `shopify._domainkey` record on the domain). Reframe to: *"SPF/DMARC/M365 DKIM are already in place; the remaining task is adding Shopify's DKIM selector so Shopify-sent mail is DKIM-aligned."*

**2. The "stage a conservative DMARC `p=none`" step (A2) conflicts with reality.**
DMARC is already at `p=quarantine`. Don't *downgrade* it to `p=none` — that would loosen protection. Either leave quarantine as-is or make a deliberate decision, but the runbook shouldn't read as if it's creating DMARC from scratch.

**3. Mail flow is Microsoft 365 *behind Proofpoint Essentials*.**
MX = `mx1/mx2-us1.ppe-hosted.com` (Proofpoint), fronting M365. The runbook's "PV email is Microsoft 365" is right, but the "do not touch MX" warning should mention the Proofpoint layer so nobody is surprised by the ppe-hosted MX records.

**4. The rollback/freeze owner is TKD, not "the WordPress host" generically.**
Per Rob McClurg (TurnKey Digital, 6/15): TKD puts the **legacy site into maintenance mode at 8:00 AM** and keeps it live on the TKD server. So Section B2's "ordering paused banner / disable WC checkout" and the rollback target are **TKD's server / TKD's action**, not something Aaron/Josh do on the box. Name TKD.

**5. Timing wrinkle with Gus.** Gus first asked to start at **8 AM** (he has a 9 AM meeting), then confirmed availability at 9 AM and added Charles as backup. The runbook's "~9:00 AM" is fine, but confirm the exact minute with Gus/Charles the morning of.

---

# Annotated runbook (section by section)

## SECTION A — Night before

### A1. Pre-stage DNS values
- 🔍 **Pull exact A/CNAME from Shopify Domains** — do this live in Settings → Domains. Note the runbook's stated apex target `23.227.38.65` is Shopify's documented IP; the domain's current apex is `141.193.213.20/.21` (GoDaddy-hosted), so they differ as expected pre-flip. Pull the precise values Shopify shows.
- ⬜ **TTL lowered to 300** — **NOT done. Still 600** on the authoritative GoDaddy records. Keep this; have Gus lower it tonight.
- ⚠️ **Delegate access to access@drbdig.com** — **RESOLVED: it's EXPIRED** (per CLAUDE.md). So the "if yes, Daniel flips" branch is off the table — **Gus executes the flip.** Rewrite the line rather than leaving it as an open question.

### A2. Email-auth records
- ✅ **SPF (Shopify include, merged, M365 preserved)** — already live. Done by Gus.
- ⚠️ **DKIM** — M365 DKIM exists; **Shopify DKIM selector is NOT present** → this is the one real remaining auth task. Pull Shopify's DKIM from Settings → Notifications and have Gus add it.
- ⚠️ **DMARC** — already exists at `p=quarantine`. Don't recreate or downgrade to `p=none`; decide deliberately.
- ✅ **MX untouched** — MX is Proofpoint→M365 and is correct; just don't touch it (add the Proofpoint note).

### A3. Final pre-flip store config
- 🔍 **Shopify Payments wired/bank-verified, still in TEST** — your emails confirm the store is in test mode (test orders #18849/#18850). Mode itself isn't readable via API; confirm bank-verification in admin. Flip is a T-0 step.
- ⬜ **`AMAZONPAYTEST-99` deleted/scoped** — **NOT done — still ACTIVE.** **Keep — top priority.** Also delete/scope **`TEST10`** (also still active).
- ✅ **Fraud guardrails (manual capture + value-hold Flow)** — active per the 5/21 Flow audit. (Only nuance: confirm the exact dollar threshold on the "Hold fulfillments by order value" workflow.)
- 🔍 **Shipping carriers (FedEx/UPS/USPS on; DHL + own-carrier off; local pickup removed)** — can't be read via API (`carrierServices` is empty because native Shopify rates aren't exposed there). Verify in Settings → Shipping. Context: own-carrier/DHL disable was being worked (Josh's "own carrier" pink flag 6/12; international/DHL intentionally off).
- ⚠️ **Activate shipping-method-load error fixed** — verify; tied to the DHL removal. Not independently confirmable here.
- ⬜ **UPS authorization** — creds were provided by Jess (6/12, "UPS Admin Access") but **2FA is blocking** completion. Treat as known day-1 gap, not blocker. Keep.
- 🔍 **Out-of-stock cart notification copy finalized** — verify in admin.
- ✅ **Share-cart shipping message** — done (built into `theme.liquid` v2, 6/12).
- ⚠️ **Legal pages live + linked in footer** — pages **exist**; footer links **Shipping Policy** and **Returns & Refunds**; **Terms of Service is not in the footer menu**, and the footer's "Your Privacy Choices" is the opt-out page (Privacy Policy itself is wired as a Shopify shop-policy). Also: as of 6/15 you were still chasing Allie for final Return/Shipping/Terms copy. So: structure mostly there, **final copy + Terms-in-footer still open.**
- ✅ **Footer "About" `#` link fixed** — now `/pages/about`.
- 🔍 **Storefront password / maintenance toggle location** — confirmed the store **is** password-protected right now (redirects to `/password`), which is the correct pre-launch state. Removal is one toggle at T-0 (Online Store → Preferences).

### A4. Lock pre-launch baselines
- ✅ **SEO snapshot (GSC)** — locked 5/21 (`pv-prelaunch-baseline-2026-05-21.md`). Predates the flip, satisfies the attribution rule. A fresh re-pull tonight is optional, not required.
- 🔍 **GA4 90-day export** — not separately found; the locked baseline is GSC-based. Pull a GA4 export tonight if you want it on record.
- ✅ **PageSpeed/Lighthouse** — captured 5/13 (mobile + desktop in `lighthouse-results/`).
- ⚠️ **Filter-UX + staging screenshots** — partial (some benchmark/snapshot images exist). Top up if you want a complete set.

### A5. Tracking ready to verify
- ⚠️ **GA4 measurement ID present** — no hardcoded GA4 ID in `theme.liquid`; GA4 fires via the GTM container. Verify the GA4 tag inside GTM rather than expecting a hardcoded ID.
- ✅ **GTM container deployed** — `GTM-PWMNJNH`, confirmed firing.
- ✅ **HubSpot loader in theme** — portal 44425657, confirmed.
- ⚠️ **GSC ready to add/submit** — the precision-vision.com property **already exists** and a sitemap is already registered (Google emailed about it 6/14). At T-0 it's really "re-verify + resubmit," not "add from scratch."

### A6. Comms
- ✅ **Gus DNS email** — sent + acknowledged (6/10).
- ✅ **PV team heads-up** — sent (your 6/11 testing window; Paul's + TKD's 6/15 notes).
- ⬜ **Allie newsletters** — the launch email is **still in draft/review** (you sent edits 6/15, Allie is revising). The "we've launched" send is **not staged yet.** Keep.

## SECTION B — Morning-of (T-2h → T-0)
- ⬜ All Section B items are day-of execution — not pre-doable. Note that **B2's freeze is TKD's job** (maintenance mode at 8 AM), so reword from "put banner on WordPress (Aaron/Josh)" to "confirm TKD has the legacy site in maintenance mode."

## SECTION C — The flip (T-0)
- ⬜ All C steps are T-0 execution. **Exception: C3 is already true** — V3 is already the published theme, so C3 becomes a quick confirm, not an action.

## SECTION D — After the flip
- ⬜ D1 smoke tests — day-of (products/theme/tracking all pre-verified, so these should pass).
- ⚠️ **D2 GMC native-integration swap with Rob** — **already kicked off today (6/15):** you set Rob up with a Shopify staff login, pulled PV's current Shopping feed, and confirmed GMC access (account 354330480). So this is in progress, not a fresh start. (Google Ads access is still pending on PV's side.)
- ⬜ D3/D4/D5 — day-of and after.

## Known day-1 gaps — all still accurate
UPS (2FA blocking), DHL/international off by design, Acctivate→Shopify inventory sync deferred, search synonyms pending, HubSpot form-embed verification. These are correctly characterized in the runbook.

---

## What I could NOT verify from here (check in admin yourself)
- Shopify Payments test-vs-live state and bank verification (API doesn't expose it).
- Whether `precision-vision.com` is already *added* as a domain in Shopify (only that it isn't the primary yet).
- Native carrier on/off states (FedEx/UPS/USPS/DHL/local pickup) — `carrierServices` is empty via API.
- Final published state/copy of the legal pages and the OOS cart-notification text.
- The exact dollar threshold on the order-value hold workflow.

*All store findings are from the live `vjas0d-p7` Admin API; DNS from live `dig` against GoDaddy nameservers; comms from Gmail; baselines/Flow/status from the `precision-vision` project repo. Where something is time-sensitive (payments mode, carriers), re-confirm the morning of.*
