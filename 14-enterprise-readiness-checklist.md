# 14. Enterprise Readiness Checklist

Use before job applications and capstone sign-off. Target **≥90%** checked.

## A. Production Engineering

- [ ] FastAPI (or equivalent) service with OpenAPI docs
- [ ] Dockerized with multi-stage build
- [ ] CI: lint, test, build, eval gate
- [ ] Deployed to cloud (not localhost-only)
- [ ] Health/readiness endpoints
- [ ] Structured logging with request IDs
- [ ] Secrets via env/vault (not in Git)
- [ ] Dependency lockfile pinned

## B. RAG / Retrieval (if applicable)

- [ ] Document ingestion pipeline automated
- [ ] Chunking strategy documented with eval justification
- [ ] Hybrid search OR documented why not needed
- [ ] Metadata + ACL filters on retrieval
- [ ] Citations shown to end users
- [ ] Ragas (or equivalent) faithfulness ≥0.85 on golden set
- [ ] Re-index strategy documented

## C. Agents (if applicable)

- [ ] Max iteration / token budget enforced
- [ ] Tool calls audit-logged
- [ ] HITL for high-risk actions
- [ ] Checkpoint/resume for long runs
- [ ] Kill switch / cancellation supported
- [ ] Sandbox for code/browser tools

## D. LLMOps

- [ ] Tracing (Langfuse/OTel) on all LLM paths
- [ ] Cost per request tracked
- [ ] Prompts versioned in Git
- [ ] Eval regression in CI
- [ ] Canary or staged prompt rollout documented
- [ ] Dashboard: latency p95, error rate, $/1K queries

## E. Security

- [ ] THREAT_MODEL.md exists
- [ ] Prompt injection test suite (≥10 cases)
- [ ] Output guardrails for domain
- [ ] RBAC or API auth implemented
- [ ] No PII in application logs
- [ ] Rate limiting on public endpoints

## F. Enterprise / Compliance

- [ ] Multi-tenant isolation tested (if B2B)
- [ ] Data retention policy documented
- [ ] User data deletion path (GDPR-style)
- [ ] Subprocessor / vendor list in docs
- [ ] Disclaimers for high-risk domains
- [ ] Model card or system limitations doc

## G. Architecture & Operations

- [ ] C4 or equivalent architecture diagram
- [ ] ≥2 ADRs for major decisions
- [ ] Runbook for one failure scenario
- [ ] Load test results (RPS, p95) OR reason N/A
- [ ] FinOps: cost optimization changelog

## H. Portfolio & Communication

- [ ] README: metrics above fold, demo GIF/video
- [ ] 90-second architecture explanation (written or video)
- [ ] GitHub pinned repos (3 max, curated)
- [ ] LinkedIn updated with quantified impact
- [ ] Resume lists projects with metrics, not courses

## Scoring

| Score | Status |
|-------|--------|
| 90–100% | Apply to senior-leaning roles |
| 75–89% | Apply to mid-level AI Engineer |
| 60–74% | Complete Month 5–6 items first |
| <60% | Not yet job-ready for enterprise |

## Auditor Notes (Self-Review)

| Section | Score /25 | Notes |
|---------|-----------|-------|
| A Production | /25 | |
| B RAG | /25 | |
| C Agents | /25 | |
| D LLMOps | /25 | |
| E Security | /25 | |
| F Enterprise | /25 | |
| G Architecture | /25 | |
| H Portfolio | /25 | |

---

*Interviews: [15-interview-preparation-matrix.md](./15-interview-preparation-matrix.md)*
