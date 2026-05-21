# 8. Project Portfolio — Industry-Level Projects

Each project includes: **architecture, tools, deployment, scalability, security, monitoring, evaluation, cloud setup, interview talking points**.

---

## Project 1: Enterprise RAG Assistant

### Architecture
```
[Web UI] → [API Gateway] → [FastAPI RAG Service]
                              ├── Query Router
                              ├── Hybrid Retriever (BM25 + Vector)
                              ├── Reranker
                              ├── LLM (with citations)
                              └── [Postgres] + [Vector DB] + [Redis Cache]
[Ingestion Worker] → Chunk → Embed → Index (ACL metadata)
```

### Tools
LangChain/LlamaIndex, Pinecone or pgvector, OpenAI embeddings, Cohere Rerank, FastAPI, Next.js, Langfuse

### Deployment
Docker → AWS ECS or Azure App Service; private LLM endpoint; CI via GitHub Actions

### Scalability
Horizontal API replicas; async ingestion queue; semantic cache; read replicas for Postgres

### Security
Tenant isolation, ACL filters on retrieval, prompt injection tests, PII redaction in logs

### Monitoring
Langfuse traces, faithfulness alerts, p95 latency, $/1K queries dashboard

### Evaluation
Ragas faithfulness ≥0.85, context precision on 100-case golden set; CI regression gate

### Cloud Setup
Azure: AI Search + Azure OpenAI OR AWS: Bedrock KB + Lambda

### Interview Talking Points
- Why hybrid search over pure vector
- Chunking experiments and metric improvement
- How you prevent cross-tenant data leaks
- Cost reduction tactics (cache, model routing)

---

## Project 2: AI Customer Support System

### Architecture
LangGraph triage → RAG → draft → **HITL approve** → CRM webhook; escalation to human agent

### Tools
LangGraph, Zendesk/Intercom API mock, Twilio (optional voice), guardrails

### Deployment
K8s with HPA; Redis for session state; separate staging with synthetic tickets

### Scalability
Queue-backed ticket processing; rate limit per customer tier

### Security
No PII in traces; role-based tool access; content safety filters

### Monitoring
CSAT proxy metric, resolution time, guardrail trigger rate

### Evaluation
DeepEval on tone, accuracy, escalation correctness; 50 synthetic tickets

### Cloud Setup
GCP Cloud Run or AWS EKS

### Interview Talking Points
- HITL design and SLA for approval
- When agent abstains vs hallucinates
- Integration with existing ticket taxonomy

---

## Project 3: AI Coding Copilot

### Architecture
IDE plugin or web UI → context collector (repo index) → RAG on codebase → agent tools (read_file, search, propose_patch) → sandbox test

### Tools
LangGraph, tree-sitter chunking, E2B sandbox, GitHub API

### Deployment
Local-first dev; cloud sync for team knowledge base optional

### Scalability
Incremental index on git push; debounced context window management

### Security
Sandbox only; no prod credentials; patch requires user accept

### Monitoring
Acceptance rate of suggestions, test pass rate after patch

### Evaluation
SWE-bench lite subset or custom 20 bug-fix tasks

### Cloud Setup
Optional: vector index on S3 + Lambda indexer

### Interview Talking Points
- Context window budgeting for large repos
- Safety of autonomous code execution
- Comparison to Copilot/Cursor architecture (high level)

---

## Project 4: Autonomous Research Agent

### Architecture
Planner agent → web/search tools (mock or Tavily) → note-taking memory → critic → final report PDF

### Tools
LangGraph or CrewAI, Playwright (controlled), report generator

### Deployment
Batch jobs on queue; 30-min max runtime; checkpoint resume

### Scalability
Parallel subtopic research; dedupe sources; token budget per run

### Security
Domain allowlist; no arbitrary code exec; cite sources mandatory

### Monitoring
Steps completed, source count, user cancel rate

### Evaluation
Human rubric: coverage, citation accuracy, hallucination count

### Cloud Setup
AWS Batch or Celery workers on ECS

### Interview Talking Points
- Planner vs reactive agent
- Preventing infinite research loops
- Source grounding and citation validation

---

## Project 5: Multi-Agent Finance Analyst

### Architecture
CrewAI: Data Researcher → Quant Analyst → Report Writer → Compliance Critic

### Tools
CrewAI, yfinance/API mock, pandas, structured outputs

### Deployment
Scheduled reports; audit log of agent messages

### Scalability
Cache market data; limit API calls; batch reports

### Security
Disclaimer: not financial advice; no trade execution tools in MVP

### Monitoring
Token cost per report, error rate per agent role

### Evaluation
Numeric accuracy checks on extracted metrics vs source

### Cloud Setup
Any; emphasis on audit trail storage

### Interview Talking Points
- Multi-agent cost control
- Compliance critic agent purpose
- Why not single LLM pass

---

## Project 6: AI DevOps Assistant

### Architecture
Log ingest → RAG on runbooks → agent suggests remediation → optional PR draft (HITL)

### Tools
LangGraph, GitHub API, Prometheus alert webhook, E2B for config validation

### Deployment
Internal tool; SSO required; read-only prod access default

### Scalability
Alert deduplication; on-call rotation integration mock

### Security
Read-only K8s RBAC; no auto-apply without approval

### Monitoring
Suggestion acceptance rate, MTTR improvement (simulated)

### Evaluation
20 historical incident scenarios with expected runbook match

### Cloud Setup
Runs in same K8s cluster (in-cluster agent)

### Interview Talking Points
- Blast radius of ops agents
- Integrating with existing incident management

---

## Project 7: AI Recruiter System

### Architecture
Resume parse → structured profile → job match RAG → outreach draft → CRM sync

### Tools
Structured extraction, vector match on job descriptions, bias fairness checks

### Deployment
SaaS-shaped with auth; GDPR delete endpoint

### Security
PII encryption; bias eval on demographic proxies; human review before send

### Evaluation
Match precision@10 on labeled dataset

### Interview Talking Points
- Responsible AI in hiring
- Structured resume parsing vs raw text RAG

---

## Project 8: AI Sales Assistant

### Architecture
CRM context + RAG on playbooks → email/call script generation → meeting prep brief

### Tools
Salesforce mock API, Next.js UI, streaming generation

### Deployment
Multi-tenant SaaS; usage metering

### Security
CRM OAuth scopes minimized; tenant data isolation

### Evaluation
A/B tone tests; factual grounding on product docs

### Interview Talking Points
- Personalization without hallucinating product features
- Token quota per sales rep tier

---

## Project 9: AI Healthcare Assistant (Non-Diagnostic)

### Architecture
HIPAA-aware RAG on patient education docs → abstain on diagnosis → escalate clinical questions

### Tools
Guardrails, high faithfulness threshold, audit logs

### Security
HIPAA checklist; BAA template awareness; no PHI in dev logs

### Evaluation
Abstention rate on clinical edge cases; faithfulness on approved content only

### Interview Talking Points
- Scope limitation and liability disclaimers
- HIPAA technical safeguards implemented

---

## Project 10: AI Legal Document Analyzer

### Architecture
Doc upload → clause extraction → risk flagging → comparison to template library

### Tools
Long-context + RAG hybrid, structured JSON clauses, LlamaIndex

### Security
Client matter isolation; encryption at rest; no training on client data

### Evaluation
Extraction F1 on labeled contract dataset (public or synthetic)

### Interview Talking Points
- Attorney-in-the-loop workflow
- Clause-level citation requirements

---

## Project 11: AI Cybersecurity Analyst

### Architecture
SIEM alert → RAG on playbooks → agent correlates IOCs → draft incident report (sandbox, read-only)

### Tools
Mock Splunk/Elastic data, threat intel API mock, red team self-tests

### Security
Isolated env; no outbound attacks; tool allowlist

### Evaluation
20 alert scenarios; correct playbook retrieval rate

### Interview Talking Points
- Why agents must not auto-block IPs without human approval
- Threat model for security copilot itself

---

## Project 12: Multimodal AI Search Engine

### Architecture
Text + image upload → multimodal embeddings → unified index → ranked results with snippets

### Tools
GPT-4o/Gemini vision, CLIP-style embeddings, Next.js UI

### Deployment
CDN for images; object storage S3/GCS

### Scalability
Separate indexes per modality with fusion ranking

### Evaluation
MRR@10 on curated query set with image+text pairs

### Interview Talking Points
- Embedding alignment across modalities
- Storage cost for image vectors

---

## Project 13: AI Workflow Automation Platform

### Architecture
Visual workflow editor → execution engine → LLM steps + integrations (email, Slack mock)

### Tools
React Flow, TypeScript, FastAPI executor, n8n-compatible export

### Deployment
Multi-tenant workflow DB; execution history API

### Security
Signed workflow definitions; secret vault per tenant

### Evaluation
Idempotency tests on retry; 10 workflow templates pass E2E

### Interview Talking Points
- DAG validation preventing cycles
- Compensating transactions on partial failure

---

## Portfolio Strategy

| Priority | Projects (minimum 3) |
|----------|----------------------|
| **RAG track** | #1, #2, #10 |
| **Agent track** | #4, #5, #13 |
| **Platform track** | #1, #6, + LLMOps from Module 06 |
| **Full-stack track** | #2, #8, #12 |
| **Security track** | #11, #1 with security docs |

**GitHub presentation:** Pin 3 repos; each README leads with metrics, architecture diagram, and 90-second demo GIF.

---

*Certifications: [09-certification-roadmap.md](./09-certification-roadmap.md)*
