# AI Resume & Portfolio Strategy

## Resume Structure (1 Page)

```
NAME | email | linkedin.com/in/you | github.com/you | City, ST (or "Remote, US")

SUMMARY
2 lines: X years SWE + production GenAI. Shipped [RAG/agents] with [metric].
Target: Generative AI Engineer | RAG | Agentic AI

TECHNICAL SKILLS
Languages: Python, TypeScript, SQL
AI: LangChain, LangGraph, RAG, OpenAI/Anthropic APIs, vector DBs (Pinecone/pgvector)
Ops: FastAPI, Docker, K8s, Terraform, Langfuse, Ragas, GitHub Actions
Cloud: AWS Bedrock | Azure OpenAI (pick primary)

EXPERIENCE
[Company] — [Title] — [Dates]
• Built [system] serving [N] users; reduced [latency/cost] by X%
• Implemented RAG with faithfulness 0.87 on 100-case eval suite
• Deployed agent workflow with LangGraph; 99.5% tool success rate

PROJECTS (if thin experience)
Enterprise RAG Assistant | github.com/... | [Live Demo]
• Hybrid search + reranking; p95 retrieval 180ms; $0.02/query

EDUCATION
[Degree] — optional if strong projects

CERTIFICATIONS
Azure AI Engineer Associate (AI-102), 2026
```

## Rules

- **Lead with impact metrics**, not course names
- **No** "Completed Andrew Ng" as headline item
- **Yes** "Faithfulness 0.87, deployed on AWS, 2K queries/day test load"
- Tailor keywords from target JD (RAG, LangGraph, Bedrock) — honestly

## GitHub Portfolio

### Pin 3 Repos Only

1. **Flagship capstone** — full enterprise checklist
2. **RAG or agent specialist** — deepest technical work
3. **Supporting** — LLMOps or full-stack UI

### README Template (Above the Fold)

```markdown
# Project Name
[![CI](badge)](link) ![Faithfulness](0.87) ![p95](180ms)

> One-sentence value prop.

[Demo GIF](link) | [Live](url) | [Architecture](docs/architecture.md)

## Metrics
| Metric | Value |
|--------|-------|
| Faithfulness | 0.87 |
| p95 latency | 180ms |
| Cost / 1K queries | $2.10 |

## Stack
FastAPI · LangGraph · Pinecone · Langfuse · AWS

## Quick Start
docker compose up
```

## LinkedIn Optimization

**Headline formula:**
`Generative AI Engineer | RAG & Agentic Systems | Python · LangGraph · AWS · Ex-[Company]`

**Featured section:** Link to top 2 GitHub repos + capstone Loom

**About (3 paragraphs):**
1. What you build (production RAG/agents)
2. Proof (metrics, deployment)
3. What you're looking for (role types, remote OK)

**Activity:** 1 technical post/week during job search (build in public)

## Referral Packet (Send to Contacts)

- 3-bullet project summary with metrics
- Link to 90-second Loom
- Specific ask: "Intros to teams building production LLM features"
