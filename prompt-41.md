# Prompt 41: Version Control and Commit Hygiene

**Stage:** 3 - Sovereignty
**Position:** 41 of 47
**Version:** 1.0
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, git
**Depends on:** 40
**Produces:** /docs/sovereignty/version-control.md

---

## Purpose

This prompt verifies version control is clean and all changes are committed. It exists at position 41 because uncommitted changes are lost changes, and a clean git history is the foundation of reproducibility.

---

## Input Contract

The product repository.

---

## Instructions for the Agent

1. Check git status is clean (no uncommitted changes).
2. Verify every Stage 1, 2, and 3 artifact is committed.
3. Check commit messages are descriptive.
4. Verify the .gitignore excludes secrets, node_modules, and build artifacts.
5. Check no secrets are in git history (git log -p grep).
6. Tag the current state as the Stage 3 release.
7. Write results to /docs/sovereignty/version-control.md.

---

## Negative Constraints

- Do not pass if git status is not clean.
- Do not pass if any artifact is uncommitted.
- Do not pass if any secret is found in git history.

---

## Output Contract

A file at /docs/sovereignty/version-control.md containing: git status, commit count, secret check result, release tag, overall result.

---

## Acceptance Criteria

PASS when:
- Git status clean.
- All artifacts committed.
- No secrets in history.
- Release tag created.

FAIL when:
- Uncommitted changes.
- Artifacts not committed.
- Secrets in history.
- No release tag.

BLOCKED when:
- No git repository initialized.

On FAIL: revert to the state recorded in the previous prompt's verification artifact and re-execute from this prompt's instruction 1.
On FAIL: revert to the git commit recorded as baseline_commit in this prompt's verification artifact and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.
**Previous verification hash (prevHash):** SHA-256 of the prompt-40 verification file contents. Record the actual hash value at execution time.
**artifact_hash:** [SHA-256 of the primary output artifact. Compute at execution time.]

---

## Verification Artifact

A file at /docs/verification/prompt-41.md containing: prompt number and name; date executed; agent version and model; acceptance criteria results (each PASS/FAIL criterion listed with its result); notes (anomalies, deviations, human interventions); next prompt to execute. Written even if this prompt fails or is blocked.

---

## Provenance Checkpoint

Hash the release tag commit hash. Record in verification artifact and hash chain.

---

## DACV Trigger

No DACV trigger. Git status is verified by direct inspection.

---

## Security and Privacy Check

Security check applies. The secret scan is the primary security check for this prompt.

---

## Accessibility Check

No accessibility check.

---

## Mobile Check

No mobile check.

---

## Inter-Prompt Contract

Prompt 42 consumes /docs/sovereignty/version-control.md. Expects: clean git status with release tag.

---

## Human Checkpoint

No human checkpoint.
