# Module 07 — Enterprise AI Systems
### Zero-to-Hero Track · Weeks 31–34 · Building AI That Enterprises Can Actually Trust

---

## Why This Module Matters

**Why learn this NOW?**  
Modules 01–06 taught you to build, operate, and evaluate AI. Module 07 teaches you to build AI that **enterprises will buy and legal will approve** — compliance, multi-tenancy, risk controls, and consulting delivery. Tutorial chatbots don't pass procurement; enterprise AI systems do.

**Why companies need this**
- **Fortune 500** cannot deploy AI without data governance, tenant isolation, and audit trails.
- **50%+ enterprise AI JDs** mention compliance, RBAC, or multi-tenancy (2026–2027 US market).
- Wrong AI answer in HR, legal, or finance = lawsuit, not just a bad UX review.

**Salary impact:** Enterprise AI Engineer roles cluster **$165K–$240K** US base. AI Consultants bill **$150–$300/hr**. Multi-tenant RAG + compliance docs on GitHub unlock both paths.

**Scalability relevance:** Enterprise patterns (tenant isolation, ACL-aware retrieval, rate limits) are the difference between a demo for 10 users and a platform for 10,000.

---

## How This Module Fits into the AI Engineering Journey

| Previous (Modules 01–06) | This Module (07) | Enables (Modules 08–12) |
|--------------------------|------------------|-------------------------|
| RAG + agents + LLMOps | **Governance + tenancy + risk** | Secure cloud deploy (08) |
| Single-tenant demo | **B2B SaaS architecture** | Full-stack product (09) |
| Guardrails basics | **Compliance + consulting** | Security depth (10), capstone (12) |

**Prerequisites:** Modules 01–06 complete — especially Module 04 (RAG), Module 06 (LLMOps, guardrails, registry).

---

## Job Roles This Module Prepares Students For

| Role | Enterprise skills from this module |
|------|-----------------------------------|
| **Enterprise AI Engineer** | Multi-tenancy, RBAC, ACL-aware RAG |
| **AI Platform Engineer** | Tenant isolation, rate limits, integrations |
| **AI Integration Engineer** | SharePoint, Salesforce, OAuth connectors |
| **Responsible AI Engineer** | Risk matrix, abstention, compliance |
| **AI Consultant** | Discovery, POC scoping, handoff docs |
| **AI Solutions Engineer** | Enterprise demos with governance story |
| **Generative AI Engineer** | Production copilots with disclaimers |

---

## Beginner Skills Students Will Learn

- Explain GDPR, HIPAA, SOC2 in AI context (plain English)
- Draw a data flow diagram for an AI feature
- Implement `tenant_id` filter on every database query
- Build abstention logic ("I don't know") when retrieval score is low
- Write a 1-page POC proposal outline

## Intermediate Skills Students Will Learn

- User deletion from vector index (right to erasure)
- JWT/OAuth2 login with mock Entra ID
- Two-tenant RAG with CI test proving isolation
- Risk register with mitigations
- SharePoint-style ACL metadata on chunks

## Advanced Skills Students Will Learn

- ACL sync job design (nightly permission refresh)
- Confidence scoring from retrieval + LLM
- Human escalation queue integration
- Enterprise connector patterns (webhooks, delegated auth)

## Production Enterprise Skills Students Will Learn

- `COMPLIANCE.md` pack (lawful basis, retention, subprocessors)
- Consulting case study + POC starter kit
- Stakeholder communication for non-technical sponsors
- EU AI Act risk tier awareness (high-risk checklist)

---

# Topic 7.1 — AI Compliance, Privacy & Data Governance

## Beginner-Friendly Explanation

**Compliance** = following laws and company rules about data.  
**Governance** = documented policies for who can use what data, how long you keep it, and which AI vendors you trust.

**Analogy:** Compliance is the speed limit. Governance is the whole driving handbook — when to brake, who can borrow the car, where you're allowed to go.

When your RAG app stores employee HR documents, you are a **data processor** — legal cares deeply.

## Why This Topic Matters in Real Companies

- EU customers require GDPR compliance or they cannot buy.
- Healthcare clients require HIPAA awareness.
- SOC2 Type II is required for most B2B SaaS sales.
- Procurement asks: "Does our data train OpenAI?"

## Problems This Topic Solves

| Problem | Without governance |
|---------|-------------------|
| PII in LLM logs | GDPR fine, breach notification |
| Indefinite chat retention | Legal discovery nightmare |
| No deletion path | Violates "right to erasure" |
| Unknown subprocessors | Contract breach with enterprise customer |

## Learning Outcome

Create `COMPLIANCE.md` + data flow diagram + user deletion API that removes data from vector index.

---

### Lesson 7.1.1 — Concept: What Data Flows Through Your AI System?

**Map every data touchpoint:**
```
User question → API → Embed → Vector DB → LLM API → Response → Logs
                ↓
         User documents (ingestion)
```

**Questions legal asks:**
1. Where is data stored? (region)
2. Who are subprocessors? (OpenAI, Pinecone, AWS)
3. How long is data retained?
4. Can users delete their data?
5. Is data used to train models?

**Beginner exercise:** Draw your Module 04 RAG data flow on paper. Label every third party.

---

### Lesson 7.1.2 — Concept: GDPR, CCPA, and AI (Beginner)

**GDPR (EU):** Users have rights — access, delete, portability. Fines up to 4% global revenue.  
**CCPA (California):** Similar consumer rights for CA residents.  
**Key AI concepts:**
- **Lawful basis** — Why you process data (contract, consent, legitimate interest)
- **Data minimization** — Only send necessary text to LLM
- **Purpose limitation** — Don't use support chat logs for marketing AI

**Interview answer:** "Customer data is not used to train foundation models; we use API with zero-retention where available; subprocessors listed in DPA."

---

### Lesson 7.1.3 — Concept: HIPAA and SOC2 (Awareness)

**HIPAA:** US health data — PHI must be encrypted, access logged, BAA with vendors.  
**SOC2 Type II:** Audit of security controls over time — relevant to AI log retention, access control, change management.

**For beginners:** You don't need to be a lawyer — you need to **know when to escalate to legal** and implement engineering controls (encryption, audit logs, retention jobs).

---

### Lesson 7.1.4 — Beginner Coding: Data Retention Job

**Policy example:** Chat logs deleted after 90 days; vector embeddings for user-uploaded docs deleted on account deletion.

```python
async def delete_user_data(user_id: str):
    await db.execute("DELETE FROM chat_messages WHERE user_id = $1", user_id)
    await vector_store.delete(filter={"user_id": user_id})
    await audit_log.record("user_data_deleted", user_id=user_id)
```

**Guided lab:** Implement `DELETE /v1/users/{id}/data` endpoint.

**Production:** Soft-delete vs hard-delete — document in COMPLIANCE.md.

---

### Lesson 7.1.5 — Intermediate: DPIA-Lite (Data Protection Impact Assessment)

**Template sections:**
1. Feature description
2. Data categories (PII? special category?)
3. Risks (leak, wrong answer, retention)
4. Mitigations (encryption, RBAC, eval)
5. Residual risk + approval

**Mini project:** 2-page DPIA for your RAG capstone.

**Enterprise use case:** Required before launching HR or health copilot in EU.

---

### Lesson 7.1.6 — Intermediate: Vendor DPAs and Zero-Training Clauses

**DPA** = Data Processing Agreement with vendor  
**Check OpenAI/Anthropic/Azure enterprise terms:**
- API data not used for training (verify current policy)
- Data residency options (Azure region, Bedrock VPC)

**Subprocessor list in COMPLIANCE.md:**
| Vendor | Purpose | Data sent | Region |
|--------|---------|-----------|--------|
| OpenAI | LLM inference | Prompt + context | US |
| Pinecone | Vector storage | Embeddings | US |

---

### Lesson 7.1.7 — Advanced: EU AI Act Risk Categories (Practical Overview)

**Risk tiers (simplified):**
- **Unacceptable** — Banned (social scoring)
- **High-risk** — HR hiring, credit scoring — strict requirements
- **Limited risk** — Chatbots — transparency (disclose AI)
- **Minimal risk** — Most internal tools

**Engineering action:** User-facing disclaimer "You are chatting with AI" for limited-risk transparency.

---

### Lesson 7.1.8 — Enterprise: Compliance Appendix for Capstone

**Deliverables:**
- [ ] `COMPLIANCE.md` — lawful basis, retention, subprocessors
- [ ] Data flow diagram (Mermaid or draw.io)
- [ ] Deletion API tested
- [ ] Privacy-by-design checklist in PR template

**Topic 7.1 — Interview questions**
- Beginner: "Does customer data train OpenAI?"
- Intermediate: "Design GDPR delete for RAG system."
- Senior: "SOC2 auditor asks about AI log retention — answer?"

**Common beginner mistakes:** Sending full SSN in prompt; infinite log retention; no subprocessors doc.

---

# Topic 7.2 — AI Risk Management & Hallucination Prevention

## Beginner-Friendly Explanation

**Risk management** = identifying what could go wrong with AI and planning mitigations before users get hurt.

**Hallucination** = confident wrong answer. In consumer chat, annoying. In enterprise HR/legal/finance, **liability**.

**Analogy:** Seatbelts don't prevent accidents — they reduce harm. Abstention + citations + human review are seatbelts for AI.

## Why This Topic Matters in Real Companies

Enterprises fear: "Bot told employee wrong PTO policy → lawsuit." Engineers must quantify and reduce that risk.

## Problems This Topic Solves

- Always-answer bots that never say "I don't know"
- No escalation when confidence is low
- Hidden uncertainty (user trusts wrong answer)

## Learning Outcome

Build risk register + abstention when retrieval score < threshold + measured hallucination reduction on golden set.

---

### Lesson 7.2.1 — Concept: Risk Tiers for AI Features

| Tier | Example | Required controls |
|------|---------|-------------------|
| **Informational** | FAQ bot | Citations, disclaimer |
| **Decision-support** | Legal research assist | Human review, abstention |
| **Automated action** | Agent sends email | HITL, audit log, kill switch |

**Rule:** Higher tier = more human oversight, never less.

**Exercise:** Classify 5 features by risk tier.

---

### Lesson 7.2.2 — Beginner: Abstention Patterns

**When to abstain:**
- No chunks retrieved
- Top similarity score < 0.65
- Question outside domain ("What's the weather?")

```python
if not chunks or chunks[0].score < ABSTAIN_THRESHOLD:
    return {
        "answer": "I don't have enough information in our documents to answer confidently.",
        "sources": [],
        "abstained": True,
    }
```

**UX:** Show abstention clearly — don't fabricate.

**Guided lab:** Measure abstention rate on 30-question golden set.

---

### Lesson 7.2.3 — Intermediate: Confidence Scores

**Combine signals:**
- Retrieval similarity (max chunk score)
- LLM self-reported confidence (use carefully)
- Citation coverage (answer sentences map to chunks)

**Display in UI:** "Confidence: Medium — verify with HR before acting."

---

### Lesson 7.2.4 — Intermediate: Human Escalation Paths

**Flow:** Low confidence → create ticket in queue → human responds within SLA  
**Integrate:** Mock Zendesk/ServiceNow API in lab  
**Metrics:** Escalation rate, time-to-human-response

---

### Lesson 7.2.5 — Advanced: Risk Register

**Template (10 risks × mitigations × owner):**

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| Wrong PTO answer | Medium | High | RAG + abstention + eval | AI Lead |
| PII in response | Low | Critical | Output guardrails | Security |

**Portfolio:** `docs/risk-register.md` in capstone repo.

---

### Lesson 7.2.6 — Production: Post-Incident Eval Updates

**When incident occurs:** Add failing case to golden set → fix → re-eval → document in changelog.

**Enterprise:** Incident runbook for "AI gave harmful/wrong answer."

**Topic 7.2 — Interview:** "Bot gave wrong medical info — incident response?"

---

# Topic 7.3 — RBAC, Multi-Tenancy & Enterprise Integrations

## Beginner-Friendly Explanation

**Multi-tenancy** = one application serves many customers (tenants), each isolated — Tenant A never sees Tenant B's data.

**RBAC** = Role-Based Access Control — Admin sees all; User sees only their team's docs.

**Analogy:** Apartment building — same building, separate locked units. RBAC is who gets which key.

## Why This Topic Matters in Real Companies

B2B AI SaaS lives or dies on tenant isolation. One data leak = company destroyed.

## Problems This Topic Solves

- Global vector index without `tenant_id` filter → cross-tenant leak
- Stale SharePoint permissions after user fired
- Service account with god-mode access

## Learning Outcome

Two-tenant RAG demo with CI test: Tenant A query never returns Tenant B documents.

---

### Lesson 7.3.1 — Concept: Multi-Tenant Database Patterns

**Shared DB, shared schema + `tenant_id` column** (beginner-friendly, most common)  
**Rule:** EVERY query includes `WHERE tenant_id = :current_tenant`

```python
async def search(query: str, tenant_id: str, user_id: str):
    chunks = await vector_store.search(
        query,
        filter={"tenant_id": tenant_id, "acl": {"$in": user_permissions}},
    )
```

**Common beginner mistake:** Forgetting tenant filter on ONE endpoint — catastrophic.

---

### Lesson 7.3.2 — Beginner: JWT Authentication Basics

**JWT** = JSON Web Token — proves who user is after login  
**Flow:** Login → receive JWT → send `Authorization: Bearer <token>` on every API call  
**Claims in token:** `user_id`, `tenant_id`, `roles[]`

**Guided lab:** Mock JWT middleware on FastAPI (use `python-jose` or mock decode for learning).

---

### Lesson 7.3.3 — Intermediate: OAuth2 / OIDC with Enterprise IdP

**OAuth2** = delegated authorization ("App can access my SharePoint")  
**OIDC** = identity layer on OAuth (who is the user)  
**Enterprise IdPs:** Microsoft Entra ID, Okta, Google Workspace

**Pattern:** User logs in via Entra → app gets token → API validates → extract tenant + groups

**Production:** Use managed libraries; never roll your own crypto.

---

### Lesson 7.3.4 — Intermediate: ACL-Aware Retrieval

**Problem:** User loses access to doc in SharePoint — RAG must not serve it next day.

**Solution:**
1. Store `allowed_groups[]` metadata on each chunk at ingest
2. Filter retrieval by user's current groups every query
3. Nightly sync job refreshes ACL metadata

**Guided lab (Intermediate):** Two users, same tenant, different doc access — prove isolation.

---

### Lesson 7.3.5 — Advanced: Enterprise Connector Patterns

**SharePoint / Confluence / Salesforce:**
- OAuth delegated auth (user context) vs service account (batch ingest)
- Webhook on doc update → re-embed pipeline
- Rate limits per tenant (fair usage)

**Architecture diagram:** Connector → ingest queue → chunk → embed → vector DB with ACL metadata

---

### Lesson 7.3.6 — Enterprise: Per-Tenant Rate Limits and Quotas

```python
async def check_quota(tenant_id: str):
    usage = await redis.get(f"tokens:{tenant_id}:{month}")
    if usage > tenant_plan.limit:
        raise HTTPException(429, "Monthly token quota exceeded")
```

**FinOps link (Module 06):** Attribute cost per tenant.

**Topic 7.3 — System design:** "Design multi-tenant RAG for 500 enterprise customers."

---

# Topic 7.4 — AI Consulting & Transformation Delivery

## Beginner-Friendly Explanation

**AI Consultant** = helps companies figure out *what* AI to build, *whether* it's worth it, and *how* to go from demo to production.

**POC** = Proof of Concept — small 2–4 week experiment to prove value before big investment.

**Analogy:** Architect's sketch before building a house — cheap, fast, validates the idea.

## Why This Topic Matters in Real Companies

Consulting is **#2 fastest-growing AI role**. Technical consultants who ship POCs win $500K+ engagements.

## Problems This Topic Solves

- "We need ChatGPT for everything" → unfocused waste
- POCs without success metrics → never get funded
- No production handoff → POC dies in slide deck

## Learning Outcome

Write 5-page POC proposal + consulting case study + reusable POC starter kit in GitHub.

---

### Lesson 7.4.1 — Concept: Build vs Buy vs Partner

| Option | When |
|--------|------|
| **Buy** | Commodity (ChatGPT Enterprise, Copilot) |
| **Build** | Differentiating IP, custom data |
| **Partner** | SI/consultant for speed |

**Framework for discovery workshops.**

---

### Lesson 7.4.2 — Beginner: Discovery Workshop Questions

1. What problem costs money today? (time, errors, churn)
2. What data exists? (quality, access, compliance)
3. Who is the user? (employee, customer, both)
4. What does success look like in 4 weeks?
5. What are kill criteria? (when to stop POC)

**Exercise:** Run mock discovery with peer for fictional retail client.

---

### Lesson 7.4.3 — Intermediate: POC Scope Control

**Thin vertical slice:** One user type, one doc set, one workflow — NOT full platform.

**Success metrics examples:**
- Faithfulness ≥ 0.85 on 50 SME-validated questions
- 30% reduction in L1 support ticket volume (pilot)
- NPS ≥ 40 from 20 beta users

**Timeline:** 2–4 weeks fixed. Production estimate = separate SOW.

---

### Lesson 7.4.4 — Intermediate: ROI Estimation

**Simple ROI:** `(hours_saved × hourly_rate × users) - AI_cost - build_cost`  
**Document assumptions** — sponsors care about logic, not false precision.

**Spreadsheet template in POC kit.**

---

### Lesson 7.4.5 — Advanced: Production Handoff Documentation

**Handoff pack:**
- Architecture diagram
- Eval results + golden set
- Runbooks, COMPLIANCE.md
- Known limitations
- 6-month roadmap estimate

**Consulting portfolio:** Case study — Problem → POC → Metrics → Lessons → Production plan.

---

### Topic 7.4 — Interview & Freelancing

**Interview:** "Client wants ChatGPT for everything — refocus how?"  
**Freelancing:** Upwork/Toptal enterprise POCs — $5K–$50K engagements with this skillset.  
**Startup:** Same discovery skills for finding product-market fit.

---

# Module 07 — Capstone & Labs Summary

## Week Progression

| Week | Focus |
|------|-------|
| 31 | Compliance + data flow + deletion API |
| 32 | Risk register + abstention + escalation |
| 33 | Multi-tenant RAG + RBAC tests in CI |
| 34 | Consulting POC proposal + case study |

## Required Deliverables

- [ ] `COMPLIANCE.md` + data flow diagram
- [ ] User deletion from vector index
- [ ] Two-tenant demo with CI isolation test
- [ ] Risk register (10 risks)
- [ ] 5-page POC proposal (fictional client OK)
- [ ] `docs/enterprise-integrations.md` architecture sketch

## Master Checklist Before Module 08

| Question | Yes / No |
|----------|----------|
| Can I explain GDPR delete for RAG in an interview? | |
| Does every DB query filter by tenant_id? | |
| Does my bot abstain when retrieval is weak? | |
| Do I have COMPLIANCE.md in capstone repo? | |

**Next:** Module 08 deploys enterprise AI on **AWS, Azure, and GCP**.

---

*Next: [module-08-cloud-ai.md](./module-08-cloud-ai.md)*
