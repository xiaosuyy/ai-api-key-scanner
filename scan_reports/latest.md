# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-28 08:20:28 UTC |
| 扫描仓库数 | 50 |
| 扫描文件数 | 9688 |
| 发现数量 | 16 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 5 |
| MEDIUM | 11 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`e2b-dev/E2B`
- **文件**：`packages/cli/tests/user_config_migration.test.ts`（第 80 行）
- **密钥（已脱敏）**：`projec...cret`
- **链接**：https://github.com/e2b-dev/E2B/blob/main/packages/cli/tests/user_config_migration.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
projectApiKey: 'project-api-key-secret',
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`e2b-dev/E2B`
- **文件**：`packages/cli/tests/user_config_permissions.test.ts`（第 38 行）
- **密钥（已脱敏）**：`projec...cret`
- **链接**：https://github.com/e2b-dev/E2B/blob/main/packages/cli/tests/user_config_permissions.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
projectApiKey: 'project-api-key-secret',
```

### 3. [HIGH] GitHub Personal Access Token

- **仓库**：`johan-becker/hushgate`
- **文件**：`README.md`（第 333 行）
- **密钥（已脱敏）**：`ghp_A1...Q7r8`
- **链接**：https://github.com/johan-becker/hushgate/blob/main/README.md
- **说明**：GitHub PAT（Copilot / GitHub Models 等场景常用）。

```text
-d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"Deploy with GITHUB_TOKEN=ghp_A1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6Q7r8 please"}]}'
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`johan-becker/hushgate`
- **文件**：`docs/superpowers/plans/2026-09-09-onboarding-setup.md`（第 1764 行）
- **密钥（已脱敏）**：`sk-fro...inal`
- **链接**：https://github.com/johan-becker/hushgate/blob/main/docs/superpowers/plans/2026-09-09-onboarding-setup.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: 'sk-from-the-terminal',
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`johan-becker/hushgate`
- **文件**：`docs/superpowers/plans/2026-09-09-onboarding-setup.md`（第 1779 行）
- **密钥（已脱敏）**：`sk-inj...page`
- **链接**：https://github.com/johan-becker/hushgate/blob/main/docs/superpowers/plans/2026-09-09-onboarding-setup.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: 'sk-injected-by-a-page',
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`johan-becker/hushgate`
- **文件**：`test/attach.external.test.ts`（第 237 行）
- **密钥（已脱敏）**：`sk-als...leak`
- **链接**：https://github.com/johan-becker/hushgate/blob/main/test/attach.external.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.OPENAI_API_KEY = 'sk-also-must-not-leak';
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`johan-becker/hushgate`
- **文件**：`test/playground.send.test.ts`（第 47 行）
- **密钥（已脱敏）**：`sk-fro...inal`
- **链接**：https://github.com/johan-becker/hushgate/blob/main/test/playground.send.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: 'sk-from-the-terminal',
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`johan-becker/hushgate`
- **文件**：`test/playground.send.test.ts`（第 136 行）
- **密钥（已脱敏）**：`sk-inj...page`
- **链接**：https://github.com/johan-becker/hushgate/blob/main/test/playground.send.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: 'sk-injected-by-a-page',
```

### 9. [HIGH] Anthropic API Key

- **仓库**：`johan-becker/hushgate`
- **文件**：`test/tenants.test.ts`（第 432 行）
- **密钥（已脱敏）**：`sk-ant...AAAA`
- **链接**：https://github.com/johan-becker/hushgate/blob/main/test/tenants.test.ts
- **说明**：Anthropic Claude API 密钥。

```text
content: 'key sk-ant-api03-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
```

### 10. [MEDIUM] Generic API key assignment

- **仓库**：`johan-becker/hushgate`
- **文件**：`test/tenants.test.ts`（第 262 行）
- **密钥（已脱敏）**：`sk-rea...-key`
- **链接**：https://github.com/johan-becker/hushgate/blob/main/test/tenants.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
proxy: { env: { OPENAI_API_KEY: 'sk-real-provider-key' } },
```

### 11. [MEDIUM] Generic API key assignment

- **仓库**：`pymc-labs/daimon`
- **文件**：`apps/harness/tests/test_isolation.py`（第 51 行）
- **密钥（已脱敏）**：`synthe...cret`
- **链接**：https://github.com/pymc-labs/daimon/blob/main/apps/harness/tests/test_isolation.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
AZURE_OPENAI_API_KEY="synthetic-model-secret",
```

### 12. [HIGH] Google Gemini / GCP API Key

- **仓库**：`punn-pca/firekeeper-core`
- **文件**：`firebase-applet-config.json`（第 4 行）
- **密钥（已脱敏）**：`AIzaSy...H_Vw`
- **链接**：https://github.com/punn-pca/firekeeper-core/blob/main/firebase-applet-config.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"apiKey": "AIzaSyCjrY8E1uYL95Z-dStlsuBklyYoFlQH_Vw",
```

### 13. [HIGH] Google Gemini / GCP API Key

- **仓库**：`punn-pca/firekeeper-core`
- **文件**：`mobile/src/lib/firebase.ts`（第 32 行）
- **密钥（已脱敏）**：`AIzaSy...H_Vw`
- **链接**：https://github.com/punn-pca/firekeeper-core/blob/main/mobile/src/lib/firebase.ts
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
apiKey: 'AIzaSyCjrY8E1uYL95Z-dStlsuBklyYoFlQH_Vw',
```

### 14. [HIGH] Google Gemini / GCP API Key

- **仓库**：`punn-pca/firekeeper-core`
- **文件**：`mobile/src/lib/firebaseRestAuth.ts`（第 9 行）
- **密钥（已脱敏）**：`AIzaSy...H_Vw`
- **链接**：https://github.com/punn-pca/firekeeper-core/blob/main/mobile/src/lib/firebaseRestAuth.ts
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
const FIREBASE_API_KEY = 'AIzaSyCjrY8E1uYL95Z-dStlsuBklyYoFlQH_Vw';
```

### 15. [MEDIUM] Generic API key assignment

- **仓库**：`langchain4j/langchain4j`
- **文件**：`docs/docs/integrations/embedding-stores/elasticsearch.md`（第 36 行）
- **密钥（已脱敏）**：`VnVhQ2...U...`
- **链接**：https://github.com/langchain4j/langchain4j/blob/main/docs/docs/integrations/embedding-stores/elasticsearch.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
String apiKey = "VnVhQ2ZHY0JDZGJrU...";
```

### 16. [MEDIUM] Generic API key assignment

- **仓库**：`theolundqvist/pr-cockpit`
- **文件**：`server/quickGenerate.test.ts`（第 66 行）
- **密钥（已脱敏）**：`sk-ant...cret`
- **链接**：https://github.com/theolundqvist/pr-cockpit/blob/main/server/quickGenerate.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
{ ANTHROPIC_API_KEY: "sk-ant-process-secret", HOME: "/elsewhere" },
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

