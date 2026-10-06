# Module 6 · Lumenore Impact — Deep Dive

**Month 2: Advanced AI & Lumenore Mastery · Weeks 4–5 · [Sessions 5–7](/sessions/s05-lumenore-ask-me)**

## Topic introduction

The handbook uses Lumenore Impact to teach a full analytics cycle: ask a focused question, build a decision-led dashboard, examine a possible ZIP-level service gap, and create useful alerts and reports. These lessons can be completed with the [synthetic practice dataset](/resources/synthetic-data). For a live demonstration, the instructor must verify DWIHN's enabled features, authorized dataset, measure definitions, filters, and export rules.

**By the end:** produce a scoped data question, validate a view, interpret a geographic difference with caution, and design an alert with an owner.

## Point 1 · Ask Me: type useful questions and read results

Natural-language analysis still depends on precise business language. Specify the **measure, population, period, comparison, and breakdown**. After a result appears, inspect source, active filters, numerator, denominator, units, freshness, and any exclusions. A correct-looking chart can answer a different question if “follow-up” or “current quarter” maps to another definition. Ask a follow-up for underlying counts and compare with a trusted report or manual sample calculation.

**Example:** Instead of “How are we doing?”, a manager asks, “For the synthetic program table, what share of qualifying records has a seven-day follow-up this quarter versus last quarter? Show counts and rates by ZIP.” They check that the displayed totals match the table and record any discrepancy.

**Apply it:** Save the exact question and validation log. See [S5](/sessions/s05-lumenore-ask-me) for the guided Ask Me exercise.

Natural-language analytics reduces the amount of query syntax a user must learn, but the user still needs to understand the measure. “Follow-up rate” may refer to different populations, windows, or events. Before asking, find out what decision the answer should support and how the metric is defined. Then phrase the question so the output can be compared with that definition. If a phrase such as “recently” or “successful” has no agreed meaning, replace it with the actual period or outcome rule.

Read the returned result in its full context. A percentage without a denominator conceals volume. A trend line may omit dates with missing data. A map can reflect the selected location field rather than where a service was delivered. Filters may persist from a prior question. Check the title, source, date range, refresh time, active filters, units, and inclusion rules before interpreting the display. If the system provides a narrative, treat it as another generated output that may omit a caveat.

When a result differs from a trusted report, do not immediately assume that one tool is broken. Compare the metric definitions and periods; check exclusions, late-arriving data, duplicate records, and rounding; then calculate a small sample if permitted. Document the discrepancy and send unresolved questions to the data owner. The purpose of validation is not to force the numbers to agree but to understand what each one represents.

## Point 2 · Build your first program dashboard

A dashboard should support a recurring decision, not show every available measure. Begin with the meeting question and select a small set of KPIs that answer it. Define each measure and denominator, use consistent periods, label targets and units, and show enough context to prevent a misleading trend. Identify who can view, edit, or export it. Product configuration may vary, so the learning outcome is a **dashboard specification** even when live build access is unavailable.

**Example:** A program team needs to monitor a synthetic follow-up rate. Its dashboard shows the current rate, previous period, numerator and denominator, a simple trend, and a note about data freshness. The team removes a decorative chart that does not help decide what to investigate.

**Apply it:** Sketch the page, label every metric and filter, and ask a peer what decision they would make from it. See [S6](/sessions/s06-lumenore-dashboards).

Dashboard design begins with a question the team asks repeatedly: “Are follow-ups happening within the agreed window?” or “Where should we investigate a change in demand?” Choose measures only when they help answer that question. A collection of charts without a decision purpose makes it difficult to see what deserves attention. Keep labels plain, identify the unit, and show comparison periods that make sense for the work. Where helpful, include counts alongside rates and annotate known data limitations.

Filters are part of the meaning of a dashboard. If a user selects a program, region, or date period, the display may change while the title stays the same. Make active filters visible and establish a reset state for meetings. Confirm refresh timing and ownership so users know whether the dashboard reflects the latest available records. A dashboard with stale data may be visually convincing and still be unsuitable for a current operational decision.

Before building a live dashboard, confirm who may see it and whether exporting, emailing, or taking screenshots is allowed. A view that is appropriate inside an authorized analytics environment may expose sensitive detail if exported to a broad audience. The course’s paper sketch asks learners to design a useful view without assuming access to the DWIHN tenant or to any specific feature.

## Point 3 · Analyze service gaps by ZIP code

A ZIP-level difference can signal a question, not prove a cause. Compare rates with their counts and denominators, check whether populations and periods are comparable, and consider small-cell privacy risk. A dark map color can exaggerate a tiny change or hide low volume. Investigate possible differences in demand, access, data completeness, or referral process before recommending action. Avoid implying that a neighborhood or member group is responsible for an observed pattern.

**Example:** Two synthetic ZIPs show different follow-up rates. One has a much smaller denominator. The team flags the difference for review, checks whether the metric uses the same eligibility rule in both places, and withholds a member-level breakdown from a broad slide deck.

**Apply it:** Write **observation → validation → alternative explanations → next data request**, then choose a proportionate follow-up.

Geographic comparison needs particular care because location can stand in for many things at once: population size, service availability, referral patterns, transportation, data completeness, or eligibility mix. The map shows a pattern in the selected dataset; it does not tell the team which explanation is correct. Compare rates and counts, examine the time period, and check whether ZIP assignment is complete and consistent. If the metric is based on small numbers, a single event may move the rate substantially.

Avoid language that turns a descriptive difference into a judgment about residents or staff. “The synthetic dataset shows a lower recorded follow-up rate in this ZIP during the period” is an observation. “Residents in this ZIP do not follow up” is an unsupported explanation and may unfairly assign responsibility. Ask what process or data checks would distinguish among explanations before proposing an intervention.

Small cells deserve a privacy check even when names are absent. The appropriate threshold and disclosure rule must come from DWIHN policy; this lesson does not invent one. If a result may identify a person or sensitive group, use an approved reporting method or withhold the breakdown while consulting the data or privacy owner. More detail is not always better analysis.

## Point 4 · Set smart alerts and export board-ready reports

An alert needs a meaningful threshold, period, recipient, owner, and planned response. Test how often it would fire against historical synthetic data; noisy alerts lose value. For a board or leadership report, state the measure definition, period, comparison, key observation, limitation, and proposed next step. Check the export for filters, labels, small cells, and approved audience. A report is ready when a reader can understand what changed and what remains uncertain.

**Example:** A team proposes an alert when the synthetic follow-up rate stays below a chosen threshold for two reporting periods. A named analyst checks data freshness first, the program lead investigates process factors, and the board brief states the threshold is a **training proposal**, not a DWIHN operating target.

**Apply it:** Draft the alert rule and a five-sentence decision brief. See [S7](/sessions/s07-lumenore-alerts).

An alert is a small operating agreement. The threshold says what change deserves attention; the owner says who receives it; the response says what that person should do; and the review says how the team will decide whether the alert remains useful. Before activation, test the rule against historical or synthetic data. If it fires every day, it may create noise. If it depends on a single low-volume fluctuation, it may send staff after ordinary variation. Calibrate only with the authorized data owner and program lead.

A leadership report should help a reader understand the signal without overstating it. Include the metric definition, the period, numerator and denominator where relevant, the comparison, and any important caveat. Then say what decision or investigation is proposed. Separate these sentences: “The rate changed” (observation), “The change may reflect incomplete records” (possible explanation), and “The analyst will confirm the denominator by Friday” (next action). This structure supports a useful discussion without pretending the cause is known.

Before exporting, inspect the file as a separate artifact. Check that titles and filters remain visible, that private notes or hidden tabs are not included, and that the audience is authorized. Follow the data owner’s rules for board materials and sensitive cells. A dashboard’s share button does not itself grant permission to distribute every view.

## Key takeaways

- A useful Ask Me question identifies the measure, population, period, and comparison.
- Validate counts, definitions, filters, and freshness before presenting a result.
- Geographic patterns and predictions prompt investigation; they do not establish cause.
- Every alert needs an owner and response, and every report needs decision context.

## Practical scenario and exercise

**Scenario:** Your program team sees a change in one KPI in the synthetic dataset and wants a concise explanation for a meeting.

1. Write a focused Ask Me question and list the filters and definitions you will check.
2. Sketch a dashboard with no more than four decision-relevant measures.
3. Compare two ZIP-level results with their denominators; write what the difference does **not** prove.
4. Design one alert with threshold, owner, review action, and false-alarm check.
5. Draft a board-style paragraph: observed result, validation, limitation, and proposed next step.

**Worked walkthrough:** A synthetic result shows 73% for the current period. Before writing “performance improved,” the analyst asks for the numerator and denominator, checks the reporting window, and confirms which records qualify. The count is 292 of 400. A second view shows 74% because its filters exclude a subgroup; neither number should be chosen until the metric owner confirms which definition supports the meeting. The analyst then checks whether ZIP-level cells are large enough for the intended report. The final brief says which validated view was used, what changed, what remains uncertain, and who will investigate the difference. It does not claim a service cause from a chart alone.

**Knowledge check:** Why request numerator and denominator? What can a ZIP map show? What makes an alert actionable?

**Answer cues:** Counts expose the volume behind a rate and can reveal denominator mismatches. A map shows a geographic pattern in the selected data, not why that pattern exists. An alert needs a meaningful condition, an owner, a response, and a review plan. Accept alternate dashboard designs when their measures support the stated decision and their limitations are visible.

**Role transfer:** Before a live analytics demonstration, have the program owner select one approved measure and provide its definition, data source, refresh schedule, and permitted audience. Ask the instructor to repeat the same question with a changed period or filter so learners can see what changes in the result. This makes the validation habit concrete and helps distinguish a general product capability from a feature that has been configured and approved for DWIHN use.

**Facilitator discussion:** Have participants exchange their dashboard sketches and ask one another to identify the question each chart answers. If a peer cannot tell what decision the view supports, remove or relabel the chart. For the ZIP case, require every group to state both an observation and one explanation they cannot yet claim.

**Action plan:** Identify the real measure owner and approved training environment before a live Lumenore task. Continue with [Module 7](/modules/module-07).
