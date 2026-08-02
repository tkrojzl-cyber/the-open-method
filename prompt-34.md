# Prompt 34: Knowledge Transfer - Documentation

**Stage:** 3 - Sovereignty
**Position:** 34 of 47
**Version:** 1.0
**Estimated time:** 60-120 minutes
**Required tools:** Text editor
**Depends on:** 33
**Produces:** /docs/knowledge/documentation.md

---

## Purpose

This prompt creates documentation that allows someone unfamiliar with the product to run and maintain it. It exists at position 34 because knowledge transfer is what makes the product sovereign.

---

## Input Contract

All Stage 1 and Stage 2 artifacts. The product codebase.

---

## Instructions for the Agent

1. Write a technical overview: what the product is, how it works, what it depends on.
2. Write setup instructions: environment requirements, installation steps, configuration.
3. Write run instructions: how to start, stop, and verify the product is running.
4. Write troubleshooting: common issues and their solutions.
5. Write maintenance: routine tasks, update procedures, monitoring.
6. Give the documentation to someone unfamiliar with the product and have them run it.
7. Record whether they succeeded without additional help.
8. Write the documentation to /docs/knowledge/documentation.md.

---

## Negative Constraints

- Do not write documentation that assumes the reader has context from the original build.
- Do not mark the documentation as complete if the test reader needed additional help.
- Do not omit troubleshooting for known issues.

---

## Output Contract

A file at /docs/knowledge/documentation.md containing: technical overview, setup, run, troubleshooting, maintenance, test reader result.

---

## Acceptance Criteria

PASS when:
- Documentation covers all required sections.
- Test reader ran the product with no additional help.

FAIL when:
- Documentation missing sections.
- Test reader needed additional help.

BLOCKED when:
- No test reader available.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-33 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-34.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/knowledge/documentation.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. Documentation is verified by the test reader.

---

## Security and Privacy Check

Security check applies. Confirm no secrets appear in the documentation.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 35 consumes /docs/knowledge/documentation.md. Expects: complete documentation with test reader result.

---

## Human Checkpoint

No human checkpoint.
