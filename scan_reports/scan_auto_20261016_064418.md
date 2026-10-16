# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-16 06:44:18 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 3520 |
| 发现数量 | 15 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 1 |
| MEDIUM | 14 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`circle-platforms/circle`
- **文件**：`apps/desktop/test/runtime.test.ts`（第 2167 行）
- **密钥（已脱敏）**：`local-...cret`
- **链接**：https://github.com/circle-platforms/circle/blob/main/apps/desktop/test/runtime.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: 'local-fixture-secret',
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`circle-platforms/circle`
- **文件**：`apps/desktop/test/runtime.test.ts`（第 4622 行）
- **密钥（已脱敏）**：`synthe...only`
- **链接**：https://github.com/circle-platforms/circle/blob/main/apps/desktop/test/runtime.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: 'synthetic-local-only',
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`circle-platforms/circle`
- **文件**：`scripts/verify-tui-sessions.ts`（第 69 行）
- **密钥（已脱敏）**：`synthe...only`
- **链接**：https://github.com/circle-platforms/circle/blob/main/scripts/verify-tui-sessions.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
saveCredentials({ api_key: 'synthetic-local-only' }, home);
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`sssstwee/switch-plus-plus`
- **文件**：`src/appConstants.ts`（第 107 行）
- **密钥（已脱敏）**：`agent-...eway`
- **链接**：https://github.com/sssstwee/switch-plus-plus/blob/main/src/appConstants.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
export const CLAUDE_CLI_LOCAL_GATEWAY_AUTH_TOKEN = "agent-switch-local-gateway";
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`sssstwee/switch-plus-plus`
- **文件**：`src/appConstants.ts`（第 108 行）
- **密钥（已脱敏）**：`agent-...eway`
- **链接**：https://github.com/sssstwee/switch-plus-plus/blob/main/src/appConstants.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
export const CODEX_LOCAL_GATEWAY_AUTH_TOKEN = "agent-switch-local-gateway";
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`sssstwee/switch-plus-plus`
- **文件**：`src/profileDisplayUtils.ts`（第 20 行）
- **密钥（已脱敏）**：`ANTHRO...OKEN`
- **链接**：https://github.com/sssstwee/switch-plus-plus/blob/main/src/profileDisplayUtils.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
ANTHROPIC_AUTH_TOKEN: "ANTHROPIC_AUTH_TOKEN",
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`sssstwee/switch-plus-plus`
- **文件**：`src/subscriptionProxyConfig.test.ts`（第 36 行）
- **密钥（已脱敏）**：`agent-...eway`
- **链接**：https://github.com/sssstwee/switch-plus-plus/blob/main/src/subscriptionProxyConfig.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
gateway_api_key: "agent-switch-local-gateway",
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`loopengine-co/loopengine`
- **文件**：`tests/deepseek-model-call.test.ts`（第 37 行）
- **密钥（已脱敏）**：`sk-ope...seek`
- **链接**：https://github.com/loopengine-co/loopengine/blob/main/tests/deepseek-model-call.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.OPENAI_API_KEY = 'sk-openai-should-not-leak-into-deepseek'
```

### 9. [MEDIUM] Generic API key assignment

- **仓库**：`loopengine-co/loopengine`
- **文件**：`tests/gemini-model-call.test.ts`（第 40 行）
- **密钥（已脱敏）**：`sk-ope...mini`
- **链接**：https://github.com/loopengine-co/loopengine/blob/main/tests/gemini-model-call.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.OPENAI_API_KEY = 'sk-openai-should-not-leak-into-gemini'
```

### 10. [MEDIUM] Generic API key assignment

- **仓库**：`loopengine-co/loopengine`
- **文件**：`tests/glm-model-call.test.ts`（第 37 行）
- **密钥（已脱敏）**：`sk-ope...-glm`
- **链接**：https://github.com/loopengine-co/loopengine/blob/main/tests/glm-model-call.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.OPENAI_API_KEY = 'sk-openai-should-not-leak-into-glm'
```

### 11. [MEDIUM] Generic API key assignment

- **仓库**：`loopengine-co/loopengine`
- **文件**：`tests/kimi-model-call.test.ts`（第 37 行）
- **密钥（已脱敏）**：`sk-ope...kimi`
- **链接**：https://github.com/loopengine-co/loopengine/blob/main/tests/kimi-model-call.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.OPENAI_API_KEY = 'sk-openai-should-not-leak-into-kimi'
```

### 12. [MEDIUM] Generic API key assignment

- **仓库**：`loopengine-co/loopengine`
- **文件**：`tests/model-key-rebuild.test.ts`（第 14 行）
- **密钥（已脱敏）**：`sk-sec...6789`
- **链接**：https://github.com/loopengine-co/loopengine/blob/main/tests/model-key-rebuild.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.OPENAI_API_KEY = 'sk-second-0123456789'
```

### 13. [MEDIUM] Generic API key assignment

- **仓库**：`loopengine-co/loopengine`
- **文件**：`tests/model-key-rebuild.test.ts`（第 21 行）
- **密钥（已脱敏）**：`sk-con...6789`
- **链接**：https://github.com/loopengine-co/loopengine/blob/main/tests/model-key-rebuild.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const create = await synthesizeCreateModelCall({ provider: 'openai', model: 'gpt-test', apiKey: 'sk-config-0123456789' })
```

### 14. [HIGH] Google Gemini / GCP API Key

- **仓库**：`lavkeshdwivedi/geo-pulse`
- **文件**：`mobile/android/app/google-services.json`（第 18 行）
- **密钥（已脱敏）**：`AIzaSy...jVvM`
- **链接**：https://github.com/lavkeshdwivedi/geo-pulse/blob/main/mobile/android/app/google-services.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"current_key": "AIzaSyCIs2f4OULthJrLl2LFlbYUPCOm4GAjVvM"
```

### 15. [MEDIUM] Google OAuth Client Secret

- **仓库**：`starfall-org/multigateway`
- **文件**：`app/src/main/java/org/starfall/multigateway/data/adapter/antigravity/AntigravityAdapter.kt`（第 21 行）
- **密钥（已脱敏）**：`GOCSPX...qDAf`
- **链接**：https://github.com/starfall-org/multigateway/blob/main/app/src/main/java/org/starfall/multigateway/data/adapter/antigravity/AntigravityAdapter.kt
- **说明**：Google OAuth 客户端密钥。

```text
51121, "/oauth-callback", "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",
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

