# Session 2 · Approved Tools, HIPAA Safety & Data Classification

**Week 2 · Modules 2 and 3 · Live session + Q&A · At least one hour; Q&A included**

## Handbook module reading

Read [Module 2 - Approved Tools & HIPAA Safety](/modules/module-02) and [Module 3 - Data Classification in Practice](/modules/module-03) before this session. The module page provides the topic introduction, four detailed learning points with examples, key takeaways, and a practical scenario. Use this session page for the live demonstration and guided practice.

## Session flow

Plan for at least one hour, including Q&A. Extend teaching, discussion, or guided practice when learners need more time. Keep practice synthetic; optional reading and follow-up reflection can happen outside the live session.

| Sequence | Activity | Learner evidence |
|---|---|---|
| 1 | Welcome; name the task and learning goal | Purpose statement |
| 2 | Tool catalog: account, feature, role, data, and task | Catalog decision path |
| 3 | Classification: four labels and mixed-data caution | Provisional classification |
| 4 | Instructor models the combined decision on a synthetic case | Pause or proceed reasoning |
| 5 | Guided tool-choice and classification case | Completed decision worksheet |
| 6 | Three-question knowledge check | Corrected response |
| 7 | Q&A, policy questions routed, and next step | Unresolved owner recorded |

## Why these modules share a session

Choosing a tool and classifying information are one workplace decision. A capable tool is still the wrong destination when the account, feature, data tier, or purpose is not authorized. This session combines the proposal's approved-tool catalog walkthrough with practical classification cases. The final authority is DWIHN's current policy and catalog, which were **not included** in the proposal.

## Outcomes and preparation

You will locate the catalog entry for a task, identify the highest data tier in a case, explain why HIPAA safeguards matter, and state when to stop and escalate. Before class, read the [data desk card](/resources/data-desk-card). The instructor must supply the current catalog or use a clearly labeled sample catalog for practice.

## Teach: approval is specific

An approval decision needs more than a product name. Check the **exact account or tenant**, **feature**, **purpose**, **permitted data classes**, **user role**, **sharing/export rules**, and **retention or recording setting**. For example, “Teams is available” does not establish that a particular AI meeting feature may process a meeting containing protected health information. “Genesys has summaries” does not establish that a summary is enabled or approved in DWIHN's tenant.

Use this decision path:

1. **Describe the task.** What outcome is needed? Could a no-data template or synthetic example accomplish it?
2. **Classify the information.** Use the highest tier present, including attachments, screenshots, and copied text.
3. **Check the catalog.** Find the exact permitted workflow and account. Confirm the current owner and any conditions.
4. **Limit and prepare.** Use only what the authorized task needs; remove unnecessary data where policy permits.
5. **Review and document.** Verify output and sharing destination. If any answer is unknown, pause.

### HIPAA boundaries

The HIPAA Privacy and Security Rules protect protected health information (PHI) and electronic PHI. HHS says a cloud provider processing or storing ePHI for a covered entity or business associate is generally a business associate and needs the applicable agreement and safeguards. A vendor's marketing statement does not by itself authorize DWIHN use. HHS also describes a **minimum necessary** standard for many uses and disclosures, with important exceptions such as treatment disclosures to or requests by a health care provider. Follow DWIHN policy and privacy guidance for the specific case. [HHS cloud guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html) · [HHS minimum necessary guidance](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/minimum-necessary-requirement/index.html)

For learners, the operational habit is simple: **do not move member information into a tool until the use and destination are confirmed**. Do not assume de-identification from merely deleting a name; dates, location, rare circumstances, or combinations can still identify someone.

## Module 3 · Classify before you act

The proposal names four tiers: **Public, Internal, Confidential, Restricted**. It does not define their DWIHN-specific boundaries. The examples below are a **provisional training model**, not an official classification policy.

| Provisional tier | Training example | Caution |
|---|---|---|
| Public | A published DWIHN service description | Verify that this exact version is public and current. |
| Internal | A non-public meeting agenda without member or personnel detail | Internal is still not public; use approved accounts. |
| Confidential | A draft contract, staff performance note, or non-public operational detail | Limit access and sharing per current policy. |
| Restricted | A member record or identifiable behavioral health information | Use only explicitly approved workflows and authorized roles. |

**Wallet analogy:** a public flyer can sit on a community table; a staff badge belongs with its owner; a private folder belongs in a controlled office; a member record is more like a locked wallet containing several sensitive items. The analogy helps recall increasing care, but the official policy decides the tier.

### Instructor demonstration

Use a **synthetic** care summary containing a fictitious name, visit date, ZIP code, and care note. Ask the class to mark each sensitive element. Open the current catalog and narrate the decision: exact tool, feature, permitted data, role, and output destination. If the catalog is unavailable, stop at “approval unknown” and show the correct escalation path rather than inventing an entry.

## Guided practice
Complete a tool-choice worksheet for these invented situations:

1. A public website description needs a plain-language rewrite.
2. A manager wants to paste a non-public staffing plan into a personal AI account.
3. A coordinator wants to summarize an identifiable member note.
4. A program analyst wants to share a ZIP-level chart where one cell represents two people.

For each, write **tier**, **purpose**, **destination or stop decision**, **what to remove or confirm**, and **human reviewer**. The safe answer for cases 2–4 cannot be a generic “yes”; it depends on catalog, policy, or disclosure review. The small chart cell may reveal individuals even without names.

### Knowledge check

1. Does an approved product name approve every feature and account?
2. If the catalog has no entry for your desired task, what do you do?
3. Why might a ZIP-level table still be sensitive?

<details><summary>Check your reasoning</summary>

1. No; approval is tied to the specific configured workflow, data, and role.
2. Pause and ask the designated tool/privacy owner; do not trial the task with real data.
3. Small cells, dates, and other attributes may permit re-identification or disclose sensitive patterns.

</details>

## Takeaway and work product

Save your four-case decision sheet. Keep the [data desk card](/resources/data-desk-card) and [daily checklist](/resources/daily-checklist) at your workstation.

---

**Previous:** [Session 1 · What AI Is — and Isn't](/sessions/s01-what-ai-is) · **Session 2 of 12** · **Next:** [Session 3 · Prompting Skills for DWIHN Roles](/sessions/s03-prompting)
