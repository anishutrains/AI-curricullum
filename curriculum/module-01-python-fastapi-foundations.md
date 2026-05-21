# Module 01 — Python & FastAPI Foundations

---

## Topic 1.1: Production Python for AI Services

### 1. Topic Name
Production Python for AI Services

### 2. Why This Topic Matters in USA Job Market
95%+ of AI Engineer JDs require Python. Employers reject candidates who only know notebooks—production async, typing, and testing are baseline.

### 3. Which Job Roles This Topic Helps With
AI Engineer, Generative AI Engineer, AI Application Developer, AI Platform Engineer, LLMOps Engineer

### 4. Learning Objectives
- Write async Python suitable for I/O-bound LLM calls
- Use type hints, Pydantic v2, and structured error handling
- Structure packages for testability and CI

### 5. Lessons/Subtopics
- Python 3.11+ async/await patterns
- Pydantic models for API contracts
- Environment configuration (12-factor)
- Logging (structlog) vs print
- pytest + pytest-asyncio

### 6. Hands-on Labs
**Lab 1.1:** Build async HTTP client wrapper with retries, timeouts, and circuit breaker stub.

### 7. Enterprise Projects
Package `ai_service_core` with config management, health endpoint, and structured logs—template for all future modules.

### 8. Portfolio Projects
Reusable FastAPI starter repo used in later RAG/agent projects.

### 9. Interview Preparation
- "How do you handle long-running LLM calls in Python?"
- "Explain async vs threading for OpenAI API calls."

### 10. Real-world Use Cases
Backend for copilots, batch embedding jobs, webhook handlers for agent events.

### 11. Tools & Technologies
Python 3.11+, Pydantic, pytest, structlog, httpx, uvicorn

### 12. Common Mistakes
- Blocking event loop with sync SDK calls
- No timeout on external APIs
- Secrets in code instead of env/vault

### 13. Industry Best Practices
- 12-factor config; never commit `.env`
- Pin dependencies in `pyproject.toml` / lockfile
- Pre-commit: ruff, mypy, pytest

### 14. Capstone Deliverables
`ai-engineer-starter` GitHub repo: linted, tested, Dockerized FastAPI skeleton.

---

## Topic 1.2: FastAPI for LLM Microservices

### 1. Topic Name
FastAPI for LLM Microservices

### 2. Why This Topic Matters
FastAPI dominates AI backend JDs. Streaming SSE, dependency injection, and OpenAPI docs are expected day-one skills.

### 3. Job Roles
AI Application Developer, Generative AI Engineer, AI Integration Engineer

### 4. Learning Objectives
- Build REST + SSE streaming endpoints
- Implement dependency injection for LLM clients
- Generate OpenAPI specs for frontend teams

### 5. Lessons/Subtopics
- Routers, middleware, CORS
- SSE streaming responses
- Background tasks and task queues intro
- API versioning (`/v1/`)
- Rate limiting middleware

### 6. Hands-on Labs
**Lab 1.2:** `/v1/chat` POST with streaming SSE; `/health` and `/ready` probes.

### 7. Enterprise Projects
API gateway pattern: auth middleware stub, request ID propagation, latency headers.

### 8. Portfolio Projects
Documented OpenAPI + Postman collection in portfolio README.

### 9. Interview Preparation
- Design a chat API with streaming—endpoints, auth, error codes
- "How would you version breaking prompt schema changes?"

### 10. Real-world Use Cases
Customer support backend, internal copilot API, mobile app AI proxy.

### 11. Tools & Technologies
FastAPI, uvicorn, SSE-Starlette, Pydantic, OpenAPI

### 12. Common Mistakes
- No request ID for distributed tracing
- Returning raw LLM errors to clients (leak prompts)
- Missing input validation on user messages

### 13. Industry Best Practices
- Problem+json error format
- Pagination for conversation history
- Idempotency keys for paid operations

### 14. Capstone Deliverables
Deployed FastAPI service (Railway/Fly.io/AWS) with public health URL.

---

## Topic 1.3: Docker, Git & CI Foundations

### 1. Topic Name
Docker, Git & CI Foundations for AI

### 2. Why This Topic Matters
"No Docker on resume" filters out candidates at mid+ levels. AI CI must run evals, not just unit tests.

### 3. Job Roles
AI Platform Engineer, LLMOps Engineer, Enterprise AI Engineer

### 4. Learning Objectives
- Multi-stage Dockerfiles for Python AI services
- GitHub Actions: lint, test, build image
- Semantic versioning for API releases

### 5. Lessons/Subtopics
- Dockerfile best practices (non-root, slim images)
- docker-compose for local dev (API + Redis + Postgres)
- Git branching (trunk-based intro)
- GitHub Actions workflows
- Container registry (GHCR, ECR)

### 6. Hands-on Labs
**Lab 1.3:** CI pipeline: ruff → pytest → docker build → push on `main`.

### 7. Enterprise Projects
Signed images, SBOM awareness, dependency scanning (Trivy) in CI.

### 8. Portfolio Projects
README badge: CI passing, Docker pull instructions.

### 9. Interview Preparation
- "Walk through your CI/CD for an AI feature."
- "How do you manage secrets in CI?"

### 10. Real-world Use Cases
Every production AI deployment starts here.

### 11. Tools & Technologies
Docker, docker-compose, GitHub Actions, Trivy, GHCR

### 12. Common Mistakes
- Giant images with CUDA when only calling APIs
- Running evals only manually before release
- No `.dockerignore` (slow builds, leaked data)

### 13. Industry Best Practices
- Separate build and runtime stages
- Cache pip layers in Docker
- Tag images with git SHA

### 14. Capstone Deliverables
Green CI on starter repo; one-page runbook: build, deploy, rollback.

---

*Next: [module-02-llm-apis-foundations.md](./module-02-llm-apis-foundations.md)*
