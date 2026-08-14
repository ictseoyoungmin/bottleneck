---
name: bottleneck
description: >-
  AI-native production discipline for large, multi-step, long-running, or multi-module work. Sketch the whole system once, freeze the architecture contract, allow only one production slice to be ACTIVE at a time, take that slice to final-quality closure, compress it into a reusable context capsule, then advance. Use for complete apps/sites/games/open worlds/dashboards/simulators, production-ready modules, complex refactors or rewrites, codebase expansion, agentic coding, vertical/deep slices, context-pollution control, duplicate implementation prevention, orphan/dead-code reduction, reusable asset production, and recovery of projects with many partial implementations. Explicit invocations include /bottleneck, bottleneck workflow, WIP=1, deep slice, finish one module first, and AI-native production harness.
---

# Bottleneck

> **Sketch wide. Build narrow. Finish deep. Freeze. Reuse. Advance.**

Bottleneck is not an MVP method. It is a **production WIP-control protocol for AI agents**.

The objective is not to reduce ambition. The objective is to limit the number of unresolved production implementations the agent must reason about at once.

## Core law

**Production WIP Limit = 1.**

Only one slice may be `ACTIVE` for production-quality expansion. Everything else must be one of:

- `SKELETON` — contract, routing, stub, fixture, or placeholder only.
- `CLOSED` — hardened, integrated, documented, and compressed into a stable capsule.
- `REOPENED` — a previously closed slice explicitly reopened with a reason and impact scope; it consumes the single ACTIVE slot while being changed.

Exploratory spikes are allowed only when they are disposable, isolated, clearly labeled, and do not become a second production implementation.

## Prime directive

**Parallelize uncertainty. Serialize commitment.**

You may explore multiple approaches cheaply. You may not keep multiple competing production implementations alive.

## When activated

For a broad request, do **not** implement the whole request shallowly.

1. Inspect the current project before creating new paths.
2. Produce or recover a one-screen system sketch.
3. Freeze the architecture contract that must remain stable across slices.
4. Select exactly one bottleneck slice.
5. Define its `Definition of Closed` before deep implementation.
6. Deep-build only that slice to final-quality closure.
7. Integrate it back into the skeleton and run hardening gates.
8. Delete or retire superseded implementations.
9. Create a context capsule for the closed slice.
10. Only then select the next slice.

If the user asks for an entire large product in one turn, deliver the **wide skeleton plus one genuinely closed production slice**, unless the user explicitly overrides this method after seeing the tradeoff.

## Step 0 — inspect before inventing

Before implementation, search the repository or workspace for:

- existing modules with the same responsibility,
- `legacy`, `old`, `new`, `v2`, `final`, `tmp`, `draft`, `copy`, `backup` variants,
- duplicate state owners,
- stale routes and adapters,
- TODO/STUB/PLACEHOLDER surfaces,
- authoritative schemas, interfaces, and tests.

Do not create `foo2`, `foo_new`, `foo_final`, or a parallel renderer/controller/service merely because modifying the existing path feels harder.

If replacing an implementation, isolate the experiment, choose a winner, migrate, then remove or explicitly retire the loser.

Read `references/anti-patterns.md` when a codebase already contains several competing implementations.

## Step 1 — sketch wide, once

Create a lightweight system sketch containing only what is needed to reason about boundaries:

- major modules or domains,
- authoritative state owners,
- data/control flow,
- public interfaces,
- lifecycle,
- persistence boundaries,
- coordinate/time conventions where relevant,
- major performance budgets,
- external dependencies.

Do not flesh out every module.

Use `templates/system-sketch.md` when the workspace needs a persistent artifact.

## Step 2 — freeze the contract

Implementation may be placeholder. **Architecture contracts may not be placeholder.**

Freeze the smallest set of decisions whose later change would invalidate closed work:

- state ownership,
- module boundaries,
- schemas/types,
- public APIs,
- coordinate/time systems,
- lifecycle and disposal,
- persistence/versioning rules,
- error semantics,
- performance envelopes.

If an architecture-invalidating uncertainty is unresolved, run a disposable spike first. Do not productionize through the uncertainty.

Read `references/contract-freeze.md` when the project has unstable foundations.

## Step 3 — select one bottleneck

Rank candidate slices using:

`Priority = Impact × Uncertainty × Reusability`

Prefer slices that:

- strongly affect final quality,
- carry technical uncertainty that could invalidate later work,
- can become reusable assets or stable infrastructure.

Do not optimize the score mechanically. A hard architectural dependency may override the ranking.

Use `templates/bottleneck-card.md` to record the selected slice.

## Step 4 — define closure before building

Before deep implementation, declare the slice's Definition of Closed.

Typical closure gates:

- correctness,
- visual quality if applicable,
- edge/error/empty states,
- performance budget,
- API stability,
- integration smoke test,
- automated tests appropriate to the domain,
- documentation/ADR,
- duplicate implementation check,
- dead/orphan path check,
- independent demo or fixture,
- context capsule.

Do not let “production-ready” remain a verbal judgment.

Read `references/definition-of-closed.md` for gate design.

## Step 5 — deep build

While a slice is ACTIVE:

- do not quality-expand unrelated skeleton modules,
- do not refactor unrelated code for aesthetic consistency,
- do not add speculative infrastructure outside the contract,
- do not create alternate production paths,
- keep mocks/fixtures explicit,
- use the real public contract at integration boundaries,
- spend quality budget on the selected slice.

For visual/interactive work, harden the slice through repeated render/inspect/fix loops instead of breadth expansion.

For data/research/business work, replace render loops with the domain's evidence/evaluation loop.

## Step 6 — harden and assetize

A slice is not closed merely because the happy path works.

Harden it, then make it independently valuable where practical:

- stable public API,
- fixtures or example inputs,
- automated verification,
- usage documentation,
- standalone demo or reproducible example,
- explicit budgets and limitations,
- integration contract.

The project should retain value even if work stops after this slice.

## Step 7 — close and compress

On closure:

1. remove obsolete or duplicate paths,
2. record the evidence that closure gates passed,
3. mark the slice `CLOSED`,
4. replace implementation detail in working context with a **Context Capsule**.

A capsule should contain only:

- public API / outputs,
- required inputs,
- invariants,
- ownership boundaries,
- budgets,
- known limitations,
- evidence/test locations,
- integration notes,
- reopen conditions.

Do not summarize away the address of authoritative sources. Compression must remain resolvable.

Use `templates/close-capsule.md`.

## Step 8 — advance or reopen

Choose the next bottleneck only after the current one is closed.

To modify a CLOSED slice, explicitly reopen it with:

- reason,
- triggering evidence/change,
- affected contract surface,
- migration risk,
- expected closure gates.

A reopened slice consumes the single production WIP slot.

Use `templates/reopen-record.md`.

## Mandatory refusal patterns

Push back on these implementation patterns even when they look faster:

- “Implement every feature roughly first.”
- “Keep the old implementation just in case.”
- “Make a second final version and switch later.”
- “Refactor the entire project while touching this module.”
- “Call this production-ready without measurable gates.”
- “Give the next agent the entire history instead of a capsule.”
- “Add visual polish everywhere while the ACTIVE slice is unfinished.”

## Lightweight output format

When applying the skill conversationally, keep the visible status compact:

```text
SYSTEM: sketched / contract frozen
ACTIVE: <one slice>
SKELETON: <major untouched areas>
CLOSED: <closed reusable slices>
NEXT GATE: <single nearest closure gate>
```

Do not bury the user in process narration. The protocol exists to improve the artifact, not to make project management the artifact.

## Optional harness

If the workspace can run Python, `scripts/bottleneck.py` provides a zero-dependency state harness:

```bash
python scripts/bottleneck.py init
python scripts/bottleneck.py status
python scripts/bottleneck.py freeze-contract
python scripts/bottleneck.py add tree-system
python scripts/bottleneck.py activate tree-system
python scripts/bottleneck.py gate tree-system correctness --pass --evidence tests/tree.txt
python scripts/bottleneck.py close tree-system
python scripts/bottleneck.py audit
```

The harness enforces one ACTIVE production slice and stores state under `.bottleneck/`.

## Reference map

Read only what the task needs:

- `references/state-model.md` — state transitions and WIP semantics.
- `references/contract-freeze.md` — what to freeze before production.
- `references/bottleneck-selection.md` — candidate ranking and dependency overrides.
- `references/definition-of-closed.md` — measurable closure gates.
- `references/context-compression.md` — minimal sufficient authoritative context.
- `references/anti-patterns.md` — duplicate/orphan implementation failure modes.
- `references/domain-adapters.md` — software, visual simulation, research, business, and creative adaptations.

## Success condition

Bottleneck succeeds when a large project can stop at any point and still contain:

- a coherent skeleton,
- no ambiguous competing production implementation for closed responsibilities,
- at least one genuinely production-grade reusable slice,
- compressed authoritative context that allows a new agent to continue safely.

**Limit unresolved implementation states, not ambition.**
