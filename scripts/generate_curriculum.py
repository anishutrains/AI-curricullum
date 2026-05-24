"""Generate detailed week-by-week CURRICULUM-COMPLETE.md from module files."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURRICULUM_DIR = ROOT / "curriculum"
OUTPUT = ROOT / "CURRICULUM-COMPLETE.md"

WEEK_PLAN = [
    (1, "Computer & Internet Fundamentals", "foundation", ["F1"]),
    (2, "Programming Mindset & Developer Tools", "foundation", ["F2", "F3"]),
    (3, "Python Basics for AI", "01", ["1.1-partial"]),
    (4, "Production Python — Async, Config & Testing", "01", ["1.1"]),
    (5, "FastAPI — REST APIs for AI (Part 1)", "01", ["1.2-partial"]),
    (6, "FastAPI — Streaming, Versioning & Middleware", "01", ["1.2"]),
    (7, "Docker, Git & CI/CD", "01", ["1.3"]),
    (8, "OpenAI API — Chat & Streaming", "02", ["2.1-partial"]),
    (9, "OpenAI API — Tools, Batch & Fine-Tuning", "02", ["2.1"]),
    (10, "Anthropic Claude & Google Gemini APIs", "02", ["2.2"]),
    (11, "Open-Source Models — Ollama & HuggingFace", "02", ["2.3"]),
    (12, "Structured Outputs & Model Routing", "02", ["2.4"]),
    (13, "Production Prompt Engineering", "03", ["3.1"]),
    (14, "DSPy — Programmatic Prompt Optimization", "03", ["3.2"]),
    (15, "Prompt Security & Injection Defense", "03", ["3.3"]),
    (16, "RAG Architecture Fundamentals", "04", ["4.1"]),
    (17, "Chunking & Embedding Strategies", "04", ["4.2"]),
    (18, "Vector Databases & Hybrid Search", "04", ["4.3"]),
    (19, "Reranking, Caching & Retrieval Optimization", "04", ["4.4"]),
    (20, "Advanced RAG — Graphs & Agentic RAG", "04", ["4.5"]),
    (21, "AI Agents & Tool Calling", "05", ["5.1"]),
    (22, "LangGraph — Stateful Agent Workflows", "05", ["5.2"]),
    (23, "Multi-Agent Systems — CrewAI & AutoGen", "05", ["5.3"]),
    (24, "Browser, Code Agents & AI Employees", "05", ["5.4"]),
    (25, "Semantic Kernel & Enterprise Agents", "05", ["5.5"]),
    (26, "LLM Observability & Tracing", "06", ["6.1"]),
    (27, "AI Evaluation Pipelines", "06", ["6.2"]),
    (28, "Prompt Versioning & AI CI/CD", "06", ["6.3"]),
    (29, "Guardrails, Governance & Model Registry", "06", ["6.4"]),
    (30, "AI Compliance, Privacy & Data Governance", "07", ["7.1"]),
    (31, "AI Risk Management & Hallucination Prevention", "07", ["7.2"]),
    (32, "RBAC, Multi-Tenancy & Enterprise Integrations", "07", ["7.3"]),
    (33, "AI Consulting & Transformation Delivery", "07", ["7.4"]),
    (34, "AWS AI — Bedrock & SageMaker", "08", ["8.1"]),
    (35, "Azure AI — OpenAI & AI Search", "08", ["8.2"]),
    (36, "GCP Vertex AI & Gemini Enterprise", "08", ["8.3"]),
    (37, "Kubernetes, GPU & Inference Optimization", "08", ["8.4"]),
    (38, "Next.js AI Frontends & Streaming UX", "09", ["9.1"]),
    (39, "Multimodal & Voice AI Applications", "09", ["9.2"]),
    (40, "AI SaaS Products & Copilot Patterns", "09", ["9.3"]),
    (41, "TypeScript & Workflow Automation UI", "09", ["9.4"]),
    (42, "AI Security — Threat Models & Red Teaming", "10", ["10.1"]),
    (43, "Responsible AI — Bias, Fairness & Transparency", "10", ["10.2"]),
    (44, "AI Governance & Audit Trails", "10", ["10.3"]),
    (45, "AI System Design & Reference Architectures", "11", ["11.1"]),
    (46, "Scalability, Cost Optimization & FinOps", "11", ["11.2"]),
    (47, "Infrastructure as Code, Runbooks & Incidents", "11", ["11.3"]),
    (48, "Capstone — Planning & Architecture", "12", ["12.1-partial"]),
    (49, "Capstone — Core Build Sprint", "12", ["12.1-build"]),
    (50, "Capstone — LLMOps, Security & Deploy", "12", ["12.1-hardening"]),
    (51, "Capstone — Polish, Demo & Documentation", "12", ["12.1-finish"]),
    (52, "Job Search, Interviews & Career Launch", "12", ["12.2"]),
]

# Detailed lesson overrides — full teaching content beyond subtopic bullets
DETAILED_LESSONS = {
    "11.3": [
        {
            "title": "Terraform fundamentals for AI infrastructure",
            "duration": "3 hrs",
            "concepts": [
                "Infrastructure as Code (IaC): why manual AWS/Azure clicks fail at scale",
                "Terraform workflow: init → plan → apply → destroy",
                "Providers (aws, azurerm, google), resources, data sources",
                "Variables (var), outputs (output), locals — parameterizing environments",
                "State file: what it tracks; why remote state (S3 + DynamoDB lock) matters",
                "Modules: reusable infra components (vpc, postgres, bedrock-access)",
            ],
            "activities": [
                "Install Terraform CLI; run terraform version",
                "Create main.tf deploying a single AWS S3 bucket for RAG document storage",
                "Add variables.tf: environment (dev/staging/prod), project_name",
                "Run terraform init, plan, apply; inspect state file",
                "Add outputs.tf: bucket ARN and name for app config",
            ],
            "deliverable": "terraform/s3-storage/ module with README and applied dev bucket",
        },
        {
            "title": "Terraform modules for AI services (VPC, DB, Bedrock)",
            "duration": "3 hrs",
            "concepts": [
                "Module structure: main.tf, variables.tf, outputs.tf, README",
                "VPC module: subnets (public/private), security groups for API and DB",
                "RDS Postgres or pgvector-ready Postgres for embeddings metadata",
                "IAM roles for Bedrock InvokeModel with least privilege (no * permissions)",
                "Environment separation: terraform workspaces OR separate var files (dev.tfvars, prod.tfvars)",
                "Tagging strategy for FinOps: project, environment, cost-center",
            ],
            "activities": [
                "Create modules/vpc and modules/postgres; compose in environments/dev/main.tf",
                "Wire security group: API tier → DB tier only on 5432",
                "Add IAM role module for Bedrock read + invoke on specific model ARN",
                "Document module inputs/outputs in each README",
            ],
            "deliverable": "Composable Terraform stack: vpc + postgres + bedrock-iam modules",
        },
        {
            "title": "GitHub Actions deploy pipelines & secrets management",
            "duration": "2.5 hrs",
            "concepts": [
                "CI vs CD: test on PR, deploy on merge to main",
                "GitHub Actions: workflow, job, step, secrets, environments",
                "Terraform in CI: fmt -check, validate, plan on PR; apply on approved merge",
                "Secrets: GitHub Secrets, AWS Secrets Manager, Azure Key Vault — never in tfvars in Git",
                "OIDC federation: GitHub Actions → AWS without long-lived access keys",
                "Container deploy after infra: build Docker → push ECR → update ECS/EKS service",
            ],
            "activities": [
                "Add .github/workflows/terraform-plan.yml running on pull_request",
                "Store AWS credentials via OIDC or scoped secrets",
                "Add deploy workflow: terraform apply -auto-approve on main (dev only)",
                "Add docker-build job publishing to GHCR or ECR",
            ],
            "deliverable": "Green CI pipeline: Terraform plan on PR + deploy to dev on merge",
        },
        {
            "title": "Production runbooks & AI incident response",
            "duration": "2.5 hrs",
            "concepts": [
                "Runbook purpose: on-call engineer fixes production without guessing",
                "Runbook template: symptoms, severity, diagnosis steps, mitigation, escalation, rollback",
                "Scenario: Bedrock/OpenAI rate limit — switch fallback model, enable queue, increase backoff",
                "Scenario: vector index corrupt — rebuild from snapshot, re-embed from source S3",
                "Scenario: eval faithfulness drop after deploy — rollback prompt version, compare traces",
                "Postmortem template: timeline, root cause, action items (blameless)",
                "On-call basics: alert → acknowledge → mitigate → communicate → postmortem",
                "Blue/green and canary for AI API deployments",
            ],
            "activities": [
                "Write runbooks/runbook-bedrock-rate-limit.md with 8 numbered steps",
                "Write runbooks/runbook-vector-index-rebuild.md",
                "Write runbooks/runbook-eval-regression.md",
                "Run tabletop drill: instructor simulates alert; students follow runbook",
            ],
            "deliverable": "/runbooks/ folder with 3 tested runbooks linked from capstone README",
        },
    ],
}

FOUNDATION_TOPICS = {
    "F1": {
        "name": "How Computers and the Internet Work",
        "why": "Students new to IT must understand hardware, software, and how web apps work before coding.",
        "objectives": [
            "Explain CPU, memory, storage, and operating system roles",
            "Describe client-server model and HTTP request/response",
            "Use terminal to navigate files and folders",
        ],
        "lessons": [
            {
                "title": "Computer hardware and software basics",
                "duration": "2 hrs",
                "concepts": [
                    "CPU, RAM, storage, input/output devices",
                    "Operating systems: Windows, macOS, Linux",
                    "Applications vs system software",
                    "How code becomes a running program (compile/interpreter overview)",
                ],
                "activities": [
                    "Draw diagram: User → Application → OS → Hardware",
                    "Identify your OS version and available disk/RAM",
                ],
                "deliverable": "One-page diagram in notebook or Notion",
            },
            {
                "title": "Internet, browsers, and how websites work",
                "duration": "2 hrs",
                "concepts": [
                    "Internet vs World Wide Web",
                    "URLs, DNS, IP addresses (conceptual)",
                    "HTTP methods: GET, POST; status codes 200, 404, 500",
                    "Frontend vs backend; JSON data format",
                ],
                "activities": [
                    "DevTools → Network → reload → inspect one request",
                    "Label: URL, method, status, response type",
                ],
                "deliverable": "Annotated screenshot of HTTP request",
            },
            {
                "title": "Command line essentials",
                "duration": "2 hrs",
                "concepts": [
                    "Terminal vs GUI; paths absolute vs relative",
                    "cd, ls/dir, mkdir, touch, cat/type, pwd",
                ],
                "activities": ["Create ai-engineer-course folder structure via terminal only"],
                "deliverable": "Folder tree screenshot",
            },
        ],
        "lab": "Write README section: 'What happens when I visit a website' in 5 steps.",
        "tools": ["Terminal", "Browser DevTools"],
        "mistakes": ["Skipping terminal practice"],
        "check": ["RAM vs storage?", "What is HTTP 404?"],
        "teachers": "Pair students for terminal labs.",
    },
    "F2": {
        "name": "Introduction to Programming",
        "why": "AI engineering is software engineering. Students need computational thinking before Python.",
        "objectives": [
            "Define algorithm, variable, function, loop, condition",
            "Write first Python programs",
            "Read and fix simple error messages",
        ],
        "lessons": [
            {
                "title": "Computational thinking",
                "duration": "2 hrs",
                "concepts": ["Algorithms", "Sequence, selection, iteration", "Decomposition", "Debugging mindset"],
                "activities": ["Pseudocode for making tea", "Trace a 3-iteration loop on paper"],
                "deliverable": "Pseudocode for guess-the-number game",
            },
            {
                "title": "Python installation and first scripts",
                "duration": "3 hrs",
                "concepts": ["Python 3.11+ install", "print, variables, input()", "strings, int, float", "f-strings"],
                "activities": ["hello.py greets user by name"],
                "deliverable": "hello.py on GitHub",
            },
            {
                "title": "Control flow and functions",
                "duration": "3 hrs",
                "concepts": ["if/elif/else", "for/while loops", "def functions", "lists, dicts", "common errors"],
                "activities": ["celsius_to_fahrenheit(c)", "loop print uppercase words"],
                "deliverable": "practice_week2.py",
            },
        ],
        "lab": "CLI quiz app: 3 questions, score at end.",
        "tools": ["Python", "VS Code"],
        "mistakes": ["Ignoring indentation errors"],
        "check": ["What is a function?", "When use a loop?"],
        "teachers": "Live-debug intentional errors.",
    },
    "F3": {
        "name": "Developer Environment Setup",
        "why": "Professional AI engineers use Git, venv, and IDE workflows daily.",
        "objectives": ["Configure VS Code", "Use GitHub", "Create virtual environments"],
        "lessons": [
            {
                "title": "VS Code for Python",
                "duration": "2 hrs",
                "concepts": ["Workspace", "Integrated terminal", "Python extension", "Breakpoints intro"],
                "activities": ["Debug quiz script with breakpoint"],
                "deliverable": "VS Code project screenshot",
            },
            {
                "title": "Git and GitHub",
                "duration": "3 hrs",
                "concepts": ["init, add, commit, push", ".gitignore", "README purpose"],
                "activities": ["Create repo; push Week 2 code"],
                "deliverable": "Public GitHub URL",
            },
            {
                "title": "Virtual environments and pip",
                "duration": "2 hrs",
                "concepts": ["venv", "pip install", "requirements.txt", "never commit secrets"],
                "activities": ["venv + pip install requests + freeze"],
                "deliverable": "requirements.txt in repo",
            },
            {
                "title": "What is AI? Roadmap preview",
                "duration": "90 min",
                "concepts": ["AI/ML/GenAI definitions", "LLM, RAG, agents preview", "52-week map"],
                "activities": ["Compare good vs bad ChatGPT prompt", "Pick 2 job roles"],
                "deliverable": "Learning goals in README",
            },
        ],
        "lab": "Full dev environment configured and pushed to GitHub.",
        "tools": ["VS Code", "Git", "GitHub", "venv"],
        "mistakes": ["Committing .env files"],
        "check": ["git commit does what?", "Why venv?"],
        "teachers": "Budget time for Git auth on Windows.",
    },
}

PARTIAL = {
    "1.1-partial": {
        "lessons": [
            {
                "title": "Python data structures and files for AI apps",
                "duration": "3 hrs",
                "concepts": [
                    "Lists and dicts for chat message history",
                    "JSON: json.load, json.dump, serialization",
                    "Reading/writing text files and JSON files",
                    "List comprehensions",
                ],
                "activities": ["Save 5 messages as messages.json", "Load and print formatted"],
                "deliverable": "messages.json + load_messages.py",
            },
            {
                "title": "Errors, exceptions, and logging basics",
                "duration": "3 hrs",
                "concepts": [
                    "try/except/finally",
                    "Common exceptions: ValueError, FileNotFoundError, KeyError",
                    "logging module: DEBUG, INFO, WARNING, ERROR",
                    "Why logging beats print in production",
                ],
                "activities": ["Wrap file load in try/except", "Configure logging to file"],
                "deliverable": "Script with logging and error handling",
            },
        ]
    },
    "1.2-partial": {"take_subtopics": (0, 2)},
    "1.2": {"take_subtopics": (2, None)},
    "2.1-partial": {"take_subtopics": (0, 3)},
    "2.1": {"take_subtopics": (3, None)},
}


def parse_module(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    topics = {}
    blocks = re.split(r"\n---\n", text)
    for block in blocks:
        m = re.search(r"## Topic (\d+\.\d+): (.+)", block)
        if not m:
            continue
        tid = m.group(1)

        def field(n):
            fm = re.search(rf"### {n}\. [^\n]+\n(.+?)(?=\n### |\Z)", block, re.S)
            return fm.group(1).strip() if fm else ""

        subtopics = [ln.strip()[2:].strip() for ln in field(5).splitlines() if ln.strip().startswith("- ")]
        topics[tid] = {
            "name": field(1) or m.group(2).strip(),
            "why": field(2),
            "roles": field(3),
            "objectives": [ln.strip()[2:] for ln in field(4).splitlines() if ln.strip().startswith("- ")],
            "subtopics": subtopics,
            "lab": field(6),
            "enterprise": field(7),
            "portfolio": field(8),
            "interview": field(9),
            "use_cases": field(10),
            "tools": field(11),
            "mistakes": [ln.strip()[2:] for ln in field(12).splitlines() if ln.strip().startswith("- ")],
            "best_practices": [ln.strip()[2:] for ln in field(13).splitlines() if ln.strip().startswith("- ")],
            "deliverables": field(14),
        }
    mod_num = re.search(r"module-(\d+)", path.name).group(1)
    title_m = re.search(r"# Module \d+ — (.+)", text)
    return {"num": mod_num, "title": title_m.group(1).strip() if title_m else "", "topics": topics}


def clean_lab(text: str) -> str:
    return re.sub(r"\*\*Lab[^:*]*:\*\*\s*", "", text).strip()


def concept_expansions(subtopic: str) -> list:
    """Add teaching detail beneath each module subtopic bullet."""
    s = subtopic.lower()
    extra = []
    if "async" in s:
        extra += [
            "Event loop: how asyncio schedules I/O-bound tasks",
            "When to use async vs sync code in AI APIs",
            "Avoid blocking the event loop with sync SDK calls",
        ]
    if "pydantic" in s:
        extra += ["BaseModel validation", "Field constraints", "Serialization for API responses"]
    if "fastapi" in s or "router" in s:
        extra += ["APIRouter for modular routes", "Dependency injection pattern"]
    if "docker" in s:
        extra += ["Layer caching in builds", "Non-root user in container", ".dockerignore"]
    if "rag" in s or "retrieval" in s:
        extra += ["Grounding LLM answers in retrieved context", "Measuring retrieval quality"]
    if "langgraph" in s or "agent" in s:
        extra += ["State management across agent steps", "Human-in-the-loop checkpoints"]
    if "terraform" in s:
        extra += ["Declarative infra", "Plan before apply", "Idempotent resource management"]
    if "eval" in s or "ragas" in s:
        extra += ["Golden datasets", "Regression gates before deploy"]
    if not extra:
        extra = [
            f"How {subtopic} fits into production AI systems",
            "Tradeoffs and when to use vs alternatives",
            "Connection to enterprise job responsibilities",
        ]
    return extra[:4]


def activities_for_subtopic(subtopic: str, topic_name: str, lab: str, index: int) -> list:
    """Generate specific step-by-step activities per subtopic."""
    s = subtopic.lower()
    if "async/await" in s or "async" in s and "python" in s:
        return [
            "Install httpx; write async def fetch(url) with await client.get",
            "Run 10 URLs concurrently with asyncio.gather; time vs sync loop",
            "Add timeout=30.0 and handle httpx.TimeoutException",
            "Write pytest-asyncio test mocking async HTTP with respx or unittest.mock",
        ]
    if "pydantic" in s:
        return [
            "Define ChatRequest(BaseModel) with message: str, max_length=4000",
            "Add validator rejecting empty strings",
            "Return model.model_dump() from endpoint; test invalid payload → 422",
        ]
    if "structlog" in s or "logging" in s:
        return [
            "Configure structlog with JSON output and timestamp",
            "Replace all print() in project with logger.info/error",
            "Add request_id to log context in FastAPI middleware",
        ]
    if "pytest" in s:
        return [
            "Create tests/test_health.py asserting GET /health == 200",
            "Add async test for chat endpoint with TestClient",
            "Run pytest -v; add to CI workflow",
        ]
    if "dockerfile" in s:
        return [
            "Write multi-stage Dockerfile: builder + slim runtime",
            "Run as non-root user; expose port 8000",
            "docker build -t ai-api . && docker run -p 8000:8000 ai-api",
        ]
    if "github actions" in s:
        return [
            "Create .github/workflows/ci.yml: checkout, setup-python, pytest, ruff",
            "Add docker build step on push to main",
            "Add status badge to README",
        ]
    if "streaming" in s and "openai" in s.lower() or "streaming deltas" in s:
        return [
            "Call client.chat.completions.create(stream=True)",
            "Iterate chunks; yield SSE from FastAPI StreamingResponse",
            "Log time-to-first-token metric",
        ]
    if "rag" in s and "architecture" in s or "ingestion" in s:
        return [
            "Build pipeline script: load PDF → chunk → embed → upsert vector DB",
            "Query endpoint returning answer + source chunk IDs",
            "Diagram pipeline in docs/rag-architecture.md",
        ]
    if "chunk" in s:
        return [
            "Split sample PDF with RecursiveCharacterTextSplitter sizes 256/512/1024",
            "Run 10 test queries; record which chunk size wins on faithfulness",
            "Document winning config in docs/chunking.md",
        ]
    if "vector" in s or "pinecone" in s or "pgvector" in s:
        return [
            "Provision vector DB (local pgvector or Pinecone free tier)",
            "Create index with metadata fields: tenant_id, doc_id, page",
            "Query with metadata filter; verify tenant isolation",
        ]
    if "langgraph" in s or "checkpoint" in s:
        return [
            "Install langgraph; define StateGraph with 3 nodes",
            "Add PostgresSaver checkpointer; restart mid-run and resume",
            "Stream node events to log for debugging",
        ]
    if "langfuse" in s or "tracing" in s:
        return [
            "Create Langfuse project; add keys to .env",
            "Wrap LLM call and retriever call in spans",
            "View full trace in Langfuse UI; screenshot for README",
        ]
    if "ragas" in s or "faithfulness" in s:
        return [
            "Create golden CSV: question, expected_sources, reference_answer",
            "Run Ragas evaluate(); record faithfulness score",
            "Add GitHub Action failing if score drops >5%",
        ]
    if "gdpr" in s or "deletion" in s:
        return [
            "Map data flows: user input → logs → vector index",
            "Implement DELETE /users/{id} removing vectors and chat history",
            "Document retention policy in COMPLIANCE.md",
        ]
    if "bedrock" in s:
        return [
            "Enable Bedrock model access in AWS console",
            "Invoke Converse API with boto3 from Python script",
            "Create Knowledge Base; sync S3 folder; query via API",
        ]
    if "next.js" in s or "usechat" in s:
        return [
            "npx create-next-app; install ai package",
            "Wire useChat hook to FastAPI SSE endpoint",
            "Render streaming markdown with loading and stop button",
        ]
    if "prompt" in s and "few-shot" in s:
        return [
            "Write system prompt with 3 labeled examples in YAML",
            "A/B test v1 vs v2 on 20-question golden set",
            "Version prompts in prompts/ folder with Git tags",
        ]
    # Default — still specific, not generic
    return [
        f"Read official docs and module notes for: {subtopic}",
        f"Implement a minimal working example of: {subtopic}",
        f"Integrate the example into your course project repo",
        f"Write docs/notes.md section: '{subtopic}' — definition, when to use, one pitfall",
        "Peer review: explain this concept to a classmate in 2 minutes",
    ]


def lesson_from_subtopic(subtopic: str, topic: dict, index: int) -> dict:
    title = subtopic.strip()
    concepts = [subtopic] + concept_expansions(subtopic)
    activities = activities_for_subtopic(subtopic, topic["name"], topic.get("lab", ""), index)
    slug = re.sub(r"[^a-z0-9]+", "-", subtopic.lower())[:40].strip("-")
    return {
        "title": title,
        "duration": "2 hrs",
        "concepts": concepts,
        "activities": activities,
        "deliverable": f"Repo artifact for `{slug}` — code, config, or doc under docs/ or src/",
    }


def build_lessons_from_subtopics(topic: dict, key: str) -> list:
    base = key.split("-")[0]
    if base in DETAILED_LESSONS and not key.endswith("-partial"):
        return DETAILED_LESSONS[base]

    if key in PARTIAL and "lessons" in PARTIAL[key]:
        return PARTIAL[key]["lessons"]

    subs = topic["subtopics"]
    if key in PARTIAL and "take_subtopics" in PARTIAL[key]:
        start, end = PARTIAL[key]["take_subtopics"]
        subs = subs[start:end]

    # One detailed lesson per subtopic (from module ### 5. Lessons/Subtopics)
    return [lesson_from_subtopic(st, topic, i) for i, st in enumerate(subs)]


def fmt_lesson(num: str, les: dict) -> str:
    lines = [
        f"#### Lesson {num}: {les['title']}",
        f"**Duration:** {les['duration']}",
        "",
        "**Concepts taught:**",
    ]
    for c in les["concepts"]:
        lines.append(f"- {c}")
    lines += ["", "**Step-by-step activities:**"]
    for i, a in enumerate(les.get("activities", []), 1):
        lines.append(f"{i}. {a}")
    if les.get("deliverable"):
        lines += ["", f"**Lesson deliverable:** {les['deliverable']}"]
    return "\n".join(lines)


def render_topic(topic_id: str, topic: dict, week: int, key: str) -> str:
    base = key.split("-")[0]
    lessons = build_lessons_from_subtopics(topic, key)
    lines = [
        f"### Topic {base}: {topic['name']}",
        "",
        f"**Why this matters (job market):** {topic['why']}",
        "",
        f"**Job roles:** {topic['roles']}",
        "",
        "**Learning objectives:**",
    ]
    for o in topic["objectives"]:
        lines.append(f"- {o}")
    lines += ["", "---", "", "**Lessons this week:**", ""]
    for i, les in enumerate(lessons, 1):
        lines.append(fmt_lesson(f"{week}.{i}", les))
        lines.append("")
    lines += [
        "---",
        "",
        "**Hands-on lab (week):**",
        clean_lab(topic["lab"]),
        "",
        "**Enterprise project extension:**",
        topic["enterprise"],
        "",
        "**Portfolio artifact:**",
        topic["portfolio"],
        "",
        "**Tools & technologies:**",
        topic["tools"],
        "",
        "**Common mistakes:**",
    ]
    for m in topic["mistakes"]:
        lines.append(f"- {m}")
    lines += ["", "**Industry best practices:**"]
    for b in topic["best_practices"]:
        lines.append(f"- {b}")
    lines += [
        "",
        "**Interview preparation:**",
        topic["interview"],
        "",
        "**Real-world use cases:**",
        topic["use_cases"],
        "",
        "**Topic deliverables (due end of week):**",
        topic["deliverables"],
        "",
    ]
    return "\n".join(lines)


def render_foundation(tid: str, week: int) -> str:
    t = FOUNDATION_TOPICS[tid]
    lines = [
        f"### Topic {tid}: {t['name']}",
        "",
        f"**Why this matters:** {t['why']}",
        "",
        "**Learning objectives:**",
    ]
    for o in t["objectives"]:
        lines.append(f"- {o}")
    lines += ["", "**Lessons this week:**", ""]
    for i, les in enumerate(t["lessons"], 1):
        lines.append(fmt_lesson(f"{week}.{i}", les))
        lines.append("")
    lines += [
        "**Hands-on lab:** " + t["lab"],
        "",
        "**Tools:** " + ", ".join(t["tools"]),
        "",
        "**Check your understanding:**",
    ]
    for c in t["check"]:
        lines.append(f"- {c}")
    lines += ["", f"**For teachers:** {t['teachers']}", ""]
    return "\n".join(lines)


CAPSTONE_LESSONS = {
    "12.1-partial": [
        {
            "title": "Capstone project selection and problem definition",
            "duration": "3 hrs",
            "concepts": [
                "Capstone selection rubric: role alignment, scope, data availability",
                "Problem statement: user, pain, success metric",
                "Build vs buy vs integrate decision",
                "Non-goals and MVP scope boundary",
            ],
            "activities": [
                "Choose one project from portfolio list (RAG, Support, Agent, etc.)",
                "Write 1-page problem statement with target users",
                "Define 3 measurable success metrics (faithfulness, latency, cost)",
                "Get teacher/mentor sign-off on scope",
            ],
            "deliverable": "docs/capstone-proposal.md",
        },
        {
            "title": "Capstone architecture and sprint planning",
            "duration": "4 hrs",
            "concepts": [
                "C4 container diagram for capstone",
                "Component list: UI, API, retriever/agent, DB, LLM provider",
                "4-week sprint backlog structure",
                "Architecture review checkpoint",
            ],
            "activities": [
                "Draw architecture diagram (draw.io/Mermaid)",
                "Write 2 ADRs: model choice and vector DB/agent framework",
                "Create GitHub project board with 20+ tasks",
                "Set up repo with Docker, CI, README template",
            ],
            "deliverable": "Architecture diagram + ADRs + populated project board",
        },
    ],
    "12.1-build": [
        {
            "title": "Capstone MVP — core user flow",
            "duration": "6 hrs",
            "concepts": ["Vertical slice delivery", "Happy-path first", "Daily commits"],
            "activities": [
                "Implement primary user journey end-to-end (even if ugly UI)",
                "Connect LLM API with basic prompt",
                "Add RAG retrieval OR agent loop (match project type)",
                "Docker compose up runs full stack locally",
            ],
            "deliverable": "MVP demo recording or screenshot",
        },
        {
            "title": "Capstone MVP — API hardening",
            "duration": "4 hrs",
            "concepts": ["Input validation", "Error handling", "Health endpoints"],
            "activities": [
                "Pydantic validation on all inputs",
                "Structured error responses; no raw LLM errors to client",
                "Add /health and /ready; logging with request IDs",
            ],
            "deliverable": "API passes manual test checklist",
        },
    ],
    "12.1-hardening": [
        {
            "title": "Capstone LLMOps — tracing and evaluation",
            "duration": "4 hrs",
            "concepts": ["Langfuse traces", "Ragas eval", "CI eval gate"],
            "activities": [
                "Instrument all LLM and retrieval calls",
                "Build 30+ case golden eval set",
                "GitHub Action fails on faithfulness regression",
            ],
            "deliverable": "Eval score in README; CI badge",
        },
        {
            "title": "Capstone security and cloud deploy",
            "duration": "5 hrs",
            "concepts": ["THREAT_MODEL.md", "Guardrails", "Cloud deployment"],
            "activities": [
                "Write threat model; red-team top 5 attacks",
                "Deploy to AWS/Azure/GCP/Railway",
                "Add rate limiting and auth stub",
            ],
            "deliverable": "Public URL + SECURITY.md",
        },
    ],
    "12.1-finish": [
        {
            "title": "Capstone UI polish and demo video",
            "duration": "4 hrs",
            "concepts": ["Portfolio presentation", "Demo video", "UX clarity"],
            "activities": [
                "Polish chat UI; show citations if RAG",
                "Record 2–3 min Loom demo",
                "Add GIF to README above fold",
            ],
            "deliverable": "Demo video link in README",
        },
        {
            "title": "Capstone documentation and presentation",
            "duration": "4 hrs",
            "concepts": ["Runbooks", "Executive summary", "Mock interview"],
            "activities": [
                "Complete README: metrics, setup, architecture, limitations",
                "Write one runbook for common failure",
                "10-min mock presentation to class/mentor",
            ],
            "deliverable": "Executive summary PDF + runbook + presentation slides",
        },
    ],
}


CAPSTONE = {
    "12.1-partial": ("Planning", "Choose project; architecture; metrics; repo; sprint backlog"),
    "12.1-build": ("Core Build", "MVP: core loop, LLM, RAG/agent, Docker local"),
    "12.1-hardening": ("Hardening", "Tracing, eval CI, security, cloud deploy"),
    "12.1-finish": ("Polish", "UI, demo video, README, runbook, presentation"),
}


def main():
    modules = {}
    for p in sorted(CURRICULUM_DIR.glob("module-*.md")):
        mod = parse_module(p)
        modules[mod["num"]] = mod

    lines = [
        "# Complete AI Engineer Curriculum",
        "### 52-Week Detailed Plan · Zero to Job-Ready",
        "",
        "> **Single source of truth** for teachers and students. Combines all content from `curriculum/module-01` through `module-12`.",
        "",
        "---",
        "",
        "## How to Read This Document",
        "",
        "Each **week** contains one or more **topics**. Each topic contains numbered **lessons**.",
        "",
        "Every lesson includes:",
        "- **Concepts taught** — exact skills and knowledge (not just a title)",
        "- **Step-by-step activities** — what to do hands-on",
        "- **Lesson deliverable** — proof you completed it",
        "",
        "Each topic also includes: lab, enterprise extension, tools, mistakes, interview prep, and deliverables from the full module curriculum.",
        "",
        "| Pace | Hours/week | Calendar |",
        "|------|------------|----------|",
        "| Standard | 12–15 | 52 weeks (~12 months) |",
        "| Intensive | 25–30 | 26 weeks (2 weeks per row) |",
        "| Part-time | 8–10 | ~78 weeks (1.5 weeks per row) |",
        "",
        "---",
        "",
        "## 52-Week Schedule",
        "",
        "| Week | Title | Module |",
        "|------|-------|--------|",
    ]
    for w, title, mod, _ in WEEK_PLAN:
        ml = "Foundation" if mod == "foundation" else f"Module {int(mod)}"
        lines.append(f"| {w} | {title} | {ml} |")

    lines += ["", "---", ""]

    for wnum, title, mod, keys in WEEK_PLAN:
        lines += [
            f"# Week {wnum}: {title}",
            "",
            f"**Hours:** 12–15 recommended | **Module:** {mod if mod != 'foundation' else 'Foundation (pre-requisite)'}",
            "",
            f"## Week {wnum} learning goals",
            f"Complete all lessons below. Submit week deliverable before starting Week {wnum + 1 if wnum < 52 else 52}.",
            "",
        ]
        for key in keys:
            if mod == "foundation":
                lines.append(render_foundation(key, wnum))
            elif key.startswith("12.1"):
                phase, desc = CAPSTONE.get(key, ("Capstone", ""))
                lines += [
                    f"### Topic 12.1: Industry Capstone — {phase} Phase",
                    "",
                    f"**Focus:** {desc}",
                    "",
                    "**Lessons this week:**",
                    "",
                ]
                for i, les in enumerate(CAPSTONE_LESSONS.get(key, []), 1):
                    lines.append(fmt_lesson(f"{wnum}.{i}", les))
                    lines.append("")
                lines += [
                    "**Reference:** module-12-capstone-job-readiness.md · 08-project-portfolio.md",
                    "",
                ]
            elif key == "12.2":
                t = modules["12"]["topics"]["12.2"]
                lines.append(render_topic("12.2", t, wnum, "12.2"))
            else:
                base = key.split("-")[0]
                t = modules[mod]["topics"][base]
                lines.append(render_topic(key, t, wnum, key))

        lines += [
            f"## Week {wnum} — submit checklist",
            "",
            "- [ ] All lesson deliverables pushed to GitHub",
            "- [ ] Lab completed and documented in README or /docs",
            "- [ ] Check-your-understanding questions answered in notes",
            "",
            f"**For teachers (Week {wnum}):** 10-min recap → live demo → lab time → 2 student demos or exit tickets.",
            "",
            "---",
            "",
        ]

    lines += [
        "## Appendix — Glossary",
        "",
        "| Term | Definition |",
        "|------|------------|",
        "| API | Interface for programs to communicate over a network |",
        "| LLM | Large Language Model (e.g. GPT-4, Claude) |",
        "| RAG | Retrieval-Augmented Generation |",
        "| Agent | AI system that plans and uses tools |",
        "| Terraform | Infrastructure as Code tool for cloud resources |",
        "| LLMOps | Operating LLM apps in production |",
        "",
        "*Source modules: `curriculum/module-*.md` · Regenerate: `python scripts/generate_curriculum.py`*",
    ]

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
