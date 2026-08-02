# Prompt 12: Clickability and Button Destinations

**Stage:** 2 - Verification
**Position:** 12 of 47
**Version:** 1.2
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, bundle inspection
**Depends on:** 11
**Produces:** /docs/sweeps/clickability.md

---

## Purpose

This prompt verifies every clickable element in the product does what its label says. It exists at position 12 because broken buttons are the second most common issue in AI-built products and directly damage user trust.

---

## Input Contract

The JS bundle from Prompt 11. All Stage 1 artifacts showing PASS.

---

## Instructions for the Agent

1. Extract every button label from the bundle.
2. For each button, determine what onClick does: navigate, submit, API call, copy, or no-op.
3. Flag any button with empty, console.log only, or undefined onClick.
4. Check every CTA resolves to its stated destination.
5. Check every external link has target=_blank and rel=noopener noreferrer.
6. Check every internal link uses the router, not window.location.
7. Write results to /docs/sweeps/clickability.md.

---

## Negative Constraints

- Do not pass a button whose onClick is a no-op without a visible disabled state.
- Do not skip disabled buttons; they must show why they are disabled.
- Do not accept window.location for internal navigation when a router is available.

---

## Output Contract

A file at /docs/sweeps/clickability.md containing: button table with label, onClick behavior, status. Issues list. Overall result.

---

## Acceptance Criteria

PASS when:
- Every clickable element has a working handler or visible disabled state.
- All external links have target=_blank.
- All internal links use the router.

FAIL when:
- Any button has empty/no-op onClick.
- Any external link lacks target=_blank.
- Any internal link uses window.location.

BLOCKED when:
- JS bundle cannot be located.
- Product does not use a router (no internal links to check).

On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
---

## Verification Artifact

A file at /docs/verification/prompt-12.md containing:

- **Prompt:** 12
- **Status:** [PASS / FAIL / BLOCKED]
- **Date:** [ISO 8601 date]
- **Agent version:** [model identifier]
- **Baseline commit:** [git commit hash at the start of this prompt's execution. Used for rollback on FAIL.]
- **Primary artifact hashed:** [path of the primary output artifact]
- **Artifact hash:** [SHA-256 of the primary output artifact. NOT the hash of this verification file.]
- **Previous verification hash (prevHash):** SHA-256 of prompt-11's verification file contents.

Acceptance criteria results (each criterion: PASS/FAIL with evidence).
Notes (findings, MEDIUM/LOW severity entries that do not block).
Chain verification: previous artifact hash recomputed, matches recorded prevHash: YES/NO.

Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sweeps/clickability.md. Record in artifact_hash. prevHash = SHA-256 of prompt-11's verification file contents.

---

## DACV Trigger

No DACV trigger. Clickability is verified by direct inspection.

---

## Security and Privacy Check

Security check applies. Flag any button that triggers an API call without input validation. Record in the sweep results.

---

## Accessibility Check

No accessibility check. No UI is modified.

---

## Mobile Check

No mobile check. No layout is modified.

---

## Inter-Prompt Contract

Prompt 13 consumes /docs/sweeps/clickability.md. Expects: button audit results.

---

## Human Checkpoint

No human checkpoint.