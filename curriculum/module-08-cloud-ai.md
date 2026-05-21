# Module 08 — Cloud AI (AWS, Azure, GCP)

---

## Topic 8.1: AWS AI Stack (Bedrock, SageMaker)

### 1. Topic Name
AWS AI — Bedrock, SageMaker & Production Patterns

### 2. Why This Topic Matters
Amazon is a top AI employer (~711 roles Q1 2026). AWS Bedrock is standard for enterprise AWS shops.

### 3. Job Roles
Enterprise AI Engineer, AI Infrastructure Engineer, AI Platform Engineer

### 4. Learning Objectives
- Deploy RAG using Bedrock Knowledge Bases
- Invoke Claude/Llama via Bedrock Converse API
- Understand SageMaker endpoints for custom models

### 5. Lessons/Subtopics
- Bedrock models and Knowledge Bases
- IAM roles and VPC endpoints
- S3 ingestion pipelines
- Lambda + API Gateway for serverless AI
- Cost allocation tags
- CloudWatch integration

### 6. Hands-on Labs
**Lab 8.1:** Bedrock Knowledge Base RAG + Lambda API proxy.

### 7. Enterprise Projects
Private VPC Bedrock deployment; no public internet for inference.

### 8. Portfolio Projects
AWS architecture diagram (Lucid/ draw.io) in repo.

### 9. Interview Preparation
- "Design RAG on AWS for 10K employees."
- "Bedrock vs self-hosted on EKS tradeoffs."

### 10. Real-world Use Cases
AWS-native enterprises, gov cloud variants.

### 11. Tools & Technologies
Bedrock, boto3, SageMaker, EKS, Terraform AWS provider

### 12. Common Mistakes
- Over-permissive IAM `*` on Bedrock
- No VPC endpoints (data exfil concern)
- Ignoring cross-region model availability

### 13. Industry Best Practices
- Least-privilege IAM per service
- Infrastructure as Code (Terraform)
- Multi-AZ for API layer

### 14. Capstone Deliverables
One AWS-deployed service OR Terraform module with README apply steps.

---

## Topic 8.2: Azure AI Stack (Azure OpenAI, AI Search)

### 1. Topic Name
Azure AI — OpenAI, AI Search & Copilot Patterns

### 2. Why This Topic Matters
Microsoft-heavy enterprises dominate consulting JDs; Azure OpenAI + AI Search is the default enterprise RAG stack.

### 3. Job Roles
Enterprise AI Engineer, AI Solutions Engineer, AI Consultant

### 4. Learning Objectives
- Deploy Azure OpenAI with private endpoints
- Build hybrid search in Azure AI Search
- Integrate Entra ID authentication

### 5. Lessons/Subtopics
- Azure OpenAI deployments and quotas
- Azure AI Search indexes and skillsets
- Document Intelligence for ingestion
- Managed identity authentication
- Copilot Studio overview
- Content safety filters

### 6. Hands-on Labs
**Lab 8.2:** Azure AI Search hybrid RAG + FastAPI on App Service.

### 7. Enterprise Projects
Private Link end-to-end; customer-managed keys option documented.

### 8. Portfolio Projects
Azure reference architecture for enterprise RAG.

### 9. Interview Preparation
- "Azure OpenAI vs public OpenAI API for bank client?"
- "AI Search skillset pipeline design."

### 10. Real-world Use Cases
M365 organizations, regulated finance on Azure.

### 11. Tools & Technologies
Azure OpenAI, AI Search, Document Intelligence, App Service, Terraform Azure

### 12. Common Mistakes
- API keys in app settings instead of managed identity
- No quota/rate limit planning
- Skipping content safety configuration

### 13. Industry Best Practices
- Hub-spoke networking for AI services
- Cost alerts on token usage
- Align with Microsoft Well-Architected Framework

### 14. Capstone Deliverables
Azure deployment guide OR multi-cloud comparison ADR.

---

## Topic 8.3: GCP Vertex AI

### 1. Topic Name
Google Cloud Vertex AI & Gemini Enterprise

### 2. Why This Topic Matters
Google (~702 AI roles); Gemini-native shops and data-heavy GCP customers need Vertex skills.

### 3. Job Roles
AI Engineer, AI Platform Engineer, Generative AI Engineer

### 4. Learning Objectives
- Use Vertex AI Gemini API and embeddings
- Deploy models on Vertex endpoints
- Integrate with BigQuery for analytics on AI logs

### 5. Lessons/Subtopics
- Vertex AI Studio vs production APIs
- Gemini Pro/Flash selection
- Vector Search on Vertex
- GCS document pipelines
- Workload identity for GKE
- Model Garden open models

### 6. Hands-on Labs
**Lab 8.3:** Vertex RAG corpus + Cloud Run API.

### 7. Enterprise Projects
VPC-SC perimeter for AI services; audit logs to BigQuery.

### 8. Portfolio Projects
GCP terraform snippet for AI service.

### 9. Interview Preparation
- "When GCP over AWS for GenAI?"
- "Vertex Vector Search vs Pinecone."

### 10. Real-world Use Cases
Analytics-heavy companies, Google Workspace integrations.

### 11. Tools & Technologies
Vertex AI, Cloud Run, GKE, Terraform GCP, BigQuery

### 12. Common Mistakes
- Confusing AI Studio experiments with prod config
- No quota project setup
- Ignoring region for data residency

### 13. Industry Best Practices
- Service accounts per environment
- Centralized logging sink
- Cost budget alerts

### 14. Capstone Deliverables
Tri-cloud ADR: which cloud for sample enterprise scenario.

---

## Topic 8.4: Kubernetes, GPU & Inference Optimization

### 1. Topic Name
Kubernetes, GPU Infrastructure & Inference Optimization

### 2. Why This Topic Matters
55%+ senior roles mention K8s; CUDA +12% premium; vLLM/Ollama for cost control at scale.

### 3. Job Roles
AI Infrastructure Engineer, AI Platform Engineer, LLMOps Engineer

### 4. Learning Objectives
- Deploy vLLM on Kubernetes with autoscaling
- Understand GPU node pools and scheduling
- Optimize inference: batching, quantization, caching

### 5. Lessons/Subtopics
- K8s deployments, HPA, ingress for AI APIs
- GPU node selectors and fractions
- vLLM throughput tuning
- Ollama for dev; vLLM for prod
- Serverless vs dedicated GPU economics
- TensorRT-LLM mention (awareness)

### 6. Hands-on Labs
**Lab 8.4:** vLLM on local k3d/minikube with load test (hey/locust).

### 7. Enterprise Projects
Inference gateway routing: cloud API vs self-hosted by policy.

### 8. Portfolio Projects
Load test report: RPS, p95 latency, $/1M tokens.

### 9. Interview Preparation
- "Scale self-hosted Llama to 100 RPS—architecture?"
- "GPU cost optimization strategies."

### 10. Real-world Use Cases
High-volume internal copilots, air-gapped inference.

### 11. Tools & Technologies
Kubernetes, vLLM, Ollama, Helm, NVIDIA device plugin, Locust

### 12. Common Mistakes
- No readiness probes on model pods (slow startup)
- Single replica on GPU workload
- Ignoring cold start in autoscaling

### 13. Industry Best Practices
- Separate embedding and generation clusters
- Spot instances for batch; on-demand for API
- Model warm-up in readiness probe

### 14. Capstone Deliverables
K8s manifests OR load test doc proving inference SLO.

---

*Next: [module-09-fullstack-ai.md](./module-09-fullstack-ai.md)*
