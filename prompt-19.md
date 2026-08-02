# Prompt 19: North Star Alignment and Full Sweep Report

**Stage:** 2 - Verification
**Position:** 19 of 47
**Version:** 1.0
**Estimated time:** 30-60 minutes
**Required tools:** Browser, text editor
**Depends on:** 11, 12, 13, 14, 15, 16, 17, 18
**Produces:** /docs/sweeps/north-star.md; /docs/sweeps/full-report.md

---

## Purpose

This prompt verifies every page answers the north star question and consolidates all sweep results into a single report. It exists at position 19 as the final sweep prompt, consuming all prior sweep artifacts.

---

## Input Contract

All sweep artifacts from Prompts 11-18. The running product.

---

## Instructions for the Agent

1. Assess whether a first-time visitor understands what the product is within 10 seconds.
2. Check the value proposition is clear in one sentence without scrolling.
3. Check a no-login preview path exists if applicable.
4. Check there is no single point of failure preventing a first-time visitor from completing the core flow.
5. Consolidate all sweep results from Prompts 11-18 into /docs/sweeps/full-report.md.
6. Count totals: GREEN, AMBER, RED across all categories.
7. Write ship assessment: ship if zero RED, no-ship if any RED.
8. Write results to /docs/sweeps/north-star.md and /docs/sweeps/full-report.md.

---

## Negative Constraints

- Do not mark ship if any category has RED items.
- Do not omit any sweep category from the full report.
- Do not mark the north star aligned if a first-time visitor cannot determine what the product is.

---

## Output Contract

A file at /docs/sweeps/north-star.md containing: first-visit assessment, value proposition check, single point of failure check. A file at /docs/sweeps/full-report.md containing: all 9 categories with GREEN/AMBER/RED lists, totals, ship assessment.

---

## Acceptance Criteria

PASS when:
- First-time visitor understands the product.
- No single point of failure.
- Full report consolidated with all 9 categories.
- Ship assessment is ship (zero RED).

FAIL when:
- Visitor cannot determine what the product is.
- Single point of failure exists.
- Any category has RED items.
- Full report is missing categories.

BLOCKED when:
- Any sweep artifact from Prompts 11-18 is missing.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-18 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-19.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sweeps/full-report.md. Record in verification artifact. This is the Stage 2 provenance anchor for the sweep layer.

---

## DACV Trigger

No DACV trigger. North star alignment is verified by direct assessment.

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

Prompt 20 consumes /docs/sweeps/full-report.md. Expects: consolidated sweep results with ship assessment. If ship assessment is no-ship, Prompt 20 proceeds but records the RED items as drift factors.

---

## Human Checkpoint

No human checkpoint.
