#!/usr/bin/env python3
"""
THE OPEN METHOD - CHAIN MANAGER v2
Implements the v1.2 Inter-Prompt Contract exactly.

3 gates (not 5). Chain runs through verification file hashes.
Gate hashes computed from artifact hashes via byte concatenation.
verify() re-hashes actual files on disk to detect tampering.

Usage:
  python3 chain_manager.py init
    Initialize a fresh chain.

  python3 chain_manager.py commit <prompt_number> <artifact_path> <verification_path>
    Hash both files, record in chain, output prevHash for next prompt.
    Example: python3 chain_manager.py commit 01 docs/discovery-brief.md docs/verification/prompt-01.md

  python3 chain_manager.py chain
    Print the full chain with integrity status.

  python3 chain_manager.py verify
    Verify chain integrity. Re-hashes actual files on disk. Detects tampering.

  python3 chain_manager.py gate <gate_number>
    Compute a gate hash (1, 2, or 3).

  python3 chain_manager.py status
    Show which prompts are committed and which are pending.

  python3 chain_manager.py next <prompt_number>
    Print the prevHash value for the specified prompt.

Chain structure (per v1.2 Inter-Prompt Contract):
  Prompt 01: prevHash = "GENESIS"
  Prompts 02-10: prevHash = SHA-256(prompt N-1 verification file)
  Prompt 11: prevHash = gate_1_hash = SHA-256(byte_concat(artifact_hash_01..10))
  Prompts 12-25: prevHash = SHA-256(prompt N-1 verification file)
  Prompt 26: prevHash = gate_2_hash = SHA-256(byte_concat(artifact_hash_11..25))
  Prompts 27-47: prevHash = SHA-256(prompt N-1 verification file)
  Gate 3: gate_3_hash = SHA-256(byte_concat(artifact_hash_26..47)) = final seal

Prerequisites: Python 3.6+
"""

import hashlib
import json
import os
import sys
from datetime import datetime, timezone

# Gate definitions per v1.2 Stage Gates spec: 3 gates, not 5
# Gate 1: after prompt 10, before prompt 11 (Stage 1 -> Stage 2)
# Gate 2: after prompt 25, before prompt 26 (Stage 2 -> Stage 3)
# Gate 3: after prompt 47 (Stage 3 completion, final seal)
GATES = {
    1: {
        "prompts": list(range(1, 11)),    # 01-10
        "boundary_before": 11,            # prompt 11 uses gate_1_hash as prevHash
        "status_file": "/docs/stage-1-status.md",
    },
    2: {
        "prompts": list(range(11, 26)),   # 11-25
        "boundary_before": 26,            # prompt 26 uses gate_2_hash as prevHash
        "status_file": "/docs/stage-2-status.md",
    },
    3: {
        "prompts": list(range(26, 48)),   # 26-47
        "boundary_before": None,          # no next prompt, this is the final seal
        "status_file": "/docs/sovereignty/final-seal.md",
    },
}

CHAIN_FILE = "chain.json"
GENESIS = "GENESIS"


def load_chain():
    if os.path.exists(CHAIN_FILE):
        with open(CHAIN_FILE, "r") as f:
            return json.load(f)
    return {
        "created": datetime.now(timezone.utc).isoformat(),
        "entries": {},
        "gates": {},
        "genesis": GENESIS,
    }


def save_chain(chain):
    with open(CHAIN_FILE, "w") as f:
        json.dump(chain, f, indent=2)


def sha256_file(filepath):
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def sha256_string(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def compute_gate_hash(chain, gate_number):
    """Compute gate hash from artifact hashes via byte concatenation."""
    gate = GATES[gate_number]
    hashes = []
    for p in gate["prompts"]:
        key = str(p).zfill(2)
        if key not in chain["entries"]:
            return None
        hashes.append(chain["entries"][key]["artifact_hash"])
    # Byte concatenation: raw UTF-8 bytes of each 64-char hex string, in order
    combined = "".join(hashes)
    return sha256_string(combined)


def get_prev_hash(chain, prompt_number):
    """
    Get the prevHash for a given prompt.
    Checks gate boundaries FIRST, then falls back to previous verification hash.
    """
    if prompt_number == 1:
        return GENESIS

    # Check gate boundaries FIRST (the bug was that this came after the plain check)
    for gate_num, gate in GATES.items():
        if prompt_number == gate["boundary_before"]:
            gate_key = f"gate_{gate_num}"
            if gate_key in chain["gates"]:
                return chain["gates"][gate_key]
            # Try to compute it if all prompts in this gate are committed
            gate_hash = compute_gate_hash(chain, gate_num)
            if gate_hash is not None:
                chain["gates"][gate_key] = gate_hash
                save_chain(chain)
                return gate_hash
            # Gate can't be computed yet, some prompts missing
            return None

    # Normal link: hash of previous prompt's verification file
    prev_key = str(prompt_number - 1).zfill(2)
    if prev_key in chain["entries"]:
        return chain["entries"][prev_key]["verification_hash"]

    return None


def cmd_commit(args):
    """Commit an artifact and verification file to the chain."""
    if len(args) < 3:
        print("Usage: python3 chain_manager.py commit <prompt_number> <artifact_path> <verification_path>")
        print("Example: python3 chain_manager.py commit 01 docs/discovery-brief.md docs/verification/prompt-01.md")
        sys.exit(1)

    prompt_num = int(args[0])
    artifact_path = args[1]
    verification_path = args[2]

    if not os.path.exists(artifact_path):
        print(f"ERROR: Artifact file not found: {artifact_path}")
        sys.exit(1)
    if not os.path.exists(verification_path):
        print(f"ERROR: Verification file not found: {verification_path}")
        print("Create the verification file first, then commit.")
        sys.exit(1)

    chain = load_chain()
    key = str(prompt_num).zfill(2)

    # Compute both hashes
    artifact_hash = sha256_file(artifact_path)
    verification_hash = sha256_file(verification_path)

    # Get prevHash (gate boundary checked first)
    prev_hash = get_prev_hash(chain, prompt_num)
    if prev_hash is None:
        # Figure out what's missing
        for gate_num, gate in GATES.items():
            if prompt_num == gate["boundary_before"]:
                missing = [p for p in gate["prompts"] if str(p).zfill(2) not in chain["entries"]]
                if missing:
                    print(f"ERROR: Cannot compute Gate {gate_num}. Missing prompts: {missing}")
                    print(f"Commit all Stage {gate_num} prompts first.")
                    sys.exit(1)
        prev_key = str(prompt_num - 1).zfill(2)
        print(f"ERROR: Previous prompt ({prev_key}) has not been committed yet.")
        sys.exit(1)

    # Record the entry
    chain["entries"][key] = {
        "prompt_number": prompt_num,
        "artifact_path": artifact_path,
        "artifact_hash": artifact_hash,
        "verification_path": verification_path,
        "verification_hash": verification_hash,
        "prev_hash": prev_hash,
        "committed_at": datetime.now(timezone.utc).isoformat(),
    }

    # Check if a gate should be computed after this commit
    for gate_num, gate in GATES.items():
        if prompt_num == gate["prompts"][-1]:
            gate_hash = compute_gate_hash(chain, gate_num)
            if gate_hash is not None:
                gate_key = f"gate_{gate_num}"
                chain["gates"][gate_key] = gate_hash
                save_chain(chain)
                print(f"\n  GATE {gate_num} computed: {gate_hash}")
                print(f"  This is the prevHash for Prompt {gate['boundary_before'] or 'N/A'}")
            else:
                save_chain(chain)

    save_chain(chain)

    print(f"\nCOMMITTED: Prompt {key}")
    print(f"  Artifact:        {artifact_path}")
    print(f"  Artifact hash:   {artifact_hash}")
    print(f"  Verification:    {verification_path}")
    print(f"  Verif hash:      {verification_hash}")
    print(f"  PrevHash:        {prev_hash}")
    print(f"  Timestamp:       {chain['entries'][key]['committed_at']}")

    # Output prevHash for the next prompt
    next_num = prompt_num + 1
    if next_num <= 47:
        next_key = str(next_num).zfill(2)
        # Compute what the next prompt's prevHash will be
        next_prev = get_prev_hash(chain, next_num)
        if next_prev is not None:
            print(f"\nNEXT: Paste this as prevHash in prompt-{next_key}.md verification file:")
            print(f"  {next_prev}")
        else:
            # This happens at gate boundaries where the gate was just computed
            for gate_num, gate in GATES.items():
                if next_num == gate["boundary_before"]:
                    gate_key = f"gate_{gate_num}"
                    if gate_key in chain["gates"]:
                        print(f"\nNEXT: Paste this GATE {gate_num} hash as prevHash in prompt-{next_key}.md:")
                        print(f"  {chain['gates'][gate_key]}")
                        break
            else:
                print(f"\nNEXT: Commit prompt {next_key} to continue.")
    else:
        # Chain complete, compute final seal
        gate3 = compute_gate_hash(chain, 3)
        if gate3:
            chain["gates"]["gate_3"] = gate3
            save_chain(chain)
            print(f"\n  GATE 3 (FINAL SEAL): {gate3}")
            print(f"\nCHAIN COMPLETE. All 47 prompts committed. Final seal computed.")


def cmd_chain(args):
    """Print the full chain."""
    chain = load_chain()
    entries = chain["entries"]

    if not entries:
        print("Chain is empty. Run 'commit' after executing a prompt.")
        return

    print("=" * 80)
    print("THE OPEN METHOD - HASH CHAIN LEDGER (v1.2 structure)")
    print(f"Created: {chain['created']}")
    print(f"Entries: {len(entries)} / 47")
    print(f"Gates:   {list(chain['gates'].keys()) if chain['gates'] else 'none computed'}")
    print("=" * 80)

    for i in range(1, 48):
        key = str(i).zfill(2)
        if key not in entries:
            continue

        e = entries[key]
        print(f"\n  Prompt {key}:")
        print(f"    artifact:     {e['artifact_path']}")
        print(f"    artifact_hash: {e['artifact_hash']}")
        print(f"    verif_hash:    {e['verification_hash']}")
        print(f"    prevHash:      {e['prev_hash']}")

        # Verify the link
        if i == 1:
            if e["prev_hash"] != GENESIS:
                print(f"    STATUS: BROKEN (expected GENESIS, got {e['prev_hash']})")
            else:
                print(f"    STATUS: OK (GENESIS)")
        else:
            # Check if this is a gate boundary
            is_gate_boundary = False
            for gate_num, gate in GATES.items():
                if i == gate["boundary_before"]:
                    is_gate_boundary = True
                    gate_key = f"gate_{gate_num}"
                    if gate_key in chain["gates"]:
                        if e["prev_hash"] == chain["gates"][gate_key]:
                            print(f"    STATUS: OK (gate {gate_num} hash)")
                        else:
                            print(f"    STATUS: BROKEN (expected gate_{gate_num} hash, got different value)")
                    else:
                        print(f"    STATUS: PENDING (gate {gate_num} not computed)")
                    break

            if not is_gate_boundary:
                prev_key = str(i - 1).zfill(2)
                if prev_key in entries:
                    expected = entries[prev_key]["verification_hash"]
                    if e["prev_hash"] == expected:
                        print(f"    STATUS: OK (links to {prev_key} verification file)")
                    else:
                        print(f"    STATUS: BROKEN (expected {expected[:16]}..., got {e['prev_hash'][:16]}...)")
                else:
                    print(f"    STATUS: PENDING (previous prompt not committed)")

        # Show gate markers
        for gate_num, gate in GATES.items():
            if i == gate["prompts"][-1]:
                gate_key = f"gate_{gate_num}"
                if gate_key in chain["gates"]:
                    print(f"    --> GATE {gate_num}: {chain['gates'][gate_key]}")

    print(f"\n{'=' * 80}")
    print(f"Total committed: {len(entries)} / 47")
    print(f"Gates computed:  {list(chain['gates'].keys()) if chain['gates'] else 'none'}")
    print(f"{'=' * 80}")


def cmd_verify(args):
    """
    Verify chain integrity. Two checks:
    1. Re-hash actual files on disk, compare to recorded hashes (tamper detection)
    2. Verify chain links (prevHash matches previous verification_hash or gate hash)
    """
    chain = load_chain()
    entries = chain["entries"]

    if not entries:
        print("Chain is empty. Nothing to verify.")
        return

    print("VERIFYING CHAIN INTEGRITY (v1.2)")
    print("=" * 80)
    print("Check 1: Re-hashing actual files on disk (tamper detection)")
    print("-" * 80)

    all_ok = True
    breaks = 0
    tampered = 0

    # CHECK 1: Re-hash actual files on disk
    for i in range(1, 48):
        key = str(i).zfill(2)
        if key not in entries:
            continue

        e = entries[key]

        # Re-hash artifact
        if os.path.exists(e["artifact_path"]):
            current_artifact_hash = sha256_file(e["artifact_path"])
            if current_artifact_hash != e["artifact_hash"]:
                print(f"  Prompt {key}: ARTIFACT TAMPERED")
                print(f"    Recorded:  {e['artifact_hash']}")
                print(f"    Actual:    {current_artifact_hash}")
                print(f"    File:      {e['artifact_path']}")
                tampered += 1
                all_ok = False
            else:
                print(f"  Prompt {key}: artifact OK")
        else:
            print(f"  Prompt {key}: ARTIFACT FILE MISSING ({e['artifact_path']})")
            tampered += 1
            all_ok = False

        # Re-hash verification file
        if os.path.exists(e["verification_path"]):
            current_verif_hash = sha256_file(e["verification_path"])
            if current_verif_hash != e["verification_hash"]:
                print(f"  Prompt {key}: VERIFICATION FILE TAMPERED")
                print(f"    Recorded:  {e['verification_hash']}")
                print(f"    Actual:    {current_verif_hash}")
                print(f"    File:      {e['verification_path']}")
                tampered += 1
                all_ok = False
            else:
                print(f"  Prompt {key}: verification file OK")
        else:
            print(f"  Prompt {key}: VERIFICATION FILE MISSING ({e['verification_path']})")
            tampered += 1
            all_ok = False

    # CHECK 2: Verify chain links
    print()
    print("Check 2: Chain link integrity (prevHash verification)")
    print("-" * 80)

    link_breaks = 0

    for i in range(1, 48):
        key = str(i).zfill(2)
        if key not in entries:
            continue

        e = entries[key]

        if i == 1:
            if e["prev_hash"] != GENESIS:
                print(f"  Prompt 01: BROKEN (prevHash is not GENESIS)")
                link_breaks += 1
                all_ok = False
            else:
                print(f"  Prompt 01: OK (GENESIS)")
        else:
            # Check if this is a gate boundary
            is_gate_boundary = False
            for gate_num, gate in GATES.items():
                if i == gate["boundary_before"]:
                    is_gate_boundary = True
                    gate_key = f"gate_{gate_num}"
                    if gate_key not in chain["gates"]:
                        print(f"  Prompt {key}: PENDING (gate {gate_num} not computed)")
                        break
                    # Recompute the gate hash from artifact hashes
                    recomputed = compute_gate_hash(chain, gate_num)
                    if recomputed != chain["gates"][gate_key]:
                        print(f"  Prompt {key}: GATE {gate_num} BROKEN (stored hash does not match recomputed)")
                        link_breaks += 1
                        all_ok = False
                    elif e["prev_hash"] != chain["gates"][gate_key]:
                        print(f"  Prompt {key}: BROKEN (prevHash does not match gate_{gate_num} hash)")
                        print(f"    Expected: {chain['gates'][gate_key]}")
                        print(f"    Actual:   {e['prev_hash']}")
                        link_breaks += 1
                        all_ok = False
                    else:
                        print(f"  Prompt {key}: OK (gate {gate_num} boundary)")
                    break

            if not is_gate_boundary:
                prev_key = str(i - 1).zfill(2)
                if prev_key not in entries:
                    print(f"  Prompt {key}: PENDING (prompt {prev_key} not committed)")
                    continue

                expected = entries[prev_key]["verification_hash"]
                if e["prev_hash"] == expected:
                    print(f"  Prompt {key}: OK (links to {prev_key})")
                else:
                    print(f"  Prompt {key}: BROKEN")
                    print(f"    Expected prevHash: {expected}")
                    print(f"    Actual prevHash:   {e['prev_hash']}")
                    link_breaks += 1
                    all_ok = False

    # CHECK 3: Verify gate hashes
    print()
    print("Check 3: Gate hash integrity")
    print("-" * 80)

    for gate_num in GATES:
        gate_key = f"gate_{gate_num}"
        if gate_key not in chain["gates"]:
            print(f"  Gate {gate_num}: not computed")
            continue
        recomputed = compute_gate_hash(chain, gate_num)
        if recomputed != chain["gates"][gate_key]:
            print(f"  Gate {gate_num}: BROKEN (recomputed != stored)")
            all_ok = False
        else:
            print(f"  Gate {gate_num}: OK")
            print(f"    {chain['gates'][gate_key]}")

    # Summary
    print()
    print("=" * 80)
    print(f"SUMMARY")
    print(f"  Files tampered or missing:  {tampered}")
    print(f"  Chain link breaks:          {link_breaks}")
    print(f"  Entries verified:           {len(entries)} / 47")
    if all_ok and tampered == 0 and link_breaks == 0:
        print(f"  CHAIN INTEGRITY: OK")
    else:
        print(f"  CHAIN INTEGRITY: BROKEN")
    print("=" * 80)


def cmd_gate(args):
    """Compute or display a gate hash."""
    if len(args) < 1:
        print("Usage: python3 chain_manager.py gate <gate_number>")
        print("Gates: 1 (prompts 01-10), 2 (prompts 11-25), 3 (prompts 26-47)")
        sys.exit(1)

    gate_num = int(args[0])
    if gate_num not in GATES:
        print(f"ERROR: Gate {gate_num} does not exist. Valid gates: 1, 2, 3")
        sys.exit(1)

    chain = load_chain()
    gate = GATES[gate_num]
    gate_prompts = gate["prompts"]
    gate_key = f"gate_{gate_num}"

    missing = [p for p in gate_prompts if str(p).zfill(2) not in chain["entries"]]
    if missing:
        print(f"ERROR: Cannot compute Gate {gate_num}. Missing prompts: {missing}")
        sys.exit(1)

    gate_hash = compute_gate_hash(chain, gate_num)
    chain["gates"][gate_key] = gate_hash
    save_chain(chain)

    print(f"GATE {gate_num}")
    print(f"  Prompts: {gate_prompts[0]:02d}-{gate_prompts[-1]:02d}")
    print(f"  Hash:    {gate_hash}")
    if gate["boundary_before"]:
        print(f"\n  This hash is the prevHash for Prompt {gate['boundary_before']:02d}.")
    else:
        print(f"\n  This is the product's final provenance seal.")


def cmd_status(args):
    """Show which prompts are committed and which are pending."""
    chain = load_chain()
    entries = chain["entries"]

    print("OPEN METHOD - CHAIN STATUS")
    print("=" * 80)

    committed = 0
    pending = 0

    for i in range(1, 48):
        key = str(i).zfill(2)
        if key in entries:
            print(f"  Prompt {key}: COMMITTED  artifact={entries[key]['artifact_hash'][:16]}...  verif={entries[key]['verification_hash'][:16]}...")
            committed += 1
        else:
            print(f"  Prompt {key}: PENDING")
            pending += 1

    print("=" * 80)
    print(f"Committed: {committed} / 47")
    print(f"Pending:   {pending}")
    print(f"Gates:     {list(chain['gates'].keys()) if chain['gates'] else 'none computed'}")


def cmd_next(args):
    """Print the prevHash to use for a given prompt."""
    if len(args) < 1:
        print("Usage: python3 chain_manager.py next <prompt_number>")
        sys.exit(1)

    prompt_num = int(args[0])
    chain = load_chain()
    prev_hash = get_prev_hash(chain, prompt_num)

    if prev_hash is None:
        # Check if it's a gate boundary with missing prompts
        for gate_num, gate in GATES.items():
            if prompt_num == gate["boundary_before"]:
                missing = [p for p in gate["prompts"] if str(p).zfill(2) not in chain["entries"]]
                if missing:
                    print(f"Cannot compute Gate {gate_num} (prevHash for prompt {str(prompt_num).zfill(2)}).")
                    print(f"Missing prompts: {missing}")
                    sys.exit(1)
        prev_key = str(prompt_num - 1).zfill(2)
        print(f"Prompt {prev_key} has not been committed yet. Commit it first.")
        sys.exit(1)

    # Label whether it's a gate hash or a verification hash
    is_gate = False
    for gate_num, gate in GATES.items():
        if prompt_num == gate["boundary_before"]:
            is_gate = True
            print(f"prevHash for prompt {str(prompt_num).zfill(2)} (GATE {gate_num} hash):")
            break
    if not is_gate:
        print(f"prevHash for prompt {str(prompt_num).zfill(2)} (verification hash of prompt {str(prompt_num - 1).zfill(2)}):")

    print(f"  {prev_hash}")


def cmd_init(args):
    """Initialize a fresh chain."""
    if os.path.exists(CHAIN_FILE):
        print("WARNING: chain.json already exists. Overwrite? (y/N)")
        confirm = input().strip().lower()
        if confirm != "y":
            print("Aborted.")
            return
        os.remove(CHAIN_FILE)

    chain = {
        "created": datetime.now(timezone.utc).isoformat(),
        "entries": {},
        "gates": {},
        "genesis": GENESIS,
    }
    save_chain(chain)
    print(f"Chain initialized. genesis = {GENESIS}")
    print(f"Run 'commit 01 <artifact_path> <verification_path>' after executing Prompt 01.")


COMMANDS = {
    "init": cmd_init,
    "commit": cmd_commit,
    "chain": cmd_chain,
    "verify": cmd_verify,
    "gate": cmd_gate,
    "status": cmd_status,
    "next": cmd_next,
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("THE OPEN METHOD - CHAIN MANAGER v2")
        print("Implements v1.2 Inter-Prompt Contract. 3 gates, verification-file chaining.")
        print("")
        print("Commands:")
        print("  init                            Initialize a fresh chain")
        print("  commit <N> <artifact> <verif>   Hash both files and add to chain")
        print("  chain                           Print full chain with integrity status")
        print("  verify                          Re-hash files on disk + verify chain links")
        print("  gate <N>                        Compute a gate hash (1, 2, or 3)")
        print("  status                          Show committed vs pending prompts")
        print("  next <N>                        Print the prevHash for prompt N")
        print("")
        print("Chain structure (v1.2):")
        print("  Prompt 01: prevHash = GENESIS")
        print("  Prompts 02-10: prevHash = SHA-256(prompt N-1 verification file)")
        print("  Prompt 11: prevHash = gate_1_hash (from artifact hashes 01-10)")
        print("  Prompts 12-25: prevHash = SHA-256(prompt N-1 verification file)")
        print("  Prompt 26: prevHash = gate_2_hash (from artifact hashes 11-25)")
        print("  Prompts 27-47: prevHash = SHA-256(prompt N-1 verification file)")
        print("  Gate 3: final seal (from artifact hashes 26-47)")
        sys.exit(0)

    COMMANDS[sys.argv[1]](sys.argv[2:])


if __name__ == "__main__":
    main()
