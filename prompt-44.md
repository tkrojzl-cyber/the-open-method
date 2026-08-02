# Prompt 44: Community Extension Specification

**Stage:** 3 - Sovereignty
**Position:** 44 of 47
**Version:** 1.0
**Estimated time:** 45-90 minutes
**Required tools:** Text editor
**Depends on:** 43
**Produces:** /docs/sovereignty/community-spec.md

---

## Purpose

This prompt defines how the community can extend the product through plugins or contributions. It exists at position 44 because community ownership of edges is a sovereignty principle.

---

## Input Contract

The extension points from /docs/extension-points.md. The architecture from /docs/architecture.md.

---

## Instructions for the Agent

1. For each extension point in /docs/extension-points.md, define the interface a contributor would implement.
2. Define the contribution process: how to submit, review, and accept extensions.
3. Define the licensing terms for community contributions.
4. Define the bounty system if applicable (rewards for specific extensions).
5. Write the community extension specification to /docs/sovereignty/community-spec.md.

---

## Negative Constraints

- Do not create a contribution process that requires the original builder's approval for every change.
- Do not define licensing terms that give the original builder ownership of community contributions.
- Do not omit the bounty system if bounties are part of the model.

---

## Output Contract

A file at /docs/sovereignty/community-spec.md containing: extension interfaces, contribution process, licensing terms, bounty system.

---

## Acceptance Criteria

PASS when:
- Extension interfaces defined for each extension point.
- Contribution process documented.
- Licensing terms clear.
- Bounty system defined if applicable.

FAIL when:
- Extension interfaces missing.
- Contribution process undefined.
- Licensing terms unclear.

BLOCKED when:
- /docs/extension-points.md is empty.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-43 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-44.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sovereignty/community-spec.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. Community spec is verified by review against extension points.

---

## Security and Privacy Check

No security check.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 45 consumes /docs/sovereignty/community-spec.md. Expects: community extension specification.

---

## Human Checkpoint

No human checkpoint.
