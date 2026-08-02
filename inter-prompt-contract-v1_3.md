# Inter-Prompt Contract v1.3

**Updated:** 2026-08-02
**Status:** Final polish pass (P1-P5)
**Changes from v1.2:** P3 (Prompt 14 dependency corrected to 13, 11 — 11 is the bundle source, not 12). Everything else unchanged from v1.2.

---

## §1. Verification Artifact Format (unchanged from v1.2)

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

### prevHash rules

- Prompt 01: prevHash = "GENESIS"
- Prompts 02-10: prevHash = SHA-256(prompt [N-1] verification file contents)
- Prompt 11: prevHash = gate_1_hash (computed from Stage 1 artifact hashes, NOT prompt-10's verification file)
- Prompts 12-25: prevHash = SHA-256(prompt [N-1] verification file contents)
- Prompt 26: prevHash = gate_2_hash (computed from Stage 2 artifact hashes, NOT prompt-25's verification file)
- Prompts 27-47: prevHash = SHA-256(prompt [N-1] verification file contents)

Stage 1 prompts DO compute artifact_hash (computed but not published). Without this, gate_1_hash is uncomputable.

---

## §2. Artifact Path Registry (unchanged from v1.1/v1.2)

[See v1.2 Artifact Path Registry — unchanged. All 47 paths remain canonical.]

---

## §3. Depends-on Rule (P3 fix — Prompt 14 corrected)

The `Depends on` field lists every prompt whose output is referenced in the Input Contract, plus the immediate predecessor (whose verification artifact provides the prevHash link). Not just the immediate predecessor.

The rule is: list the immediate predecessor (for the chain link) plus any earlier prompt whose output artifact is directly consumed by this prompt's Input Contract.

Corrected dependencies for prompts 11-17:

| Prompt | Depends on | Rationale |
|--------|----------------------|-----------|
| 11 | 10 | Immediate predecessor. Gate 1 hash comes from Stage 1. |
| 12 | 11 | Immediate predecessor. Bundle obtained in Prompt 11. |
| 13 | 12, 08 | Immediate predecessor (12). Prompt 08 provides integration docs if payment is integrated. |
| 14 | 13, 11 | Immediate predecessor (13) for chain link. Prompt 11 is where the JS bundle is first obtained ("Download or locate the product's JS bundle"). Prompt 12 reuses the same bundle from 11, it does not re-derive it. So the bundle's source is 11, not 12. (P3 fix) |
| 15 | 07, 14 | Immediate predecessor (14). Prompt 07 provides UI states for visual audit. |
| 16 | 07, 15 | Immediate predecessor (15). Prompt 07 provides UI states for mobile audit. |
| 17 | 05, 06, 16 | Immediate predecessor (16). Prompts 05 and 06 provide primary and secondary flow documentation. |

Every prompt's prevHash requires the immediately preceding verification artifact regardless of data dependency.

---

## §4. Gate Hash Registration (unchanged from v1.2)

Gate hashes are computed by byte-concatenating the artifact_hash values (64-character hex strings, UTF-8 encoded) of all prompts in that stage, in order, then hashing with SHA-256.

- Gate 1: gate_1_hash = SHA-256(byte_concat(artifact_hash_01, ..., artifact_hash_10))
  - Recorded in /docs/stage-1-status.md, field `gate_1_hash`
  - Becomes prevHash for Prompt 11

- Gate 2: gate_2_hash = SHA-256(byte_concat(artifact_hash_11, ..., artifact_hash_25))
  - Recorded in /docs/stage-2-status.md, field `gate_2_hash`
  - Becomes prevHash for Prompt 26

- Gate 3: gate_3_hash = SHA-256(byte_concat(artifact_hash_26, ..., artifact_hash_47))
  - Recorded in /docs/sovereignty/final-seal.md, field `gate_3_hash`

Verification at stage boundaries: recompute the gate hash from the recorded artifact_hash values. Do NOT hash the preceding prompt's verification file — that is a different value. See Verification Matrix v1.3 §6 for the worked example.
