# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-21 07:00:48 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 4412 |
| 发现数量 | 4 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 1 |
| MEDIUM | 3 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`openai/openai-node`
- **文件**：`ecosystem-tests/browser-direct-import/public/index.js`（第 132 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/openai/openai-node/blob/main/ecosystem-tests/browser-direct-import/public/index.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
browserError = new OpenAI({ apiKey: 'synthetic-browser-api-key' });
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`openai/openai-node`
- **文件**：`ecosystem-tests/browser-direct-import/src/test.ts`（第 14 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/openai/openai-node/blob/main/ecosystem-tests/browser-direct-import/src/test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const apiKey = live ? process.env.OPENAI_API_KEY : 'synthetic-browser-api-key';
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`openai/openai-python`
- **文件**：`examples/browser/exercise_read_only.py`（第 183 行）
- **密钥（已脱敏）**：`synthe...ader`
- **链接**：https://github.com/openai/openai-python/blob/main/examples/browser/exercise_read_only.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
api_key="synthetic-local-reader",
```

### 4. [HIGH] Google Gemini / GCP API Key

- **仓库**：`OneHumanAI/onehuman`
- **文件**：`server/firebase-auth.ts`（第 14 行）
- **密钥（已脱敏）**：`AIzaSy...XQo8`
- **链接**：https://github.com/OneHumanAI/onehuman/blob/main/server/firebase-auth.ts
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
const ONEHUMAN_WEB = { projectId: 'onehuman-ai', apiKey: 'AIzaSyAxjCRgKklxqc0_M6vSKZfpIFb8UMDXQo8', appId: '1:667471175488:web:7ced82d980e90d9e98a4a5', messagingSenderId: '667471175488' };
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

