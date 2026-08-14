# Bottleneck Selection

The next slice should maximize downstream leverage, not merely be the easiest visible task.

## Default score

```text
Priority = Impact × Uncertainty × Reusability
```

Score each dimension 1–5.

### Impact
How strongly does this slice determine perceived or actual final quality?

### Uncertainty
How much technical or conceptual uncertainty can invalidate later work?

### Reusability
If the project stops, can this slice remain useful as a module, asset, method, dataset, benchmark, or decision artifact?

## Dependency override

Use dependency order when a slice's contract is required for all other candidates.

## Prefer

- rendering/physics/input core before decorative menus in an interactive world,
- canonical data/replay semantics before analytics widgets,
- a real high-value chart before six placeholder charts,
- a validated hypothesis before polishing a full research narrative,
- a resolved acquisition channel experiment before a complete business-plan deck.

## Avoid

- selecting based on implementation convenience,
- polishing low-impact chrome because it is easy,
- choosing a slice that depends on an unfrozen architecture,
- using high uncertainty as an excuse to productionize several alternatives.
