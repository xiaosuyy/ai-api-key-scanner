# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-12 09:06:04 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 2633 |
| 发现数量 | 6 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 4 |
| LOW | 2 |

## 发现明细

### 1. [LOW] Generic API key assignment

- **仓库**：`grebocheck/FormaTranslate`
- **文件**：`tests/test_ocr.py`（第 122 行）
- **密钥（已脱敏）**：`synthe...-key`
- **链接**：https://github.com/grebocheck/FormaTranslate/blob/main/tests/test_ocr.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
result = TranslationEngine(Settings(model="offline-fake", api_key="synthetic-private-key"), provider=FakeProvider()).translate(
```

### 2. [LOW] Generic API key assignment

- **仓库**：`grebocheck/FormaTranslate`
- **文件**：`tests/test_provider.py`（第 285 行）
- **密钥（已脱敏）**：`secret...-key`
- **链接**：https://github.com/grebocheck/FormaTranslate/blob/main/tests/test_provider.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
settings(api_key="secret-sensitive-key"), transport=httpx.MockTransport(handler)
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`grebocheck/FormaTranslate`
- **文件**：`tests/test_translation_memory.py`（第 117 行）
- **密钥（已脱敏）**：`never-...-key`
- **链接**：https://github.com/grebocheck/FormaTranslate/blob/main/tests/test_translation_memory.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
settings = Settings(model="model-A", api_key="never-persist-this-key")
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`grebocheck/FormaTranslate`
- **文件**：`tests/test_ui_usage.py`（第 182 行）
- **密钥（已脱敏）**：`anothe...ount`
- **链接**：https://github.com/grebocheck/FormaTranslate/blob/main/tests/test_ui_usage.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
backend._settings = backend._settings.with_overrides(api_key="another-offline-account")
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`grebocheck/FormaTranslate`
- **文件**：`tests/test_ui_usage.py`（第 347 行）
- **密钥（已脱敏）**：`second...ount`
- **链接**：https://github.com/grebocheck/FormaTranslate/blob/main/tests/test_ui_usage.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
backend._settings = original_settings.with_overrides(api_key="second-offline-account")
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`syuancheng/readflow`
- **文件**：`tests/unit/config.test.ts`（第 25 行）
- **密钥（已脱敏）**：`sk-env...9999`
- **链接**：https://github.com/syuancheng/readflow/blob/main/tests/unit/config.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const rows = providerStatuses({}, env({ DEEPSEEK_API_KEY: "sk-env-deepseek-9999" }));
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

