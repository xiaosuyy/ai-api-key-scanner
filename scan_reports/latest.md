# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-15 07:19:14 UTC |
| 扫描仓库数 | 48 |
| 扫描文件数 | 7342 |
| 发现数量 | 6 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 2 |
| MEDIUM | 4 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`SmokeyS30/orbit-buddy`
- **文件**：`test/tools.test.js`（第 242 行）
- **密钥（已脱敏）**：`standa...back`
- **链接**：https://github.com/SmokeyS30/orbit-buddy/blob/main/test/tools.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
OPENAI_API_KEY: 'standard-key-kept-for-rollback',
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`i098/sanctum`
- **文件**：`server/tests/spoken-work.test.ts`（第 21 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/i098/sanctum/blob/main/server/tests/spoken-work.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
CEREBRAS_API_KEY: 'synthetic-cerebras-key',
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`HelpCode-ai/anythingmcp`
- **文件**：`packages/backend/src/adapters/de/weclapp.live.spec.ts`（第 101 行）
- **密钥（已脱敏）**：`sentin...2345`
- **链接**：https://github.com/HelpCode-ai/anythingmcp/blob/main/packages/backend/src/adapters/de/weclapp.live.spec.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
authConfig: { headerName: 'AuthenticationToken', apiKey: 'sentinel-token-12345' },
```

### 4. [HIGH] Google Gemini / GCP API Key

- **仓库**：`lucasdilley07-png/Morphe`
- **文件**：`docs/coach.html`（第 133 行）
- **密钥（已脱敏）**：`AIzaSy...IkhQ`
- **链接**：https://github.com/lucasdilley07-png/Morphe/blob/main/docs/coach.html
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
var FIREBASE_WEB_API_KEY = "AIzaSyAcP1XXWajPFhC13b8UfiRh1XhZdrlIkhQ";
```

### 5. [HIGH] Google Gemini / GCP API Key

- **仓库**：`lucasdilley07-png/Morphe`
- **文件**：`docs/index.html`（第 561 行）
- **密钥（已脱敏）**：`AIzaSy...IkhQ`
- **链接**：https://github.com/lucasdilley07-png/Morphe/blob/main/docs/index.html
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
var KEY = "AIzaSyAcP1XXWajPFhC13b8UfiRh1XhZdrlIkhQ", PROJECT = "morphe-3c5c2";
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`dmascord/tusker-gateway`
- **文件**：`tests/test_passthrough_providers.py`（第 251 行）
- **密钥（已脱敏）**：`sk-exp...ride`
- **链接**：https://github.com/dmascord/tusker-gateway/blob/main/tests/test_passthrough_providers.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
stream=False, api_key="sk-explicit-override",
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

