# Stage Gates Specification v1.3

**Updated:** 2026-08-02
**Status:** Final polish pass (P1-P5)
**Changes from v1.2:** P2 (chain integrity check added to Gate 1 and Gate 2 — was only in Gate 3). P1 (Prompt 32 human checkpoint confirmed). Everything else unchanged from v1.2.

---

## Purpose

Stage gates are verification barriers between stages. They are not prompts. They are not optional. A stage gate must pass before the next stage's prompts execute. If a gate fails, the stage is re-executed from the failed prompt.

---

## Gate 1: Stage 1 to Stage 2

**Location:** After Prompt 10 (Polish), before Prompt 11 (Route Audit)
**Produces:** /docs/stage-1-status.md containing `gate_1_hash`

### Pass Criteria (ALL must be true)

1. All 10 verification artifacts exist at /docs/verification/prompt-01.md through prompt-10.md and show status PASS.
2. The hash chain within Stage 1 is intact: recomputing prevHash for prompts 02-10 (SHA-256 of each preceding verification file) produces no breaks. (P2 fix — chain integrity now checked at every gate, not just Gate 3.)
3. /docs/stage-1-status.md does not list any blocking issues.
4. The product runs: the run command from /docs/architecture.md completes with exit code 0.
5. README.md is current: it describes the product as it exists now, not as it was planned.
6. /docs/data-model.md has at least one test record per entity confirmed working.

### Gate Hash

Stage 1 prompts DO produce artifact_hash values. Without these, Gate 1's hash is uncomputable.

```
gate_1_hash = SHA-256( byte_concat( artifact_hash_01, artifact_hash_02, ..., artifact_hash_10 ) )
```

`byte_concat` = concatenate the raw UTF-8 bytes of each artifact_hash string (64-character hex string) in order, then hash the resulting byte sequence with SHA-256.

Recorded in /docs/stage-1-status.md (field: `gate_1_hash`). Becomes the `prevHash` for Prompt 11's verification artifact.

IMPORTANT: Prompt 11's prevHash is gate_1_hash, NOT SHA-256 of prompt-10's verification file.

### Fail Protocol

On FAIL:
1. If chain integrity check (criterion 2) fails: identify the broken link, revert to `baseline_commit` at that prompt, re-execute.
2. If any verification artifact shows FAIL or BLOCKED: revert to that prompt's `baseline_commit`, re-execute.
3. Maximum 3 re-execution attempts per failed prompt.
4. If still failing after 3 attempts: escalate to human. Do not proceed to Stage 2.

---

## Gate 2: Stage 2 to Stage 3

**Location:** After Prompt 25 (Ship Decision), before Prompt 26 (Doomsday Recovery)
**Produces:** /docs/stage-2-status.md containing `gate_2_hash`

### Pass Criteria (ALL must be true)

1. All 15 verification artifacts (prompt-11.md through prompt-25.md) exist and show status PASS.
2. The hash chain within Stage 2 is intact: recomputing prevHash for prompts 12-25 (SHA-256 of each preceding verification file) produces no breaks. (P2 fix — chain integrity now checked at Gate 2, not just Gate 3.)
3. /docs/sweeps/full-report.md shows zero CRITICAL and zero HIGH findings. (MEDIUM and LOW are permitted.)
4. /docs/ship-decision.md shows status SHIP.
5. The product still runs: re-run the primary flow from Prompt 05 and confirm it works.
6. CEC checks all pass: /docs/cec/drift-check.md, /docs/cec/contradiction-scan.md, AND /docs/cec/scope-check.md all show no blocking findings.

### Gate Hash

```
gate_2_hash = SHA-256( byte_concat( artifact_hash_11, artifact_hash_12, ..., artifact_hash_25 ) )
```

Same `byte_concat` definition. Recorded in /docs/stage-2-status.md (field: `gate_2_hash`). Becomes the `prevHash` for Prompt 26.

IMPORTANT: Prompt 26's prevHash is gate_2_hash, NOT SHA-256 of prompt-25's verification file.

### Fail Protocol

On FAIL:
1. If chain integrity check (criterion 2) fails: identify the broken link, revert to `baseline_commit` at that prompt, re-execute.
2. If the failure is in the CEC checks (prompts 20-22), re-run the specific CEC prompt.
3. If full-report.md shows unresolved CRITICAL or HIGH, identify the source prompt and re-execute.
4. Maximum 3 re-execution attempts per failed prompt.
5. If still failing after 3 attempts: escalate to human. Do not proceed to Stage 3.

---

## Gate 3: Stage 3 Completion

**Location:** After Prompt 47 (Final Sovereignty Seal)
**Produces:** /docs/sovereignty/final-seal.md containing `gate_3_hash`

### Pass Criteria (ALL must be true)

1. All 22 verification artifacts (prompt-26.md through prompt-47.md) exist and show status PASS.
2. The hash chain is intact across all three stages: recomputing prevHash for every prompt produces no breaks. For prompts 27-47, recompute SHA-256 of the preceding verification file. For Prompt 26 specifically, recompute gate_2_hash from Stage 2 artifact hashes. (Unchanged from v1.2 — Gate 3 already had this.)
3. /docs/sovereignty/doomsday-recovery.md exists and is complete.
4. Legal documents exist: /docs/legal/terms-of-service.md, /docs/legal/privacy-policy.md, /docs/legal/ip-declaration.md.
5. The public verification API (if implemented in Prompt 29) returns correct verification results.
6. Accessibility audit (/docs/sweeps/accessibility-audit.md) shows no WCAG 2.1 AA failures.
7. The product is deployable: the run command works, the build succeeds, no blocking errors.

### Gate Hash

```
gate_3_hash = SHA-256( byte_concat( artifact_hash_26, artifact_hash_27, ..., artifact_hash_47 ) )
```

Product's final provenance seal. Recorded in /docs/sovereignty/final-seal.md (field: `gate_3_hash`).

### Fail Protocol

On FAIL:
1. If the hash chain is broken (criterion 2): re-execute the prompt where the break occurs.
2. If any verification artifact shows FAIL or BLOCKED: revert to `baseline_commit` and re-execute.
3. Maximum 3 re-execution attempts per failed prompt.
4. If still failing after 3 attempts: escalate to human. Product is not sovereign. Do not deploy.

---

## Chain Verification at Stage Boundaries (unchanged from v1.2)

The standard chain verification procedure is: recompute SHA-256 of the previous prompt's verification file and confirm it matches the `prevHash` field. This works for all prompts EXCEPT at stage boundaries:

- **Prompt 11:** prevHash = gate_1_hash. To verify: recompute gate_1_hash = SHA-256(byte_concat(artifact_hash_01 through artifact_hash_10)). Do NOT hash prompt-10's verification file.
- **Prompt 26:** prevHash = gate_2_hash. To verify: recompute gate_2_hash = SHA-256(byte_concat(artifact_hash_11 through artifact_hash_25)). Do NOT hash prompt-25's verification file.

Worked example for Gate 1:

```
Given:
  artifact_hash_01 = "a1b2c3..." (64 hex chars, UTF-8 encoded = 64 bytes)
  artifact_hash_02 = "d4e5f6..." (64 hex chars)
  ...
  artifact_hash_10 = "z9y8x7..." (64 hex chars)

gate_1_input = "a1b2c3..." + "d4e5f6..." + ... + "z9y8x7..."  (640 bytes)
gate_1_hash  = SHA-256(gate_1_input)                           (64 hex chars)

Prompt 11's verification file must contain:
  prevHash: [gate_1_hash value]

To verify: recompute SHA-256(byte_concat(artifact_hash_01, ..., artifact_hash_10))
and compare to the prevHash field in prompt-11's verification file.
```

---

## Gate Failure Protocol (unchanged from v1.2)

1. When a prompt FAILS, revert to the `baseline_commit` in that prompt's verification artifact.
2. Re-execute the prompt from instruction 1.
3. Maximum 3 re-execution attempts.
4. If still failing after 3 attempts: set verification artifact status to BLOCKED and escalate to human.
5. A BLOCKED prompt cannot be skipped. The human must either resolve the block or accept the product is incomplete.
6. No stage gate passes while any prompt in that stage is BLOCKED.

This protocol is embedded in every prompt file's Acceptance Criteria section.
