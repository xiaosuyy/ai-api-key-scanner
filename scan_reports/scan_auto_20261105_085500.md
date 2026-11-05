# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-05 08:55:00 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 3805 |
| 发现数量 | 4 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 4 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`mouse0329/nezumi-ai`
- **文件**：`app/src/main/java/com/nezumi_ai/utils/PreferencesHelper.kt`（第 27 行）
- **密钥（已脱敏）**：`brave_..._key`
- **链接**：https://github.com/mouse0329/nezumi-ai/blob/main/app/src/main/java/com/nezumi_ai/utils/PreferencesHelper.kt
- **说明**：赋值给 API key 变量的疑似密钥。

```text
private const val KEY_BRAVE_SEARCH_API_KEY = "brave_search_api_key"
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`nasser1941/lcode`
- **文件**：`docs/usage.md`（第 713 行）
- **密钥（已脱敏）**：`change...ndom`
- **链接**：https://github.com/nasser1941/lcode/blob/main/docs/usage.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secret_key: "change-me-to-something-random"
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`nasser1941/lcode`
- **文件**：`tests/test_secretscan.py`（第 45 行）
- **密钥（已脱敏）**：`change...ndom`
- **链接**：https://github.com/nasser1941/lcode/blob/main/tests/test_secretscan.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
'secret_key: "change-me-to-something-random"',
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`KaushalKumar-100/CineBook`
- **文件**：`backend/tests/test_config.py`（第 16 行）
- **密钥（已脱敏）**：`develo...cret`
- **链接**：https://github.com/KaushalKumar-100/CineBook/blob/main/backend/tests/test_config.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secret_key="development-only-change-this-secret",
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

