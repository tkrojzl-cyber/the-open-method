# Prompt 14: Copy and Content Audit

**Stage:** 2 - Verification
**Position:** 14 of 47
**Version:** 1.2
**Estimated time:** 30-60 minutes
**Required tools:** Browser (for rendered DOM inspection), terminal, bundle inspection (for email/domain checks only)
**Depends on:** 13, 11
**Produces:** /docs/sweeps/copy.md

---

## Purpose

This prompt verifies every word on every page is intentional, clean, and free of banned terms. It exists at position 14 because copy errors (em dashes, placeholders, stale content) are trust-damaging and easily caught by inspection.

---

## Input Contract

The running product (deployed or local) for rendered DOM inspection. The JS bundle for email and domain checks only.

---

## Instructions for the Agent

1. IMPORTANT: Em dash and copy checks run against RENDERED DOM TEXT (browserbase_get_content on #root element), not the raw JS bundle. Em dashes inside code strings, variable names, or minified output are structural, not copy violations.
2. Check rendered DOM for em dashes (the unicode character). Flag every occurrence visible to the user.
3. Check rendered DOM for placeholder text: lorem ipsum, coming soon, under construction, TBD, INSERT HERE.
4. Check rendered DOM for double spaces in visible text.
5. Check every page has a title and meta description under 160 characters (via bundle or DOM head inspection).
6. Check all email addresses in copy are real and correctly formatted (bundle grep acceptable for this).
7. Check all domain references in copy point to live domains (bundle grep acceptable for this).
8. Write results to /docs/sweeps/copy.md.

---

## Negative Constraints

- Do not pass any em dash in rendered text (em dashes inside code/variable names are structural, not violations).
- Do not pass any placeholder text.
- Do not pass a page missing a title or meta description.

---

## Output Contract

A file at /docs/sweeps/copy.md containing: em dash count and locations (rendered only), placeholder results, meta audit, email audit, domain audit, issues list, overall result.

---

## Acceptance Criteria

PASS when:
- Zero em dashes in rendered text.
- Zero placeholder text in rendered text.
- All pages have title and meta description.
- All emails and domains are live.

FAIL when:
- Any em dash in rendered text.
- Any placeholder text in rendered text.
- Any page missing title or meta description.
- Any dead domain.

BLOCKED when:
- Product is not running (cannot inspect rendered DOM).

On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
---

## Verification Artifact

A file at /docs/verification/prompt-14.md containing:

- **Prompt:** 14
- **Status:** [PASS / FAIL / BLOCKED]
- **Date:** [ISO 8601 date]
- **Agent version:** [model identifier]
- **Baseline commit:** [git commit hash at the start of this prompt's execution. Used for rollback on FAIL.]
- **Primary artifact hashed:** [path of the primary output artifact]
- **Artifact hash:** [SHA-256 of the primary output artifact. NOT the hash of this verification file.]
- **Previous verification hash (prevHash):** SHA-256 of prompt-13's verification file contents.

Acceptance criteria results (each criterion: PASS/FAIL with evidence).
Notes (findings, MEDIUM/LOW severity entries that do not block).
Chain verification: previous artifact hash recomputed, matches recorded prevHash: YES/NO.

Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sweeps/copy.md. Record in artifact_hash. prevHash = SHA-256 of prompt-13's verification file contents.

---

## DACV Trigger

No DACV trigger. Copy is verified by direct DOM inspection.

---

## Security and Privacy Check

No security check. Copy inspection does not touch data.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 15 consumes /docs/sweeps/copy.md. Expects: copy audit results.

---

## Human Checkpoint

No human checkpoint.