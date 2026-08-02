# Prompt 16: Mobile Optimization

**Stage:** 2 - Verification
**Position:** 16 of 47
**Version:** 1.2
**Estimated time:** 45-90 minutes
**Required tools:** Browser with responsive testing, or real device
**Depends on:** 07, 15
**Produces:** /docs/sweeps/mobile.md

---

## Purpose

This prompt verifies the product is fully functional and visually complete on a phone. It exists at position 16 because mobile failures are the most common UX gap in AI-built products and directly affect conversion.

---

## Input Contract

The running product. Stage 1 UI states from Prompt 07.

---

## Instructions for the Agent

1. Render every page at 375px width (iPhone SE).
2. Check for horizontal overflow on every page.
3. Check hero headline wraps cleanly, no overflow.
4. Check all CTA buttons have minimum 44px height (WCAG 2.1 AA). 48px recommended best practice.
5. Check all font sizes are minimum 11px.
6. Check navigation collapses correctly (hamburger or scroll tab).
7. Check hamburger menu opens, shows all links, closes cleanly.
8. Check pricing cards stack vertically, no side-by-side squeeze.

---

## Negative Constraints

- Do not pass any page with horizontal scroll at 375px.
- Do not pass a hamburger menu that does not show the same links as desktop nav.
- Do not pass form inputs with font-size under 16px (causes iOS auto-zoom).

---

## Output Contract

A file at /docs/sweeps/mobile.md containing: per-page mobile checklist at 375px, issues list, overall result.

---

## Acceptance Criteria

PASS when:
- No horizontal overflow at 375px.
- All touch targets 44px+ (WCAG 2.1 AA minimum).
- All font sizes 11px+.
- Hamburger works and matches desktop nav.
- Pricing cards stack vertically.

FAIL when:
- Any page with horizontal scroll.
- Any touch target under 44px (WCAG 2.1 AA minimum).
- Any input font under 16px.
- Hamburger missing links or broken.

BLOCKED when:
- Product is not deployed or running locally.
- No responsive testing tool available.

On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
---

## Verification Artifact

A file at /docs/verification/prompt-16.md containing:

- **Prompt:** 16
- **Status:** [PASS / FAIL / BLOCKED]
- **Date:** [ISO 8601 date]
- **Agent version:** [model identifier]
- **Baseline commit:** [git commit hash at the start of this prompt's execution. Used for rollback on FAIL.]
- **Primary artifact hashed:** [path of the primary output artifact]
- **Artifact hash:** [SHA-256 of the primary output artifact. NOT the hash of this verification file.]
- **Previous verification hash (prevHash):** SHA-256 of prompt-15's verification file contents.

Acceptance criteria results (each criterion: PASS/FAIL with evidence).
Notes (findings, MEDIUM/LOW severity entries that do not block).
Chain verification: previous artifact hash recomputed, matches recorded prevHash: YES/NO.

Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sweeps/mobile.md. Record in artifact_hash. prevHash = SHA-256 of prompt-15's verification file contents.

---

## DACV Trigger

No DACV trigger. Mobile is verified by direct rendering.

---

## Security and Privacy Check

No security check.

---

## Accessibility Check

Accessibility check applies. Confirm touch targets meet 44x44px minimum (WCAG 2.1 AA). 48px recommended best practice.

---

## Mobile Check

Mobile check is the primary check for this prompt. All mobile criteria above must pass.

---

## Inter-Prompt Contract

Prompt 17 consumes /docs/sweeps/mobile.md. Expects: mobile audit results.

---

## Human Checkpoint

No human checkpoint.