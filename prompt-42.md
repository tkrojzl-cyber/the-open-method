# Prompt 42: Error Severity Classification

**Stage:** 3 - Sovereignty
**Position:** 42 of 47
**Version:** 1.0
**Estimated time:** 30-60 minutes
**Required tools:** Text editor, codebase
**Depends on:** 41
**Produces:** /docs/sovereignty/error-classification.md

---

## Purpose

This prompt classifies every error in the product by severity. It exists at position 42 because error handling without classification leads to either over-alerting or under-alerting.

---

## Input Contract

All failure cases from Prompts 05, 06, and 08. The security audit from Prompt 24.

---

## Instructions for the Agent

1. List every error case identified in the build.
2. Classify each as: Severity 1 (blocking, product unusable), Severity 2 (degraded, reduced function), Severity 3 (cosmetic, minor issue).
3. For each Severity 1 and 2, define the user-facing message and the logging behavior.
4. Confirm no Severity 1 errors are silently swallowed.
5. Confirm all Severity 2 errors are logged.
6. Write the classification to /docs/sovereignty/error-classification.md.

---

## Negative Constraints

- Do not leave any Severity 1 error unhandled.
- Do not classify a blocking error as Severity 3.
- Do not omit the user-facing message for any Severity 1 or 2 error.

---

## Output Contract

A file at /docs/sovereignty/error-classification.md containing: error table with severity, message, logging behavior, overall result.

---

## Acceptance Criteria

PASS when:
- All errors classified.
- All Severity 1 handled with user-facing message.
- All Severity 2 logged.

FAIL when:
- Unclassified errors.
- Severity 1 swallowed silently.
- Severity 2 not logged.

BLOCKED when:
- No error cases identified (unlikely, but state if true).

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-41 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-42.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sovereignty/error-classification.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. Error classification is verified by direct review.

---

## Security and Privacy Check

No security check.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 43 consumes /docs/sovereignty/error-classification.md. Expects: error classification with severity levels.

---

## Human Checkpoint

No human checkpoint.
