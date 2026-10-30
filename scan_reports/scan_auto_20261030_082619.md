# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-30 08:26:19 UTC |
| 扫描仓库数 | 45 |
| 扫描文件数 | 6793 |
| 发现数量 | 8 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 7 |
| LOW | 1 |

## 发现明细

### 1. [MEDIUM] Google OAuth Client Secret

- **仓库**：`poweruserz/OpenTokenUsage`
- **文件**：`docs/providers/antigravity.md`（第 202 行）
- **密钥（已脱敏）**：`GOCSPX...qDAf`
- **链接**：https://github.com/poweruserz/OpenTokenUsage/blob/main/docs/providers/antigravity.md
- **说明**：Google OAuth 客户端密钥。

```text
&client_secret=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
```

### 2. [MEDIUM] Google OAuth Client Secret

- **仓库**：`poweruserz/OpenTokenUsage`
- **文件**：`plugins/antigravity/plugin.js`（第 21 行）
- **密钥（已脱敏）**：`GOCSPX...qDAf`
- **链接**：https://github.com/poweruserz/OpenTokenUsage/blob/main/plugins/antigravity/plugin.js
- **说明**：Google OAuth 客户端密钥。

```text
var GOOGLE_CLIENT_SECRET = "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"
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`poweruserz/OpenTokenUsage`
- **文件**：`plugins/antigravity/plugin.test.js`（第 1040 行）
- **密钥（已脱敏）**：`ya29.r...oken`
- **链接**：https://github.com/poweruserz/OpenTokenUsage/blob/main/plugins/antigravity/plugin.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
return { status: 200, bodyText: JSON.stringify({ access_token: "ya29.refreshed-token" }) }
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`poweruserz/OpenTokenUsage`
- **文件**：`plugins/antigravity/plugin.test.js`（第 1120 行）
- **密钥（已脱敏）**：`ya29.c...-bad`
- **链接**：https://github.com/poweruserz/OpenTokenUsage/blob/main/plugins/antigravity/plugin.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
writeCachedToken(ctx, { accessToken: "ya29.cached-also-bad", expiresAtMs: Date.now() + 3600000, refreshToken: "1//refresh" })
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`poweruserz/OpenTokenUsage`
- **文件**：`plugins/antigravity/plugin.test.js`（第 1242 行）
- **密钥（已脱敏）**：`ya29.o...ache`
- **链接**：https://github.com/poweruserz/OpenTokenUsage/blob/main/plugins/antigravity/plugin.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
writeCachedToken(ctx, { accessToken: "ya29.old-account-cache", expiresAtMs: Date.now() + 3600000, refreshToken: "1//old-account" })
```

### 6. [LOW] Generic API key assignment

- **仓库**：`poweruserz/OpenTokenUsage`
- **文件**：`plugins/antigravity/plugin.test.js`（第 1331 行）
- **密钥（已脱敏）**：`ya29.e...oken`
- **链接**：https://github.com/poweruserz/OpenTokenUsage/blob/main/plugins/antigravity/plugin.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
setupSqliteMock(ctx, makeOAuthSentinelB64(ctx, { accessToken: "ya29.expired-proto-token", refreshToken: "1//refresh", expirySeconds: pastExpiry }))
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`poweruserz/OpenTokenUsage`
- **文件**：`plugins/codex/plugin.test.js`（第 1364 行）
- **密钥（已脱敏）**：`refres...oken`
- **链接**：https://github.com/poweruserz/OpenTokenUsage/blob/main/plugins/codex/plugin.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
bodyText: JSON.stringify({ access_token: "refreshed-file-token" }),
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`poweruserz/OpenTokenUsage`
- **文件**：`plugins/kiro/plugin.test.js`（第 209 行）
- **密钥（已脱敏）**：`refres...oken`
- **链接**：https://github.com/poweruserz/OpenTokenUsage/blob/main/plugins/kiro/plugin.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: "refreshed-access-token",
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

