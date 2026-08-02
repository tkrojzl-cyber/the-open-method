# Prompt 26: Doomsday Recovery Document

**Stage:** 3 - Sovereignty
**Position:** 26 of 47
**Version:** 1.0
**Estimated time:** 60-120 minutes
**Required tools:** Text editor, terminal
**Depends on:** 25
**Produces:** /docs/sovereignty/doomsday-recovery.md

---

## Purpose

This prompt creates the document that enables full recovery if everything is lost. It exists at position 26 as the first sovereignty prompt because recovery is the foundation of operational resilience.

---

## Input Contract

The shipped product from Stage 2. All Stage 1 and Stage 2 artifacts.

---

## Instructions for the Agent

1. List every critical asset: source code, data, configuration, credentials, documentation.
2. For each asset, record its location, backup location, and recovery method.
3. Write step-by-step recovery instructions for a scenario where the primary environment is lost.
4. Identify the minimum set of assets needed to restore basic operation.
5. Record the estimated recovery time for each scenario.
6. Test the recovery by restoring one critical asset from backup.
7. Write the doomsday recovery document to /docs/sovereignty/doomsday-recovery.md.

---

## Negative Constraints

- Do not create a recovery document that depends on assets that are not backed up.
- Do not skip the restore test.
- Do not list a credential without noting where its backup copy is stored.

---

## Output Contract

A file at /docs/sovereignty/doomsday-recovery.md containing: critical asset table, recovery steps, minimum restore set, restore test result, SHA-256 hash.

---

## Acceptance Criteria

PASS when:
- All critical assets listed with backup locations.
- Recovery steps are concrete and testable.
- Restore test passed.

FAIL when:
- Any critical asset lacks a backup location.
- Recovery steps are vague.
- Restore test failed.

BLOCKED when:
- No backup system is in place.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-25 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-26.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sovereignty/doomsday-recovery.md. Record in verification artifact. This is the first entry in the Stage 3 hash chain.

---

## DACV Trigger

No DACV trigger. Recovery is verified by the restore test.

---

## Security and Privacy Check

Security check applies. Confirm no actual secret values appear in the recovery document. Only locations and methods, not credentials.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 27 consumes /docs/sovereignty/doomsday-recovery.md. Expects: recovery document with tested restore.

---

## Human Checkpoint

Human checkpoint: Yes. The human must confirm the recovery document is adequate and the restore test was genuine.
