# Session 3 · Prompting Skills for DWIHN Roles

**Week 3 · Module 4 · Live session + Q&A · At least one hour; Q&A included**

## Handbook module reading

Read [Module 4 - Prompting Skills for DWIHN Roles](/modules/module-04) before this session. The module page provides the topic introduction, four detailed learning points with examples, key takeaways, and a practical scenario. Use this session page for the live demonstration and guided practice.

## Session flow

Plan for at least one hour, including Q&A. Extend teaching, discussion, or guided practice when learners need more time. Keep practice synthetic; optional reading and follow-up reflection can happen outside the live session.

| Sequence | Activity | Learner evidence |
|---|---|---|
| 1 | Welcome and retrieve one unclear prompt | Weak prompt example |
| 2 | Teach Role, Task, Context, Format, Constraint | Five-part prompt outline |
| 3 | Instructor revises a vague request using synthetic notes | Before-and-after comparison |
| 4 | Write and revise three low-risk prompts | Three prompts and review notes |
| 5 | Peer check for source, format, and boundaries | Prompt checklist |
| 6 | Q&A and next step | Questions answered or assigned |

## Why prompting matters

A useful prompt names the job, supplies permitted context, defines the output, and states constraints. It reduces vague output and gives the reviewer a standard to check. Better wording does **not** make an unapproved data transfer safe, so classify and confirm the destination first.

## Outcomes and preparation

Write three five-part prompts for your role; improve an ambiguous prompt; spot an instruction that asks the model to invent facts or exceed its authority. Bring a **synthetic** work task from S2. Read the [prompt builder](/resources/prompt-builder).

## Teach: five-part prompt anatomy

| Part | Question | Example |
|---|---|---|
| **Role** | What perspective should the assistant take? | “Act as an administrative writing assistant.” |
| **Task** | What exact work product is needed? | “Draft a 120-word appointment reminder.” |
| **Context** | Which approved facts may it use? | “Use only these synthetic date and location details.” |
| **Format** | What structure helps the reader? | “Use a short subject and three bullets.” |
| **Constraint** | What must it avoid or flag? | “Do not invent addresses; mark missing facts for review.” |

The role is a writing instruction, **not** a grant of clinical authority. Context should be the smallest approved set of facts that can accomplish the task. A format makes output easier to inspect. Constraints direct the system to flag uncertainty, but a person still verifies it.

### Before and after examples

**Care coordination, synthetic case**

> Weak: “Write a letter to this member.”

> Better: “Act as a plain-language writing assistant. Draft a friendly 120-word follow-up letter from the synthetic facts below. Use a subject, greeting, appointment detail, and contact sentence. Do not invent a clinic address or promise a service. Put any missing fact in [brackets] for coordinator review.”

**Program manager, synthetic data**

> Weak: “Explain these numbers.”

> Better: “Act as a reporting assistant. Summarize the synthetic weekly table for a program manager in three bullets: change, possible explanations to investigate, and one question for the data owner. State the denominator and dates. Do not infer cause from a single trend.”

**Call center staff, synthetic transcript**

> Weak: “Tell me what to do with this caller.”

> Better: “Summarize this invented interaction for a supervisor review using reason for call, facts confirmed, unresolved questions, and next handoff. Quote no more personal detail than necessary. Do not determine crisis level; flag phrases that require a trained staff review.”

**Administration or compliance** can use the same pattern to draft a policy comparison: specify the exact versions supplied, ask for a side-by-side table, and instruct the model to mark missing language rather than assume a policy change.

## Instructor demonstration

Use the care letter example. Generate or display a weak output, then add the five parts one at a time. Show how the revised answer becomes easier to review. Deliberately include a missing phone number and demonstrate a bracketed placeholder instead of a fabricated number. Mark any fact not present in the synthetic source.

## Guided practice
Write three prompts:

1. One for a routine communication.
2. One for a summary or structured report.
3. One for checking a draft's clarity or missing facts.

For each, underline all five parts and record the data tier and approved destination you would need for **real** use. Exchange one prompt with a partner. The partner should identify an ambiguity, a privacy risk, and a way to make the output easier to verify. Revise once.

### Common mistakes and repairs

| Mistake | Why it fails | Repair |
|---|---|---|
| “Make this better” with no audience | “Better” is undefined | Name the reader and desired change. |
| Pasting an entire record | More data creates more exposure | Use only approved data needed for the task. |
| Asking for a definitive conclusion from incomplete facts | Encourages invented certainty | Ask for missing facts and alternatives. |
| No format | Output is hard to scan and compare | Request a table, bullets, or fixed headings. |
| No review step | Errors flow into final work | Compare every factual claim to its source. |

### Knowledge check

Which five parts are missing from “Summarize this”? Why can a perfectly structured prompt still be unsafe?

<details><summary>Check your reasoning</summary>

The prompt omits role, a specific task, authorized context, output format, and constraints. Even a good prompt is unsafe if it contains data that the destination is not permitted to process.

</details>

## Takeaway and work product

Keep your three revised prompts and partner feedback.

---

**Previous:** [Session 2 · Approved Tools, HIPAA Safety & Data Classification](/sessions/s02-tools-and-data) · **Session 3 of 12** · **Next:** [Session 4 · AI in Your Daily DWIHN Work](/sessions/s04-daily-work)
