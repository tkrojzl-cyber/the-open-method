# Prompt 29: Legal Shield - Terms of Service

**Stage:** 3 - Sovereignty
**Position:** 29 of 47
**Version:** 1.0
**Estimated time:** 60-120 minutes
**Required tools:** Text editor, legal review (human)
**Depends on:** 28
**Produces:** /docs/legal/terms.md

---

## Purpose

This prompt creates the terms of service that protect the product owner from legal liability. It exists at position 29 because legal protection is a sovereignty requirement.

---

## Input Contract

The product's features, data handling, and integration list from Stage 1.

---

## Instructions for the Agent

1. Draft terms of service covering: usage terms, limitations of liability, data handling, dispute resolution.
2. Reference the actual product features and integrations, not generic template language.
3. Include the jurisdiction applicable to the product owner.
4. Include a clause for the hash chain and verification system if applicable.
5. Present the draft to the human for legal review.
6. Record the lawyer review status.
7. Write the terms to /docs/legal/terms.md.

---

## Negative Constraints

- Do not use generic template terms that do not reference the actual product.
- Do not mark the terms as legally reviewed without a lawyer's confirmation.
- Do not omit the limitation of liability clause.

---

## Output Contract

A file at /docs/legal/terms.md containing: terms of service, jurisdiction, lawyer review status.

---

## Acceptance Criteria

PASS when:
- Terms exist and reference actual product features.
- Jurisdiction is specified.
- Lawyer review status is recorded.

FAIL when:
- Terms are generic.
- Jurisdiction missing.
- No lawyer review status recorded.

BLOCKED when:
- Lawyer not available for review.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-28 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-29.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/legal/terms.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. Legal review is a human checkpoint, not AI verification.

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

Prompt 30 consumes /docs/legal/terms.md. Expects: terms with lawyer review status.

---

## Human Checkpoint

Human checkpoint: Yes. The human must have the terms reviewed by a lawyer before the product goes live.
