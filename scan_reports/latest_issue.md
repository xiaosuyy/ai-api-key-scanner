## 🔐 发现疑似泄露的 AI API 密钥

本次扫描共发现 **6** 条疑似泄露（仓库 45 个，文件 7686 个）。

| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |
| --- | --- | --- | --- | --- |
| HIGH | `Sannrox/sekai-chisei` | `crates/chisei-gateway/src/gateway_tests.rs` | 5068 | `sk-ant...cret` |
| HIGH | `Sannrox/sekai-chisei` | `crates/chisei-gateway/src/gateway_tests.rs` | 5090 | `sk-ant...cret` |
| HIGH | `headroomlabs-ai/headroom` | `.gitguardian.yaml` | 34 | `sk-ant...ture` |
| HIGH | `headroomlabs-ai/headroom` | `crates/headroom-proxy/src/cache_stabilization/drift_detector.rs` | 761 | `sk-ant...g-me` |
| HIGH | `jshiv/cronicle` | `internal/cronicle/state/pg_secrets_test.go` | 33 | `sk-ant...lock` |
| MEDIUM | `richardichogan/knowledge-base` | `knowledge-hub-backend/scripts/mural.test.ts` | 49 | `fixtur...oken` |

> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。

