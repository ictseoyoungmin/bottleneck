# Definition of Closed

Closure is a predeclared measurable contract.

Passing every declared gate is necessary but not sufficient for closure. If direct inspection shows that the artifact remains materially below the target quality, keep the slice `ACTIVE` or `REOPEN` it. Do not use gate completion to overrule obvious whole-artifact quality or correctness failures.

Choose only gates relevant to the slice, but do not omit a gate merely because it is inconvenient.

## General gates

- **Correctness** — specified behavior and invariants hold.
- **Edge states** — error, empty, loading, malformed, extreme, or degraded states are handled.
- **Performance** — relevant latency, CPU, GPU, memory, throughput, or size budgets are measured.
- **Public contract** — stable inputs, outputs, and ownership.
- **Integration** — smoke-tested through the real skeleton boundary.
- **Verification** — unit/integration/E2E/eval/simulation checks appropriate to the domain.
- **Documentation** — use, limitations, and key design decisions.
- **Duplication** — no second active implementation for the same responsibility.
- **Orphan/dead paths** — superseded routes/files/adapters retired where safely demonstrable.
- **Independent value** — demo, fixture, notebook, reproducible case, library, or asset where practical.
- **Context capsule** — next agent can use the slice without loading internal history.

## Visual/interactive additions

- representative screenshots/render captures,
- interaction states,
- responsive/camera/viewpoint coverage,
- visual regression/reference comparison,
- frame-time and draw/memory budget.

## Research/data additions

- assumptions declared,
- provenance recorded,
- reproducible analysis,
- falsification or counter-evidence considered,
- uncertainty reported.

## Business/strategy additions

- measurable hypothesis,
- source/evidence traceability,
- constraint realism,
- decision rule for adoption/rejection,
- explicit unknowns.
