# Domain Adapters

Bottleneck is a **general agent-driven production workflow**, not a software-only rule and not an architecture method.

The common core is always:

```text
see the whole
→ select one dominant problem
→ define change / do-not-change / closed-when
→ construction
→ observation
→ correction
→ validation
→ close or reopen
```

A bottleneck is a problem, not necessarily a module. Use **one dominant problem × the smallest coherent scope needed to solve it**. Keep tightly coupled causes together when separating them would reduce whole-artifact quality.

## Software / agentic coding

Whole-artifact context: existing architecture, authoritative state/data owners, real interfaces, lifecycle, primary UX/behavior, integration boundaries, budgets.

ACTIVE: one dominant production problem taken to target quality. Its workflow scope does not need to match a code module.

Loop:

```text
implement
→ run/inspect/log/profile/use the real UI or integration
→ correct the largest defect
→ test/benchmark/validate
```

Bottleneck follows the existing product architecture. Do **not** create module boundaries, services, folders, state owners, or runtime abstractions merely to mirror slices or OPEN/CLOSED bookkeeping.

CLOSED result: a genuinely production-quality responsibility or behavior with enough evidence, integration context, and documentation to depend on safely.

## 3D / visual asset hardening

Whole-artifact context: authoritative reference views, scale/axes, comparison camera/FOV where relevant, macro silhouette and proportions, major part relationships, pose, material intent, rig/export goals.

ACTIVE: the highest-impact perceptual or functional mismatch. It may coherently span mesh, rig, pose, material, lighting, camera, or export settings when those causes are strongly coupled.

Example:

```text
Bottleneck: left shoulder silhouette
Coherent scope: clavicle pose + torso contour + upper-arm placement + comparison camera
Not four independent slices if they must move together.
```

Loop:

```text
construct/modify real geometry, rig, material, or scene state
→ render/view the actual asset against authoritative references
→ correct the largest remaining mismatch
→ validate across the necessary views and functional checks
```

Do not let render boards, overlays, metrics, penetration checks, or multi-view captures outrun construction quality. They are evidence. If macro proportion, silhouette, pose, or reference registration is wrong, reopen that upstream premise before polishing detail.

CLOSED result: the declared views/behaviors reach target quality, no known macro premise remains wrong for that scope, and the asset is usable in the intended downstream pipeline.

## Interactive world / simulation

Whole-artifact context: macro world shape, canonical state, camera/input model, physics/solver semantics, coordinate/time units, performance envelope.

ACTIVE: one high-leverage simulation or presentation bottleneck such as terrain traversal, water response, vehicle handling, solver stability, or viewer behavior.

Loop:

```text
construct behavior
→ run the real simulation
→ observe state, motion, interaction, and visual outcome
→ correct
→ validate determinism, performance, and edge conditions
```

Do not polish decorative systems while core motion, spatial relationships, or interaction semantics are still wrong.

## Dashboard / application UI

Whole-artifact context: final information hierarchy, primary user tasks, real data contracts, navigation, responsive constraints.

ACTIVE: one dominant UX or information bottleneck, not necessarily one component.

CLOSED result: the user-visible task works at target quality across relevant loading/error/empty/responsive states and real integration boundaries.

## Research / data

Whole-artifact context: hypothesis/evidence map, assumptions, dataset identity, provenance, evaluation definitions, known confounders.

ACTIVE: one falsifiable decision or analysis bottleneck.

Loop:

```text
construct experiment/analysis
→ inspect evidence and failure cases
→ correct assumptions/method/data handling
→ validate with reproducible evaluation and counter-evidence
```

Do not hide relevant confounders merely to create isolation. Reopen upstream framing when evidence invalidates it.

CLOSED result: a reproducible result whose claim is supported at the declared level of certainty, not merely a completed notebook or passing pipeline.

## Business / product strategy

Whole-artifact context: target user, value proposition, constraints, measurable outcomes, evidence quality.

ACTIVE: one decision bottleneck — acquisition, pricing, retention, distribution, unit economics, positioning, etc.

CLOSED result: an evidence-backed decision with explicit adoption/rejection rule, known uncertainty, and downstream implications.

## Creative production

Whole-artifact context: composition, narrative/world invariants, character state, style constraints, causal obligations, intended audience experience.

ACTIVE: one scene, sequence, asset family, interaction beat, or perceptual bottleneck.

CLOSED result: target-quality artifact plus the minimal authoritative state changes needed downstream.

As in 3D, do not close local detail while composition, silhouette, pacing, or another macro premise remains materially wrong.
