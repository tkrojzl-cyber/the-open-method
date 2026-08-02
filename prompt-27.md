# Prompt 27: Hash Chain Implementation

**Stage:** 3 - Sovereignty
**Position:** 27 of 47
**Version:** 1.0
**Estimated time:** 60-120 minutes
**Required tools:** Terminal, code editor, SHA-256 library or built-in
**Depends on:** 26
**Produces:** /docs/sovereignty/hash-chain.md; hash chain implementation in codebase

---

## Purpose

This prompt implements a SHA-256 hash chain that provides tamper-evident provenance for all build artifacts. It exists at position 27 because the hash chain is the cryptographic foundation of sovereignty.

---

## Input Contract

The shipped product from Stage 2. The doomsday recovery document from Prompt 26.

---

## Instructions for the Agent

1. Define the hash chain specification: SHA-256, entry format, genesis value.
2. Implement the hash chain: each entry hashes the current artifact data plus the previous entry's hash.
3. Set the genesis entry with a hardcoded initial hash (GENESIS).
4. Create the first chain entry by hashing the Stage 2 ship decision from /docs/ship-decision.md.
5. Create subsequent entries for each Stage 3 artifact as it is produced.
6. Verify the chain is intact by recomputing all hashes from genesis to the latest entry.
7. Write the chain specification and current state to /docs/sovereignty/hash-chain.md.

---

## Negative Constraints

- Do not use a weak hash algorithm. SHA-256 minimum.
- Do not store the previous hash in a way that can be modified without detection.
- Do not skip the chain integrity verification.
- Do not include mutable state (live variables) in the hash input.

---

## Output Contract

A file at /docs/sovereignty/hash-chain.md containing: chain specification, entry table with hashes, integrity verification result. Hash chain implementation in the codebase.

---

## Acceptance Criteria

PASS when:
- Hash chain implemented with SHA-256.
- Genesis entry exists.
- Chain integrity verified.
- First entry hashes the ship decision.

FAIL when:
- Chain is broken at any point.
- No genesis entry.
- Mutable state in hash input.
- Weak hash algorithm.

BLOCKED when:
- No SHA-256 library available.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-26 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-27.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

The hash chain IS the provenance mechanism. The chain's own hash is recorded in the verification artifact.

---

## DACV Trigger

DACV trigger: Yes. Question type: A (Verify). Ask second AI to verify the hash chain implementation is cryptographically correct: SHA-256 is used, each entry includes the previous hash, genesis is hardcoded, no mutable state in the hash input.

---

## Security and Privacy Check

Security check applies. Confirm the hash chain implementation does not introduce any data exposure or injection vectors.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 28 consumes /docs/sovereignty/hash-chain.md. Expects: implemented, verified hash chain.

---

## Human Checkpoint

No human checkpoint.
