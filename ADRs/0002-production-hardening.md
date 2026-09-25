# ADR-0002: Production hardening
The registry API uses FastAPI with OpenTelemetry tracing. Kubernetes/Helm provide bounded deployment; Terraform owns infrastructure inputs. Trivy/CycloneDX gate dependency and SBOM risk; HTTP contract/property tests protect registry endpoints; Locust supplies load validation.
Immutable model metadata and lifecycle state remain domain-owned and durable state is externalized in production.
