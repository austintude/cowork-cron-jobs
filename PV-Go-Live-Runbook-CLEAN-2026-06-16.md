# PV Go-Live Runbook — Clean / Remaining-Work Only

**Launch:** Tuesday, June 16, 2026, ~9:00 AM CT · DNS cutover, WooCommerce → Shopify Advanced (`vjas0d-p7`)
**Owner:** Daniel (drb·dig) · **DNS executor:** Gus (GoDaddy, oluxtech) + Charles · **Legacy host / freeze:** Rob McClurg (TurnKey Digital) · **PV coordinator:** Allie
**Rollback:** Re-point DNS to the TKD server — legacy site stays live in maintenance mode all day, returns in minutes.

> This is the trimmed runbook: items already verified complete (V3 theme published, fraud guardrails, GTM/HubSpot, share-cart, footer fix, SPF/DMARC, SEO + Lighthouse baselines, discount-code cleanup, Gus email, team heads-ups) have been removed. What remains is genuinely open or day-of. A full "what was already done" audit is archived separately.

> **Framing:** This is a DNS flip with a TKD-server rollback behind it. No step is irreversible. If anything looks wrong, point DNS back and the old store is live again. Calm beats fast.

---

## Standing context (so nothing here surprises PV)

- **Acctivate → Shopify inventory sync is deferred to post-launch.** Inventory is static (continue-selling already applied store-wide); prices change via manual bulk update. The only live integration at launch is the **Shopify → Acctivate order sync** (one-way). Its launch-critical concern is the **timestamp/lookback window** — set so no real post-launch order is skipped.
- **Email is Microsoft 365 behind Proofpoint Essentials** (MX = `mx1/mx2-us1.ppe-hosted.com`). Do not touch MX. SPF already includes Shopify + M365 + Proofpoint in one record; DMARC already exists at `p=quarantine`. The only outstanding auth task is adding **Shopify's DKIM selector** (below).
- **GoDaddy delegate access to access@drbdig.com is expired** → **Gus executes the DNS flip**, not Daniel.

---

# SECTION A — Night before (Mon 6/15 evening)

## A1. DNS prep (stage, don't flip)
- [ ] Pull the **exact A (apex) and CNAME (`www`) values** from Shopify → Settings → Domains and put them in the Gus note for copy/paste.
- [ ] **Lower TTL on apex + `www` to 300s** — currently still **600**. Have Gus drop it tonight so propagation is fast at flip.
- [ ] Confirm Gus + Charles have the values, the flip window, and the contact channel locked.

## A2. Email auth — add the one missing record
- [ ] Pull **Shopify's DKIM** value from Settings → Notifications (sender authentication) and have Gus add the `shopify._domainkey` CNAME. (SPF + DMARC + M365 DKIM are already live — do not recreate or downgrade them.)

## A3. Final pre-flip store config
- [ ] **Confirm Shopify Payments is wired + bank-verified** and ready for the 2-minute TEST→LIVE flip at T-0. (Leave in test tonight.)
- [ ] **Re-confirm the store has zero discount codes** (cleared 6/15 — `AMAZONPAYTEST-99` and `TEST10` deleted). Make sure no new test code gets added before launch.
- [ ] **Verify shipping carriers** in Settings → Shipping: FedEx/UPS/USPS enabled; DHL + "use your own carrier" disabled (not deleted); free local pickup removed. Confirm no Acctivate shipping-method-load error remains.
- [ ] **UPS authorization** — creds in hand (Jess) but 2FA is blocking. If not completed, flag as a known day-1 gap; FedEx/USPS cover checkout.
- [ ] **Finalize legal pages:** get final Return / Shipping / Terms copy from Allie; add **Terms of Service to the footer menu** (Shipping + Returns already linked; Privacy is wired as a shop-policy). GMC needs a published return policy.
- [ ] **Verify** out-of-stock cart-notification copy reads correctly.
- [ ] Know the **storefront-password toggle** location (Online Store → Preferences → "Restrict access") for a one-click removal at T-0.

## A4. Baselines (optional top-ups — core baselines already locked)
- [ ] Optional: pull a dated **GA4 90-day export** for the record (SEO/GSC baseline locked 5/21; Lighthouse locked 5/13).
- [ ] Optional: top up filter-UX / staging screenshots for a complete before/after set.

## A5. Tracking — verify, don't deploy
- [ ] Confirm the **GA4 tag fires via the GTM container** (GTM `GTM-PWMNJNH` and HubSpot loader are already in the theme).
- [ ] Have **GSC** open: the precision-vision.com property already exists with a sitemap registered — plan to **re-verify and resubmit the sitemap** at T-0 once the password is off.

## A6. Comms
- [ ] **Finalize Allie's launch newsletter** (still in review — your edits are with her) and **stage the "we've launched" send with a delay** so it doesn't fire if we roll back.

---

# SECTION B — Morning-of, before the flip (T-2h → T-0)

## B1. T-2h — Readiness gate (Daniel + PV)
- [ ] **End-to-end checkout test passes** on the myshopify URL: add to cart → checkout → real $1 card order → refund. Confirms payments + tax + shipping rates + order email in one shot. **If this fails, we do not flip.**
- [ ] Confirm the **Acctivate order-sync** is healthy and the **timestamp lookback window** is set so live orders aren't missed.
- [ ] Mobile spot-check: homepage, mega menu (hamburger), one product page, add-to-cart.

## B2. T-2h — Freeze the old store (TKD + PV)
- [ ] Confirm **TKD has placed the legacy WooCommerce site into maintenance mode** (their plan: 8:00 AM, site stays live on the TKD server).
- [ ] Confirm the **last WooCommerce orders are processed and clear** (Aaron / Josh).
- [ ] Final **WordPress order export** saved for back-office reconciliation.

## B3. T-30min — Stage everyone
- [ ] Gus + Charles on standby, values in hand, line open (note: Gus floated 8 AM; he confirmed 9 AM availability — lock the exact minute).
- [ ] Daniel in Shopify admin with Domains, Themes, Payments, Preferences tabs open.
- [ ] GSC + GA4 real-time open in another window.

---

# SECTION C — The flip (T-0, ~9:00 AM CT)

Run in this exact order:

1. **[Gus]** Flip DNS at GoDaddy: apex `A` and `www` `CNAME` to the Shopify values from A1. **This is the single action that puts the new site live.**
2. **[Gus]** In the same session, add the **Shopify DKIM** CNAME (A2). Do not touch MX/SPF/DMARC.
3. **[Daniel]** Confirm **V3 ("V3 BUILD — Working Theme") is still the published theme**; old theme + backup stay in the library as instant rollback.
4. **[Daniel]** **Set primary domain** to `precision-vision.com` (Settings → Domains).
5. **[Daniel]** **Remove the storefront password / maintenance restriction** — makes the store public.
6. **[Daniel]** **Flip Shopify Payments TEST → LIVE** (~2 min).
7. **[Daniel]** Verify **SSL active** (green padlock on `https://precision-vision.com`).

> SSL/DNS may take ~15 min to propagate — that's normal, don't panic-revert. Watch propagation on dnschecker.org before concluding anything is wrong.

---

# SECTION D — Immediately after the flip

## D1. T+15–30min — Smoke tests (Daniel)
- [ ] Homepage renders (hero, announcement bar).
- [ ] Mega menu (Services / Products / Resources) renders.
- [ ] Collection page (`/collections/all`) — 10-filter sidebar shows values + counts.
- [ ] Product pages — Sloan Pocket Card, ETDRS Original, Pelli-Robson: variants, images, spec metafields render.
- [ ] Search — "ETDRS" returns expected results.
- [ ] **Live $1 order with a real card** → confirm it appears in Orders, returns real shipping rates, sends the **order-confirmation email (and does NOT land in spam — validates the new Shopify DKIM)**, and **syncs into Acctivate** within the window. Then **refund it.**
- [ ] Mobile pass of the same.
- [ ] **301 spot-check** — 10 high-traffic legacy URLs each 301 to the right Shopify page (mapping already built; in `09-deliverables/PV-URL-Mapping-for-TDK.xlsx`).

## D2. T+0 — SEO / tracking activation (Daniel)
- [ ] **GSC:** re-verify `precision-vision.com` and **resubmit the XML sitemap** (the "Blocked by robots.txt" notice clears once the password is off).
- [ ] Confirm **GA4 / GTM / HubSpot** tags fire on the live domain (real-time).
- [ ] **Continue the GMC native-integration swap with Rob** (already kicked off 6/15 — staff login created, feed obtained, account 354330480). ⚠️ Expect a **1–3 day Google validation delay** on product listings — normal. (Google Ads access still pending on PV's side.)

## D3. T+1h — Remove freeze + announce (Daniel + Allie)
- [ ] Confirm TKD's maintenance state can come down / is no longer being hit.
- [ ] **Daniel:** short factual launch confirmation to Ed/Allie/Paul/Josh/Aaron/Jess.
- [ ] **Allie:** send the **"we've launched" newsletter** only once smoke tests are green and rollback is off the table.

## D4. T+1h → T+4h — Monitoring (Daniel)
- [ ] Watch the **Shopify orders feed** — every order should sync to Acctivate; flag any that don't.
- [ ] Watch **Acctivate order-sync logs** — investigate failed/duplicate immediately (watch for underscore-suffix duplicate-SKU artifact).
- [ ] Watch **GA4 / GSC real-time** for traffic and error patterns.
- [ ] **No deploys or config changes** unless it's an emergency fix.

## D5. T+24h — Day-after reconciliation (Daniel + Aaron)
- [ ] Order audit: every Shopify day-1 order confirmed in Acctivate.
- [ ] Re-submit the GSC sitemap if it didn't take.
- [ ] Re-run the 301 spot-check on 10 more legacy URLs.
- [ ] Capture post-launch baselines (Lighthouse on live domain, GA4 first-24h, GSC impressions).
- [ ] Confirm GMC validation status; resolve any disapprovals.
- [ ] Confirm order-confirmation + `orders@` emails land in inbox, not spam (validates DKIM over a full day).

---

# PV TEAM — what we need

| When | Who | Responsibility |
|---|---|---|
| Tonight | **Gus** | Lower TTL to 300; stage A/CNAME + Shopify DKIM values. |
| Flip (~8–9 AM) | **Gus + Charles** | Execute the GoDaddy A/CNAME flip + add Shopify DKIM; be reachable. Confirm exact start time. |
| Before flip | **Rob (TKD)** | Place legacy site in maintenance mode (8 AM); keep it live on TKD server for rollback. |
| Before flip | **Aaron / Josh** | Confirm last WooCommerce orders clear; Aaron on hand to confirm Acctivate order-sync is receiving. |
| Before flip | **Jess** | Complete **UPS authorization** (2FA) if possible; final fraud-settings confirmation. |
| Before flip | **Allie** | Final Return/Shipping/Terms policy copy; finalize launch newsletter. |
| Flip morning | **Allie** | Coordination point; hold "we've launched" newsletter until Daniel's all-clear. |
| Post-launch | **Aaron** | Verify Acctivate received all day-1 orders; restart Amazon Marketplace Connect conversation. |

---

# ROLLBACK (if anything catastrophic, T-0 → T+4h)

1. **Revert DNS** at GoDaddy — apex/`www` back to the TKD server. TTL 300s, so it returns fast.
2. **TKD takes the legacy site out of maintenance mode** / re-enables WooCommerce checkout.
3. **Disable the Acctivate order sync** so it stops writing from a store that's no longer customer-facing.
4. **Do NOT send** the "we've launched" newsletter.
5. **Postmortem** before re-attempting. V3 stays published in Shopify; nothing is lost. Shopify DKIM + lowered TTL can stay even on rollback.

---

# KNOWN DAY-1 GAPS (manage expectations, not blockers)

- **GMC re-validation:** 1–3 day Google delay on product listings. Expected.
- **UPS carrier:** may be unauthorized at launch (2FA). FedEx/USPS cover checkout; UPS is a fast-follow.
- **DHL / international:** disabled by design pending Josh's DHL conversation.
- **Acctivate → Shopify inventory sync:** deferred post-launch (inventory static/continue-selling; prices via manual bulk update).
- **Search synonyms:** ~27 still to paste in admin (Week 1).
- **HubSpot forms:** confirm embeds live on RFQ / Contact / Clinical Trial Services (verify in smoke test).

---

*Clean runbook compiled 2026-06-15 from the verified state of the live store, DNS, comms, and the project repo. Completed items removed; corrections (TKD-owned freeze, Gus-executed flip, email-auth reality) folded in.*
