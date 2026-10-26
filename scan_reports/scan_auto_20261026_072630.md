# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-26 07:26:30 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 4747 |
| 发现数量 | 17 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 6 |
| MEDIUM | 11 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`BertMarti/modelduel`
- **文件**：`docs/USO.md`（第 333 行）
- **密钥（已脱敏）**：`PEGA_A...UTER`
- **链接**：https://github.com/BertMarti/modelduel/blob/main/docs/USO.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
$env:OPENAI_API_KEY = "PEGA_AQUI_TU_CLAVE_DE_OPENROUTER"
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`BertMarti/modelduel`
- **文件**：`docs/USO.md`（第 340 行）
- **密钥（已脱敏）**：`PEGA_A...UTER`
- **链接**：https://github.com/BertMarti/modelduel/blob/main/docs/USO.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
export OPENAI_API_KEY="PEGA_AQUI_TU_CLAVE_DE_OPENROUTER"
```

### 3. [HIGH] Anthropic API Key

- **仓库**：`BerriAI/litellm`
- **文件**：`.github/workflows/e2e_record_replay.yml`（第 146 行）
- **密钥（已脱敏）**：`sk-ant...ider`
- **链接**：https://github.com/BerriAI/litellm/blob/main/.github/workflows/e2e_record_replay.yml
- **说明**：Anthropic Claude API 密钥。

```text
ANTHROPIC_API_KEY: sk-ant-replay-must-never-reach-a-provider
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`DrBradStanfield/roadmap`
- **文件**：`app/lib/email-confirmation-unsubscribe.test.ts`（第 4 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/DrBradStanfield/roadmap/blob/main/app/lib/email-confirmation-unsubscribe.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.RESEND_API_KEY = 'synthetic-not-a-real-key';
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`DrBradStanfield/roadmap`
- **文件**：`app/routes/mcp.hosted-guards.test.ts`（第 59 行）
- **密钥（已脱敏）**：`dropbo...oken`
- **链接**：https://github.com/DrBradStanfield/roadmap/blob/main/app/routes/mcp.hosted-guards.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: 'dropbox-access-token',
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`DrBradStanfield/roadmap`
- **文件**：`app/routes/mcp.hosted.test.ts`（第 56 行）
- **密钥（已脱敏）**：`dropbo...oken`
- **链接**：https://github.com/DrBradStanfield/roadmap/blob/main/app/routes/mcp.hosted.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: 'dropbox-access-token',
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`DrBradStanfield/roadmap`
- **文件**：`app/routes/mcp.knowledge.test.ts`（第 72 行）
- **密钥（已脱敏）**：`dropbo...oken`
- **链接**：https://github.com/DrBradStanfield/roadmap/blob/main/app/routes/mcp.knowledge.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: 'dropbox-access-token',
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`DrBradStanfield/roadmap`
- **文件**：`app/routes/mcp.reviewer.test.ts`（第 88 行）
- **密钥（已脱敏）**：`dropbo...oken`
- **链接**：https://github.com/DrBradStanfield/roadmap/blob/main/app/routes/mcp.reviewer.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
return Response.json({ refresh_token: `dropbox-refresh-token-${++connections}`, access_token: 'dropbox-access-token', expires_in: 14400 });
```

### 9. [MEDIUM] Generic API key assignment

- **仓库**：`woodbeary/later-dog`
- **文件**：`cloudflare/control-plane/test/sign-up-guards.test.ts`（第 213 行）
- **密钥（已脱敏）**：`0x4AAA...cret`
- **链接**：https://github.com/woodbeary/later-dog/blob/main/cloudflare/control-plane/test/sign-up-guards.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const vars = { TURNSTILE_SECRET_KEY: "0x4AAAAAAAproductionlookingsecret" };
```

### 10. [HIGH] Anthropic API Key

- **仓库**：`EXXETA/exxperts`
- **文件**：`apps/web-server/scripts/anthropic-api-key-provider-smoke.ts`（第 219 行）
- **密钥（已脱敏）**：`sk-ant...oken`
- **链接**：https://github.com/EXXETA/exxperts/blob/main/apps/web-server/scripts/anthropic-api-key-provider-smoke.ts
- **说明**：Anthropic Claude API 密钥。

```text
const token = await api("/api/auth/api-key", { method: "POST", body: JSON.stringify({ provider: KEY_PROVIDER, key: "sk-ant-oat01-synthetic-pasted-token" }) });
```

### 11. [MEDIUM] Generic API key assignment

- **仓库**：`EXXETA/exxperts`
- **文件**：`apps/web-server/scripts/anthropic-api-key-provider-smoke.ts`（第 189 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/EXXETA/exxperts/blob/main/apps/web-server/scripts/anthropic-api-key-provider-smoke.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
env: smokeHomeEnv(tempHome, { PORT: String(port), ...SMOKE_SERVER_AUTH_ENV, EXXETA_HOME: repoRoot, EXXPERTS_CODING_AGENT_DIR: agentDir, EXXETA_PERSISTENT_AGENTS_ROOT: agentsRoot, ANTHROPIC_API_KEY: "synthetic-environment-key", ANTHROPIC_OAUTH_TOKEN: "synthetic-environment-token" }) as NodeJS.ProcessEnv,
```

### 12. [MEDIUM] Generic API key assignment

- **仓库**：`EXXETA/exxperts`
- **文件**：`apps/web-server/scripts/anthropic-api-key-provider-smoke.ts`（第 189 行）
- **密钥（已脱敏）**：`synthe...oken`
- **链接**：https://github.com/EXXETA/exxperts/blob/main/apps/web-server/scripts/anthropic-api-key-provider-smoke.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
env: smokeHomeEnv(tempHome, { PORT: String(port), ...SMOKE_SERVER_AUTH_ENV, EXXETA_HOME: repoRoot, EXXPERTS_CODING_AGENT_DIR: agentDir, EXXETA_PERSISTENT_AGENTS_ROOT: agentsRoot, ANTHROPIC_API_KEY: "synthetic-environment-key", ANTHROPIC_OAUTH_TOKEN: "synthetic-environment-token" }) as NodeJS.ProcessEnv,
```

### 13. [MEDIUM] Generic API key assignment

- **仓库**：`EXXETA/exxperts`
- **文件**：`apps/web-server/scripts/gateway-bare-403-smoke.ts`（第 99 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/EXXETA/exxperts/blob/main/apps/web-server/scripts/gateway-bare-403-smoke.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const answer = await complete(model as never, { messages: [{ role: "user", content: "Hello", timestamp: Date.now() }] }, { apiKey: "synthetic-gateway-key" });
```

### 14. [HIGH] Anthropic API Key

- **仓库**：`EXXETA/exxperts`
- **文件**：`apps/web-server/scripts/native-provider-search-smoke.ts`（第 62 行）
- **密钥（已脱敏）**：`sk-ant...rint`
- **链接**：https://github.com/EXXETA/exxperts/blob/main/apps/web-server/scripts/native-provider-search-smoke.ts
- **说明**：Anthropic Claude API 密钥。

```text
else if (type === "oauth") existing.anthropic = { type: "oauth", access: "sk-ant-oat-synthetic-do-not-print", refresh: "synthetic-refresh", expires: Date.now() + 600_000 };
```

### 15. [HIGH] Anthropic API Key

- **仓库**：`EXXETA/exxperts`
- **文件**：`apps/web-server/scripts/native-provider-search-smoke.ts`（第 63 行）
- **密钥（已脱敏）**：`sk-ant...rint`
- **链接**：https://github.com/EXXETA/exxperts/blob/main/apps/web-server/scripts/native-provider-search-smoke.ts
- **说明**：Anthropic Claude API 密钥。

```text
else existing.anthropic = { type: "api_key", key: "sk-ant-api-synthetic-do-not-print" };
```

### 16. [HIGH] Anthropic API Key

- **仓库**：`EXXETA/exxperts`
- **文件**：`apps/web-server/scripts/native-provider-search-smoke.ts`（第 168 行）
- **密钥（已脱敏）**：`sk-ant...rint`
- **链接**：https://github.com/EXXETA/exxperts/blob/main/apps/web-server/scripts/native-provider-search-smoke.ts
- **说明**：Anthropic Claude API 密钥。

```text
anthropic: { type: "oauth", access: "sk-ant-oat-synthetic-do-not-print", refresh: "synthetic-refresh", expires: Date.now() + 600_000 },
```

### 17. [HIGH] Anthropic API Key

- **仓库**：`EXXETA/exxperts`
- **文件**：`apps/web-server/scripts/native-provider-search-smoke.ts`（第 529 行）
- **密钥（已脱敏）**：`sk-ant...rint`
- **链接**：https://github.com/EXXETA/exxperts/blob/main/apps/web-server/scripts/native-provider-search-smoke.ts
- **说明**：Anthropic Claude API 密钥。

```text
parsedAuth.anthropic = { type: "api_key", key: "sk-ant-api-synthetic-do-not-print" };
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

