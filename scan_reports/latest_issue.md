## 🔐 发现疑似泄露的 AI API 密钥

本次扫描共发现 **8** 条疑似泄露（仓库 50 个，文件 9033 个）。

| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |
| --- | --- | --- | --- | --- |
| MEDIUM | `ashlrai/ashlr-stack` | `packages/core/src/__tests__/credential-staging.test.ts` | 567 | `synthe...oken` |
| MEDIUM | `ashlrai/ashlr-stack` | `packages/core/src/__tests__/supabase-provider.test.ts` | 18 | `sbp_ca...oken` |
| MEDIUM | `ashlrai/ashlr-stack` | `packages/core/src/providers/aws.ts` | 24 | `AWS_SE..._KEY` |
| MEDIUM | `mojoaar/mimir` | `docs/superpowers/plans/2026-10-25-mimir-v0.2.0-learning.md` | 279 | `sk-liv...alue` |
| MEDIUM | `mojoaar/mimir` | `lib/backup/artifacts.int.test.ts` | 22 | `sk-liv...-key` |
| MEDIUM | `nranjan2code/vakyartha` | `scripts/desktop-probe.js` | 30 | `synthe...-key` |
| MEDIUM | `edgar4/yada` | `tests/starter-integration.test.ts` | 45 | `never-...ible` |
| MEDIUM | `edgar4/yada` | `tests/starter-provider.test.ts` | 59 | `server...cret` |

> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。

