# Prompt 21: Contradiction Scan

**Stage:** 2 - Verification
**Position:** 21 of 47
**Version:** 1.0
**Estimated time:** 30-60 minutes
**Required tools:** Text editor, all Stage 1 and Stage 2 artifacts
**Depends on:** 20
**Produces:** /docs/cec/contradiction-scan.md

---

## Purpose

This prompt checks whether any two decisions in the build contradict each other. It exists at position 21 because contradictions are invisible during building and only detectable by cross-referencing all decisions.

---

## Input Contract

All Stage 1 artifacts. The drift check from Prompt 20.

---

## Instructions for the Agent

1. List every decision recorded in /docs/architecture.md, /docs/data-model.md, /docs/flows/, and /docs/integrations.md.
2. For each pair of decisions, check if they conflict (one enables what the other prohibits).
3. Check the bilingual decision against the UI implementation for consistency.
4. Check the data model against the flows for field usage consistency.
5. Record any contradiction pairs with both decisions identified.
6. Write results to /docs/cec/contradiction-scan.md.

---

## Negative Constraints

- Do not pass if any two decisions conflict.
- Do not skip cross-referencing architecture decisions against flow implementations.
- Do not mark clean if the drift check found drift that was not investigated for contradictions.

---

## Output Contract

A file at /docs/cec/contradiction-scan.md containing: contradiction pairs (if any), cross-reference results, overall result.

---

## Acceptance Criteria

PASS when:
- No contradictions found.
- All decisions are consistent with each other.

FAIL when:
- Any two decisions conflict.
- Architecture and implementation are inconsistent.

BLOCKED when:
- Any Stage 1 artifact is missing.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-20 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-21.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/cec/contradiction-scan.md. Record in verification artifact.

---

## DACV Trigger

DACV trigger: Yes. Question type: C (Contradict). Ask second AI to identify any pair of decisions in the build that contradict each other. If the second AI finds a contradiction the first AI missed, that is a contradiction finding.

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

Prompt 22 consumes /docs/cec/contradiction-scan.md. Expects: contradiction results.

---

## Human Checkpoint

No human checkpoint.
