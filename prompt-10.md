# Prompt 10: Polish and Data Model Verification

**Stage:** 1 - Build (final Stage 1 prompt)
**Position:** 10 of 47
**Version:** 1.3
**Estimated time:** 30-60 minutes
**Required tools:** Terminal, browser
**Depends on:** 09
**Produces:** /docs/polish-pass.md

---

## Purpose

Final polish pass. Cross-references between pages. Footer consistency. Meta tags. SEO checklist. Bug fixes batched. Data model verification: at least one test record per entity confirmed working. This is the last Stage 1 prompt. Gate 1 runs after this.

---

## Input Contract

All pages and features built in Prompts 02-09. The discovery brief from Prompt 01. The architecture from Prompt 02. The design system from /docs/design-system.md. The scope check from Prompt 09 (/docs/scope-check.md).

---

## Instructions for the Agent

1. Check cross-references between all pages. Every internal link resolves to a real page. No dead links.
2. Footer consistency: every page has the same footer. Footer links resolve.
3. Add meta tags: title, description, og:title, og:description, og:image on every page. These affect SEO and social sharing.
4. SEO checklist: semantic HTML (h1, h2 hierarchy), meta description present, canonical URLs, sitemap.xml if applicable.
5. Final visual pass: check for visual inconsistencies, misaligned elements, broken layouts at all three viewports (375px, 768px, 1440px).
6. Batch all bug fixes found during the visual pass. Fix them together, not one at a time.
7. Data model verification: create at least one test record in every entity. Confirm CRUD works for every entity. Confirm RLS works (user sees only their records).
8. Write the polish pass summary to /docs/polish-pass.md.
9. Prepare /docs/stage-1-status.md for Gate 1. List all 10 prompts, their status, and any blocking issues.

---

## Acceptance Criteria

- [ ] All internal links resolve. No dead links.
- [ ] Footer is consistent across all pages. Footer links resolve.
- [ ] Meta tags present on every page (title, description, og:title, og:description, og:image).
- [ ] SEO checklist passed (semantic HTML, meta description, canonical URLs).
- [ ] Visual pass at 375px, 768px, 1440px shows no broken layouts.
- [ ] All bug fixes from visual pass are applied.
- [ ] At least one test record exists in every entity. CRUD confirmed.
- [ ] RLS confirmed: user sees only their records.
- [ ] /docs/polish-pass.md exists.
- [ ] /docs/stage-1-status.md exists and lists all 10 prompts with status.
- [ ] No flow regressions from Prompt 05 (primary flow still works).
- [ ] The run command completes with exit code 0.

On FAIL: revert to the git commit recorded as baseline_commit and re-execute from instruction 1. Maximum 3 re-execution attempts. If still failing after 3 attempts, set verification artifact status to BLOCKED and escalate to human.

---

## Provenance Checkpoint

**Stage 1:** Hash the primary output artifact. Record in `artifact_hash`. Do NOT publish. Computed for chain construction only. Gate 1 will use this hash (and all 10 artifact hashes) to compute gate_1_hash.

- **Primary artifact hashed:** /docs/polish-pass.md
- **Artifact hash:** [SHA-256 of /docs/polish-pass.md. Compute at execution time.]
- **Previous verification hash (prevHash):** SHA-256 of the prompt-09 verification file contents.
- **Baseline commit:** [git commit hash at the start of this prompt's execution]

---

## Human Checkpoint

Mandatory. This is a stage gate prompt. A human must confirm the product is ready for Stage 2 verification before Gate 1 passes. Review the stage-1-status.md. Confirm all 10 prompts show PASS.

---

## Gate 1 Preparation

After this prompt passes, Gate 1 computes:
```
gate_1_hash = SHA-256(byte_concat(artifact_hash_01, artifact_hash_02, ..., artifact_hash_10))
```
Record gate_1_hash in /docs/stage-1-status.md. This becomes prevHash for Prompt 11.
