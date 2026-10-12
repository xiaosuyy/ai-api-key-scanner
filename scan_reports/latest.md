# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-12 08:29:54 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 4334 |
| 发现数量 | 4 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 4 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`quodeq/quodeq`
- **文件**：`benchmarks/.corpus/synthetic/js-security/config.js`（第 2 行）
- **密钥（已脱敏）**：`sk-liv...aabb`
- **链接**：https://github.com/quodeq/quodeq/blob/develop/benchmarks/.corpus/synthetic/js-security/config.js
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey: "sk-live-11223344556677889900aabb",
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`quodeq/quodeq`
- **文件**：`benchmarks/.corpus/synthetic/py-security/config.py`（第 1 行）
- **密钥（已脱敏）**：`sk-liv...ba98`
- **链接**：https://github.com/quodeq/quodeq/blob/develop/benchmarks/.corpus/synthetic/py-security/config.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
API_KEY = "sk-live-9f8e7d6c5b4a3210fedcba98"
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`QuantSingularity/RiskOptimizer`
- **文件**：`code/backend/src/core/config.py`（第 159 行）
- **密钥（已脱敏）**：`dev-se...tion`
- **链接**：https://github.com/QuantSingularity/RiskOptimizer/blob/main/code/backend/src/core/config.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secret_key = "dev-secret-key-change-in-production"
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`QuantSingularity/RiskOptimizer`
- **文件**：`code/backend/src/core/config.py`（第 170 行）
- **密钥（已脱敏）**：`dev-jw...tion`
- **链接**：https://github.com/QuantSingularity/RiskOptimizer/blob/main/code/backend/src/core/config.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
jwt_secret_key = "dev-jwt-secret-key-change-in-production"
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

