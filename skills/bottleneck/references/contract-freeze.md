# Existing Contracts as Upstream Constraints

Bottleneck is not an architecture method. It must not invent or freeze product architecture merely to make workflow slices easier to manage.

This reference applies when a project already has software or system contracts whose instability could invalidate deep work.

## Purpose

Before taking a bottleneck deep, identify the **smallest set of existing upstream constraints** whose change would make that work invalid or misleading.

Treat those constraints as project facts for the duration of the active bottleneck unless evidence requires reopening them.

Possible software constraints include:

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

These are **not Bottleneck-prescribed architecture**. They matter only when they are already authoritative or when the project itself requires them.

## Do not over-freeze

Do not freeze merely for workflow convenience:

- private helper names,
- internal folder shape unless externally relevant,
- local implementation technique,
- reversible visual details,
- speculative extension points,
- module boundaries invented solely to match a slice,
- scene graph, mesh hierarchy, or asset structure invented solely to match ACTIVE/CLOSED bookkeeping.

The workflow follows the artifact's real structure.

## Reopen instead of protecting a false premise

If new evidence shows an upstream constraint or assumption is wrong, do not preserve it merely because downstream work was already closed.

Reopen the responsible upstream work, assess affected downstream scope, correct the premise, and then revalidate what depended on it.

## Architecture-invalidating uncertainty

If an unresolved decision could materially invalidate the selected bottleneck, run the cheapest disposable experiment capable of resolving it before deep production work.

Examples:

- WebGL pipeline supports the required instancing count?
- selected database isolation can satisfy replay semantics?
- target model format preserves the required rigging?
- chosen statistical model is identifiable with available data?

The experiment is a spike, not a second production path.

For non-software domains, use the same idea with domain-appropriate upstream assumptions: reference registration, scale/axes, camera/FOV, macro proportions, solver semantics, dataset identity, hypothesis framing, continuity, or other constraints that can invalidate downstream work.
