# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-10-22 07:24:48 UTC |
| 扫描仓库数 | 50 |
| 扫描文件数 | 8225 |
| 发现数量 | 8 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 1 |
| MEDIUM | 7 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`PMZPZM0/codex-harness-desktop`
- **文件**：`electron/features/cloud-memory-ipc.ts`（第 151 行）
- **密钥（已脱敏）**：`CLOUD_...OKEN`
- **链接**：https://github.com/PMZPZM0/codex-harness-desktop/blob/main/electron/features/cloud-memory-ipc.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
secretKey: "CLOUD_MEMORY_MCP_TOKEN",
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`Remote-Arc/remote-arc`
- **文件**：`apps/relay/scripts/arc-app-connections-test.ts`（第 30 行）
- **密钥（已脱敏）**：`privat...oken`
- **链接**：https://github.com/Remote-Arc/remote-arc/blob/master/apps/relay/scripts/arc-app-connections-test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
if(url==='https://api.notion.com/v1/oauth/token')return Response.json({access_token:'private-notion-token'});
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`Remote-Arc/remote-arc`
- **文件**：`apps/relay/scripts/arc-chat-test.ts`（第 313 行）
- **密钥（已脱敏）**：`fixtur...oken`
- **链接**：https://github.com/Remote-Arc/remote-arc/blob/master/apps/relay/scripts/arc-chat-test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
const vercelConnection=crypto.randomUUID();sql.prepare(`INSERT INTO app_connections(id,user_id,provider,account_id,account_label,status,permissions_json,scopes_json,token_ciphertext,created_at,updated_at) VALUES(?,'owner','vercel','fixture-vercel','Vercel','active','["read"]','[]',?,?,?)`).run(vercelConnection,await seal(env,{accessToken:'fixture-vercel-token',scopes:[],expiresAt:null},`app-token:
```

### 4. [MEDIUM] Generic API key assignment

- **仓库**：`Remote-Arc/remote-arc`
- **文件**：`apps/relay/scripts/arc-chat-test.ts`（第 358 行）
- **密钥（已脱敏）**：`fixtur...-key`
- **链接**：https://github.com/Remote-Arc/remote-arc/blob/master/apps/relay/scripts/arc-chat-test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
sql.prepare(`INSERT INTO app_connections(id,user_id,provider,account_id,account_label,status,permissions_json,scopes_json,token_ciphertext,created_at,updated_at) VALUES(?,'owner','google_calendar','fixture-calendar','Calendar','active','["read"]',?,?,?,?)`).run(calendarConnection,JSON.stringify(['https://www.googleapis.com/auth/calendar.readonly']),await seal(env,{accessToken:'fixture-calendar-key
```

### 5. [MEDIUM] Generic API key assignment

- **仓库**：`Remote-Arc/remote-arc`
- **文件**：`apps/relay/scripts/arc-task-eval-fixture-test.ts`（第 8 行）
- **密钥（已脱敏）**：`synthe...cret`
- **链接**：https://github.com/Remote-Arc/remote-arc/blob/master/apps/relay/scripts/arc-task-eval-fixture-test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
process.env.OPENAI_API_KEY='synthetic-eval-fixture-not-a-secret';
```

### 6. [MEDIUM] Generic API key assignment

- **仓库**：`Remote-Arc/remote-arc`
- **文件**：`apps/relay/scripts/arc-task-live-eval.ts`（第 146 行）
- **密钥（已脱敏）**：`fixtur...oken`
- **链接**：https://github.com/Remote-Arc/remote-arc/blob/master/apps/relay/scripts/arc-task-live-eval.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
if(item.id.startsWith('attention')){const calendarId=crypto.randomUUID(),scopes=['https://www.googleapis.com/auth/calendar.readonly'];sql.prepare(`INSERT INTO app_connections(id,user_id,provider,account_id,account_label,status,permissions_json,scopes_json,token_ciphertext,created_at,updated_at) VALUES(?,?,'google_calendar','fixture-calendar','Synthetic calendar','active','["read"]',?,?,?,?)`).run(
```

### 7. [MEDIUM] Generic API key assignment

- **仓库**：`Remote-Arc/remote-arc`
- **文件**：`apps/relay/scripts/arc-working-context-test.ts`（第 47 行）
- **密钥（已脱敏）**：`contex...cret`
- **链接**：https://github.com/Remote-Arc/remote-arc/blob/master/apps/relay/scripts/arc-working-context-test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
sql.prepare(`INSERT INTO app_connections(id,user_id,provider,account_id,account_label,status,permissions_json,scopes_json,token_ciphertext,created_at,updated_at) VALUES(?,?,?,?,?,'active','["read"]',?,?,?,?)`).run(id,user,provider,id,'Context fixture',JSON.stringify(appScopes(provider as any,['read'])),await seal(env,{accessToken:'context-fixture-not-a-secret'},`app-token:${user}:${provider}:${id}
```

### 8. [HIGH] Google Gemini / GCP API Key

- **仓库**：`phillipxnguyen/wikiPhidia`
- **文件**：`index.html`（第 12118 行）
- **密钥（已脱敏）**：`AIzaSy..._ZlM`
- **链接**：https://github.com/phillipxnguyen/wikiPhidia/blob/main/index.html
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
apiKey: "AIzaSyBcgv5s1xc_4tfN8k3EsyiDKCGOXaz_ZlM",
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

