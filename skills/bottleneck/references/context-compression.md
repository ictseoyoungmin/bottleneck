# Context Compression

A context capsule is **not a generic summary**.

It is the minimum sufficient authoritative projection required to safely use or extend a CLOSED slice.

## Pack

Include:

- identity and responsibility,
- public API / exposed artifacts,
- authoritative inputs and outputs,
- invariants,
- ownership boundaries,
- budgets,
- important decisions and rationale identifiers,
- evidence/test/demo locations,
- known limitations,
- conditions that require reopening.

Exclude:

- long implementation chronology,
- discarded alternatives unless they prevent repeated mistakes,
- internal helper details,
- raw logs already available by address,
- duplicated documentation.

## Preserve resolvability

Compression must retain locations or identifiers for authoritative source material. Never replace verifiable evidence with an untraceable prose summary.

## Unpack only on demand

A future agent should start from the capsule and expand into internal files only when the current task requires it.

This reduces context pollution without creating memory amnesia.
