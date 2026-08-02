# Prompt 17: Functionality and Interactivity

**Stage:** 2 - Verification
**Position:** 17 of 47
**Version:** 1.2
**Estimated time:** 60-120 minutes
**Required tools:** Browser, manual testing
**Depends on:** 05, 06, 16
**Produces:** /docs/sweeps/functionality.md

---

## Purpose

This prompt verifies every interactive feature works end to end. It exists at position 17 as the functional regression test, confirming nothing built in Stage 1 broke during the visual and mobile audits.

---

## Input Contract

The running product. Stage 1 flow documentation from Prompts 05 and 06.

---

## Instructions for the Agent

1. Run the primary flow from /docs/flows/primary-flow.md start to finish.
2. Run every secondary flow from /docs/flows/secondary-flows.md.
3. Test every form submission and confirm the handler fires.
4. Test every interactive feature noted in Stage 1.
5. Check all loading states render (not blank flash).
6. Check all error states display (not raw undefined or [object Object]).
7. Check localStorage usage reads and writes correctly.
8. Write results to /docs/sweeps/functionality.md.

---

## Negative Constraints

- Do not pass a flow that errors on completion.
- Do not pass a form with no onSubmit handler.
- Do not pass a feature that shows raw undefined or [object Object] to the user.

---

## Output Contract

A file at /docs/sweeps/functionality.md containing: per-feature test results, issues list, overall result.

---

## Acceptance Criteria

PASS when:
- Primary flow works end to end.
- All secondary flows work.
- All forms have handlers.
- No raw undefined or [object Object] in UI.
- Loading and error states render correctly.

FAIL when:
- Any flow errors on completion.
- Any form lacks a handler.
- Raw undefined or [object Object] visible.
- Any loading state is blank flash.

BLOCKED when:
- Product is not running.
- Stage 1 flow documentation is missing.

On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
---

## Verification Artifact

A file at /docs/verification/prompt-17.md containing:

- **Prompt:** 17
- **Status:** [PASS / FAIL / BLOCKED]
- **Date:** [ISO 8601 date]
- **Agent version:** [model identifier]
- **Baseline commit:** [git commit hash at the start of this prompt's execution. Used for rollback on FAIL.]
- **Primary artifact hashed:** [path of the primary output artifact]
- **Artifact hash:** [SHA-256 of the primary output artifact. NOT the hash of this verification file.]
- **Previous verification hash (prevHash):** SHA-256 of prompt-16's verification file contents.

Acceptance criteria results (each criterion: PASS/FAIL with evidence).
Notes (findings, MEDIUM/LOW severity entries that do not block).
Chain verification: previous artifact hash recomputed, matches recorded prevHash: YES/NO.

Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sweeps/functionality.md. Record in artifact_hash. prevHash = SHA-256 of prompt-16's verification file contents.

---

## DACV Trigger

No DACV trigger. Functionality is verified by manual testing.

---

## Security and Privacy Check

Security check applies. Confirm no form submits unvalidated input.

---

## Accessibility Check

No accessibility check. Addressed in Prompt 07 and re-verified here if needed.

---

## Mobile Check

No mobile check. Addressed in Prompt 16.

---

## Inter-Prompt Contract

Prompt 18 consumes /docs/sweeps/functionality.md. Expects: functionality test results.

---

## Human Checkpoint

No human checkpoint.