# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-13 09:04:03 UTC |
| 扫描仓库数 | 19 |
| 扫描文件数 | 3095 |
| 发现数量 | 2 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 2 |

## 发现明细

### 1. [MEDIUM] Google OAuth Client Secret

- **仓库**：`lidge-jun/opencodex`
- **文件**：`devlog/_fin/140_remaining-provider-ports/21_phase2_antigravity-oauth-cca.md`（第 32 行）
- **密钥（已脱敏）**：`GOCSPX...qDAf`
- **链接**：https://github.com/lidge-jun/opencodex/blob/dev/devlog/_fin/140_remaining-provider-ports/21_phase2_antigravity-oauth-cca.md
- **说明**：Google OAuth 客户端密钥。

```text
ClientSecret     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
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`XargonWan/Synthetic_Heart`
- **文件**：`container/searxng/settings.yml`（第 26 行）
- **密钥（已脱敏）**：`synth-...e-me`
- **链接**：https://github.com/XargonWan/Synthetic_Heart/blob/develop/container/searxng/settings.yml
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secret_key: "synth-searxng-local-instance-change-me"
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

