# Verification Matrix v1.3

**Updated:** 2026-08-02
**Status:** Final polish pass (P1-P5)
**Changes from v1.2:** P4 (Performance category description clarified). P1, P2, P3, P5 unchanged from v1.2.

---

## §1. Severity System (SINGLE AUTHORITATIVE COPY)

| Level | Definition | Ship blocker? |
|-------|-----------|---------------|
| CRITICAL | Revenue-blocking, data-loss, security vulnerability | YES |
| HIGH | Trust-damaging, broken user flow, wrong content, untraceable artifact | YES |
| MEDIUM | Polish gap, inconsistency, non-blocking | NO |
| LOW | Cosmetic, preference | NO |

Rule: A CRITICAL or HIGH finding on any check FAILS the prompt. MEDIUM and LOW are recorded but do not block.

### Report color vocabulary (sweep report visualization only)

| Primary level | Report color |
|--------------|-------------|
| CRITICAL | RED |
| HIGH | RED |
| MEDIUM | AMBER |
| LOW | GREEN |

### Specific rulings

- Border-radius inconsistency: MEDIUM (non-blocking). Not a FAIL condition.
- Touch target size: PASS at 44px+ (WCAG 2.1 AA minimum). FAIL under 44px. 48px recommended best practice.
- Extension point not tracing to a non-goal: HIGH (blocking). Scope violation.

---

## §2. The 10 Verification Categories (P4 fix)

| # | Category | What it checks | Relevant from | Enforced from |
|---|----------|----------------|-------------|--------------|
| 1 | Functional | Does the feature work end to end | Prompt 05 | Prompt 05 |
| 2 | Security | PII, trust boundaries, secrets, data classification | Prompt 04 | Prompt 04 |
| 3 | Accessibility | WCAG 2.1 AA, keyboard nav, screen reader, contrast | Prompt 07 | Prompt 07 |
| 4 | Mobile | 375px, 768px, 1440px viewports, touch targets, responsive | Prompt 07 | Prompt 07 |
| 5 | Performance | Load time, API response, database query time | Prompt 05 | Prompt 23 |
| 6 | Provenance | Hash chain integrity, artifact hashing, prevHash verification | Prompt 01 | Prompt 01 |
| 7 | Documentation | README, inline docs, verification artifacts written | Prompt 01 | Prompt 01 |
| 8 | Scope | Core actions only, no scope creep, non-goals respected | Prompt 01 | Prompt 01 |
| 9 | Consistency | Naming, terminology, file paths, design tokens | Prompt 10 | Prompt 10 |
| 10 | Drift | CEC drift, contradiction, scope creep checks | Prompt 20 | Prompt 20 |

"Relevant from" means the category is labeled as applicable starting at that prompt. "Enforced from" means a quantitative threshold is first checked at that prompt. For Performance: the category is relevant from Prompt 05 (a broken flow that never completes is a functional failure detectable at 05), but the quantitative thresholds (<3s load, <500ms API) are first enforced at Prompt 23. Prompts 05 and 06 should note if a flow takes an abnormally long time, but this is a functional observation, not a measured benchmark.

---

## §3. Stage 1 Checks (Prompts 01-10)

| Prompt | Categories checked | Severity enforced |
|--------|-------------------|-----------------|
| 01 | Scope, Documentation, Provenance | CRITICAL: no core actions = FAIL |
| 02 | Scope, Documentation, Provenance | CRITICAL: no stack decision = FAIL |
| 03 | Functional, Documentation, Provenance | CRITICAL: project does not start = FAIL |
| 04 | Security, Documentation, Provenance | CRITICAL: no entities = FAIL |
| 05 | Functional, Performance (observation only), Documentation, Provenance | CRITICAL: primary flow broken = FAIL |
| 06 | Functional, Performance (observation only), Documentation, Provenance | HIGH: secondary flow broken = FAIL |
| 07 | Accessibility, Mobile, Documentation, Provenance | HIGH: missing error state = FAIL |
| 08 | Security, Functional, Documentation, Provenance | CRITICAL: integration with no error handling = FAIL |
| 09 | Scope, Documentation, Provenance | HIGH: untraceable extension point = FAIL |
| 10 | Consistency, Performance (observation only), Documentation, Provenance | HIGH: flow regression = FAIL |

---

## §4. Stage 2 Checks (Prompts 11-25)

| Prompt | Categories checked | Sweep artifact | Severity enforced |
|--------|-------------------|---------------|-----------------|
| 11 | Functional, Provenance | routing.md | CRITICAL: 404 on core route = FAIL |
| 12 | Functional, Provenance | clickability.md | CRITICAL: dead CTA = FAIL |
| 13 | Security, Functional, Provenance | payments.md | CRITICAL: dead payment link = FAIL |
| 14 | Consistency, Documentation, Provenance | copy.md | HIGH: em dash in rendered text = FAIL |
| 15 | Consistency, Accessibility, Provenance | branding.md | MEDIUM: border-radius mismatch = non-blocking |
| 16 | Mobile, Accessibility, Provenance | mobile.md | HIGH: layout broken at 375px = FAIL |
| 17 | Functional, Provenance | functionality.md | CRITICAL: core flow regression = FAIL |
| 18 | Performance, Provenance | animation.md | MEDIUM: janky animation = non-blocking |
| 19 | Scope, Provenance | north-star.md | HIGH: feature contradicts north star = FAIL |
| 20 | Drift, Provenance | drift-check.md | HIGH: drift detected = FAIL |
| 21 | Drift, Provenance | contradiction-scan.md | HIGH: contradiction found = FAIL |
| 22 | Drift, Provenance | scope-check.md | HIGH: scope creep confirmed = FAIL |
| 23 | Performance, Provenance | performance.md | HIGH: load time >3s = FAIL (first quantitative enforcement) |
| 24 | All 10 | full-report.md | Aggregate of 11-23 |
| 25 | Documentation, Provenance | ship-decision.md | CRITICAL: unresolved CRITICAL/HIGH = FAIL |

---

## §5. Stage 3 Checks (Prompts 26-47)

| Prompt | Categories checked | Artifact | Severity enforced |
|--------|-------------------|---------|-----------------|
| 26 | Documentation, Provenance | doomsday-recovery.md | HIGH: incomplete recovery doc = FAIL |
| 27 | Provenance, Security | hash-chain.md + implementation | CRITICAL: chain not verifiable = FAIL |
| 28 | Provenance, Security | chain-persistence.md | CRITICAL: chain breaks on restart = FAIL |
| 29 | Provenance, Security, Functional | public-verification.md + API | CRITICAL: API returns wrong verification = FAIL |
| 30 | Security, Documentation | terms-of-service.md | HIGH: missing liability clause = FAIL |
| 31 | Security, Documentation | privacy-policy.md | HIGH: missing data handling = FAIL |
| 32 | Security, Documentation | ip-declaration.md | HIGH: missing IP claim = FAIL |
| 33 | Security, Provenance | backup-strategy.md | HIGH: no tested backup = FAIL |
| 34 | Security, Provenance | failover-plan.md | HIGH: no failover path = FAIL |
| 35 | Documentation | documentation.md | MEDIUM: incomplete docs = non-blocking |
| 36 | Documentation | onboarding.md | MEDIUM: incomplete onboarding = non-blocking |
| 37 | Accessibility | accessibility-audit.md | HIGH: WCAG 2.1 AA failure = FAIL |
| 38 | Documentation, Provenance | seo-meta.md | MEDIUM: missing meta tag = non-blocking |
| 39 | Functional, Provenance | 404-crawl.md | HIGH: unhandled 404 on linked route = FAIL |
| 40 | Performance, Provenance | load-time.md | MEDIUM: >3s load = non-blocking (already checked in 23) |
| 41 | Security, Provenance | dependency-matrix.md | HIGH: unmapped dependency = FAIL |
| 42 | Provenance, Documentation | version-control.md | MEDIUM: no commit convention = non-blocking |
| 43 | Documentation, Provenance | error-classification.md | MEDIUM: no severity system = non-blocking |
| 44 | Functional, Security | monitoring.md | MEDIUM: no alerting = non-blocking |
| 45 | Scope, Documentation | community-extensions.md | MEDIUM: no extension spec = non-blocking |
| 46 | Documentation, Provenance | bounty-board.md | MEDIUM: no bounty spec = non-blocking |
| 47 | Provenance | final-seal.md | CRITICAL: chain broken or unresolved = FAIL |

---

## §6. Provenance Chain — Authoritative Specification (unchanged from v1.2)

### Chain structure

- Prompt 01: prevHash = "GENESIS", artifact_hash = SHA-256(/docs/discovery-brief.md)
- Prompt 02: prevHash = SHA-256(prompt-01 verification file contents), artifact_hash = SHA-256(/docs/architecture.md)
- ...continuous through Prompt 10...
- Gate 1: gate_1_hash = SHA-256(byte_concat(artifact_hash_01, ..., artifact_hash_10))
- Prompt 11: prevHash = gate_1_hash (NOT SHA-256 of prompt-10's verification file)
- ...continuous through Prompt 25...
- Gate 2: gate_2_hash = SHA-256(byte_concat(artifact_hash_11, ..., artifact_hash_25))
- Prompt 26: prevHash = gate_2_hash (NOT SHA-256 of prompt-25's verification file)
- ...continuous through Prompt 47...
- Gate 3: gate_3_hash = SHA-256(byte_concat(artifact_hash_26, ..., artifact_hash_47)) = product's final provenance seal

### Chain verification procedure

1. **For all prompts EXCEPT 11 and 26:** Read prompt N's verification file. Compute SHA-256 of prompt N-1's verification file contents. Confirm it matches the `prevHash` field. If mismatch, chain is broken at prompt N.

2. **For Prompt 11:** prevHash is gate_1_hash. Recompute gate_1_hash = SHA-256(byte_concat(artifact_hash_01 through artifact_hash_10)). Confirm it matches.

3. **For Prompt 26:** prevHash is gate_2_hash. Recompute gate_2_hash = SHA-256(byte_concat(artifact_hash_11 through artifact_hash_25)). Confirm it matches.

### Definition of ||

`||` means byte concatenation. The raw bytes of each artifact_hash string (64-character hex string encoded as UTF-8) are concatenated in order, then the resulting byte sequence is hashed with SHA-256.

### Worked example

```
gate_1_input = "a1b2c3..." + "d4e5f6..." + ... + "z9y8x7..."  (640 bytes of UTF-8 hex chars)
gate_1_hash  = SHA-256(gate_1_input)                           (64 hex chars output)
```
