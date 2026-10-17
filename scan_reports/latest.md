# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-17 06:59:46 UTC |
| 扫描仓库数 | 50 |
| 扫描文件数 | 7590 |
| 发现数量 | 16 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 16 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`SailingLoong/LoongPort`
- **文件**：`src-tauri/src/commands/relay/login.rs`（第 2659 行）
- **密钥（已脱敏）**：`long-l...oken`
- **链接**：https://github.com/SailingLoong/LoongPort/blob/main/src-tauri/src/commands/relay/login.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
access_token: "long-lived-access-token".into(),
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`diegosouzapw/OmniRoute`
- **文件**：`@omniroute/opencode-plugin-v2/tests/warm-snapshot-identity.test.ts`（第 47 行）
- **密钥（已脱敏）**：`key-wr...nfig`
- **链接**：https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.52/@omniroute/opencode-plugin-v2/tests/warm-snapshot-identity.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
options: { baseURL, providerId: "warmid", apiKey: "key-written-in-the-config" },
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`whdrnr2583-cmd/koreanpulse`
- **文件**：`tests/test_corp_code.py`（第 174 行）
- **密钥（已脱敏）**：`SUPER_...2345`
- **链接**：https://github.com/whdrnr2583-cmd/koreanpulse/blob/main/tests/test_corp_code.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secret_key = "SUPER_SECRET_DART_KEY_12345"
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`whdrnr2583-cmd/koreanpulse`
- **文件**：`tests/test_corp_code.py`（第 191 行）
- **密钥（已脱敏）**：`SUPER_...2345`
- **链接**：https://github.com/whdrnr2583-cmd/koreanpulse/blob/main/tests/test_corp_code.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secret_key = "SUPER_SECRET_DART_KEY_12345"
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`whdrnr2583-cmd/koreanpulse`
- **文件**：`tests/test_dart.py`（第 889 行）
- **密钥（已脱敏）**：`SUPER_...9999`
- **链接**：https://github.com/whdrnr2583-cmd/koreanpulse/blob/main/tests/test_dart.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secret_key = "SUPER_SECRET_DART_KEY_99999"
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`whdrnr2583-cmd/koreanpulse`
- **文件**：`tests/test_dart.py`（第 907 行）
- **密钥（已脱敏）**：`SUPER_...9999`
- **链接**：https://github.com/whdrnr2583-cmd/koreanpulse/blob/main/tests/test_dart.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secret_key = "SUPER_SECRET_DART_KEY_99999"
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`Raaif-Yousuf/Wingman`
- **文件**：`src/config.rs`（第 3898 行）
- **密钥（已脱敏）**：`AIza-r...mini`
- **链接**：https://github.com/Raaif-Yousuf/Wingman/blob/master/src/config.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
config.providers.gemini.api_key = "AIza-real-secret-gemini".to_string();
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`Raaif-Yousuf/Wingman`
- **文件**：`src/config.rs`（第 4562 行）
- **密钥（已脱敏）**：`sk-rea...enai`
- **链接**：https://github.com/Raaif-Yousuf/Wingman/blob/master/src/config.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
config.providers.openai.api_key = "sk-real-secret-openai".to_string();
```

### 9. [MEDIUM] Generic API key assignment

- **仓库**：`Raaif-Yousuf/Wingman`
- **文件**：`src/config.rs`（第 4563 行）
- **密钥（已脱敏）**：`sk-ant...opic`
- **链接**：https://github.com/Raaif-Yousuf/Wingman/blob/master/src/config.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
config.providers.anthropic.api_key = "sk-ant-real-secret-anthropic".to_string();
```

### 10. [MEDIUM] Generic API key assignment

- **仓库**：`Raaif-Yousuf/Wingman`
- **文件**：`src/config.rs`（第 4590 行）
- **密钥（已脱敏）**：`sk-rea...alue`
- **链接**：https://github.com/Raaif-Yousuf/Wingman/blob/master/src/config.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
config.providers.openai.api_key = "sk-real-secret-value".to_string();
```

### 11. [MEDIUM] Generic API key assignment

- **仓库**：`Raaif-Yousuf/Wingman`
- **文件**：`src/config.rs`（第 4998 行）
- **密钥（已脱敏）**：`sk-goe...disk`
- **链接**：https://github.com/Raaif-Yousuf/Wingman/blob/master/src/config.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
config.providers.openai.api_key = "sk-goes-straight-to-disk".to_string();
```

### 12. [MEDIUM] Generic API key assignment

- **仓库**：`Raaif-Yousuf/Wingman`
- **文件**：`src/config.rs`（第 5212 行）
- **密钥（已脱敏）**：`sk-sho...disk`
- **链接**：https://github.com/Raaif-Yousuf/Wingman/blob/master/src/config.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
config.providers.openai.api_key = "sk-should-never-reach-disk".to_string();
```

### 13. [MEDIUM] Generic API key assignment

- **仓库**：`Raaif-Yousuf/Wingman`
- **文件**：`src/config.rs`（第 5230 行）
- **密钥（已脱敏）**：`sk-sho...disk`
- **链接**：https://github.com/Raaif-Yousuf/Wingman/blob/master/src/config.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
on_disk.providers.openai.api_key = "sk-should-not-reach-disk".to_string();
```

### 14. [MEDIUM] Generic API key assignment

- **仓库**：`Raaif-Yousuf/Wingman`
- **文件**：`src/config.rs`（第 5532 行）
- **密钥（已脱敏）**：`sk-rea...enai`
- **链接**：https://github.com/Raaif-Yousuf/Wingman/blob/master/src/config.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
config.providers.openai.api_key = "sk-real-secret-openai".to_string();
```

### 15. [MEDIUM] Generic API key assignment

- **仓库**：`Raaif-Yousuf/Wingman`
- **文件**：`src/config_writer.rs`（第 1439 行）
- **密钥（已脱敏）**：`sk-typ...ings`
- **链接**：https://github.com/Raaif-Yousuf/Wingman/blob/master/src/config_writer.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
after.providers.openai.api_key = "sk-typed-in-settings".into();
```

### 16. [MEDIUM] Generic API key assignment

- **仓库**：`Raaif-Yousuf/Wingman`
- **文件**：`src/ui/settings.rs`（第 8953 行）
- **密钥（已脱敏）**：`sk-liv...1234`
- **链接**：https://github.com/Raaif-Yousuf/Wingman/blob/master/src/ui/settings.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
config.providers.openai.api_key = "sk-live-secret-should-not-appear-1234".to_string();
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

