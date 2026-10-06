# DWIHN AI Readiness — course architecture

**Status:** implemented as a VitePress course in `docs/`. This file records the design decisions and source map.

## Source and design decisions

- Detailed teaching source: `DWIHN_AI_Training_Handbook.docx` (Netlink, 2026), with ten modules, forty numbered learning points, practice labs, knowledge checks, recaps, and final review.
- Schedule and program source: `Netlink_DWIHN_AI_Training_Proposal 6.pdf` (20 pages, Netlink / NetSeed, 2026).
- Audience: DWIHN care coordinators, program managers, access call center staff, administration and operations, compliance staff, managers, and leaders. Prior AI experience is not required.
- Delivery: 12 live Microsoft Teams sessions, 60 minutes each, across the nine weeks shown in the source schedule and repeated in the request. The source's "eight weeks" summary and "final two sessions" sentence conflict with its 12-session table; the table and request govern this course.
- Sequence: Phase 1, foundations and safe use (Weeks 1–3, S1–S4, Modules 1–5). Phase 2, applications and readiness (Weeks 4–9, S5–S12, Modules 6–10). These phases preserve the source's Month 1 / Month 2 labels without implying each phase lasts four calendar weeks.
- S2 covers both Modules 2 and 3. S3 covers Module 4. S4 covers Module 5, as the visual schedule on source page 10 shows.
- Every exercise uses invented, clearly labeled data. A DWIHN owner must supply current approved tools, data handling rules, incident contacts, and enabled product features before live use with organizational data.
- The learner path is month → dedicated module page → topic introduction → four detailed points with examples → takeaways → practical scenario/exercise. The 12 session pages provide the live delivery and demonstration layer.

## Learner outcomes

By the end, participants can (1) explain useful and unsafe AI applications; (2) select an approved tool for a task and apply DWIHN's data-handling rules; (3) classify a scenario before entering data; (4) write a five-part prompt and review the result; (5) perform a role-specific workflow; (6) ask, filter, and verify Lumenore results; (7) interpret Genesys summaries, knowledge suggestions, and sentiment signals with human review; (8) present evidence, uncertainty, and a decision; and (9) recognize and report an AI incident. Certification requires a knowledge assessment and a practical demonstration, with thresholds to be approved by DWIHN.

## Session architecture

| Week | Session | Module | Core topic | Format | Learner evidence |
|---|---|---|---|---|---|
| 1 | S1 | 1 | What AI Is — and Isn't | Live + Q&A | Explain three useful tasks and two limits |
| 2 | S2 | 2–3 | Approved Tools & HIPAA Safety; Data Classification in Practice | Live + Q&A | Tool-choice and classification case |
| 3 | S3 | 4 | Prompting Skills for DWIHN Roles | Live + Q&A | Three revised, safe prompts |
| 3 | S4 | 5 | AI in Your Daily DWIHN Work | Live + Q&A | Reviewed role-specific output |
| 4 | S5 | 6 | Lumenore Impact: Ask Me and trustworthy questions | Demo + practice | Question and validation log |
| 4–5 | S6 | 6 | Lumenore Impact: dashboard and service-gap analysis | Demo + practice | Filtered dashboard and map interpretation |
| 5 | S7 | 6 | Lumenore Impact: alerts and board-ready reports | Demo + practice | Alert rule and report narrative |
| 6 | S8 | 7 | Genesys AI — Call Center | Live + Q&A | Reviewed interaction summary and escalation choice |
| 7 | S9 | 8 | Objective Decisions with Data: definitions and trends | Live + Q&A | KPI definition and trend explanation |
| 7 | S10 | 8 | Objective Decisions with Data: meeting and decision | Live + Q&A | Evidence-to-action decision brief |
| 8 | S11 | 9 | Governance & Incident Handling | Live + Q&A | Five-step incident simulation |
| 9 | S12 | 10 | Assessment & Certification | Assessment + ceremony | 20-question test and practical task |

**Standard session rhythm:** 0–5 minutes welcome and retrieval; 5–20 teaching; 20–30 synthetic demonstration; 30–50 guided practice; 50–55 knowledge check and debrief; 55–60 Q&A and close. Every schedule includes Q&A in the 60-minute total. S1 and S2 adjust the practice and teaching blocks to match their existing activities. S12 uses a separate allocation for the assessment, practical case, Q&A, and close.

## Source-to-course coverage map

| Source page / module | Source topic and subtopics | Destination | Treatment |
|---|---|---|---|
| 6 / M1 | AI mechanism, capabilities, limitations, drafting, summaries, analysis, care coordination examples | S1 | Expanded |
| 6 / M2 | Approved AI Tool Catalog and tool-specific data rules | S2 | Requires DWIHN catalog before operational use |
| 6 / M2 | HIPAA boundaries and consequences of misuse | S2, S11 | Expanded with HHS guidance and incident practice |
| 6 / M2–M3 | Public, Internal, Confidential, Restricted | S2 | Expanded as a proposed exercise framework; DWIHN definitions require verification |
| 6 / M3 | Wallet analogy, classification cases, desk card | S2 + job aid | Expanded |
| 7 / M4 | Role, Task, Context, Format, Constraint | S3 | Expanded with safe prompts for five roles |
| 7 / M4 | Before/after prompts, three live prompts, common mistakes | S3 + prompt worksheet | Expanded |
| 7 / M5 | Coordinator, manager, admin, compliance workflows | S4 | Expanded |
| 7 / M5 | Emails, summaries, reports, review and edit, daily checklist | S4 + job aid | Expanded |
| 8 / M6 | Ask Me, questions, result interpretation | S5 | Expanded |
| 8 / M6 | First dashboard, program analysis, service gaps by ZIP code | S6 | Expanded with synthetic data and small-cell review |
| 8 / M6 | Smart alerts and board-ready exports | S7 | Expanded |
| 8 / M7 | Agent AI, call details and transcripts, summaries, sentiment, routing, knowledge base | S8 | Expanded; enabled features require tenant verification |
| 9 / M8 | Single source of truth, conflicting data, trends | S9 | Expanded |
| 9 / M8 | Predictive insights and a data-driven meeting | S10 | Expanded with uncertainty and human decision controls |
| 9 / M9 | Governance Committee, incident recognition, internal 24-hour target, five-step response, manager support | S11 | Expanded; internal policy and reporting clock require verification |
| 9 / M10 | Nine-module review, Q&A, 20-question assessment, certificate | S12 | Expanded with practical assessment and scoring rubric |
| 11 | All-staff and six role-group outcomes | Relevant S1–S12 exercises | Covered |
| 12 | Teams, recordings, LMS quizzes/job aids, support channel | Instructor and learner guides | Covered as proposed delivery operations |

## Instructional safeguards and verification register

1. **Approved tools:** The proposal refers to a DWIHN catalog but does not contain it. Training must not name a product as approved for PHI solely because it appears in the proposal. The live course should link the current catalog, permitted data types, approved account/tenant, and access owner.
2. **HIPAA:** HHS permits cloud processing of ePHI only when the applicable HIPAA requirements, including a business associate agreement where required, are satisfied. The course teaches task-specific authorization, role-based access, and safe handling. It does not assert that any particular AI service is compliant by default.
3. **Data tiers:** The four labels come from the proposal. Definitions, examples, and allowed destinations need DWIHN policy owner approval; exercises use conservative provisional examples.
4. **Lumenore and Genesys:** Public product documentation describes capabilities, but account permissions, licensing, connected datasets, and deployed features must be confirmed in DWIHN's environment. Demonstrations can use a sandbox or screenshots until then.
5. **Incident timing:** The proposal's 24-hour response is treated as a proposed internal escalation target, not a blanket legal breach notification deadline. Staff should report immediately through the current internal channel; privacy/security officers determine legal obligations.
6. **Clinical and member communications:** AI output remains a draft or decision aid. Qualified staff review identity, facts, tone, accessibility, and clinical implications before action or release.
7. **Practice data:** Scenarios, figures, names, dates, maps, and dashboards are synthetic unless explicitly cited as public facts. Do not paste live member records into training exercises or recordings.

## Assessment design

- S1–S11: a short knowledge check and one observable task each; feedback is formative.
- S4 milestone: submit one reviewed role-specific artifact and identify its data tier and approval path.
- S7 milestone: explain a dashboard's metric, denominator, date range, filters, uncertainty, and resulting action.
- S11 milestone: complete an incident tabletop with containment, reporting, documentation, and follow-up.
- S12: 20-question knowledge assessment plus a practical case combining classification, tool choice, prompt/output review, evidence interpretation, and escalation. Proposed passing standard: 80% on knowledge and all critical safety steps on the practical rubric; DWIHN may set its own standard.

## Public reference points

- DWIHN, [Access to Services](https://dwihn.org/programs-services/crisis-services/access-services): Access Call Center, screening, referral, and crisis collaboration.
- DWIHN, [Quality Improvement](https://dwihn.org/provider-resources/quality-improvement): quality measures and care coordination priorities.
- Lumenore, [Self-Service Analytics](https://lumenore.com/self-service-analytics/): Ask Me, dashboards, analysis, and alerts.
- Genesys, [Customizable summaries](https://help.mypurecloud.com/articles/add-and-manage-an-ai-studio-summary/): summary formats and PII caveat.
- Genesys, [Live sentiment analysis](https://help.mypurecloud.com/glossary/live-sentiment-analysis/): interpretation of emotional tone.
- HHS, [Guidance on HIPAA and Cloud Computing](https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html): business associate and cloud obligations.
- HHS, [Minimum Necessary Requirement](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/minimum-necessary-requirement/index.html): scope and exceptions.
- HHS, [Breach Notification Rule](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html): external notification framework.
