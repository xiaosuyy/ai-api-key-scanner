# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-18 07:16:15 UTC |
| 扫描仓库数 | 48 |
| 扫描文件数 | 5561 |
| 发现数量 | 2 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 2 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`jimoto-no-llm/rustdsh`
- **文件**：`docker/searxng/settings.yml`（第 19 行）
- **密钥（已脱敏）**：`rdsh-l...-key`
- **链接**：https://github.com/jimoto-no-llm/rustdsh/blob/main/docker/searxng/settings.yml
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secret_key: "rdsh-local-searxng-change-this-secret-key"
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`YeshayaYaoz/hair_salon_whatsapp_bot`
- **文件**：`backend/scripts/preview-emails.ts`（第 44 行）
- **密钥（已脱敏）**：`previe...-key`
- **链接**：https://github.com/YeshayaYaoz/hair_salon_whatsapp_bot/blob/claude/upload-v5aw7a/backend/scripts/preview-emails.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.RESEND_API_KEY = "preview-only-not-a-real-key";
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

