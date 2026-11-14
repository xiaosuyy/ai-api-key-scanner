## 🔐 发现疑似泄露的 AI API 密钥

本次扫描共发现 **11** 条疑似泄露（仓库 48 个，文件 8377 个）。

| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |
| --- | --- | --- | --- | --- |
| HIGH | `ShenSeanChen/waku-agent` | `evals/deterministic/hosted/test_install_sh.py` | 790 | `sk-ant...Z-AA` |
| HIGH | `ShenSeanChen/waku-agent` | `evals/deterministic/test_turn_receipt.py` | 146 | `sk-ant...AUTH` |
| HIGH | `ShenSeanChen/waku-agent` | `evals/deterministic/test_turn_receipt.py` | 147 | `sk-ant...IKEY` |
| HIGH | `ShenSeanChen/waku-agent` | `evals/deterministic/test_turn_receipt.py` | 148 | `sk-ant...ECHO` |
| HIGH | `ShenSeanChen/waku-agent` | `evals/hosted_docker/spawnerlib.py` | 45 | `sk-ant...ship` |
| MEDIUM | `KushalP1/context-doctor` | `src/test/ab.test.ts` | 366 | `sk-ant...leak` |
| MEDIUM | `KushalP1/context-doctor` | `src/test/canary.test.ts` | 40 | `sk-ant...king` |
| HIGH | `atliliw/langchainrust` | `crates/lc-agents/src/react/agent.rs` | 335 | `sk-6eb...43e7` |
| MEDIUM | `A220man/atlas-lens-ryan-vo` | `backend/tests/test_auth_and_security.py` | 46 | `some-p...hars` |
| MEDIUM | `krishanraja/AEO-Engine` | `tests/claudeCode.test.ts` | 29 | `synthe...oken` |
| MEDIUM | `KhatKit/Android` | `app/src/androidTest/java/heizige/kk/khatkit/app/feature/chat/C1GroupExportDeviceEvidenceTest.kt` | 111 | `sk-c1c...feed` |

> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。

