# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-11 08:11:56 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 3961 |
| 发现数量 | 2 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 2 |

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

- **仓库**：`HelpCode-ai/anythingmcp`
- **文件**：`packages/backend/src/adapters/de/weclapp.live.spec.ts`（第 101 行）
- **密钥（已脱敏）**：`sentin...2345`
- **链接**：https://github.com/HelpCode-ai/anythingmcp/blob/main/packages/backend/src/adapters/de/weclapp.live.spec.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
authConfig: { headerName: 'AuthenticationToken', apiKey: 'sentinel-token-12345' },
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

