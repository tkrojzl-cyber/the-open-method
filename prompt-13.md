# Prompt 13: Payment and Conversion Flow

**Stage:** 2 - Verification
**Position:** 13 of 47
**Version:** 1.2
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, bundle inspection
**Depends on:** 12, 08 (conditional on integrations existing)
**Produces:** /docs/sweeps/payments.md

---

## Purpose

This prompt verifies money flows without friction. Every payment path must be end-to-end clean. It exists at position 13 because payment failures are revenue-blocking and the most damaging trust failure.

---

## Input Contract

The JS bundle from Prompt 12. Stage 1 integration documentation from Prompt 08 if payment is integrated.

---

## Instructions for the Agent

1. Extract every Stripe or payment link from the bundle.
2. Confirm every payment link is a production URL, not a test or sandbox link.
3. Flag any placeholder strings: YOUR_STRIPE, STRIPE_LINK, REPLACE_ME, TODO, pk_test_, sk_test_.
4. Confirm every payment link opens in a new tab (target=_blank).
5. Confirm every payment link is in an anchor href, not a router Link.
6. Check pricing displayed matches the actual Stripe product prices.
7. Check each pricing tier has exactly one unambiguous buy CTA.
8. Write results to /docs/sweeps/payments.md.

---

## Negative Constraints

- Do not pass any test Stripe link (buy.stripe.com/test_ or pk_test_ or sk_test_) in production.
- Do not pass a payment link buried more than 2 clicks from the homepage.
- Do not pass a payment link in a router Link component instead of an anchor.

---

## Output Contract

A file at /docs/sweeps/payments.md containing: payment link table, currency audit, placeholder check, issues list, overall result.

---

## Acceptance Criteria

PASS when:
- All payment links are production URLs.
- All open in new tab.
- Pricing displayed matches Stripe.
- No placeholder strings.

FAIL when:
- Any test Stripe link in production.
- Any placeholder string.
- Currency mismatch.
- Payment link in router Link.

BLOCKED when:
- No payment integration in the product (state explicitly and stop).

On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
---

## Verification Artifact

A file at /docs/verification/prompt-13.md containing:

- **Prompt:** 13
- **Status:** [PASS / FAIL / BLOCKED]
- **Date:** [ISO 8601 date]
- **Agent version:** [model identifier]
- **Baseline commit:** [git commit hash at the start of this prompt's execution. Used for rollback on FAIL.]
- **Primary artifact hashed:** [path of the primary output artifact]
- **Artifact hash:** [SHA-256 of the primary output artifact. NOT the hash of this verification file.]
- **Previous verification hash (prevHash):** SHA-256 of prompt-12's verification file contents.

Acceptance criteria results (each criterion: PASS/FAIL with evidence).
Notes (findings, MEDIUM/LOW severity entries that do not block).
Chain verification: previous artifact hash recomputed, matches recorded prevHash: YES/NO.

Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sweeps/payments.md. Record in artifact_hash. prevHash = SHA-256 of prompt-12's verification file contents.

---

## DACV Trigger

DACV trigger: Yes, if payment links are found. Question type: A (Verify). Trigger after instruction 7 (results written to /docs/sweeps/payments.md) and before the human checkpoint. Ask second AI to verify each Stripe link resolves to a real, active Stripe checkout page, not a 404 or expired link.

---

## Security and Privacy Check

Security check applies. Confirm no Stripe secret keys (sk_) appear in the bundle. Only publishable keys (pk_) are acceptable. Flag any sk_ key as CRITICAL.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 14 consumes /docs/sweeps/payments.md. Expects: payment audit results.

---

## Human Checkpoint

Human checkpoint: Yes. The human must confirm all payment links in /docs/sweeps/payments.md are correct and point to the intended Stripe products before this prompt passes. This is mandatory per the template rule for any prompt involving payment, legal, or public deployment.