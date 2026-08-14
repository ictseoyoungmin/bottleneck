# Anti-Patterns

## Horizontal pseudo-completion

Every subsystem exists, but every subsystem is weak.

Symptom: the project looks complete in a feature checklist while no component is independently production-grade.

## Version accretion

Examples:

```text
renderer.js
renderer2.js
renderer_final.js
renderer_new.js
renderer_legacy_adapter.js
```

Replace and retire instead of accumulating parallel candidates.

## Orphan-by-refactor

New routes or state owners are added without proving the old path is disconnected.

## Context archaeology

The next agent must infer current truth from months of logs, TODOs, patches, and contradictory docs.

Fix: CLOSED capsules plus authoritative state.

## Premature global refactor

An ACTIVE slice becomes an excuse to rename/restructure unrelated modules.

Fix: change only contract-relevant dependencies.

## Fake skeleton

A “placeholder” contains enough bespoke behavior that it becomes another implementation requiring maintenance.

A proper skeleton preserves shape with minimal behavior.

## Unmeasured production-ready claim

“Looks good” or “works now” substitutes for predefined closure gates.

## Zombie experiment

A spike is wired into production “temporarily” and survives indefinitely.

Experiments must have an explicit delete/graduate decision.
