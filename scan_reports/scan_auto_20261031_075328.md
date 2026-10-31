# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-31 07:53:28 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 3449 |
| 发现数量 | 3 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 3 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`ypollak2/llm-router`
- **文件**：`audit/11_SECURITY_AUDIT.md`（第 114 行）
- **密钥（已脱敏）**：`sk-CAN...2345`
- **链接**：https://github.com/ypollak2/llm-router/blob/main/audit/11_SECURITY_AUDIT.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
export SYNTHETIC_CANARY_API_KEY="sk-CANARY-DO-NOT-LEAK-12345"
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`MiManchiALL/WhyCode`
- **文件**：`apps/desktop/src/main/config.test.ts`（第 504 行）
- **密钥（已脱敏）**：`remove...cret`
- **链接**：https://github.com/MiManchiALL/WhyCode/blob/main/apps/desktop/src/main/config.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: 'removed-custom-secret',
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`MiManchiALL/WhyCode`
- **文件**：`apps/desktop/src/main/web-search-settings.test.ts`（第 16 行）
- **密钥（已脱敏）**：`privat...-key`
- **链接**：https://github.com/MiManchiALL/WhyCode/blob/main/apps/desktop/src/main/web-search-settings.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
perplexity: { apiKey: 'private-perplexity-key' },
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

