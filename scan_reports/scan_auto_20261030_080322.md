# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-30 08:03:22 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 4209 |
| 发现数量 | 2 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 2 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`Aswellle/TokenOwl`
- **文件**：`apps/desktop/src-tauri/src/commands/mod.rs`（第 2528 行）
- **密钥（已脱敏）**：`sk-syn...-key`
- **链接**：https://github.com/Aswellle/TokenOwl/blob/main/apps/desktop/src-tauri/src/commands/mod.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
api_key: "sk-synthetic-format-key".to_owned(),
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`ihabkhaled/ClawAI`
- **文件**：`apps/claw-agent-service/src/common/testing/agent-test-env.ts`（第 13 行）
- **密钥（已脱敏）**：`inter-...n-12`
- **链接**：https://github.com/ihabkhaled/ClawAI/blob/main/apps/claw-agent-service/src/common/testing/agent-test-env.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
INTER_SERVICE_AUTH_TOKEN: 'inter-service-token-inter-service-token-12',
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

