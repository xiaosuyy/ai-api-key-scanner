# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-09 09:03:51 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 4157 |
| 发现数量 | 6 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 6 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`DrBradStanfield/roadmap`
- **文件**：`app/lib/email-confirmation-unsubscribe.test.ts`（第 4 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/DrBradStanfield/roadmap/blob/main/app/lib/email-confirmation-unsubscribe.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.RESEND_API_KEY = 'synthetic-not-a-real-key';
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`DrBradStanfield/roadmap`
- **文件**：`app/lib/email-resend-missing-id.test.ts`（第 33 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/DrBradStanfield/roadmap/blob/main/app/lib/email-resend-missing-id.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.RESEND_API_KEY = 'synthetic-not-a-real-key';
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`DrBradStanfield/roadmap`
- **文件**：`app/routes/mcp.hosted-guards.test.ts`（第 60 行）
- **密钥（已脱敏）**：`dropbo...oken`
- **链接**：https://github.com/DrBradStanfield/roadmap/blob/main/app/routes/mcp.hosted-guards.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: 'dropbox-access-token',
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`DrBradStanfield/roadmap`
- **文件**：`app/routes/mcp.hosted.test.ts`（第 56 行）
- **密钥（已脱敏）**：`dropbo...oken`
- **链接**：https://github.com/DrBradStanfield/roadmap/blob/main/app/routes/mcp.hosted.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: 'dropbox-access-token',
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`DrBradStanfield/roadmap`
- **文件**：`app/routes/mcp.knowledge.test.ts`（第 75 行）
- **密钥（已脱敏）**：`dropbo...oken`
- **链接**：https://github.com/DrBradStanfield/roadmap/blob/main/app/routes/mcp.knowledge.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: 'dropbox-access-token',
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`DrBradStanfield/roadmap`
- **文件**：`app/routes/mcp.reviewer.test.ts`（第 87 行）
- **密钥（已脱敏）**：`dropbo...oken`
- **链接**：https://github.com/DrBradStanfield/roadmap/blob/main/app/routes/mcp.reviewer.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
return Response.json({ refresh_token: `dropbox-refresh-token-${++connections}`, access_token: 'dropbox-access-token', expires_in: 14400 });
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

