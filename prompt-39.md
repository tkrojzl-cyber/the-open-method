# Prompt 39: Load Time Audit

**Stage:** 3 - Sovereignty
**Position:** 39 of 47
**Version:** 1.0
**Estimated time:** 30-60 minutes
**Required tools:** Browser, Lighthouse, terminal
**Depends on:** 38
**Produces:** /docs/sovereignty/load-time.md

---

## Purpose

This prompt measures load time on every page after all sovereignty features are added. It exists at position 39 because sovereignty features can add latency.

---

## Input Contract

The deployed product with all Stage 3 features active.

---

## Instructions for the Agent

1. Measure load time for every page with Lighthouse (mobile and desktop).
2. Measure Time to First Byte (TTFB).
3. Measure First Contentful Paint (FCP).
4. Measure Largest Contentful Paint (LCP).
5. Compare to Stage 2 performance benchmarks from Prompt 23.
6. Flag any page that regressed beyond 500ms from Stage 2.
7. Write results to /docs/sovereignty/load-time.md.

---

## Negative Constraints

- Do not pass any page that regressed beyond 500ms from Stage 2.
- Do not skip mobile measurements.
- Do not pass any page with LCP over 4s.

---

## Output Contract

A file at /docs/sovereignty/load-time.md containing: per-page metrics, regression comparison, overall result.

---

## Acceptance Criteria

PASS when:
- All pages under 3s load.
- No regression beyond 500ms from Stage 2.
- LCP under 4s on all pages.

FAIL when:
- Any page over 3s.
- Regression beyond 500ms.
- LCP over 4s.

BLOCKED when:
- Product not deployed.
- No Lighthouse available.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-38 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-39.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sovereignty/load-time.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. Load time is verified by measurement.

---

## Security and Privacy Check

No security check.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

Mobile check applies. Confirm mobile Lighthouse scores are acceptable.

---

## Inter-Prompt Contract

Prompt 40 consumes /docs/sovereignty/load-time.md. Expects: load time results with regression check.

---

## Human Checkpoint

No human checkpoint.
