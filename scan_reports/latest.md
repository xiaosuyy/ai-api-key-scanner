# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-10 09:35:49 UTC |
| 扫描仓库数 | 50 |
| 扫描文件数 | 8465 |
| 发现数量 | 7 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 6 |
| LOW | 1 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`mgsgde/whisper-shortcut`
- **文件**：`WhisperShortcut/KeychainCredential.swift`（第 28 行）
- **密钥（已脱敏）**：`custom...-key`
- **链接**：https://github.com/mgsgde/whisper-shortcut/blob/main/WhisperShortcut/KeychainCredential.swift
- **说明**：赋值给 API key 变量的疑似密钥。

```text
case customOpenAIChatAPIKey = "custom-openai-chat-api-key"
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`openai/codex-security`
- **文件**：`github-action/tests/main.test.ts`（第 338 行）
- **密钥（已脱敏）**：`synthe...uter`
- **链接**：https://github.com/openai/codex-security/blob/main/github-action/tests/main.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
Object.assign(process.env, {OPENROUTER_API_KEY:'synthetic-openrouter', FIREWORKS_API_KEY:'synthetic-fireworks',
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`openai/codex-security`
- **文件**：`github-action/tests/runtime.test.ts`（第 384 行）
- **密钥（已脱敏）**：`synthe...uter`
- **链接**：https://github.com/openai/codex-security/blob/main/github-action/tests/runtime.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
OPENROUTER_API_KEY:'synthetic-openrouter', FIREWORKS_API_KEY:'synthetic-fireworks',
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`openai/codex-security`
- **文件**：`github-action/tests/runtime.test.ts`（第 388 行）
- **密钥（已脱敏）**：`change...ture`
- **链接**：https://github.com/openai/codex-security/blob/main/github-action/tests/runtime.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
source.OPENROUTER_API_KEY = source.FIREWORKS_API_KEY = 'changed-after-capture';
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`lynox-ai/lynox`
- **文件**：`packages/web-ui/src/lib/components/preset-client-form.svelte.test.ts`（第 57 行）
- **密钥（已脱敏）**：`SHOPIF...CRET`
- **链接**：https://github.com/lynox-ai/lynox/blob/main/packages/web-ui/src/lib/components/preset-client-form.svelte.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
preset: 'shopify', client_id_key: 'SHOPIFY_CLIENT_ID', client_secret_key: 'SHOPIFY_CLIENT_SECRET',
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`franzjeger/SuperManager`
- **文件**：`SuperManagerMac/SuperManagerMac/Models/AppSettings.swift`（第 143 行）
- **密钥（已脱敏）**：`claude...iKey`
- **链接**：https://github.com/franzjeger/SuperManager/blob/main/SuperManagerMac/SuperManagerMac/Models/AppSettings.swift
- **说明**：赋值给 API key 变量的疑似密钥。

```text
static let anthropicApiKey           = "claude.anthropicApiKey"
```

### 7. [LOW] Generic API key assignment

- **仓库**：`Automattic/studio`
- **文件**：`apps/cli/commands/auth/tests/login.test.ts`（第 71 行）
- **密钥（已脱敏）**：`mock-a...2345`
- **链接**：https://github.com/Automattic/studio/blob/trunk/apps/cli/commands/auth/tests/login.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const mockAccessToken = 'mock-access-token-12345';
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

