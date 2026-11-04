# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-04 09:03:21 UTC |
| 扫描仓库数 | 48 |
| 扫描文件数 | 9518 |
| 发现数量 | 20 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 6 |
| MEDIUM | 14 |

## 发现明细

### 1. [HIGH] OpenAI API Key

- **仓库**：`yym68686/uni-api`
- **文件**：`README.md`（第 59 行）
- **密钥（已脱敏）**：`sk-Pkj...pQxx`
- **链接**：https://github.com/yym68686/uni-api/blob/main/README.md
- **说明**：OpenAI 风格 sk- 密钥（也覆盖 DeepSeek、Moonshot 等同类前缀）。

```text
- api: sk-Pkj60Yf8JFWxfgRmXQFWyGtWUddGZnmi3KlvowmRWpWpQxx # API Key, user request uni-api requires API key, required
```

### 2. [HIGH] OpenAI API Key

- **仓库**：`yym68686/uni-api`
- **文件**：`README.md`（第 257 行）
- **密钥（已脱敏）**：`sk-Kjj...pQRo`
- **链接**：https://github.com/yym68686/uni-api/blob/main/README.md
- **说明**：OpenAI 风格 sk- 密钥（也覆盖 DeepSeek、Moonshot 等同类前缀）。

```text
- api: sk-KjjI60Yf0JFWxfgRmXqFWyGtWUd9GZnmi3KlvowmRWpWpQRo # API Key, required for users to use this service
```

### 3. [HIGH] OpenAI API Key

- **仓库**：`yym68686/uni-api`
- **文件**：`README.md`（第 264 行）
- **密钥（已脱敏）**：`sk-pkh...qrhy`
- **链接**：https://github.com/yym68686/uni-api/blob/main/README.md
- **说明**：OpenAI 风格 sk- 密钥（也覆盖 DeepSeek、Moonshot 等同类前缀）。

```text
- api: sk-pkhf60Yf0JGyJxgRmXqFQyTgWUd9GZnmi3KlvowmRWpWqrhy
```

### 4. [HIGH] OpenAI API Key

- **仓库**：`yym68686/uni-api`
- **文件**：`README_CN.md`（第 59 行）
- **密钥（已脱敏）**：`sk-Pkj...pQxx`
- **链接**：https://github.com/yym68686/uni-api/blob/main/README_CN.md
- **说明**：OpenAI 风格 sk- 密钥（也覆盖 DeepSeek、Moonshot 等同类前缀）。

```text
- api: sk-Pkj60Yf8JFWxfgRmXQFWyGtWUddGZnmi3KlvowmRWpWpQxx # API Key，用户请求 uni-api 需要 API key，必填
```

### 5. [HIGH] OpenAI API Key

- **仓库**：`yym68686/uni-api`
- **文件**：`README_CN.md`（第 257 行）
- **密钥（已脱敏）**：`sk-Kjj...pQRo`
- **链接**：https://github.com/yym68686/uni-api/blob/main/README_CN.md
- **说明**：OpenAI 风格 sk- 密钥（也覆盖 DeepSeek、Moonshot 等同类前缀）。

```text
- api: sk-KjjI60Yf0JFWxfgRmXqFWyGtWUd9GZnmi3KlvowmRWpWpQRo # API Key，用户使用本服务需要 API key，必填
```

### 6. [HIGH] OpenAI API Key

- **仓库**：`yym68686/uni-api`
- **文件**：`README_CN.md`（第 264 行）
- **密钥（已脱敏）**：`sk-pkh...qrhy`
- **链接**：https://github.com/yym68686/uni-api/blob/main/README_CN.md
- **说明**：OpenAI 风格 sk- 密钥（也覆盖 DeepSeek、Moonshot 等同类前缀）。

```text
- api: sk-pkhf60Yf0JGyJxgRmXqFQyTgWUd9GZnmi3KlvowmRWpWqrhy
```

### 7. [MEDIUM] AWS Access Key ID

- **仓库**：`langwatch/langwatch`
- **文件**：`.github/scripts/__tests__/secrets-scan.test.sh`（第 26 行）
- **密钥（已脱敏）**：`AKIAQY...ZAM2`
- **链接**：https://github.com/langwatch/langwatch/blob/main/.github/scripts/__tests__/secrets-scan.test.sh
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
readonly PLANTED_SECRET='AWS_ACCESS_KEY_ID=AKIAQYLPMN5HHHFPZAM2
```

### 8. [MEDIUM] AWS Access Key ID

- **仓库**：`langwatch/langwatch`
- **文件**：`.gitleaks.toml`（第 122 行）
- **密钥（已脱敏）**：`AKIAQY...ZAM2`
- **链接**：https://github.com/langwatch/langwatch/blob/main/.gitleaks.toml
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
regexes = ['''AKIAQYLPMN5HHHFPZAM2''', '''A1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q7R8S9T0''']
```

### 9. [MEDIUM] Generic API key assignment

- **仓库**：`cheaper-inference/OmniRoute`
- **文件**：`@omniroute/opencode-plugin-v2/tests/warm-snapshot-identity.test.ts`（第 47 行）
- **密钥（已脱敏）**：`key-wr...nfig`
- **链接**：https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.53/@omniroute/opencode-plugin-v2/tests/warm-snapshot-identity.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
options: { baseURL, providerId: "warmid", apiKey: "key-written-in-the-config" },
```

### 10. [MEDIUM] Generic API key assignment

- **仓库**：`rowboatlabs/rowboat`
- **文件**：`apps/harbor/packages/server/test/managed-billing.test.ts`（第 220 行）
- **密钥（已脱敏）**：`sk-or-...1234`
- **链接**：https://github.com/rowboatlabs/rowboat/blob/main/apps/harbor/packages/server/test/managed-billing.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const r = await as('dev-ramnique').put(`/v1/agents/${hermes.id}/hosting/llm`, { provider: 'openrouter', apiKey: 'sk-or-owner-key-1234' });
```

### 11. [MEDIUM] Generic API key assignment

- **仓库**：`rowboatlabs/rowboat`
- **文件**：`apps/harbor/packages/server/test/maritime-managed.test.ts`（第 332 行）
- **密钥（已脱敏）**：`sk-ant...abcd`
- **链接**：https://github.com/rowboatlabs/rowboat/blob/main/apps/harbor/packages/server/test/maritime-managed.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const claude = (await me.post('/v1/agents/managed', { displayName: 'Own', kind: 'claude-code', anthropicApiKey: 'sk-ant-api03-ownkey-abcd' })).body as { hosting: AgentHosting };
```

### 12. [MEDIUM] Generic API key assignment

- **仓库**：`rowboatlabs/rowboat`
- **文件**：`apps/harbor/packages/server/test/maritime-managed.test.ts`（第 343 行）
- **密钥（已脱敏）**：`sk-ant...wxyz`
- **链接**：https://github.com/rowboatlabs/rowboat/blob/main/apps/harbor/packages/server/test/maritime-managed.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const set = await me.put(`/v1/agents/${agent.id}/hosting/llm`, { provider: 'anthropic', apiKey: 'sk-ant-api03-mine-wxyz', model: 'claude-sonnet-4-5' });
```

### 13. [MEDIUM] Generic API key assignment

- **仓库**：`rowboatlabs/rowboat`
- **文件**：`apps/harbor/packages/server/test/maritime-managed.test.ts`（第 371 行）
- **密钥（已脱敏）**：`sk-ant...o-no`
- **链接**：https://github.com/rowboatlabs/rowboat/blob/main/apps/harbor/packages/server/test/maritime-managed.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
expect((await me.put(`/v1/agents/${codex.agent.id}/hosting/llm`, { provider: 'anthropic', apiKey: 'sk-ant-api03-no-no-no' })).status).toBe(400);
```

### 14. [MEDIUM] Generic API key assignment

- **仓库**：`rowboatlabs/rowboat`
- **文件**：`apps/harbor/packages/server/test/maritime-managed.test.ts`（第 372 行）
- **密钥（已脱敏）**：`sk-pro...1234`
- **链接**：https://github.com/rowboatlabs/rowboat/blob/main/apps/harbor/packages/server/test/maritime-managed.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
expect((await me.put(`/v1/agents/${codex.agent.id}/hosting/llm`, { provider: 'openai', apiKey: 'sk-proj-openai-key-1234' })).status).toBe(200);
```

### 15. [MEDIUM] Generic API key assignment

- **仓库**：`rowboatlabs/rowboat`
- **文件**：`apps/harbor/packages/server/test/maritime-managed.test.ts`（第 376 行）
- **密钥（已脱敏）**：`sk-pro...0000`
- **链接**：https://github.com/rowboatlabs/rowboat/blob/main/apps/harbor/packages/server/test/maritime-managed.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
expect((await org.as('dev-harsh').put(`/v1/agents/${agent.id}/hosting/llm`, { provider: 'openai', apiKey: 'sk-proj-harsh-key-0000' })).status).toBe(403);
```

### 16. [MEDIUM] Generic API key assignment

- **仓库**：`rowboatlabs/rowboat`
- **文件**：`apps/harbor/packages/server/test/maritime-managed.test.ts`（第 401 行）
- **密钥（已脱敏）**：`sk-pro...5678`
- **链接**：https://github.com/rowboatlabs/rowboat/blob/main/apps/harbor/packages/server/test/maritime-managed.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
expect((await me.put(`/v1/agents/${agent.id}/hosting/llm`, { provider: 'openai', apiKey: 'sk-proj-openai-key-5678' })).body.hosting).toMatchObject({ funding: 'own', trial: { closedReason: 'exhausted' } });
```

### 17. [MEDIUM] Generic API key assignment

- **仓库**：`rowboatlabs/rowboat`
- **文件**：`apps/harbor/packages/server/test/maritime-managed.test.ts`（第 453 行）
- **密钥（已脱敏）**：`sk-pro...9999`
- **链接**：https://github.com/rowboatlabs/rowboat/blob/main/apps/harbor/packages/server/test/maritime-managed.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
expect((await me.put(`/v1/agents/${agent.id}/hosting/llm`, { provider: 'openai', apiKey: 'sk-proj-openai-key-9999' })).body.hosting).toMatchObject({ funding: 'own', llm: { provider: 'openai', keyHint: '…9999' } });
```

### 18. [MEDIUM] Generic API key assignment

- **仓库**：`gogoymh/decision-model-guided-function-calling`
- **文件**：`src/jev_fc/cli.py`（第 79 行）
- **密钥（已脱敏）**：`config...only`
- **链接**：https://github.com/gogoymh/decision-model-guided-function-calling/blob/main/src/jev_fc/cli.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
generator = FunctionCallingLLM(api_key="configuration-check-only")
```

### 19. [MEDIUM] Generic API key assignment

- **仓库**：`gogoymh/decision-model-guided-function-calling`
- **文件**：`src/jev_fc/cli.py`（第 82 行）
- **密钥（已脱敏）**：`config...only`
- **链接**：https://github.com/gogoymh/decision-model-guided-function-calling/blob/main/src/jev_fc/cli.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
verifier = JevVerifier(api_key="configuration-check-only")
```

### 20. [MEDIUM] Generic API key assignment

- **仓库**：`gogoymh/decision-model-guided-function-calling`
- **文件**：`tests/test_calibration.py`（第 189 行）
- **密钥（已脱敏）**：`OFFLIN...NARY`
- **链接**：https://github.com/gogoymh/decision-model-guided-function-calling/blob/main/tests/test_calibration.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
**settings, api_key="OFFLINE-CREDENTIAL-CANARY", headers={"api-key": "OFFLINE-CREDENTIAL-CANARY"})
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

