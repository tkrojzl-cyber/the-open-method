# Prompt 35: Knowledge Transfer - Onboarding Guide

**Stage:** 3 - Sovereignty
**Position:** 35 of 47
**Version:** 1.0
**Estimated time:** 45-90 minutes
**Required tools:** Text editor
**Depends on:** 34
**Produces:** /docs/knowledge/onboarding.md

---

## Purpose

This prompt creates an onboarding guide that allows a new user to complete the core flow. It exists at position 35 because user sovereignty requires that the product is usable without the builder explaining it.

---

## Input Contract

The primary flow from /docs/flows/primary-flow.md. The documentation from Prompt 34.

---

## Instructions for the Agent

1. Write step-by-step onboarding for a new user: account creation, first-time setup, first core action.
2. Include screenshots or visual aids if possible.
3. Write the guide for a non-technical user, not the builder.
4. Give the guide to a new user and have them complete the core flow.
5. Record whether they succeeded without help.
6. Write the onboarding guide to /docs/knowledge/onboarding.md.

---

## Negative Constraints

- Do not write the onboarding guide for a technical audience.
- Do not mark complete if the test user needed help.
- Do not skip the first-time setup steps.

---

## Output Contract

A file at /docs/knowledge/onboarding.md containing: onboarding steps, visual aids, test user result.

---

## Acceptance Criteria

PASS when:
- Guide covers account creation through first core action.
- Test user completed the core flow without help.

FAIL when:
- Steps missing.
- Test user needed help.
- Written for wrong audience.

BLOCKED when:
- No test user available.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-34 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-35.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/knowledge/onboarding.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. Onboarding is verified by the test user.

---

## Security and Privacy Check

No security check.

---

## Accessibility Check

Accessibility check applies. Confirm the onboarding guide is accessible (readable by screen readers, available in the product's languages).

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 36 consumes /docs/knowledge/onboarding.md. Expects: tested onboarding guide.

---

## Human Checkpoint

No human checkpoint.
