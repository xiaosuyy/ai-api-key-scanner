## 🔐 发现疑似泄露的 AI API 密钥

本次扫描共发现 **7** 条疑似泄露（仓库 44 个，文件 9416 个）。

| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |
| --- | --- | --- | --- | --- |
| MEDIUM | `DeliciousBuding/metapi-go` | `handler/admin/accounts_test.go` | 1314 | `new-se...-xyz` |
| MEDIUM | `elie222/rakazo` | `apps/api/src/security-audit.test.ts` | 20 | `sk-or-...alue` |
| MEDIUM | `OmritRenders/elidocortex` | `Cortex Agent/settings/browser/elidoSettings.ts` | 12 | `elido....ings` |
| MEDIUM | `OmritRenders/cortex-agent` | `settings/browser/elidoSettings.ts` | 12 | `elido....ings` |
| HIGH | `pghmatt/quotadial` | `crates/providers/claude/src/provider_tests.rs` | 1028 | `sk-ant...4321` |
| MEDIUM | `trick77/llmwire` | `messages_test.go` | 444 | `fixtur...-key` |
| MEDIUM | `trick77/llmwire` | `models_test.go` | 18 | `team-k...hape` |

> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。

