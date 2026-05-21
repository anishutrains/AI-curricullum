# Module 06 — LLMOps

---

## Topic 6.1: Observability, Tracing & Monitoring

### 1. Topic Name
LLM Observability — Tracing, Metrics & Monitoring

### 2. Why This Topic Matters
70%+ senior JDs mention tracing/observability. You cannot operate production AI without Langfuse/OpenTelemetry and cost dashboards.

### 3. Job Roles
LLMOps Engineer, AI Reliability Engineer, AI Platform Engineer

### 4. Learning Objectives
- Instrument LLM calls with OpenTelemetry
- Use Langfuse for trace visualization
- Define SLIs: latency, error rate, cost/query, faithfulness

### 5. Lessons/Subtopics
- Traces, spans, attributes for LLM
- Langfuse + OpenTelemetry integration
- Prometheus/Grafana dashboards
- Alerting on error spikes and cost anomalies
- User/session correlation IDs
- PII scrubbing in traces

### 6. Hands-on Labs
**Lab 6.1:** Full trace from API → retriever → LLM → response; Grafana dashboard.

### 7. Enterprise Projects
Per-tenant cost attribution; weekly FinOps report automation.

### 8. Portfolio Projects
Live dashboard screenshot in README.

### 9. Interview Preparation
- "Production LLM service is failing—debugging workflow?"
- "What metrics do you put on an AI SLA dashboard?"

### 10. Real-world Use Cases
24/7 copilots, high-volume RAG, multi-tenant SaaS.

### 11. Tools & Technologies
Langfuse, OpenTelemetry, Prometheus, Grafana, Datadog (concepts)

### 12. Common Mistakes
- Logging full prompts with PII
- No trace ID across microservices
- Alerts only on 500s, not quality degradation

### 13. Industry Best Practices
- Sample traces in prod (1–10%) for cost
- Separate dev/staging/prod Langfuse projects
- Runbooks linked from alerts

### 14. Capstone Deliverables
Observability stack on RAG project; p99 latency and $/1K queries visible.

---

## Topic 6.2: Evaluation Pipelines (Ragas, DeepEval, promptfoo)

### 1. Topic Name
AI Evaluation Pipelines

### 2. Why This Topic Matters
#1 gap between tutorials and enterprise. Hiring managers ask "how do you know it works?"—eval CI is the answer.

### 3. Job Roles
LLMOps Engineer, RAG Engineer, Responsible AI Engineer

### 4. Learning Objectives
- Build golden datasets for RAG and agents
- Run Ragas, DeepEval, promptfoo in CI
- Gate releases on regression thresholds

### 5. Lessons/Subtopics
- Faithfulness, relevance, context precision/recall
- Ragas metrics pipeline
- DeepEval test cases
- promptfoo YAML suites
- LLM-as-judge pitfalls
- Human eval sampling

### 6. Hands-on Labs
**Lab 6.2:** GitHub Action fails if faithfulness drops >5% vs baseline.

### 7. Enterprise Projects
Golden set per tenant vertical; weekly human audit sample.

### 8. Portfolio Projects
Eval badge in README: "Faithfulness 0.87 on 100-case suite."

### 9. Interview Preparation
- "Design eval pipeline for RAG chatbot."
- "LLM-as-judge biased toward GPT—mitigation?"

### 10. Real-world Use Cases
Release gates, A/B prompt tests, vendor model comparisons.

### 11. Tools & Technologies
Ragas, DeepEval, promptfoo, LangSmith evals

### 12. Common Mistakes
- Eval set too small or leaked into training prompts
- Only offline eval, no production feedback loop
- Changing metrics without versioning

### 13. Industry Best Practices
- Version golden datasets in DVC/Git LFS
- Track eval history over time
- Combine automated + weekly human review

### 14. Capstone Deliverables
CI eval gate on main project; eval report artifact per release.

---

## Topic 6.3: Prompt Versioning, Experiment Tracking & AI CI/CD

### 1. Topic Name
Prompt Versioning, Experiments & AI CI/CD

### 2. Why This Topic Matters
LLMOps Engineers own "CI/CD for prompts"—same rigor as code deploys.

### 3. Job Roles
LLMOps Engineer, AI Platform Engineer

### 4. Learning Objectives
- Version prompts/models in registry
- Track experiments (MLflow/W&B for LLM)
- Implement canary prompt deployments

### 5. Lessons/Subtopics
- Prompt registry patterns
- MLflow LLM tracking
- Feature flags for prompts
- Canary 5% → 50% → 100% rollout
- Rollback procedures
- Artifact promotion dev→staging→prod

### 6. Hands-on Labs
**Lab 6.3:** Prompt v2 canary with automatic rollback on eval failure.

### 7. Enterprise Projects
Change advisory for prod prompt changes; audit who approved.

### 8. Portfolio Projects
`CHANGELOG-prompts.md` with metric deltas per version.

### 9. Interview Preparation
- "How do you deploy a new system prompt safely?"
- "CI pipeline stages for an AI feature."

### 10. Real-world Use Cases
Seasonal prompt updates, model upgrades, compliance text changes.

### 11. Tools & Technologies
MLflow, Langfuse prompts, LaunchDarkly, GitHub Actions

### 12. Common Mistakes
- Hot-editing prod prompts in dashboard without Git
- No rollback tested
- Canary without stat significance

### 13. Industry Best Practices
- Every prompt change = PR + eval
- Immutable prompt artifacts in registry
- Post-deploy monitoring window 24h

### 14. Capstone Deliverables
Full AI CI/CD diagram + working canary on one project.

---

## Topic 6.4: Guardrails, Governance & Model Registry

### 1. Topic Name
Guardrails, Governance & Model Registry

### 2. Why This Topic Matters
Enterprise LLMOps requires guardrails (toxicity, PII, topic boundaries) and model governance for audits.

### 3. Job Roles
LLMOps Engineer, Responsible AI Engineer, Enterprise AI Engineer

### 4. Learning Objectives
- Deploy NeMo Guardrails or equivalent
- Maintain model/prompt registry with approvals
- Document lineage for compliance

### 5. Lessons/Subtopics
- Input/output guardrails
- Topic restriction rails
- PII detection and redaction
- Model cards and risk tiers
- Approval workflows
- Retention policies for logs

### 6. Hands-on Labs
**Lab 6.4:** Block medical advice in non-health bot; log guardrail triggers.

### 7. Enterprise Projects
Governance pack: model card, DPIA template, retention config.

### 8. Portfolio Projects
Guardrail trigger rate metric in observability dashboard.

### 9. Interview Preparation
- "Implement guardrails without killing UX latency."
- "Model registry fields for SOC2 audit?"

### 10. Real-world Use Cases
Regulated chatbots, HR bots, financial advice boundaries.

### 11. Tools & Technologies
NeMo Guardrails, Guardrails AI, custom classifiers, MLflow Model Registry

### 12. Common Mistakes
- Guardrails only in demo, not prod path
- No logging when guardrails fire
- Registry without owner and review date

### 13. Industry Best Practices
- Fail closed for high-risk domains
- Regular red-team updates to guardrail tests
- Quarterly registry review

### 14. Capstone Deliverables
Model registry entry + guardrail CI tests for capstone project.

---

*Next: [module-07-enterprise-ai.md](./module-07-enterprise-ai.md)*
