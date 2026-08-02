# Prompt 45: Bounty Board Specification

**Stage:** 3 - Sovereignty
**Position:** 45 of 47
**Version:** 1.0
**Estimated time:** 30-60 minutes
**Required tools:** Text editor
**Depends on:** 44
**Produces:** /docs/sovereignty/bounty-board.md

---

## Purpose

This prompt defines the bounty board for community contributions. It exists at position 45 because bounties are how sovereign products get built without a team: the community builds the edges.

---

## Input Contract

The community extension specification from Prompt 44.

---

## Instructions for the Agent

1. List specific bounties: what needs building, what the reward is, what the acceptance criteria are.
2. Define how bounties are claimed and awarded.
3. Define the review process for bounty submissions.
4. Define dispute resolution.
5. Write the bounty board specification to /docs/sovereignty/bounty-board.md.

---

## Negative Constraints

- Do not create bounties without clear acceptance criteria.
- Do not define a dispute resolution process that depends solely on the original builder.
- Do not omit the reward structure.

---

## Output Contract

A file at /docs/sovereignty/bounty-board.md containing: bounty list, claim process, review process, dispute resolution, reward structure.

---

## Acceptance Criteria

PASS when:
- Bounties listed with acceptance criteria.
- Claim and review process defined.
- Dispute resolution defined.
- Reward structure clear.

FAIL when:
- Bounties lack acceptance criteria.
- Process undefined.
- No reward structure.

BLOCKED when:
- No bounties applicable (state if the product has no community extension model).

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-44 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-45.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sovereignty/bounty-board.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. Bounty board is verified by review.

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

Prompt 46 consumes /docs/sovereignty/bounty-board.md. Expects: bounty board specification.

---

## Human Checkpoint

No human checkpoint.
