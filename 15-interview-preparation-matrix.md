# 15. AI Engineer Interview Preparation Matrix

## Interview Types × Preparation

| Type | Weight (Typical) | Prep Resource | Practice Frequency |
|------|------------------|---------------|-------------------|
| **AI System Design** | 30–40% | Module 11, this matrix | 2 mocks/week |
| **Coding (Python)** | 20–30% | LeetCode medium + async I/O | 3 problems/week |
| **Project Deep-Dive** | 20–30% | Portfolio READMEs, ADRs | 1 rehearsal/week |
| **Prompt / LLM Technical** | 10–15% | Modules 02–03 | 1 session/week |
| **Behavioral** | 10–15% | STAR stories from projects | 1 session/week |
| **Take-Home** | Varies | 48h time-box strategy below | 1 full simulation |

---

## System Design Question Bank

| Question | Key Points to Cover |
|----------|-------------------|
| Design enterprise Slack copilot | Auth, RAG on Confluence, tool calls, rate limits, eval |
| Design customer support AI | Triage graph, HITL, CRM integration, CSAT loop |
| Design multi-tenant RAG SaaS | Index isolation, ACL sync, metering, onboarding |
| Scale RAG to 1M docs | Async ingest, sharded indexes, cache, rerank budget |
| Design agent for code review | Sandbox, diff-only tools, CI integration, audit |
| Multi-region AI deployment | Data residency, model routing, failover |
| Reduce LLM costs 50% | Router, cache, smaller models, batch embed |

**Framework:** Requirements → NFRs (scale, latency, cost) → High-level diagram → Deep dives (2) → Tradeoffs → Failure modes.

---

## Coding Focus Areas

| Topic | Example Problems |
|-------|------------------|
| Async Python | Concurrent API calls with semaphore |
| String/JSON | Parse nested LLM JSON safely |
| Hash maps | Token counting, rate limiter |
| Trees/graphs | Workflow DAG validation |
| System | Implement LRU cache for embeddings |

*AI roles still test CS fundamentals—do not skip coding prep.*

---

## Prompt / LLM Interview Questions

1. Difference between temperature, top_p, and seed?
2. When RAG vs fine-tuning vs long-context?
3. How do you detect and reduce hallucinations?
4. Explain tool calling loop termination conditions.
5. How do you evaluate prompt changes before production?
6. What is DSPy and when would you use it?
7. Explain embedding model change migration.
8. How do you handle PII in prompts and logs?

---

## Project Deep-Dive Script (10 min)

1. **Problem** (30s): Who is the user, what pain?
2. **Architecture** (3 min): Diagram walkthrough
3. **Technical decisions** (3 min): 2 ADRs explained
4. **Metrics** (2 min): Eval scores, latency, cost
5. **Failures** (1 min): What broke, what you fixed
6. **Next scale step** (30s): 10× traffic plan

---

## Take-Home Strategy (48-Hour Standard)

| Hour Block | Activity |
|------------|----------|
| 0–2 | Read spec; clarify assumptions in README |
| 2–8 | MVP: core happy path only |
| 8–16 | Eval + one production practice (Docker or test) |
| 16–24 | Polish README, architecture diagram |
| 24–36 | Security pass + edge cases |
| 36–44 | Buffer for bugs |
| 44–48 | Submit + short Loom walkthrough (optional, high impact) |

**Do:** Time-box, document tradeoffs, include `ASSUMPTIONS.md`  
**Don't:** Over-scope agents; skip README; submit without running tests

---

## Behavioral STAR Stories (Prepare 5)

| Story | Situation | Use For |
|-------|-----------|---------|
| Shipped RAG under deadline | Eval tradeoff | Delivery |
| Production incident | Hallucination / outage | Ownership |
| Disagreed on model choice | ADR process | Collaboration |
| Learned new framework fast | LangGraph sprint | Adaptability |
| Reduced AI costs | FinOps win | Business impact |

---

## Mock Interview Schedule (4 Weeks Pre-Apply)

| Week | Activity |
|------|----------|
| 1 | System design mock #1 + coding ×3 |
| 2 | Project deep-dive recording + prompt quiz |
| 3 | System design mock #2 + take-home simulation |
| 4 | Full loop mock (design + coding + behavioral) |

---

## Company-Type Adjustments

| Company | Emphasize |
|---------|-----------|
| FAANG | System design scale, coding, metrics |
| Startup | Shipping speed, breadth, product sense |
| Enterprise | Security, compliance, integration |
| Consulting | Communication, POC scoping, ROI |
| AI Vendor | Ecosystem depth, DX, OSS |

---

*Job readiness playbooks: [job-readiness/README.md](./job-readiness/README.md)*
