# Module 04 — RAG Systems (Advanced)

---

## Topic 4.1: RAG Architecture Fundamentals

### 1. Topic Name
RAG Architecture Fundamentals

### 2. Why This Topic Matters
RAG is +11% salary premium skill; 80%+ enterprise GenAI JDs mention retrieval. This is the #1 differentiator vs tutorial developers.

### 3. Job Roles
RAG Engineer, Generative AI Engineer, Enterprise AI Engineer, Applied AI Engineer

### 4. Learning Objectives
- Diagram naive vs advanced RAG pipelines
- Implement ingest → chunk → embed → store → retrieve → generate
- Measure faithfulness and relevance

### 5. Lessons/Subtopics
- When RAG vs fine-tuning vs long context
- Ingestion pipelines (PDF, HTML, DOCX, APIs)
- Metadata schema design
- Query transformation (HyDE, multi-query)
- Citation and source attribution
- LangChain vs LlamaIndex vs Haystack comparison

### 6. Hands-on Labs
**Lab 4.1:** End-to-end RAG on 500-page policy PDF with source citations in UI.

### 7. Enterprise Projects
ACL-aware metadata: user only retrieves permitted documents.

### 8. Portfolio Projects
**Enterprise RAG Assistant** (flagship project #1).

### 9. Interview Preparation
- Whiteboard full RAG architecture for internal wiki Q&A
- "How do you reduce hallucinations in RAG?"

### 10. Real-world Use Cases
HR policy bots, legal discovery assist, engineering runbooks.

### 11. Tools & Technologies
LangChain, LlamaIndex, Haystack, Unstructured.io, PyMuPDF

### 12. Common Mistakes
- Chunking entire PDFs as single blocks
- No metadata filtering before vector search
- Skipping evaluation entirely

### 13. Industry Best Practices
- Document lineage IDs in chunks
- Stale content TTL and re-index jobs
- Show citations in UI always

### 14. Capstone Deliverables
RAG API with `/query` returning answer + sources + confidence; Ragas faithfulness ≥0.85 on test set.

---

## Topic 4.2: Chunking & Embedding Strategies

### 1. Topic Name
Chunking & Embedding Strategies

### 2. Why This Topic Matters
Bad chunking causes 50%+ of production RAG failures. Senior interviews drill chunk size, overlap, and structure-aware splitting.

### 3. Job Roles
RAG Engineer, LLM Engineer

### 4. Learning Objectives
- Apply recursive, semantic, and document-structure chunking
- Select embedding models for domain
- Tune chunk size/overlap with eval data

### 5. Lessons/Subtopics
- Fixed vs recursive vs semantic chunking
- Parent-child chunk retrieval
- Embedding models: OpenAI, Cohere, BGE, E5
- Multilingual embeddings
- Dimensionality and index type tradeoffs
- Embedding cache layers

### 6. Hands-on Labs
**Lab 4.2:** Grid search chunk sizes 256–1024; plot MRR@5 vs faithfulness.

### 7. Enterprise Projects
Structure-aware chunking for legal/clinical headers and tables.

### 8. Portfolio Projects
`docs/chunking-experiments.md` with charts and winner config.

### 9. Interview Preparation
- "Your RAG misses table data—what do you change?"
- "Compare OpenAI ada-3 vs open-source embeddings for cost."

### 10. Real-world Use Cases
Technical manuals with code blocks, SEC filings with tables.

### 11. Tools & Technologies
LangChain text splitters, semantic-chunker, sentence-transformers

### 12. Common Mistakes
- Same chunk config for all doc types
- Re-embedding entire corpus daily without change detection
- Ignoring token limits in chunk headers

### 13. Industry Best Practices
- Store chunk hash to skip unchanged re-embeds
- Version embedding model in index metadata
- Human spot-check 20 chunks per corpus

### 14. Capstone Deliverables
Optimal chunk config documented with eval proof.

---

## Topic 4.3: Vector Databases & Hybrid Search

### 1. Topic Name
Vector Databases & Hybrid Search

### 2. Why This Topic Matters
Vector DB skills (+9–10% premium). Enterprises require hybrid BM25 + vector for keyword-heavy queries.

### 3. Job Roles
RAG Engineer, AI Platform Engineer

### 4. Learning Objectives
- Operate Pinecone, Weaviate, pgvector, or Milvus
- Implement hybrid search and metadata filters
- Plan index sizing, namespaces, multi-tenancy

### 5. Lessons/Subtopics
- HNSW vs IVF index concepts (practical level)
- Pinecone / Weaviate / Milvus / pgvector setup
- Azure AI Search hybrid patterns
- BM25 + dense fusion (RRF)
- Namespace per tenant
- Backup and index rebuild strategies

### 6. Hands-on Labs
**Lab 4.3:** Hybrid search beating pure vector on keyword-heavy eval subset by ≥15%.

### 7. Enterprise Projects
Multi-tenant index isolation; per-tenant API keys and quotas.

### 8. Portfolio Projects
Vector DB abstraction supporting 2 backends (e.g., pgvector + Pinecone).

### 9. Interview Preparation
- "Design multi-tenant vector storage."
- "When would you choose pgvector vs managed Pinecone?"

### 10. Real-world Use Cases
E-commerce search, support KB, code search.

### 11. Tools & Technologies
Pinecone, Weaviate, Milvus, pgvector, OpenSearch, Azure AI Search

### 12. Common Mistakes
- No metadata indexes for filter fields
- Single global index for all customers (data leak risk)
- Ignoring embedding dimension mismatches on model change

### 13. Industry Best Practices
- Separate dev/staging/prod indexes
- Load test p95 retrieval latency
- Monitor index size growth and cost

### 14. Capstone Deliverables
Hybrid retriever with filter API; p95 retrieval <200ms on benchmark.

---

## Topic 4.4: Reranking & Retrieval Optimization

### 1. Topic Name
Reranking, Query Routing & Semantic Caching

### 2. Why This Topic Matters
Advanced RAG differentiates senior engineers—rerankers improve precision 20–40%; semantic cache cuts cost 30–50%.

### 3. Job Roles
RAG Engineer, Senior AI Engineer

### 4. Learning Objectives
- Add cross-encoder reranking (Cohere, bge-reranker)
- Implement semantic cache for frequent queries
- Route queries to specialized retrievers

### 5. Lessons/Subtopics
- Two-stage retrieve → rerank
- Cohere Rerank API vs open-source cross-encoders
- Semantic cache (Redis, GPTCache)
- Query classification for router
- Contextual compression
- Lost-in-the-middle mitigation

### 6. Hands-on Labs
**Lab 4.4:** Add reranker; measure nDCG@10 improvement; add cache hit rate metric.

### 7. Enterprise Projects
Cache invalidation on document updates; per-tenant cache keys.

### 8. Portfolio Projects
Cost/latency dashboard: cache hit %, reranker latency.

### 9. Interview Preparation
- "RAG is slow at 2s p95—optimization plan?"
- "Explain two-stage retrieval."

### 10. Real-world Use Cases
High-QPS support bots, repeated FAQ queries.

### 11. Tools & Technologies
Cohere Rerank, sentence-transformers cross-encoder, Redis, GPTCache

### 12. Common Mistakes
- Reranking 1000 docs (budget explosion)
- Cache without invalidation on source updates
- No diversity in retrieved chunks (redundant context)

### 13. Industry Best Practices
- Retrieve top-50, rerank to top-5
- Log cache hits to FinOps dashboard
- MMR for diversity when needed

### 14. Capstone Deliverables
Production retriever with rerank + cache; documented cost savings.

---

## Topic 4.5: Knowledge Graphs & Advanced RAG Patterns

### 1. Topic Name
Knowledge Graphs, GraphRAG & Agentic RAG

### 2. Why This Topic Matters
Microsoft GraphRAG and enterprise knowledge graphs trending for complex corpora (legal, intelligence, R&D).

### 3. Job Roles
RAG Engineer, AI Architect, Applied AI Engineer

### 4. Learning Objectives
- Explain GraphRAG vs vector-only tradeoffs
- Combine graph traversal with vector retrieval
- Integrate RAG as tool inside agents (Module 05 link)

### 5. Lessons/Subtopics
- Entity extraction and relation graphs
- Neo4j / Amazon Neptune basics
- GraphRAG community summaries
- Self-RAG, corrective RAG concepts
- RAG + agent tool pattern
- Multimodal RAG (images in docs)

### 6. Hands-on Labs
**Lab 4.5:** Optional graph layer for entity-centric queries ("Who reports to X?").

### 7. Enterprise Projects
Hybrid Graph+Vector for org chart + policy docs.

### 8. Portfolio Projects
Architecture diagram comparing vector-only vs graph-augmented.

### 9. Interview Preparation
- "When is GraphRAG worth the complexity?"
- "Design RAG for 10M document corpus."

### 10. Real-world Use Cases
M&A due diligence, pharma literature, supply chain knowledge.

### 11. Tools & Technologies
Neo4j, LlamaIndex KnowledgeGraph, Microsoft GraphRAG patterns

### 12. Common Mistakes
- Building graphs when clean metadata filters suffice
- Stale graph edges without refresh pipeline
- Over-engineering for MVP

### 13. Industry Best Practices
- Start vector-only; add graph when eval shows entity failures
- Human-validated ontology for regulated domains

### 14. Capstone Deliverables
Graph-augmented query path OR documented decision why not needed.

---

*Next: [module-05-agentic-ai.md](./module-05-agentic-ai.md)*
