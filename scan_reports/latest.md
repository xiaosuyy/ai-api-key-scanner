# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-18 06:55:29 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 2409 |
| 发现数量 | 3 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 3 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`DeliciousBuding/metapi-go`
- **文件**：`config/defaults.go`（第 7 行）
- **密钥（已脱敏）**：`change...oken`
- **链接**：https://github.com/DeliciousBuding/metapi-go/blob/master/config/defaults.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
DefaultAuthToken             = "change-me-admin-token"
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`DeliciousBuding/metapi-go`
- **文件**：`handler/admin/accounts_test.go`（第 1312 行）
- **密钥（已脱敏）**：`new-se...-xyz`
- **链接**：https://github.com/DeliciousBuding/metapi-go/blob/master/handler/admin/accounts_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
t.Errorf("expected accessToken='new-session-token-xyz', got %q", accessToken)
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`DeliciousBuding/metapi-go`
- **文件**：`handler/admin/auth_settings_test.go`（第 27 行）
- **密钥（已脱敏）**：`admin-...oken`
- **链接**：https://github.com/DeliciousBuding/metapi-go/blob/master/handler/admin/auth_settings_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
config.SetRuntime(&config.RuntimeSettings{AuthToken: "admin-auth-settings-token"})
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

