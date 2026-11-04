# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-04 08:32:55 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 4683 |
| 发现数量 | 6 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 1 |
| MEDIUM | 5 |

## 发现明细

### 1. [HIGH] GitHub Personal Access Token

- **仓库**：`jacknegri89/LogLens`
- **文件**：`client/src/lib/anonymize.test.ts`（第 132 行）
- **密钥（已脱敏）**：`ghp_16...8B4a`
- **链接**：https://github.com/jacknegri89/LogLens/blob/main/client/src/lib/anonymize.test.ts
- **说明**：GitHub PAT（Copilot / GitHub Models 等场景常用）。

```text
['a GitHub personal token', 'clone with ghp_16C7e42F292c6912E7710c838347Ae178B4a'],
```

### 2. [MEDIUM] AWS Access Key ID

- **仓库**：`jacknegri89/LogLens`
- **文件**：`client/src/lib/anonymize.test.ts`（第 154 行）
- **密钥（已脱敏）**：`AKIAJ3...QRST`
- **链接**：https://github.com/jacknegri89/LogLens/blob/main/client/src/lib/anonymize.test.ts
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
expect(anonymized(`${key} then ${key} and AKIAJ3XAMPLEKEY7QRST`)).toBe(
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`hivecommons/hive`
- **文件**：`bin/contributor-agent.test.sh`（第 468 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/hivecommons/hive/blob/v5/bin/contributor-agent.test.sh
- **说明**：赋值给 API key 变量的疑似密钥。

```text
OPENAI_API_KEY="synthetic-invalid-pi-key" \
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`hivecommons/hive`
- **文件**：`bin/contributor-relay.test.js`（第 1753 行）
- **密钥（已脱敏）**：`unrela...-key`
- **链接**：https://github.com/hivecommons/hive/blob/v5/bin/contributor-relay.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
fs.writeFileSync(path.join(agentDir, 'models.json'), JSON.stringify({ providers: { openai: { apiKey: 'selected-custom-key' }, anthropic: { apiKey: 'unrelated-custom-key' } }, defaults: {} }));
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`hivecommons/hive`
- **文件**：`bin/contributor-relay.test.js`（第 2329 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/hivecommons/hive/blob/v5/bin/contributor-relay.test.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const relay = loadRelay({ backend: 'pi', backendPerm: '', mode: 'headless', model: 'openai/gpt-5', cliVersion: 'pi 0.73.1', env: { OPENAI_API_KEY: 'synthetic-invalid-key' } });
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`baily90/ai-agent-learning`
- **文件**：`06-技术篇/30-LiteLLM与模型网关.md`（第 134 行）
- **密钥（已脱敏）**：`sk-lit...-key`
- **链接**：https://github.com/baily90/ai-agent-learning/blob/main/06-技术篇/30-LiteLLM与模型网关.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: 'sk-litellm-master-key',        // 网关的 key，不是模型厂商的 key
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

