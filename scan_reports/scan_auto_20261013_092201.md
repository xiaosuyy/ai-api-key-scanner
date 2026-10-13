# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-13 09:22:01 UTC |
| 扫描仓库数 | 48 |
| 扫描文件数 | 8408 |
| 发现数量 | 9 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 9 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`caura-ai/caura`
- **文件**：`clients/python/tests/test_interviewer_scrub.py`（第 21 行）
- **密钥（已脱敏）**：`hijklm...1234`
- **链接**：https://github.com/caura-ai/caura/blob/main/clients/python/tests/test_interviewer_scrub.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
"api_key = 'hijklmnopqrstuvwx1234'",
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`mohamedhabila/Kavi`
- **文件**：`__tests__/acceptance/e2eAgentForegroundScenarioSelectedMode.test.ts`（第 43 行）
- **密钥（已脱敏）**：`scenar...-key`
- **链接**：https://github.com/mohamedhabila/Kavi/blob/main/__tests__/acceptance/e2eAgentForegroundScenarioSelectedMode.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: 'scenario-provider-key',
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`mohamedhabila/Kavi`
- **文件**：`__tests__/acceptance/e2ePairedConditions.test.ts`（第 182 行）
- **密钥（已脱敏）**：`PRIVAT...-KEY`
- **链接**：https://github.com/mohamedhabila/Kavi/blob/main/__tests__/acceptance/e2ePairedConditions.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
provider: { ...invariant.provider, apiKey: 'PRIVATE-SMUGGLED-KEY' },
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`nuoxingchai-spec/aidd-blue-toxnet`
- **文件**：`test/test_explanation_report.py`（第 100 行）
- **密钥（已脱敏）**：`fixtur...cret`
- **链接**：https://github.com/nuoxingchai-spec/aidd-blue-toxnet/blob/main/test/test_explanation_report.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
config=ModelConfig(api_url=f'http://127.0.0.1:{server.server_port}',api_format='openai',api_key='fixture-key-not-secret',model_name='test-only',model_version='unit-v1')
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`nonahisa/novel-ai-assistant`
- **文件**：`src/ai/claudeProvider.ts`（第 32 行）
- **密钥（已脱敏）**：`novela...iKey`
- **链接**：https://github.com/nonahisa/novel-ai-assistant/blob/main/src/ai/claudeProvider.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const SECRET_KEY = "novelai.claude.apiKey";
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`nonahisa/novel-ai-assistant`
- **文件**：`src/ai/geminiProvider.ts`（第 23 行）
- **密钥（已脱敏）**：`novela...iKey`
- **链接**：https://github.com/nonahisa/novel-ai-assistant/blob/main/src/ai/geminiProvider.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const SECRET_KEY = "novelai.gemini.apiKey";
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`nonahisa/novel-ai-assistant`
- **文件**：`src/ai/openaiProvider.ts`（第 27 行）
- **密钥（已脱敏）**：`novela...iKey`
- **链接**：https://github.com/nonahisa/novel-ai-assistant/blob/main/src/ai/openaiProvider.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const SECRET_KEY = "novelai.openai.apiKey";
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`nonahisa/novel-ai-assistant`
- **文件**：`src/ai/sakuraProvider.ts`（第 46 行）
- **密钥（已脱敏）**：`novela...iKey`
- **链接**：https://github.com/nonahisa/novel-ai-assistant/blob/main/src/ai/sakuraProvider.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const SECRET_KEY = "novelai.sakura.apiKey";
```

### 9. [MEDIUM] Generic API key assignment

- **仓库**：`bek-sam/invai-backend`
- **文件**：`src/ai/openai-provider.test.ts`（第 498 行）
- **密钥（已脱敏）**：`sk-fro...ored`
- **链接**：https://github.com/bek-sam/invai-backend/blob/main/src/ai/openai-provider.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.OPENAI_API_KEY = "sk-from-dotenv-should-be-ignored";
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

