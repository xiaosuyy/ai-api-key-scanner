# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-13 09:36:43 UTC |
| 扫描仓库数 | 47 |
| 扫描文件数 | 7460 |
| 发现数量 | 20 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 15 |
| MEDIUM | 5 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`openai/codex-security`
- **文件**：`github-action/tests/main.test.ts`（第 338 行）
- **密钥（已脱敏）**：`synthe...uter`
- **链接**：https://github.com/openai/codex-security/blob/main/github-action/tests/main.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
Object.assign(process.env, {OPENROUTER_API_KEY:'synthetic-openrouter', FIREWORKS_API_KEY:'synthetic-fireworks',
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`openai/codex-security`
- **文件**：`github-action/tests/runtime.test.ts`（第 384 行）
- **密钥（已脱敏）**：`synthe...uter`
- **链接**：https://github.com/openai/codex-security/blob/main/github-action/tests/runtime.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
OPENROUTER_API_KEY:'synthetic-openrouter', FIREWORKS_API_KEY:'synthetic-fireworks',
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`openai/codex-security`
- **文件**：`github-action/tests/runtime.test.ts`（第 388 行）
- **密钥（已脱敏）**：`change...ture`
- **链接**：https://github.com/openai/codex-security/blob/main/github-action/tests/runtime.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
source.OPENROUTER_API_KEY = source.FIREWORKS_API_KEY = 'changed-after-capture';
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`MHassan-AiExpert/AI-SDR-Autonomous-Sales-Platform`
- **文件**：`web/tests/connection-tests.test.ts`（第 13 行）
- **密钥（已脱敏）**：`SECRET...0000`
- **链接**：https://github.com/MHassan-AiExpert/AI-SDR-Autonomous-Sales-Platform/blob/main/web/tests/connection-tests.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
twilio: { account_sid: 'AC' + '1'.repeat(32), auth_token: 'SECRETtwilioTOKEN000000000000000' },
```

### 5. [MEDIUM] Google OAuth Client Secret

- **仓库**：`lidge-jun/opencodex`
- **文件**：`devlog/_fin/140_remaining-provider-ports/21_phase2_antigravity-oauth-cca.md`（第 32 行）
- **密钥（已脱敏）**：`GOCSPX...qDAf`
- **链接**：https://github.com/lidge-jun/opencodex/blob/dev/devlog/_fin/140_remaining-provider-ports/21_phase2_antigravity-oauth-cca.md
- **说明**：Google OAuth 客户端密钥。

```text
ClientSecret     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
```

### 6. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 358 行）
- **密钥（已脱敏）**：`AIzaSy...YyIs`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs",
```

### 7. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 359 行）
- **密钥（已脱敏）**：`AIzaSy...agEM`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM",
```

### 8. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 360 行）
- **密钥（已脱敏）**：`AIzaSy...DrlU`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU",
```

### 9. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 361 行）
- **密钥（已脱敏）**：`AIzaSy...hrh0`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0",
```

### 10. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 362 行）
- **密钥（已脱敏）**：`AIzayD...bX4A`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A",
```

### 11. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 363 行）
- **密钥（已脱敏）**：`AIzaSy...wX7c`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c",
```

### 12. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 364 行）
- **密钥（已脱敏）**：`AIzaSy...mLd4`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4",
```

### 13. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 365 行）
- **密钥（已脱敏）**：`AIzaSy...DQgY`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQgY",
```

### 14. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 366 行）
- **密钥（已脱敏）**：`AIzaSy...4wtM`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyA5_iVawFQ8ABuTZNUdcwERLJv_a_p4wtM",
```

### 15. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 367 行）
- **密钥（已脱敏）**：`AIzaSy...P5sQ`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyA4UrcGxgwQFTfaI3no3t7Lt1sjmdnP5sQ",
```

### 16. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 368 行）
- **密钥（已脱敏）**：`AIzaSy...cS7g`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyDSb51JiIcB6OJpwwMicseKRhhrOq1cS7g",
```

### 17. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 369 行）
- **密钥（已脱敏）**：`AIzaSy...vvuU`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyBF2RrAIm4a0mO64EShQfqfd2AFnzAvvuU",
```

### 18. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 370 行）
- **密钥（已脱敏）**：`AIzaSy...NXsw`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyBcE-OOIbhjyR83gm4r2MFCu4MJmprNXsw",
```

### 19. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 371 行）
- **密钥（已脱敏）**：`AIzaSy...FmqE`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyB8qGxt4ec15vitgn44duC5ucxaOi4FmqE",
```

### 20. [HIGH] Google Gemini / GCP API Key

- **仓库**：`FAHTHIZ/Oasis-`
- **文件**：`src/security/data/secret-rules.json`（第 372 行）
- **密钥（已脱敏）**：`AIzaSy...0nvY`
- **链接**：https://github.com/FAHTHIZ/Oasis-/blob/main/src/security/data/secret-rules.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaSyA8vmApnrHNFE0bApF4hoZ11srVL_n0nvY"
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

