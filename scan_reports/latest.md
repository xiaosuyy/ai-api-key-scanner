# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-15 06:56:20 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 2288 |
| 发现数量 | 2 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 1 |
| LOW | 1 |

## 发现明细

### 1. [HIGH] Anthropic API Key

- **仓库**：`joker7866/kishore-social-studio`
- **文件**：`tests/unit/security-storage.test.ts`（第 19 行）
- **密钥（已脱敏）**：`sk-ant...3210`
- **链接**：https://github.com/joker7866/kishore-social-studio/blob/main/tests/unit/security-storage.test.ts
- **说明**：Anthropic Claude API 密钥。

```text
const ANTHROPIC_KEY = 'sk-ant-api03-ZyXwVuTsRqPoNmLkJiHgFeDcBa9876543210'
```

### 2. [LOW] AWS Access Key ID

- **仓库**：`manhquydev/flow-skill`
- **文件**：`plans/260618-usage-log-feature/cards/C-001.md`（第 51 行）
- **密钥（已脱敏）**：`AKIA12...ALUE`
- **链接**：https://github.com/manhquydev/flow-skill/blob/master/plans/260618-usage-log-feature/cards/C-001.md
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
**3. Masking — `harness --summary "api_key=AKIA12345SECRETVALUE"`:** written `args` field = `***redacted***`; leak check `'AKIA12345' in args` → False.
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

