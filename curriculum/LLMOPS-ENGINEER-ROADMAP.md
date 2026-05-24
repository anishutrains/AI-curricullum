# Complete LLMOps Engineer Roadmap (2026–2027)
### Zero-to-Production · USA Job Market · Beginner with No IT Background → Employable LLMOps Engineer

---

> **How to use this document:** This is the **definitive LLMOps specialization track**. It teaches from absolute zero and progresses through 16 phases (~52 weeks). Detailed module files (`module-01` … `module-12`) provide extended labs — this roadmap is the **master narrative + lesson spine** for LLMOps careers.

---

## Who This Curriculum Is For

| Student profile | Why this track fits |
|-----------------|---------------------|
| Complete beginner (no IT) | Phase 0 starts with "what is a computer" |
| Career switcher (support, ops, non-tech) | Ops mindset → LLMOps is natural transition |
| DevOps/cloud engineer | Phases 11–14 accelerate; review Phases 3–9 for AI-specific ops |
| Fresh graduate | Portfolio + interview pack in Phase 16 |

## Final Outcome

After completing this roadmap, you can:

- Clear **LLMOps / AI Platform / AI Reliability** interviews (US remote/hybrid, 2026–2027)
- Deploy, monitor, evaluate, and rollback production LLM applications
- Build AI CI/CD pipelines with eval gates and canary prompt releases
- Operate enterprise AI (multi-tenant, governance, FinOps, audit trails)
- Troubleshoot silent AI failures (hallucination, retrieval miss, cost spike)

## Target Job Roles & Salary Bands (USA, 2026)

| Role | Typical base | Core proof in portfolio |
|------|--------------|---------------------------|
| **LLMOps Engineer** | $155K–$220K | Eval CI + Langfuse + prompt registry |
| **AI Platform Engineer** | $165K–$235K | Terraform + multi-tenant + observability stack |
| **AI Reliability Engineer** | $160K–$225K | SLOs, runbooks, incident drills |
| **RAG Operations Engineer** | $145K–$195K | RAG eval + retrieval monitoring |
| **AI Infrastructure Engineer** | $170K–$250K | K8s/vLLM + cloud AI deploy |
| **Production AI Engineer** | $150K–$210K | End-to-end deploy + metrics in README |

---

## 52-Week Progression Map

| Weeks | Phase | Module | Theme |
|-------|-------|--------|-------|
| 1–2 | 0 | M0 | Computer, internet, terminal |
| 3–6 | 1 | M1 | Python from zero |
| 7–8 | 2 | M2 | APIs, Git, FastAPI intro |
| 9–10 | 3 | M3 | AI, GenAI, LLM fundamentals |
| 11–12 | 4 | M4 | Prompt engineering |
| 13–16 | 5 | M5 | RAG + vector DBs |
| 17–19 | 6 | M6 | Agentic AI |
| 20–21 | 7 | M7 | Introduction to LLMOps |
| 22–25 | 8 | M8 | Observability & monitoring |
| 26–29 | 9 | M9 | Evaluation systems |
| 30–32 | 10 | M10 | Prompt versioning & AI CI/CD |
| 33–35 | 11 | M11 | Docker, deploy, rollback |
| 36–39 | 12 | M12 | Cloud + Kubernetes |
| 40–42 | 13 | M13 | Enterprise + security + governance |
| 43–45 | 14 | M14 | Production reliability & SRE |
| 46–49 | 15 | M15 | Enterprise capstones |
| 50–52 | 16 | M16 | Interview & job launch |

**Cross-reference:** Phases 1–6 align with `module-01` … `module-05`. Phases 7–14 deepen `module-06` … `module-11`. Phases 15–16 align with `module-12`.

---

# PHASE 0 — COMPUTER & TECHNICAL FOUNDATIONS

# Module 0 — Digital & Technical Foundations
### Weeks 1–2 · Before You Touch AI

## Why This Module Matters

**Why companies need this:** Every LLMOps engineer uses terminals, Git, logs, and cloud consoles daily.  
**Why AI engineers need this:** AI failures appear in logs and traces — if you fear the terminal, you cannot operate production AI.  
**Production relevance:** Incident response at 2 AM is SSH, kubectl, and grep — not Jupyter notebooks.

## Why We Are Learning This NOW

You have **zero assumptions**. This module builds confidence with computers so Phase 1 (Python) does not feel alien.  
**Prepares for:** Module 1 (Python), Module 2 (Git/APIs), Module 11 (Docker CLI), Module 12 (cloud consoles).

## Job Roles This Module Helps With

All LLMOps-adjacent roles — this is universal infrastructure literacy.

## Beginner Skills Students Will Learn

- Explain hardware vs software; client vs server
- Navigate folders in terminal (Windows PowerShell + Linux basics)
- Install VS Code, Python, Git, Docker Desktop
- Open a URL and describe what happens (DNS → HTTP → server)

## Intermediate Skills Students Will Learn

- Environment variables; PATH; `.env` files (concept only)
- Read JSON in a browser devtools Network tab

## Advanced Skills Students Will Learn

- *(Deferred to later phases)*

## Production Enterprise Skills Students Will Learn

- *(Deferred)* — but you will learn why ops teams use Linux in production

---

# Topic 0.1 — Understanding Computers & the Internet

## Beginner-Friendly Explanation

A **computer** follows instructions (software) using chips (hardware).  
The **internet** connects computers so your laptop (client) can ask another computer (server) for a web page.

**Like a restaurant:** You (client) order food. Kitchen (server) prepares it. Menu (API/website) lists what you can order.

## Why This Topic Matters

LLMOps engineers deploy apps **on servers** in **cloud data centers**. You must know what a server is.

## What Problem This Solves

Fear and confusion when tutorials say "run this in terminal" or "deploy to EC2."

## Learning Outcome

Draw a diagram: Browser → Internet → Server → Database. Install dev tools successfully.

---

### Lesson 0.1.1 — Concept: What Is a Computer?

**Hardware:** CPU (brain), RAM (short-term memory), disk (long-term storage)  
**Software:** Operating system (Windows/Linux/Mac), applications (VS Code, Python)  
**Exercise:** Identify CPU/RAM on your Task Manager / Activity Monitor.

### Lesson 0.1.2 — Concept: What Is the Internet?

**Server** — computer that serves data 24/7  
**Client** — your browser or app requesting data  
**HTTP** — language of web requests (GET = fetch, POST = send data)  
**Exercise:** Open DevTools → Network → reload page → see HTTP requests.

### Lesson 0.1.3 — Beginner: Operating Systems & File Paths

**Paths:** `C:\Users\you\project` (Windows) vs `/home/you/project` (Linux)  
**Folders and files** — code lives in organized folders  
**Exercise:** Create `AI-ENGINEER-COURSE/my-first-folder` in File Explorer and terminal.

### Lesson 0.1.4 — Guided Practice: Terminal Basics

| Command (concept) | What it does |
|-------------------|--------------|
| `cd folder` | Change directory |
| `ls` / `dir` | List files |
| `mkdir name` | Create folder |
| `python --version` | Check Python installed |

**Hands-on lab 0.1:** Install VS Code, Python 3.11+, Git, Docker Desktop. Screenshot versions in `labs/phase-0-setup.md`.

### Lesson 0.1.5 — Mini Project: "My Dev Environment Doc"

One-page README: tools installed, versions, hello-world terminal commands that worked.

### Lesson 0.1.6 — Production Consideration

Production servers are **Linux**. Learn basic Linux commands even on Windows (WSL recommended).

---

# PHASE 1 — PYTHON PROGRAMMING FOUNDATIONS

# Module 1 — Python for LLMOps Engineers
### Weeks 3–6 · Your Primary Language for AI Operations

## Why This Module Matters

**Python** runs: FastAPI backends, Ragas eval scripts, Terraform-adjacent tooling, Langfuse hooks, data pipelines.  
**90%+ of LLMOps job posts** list Python. No shortcuts.

## Why We Are Learning This NOW

Phase 0 gave you terminal comfort. Python is how you **automate** everything in LLMOps.  
**Prepares for:** APIs (Phase 2), LLM SDKs (Phase 3+), eval pipelines (Phase 9).

## Job Roles This Module Helps With

LLMOps Engineer · AI Platform Engineer · RAG Operations Engineer · Production AI Engineer

## Beginner Skills Students Will Learn

- Variables, loops, functions, lists, dictionaries
- Read/write files and JSON
- `pip`, virtual environments
- Basic error handling (`try/except`)

## Intermediate Skills Students Will Learn

- HTTP requests with `httpx`/`requests`
- Async/await basics
- OOP basics (classes for config objects)
- Environment variables with `python-dotenv`

## Advanced Skills Students Will Learn

- Async FastAPI endpoints
- Pydantic models for API validation
- Structured logging

## Production Enterprise Skills Students Will Learn

- Type hints, config modules, 12-factor app patterns for AI services

**Extended content:** → [module-01-python-fastapi-foundations.md](./module-01-python-fastapi-foundations.md)

---

# Topic 1.1 — Python Basics (From Zero)

## Beginner-Friendly Explanation

**Programming** = writing instructions the computer follows exactly.  
**Python** = language that reads almost like English — best first language for AI.

## Learning Outcome

Build calculator CLI + JSON file reader + simple rule-based chatbot.

---

### Lesson 1.1.1 — Concept: What Is Programming?

Instructions → computer executes → output. No magic.  
**Analogy:** Recipe steps for a robot chef.

### Lesson 1.1.2 — Guided Coding: First Program

```python
print("Hello, LLMOps future!")
name = input("What is your name? ")
print(f"Welcome, {name}")
```

**Practice:** Change message; run from VS Code terminal.

### Lesson 1.1.3 — Variables and Data Types

```python
age = 25                    # int
price = 9.99                # float
model = "gpt-4o-mini"       # str
is_prod = False             # bool
tokens = [100, 200, 350]    # list
config = {"top_k": 5}       # dict
```

**Exercise:** Store fake LLM request metadata in a dict.

### Lesson 1.1.4 — Conditionals and Loops

```python
for token_count in tokens:
    if token_count > 300:
        print("High usage alert")
```

**Exercise:** Loop through 10 mock API costs; sum total.

### Lesson 1.1.5 — Functions

```python
def estimate_cost(tokens: int, price_per_1k: float) -> float:
    return (tokens / 1000) * price_per_1k
```

**Mini project:** Cost calculator for LLM calls — foreshadows FinOps.

### Lesson 1.1.6 — Error Handling

```python
try:
    data = json.loads(raw)
except json.JSONDecodeError:
    print("Invalid JSON — log and alert")
```

**Production:** LLMOps scripts must not crash silently on bad inputs.

---

# Topic 1.2 — Intermediate Python for APIs & Automation

### Lesson 1.2.1 — Files and JSON

Read `golden_set.jsonl` line by line — pattern used in every eval pipeline.

### Lesson 1.2.2 — Virtual Environments

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install httpx fastapi
```

**Why:** Reproducible deploys — same packages in dev and CI.

### Lesson 1.2.3 — HTTP Requests

```python
import httpx
r = httpx.get("https://api.example.com/health")
print(r.status_code, r.json())
```

**Lab 1.5:** Weather or public API client.

### Lesson 1.2.4 — Async Basics (Concept + optional)

`async def` + `await` — FastAPI and parallel eval jobs use async.  
**Depth:** → module-01 Topic 1.2.

---

# PHASE 2 — SOFTWARE ENGINEERING FOUNDATIONS

# Module 2 — APIs, Git & Backend Basics
### Weeks 7–8

## Why This Module Matters

LLMOps engineers **deploy APIs**, **version prompts in Git**, and **run CI pipelines**. You cannot operate AI without software engineering hygiene.

## Why We Are Learning This NOW

Python alone is not deployable. APIs expose LLMs; Git versions prompts; CI runs eval gates.  
**Prepares for:** LLM APIs (Phase 3), RAG services (Phase 5), AI CI/CD (Phase 10).

## Job Roles

LLMOps Engineer · AI Platform Engineer · Production AI Engineer

**Extended content:** → [module-01-python-fastapi-foundations.md](./module-01-python-fastapi-foundations.md) (Topics 1.3–1.4)

---

# Topic 2.1 — Understanding APIs

## Beginner-Friendly Explanation

**API** = menu for software. Your app orders `POST /chat` with JSON; server returns JSON answer.

## Learning Outcome

Call public API with Python; build `GET /health` and `POST /v1/chat` with FastAPI.

---

### Lesson 2.1.1 — REST: GET vs POST vs JSON

### Lesson 2.1.2 — Guided Coding: FastAPI Hello World

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```

**Lab 2.2:** Run with `uvicorn`; hit `/docs` Swagger UI.

### Lesson 2.1.3 — Production: API Keys and Auth (Intro)

Never commit secrets — use `.env` locally, secret manager in prod.

---

# Topic 2.2 — Git & GitHub

### Lesson 2.2.1 — Concept: Version Control

Track every change; rollback bad prompt; review in PR.

### Lesson 2.2.2 — Guided Practice

```bash
git init
git add .
git commit -m "Add RAG API v1"
git push origin main
```

**Lab 2.3:** Push Phase 1 calculator to GitHub — public portfolio starts here.

**Portfolio task:** Pin repo; add README with setup steps.

---

# PHASE 3 — AI & LLM FUNDAMENTALS

# Module 3 — Introduction to AI, Generative AI & LLMs
### Weeks 9–10

## Why This Module Matters

You cannot **operate** what you do not **understand**. LLMOps is operations for LLM applications — know what an LLM is first.

## Why We Are Learning This NOW

Before OpenAI SDK calls and RAG, build mental models: tokens, context, hallucination.  
**Prepares for:** Prompt engineering (Phase 4), RAG (Phase 5), eval metrics (Phase 9).

**Extended content:** → [module-02-llm-apis-foundations.md](./module-02-llm-apis-foundations.md)

---

# Topic 3.1 — What Is AI? (Absolute Beginner)

## Beginner-Friendly Explanation

Imagine a **very smart helper** inside a computer that can read, write, and answer questions — but only in ways it was designed or trained for. That is **Artificial Intelligence (AI)** in simple terms.

**Not magic:** AI follows math and patterns learned from huge amounts of data. It can be wrong. It does not "think" like a human.

## Why This Topic Matters

Every LLMOps engineer gets asked to explain AI to managers, legal, and customers. If you cannot explain it simply, you cannot lead production rollouts.

## What Problem This Solves

Fear and hype. You replace "AI is magic" with "AI is software we operate with metrics and guardrails."

## Learning Outcome

Explain AI vs ML vs deep learning vs GenAI to a non-technical recruiter in 60 seconds.

---

### Lesson 3.1.1 — Concept: What Is Artificial Intelligence?

**Definition (beginner):** Software that performs tasks that *look like* human intelligence — understanding language, recognizing patterns, making predictions.

**Real-world AI you already use:**
- Netflix recommending shows
- Gmail spam filter
- Google Maps ETA prediction
- Siri / Alexa (limited)
- ChatGPT (generative AI)

**Exercise:** List 5 AI tools you used this week. Label each as "recommendation," "classification," or "generation."

**Production consideration:** Enterprise AI is almost always **narrow AI** — one product feature, one domain — not science-fiction general AI.

---

### Lesson 3.1.2 — Concept: Types of AI (Narrow vs General)

| Type | Meaning | Exists today? |
|------|---------|---------------|
| **Narrow AI** | Good at one task (chat, search, fraud detect) | Yes — all production AI |
| **General AI (AGI)** | Human-level at any intellectual task | Research only — not in job reqs |

**Interview answer:** "We build narrow AI systems with eval and guardrails; AGI is out of scope."

---

### Lesson 3.1.3 — Concept: AI vs Machine Learning vs Deep Learning

**Machine Learning (ML):** AI that **learns from data** instead of explicit if/else rules.  
Example: Instead of writing 1000 spam rules, show 1M emails labeled spam/not spam — model learns patterns.

**Deep Learning:** ML using **neural networks** (many layers) — powers image recognition and **LLMs**.

**Relationship:**
```
Artificial Intelligence
    └── Machine Learning
            └── Deep Learning
                    └── Large Language Models (LLMs)
```

**Hands-on analogy:**  
- **Rules:** "If subject contains WINNER → spam"  
- **ML:** Model learns spam patterns from examples  
- **LLM:** Model learns language from internet-scale text

---

### Lesson 3.1.4 — Concept: What Is Generative AI?

**Generative AI** = AI that **creates new content** — text, code, images, audio.

**Examples:**
- ChatGPT writes an email
- Copilot writes code
- Midjourney creates images
- Your course RAG bot generates answers from company docs

**Difference from traditional AI:**  
- **Traditional:** "Is this email spam?" (yes/no)  
- **Generative:** "Write a reply to this customer." (creates text)

**LLMOps focus:** Generative apps are **non-deterministic**, **costly per request**, and **can hallucinate** — needs ops discipline.

---

### Lesson 3.1.5 — Concept: How ChatGPT Works (High Level)

1. You type a **prompt** (question)
2. Text is split into **tokens**
3. **LLM** predicts next tokens repeatedly until answer complete
4. Response shown to you

**You do not need to train ChatGPT for LLMOps.** You **call** it via API and operate the application around it (RAG, agents, monitoring).

**Guided practice:** Open your LLM provider playground; submit same prompt 3 times; notice output variation — this is why **eval** matters.

---

# Topic 3.2 — Understanding LLMs (Deep Beginner → Intermediate)

## Beginner-Friendly Explanation

**LLM = Large Language Model** — a giant autocomplete that read enormous amounts of text and learned patterns of language, facts (with limits), and reasoning (imperfect).

**Like:** A librarian who read millions of books but sometimes confidently cites books that do not exist.

## Learning Outcome

Use tokens, context windows, and model names correctly in code and interviews.

---

### Lesson 3.2.1 — Concept: What Is an LLM?

**Large** = billions of parameters (internal knobs)  
**Language** = text in/out  
**Model** = file + math that maps input tokens → output tokens

**Closed-source:** OpenAI GPT, Anthropic Claude, Google Gemini (API access)  
**Open-source:** Meta Llama, Mistral (download weights, self-host)

**LLMOps implication:** Closed-source = monitor API latency, cost, rate limits. Open-source = monitor GPU, vLLM throughput, model server health.

---

### Lesson 3.2.2 — Concept: Tokens Explained

**Token** ≈ piece of a word. English averages ~4 characters per token.

```text
"Hello world"     → maybe 2 tokens
"LLMOps"          → maybe 2 tokens: LL + Mops
```

**Why tokens matter for LLMOps:**
- Billed per token
- Context window measured in tokens
- Logs should record `tokens_in`, `tokens_out`

**Exercise:** Use OpenAI tokenizer or `tiktoken` to count tokens in a sample RAG prompt. Estimate cost at $0.15/1M input tokens.

---

### Lesson 3.2.3 — Concept: Training vs Inference

| Phase | Who does it | Cost | LLMOps engineer role |
|-------|-------------|------|----------------------|
| **Pre-training** | OpenAI, Anthropic, Meta | $100M+ | None — use API |
| **Fine-tuning** | Some enterprises | $1K–$100K | Optional — monitor eval |
| **Inference** | **You, every user query** | Per token | **Core LLMOps focus** |

**Inference** = production — latency, scaling, caching, routing, fallbacks.

---

### Lesson 3.2.4 — Concept: Context Windows

**Context window** = maximum tokens model can process in one request (input + output).

| Model class | Typical window |
|-------------|----------------|
| Small/fast | 8K–128K |
| Long-context | 200K–1M+ |

**RAG interaction:** If retrieved docs + question exceed window → truncation → bad answers.  
**LLMOps:** Monitor `context_tokens_used` and truncation events.

---

### Lesson 3.2.5 — Concept: GPT vs Claude vs Gemini vs Llama vs Mistral

| Model | Strengths | Enterprise note |
|-------|-----------|-----------------|
| **GPT-4o / o-series** | General, tools, vision | OpenAI API; Azure OpenAI for enterprise |
| **Claude 3.5+** | Long docs, careful tone | Anthropic API; Bedrock |
| **Gemini** | GCP integration, multimodal | Vertex AI |
| **Llama 3+** | Open weights, self-host | vLLM on K8s — cost at scale |
| **Mistral** | Efficient open models | EU sovereignty use cases |

**Production pattern:** **Model router** — cheap model for easy queries, expensive for hard ones.

---

### Lesson 3.2.6 — Concept: Open Source vs Closed Source (Operations View)

**Closed API pros:** No GPU ops, fast start, best models  
**Closed API cons:** Vendor lock-in, data policy, rate limits, cost at scale

**Open-source pros:** Data stays inside VPC, predictable cost at high volume  
**Open-source cons:** GPU ops, model updates, security patching

**Architecture decision record (ADR)** required for enterprise — Phase 14.

---

### Lesson 3.2.7 — Concept: Multimodal AI (Awareness)

**Multimodal** = text + images + audio in one model (GPT-4o, Gemini).  
**LLMOps adds:** Different latency profile, larger payloads, content moderation for uploads.

---

# Topic 3.3 — Why LLM Applications Fail & Why LLMOps Exists

## Beginner-Friendly Explanation

Building a chatbot demo takes a weekend. **Running it safely for 10,000 employees takes engineering.**

**LLMOps exists** because LLM apps fail in **new ways** normal software monitoring does not catch.

---

### Lesson 3.3.1 — Concept: Hallucinations

**Hallucination** = model states false information confidently.

**Causes:** No grounding data, bad retrieval, prompt ambiguity, model limitation  
**Mitigations:** RAG, citations, abstention, eval — Phases 5, 8, 9

**Real incident story (pattern):** HR bot cites non-existent policy section → employee makes decision → legal exposure.

---

### Lesson 3.3.2 — Concept: Latency & Timeouts

Users expect 2–5 seconds. Cold starts, long context, slow retrieval → 30s waits → abandonment.

**LLMOps:** p50/p95 latency metrics, streaming, caching, async queues for long agents.

---

### Lesson 3.3.3 — Concept: Cost Explosions

**Denial of Wallet:** Attacker or bug spams API → massive bill.  
**Viral feature:** Usage 100× overnight — no budget alert.

**LLMOps:** Per-user quotas, daily budgets, alerts at 150% of 7-day average spend.

---

### Lesson 3.3.4 — Concept: Inconsistent Outputs

Same question, different answers → breaks trust and automated downstream systems.

**Mitigations:** Lower temperature for factual tasks, eval suites, structured outputs.

---

### Lesson 3.3.5 — Concept: Scaling Problems

Demo: 1 user, 10 PDFs. Production: 5000 users, 500K docs, 100 QPS.

**Breaks:** Vector DB slow, embed queue backlog, API rate limits  
**LLMOps + Phase 12:** Autoscaling, index partitioning, batch embed jobs.

---

### Lesson 3.3.6 — Concept: Why LLMOps Exists (Summary)

**LLMOps = the discipline that makes LLM products:**
- **Observable** (traces, metrics)
- **Measurable** (eval, golden sets)
- **Deployable** (CI/CD, rollback)
- **Affordable** (FinOps)
- **Safe** (guardrails, audit)
- **Compliant** (retention, deletion)

**Mini project:** Write `docs/why-llmops.md` — one page explaining to a beginner why your future job exists. **Portfolio:** Shows product thinking.

---

### Lesson 3.3.7 — Guided Lab: First Monitored LLM Call

```python
import time, httpx, os

start = time.perf_counter()
# call your LLM API here
latency_ms = (time.perf_counter() - start) * 1000
print({"latency_ms": latency_ms, "tokens_in": ..., "tokens_out": ...})
```

Save results to CSV — primitive observability you will replace with Langfuse in Phase 8.

**Compare Lab 3.3:** GPT vs Claude on same 5 prompts — log latency and quality subjectively; foreshadow promptfoo.

---

# PHASE 4 — PROMPT ENGINEERING

# Module 4 — Prompt Engineering for Production
### Weeks 11–12

## Why This Module Matters

Prompts are **production configuration**. LLMOps owns versioning, testing, and rollback of prompts.

## Why We Are Learning This NOW

Before RAG prompts and system prompts in CI, learn structure and security basics.  
**Prepares for:** RAG templates (Phase 5), prompt registry (Phase 10).

**Extended content:** → [module-03-prompt-engineering-dspy.md](./module-03-prompt-engineering-dspy.md)

---

# Topic 4.1 — Prompt Fundamentals

### Lesson 4.1.1 — System vs User vs Assistant Messages

### Lesson 4.1.2 — Prompt Templates with Variables

```python
RAG_PROMPT = """Answer using only context below.
Context: {context}
Question: {question}
If unsure, say "I don't know."
"""
```

### Lesson 4.1.3 — Production: Prompt Injection Awareness

User tries to override system instructions — defense in depth (Module 13).

**Labs:** AI email writer; resume optimizer with structured output.

---

# PHASE 5 — RAG SYSTEMS & VECTOR DATABASES

# Module 5 — RAG & Vector Databases for Operations
### Weeks 13–16

## Why This Module Matters

**80%+ enterprise GenAI** is RAG. LLMOps for RAG = retrieval monitoring, faithfulness eval, re-index pipelines.

## Why We Are Learning This NOW

You need a working RAG app to **instrument, evaluate, and deploy** in later phases.  
**Prepares for:** Observability (Phase 8), Ragas eval (Phase 9), capstone (Phase 15).

**Extended content:** → [module-04-rag-systems.md](./module-04-rag-systems.md)

---

# Topic 5.1 — RAG Foundations

### Lesson 5.1.1 — Why RAG Exists (Hallucination → Grounding)

### Lesson 5.1.2 — RAG Pipeline Diagram

Ingest → Chunk → Embed → Store → Retrieve → Generate → Cite

### Lesson 5.1.3 — Beginner Lab: PDF Chatbot

**Deliverable:** `POST /v1/rag/query` returning answer + sources.

---

# Topic 5.2 — Embeddings & Vector Databases

### Lesson 5.2.1 — Embeddings as Semantic Coordinates

### Lesson 5.2.2 — Vector DB Ladder

JSON file (toy) → **pgvector** (Postgres) → **Pinecone** (managed)

### Lesson 5.2.3 — Chunking Strategy Affects Ops

Re-index jobs, embedding cache, version indexes — LLMOps concerns.

**Lab 5.2:** Company knowledge assistant with pgvector or Pinecone.

---

# PHASE 6 — AGENTIC AI (FOR LLMOPS CONTEXT)

# Module 6 — AI Agents & Tool Operations
### Weeks 17–19

## Why This Module Matters

Agents multiply **trace spans**, **tool failure modes**, and **security risks**. LLMOps must trace every tool call and eval agent success rate.

## Why We Are Learning This NOW

Before advanced observability, see multi-step workflows that need tracing.  
**Prepares for:** Agent traces in Langfuse (Phase 8), tool audit logs (Phase 13).

**Extended content:** → [module-05-agentic-ai.md](./module-05-agentic-ai.md)

---

# Topic 6.1 — Agents vs Chatbots

### Lesson 6.1.1 — Tool Calling Loop

### Lesson 6.1.2 — RAG as Agent Tool

### Lesson 6.1.3 — LangGraph + HITL (Intro)

**Labs:** Support triage agent with max steps + audit log.

---

# PHASE 7 — INTRODUCTION TO LLMOPS

# Module 7 — What Is LLMOps & the Production AI Lifecycle
### Weeks 20–21 · The Career Specialization Begins

## Why This Module Matters

**LLMOps** = discipline of running LLM applications reliably in production: deploy, monitor, evaluate, improve, govern.  
Companies hire LLMOps engineers because **building a demo ≠ operating a product**.

## Why We Are Learning This NOW

You have built RAG and agents. Now learn why those break in prod and what roles exist to fix them.  
**Prepares for:** Phases 8–14 (core LLMOps stack).

## Job Roles This Module Helps With

**LLMOps Engineer** (primary) · AI Reliability Engineer · AI Operations Engineer · Production AI Engineer

## Beginner Skills Students Will Learn

- Define LLMOps, MLOps, DevOps in plain English
- Name stages of AI app lifecycle
- List what breaks in production AI

## Intermediate Skills Students Will Learn

- Map tools to lifecycle stages (Langfuse, Ragas, GitHub Actions)
- Write LLMOps job description match doc for your portfolio

## Advanced Skills Students Will Learn

- Design LLMOps reference architecture for RAG SaaS

## Production Enterprise Skills Students Will Learn

- Explain LLMOps to CFO (cost) and legal (compliance) in one slide

**Extended content:** → [module-06-llmops.md](./module-06-llmops.md) (full depth)

---

# Topic 7.1 — LLMOps Foundations

## Beginner-Friendly Explanation

**MLOps** = operating traditional ML (training pipelines, model registries).  
**LLMOps** = operating **LLM applications** where the "model" changes via **prompts**, **RAG data**, and **API models** — not just weight files.

**Analogy:** MLOps is maintaining a factory that builds cars. LLMOps is maintaining Uber — live traffic, drivers, pricing, customer complaints — mostly runtime behavior.

## Why This Topic Matters

2026 US job posts increasingly say **"LLMOps"** or **"GenAI platform"** explicitly — not generic "ML engineer."

## What Problem This Solves

| Without LLMOps | Result |
|--------------|--------|
| No eval | Quality rots silently |
| No tracing | Cannot debug wrong answers |
| No versioning | Cannot rollback bad prompt |
| No cost tracking | Finance emergency |

## Learning Outcome

Whiteboard LLMOps lifecycle for your RAG project; identify gaps in your current repo.

---

### Lesson 7.1.1 — Concept: What Is LLMOps?

**Definition:** Engineering practices for **production LLM systems** — observability, evaluation, deployment, security, governance, cost management.

**You are NOT:** Training GPT from scratch.  
**You ARE:** Making RAG/agents **measurable, deployable, safe, and affordable**.

### Lesson 7.1.2 — Concept: MLOps vs LLMOps vs DevOps

| Discipline | Focus |
|------------|-------|
| **DevOps** | CI/CD, infra, uptime for any app |
| **MLOps** | ML training, feature stores, model deployment |
| **LLMOps** | Prompts, RAG, agents, LLM APIs, eval, token cost |

**Overlap:** All use Git, CI, monitoring — LLMOps adds **faithfulness eval, prompt registry, token FinOps**.

### Lesson 7.1.3 — Concept: Production AI Problems (The "Why")

1. **Hallucinations** — wrong but confident  
2. **Non-determinism** — same input, different output  
3. **Latency variance** — 1s vs 15s  
4. **Cost unpredictability** — viral feature → bill spike  
5. **Silent failures** — HTTP 200, bad retrieval  
6. **Prompt drift** — someone edits prod prompt  
7. **Data drift** — docs updated, index stale  

**Exercise:** For each problem, guess which Phase 8–14 tool addresses it.

### Lesson 7.1.4 — Concept: AI System Lifecycle

```
Design → Build → Eval → Deploy → Monitor → Incident → Improve → (loop)
         ↑                    ↓
      Prompt/RAG          Rollback/canary
```

**LLMOps engineer owns:** Eval, deploy, monitor, incident, improve loops.

### Lesson 7.1.5 — Guided Practice: LLMOps Gap Audit

Audit your RAG repo:

| Capability | Have? | Tool to add |
|------------|-------|-------------|
| Token logging | | |
| Trace per request | | |
| Golden eval set | | |
| CI eval gate | | |
| Prompt in Git | | |
| Docker deploy | | |

**Mini project:** `docs/llmops-gap-audit.md` — hiring managers love self-awareness + plan.

### Lesson 7.1.6 — Enterprise: LLMOps Team Structure

**Platform team** builds eval/obs infra; **product teams** consume; **SRE** on-call for outages; **Legal** reviews compliance.  
**You** might be first LLMOps hire — wear all hats; document everything.

---

# PHASE 8 — OBSERVABILITY & MONITORING

# Module 8 — LLM Monitoring & Observability
### Weeks 22–25 · See What Your AI Is Actually Doing

## Why This Module Matters

**70%+ senior LLMOps JDs** mention tracing/observability. AI returns 200 OK while being wrong — only traces and eval catch it.

## Why We Are Learning This NOW

Core LLMOps skill — before eval CI and enterprise FinOps, you must **see** requests.  
**Prepares for:** Eval (Phase 9), SLOs (Phase 14), incident runbooks (Phase 14).

**Extended content:** → [module-06-llmops.md](./module-06-llmops.md) Topic 6.1 (12 lessons)

---

# Topic 8.1 — Monitoring vs Observability

## Beginner-Friendly Explanation

**Monitoring** = dashboard says "engine hot."  
**Observability** = mechanic traces why — which part, which request, which user.

## Learning Outcome

Langfuse traces on full RAG pipeline + Grafana dashboard (latency, tokens, cost).

---

### Lesson 8.1.1 — Concept: Logging vs Metrics vs Traces

| Signal | Example |
|--------|---------|
| **Log** | `"retrieval returned 0 chunks"` |
| **Metric** | `rag_latency_p95 = 2.3s` |
| **Trace** | Full waterfall: embed → search → LLM |

### Lesson 8.1.2 — Beginner: Print to Structured JSON Logs

```python
import json, logging
logging.info(json.dumps({"event": "llm_call", "latency_ms": 1200, "tokens": 450}))
```

### Lesson 8.1.3 — Intermediate: Langfuse `@observe()` on RAG Steps

Retrieve span → Generate span → attach user_id, tenant_id.

### Lesson 8.1.4 — Intermediate: OpenTelemetry Intro

Vendor-neutral standard — export to Langfuse, Datadog, Jaeger.

### Lesson 8.1.5 — Production: Prometheus + Grafana

Expose `/metrics` — p95 latency, token counter, cost counter.

### Lesson 8.1.6 — Production: Alerts That Matter

Empty retrieval rate > 10%; daily cost > 150% baseline; p95 > 5s.

### Lesson 8.1.7 — Enterprise: Multi-Tenant FinOps Dashboard

Cost per tenant; top spenders; chargeback reports.

**Labs:** Lab 8.1 Langfuse chatbot · Lab 8.2 Grafana dashboard · **Portfolio:** trace screenshot in README

**Interview questions:**
- Beginner: Monitoring vs observability?  
- Intermediate: Metrics on AI SLA dashboard?  
- Senior: Observability for 1M queries/day multi-tenant RAG?

---

# PHASE 9 — AI EVALUATION SYSTEMS

# Module 9 — LLM Evaluation & Quality Gates
### Weeks 26–29 · Prove It Works (With Numbers)

## Why This Module Matters

#1 interview question: **"How do you know it works?"** — LLMOps answer is **eval pipelines**, not "we tested manually."

## Why We Are Learning This NOW

Observability shows behavior; **eval measures quality** against golden standards.  
**Prepares for:** CI/CD gates (Phase 10), reliability SLOs (Phase 14).

**Extended content:** → [module-06-llmops.md](./module-06-llmops.md) Topic 6.2 (10 lessons)

---

# Topic 9.1 — Evaluation Fundamentals

### Lesson 9.1.1 — Concept: Why Demos Lie

### Lesson 9.1.2 — Faithfulness, Relevance, Context Precision/Recall

### Lesson 9.1.3 — Golden Datasets (30 → 100+ questions, versioned)

### Lesson 9.1.4 — Beginner: First Ragas Run

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
result = evaluate(dataset, metrics=[faithfulness, answer_relevancy])
```

### Lesson 9.1.5 — Intermediate: DeepEval Pytest + promptfoo A/B

### Lesson 9.1.6 — Advanced: Eval in GitHub Actions — Fail PR if faithfulness drops >5%

### Lesson 9.1.7 — Enterprise: Per-Tenant Golden Sets + Human Audit Sampling

**Labs:** Lab 9.1 Evaluate RAG · Lab 9.2 Automated eval pipeline  
**Portfolio badge:** `Faithfulness 0.87 | 100 cases`

---

# PHASE 10 — PROMPT VERSIONING & AI CI/CD

# Module 10 — Prompt Registry & AI CI/CD Pipelines
### Weeks 30–32

## Why This Module Matters

**LLMOps owns CI/CD for prompts** — same rigor as application code: PR, eval, canary, rollback.

**Extended content:** → [module-06-llmops.md](./module-06-llmops.md) Topic 6.3

---

# Topic 10.1 — Prompt Versioning

### Lesson 10.1.1 — Prompts as Immutable Git Artifacts

`prompts/rag_v1.txt`, `CHANGELOG-prompts.md`, MLflow experiment logs.

### Lesson 10.1.2 — Feature Flags & Canary (5% → 50% → 100%)

### Lesson 10.1.3 — Auto-Rollback on Eval Regression

**Pipeline:** lint → unit → **eval gate** → staging → canary prod

---

# PHASE 11 — DEPLOYMENT, DOCKER & ROLLBACK

# Module 11 — AI Deployment & Container Operations
### Weeks 33–35

## Why This Module Matters

LLMOps engineers **ship containers**, not laptops. Docker is the unit of deploy from dev → staging → prod.

## Why We Are Learning This NOW

Eval and observability need a **deployed environment** to monitor realistically.  
**Prepares for:** Cloud (Phase 12), K8s scaling (Phase 12).

**Extended content:** → [module-01](./module-01-python-fastapi-foundations.md) Docker topic + [module-11-production-architecture.md](./module-11-production-architecture.md)

---

# Topic 11.1 — Docker for AI Applications

### Lesson 11.1.1 — Containers vs VMs (Beginner)

**Container** = app + dependencies in a box; starts in seconds.  
**VM** = full virtual computer — heavier.

### Lesson 11.1.2 — Dockerfile for FastAPI RAG Service

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Lesson 11.1.3 — Docker Compose: API + Postgres + Redis

One command: `docker compose up` — local prod-like stack.

### Lesson 11.1.4 — Production: Health Checks and Rollback

`/health` endpoint; keep previous image tag; rollback = redeploy N-1.

**Lab 11.1:** Dockerize RAG chatbot; deploy to Railway/Render/Fly.io (free tier OK).

---

# PHASE 12 — CLOUD AI & KUBERNETES

# Module 12 — Cloud AI Infrastructure & Kubernetes
### Weeks 36–39

## Why This Module Matters

Enterprise LLMOps runs on **AWS/Azure/GCP** with **IAM, private networking, autoscaling**.

**Extended content:** → [module-08-cloud-ai.md](./module-08-cloud-ai.md)

---

# Topic 12.1 — Cloud AI (Pick One Depth Path)

### AWS: Bedrock Knowledge Base + Lambda + IAM  
### Azure: Azure OpenAI + AI Search + managed identity  
### GCP: Vertex Gemini + Cloud Run  

### Lesson 12.1.1 — Cloud Basics: Region, IAM, Object Storage

### Lesson 12.1.2 — Deploy RAG to One Cloud with Private Keys Banned in Git

---

# Topic 12.2 — Kubernetes for AI (Progressive)

### Lesson 12.2.1 — What Problem K8s Solves (Scaling, Restarts, Rolling Deploy)

### Lesson 12.2.2 — Pods, Deployments, Services, Ingress

### Lesson 12.2.3 — Deploy FastAPI with 2 Replicas on minikube/k3d

### Lesson 12.2.4 — Advanced: vLLM GPU Inference + HPA Autoscaling

**Lab 12.2:** K8s local deploy OR tri-cloud ADR document.

---

# PHASE 13 — ENTERPRISE AI, SECURITY & GOVERNANCE

# Module 13 — Enterprise LLMOps: Security, Compliance & Multi-Tenancy
### Weeks 40–42

**Extended content:** → [module-07-enterprise-ai.md](./module-07-enterprise-ai.md) + [module-10-ai-security-responsible-ai.md](./module-10-ai-security-responsible-ai.md)

---

# Topic 13.1 — Multi-Tenant RAG Operations

### Lesson 13.1.1 — tenant_id on Every Query

### Lesson 13.1.2 — CI Test: Tenant A Cannot See Tenant B Docs

---

# Topic 13.2 — AI Security for LLMOps

### Lesson 13.2.1 — OWASP LLM Top 10 (Prompt Injection, Excessive Agency)

### Lesson 13.2.2 — Secrets Management (Vault, AWS SM — No Keys in Git)

### Lesson 13.2.3 — Guardrails + Audit Log on Every Block

### Lesson 13.2.4 — RBAC / JWT / OAuth for AI APIs

---

# Topic 13.3 — Governance & Compliance

### Lesson 13.3.1 — COMPLIANCE.md + Data Deletion from Vector Index

### Lesson 13.3.2 — Model Registry + Model Cards

### Lesson 13.3.3 — Append-Only Audit Export for SOC2 Audits

---

# PHASE 14 — PRODUCTION AI RELIABILITY

# Module 14 — SRE for LLM Systems: SLOs, Incidents & FinOps
### Weeks 43–45

**Extended content:** → [module-11-production-architecture.md](./module-11-production-architecture.md)

---

# Topic 14.1 — Reliability Engineering for AI

### Lesson 14.1.1 — SLIs/SLOs for AI (p95 latency, faithfulness sample, uptime)

### Lesson 14.1.2 — Runbooks: Rate Limit, Index Corrupt, Eval Regression

### Lesson 14.1.3 — Game Day Drills and Blameless Postmortems

---

# Topic 14.2 — FinOps for LLMOps

### Lesson 14.2.1 — Token Forecasting and $/1K Queries

### Lesson 14.2.2 — Semantic Cache + Model Routing (30% Cost Reduction Lab)

### Lesson 14.2.3 — Per-Tenant Chargeback Dashboard

---

# Topic 14.3 — Terraform & Production IaC

### Lesson 14.3.1 — Terraform Modules for AI Staging Environment

### Lesson 14.3.2 — Remote State + PR Plan Review

---

# PHASE 15 — ENTERPRISE CAPSTONE PROJECTS

# Module 15 — LLMOps Capstone Projects (Choose One Primary)

### Weeks 46–49 · Real Enterprise-Grade Deliverables

Each capstone MUST include: **architecture · deploy · monitoring · eval · CI/CD · security · runbook · README metrics**

---

## Capstone 1 — Enterprise RAG Platform (LLMOps Edition)

**Build:** Multi-tenant RAG API with ACL filters  
**LLMOps pack:** Langfuse + Ragas CI + prompt registry + Grafana  
**Metrics in README:** faithfulness ≥ 0.85, p95 < 3s, $/query documented  
**Enterprise:** COMPLIANCE.md + deletion API + tenant isolation test

---

## Capstone 2 — AI Monitoring & Observability Platform

**Build:** Instrumentation SDK or middleware wrapping any OpenAI-compatible API  
**Features:** Trace UI integration (Langfuse), cost dashboard, alert rules  
**Portfolio:** Before/after debug story — "found retrieval failure in 5 min via trace"

---

## Capstone 3 — AI Evaluation Pipeline (Eval-as-a-Service)

**Build:** GitHub Action + CLI `eval run --golden golden_v3.jsonl`  
**Features:** Ragas + DeepEval + regression baseline JSON + PR comment bot  
**Enterprise:** Golden set versioning; eval report artifact per release

---

## Capstone 4 — AI Reliability / Incident Simulation Platform

**Build:** Chaos-style tests — kill vector DB, spike latency, inject bad prompt  
**Features:** Runbooks triggered; rollback script; postmortem template filled  
**Interview gold:** "Tell me about a production AI incident" — use simulated drill story

---

## Capstone 5 — Multi-Agent Ops Dashboard

**Build:** LangGraph agent with **every tool call traced** and **eval suite for tool success rate**  
**Features:** HITL approval UI; audit log export; max-step enforcement  
**Metrics:** Tool success ≥ 90% on 20-task suite

---

## Capstone 6 — AI Deployment Platform (GitOps Lite)

**Build:** Docker + GitHub Actions deploy to cloud staging/prod  
**Features:** Eval gate → deploy → smoke test → automatic rollback  
**IaC:** Terraform module for vector DB + API compute

---

# PHASE 16 — INTERVIEW & JOB READINESS

# Module 16 — LLMOps Career Launch
### Weeks 50–52

**Extended content:** → [module-12-capstone-job-readiness.md](./module-12-capstone-job-readiness.md)

---

# Topic 16.1 — LLMOps Resume & Portfolio

### Resume bullet formula

`Action + LLMOps tool + metric + business outcome`

**Example:**  
*"Built Ragas eval CI gate on RAG platform — blocked 3 faithfulness regressions; maintained 0.87 score on 100-case golden set; reduced mean p95 latency 22% via semantic cache."*

### GitHub pin order

1. LLMOps capstone (eval + traces + deploy)  
2. RAG/agent project  
3. Infrastructure or eval tooling repo  

---

# Topic 16.2 — Interview Preparation

## Beginner Questions

- What is LLMOps?  
- Monitoring vs observability?  
- What is faithfulness in RAG eval?

## Intermediate Questions

- Design eval pipeline for production RAG.  
- How deploy a new system prompt safely?  
- Production LLM failing — debugging workflow?

## Advanced / System Design

- Multi-tenant RAG for 1000 B2B customers with observability.  
- AI bill went 10× — diagnose and fix.  
- Design LLMOps platform for 50 internal AI products.

## Take-Home Strategy

48h box: MVP + eval + README tradeoffs — LLMOps hires judge **operational thinking**.

---

# Topic 16.3 — Remote USA Job Strategy

- **Target titles:** LLMOps Engineer, AI Platform, AI Reliability, Production AI  
- **Apply:** 10–15/week after portfolio ready; prioritize companies shipping GenAI (not just researching)  
- **Freelance:** Eval pipeline setup ($3K–$15K fixed); observability audit ($2K–$8K)  
- **Consulting:** Phase 7 POC template → 2-week LLMOps assessment engagement  

**Resources:** [job-readiness/](../job-readiness/) · [15-interview-preparation-matrix.md](../15-interview-preparation-matrix.md)

---

# APPENDIX A — Tool Stack Reference (2026–2027)

| Category | Tools |
|----------|-------|
| Language | Python 3.11+ |
| API | FastAPI, uvicorn |
| LLM APIs | OpenAI, Anthropic, Azure OpenAI, Bedrock, Vertex |
| RAG | LangChain/LlamaIndex, pgvector, Pinecone |
| Agents | LangGraph, tool calling |
| Observability | Langfuse, OpenTelemetry, Prometheus, Grafana |
| Eval | Ragas, DeepEval, promptfoo |
| CI/CD | GitHub Actions, MLflow |
| Containers | Docker, Docker Compose |
| Orchestration | Kubernetes, Helm |
| Cloud | AWS, Azure, GCP, Terraform |
| Security | Guardrails AI, OWASP LLM, JWT/OAuth |

---

# APPENDIX B — LLMOps Engineer Readiness Checklist

| # | Capability | Evidence |
|---|------------|----------|
| 1 | Python + FastAPI production API | GitHub repo |
| 2 | RAG with citations | Demo + eval score |
| 3 | Langfuse (or OTel) full trace | Screenshot |
| 4 | Golden set ≥50 + Ragas in CI | CI badge |
| 5 | Prompts versioned in Git | CHANGELOG-prompts.md |
| 6 | Docker deploy + public URL | README link |
| 7 | Cost/latency metrics in README | Numbers, not adjectives |
| 8 | THREAT_MODEL.md + guardrails | Security section |
| 9 | Runbook for one AI incident | /runbooks/ |
| 10 | 2-min demo video | README embed |

**When all 10 are checked:** You are **interview-ready for LLMOps roles** in the USA market (2026–2027).

---

# APPENDIX C — Mapping to Course Modules

| This Roadmap Phase | Course Module File |
|--------------------|-------------------|
| Phase 0 | *(new — in this doc)* |
| Phase 1–2 | module-01 |
| Phase 3 | module-02 |
| Phase 4 | module-03 |
| Phase 5 | module-04 |
| Phase 6 | module-05 |
| Phase 7–10 | module-06 |
| Phase 13 | module-07, module-10 |
| Phase 12 | module-08 |
| Phase 11, 14 | module-11 |
| Phase 15–16 | module-12 |
| Full-stack product UI | module-09 (optional for LLMOps track) |

---

*You started with no IT background. Finish with production LLMOps engineering skills. Ship metrics, not adjectives.*
