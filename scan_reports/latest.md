# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-23 06:50:21 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 2996 |
| 发现数量 | 2 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 2 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`civarry/wickey`
- **文件**：`test/dotenv.test.ts`（第 49 行）
- **密钥（已脱敏）**：`sk-ant...3456`
- **链接**：https://github.com/civarry/wickey/blob/main/test/dotenv.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const a = one('export ANTHROPIC_API_KEY="sk-ant-api03-xyz123456"');
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`kalinbogatzevski/captain-memo`
- **文件**：`src/shared/paths.ts`（第 136 行）
- **密钥（已脱敏）**：`CAPTAI..._KEY`
- **链接**：https://github.com/kalinbogatzevski/captain-memo/blob/master/src/shared/paths.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
export const ENV_OPENAI_API_KEY = 'CAPTAIN_MEMO_OPENAI_API_KEY';
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

