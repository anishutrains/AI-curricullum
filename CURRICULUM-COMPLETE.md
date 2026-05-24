# Complete AI Engineer Curriculum
### 52-Week Detailed Plan · Zero to Job-Ready

> **Single source of truth** for teachers and students. Combines all content from `curriculum/module-01` through `module-12`.

---

## How to Read This Document

Each **week** contains one or more **topics**. Each topic contains numbered **lessons**.

Every lesson includes:
- **Concepts taught** — exact skills and knowledge (not just a title)
- **Step-by-step activities** — what to do hands-on
- **Lesson deliverable** — proof you completed it

Each topic also includes: lab, enterprise extension, tools, mistakes, interview prep, and deliverables from the full module curriculum.

| Pace | Hours/week | Calendar |
|------|------------|----------|
| Standard | 12–15 | 52 weeks (~12 months) |
| Intensive | 25–30 | 26 weeks (2 weeks per row) |
| Part-time | 8–10 | ~78 weeks (1.5 weeks per row) |

---

## 52-Week Schedule

| Week | Title | Module |
|------|-------|--------|
| 1 | Computer & Internet Fundamentals | Foundation |
| 2 | Programming Mindset & Developer Tools | Foundation |
| 3 | Python Basics for AI | Module 1 |
| 4 | Production Python — Async, Config & Testing | Module 1 |
| 5 | FastAPI — REST APIs for AI (Part 1) | Module 1 |
| 6 | FastAPI — Streaming, Versioning & Middleware | Module 1 |
| 7 | Docker, Git & CI/CD | Module 1 |
| 8 | OpenAI API — Chat & Streaming | Module 2 |
| 9 | OpenAI API — Tools, Batch & Fine-Tuning | Module 2 |
| 10 | Anthropic Claude & Google Gemini APIs | Module 2 |
| 11 | Open-Source Models — Ollama & HuggingFace | Module 2 |
| 12 | Structured Outputs & Model Routing | Module 2 |
| 13 | Production Prompt Engineering | Module 3 |
| 14 | DSPy — Programmatic Prompt Optimization | Module 3 |
| 15 | Prompt Security & Injection Defense | Module 3 |
| 16 | RAG Architecture Fundamentals | Module 4 |
| 17 | Chunking & Embedding Strategies | Module 4 |
| 18 | Vector Databases & Hybrid Search | Module 4 |
| 19 | Reranking, Caching & Retrieval Optimization | Module 4 |
| 20 | Advanced RAG — Graphs & Agentic RAG | Module 4 |
| 21 | AI Agents & Tool Calling | Module 5 |
| 22 | LangGraph — Stateful Agent Workflows | Module 5 |
| 23 | Multi-Agent Systems — CrewAI & AutoGen | Module 5 |
| 24 | Browser, Code Agents & AI Employees | Module 5 |
| 25 | Semantic Kernel & Enterprise Agents | Module 5 |
| 26 | LLM Observability & Tracing | Module 6 |
| 27 | AI Evaluation Pipelines | Module 6 |
| 28 | Prompt Versioning & AI CI/CD | Module 6 |
| 29 | Guardrails, Governance & Model Registry | Module 6 |
| 30 | AI Compliance, Privacy & Data Governance | Module 7 |
| 31 | AI Risk Management & Hallucination Prevention | Module 7 |
| 32 | RBAC, Multi-Tenancy & Enterprise Integrations | Module 7 |
| 33 | AI Consulting & Transformation Delivery | Module 7 |
| 34 | AWS AI — Bedrock & SageMaker | Module 8 |
| 35 | Azure AI — OpenAI & AI Search | Module 8 |
| 36 | GCP Vertex AI & Gemini Enterprise | Module 8 |
| 37 | Kubernetes, GPU & Inference Optimization | Module 8 |
| 38 | Next.js AI Frontends & Streaming UX | Module 9 |
| 39 | Multimodal & Voice AI Applications | Module 9 |
| 40 | AI SaaS Products & Copilot Patterns | Module 9 |
| 41 | TypeScript & Workflow Automation UI | Module 9 |
| 42 | AI Security — Threat Models & Red Teaming | Module 10 |
| 43 | Responsible AI — Bias, Fairness & Transparency | Module 10 |
| 44 | AI Governance & Audit Trails | Module 10 |
| 45 | AI System Design & Reference Architectures | Module 11 |
| 46 | Scalability, Cost Optimization & FinOps | Module 11 |
| 47 | Infrastructure as Code, Runbooks & Incidents | Module 11 |
| 48 | Capstone — Planning & Architecture | Module 12 |
| 49 | Capstone — Core Build Sprint | Module 12 |
| 50 | Capstone — LLMOps, Security & Deploy | Module 12 |
| 51 | Capstone — Polish, Demo & Documentation | Module 12 |
| 52 | Job Search, Interviews & Career Launch | Module 12 |

---

# Week 1: Computer & Internet Fundamentals

**Hours:** 12–15 recommended | **Module:** Foundation (pre-requisite)

## Week 1 learning goals
Complete all lessons below. Submit week deliverable before starting Week 2.

### Topic F1: How Computers and the Internet Work

**Why this matters:** Students new to IT must understand hardware, software, and how web apps work before coding.

**Learning objectives:**
- Explain CPU, memory, storage, and operating system roles
- Describe client-server model and HTTP request/response
- Use terminal to navigate files and folders

**Lessons this week:**

#### Lesson 1.1: Computer hardware and software basics
**Duration:** 2 hrs

**Concepts taught:**
- CPU, RAM, storage, input/output devices
- Operating systems: Windows, macOS, Linux
- Applications vs system software
- How code becomes a running program (compile/interpreter overview)

**Step-by-step activities:**
1. Draw diagram: User → Application → OS → Hardware
2. Identify your OS version and available disk/RAM

**Lesson deliverable:** One-page diagram in notebook or Notion

#### Lesson 1.2: Internet, browsers, and how websites work
**Duration:** 2 hrs

**Concepts taught:**
- Internet vs World Wide Web
- URLs, DNS, IP addresses (conceptual)
- HTTP methods: GET, POST; status codes 200, 404, 500
- Frontend vs backend; JSON data format

**Step-by-step activities:**
1. DevTools → Network → reload → inspect one request
2. Label: URL, method, status, response type

**Lesson deliverable:** Annotated screenshot of HTTP request

#### Lesson 1.3: Command line essentials
**Duration:** 2 hrs

**Concepts taught:**
- Terminal vs GUI; paths absolute vs relative
- cd, ls/dir, mkdir, touch, cat/type, pwd

**Step-by-step activities:**
1. Create ai-engineer-course folder structure via terminal only

**Lesson deliverable:** Folder tree screenshot

**Hands-on lab:** Write README section: 'What happens when I visit a website' in 5 steps.

**Tools:** Terminal, Browser DevTools

**Check your understanding:**
- RAM vs storage?
- What is HTTP 404?

**For teachers:** Pair students for terminal labs.

## Week 1 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 1):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 2: Programming Mindset & Developer Tools

**Hours:** 12–15 recommended | **Module:** Foundation (pre-requisite)

## Week 2 learning goals
Complete all lessons below. Submit week deliverable before starting Week 3.

### Topic F2: Introduction to Programming

**Why this matters:** AI engineering is software engineering. Students need computational thinking before Python.

**Learning objectives:**
- Define algorithm, variable, function, loop, condition
- Write first Python programs
- Read and fix simple error messages

**Lessons this week:**

#### Lesson 2.1: Computational thinking
**Duration:** 2 hrs

**Concepts taught:**
- Algorithms
- Sequence, selection, iteration
- Decomposition
- Debugging mindset

**Step-by-step activities:**
1. Pseudocode for making tea
2. Trace a 3-iteration loop on paper

**Lesson deliverable:** Pseudocode for guess-the-number game

#### Lesson 2.2: Python installation and first scripts
**Duration:** 3 hrs

**Concepts taught:**
- Python 3.11+ install
- print, variables, input()
- strings, int, float
- f-strings

**Step-by-step activities:**
1. hello.py greets user by name

**Lesson deliverable:** hello.py on GitHub

#### Lesson 2.3: Control flow and functions
**Duration:** 3 hrs

**Concepts taught:**
- if/elif/else
- for/while loops
- def functions
- lists, dicts
- common errors

**Step-by-step activities:**
1. celsius_to_fahrenheit(c)
2. loop print uppercase words

**Lesson deliverable:** practice_week2.py

**Hands-on lab:** CLI quiz app: 3 questions, score at end.

**Tools:** Python, VS Code

**Check your understanding:**
- What is a function?
- When use a loop?

**For teachers:** Live-debug intentional errors.

### Topic F3: Developer Environment Setup

**Why this matters:** Professional AI engineers use Git, venv, and IDE workflows daily.

**Learning objectives:**
- Configure VS Code
- Use GitHub
- Create virtual environments

**Lessons this week:**

#### Lesson 2.1: VS Code for Python
**Duration:** 2 hrs

**Concepts taught:**
- Workspace
- Integrated terminal
- Python extension
- Breakpoints intro

**Step-by-step activities:**
1. Debug quiz script with breakpoint

**Lesson deliverable:** VS Code project screenshot

#### Lesson 2.2: Git and GitHub
**Duration:** 3 hrs

**Concepts taught:**
- init, add, commit, push
- .gitignore
- README purpose

**Step-by-step activities:**
1. Create repo; push Week 2 code

**Lesson deliverable:** Public GitHub URL

#### Lesson 2.3: Virtual environments and pip
**Duration:** 2 hrs

**Concepts taught:**
- venv
- pip install
- requirements.txt
- never commit secrets

**Step-by-step activities:**
1. venv + pip install requests + freeze

**Lesson deliverable:** requirements.txt in repo

#### Lesson 2.4: What is AI? Roadmap preview
**Duration:** 90 min

**Concepts taught:**
- AI/ML/GenAI definitions
- LLM, RAG, agents preview
- 52-week map

**Step-by-step activities:**
1. Compare good vs bad ChatGPT prompt
2. Pick 2 job roles

**Lesson deliverable:** Learning goals in README

**Hands-on lab:** Full dev environment configured and pushed to GitHub.

**Tools:** VS Code, Git, GitHub, venv

**Check your understanding:**
- git commit does what?
- Why venv?

**For teachers:** Budget time for Git auth on Windows.

## Week 2 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 2):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 3: Python Basics for AI

**Hours:** 12–15 recommended | **Module:** 01

## Week 3 learning goals
Complete all lessons below. Submit week deliverable before starting Week 4.

### Topic 1.1: Production Python for AI Services

**Why this matters (job market):** 95%+ of AI Engineer JDs require Python. Employers reject candidates who only know notebooks—production async, typing, and testing are baseline.

**Job roles:** AI Engineer, Generative AI Engineer, AI Application Developer, AI Platform Engineer, LLMOps Engineer

**Learning objectives:**
- Write async Python suitable for I/O-bound LLM calls
- Use type hints, Pydantic v2, and structured error handling
- Structure packages for testability and CI

---

**Lessons this week:**

#### Lesson 3.1: Python data structures and files for AI apps
**Duration:** 3 hrs

**Concepts taught:**
- Lists and dicts for chat message history
- JSON: json.load, json.dump, serialization
- Reading/writing text files and JSON files
- List comprehensions

**Step-by-step activities:**
1. Save 5 messages as messages.json
2. Load and print formatted

**Lesson deliverable:** messages.json + load_messages.py

#### Lesson 3.2: Errors, exceptions, and logging basics
**Duration:** 3 hrs

**Concepts taught:**
- try/except/finally
- Common exceptions: ValueError, FileNotFoundError, KeyError
- logging module: DEBUG, INFO, WARNING, ERROR
- Why logging beats print in production

**Step-by-step activities:**
1. Wrap file load in try/except
2. Configure logging to file

**Lesson deliverable:** Script with logging and error handling

---

**Hands-on lab (week):**
Build async HTTP client wrapper with retries, timeouts, and circuit breaker stub.

**Enterprise project extension:**
Package `ai_service_core` with config management, health endpoint, and structured logs—template for all future modules.

**Portfolio artifact:**
Reusable FastAPI starter repo used in later RAG/agent projects.

**Tools & technologies:**
Python 3.11+, Pydantic, pytest, structlog, httpx, uvicorn

**Common mistakes:**
- Blocking event loop with sync SDK calls
- No timeout on external APIs
- Secrets in code instead of env/vault

**Industry best practices:**
- 12-factor config; never commit `.env`
- Pin dependencies in `pyproject.toml` / lockfile
- Pre-commit: ruff, mypy, pytest

**Interview preparation:**
- "How do you handle long-running LLM calls in Python?"
- "Explain async vs threading for OpenAI API calls."

**Real-world use cases:**
Backend for copilots, batch embedding jobs, webhook handlers for agent events.

**Topic deliverables (due end of week):**
`ai-engineer-starter` GitHub repo: linted, tested, Dockerized FastAPI skeleton.

## Week 3 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 3):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 4: Production Python — Async, Config & Testing

**Hours:** 12–15 recommended | **Module:** 01

## Week 4 learning goals
Complete all lessons below. Submit week deliverable before starting Week 5.

### Topic 1.1: Production Python for AI Services

**Why this matters (job market):** 95%+ of AI Engineer JDs require Python. Employers reject candidates who only know notebooks—production async, typing, and testing are baseline.

**Job roles:** AI Engineer, Generative AI Engineer, AI Application Developer, AI Platform Engineer, LLMOps Engineer

**Learning objectives:**
- Write async Python suitable for I/O-bound LLM calls
- Use type hints, Pydantic v2, and structured error handling
- Structure packages for testability and CI

---

**Lessons this week:**

#### Lesson 4.1: Python 3.11+ async/await patterns
**Duration:** 2 hrs

**Concepts taught:**
- Python 3.11+ async/await patterns
- Event loop: how asyncio schedules I/O-bound tasks
- When to use async vs sync code in AI APIs
- Avoid blocking the event loop with sync SDK calls

**Step-by-step activities:**
1. Install httpx; write async def fetch(url) with await client.get
2. Run 10 URLs concurrently with asyncio.gather; time vs sync loop
3. Add timeout=30.0 and handle httpx.TimeoutException
4. Write pytest-asyncio test mocking async HTTP with respx or unittest.mock

**Lesson deliverable:** Repo artifact for `python-3-11-async-await-patterns` — code, config, or doc under docs/ or src/

#### Lesson 4.2: Pydantic models for API contracts
**Duration:** 2 hrs

**Concepts taught:**
- Pydantic models for API contracts
- BaseModel validation
- Field constraints
- Serialization for API responses

**Step-by-step activities:**
1. Define ChatRequest(BaseModel) with message: str, max_length=4000
2. Add validator rejecting empty strings
3. Return model.model_dump() from endpoint; test invalid payload → 422

**Lesson deliverable:** Repo artifact for `pydantic-models-for-api-contracts` — code, config, or doc under docs/ or src/

#### Lesson 4.3: Environment configuration (12-factor)
**Duration:** 2 hrs

**Concepts taught:**
- Environment configuration (12-factor)
- How Environment configuration (12-factor) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Environment configuration (12-factor)
2. Implement a minimal working example of: Environment configuration (12-factor)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Environment configuration (12-factor)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `environment-configuration-12-factor` — code, config, or doc under docs/ or src/

#### Lesson 4.4: Logging (structlog) vs print
**Duration:** 2 hrs

**Concepts taught:**
- Logging (structlog) vs print
- How Logging (structlog) vs print fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Configure structlog with JSON output and timestamp
2. Replace all print() in project with logger.info/error
3. Add request_id to log context in FastAPI middleware

**Lesson deliverable:** Repo artifact for `logging-structlog-vs-print` — code, config, or doc under docs/ or src/

#### Lesson 4.5: pytest + pytest-asyncio
**Duration:** 2 hrs

**Concepts taught:**
- pytest + pytest-asyncio
- Event loop: how asyncio schedules I/O-bound tasks
- When to use async vs sync code in AI APIs
- Avoid blocking the event loop with sync SDK calls

**Step-by-step activities:**
1. Create tests/test_health.py asserting GET /health == 200
2. Add async test for chat endpoint with TestClient
3. Run pytest -v; add to CI workflow

**Lesson deliverable:** Repo artifact for `pytest-pytest-asyncio` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Build async HTTP client wrapper with retries, timeouts, and circuit breaker stub.

**Enterprise project extension:**
Package `ai_service_core` with config management, health endpoint, and structured logs—template for all future modules.

**Portfolio artifact:**
Reusable FastAPI starter repo used in later RAG/agent projects.

**Tools & technologies:**
Python 3.11+, Pydantic, pytest, structlog, httpx, uvicorn

**Common mistakes:**
- Blocking event loop with sync SDK calls
- No timeout on external APIs
- Secrets in code instead of env/vault

**Industry best practices:**
- 12-factor config; never commit `.env`
- Pin dependencies in `pyproject.toml` / lockfile
- Pre-commit: ruff, mypy, pytest

**Interview preparation:**
- "How do you handle long-running LLM calls in Python?"
- "Explain async vs threading for OpenAI API calls."

**Real-world use cases:**
Backend for copilots, batch embedding jobs, webhook handlers for agent events.

**Topic deliverables (due end of week):**
`ai-engineer-starter` GitHub repo: linted, tested, Dockerized FastAPI skeleton.

## Week 4 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 4):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 5: FastAPI — REST APIs for AI (Part 1)

**Hours:** 12–15 recommended | **Module:** 01

## Week 5 learning goals
Complete all lessons below. Submit week deliverable before starting Week 6.

### Topic 1.2: FastAPI for LLM Microservices

**Why this matters (job market):** FastAPI dominates AI backend JDs. Streaming SSE, dependency injection, and OpenAPI docs are expected day-one skills.

**Job roles:** AI Application Developer, Generative AI Engineer, AI Integration Engineer

**Learning objectives:**
- Build REST + SSE streaming endpoints
- Implement dependency injection for LLM clients
- Generate OpenAPI specs for frontend teams

---

**Lessons this week:**

#### Lesson 5.1: Routers, middleware, CORS
**Duration:** 2 hrs

**Concepts taught:**
- Routers, middleware, CORS
- APIRouter for modular routes
- Dependency injection pattern

**Step-by-step activities:**
1. Read official docs and module notes for: Routers, middleware, CORS
2. Implement a minimal working example of: Routers, middleware, CORS
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Routers, middleware, CORS' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `routers-middleware-cors` — code, config, or doc under docs/ or src/

#### Lesson 5.2: SSE streaming responses
**Duration:** 2 hrs

**Concepts taught:**
- SSE streaming responses
- How SSE streaming responses fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: SSE streaming responses
2. Implement a minimal working example of: SSE streaming responses
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'SSE streaming responses' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `sse-streaming-responses` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
`/v1/chat` POST with streaming SSE; `/health` and `/ready` probes.

**Enterprise project extension:**
API gateway pattern: auth middleware stub, request ID propagation, latency headers.

**Portfolio artifact:**
Documented OpenAPI + Postman collection in portfolio README.

**Tools & technologies:**
FastAPI, uvicorn, SSE-Starlette, Pydantic, OpenAPI

**Common mistakes:**
- No request ID for distributed tracing
- Returning raw LLM errors to clients (leak prompts)
- Missing input validation on user messages

**Industry best practices:**
- Problem+json error format
- Pagination for conversation history
- Idempotency keys for paid operations

**Interview preparation:**
- Design a chat API with streaming—endpoints, auth, error codes
- "How would you version breaking prompt schema changes?"

**Real-world use cases:**
Customer support backend, internal copilot API, mobile app AI proxy.

**Topic deliverables (due end of week):**
Deployed FastAPI service (Railway/Fly.io/AWS) with public health URL.

## Week 5 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 5):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 6: FastAPI — Streaming, Versioning & Middleware

**Hours:** 12–15 recommended | **Module:** 01

## Week 6 learning goals
Complete all lessons below. Submit week deliverable before starting Week 7.

### Topic 1.2: FastAPI for LLM Microservices

**Why this matters (job market):** FastAPI dominates AI backend JDs. Streaming SSE, dependency injection, and OpenAPI docs are expected day-one skills.

**Job roles:** AI Application Developer, Generative AI Engineer, AI Integration Engineer

**Learning objectives:**
- Build REST + SSE streaming endpoints
- Implement dependency injection for LLM clients
- Generate OpenAPI specs for frontend teams

---

**Lessons this week:**

#### Lesson 6.1: Background tasks and task queues intro
**Duration:** 2 hrs

**Concepts taught:**
- Background tasks and task queues intro
- How Background tasks and task queues intro fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Background tasks and task queues intro
2. Implement a minimal working example of: Background tasks and task queues intro
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Background tasks and task queues intro' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `background-tasks-and-task-queues-intro` — code, config, or doc under docs/ or src/

#### Lesson 6.2: API versioning (`/v1/`)
**Duration:** 2 hrs

**Concepts taught:**
- API versioning (`/v1/`)
- How API versioning (`/v1/`) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: API versioning (`/v1/`)
2. Implement a minimal working example of: API versioning (`/v1/`)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'API versioning (`/v1/`)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `api-versioning-v1` — code, config, or doc under docs/ or src/

#### Lesson 6.3: Rate limiting middleware
**Duration:** 2 hrs

**Concepts taught:**
- Rate limiting middleware
- How Rate limiting middleware fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Rate limiting middleware
2. Implement a minimal working example of: Rate limiting middleware
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Rate limiting middleware' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `rate-limiting-middleware` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
`/v1/chat` POST with streaming SSE; `/health` and `/ready` probes.

**Enterprise project extension:**
API gateway pattern: auth middleware stub, request ID propagation, latency headers.

**Portfolio artifact:**
Documented OpenAPI + Postman collection in portfolio README.

**Tools & technologies:**
FastAPI, uvicorn, SSE-Starlette, Pydantic, OpenAPI

**Common mistakes:**
- No request ID for distributed tracing
- Returning raw LLM errors to clients (leak prompts)
- Missing input validation on user messages

**Industry best practices:**
- Problem+json error format
- Pagination for conversation history
- Idempotency keys for paid operations

**Interview preparation:**
- Design a chat API with streaming—endpoints, auth, error codes
- "How would you version breaking prompt schema changes?"

**Real-world use cases:**
Customer support backend, internal copilot API, mobile app AI proxy.

**Topic deliverables (due end of week):**
Deployed FastAPI service (Railway/Fly.io/AWS) with public health URL.

## Week 6 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 6):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 7: Docker, Git & CI/CD

**Hours:** 12–15 recommended | **Module:** 01

## Week 7 learning goals
Complete all lessons below. Submit week deliverable before starting Week 8.

### Topic 1.3: Docker, Git & CI Foundations for AI

**Why this matters (job market):** "No Docker on resume" filters out candidates at mid+ levels. AI CI must run evals, not just unit tests.

**Job roles:** AI Platform Engineer, LLMOps Engineer, Enterprise AI Engineer

**Learning objectives:**
- Multi-stage Dockerfiles for Python AI services
- GitHub Actions: lint, test, build image
- Semantic versioning for API releases

---

**Lessons this week:**

#### Lesson 7.1: Dockerfile best practices (non-root, slim images)
**Duration:** 2 hrs

**Concepts taught:**
- Dockerfile best practices (non-root, slim images)
- Layer caching in builds
- Non-root user in container
- .dockerignore

**Step-by-step activities:**
1. Write multi-stage Dockerfile: builder + slim runtime
2. Run as non-root user; expose port 8000
3. docker build -t ai-api . && docker run -p 8000:8000 ai-api

**Lesson deliverable:** Repo artifact for `dockerfile-best-practices-non-root-slim` — code, config, or doc under docs/ or src/

#### Lesson 7.2: docker-compose for local dev (API + Redis + Postgres)
**Duration:** 2 hrs

**Concepts taught:**
- docker-compose for local dev (API + Redis + Postgres)
- Layer caching in builds
- Non-root user in container
- .dockerignore

**Step-by-step activities:**
1. Read official docs and module notes for: docker-compose for local dev (API + Redis + Postgres)
2. Implement a minimal working example of: docker-compose for local dev (API + Redis + Postgres)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'docker-compose for local dev (API + Redis + Postgres)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `docker-compose-for-local-dev-api-redis-p` — code, config, or doc under docs/ or src/

#### Lesson 7.3: Git branching (trunk-based intro)
**Duration:** 2 hrs

**Concepts taught:**
- Git branching (trunk-based intro)
- How Git branching (trunk-based intro) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Git branching (trunk-based intro)
2. Implement a minimal working example of: Git branching (trunk-based intro)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Git branching (trunk-based intro)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `git-branching-trunk-based-intro` — code, config, or doc under docs/ or src/

#### Lesson 7.4: GitHub Actions workflows
**Duration:** 2 hrs

**Concepts taught:**
- GitHub Actions workflows
- How GitHub Actions workflows fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Create .github/workflows/ci.yml: checkout, setup-python, pytest, ruff
2. Add docker build step on push to main
3. Add status badge to README

**Lesson deliverable:** Repo artifact for `github-actions-workflows` — code, config, or doc under docs/ or src/

#### Lesson 7.5: Container registry (GHCR, ECR)
**Duration:** 2 hrs

**Concepts taught:**
- Container registry (GHCR, ECR)
- How Container registry (GHCR, ECR) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Container registry (GHCR, ECR)
2. Implement a minimal working example of: Container registry (GHCR, ECR)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Container registry (GHCR, ECR)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `container-registry-ghcr-ecr` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
CI pipeline: ruff → pytest → docker build → push on `main`.

**Enterprise project extension:**
Signed images, SBOM awareness, dependency scanning (Trivy) in CI.

**Portfolio artifact:**
README badge: CI passing, Docker pull instructions.

**Tools & technologies:**
Docker, docker-compose, GitHub Actions, Trivy, GHCR

**Common mistakes:**
- Giant images with CUDA when only calling APIs
- Running evals only manually before release
- No `.dockerignore` (slow builds, leaked data)

**Industry best practices:**
- Separate build and runtime stages
- Cache pip layers in Docker
- Tag images with git SHA

**Interview preparation:**
- "Walk through your CI/CD for an AI feature."
- "How do you manage secrets in CI?"

**Real-world use cases:**
Every production AI deployment starts here.

**Topic deliverables (due end of week):**
Green CI on starter repo; one-page runbook: build, deploy, rollback.

## Week 7 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 7):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 8: OpenAI API — Chat & Streaming

**Hours:** 12–15 recommended | **Module:** 02

## Week 8 learning goals
Complete all lessons below. Submit week deliverable before starting Week 9.

### Topic 2.1: OpenAI API Production Patterns

**Why this matters (job market):** OpenAI appears in 90%+ of US GenAI JDs. Production means streaming, structured outputs, tool calling, retries, and cost tracking—not playground demos.

**Job roles:** Generative AI Engineer, LLM Engineer, AI Engineer, AI Product Engineer

**Learning objectives:**
- Implement chat completions with streaming
- Use JSON schema / structured outputs
- Configure tool/function calling
- Track tokens and cost per request

---

**Lessons this week:**

#### Lesson 8.1: Models: GPT-4o, o-series reasoning models
**Duration:** 2 hrs

**Concepts taught:**
- Models: GPT-4o, o-series reasoning models
- How Models: GPT-4o, o-series reasoning models fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Models: GPT-4o, o-series reasoning models
2. Implement a minimal working example of: Models: GPT-4o, o-series reasoning models
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Models: GPT-4o, o-series reasoning models' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `models-gpt-4o-o-series-reasoning-models` — code, config, or doc under docs/ or src/

#### Lesson 8.2: Messages API vs Assistants (when to use each)
**Duration:** 2 hrs

**Concepts taught:**
- Messages API vs Assistants (when to use each)
- How Messages API vs Assistants (when to use each) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Messages API vs Assistants (when to use each)
2. Implement a minimal working example of: Messages API vs Assistants (when to use each)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Messages API vs Assistants (when to use each)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `messages-api-vs-assistants-when-to-use-e` — code, config, or doc under docs/ or src/

#### Lesson 8.3: Streaming deltas handling
**Duration:** 2 hrs

**Concepts taught:**
- Streaming deltas handling
- How Streaming deltas handling fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Call client.chat.completions.create(stream=True)
2. Iterate chunks; yield SSE from FastAPI StreamingResponse
3. Log time-to-first-token metric

**Lesson deliverable:** Repo artifact for `streaming-deltas-handling` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Multi-turn chat service with token/cost middleware logging.

**Enterprise project extension:**
Model router: GPT-4o for quality, mini for simple tasks; fallback on rate limit.

**Portfolio artifact:**
OpenAI integration layer abstracted behind provider interface.

**Tools & technologies:**
OpenAI Python SDK, tiktoken, LiteLLM (routing intro)

**Common mistakes:**
- No retry with exponential backoff
- Ignoring `max_tokens` cost explosion
- Storing full prompts in logs (PII)

**Industry best practices:**
- Abstract provider behind interface for multi-vendor
- Cache system prompts where possible
- Log token usage to metrics backend

**Interview preparation:**
- "Design token budget enforcement for a SaaS copilot."
- "When would you fine-tune vs RAG vs prompt?"

**Real-world use cases:**
Support bots, code generation, document summarization.

**Topic deliverables (due end of week):**
Provider-agnostic `LLMClient` with OpenAI implementation + cost dashboard stub.

## Week 8 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 8):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 9: OpenAI API — Tools, Batch & Fine-Tuning

**Hours:** 12–15 recommended | **Module:** 02

## Week 9 learning goals
Complete all lessons below. Submit week deliverable before starting Week 10.

### Topic 2.1: OpenAI API Production Patterns

**Why this matters (job market):** OpenAI appears in 90%+ of US GenAI JDs. Production means streaming, structured outputs, tool calling, retries, and cost tracking—not playground demos.

**Job roles:** Generative AI Engineer, LLM Engineer, AI Engineer, AI Product Engineer

**Learning objectives:**
- Implement chat completions with streaming
- Use JSON schema / structured outputs
- Configure tool/function calling
- Track tokens and cost per request

---

**Lessons this week:**

#### Lesson 9.1: Tool calling loop
**Duration:** 2 hrs

**Concepts taught:**
- Tool calling loop
- How Tool calling loop fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Tool calling loop
2. Implement a minimal working example of: Tool calling loop
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Tool calling loop' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `tool-calling-loop` — code, config, or doc under docs/ or src/

#### Lesson 9.2: Batch API for offline jobs
**Duration:** 2 hrs

**Concepts taught:**
- Batch API for offline jobs
- How Batch API for offline jobs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Batch API for offline jobs
2. Implement a minimal working example of: Batch API for offline jobs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Batch API for offline jobs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `batch-api-for-offline-jobs` — code, config, or doc under docs/ or src/

#### Lesson 9.3: Fine-tuning overview (when justified)
**Duration:** 2 hrs

**Concepts taught:**
- Fine-tuning overview (when justified)
- How Fine-tuning overview (when justified) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Fine-tuning overview (when justified)
2. Implement a minimal working example of: Fine-tuning overview (when justified)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Fine-tuning overview (when justified)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `fine-tuning-overview-when-justified` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Multi-turn chat service with token/cost middleware logging.

**Enterprise project extension:**
Model router: GPT-4o for quality, mini for simple tasks; fallback on rate limit.

**Portfolio artifact:**
OpenAI integration layer abstracted behind provider interface.

**Tools & technologies:**
OpenAI Python SDK, tiktoken, LiteLLM (routing intro)

**Common mistakes:**
- No retry with exponential backoff
- Ignoring `max_tokens` cost explosion
- Storing full prompts in logs (PII)

**Industry best practices:**
- Abstract provider behind interface for multi-vendor
- Cache system prompts where possible
- Log token usage to metrics backend

**Interview preparation:**
- "Design token budget enforcement for a SaaS copilot."
- "When would you fine-tune vs RAG vs prompt?"

**Real-world use cases:**
Support bots, code generation, document summarization.

**Topic deliverables (due end of week):**
Provider-agnostic `LLMClient` with OpenAI implementation + cost dashboard stub.

## Week 9 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 9):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 10: Anthropic Claude & Google Gemini APIs

**Hours:** 12–15 recommended | **Module:** 02

## Week 10 learning goals
Complete all lessons below. Submit week deliverable before starting Week 11.

### Topic 2.2: Anthropic Claude & Google Gemini APIs

**Why this matters (job market):** Enterprise deals increasingly multi-vendor. Anthropic leads tool use/computer use; Gemini integrates with GCP Vertex.

**Job roles:** Enterprise AI Engineer, LLM Engineer, AI Solutions Engineer

**Learning objectives:**
- Implement Claude messages API with tool use
- Use Gemini via AI Studio and Vertex AI
- Compare latency, cost, context windows across vendors

---

**Lessons this week:**

#### Lesson 10.1: Claude system prompts and XML tags pattern
**Duration:** 2 hrs

**Concepts taught:**
- Claude system prompts and XML tags pattern
- How Claude system prompts and XML tags pattern fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Claude system prompts and XML tags pattern
2. Implement a minimal working example of: Claude system prompts and XML tags pattern
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Claude system prompts and XML tags pattern' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `claude-system-prompts-and-xml-tags-patte` — code, config, or doc under docs/ or src/

#### Lesson 10.2: Extended context use cases
**Duration:** 2 hrs

**Concepts taught:**
- Extended context use cases
- How Extended context use cases fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Extended context use cases
2. Implement a minimal working example of: Extended context use cases
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Extended context use cases' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `extended-context-use-cases` — code, config, or doc under docs/ or src/

#### Lesson 10.3: Gemini multimodal inputs
**Duration:** 2 hrs

**Concepts taught:**
- Gemini multimodal inputs
- How Gemini multimodal inputs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Gemini multimodal inputs
2. Implement a minimal working example of: Gemini multimodal inputs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Gemini multimodal inputs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `gemini-multimodal-inputs` — code, config, or doc under docs/ or src/

#### Lesson 10.4: Vertex AI enterprise auth (service accounts)
**Duration:** 2 hrs

**Concepts taught:**
- Vertex AI enterprise auth (service accounts)
- How Vertex AI enterprise auth (service accounts) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Vertex AI enterprise auth (service accounts)
2. Implement a minimal working example of: Vertex AI enterprise auth (service accounts)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Vertex AI enterprise auth (service accounts)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `vertex-ai-enterprise-auth-service-accoun` — code, config, or doc under docs/ or src/

#### Lesson 10.5: Cross-provider eval baselines
**Duration:** 2 hrs

**Concepts taught:**
- Cross-provider eval baselines
- Golden datasets
- Regression gates before deploy

**Step-by-step activities:**
1. Read official docs and module notes for: Cross-provider eval baselines
2. Implement a minimal working example of: Cross-provider eval baselines
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Cross-provider eval baselines' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `cross-provider-eval-baselines` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Same task on OpenAI, Anthropic, Gemini—log latency, cost, quality scores.

**Enterprise project extension:**
Vendor abstraction + contract-aware model selection (EU data residency → Azure/GCP).

**Portfolio artifact:**
Benchmark report (1-pager) in repo `/docs/model-comparison.md`.

**Tools & technologies:**
anthropic SDK, google-generativeai, Vertex AI SDK, LiteLLM

**Common mistakes:**
- Hard-coding one vendor in application layer
- Not testing tool-use compatibility across models
- Ignoring regional API availability

**Industry best practices:**
- Golden eval set run on all candidate models
- Document model selection ADR
- Feature flag per tenant model preference

**Interview preparation:**
- "How do you choose between Claude and GPT-4 for a legal RAG app?"
- "Explain Vertex AI vs direct Gemini API."

**Real-world use cases:**
Regulated industries picking vendor by data boundary; multimodal doc Q&A.

**Topic deliverables (due end of week):**
Multi-provider router with config-driven model map.

## Week 10 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 10):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 11: Open-Source Models — Ollama & HuggingFace

**Hours:** 12–15 recommended | **Module:** 02

## Week 11 learning goals
Complete all lessons below. Submit week deliverable before starting Week 12.

### Topic 2.3: HuggingFace & Open-Source LLMs (Ollama, vLLM intro)

**Why this matters (job market):** Cost-sensitive enterprises self-host. HuggingFace skills appear in platform and infra roles; Ollama for local dev, vLLM for production inference.

**Job roles:** AI Infrastructure Engineer, AI Platform Engineer, LLM Engineer

**Learning objectives:**
- Load and run models via HuggingFace Inference API / Endpoints
- Develop locally with Ollama
- Understand vLLM serving architecture (preview for Module 08)

---

**Lessons this week:**

#### Lesson 11.1: Model cards and licensing
**Duration:** 2 hrs

**Concepts taught:**
- Model cards and licensing
- How Model cards and licensing fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Model cards and licensing
2. Implement a minimal working example of: Model cards and licensing
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Model cards and licensing' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `model-cards-and-licensing` — code, config, or doc under docs/ or src/

#### Lesson 11.2: Embeddings models (BGE, E5, nomic)
**Duration:** 2 hrs

**Concepts taught:**
- Embeddings models (BGE, E5, nomic)
- How Embeddings models (BGE, E5, nomic) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Embeddings models (BGE, E5, nomic)
2. Implement a minimal working example of: Embeddings models (BGE, E5, nomic)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Embeddings models (BGE, E5, nomic)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `embeddings-models-bge-e5-nomic` — code, config, or doc under docs/ or src/

#### Lesson 11.3: Ollama local workflow
**Duration:** 2 hrs

**Concepts taught:**
- Ollama local workflow
- How Ollama local workflow fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Ollama local workflow
2. Implement a minimal working example of: Ollama local workflow
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Ollama local workflow' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `ollama-local-workflow` — code, config, or doc under docs/ or src/

#### Lesson 11.4: vLLM throughput concepts
**Duration:** 2 hrs

**Concepts taught:**
- vLLM throughput concepts
- How vLLM throughput concepts fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: vLLM throughput concepts
2. Implement a minimal working example of: vLLM throughput concepts
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'vLLM throughput concepts' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `vllm-throughput-concepts` — code, config, or doc under docs/ or src/

#### Lesson 11.5: Quantization tradeoffs (GGUF, AWQ)
**Duration:** 2 hrs

**Concepts taught:**
- Quantization tradeoffs (GGUF, AWQ)
- How Quantization tradeoffs (GGUF, AWQ) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Quantization tradeoffs (GGUF, AWQ)
2. Implement a minimal working example of: Quantization tradeoffs (GGUF, AWQ)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Quantization tradeoffs (GGUF, AWQ)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `quantization-tradeoffs-gguf-awq` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Local RAG with Ollama + same pipeline pointing to OpenAI embeddings.

**Enterprise project extension:**
Air-gapped deployment option using self-hosted Llama/Mistral.

**Portfolio artifact:**
"Cost comparison: API vs self-hosted" analysis document.

**Tools & technologies:**
HuggingFace Hub, transformers, Ollama, vLLM (intro), sentence-transformers

**Common mistakes:**
- Picking largest model without latency budget
- Ignoring license restrictions for commercial use
- No GPU memory planning

**Industry best practices:**
- Pin model revisions in config
- Warm inference pools in production
- Separate embedding and generation infrastructure

**Interview preparation:**
- "When is self-hosting cheaper than APIs at 1M queries/month?"
- "Explain embedding model selection for RAG."

**Real-world use cases:**
PII-sensitive on-prem, dev environments without API spend.

**Topic deliverables (due end of week):**
Dual-mode config: `CLOUD_API` vs `LOCAL_OLLAMA` switch in starter app.

## Week 11 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 11):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 12: Structured Outputs & Model Routing

**Hours:** 12–15 recommended | **Module:** 02

## Week 12 learning goals
Complete all lessons below. Submit week deliverable before starting Week 13.

### Topic 2.4: Structured Outputs, Parsing & Intelligent Model Routing

**Why this matters (job market):** Enterprise integrations require JSON/XML contracts, not free text. Routing saves 40–70% cost on simple queries.

**Job roles:** AI Integration Engineer, LLM Engineer, AI Automation Engineer

**Learning objectives:**
- Enforce Pydantic-validated LLM outputs
- Build classifier-based model router
- Handle parse failures gracefully

---

**Lessons this week:**

#### Lesson 12.1: JSON mode, instructor library, OpenAI structured outputs
**Duration:** 2 hrs

**Concepts taught:**
- JSON mode, instructor library, OpenAI structured outputs
- How JSON mode, instructor library, OpenAI structured outputs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: JSON mode, instructor library, OpenAI structured outputs
2. Implement a minimal working example of: JSON mode, instructor library, OpenAI structured outputs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'JSON mode, instructor library, OpenAI structured outputs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `json-mode-instructor-library-openai-stru` — code, config, or doc under docs/ or src/

#### Lesson 12.2: Constrained decoding concepts
**Duration:** 2 hrs

**Concepts taught:**
- Constrained decoding concepts
- How Constrained decoding concepts fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Constrained decoding concepts
2. Implement a minimal working example of: Constrained decoding concepts
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Constrained decoding concepts' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `constrained-decoding-concepts` — code, config, or doc under docs/ or src/

#### Lesson 12.3: Query complexity classifier (cheap model)
**Duration:** 2 hrs

**Concepts taught:**
- Query complexity classifier (cheap model)
- How Query complexity classifier (cheap model) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Query complexity classifier (cheap model)
2. Implement a minimal working example of: Query complexity classifier (cheap model)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Query complexity classifier (cheap model)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `query-complexity-classifier-cheap-model` — code, config, or doc under docs/ or src/

#### Lesson 12.4: Fallback chains
**Duration:** 2 hrs

**Concepts taught:**
- Fallback chains
- How Fallback chains fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Fallback chains
2. Implement a minimal working example of: Fallback chains
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Fallback chains' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `fallback-chains` — code, config, or doc under docs/ or src/

#### Lesson 12.5: Caching identical requests (semantic intro)
**Duration:** 2 hrs

**Concepts taught:**
- Caching identical requests (semantic intro)
- How Caching identical requests (semantic intro) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Caching identical requests (semantic intro)
2. Implement a minimal working example of: Caching identical requests (semantic intro)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Caching identical requests (semantic intro)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `caching-identical-requests-semantic-intr` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Extract structured `InvoiceData` from PDF text with validation retry loop.

**Enterprise project extension:**
Schema registry for all LLM outputs; breaking change detection in CI.

**Portfolio artifact:**
Router reducing average cost/query documented with before/after metrics.

**Tools & technologies:**
Pydantic, instructor, outlines (optional), Redis cache

**Common mistakes:**
- No retry with repair prompt on schema failure
- Routing without monitoring misroute rate
- Over-structuring simple tasks (added latency)

**Industry best practices:**
- Max 2 repair attempts then human queue
- Log parse failure reasons for prompt iteration
- A/B test router rules

**Interview preparation:**
- "LLM returned invalid JSON 15% of the time—how do you fix it?"
- "Design a model routing layer."

**Real-world use cases:**
ERP field extraction, ticket classification, CRM auto-fill.

**Topic deliverables (due end of week):**
`StructuredExtractor` class with ≥95% schema success on test set.

## Week 12 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 12):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 13: Production Prompt Engineering

**Hours:** 12–15 recommended | **Module:** 03

## Week 13 learning goals
Complete all lessons below. Submit week deliverable before starting Week 14.

### Topic 3.1: Production Prompt Engineering

**Why this matters (job market):** Prompting is table stakes, but **versioned, tested, measurable** prompts separate hires from hobbyists. Prompt Engineer roles merge into AI Engineer with eval discipline.

**Job roles:** Prompt Engineer, LLM Engineer, Generative AI Engineer, AI Product Engineer

**Learning objectives:**
- Apply CO-STAR, few-shot, chain-of-thought appropriately
- Version prompts in Git with semantic tags
- Measure quality with golden datasets

---

**Lessons this week:**

#### Lesson 13.1: System vs user vs developer messages
**Duration:** 2 hrs

**Concepts taught:**
- System vs user vs developer messages
- How System vs user vs developer messages fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: System vs user vs developer messages
2. Implement a minimal working example of: System vs user vs developer messages
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'System vs user vs developer messages' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `system-vs-user-vs-developer-messages` — code, config, or doc under docs/ or src/

#### Lesson 13.2: Few-shot selection strategies
**Duration:** 2 hrs

**Concepts taught:**
- Few-shot selection strategies
- How Few-shot selection strategies fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Few-shot selection strategies
2. Implement a minimal working example of: Few-shot selection strategies
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Few-shot selection strategies' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `few-shot-selection-strategies` — code, config, or doc under docs/ or src/

#### Lesson 13.3: Chain-of-thought and decomposition
**Duration:** 2 hrs

**Concepts taught:**
- Chain-of-thought and decomposition
- How Chain-of-thought and decomposition fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Chain-of-thought and decomposition
2. Implement a minimal working example of: Chain-of-thought and decomposition
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Chain-of-thought and decomposition' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `chain-of-thought-and-decomposition` — code, config, or doc under docs/ or src/

#### Lesson 13.4: Role and tone control for enterprise brand
**Duration:** 2 hrs

**Concepts taught:**
- Role and tone control for enterprise brand
- How Role and tone control for enterprise brand fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Role and tone control for enterprise brand
2. Implement a minimal working example of: Role and tone control for enterprise brand
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Role and tone control for enterprise brand' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `role-and-tone-control-for-enterprise-bra` — code, config, or doc under docs/ or src/

#### Lesson 13.5: Prompt templates (Jinja2) separation
**Duration:** 2 hrs

**Concepts taught:**
- Prompt templates (Jinja2) separation
- How Prompt templates (Jinja2) separation fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Prompt templates (Jinja2) separation
2. Implement a minimal working example of: Prompt templates (Jinja2) separation
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Prompt templates (Jinja2) separation' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `prompt-templates-jinja2-separation` — code, config, or doc under docs/ or src/

#### Lesson 13.6: Anti-patterns: prompt injection in instructions
**Duration:** 2 hrs

**Concepts taught:**
- Anti-patterns: prompt injection in instructions
- How Anti-patterns: prompt injection in instructions fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Anti-patterns: prompt injection in instructions
2. Implement a minimal working example of: Anti-patterns: prompt injection in instructions
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Anti-patterns: prompt injection in instructions' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `anti-patterns-prompt-injection-in-instru` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Prompt registry (`prompts/v1/support_system.yaml`) + A/B test harness.

**Enterprise project extension:**
Approval workflow: dev → staging prompt → prod with sign-off.

**Portfolio artifact:**
Before/after eval scores on 50-example golden set.

**Tools & technologies:**
promptfoo, LangSmith (prompt hub), YAML/Git, Jinja2

**Common mistakes:**
- Giant monolithic system prompt (context waste)
- No few-shot refresh when product changes
- Changing prod prompts without regression tests

**Industry best practices:**
- One concern per prompt module (compose)
- Document intended model per prompt
- Track token length budgets per template

**Interview preparation:**
- "How do you version and roll back prompts?"
- Live: improve a weak support prompt with measurable criteria

**Real-world use cases:**
Brand-safe customer agents, legal tone control, sales email generation.

**Topic deliverables (due end of week):**
Prompt library with 3 domains + promptfoo CI gate on `main`.

## Week 13 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 13):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 14: DSPy — Programmatic Prompt Optimization

**Hours:** 12–15 recommended | **Module:** 03

## Week 14 learning goals
Complete all lessons below. Submit week deliverable before starting Week 15.

### Topic 3.2: DSPy for Optimized LLM Pipelines

**Why this matters (job market):** DSPy represents shift from manual prompt hacking to **compiled, optimizable pipelines**—increasingly cited in advanced AI teams.

**Job roles:** LLM Engineer, Applied AI Engineer, AI Research-adjacent Engineer

**Learning objectives:**
- Build DSPy modules (Signature, ChainOfThought, ReAct)
- Run optimizers (BootstrapFewShot, MIPRO)
- Export optimized prompts to production non-DSPy path

---

**Lessons this week:**

#### Lesson 14.1: Signatures and modules
**Duration:** 2 hrs

**Concepts taught:**
- Signatures and modules
- How Signatures and modules fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Signatures and modules
2. Implement a minimal working example of: Signatures and modules
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Signatures and modules' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `signatures-and-modules` — code, config, or doc under docs/ or src/

#### Lesson 14.2: Teleprompters / optimizers
**Duration:** 2 hrs

**Concepts taught:**
- Teleprompters / optimizers
- How Teleprompters / optimizers fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Teleprompters / optimizers
2. Implement a minimal working example of: Teleprompters / optimizers
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Teleprompters / optimizers' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `teleprompters-optimizers` — code, config, or doc under docs/ or src/

#### Lesson 14.3: Metrics functions for optimization
**Duration:** 2 hrs

**Concepts taught:**
- Metrics functions for optimization
- How Metrics functions for optimization fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Metrics functions for optimization
2. Implement a minimal working example of: Metrics functions for optimization
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Metrics functions for optimization' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `metrics-functions-for-optimization` — code, config, or doc under docs/ or src/

#### Lesson 14.4: Bridging DSPy → frozen prompts for latency
**Duration:** 2 hrs

**Concepts taught:**
- Bridging DSPy → frozen prompts for latency
- How Bridging DSPy → frozen prompts for latency fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Bridging DSPy → frozen prompts for latency
2. Implement a minimal working example of: Bridging DSPy → frozen prompts for latency
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Bridging DSPy → frozen prompts for latency' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `bridging-dspy-frozen-prompts-for-latency` — code, config, or doc under docs/ or src/

#### Lesson 14.5: Comparison vs manual prompting ROI
**Duration:** 2 hrs

**Concepts taught:**
- Comparison vs manual prompting ROI
- How Comparison vs manual prompting ROI fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Comparison vs manual prompting ROI
2. Implement a minimal working example of: Comparison vs manual prompting ROI
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Comparison vs manual prompting ROI' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `comparison-vs-manual-prompting-roi` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Optimize classification module; achieve +10% F1 vs manual prompt on holdout.

**Enterprise project extension:**
Offline optimization pipeline; deploy only frozen approved artifacts.

**Portfolio artifact:**
Notebook + exported `optimized_prompt.json` in repo.

**Tools & technologies:**
DSPy, dspy-ai, OpenAI/Anthropic via LiteLLM

**Common mistakes:**
- Optimizing on tiny datasets
- Deploying slow compile-time chains to hot path
- No holdout set separation

**Industry best practices:**
- Holdout 20% never seen by optimizer
- Human review before promoting optimized prompts
- Log optimizer version in metadata

**Interview preparation:**
- "What is DSPy and when would you use it vs LangChain?"
- "How do you prevent overfitting prompts to eval set?"

**Real-world use cases:**
High-volume classification, extraction, routing decisions.

**Topic deliverables (due end of week):**
DSPy-optimized extractor beating baseline in documented eval report.

## Week 14 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 14):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 15: Prompt Security & Injection Defense

**Hours:** 12–15 recommended | **Module:** 03

## Week 15 learning goals
Complete all lessons below. Submit week deliverable before starting Week 16.

### Topic 3.3: Prompt Injection Defense & Input Sanitization

**Why this matters (job market):** As agents gain tool access, injection becomes **critical security**. AI Security Engineer roles require this fluency.

**Job roles:** AI Security Engineer, Enterprise AI Engineer, Responsible AI Engineer

**Learning objectives:**
- Classify direct vs indirect injection
- Implement input/output guardrails
- Design privilege boundaries for tools

---

**Lessons this week:**

#### Lesson 15.1: OWASP LLM Top 10 overview
**Duration:** 2 hrs

**Concepts taught:**
- OWASP LLM Top 10 overview
- How OWASP LLM Top 10 overview fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: OWASP LLM Top 10 overview
2. Implement a minimal working example of: OWASP LLM Top 10 overview
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'OWASP LLM Top 10 overview' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `owasp-llm-top-10-overview` — code, config, or doc under docs/ or src/

#### Lesson 15.2: System prompt hardening (limited efficacy)
**Duration:** 2 hrs

**Concepts taught:**
- System prompt hardening (limited efficacy)
- How System prompt hardening (limited efficacy) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: System prompt hardening (limited efficacy)
2. Implement a minimal working example of: System prompt hardening (limited efficacy)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'System prompt hardening (limited efficacy)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `system-prompt-hardening-limited-efficacy` — code, config, or doc under docs/ or src/

#### Lesson 15.3: Input filters, allowlists, canonicalization
**Duration:** 2 hrs

**Concepts taught:**
- Input filters, allowlists, canonicalization
- How Input filters, allowlists, canonicalization fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Input filters, allowlists, canonicalization
2. Implement a minimal working example of: Input filters, allowlists, canonicalization
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Input filters, allowlists, canonicalization' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `input-filters-allowlists-canonicalizatio` — code, config, or doc under docs/ or src/

#### Lesson 15.4: Output validation before tool execution
**Duration:** 2 hrs

**Concepts taught:**
- Output validation before tool execution
- How Output validation before tool execution fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Output validation before tool execution
2. Implement a minimal working example of: Output validation before tool execution
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Output validation before tool execution' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `output-validation-before-tool-execution` — code, config, or doc under docs/ or src/

#### Lesson 15.5: Dual-LLM pattern, Llama Guard classifiers
**Duration:** 2 hrs

**Concepts taught:**
- Dual-LLM pattern, Llama Guard classifiers
- How Dual-LLM pattern, Llama Guard classifiers fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Dual-LLM pattern, Llama Guard classifiers
2. Implement a minimal working example of: Dual-LLM pattern, Llama Guard classifiers
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Dual-LLM pattern, Llama Guard classifiers' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `dual-llm-pattern-llama-guard-classifiers` — code, config, or doc under docs/ or src/

#### Lesson 15.6: Human-in-the-loop for high-risk actions
**Duration:** 2 hrs

**Concepts taught:**
- Human-in-the-loop for high-risk actions
- How Human-in-the-loop for high-risk actions fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Human-in-the-loop for high-risk actions
2. Implement a minimal working example of: Human-in-the-loop for high-risk actions
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Human-in-the-loop for high-risk actions' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `human-in-the-loop-for-high-risk-actions` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Red-team 10 injection attacks against your chatbot; fix and re-test.

**Enterprise project extension:**
Security test suite in CI: known injection cases must fail safe.

**Portfolio artifact:**
`SECURITY.md` with threat model and mitigations.

**Tools & technologies:**
NeMo Guardrails, Llama Guard, Rebuff, custom regex + ML filters

**Common mistakes:**
- Trusting system prompt alone
- Giving agents unrestricted shell/network
- Logging user content with secrets

**Industry best practices:**
- Least-privilege tool scopes
- Separate control plane from data plane
- Rate limit and anomaly detection on inputs

**Interview preparation:**
- "User says 'ignore previous instructions'—architecture response?"
- "How do you secure agent tool calling?"

**Real-world use cases:**
Customer-facing bots, email-to-agent pipelines (indirect injection).

**Topic deliverables (due end of week):**
Injection test suite passing in CI; documented residual risks.

## Week 15 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 15):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 16: RAG Architecture Fundamentals

**Hours:** 12–15 recommended | **Module:** 04

## Week 16 learning goals
Complete all lessons below. Submit week deliverable before starting Week 17.

### Topic 4.1: RAG Architecture Fundamentals

**Why this matters (job market):** RAG is +11% salary premium skill; 80%+ enterprise GenAI JDs mention retrieval. This is the #1 differentiator vs tutorial developers.

**Job roles:** RAG Engineer, Generative AI Engineer, Enterprise AI Engineer, Applied AI Engineer

**Learning objectives:**
- Diagram naive vs advanced RAG pipelines
- Implement ingest → chunk → embed → store → retrieve → generate
- Measure faithfulness and relevance

---

**Lessons this week:**

#### Lesson 16.1: When RAG vs fine-tuning vs long context
**Duration:** 2 hrs

**Concepts taught:**
- When RAG vs fine-tuning vs long context
- Grounding LLM answers in retrieved context
- Measuring retrieval quality

**Step-by-step activities:**
1. Read official docs and module notes for: When RAG vs fine-tuning vs long context
2. Implement a minimal working example of: When RAG vs fine-tuning vs long context
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'When RAG vs fine-tuning vs long context' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `when-rag-vs-fine-tuning-vs-long-context` — code, config, or doc under docs/ or src/

#### Lesson 16.2: Ingestion pipelines (PDF, HTML, DOCX, APIs)
**Duration:** 2 hrs

**Concepts taught:**
- Ingestion pipelines (PDF, HTML, DOCX, APIs)
- How Ingestion pipelines (PDF, HTML, DOCX, APIs) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Build pipeline script: load PDF → chunk → embed → upsert vector DB
2. Query endpoint returning answer + source chunk IDs
3. Diagram pipeline in docs/rag-architecture.md

**Lesson deliverable:** Repo artifact for `ingestion-pipelines-pdf-html-docx-apis` — code, config, or doc under docs/ or src/

#### Lesson 16.3: Metadata schema design
**Duration:** 2 hrs

**Concepts taught:**
- Metadata schema design
- How Metadata schema design fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Metadata schema design
2. Implement a minimal working example of: Metadata schema design
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Metadata schema design' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `metadata-schema-design` — code, config, or doc under docs/ or src/

#### Lesson 16.4: Query transformation (HyDE, multi-query)
**Duration:** 2 hrs

**Concepts taught:**
- Query transformation (HyDE, multi-query)
- How Query transformation (HyDE, multi-query) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Query transformation (HyDE, multi-query)
2. Implement a minimal working example of: Query transformation (HyDE, multi-query)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Query transformation (HyDE, multi-query)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `query-transformation-hyde-multi-query` — code, config, or doc under docs/ or src/

#### Lesson 16.5: Citation and source attribution
**Duration:** 2 hrs

**Concepts taught:**
- Citation and source attribution
- How Citation and source attribution fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Citation and source attribution
2. Implement a minimal working example of: Citation and source attribution
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Citation and source attribution' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `citation-and-source-attribution` — code, config, or doc under docs/ or src/

#### Lesson 16.6: LangChain vs LlamaIndex vs Haystack comparison
**Duration:** 2 hrs

**Concepts taught:**
- LangChain vs LlamaIndex vs Haystack comparison
- How LangChain vs LlamaIndex vs Haystack comparison fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: LangChain vs LlamaIndex vs Haystack comparison
2. Implement a minimal working example of: LangChain vs LlamaIndex vs Haystack comparison
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'LangChain vs LlamaIndex vs Haystack comparison' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `langchain-vs-llamaindex-vs-haystack-comp` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
End-to-end RAG on 500-page policy PDF with source citations in UI.

**Enterprise project extension:**
ACL-aware metadata: user only retrieves permitted documents.

**Portfolio artifact:**
**Enterprise RAG Assistant** (flagship project #1).

**Tools & technologies:**
LangChain, LlamaIndex, Haystack, Unstructured.io, PyMuPDF

**Common mistakes:**
- Chunking entire PDFs as single blocks
- No metadata filtering before vector search
- Skipping evaluation entirely

**Industry best practices:**
- Document lineage IDs in chunks
- Stale content TTL and re-index jobs
- Show citations in UI always

**Interview preparation:**
- Whiteboard full RAG architecture for internal wiki Q&A
- "How do you reduce hallucinations in RAG?"

**Real-world use cases:**
HR policy bots, legal discovery assist, engineering runbooks.

**Topic deliverables (due end of week):**
RAG API with `/query` returning answer + sources + confidence; Ragas faithfulness ≥0.85 on test set.

## Week 16 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 16):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 17: Chunking & Embedding Strategies

**Hours:** 12–15 recommended | **Module:** 04

## Week 17 learning goals
Complete all lessons below. Submit week deliverable before starting Week 18.

### Topic 4.2: Chunking & Embedding Strategies

**Why this matters (job market):** Bad chunking causes 50%+ of production RAG failures. Senior interviews drill chunk size, overlap, and structure-aware splitting.

**Job roles:** RAG Engineer, LLM Engineer

**Learning objectives:**
- Apply recursive, semantic, and document-structure chunking
- Select embedding models for domain
- Tune chunk size/overlap with eval data

---

**Lessons this week:**

#### Lesson 17.1: Fixed vs recursive vs semantic chunking
**Duration:** 2 hrs

**Concepts taught:**
- Fixed vs recursive vs semantic chunking
- How Fixed vs recursive vs semantic chunking fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Split sample PDF with RecursiveCharacterTextSplitter sizes 256/512/1024
2. Run 10 test queries; record which chunk size wins on faithfulness
3. Document winning config in docs/chunking.md

**Lesson deliverable:** Repo artifact for `fixed-vs-recursive-vs-semantic-chunking` — code, config, or doc under docs/ or src/

#### Lesson 17.2: Parent-child chunk retrieval
**Duration:** 2 hrs

**Concepts taught:**
- Parent-child chunk retrieval
- Grounding LLM answers in retrieved context
- Measuring retrieval quality
- Golden datasets
- Regression gates before deploy

**Step-by-step activities:**
1. Split sample PDF with RecursiveCharacterTextSplitter sizes 256/512/1024
2. Run 10 test queries; record which chunk size wins on faithfulness
3. Document winning config in docs/chunking.md

**Lesson deliverable:** Repo artifact for `parent-child-chunk-retrieval` — code, config, or doc under docs/ or src/

#### Lesson 17.3: Embedding models: OpenAI, Cohere, BGE, E5
**Duration:** 2 hrs

**Concepts taught:**
- Embedding models: OpenAI, Cohere, BGE, E5
- How Embedding models: OpenAI, Cohere, BGE, E5 fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Embedding models: OpenAI, Cohere, BGE, E5
2. Implement a minimal working example of: Embedding models: OpenAI, Cohere, BGE, E5
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Embedding models: OpenAI, Cohere, BGE, E5' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `embedding-models-openai-cohere-bge-e5` — code, config, or doc under docs/ or src/

#### Lesson 17.4: Multilingual embeddings
**Duration:** 2 hrs

**Concepts taught:**
- Multilingual embeddings
- How Multilingual embeddings fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Multilingual embeddings
2. Implement a minimal working example of: Multilingual embeddings
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Multilingual embeddings' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `multilingual-embeddings` — code, config, or doc under docs/ or src/

#### Lesson 17.5: Dimensionality and index type tradeoffs
**Duration:** 2 hrs

**Concepts taught:**
- Dimensionality and index type tradeoffs
- How Dimensionality and index type tradeoffs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Dimensionality and index type tradeoffs
2. Implement a minimal working example of: Dimensionality and index type tradeoffs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Dimensionality and index type tradeoffs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `dimensionality-and-index-type-tradeoffs` — code, config, or doc under docs/ or src/

#### Lesson 17.6: Embedding cache layers
**Duration:** 2 hrs

**Concepts taught:**
- Embedding cache layers
- How Embedding cache layers fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Embedding cache layers
2. Implement a minimal working example of: Embedding cache layers
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Embedding cache layers' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `embedding-cache-layers` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Grid search chunk sizes 256–1024; plot MRR@5 vs faithfulness.

**Enterprise project extension:**
Structure-aware chunking for legal/clinical headers and tables.

**Portfolio artifact:**
`docs/chunking-experiments.md` with charts and winner config.

**Tools & technologies:**
LangChain text splitters, semantic-chunker, sentence-transformers

**Common mistakes:**
- Same chunk config for all doc types
- Re-embedding entire corpus daily without change detection
- Ignoring token limits in chunk headers

**Industry best practices:**
- Store chunk hash to skip unchanged re-embeds
- Version embedding model in index metadata
- Human spot-check 20 chunks per corpus

**Interview preparation:**
- "Your RAG misses table data—what do you change?"
- "Compare OpenAI ada-3 vs open-source embeddings for cost."

**Real-world use cases:**
Technical manuals with code blocks, SEC filings with tables.

**Topic deliverables (due end of week):**
Optimal chunk config documented with eval proof.

## Week 17 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 17):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 18: Vector Databases & Hybrid Search

**Hours:** 12–15 recommended | **Module:** 04

## Week 18 learning goals
Complete all lessons below. Submit week deliverable before starting Week 19.

### Topic 4.3: Vector Databases & Hybrid Search

**Why this matters (job market):** Vector DB skills (+9–10% premium). Enterprises require hybrid BM25 + vector for keyword-heavy queries.

**Job roles:** RAG Engineer, AI Platform Engineer

**Learning objectives:**
- Operate Pinecone, Weaviate, pgvector, or Milvus
- Implement hybrid search and metadata filters
- Plan index sizing, namespaces, multi-tenancy

---

**Lessons this week:**

#### Lesson 18.1: HNSW vs IVF index concepts (practical level)
**Duration:** 2 hrs

**Concepts taught:**
- HNSW vs IVF index concepts (practical level)
- How HNSW vs IVF index concepts (practical level) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: HNSW vs IVF index concepts (practical level)
2. Implement a minimal working example of: HNSW vs IVF index concepts (practical level)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'HNSW vs IVF index concepts (practical level)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `hnsw-vs-ivf-index-concepts-practical-lev` — code, config, or doc under docs/ or src/

#### Lesson 18.2: Pinecone / Weaviate / Milvus / pgvector setup
**Duration:** 2 hrs

**Concepts taught:**
- Pinecone / Weaviate / Milvus / pgvector setup
- How Pinecone / Weaviate / Milvus / pgvector setup fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Provision vector DB (local pgvector or Pinecone free tier)
2. Create index with metadata fields: tenant_id, doc_id, page
3. Query with metadata filter; verify tenant isolation

**Lesson deliverable:** Repo artifact for `pinecone-weaviate-milvus-pgvector-setup` — code, config, or doc under docs/ or src/

#### Lesson 18.3: Azure AI Search hybrid patterns
**Duration:** 2 hrs

**Concepts taught:**
- Azure AI Search hybrid patterns
- How Azure AI Search hybrid patterns fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Azure AI Search hybrid patterns
2. Implement a minimal working example of: Azure AI Search hybrid patterns
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Azure AI Search hybrid patterns' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `azure-ai-search-hybrid-patterns` — code, config, or doc under docs/ or src/

#### Lesson 18.4: BM25 + dense fusion (RRF)
**Duration:** 2 hrs

**Concepts taught:**
- BM25 + dense fusion (RRF)
- How BM25 + dense fusion (RRF) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: BM25 + dense fusion (RRF)
2. Implement a minimal working example of: BM25 + dense fusion (RRF)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'BM25 + dense fusion (RRF)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `bm25-dense-fusion-rrf` — code, config, or doc under docs/ or src/

#### Lesson 18.5: Namespace per tenant
**Duration:** 2 hrs

**Concepts taught:**
- Namespace per tenant
- How Namespace per tenant fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Namespace per tenant
2. Implement a minimal working example of: Namespace per tenant
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Namespace per tenant' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `namespace-per-tenant` — code, config, or doc under docs/ or src/

#### Lesson 18.6: Backup and index rebuild strategies
**Duration:** 2 hrs

**Concepts taught:**
- Backup and index rebuild strategies
- How Backup and index rebuild strategies fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Backup and index rebuild strategies
2. Implement a minimal working example of: Backup and index rebuild strategies
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Backup and index rebuild strategies' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `backup-and-index-rebuild-strategies` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Hybrid search beating pure vector on keyword-heavy eval subset by ≥15%.

**Enterprise project extension:**
Multi-tenant index isolation; per-tenant API keys and quotas.

**Portfolio artifact:**
Vector DB abstraction supporting 2 backends (e.g., pgvector + Pinecone).

**Tools & technologies:**
Pinecone, Weaviate, Milvus, pgvector, OpenSearch, Azure AI Search

**Common mistakes:**
- No metadata indexes for filter fields
- Single global index for all customers (data leak risk)
- Ignoring embedding dimension mismatches on model change

**Industry best practices:**
- Separate dev/staging/prod indexes
- Load test p95 retrieval latency
- Monitor index size growth and cost

**Interview preparation:**
- "Design multi-tenant vector storage."
- "When would you choose pgvector vs managed Pinecone?"

**Real-world use cases:**
E-commerce search, support KB, code search.

**Topic deliverables (due end of week):**
Hybrid retriever with filter API; p95 retrieval <200ms on benchmark.

## Week 18 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 18):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 19: Reranking, Caching & Retrieval Optimization

**Hours:** 12–15 recommended | **Module:** 04

## Week 19 learning goals
Complete all lessons below. Submit week deliverable before starting Week 20.

### Topic 4.4: Reranking, Query Routing & Semantic Caching

**Why this matters (job market):** Advanced RAG differentiates senior engineers—rerankers improve precision 20–40%; semantic cache cuts cost 30–50%.

**Job roles:** RAG Engineer, Senior AI Engineer

**Learning objectives:**
- Add cross-encoder reranking (Cohere, bge-reranker)
- Implement semantic cache for frequent queries
- Route queries to specialized retrievers

---

**Lessons this week:**

#### Lesson 19.1: Two-stage retrieve → rerank
**Duration:** 2 hrs

**Concepts taught:**
- Two-stage retrieve → rerank
- How Two-stage retrieve → rerank fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Two-stage retrieve → rerank
2. Implement a minimal working example of: Two-stage retrieve → rerank
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Two-stage retrieve → rerank' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `two-stage-retrieve-rerank` — code, config, or doc under docs/ or src/

#### Lesson 19.2: Cohere Rerank API vs open-source cross-encoders
**Duration:** 2 hrs

**Concepts taught:**
- Cohere Rerank API vs open-source cross-encoders
- How Cohere Rerank API vs open-source cross-encoders fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Cohere Rerank API vs open-source cross-encoders
2. Implement a minimal working example of: Cohere Rerank API vs open-source cross-encoders
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Cohere Rerank API vs open-source cross-encoders' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `cohere-rerank-api-vs-open-source-cross-e` — code, config, or doc under docs/ or src/

#### Lesson 19.3: Semantic cache (Redis, GPTCache)
**Duration:** 2 hrs

**Concepts taught:**
- Semantic cache (Redis, GPTCache)
- How Semantic cache (Redis, GPTCache) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Semantic cache (Redis, GPTCache)
2. Implement a minimal working example of: Semantic cache (Redis, GPTCache)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Semantic cache (Redis, GPTCache)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `semantic-cache-redis-gptcache` — code, config, or doc under docs/ or src/

#### Lesson 19.4: Query classification for router
**Duration:** 2 hrs

**Concepts taught:**
- Query classification for router
- APIRouter for modular routes
- Dependency injection pattern

**Step-by-step activities:**
1. Read official docs and module notes for: Query classification for router
2. Implement a minimal working example of: Query classification for router
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Query classification for router' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `query-classification-for-router` — code, config, or doc under docs/ or src/

#### Lesson 19.5: Contextual compression
**Duration:** 2 hrs

**Concepts taught:**
- Contextual compression
- How Contextual compression fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Contextual compression
2. Implement a minimal working example of: Contextual compression
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Contextual compression' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `contextual-compression` — code, config, or doc under docs/ or src/

#### Lesson 19.6: Lost-in-the-middle mitigation
**Duration:** 2 hrs

**Concepts taught:**
- Lost-in-the-middle mitigation
- How Lost-in-the-middle mitigation fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Lost-in-the-middle mitigation
2. Implement a minimal working example of: Lost-in-the-middle mitigation
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Lost-in-the-middle mitigation' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `lost-in-the-middle-mitigation` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Add reranker; measure nDCG@10 improvement; add cache hit rate metric.

**Enterprise project extension:**
Cache invalidation on document updates; per-tenant cache keys.

**Portfolio artifact:**
Cost/latency dashboard: cache hit %, reranker latency.

**Tools & technologies:**
Cohere Rerank, sentence-transformers cross-encoder, Redis, GPTCache

**Common mistakes:**
- Reranking 1000 docs (budget explosion)
- Cache without invalidation on source updates
- No diversity in retrieved chunks (redundant context)

**Industry best practices:**
- Retrieve top-50, rerank to top-5
- Log cache hits to FinOps dashboard
- MMR for diversity when needed

**Interview preparation:**
- "RAG is slow at 2s p95—optimization plan?"
- "Explain two-stage retrieval."

**Real-world use cases:**
High-QPS support bots, repeated FAQ queries.

**Topic deliverables (due end of week):**
Production retriever with rerank + cache; documented cost savings.

## Week 19 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 19):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 20: Advanced RAG — Graphs & Agentic RAG

**Hours:** 12–15 recommended | **Module:** 04

## Week 20 learning goals
Complete all lessons below. Submit week deliverable before starting Week 21.

### Topic 4.5: Knowledge Graphs, GraphRAG & Agentic RAG

**Why this matters (job market):** Microsoft GraphRAG and enterprise knowledge graphs trending for complex corpora (legal, intelligence, R&D).

**Job roles:** RAG Engineer, AI Architect, Applied AI Engineer

**Learning objectives:**
- Explain GraphRAG vs vector-only tradeoffs
- Combine graph traversal with vector retrieval
- Integrate RAG as tool inside agents (Module 05 link)

---

**Lessons this week:**

#### Lesson 20.1: Entity extraction and relation graphs
**Duration:** 2 hrs

**Concepts taught:**
- Entity extraction and relation graphs
- How Entity extraction and relation graphs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Entity extraction and relation graphs
2. Implement a minimal working example of: Entity extraction and relation graphs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Entity extraction and relation graphs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `entity-extraction-and-relation-graphs` — code, config, or doc under docs/ or src/

#### Lesson 20.2: Neo4j / Amazon Neptune basics
**Duration:** 2 hrs

**Concepts taught:**
- Neo4j / Amazon Neptune basics
- How Neo4j / Amazon Neptune basics fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Neo4j / Amazon Neptune basics
2. Implement a minimal working example of: Neo4j / Amazon Neptune basics
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Neo4j / Amazon Neptune basics' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `neo4j-amazon-neptune-basics` — code, config, or doc under docs/ or src/

#### Lesson 20.3: GraphRAG community summaries
**Duration:** 2 hrs

**Concepts taught:**
- GraphRAG community summaries
- Grounding LLM answers in retrieved context
- Measuring retrieval quality

**Step-by-step activities:**
1. Read official docs and module notes for: GraphRAG community summaries
2. Implement a minimal working example of: GraphRAG community summaries
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'GraphRAG community summaries' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `graphrag-community-summaries` — code, config, or doc under docs/ or src/

#### Lesson 20.4: Self-RAG, corrective RAG concepts
**Duration:** 2 hrs

**Concepts taught:**
- Self-RAG, corrective RAG concepts
- Grounding LLM answers in retrieved context
- Measuring retrieval quality

**Step-by-step activities:**
1. Read official docs and module notes for: Self-RAG, corrective RAG concepts
2. Implement a minimal working example of: Self-RAG, corrective RAG concepts
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Self-RAG, corrective RAG concepts' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `self-rag-corrective-rag-concepts` — code, config, or doc under docs/ or src/

#### Lesson 20.5: RAG + agent tool pattern
**Duration:** 2 hrs

**Concepts taught:**
- RAG + agent tool pattern
- Grounding LLM answers in retrieved context
- Measuring retrieval quality
- State management across agent steps
- Human-in-the-loop checkpoints

**Step-by-step activities:**
1. Read official docs and module notes for: RAG + agent tool pattern
2. Implement a minimal working example of: RAG + agent tool pattern
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'RAG + agent tool pattern' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `rag-agent-tool-pattern` — code, config, or doc under docs/ or src/

#### Lesson 20.6: Multimodal RAG (images in docs)
**Duration:** 2 hrs

**Concepts taught:**
- Multimodal RAG (images in docs)
- Grounding LLM answers in retrieved context
- Measuring retrieval quality

**Step-by-step activities:**
1. Read official docs and module notes for: Multimodal RAG (images in docs)
2. Implement a minimal working example of: Multimodal RAG (images in docs)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Multimodal RAG (images in docs)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `multimodal-rag-images-in-docs` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Optional graph layer for entity-centric queries ("Who reports to X?").

**Enterprise project extension:**
Hybrid Graph+Vector for org chart + policy docs.

**Portfolio artifact:**
Architecture diagram comparing vector-only vs graph-augmented.

**Tools & technologies:**
Neo4j, LlamaIndex KnowledgeGraph, Microsoft GraphRAG patterns

**Common mistakes:**
- Building graphs when clean metadata filters suffice
- Stale graph edges without refresh pipeline
- Over-engineering for MVP

**Industry best practices:**
- Start vector-only; add graph when eval shows entity failures
- Human-validated ontology for regulated domains

**Interview preparation:**
- "When is GraphRAG worth the complexity?"
- "Design RAG for 10M document corpus."

**Real-world use cases:**
M&A due diligence, pharma literature, supply chain knowledge.

**Topic deliverables (due end of week):**
Graph-augmented query path OR documented decision why not needed.

## Week 20 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 20):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 21: AI Agents & Tool Calling

**Hours:** 12–15 recommended | **Module:** 05

## Week 21 learning goals
Complete all lessons below. Submit week deliverable before starting Week 22.

### Topic 5.1: AI Agents, Tool Calling & Function Execution

**Why this matters (job market):** Agentic AI is the fastest-emerging JD category 2026–27. Tool calling is required for copilots, automation, and "AI employees."

**Job roles:** Agentic AI Engineer, AI Copilot Engineer, AI Automation Engineer, Generative AI Engineer

**Learning objectives:**
- Implement OpenAI/Anthropic tool calling loops
- Design safe tool schemas with validation
- Handle tool errors and timeouts

---

**Lessons this week:**

#### Lesson 21.1: Agent vs chain vs workflow
**Duration:** 2 hrs

**Concepts taught:**
- Agent vs chain vs workflow
- State management across agent steps
- Human-in-the-loop checkpoints

**Step-by-step activities:**
1. Read official docs and module notes for: Agent vs chain vs workflow
2. Implement a minimal working example of: Agent vs chain vs workflow
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Agent vs chain vs workflow' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `agent-vs-chain-vs-workflow` — code, config, or doc under docs/ or src/

#### Lesson 21.2: Tool schema design (JSON Schema)
**Duration:** 2 hrs

**Concepts taught:**
- Tool schema design (JSON Schema)
- How Tool schema design (JSON Schema) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Tool schema design (JSON Schema)
2. Implement a minimal working example of: Tool schema design (JSON Schema)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Tool schema design (JSON Schema)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `tool-schema-design-json-schema` — code, config, or doc under docs/ or src/

#### Lesson 21.3: ReAct pattern
**Duration:** 2 hrs

**Concepts taught:**
- ReAct pattern
- How ReAct pattern fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: ReAct pattern
2. Implement a minimal working example of: ReAct pattern
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'ReAct pattern' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `react-pattern` — code, config, or doc under docs/ or src/

#### Lesson 21.4: Parallel vs sequential tool calls
**Duration:** 2 hrs

**Concepts taught:**
- Parallel vs sequential tool calls
- How Parallel vs sequential tool calls fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Parallel vs sequential tool calls
2. Implement a minimal working example of: Parallel vs sequential tool calls
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Parallel vs sequential tool calls' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `parallel-vs-sequential-tool-calls` — code, config, or doc under docs/ or src/

#### Lesson 21.5: Idempotent tools
**Duration:** 2 hrs

**Concepts taught:**
- Idempotent tools
- How Idempotent tools fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Idempotent tools
2. Implement a minimal working example of: Idempotent tools
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Idempotent tools' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `idempotent-tools` — code, config, or doc under docs/ or src/

#### Lesson 21.6: MCP (Model Context Protocol) intro
**Duration:** 2 hrs

**Concepts taught:**
- MCP (Model Context Protocol) intro
- How MCP (Model Context Protocol) intro fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: MCP (Model Context Protocol) intro
2. Implement a minimal working example of: MCP (Model Context Protocol) intro
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'MCP (Model Context Protocol) intro' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `mcp-model-context-protocol-intro` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Agent with tools: `search_kb`, `create_ticket`, `get_weather` (mock)—max 5 steps.

**Enterprise project extension:**
Tool registry with RBAC: role A cannot call `delete_record`.

**Portfolio artifact:**
Tool catalog documented in OpenAPI-style spec.

**Tools & technologies:**
LangChain tools, OpenAI function calling, MCP servers

**Common mistakes:**
- Tools with side effects and no confirmation
- Unbounded agent loops
- Passing raw user input to SQL/shell tools

**Industry best practices:**
- Max iteration limits and step budgets
- Confirm destructive actions (HITL)
- Audit log every tool invocation

**Interview preparation:**
- "Design agent tools for a sales copilot."
- "What happens when a tool call fails mid-agent?"

**Real-world use cases:**
CRM updates, calendar scheduling, internal API actions.

**Topic deliverables (due end of week):**
Agent completing 10-task eval suite with tool success rate ≥90%.

## Week 21 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 21):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 22: LangGraph — Stateful Agent Workflows

**Hours:** 12–15 recommended | **Module:** 05

## Week 22 learning goals
Complete all lessons below. Submit week deliverable before starting Week 23.

### Topic 5.2: LangGraph for Production Agent Workflows

**Why this matters (job market):** LangGraph is the de facto standard in US JDs for stateful agents—graphs, checkpoints, human-in-the-loop.

**Job roles:** Agentic AI Engineer, AI Workflow Engineer, LLM Engineer

**Learning objectives:**
- Build StateGraph with nodes and conditional edges
- Persist state with checkpointers (Postgres/Redis)
- Implement human-in-the-loop interrupts

---

**Lessons this week:**

#### Lesson 22.1: Graph nodes: planner, executor, critic
**Duration:** 2 hrs

**Concepts taught:**
- Graph nodes: planner, executor, critic
- How Graph nodes: planner, executor, critic fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Graph nodes: planner, executor, critic
2. Implement a minimal working example of: Graph nodes: planner, executor, critic
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Graph nodes: planner, executor, critic' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `graph-nodes-planner-executor-critic` — code, config, or doc under docs/ or src/

#### Lesson 22.2: Conditional routing
**Duration:** 2 hrs

**Concepts taught:**
- Conditional routing
- How Conditional routing fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Conditional routing
2. Implement a minimal working example of: Conditional routing
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Conditional routing' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `conditional-routing` — code, config, or doc under docs/ or src/

#### Lesson 22.3: Memory: short-term vs long-term
**Duration:** 2 hrs

**Concepts taught:**
- Memory: short-term vs long-term
- How Memory: short-term vs long-term fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Memory: short-term vs long-term
2. Implement a minimal working example of: Memory: short-term vs long-term
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Memory: short-term vs long-term' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `memory-short-term-vs-long-term` — code, config, or doc under docs/ or src/

#### Lesson 22.4: Checkpointing and resume
**Duration:** 2 hrs

**Concepts taught:**
- Checkpointing and resume
- How Checkpointing and resume fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Install langgraph; define StateGraph with 3 nodes
2. Add PostgresSaver checkpointer; restart mid-run and resume
3. Stream node events to log for debugging

**Lesson deliverable:** Repo artifact for `checkpointing-and-resume` — code, config, or doc under docs/ or src/

#### Lesson 22.5: Subgraphs and multi-agent handoff
**Duration:** 2 hrs

**Concepts taught:**
- Subgraphs and multi-agent handoff
- State management across agent steps
- Human-in-the-loop checkpoints

**Step-by-step activities:**
1. Read official docs and module notes for: Subgraphs and multi-agent handoff
2. Implement a minimal working example of: Subgraphs and multi-agent handoff
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Subgraphs and multi-agent handoff' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `subgraphs-and-multi-agent-handoff` — code, config, or doc under docs/ or src/

#### Lesson 22.6: Streaming graph events to UI
**Duration:** 2 hrs

**Concepts taught:**
- Streaming graph events to UI
- How Streaming graph events to UI fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Streaming graph events to UI
2. Implement a minimal working example of: Streaming graph events to UI
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Streaming graph events to UI' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `streaming-graph-events-to-ui` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Support triage graph: classify → retrieve → draft → human approve → send.

**Enterprise project extension:**
Tenant-isolated thread store; SLA timers on HITL steps.

**Portfolio artifact:**
**Autonomous Research Agent** or **AI Customer Support** with LangGraph.

**Tools & technologies:**
LangGraph, LangChain, Postgres checkpointer, Redis

**Common mistakes:**
- God-graph with 20 nodes (unmaintainable)
- No persistence (lost on restart)
- Missing timeout on HITL waits

**Industry best practices:**
- Small composable subgraphs
- Visualize graph for stakeholders
- Version graph definitions in Git

**Interview preparation:**
- Draw LangGraph for research agent with 4 nodes
- "How do you resume a failed multi-hour agent run?"

**Real-world use cases:**
Approval workflows, incident response agents, research pipelines.

**Topic deliverables (due end of week):**
LangGraph agent with checkpoint resume demo video/GIF in README.

## Week 22 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 22):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 23: Multi-Agent Systems — CrewAI & AutoGen

**Hours:** 12–15 recommended | **Module:** 05

## Week 23 learning goals
Complete all lessons below. Submit week deliverable before starting Week 24.

### Topic 5.3: Multi-Agent Systems — CrewAI & AutoGen

**Why this matters (job market):** Enterprises deploy specialist agent teams (analyst + writer + critic). CrewAI and AutoGen appear frequently in senior agentic roles.

**Job roles:** Agentic AI Engineer, Applied AI Engineer, AI Consultant

**Learning objectives:**
- Model roles, goals, and delegation in CrewAI
- Run AutoGen group chats with termination conditions
- Compare frameworks for project fit

---

**Lessons this week:**

#### Lesson 23.1: CrewAI: crews, tasks, hierarchical process
**Duration:** 2 hrs

**Concepts taught:**
- CrewAI: crews, tasks, hierarchical process
- How CrewAI: crews, tasks, hierarchical process fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: CrewAI: crews, tasks, hierarchical process
2. Implement a minimal working example of: CrewAI: crews, tasks, hierarchical process
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'CrewAI: crews, tasks, hierarchical process' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `crewai-crews-tasks-hierarchical-process` — code, config, or doc under docs/ or src/

#### Lesson 23.2: AutoGen: conversable agents, GroupChat
**Duration:** 2 hrs

**Concepts taught:**
- AutoGen: conversable agents, GroupChat
- State management across agent steps
- Human-in-the-loop checkpoints

**Step-by-step activities:**
1. Read official docs and module notes for: AutoGen: conversable agents, GroupChat
2. Implement a minimal working example of: AutoGen: conversable agents, GroupChat
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'AutoGen: conversable agents, GroupChat' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `autogen-conversable-agents-groupchat` — code, config, or doc under docs/ or src/

#### Lesson 23.3: Debate / critic patterns
**Duration:** 2 hrs

**Concepts taught:**
- Debate / critic patterns
- How Debate / critic patterns fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Debate / critic patterns
2. Implement a minimal working example of: Debate / critic patterns
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Debate / critic patterns' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `debate-critic-patterns` — code, config, or doc under docs/ or src/

#### Lesson 23.4: Cost control in multi-agent (N× tokens)
**Duration:** 2 hrs

**Concepts taught:**
- Cost control in multi-agent (N× tokens)
- State management across agent steps
- Human-in-the-loop checkpoints

**Step-by-step activities:**
1. Read official docs and module notes for: Cost control in multi-agent (N× tokens)
2. Implement a minimal working example of: Cost control in multi-agent (N× tokens)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Cost control in multi-agent (N× tokens)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `cost-control-in-multi-agent-n-tokens` — code, config, or doc under docs/ or src/

#### Lesson 23.5: When single agent beats multi-agent
**Duration:** 2 hrs

**Concepts taught:**
- When single agent beats multi-agent
- State management across agent steps
- Human-in-the-loop checkpoints

**Step-by-step activities:**
1. Read official docs and module notes for: When single agent beats multi-agent
2. Implement a minimal working example of: When single agent beats multi-agent
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'When single agent beats multi-agent' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `when-single-agent-beats-multi-agent` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
3-agent crew: Researcher → Analyst → Report Writer on earnings data.

**Enterprise project extension:**
**Multi-Agent Finance Analyst** with audit trail of agent messages.

**Portfolio artifact:**
Cost comparison: 1 agent vs 3 agents on same task.

**Tools & technologies:**
CrewAI, AutoGen, LangGraph (multi-agent mode)

**Common mistakes:**
- Multi-agent for tasks solvable by one pass
- No shared memory contract between agents
- Exploding token costs

**Industry best practices:**
- Cap rounds and token budget per crew
- Shared blackboard state object
- Human review before external actions

**Interview preparation:**
- "When would you use multi-agent vs single LangGraph?"
- "How do you prevent agent infinite debate loops?"

**Real-world use cases:**
Investment research, marketing campaign generation, code review teams.

**Topic deliverables (due end of week):**
Multi-agent project with message log export and final report artifact.

## Week 23 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 23):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 24: Browser, Code Agents & AI Employees

**Hours:** 12–15 recommended | **Module:** 05

## Week 24 learning goals
Complete all lessons below. Submit week deliverable before starting Week 25.

### Topic 5.4: Browser Agents, Code Agents & AI Employees

**Why this matters (job market):** 2026–27 trend: agents that operate UIs and codebases (computer use, Devin-class patterns)—high value, high risk.

**Job roles:** Agentic AI Engineer, AI Copilot Engineer, AI Automation Engineer

**Learning objectives:**
- Understand browser automation agent architectures
- Build code agent with sandboxed execution
- Apply safety boundaries for autonomous workers

---

**Lessons this week:**

#### Lesson 24.1: Playwright + LLM vision/action loops
**Duration:** 2 hrs

**Concepts taught:**
- Playwright + LLM vision/action loops
- How Playwright + LLM vision/action loops fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Playwright + LLM vision/action loops
2. Implement a minimal working example of: Playwright + LLM vision/action loops
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Playwright + LLM vision/action loops' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `playwright-llm-vision-action-loops` — code, config, or doc under docs/ or src/

#### Lesson 24.2: Anthropic computer use patterns
**Duration:** 2 hrs

**Concepts taught:**
- Anthropic computer use patterns
- How Anthropic computer use patterns fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Anthropic computer use patterns
2. Implement a minimal working example of: Anthropic computer use patterns
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Anthropic computer use patterns' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `anthropic-computer-use-patterns` — code, config, or doc under docs/ or src/

#### Lesson 24.3: Code interpreter sandboxes (Docker, E2B)
**Duration:** 2 hrs

**Concepts taught:**
- Code interpreter sandboxes (Docker, E2B)
- Layer caching in builds
- Non-root user in container
- .dockerignore

**Step-by-step activities:**
1. Read official docs and module notes for: Code interpreter sandboxes (Docker, E2B)
2. Implement a minimal working example of: Code interpreter sandboxes (Docker, E2B)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Code interpreter sandboxes (Docker, E2B)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `code-interpreter-sandboxes-docker-e2b` — code, config, or doc under docs/ or src/

#### Lesson 24.4: AI employee workflow (email, CRM, calendar)
**Duration:** 2 hrs

**Concepts taught:**
- AI employee workflow (email, CRM, calendar)
- How AI employee workflow (email, CRM, calendar) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: AI employee workflow (email, CRM, calendar)
2. Implement a minimal working example of: AI employee workflow (email, CRM, calendar)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'AI employee workflow (email, CRM, calendar)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `ai-employee-workflow-email-crm-calendar` — code, config, or doc under docs/ or src/

#### Lesson 24.5: Scheduling and watchdog processes
**Duration:** 2 hrs

**Concepts taught:**
- Scheduling and watchdog processes
- How Scheduling and watchdog processes fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Scheduling and watchdog processes
2. Implement a minimal working example of: Scheduling and watchdog processes
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Scheduling and watchdog processes' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `scheduling-and-watchdog-processes` — code, config, or doc under docs/ or src/

#### Lesson 24.6: Legal/ethical boundaries
**Duration:** 2 hrs

**Concepts taught:**
- Legal/ethical boundaries
- How Legal/ethical boundaries fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Legal/ethical boundaries
2. Implement a minimal working example of: Legal/ethical boundaries
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Legal/ethical boundaries' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `legal-ethical-boundaries` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Code agent: fix failing unit test in sandbox repo (read-only git except patch branch).

**Enterprise project extension:**
**AI DevOps Assistant** — read logs, suggest fixes, open PR (HITL merge).

**Portfolio artifact:**
Sandbox-only browser agent demo (no production credentials).

**Tools & technologies:**
Playwright, E2B, Docker sandboxes, Semantic Kernel plugins

**Common mistakes:**
- Production credentials in agent environment
- No kill switch or spend cap
- Full internet access from code agent

**Industry best practices:**
- Ephemeral VMs per task
- Allowlist domains for browser agents
- Mandatory HITL for external communications

**Interview preparation:**
- "How do you sandbox an autonomous code agent?"
- "Risks of browser agents in enterprise?"

**Real-world use cases:**
QA automation, L1 support, routine data entry, CI triage.

**Topic deliverables (due end of week):**
Sandboxed code or browser agent with security section in README.

## Week 24 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 24):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 25: Semantic Kernel & Enterprise Agents

**Hours:** 12–15 recommended | **Module:** 05

## Week 25 learning goals
Complete all lessons below. Submit week deliverable before starting Week 26.

### Topic 5.5: Semantic Kernel & Microsoft Enterprise Agent Patterns

**Why this matters (job market):** Fortune 500 Microsoft shops standardize on Semantic Kernel + Azure—consulting and enterprise roles expect awareness.

**Job roles:** Enterprise AI Engineer, AI Solutions Engineer, AI Integration Engineer

**Learning objectives:**
- Build SK plugins and planners
- Integrate with Azure OpenAI and Microsoft Graph
- Map SK concepts to LangGraph mental model

---

**Lessons this week:**

#### Lesson 25.1: SK plugins and kernel
**Duration:** 2 hrs

**Concepts taught:**
- SK plugins and kernel
- How SK plugins and kernel fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: SK plugins and kernel
2. Implement a minimal working example of: SK plugins and kernel
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'SK plugins and kernel' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `sk-plugins-and-kernel` — code, config, or doc under docs/ or src/

#### Lesson 25.2: Planners vs explicit graphs
**Duration:** 2 hrs

**Concepts taught:**
- Planners vs explicit graphs
- How Planners vs explicit graphs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Planners vs explicit graphs
2. Implement a minimal working example of: Planners vs explicit graphs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Planners vs explicit graphs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `planners-vs-explicit-graphs` — code, config, or doc under docs/ or src/

#### Lesson 25.3: Azure OpenAI integration
**Duration:** 2 hrs

**Concepts taught:**
- Azure OpenAI integration
- How Azure OpenAI integration fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Azure OpenAI integration
2. Implement a minimal working example of: Azure OpenAI integration
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Azure OpenAI integration' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `azure-openai-integration` — code, config, or doc under docs/ or src/

#### Lesson 25.4: Copilot extensibility patterns
**Duration:** 2 hrs

**Concepts taught:**
- Copilot extensibility patterns
- How Copilot extensibility patterns fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Copilot extensibility patterns
2. Implement a minimal working example of: Copilot extensibility patterns
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Copilot extensibility patterns' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `copilot-extensibility-patterns` — code, config, or doc under docs/ or src/

#### Lesson 25.5: Entra ID auth for enterprise tools
**Duration:** 2 hrs

**Concepts taught:**
- Entra ID auth for enterprise tools
- How Entra ID auth for enterprise tools fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Entra ID auth for enterprise tools
2. Implement a minimal working example of: Entra ID auth for enterprise tools
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Entra ID auth for enterprise tools' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `entra-id-auth-for-enterprise-tools` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
SK plugin calling SharePoint mock API for document retrieval.

**Enterprise project extension:**
Microsoft-stack copilot POC for intranet search.

**Portfolio artifact:**
Side-by-side: same agent in LangGraph and SK (architecture doc).

**Tools & technologies:**
Semantic Kernel (.NET/Python), Azure OpenAI, Microsoft Graph API

**Common mistakes:**
- Ignoring Azure-specific auth flows
- Assuming SK planner is production-ready without tests

**Industry best practices:**
- Follow Microsoft reference architectures
- Use managed identity in Azure
- Align with customer's existing M365 security

**Interview preparation:**
- "Experience with Semantic Kernel vs LangChain?"
- "Integrate copilot with SharePoint and Teams."

**Real-world use cases:**
M365 copilots, internal IT helpdesk, field service apps.

**Topic deliverables (due end of week):**
SK-based demo OR documented enterprise Microsoft path in portfolio.

## Week 25 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 25):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 26: LLM Observability & Tracing

**Hours:** 12–15 recommended | **Module:** 06

## Week 26 learning goals
Complete all lessons below. Submit week deliverable before starting Week 27.

### Topic 6.1: LLM Observability — Tracing, Metrics & Monitoring

**Why this matters (job market):** 70%+ senior JDs mention tracing/observability. You cannot operate production AI without Langfuse/OpenTelemetry and cost dashboards.

**Job roles:** LLMOps Engineer, AI Reliability Engineer, AI Platform Engineer

**Learning objectives:**
- Instrument LLM calls with OpenTelemetry
- Use Langfuse for trace visualization
- Define SLIs: latency, error rate, cost/query, faithfulness

---

**Lessons this week:**

#### Lesson 26.1: Traces, spans, attributes for LLM
**Duration:** 2 hrs

**Concepts taught:**
- Traces, spans, attributes for LLM
- How Traces, spans, attributes for LLM fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Traces, spans, attributes for LLM
2. Implement a minimal working example of: Traces, spans, attributes for LLM
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Traces, spans, attributes for LLM' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `traces-spans-attributes-for-llm` — code, config, or doc under docs/ or src/

#### Lesson 26.2: Langfuse + OpenTelemetry integration
**Duration:** 2 hrs

**Concepts taught:**
- Langfuse + OpenTelemetry integration
- How Langfuse + OpenTelemetry integration fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Create Langfuse project; add keys to .env
2. Wrap LLM call and retriever call in spans
3. View full trace in Langfuse UI; screenshot for README

**Lesson deliverable:** Repo artifact for `langfuse-opentelemetry-integration` — code, config, or doc under docs/ or src/

#### Lesson 26.3: Prometheus/Grafana dashboards
**Duration:** 2 hrs

**Concepts taught:**
- Prometheus/Grafana dashboards
- How Prometheus/Grafana dashboards fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Prometheus/Grafana dashboards
2. Implement a minimal working example of: Prometheus/Grafana dashboards
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Prometheus/Grafana dashboards' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `prometheus-grafana-dashboards` — code, config, or doc under docs/ or src/

#### Lesson 26.4: Alerting on error spikes and cost anomalies
**Duration:** 2 hrs

**Concepts taught:**
- Alerting on error spikes and cost anomalies
- How Alerting on error spikes and cost anomalies fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Alerting on error spikes and cost anomalies
2. Implement a minimal working example of: Alerting on error spikes and cost anomalies
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Alerting on error spikes and cost anomalies' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `alerting-on-error-spikes-and-cost-anomal` — code, config, or doc under docs/ or src/

#### Lesson 26.5: User/session correlation IDs
**Duration:** 2 hrs

**Concepts taught:**
- User/session correlation IDs
- How User/session correlation IDs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: User/session correlation IDs
2. Implement a minimal working example of: User/session correlation IDs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'User/session correlation IDs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `user-session-correlation-ids` — code, config, or doc under docs/ or src/

#### Lesson 26.6: PII scrubbing in traces
**Duration:** 2 hrs

**Concepts taught:**
- PII scrubbing in traces
- How PII scrubbing in traces fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: PII scrubbing in traces
2. Implement a minimal working example of: PII scrubbing in traces
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'PII scrubbing in traces' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `pii-scrubbing-in-traces` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Full trace from API → retriever → LLM → response; Grafana dashboard.

**Enterprise project extension:**
Per-tenant cost attribution; weekly FinOps report automation.

**Portfolio artifact:**
Live dashboard screenshot in README.

**Tools & technologies:**
Langfuse, OpenTelemetry, Prometheus, Grafana, Datadog (concepts)

**Common mistakes:**
- Logging full prompts with PII
- No trace ID across microservices
- Alerts only on 500s, not quality degradation

**Industry best practices:**
- Sample traces in prod (1–10%) for cost
- Separate dev/staging/prod Langfuse projects
- Runbooks linked from alerts

**Interview preparation:**
- "Production LLM service is failing—debugging workflow?"
- "What metrics do you put on an AI SLA dashboard?"

**Real-world use cases:**
24/7 copilots, high-volume RAG, multi-tenant SaaS.

**Topic deliverables (due end of week):**
Observability stack on RAG project; p99 latency and $/1K queries visible.

## Week 26 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 26):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 27: AI Evaluation Pipelines

**Hours:** 12–15 recommended | **Module:** 06

## Week 27 learning goals
Complete all lessons below. Submit week deliverable before starting Week 28.

### Topic 6.2: AI Evaluation Pipelines

**Why this matters (job market):** #1 gap between tutorials and enterprise. Hiring managers ask "how do you know it works?"—eval CI is the answer.

**Job roles:** LLMOps Engineer, RAG Engineer, Responsible AI Engineer

**Learning objectives:**
- Build golden datasets for RAG and agents
- Run Ragas, DeepEval, promptfoo in CI
- Gate releases on regression thresholds

---

**Lessons this week:**

#### Lesson 27.1: Faithfulness, relevance, context precision/recall
**Duration:** 2 hrs

**Concepts taught:**
- Faithfulness, relevance, context precision/recall
- How Faithfulness, relevance, context precision/recall fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Create golden CSV: question, expected_sources, reference_answer
2. Run Ragas evaluate(); record faithfulness score
3. Add GitHub Action failing if score drops >5%

**Lesson deliverable:** Repo artifact for `faithfulness-relevance-context-precision` — code, config, or doc under docs/ or src/

#### Lesson 27.2: Ragas metrics pipeline
**Duration:** 2 hrs

**Concepts taught:**
- Ragas metrics pipeline
- Grounding LLM answers in retrieved context
- Measuring retrieval quality
- Golden datasets
- Regression gates before deploy

**Step-by-step activities:**
1. Create golden CSV: question, expected_sources, reference_answer
2. Run Ragas evaluate(); record faithfulness score
3. Add GitHub Action failing if score drops >5%

**Lesson deliverable:** Repo artifact for `ragas-metrics-pipeline` — code, config, or doc under docs/ or src/

#### Lesson 27.3: DeepEval test cases
**Duration:** 2 hrs

**Concepts taught:**
- DeepEval test cases
- Golden datasets
- Regression gates before deploy

**Step-by-step activities:**
1. Read official docs and module notes for: DeepEval test cases
2. Implement a minimal working example of: DeepEval test cases
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'DeepEval test cases' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `deepeval-test-cases` — code, config, or doc under docs/ or src/

#### Lesson 27.4: promptfoo YAML suites
**Duration:** 2 hrs

**Concepts taught:**
- promptfoo YAML suites
- How promptfoo YAML suites fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: promptfoo YAML suites
2. Implement a minimal working example of: promptfoo YAML suites
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'promptfoo YAML suites' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `promptfoo-yaml-suites` — code, config, or doc under docs/ or src/

#### Lesson 27.5: LLM-as-judge pitfalls
**Duration:** 2 hrs

**Concepts taught:**
- LLM-as-judge pitfalls
- How LLM-as-judge pitfalls fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: LLM-as-judge pitfalls
2. Implement a minimal working example of: LLM-as-judge pitfalls
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'LLM-as-judge pitfalls' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `llm-as-judge-pitfalls` — code, config, or doc under docs/ or src/

#### Lesson 27.6: Human eval sampling
**Duration:** 2 hrs

**Concepts taught:**
- Human eval sampling
- Golden datasets
- Regression gates before deploy

**Step-by-step activities:**
1. Read official docs and module notes for: Human eval sampling
2. Implement a minimal working example of: Human eval sampling
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Human eval sampling' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `human-eval-sampling` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
GitHub Action fails if faithfulness drops >5% vs baseline.

**Enterprise project extension:**
Golden set per tenant vertical; weekly human audit sample.

**Portfolio artifact:**
Eval badge in README: "Faithfulness 0.87 on 100-case suite."

**Tools & technologies:**
Ragas, DeepEval, promptfoo, LangSmith evals

**Common mistakes:**
- Eval set too small or leaked into training prompts
- Only offline eval, no production feedback loop
- Changing metrics without versioning

**Industry best practices:**
- Version golden datasets in DVC/Git LFS
- Track eval history over time
- Combine automated + weekly human review

**Interview preparation:**
- "Design eval pipeline for RAG chatbot."
- "LLM-as-judge biased toward GPT—mitigation?"

**Real-world use cases:**
Release gates, A/B prompt tests, vendor model comparisons.

**Topic deliverables (due end of week):**
CI eval gate on main project; eval report artifact per release.

## Week 27 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 27):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 28: Prompt Versioning & AI CI/CD

**Hours:** 12–15 recommended | **Module:** 06

## Week 28 learning goals
Complete all lessons below. Submit week deliverable before starting Week 29.

### Topic 6.3: Prompt Versioning, Experiments & AI CI/CD

**Why this matters (job market):** LLMOps Engineers own "CI/CD for prompts"—same rigor as code deploys.

**Job roles:** LLMOps Engineer, AI Platform Engineer

**Learning objectives:**
- Version prompts/models in registry
- Track experiments (MLflow/W&B for LLM)
- Implement canary prompt deployments

---

**Lessons this week:**

#### Lesson 28.1: Prompt registry patterns
**Duration:** 2 hrs

**Concepts taught:**
- Prompt registry patterns
- How Prompt registry patterns fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Prompt registry patterns
2. Implement a minimal working example of: Prompt registry patterns
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Prompt registry patterns' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `prompt-registry-patterns` — code, config, or doc under docs/ or src/

#### Lesson 28.2: MLflow LLM tracking
**Duration:** 2 hrs

**Concepts taught:**
- MLflow LLM tracking
- How MLflow LLM tracking fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: MLflow LLM tracking
2. Implement a minimal working example of: MLflow LLM tracking
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'MLflow LLM tracking' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `mlflow-llm-tracking` — code, config, or doc under docs/ or src/

#### Lesson 28.3: Feature flags for prompts
**Duration:** 2 hrs

**Concepts taught:**
- Feature flags for prompts
- How Feature flags for prompts fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Feature flags for prompts
2. Implement a minimal working example of: Feature flags for prompts
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Feature flags for prompts' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `feature-flags-for-prompts` — code, config, or doc under docs/ or src/

#### Lesson 28.4: Canary 5% → 50% → 100% rollout
**Duration:** 2 hrs

**Concepts taught:**
- Canary 5% → 50% → 100% rollout
- How Canary 5% → 50% → 100% rollout fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Canary 5% → 50% → 100% rollout
2. Implement a minimal working example of: Canary 5% → 50% → 100% rollout
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Canary 5% → 50% → 100% rollout' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `canary-5-50-100-rollout` — code, config, or doc under docs/ or src/

#### Lesson 28.5: Rollback procedures
**Duration:** 2 hrs

**Concepts taught:**
- Rollback procedures
- How Rollback procedures fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Rollback procedures
2. Implement a minimal working example of: Rollback procedures
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Rollback procedures' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `rollback-procedures` — code, config, or doc under docs/ or src/

#### Lesson 28.6: Artifact promotion dev→staging→prod
**Duration:** 2 hrs

**Concepts taught:**
- Artifact promotion dev→staging→prod
- How Artifact promotion dev→staging→prod fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Artifact promotion dev→staging→prod
2. Implement a minimal working example of: Artifact promotion dev→staging→prod
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Artifact promotion dev→staging→prod' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `artifact-promotion-dev-staging-prod` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Prompt v2 canary with automatic rollback on eval failure.

**Enterprise project extension:**
Change advisory for prod prompt changes; audit who approved.

**Portfolio artifact:**
`CHANGELOG-prompts.md` with metric deltas per version.

**Tools & technologies:**
MLflow, Langfuse prompts, LaunchDarkly, GitHub Actions

**Common mistakes:**
- Hot-editing prod prompts in dashboard without Git
- No rollback tested
- Canary without stat significance

**Industry best practices:**
- Every prompt change = PR + eval
- Immutable prompt artifacts in registry
- Post-deploy monitoring window 24h

**Interview preparation:**
- "How do you deploy a new system prompt safely?"
- "CI pipeline stages for an AI feature."

**Real-world use cases:**
Seasonal prompt updates, model upgrades, compliance text changes.

**Topic deliverables (due end of week):**
Full AI CI/CD diagram + working canary on one project.

## Week 28 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 28):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 29: Guardrails, Governance & Model Registry

**Hours:** 12–15 recommended | **Module:** 06

## Week 29 learning goals
Complete all lessons below. Submit week deliverable before starting Week 30.

### Topic 6.4: Guardrails, Governance & Model Registry

**Why this matters (job market):** Enterprise LLMOps requires guardrails (toxicity, PII, topic boundaries) and model governance for audits.

**Job roles:** LLMOps Engineer, Responsible AI Engineer, Enterprise AI Engineer

**Learning objectives:**
- Deploy NeMo Guardrails or equivalent
- Maintain model/prompt registry with approvals
- Document lineage for compliance

---

**Lessons this week:**

#### Lesson 29.1: Input/output guardrails
**Duration:** 2 hrs

**Concepts taught:**
- Input/output guardrails
- How Input/output guardrails fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Input/output guardrails
2. Implement a minimal working example of: Input/output guardrails
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Input/output guardrails' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `input-output-guardrails` — code, config, or doc under docs/ or src/

#### Lesson 29.2: Topic restriction rails
**Duration:** 2 hrs

**Concepts taught:**
- Topic restriction rails
- How Topic restriction rails fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Topic restriction rails
2. Implement a minimal working example of: Topic restriction rails
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Topic restriction rails' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `topic-restriction-rails` — code, config, or doc under docs/ or src/

#### Lesson 29.3: PII detection and redaction
**Duration:** 2 hrs

**Concepts taught:**
- PII detection and redaction
- How PII detection and redaction fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: PII detection and redaction
2. Implement a minimal working example of: PII detection and redaction
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'PII detection and redaction' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `pii-detection-and-redaction` — code, config, or doc under docs/ or src/

#### Lesson 29.4: Model cards and risk tiers
**Duration:** 2 hrs

**Concepts taught:**
- Model cards and risk tiers
- How Model cards and risk tiers fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Model cards and risk tiers
2. Implement a minimal working example of: Model cards and risk tiers
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Model cards and risk tiers' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `model-cards-and-risk-tiers` — code, config, or doc under docs/ or src/

#### Lesson 29.5: Approval workflows
**Duration:** 2 hrs

**Concepts taught:**
- Approval workflows
- How Approval workflows fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Approval workflows
2. Implement a minimal working example of: Approval workflows
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Approval workflows' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `approval-workflows` — code, config, or doc under docs/ or src/

#### Lesson 29.6: Retention policies for logs
**Duration:** 2 hrs

**Concepts taught:**
- Retention policies for logs
- How Retention policies for logs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Retention policies for logs
2. Implement a minimal working example of: Retention policies for logs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Retention policies for logs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `retention-policies-for-logs` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Block medical advice in non-health bot; log guardrail triggers.

**Enterprise project extension:**
Governance pack: model card, DPIA template, retention config.

**Portfolio artifact:**
Guardrail trigger rate metric in observability dashboard.

**Tools & technologies:**
NeMo Guardrails, Guardrails AI, custom classifiers, MLflow Model Registry

**Common mistakes:**
- Guardrails only in demo, not prod path
- No logging when guardrails fire
- Registry without owner and review date

**Industry best practices:**
- Fail closed for high-risk domains
- Regular red-team updates to guardrail tests
- Quarterly registry review

**Interview preparation:**
- "Implement guardrails without killing UX latency."
- "Model registry fields for SOC2 audit?"

**Real-world use cases:**
Regulated chatbots, HR bots, financial advice boundaries.

**Topic deliverables (due end of week):**
Model registry entry + guardrail CI tests for capstone project.

## Week 29 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 29):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 30: AI Compliance, Privacy & Data Governance

**Hours:** 12–15 recommended | **Module:** 07

## Week 30 learning goals
Complete all lessons below. Submit week deliverable before starting Week 31.

### Topic 7.1: AI Compliance, Privacy & Data Governance

**Why this matters (job market):** 50%+ enterprise JDs mention compliance awareness. GDPR, HIPAA, SOC2, EU AI Act basics separate enterprise hires.

**Job roles:** Enterprise AI Engineer, Responsible AI Engineer, AI Consultant

**Learning objectives:**
- Map data flows for AI features (DPIA-lite)
- Implement data minimization and retention
- Explain EU AI Act risk categories (practical)

---

**Lessons this week:**

#### Lesson 30.1: GDPR/CCPA for LLM data processing
**Duration:** 2 hrs

**Concepts taught:**
- GDPR/CCPA for LLM data processing
- How GDPR/CCPA for LLM data processing fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Map data flows: user input → logs → vector index
2. Implement DELETE /users/{id} removing vectors and chat history
3. Document retention policy in COMPLIANCE.md

**Lesson deliverable:** Repo artifact for `gdpr-ccpa-for-llm-data-processing` — code, config, or doc under docs/ or src/

#### Lesson 30.2: HIPAA considerations for health bots
**Duration:** 2 hrs

**Concepts taught:**
- HIPAA considerations for health bots
- How HIPAA considerations for health bots fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: HIPAA considerations for health bots
2. Implement a minimal working example of: HIPAA considerations for health bots
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'HIPAA considerations for health bots' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `hipaa-considerations-for-health-bots` — code, config, or doc under docs/ or src/

#### Lesson 30.3: SOC2 Type II relevance to AI logs
**Duration:** 2 hrs

**Concepts taught:**
- SOC2 Type II relevance to AI logs
- How SOC2 Type II relevance to AI logs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: SOC2 Type II relevance to AI logs
2. Implement a minimal working example of: SOC2 Type II relevance to AI logs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'SOC2 Type II relevance to AI logs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `soc2-type-ii-relevance-to-ai-logs` — code, config, or doc under docs/ or src/

#### Lesson 30.4: Data residency and vendor DPAs
**Duration:** 2 hrs

**Concepts taught:**
- Data residency and vendor DPAs
- How Data residency and vendor DPAs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Data residency and vendor DPAs
2. Implement a minimal working example of: Data residency and vendor DPAs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Data residency and vendor DPAs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `data-residency-and-vendor-dpas` — code, config, or doc under docs/ or src/

#### Lesson 30.5: Right to deletion in RAG indexes
**Duration:** 2 hrs

**Concepts taught:**
- Right to deletion in RAG indexes
- Grounding LLM answers in retrieved context
- Measuring retrieval quality

**Step-by-step activities:**
1. Map data flows: user input → logs → vector index
2. Implement DELETE /users/{id} removing vectors and chat history
3. Document retention policy in COMPLIANCE.md

**Lesson deliverable:** Repo artifact for `right-to-deletion-in-rag-indexes` — code, config, or doc under docs/ or src/

#### Lesson 30.6: EU AI Act high-risk checklist (overview)
**Duration:** 2 hrs

**Concepts taught:**
- EU AI Act high-risk checklist (overview)
- How EU AI Act high-risk checklist (overview) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: EU AI Act high-risk checklist (overview)
2. Implement a minimal working example of: EU AI Act high-risk checklist (overview)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'EU AI Act high-risk checklist (overview)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `eu-ai-act-high-risk-checklist-overview` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Data flow diagram + retention job deleting user data from vector index.

**Enterprise project extension:**
Compliance appendix for capstone: lawful basis, retention, subprocessors.

**Portfolio artifact:**
`COMPLIANCE.md` in flagship repo.

**Tools & technologies:**
Vault secrets, encryption at rest, audit logs, Azure Policy

**Common mistakes:**
- Sending PII to APIs without DPA
- Indefinite chat log retention
- No subprocessors list in docs

**Industry best practices:**
- Privacy by design in architecture reviews
- Legal review before new data sources
- Zero training clause with vendors where possible

**Interview preparation:**
- "Customer asks if data trains OpenAI—answer?"
- "Design GDPR delete for RAG system."

**Real-world use cases:**
EU customers, healthcare, financial services copilots.

**Topic deliverables (due end of week):**
Signed-off data flow diagram + deletion API endpoint.

## Week 30 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 30):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 31: AI Risk Management & Hallucination Prevention

**Hours:** 12–15 recommended | **Module:** 07

## Week 31 learning goals
Complete all lessons below. Submit week deliverable before starting Week 32.

### Topic 7.2: AI Risk Management & Hallucination Prevention

**Why this matters (job market):** Enterprises fear liability from wrong AI answers. Engineers must quantify and mitigate hallucination risk.

**Job roles:** Enterprise AI Engineer, Applied AI Engineer, AI Consultant

**Learning objectives:**
- Build risk matrix for AI features
- Apply grounding, abstention, and confidence thresholds
- Design human escalation paths

---

**Lessons this week:**

#### Lesson 31.1: Risk tiers: informational vs decision-support vs automated action
**Duration:** 2 hrs

**Concepts taught:**
- Risk tiers: informational vs decision-support vs automated action
- How Risk tiers: informational vs decision-support vs automated action fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Risk tiers: informational vs decision-support vs automated action
2. Implement a minimal working example of: Risk tiers: informational vs decision-support vs automated action
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Risk tiers: informational vs decision-support vs automated action' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `risk-tiers-informational-vs-decision-sup` — code, config, or doc under docs/ or src/

#### Lesson 31.2: Abstention ("I don't know") patterns
**Duration:** 2 hrs

**Concepts taught:**
- Abstention ("I don't know") patterns
- How Abstention ("I don't know") patterns fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Abstention ("I don't know") patterns
2. Implement a minimal working example of: Abstention ("I don't know") patterns
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Abstention ("I don't know") patterns' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `abstention-i-don-t-know-patterns` — code, config, or doc under docs/ or src/

#### Lesson 31.3: Confidence scores from retrieval + LLM
**Duration:** 2 hrs

**Concepts taught:**
- Confidence scores from retrieval + LLM
- Grounding LLM answers in retrieved context
- Measuring retrieval quality
- Golden datasets
- Regression gates before deploy

**Step-by-step activities:**
1. Read official docs and module notes for: Confidence scores from retrieval + LLM
2. Implement a minimal working example of: Confidence scores from retrieval + LLM
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Confidence scores from retrieval + LLM' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `confidence-scores-from-retrieval-llm` — code, config, or doc under docs/ or src/

#### Lesson 31.4: Human-in-the-loop thresholds
**Duration:** 2 hrs

**Concepts taught:**
- Human-in-the-loop thresholds
- How Human-in-the-loop thresholds fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Human-in-the-loop thresholds
2. Implement a minimal working example of: Human-in-the-loop thresholds
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Human-in-the-loop thresholds' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `human-in-the-loop-thresholds` — code, config, or doc under docs/ or src/

#### Lesson 31.5: Insurance and liability (awareness)
**Duration:** 2 hrs

**Concepts taught:**
- Insurance and liability (awareness)
- How Insurance and liability (awareness) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Insurance and liability (awareness)
2. Implement a minimal working example of: Insurance and liability (awareness)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Insurance and liability (awareness)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `insurance-and-liability-awareness` — code, config, or doc under docs/ or src/

#### Lesson 31.6: Documented limitations in UX
**Duration:** 2 hrs

**Concepts taught:**
- Documented limitations in UX
- How Documented limitations in UX fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Documented limitations in UX
2. Implement a minimal working example of: Documented limitations in UX
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Documented limitations in UX' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `documented-limitations-in-ux` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Abstain when retrieval score < threshold; route to human queue.

**Enterprise project extension:**
Risk register for copilot: 10 risks × mitigations × owners.

**Portfolio artifact:**
Hallucination rate metric on golden set with mitigation changelog.

**Tools & technologies:**
Ragas faithfulness, custom confidence models, ticketing integration

**Common mistakes:**
- Always answering to please users
- No escalation path
- Hiding uncertainty in UI

**Industry best practices:**
- Show sources and confidence
- Domain-specific disclaimers
- Post-incident eval set updates

**Interview preparation:**
- "Bot gave wrong medical info—incident response?"
- "When should AI refuse to answer?"

**Real-world use cases:**
Legal research assist, benefits HR bot, tax prep assist.

**Topic deliverables (due end of week):**
Risk register + abstention logic with measured hallucination reduction.

## Week 31 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 31):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 32: RBAC, Multi-Tenancy & Enterprise Integrations

**Hours:** 12–15 recommended | **Module:** 07

## Week 32 learning goals
Complete all lessons below. Submit week deliverable before starting Week 33.

### Topic 7.3: RBAC, Multi-Tenancy & Enterprise Integrations

**Why this matters (job market):** B2B AI must isolate tenants and respect document ACLs—core Enterprise AI Engineer skill.

**Job roles:** Enterprise AI Engineer, AI Integration Engineer, AI Platform Engineer

**Learning objectives:**
- Implement tenant-scoped data and auth
- Sync ACLs from SharePoint/Confluence/Salesforce
- Build OAuth enterprise connectors

---

**Lessons this week:**

#### Lesson 32.1: Multi-tenant DB schemas
**Duration:** 2 hrs

**Concepts taught:**
- Multi-tenant DB schemas
- How Multi-tenant DB schemas fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Multi-tenant DB schemas
2. Implement a minimal working example of: Multi-tenant DB schemas
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Multi-tenant DB schemas' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `multi-tenant-db-schemas` — code, config, or doc under docs/ or src/

#### Lesson 32.2: JWT/OAuth2/OIDC with Entra ID, Okta
**Duration:** 2 hrs

**Concepts taught:**
- JWT/OAuth2/OIDC with Entra ID, Okta
- How JWT/OAuth2/OIDC with Entra ID, Okta fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: JWT/OAuth2/OIDC with Entra ID, Okta
2. Implement a minimal working example of: JWT/OAuth2/OIDC with Entra ID, Okta
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'JWT/OAuth2/OIDC with Entra ID, Okta' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `jwt-oauth2-oidc-with-entra-id-okta` — code, config, or doc under docs/ or src/

#### Lesson 32.3: SharePoint, ServiceNow, Salesforce connector patterns
**Duration:** 2 hrs

**Concepts taught:**
- SharePoint, ServiceNow, Salesforce connector patterns
- How SharePoint, ServiceNow, Salesforce connector patterns fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: SharePoint, ServiceNow, Salesforce connector patterns
2. Implement a minimal working example of: SharePoint, ServiceNow, Salesforce connector patterns
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'SharePoint, ServiceNow, Salesforce connector patterns' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `sharepoint-servicenow-salesforce-connect` — code, config, or doc under docs/ or src/

#### Lesson 32.4: Webhook ingestion for doc updates
**Duration:** 2 hrs

**Concepts taught:**
- Webhook ingestion for doc updates
- How Webhook ingestion for doc updates fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Build pipeline script: load PDF → chunk → embed → upsert vector DB
2. Query endpoint returning answer + source chunk IDs
3. Diagram pipeline in docs/rag-architecture.md

**Lesson deliverable:** Repo artifact for `webhook-ingestion-for-doc-updates` — code, config, or doc under docs/ or src/

#### Lesson 32.5: Service accounts vs user-delegated auth
**Duration:** 2 hrs

**Concepts taught:**
- Service accounts vs user-delegated auth
- How Service accounts vs user-delegated auth fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Service accounts vs user-delegated auth
2. Implement a minimal working example of: Service accounts vs user-delegated auth
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Service accounts vs user-delegated auth' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `service-accounts-vs-user-delegated-auth` — code, config, or doc under docs/ or src/

#### Lesson 32.6: Rate limits per tenant
**Duration:** 2 hrs

**Concepts taught:**
- Rate limits per tenant
- How Rate limits per tenant fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Rate limits per tenant
2. Implement a minimal working example of: Rate limits per tenant
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Rate limits per tenant' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `rate-limits-per-tenant` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Two-tenant RAG: Tenant A cannot retrieve Tenant B docs (prove with test).

**Enterprise project extension:**
SharePoint mock connector with ACL metadata on chunks.

**Portfolio artifact:**
Integration architecture diagram in `/docs/enterprise-integrations.md`.

**Tools & technologies:**
Entra ID, MS Graph, Salesforce API, ServiceNow API, OAuth2

**Common mistakes:**
- Global vector index without tenant_id filter
- Stale ACLs after permission revocation
- Service account with excessive scopes

**Industry best practices:**
- Filter retrieval by user ACL every query
- Nightly ACL sync job
- Principle of least privilege on connectors

**Interview preparation:**
- "Design multi-tenant RAG for 500 enterprise customers."
- "SharePoint permission sync strategy."

**Real-world use cases:**
Internal knowledge copilots, CRM AI, IT service management.

**Topic deliverables (due end of week):**
Multi-tenant demo with RBAC tests in CI.

## Week 32 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 32):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 33: AI Consulting & Transformation Delivery

**Hours:** 12–15 recommended | **Module:** 07

## Week 33 learning goals
Complete all lessons below. Submit week deliverable before starting Week 34.

### Topic 7.4: AI Consulting — Discovery, POC & Production Handoff

**Why this matters (job market):** AI Consultant is #2 fastest-growing role—technical consultants who ship POCs win engagements.

**Job roles:** AI Consultant, AI Solutions Engineer

**Learning objectives:**
- Run AI discovery workshops
- Scope 2-week POC with success metrics
- Deliver production handoff documentation

---

**Lessons this week:**

#### Lesson 33.1: Build vs buy vs partner framework
**Duration:** 2 hrs

**Concepts taught:**
- Build vs buy vs partner framework
- How Build vs buy vs partner framework fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Build vs buy vs partner framework
2. Implement a minimal working example of: Build vs buy vs partner framework
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Build vs buy vs partner framework' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `build-vs-buy-vs-partner-framework` — code, config, or doc under docs/ or src/

#### Lesson 33.2: ROI estimation (time saved, error reduction)
**Duration:** 2 hrs

**Concepts taught:**
- ROI estimation (time saved, error reduction)
- How ROI estimation (time saved, error reduction) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: ROI estimation (time saved, error reduction)
2. Implement a minimal working example of: ROI estimation (time saved, error reduction)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'ROI estimation (time saved, error reduction)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `roi-estimation-time-saved-error-reductio` — code, config, or doc under docs/ or src/

#### Lesson 33.3: POC scope control (thin vertical slice)
**Duration:** 2 hrs

**Concepts taught:**
- POC scope control (thin vertical slice)
- How POC scope control (thin vertical slice) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: POC scope control (thin vertical slice)
2. Implement a minimal working example of: POC scope control (thin vertical slice)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'POC scope control (thin vertical slice)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `poc-scope-control-thin-vertical-slice` — code, config, or doc under docs/ or src/

#### Lesson 33.4: Stakeholder communication
**Duration:** 2 hrs

**Concepts taught:**
- Stakeholder communication
- How Stakeholder communication fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Stakeholder communication
2. Implement a minimal working example of: Stakeholder communication
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Stakeholder communication' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `stakeholder-communication` — code, config, or doc under docs/ or src/

#### Lesson 33.5: Change management basics
**Duration:** 2 hrs

**Concepts taught:**
- Change management basics
- How Change management basics fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Change management basics
2. Implement a minimal working example of: Change management basics
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Change management basics' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `change-management-basics` — code, config, or doc under docs/ or src/

#### Lesson 33.6: SOW and milestone structure
**Duration:** 2 hrs

**Concepts taught:**
- SOW and milestone structure
- How SOW and milestone structure fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: SOW and milestone structure
2. Implement a minimal working example of: SOW and milestone structure
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'SOW and milestone structure' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `sow-and-milestone-structure` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Write 5-page POC proposal for fictional retail client RAG copilot.

**Enterprise project extension:**
Consulting template pack: discovery questionnaire, architecture template, ROI calculator spreadsheet.

**Portfolio artifact:**
Case study: problem → POC → metrics → lessons (can be capstone fictionalized).

**Tools & technologies:**
Miro, Notion, architecture templates, cost calculators

**Common mistakes:**
- POC without eval criteria
- Scope creep into production complexity
- No executive summary for sponsors

**Industry best practices:**
- Fixed timeline POC (2–4 weeks)
- Kill criteria defined upfront
- Explicit production estimate separate from POC

**Interview preparation:**
- "Walk through a successful AI POC you led."
- "Client wants ChatGPT for everything—how do you refocus?"

**Real-world use cases:**
Deloitte/PwC-style transformations, vendor SI projects.

**Topic deliverables (due end of week):**
Consulting case study doc + reusable POC starter kit in GitHub.

## Week 33 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 33):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 34: AWS AI — Bedrock & SageMaker

**Hours:** 12–15 recommended | **Module:** 08

## Week 34 learning goals
Complete all lessons below. Submit week deliverable before starting Week 35.

### Topic 8.1: AWS AI — Bedrock, SageMaker & Production Patterns

**Why this matters (job market):** Amazon is a top AI employer (~711 roles Q1 2026). AWS Bedrock is standard for enterprise AWS shops.

**Job roles:** Enterprise AI Engineer, AI Infrastructure Engineer, AI Platform Engineer

**Learning objectives:**
- Deploy RAG using Bedrock Knowledge Bases
- Invoke Claude/Llama via Bedrock Converse API
- Understand SageMaker endpoints for custom models

---

**Lessons this week:**

#### Lesson 34.1: Bedrock models and Knowledge Bases
**Duration:** 2 hrs

**Concepts taught:**
- Bedrock models and Knowledge Bases
- How Bedrock models and Knowledge Bases fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Enable Bedrock model access in AWS console
2. Invoke Converse API with boto3 from Python script
3. Create Knowledge Base; sync S3 folder; query via API

**Lesson deliverable:** Repo artifact for `bedrock-models-and-knowledge-bases` — code, config, or doc under docs/ or src/

#### Lesson 34.2: IAM roles and VPC endpoints
**Duration:** 2 hrs

**Concepts taught:**
- IAM roles and VPC endpoints
- How IAM roles and VPC endpoints fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: IAM roles and VPC endpoints
2. Implement a minimal working example of: IAM roles and VPC endpoints
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'IAM roles and VPC endpoints' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `iam-roles-and-vpc-endpoints` — code, config, or doc under docs/ or src/

#### Lesson 34.3: S3 ingestion pipelines
**Duration:** 2 hrs

**Concepts taught:**
- S3 ingestion pipelines
- How S3 ingestion pipelines fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Build pipeline script: load PDF → chunk → embed → upsert vector DB
2. Query endpoint returning answer + source chunk IDs
3. Diagram pipeline in docs/rag-architecture.md

**Lesson deliverable:** Repo artifact for `s3-ingestion-pipelines` — code, config, or doc under docs/ or src/

#### Lesson 34.4: Lambda + API Gateway for serverless AI
**Duration:** 2 hrs

**Concepts taught:**
- Lambda + API Gateway for serverless AI
- How Lambda + API Gateway for serverless AI fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Lambda + API Gateway for serverless AI
2. Implement a minimal working example of: Lambda + API Gateway for serverless AI
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Lambda + API Gateway for serverless AI' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `lambda-api-gateway-for-serverless-ai` — code, config, or doc under docs/ or src/

#### Lesson 34.5: Cost allocation tags
**Duration:** 2 hrs

**Concepts taught:**
- Cost allocation tags
- How Cost allocation tags fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Cost allocation tags
2. Implement a minimal working example of: Cost allocation tags
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Cost allocation tags' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `cost-allocation-tags` — code, config, or doc under docs/ or src/

#### Lesson 34.6: CloudWatch integration
**Duration:** 2 hrs

**Concepts taught:**
- CloudWatch integration
- How CloudWatch integration fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: CloudWatch integration
2. Implement a minimal working example of: CloudWatch integration
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'CloudWatch integration' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `cloudwatch-integration` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Bedrock Knowledge Base RAG + Lambda API proxy.

**Enterprise project extension:**
Private VPC Bedrock deployment; no public internet for inference.

**Portfolio artifact:**
AWS architecture diagram (Lucid/ draw.io) in repo.

**Tools & technologies:**
Bedrock, boto3, SageMaker, EKS, Terraform AWS provider

**Common mistakes:**
- Over-permissive IAM `*` on Bedrock
- No VPC endpoints (data exfil concern)
- Ignoring cross-region model availability

**Industry best practices:**
- Least-privilege IAM per service
- Infrastructure as Code (Terraform)
- Multi-AZ for API layer

**Interview preparation:**
- "Design RAG on AWS for 10K employees."
- "Bedrock vs self-hosted on EKS tradeoffs."

**Real-world use cases:**
AWS-native enterprises, gov cloud variants.

**Topic deliverables (due end of week):**
One AWS-deployed service OR Terraform module with README apply steps.

## Week 34 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 34):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 35: Azure AI — OpenAI & AI Search

**Hours:** 12–15 recommended | **Module:** 08

## Week 35 learning goals
Complete all lessons below. Submit week deliverable before starting Week 36.

### Topic 8.2: Azure AI — OpenAI, AI Search & Copilot Patterns

**Why this matters (job market):** Microsoft-heavy enterprises dominate consulting JDs; Azure OpenAI + AI Search is the default enterprise RAG stack.

**Job roles:** Enterprise AI Engineer, AI Solutions Engineer, AI Consultant

**Learning objectives:**
- Deploy Azure OpenAI with private endpoints
- Build hybrid search in Azure AI Search
- Integrate Entra ID authentication

---

**Lessons this week:**

#### Lesson 35.1: Azure OpenAI deployments and quotas
**Duration:** 2 hrs

**Concepts taught:**
- Azure OpenAI deployments and quotas
- How Azure OpenAI deployments and quotas fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Azure OpenAI deployments and quotas
2. Implement a minimal working example of: Azure OpenAI deployments and quotas
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Azure OpenAI deployments and quotas' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `azure-openai-deployments-and-quotas` — code, config, or doc under docs/ or src/

#### Lesson 35.2: Azure AI Search indexes and skillsets
**Duration:** 2 hrs

**Concepts taught:**
- Azure AI Search indexes and skillsets
- How Azure AI Search indexes and skillsets fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Azure AI Search indexes and skillsets
2. Implement a minimal working example of: Azure AI Search indexes and skillsets
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Azure AI Search indexes and skillsets' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `azure-ai-search-indexes-and-skillsets` — code, config, or doc under docs/ or src/

#### Lesson 35.3: Document Intelligence for ingestion
**Duration:** 2 hrs

**Concepts taught:**
- Document Intelligence for ingestion
- How Document Intelligence for ingestion fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Build pipeline script: load PDF → chunk → embed → upsert vector DB
2. Query endpoint returning answer + source chunk IDs
3. Diagram pipeline in docs/rag-architecture.md

**Lesson deliverable:** Repo artifact for `document-intelligence-for-ingestion` — code, config, or doc under docs/ or src/

#### Lesson 35.4: Managed identity authentication
**Duration:** 2 hrs

**Concepts taught:**
- Managed identity authentication
- How Managed identity authentication fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Managed identity authentication
2. Implement a minimal working example of: Managed identity authentication
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Managed identity authentication' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `managed-identity-authentication` — code, config, or doc under docs/ or src/

#### Lesson 35.5: Copilot Studio overview
**Duration:** 2 hrs

**Concepts taught:**
- Copilot Studio overview
- How Copilot Studio overview fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Copilot Studio overview
2. Implement a minimal working example of: Copilot Studio overview
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Copilot Studio overview' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `copilot-studio-overview` — code, config, or doc under docs/ or src/

#### Lesson 35.6: Content safety filters
**Duration:** 2 hrs

**Concepts taught:**
- Content safety filters
- How Content safety filters fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Content safety filters
2. Implement a minimal working example of: Content safety filters
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Content safety filters' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `content-safety-filters` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Azure AI Search hybrid RAG + FastAPI on App Service.

**Enterprise project extension:**
Private Link end-to-end; customer-managed keys option documented.

**Portfolio artifact:**
Azure reference architecture for enterprise RAG.

**Tools & technologies:**
Azure OpenAI, AI Search, Document Intelligence, App Service, Terraform Azure

**Common mistakes:**
- API keys in app settings instead of managed identity
- No quota/rate limit planning
- Skipping content safety configuration

**Industry best practices:**
- Hub-spoke networking for AI services
- Cost alerts on token usage
- Align with Microsoft Well-Architected Framework

**Interview preparation:**
- "Azure OpenAI vs public OpenAI API for bank client?"
- "AI Search skillset pipeline design."

**Real-world use cases:**
M365 organizations, regulated finance on Azure.

**Topic deliverables (due end of week):**
Azure deployment guide OR multi-cloud comparison ADR.

## Week 35 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 35):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 36: GCP Vertex AI & Gemini Enterprise

**Hours:** 12–15 recommended | **Module:** 08

## Week 36 learning goals
Complete all lessons below. Submit week deliverable before starting Week 37.

### Topic 8.3: Google Cloud Vertex AI & Gemini Enterprise

**Why this matters (job market):** Google (~702 AI roles); Gemini-native shops and data-heavy GCP customers need Vertex skills.

**Job roles:** AI Engineer, AI Platform Engineer, Generative AI Engineer

**Learning objectives:**
- Use Vertex AI Gemini API and embeddings
- Deploy models on Vertex endpoints
- Integrate with BigQuery for analytics on AI logs

---

**Lessons this week:**

#### Lesson 36.1: Vertex AI Studio vs production APIs
**Duration:** 2 hrs

**Concepts taught:**
- Vertex AI Studio vs production APIs
- How Vertex AI Studio vs production APIs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Vertex AI Studio vs production APIs
2. Implement a minimal working example of: Vertex AI Studio vs production APIs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Vertex AI Studio vs production APIs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `vertex-ai-studio-vs-production-apis` — code, config, or doc under docs/ or src/

#### Lesson 36.2: Gemini Pro/Flash selection
**Duration:** 2 hrs

**Concepts taught:**
- Gemini Pro/Flash selection
- How Gemini Pro/Flash selection fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Gemini Pro/Flash selection
2. Implement a minimal working example of: Gemini Pro/Flash selection
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Gemini Pro/Flash selection' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `gemini-pro-flash-selection` — code, config, or doc under docs/ or src/

#### Lesson 36.3: Vector Search on Vertex
**Duration:** 2 hrs

**Concepts taught:**
- Vector Search on Vertex
- How Vector Search on Vertex fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Provision vector DB (local pgvector or Pinecone free tier)
2. Create index with metadata fields: tenant_id, doc_id, page
3. Query with metadata filter; verify tenant isolation

**Lesson deliverable:** Repo artifact for `vector-search-on-vertex` — code, config, or doc under docs/ or src/

#### Lesson 36.4: GCS document pipelines
**Duration:** 2 hrs

**Concepts taught:**
- GCS document pipelines
- How GCS document pipelines fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: GCS document pipelines
2. Implement a minimal working example of: GCS document pipelines
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'GCS document pipelines' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `gcs-document-pipelines` — code, config, or doc under docs/ or src/

#### Lesson 36.5: Workload identity for GKE
**Duration:** 2 hrs

**Concepts taught:**
- Workload identity for GKE
- How Workload identity for GKE fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Workload identity for GKE
2. Implement a minimal working example of: Workload identity for GKE
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Workload identity for GKE' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `workload-identity-for-gke` — code, config, or doc under docs/ or src/

#### Lesson 36.6: Model Garden open models
**Duration:** 2 hrs

**Concepts taught:**
- Model Garden open models
- How Model Garden open models fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Model Garden open models
2. Implement a minimal working example of: Model Garden open models
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Model Garden open models' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `model-garden-open-models` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Vertex RAG corpus + Cloud Run API.

**Enterprise project extension:**
VPC-SC perimeter for AI services; audit logs to BigQuery.

**Portfolio artifact:**
GCP terraform snippet for AI service.

**Tools & technologies:**
Vertex AI, Cloud Run, GKE, Terraform GCP, BigQuery

**Common mistakes:**
- Confusing AI Studio experiments with prod config
- No quota project setup
- Ignoring region for data residency

**Industry best practices:**
- Service accounts per environment
- Centralized logging sink
- Cost budget alerts

**Interview preparation:**
- "When GCP over AWS for GenAI?"
- "Vertex Vector Search vs Pinecone."

**Real-world use cases:**
Analytics-heavy companies, Google Workspace integrations.

**Topic deliverables (due end of week):**
Tri-cloud ADR: which cloud for sample enterprise scenario.

## Week 36 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 36):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 37: Kubernetes, GPU & Inference Optimization

**Hours:** 12–15 recommended | **Module:** 08

## Week 37 learning goals
Complete all lessons below. Submit week deliverable before starting Week 38.

### Topic 8.4: Kubernetes, GPU Infrastructure & Inference Optimization

**Why this matters (job market):** 55%+ senior roles mention K8s; CUDA +12% premium; vLLM/Ollama for cost control at scale.

**Job roles:** AI Infrastructure Engineer, AI Platform Engineer, LLMOps Engineer

**Learning objectives:**
- Deploy vLLM on Kubernetes with autoscaling
- Understand GPU node pools and scheduling
- Optimize inference: batching, quantization, caching

---

**Lessons this week:**

#### Lesson 37.1: K8s deployments, HPA, ingress for AI APIs
**Duration:** 2 hrs

**Concepts taught:**
- K8s deployments, HPA, ingress for AI APIs
- How K8s deployments, HPA, ingress for AI APIs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: K8s deployments, HPA, ingress for AI APIs
2. Implement a minimal working example of: K8s deployments, HPA, ingress for AI APIs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'K8s deployments, HPA, ingress for AI APIs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `k8s-deployments-hpa-ingress-for-ai-apis` — code, config, or doc under docs/ or src/

#### Lesson 37.2: GPU node selectors and fractions
**Duration:** 2 hrs

**Concepts taught:**
- GPU node selectors and fractions
- How GPU node selectors and fractions fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: GPU node selectors and fractions
2. Implement a minimal working example of: GPU node selectors and fractions
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'GPU node selectors and fractions' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `gpu-node-selectors-and-fractions` — code, config, or doc under docs/ or src/

#### Lesson 37.3: vLLM throughput tuning
**Duration:** 2 hrs

**Concepts taught:**
- vLLM throughput tuning
- How vLLM throughput tuning fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: vLLM throughput tuning
2. Implement a minimal working example of: vLLM throughput tuning
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'vLLM throughput tuning' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `vllm-throughput-tuning` — code, config, or doc under docs/ or src/

#### Lesson 37.4: Ollama for dev; vLLM for prod
**Duration:** 2 hrs

**Concepts taught:**
- Ollama for dev; vLLM for prod
- How Ollama for dev; vLLM for prod fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Ollama for dev; vLLM for prod
2. Implement a minimal working example of: Ollama for dev; vLLM for prod
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Ollama for dev; vLLM for prod' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `ollama-for-dev-vllm-for-prod` — code, config, or doc under docs/ or src/

#### Lesson 37.5: Serverless vs dedicated GPU economics
**Duration:** 2 hrs

**Concepts taught:**
- Serverless vs dedicated GPU economics
- How Serverless vs dedicated GPU economics fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Serverless vs dedicated GPU economics
2. Implement a minimal working example of: Serverless vs dedicated GPU economics
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Serverless vs dedicated GPU economics' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `serverless-vs-dedicated-gpu-economics` — code, config, or doc under docs/ or src/

#### Lesson 37.6: TensorRT-LLM mention (awareness)
**Duration:** 2 hrs

**Concepts taught:**
- TensorRT-LLM mention (awareness)
- How TensorRT-LLM mention (awareness) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: TensorRT-LLM mention (awareness)
2. Implement a minimal working example of: TensorRT-LLM mention (awareness)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'TensorRT-LLM mention (awareness)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `tensorrt-llm-mention-awareness` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
vLLM on local k3d/minikube with load test (hey/locust).

**Enterprise project extension:**
Inference gateway routing: cloud API vs self-hosted by policy.

**Portfolio artifact:**
Load test report: RPS, p95 latency, $/1M tokens.

**Tools & technologies:**
Kubernetes, vLLM, Ollama, Helm, NVIDIA device plugin, Locust

**Common mistakes:**
- No readiness probes on model pods (slow startup)
- Single replica on GPU workload
- Ignoring cold start in autoscaling

**Industry best practices:**
- Separate embedding and generation clusters
- Spot instances for batch; on-demand for API
- Model warm-up in readiness probe

**Interview preparation:**
- "Scale self-hosted Llama to 100 RPS—architecture?"
- "GPU cost optimization strategies."

**Real-world use cases:**
High-volume internal copilots, air-gapped inference.

**Topic deliverables (due end of week):**
K8s manifests OR load test doc proving inference SLO.

## Week 37 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 37):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 38: Next.js AI Frontends & Streaming UX

**Hours:** 12–15 recommended | **Module:** 09

## Week 38 learning goals
Complete all lessons below. Submit week deliverable before starting Week 39.

### Topic 9.1: Next.js AI Frontends & Streaming UX

**Why this matters (job market):** AI Application Developer roles require React/Next.js + streaming—Vercel AI SDK patterns are industry standard.

**Job roles:** AI Application Developer, AI Copilot Engineer, AI Product Engineer

**Learning objectives:**
- Build chat UI with streaming token display
- Use Vercel AI SDK / server actions
- Handle loading, errors, and stop generation

---

**Lessons this week:**

#### Lesson 38.1: Next.js App Router
**Duration:** 2 hrs

**Concepts taught:**
- Next.js App Router
- APIRouter for modular routes
- Dependency injection pattern

**Step-by-step activities:**
1. npx create-next-app; install ai package
2. Wire useChat hook to FastAPI SSE endpoint
3. Render streaming markdown with loading and stop button

**Lesson deliverable:** Repo artifact for `next-js-app-router` — code, config, or doc under docs/ or src/

#### Lesson 38.2: Server-sent events from FastAPI/Next
**Duration:** 2 hrs

**Concepts taught:**
- Server-sent events from FastAPI/Next
- APIRouter for modular routes
- Dependency injection pattern

**Step-by-step activities:**
1. Read official docs and module notes for: Server-sent events from FastAPI/Next
2. Implement a minimal working example of: Server-sent events from FastAPI/Next
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Server-sent events from FastAPI/Next' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `server-sent-events-from-fastapi-next` — code, config, or doc under docs/ or src/

#### Lesson 38.3: Vercel AI SDK `useChat`
**Duration:** 2 hrs

**Concepts taught:**
- Vercel AI SDK `useChat`
- How Vercel AI SDK `useChat` fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. npx create-next-app; install ai package
2. Wire useChat hook to FastAPI SSE endpoint
3. Render streaming markdown with loading and stop button

**Lesson deliverable:** Repo artifact for `vercel-ai-sdk-usechat` — code, config, or doc under docs/ or src/

#### Lesson 38.4: Message history and thread UI
**Duration:** 2 hrs

**Concepts taught:**
- Message history and thread UI
- How Message history and thread UI fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Message history and thread UI
2. Implement a minimal working example of: Message history and thread UI
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Message history and thread UI' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `message-history-and-thread-ui` — code, config, or doc under docs/ or src/

#### Lesson 38.5: Markdown rendering + code highlighting
**Duration:** 2 hrs

**Concepts taught:**
- Markdown rendering + code highlighting
- How Markdown rendering + code highlighting fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Markdown rendering + code highlighting
2. Implement a minimal working example of: Markdown rendering + code highlighting
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Markdown rendering + code highlighting' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `markdown-rendering-code-highlighting` — code, config, or doc under docs/ or src/

#### Lesson 38.6: Citation UI for RAG sources
**Duration:** 2 hrs

**Concepts taught:**
- Citation UI for RAG sources
- Grounding LLM answers in retrieved context
- Measuring retrieval quality

**Step-by-step activities:**
1. Read official docs and module notes for: Citation UI for RAG sources
2. Implement a minimal working example of: Citation UI for RAG sources
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Citation UI for RAG sources' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `citation-ui-for-rag-sources` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Next.js chat app consuming Module 01 FastAPI stream.

**Enterprise project extension:**
SSO login stub; branded UI; accessibility WCAG basics.

**Portfolio artifact:**
Deployed Vercel frontend + API URL in README.

**Tools & technologies:**
Next.js 14+, TypeScript, Vercel AI SDK, Tailwind, shadcn/ui

**Common mistakes:**
- Exposing API keys in frontend
- No abort/stop for long generations
- XSS via unsanitized markdown

**Industry best practices:**
- API keys only server-side
- Optimistic UI with rollback
- Mobile-responsive chat layout

**Interview preparation:**
- "Implement streaming chat with error recovery."
- "How do you show RAG citations in UI?"

**Real-world use cases:**
Customer portals, internal copilots, sales tools.

**Topic deliverables (due end of week):**
Production-quality chat UI wired to RAG backend.

## Week 38 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 38):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 39: Multimodal & Voice AI Applications

**Hours:** 12–15 recommended | **Module:** 09

## Week 39 learning goals
Complete all lessons below. Submit week deliverable before starting Week 40.

### Topic 9.2: Multimodal & Voice AI Applications

**Why this matters (job market):** Multimodal search and voice support growing in customer experience roles—Whisper + TTS pipelines expected.

**Job roles:** Conversational AI Engineer, AI Product Engineer

**Learning objectives:**
- Process image + text inputs in Gemini/GPT-4o
- Build voice pipeline: STT → LLM → TTS
- Design latency budgets for voice

---

**Lessons this week:**

#### Lesson 39.1: Vision API document Q&A
**Duration:** 2 hrs

**Concepts taught:**
- Vision API document Q&A
- How Vision API document Q&A fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Vision API document Q&A
2. Implement a minimal working example of: Vision API document Q&A
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Vision API document Q&A' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `vision-api-document-q-a` — code, config, or doc under docs/ or src/

#### Lesson 39.2: Whisper transcription
**Duration:** 2 hrs

**Concepts taught:**
- Whisper transcription
- How Whisper transcription fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Whisper transcription
2. Implement a minimal working example of: Whisper transcription
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Whisper transcription' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `whisper-transcription` — code, config, or doc under docs/ or src/

#### Lesson 39.3: ElevenLabs / OpenAI TTS
**Duration:** 2 hrs

**Concepts taught:**
- ElevenLabs / OpenAI TTS
- How ElevenLabs / OpenAI TTS fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: ElevenLabs / OpenAI TTS
2. Implement a minimal working example of: ElevenLabs / OpenAI TTS
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'ElevenLabs / OpenAI TTS' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `elevenlabs-openai-tts` — code, config, or doc under docs/ or src/

#### Lesson 39.4: Real-time voice WebRTC overview
**Duration:** 2 hrs

**Concepts taught:**
- Real-time voice WebRTC overview
- How Real-time voice WebRTC overview fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Real-time voice WebRTC overview
2. Implement a minimal working example of: Real-time voice WebRTC overview
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Real-time voice WebRTC overview' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `real-time-voice-webrtc-overview` — code, config, or doc under docs/ or src/

#### Lesson 39.5: Lip-sync and avatar (awareness)
**Duration:** 2 hrs

**Concepts taught:**
- Lip-sync and avatar (awareness)
- How Lip-sync and avatar (awareness) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Lip-sync and avatar (awareness)
2. Implement a minimal working example of: Lip-sync and avatar (awareness)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Lip-sync and avatar (awareness)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `lip-sync-and-avatar-awareness` — code, config, or doc under docs/ or src/

#### Lesson 39.6: Multimodal RAG (image chunks)
**Duration:** 2 hrs

**Concepts taught:**
- Multimodal RAG (image chunks)
- Grounding LLM answers in retrieved context
- Measuring retrieval quality

**Step-by-step activities:**
1. Split sample PDF with RecursiveCharacterTextSplitter sizes 256/512/1024
2. Run 10 test queries; record which chunk size wins on faithfulness
3. Document winning config in docs/chunking.md

**Lesson deliverable:** Repo artifact for `multimodal-rag-image-chunks` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Voice note → transcript → RAG answer → audio response.

**Enterprise project extension:**
**Multimodal AI Search Engine** — text + image upload search.

**Portfolio artifact:**
Demo video of voice or image Q&A flow.

**Tools & technologies:**
OpenAI Whisper, GPT-4o vision, Gemini multimodal, ElevenLabs

**Common mistakes:**
- Sequential STT→LLM→TTS without streaming (slow UX)
- No noise handling in telephony audio
- Storing voice recordings without consent

**Industry best practices:**
- Stream partial transcripts
- Consent banner for recording
- Fallback to text chat

**Interview preparation:**
- "Design voice customer support architecture."
- "Latency targets for voice AI?"

**Real-world use cases:**
Call center assist, field tech photo diagnosis, retail visual search.

**Topic deliverables (due end of week):**
Multimodal or voice feature in full-stack project.

## Week 39 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 39):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 40: AI SaaS Products & Copilot Patterns

**Hours:** 12–15 recommended | **Module:** 09

## Week 40 learning goals
Complete all lessons below. Submit week deliverable before starting Week 41.

### Topic 9.3: AI SaaS Products — Auth, Billing & Copilot Patterns

**Why this matters (job market):** Startup-ready engineers ship AI SaaS: auth, usage metering, embeddable copilots.

**Job roles:** AI Product Engineer, AI Application Developer, startup founders

**Learning objectives:**
- Add auth (Clerk/Auth0/NextAuth)
- Meter token usage per user
- Design embeddable copilot widget

---

**Lessons this week:**

#### Lesson 40.1: SaaS architecture for AI (API-first)
**Duration:** 2 hrs

**Concepts taught:**
- SaaS architecture for AI (API-first)
- How SaaS architecture for AI (API-first) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: SaaS architecture for AI (API-first)
2. Implement a minimal working example of: SaaS architecture for AI (API-first)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'SaaS architecture for AI (API-first)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `saas-architecture-for-ai-api-first` — code, config, or doc under docs/ or src/

#### Lesson 40.2: Stripe usage-based billing intro
**Duration:** 2 hrs

**Concepts taught:**
- Stripe usage-based billing intro
- How Stripe usage-based billing intro fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Stripe usage-based billing intro
2. Implement a minimal working example of: Stripe usage-based billing intro
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Stripe usage-based billing intro' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `stripe-usage-based-billing-intro` — code, config, or doc under docs/ or src/

#### Lesson 40.3: Rate limits per plan tier
**Duration:** 2 hrs

**Concepts taught:**
- Rate limits per plan tier
- How Rate limits per plan tier fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Rate limits per plan tier
2. Implement a minimal working example of: Rate limits per plan tier
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Rate limits per plan tier' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `rate-limits-per-plan-tier` — code, config, or doc under docs/ or src/

#### Lesson 40.4: Embeddable widget (iframe/SDK)
**Duration:** 2 hrs

**Concepts taught:**
- Embeddable widget (iframe/SDK)
- How Embeddable widget (iframe/SDK) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Embeddable widget (iframe/SDK)
2. Implement a minimal working example of: Embeddable widget (iframe/SDK)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Embeddable widget (iframe/SDK)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `embeddable-widget-iframe-sdk` — code, config, or doc under docs/ or src/

#### Lesson 40.5: White-label copilot options
**Duration:** 2 hrs

**Concepts taught:**
- White-label copilot options
- How White-label copilot options fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: White-label copilot options
2. Implement a minimal working example of: White-label copilot options
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'White-label copilot options' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `white-label-copilot-options` — code, config, or doc under docs/ or src/

#### Lesson 40.6: Onboarding and activation metrics
**Duration:** 2 hrs

**Concepts taught:**
- Onboarding and activation metrics
- How Onboarding and activation metrics fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Onboarding and activation metrics
2. Implement a minimal working example of: Onboarding and activation metrics
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Onboarding and activation metrics' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `onboarding-and-activation-metrics` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Free vs Pro tier with token quota enforcement.

**Enterprise project extension:**
**AI Sales Assistant** or **AI Recruiter System** as SaaS-shaped portfolio.

**Portfolio artifact:**
Landing page + waitlist + working product loop.

**Tools & technologies:**
Clerk, Stripe, Posthog, FastAPI middleware for quotas

**Common mistakes:**
- No usage tracking before launch
- Unlimited free tier abuse
- Weak tenant isolation in SaaS DB

**Industry best practices:**
- Instrument activation funnel day one
- Graceful degradation when quota exceeded
- Clear ToS on data usage

**Interview preparation:**
- "Design AI SaaS pricing based on tokens."
- "Embeddable copilot security model."

**Real-world use cases:**
B2B AI tools, vertical SaaS (legal, HR, sales).

**Topic deliverables (due end of week):**
SaaS MVP with auth + usage limits + 1-page business model.

## Week 40 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 40):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 41: TypeScript & Workflow Automation UI

**Hours:** 12–15 recommended | **Module:** 09

## Week 41 learning goals
Complete all lessons below. Submit week deliverable before starting Week 42.

### Topic 9.4: TypeScript AI Integration & Workflow Automation UI

**Why this matters (job market):** Full-stack AI teams use TypeScript for SDKs and workflow builders—n8n + custom UI patterns.

**Job roles:** AI Workflow Engineer, AI Automation Engineer, AI Integration Engineer

**Learning objectives:**
- Call AI APIs from TypeScript services
- Build workflow builder UI (nodes/edges)
- Integrate n8n or Trigger.dev with LLM steps

---

**Lessons this week:**

#### Lesson 41.1: OpenAI Node SDK
**Duration:** 2 hrs

**Concepts taught:**
- OpenAI Node SDK
- How OpenAI Node SDK fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: OpenAI Node SDK
2. Implement a minimal working example of: OpenAI Node SDK
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'OpenAI Node SDK' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `openai-node-sdk` — code, config, or doc under docs/ or src/

#### Lesson 41.2: React Flow for workflow UI
**Duration:** 2 hrs

**Concepts taught:**
- React Flow for workflow UI
- How React Flow for workflow UI fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: React Flow for workflow UI
2. Implement a minimal working example of: React Flow for workflow UI
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'React Flow for workflow UI' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `react-flow-for-workflow-ui` — code, config, or doc under docs/ or src/

#### Lesson 41.3: n8n LLM nodes
**Duration:** 2 hrs

**Concepts taught:**
- n8n LLM nodes
- How n8n LLM nodes fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: n8n LLM nodes
2. Implement a minimal working example of: n8n LLM nodes
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'n8n LLM nodes' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `n8n-llm-nodes` — code, config, or doc under docs/ or src/

#### Lesson 41.4: Webhook orchestration
**Duration:** 2 hrs

**Concepts taught:**
- Webhook orchestration
- How Webhook orchestration fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Webhook orchestration
2. Implement a minimal working example of: Webhook orchestration
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Webhook orchestration' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `webhook-orchestration` — code, config, or doc under docs/ or src/

#### Lesson 41.5: Event-driven agent triggers
**Duration:** 2 hrs

**Concepts taught:**
- Event-driven agent triggers
- State management across agent steps
- Human-in-the-loop checkpoints

**Step-by-step activities:**
1. Read official docs and module notes for: Event-driven agent triggers
2. Implement a minimal working example of: Event-driven agent triggers
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Event-driven agent triggers' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `event-driven-agent-triggers` — code, config, or doc under docs/ or src/

#### Lesson 41.6: Temporal intro (durable workflows)
**Duration:** 2 hrs

**Concepts taught:**
- Temporal intro (durable workflows)
- How Temporal intro (durable workflows) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Temporal intro (durable workflows)
2. Implement a minimal working example of: Temporal intro (durable workflows)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Temporal intro (durable workflows)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `temporal-intro-durable-workflows` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Visual workflow: ingest ticket → classify → RAG → draft reply.

**Enterprise project extension:**
**AI Workflow Automation Platform** (flagship).

**Portfolio artifact:**
Screenshot of workflow editor + JSON export of flows.

**Tools & technologies:**
TypeScript, React Flow, n8n, Trigger.dev, Temporal (intro)

**Common mistakes:**
- Non-idempotent LLM steps on retry
- No dead-letter queue for failures
- UI allowing cyclic workflows

**Industry best practices:**
- Version workflow definitions
- Test workflows with recorded fixtures
- Audit log per execution

**Interview preparation:**
- "Build no-code AI workflow for ops team—architecture?"
- "Idempotent workflow steps with LLMs."

**Real-world use cases:**
Ops automation, marketing pipelines, HR onboarding flows.

**Topic deliverables (due end of week):**
Workflow platform with 3 templates and execution history API.

## Week 41 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 41):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 42: AI Security — Threat Models & Red Teaming

**Hours:** 12–15 recommended | **Module:** 10

## Week 42 learning goals
Complete all lessons below. Submit week deliverable before starting Week 43.

### Topic 10.1: AI Security — Threat Models & Red Teaming

**Why this matters (job market):** Agents with tools create new attack surface; AI Security Engineer demand rising with enterprise agent rollouts.

**Job roles:** AI Security Engineer, Enterprise AI Engineer, AI Architect

**Learning objectives:**
- Create STRIDE-style threat model for LLM app
- Execute red team test suite
- Remediate OWASP LLM Top 10 risks

---

**Lessons this week:**

#### Lesson 42.1: Prompt injection (direct/indirect)
**Duration:** 2 hrs

**Concepts taught:**
- Prompt injection (direct/indirect)
- How Prompt injection (direct/indirect) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Prompt injection (direct/indirect)
2. Implement a minimal working example of: Prompt injection (direct/indirect)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Prompt injection (direct/indirect)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `prompt-injection-direct-indirect` — code, config, or doc under docs/ or src/

#### Lesson 42.2: Data exfiltration via tools
**Duration:** 2 hrs

**Concepts taught:**
- Data exfiltration via tools
- How Data exfiltration via tools fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Data exfiltration via tools
2. Implement a minimal working example of: Data exfiltration via tools
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Data exfiltration via tools' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `data-exfiltration-via-tools` — code, config, or doc under docs/ or src/

#### Lesson 42.3: Model denial of wallet
**Duration:** 2 hrs

**Concepts taught:**
- Model denial of wallet
- How Model denial of wallet fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Model denial of wallet
2. Implement a minimal working example of: Model denial of wallet
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Model denial of wallet' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `model-denial-of-wallet` — code, config, or doc under docs/ or src/

#### Lesson 42.4: Supply chain: compromised packages, models
**Duration:** 2 hrs

**Concepts taught:**
- Supply chain: compromised packages, models
- How Supply chain: compromised packages, models fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Supply chain: compromised packages, models
2. Implement a minimal working example of: Supply chain: compromised packages, models
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Supply chain: compromised packages, models' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `supply-chain-compromised-packages-models` — code, config, or doc under docs/ or src/

#### Lesson 42.5: Secrets in prompts and logs
**Duration:** 2 hrs

**Concepts taught:**
- Secrets in prompts and logs
- How Secrets in prompts and logs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Secrets in prompts and logs
2. Implement a minimal working example of: Secrets in prompts and logs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Secrets in prompts and logs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `secrets-in-prompts-and-logs` — code, config, or doc under docs/ or src/

#### Lesson 42.6: Red team automation tools
**Duration:** 2 hrs

**Concepts taught:**
- Red team automation tools
- How Red team automation tools fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Red team automation tools
2. Implement a minimal working example of: Red team automation tools
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Red team automation tools' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `red-team-automation-tools` — code, config, or doc under docs/ or src/

#### Lesson 42.7: Pen test report structure
**Duration:** 2 hrs

**Concepts taught:**
- Pen test report structure
- How Pen test report structure fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Pen test report structure
2. Implement a minimal working example of: Pen test report structure
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Pen test report structure' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `pen-test-report-structure` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Red team capstone bot; fix 8/10 attack vectors; document 2 accepted risks.

**Enterprise project extension:**
**AI Cybersecurity Analyst** agent in isolated env with read-only SIEM mock.

**Portfolio artifact:**
`THREAT_MODEL.md` + red team results table.

**Tools & technologies:**
OWASP LLM Top 10, Garak, PyRIT, custom attack libraries

**Common mistakes:**
- Security review only at launch
- Agents with internet + sensitive data same env
- No rate limiting (DoW attacks)

**Industry best practices:**
- Security in CI weekly
- Bug bounty for critical copilots
- Separate prod secrets per tenant

**Interview preparation:**
- "Threat model for email-processing agent."
- "Prevent data exfil via RAG context."

**Real-world use cases:**
Security ops copilots, email assistants, customer-facing bots.

**Topic deliverables (due end of week):**
Passed red team suite ≥80%; threat model signed in README.

## Week 42 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 42):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 43: Responsible AI — Bias, Fairness & Transparency

**Hours:** 12–15 recommended | **Module:** 10

## Week 43 learning goals
Complete all lessons below. Submit week deliverable before starting Week 44.

### Topic 10.2: Responsible AI — Bias, Fairness & Transparency

**Why this matters (job market):** Regulated industries and EU AI Act drive Responsible AI Engineer hires; required for enterprise procurement.

**Job roles:** Responsible AI Engineer, Enterprise AI Engineer, AI Consultant

**Learning objectives:**
- Run bias/fairness evals on representative samples
- Write model cards and user disclosures
- Implement appeal/human review for adverse decisions

---

**Lessons this week:**

#### Lesson 43.1: Fairness metrics for classification
**Duration:** 2 hrs

**Concepts taught:**
- Fairness metrics for classification
- How Fairness metrics for classification fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Fairness metrics for classification
2. Implement a minimal working example of: Fairness metrics for classification
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Fairness metrics for classification' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `fairness-metrics-for-classification` — code, config, or doc under docs/ or src/

#### Lesson 43.2: Disparate impact awareness
**Duration:** 2 hrs

**Concepts taught:**
- Disparate impact awareness
- How Disparate impact awareness fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Disparate impact awareness
2. Implement a minimal working example of: Disparate impact awareness
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Disparate impact awareness' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `disparate-impact-awareness` — code, config, or doc under docs/ or src/

#### Lesson 43.3: Model cards (HuggingFace template)
**Duration:** 2 hrs

**Concepts taught:**
- Model cards (HuggingFace template)
- How Model cards (HuggingFace template) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Model cards (HuggingFace template)
2. Implement a minimal working example of: Model cards (HuggingFace template)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Model cards (HuggingFace template)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `model-cards-huggingface-template` — code, config, or doc under docs/ or src/

#### Lesson 43.4: Transparency: capabilities and limits
**Duration:** 2 hrs

**Concepts taught:**
- Transparency: capabilities and limits
- How Transparency: capabilities and limits fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Transparency: capabilities and limits
2. Implement a minimal working example of: Transparency: capabilities and limits
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Transparency: capabilities and limits' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `transparency-capabilities-and-limits` — code, config, or doc under docs/ or src/

#### Lesson 43.5: Human oversight for high-risk decisions
**Duration:** 2 hrs

**Concepts taught:**
- Human oversight for high-risk decisions
- How Human oversight for high-risk decisions fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Human oversight for high-risk decisions
2. Implement a minimal working example of: Human oversight for high-risk decisions
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Human oversight for high-risk decisions' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `human-oversight-for-high-risk-decisions` — code, config, or doc under docs/ or src/

#### Lesson 43.6: EU AI Act conformity assessment (overview)
**Duration:** 2 hrs

**Concepts taught:**
- EU AI Act conformity assessment (overview)
- How EU AI Act conformity assessment (overview) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: EU AI Act conformity assessment (overview)
2. Implement a minimal working example of: EU AI Act conformity assessment (overview)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'EU AI Act conformity assessment (overview)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `eu-ai-act-conformity-assessment-overview` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Model card for support classifier; fairness check across demographic proxy slices.

**Enterprise project extension:**
Responsible AI sign-off checklist before prod launch.

**Portfolio artifact:**
`/docs/model-card.md` for capstone model/prompts.

**Tools & technologies:**
DeepEval fairness, IBM AI Fairness 360 (concepts), model card templates

**Common mistakes:**
- Fairness testing only on synthetic data
- No appeals process documented
- Overclaiming AI capabilities in marketing

**Industry best practices:**
- Diverse golden eval sets
- Legal review of user-facing disclaimers
- Periodic bias re-audit post model change

**Interview preparation:**
- "AI rejected loan application—required process?"
- "How do you test for bias in hiring copilot?"

**Real-world use cases:**
HR tech, lending assist, insurance, government services.

**Topic deliverables (due end of week):**
Model card + fairness eval report for one portfolio project.

## Week 43 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 43):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 44: AI Governance & Audit Trails

**Hours:** 12–15 recommended | **Module:** 10

## Week 44 learning goals
Complete all lessons below. Submit week deliverable before starting Week 45.

### Topic 10.3: AI Governance Programs & Audit Trails

**Why this matters (job market):** EY/Deloitte frameworks emphasize governance; enterprises need immutable audit logs for AI decisions.

**Job roles:** Enterprise AI Engineer, AI Architect, Responsible AI Engineer

**Learning objectives:**
- Design AI governance committee charter (template)
- Implement immutable audit logs
- Map controls to SOC2/NIST AI RMF

---

**Lessons this week:**

#### Lesson 44.1: AI governance operating model
**Duration:** 2 hrs

**Concepts taught:**
- AI governance operating model
- How AI governance operating model fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: AI governance operating model
2. Implement a minimal working example of: AI governance operating model
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'AI governance operating model' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `ai-governance-operating-model` — code, config, or doc under docs/ or src/

#### Lesson 44.2: Policy: approved models, data classes, use cases
**Duration:** 2 hrs

**Concepts taught:**
- Policy: approved models, data classes, use cases
- How Policy: approved models, data classes, use cases fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Policy: approved models, data classes, use cases
2. Implement a minimal working example of: Policy: approved models, data classes, use cases
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Policy: approved models, data classes, use cases' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `policy-approved-models-data-classes-use` — code, config, or doc under docs/ or src/

#### Lesson 44.3: Audit log schema (who, what, when, input hash)
**Duration:** 2 hrs

**Concepts taught:**
- Audit log schema (who, what, when, input hash)
- How Audit log schema (who, what, when, input hash) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Audit log schema (who, what, when, input hash)
2. Implement a minimal working example of: Audit log schema (who, what, when, input hash)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Audit log schema (who, what, when, input hash)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `audit-log-schema-who-what-when-input-has` — code, config, or doc under docs/ or src/

#### Lesson 44.4: NIST AI RMF functions (Govern, Map, Measure, Manage)
**Duration:** 2 hrs

**Concepts taught:**
- NIST AI RMF functions (Govern, Map, Measure, Manage)
- How NIST AI RMF functions (Govern, Map, Measure, Manage) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: NIST AI RMF functions (Govern, Map, Measure, Manage)
2. Implement a minimal working example of: NIST AI RMF functions (Govern, Map, Measure, Manage)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'NIST AI RMF functions (Govern, Map, Measure, Manage)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `nist-ai-rmf-functions-govern-map-measure` — code, config, or doc under docs/ or src/

#### Lesson 44.5: Third-party model risk assessments
**Duration:** 2 hrs

**Concepts taught:**
- Third-party model risk assessments
- How Third-party model risk assessments fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Third-party model risk assessments
2. Implement a minimal working example of: Third-party model risk assessments
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Third-party model risk assessments' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `third-party-model-risk-assessments` — code, config, or doc under docs/ or src/

#### Lesson 44.6: Incident classification for AI failures
**Duration:** 2 hrs

**Concepts taught:**
- Incident classification for AI failures
- How Incident classification for AI failures fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Incident classification for AI failures
2. Implement a minimal working example of: Incident classification for AI failures
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Incident classification for AI failures' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `incident-classification-for-ai-failures` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Append-only audit log for all agent tool calls with export API.

**Enterprise project extension:**
Governance pack aligning capstone to NIST AI RMF lite.

**Portfolio artifact:**
Sample governance charter + implemented audit API.

**Tools & technologies:**
WORM storage concepts, PostgreSQL audit tables, SIEM export

**Common mistakes:**
- Mutable logs (tampering risk)
- No retention policy alignment with legal
- Governance docs without engineering controls

**Industry best practices:**
- Quarterly access reviews for AI admin roles
- Align with existing GRC tools
- AI incident runbook alongside security IR

**Interview preparation:**
- "Set up AI governance for 500-person company."
- "Audit trail requirements for HIPAA AI."

**Real-world use cases:**
Healthcare, finance, government contractors.

**Topic deliverables (due end of week):**
Audit API + governance checklist completed for capstone.

## Week 44 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 44):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 45: AI System Design & Reference Architectures

**Hours:** 12–15 recommended | **Module:** 11

## Week 45 learning goals
Complete all lessons below. Submit week deliverable before starting Week 46.

### Topic 11.1: AI System Design & Reference Architectures

**Why this matters (job market):** Senior interviews are 50%+ system design—copilot, RAG platform, agent orchestrator whiteboards.

**Job roles:** AI Architect, Senior AI Engineer, AI Platform Engineer

**Learning objectives:**
- Whiteboard enterprise copilot architecture
- Compare sync vs async vs event-driven AI
- Size components for 10K DAU

---

**Lessons this week:**

#### Lesson 45.1: Reference architectures: RAG, agent, multimodal
**Duration:** 2 hrs

**Concepts taught:**
- Reference architectures: RAG, agent, multimodal
- Grounding LLM answers in retrieved context
- Measuring retrieval quality
- State management across agent steps
- Human-in-the-loop checkpoints

**Step-by-step activities:**
1. Build pipeline script: load PDF → chunk → embed → upsert vector DB
2. Query endpoint returning answer + source chunk IDs
3. Diagram pipeline in docs/rag-architecture.md

**Lesson deliverable:** Repo artifact for `reference-architectures-rag-agent-multim` — code, config, or doc under docs/ or src/

#### Lesson 45.2: API gateway + BFF pattern
**Duration:** 2 hrs

**Concepts taught:**
- API gateway + BFF pattern
- How API gateway + BFF pattern fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: API gateway + BFF pattern
2. Implement a minimal working example of: API gateway + BFF pattern
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'API gateway + BFF pattern' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `api-gateway-bff-pattern` — code, config, or doc under docs/ or src/

#### Lesson 45.3: Caching layers and CDN for static
**Duration:** 2 hrs

**Concepts taught:**
- Caching layers and CDN for static
- How Caching layers and CDN for static fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Caching layers and CDN for static
2. Implement a minimal working example of: Caching layers and CDN for static
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Caching layers and CDN for static' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `caching-layers-and-cdn-for-static` — code, config, or doc under docs/ or src/

#### Lesson 45.4: Queue-based async for long agents
**Duration:** 2 hrs

**Concepts taught:**
- Queue-based async for long agents
- Event loop: how asyncio schedules I/O-bound tasks
- When to use async vs sync code in AI APIs
- Avoid blocking the event loop with sync SDK calls
- State management across agent steps

**Step-by-step activities:**
1. Read official docs and module notes for: Queue-based async for long agents
2. Implement a minimal working example of: Queue-based async for long agents
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Queue-based async for long agents' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `queue-based-async-for-long-agents` — code, config, or doc under docs/ or src/

#### Lesson 45.5: Data plane vs control plane
**Duration:** 2 hrs

**Concepts taught:**
- Data plane vs control plane
- How Data plane vs control plane fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Data plane vs control plane
2. Implement a minimal working example of: Data plane vs control plane
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Data plane vs control plane' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `data-plane-vs-control-plane` — code, config, or doc under docs/ or src/

#### Lesson 45.6: Disaster recovery for vector indexes
**Duration:** 2 hrs

**Concepts taught:**
- Disaster recovery for vector indexes
- How Disaster recovery for vector indexes fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Provision vector DB (local pgvector or Pinecone free tier)
2. Create index with metadata fields: tenant_id, doc_id, page
3. Query with metadata filter; verify tenant isolation

**Lesson deliverable:** Repo artifact for `disaster-recovery-for-vector-indexes` — code, config, or doc under docs/ or src/

#### Lesson 45.7: ADR (Architecture Decision Record) format
**Duration:** 2 hrs

**Concepts taught:**
- ADR (Architecture Decision Record) format
- How ADR (Architecture Decision Record) format fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: ADR (Architecture Decision Record) format
2. Implement a minimal working example of: ADR (Architecture Decision Record) format
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'ADR (Architecture Decision Record) format' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `adr-architecture-decision-record-format` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Write 3 ADRs for capstone: model choice, vector DB, agent framework.

**Enterprise project extension:**
Reference architecture library (3 diagrams) in portfolio `/docs/architecture/`.

**Portfolio artifact:**
Architecture diagrams for all flagship projects.

**Tools & technologies:**
C4 diagrams, draw.io, Mermaid, ADR templates

**Common mistakes:**
- Single diagram without data flows
- No failure mode discussion
- Ignoring cost in design doc

**Industry best practices:**
- Non-functional requirements upfront (p95, $/query)
- Explicit out-of-scope for MVP
- Review with security before build

**Interview preparation:**
- 45-min mock: "Design Slack-integrated engineering copilot"
- "Design multi-tenant RAG for 1000 customers"
- Trade-off questions: cost vs quality vs latency

**Real-world use cases:**
Platform teams standardizing AI across product lines.

**Topic deliverables (due end of week):**
3 ADRs + C4 container diagram for capstone system.

## Week 45 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 45):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 46: Scalability, Cost Optimization & FinOps

**Hours:** 12–15 recommended | **Module:** 11

## Week 46 learning goals
Complete all lessons below. Submit week deliverable before starting Week 47.

### Topic 11.2: Scalability, Cost Optimization & FinOps for AI

**Why this matters (job market):** CFOs scrutinize AI spend 2026–27; engineers who cut cost 40% without quality loss are highly valued.

**Job roles:** AI Platform Engineer, Senior AI Engineer, AI Architect

**Learning objectives:**
- Model routing for cost tiers
- Cache and batch strategies
- Build FinOps dashboard ($/tenant/day)

---

**Lessons this week:**

#### Lesson 46.1: Token economics and forecasting
**Duration:** 2 hrs

**Concepts taught:**
- Token economics and forecasting
- How Token economics and forecasting fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Token economics and forecasting
2. Implement a minimal working example of: Token economics and forecasting
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Token economics and forecasting' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `token-economics-and-forecasting` — code, config, or doc under docs/ or src/

#### Lesson 46.2: Semantic cache ROI
**Duration:** 2 hrs

**Concepts taught:**
- Semantic cache ROI
- How Semantic cache ROI fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Semantic cache ROI
2. Implement a minimal working example of: Semantic cache ROI
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Semantic cache ROI' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `semantic-cache-roi` — code, config, or doc under docs/ or src/

#### Lesson 46.3: Batch embedding jobs
**Duration:** 2 hrs

**Concepts taught:**
- Batch embedding jobs
- How Batch embedding jobs fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Batch embedding jobs
2. Implement a minimal working example of: Batch embedding jobs
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Batch embedding jobs' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `batch-embedding-jobs` — code, config, or doc under docs/ or src/

#### Lesson 46.4: Spot GPU for offline workloads
**Duration:** 2 hrs

**Concepts taught:**
- Spot GPU for offline workloads
- How Spot GPU for offline workloads fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Spot GPU for offline workloads
2. Implement a minimal working example of: Spot GPU for offline workloads
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Spot GPU for offline workloads' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `spot-gpu-for-offline-workloads` — code, config, or doc under docs/ or src/

#### Lesson 46.5: Prompt compression techniques
**Duration:** 2 hrs

**Concepts taught:**
- Prompt compression techniques
- How Prompt compression techniques fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Prompt compression techniques
2. Implement a minimal working example of: Prompt compression techniques
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Prompt compression techniques' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `prompt-compression-techniques` — code, config, or doc under docs/ or src/

#### Lesson 46.6: SLM vs LLM routing
**Duration:** 2 hrs

**Concepts taught:**
- SLM vs LLM routing
- How SLM vs LLM routing fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: SLM vs LLM routing
2. Implement a minimal working example of: SLM vs LLM routing
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'SLM vs LLM routing' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `slm-vs-llm-routing` — code, config, or doc under docs/ or src/

#### Lesson 46.7: Chargeback models for internal AI
**Duration:** 2 hrs

**Concepts taught:**
- Chargeback models for internal AI
- How Chargeback models for internal AI fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Chargeback models for internal AI
2. Implement a minimal working example of: Chargeback models for internal AI
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Chargeback models for internal AI' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `chargeback-models-for-internal-ai` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Reduce capstone $/1K queries 30% with documented tactics.

**Enterprise project extension:**
FinOps report template; budget alerts; model downgrade policy.

**Portfolio artifact:**
Before/after cost chart in README.

**Tools & technologies:**
LiteLLM budgets, Langfuse cost tracking, Infracost

**Common mistakes:**
- GPT-4 for all queries
- Re-embedding unchanged docs nightly
- No per-feature cost attribution

**Industry best practices:**
- Cost SLO per feature
- Weekly FinOps review
- Automate downgrade on budget breach

**Interview preparation:**
- "AI bill went 10× after launch—diagnosis and fix?"
- "Capacity plan for 1M queries/day RAG."

**Real-world use cases:**
High-volume support, internal search, code completion.

**Topic deliverables (due end of week):**
FinOps dashboard + cost optimization changelog.

## Week 46 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 46):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 47: Infrastructure as Code, Runbooks & Incidents

**Hours:** 12–15 recommended | **Module:** 11

## Week 47 learning goals
Complete all lessons below. Submit week deliverable before starting Week 48.

### Topic 11.3: Infrastructure as Code & Production Runbooks

**Why this matters (job market):** AI Platform roles require Terraform + mature ops—not manual console clicks.

**Job roles:** AI Platform Engineer, AI Infrastructure Engineer, LLMOps Engineer

**Learning objectives:**
- Terraform modules for AI service infra
- Write incident runbooks for AI failures
- Implement blue/green or canary deploys

---

**Lessons this week:**

#### Lesson 47.1: Terraform fundamentals for AI infrastructure
**Duration:** 3 hrs

**Concepts taught:**
- Infrastructure as Code (IaC): why manual AWS/Azure clicks fail at scale
- Terraform workflow: init → plan → apply → destroy
- Providers (aws, azurerm, google), resources, data sources
- Variables (var), outputs (output), locals — parameterizing environments
- State file: what it tracks; why remote state (S3 + DynamoDB lock) matters
- Modules: reusable infra components (vpc, postgres, bedrock-access)

**Step-by-step activities:**
1. Install Terraform CLI; run terraform version
2. Create main.tf deploying a single AWS S3 bucket for RAG document storage
3. Add variables.tf: environment (dev/staging/prod), project_name
4. Run terraform init, plan, apply; inspect state file
5. Add outputs.tf: bucket ARN and name for app config

**Lesson deliverable:** terraform/s3-storage/ module with README and applied dev bucket

#### Lesson 47.2: Terraform modules for AI services (VPC, DB, Bedrock)
**Duration:** 3 hrs

**Concepts taught:**
- Module structure: main.tf, variables.tf, outputs.tf, README
- VPC module: subnets (public/private), security groups for API and DB
- RDS Postgres or pgvector-ready Postgres for embeddings metadata
- IAM roles for Bedrock InvokeModel with least privilege (no * permissions)
- Environment separation: terraform workspaces OR separate var files (dev.tfvars, prod.tfvars)
- Tagging strategy for FinOps: project, environment, cost-center

**Step-by-step activities:**
1. Create modules/vpc and modules/postgres; compose in environments/dev/main.tf
2. Wire security group: API tier → DB tier only on 5432
3. Add IAM role module for Bedrock read + invoke on specific model ARN
4. Document module inputs/outputs in each README

**Lesson deliverable:** Composable Terraform stack: vpc + postgres + bedrock-iam modules

#### Lesson 47.3: GitHub Actions deploy pipelines & secrets management
**Duration:** 2.5 hrs

**Concepts taught:**
- CI vs CD: test on PR, deploy on merge to main
- GitHub Actions: workflow, job, step, secrets, environments
- Terraform in CI: fmt -check, validate, plan on PR; apply on approved merge
- Secrets: GitHub Secrets, AWS Secrets Manager, Azure Key Vault — never in tfvars in Git
- OIDC federation: GitHub Actions → AWS without long-lived access keys
- Container deploy after infra: build Docker → push ECR → update ECS/EKS service

**Step-by-step activities:**
1. Add .github/workflows/terraform-plan.yml running on pull_request
2. Store AWS credentials via OIDC or scoped secrets
3. Add deploy workflow: terraform apply -auto-approve on main (dev only)
4. Add docker-build job publishing to GHCR or ECR

**Lesson deliverable:** Green CI pipeline: Terraform plan on PR + deploy to dev on merge

#### Lesson 47.4: Production runbooks & AI incident response
**Duration:** 2.5 hrs

**Concepts taught:**
- Runbook purpose: on-call engineer fixes production without guessing
- Runbook template: symptoms, severity, diagnosis steps, mitigation, escalation, rollback
- Scenario: Bedrock/OpenAI rate limit — switch fallback model, enable queue, increase backoff
- Scenario: vector index corrupt — rebuild from snapshot, re-embed from source S3
- Scenario: eval faithfulness drop after deploy — rollback prompt version, compare traces
- Postmortem template: timeline, root cause, action items (blameless)
- On-call basics: alert → acknowledge → mitigate → communicate → postmortem
- Blue/green and canary for AI API deployments

**Step-by-step activities:**
1. Write runbooks/runbook-bedrock-rate-limit.md with 8 numbered steps
2. Write runbooks/runbook-vector-index-rebuild.md
3. Write runbooks/runbook-eval-regression.md
4. Run tabletop drill: instructor simulates alert; students follow runbook

**Lesson deliverable:** /runbooks/ folder with 3 tested runbooks linked from capstone README

---

**Hands-on lab (week):**
Terraform apply staging env; runbook drill: "Bedrock rate limit."

**Enterprise project extension:**
Full IaC for one cloud; DR runbook for index rebuild.

**Portfolio artifact:**
`/runbooks/` directory with 3 scenarios.

**Tools & technologies:**
Terraform, GitHub Actions, PagerDuty (concepts), Helm

**Common mistakes:**
- Terraform state not remote-backed
- Runbooks never tested
- No rollback for vector index migrations

**Industry best practices:**
- IaC-only infrastructure changes
- Game day exercises quarterly
- Versioned runbooks in Git

**Interview preparation:**
- "Terraform structure for multi-env AI platform."
- "Incident: RAG faithfulness dropped 20% after deploy."

**Real-world use cases:**
Any production AI team with on-call rotation.

**Topic deliverables (due end of week):**
Terraform module OR runbook pack linked from capstone README.

## Week 47 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 47):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 48: Capstone — Planning & Architecture

**Hours:** 12–15 recommended | **Module:** 12

## Week 48 learning goals
Complete all lessons below. Submit week deliverable before starting Week 49.

### Topic 12.1: Industry Capstone — Planning Phase

**Focus:** Choose project; architecture; metrics; repo; sprint backlog

**Lessons this week:**

#### Lesson 48.1: Capstone project selection and problem definition
**Duration:** 3 hrs

**Concepts taught:**
- Capstone selection rubric: role alignment, scope, data availability
- Problem statement: user, pain, success metric
- Build vs buy vs integrate decision
- Non-goals and MVP scope boundary

**Step-by-step activities:**
1. Choose one project from portfolio list (RAG, Support, Agent, etc.)
2. Write 1-page problem statement with target users
3. Define 3 measurable success metrics (faithfulness, latency, cost)
4. Get teacher/mentor sign-off on scope

**Lesson deliverable:** docs/capstone-proposal.md

#### Lesson 48.2: Capstone architecture and sprint planning
**Duration:** 4 hrs

**Concepts taught:**
- C4 container diagram for capstone
- Component list: UI, API, retriever/agent, DB, LLM provider
- 4-week sprint backlog structure
- Architecture review checkpoint

**Step-by-step activities:**
1. Draw architecture diagram (draw.io/Mermaid)
2. Write 2 ADRs: model choice and vector DB/agent framework
3. Create GitHub project board with 20+ tasks
4. Set up repo with Docker, CI, README template

**Lesson deliverable:** Architecture diagram + ADRs + populated project board

**Reference:** module-12-capstone-job-readiness.md · 08-project-portfolio.md

## Week 48 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 48):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 49: Capstone — Core Build Sprint

**Hours:** 12–15 recommended | **Module:** 12

## Week 49 learning goals
Complete all lessons below. Submit week deliverable before starting Week 50.

### Topic 12.1: Industry Capstone — Core Build Phase

**Focus:** MVP: core loop, LLM, RAG/agent, Docker local

**Lessons this week:**

#### Lesson 49.1: Capstone MVP — core user flow
**Duration:** 6 hrs

**Concepts taught:**
- Vertical slice delivery
- Happy-path first
- Daily commits

**Step-by-step activities:**
1. Implement primary user journey end-to-end (even if ugly UI)
2. Connect LLM API with basic prompt
3. Add RAG retrieval OR agent loop (match project type)
4. Docker compose up runs full stack locally

**Lesson deliverable:** MVP demo recording or screenshot

#### Lesson 49.2: Capstone MVP — API hardening
**Duration:** 4 hrs

**Concepts taught:**
- Input validation
- Error handling
- Health endpoints

**Step-by-step activities:**
1. Pydantic validation on all inputs
2. Structured error responses; no raw LLM errors to client
3. Add /health and /ready; logging with request IDs

**Lesson deliverable:** API passes manual test checklist

**Reference:** module-12-capstone-job-readiness.md · 08-project-portfolio.md

## Week 49 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 49):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 50: Capstone — LLMOps, Security & Deploy

**Hours:** 12–15 recommended | **Module:** 12

## Week 50 learning goals
Complete all lessons below. Submit week deliverable before starting Week 51.

### Topic 12.1: Industry Capstone — Hardening Phase

**Focus:** Tracing, eval CI, security, cloud deploy

**Lessons this week:**

#### Lesson 50.1: Capstone LLMOps — tracing and evaluation
**Duration:** 4 hrs

**Concepts taught:**
- Langfuse traces
- Ragas eval
- CI eval gate

**Step-by-step activities:**
1. Instrument all LLM and retrieval calls
2. Build 30+ case golden eval set
3. GitHub Action fails on faithfulness regression

**Lesson deliverable:** Eval score in README; CI badge

#### Lesson 50.2: Capstone security and cloud deploy
**Duration:** 5 hrs

**Concepts taught:**
- THREAT_MODEL.md
- Guardrails
- Cloud deployment

**Step-by-step activities:**
1. Write threat model; red-team top 5 attacks
2. Deploy to AWS/Azure/GCP/Railway
3. Add rate limiting and auth stub

**Lesson deliverable:** Public URL + SECURITY.md

**Reference:** module-12-capstone-job-readiness.md · 08-project-portfolio.md

## Week 50 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 50):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 51: Capstone — Polish, Demo & Documentation

**Hours:** 12–15 recommended | **Module:** 12

## Week 51 learning goals
Complete all lessons below. Submit week deliverable before starting Week 52.

### Topic 12.1: Industry Capstone — Polish Phase

**Focus:** UI, demo video, README, runbook, presentation

**Lessons this week:**

#### Lesson 51.1: Capstone UI polish and demo video
**Duration:** 4 hrs

**Concepts taught:**
- Portfolio presentation
- Demo video
- UX clarity

**Step-by-step activities:**
1. Polish chat UI; show citations if RAG
2. Record 2–3 min Loom demo
3. Add GIF to README above fold

**Lesson deliverable:** Demo video link in README

#### Lesson 51.2: Capstone documentation and presentation
**Duration:** 4 hrs

**Concepts taught:**
- Runbooks
- Executive summary
- Mock interview

**Step-by-step activities:**
1. Complete README: metrics, setup, architecture, limitations
2. Write one runbook for common failure
3. 10-min mock presentation to class/mentor

**Lesson deliverable:** Executive summary PDF + runbook + presentation slides

**Reference:** module-12-capstone-job-readiness.md · 08-project-portfolio.md

## Week 51 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 51):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

# Week 52: Job Search, Interviews & Career Launch

**Hours:** 12–15 recommended | **Module:** 12

## Week 52 learning goals
Complete all lessons below. Submit week deliverable before starting Week 52.

### Topic 12.2: AI Job Search, Interviews & Career Launch

**Why this matters (job market):** Strong engineers fail hires due to weak portfolios and system design—not weak coding.

**Job roles:** All — transition to employment

**Learning objectives:**
- Optimize resume, LinkedIn, GitHub for AI roles
- Pass system design, coding, prompt, and take-home interviews
- Execute remote and consulting job strategies

---

**Lessons this week:**

#### Lesson 52.1: AI resume format (impact metrics, not buzzwords)
**Duration:** 2 hrs

**Concepts taught:**
- AI resume format (impact metrics, not buzzwords)
- How AI resume format (impact metrics, not buzzwords) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: AI resume format (impact metrics, not buzzwords)
2. Implement a minimal working example of: AI resume format (impact metrics, not buzzwords)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'AI resume format (impact metrics, not buzzwords)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `ai-resume-format-impact-metrics-not-buzz` — code, config, or doc under docs/ or src/

#### Lesson 52.2: GitHub portfolio curation (pin 3 repos)
**Duration:** 2 hrs

**Concepts taught:**
- GitHub portfolio curation (pin 3 repos)
- How GitHub portfolio curation (pin 3 repos) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: GitHub portfolio curation (pin 3 repos)
2. Implement a minimal working example of: GitHub portfolio curation (pin 3 repos)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'GitHub portfolio curation (pin 3 repos)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `github-portfolio-curation-pin-3-repos` — code, config, or doc under docs/ or src/

#### Lesson 52.3: LinkedIn headline and featured projects
**Duration:** 2 hrs

**Concepts taught:**
- LinkedIn headline and featured projects
- How LinkedIn headline and featured projects fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: LinkedIn headline and featured projects
2. Implement a minimal working example of: LinkedIn headline and featured projects
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'LinkedIn headline and featured projects' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `linkedin-headline-and-featured-projects` — code, config, or doc under docs/ or src/

#### Lesson 52.4: System design interview patterns
**Duration:** 2 hrs

**Concepts taught:**
- System design interview patterns
- How System design interview patterns fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: System design interview patterns
2. Implement a minimal working example of: System design interview patterns
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'System design interview patterns' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `system-design-interview-patterns` — code, config, or doc under docs/ or src/

#### Lesson 52.5: Coding: Python async, data structures still required
**Duration:** 2 hrs

**Concepts taught:**
- Coding: Python async, data structures still required
- Event loop: how asyncio schedules I/O-bound tasks
- When to use async vs sync code in AI APIs
- Avoid blocking the event loop with sync SDK calls

**Step-by-step activities:**
1. Install httpx; write async def fetch(url) with await client.get
2. Run 10 URLs concurrently with asyncio.gather; time vs sync loop
3. Add timeout=30.0 and handle httpx.TimeoutException
4. Write pytest-asyncio test mocking async HTTP with respx or unittest.mock

**Lesson deliverable:** Repo artifact for `coding-python-async-data-structures-stil` — code, config, or doc under docs/ or src/

#### Lesson 52.6: Prompt engineering interviews
**Duration:** 2 hrs

**Concepts taught:**
- Prompt engineering interviews
- How Prompt engineering interviews fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Prompt engineering interviews
2. Implement a minimal working example of: Prompt engineering interviews
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Prompt engineering interviews' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `prompt-engineering-interviews` — code, config, or doc under docs/ or src/

#### Lesson 52.7: Take-home assignment strategy (time-box, document)
**Duration:** 2 hrs

**Concepts taught:**
- Take-home assignment strategy (time-box, document)
- How Take-home assignment strategy (time-box, document) fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Take-home assignment strategy (time-box, document)
2. Implement a minimal working example of: Take-home assignment strategy (time-box, document)
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Take-home assignment strategy (time-box, document)' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `take-home-assignment-strategy-time-box-d` — code, config, or doc under docs/ or src/

#### Lesson 52.8: Negotiation and leveling basics
**Duration:** 2 hrs

**Concepts taught:**
- Negotiation and leveling basics
- How Negotiation and leveling basics fits into production AI systems
- Tradeoffs and when to use vs alternatives
- Connection to enterprise job responsibilities

**Step-by-step activities:**
1. Read official docs and module notes for: Negotiation and leveling basics
2. Implement a minimal working example of: Negotiation and leveling basics
3. Integrate the example into your course project repo
4. Write docs/notes.md section: 'Negotiation and leveling basics' — definition, when to use, one pitfall
5. Peer review: explain this concept to a classmate in 2 minutes

**Lesson deliverable:** Repo artifact for `negotiation-and-leveling-basics` — code, config, or doc under docs/ or src/

---

**Hands-on lab (week):**
Mock system design with peer; record feedback.
Complete 1 take-home in 48h with eval README.

**Enterprise project extension:**
N/A — personal career deliverables.

**Portfolio artifact:**
Polish 3 repos to "hire-ready" standard using checklist Section 14.

**Tools & technologies:**
LinkedIn, GitHub, Excalidraw, Pramp/interviewing.io, levels.fyi

**Common mistakes:**
- Resume lists courses, not shipped projects
- No metrics on portfolio READMEs
- Overstudying ML theory vs system design

**Industry best practices:**
- Apply to 10–15 targeted roles/week after portfolio ready
- Warm referrals via OSS and blog posts
- Negotiate total comp, not base only

**Interview preparation:**
See [15-interview-preparation-matrix.md](../15-interview-preparation-matrix.md) and [job-readiness/](../job-readiness/).

**Real-world use cases:**
Job applications, referrals, conference networking.

**Topic deliverables (due end of week):**
- Final resume + LinkedIn
- 3 pinned GitHub repos
- Completed mock interviews (3 types)
- 30-day job search plan

## Week 52 — submit checklist

- [ ] All lesson deliverables pushed to GitHub
- [ ] Lab completed and documented in README or /docs
- [ ] Check-your-understanding questions answered in notes

**For teachers (Week 52):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.

---

## Appendix — Glossary

| Term | Definition |
|------|------------|
| API | Interface for programs to communicate over a network |
| LLM | Large Language Model (e.g. GPT-4, Claude) |
| RAG | Retrieval-Augmented Generation |
| Agent | AI system that plans and uses tools |
| Terraform | Infrastructure as Code tool for cloud resources |
| LLMOps | Operating LLM apps in production |

*Source modules: `curriculum/module-*.md` · Regenerate: `python scripts/generate_curriculum.py`*