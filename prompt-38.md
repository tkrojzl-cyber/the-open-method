# Prompt 38: 404 Crawl

**Stage:** 3 - Sovereignty
**Position:** 38 of 47
**Version:** 1.0
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, crawl tool or manual link checking
**Depends on:** 37
**Produces:** /docs/sovereignty/404-crawl.md

---

## Purpose

This prompt crawls all internal links to find broken ones. It exists at position 38 because 404s damage trust and SEO, and are easy to miss in manual testing.

---

## Input Contract

The deployed product URL.

---

## Instructions for the Agent

1. Crawl every internal link from the homepage.
2. Record every URL that returns 404.
3. Check every external link resolves (200 or redirect, not 404).
4. Check every asset (image, CSS, JS) loads.
5. Write results to /docs/sovereignty/404-crawl.md.

---

## Negative Constraints

- Do not pass any internal link that returns 404.
- Do not pass any broken asset.
- Do not skip external links.

---

## Output Contract

A file at /docs/sovereignty/404-crawl.md containing: crawled URLs, 404 list, broken assets, overall result.

---

## Acceptance Criteria

PASS when:
- Zero internal 404s.
- Zero broken assets.
- All external links resolve.

FAIL when:
- Any internal 404.
- Any broken asset.
- Any external link returns 404.

BLOCKED when:
- Product is not deployed.
- No crawl tool available.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-37 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-38.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sovereignty/404-crawl.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. 404s are verified by crawling.

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

Prompt 39 consumes /docs/sovereignty/404-crawl.md. Expects: crawl results.

---

## Human Checkpoint

No human checkpoint.
