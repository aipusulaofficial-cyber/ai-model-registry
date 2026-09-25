# ADR-0003: Failure and retry strategy

## Decision
Explicit timeout budgets, bounded exponential backoff, idempotency-aware retries, bounded concurrency, rate limiting where applicable, and circuit breaking for repeated dependency failure.

## Why
Unbounded retries amplify incidents and can duplicate side effects.

## Alternatives considered
Unlimited retries, fixed-delay storms, and blind retries were rejected.

## Trade-offs
Bounded latency requires explicit operation classification.

## Consequences
Failure behavior is testable, observable and auditable.

## Implementation evidence
resilience.py and tests/test_resilience.py.