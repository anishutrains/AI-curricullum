# Module 12 — Capstone & Job Readiness
### Zero-to-Hero Track · Weeks 49–52 · Ship Your Flagship Project and Launch Your AI Career

---

## Why This Module Matters

**Why learn this NOW?**  
Modules 01–11 gave you skills. Module 12 converts skills into **employment**: one flagship project, polished portfolio, interview mastery, and a 30-day job search plan.

**What hiring managers actually hire**
- **One exceptional project** beats ten tutorial repos.
- **Metrics in README** (faithfulness, latency, cost) beat buzzwords.
- **System design + take-home execution** beat ML theory trivia for AI Engineer roles.

**Salary impact:** Strong capstone + interview prep unlock **$120K–$220K+** first US AI Engineer roles (remote/hybrid, 2026–2027). Consultants: portfolio = lead generation.

---

## How This Module Fits into the AI Engineering Journey

| Modules 01–11 | Module 12 |
|---------------|-----------|
| Skills + partial projects | **One integrated flagship** |
| Module exercises | **Enterprise readiness checklist** |
| Topic interviews | **Full job search system** |

**Prerequisites:** Module 04 minimum complete before capstone start. Ideally Modules 01–11 exercises integrated into capstone.

---

## Job Roles This Module Prepares Students For

**All roles** — choose capstone vertical aligned to target:

| Capstone Project | Target Role |
|------------------|-------------|
| Enterprise RAG Assistant | RAG / Enterprise AI Engineer |
| AI Customer Support System | Conversational / Agentic AI |
| AI Coding Copilot | Copilot Engineer |
| Autonomous Research Agent | Agentic AI Engineer |
| Multi-Agent Finance Analyst | Applied AI / Finance |
| AI Healthcare Assistant | Enterprise + Compliance |
| AI Legal Document Analyzer | Applied AI / Legal tech |
| AI Cybersecurity Analyst | AI Security Engineer |
| Multimodal AI Search Engine | AI Product / Full Stack |
| AI Workflow Automation Platform | Workflow / Automation Engineer |

Also: **AI Consultant**, **Freelancer**, **Founder** — same portfolio, different go-to-market.

---

## Beginner Skills Students Will Learn

- Select capstone using rubric (scope, role alignment, feasibility)
- Sprint plan 4 × 1-week iterations
- Write README recruiters actually read
- Record 2-minute demo video

## Intermediate Skills Students Will Learn

- Pass architecture + security review checkpoints
- Meet enterprise readiness checklist
- Present capstone in 10-minute format
- Optimize resume and LinkedIn for AI roles

## Advanced Skills Students Will Learn

- Mock system design interviews (3+ sessions)
- Complete take-home in 48h with eval README
- Negotiate offer basics (levels.fyi research)

## Production Enterprise Skills Students Will Learn

- Executive summary PDF for non-technical stakeholders
- Open-source strategy for portfolio components
- Referral networking and targeted applications (10–15/week)
- Freelance/consulting proposal from capstone case study

---

# Topic 12.1 — Capstone Project Execution

## Beginner-Friendly Explanation

**Capstone** = your **masterpiece** — one end-to-end AI system proving you can ship like a professional: code, deploy, measure, document, secure.

**Not a capstone:** Jupyter notebook, localhost-only demo, no eval metrics, no README diagram.

## Why This Topic Matters in Real Companies

Hiring managers use capstone to answer: *"Can this person do the job on day one?"* — substitutes for 6–12 months junior experience when executed well.

## Problems This Topic Solves

- Scattered tutorial projects that don't tell a story
- Starting capstone too early (before RAG works)
- No eval/security/deploy → instant reject

## Learning Outcome

Public GitHub flagship repo meeting full enterprise readiness checklist + demo video + blog post.

---

### Lesson 12.1.1 — Concept: Capstone Selection Rubric

**Score each 1–5:**

| Criterion | Question |
|-----------|----------|
| Role alignment | Does this match jobs I'm applying to? |
| Scope control | Can I ship MVP in 4 weeks? |
| Differentiation | Eval + deploy + enterprise angle? |
| Story | Can I explain problem → solution → metrics? |
| Foundation ready | Is Module 04 RAG working? |

**Pick ONE primary capstone.** Secondary mini-projects OK; one repo pinned.

---

### Lesson 12.1.2 — Beginner: 4-Week Sprint Plan

| Sprint | Goal | Deliverable |
|--------|------|-------------|
| **Week 49** | Core pipeline works | RAG/agent API + basic UI |
| **Week 50** | LLMOps + eval | Langfuse, golden set, CI gate |
| **Week 51** | Enterprise hardening | Multi-tenant OR compliance OR cloud deploy |
| **Week 52** | Polish + launch | README, video, blog, apply |

**Daily:** Commit code. **Weekly:** Architecture checkpoint with peer or mentor.

---

### Lesson 12.1.3 — Intermediate: Architecture Review Checkpoint

**Review agenda (60 min):**
1. C4 container diagram walkthrough
2. Data flows + tenant isolation
3. Failure modes
4. Cost estimate at 10× scale
5. Action items before security review

**Deliverable:** `/docs/architecture-review-notes.md`

---

### Lesson 12.1.4 — Intermediate: Security Review Checkpoint

**Checklist:**
- [ ] OWASP LLM top risks addressed
- [ ] API keys server-side only
- [ ] Rate limits + budget caps
- [ ] THREAT_MODEL.md
- [ ] Guardrails tested in CI

**Connect Module 10.**

---

### Lesson 12.1.5 — Advanced: Eval Gate Before Launch

**Block launch if:**
- Faithfulness < 0.80 on golden set (adjust per domain)
- p95 latency > target
- Red team pass rate < 80%

**Ship with metrics visible** — honesty builds trust.

---

### Lesson 12.1.6 — Production: Demo Video and Technical Blog

**Demo video (2–3 min):**
- Problem (15 sec)
- Live demo (90 sec)
- Architecture + metrics (30 sec)
- Call to action (GitHub link)

**Blog post:** "How I built X — lessons learned" — publish on Dev.to/Medium/LinkedIn within 2 weeks of finish.

**Recruiter tip:** Pin video above fold in README.

---

### Lesson 12.1.7 — Enterprise: Executive Summary PDF

**1-page for non-technical sponsor:**
- Business problem
- Solution overview
- Key metrics (faithfulness, cost/query, users supported)
- Risks and mitigations
- Next steps for production

**Consulting skill:** Same doc wins client sign-off.

---

### Topic 12.1 — Enterprise Readiness Checklist (Required)

**Code & deploy**
- [ ] Public GitHub repo (MIT or Apache-2.0)
- [ ] Deployed URL OR Docker one-command + video proof
- [ ] Architecture diagram (C4 container)

**Quality & ops**
- [ ] Eval metrics in README (faithfulness, latency, cost/query)
- [ ] Langfuse trace screenshot or equivalent
- [ ] CI: eval gate on PR

**Enterprise**
- [ ] `SECURITY.md` + `COMPLIANCE.md` (as applicable)
- [ ] Multi-tenant test OR abstention logic OR cloud deploy
- [ ] Runbook for one failure scenario
- [ ] Model card or prompt CHANGELOG

**Presentation**
- [ ] Demo video/GIF
- [ ] Executive summary PDF
- [ ] 10-minute presentation script practiced

**See also:** [08-project-portfolio.md](../08-project-portfolio.md)

---

# Topic 12.2 — Job Search, Interviews & Career Launch

## Beginner-Friendly Explanation

**Job search is a system**, not luck: portfolio → targeted applications → interviews → negotiation.

**Interview types for AI Engineer (2026–2027 US market):**
1. **Recruiter screen** — story, visa, comp expectations
2. **Technical phone** — Python, APIs, RAG/agent concepts
3. **System design** — whiteboard AI platform (45 min)
4. **Take-home** — build small feature in 24–48h
5. **Behavioral** — STAR stories from capstone

## Learning Outcome

Hire-ready resume + LinkedIn + 3 pinned repos + 3 mock interviews + 30-day job plan.

---

### Lesson 12.2.1 — Beginner: AI Resume That Gets Interviews

**Format (1 page for <10 years exp):**

```
Name | AI Engineer | city | email | github | linkedin

SUMMARY (2 lines)
Built production RAG copilot — 0.87 faithfulness, $0.008/query, deployed on AWS.

EXPERIENCE (impact bullets)
• Designed multi-tenant RAG API serving 3 doc collections with ACL-aware retrieval
• Reduced inference cost 35% via semantic cache + model routing

PROJECTS (capstone featured)
Enterprise RAG Assistant | Python, FastAPI, Langfuse, Pinecone
• 100-case eval suite; faithfulness 0.87; p95 latency 2.1s
• github.com/you/project | demo video link

SKILLS
Python, FastAPI, RAG, LangGraph, AWS Bedrock, Terraform, Ragas, Next.js
```

**Rules:** Metrics > adjectives. No "passionate about AI." No 20-line skills cloud.

---

### Lesson 12.2.2 — Beginner: GitHub Portfolio Curation

**Pin 3 repos:**
1. Flagship capstone
2. Strong module project (agent or LLMOps)
3. Smaller focused demo (optional)

**Each README must have:**
- One-line problem statement
- Architecture diagram
- Metrics or eval scores
- Quick start (docker compose up)
- Demo link/video

**Remove or archive:** Incomplete tutorials, empty repos, course homework clones.

---

### Lesson 12.2.3 — Intermediate: LinkedIn Optimization

**Headline:** `AI Engineer | RAG & Agents | FastAPI, LangGraph, AWS | Open to remote US roles`  
**Featured:** Capstone demo video, blog post, architecture PDF  
**About:** 3 paragraphs — what you build, capstone metrics, what you're seeking  
**Activity:** Comment thoughtfully on AI eng posts 2×/week — visibility.

---

### Lesson 12.2.4 — Intermediate: System Design Interview Mastery

**Practice schedule (2 weeks):**
- 6 mocks × 45 min
- Excalidraw or whiteboard only
- Record yourself; review pacing

**Common prompts:**
- Design customer support AI for e-commerce
- Design internal knowledge copilot for 10K employees
- Design code review agent for GitHub

**Framework:** Clarify → estimate → diagram → deep dive → tradeoffs → failures

**Resources:** [15-interview-preparation-matrix.md](../15-interview-preparation-matrix.md), [job-readiness/](../job-readiness/)

---

### Lesson 12.2.5 — Intermediate: Coding Interview (Still Required)

**AI roles still test:** Python fundamentals, async, data structures, API design  
**Practice:** 50 LeetCode easy/medium (arrays, hash maps, strings) — 30 min/day  
**AI-specific live coding:** Implement tool-calling loop, simple RAG retrieve function

**Don't over-index on ML math** for AI Engineer (Applied Scientist different).

---

### Lesson 12.2.6 — Advanced: Take-Home Assignment Strategy

**When assigned (24–48h):**
1. Read requirements twice; ask 2 clarifying questions early
2. Time-box: 60% core feature, 20% tests/eval, 20% README
3. Ship working MVP — partial beats broken ambitious
4. README: assumptions, tradeoffs, what you'd do with more time
5. Include eval or test for AI behavior

**Red flags to avoid:** Missing README, no tests, scope creep, late submit without communication.

---

### Lesson 12.2.7 — Advanced: Behavioral Interviews (STAR)

**Prepare 5 stories from capstone:**
- **Conflict:** Disagreement on architecture choice — data-driven ADR resolved it
- **Failure:** Eval regression caught in CI — rollback and fix
- **Leadership:** Drove security review across team (solo OK — "self-directed")
- **Impact:** Cost reduced 35%, documented in README
- **Learning:** Started as beginner, shipped enterprise checklist

**Format:** Situation → Task → Action → Result (with metrics)

---

### Lesson 12.2.8 — Production: Negotiation and Leveling Basics

**Research:** levels.fyi, Glassdoor, job posting range  
**Negotiate:** Total comp — base, bonus, equity, signing  
**Scripts:** "Based on market data and the scope of this role, I was targeting X–Y."  
**Remote:** Confirm timezone expectations, equipment stipend.

---

### Lesson 12.2.9 — Enterprise: Multiple Career Paths

| Path | Go-to-market |
|------|--------------|
| **Full-time US remote** | 10–15 targeted apps/week; referrals via OSS/blog |
| **Contract (Corp-to-corp)** | Toptal, Catalant, LinkedIn contract filters |
| **Freelance** | Upwork enterprise POCs; capstone as case study |
| **Consulting** | Module 07 POC proposal template → $5K–$50K engagements |
| **Startup** | Module 09 SaaS MVP → YC/indie hacker / vertical SaaS |

**30-day job search plan template:**

| Week | Actions |
|------|---------|
| 1 | Finalize capstone README + video; resume/LinkedIn |
| 2 | 10 applications; 2 mock interviews; 1 blog post |
| 3 | 15 applications; take-home if assigned; network 5 people |
| 4 | Follow-ups; second-round prep; negotiate first offer |

---

### Topic 12.2 — Interview Question Bank (Sample)

**Beginner**
- What is RAG? Agent vs chain?
- How do you know your chatbot works?

**Intermediate**
- Design eval pipeline for production RAG.
- How deploy prompt change safely?

**Advanced / System design**
- Multi-tenant RAG for 1000 B2B customers.
- AI bill went 10× — diagnose and fix.

**Prompt engineering live**
- Improve this system prompt for faithfulness.
- Detect and mitigate injection in this example.

---

# Module 12 — Final Deliverables Summary

## You Graduate When You Have:

- [ ] **Flagship capstone** — enterprise checklist complete
- [ ] **Resume + LinkedIn** — metrics-driven
- [ ] **3 pinned GitHub repos**
- [ ] **Demo video** — 2+ minutes
- [ ] **3 mock interviews** completed (system design, technical, behavioral)
- [ ] **30-day job search plan** — dated and executing
- [ ] **Optional:** Technical blog post published
- [ ] **Optional:** Consulting case study PDF

## Course Completion — You Are Now Capable Of:

✅ Building production AI applications (RAG, agents, full stack)  
✅ Operating AI with LLMOps (trace, eval, deploy, guardrails)  
✅ Designing enterprise systems (multi-tenant, compliance, cloud)  
✅ Securing AI (threat model, red team, audit)  
✅ Architecting for scale and cost (ADRs, FinOps, Terraform)  
✅ Clearing US AI engineering interviews (2026–2027)  
✅ Working remotely for US companies, consulting, or launching AI products  

---

## Congratulations — Zero to AI Engineer

You started with **no required background**. You finished with **enterprise-ready skills**. Keep shipping, keep measuring, keep learning.

*Job readiness resources: [job-readiness/README.md](../job-readiness/README.md)*  
*Interview matrix: [15-interview-preparation-matrix.md](../15-interview-preparation-matrix.md)*

---

*End of Core Curriculum — Modules 01–12 Complete*
