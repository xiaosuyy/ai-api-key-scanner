# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-25 07:23:38 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 3892 |
| 发现数量 | 3 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 1 |
| MEDIUM | 2 |

## 发现明细

### 1. [HIGH] Google Gemini / GCP API Key

- **仓库**：`721189/Market-Metrics`
- **文件**：`firebase-applet-config.json`（第 4 行）
- **密钥（已脱敏）**：`AIzaSy...IL2s`
- **链接**：https://github.com/721189/Market-Metrics/blob/main/firebase-applet-config.json
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"apiKey": "AIzaSyBf8gwNxlu7HT2iZrnvPIPL87aiiBdIL2s",
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`arbiterForge/codeArbiter`
- **文件**：`.codearbiter/reports/2026-07-14-pi-support-handoff/blocker-2-review-package-v2.md`（第 175 行）
- **密钥（已脱敏）**：`sk-CVl...e123`
- **链接**：https://github.com/arbiterForge/codeArbiter/blob/main/.codearbiter/reports/2026-07-14-pi-support-handoff/blocker-2-review-package-v2.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
self.assertTrue(self._matches('const FARM_API_KEY = "sk-CVlQvxKsecretvalue123";'))
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`arbiterForge/codeArbiter`
- **文件**：`.codearbiter/reports/2026-07-14-pi-support-handoff/blocker-2-review-package.md`（第 175 行）
- **密钥（已脱敏）**：`sk-CVl...e123`
- **链接**：https://github.com/arbiterForge/codeArbiter/blob/main/.codearbiter/reports/2026-07-14-pi-support-handoff/blocker-2-review-package.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
self.assertTrue(self._matches('const FARM_API_KEY = "sk-CVlQvxKsecretvalue123";'))
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

