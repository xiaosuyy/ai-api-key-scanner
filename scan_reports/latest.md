# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-08 09:04:41 UTC |
| 扫描仓库数 | 47 |
| 扫描文件数 | 9698 |
| 发现数量 | 5 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 1 |
| MEDIUM | 4 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`Blumlaut/saale`
- **文件**：`.env.example`（第 103 行）
- **密钥（已脱敏）**：`change...tion`
- **链接**：https://github.com/Blumlaut/saale/blob/main/.env.example
- **说明**：赋值给 API key 变量的疑似密钥。

```text
SANDBOX_API_KEY="change-me-in-production"
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`manki-review/manki`
- **文件**：`src/providers/cli-utils.test.ts`（第 535 行）
- **密钥（已脱敏）**：`refres...-run`
- **链接**：https://github.com/manki-review/manki/blob/main/src/providers/cli-utils.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
writeFileSync(target, JSON.stringify({ tokens: { access_token: 'refreshed-during-run' } }));
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`zhulongqihan/codex-pulse`
- **文件**：`src-tauri/src/pulse_pace.rs`（第 975 行）
- **密钥（已脱敏）**：`never-...ss-a`
- **链接**：https://github.com/zhulongqihan/codex-pulse/blob/main/src-tauri/src/pulse_pace.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: "never-persist-access-a".into(),
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`zhulongqihan/codex-pulse`
- **文件**：`src-tauri/src/pulse_pace.rs`（第 986 行）
- **密钥（已脱敏）**：`never-...ss-b`
- **链接**：https://github.com/zhulongqihan/codex-pulse/blob/main/src-tauri/src/pulse_pace.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
changed.access_token = "never-persist-access-b".into();
```

### 5. [HIGH] Anthropic API Key

- **仓库**：`agentmuxai/agentmux`
- **文件**：`crates/cef/src/commands/cli_login.rs`（第 1271 行）
- **密钥（已脱敏）**：`sk-ant...CRET`
- **链接**：https://github.com/agentmuxai/agentmux/blob/main/crates/cef/src/commands/cli_login.rs
- **说明**：Anthropic Claude API 密钥。

```text
let red = redact_secrets("  token: sk-ant-api03-SECRETSECRETSECRET done");
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

