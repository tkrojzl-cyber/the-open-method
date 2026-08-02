# Prompt 31: Legal Shield - IP Declaration

**Stage:** 3 - Sovereignty
**Position:** 31 of 47
**Version:** 1.0
**Estimated time:** 30-60 minutes
**Required tools:** Text editor
**Depends on:** 30
**Produces:** /docs/legal/ip-declaration.md

---

## Purpose

This prompt creates the intellectual property declaration that establishes ownership and filing status. It exists at position 31 because IP protection is a sovereignty requirement.

---

## Input Contract

The product's features and architecture from Stage 1. Any existing IP filings.

---

## Instructions for the Agent

1. List every intellectual property asset: source code, design, methodology, brand.
2. For each asset, record the ownership status and any filing numbers.
3. Record the type of IP protection: utility model, copyright, trademark.
4. Record the filing date and priority window if applicable.
5. Confirm the IP declaration matches the actual product.
6. Write the IP declaration to /docs/legal/ip-declaration.md.

---

## Negative Constraints

- Do not claim IP protection for assets that are not filed.
- Do not use the word patent if the protection is a utility model.
- Do not omit the filing date or priority window for filed IP.

---

## Output Contract

A file at /docs/legal/ip-declaration.md containing: IP asset list, ownership status, filing numbers, filing dates, priority windows.

---

## Acceptance Criteria

PASS when:
- All IP assets listed.
- Filing numbers and dates recorded.
- Correct terminology used (utility model, not patent).

FAIL when:
- IP assets missing.
- Filing information incorrect.
- Wrong terminology used.

BLOCKED when:
- No IP filings exist (state explicitly if none, the declaration still records what is owned by copyright).

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-30 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-31.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/legal/ip-declaration.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. IP declaration is verified by comparison to filing records.

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

Prompt 32 consumes /docs/legal/ip-declaration.md. Expects: IP declaration with filing status.

---

## Human Checkpoint

No human checkpoint.
