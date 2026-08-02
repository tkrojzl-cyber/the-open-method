# Prompt 37: SEO and Meta Audit

**Stage:** 3 - Sovereignty
**Position:** 37 of 47
**Version:** 1.0
**Estimated time:** 30-60 minutes
**Required tools:** Browser, bundle inspection
**Depends on:** 36
**Produces:** /docs/sovereignty/seo-meta.md

---

## Purpose

This prompt verifies SEO metadata is complete and correct. It exists at position 37 because search visibility is how the product is found without paid distribution.

---

## Input Contract

The running product. The JS bundle.

---

## Instructions for the Agent

1. Check every page has a unique title tag.
2. Check every page has a meta description under 160 characters.
3. Check OG image tags point to real, accessible image URLs.
4. Check canonical URLs are set if duplicate content exists.
5. Check robots.txt exists and is correct.
6. Check sitemap.xml exists if applicable.
7. Check structured data (JSON-LD) where applicable.
8. Write results to /docs/sovereignty/seo-meta.md.

---

## Negative Constraints

- Do not pass any page with a duplicate or missing title.
- Do not pass any OG image that returns 404.
- Do not pass a missing robots.txt.

---

## Output Contract

A file at /docs/sovereignty/seo-meta.md containing: per-page meta audit, OG image check, robots.txt check, issues list, overall result.

---

## Acceptance Criteria

PASS when:
- All pages have unique titles.
- All pages have meta descriptions under 160 chars.
- All OG images return 200.
- robots.txt exists.

FAIL when:
- Any page missing or duplicate title.
- Any meta description over 160 chars.
- Any OG image 404.
- robots.txt missing.

BLOCKED when:
- Product is not deployed.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-36 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-37.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sovereignty/seo-meta.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. SEO is verified by direct inspection.

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

Prompt 38 consumes /docs/sovereignty/seo-meta.md. Expects: SEO audit results.

---

## Human Checkpoint

No human checkpoint.
