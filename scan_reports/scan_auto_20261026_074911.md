# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-26 07:49:11 UTC |
| 扫描仓库数 | 44 |
| 扫描文件数 | 9416 |
| 发现数量 | 10 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 1 |
| MEDIUM | 9 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`DeliciousBuding/metapi-go`
- **文件**：`config/defaults.go`（第 7 行）
- **密钥（已脱敏）**：`change...oken`
- **链接**：https://github.com/DeliciousBuding/metapi-go/blob/master/config/defaults.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
DefaultAuthToken             = "change-me-admin-token"
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`DeliciousBuding/metapi-go`
- **文件**：`handler/admin/accounts_test.go`（第 1314 行）
- **密钥（已脱敏）**：`new-se...-xyz`
- **链接**：https://github.com/DeliciousBuding/metapi-go/blob/master/handler/admin/accounts_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
t.Errorf("expected accessToken='new-session-token-xyz', got %q", accessToken)
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`DeliciousBuding/metapi-go`
- **文件**：`handler/admin/auth_settings_test.go`（第 27 行）
- **密钥（已脱敏）**：`admin-...oken`
- **链接**：https://github.com/DeliciousBuding/metapi-go/blob/master/handler/admin/auth_settings_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
config.SetRuntime(&config.RuntimeSettings{AuthToken: "admin-auth-settings-token"})
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`woodbeary/later-dog`
- **文件**：`cloudflare/control-plane/test/sign-up-guards.test.ts`（第 213 行）
- **密钥（已脱敏）**：`0x4AAA...cret`
- **链接**：https://github.com/woodbeary/later-dog/blob/main/cloudflare/control-plane/test/sign-up-guards.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const vars = { TURNSTILE_SECRET_KEY: "0x4AAAAAAAproductionlookingsecret" };
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`elie222/rakazo`
- **文件**：`apps/api/src/security-audit.test.ts`（第 20 行）
- **密钥（已脱敏）**：`sk-or-...alue`
- **链接**：https://github.com/elie222/rakazo/blob/main/apps/api/src/security-audit.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
{ provider: "openrouter", apiKey: "sk-or-v1-secretvalue", label: "Work key" },
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`OmritRenders/elidocortex`
- **文件**：`Cortex Agent/settings/browser/elidoSettings.ts`（第 12 行）
- **密钥（已脱敏）**：`elido....ings`
- **链接**：https://github.com/OmritRenders/elidocortex/blob/main/Cortex Agent/settings/browser/elidoSettings.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
export const ELIDO_SETTINGS_COMMAND_OPEN_API_KEY = 'elido.cortex.openApiKeySettings';
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`OmritRenders/cortex-agent`
- **文件**：`settings/browser/elidoSettings.ts`（第 12 行）
- **密钥（已脱敏）**：`elido....ings`
- **链接**：https://github.com/OmritRenders/cortex-agent/blob/main/settings/browser/elidoSettings.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
export const ELIDO_SETTINGS_COMMAND_OPEN_API_KEY = 'elido.cortex.openApiKeySettings';
```

### 8. [HIGH] Anthropic API Key

- **仓库**：`pghmatt/quotadial`
- **文件**：`crates/providers/claude/src/provider_tests.rs`（第 1028 行）
- **密钥（已脱敏）**：`sk-ant...4321`
- **链接**：https://github.com/pghmatt/quotadial/blob/main/crates/providers/claude/src/provider_tests.rs
- **说明**：Anthropic Claude API 密钥。

```text
shell("sk-ant-oat01-QUOTADIAL-OTHER-TOKEN-987654321"),
```

### 9. [MEDIUM] Generic API key assignment

- **仓库**：`trick77/llmwire`
- **文件**：`messages_test.go`（第 444 行）
- **密钥（已脱敏）**：`fixtur...-key`
- **链接**：https://github.com/trick77/llmwire/blob/master/messages_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
c := clientOn(t, srv.URL, Config{APIKey: "fixture-anthropic-key", APIKeyHeader: "x-api-key",
```

### 10. [MEDIUM] Generic API key assignment

- **仓库**：`trick77/llmwire`
- **文件**：`models_test.go`（第 18 行）
- **密钥（已脱敏）**：`team-k...hape`
- **链接**：https://github.com/trick77/llmwire/blob/master/models_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
c := New(Config{BaseURL: srv.URL, APIKey: "team-key-of-no-known-shape"})
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

