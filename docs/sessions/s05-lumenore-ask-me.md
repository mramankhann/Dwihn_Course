# Session 5 · Lumenore Impact: Ask Me and Trustworthy Questions

**Week 4 · Module 6, part 1 of 3 · Live demo + practice · At least one hour; Q&A included**

## Handbook module reading

Read [Module 6 - Lumenore Impact - Deep Dive](/modules/module-06) before this session. The module page provides the topic introduction, four detailed learning points with examples, key takeaways, and a practical scenario. Use this session page for the live demonstration and guided practice.

## Session flow

Plan for at least one hour, including Q&A. Extend teaching, discussion, or guided practice when learners need more time. Keep practice synthetic; optional reading and follow-up reflection can happen outside the live session.

| Sequence | Activity | Learner evidence |
|---|---|---|
| 1 | Welcome and recap the measure-validation loop | Question recalled |
| 2 | Teach measure, population, period, comparison, and breakdown | Scoped question |
| 3 | Instructor Ask Me demonstration and filter inspection | Validation steps observed |
| 4 | Learner question writing and synthetic result review | Question and validation log |
| 5 | Check denominator, filters, and uncertainty | Corrected interpretation |
| 6 | Q&A and next step | Questions answered or assigned |

## Why this matters

Lumenore's public documentation describes **Ask Me** as a way to ask governed data questions in natural language and receive tables, charts, or narratives. The proposal positions Lumenore Impact as a primary DWIHN analytics tool. The live dataset, measure names, permissions, and interface must be confirmed in DWIHN's environment before training. A natural-language answer is useful only when the underlying measure and filter answer the intended question. [Lumenore self-service analytics](https://lumenore.com/self-service-analytics/)

## Outcomes and preparation

Write a scoped question, inspect its result, ask a follow-up, and record the source, measure, denominator, date range, filters, and uncertainty. Read the [synthetic practice data](/resources/synthetic-data) and [analytics review card](/resources/analytics-checklist).

## Teach: from a vague request to a data question

“How are we doing?” leaves the system to guess the measure, population, and period. A better question states **metric + population + period + comparison + breakdown**. For example:

> “Using the synthetic follow-up dataset, show the seven-day follow-up rate for qualifying discharges in the current quarter, compared with the prior quarter, by ZIP code. Include numerator and denominator.”

This wording still needs verification. The phrase “follow-up rate” could map to more than one organizational definition. A chart can be correct for a selected dataset but irrelevant to the decision. Ask Me can help discover an answer; it does not replace the data dictionary or the person who owns the measure.

### The Ask Me validation loop

1. **Ask.** State the measure and comparison clearly.
2. **Inspect.** Read the chart title, axis, units, source, date range, filters, numerator and denominator.
3. **Challenge.** Ask a follow-up such as “Show the underlying counts” or “Which filters are active?”
4. **Compare.** Check a known report or independently calculate a sample rate.
5. **Record.** Save the question, view, validation, uncertainty, and intended decision.

For the synthetic table, `292 ÷ 400 = 73.0%`. A result of 73% is plausible only if the platform used the same 400 qualifying records and period. If it reports 74%, investigate instead of “rounding away” the discrepancy.

## Instructor demonstration

In an authorized sandbox, show where to enter a question, inspect the answer, and refine it. If a live sandbox is unavailable, use the [synthetic table](/resources/synthetic-data) as a paper demonstration. Narrate each validation step. Ask first for the overall current-quarter rate, then “show numerator and denominator,” then “break down by ZIP.” Do not enter member-level records into the training demonstration.

## Guided practice
Working with a partner, write three questions for the synthetic data:

1. A **description** question: What is the current overall rate?
2. A **comparison** question: How did the rate change from the prior quarter by ZIP?
3. An **investigation** question: Which data or process checks would help explain the change in 48205?

For each, complete a validation log with **exact wording**, **measure definition**, **period**, **filters**, **counts**, **observed result**, **possible alternative explanation**, and **person to consult**. The third question should yield a plan to investigate, not a confident causal claim.

### Knowledge check

1. What is the difference between “the rate fell by 1.5%” and “the rate fell by 1.5 percentage points” here?
2. What should you do if Ask Me's rate differs from your manual calculation?

<details><summary>Check your reasoning</summary>

1. The synthetic rate moves from 74.5% to 73.0%, a 1.5 **percentage-point** decline. A relative percent change would be about 2.0% of the original rate.
2. Check denominator, period, filters, definition, data freshness, and rounding; then consult the data owner if unresolved.

</details>

## Takeaway and work product

Keep one validated question and its log.

---

**Previous:** [Session 4 · AI in Your Daily DWIHN Work](/sessions/s04-daily-work) · **Session 5 of 12** · **Next:** [Session 6 · Lumenore Impact: Dashboards and Service-Gap Analysis](/sessions/s06-lumenore-dashboards)
