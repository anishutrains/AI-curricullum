# Interview Playbooks

## System Design Playbook (45 min)

| Minute | Activity |
|--------|----------|
| 0–5 | Clarify users, scale, constraints, success metrics |
| 5–10 | High-level boxes: client, API, retrieval, LLM, data stores |
| 10–25 | Deep dive #1 (usually RAG or agent flow) |
| 25–35 | Deep dive #2 (scaling, security, or eval) |
| 35–40 | Failure modes + monitoring |
| 40–45 | Tradeoffs summary; ask clarifying questions |

**Phrases that signal seniority:**
- "I'd gate this prompt change with eval regression in CI."
- "Per-tenant vector isolation is non-negotiable for B2B."
- "I'd abstain below retrieval confidence 0.7."

## Coding Playbook

- Language: **Python** unless interviewer specifies
- Talk through: approach → complexity → edge cases → tests
- For AI companies: expect async HTTP, JSON parsing, simple data structures
- Practice on: LeetCode medium, focus arrays/hashmaps/graphs

## Prompt Engineering Interview

Often live: improve a broken support prompt.

**Process:**
1. Identify failure mode (verbosity, hallucination, tone)
2. Propose structured system prompt with boundaries
3. Add 2 few-shot examples
4. Define eval criteria (3 test cases)
5. Mention versioning and A/B plan

## Take-Home Playbook

See [15-interview-preparation-matrix.md](../15-interview-preparation-matrix.md).

**Submission email template:**
```
Subject: [Your Name] — Take-Home — [Role]

Attached/linked: repo, README, ASSUMPTIONS.md
Highlights:
• Core flow working in Docker
• Eval: faithfulness X on N cases
• Known limitations: [list]
Time spent: ~12h (honest)
```

## Post-Interview Debrief Template

| Question | Notes |
|----------|-------|
| Questions asked? | |
| What went well? | |
| Gaps exposed? | |
| Follow-up study? | |
| Thank-you sent? | |
