## 🔐 发现疑似泄露的 AI API 密钥

本次扫描共发现 **8** 条疑似泄露（仓库 50 个，文件 8225 个）。

| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |
| --- | --- | --- | --- | --- |
| MEDIUM | `PMZPZM0/codex-harness-desktop` | `electron/features/cloud-memory-ipc.ts` | 151 | `CLOUD_...OKEN` |
| MEDIUM | `Remote-Arc/remote-arc` | `apps/relay/scripts/arc-app-connections-test.ts` | 30 | `privat...oken` |
| MEDIUM | `Remote-Arc/remote-arc` | `apps/relay/scripts/arc-chat-test.ts` | 313 | `fixtur...oken` |
| MEDIUM | `Remote-Arc/remote-arc` | `apps/relay/scripts/arc-chat-test.ts` | 358 | `fixtur...-key` |
| MEDIUM | `Remote-Arc/remote-arc` | `apps/relay/scripts/arc-task-eval-fixture-test.ts` | 8 | `synthe...cret` |
| MEDIUM | `Remote-Arc/remote-arc` | `apps/relay/scripts/arc-task-live-eval.ts` | 146 | `fixtur...oken` |
| MEDIUM | `Remote-Arc/remote-arc` | `apps/relay/scripts/arc-working-context-test.ts` | 47 | `contex...cret` |
| HIGH | `phillipxnguyen/wikiPhidia` | `index.html` | 12118 | `AIzaSy..._ZlM` |

> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。

