# Prompt 04: Feature Layer 3 and Security

**Stage:** 1 - Build
**Position:** 4 of 47
**Version:** 1.3
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, Base44 builder or equivalent
**Depends on:** 03
**Produces:** /docs/security-model.md

---

## Purpose

Build the final 2-3 feature pages and enforce the security model. This completes the feature set from the core actions list. Security is not optional: RLS, CORS, input validation, and trust boundaries are applied to every entity and every endpoint.

---

## Input Contract

The architecture from Prompt 02 (/docs/architecture.md). The entity schemas from Prompt 01. The pages built in Prompts 02 and 03. The design system from /docs/design-system.md.

---

## Instructions for the Agent

1. Build the remaining 2-3 feature pages from the core actions list.
2. Apply Row-Level Security (RLS) to every entity. Non-admin users see only their own records. Admins see all.
3. Configure CORS. Only allow the product's own domain.
4. Add input validation to every form and API endpoint. No unvalidated input reaches the database.
5. Define trust boundaries: which data is public, which is user-private, which is admin-only. Document in /docs/security-model.md.
6. Check for PII in entities. Flag any field that stores personally identifiable information. Ensure RLS covers it.
7. The run command must still work.

---

## Acceptance Criteria

- [ ] 2-3 remaining feature pages are built with full CRUD.
- [ ] RLS is enabled on all entities with user-scoped data.
- [ ] CORS is configured for the product domain only.
- [ ] Input validation is present on all forms and endpoints.
- [ ] /docs/security-model.md exists with trust boundary definitions.
- [ ] PII fields are identified and protected.
- [ ] The run command completes with exit code 0.

On FAIL: revert to the git commit recorded as baseline_commit and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.

---

## Provenance Checkpoint

**Stage 1:** Hash the primary output artifact. Record in `artifact_hash`. Do NOT publish. Computed for chain construction only.

- **Primary artifact hashed:** /docs/security-model.md
- **Artifact hash:** [SHA-256 of /docs/security-model.md. Compute at execution time.]
- **Previous verification hash (prevHash):** SHA-256 of the prompt-03 verification file contents.
- **Baseline commit:** [git commit hash at the start of this prompt's execution]
