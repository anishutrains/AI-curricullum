# 4. Skills Gap Analysis

## The Gap Defined

**90% of US enterprises** report AI skill shortages, yet **82% provide some AI training**—only **35%** have mature, job-aligned upskilling. The gap is not “knowing AI exists”; it is **shipping production systems safely at scale**.

## Three-Dimensional Engineer Profile (Karat Framework)

| Dimension | Tutorial Developer | Enterprise Engineer |
|-----------|-------------------|---------------------|
| **Technical** | Copy-paste API calls | End-to-end systems, evals, infra |
| **Communication** | Cannot explain tradeoffs | ADRs, stakeholder docs, incident reports |
| **AI Proficiency** | Prompt hacks | RAG + agents + LLMOps + governance |

**Strong AI engineers deliver ~3× their compensation in value; weak engineers deliver zero or negative value** (rework, incidents, compliance risk).

## Skill Gap Matrix

| Skill Area | Market Demand | Tutorial Supply | Gap Severity |
|------------|---------------|-----------------|--------------|
| Production RAG | Critical | Low quality | **Severe** |
| Agentic orchestration | Critical | Very low | **Severe** |
| LLMOps / observability | High | Near zero | **Severe** |
| AI security | High | Near zero | **Severe** |
| Cost optimization | High | Low | **High** |
| Enterprise compliance | Medium-High | Very low | **High** |
| Cloud AI deployment | High | Low | **High** |
| Evaluation pipelines | Critical | Low | **Severe** |
| Full-stack AI UX | High | Medium | **Medium** |
| Fine-tuning | Medium | Medium | **Medium** |
| Deep ML math | Low (for GenAI roles) | Oversupplied | **Inverse gap** |

## What Tutorials Teach vs What Jobs Require

### Tutorials Over-Index On
- One-file LangChain chains
- ChromaDB local demos
- “Build ChatGPT in 10 minutes”
- Prompt tricks without versioning
- Jupyter-only workflows

### Jobs Require
- Multi-tenant architecture
- Hybrid search + reranking + caching
- Stateful agent graphs with HITL
- Regression tests on prompts and retrieval
- OpenTelemetry traces + cost dashboards
- Guardrails and audit logs
- Terraform + K8s deployment runbooks

## How This Curriculum Closes the Gap

| Gap | Closure Mechanism |
|-----|-------------------|
| No production experience | Every module has deployment lab + checklist |
| No metrics | Ragas/DeepEval/promptfoo in Modules 04, 06 |
| No security | Module 10 + security section in every project |
| No agents | Module 05 full agentic track |
| No enterprise context | Module 07 governance + compliance labs |
| Weak portfolio | 13 industry projects with interview talking points |
| Weak interviews | Module 12 + Section 15 matrix |

## Self-Assessment Rubric

Rate yourself 1–5 on each. **Below 3 on any row = prioritize that module before job applications.**

| Skill | Target for Job-Ready |
|-------|---------------------|
| Deploy FastAPI LLM service to cloud | 4+ |
| Explain RAG chunking strategies | 4+ |
| Build LangGraph agent with tools | 4+ |
| Set up tracing (Langfuse/OTel) | 3+ |
| Run automated eval regression | 4+ |
| Implement RBAC + tenant isolation | 3+ |
| Defend against prompt injection | 3+ |
| System design AI copilot (whiteboard) | 4+ |
| Estimate cost per 1K queries | 4+ |

---

*Next: [05-complete-learning-roadmap.md](./05-complete-learning-roadmap.md)*
