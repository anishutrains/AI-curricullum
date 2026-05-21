# Module 02 — LLM APIs & Foundations

---

## Topic 2.1: OpenAI API Production Patterns

### 1. Topic Name
OpenAI API Production Patterns

### 2. Why This Topic Matters
OpenAI appears in 90%+ of US GenAI JDs. Production means streaming, structured outputs, tool calling, retries, and cost tracking—not playground demos.

### 3. Job Roles
Generative AI Engineer, LLM Engineer, AI Engineer, AI Product Engineer

### 4. Learning Objectives
- Implement chat completions with streaming
- Use JSON schema / structured outputs
- Configure tool/function calling
- Track tokens and cost per request

### 5. Lessons/Subtopics
- Models: GPT-4o, o-series reasoning models
- Messages API vs Assistants (when to use each)
- Streaming deltas handling
- Tool calling loop
- Batch API for offline jobs
- Fine-tuning overview (when justified)

### 6. Hands-on Labs
**Lab 2.1:** Multi-turn chat service with token/cost middleware logging.

### 7. Enterprise Projects
Model router: GPT-4o for quality, mini for simple tasks; fallback on rate limit.

### 8. Portfolio Projects
OpenAI integration layer abstracted behind provider interface.

### 9. Interview Preparation
- "Design token budget enforcement for a SaaS copilot."
- "When would you fine-tune vs RAG vs prompt?"

### 10. Real-world Use Cases
Support bots, code generation, document summarization.

### 11. Tools & Technologies
OpenAI Python SDK, tiktoken, LiteLLM (routing intro)

### 12. Common Mistakes
- No retry with exponential backoff
- Ignoring `max_tokens` cost explosion
- Storing full prompts in logs (PII)

### 13. Industry Best Practices
- Abstract provider behind interface for multi-vendor
- Cache system prompts where possible
- Log token usage to metrics backend

### 14. Capstone Deliverables
Provider-agnostic `LLMClient` with OpenAI implementation + cost dashboard stub.

---

## Topic 2.2: Anthropic & Gemini APIs

### 1. Topic Name
Anthropic Claude & Google Gemini APIs

### 2. Why This Topic Matters
Enterprise deals increasingly multi-vendor. Anthropic leads tool use/computer use; Gemini integrates with GCP Vertex.

### 3. Job Roles
Enterprise AI Engineer, LLM Engineer, AI Solutions Engineer

### 4. Learning Objectives
- Implement Claude messages API with tool use
- Use Gemini via AI Studio and Vertex AI
- Compare latency, cost, context windows across vendors

### 5. Lessons/Subtopics
- Claude system prompts and XML tags pattern
- Extended context use cases
- Gemini multimodal inputs
- Vertex AI enterprise auth (service accounts)
- Cross-provider eval baselines

### 6. Hands-on Labs
**Lab 2.2:** Same task on OpenAI, Anthropic, Gemini—log latency, cost, quality scores.

### 7. Enterprise Projects
Vendor abstraction + contract-aware model selection (EU data residency → Azure/GCP).

### 8. Portfolio Projects
Benchmark report (1-pager) in repo `/docs/model-comparison.md`.

### 9. Interview Preparation
- "How do you choose between Claude and GPT-4 for a legal RAG app?"
- "Explain Vertex AI vs direct Gemini API."

### 10. Real-world Use Cases
Regulated industries picking vendor by data boundary; multimodal doc Q&A.

### 11. Tools & Technologies
anthropic SDK, google-generativeai, Vertex AI SDK, LiteLLM

### 12. Common Mistakes
- Hard-coding one vendor in application layer
- Not testing tool-use compatibility across models
- Ignoring regional API availability

### 13. Industry Best Practices
- Golden eval set run on all candidate models
- Document model selection ADR
- Feature flag per tenant model preference

### 14. Capstone Deliverables
Multi-provider router with config-driven model map.

---

## Topic 2.3: HuggingFace & Open-Source Models

### 1. Topic Name
HuggingFace & Open-Source LLMs (Ollama, vLLM intro)

### 2. Why This Topic Matters
Cost-sensitive enterprises self-host. HuggingFace skills appear in platform and infra roles; Ollama for local dev, vLLM for production inference.

### 3. Job Roles
AI Infrastructure Engineer, AI Platform Engineer, LLM Engineer

### 4. Learning Objectives
- Load and run models via HuggingFace Inference API / Endpoints
- Develop locally with Ollama
- Understand vLLM serving architecture (preview for Module 08)

### 5. Lessons/Subtopics
- Model cards and licensing
- Embeddings models (BGE, E5, nomic)
- Ollama local workflow
- vLLM throughput concepts
- Quantization tradeoffs (GGUF, AWQ)

### 6. Hands-on Labs
**Lab 2.3:** Local RAG with Ollama + same pipeline pointing to OpenAI embeddings.

### 7. Enterprise Projects
Air-gapped deployment option using self-hosted Llama/Mistral.

### 8. Portfolio Projects
"Cost comparison: API vs self-hosted" analysis document.

### 9. Interview Preparation
- "When is self-hosting cheaper than APIs at 1M queries/month?"
- "Explain embedding model selection for RAG."

### 10. Real-world Use Cases
PII-sensitive on-prem, dev environments without API spend.

### 11. Tools & Technologies
HuggingFace Hub, transformers, Ollama, vLLM (intro), sentence-transformers

### 12. Common Mistakes
- Picking largest model without latency budget
- Ignoring license restrictions for commercial use
- No GPU memory planning

### 13. Industry Best Practices
- Pin model revisions in config
- Warm inference pools in production
- Separate embedding and generation infrastructure

### 14. Capstone Deliverables
Dual-mode config: `CLOUD_API` vs `LOCAL_OLLAMA` switch in starter app.

---

## Topic 2.4: Structured Outputs & Model Routing

### 1. Topic Name
Structured Outputs, Parsing & Intelligent Model Routing

### 2. Why This Topic Matters
Enterprise integrations require JSON/XML contracts, not free text. Routing saves 40–70% cost on simple queries.

### 3. Job Roles
AI Integration Engineer, LLM Engineer, AI Automation Engineer

### 4. Learning Objectives
- Enforce Pydantic-validated LLM outputs
- Build classifier-based model router
- Handle parse failures gracefully

### 5. Lessons/Subtopics
- JSON mode, instructor library, OpenAI structured outputs
- Constrained decoding concepts
- Query complexity classifier (cheap model)
- Fallback chains
- Caching identical requests (semantic intro)

### 6. Hands-on Labs
**Lab 2.4:** Extract structured `InvoiceData` from PDF text with validation retry loop.

### 7. Enterprise Projects
Schema registry for all LLM outputs; breaking change detection in CI.

### 8. Portfolio Projects
Router reducing average cost/query documented with before/after metrics.

### 9. Interview Preparation
- "LLM returned invalid JSON 15% of the time—how do you fix it?"
- "Design a model routing layer."

### 10. Real-world Use Cases
ERP field extraction, ticket classification, CRM auto-fill.

### 11. Tools & Technologies
Pydantic, instructor, outlines (optional), Redis cache

### 12. Common Mistakes
- No retry with repair prompt on schema failure
- Routing without monitoring misroute rate
- Over-structuring simple tasks (added latency)

### 13. Industry Best Practices
- Max 2 repair attempts then human queue
- Log parse failure reasons for prompt iteration
- A/B test router rules

### 14. Capstone Deliverables
`StructuredExtractor` class with ≥95% schema success on test set.

---

*Next: [module-03-prompt-engineering-dspy.md](./module-03-prompt-engineering-dspy.md)*
