# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-13 08:48:28 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 2883 |
| 发现数量 | 1 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 1 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`Opti-Advisr/Opti-Advisr`
- **文件**：`frontend/src/lib/api.js`（第 11 行）
- **密钥（已脱敏）**：`oYQslE...Gk0Y`
- **链接**：https://github.com/Opti-Advisr/Opti-Advisr/blob/main/frontend/src/lib/api.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const DEFAULT_API_KEY = "oYQslEeolb4oly9qw1sKo4tTT6owJZl5695SGk0Y";
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

