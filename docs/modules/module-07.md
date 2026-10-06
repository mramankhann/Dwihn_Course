# Module 7 · Genesys AI — Call Center Excellence

**Month 2: Advanced AI & Lumenore Mastery · Week 6 · [Session 8](/sessions/s08-genesys)**

## Topic introduction

The handbook introduces Agent AI, automatic call summaries, sentiment signals, and predictive routing. These capabilities can reduce repetitive work and surface useful cues, but they do not replace listening to the caller or following DWIHN's current service and escalation process. Availability and permission depend on the actual Genesys tenant, role, recording settings, and local procedures; all examples below are synthetic.

**By the end:** review AI suggestions and summaries, interpret sentiment cautiously, and describe a human fallback when routing does not fit a caller's needs.

## Point 1 · Agent AI insights and suggestions from calls

An agent-facing suggestion may point to a knowledge article, prompt a question, or organize possible next steps. It may also misunderstand speech, omit context, or surface an inapplicable article. The agent needs to confirm that the suggestion fits the caller's actual words, authorized information, and current procedure before using it. When a call involves urgent or sensitive needs, follow the established service and escalation protocol rather than deferring to a generated cue.

**Example:** A synthetic caller asks about a referral and the system displays a suggested article. The agent checks whether the article is current and relevant to the caller's situation, then explains the appropriate next step in their own words.

**Apply it:** During review, distinguish the **caller statement**, **system suggestion**, and **agent decision**. Do not document a suggestion as something the caller confirmed.

An agent-assistance panel may combine several kinds of information: a knowledge article, a suggested response, a reminder, or a summary of the current interaction. Each item needs its own check. Is the article current? Does it answer this caller’s question? Is the suggested wording consistent with the service process? Does the system have enough context, or is the caller explaining an exception the model cannot see? Treat the screen as a source of prompts for the agent’s attention, not as a script that must be followed.

The safest use often occurs between conversational turns or after a question, when the agent can check a suggestion without losing track of what the caller is saying. If the interface distracts from listening, the agent should follow the approved operational guidance for managing the interaction. Teams should also review recurring irrelevant suggestions with the product owner; an individual agent should not try to change system configuration unless authorized.

For training, label each sentence in a sample record as “caller said,” “system suggested,” or “agent confirmed.” This makes the boundaries visible. It also helps prevent a common documentation error: converting a model’s recommendation into a claim about what the caller requested or agreed to do.

## Point 2 · Review Auto Call Summary before saving

Automatic call summaries can create a first draft of notes, but transcription and summarization can miss names, dates, numbers, negation, commitments, or who said what. Compare the generated summary with the available authorized call record and the agent's direct understanding. Correct errors, preserve material caveats, and confirm actions and handoffs. The handbook's aspirational “stop manual note-taking” message still requires human validation of the final record.

**Example:** The synthetic summary says a referral was completed; the call only shows that an agent offered to start one. The agent edits the note to match the conversation and records the actual follow-up owner.

**Apply it:** Use a review list for **identity, request, action, outcome, outstanding need, and next owner**. Follow current recording and retention rules.

A call summary is a compressed account of a conversation, so it can lose the sequence that explains why an action occurred. Negation is especially easy to damage: “I do not want a call next week” must not become “call next week.” A summary may also confuse an offer with an acceptance, or report that a referral was made when it was only discussed. Check the source recording or authorized transcript where policy allows, and consult the agent’s contemporaneous notes when that is the approved reference.

Review should focus first on information that affects follow-up: the caller’s stated need, action taken, commitments, safety escalation, and unresolved issue. Then check names, dates, numbers, and attribution. Correct a model error before the note enters the official record; if the record has already been saved or used, follow the normal correction and incident process rather than silently replacing it.

Do not assume that every call should be recorded, transcribed, or summarized. Consent, notice, retention, access, and permitted use depend on the current DWIHN procedure and system configuration. A live demonstration should use a synthetic call or an approved training recording and should not display real member information to an unauthorized audience.

## Point 3 · Treat sentiment alerts as cues

Sentiment systems estimate tone from speech or text. They can miss sarcasm, language variation, distress expressed quietly, or context outside a short segment. A negative signal is not a diagnosis, measure of risk, or proof of intent. It may remind an agent to slow down, clarify the concern, and use the current escalation pathway where required. A missing alert does not mean the call is safe or resolved.

**Example:** A sentiment alert appears during a difficult synthetic call. The agent does not label the caller or change a service decision based on the score. They listen, ask a clarifying question, and follow the approved process for the concern described.

**Apply it:** In a role play, record what the caller actually said and the agent's response separately from the system signal.

Sentiment analysis estimates features of speech or text; it cannot directly observe a person’s internal state. Audio quality, background noise, language, accent, speech disability, cultural expression, and the selected model can affect the signal. A high or low score should not be treated as a clinical assessment, a reliable measure of intent, or a standalone reason to change access to service. Staff should respond to the caller’s words and established procedures.

Use the signal, when authorized and available, as a possible nudge: listen carefully, give the caller time, summarize what you heard, and ask whether you understood the concern. If the caller describes an urgent need, respond under the applicable protocol even if the dashboard shows no alert. If the alert seems inconsistent with the conversation, do not label the caller or repeat the score in a way that could bias another staff member.

After a training role play, compare three things: what the participant heard, what the indicator showed, and what the agent did. Ask whether the action would still make sense without the score. This helps ensure that the human response is grounded in the interaction and policy rather than in an unverified emotional label.

## Point 4 · Understand predictive routing and the human fallback

Routing aims to direct a call to an appropriate team based on configured rules or predictions. It can reduce transfers when configured well, but it can also send a caller to a path that does not fit their real need. Staff should know the intended routing goal, the local transfer and escalation options, and how to flag repeated mismatches for review. The actual inputs and logic must be confirmed with the DWIHN contact center owner.

**Example:** A synthetic call arrives in a routine information queue, but the agent learns the caller needs a different service path. They follow the approved transfer or escalation procedure and record the mismatch for the operations team.

**Apply it:** Map the handoff: **initial route → agent verification → correct path → documented outcome → improvement feedback**.

Predictive routing depends on a configured objective, available signals, and routing rules. The proposal names the concept but does not specify DWIHN’s model inputs or logic. Before training staff on a live route, the contact center owner should explain what the system is intended to optimize, which teams are in scope, what happens when information is missing, and how agents can override or correct a route. Staff should not infer the system’s reasoning from a single call.

Routing can improve efficiency while still creating uneven experiences. A call may be sent to the wrong queue because the caller’s need changed, the initial description was incomplete, or the model’s categories do not fit the situation. A human fallback is therefore part of the design. The agent needs a clear way to transfer or escalate, and operations staff need a way to detect repeated mismatches without blaming individual callers.

When evaluating routing, teams can review aggregate measures such as transfers, wait time, repeat contacts, and unresolved calls, provided the measures are defined and used under approved rules. A faster route alone does not prove better service. Pair efficiency measures with quality and access questions, and examine whether performance differs across groups before making a broad claim.

## Key takeaways

- AI suggestions support agents; they do not override the caller or policy.
- A generated call summary is a draft until an authorized person corrects it.
- Sentiment is a possible cue, not a diagnosis or automatic triage decision.
- Routing needs a clear human transfer or escalation path.

## Practical scenario and exercise

**Scenario:** A synthetic AI call summary looks useful but says an action was completed when the caller and agent only discussed it. A sentiment indicator also appears.

1. Identify the unsupported statement and rewrite the summary accurately.
2. List what must be checked before the note is saved or shared.
3. Explain how the sentiment cue could help attention without determining the caller's state.
4. Decide what the agent should do if the route is wrong or the need requires escalation.
5. Name the tenant settings or procedures the instructor must verify before a live demonstration.

**Worked walkthrough:** In a synthetic call, the caller says, “I might be able to attend on Tuesday, but I need to check with my ride.” The generated note reads, “Member confirmed Tuesday appointment.” Before saving, the agent corrects “confirmed” to “tentative,” preserves the transportation condition, and checks the appointment details through the authorized workflow. A sentiment alert appears, but the agent does not label the caller based on the score; they ask whether the caller wants help confirming transportation. If the call was routed to the wrong queue, they follow the transfer procedure. The reviewer can now distinguish what the caller said, what the system inferred, and what the agent did.

**Knowledge check:** Who validates the final call record? What can sentiment not establish? What is the fallback for a wrong route?

**Answer cues:** The authorized agent or designated reviewer checks the final record under local procedure. Sentiment cannot establish diagnosis, intent, or a definitive emotional state. A wrong route is handled through the approved transfer or escalation path. A good answer preserves the caller’s own words and does not turn the AI suggestion into a confirmed fact.

**Role transfer:** Contact center supervisors can reinforce these skills in ordinary quality review. Ask agents whether a summary preserved the caller’s stated need, whether suggestions matched the conversation, and whether the correct route was followed. Track recurring errors through the approved service-improvement process. Do not use an isolated sentiment score as a performance judgment or ask staff to share recordings outside the authorized review system.

The caller should not have to understand which parts of the interaction came from automation. They should receive a clear, respectful response that reflects what they actually asked for. If a system suggestion conflicts with the caller’s words, the agent should clarify the need and use the appropriate service process. The team can later examine whether the feature needs improvement, but the caller’s access and dignity remain central during the interaction.

**Facilitator discussion:** In the synthetic call exercise, ask one participant to act as the agent and another as the reviewer. The reviewer should mark where the AI summary is supported, where it is uncertain, and where the agent’s decision depends on the actual conversation. Discuss how the team would report a recurring system error through the approved product process.

**Action plan:** Review the locally approved summary and escalation process with the contact center owner. Continue with [Module 8](/modules/module-08).
