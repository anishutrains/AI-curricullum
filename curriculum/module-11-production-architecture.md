# Module 11 — Production Architecture & System Design

---

## Topic 11.1: AI System Design & Reference Architectures

### 1. Topic Name
AI System Design & Reference Architectures

### 2. Why This Topic Matters
Senior interviews are 50%+ system design—copilot, RAG platform, agent orchestrator whiteboards.

### 3. Job Roles
AI Architect, Senior AI Engineer, AI Platform Engineer

### 4. Learning Objectives
- Whiteboard enterprise copilot architecture
- Compare sync vs async vs event-driven AI
- Size components for 10K DAU

### 5. Lessons/Subtopics
- Reference architectures: RAG, agent, multimodal
- API gateway + BFF pattern
- Caching layers and CDN for static
- Queue-based async for long agents
- Data plane vs control plane
- Disaster recovery for vector indexes
- ADR (Architecture Decision Record) format

### 6. Hands-on Labs
**Lab 11.1:** Write 3 ADRs for capstone: model choice, vector DB, agent framework.

### 7. Enterprise Projects
Reference architecture library (3 diagrams) in portfolio `/docs/architecture/`.

### 8. Portfolio Projects
Architecture diagrams for all flagship projects.

### 9. Interview Preparation
- 45-min mock: "Design Slack-integrated engineering copilot"
- "Design multi-tenant RAG for 1000 customers"
- Trade-off questions: cost vs quality vs latency

### 10. Real-world Use Cases
Platform teams standardizing AI across product lines.

### 11. Tools & Technologies
C4 diagrams, draw.io, Mermaid, ADR templates

### 12. Common Mistakes
- Single diagram without data flows
- No failure mode discussion
- Ignoring cost in design doc

### 13. Industry Best Practices
- Non-functional requirements upfront (p95, $/query)
- Explicit out-of-scope for MVP
- Review with security before build

### 14. Capstone Deliverables
3 ADRs + C4 container diagram for capstone system.

---

## Topic 11.2: Scalability, Cost Optimization & FinOps

### 1. Topic Name
Scalability, Cost Optimization & FinOps for AI

### 2. Why This Topic Matters
CFOs scrutinize AI spend 2026–27; engineers who cut cost 40% without quality loss are highly valued.

### 3. Job Roles
AI Platform Engineer, Senior AI Engineer, AI Architect

### 4. Learning Objectives
- Model routing for cost tiers
- Cache and batch strategies
- Build FinOps dashboard ($/tenant/day)

### 5. Lessons/Subtopics
- Token economics and forecasting
- Semantic cache ROI
- Batch embedding jobs
- Spot GPU for offline workloads
- Prompt compression techniques
- SLM vs LLM routing
- Chargeback models for internal AI

### 6. Hands-on Labs
**Lab 11.2:** Reduce capstone $/1K queries 30% with documented tactics.

### 7. Enterprise Projects
FinOps report template; budget alerts; model downgrade policy.

### 8. Portfolio Projects
Before/after cost chart in README.

### 9. Interview Preparation
- "AI bill went 10× after launch—diagnosis and fix?"
- "Capacity plan for 1M queries/day RAG."

### 10. Real-world Use Cases
High-volume support, internal search, code completion.

### 11. Tools & Technologies
LiteLLM budgets, Langfuse cost tracking, Infracost

### 12. Common Mistakes
- GPT-4 for all queries
- Re-embedding unchanged docs nightly
- No per-feature cost attribution

### 13. Industry Best Practices
- Cost SLO per feature
- Weekly FinOps review
- Automate downgrade on budget breach

### 14. Capstone Deliverables
FinOps dashboard + cost optimization changelog.

---

## Topic 11.3: Terraform, GitHub Actions & Production Runbooks

### 1. Topic Name
Infrastructure as Code & Production Runbooks

### 2. Why This Topic Matters
AI Platform roles require Terraform + mature ops—not manual console clicks.

### 3. Job Roles
AI Platform Engineer, AI Infrastructure Engineer, LLMOps Engineer

### 4. Learning Objectives
- Terraform modules for AI service infra
- Write incident runbooks for AI failures
- Implement blue/green or canary deploys

### 5. Lessons/Subtopics
- Terraform modules (VPC, DB, K8s, Bedrock)
- GitHub Actions deploy pipelines
- Secrets management (Vault/AWS SM)
- Runbooks: model outage, vector index corrupt, eval regression
- On-call basics for AI services
- Postmortem template for AI incidents

### 6. Hands-on Labs
**Lab 11.3:** Terraform apply staging env; runbook drill: "Bedrock rate limit."

### 7. Enterprise Projects
Full IaC for one cloud; DR runbook for index rebuild.

### 8. Portfolio Projects
`/runbooks/` directory with 3 scenarios.

### 9. Interview Preparation
- "Terraform structure for multi-env AI platform."
- "Incident: RAG faithfulness dropped 20% after deploy."

### 10. Real-world Use Cases
Any production AI team with on-call rotation.

### 11. Tools & Technologies
Terraform, GitHub Actions, PagerDuty (concepts), Helm

### 12. Common Mistakes
- Terraform state not remote-backed
- Runbooks never tested
- No rollback for vector index migrations

### 13. Industry Best Practices
- IaC-only infrastructure changes
- Game day exercises quarterly
- Versioned runbooks in Git

### 14. Capstone Deliverables
Terraform module OR runbook pack linked from capstone README.

---

*Next: [module-12-capstone-job-readiness.md](./module-12-capstone-job-readiness.md)*
