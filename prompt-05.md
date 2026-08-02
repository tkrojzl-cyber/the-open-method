# Prompt 05: Visualization and Primary Flow

**Stage:** 1 - Build
**Position:** 5 of 47
**Version:** 1.3
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, Base44 builder or equivalent, browser
**Depends on:** 04
**Produces:** /docs/primary-flow.md

---

## Purpose

Add canvas-based visualizations, chart components, interactive elements, and animation. Then verify the primary user flow works end to end. This is the first prompt where "does it work" is checked, not just "does it render."

Performance category becomes relevant here. A flow that never completes or takes an abnormally long time is a functional failure. This is an observation, not a measured benchmark. Quantitative performance thresholds (<3s load, <500ms API) are first enforced at Prompt 23.

---

## Input Contract

All feature pages built in Prompts 02-04. The entity schemas from Prompt 01. The architecture from Prompt 02. The design system from /docs/design-system.md.

---

## Instructions for the Agent

1. Build canvas-based visualizations where the product calls for them. Use the canvas useEffect retry pattern: retry canvas mount until the DOM element exists. Never assume the canvas is mounted when useEffect fires.
2. Add chart components for data display. Interactive elements: hover states, click handlers, drill-down.
3. Add transitions and animation. Loading skeletons for async data.
4. Run the primary user flow end to end. The primary flow is the most common path a user takes through the product. Document it in /docs/primary-flow.md.
5. Confirm the primary flow completes. If it does not complete, that is a CRITICAL failure.
6. Note the time the flow takes. If it is abnormally slow (multiple minutes for a simple action), flag it. This is a functional observation, not a measured benchmark.

---

## Acceptance Criteria

- [ ] Canvas visualizations render correctly (if applicable to the product).
- [ ] Chart components display data with interactive elements.
- [ ] Loading skeletons are present for async data.
- [ ] The primary user flow completes end to end.
- [ ] /docs/primary-flow.md documents the primary flow path.
- [ ] No abnormally slow operations in the primary flow (observation, not benchmark).

On FAIL: revert to the git commit recorded as baseline_commit and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.

---

## Provenance Checkpoint

**Stage 1:** Hash the primary output artifact. Record in `artifact_hash`. Do NOT publish. Computed for chain construction only.

- **Primary artifact hashed:** /docs/primary-flow.md
- **Artifact hash:** [SHA-256 of /docs/primary-flow.md. Compute at execution time.]
- **Previous verification hash (prevHash):** SHA-256 of the prompt-04 verification file contents.
- **Baseline commit:** [git commit hash at the start of this prompt's execution]
