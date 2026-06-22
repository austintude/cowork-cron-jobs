# Phase 3 Payment — Proposed Deliverable Scope (DRAFT for your approval)

**Purpose:** Lock the set of deliverables that gate the **Phase 3 / M3 (P3-007 "Phase 3 Review")** payment, *before* I create any tickets. Per the MSA, payment is **deliverable-triggered** and **Allie must approve the phase in writing** — so this list = "everything that must be done and demonstrable to submit for Phase 3 payment."

**Decisions already made:** tickets go in the new PV hub (auto-hidden internal); **delivery work only** (no invoice/approval tickets); **one ticket per deliverable, each with a deep checklist**; assembled from all sources for your approval.

**⚠️ Before I build tickets, I need you to resolve 3 scope questions (Section D) and approve/trim the list.**

---

## A. Core Phase 3 build deliverables (proposed — these gate the payment)

The contract's Phase 3 is the **HubSpot / CRM automation layer** that turns the launched site into the "revenue platform." Audit language: *"Phase 3 HubSpot work — lifecycle stages, lead scoring, workflows."* Proposed tickets:

**A1. HubSpot account configuration & data model**
Deep checklist: confirm HubSpot Professional provisioned & billing active · connect the precision-vision.com domain/tracking · define **lifecycle stages** (subscriber → lead → MQL → SQL → opportunity → customer) · build the **contact properties** (persona, product interest, clinical-trial flag, account type) · build **company properties** (distributor/practice/research/clinical-trial) · set the **deal pipeline(s)** & stages · confirm the verified portal (44425657) tracking already in `theme.liquid` is firing.

**A2. Lead-capture forms integrated on key pages**
Deep checklist: build/style HubSpot forms for **RFQ / Request a Quote, Contact, Clinical Trial Services, Request a Catalog, Newsletter/Subscribe** · embed on the matching Shopify pages · field mapping to contact/company properties · spam/validation · confirm submissions create/update the right records · test each form end-to-end · verify the embeds flagged as a launch gap are live.

**A3. Lead scoring model**
Deep checklist: define scoring criteria by persona & behavior (page views, form fills, product interest, email engagement) · positive + negative attributes · MQL threshold → triggers lifecycle change · validate against sample contacts · document the model for PV.

**A4. Lifecycle & nurture workflows + routing**
Deep checklist: enrollment triggers per lifecycle stage · internal **notification/routing** to Paul + the two reps (and Allie) · new-lead acknowledgment / nurture sequences (persona-aware) · clinical-trial / quote-request fast-path · exit & re-enroll conditions · test enrollments end-to-end.

**A5. Website ↔ HubSpot event & attribution wiring**
Deep checklist: confirm GTM/GA4 + HubSpot tracking coexist cleanly · form events captured · UTM/source attribution preserved through to the contact · key conversion events defined · validate in HubSpot's traffic/contacts views.

**A6. Shopify ↔ HubSpot data flow (as scoped)**
Deep checklist: define what syncs (contacts, and orders/deals if in scope) · choose mechanism (native integration vs. middleware) · field mapping · dedupe rules · respect the MSA boundary (Acctivate two-way is **out of scope**) · test with live orders · document.

**A7. Sales enablement layer**
Deep checklist: deal pipeline ownership & routing rules · saved views for Paul + reps · email/snippet templates for common motions (quote follow-up, clinical-trial intake) · quick-start doc for the sales team.

**A8. Phase 3 documentation & PV handoff/training**
Deep checklist: written system doc (data model, forms, scoring, workflows) · short Loom/training for Allie + Paul · "how PV maintains this" notes · package the demonstrable evidence Allie needs to approve the phase in writing.

---

## B. Phase 2 carryover that likely must close first (confirm)

These were defined as **Phase 2** but flagged "not started" in the 5/21 audit. They're prerequisites for Phase 3 and may need to be closed/acknowledged so the Phase 3 work sits on a complete Phase 2:

- **P2-004 HubSpot Account Setup & Integration** — "app installed, no config evidence."
- **P2-005 HubSpot Forms Implementation** — "no artifact."

**Question:** were these effectively rolled into Phase 3, already credited under Phase 2, or do they need to close before Phase 3 can be submitted? (See D2.)

---

## C. "Phase 3 candidate" / retainer items — proposed to EXCLUDE from the payment gate

Your docs explicitly tag these as **candidates / retainer / post-launch**, not core build. Proposed: **not** part of the Phase 3 payment scope (move to retainer backlog) unless you say otherwise:

- Distributor portal (`/distributors/`) — future-tasks "Phase 3 candidate"
- International / multilingual (hreflang localized BOFU articles) — "candidate"
- Counterfeit reporting dashboard — "candidate"
- Newsletter rollup SEO cleanup (51 rollups) — "Phase 3 retainer work," best after 60–90 days live
- CRO A/B test program — needs 60+ days of HubSpot data
- Acctivate two-way reconnection — explicitly **out of MSA scope** / post-launch assessment

Also note: the **6/19 meeting items** (fraud-rule fix, ticket-system build, Shopify logins, order-history merge, SMS) are **post-launch ops / retainer**, not Phase 3 build — proposed to keep out of this payment scope.

---

## D. Open questions to resolve before I build tickets

1. **HubSpot scope decision (the big one).** The audit flagged an unmade decision: *minimum-viable HubSpot vs. full Phase 3 build vs. defer.* What does Phase 3 actually commit to? This sizes A1–A8.
2. **Phase 2 ↔ 3 HubSpot boundary.** Are P2-004/005 (HubSpot setup + forms) part of Phase 2 (already covered) or do they fold into the Phase 3 deliverables above?
3. **Anchor to the SOW Exhibit?** Do you want me to pull the exact Phase 3 deliverable list from the signed MSA / Scope of Work - Build (Exhibit) so the tickets map 1:1 to contract language? I can read it if you want this anchored contractually rather than inferred.

---

## What happens after you approve

For each approved deliverable I'll create one ticket in the hub with: a clear subject, a full description, **category = "Phase 3"**, priority, assignee (you by default; flag any that go to Jalpesh), and the deep checklist above (via `addsteps`). I'll create the **first** ticket, confirm it does **not** appear on PV's client board (validating the new auto-hide), then batch the rest.
