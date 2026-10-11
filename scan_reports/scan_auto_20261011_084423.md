# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-11 08:44:23 UTC |
| 扫描仓库数 | 50 |
| 扫描文件数 | 9193 |
| 发现数量 | 9 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| MEDIUM | 9 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`sleep2agi/agent-network`
- **文件**：`agent-network/bin/cli.ts`（第 7394 行）
- **密钥（已脱敏）**：`disabl...rent`
- **链接**：https://github.com/sleep2agi/agent-network/blob/main/agent-network/bin/cli.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
COMMHUB_AUTH_TOKEN: "disabled-for-grok-cli-parent",
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`sleep2agi/agent-network`
- **文件**：`agent-network/bin/cli.ts`（第 7454 行）
- **密钥（已脱敏）**：`disabl...rent`
- **链接**：https://github.com/sleep2agi/agent-network/blob/main/agent-network/bin/cli.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
env.COMMHUB_AUTH_TOKEN = "disabled-for-grok-cli-parent";
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`umutkeltek/switchback`
- **文件**：`cli/tests/sb_claude_profiles.zsh`（第 118 行）
- **密钥（已脱敏）**：`fixtur...leak`
- **链接**：https://github.com/umutkeltek/switchback/blob/main/cli/tests/sb_claude_profiles.zsh
- **说明**：赋值给 API key 变量的疑似密钥。

```text
fixture_access_token="fixture-access-token-must-not-leak"
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`umutkeltek/switchback`
- **文件**：`cli/tests/sb_pulse.zsh`（第 39 行）
- **密钥（已脱敏）**：`scout-...leak`
- **链接**：https://github.com/umutkeltek/switchback/blob/main/cli/tests/sb_pulse.zsh
- **说明**：赋值给 API key 变量的疑似密钥。

```text
export SWITCHBACK_SCOUT_API_KEY="scout-secret-value-must-not-leak"
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`yyjeqhc/webcodex`
- **文件**：`apps/desktop/src/features/ConnectionsTools.test.tsx`（第 147 行）
- **密钥（已脱敏）**：`write-...-key`
- **链接**：https://github.com/yyjeqhc/webcodex/blob/main/apps/desktop/src/features/ConnectionsTools.test.tsx
- **说明**：赋值给 API key 变量的疑似密钥。

```text
api_key: "write-only-server-key",
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`yyjeqhc/webcodex`
- **文件**：`apps/desktop/src/features/ConnectionsTools.test.tsx`（第 548 行）
- **密钥（已脱敏）**：`write-...cret`
- **链接**：https://github.com/yyjeqhc/webcodex/blob/main/apps/desktop/src/features/ConnectionsTools.test.tsx
- **说明**：赋值给 API key 变量的疑似密钥。

```text
expect(captured[0]).toMatchObject({ id: "personal", expected_revision: 1, name: "Personal renamed", host_mode: "standalone", api_key: "write-only-fixture-secret" });
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`yyjeqhc/webcodex`
- **文件**：`apps/desktop/src/features/ConnectionsTools.test.tsx`（第 569 行）
- **密钥（已脱敏）**：`mcp-ui...ture`
- **链接**：https://github.com/yyjeqhc/webcodex/blob/main/apps/desktop/src/features/ConnectionsTools.test.tsx
- **说明**：赋值给 API key 变量的疑似密钥。

```text
expect(captured[0]).toMatchObject({ id: null, expected_revision: 0, command: "npx", args: ["-y", "@playwright/mcp"], env: { API_KEY: "mcp-ui-private-fixture" } });
```

### 8. [MEDIUM] Generic API key assignment

- **仓库**：`HelpCode-ai/anythingmcp`
- **文件**：`packages/backend/src/adapters/de/weclapp.live.spec.ts`（第 101 行）
- **密钥（已脱敏）**：`sentin...2345`
- **链接**：https://github.com/HelpCode-ai/anythingmcp/blob/main/packages/backend/src/adapters/de/weclapp.live.spec.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
authConfig: { headerName: 'AuthenticationToken', apiKey: 'sentinel-token-12345' },
```

### 9. [MEDIUM] Generic API key assignment

- **仓库**：`SpiralCloudOmega/DevTeam6`
- **文件**：`ASSET_INVENTORY.md`（第 60 行）
- **密钥（已脱敏）**：`cyborg...a994`
- **链接**：https://github.com/SpiralCloudOmega/DevTeam6/blob/main/ASSET_INVENTORY.md
- **说明**：赋值给 API key 变量的疑似密钥。

```text
CYBORGDB_API_KEY="cyborg_bfaea874c10d48bab8b69e4bc29da994"
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

