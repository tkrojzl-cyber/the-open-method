# Prompt 22: Scope Creep Check

**Stage:** 2 - Verification
**Position:** 22 of 47
**Version:** 1.0
**Estimated time:** 20-30 minutes
**Required tools:** Text editor, all Stage 1 artifacts
**Depends on:** 21
**Produces:** /docs/cec/scope-check.md

---

## Purpose

This prompt verifies no features were added beyond the core actions in the discovery brief. It exists at position 22 as the final CEC check, confirming the build stayed within scope.

---

## Input Contract

The discovery brief. All implemented features from Stage 1.

---

## Instructions for the Agent

1. List every implemented feature from Prompts 05, 06, 07, and 08.
2. For each feature, map it to a core action in /docs/discovery-brief.md.
3. Flag any feature that does not map to a core action.
4. Check the extension points from Prompt 09 for features that were built instead of deferred.
5. Write results to /docs/cec/scope-check.md.

---

## Negative Constraints

- Do not pass any feature that does not map to a core action.
- Do not mark clean if extension points were built instead of documented.

---

## Output Contract

A file at /docs/cec/scope-check.md containing: feature-to-core-action mapping table, scope creep findings, overall result.

---

## Acceptance Criteria

PASS when:
- Every feature maps to a core action.
- No features built from the extension points list.

FAIL when:
- Any feature does not map to a core action.
- Extension point features were built instead of deferred.

BLOCKED when:
- /docs/discovery-brief.md is missing.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-21 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-22.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/cec/scope-check.md. Record in verification artifact.

---

## DACV Trigger

No DACV trigger. Scope is verified by direct comparison.

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

Prompt 23 consumes /docs/cec/scope-check.md. Expects: scope check results. If scope creep is detected, Prompt 23 records the extra features for the performance audit.

---

## Human Checkpoint

No human checkpoint.
