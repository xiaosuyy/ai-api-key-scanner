## 🔐 发现疑似泄露的 AI API 密钥

本次扫描共发现 **5** 条疑似泄露（仓库 47 个，文件 9698 个）。

| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |
| --- | --- | --- | --- | --- |
| MEDIUM | `Blumlaut/saale` | `.env.example` | 103 | `change...tion` |
| MEDIUM | `manki-review/manki` | `src/providers/cli-utils.test.ts` | 535 | `refres...-run` |
| MEDIUM | `zhulongqihan/codex-pulse` | `src-tauri/src/pulse_pace.rs` | 975 | `never-...ss-a` |
| MEDIUM | `zhulongqihan/codex-pulse` | `src-tauri/src/pulse_pace.rs` | 986 | `never-...ss-b` |
| HIGH | `agentmuxai/agentmux` | `crates/cef/src/commands/cli_login.rs` | 1271 | `sk-ant...CRET` |

> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。

