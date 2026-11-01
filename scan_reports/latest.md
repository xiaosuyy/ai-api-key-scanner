# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-01 08:58:46 UTC |
| 扫描仓库数 | 45 |
| 扫描文件数 | 4585 |
| 发现数量 | 8 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 8 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`Team-Commonly/commonly`
- **文件**：`backend/__tests__/service/integrations-e2e.test.js`（第 1454 行）
- **密钥（已脱敏）**：`groupm...oken`
- **链接**：https://github.com/Team-Commonly/commonly/blob/main/backend/__tests__/service/integrations-e2e.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: 'groupme-access-token',
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`Team-Commonly/commonly`
- **文件**：`backend/__tests__/service/integrations-e2e.test.js`（第 1510 行）
- **密钥（已脱敏）**：`groupm...vate`
- **链接**：https://github.com/Team-Commonly/commonly/blob/main/backend/__tests__/service/integrations-e2e.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: 'groupme-token-heartbeat-private',
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`Team-Commonly/commonly`
- **文件**：`backend/__tests__/service/oauthBrowserBinding.test.js`（第 38 行）
- **密钥（已脱敏）**：`synthe...oken`
- **链接**：https://github.com/Team-Commonly/commonly/blob/main/backend/__tests__/service/oauthBrowserBinding.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
return { data: { access_token: 'synthetic-provider-token' } };
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

- **仓库**：`OpenHands/OpenHands`
- **文件**：`__tests__/api/automation-service.test.ts`（第 607 行）
- **密钥（已脱敏）**：`runtim...-key`
- **链接**：https://github.com/OpenHands/OpenHands/blob/main/__tests__/api/automation-service.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: "runtime-injected-key",
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`OpenHands/OpenHands`
- **文件**：`__tests__/api/mars-web-bridge.test.ts`（第 127 行）
- **密钥（已脱敏）**：`qa-typ...-key`
- **链接**：https://github.com/OpenHands/OpenHands/blob/main/__tests__/api/mars-web-bridge.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: "qa-typed-session-key",
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`OpenHands/OpenHands`
- **文件**：`__tests__/components/backends/api-key-entry-screen.test.tsx`（第 136 行）
- **密钥（已脱敏）**：`old-st...sion`
- **链接**：https://github.com/OpenHands/OpenHands/blob/main/__tests__/components/backends/api-key-entry-screen.test.tsx
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: "old-stale-key-from-previous-session",
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

