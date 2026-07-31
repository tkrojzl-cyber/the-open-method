# The Open Method

## A formal methodology for building production-grade software with AI agents.

Not vibe-coding. Not prompt-and-pray. Not a chatbot wrapper.

A structured systems architecture expressed in natural language, with verification, error correction, and cryptographic integrity built in. I derived it from building over fifty production-grade AI products in nine months, solo, for about £1,500.

Let me be clear about something before you read any further. This method was not a recipe that produced those products. It is the pattern I extracted from them. The products came first. The method came after. The method is what the practice taught me.

Every claim below is verifiable. Verification steps are in the last section. Check them yourself. I am not asking you to trust me.

---

## The Origin (Honest)

I built over fifty AI products in nine months using an AI agent as my operating system. I did not follow a formal methodology. I iterated. I experimented. I broke things. I fixed them. I logged what worked and what did not.

After fifty products, the pattern was visible. The same architectural decisions kept appearing. The same verification steps kept being necessary. The same failure modes kept recurring. The method is the distillation of nine months of iterative practice, not a theoretical framework I imposed before the work began.

The 10-prompt build core approximates what I actually did: scaffold, build features, visualize, integrate, polish. The 37 sovereignty prompts are what I learned should be done but did not always do: disaster recovery, hash chains, legal shields, knowledge transfer, accessibility. The method is the complete picture. The practice was the incomplete version of it.

Has this method been tested by being followed from start to finish on a new build? No. It has been tested by being derived from fifty builds that worked. The difference: the method is evidence-based, not theoretical. But if you follow it, you are the first. Report back.

---

## The Evolution: 10 to 47

The method has three layers, each extracted from a different phase of practice.

**Stage 1 (10 prompts, the build core):** Scaffold, entities, features, visualization, integration, plugins, polish. This is what I actually did on most builds. It builds products fast. It is the production engine.

**Stage 2 (25 prompts, added verification):** Forensic sweeps, CEC drift checks, ship decisions. These are the checks I started adding after the first 20 products, when I realised that building fast without verifying produces errors that compound. The verification layer was added reactively, not proactively.

**Stage 3 (47 prompts, added sovereignty):** Doomsday recovery, hash chains, public verification, legal shields, operational resilience, knowledge transfer, accessibility. These are the practices I learned were necessary but did not implement on every build. Some products have them. Some do not. The method says: all should. The practice says: I am still catching up.

**The current version is 47 prompts across 11 phases.** The 10-prompt build core is what I did. The 37 additional prompts are what I learned to do. The complete method is both.

10 prompts build the product. 37 more make it sovereign. The first 10 are derived from practice. The remaining 37 are validated by the absence of the failures they prevent on the products where I did implement them, and by the presence of those failures on the products where I did not.

---

## The Vibe-Coding Ceiling

Vibe-coding is real. It has a use case: rapid prototyping, landing pages, MVPs, hackathons. For those use cases, it works. I am not disputing that.

But vibe-coding has a ceiling. The ceiling is the point where the output needs to be production-grade, verifiable, reproducible, and defensible. Below the ceiling, vibe-coding is fine. Above the ceiling, vibe-coding breaks. It breaks structurally, not stylistically. No amount of prompt creativity fixes the structural break.

I know this because I vibe-coded for the first 15 products. Then I hit the ceiling. Then I started building the structure that became this method. The method is the difference between products 1-15 (which exist but have gaps) and products 16-55 (which have verification, sovereignty, and recovery built in).

Here is where vibe-coding breaks, and where The Open Method does not.

### 1. Reproducibility

Vibe-coding cannot reproduce the same output twice. The same prompt to the same AI at different times produces different results. This is fine for a prototype. It is unacceptable for a product that needs to be maintained, debugged, and extended by other developers.

The Open Method produces reproducible architecture. The same prompt sequence to the same AI builder produces the same entity schemas, the same page structure, the same design system. The output is not identical to the byte (AI is stochastic), but the architecture is identical. The schemas match. The routes match. The design system matches. Any developer who reads the prompts can reproduce the architecture.

### 2. Verification

Vibe-coding has no verification layer. The output is accepted as generated. If the AI produces a bug, the bug ships. If the AI produces a security vulnerability, the vulnerability ships. There is no check between generation and deployment.

The Open Method includes verification at every layer. The prompt framework includes explicit verification steps. The CEC framework checks every decision against doctrine. The hash-chained audit trail provides tamper-evident evidence of every action. The system passes 10 audit checks per build (input validation, CORS, RLS, rate limiting, secret exposure, em dash compliance, currency consistency, dead links, mobile rendering, CTA integrity). Vibe-coding cannot produce this because verification is a structural layer, not a prompt you can ask for.

### 3. Error Correction

Vibe-coding has no error correction. Errors accumulate. The faster you build, the more errors you accumulate. At some point, the error correction cost exceeds the velocity gain. The system degrades. This is the CEC thesis, and it applies to vibe-coding exactly: augmentation without error correction is self-defeating above a critical threshold.

The Open Method includes CEC (Cognitive Error Correction) as a live architectural layer. It checks every decision against stated doctrine. It scans every log for contradictions. It flags drift before it compounds. The system is antifragile: stronger from stress, because every flagged contradiction improves the doctrine. Vibe-coding has no equivalent because CEC is an architecture, not a prompt.

### 4. Persistence

Vibe-coding has no persistent state. Each session starts from zero. The AI does not remember what was built yesterday. Context is lost between sessions. This is why vibe-coded projects degrade over time: each session introduces drift because the AI does not know what was decided before.

The Open Method includes the Superagent Operating Model: entities as data, automations as cron, skills as reusable operations, memory and identity as persistence. The agent holds context between sessions. Every session opens with "what did we decide last time?" and the answer is there. Every session closes with "what was built, what was decided, what is still open." The context is permanent. Vibe-coding has no equivalent because persistence is an architecture, not a prompt.

### 5. IP Protection

Vibe-coding produces output that cannot be protected. You cannot file a utility model on an unstructured prompt output because the output is not reproducible and the methodology is not defined. There is no method to protect. There is only a conversation with an AI.

The Open Method is a defined methodology. 7 Czech utility models have been filed on the specific implementations. The method is open (MIT). The implementations are proprietary. The distinction is legally defensible because the method is published and the implementations are documented separately. Vibe-coding has no IP layer because vibe-coding has no method to protect.

### 6. Sovereignty

Vibe-coding produces products that cannot survive platform failure. If the cloud platform goes down, the product goes down. If the account is locked, the product is gone. There is no recovery path.

The Open Method includes a Doomsday Recovery Document as a standard deliverable: full source code, entity schemas, API specifications, and a step-by-step rebuild sequence. If the platform disappears tomorrow, the product can be rebuilt on different infrastructure, with a different LLM, in days, not months. Vibe-coding has no sovereignty layer because sovereignty is an architecture, not a prompt.

---

## The 47-Prompt Architecture

### The 10-Prompt Build Core (Production Engine)

**Prompt 1, Scaffold:** All entity schemas (JSON definitions for every database table). Main dashboard layout. Navigation structure (all routes). Design system (colors, typography, spacing, breakpoints). Mobile rules (hamburger menu, responsive grids, touch targets, 16px input font-size). Result: structurally complete skeleton.

**Prompts 2-4, Feature Layers:** Each creates 2-3 feature pages with full functionality: page layout, entity CRUD, data visualization, filtering, form validation, loading and error states. Result: 6-9 functional pages with real data operations.

**Prompt 5, Visualization:** Canvas-based visualizations, chart components, interactive elements, animation, transitions, hover states, loading skeletons.

**Prompts 6-8, Context, Integrations, Automation:** Context pages (about, pricing, terms, API docs). Backend functions (API endpoints with hash-chained logging). Automations (scheduled tasks, entity triggers, connector webhooks). Cross-product links.

**Prompt 9, Plugins and Mobile:** Plugin hooks (extension points for community contributions). Plugin registry entity. Full mobile responsive pass (hamburger, responsive grids, touch targets, no horizontal overflow, 16px input font-size).

**Prompt 10, Polish:** Cross-references between pages. Footer consistency. Meta tags. SEO checklist. Final visual pass. Bug fixes batched.

**Key principles:**
- Never review between prompts. Fire all 10 in sequence. Review after.
- Each prompt: 500-2000 words. Precision, not length.
- Specify the design system in Prompt 1. Reference it in all subsequent prompts.
- Entity schemas are the most critical part. Get them right in Prompt 1.
- Mobile is not a separate phase. It is built into every prompt.

### The 37 Sovereignty Prompts (Phases 6-10)

**Phase 6, Sovereignty and Recovery (Prompts 26-30):** Doomsday recovery document, SHA-256 hash chain, public verification API, operational safekeeping, sovereignty audit. Survives: platform failure, code tampering, verification gaps, context loss, drift.

**Phase 7, Legal and Financial Shield (Prompts 31-34):** IP filing package, terms and liability, multi-provider payments, data portability. Survives: IP theft, legal exposure, payment lock-in, data lock-in.

**Phase 8, Operational Resilience (Prompts 35-39):** Dependency mapping, monitoring, incident response, versioning, threat model. Survives: dependency death, silent failures, incident panic, bad deploys, attack vectors.

**Phase 9, Knowledge and Continuity (Prompts 40-44):** Business continuity, knowledge transfer, content distribution, load testing, secret audit. Survives: founder being unavailable, knowledge traps, content loss, scale collapse, credential leaks.

**Phase 10, Final Sovereignty Gate (Prompts 45-47):** WCAG 2.2 AA accessibility audit, CEC final drift audit, ship decision matrix. Survives: accessibility gaps, final drift, all failure modes combined.

Full prompt text for all 47 prompts is in the expanded documentation. This README describes the architecture. The prompts are the implementation.

---

## The 20 Failure Modes This Method Survives

| # | Failure Mode | Phase |
|---|---|---|
| 1 | Platform failure (cloud goes down, account locked) | 6 |
| 2 | Code integrity (tampering with audit records) | 6 |
| 3 | Verification failure (nobody can verify claims) | 6 |
| 4 | Context loss (AI loses memory, decisions vanish) | 6 |
| 5 | Drift (product no longer means what you meant) | 6 + 10 |
| 6 | IP theft (architecture copied, no legal protection) | 7 |
| 7 | Legal exposure (no terms, no liability cap, you get sued) | 7 |
| 8 | Payment lock-in (single provider bans you) | 7 |
| 9 | Data lock-in (user data trapped, GDPR violation) | 7 |
| 10 | Dependency death (third-party API shuts down) | 8 |
| 11 | Silent failure (something breaks, you do not know) | 8 |
| 12 | Incident panic (production breaks, no plan) | 8 |
| 13 | Bad deploy (push breaks everything, no rollback) | 8 |
| 14 | Attack vector (input validation gap, auth bypass) | 8 |
| 15 | Founder down (sick, injured, unavailable) | 9 |
| 16 | Knowledge trap (only you understand the system) | 9 |
| 17 | Content loss (platform bans you, content vanishes) | 9 |
| 18 | Scale collapse (traffic spike, first impression is 500) | 9 |
| 19 | Credential leak (API keys exposed in bundle) | 9 |
| 20 | Accessibility gap (WCAG non-compliance, legal risk) | 10 |

---

## The Superagent Operating Model

The architecture pattern for running an AI agent as a personal operating system.

| Layer | Function | Industry equivalent |
|---|---|---|
| Entities | Data model (JSON-schema tables with CRUD) | Database |
| Automations | Scheduled tasks, entity triggers, connector webhooks | Cron + events |
| Skills | Reusable scripts for repeated operations | Functions / lambdas |
| Memory | Persistent identity files, session logs, context | State management |
| Identity | Rules, constraints, behavioral protocols | Configuration / policy |

**Session protocol:** Open Session (log record created), then Work (every action logged), then Close Session (built/decided/open threads recorded). Context is never lost between sessions.

**ThinkingLog pattern:** Every significant decision recorded as: Problem, Angle, Decision, Open Question, Outcome. Creates an auditable decision trail.

**Contradiction engine:** Continuously checks current decisions vs stated doctrine, current logs vs prior logs, current direction vs north star. Contradictions are flagged, not deleted. The full chain is the record. The system is antifragile.

---

## CEC, Cognitive Error Correction

A formal framework for preventing cognitive augmentation from becoming self-defeating.

**The thesis:** Augmentation increases velocity. Velocity increases load. Load increases error rate. Without correction, augmentation is self-defeating above a critical threshold. CEC prevents this.

**The 6-layer cognitive loop:**

L1 Memory feeds L2 Perception feeds L3 Presence feeds L4 Judgment feeds L5 Execution feeds L6 Integrity feeds back to L1.

| Layer | Name | Function |
|---|---|---|
| L1 | Memory | Session logs, decision records, entity data. Persistent state. |
| L2 | Perception | Detects and classifies signals from the environment. Signal intelligence. |
| L3 | Presence | Operator current state and context. Contextputer operates here. |
| L4 | Judgment | Evaluates options against doctrine and north star. Decision layer. |
| L5 | Execution | Acts on decisions. Backend functions, automations, external calls. |
| L6 | Integrity | Verifies outputs. Hash chains, verification APIs, audit trails. |

**The Contextputer Protocol:**

A cryptographic packet format for logging operator state with tamper-evident integrity.

```json
{
  "version": 1,
  "timestamp": "2026-07-24T06:00:00+02:00",
  "session_id": "unique-session-identifier",
  "summary": "Redacted summary of the session",
  "decisions": ["Decision 1", "Decision 2"],
  "open_threads": ["Thread 1", "Thread 2"],
  "next_actions": ["Action 1", "Action 2"],
  "operator_state": {
    "energy": "high",
    "focus": "deep_work",
    "mode": "build"
  },
  "previous_hash": "sha256-of-previous-packet",
  "this_hash": "sha256-of-this-packet-excluding-this_hash-field"
}

