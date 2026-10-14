# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-14 07:05:55 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 3765 |
| 发现数量 | 5 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 5 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`ai-zen/agents`
- **文件**：`packages/core/src/integration.test.ts`（第 456 行）
- **密钥（已脱敏）**：`sk-inv...2345`
- **链接**：https://github.com/ai-zen/agents/blob/main/packages/core/src/integration.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: "sk-invalid-key-12345",
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`atomantic/PortOS`
- **文件**：`autofixer/sandbox.test.js`（第 78 行）
- **密钥（已脱敏）**：`sk-ant...e123`
- **链接**：https://github.com/atomantic/PortOS/blob/main/autofixer/sandbox.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
ANTHROPIC_API_KEY: 'sk-ant-childkeyvalue123',
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`atomantic/PortOS`
- **文件**：`autofixer/sandbox.test.js`（第 79 行）
- **密钥（已脱敏）**：`oauth-...-123`
- **链接**：https://github.com/atomantic/PortOS/blob/main/autofixer/sandbox.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
CLAUDE_CODE_OAUTH_TOKEN: 'oauth-secret-value-123',
```

### 4. [MEDIUM] AWS Access Key ID

- **仓库**：`atomantic/PortOS`
- **文件**：`autofixer/sandbox.test.js`（第 258 行）
- **密钥（已脱敏）**：`AKIAOL...0000`
- **链接**：https://github.com/atomantic/PortOS/blob/main/autofixer/sandbox.test.js
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
-const old = "AKIAOLDKEY0000000000"
```

### 5. [MEDIUM] AWS Access Key ID

- **仓库**：`atomantic/PortOS`
- **文件**：`autofixer/sandbox.test.js`（第 259 行）
- **密钥（已脱敏）**：`AKIACO...0000`
- **链接**：https://github.com/atomantic/PortOS/blob/main/autofixer/sandbox.test.js
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
context AKIACONTEXT000000000
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

