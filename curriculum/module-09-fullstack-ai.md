# Module 09 — Full Stack AI Applications
### Zero-to-Hero Track · Weeks 39–42 · Building Complete AI Products Users Actually Touch

---

## Why This Module Matters

**Why learn this NOW?**  
Backend AI (Modules 01–08) powers the brain. **Full stack** gives it a face — chat UI, streaming, auth, billing, embeddable copilots. **AI Application Developer** is one of the most hired roles for product-facing AI (2026–2027).

**Why companies need this**
- Users don't curl APIs — they use **Next.js chatUpload, streaming chat**.
- Product teams hire engineers who ship **end-to-end**: FastAPI + React + deploy.
- SaaS AI startups need **auth, quotas, Stripe** — not just prompts.

**Salary impact:** Full Stack AI Engineer **$145K–$210K** US. Founders with shipping ability unlock consulting + startup paths.

---

## How This Module Fits into the AI Engineering Journey

| Modules 01–08 | Module 09 | Modules 10–12 |
|---------------|-----------|---------------|
| API + cloud backend | **User-facing product** | Security hardening |
| RAG/agent logic | **Streaming UX + citations UI** | Production scale |
| Enterprise tenancy | **SaaS auth + billing** | Capstone polish |

**Prerequisites:** Module 01 (FastAPI), Module 04 (RAG API), Module 06 (streaming awareness). Basic HTML/CSS helpful; React taught from beginner level.

---

## Job Roles This Module Prepares Students For

AI Application Developer · AI Copilot Engineer · AI Product Engineer · Full Stack AI Engineer · Conversational AI Engineer · AI Workflow Engineer · Startup founder / indie hacker

---

## Beginner Skills Students Will Learn

- HTML/React/Next.js fundamentals for chat UI
- Consume FastAPI SSE/stream from frontend
- Display loading states and errors in chat
- Render markdown + code blocks safely
- Show RAG citation chips in UI

## Intermediate Skills Students Will Learn

- Vercel AI SDK `useChat` pattern
- Next.js App Router + server actions
- Auth integration (Clerk/NextAuth mock)
- Token quota enforcement per user

## Advanced Skills Students Will Learn

- Multimodal input (image upload + vision API)
- Voice pipeline: STT → LLM → TTS
- Embeddable copilot widget (iframe/SDK)

## Production Enterprise Skills Students Will Learn

- SSO stub + WCAG accessibility basics
- Stripe usage-based billing intro
- Workflow builder UI (React Flow)
- n8n / Trigger.dev integration patterns

---

# Topic 9.1 — Next.js AI Frontends & Streaming UX

## Beginner-Friendly Explanation

**Frontend** = what users see and click. **Streaming** = AI response appears word-by-word (like ChatGPT), not all at once after 10 seconds.

**Why streaming matters:** Users perceive faster apps; they can stop bad generations early.

**Analogy:** Streaming is like watching a download progress bar vs staring at a frozen screen.

## Why This Topic Matters in Real Companies

Every copilot product has a chat UI. **Vercel AI SDK** patterns are industry standard for Next.js teams.

## Problems This Topic Solves

- Blank screen for 8 seconds → user leaves
- API keys exposed in browser JavaScript
- No way to cancel long generation

## Learning Outcome

Production-quality Next.js chat app wired to Module 04 FastAPI RAG backend with streaming + citation UI.

---

### Lesson 9.1.1 — Concept: How Web Apps Talk to AI Backends

```
Browser (Next.js)  --HTTP/SSE-->  FastAPI (Python)  -->  OpenAI/RAG
```

**REST** = request/response JSON  
**SSE (Server-Sent Events)** = server pushes tokens one-way to browser  
**WebSockets** = two-way real-time (voice, collaborative editing)

**Beginner:** Start with SSE for chat streaming — simpler than WebSockets.

---

### Lesson 9.1.2 — Beginner: React and Next.js Essentials for AI Devs

**You need (minimal):**
- Components (`function ChatMessage() { ... }`)
- State (`useState` for messages)
- Effects (`useEffect` for fetch on mount)
- Next.js App Router: `app/page.tsx`, `app/api/chat/route.ts`

**Guided lab:** Static chat UI with hardcoded messages — no AI yet.

---

### Lesson 9.1.3 — Beginner Coding: Fetch Non-Streaming Chat

```typescript
const res = await fetch("/api/chat", {
  method: "POST",
  body: JSON.stringify({ message: input }),
});
const data = await res.json();
setMessages((prev) => [...prev, { role: "assistant", content: data.answer }]);
```

**Exercise:** Wire to your FastAPI `POST /v1/rag/query` — display answer + sources.

---

### Lesson 9.1.4 — Intermediate: Server-Sent Events Streaming

**FastAPI side (recap Module 02):** `StreamingResponse` with token chunks  
**Next.js API route:** Proxy stream to client  
**Client:** `ReadableStream` reader OR Vercel AI SDK

```typescript
import { useChat } from "ai/react";

const { messages, input, handleSubmit, isLoading, stop } = useChat({
  api: "/api/chat",
});
```

**Guided lab:** Token-by-token display; Stop button calls abort.

---

### Lesson 9.1.5 — Intermediate: Citation UI for RAG

**Design pattern:**
```
Assistant message text here...

Sources: [HR Handbook p.12] [Benefits Guide §4.2]
```

**Click source** → expand chunk preview or link to doc  
**Connect Module 04:** API returns `sources[]` — frontend renders chips

**Mini project:** Citation popover with snippet text.

---

### Lesson 9.1.6 — Production: Error States, Retries, and Loading UX

**Handle:** Network error, 429 rate limit, 500 server error, empty response  
**UX:** Skeleton loader, retry button, "Something went wrong" with support link  
**Never:** Expose stack traces to user

---

### Lesson 9.1.7 — Production: Security — API Keys Server-Side Only

**Rule:** OpenAI key lives in FastAPI or Next.js **server** route — NEVER `NEXT_PUBLIC_OPENAI_KEY`

**Pattern:** Browser → your API route → backend with secret

**Common beginner mistake:** Key in frontend env — instant security fail in interview.

---

### Lesson 9.1.8 — Enterprise: SSO Stub and Accessibility

**SSO:** Clerk/NextAuth with "Sign in with Microsoft" button (mock OK for portfolio)  
**WCAG basics:** Keyboard navigation, contrast, screen reader labels on chat input

---

# Topic 9.2 — Multimodal & Voice AI Applications

## Beginner-Friendly Explanation

**Multimodal** = AI understands **text + images** (and more).  
**Voice AI** = speak question → transcribe → LLM → speak answer.

## Learning Outcome

Build voice note → transcript → RAG answer OR image upload → vision Q&A demo.

---

### Lesson 9.2.1 — Concept: Vision API Document Q&A

**Flow:** User uploads invoice photo → GPT-4o/Gemini vision → "What is the total?"  
**Connect RAG:** Image + text hybrid search (advanced)

**Guided lab:** Upload PNG → vision API → structured JSON extract.

---

### Lesson 9.2.2 — Beginner: Whisper Speech-to-Text

```python
from openai import OpenAI
client = OpenAI()
with open("voice.webm", "rb") as f:
    transcript = client.audio.transcriptions.create(model="whisper-1", file=f)
```

**Frontend:** MediaRecorder API capture audio blob → upload to API.

---

### Lesson 9.2.3 — Intermediate: Voice Pipeline STT → LLM → TTS

**Latency budget:** Target < 3s for conversational feel  
**TTS:** OpenAI TTS or ElevenLabs  
**Stream:** Partial transcript display while user still speaking (advanced)

**Guided lab:** Voice question → RAG answer → audio playback.

---

### Lesson 9.2.4 — Production: Consent, Privacy, and Fallback

**Consent banner** before recording (GDPR, two-party consent states)  
**Fallback:** Text chat if mic denied  
**Don't store** voice recordings without policy in COMPLIANCE.md

---

# Topic 9.3 — AI SaaS Products (Auth, Billing, Copilot Patterns)

## Beginner-Friendly Explanation

**SaaS** = Software as a Service — users pay monthly, multi-tenant, you host it.  
**AI SaaS** adds: token metering, plan tiers, embeddable widget for customer sites.

## Learning Outcome

SaaS MVP: login + free/pro token quota + landing page + working product loop.

---

### Lesson 9.3.1 — Concept: SaaS Architecture for AI

```
Landing (marketing) → Auth → App (chat) → API → LLM
                              ↓
                         Usage DB (tokens per user)
```

**API-first:** Same backend serves web app + embeddable widget + mobile later.

---

### Lesson 9.3.2 — Beginner: Auth with Clerk or NextAuth

**Clerk** — fastest for beginners (hosted auth UI)  
**Flow:** Sign up → JWT/session → pass user_id to FastAPI for quota + tenant

**Guided lab:** Protected `/chat` route — redirect if not logged in.

---

### Lesson 9.3.3 — Intermediate: Token Quotas per Plan

```python
async def enforce_quota(user_id: str, tokens_used: int):
    plan = await get_user_plan(user_id)
    if await get_monthly_usage(user_id) + tokens_used > plan.limit:
        raise HTTPException(402, "Upgrade to Pro for more queries")
```

**Free tier:** 50 queries/mo · **Pro:** 5000 queries/mo

---

### Lesson 9.3.4 — Intermediate: Stripe Usage-Based Billing (Intro)

**Pattern:** Stripe metered billing on `tokens_used` event  
**Beginner depth:** Document pricing page + mock upgrade flow; Stripe webhook stub

**Startup opportunity:** Vertical SaaS (legal, HR, sales) with this stack.

---

### Lesson 9.3.5 — Advanced: Embeddable Copilot Widget

**iframe or JS SDK** — customer embeds on their site  
**Security:** API key per customer, domain allowlist, CORS strict  
**White-label:** Custom colors, logo

---

# Topic 9.4 — Workflow Automation UI & TypeScript AI Integration

## Beginner-Friendly Explanation

**Workflow automation** = visual chain: "When ticket arrives → classify → RAG → draft reply"  
**Tools:** n8n (low-code), React Flow (custom UI), Trigger.dev (background jobs)

## Learning Outcome

Visual workflow editor OR n8n flow: ingest → classify → RAG → draft with execution history.

---

### Lesson 9.4.1 — Concept: Event-Driven AI Workflows

**Trigger:** Webhook, schedule, queue message  
**Steps:** Must be **idempotent** (safe to retry) — LLM steps especially

**Connect Module 05:** Agent as one node in larger workflow.

---

### Lesson 9.4.2 — Beginner: n8n LLM Nodes

**Lab:** n8n cloud or self-host → HTTP node to your RAG API → Slack notification  
**No-code win:** Ops teams modify workflow without Python deploy.

---

### Lesson 9.4.3 — Intermediate: React Flow Workflow Builder

**Nodes:** Ingest, Classify, RAG, Approve, Send  
**Edges:** Connect outputs → inputs  
**Export:** JSON workflow definition — version in Git

**Flagship project path:** AI Workflow Automation Platform capstone.

---

### Lesson 9.4.4 — Production: Execution History and Audit Log

**Store:** `{workflow_id, run_id, steps[], tokens, status, timestamp}`  
**UI:** Run history table with expand-to-see each step  
**Enterprise:** Same audit requirements as Module 07/10.

---

# Module 09 — Capstone Integration

## Week Progression

| Week | Focus |
|------|-------|
| 39 | Next.js chat UI + non-streaming RAG |
| 40 | Streaming + citations + error UX |
| 41 | Auth + token quotas |
| 42 | Voice/multimodal OR workflow OR SaaS landing |

## Required Deliverables

- [ ] Deployed frontend (Vercel) + backend URL in README
- [ ] Streaming chat with Stop button
- [ ] RAG citation UI
- [ ] Auth on at least one route
- [ ] Demo video (2 min) GIF or Loom

## Interview Questions

- "Implement streaming chat with error recovery."  
- "How show RAG citations in UI?"  
- "Embeddable copilot security model?"  
- "Design AI SaaS pricing based on tokens."

## Master Checklist Before Module 10

| Question | Yes / No |
|----------|----------|
| Is API key only server-side? | |
| Does chat handle loading and errors? | |
| Can I demo deployed URL in interview? | |

---

*Next: [module-10-ai-security-responsible-ai.md](./module-10-ai-security-responsible-ai.md)*
