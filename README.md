# The Open Method

## A formal methodology for building production-grade software with AI agents.

Not vibe-coding, or prompt-and-pray, or a chatbot wrapper.

A structured systems architecture expressed in natural language, with verification, error correction, and cryptographic integrity built in. Derived from a systematic building practice over nine months, solo, for about â‚¬2,100.

This method was not a recipe that produced those products. It is the pattern extracted from them. The products came first. The method came after. The method is what the practice taught.

Every claim below is verifiable. Verification steps are in the last section. Check it yourself. No trust required.

---

## The Origin (Honest)

Production-grade AI products were built over nine months using an AI agent as an operating system. No formal methodology was followed. Iteration. Experimentation. Things broke. Things got fixed. What worked and what did not got logged.

After extensive building, the pattern was visible. The same architectural decisions kept appearing. The same verification steps kept being necessary. The same failure modes kept recurring. The method is the distillation of nine months of iterative practice, not a theoretical framework imposed before the work began.

The 10-prompt build core approximates what was actually done: scaffold, build features, visualize, integrate, polish. The 37 sovereignty prompts are what was learned should be done but was not always done: disaster recovery, hash chains, legal shields, knowledge transfer, accessibility. The method is the complete picture. The practice was the incomplete version of it.

Has this method been tested by being followed from start to finish on a new build? No. It has been tested by being derived from builds that worked. The difference: the method is evidence-based, not theoretical. But if you follow it, you are the first. Report back.

---

## The Evolution: 10 to 47

The method has three layers, each extracted from a different phase of practice.

**Stage 1 (10 prompts, the build core):** Scaffold, entities, features, visualization, integration, plugins, polish. This is what was actually done on most builds. It builds products fast. It is the production engine.

**Stage 2 (25 prompts, added verification):** Forensic sweeps, CEC drift checks, ship decisions. These are the checks that started appearing after the first products, when it became clear that building fast without verifying produces errors that compound. The verification layer was added reactively, not proactively.

**Stage 3 (47 prompts, added sovereignty):** Doomsday recovery, hash chains, public verification, legal shields, operational resilience, knowledge transfer, accessibility. These are the practices that were learned to be necessary but were not implemented on every build. Some products have them. Some do not. The method says: all should. The practice says: still catching up.

**The current version is 47 prompts across 11 phases.** The 10-prompt build core is what was done. The 37 additional prompts are what was learned to do. The complete method is both.

10 prompts build the product. 37 more make it sovereign. The first 10 are derived from practice. The remaining 37 are validated by the absence of the failures they prevent on the products where they were implemented, and by the presence of those failures on the products where they were not.

---

## The Vibe-Coding Ceiling

Vibe-coding is real. It has a use case: rapid prototyping, landing pages, MVPs, hackathons. For those use cases, it works. That is not in dispute.

But vibe-coding has a ceiling. The ceiling is the point where the output needs to be production-grade, verifiable, reproducible, and defensible. Below the ceiling, vibe-coding is fine. Above the ceiling, vibe-coding breaks. It breaks structurally, not stylistically. No amount of prompt creativity fixes the structural break.

The first products were vibe-coded. Then the ceiling hit. Then the structure that became this method started being built. The method is the difference between early products (which exist but have gaps) and later products (which have verification, sovereignty, and recovery built in).

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

A working software layer that detects drift from the north star. Not a theoretical framework. A system that runs.

**The thesis:** Augmentation increases velocity. Velocity increases load. Load increases error rate. Without correction, augmentation is self-defeating above a critical threshold. CEC prevents this by catching drift before it compounds.

**What CEC actually does (three components, all running):**

**1. Decision Logging (ThinkingLog).** Every significant decision is recorded as a structured entry: Problem, Angle, Decision, Open Question, Outcome. This is not a diary. It is an auditable decision trail. Each entry is tagged, dated, and linked to the product and lead it relates to. The ThinkingLog is the input. Without logged decisions, there is nothing to check.

**2. Contradiction Engine.** Scans the ThinkingLog for contradictions. Compares current decisions against prior decisions. If Entry A (older) contradicts Entry B (newer), Entry A gets flagged. Temporal weighting: the newer decision wins, the older entry gets the flag. This stops the system from flagging decisions you already resolved. A 60-day recency window prevents the engine from flagging intentional pivots as contradictions. Decisions more than 60 days apart are probably deliberate changes of direction, not drift.

The contradiction engine also checks decisions against the north star. If the current direction contradicts the stated objective, the contradiction is flagged. Not deleted. The full chain is the record. The system is antifragile: every flagged contradiction improves the doctrine.

**3. Coherence Audit.** A weekly cross-reference of the entire system. Checks whether outreach verticals, content calendar, LinkedIn posts, VOID signal scans, and ThinkingLog focus are all pointing in the same direction. Scores coherence 0-10. If the score drops below 7, drift is flagged. This catches the failure mode where each part of the system is working but they are working against each other.

**How CEC runs:**

CEC runs after every build phase. The output is stored on the BuildSession record: cec_last_run, cec_drift_severity, cec_contradiction_flag, cec_output_summary. The drift severity tells you how far off course you are. The contradiction flag tells you which decisions conflict. The summary tells you what to fix.

This is not a dashboard you look at. It is a layer that runs. It flags problems before they compound. It does not fix them. The operator fixes them. CEC identifies. The human decides.

**Why this is not vibe-coding:**

Vibe-coding has no error correction. Errors accumulate. The faster you build, the more errors you accumulate. At some point, the error correction cost exceeds the velocity gain. The system degrades. CEC prevents this because it runs continuously, not after the fact. It is the difference between a smoke alarm and a fire investigation. One catches the fire while it is small. The other figures out why it burned.

**What CEC is not:**

CEC is not a cognitive model. It is not a theory of mind. It is not a 6-layer architecture diagram. It is a working system: log decisions, check for contradictions, audit coherence, flag drift. The same three steps every time. The value is in running it, not in diagramming it.

**The Contextputer Protocol:**

A cryptographic packet format for logging operator state with tamper-evident integrity. This is the hardware layer of CEC. The software layer (ThinkingLog, contradiction engine, coherence audit) runs on the agent. The hardware layer (Contextputer) runs on the CardPuter. Both produce evidence. Both are tamper-evident. One is cloud. One is silicon.

```json
{
  "version": 1,
  "timestamp": "2026-07-24T06:00:00+02:00",
  "session_id": "unique-session-identifier",
  "summary": "Redacted summary of the session",
  "decisions": ["Decision 1", "Decision 2"],
  "open_threads": ["Thread 1", "Thread 2"],
  "next_actions": ["Action 1", "Action 2"],
  "previous_hash": "sha256-of-previous-packet",
  "this_hash": "sha256-of-this-packet-excluding-this_hash-field"
}
```

**Critical rules:**
- summary is redacted before hashing. No sensitive data in the chain.
- previous_hash links to the previous packet. SHA-256. Break the chain, every downstream packet fails verification instantly.
- Not a blockchain (no distributed consensus). Local, tamper-evident.

**Three-tier build sequence:**

| Tier | What | Hardware |
|---|---|---|
| Tier 1 | Packet storage to SD card. No firmware. | M5Cardputer or any ESP32-S3 |
| Tier 2 | USB bridge to host. Packets sync to local DB. | Same + USB |
| Tier 3 | Full firmware daemon. Continuous logging, real-time hash chain. | Same + PresenceOS firmware |

Note: Contextputer is the protocol. The M5Cardputer is the hardware that runs it.
---

## How Infrastructure Standards Are Born

ISO 27001 started as one document. One organization. One audit. One certificate. Then adoption. Then global infrastructure. The standard defines what acceptable security looks like. The audit verifies it. The certificate proves it. Three components. One system. Now deployed in over 96,000 organizations worldwide.

SSL started as one implementation. One browser. One certificate authority. Then adoption. Then global infrastructure. The standard defines the protocol. The implementation runs it. The certificate authority issues the trust. Three components. One system. Now securing every HTTPS connection on the internet.

The Open Method follows the same architecture. The method is the standard. The implementation is the product. The seal is the certificate. The deployment network is the certificate authority network. The law creates the need. The standard fills the need. The deployment network scales it.

This is not a product. This is how infrastructure standards are born.

---

## The Open-Core Model

**Open (MIT, this repo):** Presence.js, 10-Prompt Build Core, 47-Prompt Sovereignty Framework, Superagent Operating Model, CEC Framework, Contextputer Protocol.

**Proprietary (utility models):** Cognos, Proof of Operator, Digital Sovereignty, Ghost OS, Sovereignty Stack (â‚¬8,500 + 2% rev share).

**Deployment network (bounty-driven):** Open Cognos Initiative, Plugin Registry, community plugins. Contributors own their work. Brainiac owns the platform.

**The principle:** Open the HOW. Sell the WHAT. Own the WHERE.

This is the open-core model. Red Hat built it and was acquired by IBM for $34B. GitHub built it and was acquired by Microsoft for $7.5B. Supabase built it and became venture-backed. The method is free. The deployment is paid. The network compounds the value.

---

## The Deployment Network

15 bounties. No cash up front. You own your work. You earn from it.

**How it works:**

This is an open-core project with a revenue-sharing model. The deployment network activates with the first paid client engagement. Until then, contributions are volunteer, portfolio-building, and MIT-licensed. When revenue arrives, contributors get paid from it. No cash is promised from a fund that does not exist. This is a revenue share from real money when real money lands.

**The deal:**

- Build a bounty. Submit a PR with tests and documentation.
- If accepted and merged, you receive: a public credit line on the repository, a revenue share from your plugin once it is deployed to a paying client, and first right of refusal on paid maintenance contracts for your contribution.
- You retain ownership of your code. Brainiac retains the right to merge it into the platform.
- If no client revenue arrives, no cash is owed. You still own your code. You still have the credit line. You still have a shipped plugin on a public repository with a live audience.

**Why this is fair:**

The method is published for free because the method is stronger when other people build on it. But cash that does not exist will not be promised. That would violate the honesty principle this entire repository is built on. What can be promised: a real platform, a real audience, a real method, and a real revenue share the moment revenue exists. If you build something that matters, you share in what it earns. If it earns nothing, you keep your work and your reputation.

**This is how infrastructure deploys:**

ISO 27001 does not deploy through one auditor. It deploys through a network of certified auditors. SSL does not deploy through one certificate authority. It deploys through a network of certificate authorities. The bounty board is the deployment network. The method is the standard. The plugins are the implementations. The revenue share is the installer fee.

**The principle:** Open the HOW. Sell the WHAT. Share the WHAT when it sells.

| # | Bounty | Layer | Revenue Share |
|---|---|---|---|
| 1 | Signal Detector: LinkedIn Scraper | L2 | 5% of client revenue from this plugin |
| 2 | Signal Detector: Reddit Sentiment | L2 | 5% of client revenue from this plugin |
| 3 | Signal Detector: GitHub Referrer | L2 | 5% of client revenue from this plugin |
| 4 | Signal Detector: Hacker News Score | L2 | 5% of client revenue from this plugin |
| 5 | Signal Detector: Search Intent | L2 | 5% of client revenue from this plugin |
| 6 | PresenceOS: Voice Logger | L3 | 10% of client revenue from this plugin |
| 7 | PresenceOS: LoRa Sync | L3 | 10% of client revenue from this plugin |
| 8 | PresenceOS: Cognitive Twin | L3 | 10% of client revenue from this plugin |
| 9 | Judgment Template: Finance | L4 | 5% of client revenue from this template |
| 10 | Judgment Template: Healthcare | L4 | 5% of client revenue from this template |
| 11 | Judgment Template: Legal | L4 | 5% of client revenue from this template |
| 12 | Judgment Template: Education | L4 | 5% of client revenue from this template |
| 13 | Plugin: CEC Dashboard | L6 | 10% of client revenue from this plugin |
| 14 | Plugin: Session Replay | L1 | 5% of client revenue from this plugin |
| 15 | Plugin: Multi-Agent Bridge | L5 | 10% of client revenue from this plugin |

**To claim:** Fork, build, submit PR with tests and docs. All contributions must be MIT licensed, include documentation, include tests, and be compatible with the 6-layer architecture. No proprietary dependencies.

**The fine print, stated plainly:** Revenue share is calculated from gross revenue received by Brainiac Ltd for the specific plugin or template the contributor built. Share is paid quarterly. Minimum payout threshold is â‚¬100. If the plugin generates no client revenue, no payment is owed. This is a revenue share, not a salary, not a guarantee, and not a debt. It is a deal between builders who believe the method works and want to prove it together.

---

## The 15 Governing Principles

1. Database first, always. Entities before pages. No exceptions.
2. Bilingual from day one. Locale detection + translation keys in the foundation.
3. Mobile-first. Design for 375px, then scale up. Hamburger is not an afterthought.
4. Security is not optional. RLS, CORS, input validation. Every product, every time.
5. Every state has a design. Loading, empty, error, success. No blank pages, ever.
6. Voice is enforced programmatically. Em dash checks built in, not swept.
7. Builder "ready" does not equal live. Verify bundle changed. Check mobile. Run a sweep.
8. The IA Constitution is the first check. Amplify or replace? Before any build begins.
9. Each prompt is self-contained. Paste it, it works. No interpretation needed.
10. CEC runs after every phase. Drift detection, contradiction check, coherence audit.
11. If you cannot leave, you are not sovereign. Every build produces a Doomsday doc before it ships.
12. Trust requires proof, not claims. Every claim is verifiable via a public endpoint requiring no authentication.
13. Context loss is inevitable. Every build produces an operational safekeeping file that survives it.
14. The founder is a single point of failure. Every build produces a knowledge transfer document that a competent stranger could use to continue the work.
15. The last check is not "does it work." It is "does it still mean what we meant when we started."

---

## The Cost Comparison

All figures verified July 31, 2026. CZK inputs are actual purchase prices. EUR at approximately 25 CZK/EUR.

| Component | Industry cost (EU market rates) | Open Method cost |
|---|---|---|
| Backend engineering (hash-chained API functions) | â‚¬45K-90K | â‚¬0 |
| Security and quality engineering (10 audit checks per build) | â‚¬17K-34K | â‚¬0 |
| UI/UX design (production-grade products) | â‚¬34K-68K | â‚¬0 |
| Internationalization (Czech/English) | â‚¬9K-17K | â‚¬0 |
| Product management (systematic building practice) | â‚¬28K-56K | â‚¬0 |
| IP filing (7 utility models) | â‚¬5K-17K | â‚¬140 |
| Technical writing (API docs, specs) | â‚¬11K-22K | â‚¬0 |
| Legal (terms, privacy, GDPR) | â‚¬11K-28K | â‚¬0 |
| Disaster recovery planning | â‚¬17K-34K | â‚¬0 |
| Business continuity planning | â‚¬11K-22K | â‚¬0 |
| Accessibility audit (WCAG 2.2 AA) | â‚¬6K-17K | â‚¬0 |
| **Total** | **â‚¬194K-405K** | **~â‚¬2,100** |

**The â‚¬2,100 breakdown:**

| Category | Item | CZK input | EUR value | Role in system |
|---|---|---|---|---|
| Sovereignty Stack | M5Cardputer Field Unit | 1,500 CZK | â‚¬60 | Physical hash-chain and field logger |
| Sovereignty Stack | Beelink SER5 Mini PC Host | 13,000 CZK | â‚¬520 | Air-gapped local inference server |
| **Sovereignty subtotal** | **Core infrastructure** | **14,500 CZK** | **â‚¬580** | **Core AI and verification hardware** |
| Production and IP | 7x utility model filings | 3,500 CZK (7 x 500 CZK online via upv.gov.cz) | â‚¬140 | IP protection (12-mo EPO priority) |
| Production and IP | Blue Yeti microphone | 3,000 CZK | â‚¬120 | Audio processing and capture |
| Production and IP | Cables and adapters | 3,000 CZK | â‚¬120 | Interconnects and signal pipeline |
| Production and IP | USB drives and storage | 3,000 CZK | â‚¬120 | Offline air-gapped backups |
| Production and IP | Legacy build host (GTX 1070 era) | 7,500 CZK (estimated market value) | â‚¬300 | Secondary build host |
| Production and IP | Dual display monitors | 6,000 CZK | â‚¬240 | Production display array |
| Production and IP | iPhone 14 camera node | 12,000 CZK | â‚¬480 | Video B-roll / overhead camera |
| **Total** | **Full keynote and filings stack** | **52,000 CZK** | **~â‚¬2,100** | **Complete physical and IP production** |

Every line item is verifiable. The first two lines are the sovereignty stack: the hardware that runs the hash chain and the local models. The remaining lines are production gear, IP filings, and the legacy build host. No hidden costs. No rounding tricks.

**The sovereignty stack alone: â‚¬580.** This is the CardPuter plus the Beelink. This is what runs the hash chain and the local AI models. This is the infrastructure the talk is about.

**The cloud equivalent: approximately â‚¬10,000 per year** in API subscriptions across four model providers, based on current per-token enterprise pricing. The sovereignty stack costs â‚¬580 once. Break-even: under four weeks.

**Multiplier: 92x to 192x.** This is not a rounding error. It is a structural difference in cost architecture between the industry model (teams, hours, overhead) and the Open Method (one person, one agent, structured prompts, persistent state, error correction, verification).

---

## VERIFY THIS YOURSELF

Every claim in this repository is verifiable. Do not take anyone's word for it. Check it yourself. The entire methodology is built on the principle that claims must be verifiable. If a claim cannot be verified, it is not a claim. It is marketing.

### Step 1: Verify the products exist (30 seconds)
- Visit `https://auditproof.pro`. The operator assessment system should load. Three verifiable tonight: auditproof.pro, digitalsovereignty.online, ghost-os.online.
- Visit `https://digitalsovereignty.online`. The B2B platform should load. Czech default if your browser is in Czech or your timezone is Prague.
- Visit `https://ghost-os.online`. The tactical field manual should load.

### Step 2: Verify Presence.js works (60 seconds)
- Open your browser console on any page.
- Paste: `<script src="https://cdn.jsdelivr.net/gh/tkrojzl-cyber/presence@main/presence.js"></script>`
- Then type: `Presence.signals`. You should see 14 signals about your current session.
- Then type: `Presence.getIntentState()`. You should see your 3-axis intent state.
- Then type: `Presence.debug()`. All signals print to console.

Note: The GitHub version of Presence.js has 14 signals. The production version on auditproof.pro has 40 signals. The 14-signal version is the open-source baseline. The 40-signal version is proprietary.

### Step 3: Verify the audit seal system (2 minutes)
- Visit `https://auditproof.pro`.
- Run the free 26-question audit.
- At the end, you receive a seal with a hash.
- Copy the hash.
- Visit `https://auditproof.pro/verify` and paste the hash.
- The system returns a verification result.

### Step 4: Verify the hash chain (2 minutes)
- The verification API is public. No account required.
- Call: `GET https://jeeves-7cf35109.base44.app/functions/verifyAuditSeal?hash=YOUR_HASH`
- The response includes: seal data, hash chain link to previous entry, verification status.
- This is a live SHA-256 hash chain. You can verify the math yourself.

### Step 5: Verify the GitHub repository (30 seconds)
- Visit `github.com/tkrojzl-cyber/presence`. Presence.js source code, MIT license.
- Visit `github.com/tkrojzl-cyber/the-open-method`. This repository.

### Step 6: Verify the IP filings (5 minutes)
- Search the Czech Industrial Property Office (UPV) database for utility model filings under Krojzl.
- 7 utility models filed. Total cost: 3,500 CZK (7 x 500 CZK). 12-month EPO priority window active.

---

## Who Built This

**Tom Krojzl**, Brainiac Ltd
- Building since October 2025
- Production-grade AI products across multiple verticals
- 7 utility models filed
- Operating from Prague, Czech Republic
- Company registered in London (167-169 Great Portland Street, W1W 5PF)
- Contact: thomas@brainiaclimited.com

## License

MIT. Use it. Build with it. Fork it. If you build something that matters, say so.

The method is open. The deployment is paid. The standard is the moat.

---

*This repository goes public on August 1, 2026 at 19:00 CET. The deployment network launches the same day. Everything before that date is preparation. Everything after is the flywheel.*


