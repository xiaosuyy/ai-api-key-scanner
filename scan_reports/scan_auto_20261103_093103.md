# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-03 09:31:03 UTC |
| 扫描仓库数 | 50 |
| 扫描文件数 | 10035 |
| 发现数量 | 6 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 2 |
| MEDIUM | 4 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`apoorvdarshan/scowld`
- **文件**：`ios/Scowld/Core/TipJar.swift`（第 11 行）
- **密钥（已脱敏）**：`appl_y...mcLy`
- **链接**：https://github.com/apoorvdarshan/scowld/blob/main/ios/Scowld/Core/TipJar.swift
- **说明**：赋值给 API key 变量的疑似密钥。

```text
static let publicAPIKey = "appl_yFwHjxnttQhHaATjcIuehZBmcLy"
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`mkupermann/throughline`
- **文件**：`docs/demo/rust/assistants/home/.codex/config.toml`（第 2 行）
- **密钥（已脱敏）**：`sk-dem...0000`
- **链接**：https://github.com/mkupermann/throughline/blob/main/docs/demo/rust/assistants/home/.codex/config.toml
- **说明**：赋值给 API key 变量的疑似密钥。

```text
api_key = "sk-demo-0000000000000000000000"
```

### 3. [HIGH] Anthropic API Key

- **仓库**：`mkupermann/throughline`
- **文件**：`rust/crates/throughline/src/pii.rs`（第 148 行）
- **密钥（已脱敏）**：`sk-ant...x234`
- **链接**：https://github.com/mkupermann/throughline/blob/main/rust/crates/throughline/src/pii.rs
- **说明**：Anthropic Claude API 密钥。

```text
redact("key sk-ant-abc123def456ghi789jkl012mno345pqr678stu901vwx234 and me@company.io");
```

### 4. [HIGH] Anthropic API Key

- **仓库**：`mkupermann/throughline`
- **文件**：`tests/test_export_markdown.py`（第 352 行）
- **密钥（已脱敏）**：`sk-ant...BBBB`
- **链接**：https://github.com/mkupermann/throughline/blob/main/tests/test_export_markdown.py
- **说明**：Anthropic Claude API 密钥。

```text
"content": "Key sk-ant-api03-BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
```

### 5. [MEDIUM] Anthropic API Key

- **仓库**：`mkupermann/throughline`
- **文件**：`tests/test_export_markdown.py`（第 314 行）
- **密钥（已脱敏）**：`sk-ant...AAAA`
- **链接**：https://github.com/mkupermann/throughline/blob/main/tests/test_export_markdown.py
- **说明**：Anthropic Claude API 密钥。

```text
_msg("user", content="Mein Key ist sk-ant-api03-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA und mail@example.com", minute=0),
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`gitstore-dev/GitStore`
- **文件**：`gitstore-api/cmd/gitctl/enroll_serviceaccount_test.go`（第 196 行）
- **密钥（已脱敏）**：`access...nted`
- **链接**：https://github.com/gitstore-dev/GitStore/blob/main/gitstore-api/cmd/gitctl/enroll_serviceaccount_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken   = "access-token-must-not-be-printed"
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

