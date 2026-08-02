# Prompt 02: Architecture and Feature Layer 1

**Stage:** 1 - Build
**Position:** 2 of 47
**Version:** 1.3
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, Base44 builder or equivalent
**Depends on:** 01
**Produces:** /docs/architecture.md

---

## Purpose

Define the technical architecture and build the first 2-3 feature pages with full CRUD functionality. This prompt takes the skeleton from Prompt 01 and makes it functional. The architecture decision document records every stack choice and why it was made.

---

## Input Contract

The discovery brief from Prompt 01 (/docs/discovery-brief.md). All entity schemas from Prompt 01. The design system from /docs/design-system.md. The route structure from Prompt 01.

---

## Instructions for the Agent

1. Write the architecture document to /docs/architecture.md. Include: stack decisions (database, frontend, backend, hosting), the run command (how to start the product), and why each choice was made.
2. Build 2-3 feature pages from the core actions list. Each page must have: page layout, entity CRUD (create, read, update, delete), data visualization, filtering, form validation, loading states, error states, and empty states.
3. Every state has a design. Loading. Empty. Error. Success. No blank pages, ever.
4. Use the design system from Prompt 01. Do not introduce new colors, fonts, or spacing values.
5. Ensure the run command works. The product must start with exit code 0.

---

## Acceptance Criteria

- [ ] /docs/architecture.md exists with stack decisions and run command.
- [ ] 2-3 feature pages are built with full CRUD functionality.
- [ ] Each page has loading, empty, error, and success states.
- [ ] Form validation is present on all forms.
- [ ] The run command completes with exit code 0.
- [ ] No blank pages exist in the built pages.

On FAIL: revert to the git commit recorded as baseline_commit and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.

---

## Provenance Checkpoint

**Stage 1:** Hash the primary output artifact. Record in `artifact_hash`. Do NOT publish. Computed for chain construction only.

- **Primary artifact hashed:** /docs/architecture.md
- **Artifact hash:** [SHA-256 of /docs/architecture.md. Compute at execution time.]
- **Previous verification hash (prevHash):** SHA-256 of the prompt-01 verification file contents.
- **Baseline commit:** [git commit hash at the start of this prompt's execution]

---

## Human Checkpoint

Mandatory. A human must review and approve the architecture decisions and the run command before proceeding. Wrong stack choices here are expensive to fix later.
