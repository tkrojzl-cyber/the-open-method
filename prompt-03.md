# Prompt 03: Feature Layer 2

**Stage:** 1 - Build
**Position:** 3 of 47
**Version:** 1.3
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, Base44 builder or equivalent
**Depends on:** 02
**Produces:** /docs/feature-layer-2.md

---

## Purpose

Build the next 2-3 feature pages. This continues the core build, adding the second layer of functionality. Each page follows the same pattern as Prompt 02: full CRUD, all states, design system compliance.

---

## Input Contract

The architecture from Prompt 02 (/docs/architecture.md). The entity schemas from Prompt 01. The design system from /docs/design-system.md. The run command from /docs/architecture.md. The pages already built in Prompt 02.

---

## Instructions for the Agent

1. Build 2-3 additional feature pages from the core actions list (different from Prompt 02's pages).
2. Each page must have: page layout, entity CRUD, data visualization, filtering, form validation, loading states, error states, empty states.
3. Cross-reference between pages built in Prompt 02 and this prompt. Navigation between feature pages must work.
4. Maintain the design system. No new tokens.
5. The run command must still work after these pages are added.
6. Write a summary of pages built to /docs/feature-layer-2.md.

---

## Acceptance Criteria

- [ ] 2-3 additional feature pages are built with full CRUD.
- [ ] Each page has loading, empty, error, and success states.
- [ ] Navigation between Prompt 02 pages and Prompt 03 pages works.
- [ ] The run command completes with exit code 0.
- [ ] /docs/feature-layer-2.md lists the pages built.

On FAIL: revert to the git commit recorded as baseline_commit and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.

---

## Provenance Checkpoint

**Stage 1:** Hash the primary output artifact. Record in `artifact_hash`. Do NOT publish. Computed for chain construction only.

- **Primary artifact hashed:** /docs/feature-layer-2.md
- **Artifact hash:** [SHA-256 of /docs/feature-layer-2.md. Compute at execution time.]
- **Previous verification hash (prevHash):** SHA-256 of the prompt-02 verification file contents.
- **Baseline commit:** [git commit hash at the start of this prompt's execution]
