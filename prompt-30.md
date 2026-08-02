# Prompt 30: Legal Shield - Privacy Policy

**Stage:** 3 - Sovereignty
**Position:** 30 of 47
**Version:** 1.0
**Estimated time:** 60-120 minutes
**Required tools:** Text editor, legal review (human)
**Depends on:** 29
**Produces:** /docs/legal/privacy.md

---

## Purpose

This prompt creates the privacy policy that protects user data and complies with applicable regulations. It exists at position 30 because privacy compliance is a legal requirement and a trust signal.

---

## Input Contract

The data model from Prompt 04. The integration list from Prompt 08.

---

## Instructions for the Agent

1. Draft privacy policy covering: what data is collected, how it is stored, how it is used, third-party sharing, user rights, data retention.
2. Reference the actual entities from /docs/data-model.md, not generic data categories.
3. Reference the actual integrations from /docs/integrations.md that process user data.
4. Include GDPR compliance if EU users are possible.
5. Present the draft to the human for legal review.
6. Write the privacy policy to /docs/legal/privacy.md.

---

## Negative Constraints

- Do not use a generic privacy policy template.
- Do not list data categories that do not exist in the product.
- Do not omit third-party data sharing if integrations send user data externally.

---

## Output Contract

A file at /docs/legal/privacy.md containing: privacy policy with actual data references, GDPR compliance, lawyer review status.

---

## Acceptance Criteria

PASS when:
- Privacy policy references actual entities and integrations.
- GDPR compliance addressed.
- Lawyer review status recorded.

FAIL when:
- Generic template used.
- Actual data handling not referenced.
- GDPR not addressed for EU-accessible products.

BLOCKED when:
- Lawyer not available for review.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-29 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-30.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/legal/privacy.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. Legal review is a human checkpoint.

---

## Security and Privacy Check

Security check applies. Confirm the privacy policy matches the actual data handling verified in Prompt 24's security audit.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 31 consumes /docs/legal/privacy.md. Expects: privacy policy with review status.

---

## Human Checkpoint

Human checkpoint: Yes. The human must have the privacy policy reviewed by a lawyer.
