# Prompt 06: Secondary Flow and Context Pages

**Stage:** 1 - Build
**Position:** 6 of 47
**Version:** 1.3
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, Base44 builder or equivalent, browser
**Depends on:** 05
**Produces:** /docs/secondary-flows.md

---

## Purpose

Build context pages (about, pricing, terms, API docs) and verify all secondary user flows. Context pages are not afterthoughts. They are the pages visitors see before deciding to engage. A broken secondary flow is a HIGH severity failure.

Performance category is relevant here (observation only). A secondary flow that never completes is a functional failure.

---

## Input Contract

The primary flow from Prompt 05 (/docs/primary-flow.md). The architecture from Prompt 02. The design system from /docs/design-system.md. All feature pages from Prompts 02-04.

---

## Instructions for the Agent

1. Build context pages: about page, pricing page, terms page (placeholder is fine for now, legal content comes in Prompt 30-31), API docs page (if applicable).
2. Run all secondary user flows end to end. A secondary flow is any path a user can take that is not the primary flow.
3. Document each secondary flow in /docs/secondary-flows.md. Include the flow path and whether it completes.
4. Check cross-references between context pages and feature pages. Links must resolve.
5. Confirm the run command still works after adding context pages.

---

## Acceptance Criteria

- [ ] About page exists and renders.
- [ ] Pricing page exists and renders.
- [ ] Terms page exists (placeholder acceptable).
- [ ] All secondary flows complete end to end.
- [ ] /docs/secondary-flows.md documents each secondary flow.
- [ ] Cross-references between pages resolve.
- [ ] The run command completes with exit code 0.

On FAIL: revert to the git commit recorded as baseline_commit and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.

---

## Provenance Checkpoint

**Stage 1:** Hash the primary output artifact. Record in `artifact_hash`. Do NOT publish. Computed for chain construction only.

- **Primary artifact hashed:** /docs/secondary-flows.md
- **Artifact hash:** [SHA-256 of /docs/secondary-flows.md. Compute at execution time.]
- **Previous verification hash (prevHash):** SHA-256 of the prompt-05 verification file contents.
- **Baseline commit:** [git commit hash at the start of this prompt's execution]
