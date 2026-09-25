# ADR-0004: Security decision

## Decision
Treat model metadata, artifacts, configuration and provider output as untrusted. Validate boundaries, enforce least privilege, protect provenance, sanitize telemetry and fail closed for lifecycle/promotion authorization.

## Why
Model registries are trust boundaries for deployment artifacts.

## Alternatives considered
Trusting internal callers, logging secrets/raw artifact metadata, and fail-open promotion were rejected.

## Trade-offs
Redaction reduces debugging detail; correlation IDs and structured error categories preserve diagnosis.

## Consequences
Lifecycle decisions are deterministic and auditable.