#!/usr/bin/env python3
"""Zero-dependency state harness for the Bottleneck skill.

This tool does not replace repository-aware engineering judgment. It enforces the
small set of mechanical invariants that are valuable to make machine-checkable:

- a frozen architecture contract before production activation,
- at most one ACTIVE/REOPENED production slice,
- predeclared closure gates,
- evidence-backed gate completion,
- a non-placeholder context capsule before CLOSED,
- explicit reopen records.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

STATE_DIR = ".bottleneck"
STATE_FILE = "state.json"
DEFAULT_GATES = [
    "correctness",
    "edge-states",
    "performance",
    "api-stability",
    "integration",
    "verification",
    "docs",
    "duplication-check",
    "orphan-check",
    "context-capsule",
]
IGNORE_DIRS = {
    ".git", ".hg", ".svn", ".bottleneck", "node_modules", "vendor", "dist",
    "build", "coverage", ".next", ".cache", ".venv", "venv", "__pycache__",
}
RISKY_NAME = re.compile(
    r"(?:^|[._-])(old|new|legacy|final|final2|v2|v3|copy|backup|bak|tmp|temp|draft)(?:[._-]|$)",
    re.IGNORECASE,
)
MARKER = re.compile(r"\b(TODO|FIXME|STUB|PLACEHOLDER|TEMPORARY|HACK)\b", re.IGNORECASE)
TEXT_EXTS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".java", ".go", ".rs", ".c", ".h",
    ".cpp", ".hpp", ".cs", ".rb", ".php", ".swift", ".kt", ".kts", ".html",
    ".css", ".scss", ".md", ".json", ".yaml", ".yml", ".toml", ".sh", ".sql",
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def project_root(value: str | None) -> Path:
    return Path(value or ".").expanduser().resolve()


def bn_dir(root: Path) -> Path:
    return root / STATE_DIR


def state_path(root: Path) -> Path:
    return bn_dir(root) / STATE_FILE


def die(message: str, code: int = 2) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(code)


def load_state(root: Path) -> dict[str, Any]:
    path = state_path(root)
    if not path.exists():
        die(f"No Bottleneck state found at {path}. Run `init` first.")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        die(f"Cannot read state: {exc}")


def save_state(root: Path, state: dict[str, Any]) -> None:
    path = state_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def history(state: dict[str, Any], event: str, **details: Any) -> None:
    state.setdefault("history", []).append({"at": now(), "event": event, **details})


def validate_id(slice_id: str) -> str:
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]{0,63}", slice_id):
        die("Slice id must match [a-z0-9][a-z0-9._-]{0,63}.")
    return slice_id


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def cmd_init(args: argparse.Namespace) -> None:
    root = project_root(args.root)
    target = bn_dir(root)
    target.mkdir(parents=True, exist_ok=True)
    if state_path(root).exists() and not args.force:
        die(f"State already exists at {state_path(root)}. Use --force only if reset is intentional.")

    state = {
        "schema_version": 1,
        "protocol": "bottleneck",
        "project": args.project or root.name,
        "created_at": now(),
        "contract_frozen": False,
        "contract_frozen_at": None,
        "active_slice": None,
        "slices": {},
        "history": [],
    }
    history(state, "init")
    save_state(root, state)

    write_if_missing(target / "system-sketch.md", """# System Sketch\n\n## Objective\n\nTBD\n\n## Canonical owners\n\nTBD\n\n## Major modules\n\nTBD\n\n## Data / control flow\n\nTBD\n\n## Architecture-invalidating unknowns\n\nTBD\n""")
    write_if_missing(target / "contract.md", """# Architecture Contract\n\nReplace every `TBD` before freezing.\n\n- Canonical state ownership: TBD\n- Module boundaries: TBD\n- Public schemas/APIs: TBD\n- Coordinate/unit conventions: TBD\n- Time/lifecycle semantics: TBD\n- Persistence/versioning: TBD\n- Error semantics: TBD\n- Performance envelope: TBD\n""")
    (target / "capsules").mkdir(exist_ok=True)
    (target / "evidence").mkdir(exist_ok=True)
    (target / "reopen").mkdir(exist_ok=True)
    print(f"Initialized Bottleneck state in {target}")


def cmd_status(args: argparse.Namespace) -> None:
    root = project_root(args.root)
    state = load_state(root)
    if args.json:
        print(json.dumps(state, indent=2, ensure_ascii=False))
        return

    print(f"PROJECT: {state.get('project', root.name)}")
    print(f"CONTRACT: {'FROZEN' if state.get('contract_frozen') else 'UNFROZEN'}")
    print(f"ACTIVE: {state.get('active_slice') or '-'}")
    grouped = {"SKELETON": [], "ACTIVE": [], "REOPENED": [], "CLOSED": []}
    for sid, item in state.get("slices", {}).items():
        grouped.setdefault(item.get("status", "?"), []).append(sid)
    for status in ["SKELETON", "ACTIVE", "REOPENED", "CLOSED"]:
        print(f"{status}: {', '.join(sorted(grouped.get(status, []))) or '-'}")

    active = state.get("active_slice")
    if active:
        item = state["slices"][active]
        pending = [name for name, gate in item.get("gates", {}).items() if gate.get("status") != "pass"]
        print(f"NEXT GATE: {pending[0] if pending else 'capsule/close'}")


def contract_ready(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, "contract.md does not exist"
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text.strip()) < 120:
        return False, "contract.md is too small to be meaningful"
    if re.search(r"\bTBD\b|<fill>|PLACEHOLDER", text, re.IGNORECASE):
        return False, "contract.md still contains TBD/placeholder markers"
    return True, "ok"


def cmd_freeze_contract(args: argparse.Namespace) -> None:
    root = project_root(args.root)
    state = load_state(root)
    ok, reason = contract_ready(bn_dir(root) / "contract.md")
    if not ok and not args.force:
        die(f"Contract cannot be frozen: {reason}. Resolve it or use --force with an explicit external justification.")
    state["contract_frozen"] = True
    state["contract_frozen_at"] = now()
    history(state, "contract-frozen", forced=bool(args.force), note=args.note or "")
    save_state(root, state)
    print("Architecture contract frozen.")


def parse_gates(raw: str | None) -> list[str]:
    if not raw:
        return list(DEFAULT_GATES)
    gates = [g.strip().lower().replace(" ", "-") for g in raw.split(",") if g.strip()]
    if not gates:
        die("At least one closure gate is required.")
    if len(set(gates)) != len(gates):
        die("Closure gates must be unique.")
    return gates


def cmd_add(args: argparse.Namespace) -> None:
    root = project_root(args.root)
    state = load_state(root)
    sid = validate_id(args.slice_id)
    if sid in state["slices"]:
        die(f"Slice {sid!r} already exists.")
    gates = parse_gates(args.gates)
    state["slices"][sid] = {
        "title": args.title or sid,
        "status": "SKELETON",
        "created_at": now(),
        "activated_at": None,
        "closed_at": None,
        "gates": {g: {"status": "pending", "evidence": []} for g in gates},
        "capsule": None,
        "reopen_count": 0,
    }
    history(state, "slice-added", slice=sid, gates=gates)
    save_state(root, state)
    print(f"Added SKELETON slice: {sid}")


def cmd_activate(args: argparse.Namespace) -> None:
    root = project_root(args.root)
    state = load_state(root)
    sid = validate_id(args.slice_id)
    if not state.get("contract_frozen"):
        die("Architecture contract is not frozen. Freeze it before production activation.")
    if sid not in state["slices"]:
        die(f"Unknown slice {sid!r}. Add it first.")
    item = state["slices"][sid]
    if item["status"] not in {"SKELETON", "REOPENED"}:
        die(f"Slice {sid!r} is {item['status']}; only SKELETON or REOPENED can become ACTIVE.")
    current = state.get("active_slice")
    if current and current != sid:
        die(f"Production WIP limit violation: {current!r} is already active.")
    item["status"] = "ACTIVE"
    item["activated_at"] = now()
    state["active_slice"] = sid
    history(state, "slice-activated", slice=sid)
    save_state(root, state)
    print(f"ACTIVE: {sid}")


def cmd_gate(args: argparse.Namespace) -> None:
    root = project_root(args.root)
    state = load_state(root)
    sid = validate_id(args.slice_id)
    if sid not in state["slices"]:
        die(f"Unknown slice {sid!r}.")
    item = state["slices"][sid]
    if item["status"] != "ACTIVE" or state.get("active_slice") != sid:
        die("Closure gates can only be changed for the current ACTIVE slice.")
    gate_name = args.gate.lower()
    if gate_name not in item["gates"]:
        die(f"Unknown gate {gate_name!r}. Known: {', '.join(item['gates'])}")
    if args.passed == args.failed:
        die("Choose exactly one of --pass or --fail.")
    status = "pass" if args.passed else "fail"
    evidence = list(item["gates"][gate_name].get("evidence", []))
    if args.evidence:
        evidence.extend(args.evidence)
    if status == "pass" and not evidence and not args.no_evidence:
        die("Passing a gate requires --evidence (or --no-evidence for a deliberately non-file-verifiable gate).")
    item["gates"][gate_name] = {"status": status, "evidence": evidence, "updated_at": now()}
    history(state, "gate-updated", slice=sid, gate=gate_name, status=status, evidence=evidence)
    save_state(root, state)
    print(f"{sid}:{gate_name} -> {status.upper()}")


def capsule_path(root: Path, sid: str) -> Path:
    return bn_dir(root) / "capsules" / f"{sid}.md"


def cmd_capsule(args: argparse.Namespace) -> None:
    root = project_root(args.root)
    state = load_state(root)
    sid = validate_id(args.slice_id)
    if sid not in state["slices"]:
        die(f"Unknown slice {sid!r}.")
    item = state["slices"][sid]
    path = capsule_path(root, sid)
    if path.exists() and not args.force:
        print(path)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    evidence = []
    for gate, data in item.get("gates", {}).items():
        for ev in data.get("evidence", []):
            evidence.append(f"- {gate}: {ev}")
    evidence_text = "\n".join(evidence) or "- TBD"
    path.write_text(f"""# CLOSED Capsule — {sid}\n\n## Responsibility\n\nTBD\n\n## Public surface\n\nTBD\n\n## Authoritative inputs\n\nTBD\n\n## Outputs / artifacts\n\nTBD\n\n## Invariants\n\nTBD\n\n## Ownership boundaries\n\nTBD\n\n## Budgets\n\nTBD\n\n## Evidence\n\n{evidence_text}\n\n## Known limitations\n\nTBD\n\n## Integration notes\n\nTBD\n\n## Reopen conditions\n\nTBD\n\n## Authoritative source locations\n\nTBD\n""", encoding="utf-8")
    print(path)


def capsule_ready(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, "capsule file does not exist"
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text.strip()) < 180:
        return False, "capsule is too small"
    if re.search(r"\bTBD\b|<fill>|PLACEHOLDER", text, re.IGNORECASE):
        return False, "capsule still contains TBD/placeholder markers"
    return True, "ok"


def cmd_close(args: argparse.Namespace) -> None:
    root = project_root(args.root)
    state = load_state(root)
    sid = validate_id(args.slice_id)
    if sid not in state["slices"]:
        die(f"Unknown slice {sid!r}.")
    item = state["slices"][sid]
    if item["status"] != "ACTIVE" or state.get("active_slice") != sid:
        die(f"Slice {sid!r} is not the current ACTIVE slice.")
    failed = [g for g, data in item["gates"].items() if data.get("status") != "pass"]
    if failed:
        die("Cannot close; gates not passed: " + ", ".join(failed))
    path = capsule_path(root, sid)
    ok, reason = capsule_ready(path)
    if not ok and not args.force:
        die(f"Cannot close; context capsule invalid: {reason}. Run `capsule {sid}` and fill it.")
    item["status"] = "CLOSED"
    item["closed_at"] = now()
    item["capsule"] = str(path.relative_to(root)) if path.exists() else None
    state["active_slice"] = None
    history(state, "slice-closed", slice=sid, capsule=item["capsule"], forced=bool(args.force))
    save_state(root, state)
    print(f"CLOSED: {sid}")


def cmd_reopen(args: argparse.Namespace) -> None:
    root = project_root(args.root)
    state = load_state(root)
    sid = validate_id(args.slice_id)
    if sid not in state["slices"]:
        die(f"Unknown slice {sid!r}.")
    if state.get("active_slice"):
        die(f"Cannot reopen while {state['active_slice']!r} occupies the production WIP slot.")
    item = state["slices"][sid]
    if item["status"] != "CLOSED":
        die("Only a CLOSED slice can be reopened.")
    if not args.reason or len(args.reason.strip()) < 8:
        die("Reopen requires a meaningful --reason.")
    item["status"] = "REOPENED"
    item["reopen_count"] = int(item.get("reopen_count", 0)) + 1
    # Previously passing gates become pending only when explicitly requested; by default
    # keep evidence and require the agent to reset affected gates with --reset-gates.
    if args.reset_gates:
        requested = [g.strip() for g in args.reset_gates.split(",") if g.strip()]
        for gate in requested:
            if gate not in item["gates"]:
                die(f"Unknown gate in --reset-gates: {gate}")
            item["gates"][gate]["status"] = "pending"
    record = bn_dir(root) / "reopen" / f"{sid}-{item['reopen_count']}.md"
    record.write_text(
        f"# REOPEN Record — {sid}\n\n- At: {now()}\n- Reason: {args.reason.strip()}\n- Reset gates: {args.reset_gates or 'none declared'}\n",
        encoding="utf-8",
    )
    state["active_slice"] = sid
    # REOPENED itself consumes the slot; activation command is not required.
    history(state, "slice-reopened", slice=sid, reason=args.reason.strip(), record=str(record.relative_to(root)))
    save_state(root, state)
    print(f"REOPENED (occupies WIP slot): {sid}")


def cmd_score(args: argparse.Namespace) -> None:
    vals = [args.impact, args.uncertainty, args.reusability]
    if any(v < 1 or v > 5 for v in vals):
        die("Impact, uncertainty, and reusability must each be 1..5.")
    raw = args.impact * args.uncertainty * args.reusability
    normalized = round(raw / 125 * 100)
    print(json.dumps({
        "impact": args.impact,
        "uncertainty": args.uncertainty,
        "reusability": args.reusability,
        "raw": raw,
        "normalized_100": normalized,
    }, indent=2))


def scan_files(root: Path, max_bytes: int = 512_000) -> dict[str, list[dict[str, Any]]]:
    risky: list[dict[str, Any]] = []
    markers: list[dict[str, Any]] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel_parts = path.relative_to(root).parts
        if any(part in IGNORE_DIRS for part in rel_parts[:-1]):
            continue
        rel = str(path.relative_to(root))
        if RISKY_NAME.search(path.name):
            risky.append({"path": rel, "reason": "version/legacy/temp-like filename"})
        if path.suffix.lower() not in TEXT_EXTS:
            continue
        try:
            if path.stat().st_size > max_bytes:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for idx, line in enumerate(text.splitlines(), 1):
            m = MARKER.search(line)
            if m:
                markers.append({"path": rel, "line": idx, "marker": m.group(1).upper(), "text": line.strip()[:180]})
                if len(markers) >= 200:
                    break
    return {"risky_names": risky[:200], "markers": markers[:200]}


def cmd_audit(args: argparse.Namespace) -> None:
    root = project_root(args.root)
    state = load_state(root)
    slots = [sid for sid, item in state.get("slices", {}).items() if item.get("status") in {"ACTIVE", "REOPENED"}]
    state_issues = []
    if len(slots) > 1:
        state_issues.append(f"WIP violation: {len(slots)} slices occupy production slot: {slots}")
    if state.get("active_slice") and state["active_slice"] not in slots:
        state_issues.append("active_slice pointer disagrees with slice status")
    for sid, item in state.get("slices", {}).items():
        if item.get("status") == "CLOSED":
            cap = root / item.get("capsule", "") if item.get("capsule") else capsule_path(root, sid)
            ok, reason = capsule_ready(cap)
            if not ok:
                state_issues.append(f"CLOSED {sid}: invalid capsule ({reason})")
            unpassed = [g for g, data in item.get("gates", {}).items() if data.get("status") != "pass"]
            if unpassed:
                state_issues.append(f"CLOSED {sid}: gates no longer pass: {unpassed}")

    scan = scan_files(root)
    result = {
        "project": state.get("project"),
        "production_slots": slots,
        "state_issues": state_issues,
        "suspected_risky_names": scan["risky_names"],
        "placeholder_markers": scan["markers"],
        "notes": [
            "Filename and marker findings are heuristics, not proof of dead/orphan code.",
            "Confirm reachability/ownership before deletion.",
        ],
    }
    out = bn_dir(root) / "audit.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"WIP slots: {slots or '-'}")
        print(f"State issues: {len(state_issues)}")
        for issue in state_issues:
            print(f"  - {issue}")
        print(f"Risky filenames: {len(scan['risky_names'])}")
        print(f"TODO/STUB/PLACEHOLDER-like markers: {len(scan['markers'])}")
        print(f"Audit written to {out}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="bottleneck", description="Bottleneck WIP=1 production harness")
    sub = parser.add_subparsers(dest="command", required=True)

    def root_arg(p: argparse.ArgumentParser) -> None:
        p.add_argument("--root", default=".", help="Project root (default: current directory)")

    p = sub.add_parser("init", help="Initialize .bottleneck state")
    root_arg(p); p.add_argument("--project"); p.add_argument("--force", action="store_true"); p.set_defaults(func=cmd_init)

    p = sub.add_parser("status", help="Show compact protocol state")
    root_arg(p); p.add_argument("--json", action="store_true"); p.set_defaults(func=cmd_status)

    p = sub.add_parser("freeze-contract", help="Freeze architecture contract")
    root_arg(p); p.add_argument("--force", action="store_true"); p.add_argument("--note"); p.set_defaults(func=cmd_freeze_contract)

    p = sub.add_parser("add", help="Add a SKELETON slice")
    root_arg(p); p.add_argument("slice_id"); p.add_argument("--title"); p.add_argument("--gates", help="Comma-separated closure gates")
    p.set_defaults(func=cmd_add)

    p = sub.add_parser("activate", help="Occupy the single production WIP slot")
    root_arg(p); p.add_argument("slice_id"); p.set_defaults(func=cmd_activate)

    p = sub.add_parser("gate", help="Pass/fail a closure gate for ACTIVE slice")
    root_arg(p); p.add_argument("slice_id"); p.add_argument("gate")
    p.add_argument("--pass", dest="passed", action="store_true"); p.add_argument("--fail", dest="failed", action="store_true")
    p.add_argument("--evidence", action="append", default=[]); p.add_argument("--no-evidence", action="store_true")
    p.set_defaults(func=cmd_gate)

    p = sub.add_parser("capsule", help="Create/locate the context capsule template")
    root_arg(p); p.add_argument("slice_id"); p.add_argument("--force", action="store_true"); p.set_defaults(func=cmd_capsule)

    p = sub.add_parser("close", help="Close ACTIVE slice after gates and capsule")
    root_arg(p); p.add_argument("slice_id"); p.add_argument("--force", action="store_true"); p.set_defaults(func=cmd_close)

    p = sub.add_parser("reopen", help="Reopen a CLOSED slice; consumes WIP slot")
    root_arg(p); p.add_argument("slice_id"); p.add_argument("--reason", required=True); p.add_argument("--reset-gates")
    p.set_defaults(func=cmd_reopen)

    p = sub.add_parser("score", help="Compute Impact × Uncertainty × Reusability")
    p.add_argument("--impact", type=int, required=True); p.add_argument("--uncertainty", type=int, required=True); p.add_argument("--reusability", type=int, required=True)
    p.set_defaults(func=cmd_score)

    p = sub.add_parser("audit", help="Audit WIP state and heuristic codebase risks")
    root_arg(p); p.add_argument("--json", action="store_true"); p.set_defaults(func=cmd_audit)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
