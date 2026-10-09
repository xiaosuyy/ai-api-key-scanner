## 🔐 发现疑似泄露的 AI API 密钥

本次扫描共发现 **6** 条疑似泄露（仓库 20 个，文件 3944 个）。

| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |
| --- | --- | --- | --- | --- |
| MEDIUM | `luqman-v1/9router-go` | `benchmark/runner.go` | 57 | `sk-ben...-key` |
| MEDIUM | `luqman-v1/9router-go` | `internal/handlers/chat/kimchi_handler_test.go` | 315 | `sk-kim...2345` |
| MEDIUM | `luqman-v1/9router-go` | `internal/handlers/chat/kimchi_handler_test.go` | 325 | `oauth-...7890` |
| MEDIUM | `DeliciousBuding/metapi-go` | `config/defaults.go` | 7 | `change...oken` |
| MEDIUM | `DeliciousBuding/metapi-go` | `handler/admin/accounts_test.go` | 1320 | `new-se...-xyz` |
| MEDIUM | `DeliciousBuding/metapi-go` | `handler/admin/auth_settings_test.go` | 27 | `admin-...oken` |

> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。

