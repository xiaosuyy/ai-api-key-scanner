# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-06 09:18:08 UTC |
| 扫描仓库数 | 48 |
| 扫描文件数 | 9404 |
| 发现数量 | 5 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 4 |
| LOW | 1 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`Sociaro-Research/open-media-gateway`
- **文件**：`internal/api/provider_resources_test.go`（第 274 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/Sociaro-Research/open-media-gateway/blob/main/internal/api/provider_resources_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
native, e := kling.Definition().Factory(providerkit.Credentials{APIKey: "synthetic-resource-key", Extra: prices}, nil, &http.Client{Transport: resourceAPITransport{t}})
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`piazzatron/anki-smart-notes`
- **文件**：`tests/test_local_server.py`（第 329 行）
- **密钥（已脱敏）**：`jwt-fr...nfig`
- **链接**：https://github.com/piazzatron/anki-smart-notes/blob/main/tests/test_local_server.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
auth_token="jwt-from-plugin-config",
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`piazzatron/anki-smart-notes`
- **文件**：`tests/test_local_server.py`（第 596 行）
- **密钥（已脱敏）**：`synthe...oken`
- **链接**：https://github.com/piazzatron/anki-smart-notes/blob/main/tests/test_local_server.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
config.auth_token = "synthetic-auth-token"
```

### 4. [LOW] Generic API key assignment

- **仓库**：`piazzatron/anki-smart-notes`
- **文件**：`tests/test_local_server.py`（第 305 行）
- **密钥（已脱敏）**：`jwt-fr...nfig`
- **链接**：https://github.com/piazzatron/anki-smart-notes/blob/main/tests/test_local_server.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
MagicMock(auth_token="jwt-from-plugin-config", times_used=3),
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`milind-soni/OpenMausBot`
- **文件**：`cloudflare/control-plane/test/highlevel.test.ts`（第 21 行）
- **密钥（已脱敏）**：`eyJhbG....sig`
- **链接**：https://github.com/milind-soni/OpenMausBot/blob/main/cloudflare/control-plane/test/highlevel.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.access-token-for-location.sig";
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

