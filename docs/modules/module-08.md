# Module 8 · Objective Decisions with Data

**Month 2: Advanced AI & Lumenore Mastery · Week 7 · [Sessions 9–10](/sessions/s09-objective-data)**

## Topic introduction

AI can summarize a trend, but a team still needs agreed definitions, reliable data, and an accountable decision process. The handbook moves from a shared source of truth to trend interpretation, predictive insights, and a well-run meeting. Use the [synthetic dataset](/resources/synthetic-data) to practice without claiming that its figures represent DWIHN performance.

**By the end:** reconcile conflicting measures, describe a trend without inventing its cause, evaluate a prediction cautiously, and run a meeting that produces an owner and next step.

## Point 1 · Establish a single source of truth

Two spreadsheets may disagree because they use different populations, time periods, refresh dates, exclusions, or denominator rules. Calling one dashboard “official” does not resolve these differences unless the team also agrees on its metric dictionary, owner, and version. Before debating performance, define the question and compare the measure definitions. Preserve any legitimate differences so the group knows which view answers which decision.

**Example:** One synthetic report counts all follow-up contacts; another counts only qualifying discharges with a contact within seven days. The rates differ. The team checks denominator and period, chooses the governed measure for the meeting, and records why the other figure is not directly comparable.

**Apply it:** Complete a definition card with **name, numerator, denominator, exclusions, period, source, refresh date, and owner**. See [S9](/sessions/s09-objective-data).

A trustworthy source of truth is not simply the newest spreadsheet or the dashboard with the most attractive design. It has an accountable owner, documented definitions, an expected refresh schedule, controlled access, and a known path for correcting errors. When two reports disagree, compare their definitions before comparing their values. A report might count services by the date they were requested while another counts them by the date they were completed. Both may be internally correct and still answer different questions.

Teams should agree on which measure governs a particular decision, not pretend that every use needs one universal number. A program manager may need a monthly operations view; a quality team may need an audited measure with a different inclusion rule. The meeting record should identify which source and definition were used so a later reader can reproduce the reasoning.

When data ownership is unclear, learners should avoid quietly selecting the value that supports their preferred conclusion. They can show both results, describe the difference in definitions or freshness if known, and assign the data owner to resolve the discrepancy. This keeps the disagreement visible and protects the decision from false precision.

## Point 2 · Read and present AI-generated trend analysis

A useful trend statement says **what changed, over what period, by how much, and for whom**. Check the underlying counts, missing data, scale, and whether the comparison is like for like. A line or AI narrative may suggest possible explanations, but a trend alone does not prove one. Separate the observed result from interpretation and the question that should be investigated next.

**Example:** A synthetic rate falls from 74.5% to 73.0%. The presenter calls this a **1.5 percentage-point decline**, confirms the counts, and notes that the chart cannot establish why the change occurred. They request a data-quality and process review before attributing it to staffing or demand.

**Apply it:** Write three labeled sentences: **Observation**, **Limit**, **Next check**. Avoid converting a possible cause into a headline.

Trend analysis requires attention to the comparison itself. Are the periods the same length? Are they seasonal? Did the service definition or documentation process change? Did a new program enter the dataset? Did the number of eligible records become smaller? A percentage may rise while the underlying count falls, or vice versa. Reporting both rates and counts helps the audience understand the scale of the change.

AI-generated explanations should be treated as hypotheses to test. A model may list “staffing shortage,” “increased demand,” or “system outage” because those are common explanations in similar text, not because the data prove any of them. Present the observed pattern first, then list what information would help assess possible causes. Avoid words such as “because” or “resulted in” unless the evidence and method support a causal conclusion.

Before presenting, verify the calculation independently where practical. Check a sample against the source table, confirm the units and date range, and make sure rounding has not changed the message. If a result cannot be reproduced or explained, mark it as preliminary and ask the data owner rather than polishing the language around uncertainty.

## Point 3 · Use predictive insights proportionately

A prediction is an estimate based on the data, outcome definition, and assumptions used to build it. It can help prioritize investigation, but it may be less reliable after a process change or for groups poorly represented in past data. Ask what is being predicted, the time horizon, how the output was validated, and what harm could follow from acting on a wrong prediction. Set a human review step before any consequential action.

**Example:** A synthetic risk indicator increases. The team does not declare that a service failure will occur. It checks current conditions, asks the data owner about model limits, and considers a reversible, proportionate follow-up.

**Apply it:** Note the predicted outcome, uncertainty, potential false positive and false negative consequences, and the person who approves the response. See [S10](/sessions/s10-decisions).

Predictions are outputs of a model built for a target outcome and a time horizon. A “risk score” is not self-explanatory: learners need to know what event it predicts, over what period, how it was evaluated, and what threshold or action—if any—is authorized. A model developed on past patterns can reflect gaps or biases in historical data. It may also lose accuracy when programs, definitions, or populations change.

Consider both kinds of error. A **false positive** may direct staff attention toward a case that does not need the anticipated intervention. A **false negative** may fail to flag a situation that later requires attention. The practical cost depends on the task. For a low-risk review queue, the response may be to examine more cases. For a consequential service decision, a prediction alone should not determine what happens to a person. Follow the approved process and preserve meaningful human review.

Before an organization acts on a predictive output, the responsible governance and data owners should establish validation, monitoring, access, contestability, and a process for correcting adverse effects. Learners do not need to audit a model during this course, but they should know when to ask who owns these safeguards and how to escalate a concern.

## Point 4 · Run a data-driven meeting with Lumenore

Start with one decision question and a few agreed KPIs. Open the governed view, verify period and filters, then ask participants to distinguish what they observe from what they infer. Record a decision, unresolved evidence, owner, due date, and success check. The dashboard focuses the conversation; facilitation prevents it from becoming a tour of charts. If a metric is disputed, assign a validation action rather than forcing a false consensus.

**Example:** A team reviews three synthetic KPIs, notices one unusual trend, and assigns an analyst to check definitions. The program lead records a tentative action and a date for deciding after the validation result returns.

**Apply it:** Use a short sequence: question → evidence → caveat → options → owner and follow-up.

Good meeting facilitation moves from data to a decision without skipping the conversation in between. Begin by stating the question and the source view. Invite someone to confirm the measure and filters. Ask what the group observes before asking what it might mean. Name missing evidence openly. Then consider options, including the option to gather more information before acting. Close by recording what was decided, what remains open, who owns the next step, and when the group will review the result.

Participants should distinguish between an **operational response** and a **causal conclusion**. A team may decide to check a process because a rate changed, even when it does not know why. That action is proportionate to the evidence. Declaring that a particular policy caused the change would require a stronger analysis. Meeting notes should preserve that distinction so a tentative investigation does not later appear as a proven finding.

If participants disagree about a metric, record the competing definitions and assign a validation task. Do not spend the whole meeting debating a chart with hidden filters. Return to the decision question, agree what evidence is needed, and set a time to revisit it. A short, well-documented follow-up is often more objective than a quick forced consensus.

## Key takeaways

- Shared data means shared definitions, ownership, period, and source.
- State observed change separately from its possible cause.
- A prediction guides attention and needs limits and human review.
- End meetings with a documented decision or a named validation task.

## Practical scenario and exercise

**Scenario:** A synthetic dashboard shows a concerning trend, while another report appears to disagree.

1. Compare the two measure definitions and identify the likely source of conflict.
2. Write an observation that includes period, counts or rate, and uncertainty.
3. Name two plausible checks before discussing cause.
4. Draft a short meeting agenda with one decision question and three KPIs at most.
5. Record a proposed action, owner, due date, and evidence needed to revisit it.

**Worked walkthrough:** Two dashboards report different follow-up rates for the same month. One counts every recorded contact; the other counts a contact within a defined period after a qualifying event. Before sharing either figure, the team checks the numerator, denominator, population, and refresh date. It identifies the second measure as the one required for the planned review, while recording the first as a broader operations count. The trend shows a decline, but the available table does not explain why. The group asks the data owner to check late records and assigns a program lead to review the process. The meeting notes say “investigate possible causes,” not “staffing caused the decline.”

**Knowledge check:** What makes a source of truth trustworthy? Why is a trend not a causal explanation? How should a prediction affect action?

**Answer cues:** Look for a documented definition, owner, refresh schedule, and controlled source. A trend describes change over time but does not isolate the cause. A prediction can prioritize review, with attention to validation, limits, false results, and human oversight. Learners should not treat a score as an automatic decision.

**Role transfer:** Before your next data meeting, write the decision question in one sentence and ask the metric owner to confirm the measure and period. Bring one chart with its counts and filters visible. At the meeting, assign someone to capture the observation, limitation, and next evidence request separately. Afterward, check whether the assigned action answered the original question. This small routine makes the decision traceable even when the analysis remains uncertain.

Leaders can strengthen this practice by rewarding accurate uncertainty. A presenter who says “we do not yet know why” may be giving the most useful account available. Avoid pressuring staff to produce a single explanation before the data support one. The team can still act: it can validate a record, review a process, or monitor a measure while holding off on a broader claim. Decisions should be proportionate to the evidence and revisited when new information arrives.

Keep a short decision log after the meeting: source and definition used, result discussed, limitation noted, action assigned, and date for review. This makes it easier to see whether new evidence changed the decision and to explain the reasoning to colleagues who were not present.

**Facilitator discussion:** Ask learners to present one chart in three statements: what it shows, what it cannot establish, and what question should come next. Invite a second learner to challenge the denominator or period. The presenter should either support the definition with the source or mark the question for follow-up.

**Action plan:** Find the owner of one real metric your team uses and confirm its definition before the next meeting. Continue with [Module 9](/modules/module-09).
