# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-20 07:05:16 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 4129 |
| 发现数量 | 3 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 3 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`reefbarman/agentlink`
- **文件**：`apps/server/src/publisher.test.ts`（第 141 行）
- **密钥（已脱敏）**：`ghu_re...6789`
- **链接**：https://github.com/reefbarman/agentlink/blob/main/apps/server/src/publisher.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: "ghu_refreshedtoken0123456789",
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`reefbarman/agentlink`
- **文件**：`apps/server/src/publisher.test.ts`（第 522 行）
- **密钥（已脱敏）**：`ghu_re...6789`
- **链接**：https://github.com/reefbarman/agentlink/blob/main/apps/server/src/publisher.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: "ghu_refreshedtoken0123456789",
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`computer-mcp/computer-mcp`
- **文件**：`Sources/ComputerMCP/CloudflareTunnel.swift`（第 168 行）
- **密钥（已脱敏）**：`genera...oken`
- **链接**：https://github.com/computer-mcp/computer-mcp/blob/master/Sources/ComputerMCP/CloudflareTunnel.swift
- **说明**：赋值给 API key 变量的疑似密钥。

```text
case generatedAccessToken = "generated_access_token"
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

