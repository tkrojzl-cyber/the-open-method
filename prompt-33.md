# Prompt 33: Failover Plan

**Stage:** 3 - Sovereignty
**Position:** 33 of 47
**Version:** 1.0
**Estimated time:** 45-90 minutes
**Required tools:** Terminal, deployment platform
**Depends on:** 32
**Produces:** /docs/sovereignty/failover-plan.md

---

## Purpose

This prompt defines and tests the failover plan for when the primary service goes down. It exists at position 33 because operational resilience requires a tested path to recovery.

---

## Input Contract

The backup strategy from Prompt 32. The hosting decision from /docs/architecture.md.

---

## Instructions for the Agent

1. Define the primary failure scenarios: server crash, network outage, data corruption, provider outage.
2. For each scenario, define the failover steps and responsible party.
3. Define the Recovery Time Objective (RTO) for each scenario.
4. Define the Recovery Point Objective (RPO) for data.
5. Test one failover scenario.
6. Record the actual recovery time against the RTO.
7. Write the failover plan to /docs/sovereignty/failover-plan.md.

---

## Negative Constraints

- Do not define an RTO without testing against it.
- Do not create a failover plan that depends on a single provider with no alternative.
- Do not skip the failover test.

---

## Output Contract

A file at /docs/sovereignty/failover-plan.md containing: failure scenarios, failover steps, RTO/RPO, test result.

---

## Acceptance Criteria

PASS when:
- All scenarios defined.
- RTO and RPO set.
- Failover test passed within RTO.

FAIL when:
- Scenarios missing.
- No RTO/RPO.
- Failover test failed or exceeded RTO.

BLOCKED when:
- No failover capability available.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-32 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-33.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sovereignty/failover-plan.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. Failover is verified by the test.

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

Prompt 34 consumes /docs/sovereignty/failover-plan.md. Expects: tested failover plan.

---

## Human Checkpoint

No human checkpoint.
