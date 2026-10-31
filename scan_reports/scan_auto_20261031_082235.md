# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-31 08:22:35 UTC |
| 扫描仓库数 | 50 |
| 扫描文件数 | 9033 |
| 发现数量 | 8 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 8 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`ashlrai/ashlr-stack`
- **文件**：`packages/core/src/__tests__/credential-staging.test.ts`（第 567 行）
- **密钥（已脱敏）**：`synthe...oken`
- **链接**：https://github.com/ashlrai/ashlr-stack/blob/main/packages/core/src/__tests__/credential-staging.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: "synthetic-oauth-token",
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`ashlrai/ashlr-stack`
- **文件**：`packages/core/src/__tests__/supabase-provider.test.ts`（第 18 行）
- **密钥（已脱敏）**：`sbp_ca...oken`
- **链接**：https://github.com/ashlrai/ashlr-stack/blob/main/packages/core/src/__tests__/supabase-provider.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
{ STACK_SUPABASE_ACCESS_TOKEN: "sbp_cached_valid_token" },
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`ashlrai/ashlr-stack`
- **文件**：`packages/core/src/providers/aws.ts`（第 24 行）
- **密钥（已脱敏）**：`AWS_SE..._KEY`
- **链接**：https://github.com/ashlrai/ashlr-stack/blob/main/packages/core/src/providers/aws.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const SECRET_SECRET_KEY = "AWS_SECRET_ACCESS_KEY";
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`mojoaar/mimir`
- **文件**：`docs/superpowers/plans/2026-10-25-mimir-v0.2.0-learning.md`（第 279 行）
- **密钥（已脱敏）**：`sk-liv...alue`
- **链接**：https://github.com/mojoaar/mimir/blob/main/docs/superpowers/plans/2026-10-25-mimir-v0.2.0-learning.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
label: 'work', model: 'deepseek-chat', apiKey: 'sk-live-secret-value',
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`mojoaar/mimir`
- **文件**：`lib/backup/artifacts.int.test.ts`（第 22 行）
- **密钥（已脱敏）**：`sk-liv...-key`
- **链接**：https://github.com/mojoaar/mimir/blob/main/lib/backup/artifacts.int.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: 'sk-live-this-is-the-real-key',
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`nranjan2code/vakyartha`
- **文件**：`scripts/desktop-probe.js`（第 30 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/nranjan2code/vakyartha/blob/main/scripts/desktop-probe.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const secretUpdate=await request('/api/settings','PUT',{values:{OPENAI_API_KEY:'synthetic-refused-worker-key'}});
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`edgar4/yada`
- **文件**：`tests/starter-integration.test.ts`（第 45 行）
- **密钥（已脱敏）**：`never-...ible`
- **链接**：https://github.com/edgar4/yada/blob/main/tests/starter-integration.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
YADA_LLM_API_KEY: "never-browser-visible",
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`edgar4/yada`
- **文件**：`tests/starter-provider.test.ts`（第 59 行）
- **密钥（已脱敏）**：`server...cret`
- **链接**：https://github.com/edgar4/yada/blob/main/tests/starter-provider.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
YADA_LLM_API_KEY: "server-only-provider-secret",
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

