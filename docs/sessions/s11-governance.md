# Session 11 · AI Governance & Incident Handling

**Week 8 · Module 9 · Live session + Q&A · At least one hour; Q&A included**

## Handbook module reading

Read [Module 9 - AI Governance & Incident Handling](/modules/module-09) before this session. The module page provides the topic introduction, four detailed learning points with examples, key takeaways, and a practical scenario. Use this session page for the live demonstration and guided practice.

## Session flow

Plan for at least one hour, including Q&A. Extend teaching, discussion, or guided practice when learners need more time. Keep practice synthetic; optional reading and follow-up reflection can happen outside the live session.

| Sequence | Activity | Learner evidence |
|---|---|---|
| 1 | Welcome; recall the reporting route | Channel or policy gap named |
| 2 | Teach governance roles and incident recognition | Role map |
| 3 | Instructor models a factual incident report | Facts separated from assumptions |
| 4 | Tabletop: contain safely, preserve facts, report, cooperate | Completed response record |
| 5 | Debrief and knowledge check | First action explained |
| 6 | Q&A and next step | Unresolved owner recorded |

## Why this matters

Governance makes safe use repeatable: someone approves tools and data, monitors performance, handles exceptions, and learns from incidents. The proposal mentions an AI Governance Committee, a 24-hour response target, and a five-step process, but does not provide DWIHN's charter, contacts, or written procedure. This lesson teaches a **proposed practice framework** until those documents are supplied. Staff should report a suspected exposure **immediately through the current internal channel**; privacy and security officers determine formal deadlines and notifications. [HHS breach notification framework](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html)

## Outcomes and preparation

Recognize a possible AI incident, carry out immediate safe actions, document facts without spreading sensitive data, and explain who owns investigation and notification. Read the [incident card](/resources/incident-card).

## Teach: who does what

| Role | Proposed responsibility to confirm with DWIHN |
|---|---|
| Staff member | Stop further use or sharing, preserve facts, report promptly, cooperate with instructions. |
| Manager | Help the staff member report, protect members and evidence, maintain a supportive culture, avoid independent legal conclusions. |
| Privacy / security response | Triage exposure, assess scope and risk, direct containment, preserve records, determine required notifications. |
| Tool and data owners | Check configuration, permissions, logs, model behavior, and corrective controls. |
| AI Governance Committee | Review patterns, approved use cases, risk controls, training changes, and closure evidence. |

The committee structure above is instructional. DWIHN must confirm its actual ownership and escalation map.

## Recognize an incident

Examples include entering PHI into an unapproved AI account; exporting a restricted dashboard to the wrong group; an AI-generated summary being saved as fact when it invents a critical event; a bot recommending an unsafe response; an unauthorized recording; or a permission change that exposes data. A **near miss** also deserves reporting under current policy, because it can reveal a broken control before harm occurs.

### Proposed five-step response

![Five-step incident response](/diagrams/incident-flow.svg){.diagram}

1. **Stop and contain.** Stop the activity, stop further sharing, and follow approved containment instructions. Do not attempt a risky cleanup or delete evidence on your own.
2. **Report.** Contact the current DWIHN incident channel or supervisor immediately with the known facts. The proposal's “within 24 hours” is a proposed internal target, **not** permission to wait.
3. **Preserve facts.** Record time, tool/account, data type, recipient/destination, actions already taken, and what remains uncertain. Use approved secure channels; do not copy the exposed data into a new message.
4. **Assess and remediate.** Authorized privacy/security and tool owners determine scope, obligations, containment, notifications, and technical or process changes.
5. **Learn and close.** Document root cause, owner, corrective action, due date, and a check that the fix works. Share sanitized lessons with staff.

HHS breach notification timelines depend on the type and facts of a breach. The internal staff action here is **prompt reporting**, not deciding whether an event meets a legal definition.

## Instructor demonstration

Present this **synthetic** event: a program analyst exports a ZIP chart that includes a small cell and accidentally shares the link with a broad Teams group. The analyst notices shortly afterward. Walk through the five steps. Model a factual report: when, where, what type of data, who may have access, and what has been done. Avoid blame and avoid forwarding the chart again to “show” the problem.

## Guided practice
In groups, run a tabletop. Assign staff, manager, privacy/security lead, and tool owner. As the exercise unfolds, the link is shared, someone outside the intended group opens it, and the analyst considers deleting the post. Record each role's action and the facts needed. The instructor may add a complication: the chart source might contain identifiable information despite a missing name.

Deliver a one-page incident record with **timeline**, **known facts**, **unknowns**, **containment request**, **reporting route**, and **one preventive control**. Score the sequence, not the confidence of a legal conclusion.

### Knowledge check

1. Should staff wait up to 24 hours before reporting a possible exposure?
2. Who decides whether legal breach notification is required?
3. Why should staff avoid forwarding the exposed data as proof?

<details><summary>Check your reasoning</summary>

1. No; report promptly using current internal instructions.
2. Authorized privacy/security/legal decision makers apply the facts and law.
3. Forwarding may widen the exposure; report facts through the approved secure channel.

</details>

## Takeaway and work product

Keep the incident record and learn your current reporting channel before using live AI tools.

---

**Previous:** [Session 10 · Objective Decisions with Data: From Trend to Action](/sessions/s10-decisions) · **Session 11 of 12** · **Next:** [Session 12 · Assessment & Certification](/sessions/s12-certification)
