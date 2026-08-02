# Prompt 09: Plugins, Scope Check, and Mobile Final

**Stage:** 1 - Build
**Position:** 9 of 47
**Version:** 1.3
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, browser, browserbase (for mobile verification)
**Depends on:** 08
**Produces:** /docs/scope-check.md

---

## Purpose

Add plugin hooks and extension points for community contributions. Run the final mobile responsive pass. Then check scope: does the product contain only what the core actions list calls for? Any feature not traceable to a core action is scope creep. Scope creep is HIGH severity (ship-blocking).

---

## Input Contract

The discovery brief from Prompt 01 (/docs/discovery-brief.md) with the core actions and non-goals list. All pages and features built in Prompts 02-08. The design system from /docs/design-system.md.

---

## Instructions for the Agent

1. Add plugin hooks if the product supports extension points. Create a Plugin Registry entity for community contributions. Plugin hooks must be traceable: each hook is documented with what it does and which core action it serves.
2. Run the final mobile responsive pass. Hamburger menu opens. All nav items reachable. No horizontal overflow at 375px. Touch targets 44px. Input font-size 16px.
3. Scope check: list every feature and page in the product. Trace each one to a core action in the discovery brief. If a feature does not trace to a core action, it is scope creep. Flag it as HIGH.
4. Check non-goals: has any non-goal been implemented? If yes, remove it. Flag as HIGH.
5. Document the scope check results in /docs/scope-check.md. List each feature, its core action, and whether it is in scope or scope creep.
6. The run command must still work.

---

## Acceptance Criteria

- [ ] Plugin hooks are documented and traceable (if applicable).
- [ ] Plugin Registry entity exists (if applicable).
- [ ] Mobile pass: hamburger opens, all nav reachable, no overflow at 375px, 44px targets, 16px inputs.
- [ ] Every feature traces to a core action. Untraceable features are flagged as HIGH and removed.
- [ ] No non-goals have been implemented. If found, removed and flagged.
- [ ] /docs/scope-check.md documents the full scope check.
- [ ] The run command completes with exit code 0.

On FAIL: revert to the git commit recorded as baseline_commit and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.

---

## Provenance Checkpoint

**Stage 1:** Hash the primary output artifact. Record in `artifact_hash`. Do NOT publish. Computed for chain construction only.

- **Primary artifact hashed:** /docs/scope-check.md
- **Artifact hash:** [SHA-256 of /docs/scope-check.md. Compute at execution time.]
- **Previous verification hash (prevHash):** SHA-256 of the prompt-08 verification file contents.
- **Baseline commit:** [git commit hash at the start of this prompt's execution]
