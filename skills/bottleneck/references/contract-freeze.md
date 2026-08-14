# Contract Freeze

The purpose of Contract Freeze is to prevent a deeply finished slice from being invalidated by avoidable architectural churn.

Freeze only decisions that are expensive to change after closure.

## Freeze candidates

- canonical state owner,
- module/service ownership boundary,
- input/output schemas,
- public function/event/API surface,
- coordinate system and units,
- time semantics and clocks,
- lifecycle: create/start/update/stop/dispose,
- persistence/version migration rules,
- error and retry semantics,
- concurrency/ordering rules,
- target performance envelope,
- external dependency boundaries.

## Do not over-freeze

Do not freeze:

- private helper names,
- internal folder shape unless externally relevant,
- local implementation technique,
- reversible visual details,
- speculative extension points.

Freeze interfaces and invariants, not every implementation choice.

## Architecture-invalidating uncertainty

If a decision could invalidate the slice after completion, do not guess and proceed. Run the cheapest experiment capable of resolving it.

Examples:

- WebGL pipeline supports required instancing count?
- selected database isolation can satisfy replay semantics?
- target model format preserves required rigging?
- chosen statistical model is identifiable with available data?

The experiment is a spike, not a second production path.
