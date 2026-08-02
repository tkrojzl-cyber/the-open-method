# Prompt 28: Public Verification API

**Stage:** 3 - Sovereignty
**Position:** 28 of 47
**Version:** 1.0
**Estimated time:** 60-120 minutes
**Required tools:** Terminal, code editor, deployment platform
**Depends on:** 27
**Produces:** /docs/sovereignty/verification-api.md; deployed verification API endpoint

---

## Purpose

This prompt deploys a public API that allows anyone to verify the product's hash chain without trusting the author. It exists at position 28 because public verification is the core sovereignty claim.

---

## Input Contract

The hash chain implementation from Prompt 27.

---

## Instructions for the Agent

1. Define the API endpoint URL and HTTP method.
2. Define the request format: hash parameter or seal ID.
3. Define the response format: verified status, chain data, timestamp.
4. Implement the API endpoint that reads the hash chain and returns verification results.
5. Deploy the API to a public URL.
6. Test the API by calling it with a known hash from the chain.
7. Confirm the API returns the correct verified status and chain data.
8. Write the API documentation to /docs/sovereignty/verification-api.md.

---

## Negative Constraints

- Do not deploy an API that returns incorrect verification results.
- Do not expose the full hash chain in the API response (only the requested entry and its link).
- Do not skip the external test (call from outside the development environment).

---

## Output Contract

A file at /docs/sovereignty/verification-api.md containing: endpoint URL, method, request format, response format, test result. Deployed API endpoint.

---

## Acceptance Criteria

PASS when:
- API is deployed and publicly accessible.
- API returns correct verification results for a known hash.
- External test passes.

FAIL when:
- API is not accessible.
- API returns incorrect results.
- API exposes full chain data.

BLOCKED when:
- No deployment platform available.
- Hash chain from Prompt 27 is not working.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-27 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-28.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash the API endpoint URL and its deployed configuration. Record in verification artifact and in the hash chain.

---

## DACV Trigger

DACV trigger: Yes. Question type: A (Verify). Ask second AI to verify the API returns correct results by calling it independently with a known hash.

---

## Security and Privacy Check

Security check applies. Confirm the API does not expose secrets, does not allow injection, and has rate limiting.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 29 consumes /docs/sovereignty/verification-api.md. Expects: deployed, tested verification API.

---

## Human Checkpoint

No human checkpoint.
