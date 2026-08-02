# Prompt 36: Accessibility Audit (WCAG)

**Stage:** 3 - Sovereignty
**Position:** 36 of 47
**Version:** 1.0
**Estimated time:** 60-120 minutes
**Required tools:** Browser, accessibility scanner (axe, Lighthouse), manual testing
**Depends on:** 35
**Produces:** /docs/sovereignty/accessibility-audit.md

---

## Purpose

This prompt runs a full WCAG 2.1 AA compliance audit. It exists at position 36 because accessibility is a legal requirement in many jurisdictions and a sovereignty principle.

---

## Input Contract

The running product. The UI states from Prompt 07.

---

## Instructions for the Agent

1. Run an automated accessibility scanner (axe or Lighthouse) on every page.
2. Manually test keyboard navigation on every flow: can all actions be performed without a mouse.
3. Test screen reader compatibility with NVDA or VoiceOver.
4. Check color contrast for all text against backgrounds (4.5:1 for normal text, 3:1 for large text).
5. Check all images have alt text.
6. Check all form inputs have associated labels.
7. Write results to /docs/sovereignty/accessibility-audit.md.

---

## Negative Constraints

- Do not pass any page that fails automated scanning for WCAG 2.1 AA.
- Do not pass any flow that cannot be completed with keyboard only.
- Do not pass any image without alt text.

---

## Output Contract

A file at /docs/sovereignty/accessibility-audit.md containing: per-page scan results, manual test results, contrast check, issues list, overall result.

---

## Acceptance Criteria

PASS when:
- All pages pass automated WCAG 2.1 AA scan.
- All flows keyboard-navigable.
- All images have alt text.
- All inputs have labels.

FAIL when:
- Any page fails automated scan.
- Any flow not keyboard-navigable.
- Any image without alt text.
- Any input without label.

BLOCKED when:
- No accessibility scanner available.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-35 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-36.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sovereignty/accessibility-audit.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. Accessibility is verified by scanner and manual testing.

---

## Security and Privacy Check

No security check.

---

## Accessibility Check

Accessibility check is the primary check for this prompt. All WCAG 2.1 AA criteria must pass.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 37 consumes /docs/sovereignty/accessibility-audit.md. Expects: WCAG audit results.

---

## Human Checkpoint

No human checkpoint.
