# Module 10 — AI Security & Responsible AI

---

## Topic 10.1: AI Security — Threat Models & Red Teaming

### 1. Topic Name
AI Security — Threat Models & Red Teaming

### 2. Why This Topic Matters
Agents with tools create new attack surface; AI Security Engineer demand rising with enterprise agent rollouts.

### 3. Job Roles
AI Security Engineer, Enterprise AI Engineer, AI Architect

### 4. Learning Objectives
- Create STRIDE-style threat model for LLM app
- Execute red team test suite
- Remediate OWASP LLM Top 10 risks

### 5. Lessons/Subtopics
- Prompt injection (direct/indirect)
- Data exfiltration via tools
- Model denial of wallet
- Supply chain: compromised packages, models
- Secrets in prompts and logs
- Red team automation tools
- Pen test report structure

### 6. Hands-on Labs
**Lab 10.1:** Red team capstone bot; fix 8/10 attack vectors; document 2 accepted risks.

### 7. Enterprise Projects
**AI Cybersecurity Analyst** agent in isolated env with read-only SIEM mock.

### 8. Portfolio Projects
`THREAT_MODEL.md` + red team results table.

### 9. Interview Preparation
- "Threat model for email-processing agent."
- "Prevent data exfil via RAG context."

### 10. Real-world Use Cases
Security ops copilots, email assistants, customer-facing bots.

### 11. Tools & Technologies
OWASP LLM Top 10, Garak, PyRIT, custom attack libraries

### 12. Common Mistakes
- Security review only at launch
- Agents with internet + sensitive data same env
- No rate limiting (DoW attacks)

### 13. Industry Best Practices
- Security in CI weekly
- Bug bounty for critical copilots
- Separate prod secrets per tenant

### 14. Capstone Deliverables
Passed red team suite ≥80%; threat model signed in README.

---

## Topic 10.2: Responsible AI — Bias, Fairness & Transparency

### 1. Topic Name
Responsible AI — Bias, Fairness & Transparency

### 2. Why This Topic Matters
Regulated industries and EU AI Act drive Responsible AI Engineer hires; required for enterprise procurement.

### 3. Job Roles
Responsible AI Engineer, Enterprise AI Engineer, AI Consultant

### 4. Learning Objectives
- Run bias/fairness evals on representative samples
- Write model cards and user disclosures
- Implement appeal/human review for adverse decisions

### 5. Lessons/Subtopics
- Fairness metrics for classification
- Disparate impact awareness
- Model cards (HuggingFace template)
- Transparency: capabilities and limits
- Human oversight for high-risk decisions
- EU AI Act conformity assessment (overview)

### 6. Hands-on Labs
**Lab 10.2:** Model card for support classifier; fairness check across demographic proxy slices.

### 7. Enterprise Projects
Responsible AI sign-off checklist before prod launch.

### 8. Portfolio Projects
`/docs/model-card.md` for capstone model/prompts.

### 9. Interview Preparation
- "AI rejected loan application—required process?"
- "How do you test for bias in hiring copilot?"

### 10. Real-world Use Cases
HR tech, lending assist, insurance, government services.

### 11. Tools & Technologies
DeepEval fairness, IBM AI Fairness 360 (concepts), model card templates

### 12. Common Mistakes
- Fairness testing only on synthetic data
- No appeals process documented
- Overclaiming AI capabilities in marketing

### 13. Industry Best Practices
- Diverse golden eval sets
- Legal review of user-facing disclaimers
- Periodic bias re-audit post model change

### 14. Capstone Deliverables
Model card + fairness eval report for one portfolio project.

---

## Topic 10.3: AI Governance Programs & Audit Trails

### 1. Topic Name
AI Governance Programs & Audit Trails

### 2. Why This Topic Matters
EY/Deloitte frameworks emphasize governance; enterprises need immutable audit logs for AI decisions.

### 3. Job Roles
Enterprise AI Engineer, AI Architect, Responsible AI Engineer

### 4. Learning Objectives
- Design AI governance committee charter (template)
- Implement immutable audit logs
- Map controls to SOC2/NIST AI RMF

### 5. Lessons/Subtopics
- AI governance operating model
- Policy: approved models, data classes, use cases
- Audit log schema (who, what, when, input hash)
- NIST AI RMF functions (Govern, Map, Measure, Manage)
- Third-party model risk assessments
- Incident classification for AI failures

### 6. Hands-on Labs
**Lab 10.3:** Append-only audit log for all agent tool calls with export API.

### 7. Enterprise Projects
Governance pack aligning capstone to NIST AI RMF lite.

### 8. Portfolio Projects
Sample governance charter + implemented audit API.

### 9. Interview Preparation
- "Set up AI governance for 500-person company."
- "Audit trail requirements for HIPAA AI."

### 10. Real-world Use Cases
Healthcare, finance, government contractors.

### 11. Tools & Technologies
WORM storage concepts, PostgreSQL audit tables, SIEM export

### 12. Common Mistakes
- Mutable logs (tampering risk)
- No retention policy alignment with legal
- Governance docs without engineering controls

### 13. Industry Best Practices
- Quarterly access reviews for AI admin roles
- Align with existing GRC tools
- AI incident runbook alongside security IR

### 14. Capstone Deliverables
Audit API + governance checklist completed for capstone.

---

*Next: [module-11-production-architecture.md](./module-11-production-architecture.md)*
