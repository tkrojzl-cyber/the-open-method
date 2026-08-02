# Prompt 08: Integrations and Backend Functions

**Stage:** 1 - Build
**Position:** 8 of 47
**Version:** 1.3
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, Base44 builder or equivalent
**Depends on:** 07
**Produces:** /docs/integrations.md

---

## Purpose

Build backend functions, API endpoints, and external integrations. Every integration must have error handling. An integration with no error handling is a CRITICAL failure. This prompt also adds cross-product links if applicable.

---

## Input Contract

The architecture from Prompt 02 (/docs/architecture.md). The security model from Prompt 04 (/docs/security-model.md). All feature pages from Prompts 02-04. The entity schemas from Prompt 01.

---

## Instructions for the Agent

1. Build backend functions for API endpoints. Each function must have hash-chained logging: every call logs a SHA-256 hash of the request, creating an audit trail.
2. Add external integrations (Stripe, email, calendars, OAuth connectors) as the product requires. Every integration must have try/catch error handling. No unhandled rejections.
3. Add scheduled automations if the product calls for them (cron jobs, entity triggers, connector webhooks).
4. Add cross-product links if the product is part of a stack. Links must resolve to live destinations.
5. Document all integrations, endpoints, and automations in /docs/integrations.md.
6. The run command must still work. No integration should break the build.

---

## Acceptance Criteria

- [ ] Backend functions are deployed and callable.
- [ ] Each backend function has hash-chained logging.
- [ ] All integrations have error handling (try/catch, no unhandled rejections).
- [ ] Automations are configured (if applicable).
- [ ] Cross-product links resolve to live destinations (if applicable).
- [ ] /docs/integrations.md lists all integrations and endpoints.
- [ ] The run command completes with exit code 0.

On FAIL: revert to the git commit recorded as baseline_commit and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.

---

## Provenance Checkpoint

**Stage 1:** Hash the primary output artifact. Record in `artifact_hash`. Do NOT publish. Computed for chain construction only.

- **Primary artifact hashed:** /docs/integrations.md
- **Artifact hash:** [SHA-256 of /docs/integrations.md. Compute at execution time.]
- **Previous verification hash (prevHash):** SHA-256 of the prompt-07 verification file contents.
- **Baseline commit:** [git commit hash at the start of this prompt's execution]

---

## Human Checkpoint

Mandatory. A human must review integrations before proceeding. External integrations (payments, email, OAuth) have security and cost implications. Human must confirm which integrations are needed and which are not.
