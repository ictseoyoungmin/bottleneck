# Definition of Closed

Closure is a **predeclared target-quality condition**, supported by relevant evidence.

Before deep work, declare:

```text
CHANGE: <what may change>
DO NOT CHANGE: <what stays outside this bottleneck>
CLOSED WHEN: <observable state that represents target quality>
```

Choose only gates relevant to the bottleneck, but do not omit a gate merely because it is inconvenient.

## Quality outranks gate completion

Tests, checklists, screenshots, renders, comparison boards, metrics, benchmarks, and QA reports are evidence. They are **necessary where useful, but never sufficient by themselves**.

Do not close work when the actual artifact is visibly, behaviorally, structurally, scientifically, or operationally below the declared target quality.

If the local gates pass but a macro premise is wrong, reopen the responsible upstream work instead of preserving local closure.

## General evidence gates

- **Correctness** — specified behavior and invariants hold.
- **Whole-artifact fit** — the bottleneck no longer violates known macro relationships or upstream premises.
- **Edge states** — relevant error, empty, loading, malformed, extreme, or degraded states are handled.
- **Performance** — relevant latency, CPU, GPU, memory, throughput, or size budgets are measured where material.
- **Integration** — exercised through the real artifact boundary where applicable.
- **Verification** — unit/integration/E2E/eval/simulation checks appropriate to the domain.
- **Documentation/context** — use, limitations, important assumptions, and reopen conditions are recorded.
- **Duplication** — no ambiguous second active production path for the same responsibility where applicable.
- **Orphan/dead paths** — superseded routes/files/adapters/assets are retired where safely demonstrable.
- **Independent value** — demo, fixture, notebook, reproducible case, library, render set, or asset where practical.
- **Context capsule** — the next agent can use the result without loading unnecessary internal history.

## Visual / 3D / interactive additions

- macro silhouette/proportion/pose or primary UX is not knowingly wrong,
- representative actual renders/viewports/screenshots,
- authoritative-reference comparison where available,
- required camera/viewpoint coverage,
- interaction/animation/rig/export states where relevant,
- penetration/clearance/topology/material checks only when they materially affect the target,
- frame-time, draw, memory, or asset-size budget where relevant.

A dense QA board does not compensate for an inaccurate mesh, wrong pose, broken interaction, or poor visual read.

## Research / data additions

- assumptions declared,
- provenance recorded,
- reproducible analysis,
- falsification or counter-evidence considered,
- uncertainty reported,
- the claim matches the actual strength of evidence rather than pipeline completion.

## Business / strategy additions

- measurable hypothesis,
- source/evidence traceability,
- constraint realism,
- decision rule for adoption/rejection,
- explicit unknowns,
- decision quality rather than deck/report completeness.
