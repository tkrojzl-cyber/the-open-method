# Prompt 23: Performance Benchmark

**Stage:** 2 - Verification
**Position:** 23 of 47
**Version:** 1.0
**Estimated time:** 30-60 minutes
**Required tools:** Browser, Lighthouse or manual benchmarking, terminal
**Depends on:** 22
**Produces:** /docs/audits/performance.md

---

## Purpose

This prompt measures the product against defined performance thresholds. It exists at position 23 because performance directly affects user retention and conversion, and must be benchmarked before the ship decision.

---

## Input Contract

The running product (deployed or local).

---

## Instructions for the Agent

1. Measure page load time for every primary route.
2. Measure API response time for every backend function.
3. Measure database query time for the primary flow.
4. Check for render-blocking resources.
5. Check image sizes and formats.
6. Record all metrics against thresholds: page load under 3s, API response under 500ms, DB query under 200ms.
7. Write results to /docs/audits/performance.md.

---

## Negative Constraints

- Do not pass any page that exceeds the 3s load threshold.
- Do not pass any API response that exceeds 500ms.
- Do not skip any primary route.

---

## Output Contract

A file at /docs/audits/performance.md containing: per-page metrics table, API response table, DB query table, threshold comparison, overall result.

---

## Acceptance Criteria

PASS when:
- All pages load under 3s.
- All API responses under 500ms.
- All DB queries under 200ms.

FAIL when:
- Any page exceeds 3s load.
- Any API exceeds 500ms.
- Any DB query exceeds 200ms.

BLOCKED when:
- Product is not running.
- No benchmarking tool available.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-22 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-23.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/audits/performance.md. Record in verification artifact.

---

## DACV Trigger

No DACV trigger. Performance is verified by direct measurement.

---

## Security and Privacy Check

No security check.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

Mobile check applies. Confirm performance at 375px with simulated 3G connection (Lighthouse mobile).

---

## Inter-Prompt Contract

Prompt 24 consumes /docs/audits/performance.md. Expects: performance benchmark results.

---

## Human Checkpoint

No human checkpoint.
