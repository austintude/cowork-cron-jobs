# BOFU draft: pre-surgical and insurance-required bariatric psychological evaluation

Prepared 2026-09-25 by Claude for Daniel (Action Items sheet). DRAFT ONLY: nothing was written to staging or production, nothing was emailed, queue_apply.py was not run. For clinical QC by Sara Hamilton PsyD and review by Todd McCord.

Target queries: "pre-surgical psychological evaluation" (bariatric), "insurance-required bariatric psych evaluation" / "bariatric psych eval insurance".

---

## 1. Gap note

### What BCC already has (production, read-only fetch 2026-09-25)

| URL | Title tag | What it covers |
|---|---|---|
| /bariatric-surgery-psychological-evaluation-in-san-antonio-tx/ | Bariatric Psychological Evaluation, San Antonio + TX Telehealth | The main service page. What the evaluator looks at, "not designed to disqualify you", team, IOP, carrier list, 6 FAQs. This is the URL the Aug 27 plan names as the consolidation target (gate-findings Finding 3: position 25.3, 20.4, 30.9, 41.0 across the four baseline windows, zero clicks). |
| /bariatric-psych-eval-in-texas/ | Bariatric Psych Eval In Texas, Telehealth Statewide | Telehealth from other Texas cities (Austin, Houston, DFW, El Paso, Lubbock), not pass or fail, carrier list. |
| /bariatric-psychological-evaluation-near-me/ | Bariatric Psychological Evaluation Near Me | How to choose an evaluator, "rubber stamp" warning, near-me resolved by telehealth. |
| /what-happens-in-a-bariatric-psych-eval/ | What Happens In A Bariatric Psych Eval? Cost & Insurance | Appointment walk-through, "one appointment, usually 60 to 90 minutes", cost section. |
| Blog: /self-improvement/weight-loss-journey-self-improvement/pre-bariatric-surgery-binge-eating-screening/ | Pre-Bariatric Surgery and Binge Eating Screening | Why surgeons screen for binge eating; names common instruments (BES, QEWP-R, PHQ-9, GAD-7) as typical, not as BCC's battery. |
| Blog: /self-improvement/mental-health/preparing-for-bariatric-surgery-a-mental-health-checklist/ | Preparing for Bariatric Surgery: Mental Health Checklist | Emotional preparation (Sara Broussard Garcia, R-DMT, LPC). |

Search signal. GSC query universe (`seo-tools/_gsc-query-universe.json`, read 2026-09-25): "bariatric psychological evaluation near me" 243 impressions at best position 20.6; "bariatric psychologist" 192 at 9.7; "bariatric psychiatrist" 136 at 11.0; "bariatric psych eval san antonio" 86 at 1.5; "bariatric psych eval texas" 38 at 11.0; "bariatric psych eval cost" 15 at 6.5; "bariatric psych eval insurance" 9 at 8.0; "failed psych eval for bariatric surgery" 6 at 4.0; "pre surgical psych eval san antonio" 7 at 16.0; "same day bariatric psych eval" 3 at 14.0. Google Ads volume (`cron-jobs\bariatric-counseling-center\keyword-universe\data\keyword-universe-2026-09-22.csv`): "bariatric psychological evaluation" 20 a month in Texas, 170 US, $11.50 CPC. "pre-surgical psychological evaluation" has not been priced (not in the universe yet).

### What the cluster misses for these two searches

1. **Nobody owns the phrase.** "Pre-surgical psychological evaluation" appears once, in body copy, on the San Antonio page. No title or H1 on the site uses "pre-surgical" or "insurance".
2. **The insurance mechanics are missing.** The pages list carriers and say most people pay nothing. None explains why the plan requires the evaluation, where the report goes (the surgical program's prior authorization packet), what the report contains, or what happens if the plan or surgeon asks for more (treatment first, then an updated letter). That is the question behind "insurance-required".
3. **No direct-answer blocks.** The S10 spec asks for three 25 to 40 word answers leading their sections (how long, does insurance cover it in Texas, can it be done by video in Texas). None exist.
4. **Delivery mode contradicts itself.** /faq/ says "we offer telehealth sessions for the IOP and phone sessions for psychological evaluations for bariatric surgery". The eval pages say video telehealth. Sara needs to settle this before any page promises either.
5. **Turnaround is never stated.** Every page says "we tell you the expected turnaround up front". A searcher with a surgery date wants the number.
6. **The evaluator is never named.** No clinician name, credential or license number (S10 spec requires them). The production /sara-hamilton-psyd/ page is also showing an unfilled "PLACEHOLDER, VERIFY BEFORE PUBLISH" line to the public.
7. **No weight-regain section** on the eval page (S10 spec: one H2 on post-op weight regain).
8. **Compliance problems a rewrite must not carry forward.** Live eval pages carry: Joint Commission claims (gate D4 not cleared); "the only program of its kind in Texas"; "most pay $0" / "$0 out of pocket" (the replan's "free" rule); "Clinical Psychologists" plural (kit b says "a clinical psychologist"); "surgical teams ... have been reading them for years" (unverified); "most accept it" for telehealth (unverified); phone (210) 934-3420 on the eval pages versus (210) 634-2200 in the kit, on the homepage and in the schema; and the address "9907 Broadway St, San Antonio, TX 78217" in the footer block of /telehealth-eating-disorder-treatment-in-texas/ and the weight-regain page, versus 9618 Huebner Road, Suite 320 in the schema.
9. **Cannibalization.** Three URLs split "bariatric psychological evaluation near me" (Aug 27 plan play 6). A fifth eval URL would make it worse.

### Recommendation

Do not create a new slug. Rewrite the consolidation target, `/bariatric-surgery-psychological-evaluation-in-san-antonio-tx/`, in place, and fold the insurance-required angle (card DRB-1147) in as sections, which is what S7 and S10 already call for. The draft below is written as that rewrite. Do not ship the 2026-08-10 draft `draft-insurance-requirements-for-bariatric-psychological-evaluation-2026-08-10.md` as its own page: it adds a URL and carries a Joint Commission claim, "the only program of its kind in Texas" and "usually within days".

Sequencing (from `digital-transition\BCC-Texas-Launch-Replan-2026-09-22.md`): S7 consolidation ships alone first (Oct 5 to 9), then this content goes in as the S10 upgrade (January by default unless Daniel pulls it forward). Staging only; Sara's review before placement.

---

## 2. Page draft (rewrite of the S7 consolidation target)

- **URL:** /bariatric-surgery-psychological-evaluation-in-san-antonio-tx/ (keep; do not change the slug)
- **Meta title (59):** Pre-Surgical Psychological Evaluation for Bariatric Surgery
- **Meta description (154):** Need a psych eval before bariatric surgery? BCC completes insurance-required evaluations in San Antonio or by telehealth across Texas. See what to expect.
- **Focus keyword:** pre-surgical psychological evaluation
- **Supporting:** bariatric psych eval insurance, insurance required psychological evaluation bariatric surgery, bariatric psychological evaluation, bariatric psych eval texas, bariatric psych eval san antonio
- **Byline:** BCC Staff. Review line: "Clinically reviewed by Dr. Sara Hamilton, PsyD" only after she has reviewed it.
- **Schema:** keep the existing FAQPage; MedicalClinic and Person as hygiene only (S10), not a KPI.

<!-- PAGE START -->

# Pre-Surgical Psychological Evaluation for Bariatric Surgery in Texas

A pre-surgical psychological evaluation is a clinical interview, usually paired with written questionnaires, that most bariatric surgery programs and many insurance plans require before they approve weight loss surgery. At the Bariatric Counseling Center, a licensed mental health professional completes it in one appointment, in person in San Antonio or by telehealth anywhere in Texas, and sends the written report to your surgical team. [SARA TO CONFIRM: telehealth evaluations are done by video, by phone, or either; /faq/ currently says phone]

If "psych eval" is the last unchecked box on your surgeon's list and your insurance company is waiting on it, this page covers what the insurer needs, what happens in the appointment, and what comes after.

## Why your insurance requires a psychological evaluation

**Insurers and surgical programs ask for a psychological evaluation because results after surgery depend on eating behavior, mood and support at home. The evaluation documents that you understand the surgery and are ready for the changes it asks of you.**

Surgery changes the size of the stomach. It does not change why, when or how a person eats. A plan that pays for bariatric surgery generally wants an independent professional opinion on three things: that you understand the procedure and the routine that follows it, that any eating or mental health concern has been identified, and that there is a plan to support you.

The American Society for Metabolic and Bariatric Surgery describes the same purpose in its recommendations for the presurgical psychosocial evaluation (Sogg, Lauretti and West-Smith, 2016): identifying factors that could affect emotional adjustment, adherence to the post-surgery routine and long-term outcomes, and recommending ways to address them.

The exact requirement is written into your plan's bariatric surgery policy, and it varies by carrier, by plan and by employer. The psychological evaluation is usually one item among several. Your surgeon's office holds the checklist for your plan and can tell you which items are still open.

## What the evaluation includes

**Expect one appointment of about 60 to 90 minutes: a conversation with a licensed clinician plus written questionnaires about your eating, mood, stress, support at home and what you expect from surgery.** [SARA TO CONFIRM length and that questionnaires are used]

Your clinician will ask about:

- Your weight, dieting and health history, and your relationship with food today
- Eating patterns such as binge eating, grazing, night eating and emotional eating
- Mood, anxiety, trauma history and current stressors
- Alcohol and substance use, since risk can shift after surgery
- What you understand about the procedure and the routine afterward
- Who supports you at home and how your schedule and kitchen actually work
- Your reasons for surgery and what you expect it to change

[SARA TO CONFIRM: which standardized questionnaires BCC uses, so the page can name them or say "validated questionnaires" only]

Honesty helps you here. A report that reflects what is really going on is the one that gets you the right support. Binge eating, for example, is common among people seeking surgery, it is treatable, and naming it early protects your result.

## What your surgeon and insurer receive

With your written consent, BCC sends a written report to your surgical program. It summarizes what the evaluation found, gives the clinician's opinion on your readiness, and lists any recommendations. Your surgical program adds it to the packet it submits to your insurance company for approval. [SARA TO CONFIRM: report contents; whether BCC sends the report only to the surgical program or also to the insurer on request]

Timing matters when a surgery date is on the calendar. Reports are typically ready [SARA/LELONI TO CONFIRM: number of business days from appointment to report]. If your surgeon's office needs something added or clarified, we update it directly with them.

## Can you fail a bariatric psychological evaluation?

It is not a pass or fail test. Most people are ready for surgery, some with recommendations for support along the way. When a clinician recommends addressing something first, such as active binge eating or depression that is not yet managed, it is because it would make recovery harder, and it comes with a specific plan. [SARA TO CONFIRM: the outcome wording BCC uses in its reports, for example "ready", "ready with recommendations", "recommend treatment, then re-evaluate"]

## Does insurance cover the evaluation in Texas?

**BCC is in-network with most major health insurance plans, and our claims are processed under your mental health benefits. Benefits vary by plan, so we verify yours before your appointment and tell you what to expect.**

BCC is in-network with Blue Cross Blue Shield, Aetna, Cigna, UnitedHealthcare, Tricare, Humana, UMR, Carelon, Oscar, Imagine Health, Sana, MultiPlan, Meritain Health, ComPsych, Curative, 90 Degree Benefits and Healthcare Highways. [TODD TO CONFIRM list is current] We also accept CareCredit. If a claim is denied, BCC files the appeal at no cost to you. [TODD TO CONFIRM still offered] If you are paying on your own, ask us for the price before you book. [TODD TO CONFIRM whether a self-pay price should be published]

## Can the evaluation be done by video in Texas?

**Yes. BCC completes evaluations by telehealth for adults anywhere in Texas, with the same clinicians who see people at our San Antonio office. Check with your surgeon's office that its program accepts a telehealth evaluation.** [SARA TO CONFIRM video, phone or both; adjust "by video" in the heading to match]

You need a private space, a phone or computer with a camera and a steady connection, and your insurance card. If you are in San Antonio and would rather come in, we see people in person at our office in the Medical Center area. BCC serves adults.

## When the evaluation recommends support first

An evaluation that ends with a referral list and "good luck" leaves you on your own at the moment you need help. At BCC, the evaluation sits inside a full behavioral program, so a recommendation turns into a plan with the same team.

The Intensive Outpatient Program runs about three months and roughly 30 sessions, meeting 2 to 3 times per week, with morning, evening and Saturday tracks, onsite in San Antonio or by telehealth. It brings together four disciplines: Behavioral Therapy & Counseling. Dietary Guidance & Support. Culinary Classes. Mindful Movement. One program, not four.

The staff is comprised of a clinical psychologist, licensed professional counselors, registered dietitians, movement therapists, and a registered nurse, as well as a professional chef. Our team coordinates care with your surgical program and, at discharge, sends a detailed summary of your progress to the providers who referred you.

The evaluation is a standalone service. You do not have to join the program to get your report, and the decision is yours.

## After surgery: when old eating patterns come back

Weight regain after bariatric surgery is common and treatable. Surgery does not treat binge eating or emotional eating, and for some people those patterns return in a new shape: grazing through the day, soft or liquid foods that pass easily, or loss of control with smaller amounts. That is not a failed surgery. It is the behavioral work that was never part of the operation.

BCC works with people before and after surgery, including years after. If you have had surgery and the old patterns are back, start with a call; you do not need a new evaluation to get help. [SARA TO CONFIRM]

## Who performs your evaluation

Your evaluation is completed by a licensed mental health professional on BCC's clinical team, led by Dr. Sara Hamilton, PsyD, licensed clinical psychologist and Director of Clinical Services.

[SARA TO CONFIRM: name, credential and Texas license number of each clinician who performs evaluations, printed in plain text, plus one line on how to verify a license with the Texas Behavioral Health Executive Council. BHEC results are session-based, so describe the search rather than linking to a result.]

## Frequently asked questions

### Does every insurance plan require a psychological evaluation before bariatric surgery?
Most plans that cover bariatric surgery ask for one, and most surgical programs require it whatever the plan says. The details are in your plan's bariatric surgery policy. Your surgeon's office can tell you exactly what yours needs.

### What is in the report BCC sends to my surgeon?
A summary of the evaluation, the clinician's opinion on your readiness for surgery, and any recommendations for support before or after surgery. It goes to your surgical program with your written consent. [SARA TO CONFIRM]

### How long does it take, and when is the report ready?
The appointment is typically 60 to 90 minutes. The report is typically ready within [SARA/LELONI TO CONFIRM] business days, and we send it straight to your surgeon's office.

### Can I do my evaluation by telehealth if I live outside San Antonio?
Yes. BCC completes evaluations by telehealth for adults anywhere in Texas. [SARA TO CONFIRM video, phone or both] Ask your surgeon's office to confirm that its program accepts a telehealth evaluation.

### What if my evaluation recommends treatment before surgery?
You get a specific plan, not an open-ended delay. BCC can provide that treatment, coordinate with your surgeon on timing, and update your documentation when you are ready. [SARA TO CONFIRM re-evaluation process]

### Do I have to join BCC's program after my evaluation?
No. The evaluation stands on its own. If ongoing support would help, we will explain the options and the choice is yours.

### I already had surgery and I am regaining weight. Can BCC help?
Yes. Regain, returning binge urges and low mood after surgery are common and treatable, and BCC works with people at every stage after surgery, in San Antonio and by telehealth across Texas.

## Schedule your pre-surgical evaluation

Your surgery date should not wait on this step. Call the Bariatric Counseling Center at (210) 634-2200 or request an intake online. Our admissions team verifies your benefits before your appointment, and we send your report straight to your surgical team.

<!-- PAGE END -->

---

## 3. Claims that need Sara or Todd to confirm

Sara (clinical):
1. Telehealth evaluations: video, phone or both (/faq/ says phone; eval pages say telehealth).
2. Appointment length 60 to 90 minutes (stated on /what-happens-in-a-bariatric-psych-eval/ and for IOP intake on /faq/).
3. Whether standardized questionnaires are used, and which.
4. Report contents; recipients (surgical program only, or insurer on request).
5. Report turnaround in business days (with Leloni).
6. Outcome wording used in reports.
7. Re-evaluation process after pre-surgical treatment.
8. "You do not need a new evaluation to get help after surgery."
9. Names, credentials and Texas license numbers of evaluating clinicians.

Todd (business):
10. Carrier list current.
11. Appeals filed at no cost (on production today, not in the kit).
12. Whether to publish a self-pay price.
13. The page uses no Joint Commission line (gate D4) and no "only program" line. Confirm he accepts that for now.

Already verified on production or in the kit: IOP length, sessions and frequency; tracks; San Antonio office plus telehealth across Texas; adults only; CareCredit; the kit's people sentence, four pillars and "One program, not four"; discharge summary to referring providers (kit f, Corine); phone (210) 634-2200.

## 4. Suggested internal links (all confirmed in page-sitemap.xml / post-sitemap.xml on 2026-09-25)

From this page:
- /self-improvement/weight-loss-journey-self-improvement/pre-bariatric-surgery-binge-eating-screening/ (anchor: "binge eating screening before surgery")
- /self-improvement/mental-health/preparing-for-bariatric-surgery-a-mental-health-checklist/ (anchor: "prepare emotionally for surgery")
- /ourprogram/details/ (anchor: "Intensive Outpatient Program")
- /post-bariatric-surgery-support/ (anchor: "support after bariatric surgery")
- /ourprogram/coordinate-with-medical-providers/ (anchor: "coordinates care with your surgical program")
- /ourprogram/meet-with-registered-dietitians/ (anchor: "registered dietitians")
- /sara-hamilton-psyd/ (anchor: "Dr. Sara Hamilton, PsyD"; fix the public placeholder on that page first)
- /glp-1-weight-regain-counseling-in-san-antonio-tx/ (anchor: "regain after weight loss medications")
- /refer-a-patient/ (footer line for surgeons' offices)

Into this page:
- /healthy-living-2/why-hydration-is-essential-for-weight-loss-and-management/ (S10: carries about half of site clicks)
- /bariatric-surgery-counseling-in-san-antonio-tx/, /bariatric-therapist-in-san-antonio-tx/, /faq/ (anchor: "pre-surgical psychological evaluation")
- After S7, repoint every internal anchor that pointed at the merged URLs.
