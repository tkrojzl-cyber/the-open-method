# Prompt 24: Security Audit

**Stage:** 2 - Verification
**Position:** 24 of 47
**Version:** 1.0
**Estimated time:** 45-90 minutes
**Required tools:** Terminal, bundle inspection, automated security scanner if available
**Depends on:** 23
**Produces:** /docs/audits/security.md

---

## Purpose

This prompt runs a full security audit of the product. It exists at position 24 because security vulnerabilities are the most damaging finding and must be checked before the ship decision.

---

## Input Contract

The running product. The JS bundle. All Stage 1 artifacts.

---

## Instructions for the Agent

1. Check input validation on every form and API endpoint.
2. Check CORS configuration.
3. Check Row-Level Security (RLS) is enabled on entities containing user data.
4. Check rate limiting on API endpoints.
5. Grep the bundle for exposed secrets, API keys, or credentials.
6. Check authentication flows for session management issues.
7. Check for XSS vectors (dangerouslySetInnerHTML, unescaped user input).
8. Write results to /docs/audits/security.md.

---

## Negative Constraints

- Do not pass any exposed secret in the bundle.
- Do not pass any form without input validation.
- Do not pass any API endpoint without rate limiting if it accepts user input.
- Do not pass any XSS vector.

---

## Output Contract

A file at /docs/audits/security.md containing: security checklist with results, vulnerability list (if any), overall result.

---

## Acceptance Criteria

PASS when:
- All inputs validated.
- CORS configured correctly.
- RLS enabled where needed.
- No exposed secrets.
- No XSS vectors.

FAIL when:
- Any exposed secret.
- Any unvalidated input.
- Any XSS vector.
- RLS missing on user data entities.

BLOCKED when:
- Product is not running.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-23 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-24.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/audits/security.md. Record in verification artifact.

---

## DACV Trigger

DACV trigger: Yes. Question type: C (Contradict). Ask second AI to identify any security vulnerability the first AI missed, focusing on injection, authentication, and data exposure.

---

## Security and Privacy Check

Security check is the primary check for this prompt. All security criteria above must pass.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 25 consumes /docs/audits/security.md. Expects: security audit results.

---

## Human Checkpoint

No human checkpoint.
