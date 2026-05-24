# Module 01 — Python & FastAPI Foundations
### Zero-to-Hero Track · Weeks 3–7 · Foundation of Every AI Engineer Career

---

## Module Objective

This module takes you from **little or no programming experience** to building and deploying a **production-ready AI backend API** — the same kind of service that powers ChatGPT-style apps at startups and enterprises.

**Why this module matters**
- **95%+ of US AI Engineer job postings** require Python.
- Every RAG system, agent, and copilot you will build in later modules **sits on top of a web API**.
- Hiring managers reject candidates who only know Jupyter notebooks. They hire engineers who can **ship FastAPI services in Docker with CI/CD**.

**Where this is used in real companies**
- OpenAI, Anthropic, and Google sell LLMs — **your company builds the app layer in Python**.
- Stripe, Notion, and Duolingo run AI features behind **FastAPI or similar Python microservices**.
- Consulting firms deploy client copilots as **containerized Python APIs on AWS/Azure**.

**Projects you can build after this module**
- AI chat backend (ready for Module 02 LLM connection)
- Document upload API (ready for Module 04 RAG)
- Reusable `ai-engineer-starter` GitHub portfolio repo

---

## Job Roles Prepared By This Module

| Role | How this module helps |
|------|----------------------|
| AI Engineer | Core Python + API skills |
| Generative AI Engineer | Backend for LLM features |
| AI Application Developer | FastAPI + deployment |
| LLM Engineer | Production Python patterns |
| AI Platform Engineer | Docker, CI/CD foundations |
| AI Integration Engineer | REST APIs, JSON, HTTP |

---

## Beginner Skills Students Will Learn
- Install Python, VS Code, Git; use terminal without fear
- Variables, types, loops, functions, lists, dictionaries
- Read/write files and JSON
- Make HTTP requests to external APIs
- Understand what an API is and how client-server works
- Write first pytest tests

## Intermediate Skills Students Will Learn
- Object-oriented Python (classes for AI clients)
- Exception handling and logging
- Type hints and Pydantic validation
- Build REST APIs with FastAPI
- Environment variables and project structure
- async/await for concurrent I/O

## Advanced Skills Students Will Learn
- Streaming responses (SSE) for chat UIs
- Middleware, dependency injection, API versioning
- Multi-stage Docker builds
- GitHub Actions CI pipelines
- Rate limiting and request tracing

## Production-Level Skills Students Will Learn
- 12-factor app configuration
- Health/readiness probes for Kubernetes
- Structured logging (not print statements)
- Secrets management (.env, never in Git)
- Deployed public API URL with CI badge on README

---

# Topic 1.1 — Python Foundations for AI Engineers

## Why This Topic Matters

Python is the **primary language of AI engineering** in the USA. Before you call OpenAI or build RAG, you must think in code: variables, functions, data structures, files, and errors. Companies like **Databricks, Scale AI, and most YC AI startups** standardize on Python for AI backends.

**Real-world usage:** A support copilot backend receives JSON → validates it → calls an LLM → returns JSON. That entire path is Python.

## Learning Outcome

After this topic you will **write clean Python programs**, handle files and JSON, call HTTP APIs, use virtual environments, and structure a project folder like a professional engineer — not copy-paste from tutorials.

---

### Lesson 1.1.1 — What Is Programming? (Mindset Before Code)

**Concepts**
- Programs as step-by-step instructions for a computer
- Syntax: rules the language enforces (Python is strict about indentation)
- Debugging: expected part of learning, not failure
- AI engineering = software engineering + AI tools

**Analogy:** A program is a recipe. The computer is a chef who follows every step literally — if you forget "preheat oven," the dish fails.

**Exercise**
- Write pseudocode (English steps) for: "Take user question → search docs → send to AI → return answer"
- Identify inputs and outputs of each step

**Check:** Can you explain why AI engineers still need programming if ChatGPT writes code?

---

### Lesson 1.1.2 — Installing Python 3.11+ and Verifying Setup

**Concepts**
- Python interpreter vs IDE vs terminal
- PATH environment variable (Windows/Mac)
- `python --version` and `pip --version`
- Why AI courses use Python 3.11+ (performance, typing features)

**Step-by-step**
1. Download Python from python.org (check "Add to PATH" on Windows)
2. Open terminal; run `python --version` → expect 3.11.x or 3.12.x
3. Run `python` → see `>>>` REPL prompt → type `print("Hello AI")` → exit with `exit()`
4. Run `pip --version`

**Common beginner errors**
- Multiple Python versions installed; wrong one runs
- Microsoft Store Python quirks on Windows — prefer python.org installer

**Deliverable:** Screenshot of successful version check in README `setup.md`

---

### Lesson 1.1.3 — VS Code Setup for Python Development

**Concepts**
- Editor vs IDE; why VS Code dominates Python/AI work
- Extensions: Python (Microsoft), Pylance, Python Debugger
- Integrated terminal (Ctrl+` )
- Running scripts vs REPL

**Step-by-step**
1. Install VS Code
2. Install Python extension pack
3. Create folder `ai-engineer-labs`
4. Create `hello.py`; run via terminal: `python hello.py`
5. Set Python interpreter to your venv (later lesson)

**Exercise:** Configure format on save with Black or Ruff (optional preview)

**Deliverable:** `hello.py` committed to GitHub

---

### Lesson 1.1.4 — Virtual Environments and pip

**Concepts**
- Why global pip installs break projects (dependency conflicts)
- `venv` standard library module
- Activation: Windows `venv\Scripts\activate` vs Mac `source venv/bin/activate`
- `pip install package` and `pip freeze > requirements.txt`
- `.gitignore` must include `venv/` and `.env`

**Analogy:** A venv is a separate toolbox per project — hammer from Project A doesn't mix with Project B.

**Step-by-step**
1. `cd ai-engineer-labs`
2. `python -m venv venv`
3. Activate venv
4. `pip install requests httpx pytest`
5. `pip freeze > requirements.txt`

**Production note:** Enterprise projects pin versions: `requests==2.31.0`

**Deliverable:** `requirements.txt` in repo

---

### Lesson 1.1.5 — Variables, Data Types, and f-Strings

**Concepts**
- Variables as labeled boxes: `name = "Alex"`, `age = 25`
- Types: `str`, `int`, `float`, `bool`, `None`
- `type()` function
- f-strings: `f"Hello {name}"`
- Dynamic typing (Python doesn't require type declaration at assignment)

**Coding exercises**
```python
model_name = "gpt-4o"
max_tokens = 1024
temperature = 0.7
is_streaming = True
print(f"Calling {model_name} with max_tokens={max_tokens}")
```

**Exercise:** Create variables for a fake LLM request; print a formatted summary string.

**Common errors:** Using `=` vs `==`; forgetting quotes on strings

---

### Lesson 1.1.6 — Lists, Dictionaries, and JSON (Critical for AI)

**Concepts**
- Lists: ordered collections `[1, 2, 3]` — chat message history is a list
- Dictionaries: key-value `{ "role": "user", "content": "Hi" }` — OpenAI message format
- List of dictionaries = conversation history
- JSON: text format for API data; looks like Python dicts
- `json.dumps()` and `json.loads()`

**Real-world example:** OpenAI chat format
```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is RAG?"},
]
```

**Exercises**
1. Build a 3-message conversation list manually
2. Save to `chat.json` with `json.dump`
3. Load back and print each message role and content

**Deliverable:** `chat.json` + `load_chat.py`

---

### Lesson 1.1.7 — Conditionals and Loops

**Concepts**
- `if / elif / else` for branching
- `for item in list` and `while` loops
- `range()`, `enumerate()`
- When AI apps use loops: batch processing documents, retry logic

**Coding exercise:** Loop through messages; if role is `user`, count user messages; print total.

**Exercise:** Write `classify_intent(text)` returning "support" if "help" in text else "general"

---

### Lesson 1.1.8 — Functions and Return Values

**Concepts**
- `def function_name(param):` definition
- Parameters, return values, default arguments
- Docstrings: `"""Explain what function does."""`
- Pure functions vs side effects

**Coding exercise**
```python
def build_openai_message(role: str, content: str) -> dict:
    """Return a single message dict for OpenAI API."""
    return {"role": role, "content": content}
```

**Exercise:** Write `estimate_tokens(text)` rough estimate as `len(text.split()) * 1.3`

**Interview prep:** "What is the difference between a function and a method?"

---

### Lesson 1.1.9 — Modules, Packages, and Project Structure

**Concepts**
- One `.py` file = module; folder with `__init__.py` = package
- `import requests` vs `from utils import helper`
- Standard AI project layout:
```
my-ai-app/
  app/
    __init__.py
    main.py
    services/
    models/
  tests/
  requirements.txt
  .env
  README.md
```

**Exercise:** Refactor earlier scripts into `app/` package structure

**Production note:** Never name your file `openai.py` — shadows the real library

---

### Lesson 1.1.10 — File Handling and Reading Documents (RAG Preview)

**Concepts**
- `open(path, "r", encoding="utf-8")` with `with` context manager
- Reading `.txt`, preview of PDF (PyMuPDF in Module 04)
- Pathlib: `from pathlib import Path`

**Coding exercise:** Read `policy.txt`; count lines; search if keyword exists

**Real-world:** RAG pipelines start by reading files from disk — this is step zero

---

### Lesson 1.1.11 — Exceptions and try/except

**Concepts**
- Errors are normal: FileNotFoundError, ValueError, KeyError
- `try / except / finally` blocks
- Raising exceptions: `raise ValueError("message too long")`
- Fail gracefully in APIs — never crash silently

**Coding exercise:** Wrap file read; on missing file return friendly error dict

**Common beginner mistake:** Bare `except:` hiding all errors — always catch specific exceptions

---

### Lesson 1.1.12 — HTTP Requests with requests and httpx (Sync)

**Concepts**
- HTTP recap: GET (read), POST (send data), status codes 200/400/500
- Public APIs: `requests.get("https://api.github.com")`
- Headers, query params, JSON body
- API keys in headers (preview for Module 02)

**Step-by-step**
1. `pip install requests`
2. Call a free public API; print status code and JSON keys
3. Handle `requests.exceptions.Timeout`

**Exercise:** Function `fetch_url(url)` returning JSON or error dict

**Architecture note:** Your FastAPI app will BE the server; here you learn to BE the client

---

### Lesson 1.1.13 — Object-Oriented Python (Classes for AI Clients)

**Concepts**
- Classes and objects: blueprint vs instance
- `__init__`, `self`, instance methods
- Modeling an LLM client class (skeleton before real API)

**Coding exercise**
```python
class ChatHistory:
    def __init__(self):
        self.messages: list[dict] = []

    def add(self, role: str, content: str) -> None:
        self.messages.append({"role": role, "content": content})

    def as_list(self) -> list[dict]:
        return self.messages
```

**Exercise:** Add `clear()` and `last_user_message()` methods

**Why OOP for AI:** OpenAI SDK, LangChain clients, and custom services use class-based design

---

### Lesson 1.1.14 — Type Hints and Why They Matter in AI Codebases

**Concepts**
- Annotations: `def foo(x: str) -> int:`
- `list[str]`, `dict[str, Any]`, optional `str | None`
- Pydantic preview — validates types at runtime
- mypy in CI (production teams use this)

**Coding exercise:** Add type hints to all functions in your project so far

---

### Lesson 1.1.15 — Intro to Testing with pytest

**Concepts**
- Why tests matter: AI apps break when you change prompts OR code
- `test_*.py` naming; `assert` statements
- Running `pytest -v`
- Test one function with known input/output

**Coding exercise**
```python
# tests/test_messages.py
from app.messages import build_openai_message

def test_build_openai_message():
    msg = build_openai_message("user", "hi")
    assert msg["role"] == "user"
    assert msg["content"] == "hi"
```

**Production:** CI runs pytest on every git push — you will set this up in Topic 1.3

**Deliverable:** At least 5 passing tests in repo

---

### Topic 1.1 — Beginner Exercises
1. CLI mad-libs program using input() and f-strings
2. JSON contact list manager (add/list/delete contacts in file)
3. Fetch weather or GitHub API and pretty-print 3 fields
4. Quiz game with score counter and if/else

### Topic 1.1 — Mini Project
**Personal Learning Log API (CLI version):** Python script that appends daily AI learning notes to JSON file with date, topic, summary.

### Topic 1.1 — Assignment (Graded)
Build `message_utils.py` with functions: `build_message`, `save_conversation`, `load_conversation`, `count_tokens_estimate` + pytest suite with 8 tests.

### Topic 1.1 — Enterprise Scenario
*"Startup needs script to batch-read 100 support ticket JSON exports and extract customer email field for CRM import."* — Use loops, dicts, file I/O, error handling.

### Topic 1.1 — Interview Questions
- What is the difference between a list and a dictionary?
- How do you manage Python dependencies in production?
- What happens when an exception is not caught?

### Topic 1.1 — GitHub Portfolio Task
Repo `python-ai-foundations` with README, requirements.txt, tests passing, clean folder structure.

### Topic 1.1 — Common Beginner Errors
- IndentationError from mixed tabs/spaces
- Mutable default arguments in functions
- Modifying list while iterating
- Forgetting to activate venv before pip install

### Topic 1.1 — Production Best Practices
- Pin dependencies; use venv; never commit secrets
- Type hints on public functions
- Tests for any business logic

### Topic 1.1 — Architecture Diagram (Describe)
```
[Developer] → writes Python in app/
     ↓
[pytest] → validates logic
     ↓
[requirements.txt] → pins deps for reproducible deploy
```

---

# Topic 1.2 — Asynchronous & Production Python for AI Services

## Why This Topic Matters

AI applications spend most of their time **waiting**: waiting for OpenAI, waiting for a database, waiting for a vector search. Synchronous code blocks and wastes server resources. **Async Python** is how production AI APIs handle hundreds of concurrent users.

**Real-world usage:** A FastAPI server at a YC startup handles 50 simultaneous chat streams using async I/O — not 50 threads.

## Learning Outcome

You will explain async vs sync, write `async/await` code, call APIs concurrently, configure environment-based settings, and log like a production engineer.

---

### Lesson 1.2.1 — Synchronous vs Asynchronous Execution

**Concepts**
- Sync: one task at a time, blocking — like one cashier serving one customer until done
- Async: start task, switch while waiting — like taking orders while burgers cook
- I/O-bound (AI APIs) vs CPU-bound (video encoding)
- Why LLM calls are perfect for async

**Analogy:** Sync = waiting on hold doing nothing. Async = putting caller on hold and helping others until the line responds.

**Exercise:** List 5 operations in an AI chat app that involve waiting.

---

### Lesson 1.2.2 — async, await, and Coroutines

**Concepts**
- `async def` defines a coroutine (async function)
- `await` pauses until result ready
- Coroutine lifecycle: created → awaited → completed
- Cannot use `await` outside `async def`

**Coding**
```python
import asyncio

async def main():
    print("start")
    await asyncio.sleep(1)
    print("end")

asyncio.run(main())
```

**Exercise:** Write async function that waits 2 seconds then returns a string

**Common error:** Forgetting `asyncio.run()` or calling async function without await

---

### Lesson 1.2.3 — asyncio: gather, create_task, and Concurrent API Calls

**Concepts**
- `asyncio.gather()` runs multiple coroutines concurrently
- `asyncio.create_task()` schedules work
- Concurrent != parallel (still one thread, event loop switches)
- Timing demo: 5 sequential sleeps vs gather

**Coding exercise:** Fetch 5 URLs with httpx.AsyncClient in one gather; compare elapsed time to sequential

**Real-world:** Batch-embed 20 document chunks concurrently (with rate limit — later)

---

### Lesson 1.2.4 — Async HTTP with httpx for LLM-Ready Clients

**Concepts**
- `httpx.AsyncClient` context manager
- Timeouts: `timeout=30.0`
- Exception: `httpx.TimeoutException`, `httpx.HTTPStatusError`
- Headers and JSON POST body

**Coding exercise**
```python
import httpx
import asyncio

async def post_json(url: str, payload: dict) -> dict:
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        return response.json()
```

**Deliverable:** `async_client.py` with retry stub

---

### Lesson 1.2.5 — Production Async Patterns: Retries, Timeouts, Rate Limits

**Concepts**
- Exponential backoff: wait 1s, 2s, 4s on failure
- Circuit breaker concept (stop calling failing service)
- Connection pooling in httpx
- Never block event loop with `time.sleep` — use `asyncio.sleep`

**Coding exercise:** `async def fetch_with_retry(url, max_retries=3)` with exponential backoff

**Enterprise scenario:** OpenAI rate limit 429 → backoff and retry with jitter

---

### Lesson 1.2.6 — Environment Configuration (12-Factor Apps)

**Concepts**
- Config in environment variables, not hardcoded
- `.env` file + `python-dotenv` for local dev
- Never commit `.env` to Git
- Settings class loading from env

**Coding**
```python
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set")
```

**Production:** AWS Secrets Manager, Azure Key Vault in cloud — not .env files

---

### Lesson 1.2.7 — Structured Logging with logging and structlog

**Concepts**
- Why `print()` fails in production (no levels, no timestamps, no aggregation)
- DEBUG, INFO, WARNING, ERROR levels
- structlog for JSON logs (CloudWatch, Datadog ingest)
- Request ID in every log line (preview middleware in FastAPI topic)

**Coding exercise:** Replace all prints in project with `logger.info("event", key=value)`

**Deliverable:** Logs write JSON lines to stdout

---

### Lesson 1.2.8 — Pydantic Models for Data Validation

**Concepts**
- `BaseModel` classes define expected shape
- Automatic validation on creation
- `.model_dump()` for dict export
- Field constraints: `max_length`, `ge`, `le`

**Coding**
```python
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)
    temperature: float = Field(0.7, ge=0.0, le=2.0)
```

**Exercise:** Model `ChatResponse` with `answer: str` and `tokens_used: int`

**Bridge to FastAPI:** FastAPI uses Pydantic for request/response automatically

---

### Lesson 1.2.9 — pytest-asyncio for Testing Async Code

**Concepts**
- `@pytest.mark.asyncio` decorator
- `AsyncMock` for mocking httpx calls
- Test timeout behavior with short timeouts

**Coding exercise:** Test `fetch_with_retry` succeeds on 2nd attempt using mock

**Deliverable:** Async tests in CI (Topic 1.3)

---

### Topic 1.2 — Beginner Exercises
- Convert sync HTTP script to async with httpx
- Add .env loading to all configs
- Add logging to every function entry/exit

### Topic 1.2 — Mini Project
**Async Batch Fetcher:** Given list of 20 URLs in JSON file, fetch all concurrently; save results + timings to report.json.

### Topic 1.2 — Assignment
Build `AIServiceCore` package: settings from env, structured logging, async HTTP helper with retry, Pydantic request models, 10+ tests.

### Topic 1.2 — Enterprise Scenario
*"SaaS copilot must call OpenAI for 200 users at peak without 200 blocking threads."* — Design uses async FastAPI + httpx.

### Topic 1.2 — Interview Questions
- Explain async vs threading for I/O-bound LLM calls
- How do you handle OpenAI timeout errors?
- Why shouldn't you put API keys in source code?

### Topic 1.2 — Architecture Diagram
```
[User Request] → [FastAPI async route]
       ↓ await
[httpx AsyncClient] → [OpenAI API]
       ↓ await
[Response stream back to user]
Event loop handles other users while awaiting OpenAI
```

---

# Topic 1.3 — FastAPI: Building AI Backend APIs from Zero

## Why This Topic Matters

**FastAPI** is the most common Python framework for AI backends in the US job market. If you can build a FastAPI service with streaming, validation, and docs, you can integrate any LLM, RAG pipeline, or agent from later modules.

**Real-world usage:** Internal copilot at a Fortune 500 bank — React frontend talks to FastAPI on Azure App Service talks to Azure OpenAI.

## Learning Outcome

You will build a documented REST API with health checks, validated endpoints, streaming SSE for chat, middleware, and deployment-ready structure.

---

### Lesson 1.3.1 — What Is an API? (Absolute Beginner)

**Concepts**
- API = contract for programs to talk over a network
- Restaurant analogy: menu = API docs, order = request, food = response
- REST: resources identified by URLs (`/users/123`)
- JSON request and response bodies
- Frontend/backend separation

**Exercise:** Draw client (browser) → API (server) → database diagram for a chat app

---

### Lesson 1.3.2 — HTTP Methods, Status Codes, and Headers

**Concepts**
- GET (read), POST (create/action), PUT/PATCH (update), DELETE
- Status: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 422 Validation Error, 500 Server Error
- Headers: Content-Type, Authorization, X-Request-ID
- Query params: `/search?q=hello&limit=10`

**Exercise:** Use browser or curl to call https://httpbin.org/get?test=1 — inspect response

---

### Lesson 1.3.3 — Your First FastAPI Application

**Concepts**
- Install: `pip install fastapi uvicorn`
- Minimal app: `@app.get("/")`
- Run: `uvicorn app.main:app --reload`
- Automatic interactive docs at `/docs` (Swagger UI)

**Coding**
```python
from fastapi import FastAPI

app = FastAPI(title="AI Engineer Starter")

@app.get("/")
def root():
    return {"message": "AI API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
```

**Deliverable:** Running local server; screenshot of `/docs`

---

### Lesson 1.3.4 — Routes, Path Parameters, and Query Parameters

**Concepts**
- Path: `/users/{user_id}`
- Query: optional filters
- Type validation: `user_id: int` auto-converts and validates

**Exercise:** `/models/{model_name}` endpoint returning fake model info dict

---

### Lesson 1.3.5 — Request Bodies and Pydantic Integration

**Concepts**
- POST with JSON body
- FastAPI + Pydantic = automatic validation
- 422 response on invalid input with details

**Coding**
```python
@app.post("/v1/echo")
def echo(request: ChatRequest):
    return {"echo": request.message}
```

**Exercise:** POST invalid body (empty message) — observe 422 error structure

---

### Lesson 1.3.6 — APIRouter and Project Structure

**Concepts**
- Split routes: `routers/chat.py`, `routers/health.py`
- `app.include_router(chat_router, prefix="/v1")`
- Separation of concerns for team development

**Exercise:** Refactor app into `app/routers/`, `app/models/schemas.py`, `app/main.py`

---

### Lesson 1.3.7 — Middleware, CORS, and Request IDs

**Concepts**
- Middleware wraps every request
- CORS: allow frontend on different port (localhost:3000 → localhost:8000)
- Generate UUID request_id; add to logs and response header

**Coding:** Add CORS middleware for local Next.js frontend (Module 09 preview)

**Production:** Restrict CORS origins in prod — not `*` with credentials

---

### Lesson 1.3.8 — Dependency Injection in FastAPI

**Concepts**
- `Depends()` for shared logic: DB sessions, settings, LLM clients
- Testability: override dependencies in tests
- Lifecycle of dependencies

**Coding**
```python
def get_settings():
    return Settings()

@app.post("/v1/chat")
def chat(req: ChatRequest, settings: Settings = Depends(get_settings)):
    ...
```

**Real-world:** Inject OpenAI client singleton per request

---

### Lesson 1.3.9 — Server-Sent Events (SSE) for Streaming Chat

**Concepts**
- Why streaming: LLM tokens arrive over time — show typing effect
- SSE vs WebSockets (SSE simpler for one-way stream)
- `StreamingResponse` with async generator
- Media type `text/event-stream`

**Coding:** Mock stream endpoint yielding words "Hello" "from" "AI" every 0.2s

**Bridge Module 02:** Replace mock with real OpenAI stream

**Deliverable:** `/v1/chat/stream` working in browser or curl

---

### Lesson 1.3.10 — Background Tasks and API Versioning

**Concepts**
- BackgroundTasks for non-blocking side work (log to file, send webhook)
- Version prefix `/v1/` — breaking changes go to `/v2/`
- Deprecation policy in enterprise APIs

**Exercise:** After chat response, background task appends to `audit.log`

---

### Lesson 1.3.11 — Rate Limiting and Error Handling

**Concepts**
- Basic in-memory rate limiter per IP (production uses Redis)
- HTTPException with proper status codes
- Never return stack traces to clients
- Problem+JSON error format (preview)

**Exercise:** Max 10 requests/minute per IP on `/v1/chat`; return 429

---

### Lesson 1.3.12 — Authentication Intro (API Keys)

**Concepts**
- Header `Authorization: Bearer <token>` or `X-API-Key`
- Dependency verifying key before route runs
- 401 vs 403

**Coding:** Protect `/v1/chat` with API key from env; health stays public

**Production:** OAuth2, JWT, SSO — Module 07 enterprise

---

### Lesson 1.3.13 — OpenAPI, Testing FastAPI, and Deployment Prep

**Concepts**
- Auto-generated OpenAPI schema — share with frontend team
- `TestClient` from fastapi.testclient
- Test health and chat endpoints
- Readiness vs liveness: `/health` vs `/ready` (checks dependencies)

**Coding**
```python
from fastapi.testclient import TestClient
client = TestClient(app)

def test_health():
    assert client.get("/health").status_code == 200
```

**Deployment prep:** Bind `0.0.0.0:8000`; use production ASGI server settings

---

### Topic 1.3 — Beginner Exercises
- Build CRUD API for "prompts" stored in JSON file
- Add validation: prompt text max 2000 chars
- Write 6 TestClient tests

### Topic 1.3 — Mini Project
**Echo Chat API v1:** POST message → validated echo; GET health; streaming mock tokens; OpenAPI docs; pytest suite.

### Topic 1.3 — Assignment
Full **`/v1/chat`** API ready for Module 02 OpenAI swap — streaming SSE, API key auth, request ID middleware, CORS, rate limit.

### Topic 1.3 — Enterprise Scenario
*"Mobile app team needs OpenAPI spec and stable /v1/ contract before integrating LLM."*

### Topic 1.3 — Interview Questions
- Design a chat API with streaming — endpoints, auth, errors
- What is dependency injection and why use it in FastAPI?
- Difference between SSE and WebSockets for LLM streaming?

### Topic 1.3 — Deployment Exercise
Deploy to Railway or Fly.io; public URL in README; test `/health` from phone browser.

### Topic 1.3 — Architecture Diagram
```
[React/Next.js UI] --HTTP/SSE--> [FastAPI /v1/chat/stream]
                                      |
                                 [Pydantic validate]
                                      |
                                 [LLM Client] (Module 02)
                                      |
                                 [Logs + Request ID]
```

---

# Topic 1.4 — Docker, Git Workflow & CI/CD for AI Projects

## Why This Topic Matters

Interviewers ask: *"Can you deploy your AI service?"* Docker packages your app identically on laptop and cloud. GitHub Actions runs tests automatically so you never break production silently.

## Learning Outcome

You will containerize your FastAPI app, use Git branches professionally, and run CI that tests + builds Docker on every push.

---

### Lesson 1.4.1 — Git Fundamentals for AI Engineers

**Concepts**
- commit = snapshot; push = upload to GitHub
- `.gitignore`: venv, .env, __pycache__, .pytest_cache
- Meaningful commit messages: "Add streaming chat endpoint"
- Branch `feature/chat-stream`; merge via PR

**Exercise:** 10 commits on starter repo with clear messages; no secrets committed

---

### Lesson 1.4.2 — Dockerfile Line-by-Line for Python AI API

**Concepts**
- Base image `python:3.11-slim`
- WORKDIR, COPY requirements, pip install, COPY app
- EXPOSE 8000
- CMD uvicorn command
- Multi-stage build: builder + runtime (smaller image)
- Non-root USER for security

**Coding:** Dockerfile that runs your FastAPI app; `.dockerignore` excludes venv and tests cache

**Exercise:** `docker build -t ai-api .` && `docker run -p 8000:8000 ai-api`

---

### Lesson 1.4.3 — docker-compose for Local Development

**Concepts**
- Multi-container: API + Postgres + Redis (Redis used later for cache)
- `docker-compose.yml` services, ports, env_file
- Volume mounts for hot reload during dev

**Exercise:** compose file with `api` service; optional `postgres` for Module 04

---

### Lesson 1.4.4 — GitHub Actions CI Pipeline

**Concepts**
- Trigger on push and pull_request
- Steps: checkout → setup-python → pip install → pytest → ruff lint
- Fail PR if tests fail — enterprise standard

**Coding:** `.github/workflows/ci.yml` with Python 3.11 matrix

**Deliverable:** CI badge in README `[![CI](https://github.com/you/repo/actions/workflows/ci.yml/badge.svg)]`

---

### Lesson 1.4.5 — Docker Build in CI and Image Registry

**Concepts**
- Build and push to GitHub Container Registry (ghcr.io)
- Tag with git SHA for traceability
- Trivy scan for vulnerabilities (awareness)

**Production:** Deploy same SHA image to staging then prod — immutable artifacts

---

### Topic 1.4 — Beginner Exercises
- Fix intentional failing test; watch CI fail then pass
- Add ruff format check to CI

### Topic 1.4 — Mini Project
Dockerized AI starter with green CI on every push to main.

### Topic 1.4 — Assignment
Full pipeline: lint → test → docker build → push GHCR on merge to main.

### Topic 1.4 — Enterprise Scenario
*"Platform team requires all AI microservices deployed only from CI-built signed images."*

### Topic 1.4 — Interview Questions
- Walk through your CI/CD for an AI feature
- What goes in .dockerignore and why?
- How do you manage secrets in CI?

### Topic 1.4 — Runbook (Write This)
**Deploy new version:** merge PR → CI green → pull image SHA xyz → deploy → verify /health → rollback if 5xx spike.

### Topic 1.4 — Module 01 Capstone Deliverable
**`ai-engineer-starter` GitHub repository containing:**
- [ ] Python package structure with tests (20+ tests)
- [ ] FastAPI `/v1/chat` + `/health` + streaming mock
- [ ] Dockerfile + docker-compose
- [ ] GitHub Actions CI passing
- [ ] Deployed public URL OR screenshot
- [ ] README with architecture diagram and setup steps

---

## Module 01 — Master Checklist Before Module 02

| Skill | Can you do this? |
|-------|------------------|
| Python venv + pip | Yes / No |
| Write functions with types | Yes / No |
| Read/write JSON | Yes / No |
| pytest passing locally | Yes / No |
| async httpx call | Yes / No |
| FastAPI with Pydantic | Yes / No |
| SSE streaming endpoint | Yes / No |
| Docker run locally | Yes / No |
| CI green on GitHub | Yes / No |

**If any "No" — complete that topic before Module 02.** Module 02 connects real OpenAI keys to the FastAPI app you built here.

---

*Next module: [module-02-llm-apis-foundations.md](./module-02-llm-apis-foundations.md)*
