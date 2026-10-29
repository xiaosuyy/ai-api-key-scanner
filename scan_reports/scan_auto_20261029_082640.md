# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-29 08:26:40 UTC |
| 扫描仓库数 | 50 |
| 扫描文件数 | 8185 |
| 发现数量 | 6 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 6 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`PMZPZM0/codex-harness-desktop`
- **文件**：`electron/features/cloud-memory-ipc.ts`（第 151 行）
- **密钥（已脱敏）**：`CLOUD_...OKEN`
- **链接**：https://github.com/PMZPZM0/codex-harness-desktop/blob/main/electron/features/cloud-memory-ipc.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secretKey: "CLOUD_MEMORY_MCP_TOKEN",
```

### 2. [MEDIUM] AWS Access Key ID

- **仓库**：`langwatch/langwatch`
- **文件**：`.github/scripts/__tests__/secrets-scan.test.sh`（第 26 行）
- **密钥（已脱敏）**：`AKIAQY...ZAM2`
- **链接**：https://github.com/langwatch/langwatch/blob/main/.github/scripts/__tests__/secrets-scan.test.sh
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
readonly PLANTED_SECRET='AWS_ACCESS_KEY_ID=AKIAQYLPMN5HHHFPZAM2
```

### 3. [MEDIUM] AWS Access Key ID

- **仓库**：`langwatch/langwatch`
- **文件**：`.gitleaks.toml`（第 122 行）
- **密钥（已脱敏）**：`AKIAQY...ZAM2`
- **链接**：https://github.com/langwatch/langwatch/blob/main/.gitleaks.toml
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
regexes = ['''AKIAQYLPMN5HHHFPZAM2''', '''A1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q7R8S9T0''']
```

### 4. [MEDIUM] Anthropic API Key

- **仓库**：`Baldri/mingly`
- **文件**：`tests/e2e/app.spec.ts`（第 456 行）
- **密钥（已脱敏）**：`sk-ant...here`
- **链接**：https://github.com/Baldri/mingly/blob/main/tests/e2e/app.spec.ts
- **说明**：Anthropic Claude API 密钥。

```text
const testData = 'My email is user@example.com and key sk-ant-api03-very-long-key-here'
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`ostrium-labs/loams`
- **文件**：`apps/desktop-electron/test/agent-loop.test.ts`（第 841 行）
- **密钥（已脱敏）**：`sk-ant...6789`
- **链接**：https://github.com/ostrium-labs/loams/blob/main/apps/desktop-electron/test/agent-loop.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: "sk-ant-other-0123456789",
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`Fooftilly/local-search-mcp`
- **文件**：`config/crawler/searxng-settings.yml`（第 6 行）
- **密钥（已脱敏）**：`__GENE...EY__`
- **链接**：https://github.com/Fooftilly/local-search-mcp/blob/master/config/crawler/searxng-settings.yml
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secret_key: '__GENERATE_PRIVATE_SEARXNG_KEY__'
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

