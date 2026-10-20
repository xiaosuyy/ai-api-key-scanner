# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-20 07:42:42 UTC |
| 扫描仓库数 | 50 |
| 扫描文件数 | 9938 |
| 发现数量 | 2 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 1 |
| LOW | 1 |

## 发现明细

### 1. [HIGH] Anthropic API Key

- **仓库**：`BerriAI/litellm`
- **文件**：`.github/workflows/e2e_record_replay.yml`（第 146 行）
- **密钥（已脱敏）**：`sk-ant...ider`
- **链接**：https://github.com/BerriAI/litellm/blob/main/.github/workflows/e2e_record_replay.yml
- **说明**：Anthropic Claude API 密钥。

```text
ANTHROPIC_API_KEY: sk-ant-replay-must-never-reach-a-provider
```

### 2. [LOW] Generic API key assignment

- **仓库**：`draenger/whisperio`
- **文件**：`desktop/tests/transcribeKeyStoreConsumer.test.ts`（第 114 行）
- **密钥（已脱敏）**：`sk-pla...back`
- **链接**：https://github.com/draenger/whisperio/blob/main/desktop/tests/transcribeKeyStoreConsumer.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
mockLoadSettings.mockReturnValue({ openaiApiKey: 'sk-plaintext-fallback', transcriptionPrompt: '' })
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

