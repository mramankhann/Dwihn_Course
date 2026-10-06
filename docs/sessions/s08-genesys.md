# Session 8 · Genesys AI — Call Center Excellence

**Week 6 · Module 7 · Live session + Q&A · At least one hour; Q&A included**

## Handbook module reading

Read [Module 7 - Genesys AI - Call Center Excellence](/modules/module-07) before this session. The module page provides the topic introduction, four detailed learning points with examples, key takeaways, and a practical scenario. Use this session page for the live demonstration and guided practice.

## Session flow

Plan for at least one hour, including Q&A. Extend teaching, discussion, or guided practice when learners need more time. Keep practice synthetic; optional reading and follow-up reflection can happen outside the live session.

| Sequence | Activity | Learner evidence |
|---|---|---|
| 1 | Welcome; recall a human-review boundary | Boundary stated |
| 2 | Teach suggestions, summaries, sentiment, and routing limits | Signal-versus-decision notes |
| 3 | Instructor reviews a synthetic call summary | Correction demonstrated |
| 4 | Role-play summary review and wrong-route response | Corrected call record |
| 5 | Knowledge check and debrief | Escalation choice explained |
| 6 | Q&A and next step | Questions answered or assigned |

## Why this matters

The proposal highlights Genesys AI for call details, transcripts, automatic summaries, sentiment alerts, predictive routing, and knowledge support. These features can help staff find information and document a call, but availability depends on licensing, permissions, and configuration. Genesys documentation describes summary configuration, sentiment analysis, transcription, and routing capabilities; it does not establish what is active or permitted in the DWIHN tenant. [Genesys summary configuration](https://help.mypurecloud.com/articles/add-and-manage-an-ai-studio-summary/) · [Genesys sentiment](https://help.mypurecloud.com/glossary/live-sentiment-analysis/) · [Genesys transcription accuracy](https://help.mypurecloud.com/articles/improving-transcription-accuracy/)

## Outcomes and preparation

Review a synthetic interaction transcript and AI summary, distinguish a sentiment signal from a professional assessment, use a knowledge suggestion critically, and explain routing and escalation. The instructor must confirm enabled features and DWIHN call-handling policy before a live demo.

## Teach: the human-in-the-loop call

1. **Incoming interaction and routing.** Genesys may route a call based on configured rules or predictive routing where enabled. Staff still follow their queue and warm-transfer procedures. A routing suggestion is not proof of caller need.
2. **Transcript and assistance.** Voice transcription converts speech to text. Audio quality, accents, names, and domain terms can create errors. Knowledge suggestions may surface an article, but staff verify version and fit.
3. **Sentiment signal.** A model may flag negative emotional tone. It is a cue to listen carefully or seek support, **not a diagnosis, crisis classification, or substitute for trained judgment**.
4. **Auto summary.** A draft can capture reason for call, action, resolution, and open items. The agent checks it against the interaction and corrects errors before saving under DWIHN rules.
5. **Documentation and follow-up.** Record what actually happened, required handoff, and unresolved tasks in the approved system. Observe recording access and retention policy.

Genesys notes that an “Avoid PII” summary option may avoid common identifiers but does **not guarantee PII compliance**. Treat privacy settings as one control among authorization, configuration, and review. [Genesys summary documentation](https://help.mypurecloud.com/articles/add-and-manage-an-ai-studio-summary/)

## Synthetic practice call

> A caller asks how to arrange a routine follow-up appointment after discharge. The caller says, “I missed a call yesterday and I am worried I will lose the appointment.” The agent checks the current scheduling guidance, confirms a callback route, and does **not** promise a specific appointment. The AI transcript incorrectly says “I lost the appointment,” and the generated summary says, “Appointment booked.”

The transcript changes the caller's meaning, and the summary invents an outcome. A correct note would preserve the caller's concern, say what the agent actually checked, and leave the appointment status unresolved. The caller's worry merits attentive response; a sentiment label cannot determine what service or escalation is needed. If the call includes a crisis indicator, staff follow DWIHN's current crisis protocol immediately.

## Instructor demonstration

In an authorized sandbox, show the agent view and a **synthetic** recorded interaction. Point out where a transcript, article suggestion, sentiment signal, and summary would appear **if enabled**. Demonstrate a correction and feedback route. If a feature is unavailable, use the printed case; do not present an invented control as a DWIHN screen. Show the permitted knowledge-base article and its version date.

## Guided practice
Working in pairs, compare the synthetic call with this AI draft:

> “Caller lost a discharge follow-up appointment. Agent booked a new appointment. Caller was angry. No further action needed.”

Mark every unsupported claim. Rewrite under four headings: **reason for call**, **facts confirmed**, **action taken**, **open item / handoff**. Add one sentence explaining how you would respond to a negative sentiment alert without allowing it to override the actual call content. Identify who must verify a predictive routing change in the contact center, rather than changing it as an agent.

### Knowledge check

1. Can a sentiment flag establish a caller's clinical condition or crisis level?
2. When may an agent save an auto summary without checking it against the interaction?
3. What could make a transcript unreliable?

<details><summary>Check your reasoning</summary>

1. No. It is an imperfect cue; trained staff apply the current call and crisis protocols.
2. Do not treat it as final without the required human review and documentation process.
3. Audio quality, dialect, names, background sound, and configuration can change transcription accuracy.

</details>

## Takeaway and work product

Keep the corrected summary and an error log.

---

**Previous:** [Session 7 · Lumenore Impact: Smart Alerts and Board-Ready Reports](/sessions/s07-lumenore-alerts) · **Session 8 of 12** · **Next:** [Session 9 · Objective Decisions with Data: A Single Source of Truth](/sessions/s09-objective-data)
