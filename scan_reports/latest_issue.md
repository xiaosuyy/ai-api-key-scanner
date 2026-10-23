## 🔐 发现疑似泄露的 AI API 密钥

本次扫描共发现 **5** 条疑似泄露（仓库 50 个，文件 8258 个）。

| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |
| --- | --- | --- | --- | --- |
| MEDIUM | `langwatch/langwatch` | `.github/scripts/__tests__/secrets-scan.test.sh` | 26 | `AKIAQY...ZAM2` |
| MEDIUM | `langwatch/langwatch` | `.gitleaks.toml` | 122 | `AKIAQY...ZAM2` |
| MEDIUM | `zereight/gitlab-mcp` | `test/dynamic-routing-tests.ts` | 16 | `mcp-st...oken` |
| MEDIUM | `zereight/gitlab-mcp` | `test/oauth-device-flow-tests.ts` | 19 | `oauth-...oken` |
| MEDIUM | `starfall-org/generative` | `app/src/main/kotlin/org/starfall/generative/integrations/modelapis/antigravity/AntigravityAdapter.kt` | 31 | `GOCSPX...qDAf` |

> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。

