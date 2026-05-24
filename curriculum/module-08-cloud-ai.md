# Module 08 — Cloud AI (AWS, Azure, GCP)
### Zero-to-Hero Track · Weeks 35–38 · Deploying AI on the Cloud (Beginner to Production)

---

## Why This Module Matters

**Why learn this NOW?**  
Your AI app runs on a laptop. Production AI runs on **cloud infrastructure** — secure networks, managed AI APIs, autoscaling, and billing. US employers expect cloud fluency: **Amazon (~711 AI roles), Google (~702), Microsoft (Azure-heavy enterprise)** in 2026 hiring data.

**Why companies need this**
- Enterprise customers require **VPC isolation**, **managed identity**, and **data residency**.
- Cloud-managed AI (Bedrock, Azure OpenAI, Vertex) reduces ops burden vs self-hosting.
- **Terraform + GitHub Actions** = industry standard for reproducible deploys.

**Salary impact:** Cloud AI + K8s skills add **$15K–$35K** premium. AI Infrastructure Engineer roles: **$170K–$250K**.

**Scalability:** Cloud autoscaling, multi-region, and GPU node pools enable 10K+ concurrent users — impossible on a single laptop.

---

## How This Module Fits into the AI Engineering Journey

| Module 07 (Enterprise) | Module 08 (Cloud) | Module 09+ |
|------------------------|-------------------|------------|
| Multi-tenant logic | **Deploy on AWS/Azure/GCP** | Full-stack UI (09) |
| COMPLIANCE.md | **Private endpoints, IAM** | Security hardening (10) |
| LLMOps observability | **CloudWatch, Azure Monitor** | Production architecture (11) |

**Prerequisites:** Modules 01–07 — Docker, FastAPI, RAG, LLMOps, enterprise tenancy concepts.

---

## Job Roles This Module Prepares Students For

Enterprise AI Engineer · Cloud AI Engineer · AI Infrastructure Engineer · AI Platform Engineer · Generative AI Engineer · AI Solutions Architect · LLMOps Engineer

---

## Beginner Skills Students Will Learn

- Explain cloud vs local deployment in plain English
- Create AWS/Azure/GCP free-tier accounts safely
- Deploy FastAPI to one cloud service (App Service / Cloud Run / Lambda)
- Invoke managed LLM API (Bedrock / Azure OpenAI / Vertex)
- Read IAM role basics (who can call what)

## Intermediate Skills Students Will Learn

- Bedrock Knowledge Base or Azure AI Search RAG
- Managed identity / IAM roles (no API keys in config)
- Terraform basics for one AI service
- CloudWatch / Azure Monitor integration

## Advanced Skills Students Will Learn

- Private VPC / Private Link deployments
- Tri-cloud architecture decision (ADR)
- Cost allocation tags and budget alerts

## Production Enterprise Skills Students Will Learn

- Kubernetes + vLLM inference deployment
- GPU node pools and autoscaling
- Load testing and $/1M tokens reporting
- Disaster recovery for vector indexes

---

# Topic 8.1 — AWS AI Stack (Bedrock, SageMaker, Serverless)

## Beginner-Friendly Explanation

**AWS (Amazon Web Services)** = rent computers and AI services in Amazon's data centers.  
**Bedrock** = AWS's managed LLM API (Claude, Llama, etc.) + Knowledge Bases for RAG.  
**Analogy:** Instead of owning a power plant, you plug into the electric grid — pay for what you use.

## Why This Topic Matters in Real Companies

AWS is the largest cloud. Enterprises on AWS use Bedrock for **private, IAM-controlled** AI without sending data to random APIs.

## Problems This Topic Solves

- Manual API keys in code → IAM roles
- Self-managed vector infra → Bedrock Knowledge Bases
- Unpredictable scaling → Lambda + API Gateway serverless

## Learning Outcome

Deploy RAG using Bedrock Knowledge Base OR Bedrock Converse API + document in README with architecture diagram.

---

### Lesson 8.1.1 — Concept: Cloud Fundamentals for AI Beginners

**Core concepts**
| Term | Meaning |
|------|---------|
| **Region** | Geographic data center (us-east-1) |
| **IAM** | Who can access which AWS service |
| **S3** | File storage (PDFs for RAG) |
| **VPC** | Private network for your services |
| **Lambda** | Run code without managing servers |

**Why region matters:** Data residency, latency, model availability.

**Beginner exercise:** Draw: User → API Gateway → Lambda → Bedrock → Response

---

### Lesson 8.1.2 — Concept: AWS Bedrock Overview

**Bedrock provides:**
- Foundation models (Claude 3, Llama 3, Titan)
- **Knowledge Bases** — managed RAG (S3 → embed → vector → retrieve)
- **Converse API** — unified chat interface

**When Bedrock vs OpenAI API:** AWS-native enterprise, IAM, no data leaves AWS contract boundary (verify current terms).

---

### Lesson 8.1.3 — Beginner: First Bedrock Model Invocation (boto3)

```python
import boto3

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
response = bedrock.converse(
    modelId="anthropic.claude-3-haiku-20240307-v1:0",
    messages=[{"role": "user", "content": [{"text": "Hello"}]}],
)
```

**Guided lab:** Invoke Claude via Bedrock from Python; log tokens.

**Security:** Use IAM role on EC2/Lambda — never hardcode AWS keys in Git.

---

### Lesson 8.1.4 — Intermediate: Bedrock Knowledge Base RAG

**Pipeline (managed):**
1. Upload PDFs to S3
2. Create Knowledge Base → OpenSearch Serverless vector store
3. Sync data source
4. Query with `retrieve_and_generate`

**Compare to Module 04:** Same RAG pattern, AWS manages embedding + index.

**Mini project:** 3 PDFs → Bedrock KB → CLI query with citations.

---

### Lesson 8.1.5 — Intermediate: Lambda + API Gateway Serverless AI

**Pattern:** API Gateway → Lambda → Bedrock → JSON response  
**Pros:** Pay per request, auto-scale, no server management  
**Cons:** Cold start latency, 15-min timeout limit

**Guided lab:** Serverless proxy API for Bedrock chat.

---

### Lesson 8.1.6 — Production: IAM Least Privilege and VPC Endpoints

**Anti-pattern:** `"Action": "*", "Resource": "*"` on Bedrock  
**Best practice:** Role per Lambda with only `bedrock:InvokeModel` on specific model ARNs

**VPC endpoint:** Bedrock traffic stays on AWS private network — no public internet.

---

### Lesson 8.1.7 — Production: CloudWatch, Cost Tags, and Alerts

**Metrics:** Lambda duration, Bedrock invocation count, errors  
**Cost allocation tags:** `project=rag-copilot`, `env=prod`  
**Budget alert:** Email when monthly spend > $100

**Enterprise lab:** FinOps dashboard for AWS AI spend.

---

### Topic 8.1 — Interview & Portfolio

**Beginner:** "What is Bedrock?"  
**Intermediate:** "Design RAG on AWS for 10K employees."  
**Senior:** "Bedrock vs self-hosted on EKS tradeoffs?"  
**Portfolio:** AWS architecture diagram in `/docs/aws-architecture.png`

---

# Topic 8.2 — Azure AI Stack (Azure OpenAI, AI Search)

## Beginner-Friendly Explanation

**Azure** = Microsoft's cloud. **Azure OpenAI** = GPT models hosted in *your* Azure subscription — enterprise contract, private networking, Entra ID auth.

**Azure AI Search** = managed search + vector (hybrid RAG) — default stack for Microsoft-heavy enterprises.

## Why This Topic Matters in Real Companies

**70%+ of Fortune 500** use Microsoft 365. Consulting JDs overwhelmingly mention Azure OpenAI + AI Search.

## Problems This Topic Solves

- Public OpenAI API unacceptable for bank compliance → Azure OpenAI with Private Link
- DIY vector search → AI Search hybrid (BM25 + vector)

## Learning Outcome

Deploy hybrid RAG with Azure AI Search + Azure OpenAI; authenticate with managed identity.

---

### Lesson 8.2.1 — Concept: Azure OpenAI vs Public OpenAI API

| Public OpenAI | Azure OpenAI |
|---------------|--------------|
| openai.com API key | Your Azure resource |
| Standard DPA | Enterprise Microsoft contract |
| Shared infra | Dedicated deployment name |
| Good for learning | Good for regulated enterprise |

**Interview:** "Bank client — which do you recommend and why?"

---

### Lesson 8.2.2 — Beginner: Create Azure OpenAI Resource

**Steps (portal):**
1. Create Azure OpenAI resource in approved region
2. Deploy model (gpt-4o-mini)
3. Copy endpoint + key (dev only — use managed identity in prod)

```python
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_KEY"],
    api_version="2024-02-15-preview",
)
```

---

### Lesson 8.2.3 — Intermediate: Azure AI Search Hybrid RAG

**Index fields:** `content`, `content_vector`, `metadata`  
**Hybrid query:** Keyword + vector + semantic ranker  
**Ingestion:** Blob storage → indexer → skillset (chunk + embed)

**Guided lab:** AI Search index with 10 docs; hybrid query from Python.

---

### Lesson 8.2.4 — Intermediate: Managed Identity (No Keys in Config)

**Managed identity** = Azure assigns identity to App Service/Function; no API keys in environment.

**Pattern:** App Service → managed identity → Azure OpenAI + AI Search (RBAC roles assigned)

**Production:** Keys in Key Vault as fallback only.

---

### Lesson 8.2.5 — Advanced: Private Link and Content Safety

**Private Link:** Azure OpenAI not reachable from public internet  
**Content Safety filters:** Block hate, violence, self-harm in API layer

**Enterprise:** Document in COMPLIANCE.md for customer audits.

---

### Lesson 8.2.6 — Production: Deploy FastAPI on App Service

**Flow:** GitHub Actions → build Docker → deploy App Service → env vars from Key Vault  
**Connect Module 07:** Entra ID auth on App Service Easy Auth (optional lab)

**Portfolio:** Azure reference architecture diagram.

---

# Topic 8.3 — GCP Vertex AI & Gemini

## Beginner-Friendly Explanation

**GCP (Google Cloud Platform)** = Google's cloud. **Vertex AI** = Google's managed ML/GenAI platform. **Gemini** = Google's foundation models.

**Best for:** Data-heavy companies, BigQuery analytics, Google Workspace integrations.

## Learning Outcome

Vertex Gemini API call + optional Vector Search RAG + Cloud Run API deploy.

---

### Lesson 8.3.1 — Concept: When to Choose GCP for GenAI

**Choose GCP when:** Company on BigQuery/GCP; strong analytics on AI logs; Gemini-native strategy.  
**Compare:** Tri-cloud ADR — same enterprise scenario on AWS vs Azure vs GCP.

---

### Lesson 8.3.2 — Beginner: Vertex AI Gemini API

```python
import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project="my-project", location="us-central1")
model = GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain RAG in one paragraph.")
```

**Guided lab:** Gemini call from Cloud Shell or local with service account JSON (dev only).

---

### Lesson 8.3.3 — Intermediate: Vertex AI Vector Search

**Managed vector index** — alternative to Pinecone on GCP  
**Pipeline:** GCS docs → embedding → Vector Search index → query

---

### Lesson 8.3.4 — Intermediate: Cloud Run Deployment

**Cloud Run** = serverless containers — ideal for FastAPI AI APIs  
**Deploy:** `gcloud run deploy rag-api --source .`

**Compare:** Lambda vs Cloud Run vs App Service — document tradeoffs in ADR.

---

### Lesson 8.3.5 — Enterprise: VPC-SC, Audit Logs to BigQuery

**VPC Service Controls** — perimeter around AI services  
**BigQuery sink** — analyze AI usage logs at scale

---

# Topic 8.4 — Kubernetes, GPU & Inference Optimization

## Beginner-Friendly Explanation

**Problem:** One server handles 10 users. Ten thousand users need **many copies** of your app — who starts them, health-checks them, routes traffic?

**Kubernetes (K8s)** = orchestrator for containers — auto-restart, scale replicas, load balance.

**Analogy:** Kubernetes is an air traffic controller for container planes.

## Why This Topic Matters

**55%+ senior AI roles** mention Kubernetes. Self-hosted **vLLM** cuts cost at high volume vs API-only.

---

### Lesson 8.4.1 — Concept: What Problem Kubernetes Solves

- Manual server management doesn't scale
- Containers (Docker) package app + dependencies
- K8s schedules containers across machines

**Connect Module 01:** Docker recap — image, container, Dockerfile.

---

### Lesson 8.4.2 — Concept: Kubernetes Architecture (Beginner)

| Component | Role |
|-----------|------|
| **Node** | Machine (VM) running containers |
| **Pod** | One or more containers (smallest unit) |
| **Deployment** | Desired replica count (scale to 3) |
| **Service** | Stable network endpoint for pods |
| **Ingress** | External HTTP routing |

**Exercise:** Label diagram — User → Ingress → Service → Pod → vLLM

---

### Lesson 8.4.3 — Beginner: Deploy Simple FastAPI on k3d/minikube

**k3d** = lightweight local Kubernetes for learning

```yaml
# deployment.yaml (conceptual)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rag-api
spec:
  replicas: 2
  template:
    spec:
      containers:
        - name: api
          image: rag-api:latest
          ports:
            - containerPort: 8000
```

**Guided lab:** 2 replicas; kill one pod; verify traffic continues.

---

### Lesson 8.4.4 — Intermediate: vLLM on Kubernetes

**vLLM** = high-throughput LLM inference server  
**GPU node pool** — nodes with NVIDIA GPUs; schedule model pods with `nodeSelector`

**Readiness probe:** Model load takes minutes — don't mark ready until warm.

---

### Lesson 8.4.5 — Advanced: Autoscaling and Load Testing

**HPA (Horizontal Pod Autoscaler)** — scale replicas on CPU/latency/custom metric  
**Load test:** Locust or `hey` — report RPS, p95 latency, $/1M tokens

**Portfolio:** Load test report in `/docs/inference-benchmark.md`

---

### Lesson 8.4.6 — Enterprise: Inference Gateway Pattern

**Router:** Simple query → cheap API; complex → GPT-4; high volume → self-hosted vLLM  
**Policy-driven routing** — cost vs quality vs data residency

---

# Module 08 — Capstone & Labs

## Week Progression

| Week | Focus |
|------|-------|
| 35 | Cloud basics + one managed LLM call (pick AWS/Azure/GCP) |
| 36 | Managed RAG (Bedrock KB or AI Search or Vertex) |
| 37 | Terraform OR GitHub Actions deploy to cloud |
| 38 | K8s local deploy OR tri-cloud ADR |

## Choose One Cloud Depth Path + One Infra Lab

- [ ] **AWS path:** Bedrock KB + Lambda API + architecture diagram
- [ ] **Azure path:** AI Search hybrid + App Service + managed identity
- [ ] **GCP path:** Gemini + Cloud Run
- [ ] **K8s lab:** FastAPI on k3d with 2 replicas OR vLLM load test doc
- [ ] **Tri-cloud ADR:** 2-page decision doc for sample enterprise scenario

## Interview Talking Points

1. Azure OpenAI vs public OpenAI for regulated client  
2. When self-host vLLM vs use API?  
3. IAM least privilege for Bedrock  
4. K8s components for AI API deployment  

## Master Checklist Before Module 09

| Question | Yes / No |
|----------|----------|
| Did I deploy at least one AI API to a cloud? | |
| Are secrets out of Git (IAM/managed identity)? | |
| Do I have a cloud architecture diagram? | |
| Can I explain Pod vs Deployment vs Service? | |

---

*Next: [module-09-fullstack-ai.md](./module-09-fullstack-ai.md)*
