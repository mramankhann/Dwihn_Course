# Five-part prompt builder

Classify the source and confirm the approved destination **before** filling this worksheet with real information.

| Part | Fill in |
|---|---|
| **Role** | “Act as a [writing / reporting / quality-review] assistant.” |
| **Task** | “Create [one specific output] for [audience and purpose].” |
| **Context** | “Use only the approved facts below: [minimal data].” |
| **Format** | “Return [headings, table, bullets, word limit].” |
| **Constraint** | “Do not invent facts or make an autonomous decision. Flag missing information.” |

## Copyable template

```text
Act as a [role].
Task: [specific work product and audience].
Context: Use only [approved, minimal facts].
Format: [structure, length, tone].
Constraints: Do not [unsafe action]. Mark missing or uncertain facts.
After drafting, list the facts a human must verify.
```

## Review the result

Mark each claim **confirmed**, **needs confirmation**, or **remove**. Compare numbers, dates, policy language, and names with the original source. Ask whether the draft discloses more than its audience may see. Save the edited version using normal DWIHN review and retention rules.

### Synthetic role examples

- **Coordinator:** Plain-language letter; do not invent appointment or service details.
- **Program manager:** Trend summary; state numerator, denominator, period, and uncertainty.
- **Call center:** Handoff note; preserve unresolved issues and avoid clinical judgment.
- **Admin:** Memo; cite the supplied policy version and mark missing approval.

See [S3](/sessions/s03-prompting) for before-and-after examples.
