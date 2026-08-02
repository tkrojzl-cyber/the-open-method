# Prompt 01: Scaffold and Discovery

**Stage:** 1 - Build
**Position:** 1 of 47
**Version:** 1.3
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, Base44 builder or equivalent
**Depends on:** None (genesis prompt)
**Produces:** /docs/discovery-brief.md

---

## Purpose

This is the genesis prompt. It produces the discovery brief, the product skeleton, and all entity schemas. Everything downstream depends on this. If the scaffold is wrong, the product is wrong. No exceptions.

The IA Constitution check runs here: does this product amplify the human or replace them? Before any build begins.

---

## Input Contract

A product idea, described in 1-3 sentences. A target audience. A primary language (bilingual by default). Any constraints from the founder.

---

## Instructions for the Agent

1. Write the discovery brief to /docs/discovery-brief.md. Include: product name, one-sentence description, target persona, primary language, secondary language, 3-5 core actions (what the user does), 3-5 non-goals (what the product does NOT do), and the IA Constitution verdict (amplify or replace).
2. Define ALL entity schemas. JSON definitions for every database table. Fields, types, enums, required fields. This is the most critical step. Get entities right here or everything downstream breaks.
3. Create the main dashboard layout. Navigation structure with all routes defined. The skeleton must be structurally complete.
4. Specify the design system: colors, typography, spacing, breakpoints. Record it in /docs/design-system.md.
5. Define mobile rules: hamburger menu, responsive grids, touch targets (44px minimum), 16px input font-size. These are non-negotiable.
6. Set up bilingual infrastructure: locale detection and translation keys from the first commit. Not an afterthought.

---

## Acceptance Criteria

- [ ] /docs/discovery-brief.md exists and lists 3-5 core actions and 3-5 non-goals.
- [ ] All entity schemas are defined and created in the database.
- [ ] Main dashboard renders with navigation structure.
- [ ] All routes are defined in the router.
- [ ] Design system is documented in /docs/design-system.md.
- [ ] Mobile rules are specified (hamburger, 44px touch targets, 16px input font-size).
- [ ] Bilingual infrastructure is present (locale detection + translation keys).
- [ ] IA Constitution verdict is recorded in the discovery brief.

On FAIL: revert to the git commit recorded as baseline_commit and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.

---

## Provenance Checkpoint

**Stage 1:** Hash the primary output artifact using SHA-256. Record it in the verification artifact's `artifact_hash` field. Do NOT publish or publicly verify this hash. The hash exists for chain construction only. Gate 1 needs it to compute the gate hash.

- **Primary artifact hashed:** /docs/discovery-brief.md
- **Artifact hash:** [SHA-256 of /docs/discovery-brief.md. Compute at execution time.]
- **Previous verification hash (prevHash):** GENESIS
- **Baseline commit:** [git commit hash at the start of this prompt's execution]

---

## Human Checkpoint

Mandatory. A human must review and approve the discovery brief, entity schemas, and core actions before proceeding to Prompt 02. This is the foundation. Everything builds on it.
