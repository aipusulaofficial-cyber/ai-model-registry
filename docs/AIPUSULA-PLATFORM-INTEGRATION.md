# AIPusula Platform Integration — Model Governance

Lifecycle: REGISTERED -> SECURITY_VALIDATED -> EVALUATED -> COST_VALIDATED -> STAGING -> CANARY -> PRODUCTION -> ARCHIVED.

Every transition requires versioned evidence, actor/system, timestamp and audit reference. Promotion is blocked when security, quality, cost, provenance or deployment evidence is missing.

Integrates with evaluation, gateway policy, inference runtime, observability and cost control.

Engineering standard: Code -> Contract -> Test -> Security -> Runtime -> Observability -> Deployment -> Evidence
