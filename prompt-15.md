# Prompt 15: Branding and Visual Consistency

**Stage:** 2 - Verification
**Position:** 15 of 47
**Version:** 1.2
**Estimated time:** 30-60 minutes
**Required tools:** Browser, bundle inspection
**Depends on:** 07, 14
**Produces:** /docs/sweeps/branding.md

---

## Purpose

This prompt verifies the product looks like one product made by one team with one visual system. It exists at position 15 because visual inconsistency signals unprofessionalism and undermines trust before the user reads a word.

---

## Input Contract

The running product (deployed or local). The JS bundle. Stage 1 UI states from Prompt 07.

---

## Instructions for the Agent

1. Check background color is consistent across all pages.
2. Check font is consistent across all pages, no fallback to system sans-serif.
3. Check primary accent color is used consistently for CTAs and active states.
4. Check no mixing of icon libraries.
5. Check no emoji used as icons or logos in headers, nav, or CTAs.
6. Check button border-radius is consistent.
7. Check heading hierarchy is logical (h1 > h2 > h3).
8. Check footer is identical across all pages.

---

## Negative Constraints

- Do not pass a page with a different background color from the rest.
- Do not pass mixed icon libraries on the same page.
- Do not pass emoji used as logos or icons.

---

## Output Contract

A file at /docs/sweeps/branding.md containing: visual consistency checklist with results, issues list (with severity levels per finding), overall result.

---

## Acceptance Criteria

PASS when:
- Consistent background, font, accent color across all pages.
- No mixed icon libraries.
- Logical heading hierarchy.
- Identical footer.

FAIL when:
- Any page with different background or font.
- Mixed icon libraries.
- Emoji as icons.

BLOCKED when:
- Product is not deployed or running locally.

On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
---

## Verification Artifact

A file at /docs/verification/prompt-15.md containing:

- **Prompt:** 15
- **Status:** [PASS / FAIL / BLOCKED]
- **Date:** [ISO 8601 date]
- **Agent version:** [model identifier]
- **Baseline commit:** [git commit hash at the start of this prompt's execution. Used for rollback on FAIL.]
- **Primary artifact hashed:** [path of the primary output artifact]
- **Artifact hash:** [SHA-256 of the primary output artifact. NOT the hash of this verification file.]
- **Previous verification hash (prevHash):** SHA-256 of prompt-14's verification file contents.

Acceptance criteria results (each criterion: PASS/FAIL with evidence).
Notes (findings, MEDIUM/LOW severity entries that do not block).
Chain verification: previous artifact hash recomputed, matches recorded prevHash: YES/NO.

Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sweeps/branding.md. Record in artifact_hash. prevHash = SHA-256 of prompt-14's verification file contents.

---

## DACV Trigger

No DACV trigger. Visual consistency is verified by direct inspection.

---

## Security and Privacy Check

No security check.

---

## Accessibility Check

Accessibility check applies. Confirm color contrast meets WCAG 2.1 AA (4.5:1) as part of the visual audit.

---

## Mobile Check

No mobile check. Layout is checked in Prompt 16.

---

## Inter-Prompt Contract

Prompt 16 consumes /docs/sweeps/branding.md. Expects: branding audit results.

---

## Human Checkpoint

No human checkpoint.

---

## Severity Note

Border-radius mismatch is MEDIUM severity (non-blocking). It is recorded in the issues list with severity MEDIUM but does not cause a FAIL. Inconsistent border-radius alone does not fail this prompt.