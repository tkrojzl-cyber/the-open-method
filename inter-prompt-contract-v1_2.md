# Inter-Prompt Contract v1.2

**Updated:** 2026-08-02
**Status:** Second-pass corrections
**Changes from v1.1:** S1 (Stage 1 hash rule aligned with template). S2 (chain-verification exceptions + || definition). S4 (Prompt 14 dependency corrected: 13 added). Severity table removed (defers to Verification Matrix v1.2 per S7).

---

## §1. Verification Artifact Format (corrected — S1)

Every prompt writes to `/docs/verification/prompt-[NN].md`:

```markdown
# Verification Artifact — Prompt [NN]

**Prompt:** [NN]
**Status:** [PASS / FAIL / BLOCKED]
**Date:** [ISO 8601 date]
**Agent version:** [model identifier and version]
**Baseline commit:** [git commit hash at the start of this prompt's execution. Used for rollback on FAIL.]
**Primary artifact hashed:** [path of the file that was hashed]
**Artifact hash:** [SHA-256 hash of the primary output artifact. NOT the hash of this verification file.]
**Previous verification hash (prevHash):** [See chain rules below]

## Acceptance Criteria Results
- [criterion text]: PASS — [evidence]
- [criterion text]: FAIL — [evidence]

## Notes
[Findings, deviations, observations. MEDIUM and LOW severity findings recorded here but do not block.]

## Chain Verification
[For Stage 2 and Stage 3 prompts only:]
Previous artifact hash (recomputed): [hash]
Matches recorded prevHash: [YES / NO]
```

### prevHash rules (S1 + S2 fix)

- Prompt 01: prevHash = "GENESIS"
- Prompts 02-10: prevHash = SHA-256(prompt [N-1] verification file contents)
- Prompt 11: prevHash = gate_1_hash (computed from Stage 1 artifact hashes, NOT prompt-10's verification file)
- Prompts 12-25: prevHash = SHA-256(prompt [N-1] verification file contents)
- Prompt 26: prevHash = gate_2_hash (computed from Stage 2 artifact hashes, NOT prompt-25's verification file)
- Prompts 27-47: prevHash = SHA-256(prompt [N-1] verification file contents)

Stage 1 prompts DO compute artifact_hash (S1 fix — Stage 1 hashes are computed but not published). Without this, gate_1_hash is uncomputable.

---

## §2. Artifact Path Registry (unchanged from v1.1)

[See v1.1 Artifact Path Registry — unchanged. All 47 paths remain canonical.]

---

## §3. Depends-on Rule (S4 fix — Prompt 14 corrected)

The `Depends on` field lists every prompt whose output is referenced in the Input Contract. Not just the immediate predecessor.

Corrected dependencies for prompts 11-17:

| Prompt | Depends on (corrected) |
|--------|----------------------|
| 11 | 10 |
| 12 | 11 |
| 13 | 12, 08 (conditional on integrations existing) |
| 14 | 13, 12 (S4 fix: 13 was missing — 13 is the immediate predecessor, 12 provides the bundle) |
| 15 | 07, 14 |
| 16 | 07, 15 |
| 17 | 05, 06, 16 |

Every prompt's prevHash still requires the immediately preceding verification artifact regardless of data dependency. Prompt 14's prevHash links to Prompt 13's verification file even though Prompt 14 depends on Prompt 12 for input data.

---

## §4. Gate Hash Registration (S2 fix — || defined)

Gate hashes are computed by byte-concatenating the artifact_hash values (64-character hex strings, UTF-8 encoded) of all prompts in that stage, in order, then hashing with SHA-256.

- Gate 1: gate_1_hash = SHA-256(byte_concat(artifact_hash_01, ..., artifact_hash_10))
  - Recorded in /docs/stage-1-status.md, field `gate_1_hash`
  - Becomes prevHash for Prompt 11

- Gate 2: gate_2_hash = SHA-256(byte_concat(artifact_hash_11, ..., artifact_hash_25))
  - Recorded in /docs/stage-2-status.md, field `gate_2_hash`
  - Becomes prevHash for Prompt 26

- Gate 3: gate_3_hash = SHA-256(byte_concat(artifact_hash_26, ..., artifact_hash_47))
  - Recorded in /docs/sovereignty/final-seal.md, field `gate_3_hash`
  - This is the product's final provenance seal

Verification at stage boundaries: recompute the gate hash from the recorded artifact_hash values. Do NOT hash the preceding prompt's verification file — that is a different value. See Verification Matrix v1.2 §6 for the worked example.
