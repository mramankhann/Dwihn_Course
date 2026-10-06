# Module 4 · Prompting Skills for DWIHN Roles

**Month 1: AI Foundations & Safe Usage · Week 3 · [Session 3](/sessions/s03-prompting)**

## Topic introduction

A prompt is a work instruction. The handbook's five-part structure—**Role, Task, Context, Format, Constraint**—helps a learner make the request specific enough to review. It does not make an unapproved tool safe or guarantee an accurate answer. Begin only with information permitted in the chosen workflow, then improve the prompt after checking the output.

**By the end:** write a five-part prompt, improve role-specific weak requests, test three low-risk prompts, and repair common errors.

## Point 1 · The five-part prompt anatomy

**Role** names the perspective, such as “writing assistant”; it does not give the system professional authority. **Task** states the one job to perform. **Context** supplies only approved source material and audience. **Format** tells the tool how to structure a reviewable answer. **Constraint** sets boundaries such as length, source limits, tone, privacy, and “mark missing facts.” Clear constraints reduce guesswork, while source checking catches errors that remain.

**Example:** “Role: writing assistant. Task: summarize these synthetic meeting notes. Context: for the program lead; use only the notes below. Format: decisions, owners, due dates, and open questions. Constraint: do not invent an owner or date; label anything unresolved.”

**Apply it:** Before submitting, point to each of the five parts and confirm that the context is permitted in the selected tool.

Think of the five parts as a compact work brief. **Role** sets a helpful voice or perspective, but it does not grant credentials or authority; “act as a clinician” cannot turn a general model into a licensed decision maker. **Task** tells the system what action to take and should usually describe one deliverable. **Context** supplies the facts and audience. **Format** makes the answer easier to inspect. **Constraint** states what must not be changed, inferred, or disclosed. If one part is absent, the system fills the gap by guessing from patterns.

There is no reward for writing a long prompt. A short prompt can work well when the task is narrow and the input is clear. Add detail only when it removes a meaningful ambiguity or makes the output easier to check. For example, “draft a reminder” could mean a text message, an email, or a staff bulletin. Adding the audience, channel, and required details reduces uncertainty. Adding unrelated organizational history makes the prompt longer without making it more useful.

Before running the prompt, read it as if you were the system: What exactly is being requested? Which facts are provided? What shape should the answer take? What should happen when information is missing? This quick read-through catches contradictory instructions such as “be brief” and “include every detail” before they become output problems.

## Point 2 · Compare weak and strong role prompts

“Write a report” leaves the audience, evidence, and purpose undefined. A stronger prompt sets a narrow outcome and review criteria. For a coordinator, this might be a structured summary of approved, synthetic notes; for a manager, a status brief based on validated measures; for an administrator, a clear scheduling announcement; for a compliance reviewer, a list of questions to investigate rather than a policy ruling. Avoid asking the model to fill missing facts from imagination.

**Example:** Replace “Summarize this” with “Using only these approved notes, write five bullets for leadership: progress, risks, decisions, owners, and next steps. Flag any missing owner or date.” The second version makes unsupported additions easier to spot.

**Apply it:** Compare two drafts for **factual accuracy, missing caveats, useful structure, and tone**. A longer prompt is helpful only when the added detail changes the task.

The right prompt depends on the role and the decision that follows. A coordinator may need a neutral list of follow-up actions from approved notes. A program manager may need a narrative explaining a verified rate and its limits. An administrator may need a clear announcement with a date, audience, and action. A compliance reviewer may ask for questions that help organize a review, while keeping formal interpretation with authorized staff. The same phrase—“summarize this”—is not precise enough for all four jobs.

Use the before-and-after comparison to identify what changed. Did the stronger prompt define the recipient? Did it limit the answer to a source? Did it ask for a specific structure? Did it set a boundary against inventing dates or recommendations? Ask learners to underline the words that make the result easier to review. This shows them that prompting is a writing and work-design skill, not a secret command language.

Be careful with requests to imitate a person or make a message “sound more professional.” The system may introduce a tone that is too certain, too informal, or inconsistent with the relationship. Specify the intended effect—plain language, respectful, concise, neutral—and read the result aloud before use. The employee remains responsible for the words sent in their name.

## Point 3 · Write and revise three work prompts

Prompting is an iterative skill. Choose three low-risk tasks you understand: an email, a meeting summary, and a structured list. Draft the five parts, run each task only in an approved environment with permitted or synthetic material, inspect the result, then revise one instruction. Record what changed and whether the revision improved the output. This teaches cause and effect rather than memorized wording.

**Example:** An email draft sounds too certain about a proposed meeting date. The learner changes the constraint to “state the date as tentative and request confirmation,” reruns it, and checks that the revised draft matches the source.

**Apply it:** Keep a short prompt log: objective, tier, tool approval, version 1, observed issue, version 2, and final human correction. Use the [prompt builder](/resources/prompt-builder) if you need a template.

Three contrasting prompts make the practice more informative than three versions of the same request. Try one to organize an email, one to summarize notes, and one to create a structured checklist. Give each the same kind of clear boundary: use only the supplied approved material and mark missing details. After reviewing the first output, revise one part at a time. If you change task, audience, format, and tone all at once, it becomes difficult to tell which change improved the result.

Keep the initial output as part of the learning exercise, even when it is messy. Note whether the system omitted an item, added a fact, misunderstood the audience, or used an unsuitable tone. A revision should respond to a specific problem. For instance, “include the next step” may still invite invention; “list only next steps explicitly assigned in the notes and place all others under ‘unassigned’” is easier to test.

Do not use a prompt log to store member information or credentials. The useful record is the instruction pattern and the kind of correction required, using synthetic or approved content. If a team shares templates, have a knowledgeable person review them for hidden assumptions before people reuse them for work.

## Point 4 · Fix common mistakes and misleading output

Vague instructions, unrelated context, conflicting requirements, very broad tasks, and unspecified formats all increase review effort. Asking for facts that the source does not provide invites unsupported answers. A polished paragraph can still be wrong. Repair the prompt by narrowing the task, identifying the trusted source, stating the required format, and instructing the tool to flag uncertainty. Then independently verify important facts.

**Example:** “Analyze our performance” becomes “Using this synthetic quarterly table, compare the stated follow-up rate across the two periods; show the numerator and denominator and list possible questions, without claiming a cause.” The result is easier to audit.

**Apply it:** When an output is wrong, diagnose whether the issue came from **input data, ambiguous instructions, model invention, or a mistaken review**. Correct the source or process, not only the wording.

Prompt failures often have a recognizable shape. A vague task produces generic filler. Conflicting directions lead the model to satisfy one instruction and ignore another. Missing sources invite the system to invent plausible facts. A long prompt can bury the important requirement. A request to compare periods without naming the periods may yield an answer that looks precise but is not relevant. The repair is to narrow the request, make the evidence available through an approved method, state the format, and ask the system to expose uncertainty.

Sometimes the problem is not the prompt at all. The source may be out of date, the data may be incomplete, or the requested answer may not be possible from the information supplied. In those cases, better wording cannot create reliable evidence. Teach learners to stop and ask for the missing source or consult the person who owns the data. “I cannot determine this from the material provided” is a useful result.

For important work, create explicit acceptance criteria before running the task. A meeting recap might need to preserve every confirmed decision, label unresolved items, and include owners only when named. A data summary might need the date range, denominator, filters, and a statement about uncertainty. When the result can be checked against criteria, review becomes less subjective.

## Key takeaways

- Role, Task, Context, Format, and Constraint make a prompt reviewable.
- Provide approved context only and ask the tool to flag missing information.
- Compare drafts with the source; wording quality is not factual proof.
- Improve prompts through short test, review, and revision cycles.

## Practical scenario and exercise

**Scenario:** You need a first-draft weekly update for leadership from synthetic bullet notes.

1. Write a five-part prompt with an audience, a concise format, and a constraint against invented results.
2. Draft two additional prompts: one for an email and one for a structured action list.
3. Review the three outputs for a missing fact, an overstatement, or an unsuitable tone.
4. Revise each prompt once and record whether the change helped.
5. Submit the prompt log and one corrected human-approved draft.

**Worked walkthrough:** Begin with “write a weekly update.” The first draft is generic and invents a completion date. Add an audience, a source, and a format: “Use only these synthetic notes to draft a short update for the program lead, with sections for progress, risks, decisions, and next steps.” The date still appears, so add a constraint: “Do not infer dates or mark a proposal as approved; put missing details under ‘Needs confirmation.’” The revised version is easier to inspect. The learner still checks every statement against the notes, because even a well-bounded prompt cannot guarantee that the system will follow every instruction.

**Knowledge check:** Which prompt part limits unsupported claims? Why must a clear prompt still be reviewed? How would you repair a vague request?

**Answer cues:** Constraints can explicitly forbid inference and ask the system to flag missing facts; the source and format also help make claims checkable. Review remains necessary because instructions can be ignored or misapplied. Repair a vague prompt by narrowing the task, naming approved context and audience, choosing a format, and stating what the tool must not assume.

**Role transfer:** Keep the best prompt from the exercise as a pattern, not as a form to paste blindly. The next time the task changes, re-check its audience, source, data tier, and expected output. A prompt that worked for a public announcement may not suit a private staffing note. Share templates only through approved channels, and remove any real names, member details, or credentials before saving an example for colleagues.

When a prompt is reused, treat it as a draft that needs context. Replace last month’s dates, verify that the source is still authoritative, and remove constraints that no longer fit the task. Ask a colleague to review a shared template as they would a work instruction: can a new employee tell what information is allowed, what output is expected, and what needs human approval? A good prompt library grows through review, not through copying every successful chat into a shared folder.

**Facilitator discussion:** Ask participants to read a weak prompt and identify the missing audience, source, structure, and boundary. Then compare the revised prompt with its first output. The discussion should focus on which edits made errors easier to catch, rather than on who can write the longest instruction.

**Action plan:** Save a reusable prompt template that contains no sensitive data. Continue with [Module 5](/modules/module-05).
