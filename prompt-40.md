# Prompt 40: Dependency Risk Matrix

**Stage:** 3 - Sovereignty
**Position:** 40 of 47
**Version:** 1.0
**Estimated time:** 30-60 minutes
**Required tools:** Text editor, terminal
**Depends on:** 39
**Produces:** /docs/sovereignty/dependency-matrix.md

---

## Purpose

This prompt maps every external dependency and its risk. It exists at position 40 because dependency failures are a common cause of outages and must be understood before they happen.

---

## Input Contract

The integration list from /docs/integrations.md. The architecture from /docs/architecture.md.

---

## Instructions for the Agent

1. List every external dependency: APIs, libraries, hosting, databases, CDN.
2. For each dependency, assess: blast radius if it fails, replacement path, vendor lock-in risk.
3. Classify each: critical (product breaks), degraded (reduced function), cosmetic (minor impact).
4. Identify any dependency with no replacement path.
5. Write the dependency risk matrix to /docs/sovereignty/dependency-matrix.md.

---

## Negative Constraints

- Do not omit any external dependency.
- Do not classify a critical dependency as degraded.
- Do not leave the replacement path blank for any dependency.

---

## Output Contract

A file at /docs/sovereignty/dependency-matrix.md containing: dependency table with blast radius, replacement path, classification, overall risk assessment.

---

## Acceptance Criteria

PASS when:
- All dependencies listed.
- Each has a blast radius classification.
- Each has a replacement path (or documented reason for none).

FAIL when:
- Dependencies missing.
- Blast radius not classified.
- Replacement path blank.

BLOCKED when:
- /docs/integrations.md is missing.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-39 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-40.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sovereignty/dependency-matrix.md. Record in verification artifact and hash chain.

---

## DACV Trigger

DACV trigger: Yes. Question type: B (Extend). Ask second AI to identify any dependency risk the first AI missed, especially around vendor lock-in and silent failure modes.

---

## Security and Privacy Check

Security check applies. Confirm no dependency has access to data it does not need.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 41 consumes /docs/sovereignty/dependency-matrix.md. Expects: dependency risk assessment.

---

## Human Checkpoint

No human checkpoint.
