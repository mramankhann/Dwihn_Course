# Session 7 · Lumenore Impact: Smart Alerts and Board-Ready Reports

**Week 5 · Module 6, part 3 of 3 · Live demo + practice · At least one hour; Q&A included**

## Handbook module reading

Read [Module 6 - Lumenore Impact - Deep Dive](/modules/module-06) before this session. The module page provides the topic introduction, four detailed learning points with examples, key takeaways, and a practical scenario. Use this session page for the live demonstration and guided practice.

## Session flow

Plan for at least one hour, including Q&A. Extend teaching, discussion, or guided practice when learners need more time. Keep practice synthetic; optional reading and follow-up reflection can happen outside the live session.

| Sequence | Activity | Learner evidence |
|---|---|---|
| 1 | Welcome and retrieve one alert use case | Alert purpose |
| 2 | Teach threshold, owner, response, and review cycle | Draft alert rule |
| 3 | Instructor demonstrates a synthetic alert and report | Recipient and context checked |
| 4 | Create alert plan and leadership narrative | Alert and report brief |
| 5 | Review false-alarm and export risks | One safeguard identified |
| 6 | Q&A and next step | Questions answered or assigned |

## Why this matters

An alert can bring a change to the right person's attention; a board report can turn a chart into an accountable action. Both can also amplify a bad measure or disclose sensitive detail. Lumenore describes alerts, dashboards, and export/sharing capabilities publicly, but the DWIHN tenant, permissions, and release rules must be checked before live use. [Lumenore self-service analytics](https://lumenore.com/self-service-analytics/) · [Lumenore dashboards](https://lumenore.com/dashboards/)

## Outcomes and preparation

Design an alert with a meaningful threshold and owner, write a board-style narrative with source and uncertainty, and review an export for privacy and context. Bring the S6 dashboard and [analytics card](/resources/analytics-checklist).

## Teach: an alert is a workflow

An alert requires more than a threshold. Define **measure**, **comparison**, **minimum data volume**, **frequency**, **recipient**, **response**, and **closure**. Otherwise, teams either miss a signal or become numb to repeated notices.

| Alert element | Synthetic example |
|---|---|
| Measure | Seven-day follow-up rate, from the exercise definition |
| Trigger | Below 65% for two complete weekly periods, with at least 50 eligible cases per period |
| Recipient | Assigned program manager in the training scenario |
| First check | Confirm data completeness and calculation; inspect ZIP/service mix |
| Action | Convene a workflow review, not automatic member-level intervention |
| Closure | Record finding, owner, follow-up date, and whether the rate recovers |

The threshold above is **invented for practice** and is not a DWIHN KPI or operational alert rule. An alert can prioritize attention but cannot establish cause. If the true production measure is unstable or data arrive late, the alert should reflect that.

### Board-ready reporting

A good brief answers five questions: **What changed? How do we know? What might explain it? What will we do? When will we check again?** The synthetic table supports: “Overall follow-up moved from 74.5% to 73.0%, down 1.5 percentage points, with 400 eligible cases each quarter.” It does **not** support: “The decline was caused by scheduling.” That is a hypothesis to test.

Before exporting a chart or report, verify the latest data, period, denominator, labels, small cells, permitted audience, and version date. Keep the board narrative separate from any restricted member-level view.

## Instructor demonstration

Using a sandbox or paper template, configure an alert and show who receives it. Then export a synthetic chart and deliberately omit its date range. Ask learners to diagnose why the report could mislead. Add the source, definition, period, and privacy-safe breakdown to the final version.

## Guided practice
Draft a one-page board brief from [the synthetic table](/resources/synthetic-data):

1. Headline with the exact current and prior rates.
2. One chart or table with numerator and denominator.
3. One finding by ZIP and **two alternative explanations** to investigate.
4. A proposed action with owner and date.
5. One limitation or data-quality question.

Write an accompanying alert rule with an owner, response, and closure condition. Peer review using the [analytics checklist](/resources/analytics-checklist). The instructor scores the brief for traceable numbers, restrained claims, readability, privacy, and a clear next action.

### Knowledge check

What would you do if an alert fires during a known data-load delay? Why should a board chart include its denominator and date range?

<details><summary>Check your reasoning</summary>

Confirm data completeness before escalating a trend; the alert may need a data-quality hold. Denominator and date range show what was measured and whether comparisons are meaningful.

</details>

## Module 6 milestone

Submit the validated chart, alert design, and board narrative.

---

**Previous:** [Session 6 · Lumenore Impact: Dashboards and Service-Gap Analysis](/sessions/s06-lumenore-dashboards) · **Session 7 of 12** · **Next:** [Session 8 · Genesys AI — Call Center Excellence](/sessions/s08-genesys)
