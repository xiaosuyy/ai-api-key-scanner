## 🔐 发现疑似泄露的 AI API 密钥

本次扫描共发现 **7** 条疑似泄露（仓库 48 个，文件 8036 个）。

| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |
| --- | --- | --- | --- | --- |
| HIGH | `toul10/agent-authority-pilot` | `tests/test_settings.py` | 47 | `sk-ant...0000` |
| HIGH | `toul10/agent-authority-pilot` | `tests/test_settings.py` | 48 | `sk-ant...0000` |
| MEDIUM | `toul10/agent-authority-pilot` | `tests/test_settings.py` | 109 | `sk-ant...0000` |
| MEDIUM | `orrery-node/orrery` | `node/devtools/e2e.ts` | 623 | `sk-ant...d-on` |
| MEDIUM | `pipodev06/omni-rag` | `apps/api/test/settings.test.ts` | 150 | `gsk_se...laro` |
| MEDIUM | `deepnote/vscode-deepnote` | `src/kernels/execution/cellExecution.federatedAuth.unit.test.ts` | 194 | `access...-log` |
| MEDIUM | `DrBradStanfield/roadmap` | `app/lib/email-resend-missing-id.test.ts` | 45 | `synthe...-key` |

> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。

