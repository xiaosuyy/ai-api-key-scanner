## 🔐 发现疑似泄露的 AI API 密钥

本次扫描共发现 **12** 条疑似泄露（仓库 50 个，文件 9688 个）。

| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |
| --- | --- | --- | --- | --- |
| MEDIUM | `e2b-dev/E2B` | `packages/cli/tests/user_config_migration.test.ts` | 80 | `projec...cret` |
| MEDIUM | `e2b-dev/E2B` | `packages/cli/tests/user_config_permissions.test.ts` | 38 | `projec...cret` |
| HIGH | `johan-becker/hushgate` | `README.md` | 333 | `ghp_A1...Q7r8` |
| MEDIUM | `johan-becker/hushgate` | `docs/superpowers/plans/2026-09-09-onboarding-setup.md` | 1764 | `sk-fro...inal` |
| MEDIUM | `johan-becker/hushgate` | `docs/superpowers/plans/2026-09-09-onboarding-setup.md` | 1779 | `sk-inj...page` |
| MEDIUM | `johan-becker/hushgate` | `test/attach.external.test.ts` | 237 | `sk-als...leak` |
| MEDIUM | `johan-becker/hushgate` | `test/playground.send.test.ts` | 47 | `sk-fro...inal` |
| MEDIUM | `johan-becker/hushgate` | `test/playground.send.test.ts` | 136 | `sk-inj...page` |
| HIGH | `johan-becker/hushgate` | `test/tenants.test.ts` | 432 | `sk-ant...AAAA` |
| MEDIUM | `johan-becker/hushgate` | `test/tenants.test.ts` | 262 | `sk-rea...-key` |
| MEDIUM | `pymc-labs/daimon` | `apps/harness/tests/test_isolation.py` | 51 | `synthe...cret` |
| MEDIUM | `theolundqvist/pr-cockpit` | `server/quickGenerate.test.ts` | 66 | `sk-ant...cret` |

> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。

