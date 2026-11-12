# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-12 09:46:48 UTC |
| 扫描仓库数 | 48 |
| 扫描文件数 | 8036 |
| 发现数量 | 10 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 2 |
| MEDIUM | 8 |

## 发现明细

### 1. [HIGH] Anthropic API Key

- **仓库**：`toul10/agent-authority-pilot`
- **文件**：`tests/test_settings.py`（第 47 行）
- **密钥（已脱敏）**：`sk-ant...0000`
- **链接**：https://github.com/toul10/agent-authority-pilot/blob/main/tests/test_settings.py
- **说明**：Anthropic Claude API 密钥。

```text
monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-from-the-environment-000000")
```

### 2. [HIGH] Anthropic API Key

- **仓库**：`toul10/agent-authority-pilot`
- **文件**：`tests/test_settings.py`（第 48 行）
- **密钥（已脱敏）**：`sk-ant...0000`
- **链接**：https://github.com/toul10/agent-authority-pilot/blob/main/tests/test_settings.py
- **说明**：Anthropic Claude API 密钥。

```text
assert resolve_key() == ("sk-ant-from-the-environment-000000", "environment")
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`toul10/agent-authority-pilot`
- **文件**：`tests/test_settings.py`（第 109 行）
- **密钥（已脱敏）**：`sk-ant...0000`
- **链接**：https://github.com/toul10/agent-authority-pilot/blob/main/tests/test_settings.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
wrong = anthropic.Anthropic(api_key="sk-ant-wrong-key-000000000000", base_url=api.url, max_retries=0)
```

### 4. [MEDIUM] AWS Access Key ID

- **仓库**：`langwatch/langwatch`
- **文件**：`.github/scripts/__tests__/secrets-scan.test.sh`（第 26 行）
- **密钥（已脱敏）**：`AKIAQY...ZAM2`
- **链接**：https://github.com/langwatch/langwatch/blob/main/.github/scripts/__tests__/secrets-scan.test.sh
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
readonly PLANTED_SECRET='AWS_ACCESS_KEY_ID=AKIAQYLPMN5HHHFPZAM2
```

### 5. [MEDIUM] AWS Access Key ID

- **仓库**：`langwatch/langwatch`
- **文件**：`.gitleaks.toml`（第 122 行）
- **密钥（已脱敏）**：`AKIAQY...ZAM2`
- **链接**：https://github.com/langwatch/langwatch/blob/main/.gitleaks.toml
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
regexes = ['''AKIAQYLPMN5HHHFPZAM2''', '''A1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q7R8S9T0''']
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`orrery-node/orrery`
- **文件**：`node/devtools/e2e.ts`（第 623 行）
- **密钥（已脱敏）**：`sk-ant...d-on`
- **链接**：https://github.com/orrery-node/orrery/blob/main/node/devtools/e2e.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
{ cwd: join(ROOT, 'node'), stdio: ['ignore', 'pipe', 'pipe'], env: { ...process.env, PATH: `${stubDir}:${process.env.PATH}`, ANTHROPIC_API_KEY: 'sk-ant-not-passed-on', ANTHROPIC_AUTH_TOKEN: 'not-passed-on' } });
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`pipodev06/omni-rag`
- **文件**：`apps/api/test/settings.test.ts`（第 150 行）
- **密钥（已脱敏）**：`gsk_se...laro`
- **链接**：https://github.com/pipodev06/omni-rag/blob/main/apps/api/test/settings.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
await s.applySettings({ GROQ_API_KEY: "gsk_secreto-en-claro" }, "root");
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`deepnote/vscode-deepnote`
- **文件**：`src/kernels/execution/cellExecution.federatedAuth.unit.test.ts`（第 194 行）
- **密钥（已脱敏）**：`access...-log`
- **链接**：https://github.com/deepnote/vscode-deepnote/blob/main/src/kernels/execution/cellExecution.federatedAuth.unit.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const ACCESS_TOKEN = 'access-token-secret-do-not-log';
```

### 9. [MEDIUM] Generic API key assignment

- **仓库**：`DrBradStanfield/roadmap`
- **文件**：`app/lib/email-confirmation-unsubscribe.test.ts`（第 4 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/DrBradStanfield/roadmap/blob/main/app/lib/email-confirmation-unsubscribe.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.RESEND_API_KEY = 'synthetic-not-a-real-key';
```

### 10. [MEDIUM] Generic API key assignment

- **仓库**：`DrBradStanfield/roadmap`
- **文件**：`app/lib/email-resend-missing-id.test.ts`（第 45 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/DrBradStanfield/roadmap/blob/main/app/lib/email-resend-missing-id.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.RESEND_API_KEY = 'synthetic-not-a-real-key';
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

