# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-24 07:07:13 UTC |
| 扫描仓库数 | 45 |
| 扫描文件数 | 7686 |
| 发现数量 | 6 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 5 |
| MEDIUM | 1 |

## 发现明细

### 1. [HIGH] Anthropic API Key

- **仓库**：`Sannrox/sekai-chisei`
- **文件**：`crates/chisei-gateway/src/gateway_tests.rs`（第 5068 行）
- **密钥（已脱敏）**：`sk-ant...cret`
- **链接**：https://github.com/Sannrox/sekai-chisei/blob/main/crates/chisei-gateway/src/gateway_tests.rs
- **说明**：Anthropic Claude API 密钥。

```text
.bearer_auth("sk-ant-oat-client-subscription-secret")
```

### 2. [HIGH] Anthropic API Key

- **仓库**：`Sannrox/sekai-chisei`
- **文件**：`crates/chisei-gateway/src/gateway_tests.rs`（第 5090 行）
- **密钥（已脱敏）**：`sk-ant...cret`
- **链接**：https://github.com/Sannrox/sekai-chisei/blob/main/crates/chisei-gateway/src/gateway_tests.rs
- **说明**：Anthropic Claude API 密钥。

```text
Some("Bearer sk-ant-oat-client-subscription-secret")
```

### 3. [HIGH] Anthropic API Key

- **仓库**：`headroomlabs-ai/headroom`
- **文件**：`.gitguardian.yaml`（第 34 行）
- **密钥（已脱敏）**：`sk-ant...ture`
- **链接**：https://github.com/headroomlabs-ai/headroom/blob/main/.gitguardian.yaml
- **说明**：Anthropic Claude API 密钥。

```text
match: "sk-ant-api03-payg-bearer-fixture"
```

### 4. [HIGH] Anthropic API Key

- **仓库**：`headroomlabs-ai/headroom`
- **文件**：`crates/headroom-proxy/src/cache_stabilization/drift_detector.rs`（第 761 行）
- **密钥（已脱敏）**：`sk-ant...g-me`
- **链接**：https://github.com/headroomlabs-ai/headroom/blob/main/crates/headroom-proxy/src/cache_stabilization/drift_detector.rs
- **说明**：Anthropic Claude API 密钥。

```text
"Bearer sk-ant-very-secret-token-do-not-log-me"
```

### 5. [HIGH] Anthropic API Key

- **仓库**：`jshiv/cronicle`
- **文件**：`internal/cronicle/state/pg_secrets_test.go`（第 33 行）
- **密钥（已脱敏）**：`sk-ant...lock`
- **链接**：https://github.com/jshiv/cronicle/blob/main/internal/cronicle/state/pg_secrets_test.go
- **说明**：Anthropic Claude API 密钥。

```text
const secret = "sk-ant-xchacha-roundtrip-9f3c-AND-some-padding-to-exceed-a-block"
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`richardichogan/knowledge-base`
- **文件**：`knowledge-hub-backend/scripts/mural.test.ts`（第 49 行）
- **密钥（已脱敏）**：`fixtur...oken`
- **链接**：https://github.com/richardichogan/knowledge-base/blob/main/knowledge-hub-backend/scripts/mural.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: 'fixture-access-token', refresh_token: 'fixture-refresh-token', expires_in: seconds,
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

