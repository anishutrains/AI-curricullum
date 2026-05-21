# Module 09 — Full Stack AI

---

## Topic 9.1: Next.js AI Frontends & Streaming UX

### 1. Topic Name
Next.js AI Frontends & Streaming UX

### 2. Why This Topic Matters
AI Application Developer roles require React/Next.js + streaming—Vercel AI SDK patterns are industry standard.

### 3. Job Roles
AI Application Developer, AI Copilot Engineer, AI Product Engineer

### 4. Learning Objectives
- Build chat UI with streaming token display
- Use Vercel AI SDK / server actions
- Handle loading, errors, and stop generation

### 5. Lessons/Subtopics
- Next.js App Router
- Server-sent events from FastAPI/Next
- Vercel AI SDK `useChat`
- Message history and thread UI
- Markdown rendering + code highlighting
- Citation UI for RAG sources

### 6. Hands-on Labs
**Lab 9.1:** Next.js chat app consuming Module 01 FastAPI stream.

### 7. Enterprise Projects
SSO login stub; branded UI; accessibility WCAG basics.

### 8. Portfolio Projects
Deployed Vercel frontend + API URL in README.

### 9. Interview Preparation
- "Implement streaming chat with error recovery."
- "How do you show RAG citations in UI?"

### 10. Real-world Use Cases
Customer portals, internal copilots, sales tools.

### 11. Tools & Technologies
Next.js 14+, TypeScript, Vercel AI SDK, Tailwind, shadcn/ui

### 12. Common Mistakes
- Exposing API keys in frontend
- No abort/stop for long generations
- XSS via unsanitized markdown

### 13. Industry Best Practices
- API keys only server-side
- Optimistic UI with rollback
- Mobile-responsive chat layout

### 14. Capstone Deliverables
Production-quality chat UI wired to RAG backend.

---

## Topic 9.2: Multimodal & Voice AI Applications

### 1. Topic Name
Multimodal & Voice AI Applications

### 2. Why This Topic Matters
Multimodal search and voice support growing in customer experience roles—Whisper + TTS pipelines expected.

### 3. Job Roles
Conversational AI Engineer, AI Product Engineer

### 4. Learning Objectives
- Process image + text inputs in Gemini/GPT-4o
- Build voice pipeline: STT → LLM → TTS
- Design latency budgets for voice

### 5. Lessons/Subtopics
- Vision API document Q&A
- Whisper transcription
- ElevenLabs / OpenAI TTS
- Real-time voice WebRTC overview
- Lip-sync and avatar (awareness)
- Multimodal RAG (image chunks)

### 6. Hands-on Labs
**Lab 9.2:** Voice note → transcript → RAG answer → audio response.

### 7. Enterprise Projects
**Multimodal AI Search Engine** — text + image upload search.

### 8. Portfolio Projects
Demo video of voice or image Q&A flow.

### 9. Interview Preparation
- "Design voice customer support architecture."
- "Latency targets for voice AI?"

### 10. Real-world Use Cases
Call center assist, field tech photo diagnosis, retail visual search.

### 11. Tools & Technologies
OpenAI Whisper, GPT-4o vision, Gemini multimodal, ElevenLabs

### 12. Common Mistakes
- Sequential STT→LLM→TTS without streaming (slow UX)
- No noise handling in telephony audio
- Storing voice recordings without consent

### 13. Industry Best Practices
- Stream partial transcripts
- Consent banner for recording
- Fallback to text chat

### 14. Capstone Deliverables
Multimodal or voice feature in full-stack project.

---

## Topic 9.3: AI SaaS Products & Copilot Patterns

### 1. Topic Name
AI SaaS Products — Auth, Billing & Copilot Patterns

### 2. Why This Topic Matters
Startup-ready engineers ship AI SaaS: auth, usage metering, embeddable copilots.

### 3. Job Roles
AI Product Engineer, AI Application Developer, startup founders

### 4. Learning Objectives
- Add auth (Clerk/Auth0/NextAuth)
- Meter token usage per user
- Design embeddable copilot widget

### 5. Lessons/Subtopics
- SaaS architecture for AI (API-first)
- Stripe usage-based billing intro
- Rate limits per plan tier
- Embeddable widget (iframe/SDK)
- White-label copilot options
- Onboarding and activation metrics

### 6. Hands-on Labs
**Lab 9.3:** Free vs Pro tier with token quota enforcement.

### 7. Enterprise Projects
**AI Sales Assistant** or **AI Recruiter System** as SaaS-shaped portfolio.

### 8. Portfolio Projects
Landing page + waitlist + working product loop.

### 9. Interview Preparation
- "Design AI SaaS pricing based on tokens."
- "Embeddable copilot security model."

### 10. Real-world Use Cases
B2B AI tools, vertical SaaS (legal, HR, sales).

### 11. Tools & Technologies
Clerk, Stripe, Posthog, FastAPI middleware for quotas

### 12. Common Mistakes
- No usage tracking before launch
- Unlimited free tier abuse
- Weak tenant isolation in SaaS DB

### 13. Industry Best Practices
- Instrument activation funnel day one
- Graceful degradation when quota exceeded
- Clear ToS on data usage

### 14. Capstone Deliverables
SaaS MVP with auth + usage limits + 1-page business model.

---

## Topic 9.4: TypeScript AI SDKs & Workflow Automation UI

### 1. Topic Name
TypeScript AI Integration & Workflow Automation UI

### 2. Why This Topic Matters
Full-stack AI teams use TypeScript for SDKs and workflow builders—n8n + custom UI patterns.

### 3. Job Roles
AI Workflow Engineer, AI Automation Engineer, AI Integration Engineer

### 4. Learning Objectives
- Call AI APIs from TypeScript services
- Build workflow builder UI (nodes/edges)
- Integrate n8n or Trigger.dev with LLM steps

### 5. Lessons/Subtopics
- OpenAI Node SDK
- React Flow for workflow UI
- n8n LLM nodes
- Webhook orchestration
- Event-driven agent triggers
- Temporal intro (durable workflows)

### 6. Hands-on Labs
**Lab 9.4:** Visual workflow: ingest ticket → classify → RAG → draft reply.

### 7. Enterprise Projects
**AI Workflow Automation Platform** (flagship).

### 8. Portfolio Projects
Screenshot of workflow editor + JSON export of flows.

### 9. Interview Preparation
- "Build no-code AI workflow for ops team—architecture?"
- "Idempotent workflow steps with LLMs."

### 10. Real-world Use Cases
Ops automation, marketing pipelines, HR onboarding flows.

### 11. Tools & Technologies
TypeScript, React Flow, n8n, Trigger.dev, Temporal (intro)

### 12. Common Mistakes
- Non-idempotent LLM steps on retry
- No dead-letter queue for failures
- UI allowing cyclic workflows

### 13. Industry Best Practices
- Version workflow definitions
- Test workflows with recorded fixtures
- Audit log per execution

### 14. Capstone Deliverables
Workflow platform with 3 templates and execution history API.

---

*Next: [module-10-ai-security-responsible-ai.md](./module-10-ai-security-responsible-ai.md)*
