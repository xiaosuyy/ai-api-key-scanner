## 🔐 发现疑似泄露的 AI API 密钥

本次扫描共发现 **6** 条疑似泄露（仓库 50 个，文件 10035 个）。

| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |
| --- | --- | --- | --- | --- |
| MEDIUM | `apoorvdarshan/scowld` | `ios/Scowld/Core/TipJar.swift` | 11 | `appl_y...mcLy` |
| MEDIUM | `mkupermann/throughline` | `docs/demo/rust/assistants/home/.codex/config.toml` | 2 | `sk-dem...0000` |
| HIGH | `mkupermann/throughline` | `rust/crates/throughline/src/pii.rs` | 148 | `sk-ant...x234` |
| HIGH | `mkupermann/throughline` | `tests/test_export_markdown.py` | 352 | `sk-ant...BBBB` |
| MEDIUM | `mkupermann/throughline` | `tests/test_export_markdown.py` | 314 | `sk-ant...AAAA` |
| MEDIUM | `gitstore-dev/GitStore` | `gitstore-api/cmd/gitctl/enroll_serviceaccount_test.go` | 196 | `access...nted` |

> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。

