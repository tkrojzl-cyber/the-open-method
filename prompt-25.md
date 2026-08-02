# Prompt 25: Ship Decision

**Stage:** 2 - Verification
**Position:** 25 of 47
**Version:** 1.0
**Estimated time:** 20-30 minutes
**Required tools:** Text editor, all Stage 2 artifacts
**Depends on:** 11-24
**Produces:** /docs/ship-decision.md

---

## Purpose

This prompt consolidates all Stage 2 verification results into a ship decision. It exists at position 25 as the Stage 2 gate, confirming the product is ready for Stage 3 sovereignty or identifying what must be fixed first.

---

## Input Contract

All 14 Stage 2 verification artifacts (Prompts 11-24). The full sweep report from Prompt 19. The CEC results from Prompts 20-22. The performance and security audits from Prompts 23-24.

---

## Instructions for the Agent

1. Check all 15 Stage 2 verification artifacts exist and show PASS.
2. Check all 10 Stage 1 verification artifacts still show PASS (no regression).
3. Check the sweep report shows no RED items.
4. Check the CEC results show no blocking contradictions or drift.
5. Record the ship decision: ship if all criteria pass, no-ship if any fail.
6. Record any conditions or caveats.
7. Confirm Gate 2 status.
8. Write results to /docs/ship-decision.md.

---

## Negative Constraints

- Do not mark ship if any verification artifact shows FAIL.
- Do not mark ship if any sweep category has RED items.
- Do not mark ship if CEC found blocking drift or contradictions.
- Do not omit conditions or caveats from the ship decision.

---

## Output Contract

A file at /docs/ship-decision.md containing: Gate 2 criteria checklist, ship decision, conditions, SHA-256 hash.

---

## Acceptance Criteria

PASS when:
- All 25 verification artifacts exist and show PASS.
- No regression in Stage 1.
- Sweep shows no RED.
- CEC shows no blocking items.
- Ship decision is ship.

FAIL when:
- Any artifact missing or showing FAIL.
- Any regression.
- Any RED items.
- Any blocking CEC items.

BLOCKED when:
- Any prior Stage 2 prompt has not produced its artifact.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-24 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-25.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/ship-decision.md. Record in verification artifact. This is the Stage 2 provenance anchor.

---

## DACV Trigger

No DACV trigger. The ship decision is verified by Gate 2 criteria, not cross-AI verification.

---

## Security and Privacy Check

No security check beyond confirming the security audit from Prompt 24 shows PASS.

---

## Accessibility Check

No accessibility check beyond confirming Prompt 07's accessibility check passed.

---

## Mobile Check

No mobile check beyond confirming Prompt 16's mobile audit passed.

---

## Inter-Prompt Contract

Prompt 26 (Stage 3, Sovereignty) consumes: all 25 verification artifacts, /docs/ship-decision.md, and the current product. Prompt 26 expects: Gate 2 passed, ship decision is ship. If Gate 2 is blocked, Prompt 26 cannot execute and Stage 3 does not begin.

---

## Human Checkpoint

Human checkpoint: Yes. The human must review the ship decision before Stage 3 begins. The human confirms the product is ready for sovereignty layers.
