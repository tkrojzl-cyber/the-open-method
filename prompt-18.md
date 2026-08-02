# Prompt 18: Animation and Smoothness

**Stage:** 2 - Verification
**Position:** 18 of 47
**Version:** 1.0
**Estimated time:** 30-60 minutes
**Required tools:** Browser, code inspection
**Depends on:** 17
**Produces:** /docs/sweeps/animation.md

---

## Purpose

This prompt verifies the product feels alive and premium, not static and janky. It exists at position 18 because animation failures (canvas blank after tab switch, hard snap transitions) are the most common polish gap in AI-built products.

---

## Input Contract

The running product. Stage 1 codebase.

---

## Instructions for the Agent

1. Check all canvas draw loop useEffects use the retry pattern (retries until canvas mounted).
2. Check page transitions have minimum opacity fade.
3. Check tab switches have a transition, not a hard snap.
4. Check hover states on buttons and links have transition-colors or transition-opacity.
5. Check loading skeletons or spinners exist for all async data fetches.
6. Check no layout shift (CLS) on page load.
7. Check scroll behavior is smooth.
8. Write results to /docs/sweeps/animation.md.

---

## Negative Constraints

- Do not pass a canvas useEffect that silently returns on null canvas without retry.
- Do not pass a tab switch with no transition.
- Do not pass an async data fetch with no loading state.

---

## Output Contract

A file at /docs/sweeps/animation.md containing: animation checklist, canvas retry pattern verification, issues list, overall result.

---

## Acceptance Criteria

PASS when:
- All canvas useEffects use retry pattern.
- All transitions smooth.
- All async fetches have loading states.
- No layout shift.

FAIL when:
- Any canvas useEffect without retry pattern.
- Any hard snap transition.
- Any async fetch without loading state.
- Any layout shift.

BLOCKED when:
- Product is not running.
- No canvas or animation in the product (state explicitly and stop).

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-17 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-18.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sweeps/animation.md. Record in verification artifact.

---

## DACV Trigger

No DACV trigger. Animation is verified by direct inspection.

---

## Security and Privacy Check

No security check.

---

## Accessibility Check

Accessibility check applies. Confirm prefers-reduced-motion is respected where animations exist.

---

## Mobile Check

No mobile check. Addressed in Prompt 16.

---

## Inter-Prompt Contract

Prompt 19 consumes /docs/sweeps/animation.md. Expects: animation audit results.

---

## Human Checkpoint

No human checkpoint.
