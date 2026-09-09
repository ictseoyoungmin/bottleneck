# Bottleneck Selection

The next bottleneck should maximize downstream leverage, not merely be the easiest visible task.

## Default score

```text
Priority = Impact × Uncertainty × Reusability
```

Score each dimension 1–5 when a rough ranking helps.

### Impact
How strongly does this problem determine perceived or actual final quality?

### Uncertainty
How much technical, perceptual, conceptual, or evidential uncertainty could invalidate later work?

### Reusability
If the project stops, can the result remain useful as a module, asset, method, dataset, benchmark, decision artifact, or authoritative correction?

## Overrides

The score is only a heuristic.

Use these overrides first:

1. **Macro correctness override** — if silhouette, major relationships, core behavior, primary UX, framing, or another upstream premise is materially wrong, fix that before detail.
2. **Dependency override** — resolve an upstream assumption when downstream work would otherwise be built on an unstable or false premise.
3. **Whole-quality override** — do not choose a locally convenient task when it barely changes the user's perceived or actual quality.

## Scope rule

Use:

> **One dominant problem × the smallest coherent scope needed to solve it.**

Do not mechanically force `one capability × one scope`.

A coherent bottleneck may cross module, mesh, rig, material, camera, UI component, dataset, or analysis boundaries when those parts are tightly coupled causes of the same dominant problem. Workflow scope does not dictate artifact architecture.

## Prefer

- the macro silhouette/proportion error before secondary surface detail in a 3D asset,
- rendering/physics/input correctness before decorative menus in an interactive world,
- canonical data/replay semantics before analytics chrome,
- a real high-value user task before six placeholder widgets,
- a validated hypothesis before polishing a full research narrative,
- a resolved acquisition channel experiment before a complete business-plan deck.

## Avoid

- selecting based on implementation convenience,
- polishing low-impact chrome because it is easy,
- polishing micro detail while a macro premise is still wrong,
- choosing work that depends on an unresolved upstream assumption likely to invalidate it,
- splitting tightly coupled causes just to make slices look cleaner,
- using high uncertainty as an excuse to productionize several alternatives.
