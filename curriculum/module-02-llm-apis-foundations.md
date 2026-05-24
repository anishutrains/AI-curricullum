# Module 02 — LLM APIs & Foundations
### Zero-to-Hero Track · Weeks 8–12 · Connect Real AI to Your Backend

---

## Module Objective

This module teaches you to **call real Large Language Models (LLMs)** from Python and FastAPI — OpenAI, Anthropic, Google Gemini, and open-source models via Ollama/HuggingFace. You will go from *"I used ChatGPT in a browser"* to *"I built a production LLM integration layer with streaming, cost tracking, and multi-provider support."*

**Why this module matters**
- **90%+ of US Generative AI job postings** mention OpenAI, Claude, or Gemini APIs.
- Every RAG system (Module 04) and agent (Module 05) **calls an LLM at the core**.
- Companies pay $150K–$220K for engineers who integrate LLMs **safely, cheaply, and reliably** — not demo scripts.

**Where this is used in real companies**
- **Startups:** GPT-4o powers product features via backend API calls
- **Enterprises:** Azure OpenAI or Bedrock for data residency
- **Consulting:** Compare Claude vs GPT for client use case and document ADR

**Projects after this module**
- Multi-provider `LLMClient` library (portfolio piece)
- Real streaming chat API (upgrade Module 01 FastAPI)
- Model comparison benchmark report for interviews

---

## Job Roles Prepared By This Module

Generative AI Engineer · LLM Engineer · AI Engineer · AI Product Engineer · Enterprise AI Engineer · AI Solutions Engineer · AI Infrastructure Engineer · AI Integration Engineer

---

## Beginner Skills Students Will Learn
- What an LLM is and how API pricing works (tokens)
- Create OpenAI account; store API keys safely in `.env`
- Send first chat completion request
- Understand messages, roles, system prompts
- Read API documentation and SDK examples

## Intermediate Skills Students Will Learn
- Multi-turn conversations with history
- Streaming tokens to FastAPI SSE endpoint
- Token counting and cost estimation
- Anthropic Claude and Google Gemini SDK usage
- Run local models with Ollama

## Advanced Skills Students Will Learn
- Tool/function calling loops
- Structured JSON outputs with Pydantic validation
- Model routing (cheap vs expensive models)
- Provider abstraction layer for multi-vendor
- Batch API and fine-tuning decision framework

## Production-Level Skills Students Will Learn
- Retry with exponential backoff on 429/500
- Provider-agnostic interface with fallbacks
- Cost logging per request and per user
- Never log PII or full prompts in production logs
- Benchmark latency/cost/quality across providers (ADR)

---

# Topic 2.1 — OpenAI API: From First Call to Production Patterns

## Why This Topic Matters

OpenAI (GPT-4o, o-series) appears in more US AI job descriptions than any other single vendor. If you cannot implement chat, streaming, tools, and cost control with the OpenAI Python SDK, you are not yet employable as a GenAI engineer.

**Real companies:** Duolingo, Stripe, and thousands of startups ship features on OpenAI APIs daily.

## Learning Outcome

You will build a production-grade OpenAI integration with streaming, token tracking, error handling, and a clean client class plugged into your Module 01 FastAPI app.

---

### Lesson 2.1.1 — What Is a Large Language Model? (Conceptual Foundation)

**Concepts**
- LLM = neural network trained on vast text; predicts next token
- Tokens ≈ word pieces; pricing is per token (input + output)
- Models: GPT-4o (fast + multimodal), o-series (reasoning), GPT-4o-mini (cheap)
- ChatGPT website vs OpenAI API (API = you build the product)
- Temperature: 0 = deterministic, 1 = creative

**Analogy:** LLM is an extremely well-read assistant who completes sentences — you provide context (prompt), it continues.

**Exercise:** Open platform.openai.com; explore model docs; note price per 1M tokens for gpt-4o vs gpt-4o-mini

**Check:** Why do companies use API instead of telling users "go to ChatGPT"?

---

### Lesson 2.1.2 — API Keys, Billing, and Security (Do This First)

**Concepts**
- API key = password for your app; never expose in frontend or GitHub
- `.env` file: `OPENAI_API_KEY=sk-...`
- `.gitignore` must include `.env`
- Usage limits and billing alerts in OpenAI dashboard
- Organization vs project API keys (enterprise)

**Step-by-step**
1. Create OpenAI account; add payment method (set $5–10 limit for learning)
2. Create API key; copy once — store in `.env`
3. Verify `.env` is gitignored: `git status` should NOT show `.env`

**Common disaster:** Key pushed to GitHub → bots drain account in minutes → rotate key immediately

**Deliverable:** `.env.example` with `OPENAI_API_KEY=` placeholder (no real key)

---

### Lesson 2.1.3 — Your First OpenAI Chat Completion (Sync)

**Concepts**
- Install: `pip install openai`
- Client: `OpenAI()` reads key from env automatically
- Chat Completions API: `client.chat.completions.create(...)`
- Messages list: system, user, assistant roles
- Response: `response.choices[0].message.content`

**Coding**
```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful AI tutor."},
        {"role": "user", "content": "Explain APIs in one paragraph."},
    ],
)
print(response.choices[0].message.content)
print(response.usage.total_tokens)
```

**Exercise:** Change system prompt to "Explain like I'm 10"; compare outputs

**Deliverable:** `scripts/first_openai_call.py`

---

### Lesson 2.1.4 — Understanding Messages and Multi-Turn Conversations

**Concepts**
- LLM is stateless — you send full history every call
- Building history: append user message, get assistant reply, append assistant message
- Context window limit (max tokens in one request)
- Truncation strategies when history too long (preview Module 04)

**Coding exercise:** CLI chat loop maintaining `messages` list until user types `quit`

**Real-world:** Customer support bot remembers thread by sending last N messages

**Common error:** Forgetting to append assistant response to history — model "forgets" its answer

---

### Lesson 2.1.5 — Model Selection and Cost Control

**Concepts**
- gpt-4o-mini for simple tasks; gpt-4o for complex reasoning
- `max_tokens` caps output length and cost
- `tiktoken` library counts tokens before sending
- Log `response.usage.prompt_tokens`, `completion_tokens`

**Coding exercise:** Function `estimate_cost(model, prompt_tokens, completion_tokens)` using OpenAI pricing page rates

**Enterprise:** CFO asks "cost per user per month" — you need token logs from day one

---

### Lesson 2.1.6 — Streaming Responses (Sync Iterator)

**Concepts**
- `stream=True` returns chunks as tokens generate
- Iterate `for chunk in stream:` → `chunk.choices[0].delta.content`
- Time-to-first-token UX metric
- Why streaming matters for chat UIs (Module 09)

**Coding exercise:** Print tokens as they arrive in terminal (typewriter effect)

**Bridge FastAPI:** Connect stream to SSE endpoint from Module 01 Topic 1.3

---

### Lesson 2.1.7 — Integrating OpenAI Stream into FastAPI SSE

**Concepts**
- Async generator yielding SSE format: `data: {json}\n\n`
- Client disconnect handling
- Error mid-stream: send error event or close gracefully

**Coding exercise:** Replace mock stream in `/v1/chat/stream` with real OpenAI stream

**Deliverable:** Working streaming chat UI endpoint (test with curl or simple HTML page)

**Architecture**
```
Browser → FastAPI SSE → OpenAI stream=True → tokens flow back
```

---

### Lesson 2.1.8 — Error Handling, Retries, and Rate Limits

**Concepts**
- Exceptions: RateLimitError (429), APIConnectionError, AuthenticationError
- Exponential backoff: 1s, 2s, 4s + random jitter
- `max_retries` on OpenAI client
- User-friendly error messages (don't leak API details)

**Coding exercise:** Wrapper `call_openai_with_retry()` handling 429 with backoff

**Production:** Circuit breaker if OpenAI down — fallback model or cached response

---

### Lesson 2.1.9 — Tool Calling (Function Calling) Fundamentals

**Concepts**
- LLM chooses to call functions you define (search, calculator, CRM)
- Tools schema: name, description, parameters (JSON Schema)
- Loop: model returns tool_calls → you execute → send tool result → model final answer
- Foundation for agents (Module 05)

**Coding exercise:** One tool `get_current_weather(city)` — mock return — model uses it to answer "Weather in NYC?"

**Real-world:** Copilot searches internal docs via tool before answering

---

### Lesson 2.1.10 — Batch API and Fine-Tuning Overview (When to Use)

**Concepts**
- Batch API: cheap async jobs for 1000s of requests (not real-time chat)
- Fine-tuning: custom model weights for specialized tone/format
- Decision: prompt engineering → RAG → fine-tune (in that cost order usually)
- Fine-tuning needs quality dataset; maintenance burden

**Exercise:** Write 1-page decision matrix: when NOT to fine-tune (most startup cases)

**Interview:** "When would you fine-tune vs RAG vs long context?"

---

### Lesson 2.1.11 — Messages API vs Assistants API (Architecture Choice)

**Concepts**
- Chat Completions: you manage state, tools, RAG — full control (most common)
- Assistants API: OpenAI manages threads, code interpreter, file search — faster POC, less control
- Enterprise production usually prefers Completions + own architecture

**Exercise:** List pros/cons table for startup MVP vs enterprise scale

---

### Topic 2.1 — Exercises, Projects, Interview

**Beginner exercises:** Change models; adjust temperature; count tokens for 10 prompts  
**Mini project:** CLI tutor bot with history + cost summary on exit  
**Assignment:** `OpenAIClient` class: chat, stream, retry, token logging — 8 tests with mocks  
**Enterprise scenario:** Support bot must stay under $0.02 per ticket — enforce max_tokens + model routing  
**Interview questions:** Token budget design; streaming vs non-streaming; handle 429  
**Portfolio:** Screenshot of streaming API + usage dashboard in README  
**Common errors:** Key in frontend; unbounded history; no max_tokens  
**Production:** Abstract client interface; log usage; never log full PII prompts  

---

# Topic 2.2 — Anthropic Claude & Google Gemini APIs

## Why This Topic Matters

Enterprises rarely lock to one vendor. **Anthropic Claude** excels at long context and tool use; **Google Gemini** integrates with GCP Vertex for regulated Google-shop customers. US job posts increasingly say "OpenAI **or** Anthropic."

## Learning Outcome

You will call Claude and Gemini for the same task, compare results, and add them to a multi-provider router behind one interface.

---

### Lesson 2.2.1 — Multi-Vendor Strategy (Why Not OpenAI Only?)

**Concepts**
- Vendor risk: outage, price change, policy change
- Best model varies by task (code, legal, vision)
- Data residency: Azure OpenAI, Vertex for EU/GCP requirements
- Abstraction layer pattern: one `LLMClient` interface, many providers

---

### Lesson 2.2.2 — Anthropic Claude: Setup and First Message

**Concepts**
- `pip install anthropic`; `ANTHROPIC_API_KEY` in `.env`
- Messages API similar to OpenAI
- System prompt often passed separately in Claude API
- Models: Claude 3.5 Sonnet, Haiku (fast/cheap)

**Coding:** Same tutor prompt on Claude; compare tone and length to GPT

---

### Lesson 2.2.3 — Claude System Prompts and XML Tags Pattern

**Concepts**
- Anthropic docs recommend structuring prompts with XML tags: `<document>`, `<instructions>`
- Helps model separate context from task
- Extended context windows for long documents (RAG preview)

**Exercise:** Wrap policy text in `<document>` tags; ask questions about it

---

### Lesson 2.2.4 — Google Gemini via AI Studio and SDK

**Concepts**
- Google AI Studio for playground (like OpenAI playground)
- `pip install google-generativeai`
- `GEMINI_API_KEY` in `.env`
- Gemini Pro vs Flash (speed/cost)

**Coding:** Generate answer from same prompt; log latency

---

### Lesson 2.2.5 — Gemini Multimodal Inputs (Image + Text)

**Concepts**
- Send image bytes + text question in one request
- Use cases: diagram Q&A, receipt scan, UI mockup feedback
- Preview for Module 09 multimodal apps

**Exercise:** Upload image screenshot; ask "What does this UI show?"

---

### Lesson 2.2.6 — Vertex AI Enterprise Auth (Awareness)

**Concepts**
- Production on GCP uses service accounts, not API keys in code
- VPC, private endpoints, audit logs
- Module 08 goes deep — here know the distinction exists

---

### Lesson 2.2.7 — Cross-Provider Benchmark Lab

**Concepts**
- Same 20 prompts → GPT, Claude, Gemini
- Measure: latency, cost, subjective quality score 1–5
- Document in ADR (Architecture Decision Record)

**Deliverable:** `/docs/model-comparison.md` with table and recommendation

**Interview:** "How do you choose Claude vs GPT-4 for legal RAG?"

---

### Topic 2.2 — Mini Project
**Model Arena Script:** Run benchmark suite; output CSV; chart cost vs quality in README.

---

# Topic 2.3 — Open-Source & Local Models (Ollama, HuggingFace)

## Why This Topic Matters

Not every company sends data to OpenAI. **Air-gapped**, **cost-sensitive**, and **privacy-first** teams run Llama/Mistral locally. **HuggingFace** is the GitHub of ML models — platform engineers use it daily.

## Learning Outcome

You will run local models with Ollama, understand HuggingFace model cards, and switch your app between cloud API and local inference.

---

### Lesson 2.3.1 — Open Source vs Closed API Models

**Concepts**
- Closed: GPT-4, Claude — pay per token, no weight access
- Open weights: Llama, Mistral — self-host, hardware cost
- Tradeoffs: privacy, cost at scale, quality, ops burden

**Analogy:** API = taxi; self-host = owning a car (maintenance + parking)

---

### Lesson 2.3.2 — HuggingFace Hub and Model Cards

**Concepts**
- huggingface.co hosts models, datasets, spaces
- Model card: intended use, limitations, license (commercial use?)
- Inference API for quick tests without GPU

**Exercise:** Find `BAAI/bge-small-en-v1.5` embedding model — read license — note use in RAG (Module 04)

---

### Lesson 2.3.3 — Ollama: Install and Run Local Chat

**Concepts**
- ollama.com — one-command local models
- `ollama pull llama3.2` then `ollama run llama3.2`
- HTTP API on localhost:11434 — call from Python

**Coding:** Python requests to Ollama API with same prompt as OpenAI

**Deliverable:** App config `LLM_PROVIDER=ollama|openai` switch

---

### Lesson 2.3.4 — Embedding Models (Open Source)

**Concepts**
- Embeddings = vectors for semantic search (Module 04 RAG)
- Models: OpenAI ada, BGE, E5, nomic-embed-text via Ollama
- Same pipeline, swap embedding provider

**Exercise:** Generate embeddings for 5 sentences; print vector length

---

### Lesson 2.3.5 — vLLM and Quantization (Production Self-Host Preview)

**Concepts**
- vLLM serves open models at scale on GPU
- Quantization GGUF/AWQ reduces memory — quality tradeoff
- When self-host beats API: high volume, strict privacy

**Interview:** "When is self-hosting cheaper at 1M queries/month?" — back-of-envelope math exercise

---

### Topic 2.3 — Assignment
Dual-mode `LLMClient`: integration tests with Ollama (skip if not installed) + OpenAI; cost comparison doc.

---

# Topic 2.4 — Structured Outputs & Intelligent Model Routing

## Why This Topic Matters

Enterprise systems need **JSON a ERP can parse**, not prose. Intelligent routing sends easy questions to cheap models — **saving 40–70%** on API bills at scale.

## Learning Outcome

You will extract validated Pydantic objects from LLM outputs and build a router that picks the right model per request.

---

### Lesson 2.4.1 — Why Structured Outputs Matter

**Concepts**
- Free text unusable for SQL insert, CRM update, workflow trigger
- JSON mode / structured outputs enforce shape
- Validation failures happen — plan retry logic

**Example:** Extract `{ "customer_name", "issue_type", "urgency" }` from support email

---

### Lesson 2.4.2 — OpenAI JSON Mode and response_format

**Concepts**
- `response_format={"type": "json_object"}`
- Prompt must mention JSON explicitly
- Parse with `json.loads`; validate with Pydantic

**Coding:** Extract `InvoiceData` from messy text; Pydantic catches missing fields

---

### Lesson 2.4.3 — Instructor Library Pattern

**Concepts**
- `pip install instructor`
- Patch OpenAI client; `response_model=MyModel`
- Automatic retry on validation failure (library feature)

**Coding:** `class Person(BaseModel): name: str; age: int` from biography paragraph

---

### Lesson 2.4.4 — Repair Loops When JSON Is Invalid

**Concepts**
- Max 2 repair attempts: send error back to model "fix JSON to match schema"
- Then escalate to human queue — don't infinite loop
- Log parse failure rate metric

**Production:** 95%+ schema success target for automation

---

### Lesson 2.4.5 — Query Complexity Classifier (Model Router)

**Concepts**
- Cheap model classifies: "simple" vs "complex"
- Simple → gpt-4o-mini; complex → gpt-4o
- Fallback chain if primary fails
- Monitor misroute rate with human spot checks

**Coding:** Router function returning model name; log routing decision + final quality

---

### Lesson 2.4.6 — Semantic Cache Introduction

**Concepts**
- Identical or similar questions → cache response — save money
- Hash exact match vs embedding similarity (Module 04 ties in)
- TTL and invalidation when knowledge base updates

**Exercise:** Dict cache for exact match; measure hit rate on repeated FAQ queries

---

### Topic 2.4 — Capstone Deliverable for Module 02

**`LLMClient` package in your portfolio repo:**
- [ ] Providers: OpenAI, Anthropic, Gemini (at least 2 working)
- [ ] Methods: `chat()`, `stream()`, `chat_structured()`
- [ ] Retry, timeout, token/cost logging
- [ ] Model router with config YAML
- [ ] FastAPI `/v1/chat` uses real LLMClient
- [ ] `/docs/model-comparison.md` benchmark
- [ ] 15+ tests with mocked HTTP
- [ ] `.env.example` documented

---

## Module 02 — Master Checklist Before Module 03

| Skill | Yes / No |
|-------|----------|
| Secure API key storage | |
| OpenAI chat + stream | |
| Token/cost logging | |
| Claude OR Gemini integrated | |
| Ollama local fallback tried | |
| Structured Pydantic extraction | |
| Model router stub | |
| FastAPI uses real LLM | |

---

*Next module: [module-03-prompt-engineering-dspy.md](./module-03-prompt-engineering-dspy.md)*
