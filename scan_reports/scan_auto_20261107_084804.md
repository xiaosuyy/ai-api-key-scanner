# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-07 08:48:04 UTC |
| 扫描仓库数 | 46 |
| 扫描文件数 | 8567 |
| 发现数量 | 4 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 4 |

## 发现明细

### 1. [MEDIUM] AWS Access Key ID

- **仓库**：`vostride/agent-qa`
- **文件**：`packages/agent/src/config-mutation/__tests__/config-ops.test.ts`（第 1002 行）
- **密钥（已脱敏）**：`AKIAQW...DFGH`
- **链接**：https://github.com/vostride/agent-qa/blob/main/packages/agent/src/config-mutation/__tests__/config-ops.test.ts
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
pluginPackage: 'AKIAQWERTYUIOPASDFGH',
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`cheaper-inference/OmniRoute`
- **文件**：`@omniroute/opencode-plugin-v2/tests/warm-snapshot-identity.test.ts`（第 47 行）
- **密钥（已脱敏）**：`key-wr...nfig`
- **链接**：https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.54/@omniroute/opencode-plugin-v2/tests/warm-snapshot-identity.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
options: { baseURL, providerId: "warmid", apiKey: "key-written-in-the-config" },
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`starfall-org/generative`
- **文件**：`app/src/androidTest/java/org/starfall/generative/RoomOAuthDeviceTest.kt`（第 42 行）
- **密钥（已脱敏）**：`secret...tore`
- **链接**：https://github.com/starfall-org/generative/blob/main/app/src/androidTest/java/org/starfall/generative/RoomOAuthDeviceTest.kt
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken = "secret-access-data-store",
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`HaitoDann/atom`
- **文件**：`searxng/settings.yml`（第 8 行）
- **密钥（已脱敏）**：`rempla...CRET`
- **链接**：https://github.com/HaitoDann/atom/blob/claude/new-session-q4ozge/searxng/settings.yml
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secret_key: "remplace-par-SEARXNG_SECRET"   # écrasé par la variable SEARXNG_SECRET
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

