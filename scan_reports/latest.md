# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-16 07:34:36 UTC |
| 扫描仓库数 | 47 |
| 扫描文件数 | 9935 |
| 发现数量 | 8 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 8 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`Team-Commonly/commonly`
- **文件**：`backend/__tests__/service/integrations-e2e.test.js`（第 1453 行）
- **密钥（已脱敏）**：`groupm...oken`
- **链接**：https://github.com/Team-Commonly/commonly/blob/main/backend/__tests__/service/integrations-e2e.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: 'groupme-access-token',
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`Team-Commonly/commonly`
- **文件**：`backend/__tests__/service/integrations-e2e.test.js`（第 1509 行）
- **密钥（已脱敏）**：`groupm...vate`
- **链接**：https://github.com/Team-Commonly/commonly/blob/main/backend/__tests__/service/integrations-e2e.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: 'groupme-token-heartbeat-private',
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`Team-Commonly/commonly`
- **文件**：`backend/__tests__/unit/models/integrationPublicConfig.test.js`（第 89 行）
- **密钥（已脱敏）**：`SENTIN...OKEN`
- **链接**：https://github.com/Team-Commonly/commonly/blob/main/backend/__tests__/unit/models/integrationPublicConfig.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: 'SENTINEL_ACCESS_TOKEN',
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`Team-Commonly/commonly`
- **文件**：`backend/__tests__/unit/routes/agentBinding.phase2.test.js`（第 81 行）
- **密钥（已脱敏）**：`litera...avel`
- **链接**：https://github.com/Team-Commonly/commonly/blob/main/backend/__tests__/unit/routes/agentBinding.phase2.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
PRIVATE_API_KEY: 'literal-secret-must-not-travel',
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`Team-Commonly/commonly`
- **文件**：`backend/__tests__/unit/routes/integrations.routingState.test.js`（第 69 行）
- **密钥（已脱敏）**：`SENTIN...OKEN`
- **链接**：https://github.com/Team-Commonly/commonly/blob/main/backend/__tests__/unit/routes/integrations.routingState.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: 'SENTINEL_ACCESS_TOKEN',
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`timongentzsch/uAgent`
- **文件**：`tests/integration_tools.py`（第 889 行）
- **密钥（已脱敏）**：`adjace...cret`
- **链接**：https://github.com/timongentzsch/uAgent/blob/master/tests/integration_tools.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
LOCAL_PROXY_API_KEY="adjacent-integration-secret",
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`timongentzsch/uAgent`
- **文件**：`tests/integration_ui.py`（第 1199 行）
- **密钥（已脱敏）**：`contex...inel`
- **链接**：https://github.com/timongentzsch/uAgent/blob/master/tests/integration_ui.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
OPENROUTER_API_KEY="context-secret-sentinel",
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`losseeer/codebase-teaching-agent`
- **文件**：`packages/engine/src/llm/runtime.test.ts`（第 171 行）
- **密钥（已脱敏）**：`sk-sup...alue`
- **链接**：https://github.com/losseeer/codebase-teaching-agent/blob/main/packages/engine/src/llm/runtime.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
setLlmRuntimeSettings({ apiKey: "sk-super-secret-value", inputUsdPerMillion: "0.28" });
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

