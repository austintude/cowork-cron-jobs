# Payment 3 — Deliverables & Proposed Tickets (contract-anchored)

**Corrected scope.** Per the signed MSA (`sow/Complete_with_Docusign_…MSA.pdf`), **Payment 3 ($26,250)** is triggered by the **Phase 2** deliverables — *not* the HubSpot lifecycle/automation work (that rolls into the **Final** Payment with Phase 4). You've just received **Payment 2** (operational launch / Phase 1). 

**Exact SOW trigger (verbatim, Payment 3 row):**
> "All twenty (20) page templates complete and submitted; full Shopify platform infrastructure configured; HubSpot integration **initiated** and contact-capture forms live on site." — *submission by week 16 triggers Payment 3.*

**Phase 2 (Exhibit A / §9, verbatim):** "Page Template Design & Platform Infrastructure. Completion of all twenty (20) page templates and full Shopify platform infrastructure configuration. HubSpot integration initiated and contact-capture forms live on site."

So there are exactly **four** deliverable buckets. Note "HubSpot integration **initiated**" — the contract bar is *initiated* (connector + tracking + forms), **not** lifecycle/automation. Don't over-build into Final-Payment scope.

---

## The four Payment 3 deliverables + current state

Status below is from your 2026-05-06 payment-status working doc; **each ticket's first checklist step is to re-verify against the live store today (6/22)** since that doc predates launch.

| # | Deliverable (SOW) | Last-known status (5/6) | Gap to close |
|---|---|---|---|
| 1 | **All 20 page templates** complete & submitted | 🟡 17 of 20 built | Build/assign final 3; QA all 20; capture for submission |
| 2 | **Full Shopify platform infrastructure** configured | ✅ Complete (Flow, S&D filters, metafields, perf, SEO, robots) | Verify + document for the package |
| 3 | **HubSpot integration initiated** | ✅ Connector installed; tracking loader (44425657) live in theme | Verify connected + safe sync; document |
| 4 | **Contact-capture forms live on site** | ⏳ Pending (embed strategy) | The main open item — build + embed + test |

---

## Proposed tickets (delivery work only — per your call, no invoice/approval tickets)

One ticket per deliverable, each with a deep checklist. Category = **"Phase 2 / Payment 3"**, source internal (auto-hidden from PV's board).

### TICKET 1 — Complete all 20 page templates
- [ ] Pull the canonical 20-template list from the IA/template spec; reconcile against what's actually built + assigned in the **V3 BUILD** theme
- [ ] Identify the 3 not-yet-complete templates; confirm which pages they map to
- [ ] Build the remaining templates (Prestige section types, PV brand styling)
- [ ] Assign each page's `template_suffix` in Online Store → Pages (templates are inert until assigned)
- [ ] Integrate Allie's final copy where pending (service hubs, About narrative)
- [ ] QA every template on desktop + mobile (hero, sections, CTAs, links, images)
- [ ] Capture a screenshot of each of the 20 for the submission package

### TICKET 2 — Verify & document full Shopify platform infrastructure
- [ ] Flow workflows active (fraud capture/hold, B2B alert, low-inventory, abandoned checkout)
- [ ] Search & Discovery: 10-filter sidebar live with values + counts on `/collections/all`
- [ ] Metafields populated (spec/contrast/optotype/etc.) and rendering on PDPs
- [ ] Performance: Lighthouse pass on home + category + product + article (capture results)
- [ ] SEO: titles/meta, canonicals, robots.txt, XML sitemap submitted in GSC
- [ ] 301 redirect map verified (legacy WooCommerce → Shopify)
- [ ] Shipping (FedEx/USPS/UPS) + tax config confirmed
- [ ] Write a one-page "platform infrastructure configured" summary for the package

### TICKET 3 — Confirm HubSpot integration is "initiated" (contract bar)
- [ ] HubSpot Professional provisioned + billing active (PV responsibility — confirm)
- [ ] Connector installed and connected to portal 44425657
- [ ] Tracking loader live in `theme.liquid` (already confirmed) — verify firing on live domain
- [ ] Sync settings safe (no prod-CRM pollution); document what is/isn't syncing
- [ ] One-paragraph "integration initiated" note for the package (explicitly NOT lifecycle/automation — that's Final Payment)

### TICKET 4 — Contact-capture forms live on site
- [ ] Decide embed strategy: HubSpot native forms vs. Shopify form → HubSpot (recommend HubSpot forms so submissions land in CRM, satisfying "initiated")
- [ ] Build forms: Contact, Request a Quote (RFQ), Clinical Trial Services, Request a Catalog, Newsletter/Subscribe
- [ ] Embed + brand-style on each page; mobile check
- [ ] Field mapping to HubSpot contact properties
- [ ] Test each submission end-to-end (record created, notification fires)
- [ ] Confirm the form embeds flagged as a launch gap (RFQ/Contact/Clinical Trial) are live

---

## Open item I need from you
**Forms strategy (Ticket 4):** HubSpot-native embedded forms (recommended — submissions flow to CRM and reinforce "integration initiated"), or Shopify-native forms piped to HubSpot? This is the one real decision that shapes Ticket 4.

## Note on the payment trigger itself
The SOW trigger is "**submission** of these deliverables by week 16" + Allie's **written phase approval**. Per your instruction I've left the *submit/approve/invoice* steps out of the tickets — just know that packaging + sending for Allie's written sign-off is the actual trigger, sitting outside this ticket set.

---

*Anchored to: signed MSA Payment table + §9 + Exhibit A; current state from `pv-project/06-documentation/p1-phase-payment-status.md` (5/6) — to be re-verified live before each ticket is worked.*
