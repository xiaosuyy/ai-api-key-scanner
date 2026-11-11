# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-11 09:11:28 UTC |
| 扫描仓库数 | 45 |
| 扫描文件数 | 6429 |
| 发现数量 | 16 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 5 |
| MEDIUM | 11 |

## 发现明细

### 1. [HIGH] Google Gemini / GCP API Key

- **仓库**：`ZGhey/linglens`
- **文件**：`e2e/onboarding.spec.ts`（第 32 行）
- **密钥（已脱敏）**：`AIzaGO...0000`
- **链接**：https://github.com/ZGhey/linglens/blob/main/e2e/onboarding.spec.ts
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
return key === 'AIzaGOODKEY0000000000000000000000000000'
```

### 2. [HIGH] Google Gemini / GCP API Key

- **仓库**：`ZGhey/linglens`
- **文件**：`e2e/onboarding.spec.ts`（第 67 行）
- **密钥（已脱敏）**：`AIzaGO...0000`
- **链接**：https://github.com/ZGhey/linglens/blob/main/e2e/onboarding.spec.ts
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
await keyInput.fill('AIzaGOODKEY0000000000000000000000000000')
```

### 3. [HIGH] Google Gemini / GCP API Key

- **仓库**：`ZGhey/linglens`
- **文件**：`e2e/onboarding.spec.ts`（第 74 行）
- **密钥（已脱敏）**：`AIzaGO...0000`
- **链接**：https://github.com/ZGhey/linglens/blob/main/e2e/onboarding.spec.ts
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
apiKeys: { gemini: 'AIzaGOODKEY0000000000000000000000000000' },
```

### 4. [HIGH] Google Gemini / GCP API Key

- **仓库**：`ZGhey/linglens`
- **文件**：`e2e/onboarding.spec.ts`（第 230 行）
- **密钥（已脱敏）**：`AIzaNE...0000`
- **链接**：https://github.com/ZGhey/linglens/blob/main/e2e/onboarding.spec.ts
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
await page.locator('#apiKey').fill('AIzaNEWKEY000000000000000000000000000000')
```

### 5. [HIGH] Google Gemini / GCP API Key

- **仓库**：`ZGhey/linglens`
- **文件**：`scripts/demo/record.spec.ts`（第 259 行）
- **密钥（已脱敏）**：`AIzaSy...0000`
- **链接**：https://github.com/ZGhey/linglens/blob/main/scripts/demo/record.spec.ts
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
await page.locator('#geminiKey').fill('AIzaSyD3m0-Linglens-demo-key-0000000000')
```

### 6. [MEDIUM] Google OAuth Client Secret

- **仓库**：`lidge-jun/opencodex`
- **文件**：`devlog/_fin/140_remaining-provider-ports/21_phase2_antigravity-oauth-cca.md`（第 32 行）
- **密钥（已脱敏）**：`GOCSPX...qDAf`
- **链接**：https://github.com/lidge-jun/opencodex/blob/dev/devlog/_fin/140_remaining-provider-ports/21_phase2_antigravity-oauth-cca.md
- **说明**：Google OAuth 客户端密钥。

```text
ClientSecret     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
```

### 7. [MEDIUM] Google OAuth Client Secret

- **仓库**：`router-for-me/CLIProxyAPI`
- **文件**：`internal/api/handlers/management/api_tools.go`（第 28 行）
- **密钥（已脱敏）**：`GOCSPX...qDAf`
- **链接**：https://github.com/router-for-me/CLIProxyAPI/blob/main/internal/api/handlers/management/api_tools.go
- **说明**：Google OAuth 客户端密钥。

```text
antigravityOAuthClientSecret = "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"
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`router-for-me/CLIProxyAPI`
- **文件**：`internal/api/handlers/management/api_tools_test.go`（第 948 行）
- **密钥（已脱敏）**：`xai-va...oken`
- **链接**：https://github.com/router-for-me/CLIProxyAPI/blob/main/internal/api/handlers/management/api_tools_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
AccessToken:   "xai-valid-storage-token",
```

### 9. [MEDIUM] Generic API key assignment

- **仓库**：`router-for-me/CLIProxyAPI`
- **文件**：`internal/api/handlers/management/api_tools_test.go`（第 1176 行）
- **密钥（已脱敏）**：`xai-re...oken`
- **链接**：https://github.com/router-for-me/CLIProxyAPI/blob/main/internal/api/handlers/management/api_tools_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
AccessToken:   "xai-real-access-token",
```

### 10. [MEDIUM] Generic API key assignment

- **仓库**：`router-for-me/CLIProxyAPI`
- **文件**：`internal/api/handlers/management/api_tools_test.go`（第 1258 行）
- **密钥（已脱敏）**：`xai-st...rent`
- **链接**：https://github.com/router-for-me/CLIProxyAPI/blob/main/internal/api/handlers/management/api_tools_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
AccessToken:   "xai-stale-concurrent",
```

### 11. [MEDIUM] Generic API key assignment

- **仓库**：`router-for-me/CLIProxyAPI`
- **文件**：`internal/api/handlers/management/auth_files_cooldown_test.go`（第 1333 行）
- **密钥（已脱敏）**：`secret...oken`
- **链接**：https://github.com/router-for-me/CLIProxyAPI/blob/main/internal/api/handlers/management/auth_files_cooldown_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
RejectedAccessToken:  "secret-dead-access-token",
```

### 12. [MEDIUM] Generic API key assignment

- **仓库**：`router-for-me/CLIProxyAPI`
- **文件**：`internal/api/handlers/management/auth_files_targeted_oauth_test.go`（第 425 行）
- **密钥（已脱敏）**：`ag-fre...atch`
- **链接**：https://github.com/router-for-me/CLIProxyAPI/blob/main/internal/api/handlers/management/auth_files_targeted_oauth_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
agSvc.accessToken = "ag-fresh-token-match"
```

### 13. [MEDIUM] Generic API key assignment

- **仓库**：`router-for-me/CLIProxyAPI`
- **文件**：`internal/api/handlers/management/auth_files_targeted_oauth_test.go`（第 920 行）
- **密钥（已脱敏）**：`xai-em...resh`
- **链接**：https://github.com/router-for-me/CLIProxyAPI/blob/main/internal/api/handlers/management/auth_files_targeted_oauth_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
xaiSvc.accessToken = "xai-email-only-fresh"
```

### 14. [MEDIUM] Generic API key assignment

- **仓库**：`NenoPetkov/paperfrog`
- **文件**：`tests/integration/test_adaptive.py`（第 314 行）
- **密钥（已脱敏）**：`privat...alue`
- **链接**：https://github.com/NenoPetkov/paperfrog/blob/master/tests/integration/test_adaptive.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
s = ai_settings(settings, binance_api_secret="private-sentinel-value")
```

### 15. [MEDIUM] Generic API key assignment

- **仓库**：`NenoPetkov/paperfrog`
- **文件**：`tests/unit/test_readiness.py`（第 54 行）
- **密钥（已脱敏）**：`dedica...-key`
- **链接**：https://github.com/NenoPetkov/paperfrog/blob/master/tests/unit/test_readiness.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
binance_api_key="dedicated-account-key",
```

### 16. [MEDIUM] Generic API key assignment

- **仓库**：`pingmike2/freebuff2api-wokers`
- **文件**：`worker.js`（第 3 行）
- **密钥（已脱敏）**：`freebu...-key`
- **链接**：https://github.com/pingmike2/freebuff2api-wokers/blob/main/worker.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const DEFAULT_API_KEY = "freebuff-default-key";
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

