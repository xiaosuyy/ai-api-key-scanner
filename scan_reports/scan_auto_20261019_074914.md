# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-19 07:49:14 UTC |
| 扫描仓库数 | 49 |
| 扫描文件数 | 10797 |
| 发现数量 | 10 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 10 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`openai/codex-security`
- **文件**：`github-action/tests/main.test.ts`（第 270 行）
- **密钥（已脱敏）**：`synthe...uter`
- **链接**：https://github.com/openai/codex-security/blob/main/github-action/tests/main.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
Object.assign(process.env, {OPENROUTER_API_KEY:'synthetic-openrouter', FIREWORKS_API_KEY:'synthetic-fireworks',
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`openai/codex-security`
- **文件**：`github-action/tests/runtime.test.ts`（第 282 行）
- **密钥（已脱敏）**：`synthe...uter`
- **链接**：https://github.com/openai/codex-security/blob/main/github-action/tests/runtime.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
OPENROUTER_API_KEY:'synthetic-openrouter', FIREWORKS_API_KEY:'synthetic-fireworks',
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`openai/codex-security`
- **文件**：`github-action/tests/runtime.test.ts`（第 286 行）
- **密钥（已脱敏）**：`change...ture`
- **链接**：https://github.com/openai/codex-security/blob/main/github-action/tests/runtime.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
source.OPENROUTER_API_KEY = source.FIREWORKS_API_KEY = 'changed-after-capture';
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`openai/codex-security`
- **文件**：`plugins/codex-security/mcp-app/tests/test_deep_scan_executor.ts`（第 2436 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/openai/codex-security/blob/main/plugins/codex-security/mcp-app/tests/test_deep_scan_executor.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.CODEX_API_KEY = "synthetic-worker-api-key";
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`diegosouzapw/OmniRoute`
- **文件**：`@omniroute/opencode-plugin-v2/tests/warm-snapshot-identity.test.ts`（第 47 行）
- **密钥（已脱敏）**：`key-wr...nfig`
- **链接**：https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.52/@omniroute/opencode-plugin-v2/tests/warm-snapshot-identity.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
options: { baseURL, providerId: "warmid", apiKey: "key-written-in-the-config" },
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`tbphp/gpt-load`
- **文件**：`internal/control/discover_group_test.go`（第 566 行）
- **密钥（已脱敏）**：`route-...cess`
- **链接**：https://github.com/tbphp/gpt-load/blob/main/internal/control/discover_group_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
credential.AccessToken = "route-refreshed-access"
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`YosefHayim/ebay-mcp`
- **文件**：`tests/integration/authTokenPersistence.test.ts`（第 45 行）
- **密钥（已脱敏）**：`integr...oken`
- **链接**：https://github.com/YosefHayim/ebay-mcp/blob/main/tests/integration/authTokenPersistence.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: 'integration_access_token',
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`YosefHayim/ebay-mcp`
- **文件**：`tests/integration/authTokenPersistence.test.ts`（第 55 行）
- **密钥（已脱敏）**：`integr...oken`
- **链接**：https://github.com/YosefHayim/ebay-mcp/blob/main/tests/integration/authTokenPersistence.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: 'integration_app_token',
```

### 9. [MEDIUM] Generic API key assignment

- **仓库**：`YosefHayim/ebay-mcp`
- **文件**：`tests/integration/authTokenPersistence.test.ts`（第 64 行）
- **密钥（已脱敏）**：`integr...oken`
- **链接**：https://github.com/YosefHayim/ebay-mcp/blob/main/tests/integration/authTokenPersistence.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
EBAY_USER_ACCESS_TOKEN: 'integration_access_token',
```

### 10. [MEDIUM] Generic API key assignment

- **仓库**：`YosefHayim/ebay-mcp`
- **文件**：`tests/integration/authTokenPersistence.test.ts`（第 66 行）
- **密钥（已脱敏）**：`integr...oken`
- **链接**：https://github.com/YosefHayim/ebay-mcp/blob/main/tests/integration/authTokenPersistence.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
EBAY_APP_ACCESS_TOKEN: 'integration_app_token',
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

