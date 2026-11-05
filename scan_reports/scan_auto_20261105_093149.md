# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-05 09:31:49 UTC |
| 扫描仓库数 | 50 |
| 扫描文件数 | 9618 |
| 发现数量 | 8 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 8 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`wink-run/tokenbank`
- **文件**：`client/electron/__tests__/cursor-ide-auth.test.js`（第 39 行）
- **密钥（已脱敏）**：`eyJhbG...rtxx`
- **链接**：https://github.com/wink-run/tokenbank/blob/main/client/electron/__tests__/cursor-ide-auth.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIn0.signaturepartxx',
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`amaranthic/harnex`
- **文件**：`tests/providers.test.ts`（第 168 行）
- **密钥（已脱敏）**：`custom...cret`
- **链接**：https://github.com/amaranthic/harnex/blob/main/tests/providers.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: "custom-bearer-secret",
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`crmne/ruby_llm`
- **文件**：`docs/_advanced/rails-advanced-config.md`（第 95 行）
- **密钥（已脱敏）**：`sk-cus...-key`
- **链接**：https://github.com/crmne/ruby_llm/blob/main/docs/_advanced/rails-advanced-config.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
config.openai_api_key = 'sk-customer-specific-key'
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`crmne/ruby_llm`
- **文件**：`lib/ruby_llm.rb`（第 251 行）
- **密钥（已脱敏）**：`sk-cus...-key`
- **链接**：https://github.com/crmne/ruby_llm/blob/main/lib/ruby_llm.rb
- **说明**：赋值给 API key 变量的疑似密钥。

```text
#     config.openai_api_key = 'sk-customer-specific-key'
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`OpenHands/OpenHands`
- **文件**：`__tests__/api/automation-service.test.ts`（第 606 行）
- **密钥（已脱敏）**：`runtim...-key`
- **链接**：https://github.com/OpenHands/OpenHands/blob/main/__tests__/api/automation-service.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: "runtime-injected-key",
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`OpenHands/OpenHands`
- **文件**：`__tests__/api/mars-web-bridge.test.ts`（第 127 行）
- **密钥（已脱敏）**：`qa-typ...-key`
- **链接**：https://github.com/OpenHands/OpenHands/blob/main/__tests__/api/mars-web-bridge.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: "qa-typed-session-key",
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`OpenHands/OpenHands`
- **文件**：`__tests__/components/backends/api-key-entry-screen.test.tsx`（第 136 行）
- **密钥（已脱敏）**：`old-st...sion`
- **链接**：https://github.com/OpenHands/OpenHands/blob/main/__tests__/components/backends/api-key-entry-screen.test.tsx
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: "old-stale-key-from-previous-session",
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`elie222/rakazo`
- **文件**：`apps/api/src/security-audit.test.ts`（第 20 行）
- **密钥（已脱敏）**：`sk-or-...alue`
- **链接**：https://github.com/elie222/rakazo/blob/main/apps/api/src/security-audit.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
{ provider: "openrouter", apiKey: "sk-or-v1-secretvalue", label: "Work key" },
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

