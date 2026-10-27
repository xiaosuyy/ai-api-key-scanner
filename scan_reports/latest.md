# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-27 07:41:15 UTC |
| 扫描仓库数 | 47 |
| 扫描文件数 | 7240 |
| 发现数量 | 6 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 6 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`CollieAi/llm-firewall`
- **文件**：`docs/getting-started/api-keys.md`（第 47 行）
- **密钥（已脱敏）**：`clai_A...1234`
- **链接**：https://github.com/CollieAi/llm-firewall/blob/main/docs/getting-started/api-keys.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
api_key="clai_AbCSSs2IjKlMnOpQrStUvWxYz01328901234",
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`Team-Commonly/commonly`
- **文件**：`backend/__tests__/service/integrations-e2e.test.js`（第 1453 行）
- **密钥（已脱敏）**：`groupm...oken`
- **链接**：https://github.com/Team-Commonly/commonly/blob/main/backend/__tests__/service/integrations-e2e.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: 'groupme-access-token',
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`Team-Commonly/commonly`
- **文件**：`backend/__tests__/service/integrations-e2e.test.js`（第 1509 行）
- **密钥（已脱敏）**：`groupm...vate`
- **链接**：https://github.com/Team-Commonly/commonly/blob/main/backend/__tests__/service/integrations-e2e.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: 'groupme-token-heartbeat-private',
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`Team-Commonly/commonly`
- **文件**：`backend/__tests__/unit/models/integrationPublicConfig.test.js`（第 89 行）
- **密钥（已脱敏）**：`SENTIN...OKEN`
- **链接**：https://github.com/Team-Commonly/commonly/blob/main/backend/__tests__/unit/models/integrationPublicConfig.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: 'SENTINEL_ACCESS_TOKEN',
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`Team-Commonly/commonly`
- **文件**：`backend/__tests__/unit/models/integrationPublicConfig.test.js`（第 170 行）
- **密钥（已脱敏）**：`feed-a...inel`
- **链接**：https://github.com/Team-Commonly/commonly/blob/main/backend/__tests__/unit/models/integrationPublicConfig.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: 'feed-access-token-sentinel',
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`Team-Commonly/commonly`
- **文件**：`backend/__tests__/unit/routes/agentBinding.phase2.test.js`（第 83 行）
- **密钥（已脱敏）**：`litera...avel`
- **链接**：https://github.com/Team-Commonly/commonly/blob/main/backend/__tests__/unit/routes/agentBinding.phase2.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
PRIVATE_API_KEY: 'literal-secret-must-not-travel',
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

