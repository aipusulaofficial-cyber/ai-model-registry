# Operational runbook

Track p50/p95/p99 latency, throughput, error rate, concurrency, dependency health, retry_count, circuit state and promotion/rollback counts.

1. Confirm readiness and deployment revision.
2. Trace by request_id/correlation_id.
3. Inspect model version, lifecycle state and provenance.
4. Inspect dependency latency and retry/circuit state.
5. If promotion fails, restore the last valid lifecycle state and verify audit evidence.
6. Run smoke/integration checks before reopening promotion.