# Module 04 — RAG Systems (Retrieval-Augmented Generation)
### Zero-to-Hero Track · Weeks 16–20 · Teach AI to Answer From *Your* Documents

---

## Why This Module Exists

**Why learn this NOW?**  
You completed Modules 01–03: you can build APIs, call LLMs, and engineer prompts. But raw LLMs **hallucinate** and **don't know your company's data**. RAG is the #1 pattern enterprises use to fix that — it appears in **80%+ of US Generative AI job postings**.

**Why companies care**  
- **Stripe, Morgan Stanley, and Walmart** deploy internal copilots grounded on policy docs, not generic ChatGPT.
- RAG skills carry a **~11% salary premium** in US AI engineer compensation surveys (2026).
- Tutorial developers build "chat with PDF" demos; **employable engineers** build RAG with eval metrics, citations, and security.

**How this connects to the career path**
| Before (Modules 01–03) | This module (04) | After (Modules 05+) |
|------------------------|------------------|---------------------|
| LLM answers from memory only | LLM answers from **retrieved documents** | Agents **use RAG as a tool** |
| Prompts control tone | Retrieval controls **facts** | Multi-agent research pipelines |

**Prerequisites (you must have these first)**
- Module 01: Python, FastAPI, files, JSON, Docker
- Module 02: OpenAI/LLM API calls, streaming, token logging
- Module 03: System prompts, prompt templates, basic eval mindset

**Future modules that depend on Module 04**
- **Module 05 (Agents):** `search_knowledge_base` tool = RAG pipeline
- **Module 06 (LLMOps):** Ragas eval on RAG quality
- **Module 07 (Enterprise):** ACL-aware retrieval, multi-tenant indexes
- **Module 08 (Cloud):** Bedrock Knowledge Bases, Azure AI Search

---

## What Students Will Become Capable Of

**After this module you can:**
- Explain RAG to a hiring manager and whiteboard the full pipeline
- Build document Q&A on PDFs with **source citations**
- Choose chunking strategy with **data**, not guesses
- Store and query embeddings in a **vector database**
- Improve retrieval with **hybrid search and reranking**
- Measure faithfulness with **Ragas** (preview for Module 06)
- Ship **Enterprise RAG Assistant** — flagship portfolio project #1

---

## Job Roles This Module Supports

| Role | Why RAG is required |
|------|---------------------|
| **RAG Engineer** | Core job function |
| **Generative AI Engineer** | Most product features use RAG |
| **Enterprise AI Engineer** | Internal knowledge copilots |
| **Applied AI Engineer** | Vertical solutions (legal, HR, finance) |
| **AI Solutions Engineer** | Client POCs are 70% RAG |
| **LLM Engineer** | Grounding reduces hallucination |
| **AI Consultant** | "Should we fine-tune or RAG?" — you answer RAG first |

**Recruiter value:** Portfolio RAG project with **faithfulness score + architecture diagram** beats ten tutorial chatbots.

**Salary impact:** RAG + production deployment moves candidates from $120K junior band toward $155K–$190K mid-level GenAI roles (US, 2026).

---

## Skill Progression in This Module

| Level | You will... |
|-------|-------------|
| **Beginner** | Understand why RAG exists; run first "chat with PDF" locally |
| **Intermediate** | Chunk, embed, store, retrieve, generate with citations |
| **Advanced** | Hybrid search, reranking, query transformation |
| **Production** | Eval metrics, latency targets, cache, cost per query |
| **Enterprise** | Multi-tenant indexes, ACL filters, graph-augmented retrieval (optional) |

---

# Topic 4.1 — Understanding RAG: The Problem and the Pipeline

## Beginner Explanation

Imagine you ask ChatGPT: *"What is our company's vacation policy?"*  
ChatGPT **does not know** — it will guess (hallucinate).  

**RAG** fixes this in 3 steps:
1. **Retrieve** — search your real documents for relevant paragraphs  
2. **Augment** — paste those paragraphs into the prompt  
3. **Generate** — LLM writes answer **using only that context**

**Analogy:** Open-book exam. Without RAG = closed-book (memorization/hallucination). With RAG = open-book (lookup + explain).

## Why Companies Use This

- **HR bots** answer from official policy PDFs (liability reduction)
- **Engineering copilots** search internal wikis and runbooks
- **Legal assistants** cite contract clauses with page numbers
- Cheaper than fine-tuning for most knowledge that **changes frequently**

## Learning Outcome

You will diagram naive vs production RAG, implement ingest→chunk→embed→store→retrieve→generate, and explain when to use RAG vs fine-tuning vs long context.

---

### Lesson 4.1.1 — Concept: Why LLMs Hallucinate and What RAG Fixes

**1. Concept understanding**
- LLMs predict text — they don't "know" your private data
- Hallucination = confident wrong answer
- RAG grounds answers in retrieved text (not perfect, but much better)

**2. Beginner exercise (no code)**  
List 5 questions your LLM from Module 02 **cannot** answer about a fake company. Then explain how RAG would help each.

**3. Real-world use case**  
Healthcare admin bot must cite patient education pamphlets — not invent medical advice.

**4. Production consideration**  
Always show **sources** in UI so users can verify.

**5. Enterprise usage**  
Compliance teams require audit trail: which document chunks supported each answer.

**Deliverable:** One-page `docs/why-rag.md` in your repo

---

### Lesson 4.1.2 — Concept: RAG vs Fine-Tuning vs Long Context

**1. Concept understanding**
| Approach | Best when | Weak when |
|----------|-----------|-----------|
| **RAG** | Knowledge changes often; need citations | Very small static corpus maybe overkill |
| **Fine-tuning** | Fixed style/format; domain language | Knowledge updates require re-training |
| **Long context** | Single huge doc fits in window | Expensive; "lost in middle"; no granular citations |

**2. Beginner decision tree (draw on paper)**  
Start with RAG → if style wrong, tune prompts → if still failing, consider fine-tune.

**3. Interview answer**  
*"We chose RAG because policies update monthly and legal requires source citations."*

---

### Lesson 4.1.3 — Beginner Coding: Load a PDF and Ask Questions (Naive RAG)

**Prerequisites check:** Can you read a file in Python? (Module 01)

**Concept:** Simplest RAG = dump whole PDF in prompt (works only for small docs)

**Step-by-step**
1. `pip install pymupdf` (or pypdf)
2. Extract text from 5-page PDF
3. Build prompt: `"Context:\n{text}\n\nQuestion: {q}\nAnswer:"`
4. Call OpenAI from Module 02 `LLMClient`
5. Print answer

**Common error:** PDF text garbled — scanned PDFs need OCR (Document Intelligence in Module 08)

**Mini project:** CLI `ask_policy.py "How many PTO days?"`

**Production gap:** Whole PDF exceeds context window for real docs — leads to Topic 4.2 chunking

---

### Lesson 4.1.4 — Concept: The Full RAG Pipeline Diagram

**Architecture (describe and draw)**
```
[Documents] → INGEST → [Raw text]
                ↓
            CHUNK → [Pieces ~500 tokens]
                ↓
            EMBED → [Vectors]
                ↓
            STORE → [Vector DB]
                
[User question] → EMBED query → SEARCH → [Top K chunks]
                ↓
            PROMPT = system + chunks + question
                ↓
            LLM → [Answer + citations]
```

**Exercise:** Draw this from memory; label each box with Python file you will create

---

### Lesson 4.1.5 — Intermediate: Document Ingestion (PDF, TXT, HTML)

**Concepts**
- Ingestion = getting text into your system reliably
- Formats: PDF, DOCX, HTML, Markdown, API JSON
- `Unstructured.io` or `PyMuPDF` for extraction
- Store `doc_id`, `source`, `page`, `ingested_at` metadata

**Coding**
```python
def ingest_pdf(path: str) -> list[dict]:
    """Return list of {text, page, source} records."""
```

**Real-world:** Nightly job ingests new Confluence exports

**Production:** Idempotent ingestion — don't duplicate chunks on re-run

---

### Lesson 4.1.6 — Practical: Metadata Schema Design

**Concepts**
- Metadata enables filtering: `department=HR`, `year=2026`
- Enterprise: `tenant_id`, `acl_group`, `classification=confidential`

**Exercise:** Design JSON schema for chunk metadata; justify each field

**Enterprise:** User only retrieves chunks their AD groups allow (Module 07 deep dive)

---

### Lesson 4.1.7 — Intermediate: Building the RAG Prompt Template

**Connect Module 03 prompts with retrieval context**

```jinja2
System: You answer ONLY using the provided context. If unsure, say "I don't know."
Cite sources as [doc_id:page].

Context:
{% for chunk in chunks %}
[{{ chunk.id }}] {{ chunk.text }}
{% endfor %}

User question: {{ question }}
```

**Exercise:** Test with irrelevant context — model should abstain

---

### Lesson 4.1.8 — Production: Citations and Source Attribution in API

**FastAPI endpoint**
```python
@app.post("/v1/rag/query")
def rag_query(req: RAGRequest) -> RAGResponse:
    # returns answer: str, sources: list[SourceChunk], confidence: float
```

**UI contract:** Frontend shows clickable citations

**Interview:** "How do you reduce hallucinations in RAG?" → citations + abstain + eval

---

### Lesson 4.1.9 — Framework Overview: LangChain vs LlamaIndex vs Haystack

**Beginner explanation**
- **Frameworks** = pre-built RAG plumbing (loaders, splitters, retrievers)
- **LangChain** — most popular, large ecosystem
- **LlamaIndex** — data/index focused
- **Haystack** — enterprise search roots

**Decision for course:** Pick **one** (LangChain or LlamaIndex) for consistency; know others exist for interviews

**Enterprise:** Teams often wrap frameworks behind internal platform API

---

### Topic 4.1 — Projects & Assessments

**Beginner exercise:** Naive full-PDF Q&A on 5-page doc  
**Mini project:** `/v1/rag/query` returning answer + source strings  
**Assignment:** Ingest 3 PDFs; metadata in JSON sidecar  
**Enterprise scenario:** Legal firm — every answer must include clause ID  
**Interview:** Whiteboard RAG for internal wiki  
**Portfolio:** Architecture diagram in README  
**Checkpoint:** Can you explain each pipeline stage without looking?

---

# Topic 4.2 — Chunking & Embeddings: Turning Text Into Searchable Pieces

## Beginner Explanation

A 500-page manual cannot fit in one prompt. **Chunking** splits documents into small pieces. **Embeddings** convert each piece into numbers (vectors) so computers can find **similar meaning**.

**Analogy:** Chunking = cutting a textbook into index cards. Embeddings = assigning each card a GPS coordinate in "meaning space." Similar cards sit close together.

## Why Companies Use This

Bad chunking causes **50%+ of production RAG failures** — right answer exists in doc but wrong chunk retrieved. Engineers who tune chunking + embeddings get hired over demo builders.

## Learning Outcome

You will compare chunk strategies with eval data, select embedding models, and document optimal config.

---

### Lesson 4.2.1 — Concept: What Is a Text Chunk?

**1. Concept** — Chunk = contiguous text block, typically 256–1024 tokens  
**2. Why size matters** — Too small: no context. Too large: irrelevant noise  
**3. Overlap** — Repeat last 50 tokens of previous chunk so sentences aren't cut mid-thought  

**Exercise:** Manually split one page into 3 chunks by hand; note where cuts feel wrong

---

### Lesson 4.2.2 — Concept: Fixed vs Recursive vs Semantic Chunking

| Type | How | When |
|------|-----|------|
| Fixed | Every N characters | Simple demos only |
| Recursive | Split by paragraphs → sentences | General purpose default |
| Semantic | Split when meaning shifts | Heterogeneous docs |
| Structure-aware | Respect headings, tables | Legal, technical manuals |

**Beginner coding:** LangChain `RecursiveCharacterTextSplitter(chunk_size=512, overlap=50)`

---

### Lesson 4.2.3 — Concept: What Are Embeddings?

**1. Concept** — Embedding model maps text → vector (e.g., 1536 numbers)  
**2. Similar meaning → vectors close together** (cosine similarity)  
**3. Not keyword match** — "PTO policy" matches "vacation days" semantically  

**Analogy:** Embeddings are like translating sentences into coordinates on a map of ideas.

**Exercise:** OpenAI embeddings API on two similar and two dissimilar sentences; observe distance (optional code)

---

### Lesson 4.2.4 — Beginner Coding: Generate Your First Embeddings

```python
from openai import OpenAI
client = OpenAI()
resp = client.embeddings.create(
    model="text-embedding-3-small",
    input=["vacation policy", "holiday schedule"],
)
vector = resp.data[0].embedding
print(len(vector))  # dimension
```

**Deliverable:** Script `embed_demo.py`

---

### Lesson 4.2.5 — Intermediate: Embedding Model Selection

| Model | Pros | Cons |
|-------|------|------|
| OpenAI text-embedding-3-small | Easy, quality | Cost, data leaves VPC |
| BGE / E5 (open source) | Self-host, free | Ops burden |
| Cohere embed | Strong multilingual | Vendor lock |

**Enterprise:** Air-gapped → open-source on private GPU

**Exercise:** Same 10 queries with two models; compare retrieval hit rate manually

---

### Lesson 4.2.6 — Intermediate: Parent-Child Chunking

**Concept** — Index small chunks for search; retrieve parent paragraph for LLM context  
**Why** — Precision of small search + context of large read  

**Real-world:** Search sentence-level; feed LLM full section

---

### Lesson 4.2.7 — Advanced: Chunking Grid Search with Eval

**Method**
1. Try chunk sizes 256, 512, 1024
2. Run 20 golden questions
3. Record faithfulness or manual hit@3
4. Plot in `docs/chunking-experiments.md`

**Production:** Winner config checked into Git — not tuned only on laptop

---

### Lesson 4.2.8 — Production: Embedding Cache and Re-Embed Strategy

**Concepts**
- Cache chunk hash → skip unchanged re-embeds
- Version embedding model in index metadata
- Migration plan when changing models (re-index all)

**Enterprise:** 1M chunks re-embed = budget item — plan ahead

---

### Topic 4.2 — Mini Project
**Chunk Lab:** Tool that splits sample PDF at 3 sizes; prints chunks; human scores readability 1–5

---

# Topic 4.3 — Vector Databases & Semantic Search

## Beginner Explanation

You have thousands of embedding vectors. You need a **vector database** to store them and find **nearest neighbors** fast when a user asks a question.

**Analogy:** Traditional database finds exact match ("WHERE title = 'X'"). Vector DB finds **closest meaning** ("documents most like this question").

## Why Companies Use This

Vector DB skills = **+9–10% salary premium**. Every enterprise RAG system uses one: Pinecone, pgvector, Weaviate, Azure AI Search, etc.

## Learning Outcome

You will explain semantic vs keyword search, store embeddings, query similar documents, and add metadata filters.

---

### Lesson 4.3.1 — Concept: What Problem Vector Databases Solve

**1. Problem** — Brute-force compare query to 1M vectors = too slow  
**2. Solution** — Approximate nearest neighbor (ANN) indexes (HNSW, IVF)  
**3. Tradeoff** — Speed vs 100% recall accuracy  

**Beginner:** You don't implement HNSW — you configure it in Pinecone/pgvector

---

### Lesson 4.3.2 — Concept: Traditional Search vs Semantic Search

| Keyword (BM25) | Semantic (vector) |
|----------------|-------------------|
| Matches exact words | Matches meaning |
| Fails on synonyms | Handles paraphrase |
| Great for SKUs, IDs | Great for natural language questions |

**Exercise:** Query "laptop warranty" — keyword misses "notebook guarantee" — semantic hits it

---

### Lesson 4.3.3 — Concept: Similarity Search (Cosine Similarity)

**Concept** — Compare query vector to stored vectors; rank by cosine similarity score  
**Threshold** — Below 0.7? Maybe no good match — abstain (Module 07)

**Coding (numpy intuition, optional):** `similarity = dot(a,b) / (norm(a)*norm(b))`

---

### Lesson 4.3.4 — Beginner: Store Embeddings in a JSON File (Toy Vector Store)

**Purpose:** Understand retrieval logic **before** managed DB complexity

```python
# chunks.json: [{id, text, embedding: [...]}]
def search(query_embedding, top_k=5):
    scores = [(cosine_sim(query_embedding, c["embedding"]), c) for c in chunks]
    return sorted(scores, reverse=True)[:top_k]
```

**Limitation:** Doesn't scale — motivates real vector DB

---

### Lesson 4.3.5 — Intermediate: Introduction to pgvector (Postgres Extension)

**Why pgvector first** — You likely know SQL; runs locally; free; enterprise uses Postgres

**Steps**
1. Docker Postgres with pgvector image
2. Create table `chunks (id, text, embedding vector(1536), metadata jsonb)`
3. Insert 100 chunks
4. Query `ORDER BY embedding <=> query_vector LIMIT 5`

**Deliverable:** `docker-compose.yml` with postgres + pgvector

---

### Lesson 4.3.6 — Intermediate: Introduction to Pinecone (Managed Vector DB)

**When managed** — Startup wants speed; no DB ops team  
**Concepts** — Index, namespace, upsert, query  
**Free tier** for learning  

**Exercise:** Same 100 chunks in Pinecone; compare query latency to pgvector

---

### Lesson 4.3.7 — Practical: Building Semantic Search End-to-End

**Pipeline**
1. User question → embed query
2. Vector search top K=10
3. Pass chunks to RAG prompt (Topic 4.1)
4. Return answer + source IDs

**Mini project:** `semantic_search.py` CLI — question in, top 3 chunks out

---

### Lesson 4.3.8 — Intermediate: Metadata Filtering

**Concept** — `filter={"tenant_id": "acme", "department": "HR"}` before/after vector search  
**Why** — Security + relevance  

**Coding:** Query with filter; prove Tenant A never sees Tenant B docs (test required)

---

### Lesson 4.3.9 — Advanced: Hybrid Search (BM25 + Vector + RRF)

**Concept**
1. Run keyword search → top 50
2. Run vector search → top 50
3. **Reciprocal Rank Fusion (RRF)** merge results

**Why enterprises need it** — Users search product SKUs (keyword) and natural language (semantic)

**Target:** Hybrid beats pure vector ≥15% on keyword-heavy eval set

---

### Lesson 4.3.10 — Production: Index Sizing, Backups, Multi-Tenant Namespaces

**Production topics**
- Separate indexes: dev / staging / prod
- Namespace per customer (B2B SaaS)
- Backup strategy before re-index
- p95 retrieval latency < 200ms target

**Enterprise:** Load test with Locust — 50 concurrent queries

---

### Lesson 4.3.11 — Enterprise: Multi-Tenant AI Search Architecture

**Describe diagram**
```
Tenant A docs → namespace A ┐
Tenant B docs → namespace B ├→ Shared embedding service
Tenant C docs → namespace C ┘
Query includes tenant_id from JWT → filter enforced every request
```

**Interview:** "Design multi-tenant vector storage for 500 customers"

---

### Topic 4.3 — Assignment
Vector DB abstraction interface: `upsert()`, `search()` with pgvector AND one cloud option; hybrid search optional stretch goal.

---

# Topic 4.4 — Retrieval Optimization: Reranking, Caching, Query Intelligence

## Beginner Explanation

First retrieval pass gets **approximate top 50** chunks. **Reranking** uses a smarter model to pick the best 5. **Caching** stores answers to repeated questions to save money and time.

## Why Companies Use This

Senior RAG engineers differentiate here — demo RAG stops at vector search; **production RAG** adds rerank + cache + query routing.

## Learning Outcome

You will implement two-stage retrieval, semantic cache, and measure cost/latency improvement.

---

### Lesson 4.4.1 — Concept: Two-Stage Retrieve → Rerank

**Stage 1:** Fast bi-encoder (embeddings) → top 50  
**Stage 2:** Slow cross-encoder reranker → top 5  
**Analogy:** Cast wide net, then expert picks best fish

---

### Lesson 4.4.2 — Beginner: Why Retrieval Returns Wrong Chunks

**Debug checklist**
- Chunk too big/small?
- Wrong embedding model?
- Query ambiguous?
- Stale index?

**Exercise:** Log retrieved chunks for 5 failed queries; diagnose root cause

---

### Lesson 4.4.3 — Intermediate: Cohere Rerank API (or bge-reranker)

**Coding:** Send query + 50 doc texts to reranker; receive ordered list  
**Metric:** nDCG@10 or manual before/after on 20 questions

---

### Lesson 4.4.4 — Intermediate: Query Transformation (HyDE, Multi-Query)

**HyDE** — LLM generates hypothetical answer; embed *that* for search  
**Multi-query** — LLM generates 3 search queries; merge results  

**When:** Vocabulary mismatch between user and docs

---

### Lesson 4.4.5 — Intermediate: Semantic Cache (Redis / GPTCache)

**Concept** — Embed question; if similar to prior question (>0.95), return cached answer  
**Invalidate** when source documents update  

**Production metric:** Cache hit rate on dashboard

---

### Lesson 4.4.6 — Advanced: Contextual Compression & Lost-in-the-Middle

**Problem** — LLM ignores info in middle of long context  
**Fix** — Compress chunks; put most relevant at start/end; limit chunk count

---

### Lesson 4.4.7 — Production: Cost/Latency Dashboard

**Log per query:** embed ms, search ms, rerank ms, LLM ms, $ cost  
**Target:** Reduce $/1K queries 30% with cache + routing (preview Module 11 FinOps)

---

### Topic 4.4 — Mini Project
Add reranker + cache to Enterprise RAG; document before/after metrics in README.

---

# Topic 4.5 — Advanced RAG Patterns (Optional Path to Enterprise)

## Beginner Explanation

Most jobs need **solid vector RAG first**. GraphRAG, agentic RAG, and multimodal RAG are **advanced** patterns for complex corpora — learn after Topic 4.1–4.4 work well.

## Why Companies Use This

Microsoft GraphRAG for intelligence analysis; agents that call RAG as a tool; image-heavy manuals need multimodal RAG.

## Learning Outcome

You will know when **not** to over-engineer, and when graphs or agents justify complexity.

---

### Lesson 4.5.1 — Concept: GraphRAG vs Vector-Only (When to Add Complexity)

**Start vector-only** → eval fails on entity questions ("Who reports to CEO?") → consider graph

---

### Lesson 4.5.2 — Concept: Entities, Relations, Knowledge Graphs Intro

**Nodes:** people, products, policies  
**Edges:** reports_to, belongs_to, references  

**Tools:** Neo4j basics (awareness)

---

### Lesson 4.5.3 — Concept: RAG as an Agent Tool (Bridge to Module 05)

```python
def search_knowledge_base(query: str) -> str:
    """Tool the agent calls — wraps your RAG pipeline."""
```

**This connects Module 04 → Module 05 directly**

---

### Lesson 4.5.4 — Advanced: Self-RAG and Corrective RAG (Conceptual)

**Self-RAG** — Model critiques its retrieval need  
**CRAG** — Correct when retrieval quality low  

**Production:** Research patterns — implement after baseline RAG stable

---

### Lesson 4.5.5 — Enterprise Decision Document

**Deliverable:** ADR — "Why we chose vector-only vs GraphRAG for our capstone" with eval evidence

---

# Module 04 — Capstone: Enterprise RAG Assistant

## Project Progression (Ascending Complexity)

| Phase | What you build |
|-------|----------------|
| **Week 16** | Naive PDF Q&A |
| **Week 17** | Chunk + embed + pgvector search |
| **Week 18** | Full RAG API with citations |
| **Week 19** | Hybrid search OR reranker |
| **Week 20** | Eval score + README metrics + deploy |

## Required Deliverables

- [ ] `POST /v1/rag/query` → `{ answer, sources[], confidence }`
- [ ] Ingest at least 3 PDFs with metadata
- [ ] Vector DB (pgvector or Pinecone)
- [ ] Prompt template with abstention rule
- [ ] **Ragas faithfulness ≥ 0.80** on 30-question golden set (stretch 0.85)
- [ ] Architecture diagram in README
- [ ] Deployed URL or Docker one-command run
- [ ] `docs/chunking-experiments.md` with chosen config

## Interview Talking Points

1. Walk through pipeline diagram end-to-end  
2. "How did you choose chunk size?" — show data  
3. "How prevent cross-tenant leak?" — metadata filters  
4. "How know it works?" — Ragas + golden set  

---

## Module 04 — Master Checklist Before Module 05

| Question | Yes / No |
|----------|----------|
| Can I explain RAG in 60 seconds to a non-technical recruiter? | |
| Does my API return source citations? | |
| Did I measure quality (not just "looks good")? | |
| Can I debug a wrong answer (chunk? embed? prompt?)? | |
| Is project on GitHub with diagram? | |

**Only proceed to Module 05 (Agents) when RAG works reliably.** Agents multiply failures — fix retrieval first.

---

*Next: [module-05-agentic-ai.md](./module-05-agentic-ai.md) — Agents use RAG as a tool*
