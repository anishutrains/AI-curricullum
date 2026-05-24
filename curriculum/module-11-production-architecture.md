# Module 11 — Production Architecture & System Design
### Zero-to-Hero Track · Weeks 46–48 · Designing AI Systems That Scale and Survive

---

## Why This Module Matters

**Why learn this NOW?**  
You can build and deploy AI features. Senior interviews and platform roles require **system design**: whiteboard a copilot for 10K users, cut AI cost 40%, write Terraform, and run incident drills.

**Why companies need this**
- Startups hit scale walls at 100× traffic without architecture planning.
- **CFOs scrutinize AI spend** — FinOps is engineering work in 2026–27.
- Platform teams need **ADRs, runbooks, IaC** — not heroics at 3 AM.

**Salary impact:** Senior AI Engineer / AI Architect **$190K–$280K+**. System design performance separates L4 from L5 offers.

---

## How This Module Fits into the AI Engineering Journey

| Modules 01–10 | Module 11 | Module 12 |
|---------------|-----------|-----------|
| Working features | **Architecture + scale + cost** | Capstone + job search |
| Cloud deploy (08) | **Terraform + runbooks** | Portfolio polish |
| LLMOps (06) | **FinOps + SLOs** | Mock interviews |

**Prerequisites:** All prior modules conceptually; capstone project in progress.

---

## Job Roles This Module Prepares Students For

AI Architect · Senior AI Engineer · AI Platform Engineer · AI Infrastructure Engineer · Staff AI Engineer · AI Solutions Architect

---

## Beginner Skills Students Will Learn

- Read and draw C4 container diagrams
- Write ADR (Architecture Decision Record)
- Explain sync vs async vs queue-based AI
- List non-functional requirements (latency, cost, availability)

## Intermediate Skills Students Will Learn

- Size RAG platform for 10K DAU (back-of-envelope)
- Model routing for cost tiers
- Semantic cache ROI calculation
- GitHub Actions deploy pipeline

## Advanced Skills Students Will Learn

- FinOps dashboard ($/tenant/day)
- Queue-based long-running agents
- Vector index disaster recovery plan
- Blue/green and canary deploy patterns

## Production Enterprise Skills Students Will Learn

- Terraform modules for AI infra
- Game day runbook drills
- Postmortem template for AI incidents
- Chargeback model for internal AI platform

---

# Topic 11.1 — AI System Design & Reference Architectures

## Beginner-Friendly Explanation

**System design** = planning how all pieces connect before you code — APIs, databases, queues, caches, failure modes.

**Reference architecture** = proven template (RAG platform, agent orchestrator) you adapt, not invent from scratch.

## Learning Outcome

3 ADRs + C4 container diagram for capstone + answer 45-min mock system design interview.

---

### Lesson 11.1.1 — Concept: Non-Functional Requirements First

**Before features, define:**
| NFR | Example target |
|-----|----------------|
| p95 latency | < 3s RAG query |
| Availability | 99.9% |
| Cost | < $0.02/query |
| Faithfulness | ≥ 0.85 |

**Interview:** Always ask clarifying questions on scale, users, compliance, budget.

---

### Lesson 11.1.2 — Concept: Reference Architecture — RAG Platform

```
                    ┌─────────────┐
  Users ──▶ CDN ──▶ │  API Gateway │
                    └──────┬──────┘
                           ▼
                    ┌─────────────┐     ┌──────────────┐
                    │  RAG Service │──▶│ Vector DB    │
                    └──────┬──────┘     └──────────────┘
                           ▼
                    ┌─────────────┐
                    │  LLM API    │
                    └─────────────┘
        Async: Ingest queue ──▶ Embed workers ──▶ Vector DB
```

**Data plane** (user queries) vs **control plane** (admin, eval, config).

---

### Lesson 11.1.3 — Concept: Reference Architecture — Agent Orchestrator

**Sync path:** Short agent (<30s) — API waits  
**Async path:** Long research agent — queue + webhook + status polling

**Connect Module 05:** LangGraph checkpoint in Postgres for resume.

---

### Lesson 11.1.4 — Beginner: C4 Diagrams for Your Capstone

**C4 levels:** Context → Container → Component (don't over-detail Component in interview)

**Guided lab:** Container diagram — Browser, API, Vector DB, LLM, Observability.

**Portfolio:** `/docs/architecture/c4-container.png`

---

### Lesson 11.1.5 — Intermediate: ADR Format and Examples

```markdown
# ADR-001: Vector Database Choice
## Status: Accepted
## Context: Need managed vector search for 500K chunks
## Decision: Pinecone serverless
## Consequences: +$800/mo, low ops burden, vendor lock-in
## Alternatives: pgvector (cheaper, more ops), Weaviate
```

**Write 3 ADRs:** model choice, vector DB, agent framework.

---

### Lesson 11.1.6 — Advanced: Failure Modes and Disaster Recovery

| Failure | Mitigation |
|---------|------------|
| Vector index corrupt | S3 backup + rebuild job |
| LLM provider outage | Fallback model router |
| Embed service down | Queue ingest, serve stale index |
| Region outage | Multi-region read replica (enterprise) |

**Exercise:** 15-min "what if" drill for each failure.

---

### Topic 11.1 — System Design Interview Practice

**45-min mocks:**
1. Design Slack-integrated engineering copilot  
2. Design multi-tenant RAG for 1000 customers  
3. Design real-time voice support architecture  

**Framework:** Requirements → estimate scale → high-level diagram → deep dive 2 components → tradeoffs → failure modes.

---

# Topic 11.2 — Scalability, Cost Optimization & FinOps

## Beginner-Friendly Explanation

**FinOps** = managing cloud AI spend like a budget — not surprise bills.  
**Token economics:** 1M tokens ≈ $X — at scale, small optimizations = thousands saved.

## Learning Outcome

Reduce capstone $/1K queries 30% with documented tactics + FinOps dashboard.

---

### Lesson 11.2.1 — Concept: Token Economics and Forecasting

**Calculate:** `monthly_cost = DAU × queries_per_user × avg_tokens × price_per_token`  
**Exercise:** Forecast cost at 10K DAU; when does self-host vLLM break even?

---

### Lesson 11.2.2 — Beginner: Model Routing for Cost Tiers

```python
def select_model(query: str) -> str:
    if is_simple_faq(query):
        return "gpt-4o-mini"  # cheap
    if requires_reasoning(query):
        return "gpt-4o"       # expensive
    return "gpt-4o-mini"
```

**Router LLM** (small) classifies complexity — meta-cost tradeoff.

---

### Lesson 11.2.3 — Intermediate: Semantic Cache

**Same or similar question** → return cached answer — skip LLM call  
**Tools:** Redis, GPTCache, Langfuse cache  
**ROI lab:** Measure cache hit rate on golden set; calculate savings.

---

### Lesson 11.2.4 — Intermediate: Batch Embedding and Prompt Compression

**Don't:** Re-embed unchanged docs nightly  
**Do:** Hash doc content → embed only on change  
**Prompt compression:** Remove redundant instructions; shorter context when possible

---

### Lesson 11.2.5 — Advanced: SLM vs LLM and Spot GPU

**Small Language Models** for classification/routing; LLM only for generation  
**Spot GPU** for batch ingest; on-demand for user-facing API

---

### Lesson 11.2.6 — Enterprise: Chargeback and Cost SLOs

**Internal platform:** Charge eng teams $X per 1K queries — drives efficient usage  
**Cost SLO:** Feature X must stay under $500/day — alert on breach

**Portfolio:** Before/after cost chart in README.

---

# Topic 11.3 — Terraform, CI/CD & Production Runbooks

## Beginner-Friendly Explanation

**Infrastructure as Code (IaC)** = define servers, databases, AI services in **Terraform** files — reproducible, reviewable in PR.  
**Runbook** = step-by-step playbook when production breaks at 2 AM.

## Learning Outcome

Terraform module OR staging deploy pipeline + 3 runbooks tested in table-top drill.

---

### Lesson 11.3.1 — Concept: Why Manual Console Clicks Fail

**Problems:** Drift, no audit trail, "works on my account," disaster recovery impossible  
**IaC fix:** `terraform apply` — same infra every time

**Beginner:** Start with one resource (S3 bucket or Azure resource group).

---

### Lesson 11.3.2 — Beginner: Terraform Core Concepts

```hcl
resource "aws_s3_bucket" "rag_docs" {
  bucket = "my-rag-docs-${var.env}"
  tags = {
    Project = "rag-copilot"
    Env     = var.env
  }
}
```

**State:** Remote backend (S3 + DynamoDB lock) — never local state in team prod.

---

### Lesson 11.3.3 — Intermediate: Terraform Module for AI Service

**Module inputs:** env, region, model_name  
**Outputs:** api_endpoint, bucket_name  
**Connect Module 08:** Bedrock/Azure/GCP resource definitions.

---

### Lesson 11.3.4 — Intermediate: GitHub Actions Deploy Pipeline

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: terraform plan
      - run: terraform apply -auto-approve  # staging only
      - run: python eval/run_smoke.py
```

**Gate:** Eval smoke test before prod promotion (Module 06).

---

### Lesson 11.3.5 — Advanced: Runbooks for AI Incidents

**Runbook 1:** Bedrock/OpenAI rate limit — backoff, fallback model  
**Runbook 2:** Vector index corrupt — restore from S3 snapshot  
**Runbook 3:** Faithfulness dropped 20% post-deploy — rollback prompt version

**Format:** Symptoms → Diagnosis steps → Fix → Escalation → Postmortem link

**Lab:** Table-top drill — teammate reads symptom, you walk runbook.

---

### Lesson 11.3.6 — Enterprise: Game Days and Postmortems

**Game day:** Simulate outage quarterly — measure MTTR  
**Blameless postmortem:** Timeline, root cause, action items, eval set update

---

# Module 11 — Capstone Architecture Pack

## Week Progression

| Week | Focus |
|------|-------|
| 46 | C4 diagram + 3 ADRs |
| 47 | FinOps optimization + cost chart |
| 48 | Terraform OR runbooks + mock system design |

## Required Deliverables

- [ ] `/docs/architecture/` — C4 + 3 ADRs
- [ ] FinOps: before/after $/1K queries
- [ ] `/runbooks/` — 3 scenarios
- [ ] 1 recorded mock system design (peer or self-practice)

## Master Checklist Before Module 12

| Question | Yes / No |
|----------|----------|
| Can I whiteboard RAG platform in 15 min? | |
| Do I have ADRs explaining key choices? | |
| Can I explain cost optimization I implemented? | |

---

*Next: [module-12-capstone-job-readiness.md](./module-12-capstone-job-readiness.md)*
