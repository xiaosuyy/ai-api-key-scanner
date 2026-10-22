# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-22 07:07:39 UTC |
| 扫描仓库数 | 19 |
| 扫描文件数 | 2948 |
| 发现数量 | 4 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 1 |
| MEDIUM | 2 |
| LOW | 1 |

## 发现明细

### 1. [MEDIUM] Anthropic API Key

- **仓库**：`isseis/yt2column`
- **文件**：`cmd/yt2column-server/test_helpers.go`（第 39 行）
- **密钥（已脱敏）**：`sk-ant...8ANT`
- **链接**：https://github.com/isseis/yt2column/blob/main/cmd/yt2column-server/test_helpers.go
- **说明**：Anthropic Claude API 密钥。

```text
testAnthropicKey  = "sk-ant-ANTHROPICVALUE-0123456789-TAIL8ANT" //nolint:gosec // a fake key the redaction checks look for
```

### 2. [LOW] Generic API key assignment

- **仓库**：`isseis/yt2column`
- **文件**：`cmd/yt2column-server/test_helpers.go`（第 37 行）
- **密钥（已脱敏）**：`sk-uni...8KEY`
- **链接**：https://github.com/isseis/yt2column/blob/main/cmd/yt2column-server/test_helpers.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
testAPIKey        = "sk-unit-APIKEYVALUE-0123456789-TAIL8KEY" //nolint:gosec // a fake key the redaction checks look for
```

### 3. [HIGH] Anthropic API Key

- **仓库**：`isseis/yt2column`
- **文件**：`cmd/yt2column/run_test.go`（第 47 行）
- **密钥（已脱敏）**：`sk-ant...8ANT`
- **链接**：https://github.com/isseis/yt2column/blob/main/cmd/yt2column/run_test.go
- **说明**：Anthropic Claude API 密钥。

```text
testAnthropicKey = "sk-ant-APIKEYVALUE-0123456789-TAIL8ANT"
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`isseis/yt2column`
- **文件**：`cmd/yt2column/run_test.go`（第 44 行）
- **密钥（已脱敏）**：`sk-uni...8KEY`
- **链接**：https://github.com/isseis/yt2column/blob/main/cmd/yt2column/run_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
testAPIKey = "sk-unit-APIKEYVALUE-0123456789-TAIL8KEY"
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

