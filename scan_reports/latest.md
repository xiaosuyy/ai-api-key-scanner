# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-21 07:24:17 UTC |
| 扫描仓库数 | 49 |
| 扫描文件数 | 9466 |
| 发现数量 | 9 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 8 |
| LOW | 1 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`vayungodara/cliproxy-rs`
- **文件**：`bench/run.sh`（第 72 行）
- **密钥（已脱敏）**：`sk-ben...real`
- **链接**：https://github.com/vayungodara/cliproxy-rs/blob/master/bench/run.sh
- **说明**：赋值给 API key 变量的疑似密钥。

```text
- api-key: "sk-bench-upstream-not-real"
```

### 2. [MEDIUM] Google OAuth Client Secret

- **仓库**：`vayungodara/cliproxy-rs`
- **文件**：`crates/cpa-exec/src/antigravity_auth.rs`（第 30 行）
- **密钥（已脱敏）**：`GOCSPX...qDAf`
- **链接**：https://github.com/vayungodara/cliproxy-rs/blob/master/crates/cpa-exec/src/antigravity_auth.rs
- **说明**：Google OAuth 客户端密钥。

```text
pub const CLIENT_SECRET: &str = "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";
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`diegosouzapw/OmniRoute`
- **文件**：`@omniroute/opencode-plugin-v2/tests/warm-snapshot-identity.test.ts`（第 47 行）
- **密钥（已脱敏）**：`key-wr...nfig`
- **链接**：https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.53/@omniroute/opencode-plugin-v2/tests/warm-snapshot-identity.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
options: { baseURL, providerId: "warmid", apiKey: "key-written-in-the-config" },
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`s3ntin3l8/runway-ai-usage-tracker`
- **文件**：`app/core/config.py`（第 55 行）
- **密钥（已脱敏）**：`sideca...cret`
- **链接**：https://github.com/s3ntin3l8/runway-ai-usage-tracker/blob/main/app/core/config.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
DEFAULT_INGEST_API_KEY = "sidecar-default-secret"
```

### 5. [MEDIUM] Google OAuth Client Secret

- **仓库**：`s3ntin3l8/runway-ai-usage-tracker`
- **文件**：`app/services/token_refresher.py`（第 42 行）
- **密钥（已脱敏）**：`GOCSPX...Fsxl`
- **链接**：https://github.com/s3ntin3l8/runway-ai-usage-tracker/blob/main/app/services/token_refresher.py
- **说明**：Google OAuth 客户端密钥。

```text
_GEMINI_CLI_CLIENT_SECRET = "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"
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`Qquench/Quorch`
- **文件**：`plugins/quench-dev-tasks/server/tests/test_handoff_protocol.py`（第 256 行）
- **密钥（已脱敏）**：`sk-sup...leak`
- **链接**：https://github.com/Qquench/Quorch/blob/main/plugins/quench-dev-tasks/server/tests/test_handoff_protocol.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secret_key = "sk-super-secret-key-that-must-never-leak"
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`trvny/trvny`
- **文件**：`gh-apps/kanarek-companion/test/engram-actions.test.ts`（第 73 行）
- **密钥（已脱敏）**：`eng_li...cret`
- **链接**：https://github.com/trvny/trvny/blob/main/gh-apps/kanarek-companion/test/engram-actions.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
{ ENGRAM_API_KEY: 'eng_live_super_secret' },
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`trvny/trvny`
- **文件**：`gh-apps/kanarek-companion/test/engram-actions.test.ts`（第 98 行）
- **密钥（已脱敏）**：`eng_li...cret`
- **链接**：https://github.com/trvny/trvny/blob/main/gh-apps/kanarek-companion/test/engram-actions.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const env = { ENGRAM_API_KEY: 'eng_live_super_secret' } satisfies EngramActionEnv;
```

### 9. [LOW] Generic API key assignment

- **仓库**：`dtssv/CodePilot`
- **文件**：`packages/core/test/mcpOAuthFlow.test.ts`（第 84 行）
- **密钥（已脱敏）**：`access...mock`
- **链接**：https://github.com/dtssv/CodePilot/blob/main/packages/core/test/mcpOAuthFlow.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: "access-token-from-mock",
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

