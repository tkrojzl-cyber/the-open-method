# Prompt 11: Routing and Navigation Audit

**Stage:** 2 - Verification
**Position:** 11 of 47
**Version:** 1.2
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, browser, bundle download capability
**Depends on:** 10
**Produces:** /docs/sweeps/routing.md

---

## Purpose

This prompt verifies every route in the product renders a real component, not a blank state, a login wall it should not be behind, or a 404. It exists at position 11 as the first Stage 2 forensic sweep, because routing failures are the most common broken-experience issue in AI-built products.

---

## Input Contract

The deployed or locally running product, the JS bundle at /dist/ or the live URL. All Stage 1 verification artifacts showing PASS, per Gate 1. The gate_1_hash from /docs/stage-1-status.md.

---

## Instructions for the Agent

1. Download or locate the product's JS bundle.
2. Extract every route path declaration from the bundle.
3. Confirm each route resolves to a defined component, not undefined or null.
4. Check every internal Link and navigate() call points to a route that exists in the router.
5. Check the 404 fallback route exists and renders a real 404 page.
6. Check authenticated-only routes redirect to login when no session exists.
7. Check public routes do not redirect to login.
8. Write results to /docs/sweeps/routing.md.

---

## Negative Constraints

- Do not skip routes that appear unused; orphaned routes are still checked.
- Do not pass a route that resolves to a component that renders blank or null.
- Do not mark a route GREEN if it redirects to login when it should be public.

---

## Output Contract

A file at /docs/sweeps/routing.md containing: route table with component status (GREEN/AMBER/RED), issues list, overall result.

---

## Acceptance Criteria

PASS when:
- Every route resolves to a real component.
- 404 fallback exists.
- Public routes are accessible without login.

FAIL when:
- Any route is 404, blank, or resolves to undefined.
- 404 fallback is missing.
- Public route incorrectly redirects to login.

BLOCKED when:
- Product is not deployed or running locally.
- JS bundle cannot be located.

On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
---

## Verification Artifact

A file at /docs/verification/prompt-11.md containing:

- **Prompt:** 11
- **Status:** [PASS / FAIL / BLOCKED]
- **Date:** [ISO 8601 date]
- **Agent version:** [model identifier]
- **Baseline commit:** [git commit hash at the start of this prompt's execution. Used for rollback on FAIL.]
- **Primary artifact hashed:** [path of the primary output artifact]
- **Artifact hash:** [SHA-256 of the primary output artifact. NOT the hash of this verification file.]
- **Previous verification hash (prevHash):** gate_1_hash from /docs/stage-1-status.md. This is NOT the hash of prompt-10's verification file. See Verification Matrix v1.2 §6 and Inter-Prompt Contract v1.2 §4 for gate hash computation.

Acceptance criteria results (each criterion: PASS/FAIL with evidence).
Notes (findings, MEDIUM/LOW severity entries that do not block).
Chain verification: previous artifact hash recomputed, matches recorded prevHash: YES/NO.

Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sweeps/routing.md using SHA-256. Record in the verification artifact's artifact_hash field. The prevHash for this verification artifact is gate_1_hash from /docs/stage-1-status.md (NOT SHA-256 of prompt-10's verification file). This is the first link in the Stage 2 chain.

---

## DACV Trigger

No DACV trigger. Routing is verified by direct inspection, not cross-AI verification.

---

## Security and Privacy Check

No security check. This prompt inspects routing structure, not data.

---

## Accessibility Check

No accessibility check. No UI is modified.

---

## Mobile Check

No mobile check. No layout is modified.

---

## Inter-Prompt Contract

Prompt 12 consumes: /docs/sweeps/routing.md. Expects: route table and status results. If not produced, Prompt 12 cannot reference routing in the full sweep report.

---

## Human Checkpoint

No human checkpoint. Agent proceeds to Prompt 12 upon passing.