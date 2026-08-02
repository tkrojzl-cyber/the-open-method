# Prompt 20: CEC Drift Check

**Stage:** 2 - Verification
**Position:** 20 of 47
**Version:** 1.0
**Estimated time:** 30-60 minutes
**Required tools:** Text editor, Stage 1 artifacts
**Depends on:** 19
**Produces:** /docs/cec/drift-check.md

---

## Purpose

This prompt checks whether any decision made during the build drifted from the north star defined in Prompt 01. It exists at position 20 because drift is invisible during building and only detectable by comparing the final state to the original brief.

---

## Input Contract

The discovery brief at /docs/discovery-brief.md. The architecture at /docs/architecture.md. The full sweep report from Prompt 19.

---

## Instructions for the Agent

1. List every architectural decision made in /docs/architecture.md.
2. For each decision, check it traces to a core action or non-goal in /docs/discovery-brief.md.
3. List every feature implemented in Prompts 05-08.
4. For each feature, check it maps to a core action in /docs/discovery-brief.md.
5. Check the sweep report for any items that suggest scope beyond the discovery brief.
6. Record any drifted decisions with their traceability gap.
7. Write results to /docs/cec/drift-check.md.

---

## Negative Constraints

- Do not pass a decision that does not trace to the discovery brief.
- Do not mark clean if any sweep RED item suggests scope drift.
- Do not skip checking architecture decisions against the discovery brief.

---

## Output Contract

A file at /docs/cec/drift-check.md containing: decision traceability table, drift findings, overall result (clean/drift detected).

---

## Acceptance Criteria

PASS when:
- Every decision traces to a core action or non-goal.
- No features exist outside the core actions list.
- No sweep items suggest scope drift.

FAIL when:
- Any decision does not trace to the discovery brief.
- Any feature exists outside core actions.
- Sweep items suggest scope drift.

BLOCKED when:
- /docs/discovery-brief.md is missing or not confirmed.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-19 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-20.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/cec/drift-check.md. Record in verification artifact.

---

## DACV Trigger

DACV trigger: Yes. Question type: C (Contradict). Ask second AI to identify any decision in the build that contradicts the discovery brief's non-goals. If the second AI finds a contradiction the first AI missed, that is a drift finding.

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

Prompt 21 consumes /docs/cec/drift-check.md. Expects: drift check results. If drift is detected, Prompt 21 checks for contradictions that may have caused the drift.

---

## Human Checkpoint

No human checkpoint.
