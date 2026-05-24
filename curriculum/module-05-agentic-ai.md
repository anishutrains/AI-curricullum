# Module 05 — Agentic AI Systems
### Zero-to-Hero Track · Weeks 21–25 · From Chatbots to AI That *Acts*

---

## Why This Module Exists

**Why learn this NOW?**  
Modules 01–04 taught you to **respond** with LLMs and **ground answers** with RAG. Module 05 teaches AI to **take actions**: search databases, create tickets, run code, approve workflows. **Agentic AI** is the fastest-emerging job category in US postings for 2026–2027 — but only **after** you can build reliable APIs, LLM calls, prompts, and RAG.

**Why companies care**
- **Salesforce, Microsoft, and HubSpot** embed agents that update CRM, send emails, and query docs.
- "AI employee" and "copilot" products are **agent architectures**, not single prompts.
- Engineers who skip to agents without RAG produce **autonomous hallucination machines** — fired, not hired.

**How this connects to the career path**
| Module 04 (RAG) | Module 05 (Agents) | Module 06+ |
|-----------------|-------------------|------------|
| `search_docs()` function | Agent **decides** when to call it | LLMOps traces every tool call |
| Static Q&A | Multi-step workflows | Enterprise HITL + audit |

**Prerequisites (mandatory)**
- Module 01: FastAPI, async Python, Docker
- Module 02: Tool calling API basics from OpenAI lesson
- Module 03: Prompt security, injection awareness
- Module 04: Working RAG pipeline you can wrap as a tool

**Future modules that depend on Module 05**
- **Module 06 (LLMOps):** Trace agent steps, eval tool success rate
- **Module 07 (Enterprise):** RBAC on tools, human-in-the-loop SLAs
- **Module 10 (Security):** Agent tool abuse, sandboxing

---

## What Students Will Become Capable Of

- Explain **agent vs chain vs workflow** to interviewers
- Build **tool-calling loops** with safe schemas and limits
- Orchestrate **LangGraph** workflows with checkpoints and human approval
- Run **multi-agent crews** when problem truly requires specialization
- Ship **Autonomous Research Agent** or **AI Customer Support** portfolio projects
- Apply **safety boundaries** before giving agents production access

---

## Job Roles This Module Supports

| Role | Agent skills needed |
|------|---------------------|
| **Agentic AI Engineer** | Core focus |
| **AI Copilot Engineer** | Tool use + embedded context |
| **AI Automation Engineer** | Workflow agents |
| **AI Workflow Engineer** | LangGraph, state machines |
| **Generative AI Engineer** | Agents + RAG combined |
| **AI Solutions Engineer** | Demo multi-step automations |
| **Enterprise AI Engineer** | HITL, audit, Microsoft Semantic Kernel |

**Recruiter signal:** GitHub agent project with **tool audit log + max-step limits + demo video** proves maturity beyond LangChain tutorial.

**Salary impact:** Agentic AI roles cluster $160K–$230K US base (2026) — premium over basic prompt-only developers.

---

## Skill Progression in This Module

| Level | Capability |
|-------|------------|
| **Beginner** | Understand what an agent is; one tool, one loop |
| **Intermediate** | Multi-tool agent with error handling |
| **Advanced** | LangGraph stateful graphs, checkpoints |
| **Production** | HITL, timeouts, token budgets, tracing |
| **Enterprise** | Multi-agent, RBAC tools, Semantic Kernel / Azure |

---

# Topic 5.1 — Agent Foundations: From LLM Responses to Actions

## Beginner Explanation

**Chatbot:** User asks → LLM answers (one shot).  
**Agent:** User asks → LLM **thinks** → LLM **chooses a tool** → your code **runs tool** → LLM **continues** until done.

**Analogy:** Chatbot is a librarian who only talks. Agent is a librarian who can **look up the catalog, print a form, and email you** — but needs rules so they don't email the whole city.

## Why Companies Use This

- Update CRM after sales call
- Triage support ticket → search KB (your RAG!) → draft reply → human approve
- Schedule meetings, run SQL reports (with guardrails)

## Learning Outcome

You will implement a safe tool-calling loop with max iterations, error handling, and audit logging.

---

### Lesson 5.1.1 — Concept: Chain vs Agent vs Workflow

| Pattern | Who decides next step | Example |
|---------|----------------------|---------|
| **Chain** | Developer (fixed code) | Always: retrieve → generate |
| **Agent** | LLM chooses tools | Maybe search, maybe calculator |
| **Workflow** | Developer graph + LLM nodes | Classify → RAG OR calculator path |

**Rule:** Start with **chain** when possible. Add **agent** when paths vary by user input.

**Exercise:** Classify 5 tasks as chain or agent: "Summarize PDF" vs "Book cheapest flight to NYC"

---

### Lesson 5.1.2 — Concept: What Is Tool Calling (Function Calling)?

**1. You register tools** with name, description, JSON schema parameters  
**2. LLM returns** `tool_calls` instead of final answer  
**3. You execute** tool in Python  
**4. You send** result back to LLM  
**5. Repeat** until LLM gives final text answer  

**Connect Module 02 Lesson 2.1.9** — revisit OpenAI tools lesson before coding

---

### Lesson 5.1.3 — Beginner Coding: Mock Tool (Calculator)

**Simplest tool — no external API**

```python
tools = [{
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Evaluate math expressions",
        "parameters": {
            "type": "object",
            "properties": {"expression": {"type": "string"}},
            "required": ["expression"]
        }
    }
}]

def run_calculator(expression: str) -> str:
  # safe eval or ast.literal_eval pattern — never raw eval(user_input)
    return str(safe_calculate(expression))
```

**Exercise:** Ask "What is 47 * 89?" — model must call calculator

**Security:** Never `eval()` user strings directly

---

### Lesson 5.1.4 — Beginner Coding: RAG as a Tool (Connect Module 04)

```python
def search_knowledge_base(query: str) -> str:
    """Search company docs and return top 3 chunks as text."""
    chunks = rag_pipeline.search(query, top_k=3)
    return "\n\n".join(c.text for c in chunks)
```

**This is the most important integration in the course** — Module 04 + Module 05 together = employable copilot.

**Mini project:** Agent with tools: `search_knowledge_base`, `get_current_time` (mock)

---

### Lesson 5.1.4b — Practical: Complete Tool-Calling Loop (End-to-End)

**This is the core pattern every agent framework wraps.** Build it once in plain Python before LangGraph.

```python
from openai import OpenAI

client = OpenAI()
MAX_ITERATIONS = 5

def run_agent(user_message: str) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Use tools when needed."},
        {"role": "user", "content": user_message},
    ]
    for _ in range(MAX_ITERATIONS):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=TOOLS,
        )
        msg = response.choices[0].message
        if not msg.tool_calls:
            return msg.content or ""
        messages.append(msg)
        for call in msg.tool_calls:
            result = execute_tool(call.function.name, call.function.arguments)
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result,
            })
    return "Agent stopped: max iterations reached."
```

**Real-world use case:** Internal HR copilot — user asks about PTO → agent calls `search_knowledge_base` → cites policy section.

**Production considerations:** Log every iteration; return partial answer if max iterations hit; never expose raw tool errors to user.

**Exercise:** Add `create_support_ticket` mock tool; verify agent chooses RAG vs ticket based on question type.

---

### Lesson 5.1.5 — Intermediate: The ReAct Pattern (Reason + Act)

**Concept:** LLM alternates **Thought → Action → Observation**  
**Benefit:** Easier to debug than black-box tool loops  
**Prompt style:** "Think step by step. Then choose a tool if needed."

**Exercise:** Log each thought/action/observation to `agent_trace.jsonl`

---

### Lesson 5.1.6 — Intermediate: Tool Schema Design Best Practices

**Good tool description:** "Search internal HR policy documents. Use when user asks about PTO, benefits, or leave."  
**Bad:** "Search docs"

**Parameters:** Minimal, typed, validated with Pydantic before execution

**Enterprise:** Tool catalog document shared with security team

---

### Lesson 5.1.7 — Intermediate: Parallel vs Sequential Tool Calls

**Sequential:** Search docs → then create ticket (order matters)  
**Parallel:** Fetch weather AND stock price (independent)  

**OpenAI API:** May return multiple tool calls in one turn

---

### Lesson 5.1.8 — Production: Idempotent Tools and Side Effects

**Idempotent** — Running twice = same result (safe retry)  
**Side effects** — send_email, charge_card — require **human confirmation**

**Rule:** Read-only tools auto-run; write tools need HITL (Topic 5.2)

---

### Lesson 5.1.9 — Production: Agent Loop Limits and Budgets

```python
MAX_ITERATIONS = 5
MAX_TOOL_CALLS = 10
MAX_TOKENS_PER_RUN = 8000
```

**Why:** Prevent runaway loops and bill explosions

**Audit log:** Every tool call → `{timestamp, tool, args_hash, user_id, result_status}`

---

### Lesson 5.1.10 — Concept: MCP (Model Context Protocol) Intro

**What:** Standard way to expose tools to multiple LLM clients (like USB for tools)  
**When:** Integrating with Cursor, Claude Desktop, enterprise tool registries  
**Depth:** Awareness now; implement in advanced track

---

### Topic 5.1 — Assessments

**Beginner:** Calculator agent  
**Intermediate:** RAG + ticket mock agent  
**Assignment:** 10-task eval suite; ≥90% tool success  
**Interview:** "What happens when tool call fails mid-agent?"  
**Common errors:** Unbounded loops; SQL tool with raw user input; no audit log  

---

# Topic 5.2 — LangGraph: Stateful Agent Workflows

## Beginner Explanation

Simple tool loops are **flat**. Real business processes have **branches and approvals**: "If billing issue → route A; if technical → route B; if high severity → ask human."

**LangGraph** models this as a **graph**: nodes (steps) and edges (transitions). State persists between steps.

**Analogy:** Flowchart on the wall — agent follows the boxes, not random walks.

## Why Companies Use This

LangGraph appears in **most senior Agentic AI JDs** (2026). Support triage, approval workflows, and research pipelines use graphs with **checkpoints** (resume after crash).

## Learning Outcome

Build a support triage graph: classify → retrieve → draft → **human approve** → send.

---

### Lesson 5.2.1 — Concept: Why Flat Loops Fail in Enterprise

**Problems:** No persistence, no human pause, hard to visualize, can't resume  
**LangGraph fixes:** State object, checkpointing, conditional edges, HITL interrupts

---

### Lesson 5.2.2 — Concept: Graphs — Nodes, Edges, State

**State** — Shared dict: `{messages, ticket_type, draft_reply, approved}`  
**Node** — Function that updates state  
**Edge** — Fixed or conditional next node  
**Conditional edge** — `if severity == "high": human_review else send`

**Exercise:** Draw support triage flowchart on paper before coding

---

### Lesson 5.2.3 — Beginner: Install LangGraph and Hello Graph

```python
from langgraph.graph import StateGraph, END

# Define state TypedDict
# Add nodes: classify, respond
# Set entry point; add edges; compile()
```

**Deliverable:** 2-node graph running end-to-end

---

### Lesson 5.2.4 — Intermediate: Conditional Routing Node

**Node `classify_ticket`** → returns `billing | technical | unknown`  
**Router** sends to specialized sub-graphs  

**Connect Module 03:** Classification prompt quality determines routing accuracy

---

### Lesson 5.2.5 — Intermediate: Integrate RAG Node in Graph

**Node `retrieve_context`** calls Module 04 pipeline  
**Node `draft_reply`** LLM with retrieved chunks  
**Node `cite_sources`** formats citations  

---

### Lesson 5.2.6 — Advanced: Human-in-the-Loop (HITL) Interrupt

**Concept:** Graph pauses before `send_email` node  
**Human** approves/edits in UI or CLI  
**Graph resumes** from checkpoint  

**Enterprise:** SLA — human must respond within 4 hours or escalate

---

### Lesson 5.2.7 — Advanced: Checkpointing with Postgres

**Why:** Server restart mid-workflow must not lose state  
**LangGraph checkpointer** saves state after each node  

**Exercise:** Kill process mid-run; resume; verify continuation

---

### Lesson 5.2.8 — Production: Streaming Graph Events to UI

**Stream events:** `node_started`, `node_completed`, `waiting_for_human`  
**Frontend:** Show "Drafting reply..." progress (Module 09)

---

### Lesson 5.2.9 — Production: Avoid the God-Graph

**Anti-pattern:** 20 nodes in one file  
**Fix:** Subgraphs — `billing_subgraph`, `technical_subgraph`  
**Version graphs in Git** like code

---

### Topic 5.2 — Mini Project
**Support Triage Graph:** classify → RAG → draft → HITL approve → log sent (mock send)

**Portfolio:** GIF of checkpoint resume in README

---

# Topic 5.3 — Multi-Agent Systems (When One Agent Is Not Enough)

## Beginner Explanation

**Multi-agent** = several LLM "roles" collaborate: Researcher finds data, Analyst interprets, Writer formats report, Critic checks quality.

**Warning for beginners:** Multi-agent costs **3–5× tokens** and adds complexity. Use only when **eval proves** single agent fails.

## Why Companies Use This

Investment research, marketing campaign generation, code review teams — specialist roles map to specialist agents.

## Learning Outcome

Build a 3-agent crew; measure cost vs quality vs single agent; know when to simplify back to one.

---

### Lesson 5.3.1 — Concept: Single Agent vs Multi-Agent Decision

| Use single agent | Use multi-agent |
|------------------|-----------------|
| Clear linear task | Distinct expert roles |
| Latency sensitive | Quality > cost |
| Small scope | Research + write + review |

**Interview:** "When would you use multi-agent vs single LangGraph?"

---

### Lesson 5.3.2 — Beginner: CrewAI — Roles, Goals, Tasks

**Concepts**
- **Agent:** role + goal + backstory
- **Task:** assignment with expected output
- **Crew:** orchestrates execution order

**Exercise:** Researcher + Writer crew on public company 10-K summary (public data)

---

### Lesson 5.3.3 — Intermediate: Hierarchical Process (Manager Agent)

**Manager** delegates to workers; workers report back  
**Risk:** Token explosion — set `max_rpm`, max iterations

---

### Lesson 5.3.4 — Intermediate: AutoGen Group Chat Pattern

**Agents** message each other in group chat until termination condition  
**Termination:** "TERMINATE" keyword or max rounds  

**Exercise:** Critic agent must approve before Writer finishes

---

### Lesson 5.3.5 — Advanced: Debate / Critic Patterns

**Pro/con agents** debate decision → judge synthesizes  
**Use case:** High-stakes analysis where blind spots costly

---

### Lesson 5.3.6 — Production: Cost Control in Multi-Agent

**Log tokens per agent role**  
**Compare:** 1 LangGraph vs 3-agent crew on same task — document in README  
**Cap:** $0.50 max spend per user request in demo

---

### Topic 5.3 — Assignment
**Multi-Agent Finance Analyst** (public data): Researcher → Analyst → Report + exported message log

---

# Topic 5.4 — Browser Agents, Code Agents & AI Employees (Advanced / High Risk)

## Beginner Explanation

Some agents **use computers**: click websites (browser agent), edit code (coding agent), send emails (AI employee). **Highest value, highest risk** — learn only after Topics 5.1–5.3 solid.

## Why Companies Use This

QA automation, L1 IT support, CI failure triage, DevOps assistants — **always with sandbox and human gates**.

## Learning Outcome

Understand architectures; build **sandboxed code agent** demo; never put production credentials in agent env.

---

### Lesson 5.4.1 — Concept: Browser Agents (Playwright + Vision)

**Loop:** Screenshot → LLM decides click/type → Playwright executes → repeat  
**Risks:** Wrong click, data exfiltration, credential theft  

**Rule:** Allowlist domains; no banking sites in learning lab

---

### Lesson 5.4.2 — Concept: Code Agents and Sandboxes

**Agent reads repo** → proposes patch → runs tests in **Docker/E2B sandbox**  
**Human** reviews PR before merge  

**Never:** Give agent unrestricted shell on laptop with prod keys

---

### Lesson 5.4.3 — Beginner Coding: Sandboxed Code Agent Lab

**Setup:** Clone tiny repo with one failing test  
**Agent tools:** `read_file`, `write_patch`, `run_tests` (sandbox only)  
**Success:** Test passes; human approves diff  

**Deliverable:** `SECURITY.md` section on sandbox boundaries

---

### Lesson 5.4.4 — Concept: AI Employee Workflows (Email, CRM, Calendar)

**Architecture:** Scheduler triggers agent → reads inbox → classifies → drafts → HITL send  
**Legal/ethical:** Consent, recording laws, employment boundaries  

---

### Lesson 5.4.5 — Production: Kill Switch, Spend Cap, Watchdog

**Kill switch:** API endpoint `/admin/agents/stop-all`  
**Spend cap:** Daily token budget per tenant  
**Watchdog:** Alert if agent loops > N times

---

### Topic 5.4 — Enterprise Scenario
**AI DevOps Assistant (read-only):** Ingest log snippet → RAG on runbooks → suggest fix — **no auto-apply**

---

# Topic 5.5 — Enterprise Agents: Semantic Kernel & Microsoft Stack

## Beginner Explanation

Many Fortune 500 companies standardize on **Microsoft**: Azure OpenAI, M365, SharePoint, Teams. **Semantic Kernel (SK)** is Microsoft's agent framework — alternative mental model to LangGraph.

## Why Companies Use This

Consulting roles (Deloitte, Accenture) on Azure deals expect SK + Graph API awareness.

## Learning Outcome

Map SK concepts to LangGraph; build plugin calling mock SharePoint search; document when SK vs LangGraph for interviews.

---

### Lesson 5.5.1 — Concept: SK Plugins and Kernel

**Plugin** = functions exposed to LLM (like tools)  
**Kernel** = orchestration host  

**Exercise:** Same RAG tool as SK plugin vs LangChain tool — compare code structure

---

### Lesson 5.5.2 — Concept: Planners vs Explicit Graphs

**SK Planner** — LLM generates plan dynamically (less control)  
**LangGraph** — Developer defines graph explicitly (more control)  
**Production trend:** Explicit graphs for compliance-heavy workflows

---

### Lesson 5.5.3 — Intermediate: Azure OpenAI + Entra ID for Enterprise Tools

**Managed identity** instead of API keys in config  
**Graph API** for SharePoint/Outlook integration (mock in lab)

---

### Lesson 5.5.4 — Production: Copilot Extensibility Patterns (Awareness)

**Microsoft 365 Copilot** extensibility for ISVs — know term for interviews  
**Deep implementation:** Module 08 Azure + Module 07 enterprise

---

### Topic 5.5 — Deliverable
Architecture doc: "Same support agent in LangGraph vs Semantic Kernel" — 1 page comparison

---

# Module 05 — Capstone Projects (Choose One)

## Project Progression (Ascending Complexity)

| Phase | What you build |
|-------|----------------|
| **Week 21** | Calculator + one-tool agent loop |
| **Week 22** | RAG-as-tool agent with audit log |
| **Week 23** | LangGraph support triage with HITL |
| **Week 24** | Multi-agent OR browser/code agent (sandboxed) |
| **Week 25** | Capstone polish + eval suite + demo video |

## Architecture Reference (Support Agent)

```
User Request
     │
     ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Classify   │────▶│  RAG Retrieve │────▶│ Draft Reply │
│   Node      │     │  (Module 04)  │     │    Node     │
└─────────────┘     └──────────────┘     └──────┬──────┘
                                                 │
                    ┌──────────────┐             ▼
                    │ Human Approve│◀──── HITL Interrupt
                    │   (HITL)     │
                    └──────┬───────┘
                           ▼
                    ┌──────────────┐
                    │ Send / Log   │
                    │  (mock)      │
                    └──────────────┘
```

## Project A: Autonomous Research Agent
- Tools: web search (mock or Tavily), note storage, final report writer
- LangGraph with max 8 steps
- Checkpoint + trace log
- **Portfolio:** PDF report + `traces.jsonl`

## Project B: AI Customer Support Agent
- Tools: RAG (Module 04), create_ticket (mock), escalate_human
- LangGraph HITL before send
- **Portfolio:** Demo video showing approval step

## Project C: Multi-Agent Analyst (Advanced)
- CrewAI 3 roles
- Cost comparison doc vs single agent

## Required for All Capstones

- [ ] Max iteration + token budget enforced
- [ ] Tool audit log (who called what, when)
- [ ] RAG integrated as at least one tool
- [ ] Security section: injection test on agent input
- [ ] README architecture diagram
- [ ] ≥90% success on 10-task eval suite

## Interview Talking Points

1. "Agent vs chain?" — Developer decides path vs LLM chooses tools  
2. "How prevent runaway loops?" — max iterations, token budget, watchdog  
3. "When multi-agent?" — Only when eval proves single agent fails; cite cost data  
4. "How secure write tools?" — HITL, RBAC, audit log, idempotency  
5. Whiteboard LangGraph: classify → RAG → draft → approve → send  

## Common Mistakes (Hiring Feedback)

| Mistake | Why it fails interviews |
|---------|-------------------------|
| Agent with no max steps | Shows no production awareness |
| SQL tool with raw user input | Security red flag |
| Multi-agent for simple Q&A | Over-engineering; cost waste |
| No RAG integration | "Agent" that hallucinates freely |
| No trace/audit log | Cannot debug or comply in enterprise |

---

## Module 05 — Master Checklist Before Module 06 (LLMOps)

| Question | Yes / No |
|----------|----------|
| Can I explain agent vs chain in an interview? | |
| Does my agent use Module 04 RAG as a tool? | |
| Are write-tools blocked without human approval? | |
| Is there a max-step limit and audit log? | |
| Did I measure cost of multi-agent vs single? | |

**Next module:** Module 06 teaches you to **observe, evaluate, and deploy** these agents reliably in production — tracing, Ragas, CI gates.

---

*Next: [module-06-llmops.md](./module-06-llmops.md)*
