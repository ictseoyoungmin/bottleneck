# Bottleneck State Model

## States

### SKELETON
A responsibility exists only as enough structure to preserve system shape:

- interface/schema,
- route,
- explicit stub,
- fixture/mock,
- placeholder visual,
- ownership declaration.

A Skeleton must not masquerade as production-complete.

### ACTIVE
The single responsibility currently allowed to receive production-quality expansion.

Invariant:

```text
count(ACTIVE production slices) <= 1
```

### CLOSED
The responsibility has passed its predeclared closure gates, is integrated, and has a context capsule.

Closed means “stable enough to depend on”, not “immutable forever”.

### REOPENED
A previously CLOSED responsibility has an explicit reason to change. While being modified it occupies the same single WIP slot as ACTIVE.

## Allowed transitions

```text
SKELETON -> ACTIVE -> CLOSED
CLOSED -> REOPENED -> CLOSED
```

A direct `SKELETON -> CLOSED` is only valid for purely declarative artifacts where no production implementation exists.

## Exploration exception

Disposable experiments may occur beside the state model if all are true:

- located in a sandbox/branch/temp path,
- clearly marked experimental,
- not wired as a production path,
- deleted or archived after selection,
- do not create ambiguous ownership.

Exploration WIP may be wide. Production commitment WIP remains one.
