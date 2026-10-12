# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-12 09:08:31 UTC |
| 扫描仓库数 | 46 |
| 扫描文件数 | 10246 |
| 发现数量 | 12 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 12 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`sleep2agi/agent-network`
- **文件**：`agent-network/bin/cli.ts`（第 7505 行）
- **密钥（已脱敏）**：`disabl...rent`
- **链接**：https://github.com/sleep2agi/agent-network/blob/main/agent-network/bin/cli.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
COMMHUB_AUTH_TOKEN: "disabled-for-grok-cli-parent",
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`sleep2agi/agent-network`
- **文件**：`agent-network/bin/cli.ts`（第 7565 行）
- **密钥（已脱敏）**：`disabl...rent`
- **链接**：https://github.com/sleep2agi/agent-network/blob/main/agent-network/bin/cli.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
env.COMMHUB_AUTH_TOKEN = "disabled-for-grok-cli-parent";
```

### 3. [MEDIUM] AWS Access Key ID

- **仓库**：`berkayturanci/ai-jury`
- **文件**：`tests/test_redaction.py`（第 109 行）
- **密钥（已脱敏）**：`AKIAQR...2345`
- **链接**：https://github.com/berkayturanci/ai-jury/blob/main/tests/test_redaction.py
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
text = "AKIAABCDEFGHIJKLMNOP AKIAQRSTUVWXYZ012345"
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`RohanMuppa/brightspace-mcp-server`
- **文件**：`tests/api/client.test.ts`（第 431 行）
- **密钥（已脱敏）**：`fresh-...4321`
- **链接**：https://github.com/RohanMuppa/brightspace-mcp-server/blob/main/tests/api/client.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
freshToken.accessToken = "fresh-token-87654321";
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`RohanMuppa/brightspace-mcp-server`
- **文件**：`tests/api/client.test.ts`（第 955 行）
- **密钥（已脱敏）**：`fresh-...4321`
- **链接**：https://github.com/RohanMuppa/brightspace-mcp-server/blob/main/tests/api/client.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
freshToken.accessToken = "fresh-token-87654321";
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`RohanMuppa/brightspace-mcp-server`
- **文件**：`tests/auth/browser-live.test.ts`（第 154 行）
- **密钥（已脱敏）**：`fixtur...oken`
- **链接**：https://github.com/RohanMuppa/brightspace-mcp-server/blob/main/tests/auth/browser-live.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
return new Response(JSON.stringify({ access_token: "fixture-access-token" }), { headers: { "content-type": "application/json" } });
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`RohanMuppa/brightspace-mcp-server`
- **文件**：`tests/auth/browser-live.test.ts`（第 158 行）
- **密钥（已脱敏）**：`fixtur...oken`
- **链接**：https://github.com/RohanMuppa/brightspace-mcp-server/blob/main/tests/auth/browser-live.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
expect(first).toMatchObject({ accessToken: "fixture-access-token", csrfToken: "fixture-xsrf", tenantOrigin: BASE });
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`s3ntin3l8/runway-ai-usage-tracker`
- **文件**：`app/core/config.py`（第 55 行）
- **密钥（已脱敏）**：`sideca...cret`
- **链接**：https://github.com/s3ntin3l8/runway-ai-usage-tracker/blob/main/app/core/config.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
DEFAULT_INGEST_API_KEY = "sidecar-default-secret"
```

### 9. [MEDIUM] Google OAuth Client Secret

- **仓库**：`s3ntin3l8/runway-ai-usage-tracker`
- **文件**：`app/services/token_refresher.py`（第 42 行）
- **密钥（已脱敏）**：`GOCSPX...Fsxl`
- **链接**：https://github.com/s3ntin3l8/runway-ai-usage-tracker/blob/main/app/services/token_refresher.py
- **说明**：Google OAuth 客户端密钥。

```text
_GEMINI_CLI_CLIENT_SECRET = "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"
```

### 10. [MEDIUM] Google OAuth Client Secret

- **仓库**：`lidge-jun/opencodex`
- **文件**：`devlog/_fin/140_remaining-provider-ports/21_phase2_antigravity-oauth-cca.md`（第 32 行）
- **密钥（已脱敏）**：`GOCSPX...qDAf`
- **链接**：https://github.com/lidge-jun/opencodex/blob/main/devlog/_fin/140_remaining-provider-ports/21_phase2_antigravity-oauth-cca.md
- **说明**：Google OAuth 客户端密钥。

```text
ClientSecret     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
```

### 11. [MEDIUM] Generic API key assignment

- **仓库**：`aipoch/open-science`
- **文件**：`e2e/pdf-translation-pair.spec.ts`（第 132 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/aipoch/open-science/blob/main/e2e/pdf-translation-pair.spec.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
api_key: 'synthetic-private-key'
```

### 12. [MEDIUM] Generic API key assignment

- **仓库**：`balkhaev/devhub`
- **文件**：`test/ai-accounts.test.ts`（第 519 行）
- **密钥（已脱敏）**：`rotate...nect`
- **链接**：https://github.com/balkhaev/devhub/blob/main/test/ai-accounts.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: "rotated-after-disconnect",
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

