# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-29 07:56:46 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 2868 |
| 发现数量 | 4 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 4 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`cheaper-inference/OmniRoute`
- **文件**：`@omniroute/opencode-plugin-v2/tests/warm-snapshot-identity.test.ts`（第 47 行）
- **密钥（已脱敏）**：`key-wr...nfig`
- **链接**：https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.53/@omniroute/opencode-plugin-v2/tests/warm-snapshot-identity.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
options: { baseURL, providerId: "warmid", apiKey: "key-written-in-the-config" },
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`aurorax-neo/chatgptx`
- **文件**：`apps/chatgptx-manager/src/pure-api-auth.test.ts`（第 51 行）
- **密钥（已脱敏）**：`fixtur...-key`
- **链接**：https://github.com/aurorax-neo/chatgptx/blob/main/apps/chatgptx-manager/src/pure-api-auth.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: "fixture-provider-key", officialMixApiKey: false, modelRoutes: [],
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`aurorax-neo/chatgptx`
- **文件**：`apps/chatgptx-manager/src/pure-api-auth.test.ts`（第 53 行）
- **密钥（已脱敏）**：`fixtur...-key`
- **链接**：https://github.com/aurorax-neo/chatgptx/blob/main/apps/chatgptx-manager/src/pure-api-auth.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
authContents: JSON.stringify({ OPENAI_API_KEY: "fixture-provider-key", vendor: "stored" }),
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`aurorax-neo/chatgptx`
- **文件**：`assets/inject/floating-panel/runtime/state.js`（第 25 行）
- **密钥（已脱敏）**：`__code...anel`
- **链接**：https://github.com/aurorax-neo/chatgptx/blob/main/assets/inject/floating-panel/runtime/state.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const API_KEY = "__codexStepwisePanel";
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

