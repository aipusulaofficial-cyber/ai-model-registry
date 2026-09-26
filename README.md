# AI Model Registry

A model lifecycle service for validated metadata, provenance, explicit state transitions and controlled promotion.

## Lifecycle
```text
model artifact + metadata
        -> validation
        -> registered version
        -> lifecycle state
        -> promotion decision
        -> deployment consumer
```

## Core contracts
- Model metadata is validated before registration.
- Versions are immutable references for lifecycle decisions.
- Provenance links a model to its source and validation context.
- Promotion is a state transition with explicit preconditions.
- Invalid transitions are rejected rather than silently coerced.

## Runtime
The container runs non-root and exposes health probes. Helm deployment templates define non-root security context, versioned image references, resources, readiness and liveness checks.

## Verification
CI, dependency auditing and production tests validate lifecycle behavior and deployment assumptions.

## Evidence
[ARCHITECTURE.md](ARCHITECTURE.md) · [docs/PRINCIPAL-ENGINEERING.md](docs/PRINCIPAL-ENGINEERING.md) · [ADRs](ADRs/)

The registry is intentionally lifecycle-oriented: storing an artifact is not the same thing as approving it for promotion.