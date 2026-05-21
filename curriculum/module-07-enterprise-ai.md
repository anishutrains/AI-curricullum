# Module 07 — Enterprise AI

---

## Topic 7.1: AI Compliance, Privacy & Data Governance

### 1. Topic Name
AI Compliance, Privacy & Data Governance

### 2. Why This Topic Matters
50%+ enterprise JDs mention compliance awareness. GDPR, HIPAA, SOC2, EU AI Act basics separate enterprise hires.

### 3. Job Roles
Enterprise AI Engineer, Responsible AI Engineer, AI Consultant

### 4. Learning Objectives
- Map data flows for AI features (DPIA-lite)
- Implement data minimization and retention
- Explain EU AI Act risk categories (practical)

### 5. Lessons/Subtopics
- GDPR/CCPA for LLM data processing
- HIPAA considerations for health bots
- SOC2 Type II relevance to AI logs
- Data residency and vendor DPAs
- Right to deletion in RAG indexes
- EU AI Act high-risk checklist (overview)

### 6. Hands-on Labs
**Lab 7.1:** Data flow diagram + retention job deleting user data from vector index.

### 7. Enterprise Projects
Compliance appendix for capstone: lawful basis, retention, subprocessors.

### 8. Portfolio Projects
`COMPLIANCE.md` in flagship repo.

### 9. Interview Preparation
- "Customer asks if data trains OpenAI—answer?"
- "Design GDPR delete for RAG system."

### 10. Real-world Use Cases
EU customers, healthcare, financial services copilots.

### 11. Tools & Technologies
Vault secrets, encryption at rest, audit logs, Azure Policy

### 12. Common Mistakes
- Sending PII to APIs without DPA
- Indefinite chat log retention
- No subprocessors list in docs

### 13. Industry Best Practices
- Privacy by design in architecture reviews
- Legal review before new data sources
- Zero training clause with vendors where possible

### 14. Capstone Deliverables
Signed-off data flow diagram + deletion API endpoint.

---

## Topic 7.2: AI Risk Management & Hallucination Prevention

### 1. Topic Name
AI Risk Management & Hallucination Prevention

### 2. Why This Topic Matters
Enterprises fear liability from wrong AI answers. Engineers must quantify and mitigate hallucination risk.

### 3. Job Roles
Enterprise AI Engineer, Applied AI Engineer, AI Consultant

### 4. Learning Objectives
- Build risk matrix for AI features
- Apply grounding, abstention, and confidence thresholds
- Design human escalation paths

### 5. Lessons/Subtopics
- Risk tiers: informational vs decision-support vs automated action
- Abstention ("I don't know") patterns
- Confidence scores from retrieval + LLM
- Human-in-the-loop thresholds
- Insurance and liability (awareness)
- Documented limitations in UX

### 6. Hands-on Labs
**Lab 7.2:** Abstain when retrieval score < threshold; route to human queue.

### 7. Enterprise Projects
Risk register for copilot: 10 risks × mitigations × owners.

### 8. Portfolio Projects
Hallucination rate metric on golden set with mitigation changelog.

### 9. Interview Preparation
- "Bot gave wrong medical info—incident response?"
- "When should AI refuse to answer?"

### 10. Real-world Use Cases
Legal research assist, benefits HR bot, tax prep assist.

### 11. Tools & Technologies
Ragas faithfulness, custom confidence models, ticketing integration

### 12. Common Mistakes
- Always answering to please users
- No escalation path
- Hiding uncertainty in UI

### 13. Industry Best Practices
- Show sources and confidence
- Domain-specific disclaimers
- Post-incident eval set updates

### 14. Capstone Deliverables
Risk register + abstention logic with measured hallucination reduction.

---

## Topic 7.3: RBAC, Multi-Tenancy & Enterprise Integrations

### 1. Topic Name
RBAC, Multi-Tenancy & Enterprise Integrations

### 2. Why This Topic Matters
B2B AI must isolate tenants and respect document ACLs—core Enterprise AI Engineer skill.

### 3. Job Roles
Enterprise AI Engineer, AI Integration Engineer, AI Platform Engineer

### 4. Learning Objectives
- Implement tenant-scoped data and auth
- Sync ACLs from SharePoint/Confluence/Salesforce
- Build OAuth enterprise connectors

### 5. Lessons/Subtopics
- Multi-tenant DB schemas
- JWT/OAuth2/OIDC with Entra ID, Okta
- SharePoint, ServiceNow, Salesforce connector patterns
- Webhook ingestion for doc updates
- Service accounts vs user-delegated auth
- Rate limits per tenant

### 6. Hands-on Labs
**Lab 7.3:** Two-tenant RAG: Tenant A cannot retrieve Tenant B docs (prove with test).

### 7. Enterprise Projects
SharePoint mock connector with ACL metadata on chunks.

### 8. Portfolio Projects
Integration architecture diagram in `/docs/enterprise-integrations.md`.

### 9. Interview Preparation
- "Design multi-tenant RAG for 500 enterprise customers."
- "SharePoint permission sync strategy."

### 10. Real-world Use Cases
Internal knowledge copilots, CRM AI, IT service management.

### 11. Tools & Technologies
Entra ID, MS Graph, Salesforce API, ServiceNow API, OAuth2

### 12. Common Mistakes
- Global vector index without tenant_id filter
- Stale ACLs after permission revocation
- Service account with excessive scopes

### 13. Industry Best Practices
- Filter retrieval by user ACL every query
- Nightly ACL sync job
- Principle of least privilege on connectors

### 14. Capstone Deliverables
Multi-tenant demo with RBAC tests in CI.

---

## Topic 7.4: AI Consulting & Transformation Delivery

### 1. Topic Name
AI Consulting — Discovery, POC & Production Handoff

### 2. Why This Topic Matters
AI Consultant is #2 fastest-growing role—technical consultants who ship POCs win engagements.

### 3. Job Roles
AI Consultant, AI Solutions Engineer

### 4. Learning Objectives
- Run AI discovery workshops
- Scope 2-week POC with success metrics
- Deliver production handoff documentation

### 5. Lessons/Subtopics
- Build vs buy vs partner framework
- ROI estimation (time saved, error reduction)
- POC scope control (thin vertical slice)
- Stakeholder communication
- Change management basics
- SOW and milestone structure

### 6. Hands-on Labs
**Lab 7.4:** Write 5-page POC proposal for fictional retail client RAG copilot.

### 7. Enterprise Projects
Consulting template pack: discovery questionnaire, architecture template, ROI calculator spreadsheet.

### 8. Portfolio Projects
Case study: problem → POC → metrics → lessons (can be capstone fictionalized).

### 9. Interview Preparation
- "Walk through a successful AI POC you led."
- "Client wants ChatGPT for everything—how do you refocus?"

### 10. Real-world Use Cases
Deloitte/PwC-style transformations, vendor SI projects.

### 11. Tools & Technologies
Miro, Notion, architecture templates, cost calculators

### 12. Common Mistakes
- POC without eval criteria
- Scope creep into production complexity
- No executive summary for sponsors

### 13. Industry Best Practices
- Fixed timeline POC (2–4 weeks)
- Kill criteria defined upfront
- Explicit production estimate separate from POC

### 14. Capstone Deliverables
Consulting case study doc + reusable POC starter kit in GitHub.

---

*Next: [module-08-cloud-ai.md](./module-08-cloud-ai.md)*
