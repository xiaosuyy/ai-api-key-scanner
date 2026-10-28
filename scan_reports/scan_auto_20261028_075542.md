# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-28 07:55:42 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 4295 |
| 发现数量 | 2 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 2 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`xiaoqi8553/codex-token-dashboard`
- **文件**：`tests/dashboard-ui.test.js`（第 367 行）
- **密钥（已脱敏）**：`SECRET...DATA`
- **链接**：https://github.com/xiaoqi8553/codex-token-dashboard/blob/main/tests/dashboard-ui.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
fs.writeFileSync(path.join(codexHome, "auth.json"), JSON.stringify({ tokens: { account_id: "test-account", access_token: "SECRET_SHOULD_NOT_BE_IN_METADATA" } }));
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`CorbanuCore/CorbanuTerminal`
- **文件**：`.github/workflows/corbanu-terminal-release.yml`（第 567 行）
- **密钥（已脱敏）**：`corban...moke`
- **链接**：https://github.com/CorbanuCore/CorbanuTerminal/blob/main/.github/workflows/corbanu-terminal-release.yml
- **说明**：赋值给 API key 变量的疑似密钥。

```text
$env:CLAUDE_CODE_OAUTH_TOKEN = "corbanu-release-smoke"
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

