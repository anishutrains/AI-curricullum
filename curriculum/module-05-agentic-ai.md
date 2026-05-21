# Module 05 — Agentic AI

---

## Topic 5.1: Agent Fundamentals & Tool Calling

### 1. Topic Name
AI Agents, Tool Calling & Function Execution

### 2. Why This Topic Matters
Agentic AI is the fastest-emerging JD category 2026–27. Tool calling is required for copilots, automation, and "AI employees."

### 3. Job Roles
Agentic AI Engineer, AI Copilot Engineer, AI Automation Engineer, Generative AI Engineer

### 4. Learning Objectives
- Implement OpenAI/Anthropic tool calling loops
- Design safe tool schemas with validation
- Handle tool errors and timeouts

### 5. Lessons/Subtopics
- Agent vs chain vs workflow
- Tool schema design (JSON Schema)
- ReAct pattern
- Parallel vs sequential tool calls
- Idempotent tools
- MCP (Model Context Protocol) intro

### 6. Hands-on Labs
**Lab 5.1:** Agent with tools: `search_kb`, `create_ticket`, `get_weather` (mock)—max 5 steps.

### 7. Enterprise Projects
Tool registry with RBAC: role A cannot call `delete_record`.

### 8. Portfolio Projects
Tool catalog documented in OpenAPI-style spec.

### 9. Interview Preparation
- "Design agent tools for a sales copilot."
- "What happens when a tool call fails mid-agent?"

### 10. Real-world Use Cases
CRM updates, calendar scheduling, internal API actions.

### 11. Tools & Technologies
LangChain tools, OpenAI function calling, MCP servers

### 12. Common Mistakes
- Tools with side effects and no confirmation
- Unbounded agent loops
- Passing raw user input to SQL/shell tools

### 13. Industry Best Practices
- Max iteration limits and step budgets
- Confirm destructive actions (HITL)
- Audit log every tool invocation

### 14. Capstone Deliverables
Agent completing 10-task eval suite with tool success rate ≥90%.

---

## Topic 5.2: LangGraph — Stateful Agent Orchestration

### 1. Topic Name
LangGraph for Production Agent Workflows

### 2. Why This Topic Matters
LangGraph is the de facto standard in US JDs for stateful agents—graphs, checkpoints, human-in-the-loop.

### 3. Job Roles
Agentic AI Engineer, AI Workflow Engineer, LLM Engineer

### 4. Learning Objectives
- Build StateGraph with nodes and conditional edges
- Persist state with checkpointers (Postgres/Redis)
- Implement human-in-the-loop interrupts

### 5. Lessons/Subtopics
- Graph nodes: planner, executor, critic
- Conditional routing
- Memory: short-term vs long-term
- Checkpointing and resume
- Subgraphs and multi-agent handoff
- Streaming graph events to UI

### 6. Hands-on Labs
**Lab 5.2:** Support triage graph: classify → retrieve → draft → human approve → send.

### 7. Enterprise Projects
Tenant-isolated thread store; SLA timers on HITL steps.

### 8. Portfolio Projects
**Autonomous Research Agent** or **AI Customer Support** with LangGraph.

### 9. Interview Preparation
- Draw LangGraph for research agent with 4 nodes
- "How do you resume a failed multi-hour agent run?"

### 10. Real-world Use Cases
Approval workflows, incident response agents, research pipelines.

### 11. Tools & Technologies
LangGraph, LangChain, Postgres checkpointer, Redis

### 12. Common Mistakes
- God-graph with 20 nodes (unmaintainable)
- No persistence (lost on restart)
- Missing timeout on HITL waits

### 13. Industry Best Practices
- Small composable subgraphs
- Visualize graph for stakeholders
- Version graph definitions in Git

### 14. Capstone Deliverables
LangGraph agent with checkpoint resume demo video/GIF in README.

---

## Topic 5.3: Multi-Agent Systems (CrewAI, AutoGen)

### 1. Topic Name
Multi-Agent Systems — CrewAI & AutoGen

### 2. Why This Topic Matters
Enterprises deploy specialist agent teams (analyst + writer + critic). CrewAI and AutoGen appear frequently in senior agentic roles.

### 3. Job Roles
Agentic AI Engineer, Applied AI Engineer, AI Consultant

### 4. Learning Objectives
- Model roles, goals, and delegation in CrewAI
- Run AutoGen group chats with termination conditions
- Compare frameworks for project fit

### 5. Lessons/Subtopics
- CrewAI: crews, tasks, hierarchical process
- AutoGen: conversable agents, GroupChat
- Debate / critic patterns
- Cost control in multi-agent (N× tokens)
- When single agent beats multi-agent

### 6. Hands-on Labs
**Lab 5.3:** 3-agent crew: Researcher → Analyst → Report Writer on earnings data.

### 7. Enterprise Projects
**Multi-Agent Finance Analyst** with audit trail of agent messages.

### 8. Portfolio Projects
Cost comparison: 1 agent vs 3 agents on same task.

### 9. Interview Preparation
- "When would you use multi-agent vs single LangGraph?"
- "How do you prevent agent infinite debate loops?"

### 10. Real-world Use Cases
Investment research, marketing campaign generation, code review teams.

### 11. Tools & Technologies
CrewAI, AutoGen, LangGraph (multi-agent mode)

### 12. Common Mistakes
- Multi-agent for tasks solvable by one pass
- No shared memory contract between agents
- Exploding token costs

### 13. Industry Best Practices
- Cap rounds and token budget per crew
- Shared blackboard state object
- Human review before external actions

### 14. Capstone Deliverables
Multi-agent project with message log export and final report artifact.

---

## Topic 5.4: Browser Agents, Code Agents & AI Employees

### 1. Topic Name
Browser Agents, Code Agents & AI Employees

### 2. Why This Topic Matters
2026–27 trend: agents that operate UIs and codebases (computer use, Devin-class patterns)—high value, high risk.

### 3. Job Roles
Agentic AI Engineer, AI Copilot Engineer, AI Automation Engineer

### 4. Learning Objectives
- Understand browser automation agent architectures
- Build code agent with sandboxed execution
- Apply safety boundaries for autonomous workers

### 5. Lessons/Subtopics
- Playwright + LLM vision/action loops
- Anthropic computer use patterns
- Code interpreter sandboxes (Docker, E2B)
- AI employee workflow (email, CRM, calendar)
- Scheduling and watchdog processes
- Legal/ethical boundaries

### 6. Hands-on Labs
**Lab 5.4:** Code agent: fix failing unit test in sandbox repo (read-only git except patch branch).

### 7. Enterprise Projects
**AI DevOps Assistant** — read logs, suggest fixes, open PR (HITL merge).

### 8. Portfolio Projects
Sandbox-only browser agent demo (no production credentials).

### 9. Interview Preparation
- "How do you sandbox an autonomous code agent?"
- "Risks of browser agents in enterprise?"

### 10. Real-world Use Cases
QA automation, L1 support, routine data entry, CI triage.

### 11. Tools & Technologies
Playwright, E2B, Docker sandboxes, Semantic Kernel plugins

### 12. Common Mistakes
- Production credentials in agent environment
- No kill switch or spend cap
- Full internet access from code agent

### 13. Industry Best Practices
- Ephemeral VMs per task
- Allowlist domains for browser agents
- Mandatory HITL for external communications

### 14. Capstone Deliverables
Sandboxed code or browser agent with security section in README.

---

## Topic 5.5: Semantic Kernel & Enterprise Agent Patterns

### 1. Topic Name
Semantic Kernel & Microsoft Enterprise Agent Patterns

### 2. Why This Topic Matters
Fortune 500 Microsoft shops standardize on Semantic Kernel + Azure—consulting and enterprise roles expect awareness.

### 3. Job Roles
Enterprise AI Engineer, AI Solutions Engineer, AI Integration Engineer

### 4. Learning Objectives
- Build SK plugins and planners
- Integrate with Azure OpenAI and Microsoft Graph
- Map SK concepts to LangGraph mental model

### 5. Lessons/Subtopics
- SK plugins and kernel
- Planners vs explicit graphs
- Azure OpenAI integration
- Copilot extensibility patterns
- Entra ID auth for enterprise tools

### 6. Hands-on Labs
**Lab 5.5:** SK plugin calling SharePoint mock API for document retrieval.

### 7. Enterprise Projects
Microsoft-stack copilot POC for intranet search.

### 8. Portfolio Projects
Side-by-side: same agent in LangGraph and SK (architecture doc).

### 9. Interview Preparation
- "Experience with Semantic Kernel vs LangChain?"
- "Integrate copilot with SharePoint and Teams."

### 10. Real-world Use Cases
M365 copilots, internal IT helpdesk, field service apps.

### 11. Tools & Technologies
Semantic Kernel (.NET/Python), Azure OpenAI, Microsoft Graph API

### 12. Common Mistakes
- Ignoring Azure-specific auth flows
- Assuming SK planner is production-ready without tests

### 13. Industry Best Practices
- Follow Microsoft reference architectures
- Use managed identity in Azure
- Align with customer's existing M365 security

### 14. Capstone Deliverables
SK-based demo OR documented enterprise Microsoft path in portfolio.

---

*Next: [module-06-llmops.md](./module-06-llmops.md)*
