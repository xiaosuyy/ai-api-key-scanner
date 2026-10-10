## 🔐 发现疑似泄露的 AI API 密钥

本次扫描共发现 **7** 条疑似泄露（仓库 50 个，文件 8582 个）。

| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |
| --- | --- | --- | --- | --- |
| MEDIUM | `adityajha2005/decisionkit` | `test/server.test.ts` | 73 | `ambien...ored` |
| MEDIUM | `truffle-ai/dexto` | `docs/docusaurus.config.ts` | 87 | `e82461...3ecc` |
| MEDIUM | `quodeq/quodeq` | `benchmarks/.corpus/synthetic/js-security/config.js` | 2 | `sk-liv...aabb` |
| MEDIUM | `quodeq/quodeq` | `benchmarks/.corpus/synthetic/py-security/config.py` | 1 | `sk-liv...ba98` |
| MEDIUM | `getmodern-ai/graft` | `apps/server/src/app.test.ts` | 43 | `sk_liv..._key` |
| HIGH | `getmodern-ai/graft` | `apps/server/src/database.integration.test.ts` | 117 | `sk-ant...6789` |
| MEDIUM | `getmodern-ai/graft` | `apps/server/src/database.integration.test.ts` | 116 | `sk_liv...6789` |

> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。

