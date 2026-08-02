# Prompt 32: Backup Strategy

**Stage:** 3 - Sovereignty
**Position:** 32 of 47
**Version:** 1.0
**Estimated time:** 45-90 minutes
**Required tools:** Terminal, backup tooling
**Depends on:** 31
**Produces:** /docs/sovereignty/backup-strategy.md

---

## Purpose

This prompt defines and tests the backup strategy for the product. It exists at position 32 because backups are the operational safety net that prevents data loss.

---

## Input Contract

The data model from Prompt 04. The doomsday recovery document from Prompt 26.

---

## Instructions for the Agent

1. Identify all data that needs backing up: database, files, configuration, documentation.
2. Define backup frequency for each data type.
3. Define backup location (local, cloud, offline).
4. Implement automated backup if possible.
5. Perform a full backup.
6. Test restoring from the backup.
7. Write the backup strategy to /docs/sovereignty/backup-strategy.md.

---

## Negative Constraints

- Do not define a backup strategy without testing a restore.
- Do not store backups in the same location as the primary data.
- Do not skip backing up documentation and configuration.

---

## Output Contract

A file at /docs/sovereignty/backup-strategy.md containing: data inventory, backup schedule, backup locations, restore test result.

---

## Acceptance Criteria

PASS when:
- All data types have backup.
- Restore tested and passed.
- Backups stored separately from primary.

FAIL when:
- Any data type lacks backup.
- Restore test failed.
- Backups in same location as primary.

BLOCKED when:
- No backup tooling available.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-31 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-32.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash /docs/sovereignty/backup-strategy.md. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. Backup is verified by the restore test.

---

## Security and Privacy Check

Security check applies. Confirm backups are encrypted if they contain PII.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 33 consumes /docs/sovereignty/backup-strategy.md. Expects: tested backup strategy.

---

## Human Checkpoint

No human checkpoint.
