---
name: bottleneck
description: >-
  AI-native production workflow for large, multi-step, long-running, or multi-surface work. Keep the whole artifact visible, select one dominant production bottleneck at a time, define closure before deep work, harden through construction → observation → correction → validation, reopen upstream work when assumptions fail, compress genuinely closed work into reusable context, then advance. Use for software and agentic coding, 3D/visual asset hardening, simulations, dashboards, research/data, creative production, reusable asset production, complex refactors or rewrites, context-pollution control, duplicate implementation prevention, and recovery of projects with many partial implementations. Explicit invocations include /bottleneck, bottleneck workflow, WIP=1, deep slice, hardening loop, finish one bottleneck first, and AI-native production harness.
---

# Bottleneck

> **See whole. Build narrow. Correct deeply. Close only when good. Reopen when wrong. Advance.**

Bottleneck is not an MVP method. It is an **agent-driven production workflow and WIP-control protocol**.

It governs how work is selected, hardened, closed, reopened, and advanced. It is **not** a product architecture, runtime architecture, code organization, scene graph, mesh hierarchy, research ontology, or artifact structure.

The objective is not to reduce ambition. The objective is to limit unresolved production commitments while preserving whole-artifact correctness and quality.

## Core law

**Production WIP Limit = 1 dominant bottleneck.**

Only one production bottleneck may be `ACTIVE` for deep quality expansion at a time. Everything else must be one of:

- `SKELETON` — enough structure, context, placeholder, or reference to preserve the whole.
- `CLOSED` — genuinely at target quality for its declared scope, integrated where applicable, and compressed into stable context.
- `REOPENED` — previously closed work explicitly reopened because new evidence invalidated its premise or quality claim; while being changed it consumes the single ACTIVE slot.

Exploratory spikes are allowed only when they are disposable, isolated, clearly labeled, and do not become a second production commitment.

## Prime directive

**Parallelize uncertainty. Serialize commitment.**

You may explore multiple approaches cheaply. Do not keep multiple competing production paths alive merely because choosing is uncomfortable.

## Non-negotiable guardrails

1. **Workflow only.** Bottleneck states and slices are work-management concepts. Never reshape product architecture, runtime design, code modules, file layout, scene structure, mesh hierarchy, or artifact topology merely to mirror `SKELETON`/`ACTIVE`/`CLOSED`/`REOPENED` bookkeeping. The workflow follows the artifact; the artifact does not follow the workflow bookkeeping.
2. **Macro correctness comes first.** Do not descend into detail while the overall silhouette, major relationships, primary behavior, key UX, composition, or other high-level premise is still wrong. If downstream work reveals an upstream premise is false, REOPEN the responsible upstream work even if it was previously CLOSED.
3. **One dominant problem × the smallest coherent scope needed to solve it.** Slice boundaries are pragmatic, not doctrinal. Do not force `one capability × one scope` when tightly coupled parts must move together for the whole result to improve.
4. **Closure is quality-based.** Tests, checklists, screenshots, metrics, comparison boards, renders, benchmarks, and QA gates are evidence, not closure by themselves. Never mark low-quality work CLOSED merely because verification artifacts exist or automated gates pass.
5. **Production precedes verification theater.** Prefer `construction → observation → correction → validation`. Observation and validation should reveal what to fix; they must not become a substitute for producing the right artifact.
6. **Highest-impact bottleneck first.** Prioritize what most limits perceived or actual final quality. Stop polishing an issue once it is no longer the dominant constraint and move to the next bottleneck.
7. **Declare closure before deep work.** State what will change, what intentionally will not change, and what observable state qualifies as CLOSED before beginning the hardening pass.

These guardrails override slice bookkeeping, gate completion, local convenience, and premature optimization when those mechanisms conflict with whole-artifact correctness or quality.

## When activated

For a broad request, do **not** implement or polish the whole request shallowly.

1. Inspect the current artifact, repository, workspace, references, and existing work before inventing new paths.
2. Recover a compact whole-artifact sketch: macro shape, major relationships, primary behavior/UX, authoritative references, and critical constraints.
3. Identify only the upstream assumptions whose instability could invalidate deep work. Resolve those uncertainties without inventing architecture for the sake of Bottleneck.
4. Select exactly one dominant bottleneck.
5. Define its `Definition of Closed` before deep implementation or hardening, including `change`, `do not change`, and `closed when`.
6. Deep-build or harden only the coherent scope needed to solve that bottleneck.
7. Observe the real artifact, correct the largest remaining mismatch, then validate.
8. Integrate the result and retire superseded production paths where applicable.
9. Create a compact context capsule for genuinely closed work.
10. Only then select the next dominant bottleneck.

If the user asks for an entire large product or asset in one turn, preserve the whole-artifact context and take the highest-impact bottleneck as far toward genuine closure as possible. Do not manufacture shallow breadth merely to claim completion.

## Step 0 — inspect before inventing

Before production work, search the repository, workspace, scene, references, or project state for what is already authoritative.

Depending on the domain, inspect for:

- existing implementations, assets, meshes, rigs, materials, datasets, analyses, or decisions with the same responsibility,
- `legacy`, `old`, `new`, `v2`, `final`, `tmp`, `draft`, `copy`, `backup`, or parallel variants,
- duplicate state/reference owners,
- stale routes, adapters, materials, nodes, export paths, or analysis paths,
- TODO/STUB/PLACEHOLDER surfaces,
- authoritative schemas, interfaces, coordinate systems, scale/unit conventions, reference views, cameras, tests, benchmarks, or evaluation criteria.

Do not create `foo2`, `foo_new`, `foo_final`, a parallel renderer/controller/service, or an equivalent duplicate asset merely because modifying the existing path feels harder.

If replacing an implementation or asset path, isolate the experiment, choose a winner, migrate/integrate, then remove or explicitly retire the loser where safe.

Read `references/anti-patterns.md` when several competing production paths already exist.

## Step 1 — see the whole, once

Create a lightweight whole-artifact sketch containing only what is needed to avoid local optimization.

Useful elements include, where relevant:

- overall silhouette, composition, information architecture, or system shape,
- major modules, domains, asset parts, scenes, or analysis units,
- authoritative state/reference owners,
- major spatial, data, control, causal, kinematic, or interaction relationships,
- public/integration boundaries,
- lifecycle or production stages,
- coordinate, scale, unit, time, camera/FOV, or reference-registration conventions,
- major performance/quality budgets,
- external dependencies and hard constraints.

Do not flesh out every part. This sketch is reasoning context for production work; **Bottleneck does not require the artifact itself to adopt the sketch as its architecture.**

Use `templates/system-sketch.md` when the workspace benefits from a persistent artifact.

## Step 2 — stabilize only upstream assumptions that matter

Do not freeze architecture merely because Bottleneck prefers stable work.

Instead, identify the **smallest set of upstream assumptions** whose change would invalidate the selected bottleneck after deep work. Respect existing authoritative architecture or artifact structure when it is already sound.

Examples:

- software: an existing public API, state owner, schema, coordinate/time convention, or lifecycle invariant,
- 3D/visual: reference registration, overall proportions, scale/axes, major pose, skeleton convention, or comparison camera/FOV,
- simulation: solver semantics, units, time step, collision conventions, or canonical state,
- research/data: hypothesis framing, dataset identity, metric definition, provenance, or statistical assumptions,
- creative production: character/world invariants, continuity, style constraints, or causal obligations.

If an upstream uncertainty could materially invalidate the bottleneck, run the cheapest disposable experiment capable of resolving it. Do not productionize through a false premise.

If the project already uses stable software contracts, `references/contract-freeze.md` explains how to treat them as **project constraints**, not as Bottleneck-imposed architecture.

## Step 3 — select one dominant bottleneck

Rank candidate bottlenecks using:

`Priority = Impact × Uncertainty × Reusability`

Prefer bottlenecks that:

- strongly determine final perceived or actual quality,
- contain uncertainty that could invalidate downstream work,
- unlock dependent work or become reusable knowledge/assets.

Use the formula as a heuristic, not a mechanical optimizer. Macro correctness and hard dependencies override the score.

A bottleneck is a **problem**, not necessarily a module or capability. Its coherent scope may span multiple tightly coupled concerns.

Example: if a character shoulder silhouette is wrong because clavicle pose, torso contour, upper-arm placement, and camera perspective interact, treat that coupled set as one bottleneck instead of closing four locally correct but globally inconsistent slices.

Use `templates/bottleneck-card.md` to record the selected bottleneck.

## Step 4 — define closure before building

Before deep work, declare:

```text
CHANGE: <what may change to solve this bottleneck>
DO NOT CHANGE: <stable areas intentionally outside scope>
CLOSED WHEN: <observable target-quality condition>
```

Then add only the gates relevant to the bottleneck.

Typical evidence may include:

- correctness and specified invariants,
- visual or perceptual quality where applicable,
- representative edge/error/empty/extreme states,
- performance budget,
- integration through the real boundary,
- automated tests/evals appropriate to the domain,
- comparison renders or representative screenshots,
- duplicate/dead/orphan production-path check,
- documentation or context capsule.

**Evidence is necessary where useful, but passing evidence gates is not sufficient if the artifact is visibly, behaviorally, structurally, or scientifically below target quality.**

Read `references/definition-of-closed.md` for gate design.

## Step 5 — deep build and correct

While a bottleneck is ACTIVE:

- do not quality-expand unrelated areas merely because they are easy,
- do not refactor or reorganize unrelated structure for aesthetic consistency,
- do not create alternate production paths without a bounded disposable experiment,
- keep placeholders, mocks, proxies, and reference approximations explicit,
- respect the artifact's real interfaces and relationships,
- spend the quality budget on the selected dominant problem,
- keep tightly coupled causes together when separating them would harm the whole.

Use the default loop:

```text
construction
→ observation of the real artifact
→ correction of the largest remaining mismatch
→ validation that the correction holds
→ repeat if the bottleneck still materially limits quality
```

For software, observation may be execution, logs, profiler traces, UI behavior, or real integration.

For 3D/visual work, observation should use actual renders/viewports against authoritative references; correction may legitimately span mesh, rig, material, lighting, or comparison camera when those causes are coupled.

For research/data/business work, replace render loops with the domain's real evidence/evaluation loop.

## Step 6 — harden and assetize

A bottleneck is not closed merely because the happy path works or a comparison board exists.

Harden it until the declared target quality is real. Then make the result independently useful where practical:

- stable integration surface or export,
- fixtures/example inputs/reference cases,
- automated verification where appropriate,
- usage documentation,
- standalone demo, render set, reproducible example, benchmark, notebook, or asset,
- explicit budgets, assumptions, and limitations,
- integration notes.

The project should retain value even if work stops after this bottleneck.

## Step 7 — close and compress

On closure:

1. confirm the actual artifact meets `CLOSED WHEN`, not merely that gates were executed,
2. remove obsolete or duplicate production paths where safe,
3. record only the evidence needed to justify and reproduce the closure claim,
4. mark the bottleneck `CLOSED`,
5. replace unnecessary implementation history in working context with a **Context Capsule**.

A capsule should contain only what the next worker needs, such as:

- authoritative outputs or artifact location,
- required inputs/references,
- invariants and important relationships,
- stable boundaries or constraints,
- budgets/quality targets,
- known limitations,
- evidence/test/render locations,
- integration notes,
- reopen conditions.

Do not summarize away the address of authoritative sources. Compression must remain resolvable.

Use `templates/close-capsule.md`.

## Step 8 — advance or reopen

Choose the next bottleneck only after the current one is no longer the dominant unresolved constraint or has genuinely reached closure.

A CLOSED result is not sacred. Reopen it when new evidence shows that:

- its quality claim was premature,
- an upstream assumption was false,
- a macro relationship is wrong,
- downstream integration exposes a hidden defect,
- user-visible quality is materially limited by it again.

To modify CLOSED work, record:

- reason,
- triggering evidence/change,
- affected scope and upstream/downstream implications,
- what remains intentionally untouched,
- expected closure condition.

A reopened bottleneck consumes the single production WIP slot while being changed.

Use `templates/reopen-record.md`.

## Mandatory refusal patterns

Push back on these patterns even when they look faster:

- “Implement every feature roughly first.”
- “Keep the old implementation just in case.”
- “Make a second final version and switch later.”
- “Reshape the architecture or scene hierarchy so it matches Bottleneck slices.”
- “Split tightly coupled causes merely to preserve one capability × one scope.”
- “Keep polishing details while the macro silhouette/behavior/UX premise is wrong.”
- “Call this CLOSED because tests, screenshots, metrics, or QA artifacts pass.”
- “Generate more validation material instead of correcting the artifact.”
- “Continue downstream after upstream evidence invalidates the current premise.”
- “Give the next agent the entire history instead of a resolvable capsule.”

## Lightweight output format

When applying the skill conversationally, keep visible status compact:

```text
WHOLE: <macro state / key upstream assumptions>
ACTIVE: <one dominant bottleneck>
BOUNDARY: <change / do not change>
CLOSED: <genuinely closed reusable work>
NEXT GATE: <single nearest target-quality condition>
```

Do not bury the user in process narration. The workflow exists to improve the artifact, not to make project management the artifact.

## Optional harness

If the workspace can run Python, `scripts/bottleneck.py` provides a zero-dependency WIP=1 state harness:

```bash
python scripts/bottleneck.py init
python scripts/bottleneck.py status
python scripts/bottleneck.py add tree-system
python scripts/bottleneck.py activate tree-system
python scripts/bottleneck.py gate tree-system correctness --pass --evidence tests/tree.txt
python scripts/bottleneck.py close tree-system
python scripts/bottleneck.py audit
```

The harness stores workflow state under `.bottleneck/`. Its state files are **project-management metadata only** and must not dictate runtime architecture, scene structure, or artifact topology.

The legacy `freeze-contract` harness command may still be useful for software projects that already have explicit contracts, but it is optional and is not a core Bottleneck law.

## Reference map

Read only what the task needs:

- `references/state-model.md` — state transitions and WIP semantics.
- `references/contract-freeze.md` — treating existing software contracts as upstream project constraints without making Bottleneck an architecture method.
- `references/bottleneck-selection.md` — candidate ranking, macro/dependency overrides, and coherent scope.
- `references/definition-of-closed.md` — quality-first closure and relevant evidence gates.
- `references/context-compression.md` — minimal sufficient authoritative context.
- `references/anti-patterns.md` — duplicate/orphan implementation failure modes.
- `references/domain-adapters.md` — software, 3D/visual, simulation, research, business, and creative adaptations.

## Success condition

Bottleneck succeeds when a large project can stop at any point and still contain:

- a coherent whole-artifact shape or skeleton,
- no known macro error being hidden by closed detail work,
- no ambiguous competing production path for closed responsibilities where applicable,
- at least one genuinely high-quality reusable closed result,
- compressed authoritative context that allows a new agent to continue safely,
- freedom for the product or artifact to keep the architecture and structure appropriate to its own domain.

**Limit unresolved production commitments, not ambition.**
