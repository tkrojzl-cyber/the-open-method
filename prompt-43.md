# Prompt 43: Monitoring and Alerting Setup

**Stage:** 3 - Sovereignty
**Position:** 43 of 47
**Version:** 1.0
**Estimated time:** 45-90 minutes
**Required tools:** Terminal, monitoring platform if available
**Depends on:** 42
**Produces:** /docs/sovereignty/monitoring.md

---

## Purpose

This prompt sets up monitoring and alerting for the product. It exists at position 43 because a product without monitoring is a product whose failures are invisible until a user reports them.

---

## Input Contract

The error classification from Prompt 42. The performance benchmarks from Prompt 23.

---

## Instructions for the Agent

1. Define what to monitor: uptime, error rate, response time, resource usage.
2. Define alert thresholds: error rate above X%, response time above Yms, downtime.
3. Set up monitoring (automated tool, log-based, or manual check schedule).
4. Set up alerting (email, webhook, or manual notification).
5. Test the alerting by triggering a test alert.
6. Write the monitoring setup to /docs/sovereignty/monitoring.md.

---

## Negative Constraints

- Do not set up alerting without testing it.
- Do not set thresholds so low that alerts become noise.
- Do not omit uptime monitoring.

---

## Output Contract

A file at /docs/sovereignty/monitoring.md containing: monitoring targets, alert thresholds, alerting method, test alert result.

---

## Acceptance Criteria

PASS when:
- Monitoring covers uptime, errors, and response time.
- Alert thresholds defined.
- Test alert received.

FAIL when:
- Monitoring incomplete.
- No alert thresholds.
- Test alert not received.

BLOCKED when:
- No monitoring tool available (document manual monitoring schedule instead).

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-42 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-43.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sovereignty/monitoring.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. Monitoring is verified by the test alert.

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

Prompt 44 consumes /docs/sovereignty/monitoring.md. Expects: monitoring setup with tested alerting.

---

## Human Checkpoint

No human checkpoint.
