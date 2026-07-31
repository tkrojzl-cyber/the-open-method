# The Open Method

## A formal methodology for building production-grade software with AI agents.

Not vibe-coding. Not prompt-and-pray. Not a chatbot wrapper.

A structured systems architecture expressed in natural language, with verification, error correction, and cryptographic integrity built in. Derived from building over fifty production-grade AI products in nine months, solo, for approximately £1,500.

This method was not a recipe that produced those products. It is the pattern extracted from them. The products came first. The method came after. The method is what the practice taught.

Every claim below is verifiable. Verification steps are in the last section. Check them yourself.

---

## The Origin (Honest)

I built over fifty AI products in nine months using an AI agent as my operating system. I did not follow a formal methodology. I iterated. I experimented. I broke things. I fixed them. I logged what worked and what did not.

After fifty products, the pattern was visible. The same architectural decisions kept appearing. The same verification steps kept being necessary. The same failure modes kept recurring. The method is the distillation of nine months of iterative practice, not a theoretical framework imposed before the work began.

The 10-prompt build core approximates what I actually did: scaffold, build features, visualize, integrate, polish. The 37 sovereignty prompts are what I learned should be done but did not always do: disaster recovery, hash chains, legal shields, knowledge transfer, accessibility. The method is the complete picture. The practice was the incomplete version of it.

The method has not been tested by being followed from start to finish on a new build. It has been tested by being derived from fifty builds that worked. The difference: the method is evidence-based, not theoretical. But if you follow it, you are the first. Report back.

---

## The Evolution: 10 to 47

The method has three layers, each extracted from a different phase of practice:

**Stage 1 (10 prompts - the build core):** Scaffold, entities, features, visualization, integration, plugins, polish. This is what I actually did on most builds. It builds products fast. It is the production engine.

**Stage 2 (25 prompts - added verification):** Forensic sweeps, CEC drift checks, ship decisions. These are the checks I started adding after the first 20 products, when I realized that building fast without verifying produces errors that compound. The verification layer was added reactively, not proactively.

**Stage 3 (47 prompts - added sovereignty):** Doomsday recovery, hash chains, public verification, legal shields, operational resilience, knowledge transfer, accessibility. These are the practices I learned were necessary but did not implement on every build. Some products have them. Some do not. The method says: all should. The practice says: I am still catching up.

**The current version is 47 prompts across 11 phases.** The 10-prompt build core is what I did. The 37 additional prompts are what I learned to do. The complete method is both.

10 prompts build the product. 37 more make it sovereign. The first 10 are derived from practice. The remaining 37 are validated by the absence of the failures they prevent on the products where I did implement them, and by the presence of those failures on the products where I did not.

---

## The Vibe-Coding Ceiling

Vibe-coding is real. It has a use case: rapid prototyping, landing pages, MVPs, hackathons. For those use cases, it works. This repository does not dispute that.

But vibe-coding has a ceiling. The ceiling is the point where the output needs to be production-grade, verifiable, reproducible, and defensible. Below the ceiling, vibe-coding is fine. Above the ceiling, vibe-coding breaks. It breaks structurally, not stylistically. No amount of prompt creativity fixes the structural break.

I know this because I vibe-coded for the first 15 products. Then I hit the ceiling. Then I started building the structure that became this method. The method is the difference between products 1-15 (which exist but have gaps) and products 16-55 (which have verification, sovereignty, and recovery built in).

Here is where vibe-coding breaks, and where The Open Method does not:

### 1. Reproducibility

Vibe-coding cannot reproduce the same output twice. The same prompt to the same AI at different times produces different results. This is acceptable for a prototype. It is unacceptable for a product that needs to be maintained, debugged, and extended by other developers.

The Open Method produces reproducible architecture. The same prompt sequence to the same AI builder produces the same entity schemas, the same page structure, the same design system. The output is not identical to the byte (AI is stochastic), but the architecture is identical. The schemas match. The routes match. The design system matches. Any developer who reads the prompts can reproduce the architecture.

### 2. Verification

Vibe-coding has no verification layer. The output is accepted as generated. If the AI produces a bug, the bug ships. If the AI produces a security vulnerability, the vulnerability ships. There is no check between generation and deployment.

The Open Method includes verification at every layer. The prompt framework includes explicit verification steps. The CEC framework checks every decision against doctrine. The hash-chained audit trail provides tamper-evident evidence of every action. The W3C Verifiable Credentials output conforms to an international standard. The system passes 10 security audit checks per build (input validation, CORS, RLS, rate limiting, secret exposure, em dash compliance, currency consistency, dead links, mobile rendering, CTA integrity). Vibe-coding cannot produce this because verification is a structural layer, not a prompt you can ask for.

### 3. Error Correction

Vibe-coding has no error correction. Errors accumulate. The faster you build, the more errors you accumulate. At some point, the error correction cost exceeds the velocity gain. The system degrades. This is the CEC thesis, and it applies to vibe-coding exactly: augmentation without error correction is self-defeating above a critical threshold.

The Open Method includes CEC (Cognitive Error Correction) as a live architectural layer. It checks every decision against stated doctrine. It scans every log for contradictions. It flags drift before it compounds. The system is antifragile: stronger from stress, because every flagged contradiction improves the doctrine. Vibe-coding has no equivalent because CEC is an architecture, not a prompt.

### 4. Persistence

Vibe-coding has no persistent state. Each session starts from zero. The AI does not remember what was built yesterday. Context is lost between sessions. This is why vibe-coded projects degrade over time: each session introduces drift because the AI does not know what was decided before.

The Open Method includes the Superagent Operating Model: entities as data, automations as cron, skills as reusable operations, memory and identity as persistence. The agent holds context between sessions. Every session opens with "what did we decide last time?" and the answer is there. Every session closes with "what was built, what was decided, what is still open." The context is permanent. Vibe-coding has no equivalent because persistence is an architecture, not a prompt.

### 5. IP Protection

Vibe-coding produces output that cannot be protected. You cannot file a utility model on an unstructured prompt output because the output is not reproducible and the methodology is not defined. There is no method to protect. There is only a conversation with an AI.

The Open Method is a defined methodology. 7 Czech utility models have been filed on the specific implementations. The method is open (MIT). The implementations are proprietary. The

