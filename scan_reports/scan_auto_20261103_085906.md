# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-03 08:59:06 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 3938 |
| 发现数量 | 6 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 2 |
| MEDIUM | 4 |

## 发现明细

### 1. [HIGH] GitHub Personal Access Token

- **仓库**：`avivsinai/telclaude`
- **文件**：`.gitleaks.toml`（第 36 行）
- **密钥（已脱敏）**：`ghp_ab...r678`
- **链接**：https://github.com/avivsinai/telclaude/blob/main/.gitleaks.toml
- **说明**：GitHub PAT（Copilot / GitHub Models 等场景常用）。

```text
'''ghp_abc123def456ghi789jkl012mno345pqr678''',
```

### 2. [HIGH] GitHub Personal Access Token

- **仓库**：`avivsinai/telclaude`
- **文件**：`src/commands/doctor.ts`（第 45 行）
- **密钥（已脱敏）**：`ghp_ab...r678`
- **链接**：https://github.com/avivsinai/telclaude/blob/main/src/commands/doctor.ts
- **说明**：GitHub PAT（Copilot / GitHub Models 等场景常用）。

```text
input: "key: ghp_abc123def456ghi789jkl012mno345pqr678",
```

### 3. [MEDIUM] GitHub Personal Access Token

- **仓库**：`avivsinai/telclaude`
- **文件**：`src/commands/doctor.ts`（第 292 行）
- **密钥（已脱敏）**：`ghp_ab...r678`
- **链接**：https://github.com/avivsinai/telclaude/blob/main/src/commands/doctor.ts
- **说明**：GitHub PAT（Copilot / GitHub Models 等场景常用）。

```text
const exampleInput = "API key: ghp_abc123def456ghi789jkl012mno345pqr678";
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`yyjeqhc/webcodex`
- **文件**：`apps/desktop/src/features/ConnectionsTools.test.tsx`（第 147 行）
- **密钥（已脱敏）**：`write-...-key`
- **链接**：https://github.com/yyjeqhc/webcodex/blob/main/apps/desktop/src/features/ConnectionsTools.test.tsx
- **说明**：赋值给 API key 变量的疑似密钥。

```text
api_key: "write-only-server-key",
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`yyjeqhc/webcodex`
- **文件**：`apps/desktop/src/features/ConnectionsTools.test.tsx`（第 548 行）
- **密钥（已脱敏）**：`write-...cret`
- **链接**：https://github.com/yyjeqhc/webcodex/blob/main/apps/desktop/src/features/ConnectionsTools.test.tsx
- **说明**：赋值给 API key 变量的疑似密钥。

```text
expect(captured[0]).toMatchObject({ id: "personal", expected_revision: 1, name: "Personal renamed", host_mode: "standalone", api_key: "write-only-fixture-secret" });
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`yyjeqhc/webcodex`
- **文件**：`apps/desktop/src/features/ConnectionsTools.test.tsx`（第 569 行）
- **密钥（已脱敏）**：`mcp-ui...ture`
- **链接**：https://github.com/yyjeqhc/webcodex/blob/main/apps/desktop/src/features/ConnectionsTools.test.tsx
- **说明**：赋值给 API key 变量的疑似密钥。

```text
expect(captured[0]).toMatchObject({ id: null, expected_revision: 0, command: "npx", args: ["-y", "@playwright/mcp"], env: { API_KEY: "mcp-ui-private-fixture" } });
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

