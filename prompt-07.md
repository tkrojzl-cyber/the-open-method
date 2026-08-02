# Prompt 07: Accessibility and Mobile Pass

**Stage:** 1 - Build
**Position:** 7 of 47
**Version:** 1.3
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, browser, browserbase (for viewport testing)
**Depends on:** 06
**Produces:** /docs/accessibility-mobile-pass.md

---

## Purpose

Run the full accessibility and mobile responsive pass. This is not optional. WCAG 2.1 AA is the standard. Mobile is not an afterthought. Design for 375px, then scale up. Every state has a design. Missing error states are HIGH severity.

---

## Input Contract

All pages built in Prompts 02-06. The design system from /docs/design-system.md. The mobile rules from Prompt 01 (hamburger menu, responsive grids, 44px touch targets, 16px input font-size).

---

## Instructions for the Agent

1. Check keyboard navigation on every page. Tab moves through interactive elements in logical order. Focus is visible.
2. Check screen reader compatibility. Semantic HTML. ARIA labels where needed. alt text on all images.
3. Check color contrast. WCAG 2.1 AA minimum: 4.5:1 for normal text, 3:1 for large text.
4. Test at 375px viewport (mobile). Hamburger menu visible. No horizontal overflow. Touch targets 44px minimum. Input font-size 16px (prevents iOS zoom).
5. Test at 768px viewport (tablet). Responsive grids adapt.
6. Test at 1440px viewport (desktop). Layout does not break.
7. Verify every interactive state has a design: loading, empty, error, success. Missing error states are HIGH.
8. Document results in /docs/accessibility-mobile-pass.md.

---

## Acceptance Criteria

- [ ] Keyboard navigation works on all pages. Focus is visible.
- [ ] Screen reader: semantic HTML, ARIA labels, alt text present.
- [ ] Color contrast meets WCAG 2.1 AA (4.5:1 normal, 3:1 large).
- [ ] 375px: hamburger visible, no horizontal overflow, 44px touch targets, 16px input font-size.
- [ ] 768px: responsive grids adapt.
- [ ] 1440px: layout intact.
- [ ] All interactive states have designs (loading, empty, error, success).
- [ ] /docs/accessibility-mobile-pass.md documents results.
- [ ] No missing error states (HIGH severity if found).

On FAIL: revert to the git commit recorded as baseline_commit and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.

---

## Provenance Checkpoint

**Stage 1:** Hash the primary output artifact. Record in `artifact_hash`. Do NOT publish. Computed for chain construction only.

- **Primary artifact hashed:** /docs/accessibility-mobile-pass.md
- **Artifact hash:** [SHA-256 of /docs/accessibility-mobile-pass.md. Compute at execution time.]
- **Previous verification hash (prevHash):** SHA-256 of the prompt-06 verification file contents.
- **Baseline commit:** [git commit hash at the start of this prompt's execution]
