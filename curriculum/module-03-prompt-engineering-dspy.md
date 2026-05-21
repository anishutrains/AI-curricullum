# Module 03 — Prompt Engineering & DSPy

---

## Topic 3.1: Production Prompt Engineering

### 1. Topic Name
Production Prompt Engineering

### 2. Why This Topic Matters
Prompting is table stakes, but **versioned, tested, measurable** prompts separate hires from hobbyists. Prompt Engineer roles merge into AI Engineer with eval discipline.

### 3. Job Roles
Prompt Engineer, LLM Engineer, Generative AI Engineer, AI Product Engineer

### 4. Learning Objectives
- Apply CO-STAR, few-shot, chain-of-thought appropriately
- Version prompts in Git with semantic tags
- Measure quality with golden datasets

### 5. Lessons/Subtopics
- System vs user vs developer messages
- Few-shot selection strategies
- Chain-of-thought and decomposition
- Role and tone control for enterprise brand
- Prompt templates (Jinja2) separation
- Anti-patterns: prompt injection in instructions

### 6. Hands-on Labs
**Lab 3.1:** Prompt registry (`prompts/v1/support_system.yaml`) + A/B test harness.

### 7. Enterprise Projects
Approval workflow: dev → staging prompt → prod with sign-off.

### 8. Portfolio Projects
Before/after eval scores on 50-example golden set.

### 9. Interview Preparation
- "How do you version and roll back prompts?"
- Live: improve a weak support prompt with measurable criteria

### 10. Real-world Use Cases
Brand-safe customer agents, legal tone control, sales email generation.

### 11. Tools & Technologies
promptfoo, LangSmith (prompt hub), YAML/Git, Jinja2

### 12. Common Mistakes
- Giant monolithic system prompt (context waste)
- No few-shot refresh when product changes
- Changing prod prompts without regression tests

### 13. Industry Best Practices
- One concern per prompt module (compose)
- Document intended model per prompt
- Track token length budgets per template

### 14. Capstone Deliverables
Prompt library with 3 domains + promptfoo CI gate on `main`.

---

## Topic 3.2: DSPy — Programmatic Prompt Optimization

### 1. Topic Name
DSPy for Optimized LLM Pipelines

### 2. Why This Topic Matters
DSPy represents shift from manual prompt hacking to **compiled, optimizable pipelines**—increasingly cited in advanced AI teams.

### 3. Job Roles
LLM Engineer, Applied AI Engineer, AI Research-adjacent Engineer

### 4. Learning Objectives
- Build DSPy modules (Signature, ChainOfThought, ReAct)
- Run optimizers (BootstrapFewShot, MIPRO)
- Export optimized prompts to production non-DSPy path

### 5. Lessons/Subtopics
- Signatures and modules
- Teleprompters / optimizers
- Metrics functions for optimization
- Bridging DSPy → frozen prompts for latency
- Comparison vs manual prompting ROI

### 6. Hands-on Labs
**Lab 3.2:** Optimize classification module; achieve +10% F1 vs manual prompt on holdout.

### 7. Enterprise Projects
Offline optimization pipeline; deploy only frozen approved artifacts.

### 8. Portfolio Projects
Notebook + exported `optimized_prompt.json` in repo.

### 9. Interview Preparation
- "What is DSPy and when would you use it vs LangChain?"
- "How do you prevent overfitting prompts to eval set?"

### 10. Real-world Use Cases
High-volume classification, extraction, routing decisions.

### 11. Tools & Technologies
DSPy, dspy-ai, OpenAI/Anthropic via LiteLLM

### 12. Common Mistakes
- Optimizing on tiny datasets
- Deploying slow compile-time chains to hot path
- No holdout set separation

### 13. Industry Best Practices
- Holdout 20% never seen by optimizer
- Human review before promoting optimized prompts
- Log optimizer version in metadata

### 14. Capstone Deliverables
DSPy-optimized extractor beating baseline in documented eval report.

---

## Topic 3.3: Prompt Security & Injection Defense

### 1. Topic Name
Prompt Injection Defense & Input Sanitization

### 2. Why This Topic Matters
As agents gain tool access, injection becomes **critical security**. AI Security Engineer roles require this fluency.

### 3. Job Roles
AI Security Engineer, Enterprise AI Engineer, Responsible AI Engineer

### 4. Learning Objectives
- Classify direct vs indirect injection
- Implement input/output guardrails
- Design privilege boundaries for tools

### 5. Lessons/Subtopics
- OWASP LLM Top 10 overview
- System prompt hardening (limited efficacy)
- Input filters, allowlists, canonicalization
- Output validation before tool execution
- Dual-LLM pattern, Llama Guard classifiers
- Human-in-the-loop for high-risk actions

### 6. Hands-on Labs
**Lab 3.3:** Red-team 10 injection attacks against your chatbot; fix and re-test.

### 7. Enterprise Projects
Security test suite in CI: known injection cases must fail safe.

### 8. Portfolio Projects
`SECURITY.md` with threat model and mitigations.

### 9. Interview Preparation
- "User says 'ignore previous instructions'—architecture response?"
- "How do you secure agent tool calling?"

### 10. Real-world Use Cases
Customer-facing bots, email-to-agent pipelines (indirect injection).

### 11. Tools & Technologies
NeMo Guardrails, Llama Guard, Rebuff, custom regex + ML filters

### 12. Common Mistakes
- Trusting system prompt alone
- Giving agents unrestricted shell/network
- Logging user content with secrets

### 13. Industry Best Practices
- Least-privilege tool scopes
- Separate control plane from data plane
- Rate limit and anomaly detection on inputs

### 14. Capstone Deliverables
Injection test suite passing in CI; documented residual risks.

---

*Next: [module-04-rag-systems.md](./module-04-rag-systems.md)*
