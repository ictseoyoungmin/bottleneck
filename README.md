<div align="center">
  <img src="skills/bottleneck/assets/icon.svg" width="96" height="96" alt="Bottleneck icon">
  <h1>Bottleneck v1.0.0</h1>
  <p><strong>AI-Native WIP-Constrained Production Protocol</strong></p>
</div>

Bottleneck is a portable agent skill for large, multi-step work where shallow breadth causes context pollution, duplicate implementations, orphan code, and low-quality accumulation.

It replaces “build everything minimally, then improve everything” with:

> **Sketch wide → Freeze contracts → Build one slice deeply → Harden → Assetize → Close → Compress → Advance**

## Skill payload

The distributable payload lives under `skills/bottleneck/`. It contains only files an
agent may need at runtime:

- `SKILL.md` — the skill contract and instructions.
- `agents/openai.yaml` — optional Codex UI metadata.
- `references/`, `scripts/`, `templates/`, and `assets/` — progressive-disclosure resources.

Repository documentation, examples, evals, tests, manifests, and Claude marketplace
metadata remain at the repository root and are not part of the skill payload.

## Invocation

Use the skill by name or slash command:

```text
/bottleneck
```

After installation, invoke the skill as `$bottleneck` in Codex or `/bottleneck`
in Claude Code. The canonical entry point is always `skills/bottleneck/SKILL.md`.

## Installation

### Claude Code, Codex, and other compatible agents

The repository follows the open agent skills layout, so the Vercel `skills` CLI can
discover `skills/bottleneck/SKILL.md` directly:

```bash
npx skills add ictseoyoungmin/bottleneck --skill bottleneck --agent claude-code --agent codex --global --copy --yes
```

For a local checkout, replace the repository argument with `.`. Omit `--global` to
install into the current project.

### Claude Code plugin installation

This repository also includes a Claude marketplace and plugin manifest:

```text
/plugin marketplace add ictseoyoungmin/bottleneck
/plugin install bottleneck@bottleneck
```

Marketplace installation uses `skills/bottleneck/` as the plugin source, so the
installed plugin contains the runtime payload instead of repository docs, tests,
or evals. Claude Code plugin skills are namespaced; invoke this install as
`/bottleneck:bottleneck`.

Validate a local checkout with:

```bash
claude plugin validate .
claude --plugin-dir .
```

### Codex local discovery

Codex discovers installed skills from its `.agents/skills` locations. After the
`npx skills add` command, start Codex and invoke it explicitly with `$bottleneck`,
or let the description trigger it implicitly.

## Package contents

- `skills/bottleneck/SKILL.md` — primary behavior contract and activation description.
- `skills/bottleneck/references/` — state, contract, closure, context, selection, anti-patterns, domain adapters.
- `skills/bottleneck/templates/` — persistent project artifacts.
- `skills/bottleneck/scripts/bottleneck.py` — optional zero-dependency WIP=1 state harness and audit.
- `tests/` — regression tests for the harness (development-only).
- `evals/evals.json` — behavioral eval cases for the skill itself (development-only).
- `examples/` — domain examples.
- `skills/bottleneck/assets/icon.svg` — text-free symbolic icon.
- `.claude-plugin/` — Claude Code plugin and marketplace manifests.
- `.codex-plugin/` — Codex plugin manifest.

## Development checks

```bash
python3 -m unittest discover -s tests -v
claude plugin validate .
```

The checks above use only repository files and installed CLIs; they do not depend on
an agent's private skill installation paths.

## Design principles

1. **Production WIP = 1.**
2. **Parallelize uncertainty; serialize commitment.**
3. **Implementation may be temporary; architecture contracts may not.**
4. **No second production implementation before retiring or replacing the first.**
5. **Define closure before deep implementation.**
6. **Closed slices become reusable assets and compressed context capsules.**
7. **A stopped project should still leave valuable finished components.**


## Example Usages

Bottleneck is useful when a project has many dependent parts and unfinished work can accumulate faster than it can be reviewed.

### Build a large product without spreading quality thin

> Build an analytics platform with dashboards, alerts, reports, team management, and billing.  
> Use Bottleneck. Keep the whole architecture visible, but only allow one production slice to be ACTIVE at a time.

Bottleneck may sketch the full system first, then select one slice:

```text
SYSTEM SKELETON
├── Dashboard  ← ACTIVE
├── Alerts
├── Reports
├── Team
└── Billing
```

The Dashboard is taken through implementation, edge cases, tests, visual QA, and integration before it becomes CLOSED. Only then does the next slice become active.

### Recover a chaotic codebase

This repository has duplicated implementations, dead code, and several half-finished workflows. Use Bottleneck to recover it.

Instead of refactoring everything at once:

```text
Map the system
→ choose one unresolved responsibility
→ make one path authoritative
→ migrate callers
→ test
→ remove obsolete paths
→ CLOSED
```

Then advance to the next bottleneck.

### Reopen work when new evidence disproves closure

We finished this feature, but production usage exposed a serious regression. Reopen it and fix the problem before continuing.

```text
CLOSED
  ↓
REOPENED
  ↓
ACTIVE
  ↓
VERIFY
  ↓
RECLOSED
```

Previous closure checks are rerun so fixing one problem does not silently introduce another.

### Typical invocation

> Use Bottleneck. Sketch the whole system, select the highest-value unresolved production slice, finish and verify it deeply, close it, then advance.

Bottleneck limits unresolved work, not ambition.

## License

Licensed under the [Apache License 2.0](LICENSE).
