# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-23 07:29:09 UTC |
| 扫描仓库数 | 50 |
| 扫描文件数 | 8258 |
| 发现数量 | 10 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 3 |
| MEDIUM | 5 |
| LOW | 2 |

## 发现明细

### 1. [MEDIUM] AWS Access Key ID

- **仓库**：`langwatch/langwatch`
- **文件**：`.github/scripts/__tests__/secrets-scan.test.sh`（第 26 行）
- **密钥（已脱敏）**：`AKIAQY...ZAM2`
- **链接**：https://github.com/langwatch/langwatch/blob/main/.github/scripts/__tests__/secrets-scan.test.sh
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
readonly PLANTED_SECRET='AWS_ACCESS_KEY_ID=AKIAQYLPMN5HHHFPZAM2
```

### 2. [MEDIUM] AWS Access Key ID

- **仓库**：`langwatch/langwatch`
- **文件**：`.gitleaks.toml`（第 122 行）
- **密钥（已脱敏）**：`AKIAQY...ZAM2`
- **链接**：https://github.com/langwatch/langwatch/blob/main/.gitleaks.toml
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
regexes = ['''AKIAQYLPMN5HHHFPZAM2''', '''A1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q7R8S9T0''']
```

### 3. [LOW] Generic API key assignment

- **仓库**：`zereight/gitlab-mcp`
- **文件**：`test/callback-proxy-redirect-policy.test.ts`（第 32 行）
- **密钥（已脱敏）**：`glpat-...oken`
- **链接**：https://github.com/zereight/gitlab-mcp/blob/main/test/callback-proxy-redirect-policy.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const MOCK_ACCESS_TOKEN = "glpat-mock-redirect-policy-token";
```

### 4. [LOW] Generic API key assignment

- **仓库**：`zereight/gitlab-mcp`
- **文件**：`test/callback-proxy-tests.ts`（第 23 行）
- **密钥（已脱敏）**：`ya29.m...3456`
- **链接**：https://github.com/zereight/gitlab-mcp/blob/main/test/callback-proxy-tests.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const MOCK_ACCESS_TOKEN = "ya29.mock-callback-proxy-token-123456";
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`zereight/gitlab-mcp`
- **文件**：`test/dynamic-routing-tests.ts`（第 16 行）
- **密钥（已脱敏）**：`mcp-st...oken`
- **链接**：https://github.com/zereight/gitlab-mcp/blob/main/test/dynamic-routing-tests.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const MCP_AUTH_TOKEN = 'mcp-static-auth-token';
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`zereight/gitlab-mcp`
- **文件**：`test/oauth-device-flow-tests.ts`（第 19 行）
- **密钥（已脱敏）**：`oauth-...oken`
- **链接**：https://github.com/zereight/gitlab-mcp/blob/main/test/oauth-device-flow-tests.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const ACCESS_TOKEN = "oauth-device-flow-access-token";
```

### 7. [HIGH] Google Gemini / GCP API Key

- **仓库**：`punn-pca/firekeeper-core`
- **文件**：`firebase-applet-config.json`（第 4 行）
- **密钥（已脱敏）**：`AIzaSy...H_Vw`
- **链接**：https://github.com/punn-pca/firekeeper-core/blob/main/firebase-applet-config.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"apiKey": "AIzaSyCjrY8E1uYL95Z-dStlsuBklyYoFlQH_Vw",
```

### 8. [HIGH] Google Gemini / GCP API Key

- **仓库**：`punn-pca/firekeeper-core`
- **文件**：`mobile/src/lib/firebase.ts`（第 32 行）
- **密钥（已脱敏）**：`AIzaSy...H_Vw`
- **链接**：https://github.com/punn-pca/firekeeper-core/blob/main/mobile/src/lib/firebase.ts
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
apiKey: 'AIzaSyCjrY8E1uYL95Z-dStlsuBklyYoFlQH_Vw',
```

### 9. [HIGH] Google Gemini / GCP API Key

- **仓库**：`punn-pca/firekeeper-core`
- **文件**：`mobile/src/lib/firebaseRestAuth.ts`（第 9 行）
- **密钥（已脱敏）**：`AIzaSy...H_Vw`
- **链接**：https://github.com/punn-pca/firekeeper-core/blob/main/mobile/src/lib/firebaseRestAuth.ts
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
const FIREBASE_API_KEY = 'AIzaSyCjrY8E1uYL95Z-dStlsuBklyYoFlQH_Vw';
```

### 10. [MEDIUM] Google OAuth Client Secret

- **仓库**：`starfall-org/generative`
- **文件**：`app/src/main/kotlin/org/starfall/generative/integrations/modelapis/antigravity/AntigravityAdapter.kt`（第 31 行）
- **密钥（已脱敏）**：`GOCSPX...qDAf`
- **链接**：https://github.com/starfall-org/generative/blob/main/app/src/main/kotlin/org/starfall/generative/integrations/modelapis/antigravity/AntigravityAdapter.kt
- **说明**：Google OAuth 客户端密钥。

```text
51121, "/oauth-callback", "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",
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

