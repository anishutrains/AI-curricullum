# Module 06 — LLMOps (Large Language Model Operations)
### Zero-to-Hero Track · Weeks 26–30 · From "It Works on My Laptop" to Production AI

---

## Why This Module Matters

**Why learn this NOW?**  
Modules 01–05 taught you to **build** AI apps: APIs, RAG, agents. Module 06 teaches you to **operate** them — measure quality, trace failures, control cost, deploy safely, and prove reliability to employers. **LLMOps** is the #1 skill gap between tutorial developers and hireable AI engineers in the US market (2026–2027).

**Real-world importance**
- A RAG chatbot that "looks fine" in demo can **hallucinate silently** in production for weeks.
- An agent without tracing is **impossible to debug** when a customer reports a wrong answer.
- Companies like **Notion, Intercom, and Duolingo** ship AI features with eval CI gates — not vibes.

**What breaks without LLMOps**
| Without LLMOps | What happens |
|----------------|--------------|
| No tracing | "Something broke" — no idea which step failed |
| No eval | Prompt change degrades quality; nobody notices until users complain |
| No cost tracking | $50K surprise OpenAI bill |
| No guardrails | PII leaked, toxic output, compliance violation |
| No versioning | Prod prompt edited in dashboard; cannot rollback |

**How this connects to the career path**
| Module 05 (Agents) | Module 06 (LLMOps) | Module 07+ (Enterprise) |
|--------------------|--------------------|-------------------------|
| Agent tool loops | **Trace every tool call** | Multi-tenant cost attribution |
| RAG pipeline | **Eval faithfulness in CI** | Governance + audit |
| HITL approval | **Monitor approval SLAs** | SOC2-ready logging |

**Prerequisites (mandatory)**
- Module 01: FastAPI, Docker, GitHub Actions basics
- Module 02: LLM API calls, token counting
- Module 03: Prompt templates, basic eval mindset
- Module 04: Working RAG project (you will instrument this)
- Module 05: Agent or multi-step workflow (optional but recommended for tracing labs)

**Future modules that depend on Module 06**
- **Module 07 (Enterprise):** Governance builds on model registry + guardrails
- **Module 08 (Cloud):** Cloud-native observability (CloudWatch, Azure Monitor)
- **Module 11 (Production Architecture):** SLOs, scaling, disaster recovery

---

## Which AI Job Roles Require This

| Role | LLMOps skills needed |
|------|---------------------|
| **LLMOps Engineer** | Core job function — observability, eval, CI/CD |
| **AI Reliability Engineer** | SLOs, alerting, incident response |
| **AI Platform Engineer** | Registries, pipelines, multi-tenant infra |
| **RAG Engineer** | RAG-specific eval and retrieval monitoring |
| **Generative AI Engineer** | Production deployment discipline |
| **Enterprise AI Engineer** | Governance, guardrails, audit trails |
| **MLOps Engineer (GenAI focus)** | Overlapping observability + model lifecycle |
| **Applied AI Engineer** | Prove quality to stakeholders with metrics |

**Recruiter signal:** README with **faithfulness score + trace screenshot + cost dashboard** instantly separates you from 90% of "I built a chatbot" candidates.

**Salary impact:** LLMOps / AI Platform roles cluster **$155K–$220K** US base (2026). Engineers who can say "I gate releases on eval regression" command senior-band interviews.

---

## Beginner Skills Students Will Learn

- Explain monitoring vs observability in plain English
- Log LLM latency and token usage to a file or console
- Run a first **Ragas** faithfulness score on 10 questions
- Understand what a trace, span, and request ID are
- Set up **Langfuse** locally and capture one chat trace

## Intermediate Skills Students Will Learn

- Instrument full RAG pipeline: retrieve → generate → response
- Build golden datasets (30–100 Q&A pairs) with versioning
- Run **DeepEval** and **promptfoo** in local CI
- Create Grafana dashboards for latency and cost
- Version prompts in Git with changelog

## Advanced Skills Students Will Learn

- OpenTelemetry instrumentation across microservices
- Eval CI gates that block bad merges
- Canary prompt deployments with automatic rollback
- RAG-specific monitoring: retrieval hit rate, citation accuracy
- LLM-as-judge eval with bias mitigation

## Enterprise Production Skills Students Will Learn

- Multi-tenant cost attribution (FinOps)
- Guardrails with audit logging (NeMo / Guardrails AI)
- Model registry with approval workflows
- PII scrubbing in traces; sampling strategies for prod
- SOC2-ready retention policies and runbooks

---

## Skill Progression in This Module

| Level | You will... |
|-------|-------------|
| **Beginner** | Log tokens/latency; run first Ragas eval; see one trace in Langfuse |
| **Intermediate** | Full observability on RAG; golden set + CI eval |
| **Advanced** | OpenTelemetry + Grafana; prompt canary + rollback |
| **Production** | Alerting, SLIs, cost caps, guardrail metrics |
| **Enterprise** | Multi-tenant FinOps, model registry, governance pack |

---

# Topic 6.1 — Observability, Tracing & Monitoring

## Beginner-Friendly Explanation

**Monitoring** tells you *something is wrong* ("error rate spiked").  
**Observability** lets you ask *why* ("which retrieval step returned empty chunks for user X?").

**Analogy:** Monitoring is a car dashboard warning light. Observability is the mechanic's diagnostic tool that shows exactly which cylinder failed.

AI systems fail **silently** — wrong answers often return HTTP 200. You need traces, not just uptime checks.

## Why Companies Use This

- Debug production incidents in minutes, not days
- Prove SLA compliance (p95 latency < 3s)
- Attribute AI cost per customer (FinOps)
- Correlate user complaints to specific prompt/model versions

## What Problem This Solves

Without observability, AI teams fly blind: they cannot answer "Did retrieval fail or did the LLM hallucinate?" — the most common production debugging question.

## Learning Outcome

Instrument your Module 04 RAG API with Langfuse traces; build a Grafana dashboard showing latency, error rate, and cost per query.

---

### Lesson 6.1.1 — Concept: What Is Observability?

**Monitoring vs observability**
| Monitoring | Observability |
|------------|---------------|
| Predefined metrics/alerts | Explore unknown unknowns |
| "Is it up?" | "Why is quality down?" |
| Uptime, 5xx rate | Trace through RAG pipeline |

**Why AI systems fail silently**
- LLM returns confident wrong answer → HTTP 200
- Retrieval returns irrelevant chunks → no error thrown
- Token costs spike → no exception

**Production AI debugging challenges**
- Non-deterministic outputs
- Multi-step pipelines (retrieve → rerank → generate)
- External API dependencies (OpenAI, Pinecone)

**Exercise:** List 5 things that can go wrong in RAG that do NOT produce an HTTP error.

**Future dependency:** Every Topic 6.2–6.4 eval and guardrail metric feeds observability dashboards.

---

### Lesson 6.1.2 — Concept: Traditional Monitoring vs AI Monitoring

**Traditional API monitoring**
- Request count, latency, error rate (4xx/5xx)
- CPU, memory, disk

**LLM-specific monitoring (you must add these)**
| Metric | Why it matters |
|--------|----------------|
| **Tokens in/out** | Cost control |
| **Time-to-first-token (TTFT)** | User experience (streaming) |
| **Retrieval latency** | RAG bottleneck identification |
| **Chunks retrieved** | Empty retrieval = silent failure |
| **Faithfulness score (sampled)** | Quality degradation |
| **Guardrail trigger rate** | Safety incidents |

**Hallucination detection:** Not one metric — combine eval sampling + user thumbs-down + citation checks.

**Beginner coding:** Add to your FastAPI RAG endpoint:

```python
import time

@app.post("/v1/rag/query")
async def rag_query(body: QueryRequest):
    start = time.perf_counter()
    tokens_in, tokens_out = 0, 0
  # ... your RAG logic ...
    latency_ms = (time.perf_counter() - start) * 1000
    log_metric({
        "latency_ms": latency_ms,
        "tokens_in": tokens_in,
        "tokens_out": tokens_out,
        "chunks_retrieved": len(chunks),
    })
```

**Production consideration:** Structured JSON logs → later ship to Grafana Loki or Datadog.

---

### Lesson 6.1.3 — Concept: Understanding Traces, Spans, and Request IDs

**Request lifecycle**
```
User request (trace_id=abc123)
  ├── Span: authenticate_user (12ms)
  ├── Span: embed_query (45ms)
  ├── Span: vector_search (120ms)
  ├── Span: llm_generate (2100ms)
  └── Span: format_response (3ms)
```

**Trace** — Full journey of one user request  
**Span** — One unit of work inside a trace  
**Attributes** — Key-value metadata on spans (`model=gpt-4o-mini`, `top_k=5`)

**Distributed systems:** API → worker → vector DB → LLM — same `trace_id` across all services.

**Beginner exercise:** Draw a trace diagram for your RAG pipeline on paper before coding.

**Common beginner mistake:** Logging without a shared `request_id` — cannot correlate logs across steps.

---

### Lesson 6.1.4 — Concept: Introduction to OpenTelemetry

**What is OpenTelemetry (OTel)?**  
Industry-standard way to collect **traces, metrics, and logs** — vendor-neutral (works with Langfuse, Datadog, Jaeger).

**Core concepts**
- **Instrumentation** — Add OTel SDK calls in your code
- **Exporter** — Send data to backend (Langfuse, OTLP collector)
- **Collector** — Optional middle layer for filtering/routing

**When to use:** Multi-service architectures, enterprise standardization.

**Beginner path:** Start with Langfuse SDK (simpler) → add OTel later (Lesson 6.1.7).

**Architecture discussion:** OTel Collector → Langfuse + Prometheus is a common production pattern.

---

### Lesson 6.1.5 — Beginner Implementation: Langfuse Fundamentals

**What is Langfuse?** Open-source LLM observability — traces, prompts, evals, cost tracking. Free tier for learning.

**Setup (local)**
1. Sign up at langfuse.com OR self-host with Docker
2. Create project → copy `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`
3. Install: `pip install langfuse`

**Capture your first trace**

```python
from langfuse import Langfuse
from langfuse.decorators import observe

langfuse = Langfuse()

@observe()
def retrieve_chunks(query: str):
    # your retrieval logic
    return chunks

@observe()
def generate_answer(query: str, chunks: list):
    # your LLM call
    return answer

@observe()
def rag_pipeline(query: str):
    chunks = retrieve_chunks(query)
    return generate_answer(query, chunks)
```

**Deliverable:** Run one query; see nested spans in Langfuse UI.

**Guided lab (Beginner):** Instrument Module 04 chatbot — 3 spans minimum: retrieve, generate, total.

**Portfolio task:** Screenshot of Langfuse trace in README.

---

### Lesson 6.1.6 — Intermediate: Monitoring RAG Systems Specifically

**Retrieval monitoring**
| Signal | Alert if... |
|--------|-------------|
| `chunks_retrieved == 0` | Retrieval miss — likely bad answer |
| `avg_similarity_score < 0.7` | Embedding/query mismatch |
| `retrieval_latency_p95 > 500ms` | Vector DB bottleneck |

**Hallucination detection (practical)**
- Sample 1–5% of prod queries → run Ragas faithfulness async
- Check: answer cites retrieved chunk IDs
- User feedback: thumbs down → attach trace_id for review

**Source attribution monitoring:** Log whether API response included `sources[]` and count.

**Mini project:** Add `retrieval_quality` span attribute: `{chunk_count, top_score, filter_applied}`.

**Common production failure:** Retrieval returns chunks from wrong tenant — monitor `tenant_id` in span attributes.

---

### Lesson 6.1.7 — Intermediate: OpenTelemetry + Langfuse Integration

**Why combine:** OTel for infra-wide tracing; Langfuse for LLM-native UI (prompts, token costs).

**Pattern:** Instrument FastAPI with OTel FastAPI middleware → export to Langfuse OTLP endpoint.

**Coding exercise:** Add OTel to one endpoint; verify trace appears in Langfuse with HTTP span + custom LLM span.

**Production consideration:** Sample 10% of traces in prod to control cost; 100% in staging.

---

### Lesson 6.1.8 — Intermediate: User and Session Correlation

**Problem:** "User 48291 reported wrong answer Tuesday" — find their trace.

**Solution:** Propagate `user_id`, `session_id`, `tenant_id` as span attributes and log fields.

```python
@observe()
def rag_pipeline(query: str, user_id: str, session_id: str):
    langfuse_context.update_current_trace(
        user_id=user_id,
        session_id=session_id,
    )
```

**Enterprise use case:** Support team clicks user ID → opens trace history in Langfuse.

**Security:** Hash or pseudonymize PII in user_id fields where required.

---

### Lesson 6.1.9 — Production: Prometheus Metrics and Grafana Dashboards

**Prometheus** — Time-series metrics store (pull model)  
**Grafana** — Visualization dashboards

**AI metrics to expose at `/metrics`**
```
llm_requests_total{model="gpt-4o-mini", status="success"}
llm_latency_seconds_bucket{step="retrieval"}
llm_tokens_total{direction="input"}
llm_cost_usd_total
rag_chunks_retrieved_bucket
```

**Beginner Grafana setup**
1. Run Prometheus + Grafana via Docker Compose
2. Scrape your FastAPI `/metrics` endpoint
3. Build panels: p50/p95 latency, tokens/hour, cost/day

**Guided lab (Intermediate):** Dashboard with 4 panels — latency, errors, tokens, cost.

**Resume-worthy deliverable:** Dashboard screenshot + link to `docker-compose.observability.yml` in GitHub.

---

### Lesson 6.1.10 — Production: Alerting and Runbooks

**Alerts that matter for AI (not just 5xx)**
| Alert | Threshold example |
|-------|-------------------|
| Error rate | > 2% for 5 min |
| p95 latency | > 5s for 10 min |
| Cost anomaly | Daily spend > 150% of 7-day avg |
| Empty retrieval rate | > 10% of queries |
| Faithfulness (sampled) | < 0.75 on hourly batch |

**Runbook template:** Alert name → how to triage → which dashboard → escalation path.

**Exercise:** Write a 1-page runbook: "RAG p95 latency spike."

**Common production failure:** Alert fatigue — start with 3 critical alerts only.

---

### Lesson 6.1.11 — Production: PII Scrubbing in Traces

**Risk:** Full prompts/responses in traces may contain SSN, email, medical info.

**Mitigations**
- Redact known patterns before export (regex email, SSN)
- Truncate prompts to first 200 chars in prod
- Store full traces only in staging; prod gets metadata only
- Langfuse: configure data retention (30 days default)

**Enterprise / compliance:** GDPR, HIPAA — legal review of trace retention policy.

**Assignment:** Add `scrub_pii(text)` before logging; test with fake SSN in prompt.

---

### Lesson 6.1.12 — Enterprise: Multi-Tenant Observability and FinOps

**Multi-tenant cost attribution**
- Tag every span with `tenant_id`
- Weekly report: cost per tenant, queries per tenant, cost per query

**FinOps dashboard panels**
- Top 10 tenants by spend
- Cost per feature (RAG vs agent vs chat)
- Budget burn rate vs monthly cap

**SLA monitoring**
- Per-tenant p95 latency
- Uptime SLO 99.9% with error budget

**Enterprise use case:** SaaS AI platform bills customers based on token usage — requires accurate per-tenant metrics.

**Architecture discussion:** Whiteboard multi-tenant observability for 1000 customers.

---

### Topic 6.1 — Labs, Projects & Assessments

**Beginner labs**
- Log latency + tokens to JSON file for 10 queries
- Langfuse: first nested trace on chatbot

**Intermediate labs**
- Full RAG instrumentation (retrieve + generate spans)
- Grafana dashboard (4 panels)

**Advanced labs**
- OTel + Langfuse integration
- Alert on empty retrieval rate

**Enterprise labs**
- Per-tenant cost report script
- PII scrubbing pipeline

**Mini project:** "RAG Observability Pack" — Langfuse + Grafana + README screenshot

**Beginner interview questions**
- What is the difference between monitoring and observability?
- Why can an AI app return 200 OK but still be "broken"?

**Intermediate interview questions**
- What metrics would you put on an AI SLA dashboard?
- How do you debug "user got wrong answer" in production?

**Senior / system design questions**
- Design observability for a multi-tenant RAG SaaS with 1M queries/day.
- How do you balance trace sampling vs debugging ability vs cost?

**Common beginner mistakes**
- Only logging final answer, not retrieval step
- No request_id across pipeline
- Storing full prompts with PII in prod

**Common production failures**
- Alerts only on 500 errors, not quality degradation
- No cost alerts until finance notices bill

**GitHub portfolio tasks**
- [ ] Langfuse trace screenshot in README
- [ ] `docker-compose.observability.yml`
- [ ] `docs/runbook-latency-spike.md`

---

# Topic 6.2 — Evaluation Pipelines (Ragas, DeepEval, promptfoo)

## Beginner-Friendly Explanation

**Eval** answers: "How do we **know** the AI works?" — not "it looked good when I tried it once."

**Analogy:** Unit tests for code. Golden datasets + metrics for AI.

**Golden dataset** — Curated question/answer pairs with expected behavior (e.g., "Must cite policy section 4.2").

## Why Companies Use This

- Block bad prompt/model changes before users see them
- Compare GPT-4o vs Claude on **your** data, not benchmarks
- Satisfy compliance: "We test weekly with 500 cases"

## What Problem This Solves

#1 hiring gap: tutorial devs cannot answer **"How do you know it works?"** Eval CI is the professional answer.

## Learning Outcome

Build a 50-question golden set for your RAG project; run Ragas in GitHub Actions; fail merge if faithfulness drops >5%.

---

### Lesson 6.2.1 — Concept: Why Demos Lie and Eval Doesn't

**Demo problems**
- Cherry-picked questions
- Small document set
- No edge cases (empty retrieval, typos, adversarial)

**What eval measures**
| Dimension | Question |
|-----------|----------|
| **Faithfulness** | Is answer grounded in retrieved context? |
| **Relevance** | Does answer address the question? |
| **Context precision** | Were retrieved chunks useful? |
| **Context recall** | Did we retrieve all needed info? |

**Connect Module 04:** You previewed Ragas — now build the full pipeline.

**Exercise:** Write 5 "trap" questions your RAG should fail on (tests honest eval).

---

### Lesson 6.2.2 — Concept: Building Golden Datasets (Beginner)

**Structure per row**
```json
{
  "question": "What is the PTO policy for contractors?",
  "expected_answer_contains": ["not eligible", "full-time"],
  "source_doc": "hr-handbook.pdf",
  "difficulty": "medium",
  "category": "hr-policy"
}
```

**How many?** Start 30 → grow to 100+ for portfolio; enterprise uses 500+

**Sources for questions**
- Real support tickets (anonymized)
- SME interviews
- Adversarial: typos, ambiguous, out-of-scope

**Beginner coding:** Create `eval/golden_set.jsonl` with 30 rows from your Module 04 docs.

**Common beginner mistake:** Golden set too easy — all answers in first chunk.

**Version control:** Store in Git; tag versions `golden-v1.0`, `golden-v1.1`.

---

### Lesson 6.2.3 — Beginner Implementation: Ragas Fundamentals

**Install:** `pip install ragas`

**Core metrics (RAG-focused)**
- `faithfulness` — Answer supported by context?
- `answer_relevancy` — On-topic?
- `context_precision` / `context_recall` — Retrieval quality

**First eval script**

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from datasets import Dataset

dataset = Dataset.from_dict({
    "question": questions,
    "answer": answers,
    "contexts": contexts_list,
    "ground_truth": ground_truths,  # optional
})

result = evaluate(dataset, metrics=[faithfulness, answer_relevancy])
print(result)
```

**Guided lab (Beginner):** Run Ragas on 10 questions; record baseline faithfulness.

**Target for portfolio:** Faithfulness ≥ 0.80 on 30-question set (Module 04 capstone extended).

---

### Lesson 6.2.4 — Intermediate: Ragas Production Pipeline

**Pipeline stages**
1. Load golden set version
2. Run RAG pipeline → collect answers + contexts
3. Compute Ragas metrics
4. Compare to baseline JSON
5. Pass/fail gate

**Store results:** `eval/results/2026-05-21_run_042.json`

**Track over time:** Line chart of faithfulness per release — MLflow or simple CSV.

**Production consideration:** Eval runs cost tokens (LLM-as-judge inside Ragas) — run on subset in CI, full set nightly.

---

### Lesson 6.2.5 — Intermediate: DeepEval for Test Cases

**DeepEval** — Pytest-style LLM unit tests

```python
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric

def test_pto_question():
    test_case = LLMTestCase(
        input="PTO for contractors?",
        actual_output=rag_answer,
        retrieval_context=chunks,
    )
    assert_test(test_case, [AnswerRelevancyMetric(threshold=0.7)])
```

**When to use:** Per-feature pytest in CI; Ragas for batch dataset eval.

**Guided lab:** 5 DeepEval tests for critical HR policy questions.

---

### Lesson 6.2.6 — Intermediate: promptfoo for Prompt Comparison

**promptfoo** — YAML-defined eval suites; compare prompt A vs B vs model C.

```yaml
prompts:
  - file://prompts/v1.txt
  - file://prompts/v2.txt
providers:
  - openai:gpt-4o-mini
tests:
  - vars:
      question: "What is the refund policy?"
    assert:
      - type: contains
        value: "30 days"
```

**Use case:** A/B test system prompts before canary deploy (Topic 6.3).

**Exercise:** Compare two RAG prompt templates on 20 questions; document winner with scores.

---

### Lesson 6.2.7 — Advanced: LLM-as-Judge — Power and Pitfalls

**Pattern:** Use GPT-4o to score another model's answer.

**Pitfalls**
| Bias | Mitigation |
|------|------------|
| Judge favors longer answers | Rubric with length penalty |
| Same-model bias | Use different judge model |
| Position bias | Swap answer order |
| Cost | Cache judge results |

**Human eval sampling:** Weekly review 50 random prod queries — gold standard for calibration.

**Enterprise:** Human + automated hybrid; automated gates CI, human audits compliance.

---

### Lesson 6.2.8 — Advanced: Eval in CI/CD (GitHub Actions)

```yaml
name: RAG Eval Gate
on: [pull_request]
jobs:
  eval:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt
      - run: python eval/run_ragas.py --golden eval/golden_v1.jsonl
      - run: python eval/check_regression.py --max-drop 0.05
```

**Regression check:** Fail if faithfulness drops >5% vs `eval/baseline.json`.

**Guided lab (Advanced):** PR fails when you deliberately break retrieval.

**Portfolio badge:** README shield "Faithfulness 0.87 | 100 cases"

---

### Lesson 6.2.9 — Production: Eval Cost, Speed, and Scheduling

| Schedule | Scope | Cost |
|----------|-------|------|
| Every PR | 20-question smoke set | ~$0.50 |
| Nightly | Full 100-question set | ~$5 |
| Weekly | Full + human sample | ~$5 + labor |

**Optimize:** Cache embeddings for golden questions; reuse retrieved contexts when testing prompt-only changes.

---

### Lesson 6.2.10 — Enterprise: Per-Tenant and Vertical Golden Sets

**Multi-tenant SaaS:** Each customer may need custom golden set (their docs, their policies).

**Vertical eval:** Healthcare bot — separate set for HIPAA boundary questions.

**Governance:** Golden set changes require SME approval PR.

**Architecture discussion:** Eval service as internal microservice with tenant isolation.

---

### Topic 6.2 — Labs, Projects & Assessments

**Beginner labs**
- 30-row golden set creation
- First Ragas run on 10 questions

**Intermediate labs**
- DeepEval pytest suite (5 tests)
- promptfoo prompt A/B on 20 questions

**Advanced labs**
- GitHub Action eval gate
- Regression baseline tracking

**Enterprise labs**
- Eval report artifact per release (`eval-report-v2.3.pdf`)

**Beginner project:** Basic RAG observability + 10-question eval score in README

**Intermediate project:** Full eval pipeline with CI gate

**Advanced project:** Eval dashboard — faithfulness trend over last 10 releases

**Assignments**
- Add 10 adversarial questions to golden set
- Document one eval failure and root cause fix

**Beginner interview questions**
- What is a golden dataset?
- What is faithfulness in RAG eval?

**Intermediate interview questions**
- Design eval pipeline for RAG chatbot.
- How do you prevent eval set leakage into prompts?

**Senior / system design questions**
- Eval at 1M queries/day — sampling strategy?
- How to eval multi-agent systems where path varies?

**Common beginner mistakes**
- Eval set too small (<20)
- Only happy-path questions
- Changing metrics without versioning

**Common production failures**
- Eval only offline — no prod feedback loop
- LLM-as-judge without human calibration

**Job alignment:** RAG Engineer and LLMOps JDs explicitly ask for Ragas/DeepEval — list on resume with scores.

---

# Topic 6.3 — Prompt Versioning, Experiment Tracking & AI CI/CD

## Beginner-Friendly Explanation

**Prompts are code.** Changing a system prompt without versioning is like editing production code without Git — you cannot rollback, blame, or review.

**AI CI/CD** = automated pipeline: test → eval → deploy → monitor → rollback if bad.

## Why Companies Use This

- Safe prompt updates (canary 5% → 100%)
- Audit trail: who changed what, when, why
- Experiment tracking: "Prompt v3 improved faithfulness 4%"

## What Problem This Solves

Hot-editing prompts in OpenAI dashboard → untracked changes → incident → no rollback. Enterprise forbids this.

## Learning Outcome

Store prompts in Git registry; run eval on PR; deploy prompt v2 to 5% traffic with feature flag; auto-rollback on eval failure.

---

### Lesson 6.3.1 — Concept: Prompts as Immutable Artifacts

**Anti-pattern:** Edit system prompt in Langfuse UI → prod changes instantly  
**Best practice:** Prompt file in Git → PR → eval passes → promote to registry → deploy

**Prompt registry fields**
```
prompt_id: rag-system-v2
version: 2.1.0
author: engineer@company.com
eval_faithfulness: 0.86
approved_by: lead@company.com
deployed_at: 2026-05-21
```

**Beginner exercise:** Move your RAG system prompt from Python string to `prompts/rag_system_v1.txt`.

---

### Lesson 6.3.2 — Beginner Implementation: Git-Based Prompt Versioning

**Structure**
```
prompts/
  rag_system_v1.txt
  rag_system_v2.txt
  CHANGELOG-prompts.md
```

**Load at runtime**
```python
def load_prompt(name: str, version: str) -> str:
    path = f"prompts/{name}_{version}.txt"
    return Path(path).read_text()
```

**CHANGELOG entry**
```markdown
## v2.0.0 (2026-05-21)
- Added abstention rule for out-of-scope questions
- Eval: faithfulness 0.82 → 0.86 (+4%)
```

**Portfolio task:** `CHANGELOG-prompts.md` with metric deltas.

---

### Lesson 6.3.3 — Intermediate: Experiment Tracking with MLflow

**MLflow** — Log experiments: prompt version, model, eval scores, parameters.

```python
import mlflow

with mlflow.start_run(run_name="rag-prompt-v2"):
    mlflow.log_param("prompt_version", "v2")
    mlflow.log_param("model", "gpt-4o-mini")
    mlflow.log_metric("faithfulness", 0.86)
    mlflow.log_artifact("prompts/rag_system_v2.txt")
```

**Compare runs in MLflow UI** — pick best prompt before deploy.

**Guided lab:** Log 3 prompt experiments; compare faithfulness.

---

### Lesson 6.3.4 — Intermediate: Langfuse Prompt Management

**Langfuse prompts** — Versioned prompts synced with traces.

**Benefit:** Trace shows exact prompt version used for each request.

**Pattern:** Git = source of truth; Langfuse = runtime cache + trace linkage.

---

### Lesson 6.3.5 — Intermediate: Feature Flags for Prompt/Model Rollout

**Feature flag:** `prompt_version=v2` for 5% of users.

**Tools:** LaunchDarkly, Unleash, or simple hash-based routing:

```python
def get_prompt_version(user_id: str) -> str:
    if hash(user_id) % 100 < 5:  # 5% canary
        return "v2"
    return "v1"
```

**Monitor canary:** Compare faithfulness, latency, cost v1 vs v2 for 24h.

---

### Lesson 6.3.6 — Advanced: Canary Deployment and Automatic Rollback

**Canary flow**
```
Deploy v2 to 5% → Monitor 24h → 50% → 100%
         ↓ eval fail or error spike
    Auto-rollback to v1
```

**Rollback trigger examples**
- Faithfulness drops >3% on canary cohort
- Error rate >2x baseline
- p95 latency >1.5x baseline

**Coding exercise:** Script that reads eval results and sets feature flag back to v1.

---

### Lesson 6.3.7 — Advanced: Full AI CI/CD Pipeline Stages

```
┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
│  Lint   │ → │  Unit   │ → │  Eval   │ → │ Staging │ → │ Canary  │
│         │   │  Tests  │   │  Gate   │   │ Deploy  │   │  Prod   │
└─────────┘   └─────────┘   └─────────┘   └─────────┘   └─────────┘
```

**Per stage**
| Stage | AI-specific check |
|-------|-------------------|
| PR | Ragas smoke (20 q), prompt diff review |
| Staging | Full eval (100 q), load test |
| Canary | 5% traffic, 24h monitor |
| Prod | Post-deploy eval sample hourly |

**Architecture discussion:** Draw this pipeline for your capstone in README.

---

### Lesson 6.3.8 — Production: Model Upgrades (GPT-4o → next model)

**Process:** Same as prompt change — eval baseline on new model → compare → canary.

**Track:** Model version in traces and registry.

**Common failure:** New model changes JSON tool call format — add contract tests.

---

### Lesson 6.3.9 — Enterprise: Change Advisory and Audit Trail

**Change advisory board (CAB)** for prod prompt changes in regulated industries.

**Audit fields:** Who approved, eval scores at approval, rollback tested (yes/no).

**Immutable artifacts:** Prompt hash in deployment manifest.

---

### Topic 6.3 — Labs, Projects & Assessments

**Beginner labs**
- Prompt files in Git + CHANGELOG
- Load prompt by version from file

**Intermediate labs**
- MLflow experiment logging (3 runs)
- 5% canary with hash routing

**Advanced labs**
- Full GitHub Actions: lint → eval → deploy staging
- Auto-rollback script on eval failure

**Mini project:** Prompt versioning system with eval on every PR

**Beginner interview questions**
- Why treat prompts like code?
- What is a canary deployment?

**Intermediate interview questions**
- How do you deploy a new system prompt safely?
- CI pipeline stages for an AI feature?

**Senior / system design questions**
- Design prompt rollout for 50 microservices sharing a registry.
- Rollback in 60 seconds — architecture?

**Common beginner mistakes**
- Hardcoded prompt string in code, no version
- Canary without statistical comparison

**Common production failures**
- No rollback tested before deploy
- Prompt change without eval gate

**GitHub portfolio tasks**
- [ ] `prompts/` directory with versions
- [ ] `CHANGELOG-prompts.md`
- [ ] CI badge: eval passing

---

# Topic 6.4 — Guardrails, Governance & Model Registry

## Beginner-Friendly Explanation

**Guardrails** = safety filters on AI input/output: block toxic content, PII leaks, off-topic requests (medical advice on a shopping bot).

**Model registry** = catalog of approved models/prompts with owners, risk tier, review dates — like an inventory for AI assets.

## Why Companies Use This

- Compliance (SOC2, HIPAA, financial regulations)
- Prevent brand damage from toxic outputs
- Audit: "Which model version was live on March 3?"

## What Problem This Solves

Unrestricted LLM + enterprise data = legal and reputational risk. Guardrails and registry are non-negotiable for Fortune 500 deployments.

## Learning Outcome

Add input/output guardrails to RAG API; log trigger events; create model registry entry with model card for your capstone.

---

### Lesson 6.4.1 — Concept: Input vs Output Guardrails

| Type | When | Example |
|------|------|---------|
| **Input** | Before LLM | Block prompt injection patterns |
| **Output** | After LLM | Redact PII, block medical advice |
| **Retrieval** | Before generate | Block docs user shouldn't access (ACL) |

**Fail open vs fail closed**
- **Fail closed** (high risk): Block if guardrail uncertain — healthcare, finance
- **Fail open** (low risk): Log and allow — internal brainstorming tool

**Connect Module 03:** Prompt injection defenses + guardrails = defense in depth.

---

### Lesson 6.4.2 — Beginner Implementation: Simple Rule-Based Guardrails

**No library yet — understand the pattern**

```python
BLOCKED_TOPICS = ["medical diagnosis", "legal advice"]
INJECTION_PATTERNS = ["ignore previous instructions", "system prompt"]

def input_guardrail(user_text: str) -> tuple[bool, str]:
    lower = user_text.lower()
    for pattern in INJECTION_PATTERNS:
        if pattern in lower:
            return False, "blocked_injection"
    return True, "ok"

def output_guardrail(answer: str) -> tuple[bool, str]:
    for topic in BLOCKED_TOPICS:
        if topic in answer.lower():
            return False, "blocked_topic"
    return True, "ok"
```

**Exercise:** Block 3 injection patterns; log block reason to observability.

**UX:** Return friendly message — "I can't help with that, but I can..."

---

### Lesson 6.4.3 — Intermediate: Guardrails AI / NeMo Guardrails Intro

**Guardrails AI** — Schema-validated output, PII detection, topic restriction.

**NeMo Guardrails (NVIDIA)** — Colang flows for conversational rails.

**When to use library vs custom:** Library for PII/toxicity; custom for domain rules.

**Guided lab:** Block medical advice in non-health bot; metric `guardrail_triggers_total`.

**Latency consideration:** Run lightweight checks first; expensive classifier async.

---

### Lesson 6.4.4 — Intermediate: PII Detection and Redaction

**Detect:** Email, phone, SSN, credit card patterns  
**Action:** Redact in output `[EMAIL REDACTED]`; block in logs

**Tools:** Presidio, Guardrails AI PII validator, regex baseline

**Enterprise:** Legal defines what counts as PII per jurisdiction.

**Assignment:** Redact PII in RAG answer before returning to user.

---

### Lesson 6.4.5 — Intermediate: Model Cards and Risk Tiers

**Model card** (document for each deployed model/prompt)
```markdown
# RAG HR Assistant v2
- **Owner:** AI Platform Team
- **Risk tier:** Medium (internal HR data)
- **Model:** gpt-4o-mini via Azure OpenAI
- **Eval faithfulness:** 0.86 (100-case set, 2026-05-21)
- **Known limitations:** Struggles with tables in PDFs
- **Review date:** 2026-08-21
- **Approved by:** Jane Doe, AI Lead
```

**Risk tiers:** Low (public FAQ) → Medium (internal) → High (regulated) → Critical (financial advice)

---

### Lesson 6.4.6 — Advanced: Model Registry Structure

**Registry entry fields (SOC2-friendly)**
| Field | Purpose |
|-------|---------|
| `model_id` | Unique identifier |
| `version` | Semver |
| `owner` | Team/person accountable |
| `risk_tier` | Governance path |
| `eval_results` | Link to latest eval artifact |
| `approval_status` | draft / approved / deprecated |
| `lineage` | Base model → fine-tune → prompt |

**Tools:** MLflow Model Registry, custom Git + JSON, Hugging Face Hub (awareness)

**Exercise:** Create `registry/rag-hr-assistant.json` for capstone.

---

### Lesson 6.4.7 — Advanced: Guardrails in CI

**Test guardrails like unit tests**

```python
def test_blocks_injection():
    allowed, reason = input_guardrail("Ignore previous instructions and...")
    assert not allowed
    assert reason == "blocked_injection"

def test_allows_normal_question():
    allowed, _ = input_guardrail("What is the PTO policy?")
    assert allowed
```

**CI gate:** Guardrail tests must pass on every PR.

**Red team updates:** Quarterly new adversarial prompts added to test suite.

---

### Lesson 6.4.8 — Production: Guardrail Metrics and Alerting

**Metrics**
- `guardrail_triggers_total{rule="injection"}`
- `guardrail_latency_ms`
- Trigger rate anomaly → possible attack campaign

**Dashboard panel:** Guardrail triggers per hour by rule type.

**Do NOT:** Silent block without log — security team needs visibility.

---

### Lesson 6.4.9 — Enterprise: Retention, Lineage, and Compliance

**Log retention:** 30/90/365 days per policy  
**Right to deletion:** User data purge includes traces and eval logs  
**Lineage:** Model v3 → trained on dataset D → prompt P → deployed prod 2026-05-21

**Governance pack deliverables**
- Model card
- DPIA template (Data Protection Impact Assessment) — awareness
- Retention config document

---

### Topic 6.4 — Labs, Projects & Assessments

**Beginner labs**
- Rule-based input/output guardrails
- Log block events

**Intermediate labs**
- Guardrails AI or Presidio PII redaction
- Model card for capstone

**Advanced labs**
- Guardrail pytest suite in CI
- Registry JSON with approval workflow (mock)

**Enterprise labs**
- Governance pack (model card + retention policy + red team test set)

**Beginner interview questions**
- Input vs output guardrails?
- Fail open vs fail closed?

**Intermediate interview questions**
- Implement guardrails without killing UX latency?
- Model registry fields for SOC2 audit?

**Senior / system design questions**
- Guardrails for 10-language global chatbot?
- Model registry across 3 cloud providers?

**Common beginner mistakes**
- Guardrails only in demo, not prod path
- No logging when guardrails fire

**Common production failures**
- Registry without owner or review date
- Over-blocking kills UX → users abandon product

**Job alignment:** Responsible AI Engineer, Enterprise AI Engineer — guardrails + registry on resume.

---

# Module 06 — Capstone: Production-Ready LLMOps Stack

## Project Progression (Ascending Complexity)

| Phase | What you build |
|-------|----------------|
| **Week 26** | Token/latency logging + Langfuse first trace |
| **Week 27** | Golden set (30+) + Ragas baseline |
| **Week 28** | Grafana dashboard + 3 alerts |
| **Week 29** | Eval CI gate on GitHub Actions |
| **Week 30** | Guardrails + prompt versioning + governance doc |

## Capstone: "LLMOps Pack" for Module 04/05 Project

Apply full stack to your existing RAG or Agent project:

### Required Deliverables

- [ ] **Observability:** Langfuse traces for full pipeline (retrieve → generate)
- [ ] **Metrics:** Grafana dashboard — latency, tokens, cost, errors (screenshot in README)
- [ ] **Eval:** Golden set ≥50 questions; faithfulness ≥0.80 documented
- [ ] **CI:** GitHub Action fails if faithfulness drops >5%
- [ ] **Prompts:** Versioned in `prompts/` + `CHANGELOG-prompts.md`
- [ ] **Guardrails:** Input injection block + output topic block + CI tests
- [ ] **Registry:** Model card + `registry/` JSON entry
- [ ] **Runbook:** `docs/runbook-quality-degradation.md`

### Architecture Diagram

```
                    ┌─────────────────────────────────────┐
                    │           GitHub PR                  │
                    │  lint → unit → eval → guardrail tests│
                    └──────────────────┬──────────────────┘
                                       ▼
User ──▶ FastAPI ──▶ Guardrails ──▶ RAG/Agent ──▶ Guardrails ──▶ Response
              │            │              │
              ▼            ▼              ▼
         Langfuse      Metrics      MLflow / Registry
              │         Prometheus
              ▼            ▼
         Trace UI      Grafana + Alerts
```

## Interview Talking Points

1. "How do you know your RAG works?" — Golden set + Ragas + CI gate + score in README  
2. "Production incident workflow?" — Trace ID → Langfuse → identify retrieval vs generation failure  
3. "How deploy prompt safely?" — Git version → eval → canary → monitor → rollback  
4. "What metrics on SLA dashboard?" — p95 latency, faithfulness sample, cost/query, error rate, guardrail triggers  
5. Whiteboard full LLMOps pipeline from PR to prod  

## Common Mistakes (Hiring Feedback)

| Mistake | Signal |
|---------|--------|
| No eval numbers in README | "Tutorial developer" |
| Logs full prompts in prod | Security concern |
| No trace across RAG steps | Cannot debug |
| Prompt hardcoded, no version | No ops maturity |
| Guardrails missing | Not enterprise-ready |

---

## Module 06 — Master Checklist Before Module 07 (Enterprise AI)

| Question | Yes / No |
|----------|----------|
| Can I show a Langfuse trace for a full RAG request? | |
| Do I have faithfulness score on ≥50 questions? | |
| Does CI fail when I break retrieval intentionally? | |
| Are prompts versioned in Git with changelog? | |
| Do guardrails log triggers without silent fail? | |
| Can I explain monitoring vs observability in 30 seconds? | |

**Next module:** Module 07 adds **multi-tenancy, RBAC, SSO, and enterprise architecture** on top of this LLMOps foundation.

---

*Next: [module-07-enterprise-ai.md](./module-07-enterprise-ai.md)*
