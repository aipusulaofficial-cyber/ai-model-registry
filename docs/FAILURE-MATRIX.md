# Failure matrix

| Failure | Detection | Action | Retry? | Impact |
|---|---|---|---|---|
| Invalid model metadata | validation | reject | No | 4xx |
| Registry dependency timeout | timeout budget | normalize | Safe/idempotent only | bounded failure |
| Repeated dependency failure | circuit breaker | open circuit | No while open | fast failure |
| Concurrent overload | bounded executor | fail fast | No | explicit overload |
| Promotion conflict | lifecycle validation | reject/rollback | No | no partial promotion |

Promotion must be atomic from the caller's perspective; rollback is explicit.