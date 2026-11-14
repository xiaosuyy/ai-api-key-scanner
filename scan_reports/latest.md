# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-14 08:58:38 UTC |
| 扫描仓库数 | 48 |
| 扫描文件数 | 8377 |
| 发现数量 | 13 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 6 |
| MEDIUM | 5 |
| LOW | 2 |

## 发现明细

### 1. [HIGH] Anthropic API Key

- **仓库**：`ShenSeanChen/waku-agent`
- **文件**：`evals/deterministic/hosted/test_install_sh.py`（第 790 行）
- **密钥（已脱敏）**：`sk-ant...Z-AA`
- **链接**：https://github.com/ShenSeanChen/waku-agent/blob/main/evals/deterministic/hosted/test_install_sh.py
- **说明**：Anthropic Claude API 密钥。

```text
key = _key_file(tmp_path, "sk-ant-api03-AbC_dEf-123456789_XyZ-AA\n")
```

### 2. [HIGH] Anthropic API Key

- **仓库**：`ShenSeanChen/waku-agent`
- **文件**：`evals/deterministic/test_turn_receipt.py`（第 146 行）
- **密钥（已脱敏）**：`sk-ant...AUTH`
- **链接**：https://github.com/ShenSeanChen/waku-agent/blob/main/evals/deterministic/test_turn_receipt.py
- **说明**：Anthropic Claude API 密钥。

```text
SECRETS = ("Bearer sk-ant-api03-AUTHAUTHAUTHAUTHAUTHAUTHAUTHAUTH",
```

### 3. [HIGH] Anthropic API Key

- **仓库**：`ShenSeanChen/waku-agent`
- **文件**：`evals/deterministic/test_turn_receipt.py`（第 147 行）
- **密钥（已脱敏）**：`sk-ant...IKEY`
- **链接**：https://github.com/ShenSeanChen/waku-agent/blob/main/evals/deterministic/test_turn_receipt.py
- **说明**：Anthropic Claude API 密钥。

```text
"sk-ant-api03-APIKEYAPIKEYAPIKEYAPIKEYAPIKEY",
```

### 4. [HIGH] Anthropic API Key

- **仓库**：`ShenSeanChen/waku-agent`
- **文件**：`evals/deterministic/test_turn_receipt.py`（第 148 行）
- **密钥（已脱敏）**：`sk-ant...ECHO`
- **链接**：https://github.com/ShenSeanChen/waku-agent/blob/main/evals/deterministic/test_turn_receipt.py
- **说明**：Anthropic Claude API 密钥。

```text
"sk-ant-api03-ECHOECHOECHOECHOECHOECHOECHOECHO")
```

### 5. [HIGH] Anthropic API Key

- **仓库**：`ShenSeanChen/waku-agent`
- **文件**：`evals/hosted_docker/spawnerlib.py`（第 45 行）
- **密钥（已脱敏）**：`sk-ant...ship`
- **链接**：https://github.com/ShenSeanChen/waku-agent/blob/main/evals/hosted_docker/spawnerlib.py
- **说明**：Anthropic Claude API 密钥。

```text
PLANTED_PLATFORM_KEY = "sk-ant-PLANTED-PLATFORM-KEY-do-not-ship"
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`KushalP1/context-doctor`
- **文件**：`src/test/ab.test.ts`（第 366 行）
- **密钥（已脱敏）**：`sk-ant...leak`
- **链接**：https://github.com/KushalP1/context-doctor/blob/main/src/test/ab.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.ANTHROPIC_API_KEY = "sk-ant-should-not-leak";
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`KushalP1/context-doctor`
- **文件**：`src/test/canary.test.ts`（第 40 行）
- **密钥（已脱敏）**：`sk-ant...king`
- **链接**：https://github.com/KushalP1/context-doctor/blob/main/src/test/canary.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
bad({ ANTHROPIC_API_KEY: "sk-ant-api03-real-looking" }, /ANTHROPIC_API_KEY is set/);
```

### 8. [LOW] Generic API key assignment

- **仓库**：`KushalP1/context-doctor`
- **文件**：`src/test/canary.test.ts`（第 242 行）
- **密钥（已脱敏）**：`sk-ant...ller`
- **链接**：https://github.com/KushalP1/context-doctor/blob/main/src/test/canary.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const r = run(["--claude", fake], { ...process.env, ANTHROPIC_API_KEY: "sk-ant-api03-from-the-caller", CLAUDE_CODE_OAUTH_TOKEN: "sk-ant-oat01-from-the-caller", ANTHROPIC_BASE_URL: "https://api.anthropic.com", GITHUB_ACTIONS: "" });
```

### 9. [LOW] Generic API key assignment

- **仓库**：`KushalP1/context-doctor`
- **文件**：`src/test/canary.test.ts`（第 242 行）
- **密钥（已脱敏）**：`sk-ant...ller`
- **链接**：https://github.com/KushalP1/context-doctor/blob/main/src/test/canary.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const r = run(["--claude", fake], { ...process.env, ANTHROPIC_API_KEY: "sk-ant-api03-from-the-caller", CLAUDE_CODE_OAUTH_TOKEN: "sk-ant-oat01-from-the-caller", ANTHROPIC_BASE_URL: "https://api.anthropic.com", GITHUB_ACTIONS: "" });
```

### 10. [HIGH] OpenAI API Key

- **仓库**：`atliliw/langchainrust`
- **文件**：`crates/lc-agents/src/react/agent.rs`（第 335 行）
- **密钥（已脱敏）**：`sk-6eb...43e7`
- **链接**：https://github.com/atliliw/langchainrust/blob/main/crates/lc-agents/src/react/agent.rs
- **说明**：OpenAI 风格 sk- 密钥（也覆盖 DeepSeek、Moonshot 等同类前缀）。

```text
api_key: "sk-6eb65fcf5d17491ca10b984efe1f43e7".into(),
```

### 11. [MEDIUM] Generic API key assignment

- **仓库**：`A220man/atlas-lens-ryan-vo`
- **文件**：`backend/tests/test_auth_and_security.py`（第 46 行）
- **密钥（已脱敏）**：`some-p...hars`
- **链接**：https://github.com/A220man/atlas-lens-ryan-vo/blob/main/backend/tests/test_auth_and_security.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secret_key="some-production-secret-key-at-least-32-chars",
```

### 12. [MEDIUM] Generic API key assignment

- **仓库**：`krishanraja/AEO-Engine`
- **文件**：`tests/claudeCode.test.ts`（第 29 行）
- **密钥（已脱敏）**：`synthe...oken`
- **链接**：https://github.com/krishanraja/AEO-Engine/blob/main/tests/claudeCode.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const TOKEN_ENV = { PATH: '/usr/bin:/bin', CLAUDE_CODE_OAUTH_TOKEN: 'synthetic-oauth-token' }
```

### 13. [MEDIUM] Generic API key assignment

- **仓库**：`KhatKit/Android`
- **文件**：`app/src/androidTest/java/heizige/kk/khatkit/app/feature/chat/C1GroupExportDeviceEvidenceTest.kt`（第 111 行）
- **密钥（已脱敏）**：`sk-c1c...feed`
- **链接**：https://github.com/KhatKit/Android/blob/main/app/src/androidTest/java/heizige/kk/khatkit/app/feature/chat/C1GroupExportDeviceEvidenceTest.kt
- **说明**：赋值给 API key 变量的疑似密钥。

```text
private val canaryApiKey = "sk-c1canary-7f3d9a2b5c8e4f01feed"
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

