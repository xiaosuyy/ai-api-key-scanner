# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-08 08:26:14 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 3712 |
| 发现数量 | 39 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 34 |
| MEDIUM | 5 |

## 发现明细

### 1. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`.github/bandit-baseline.json`（第 3278 行）
- **密钥（已脱敏）**：`sk-ant...a1b2`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/.github/bandit-baseline.json
- **说明**：Anthropic Claude API 密钥。

```text
"code": "111 \n112 SECRET = \"sk-ant-a1b2c3d4a1b2c3d4a1b2c3d4a1b2c3d4a1b2\"\n113 \n",
```

### 2. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`.github/bandit-baseline.json`（第 3288 行）
- **密钥（已脱敏）**：`sk-ant...a1b2`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/.github/bandit-baseline.json
- **说明**：Anthropic Claude API 密钥。

```text
"issue_text": "Possible hardcoded password: 'sk-ant-a1b2c3d4a1b2c3d4a1b2c3d4a1b2c3d4a1b2'",
```

### 3. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`.github/bandit-baseline.json`（第 3876 行）
- **密钥（已脱敏）**：`sk-ant...u901`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/.github/bandit-baseline.json
- **说明**：Anthropic Claude API 密钥。

```text
"code": "425 \n426 SECRET = \"sk-ant-abc123def456ghi789jkl012mno345pqr678stu901\"\n427 \n",
```

### 4. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`.github/bandit-baseline.json`（第 3886 行）
- **密钥（已脱敏）**：`sk-ant...u901`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/.github/bandit-baseline.json
- **说明**：Anthropic Claude API 密钥。

```text
"issue_text": "Possible hardcoded password: 'sk-ant-abc123def456ghi789jkl012mno345pqr678stu901'",
```

### 5. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`.github/bandit-baseline.json`（第 3896 行）
- **密钥（已脱敏）**：`sk-ant...AAAA`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/.github/bandit-baseline.json
- **说明**：Anthropic Claude API 密钥。

```text
"code": "526 \n527     SECRET = \"invalid key: sk-ant-api03-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\"\n528 \n",
```

### 6. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`.github/bandit-baseline.json`（第 3906 行）
- **密钥（已脱敏）**：`sk-ant...AAAA`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/.github/bandit-baseline.json
- **说明**：Anthropic Claude API 密钥。

```text
"issue_text": "Possible hardcoded password: 'invalid key: sk-ant-api03-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'",
```

### 7. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`.github/bandit-baseline.json`（第 3916 行）
- **密钥（已脱敏）**：`sk-ant...BBBB`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/.github/bandit-baseline.json
- **说明**：Anthropic Claude API 密钥。

```text
"code": "571 \n572     SECRET = \"sk-ant-api03-BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\"\n573 \n",
```

### 8. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`.github/bandit-baseline.json`（第 3926 行）
- **密钥（已脱敏）**：`sk-ant...BBBB`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/.github/bandit-baseline.json
- **说明**：Anthropic Claude API 密钥。

```text
"issue_text": "Possible hardcoded password: 'sk-ant-api03-BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'",
```

### 9. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`.github/bandit-baseline.json`（第 3936 行）
- **密钥（已脱敏）**：`sk-ant...r678`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/.github/bandit-baseline.json
- **说明**：Anthropic Claude API 密钥。

```text
"code": "645         _input_leaf's refusal already states.\"\"\"\n646         secret = \"sk-ant-abc123def456ghi789jkl012mno345pqr678\"\n647         check_output_policy(\"t\", {\"content\": f\"key={secret}\"})\n",
```

### 10. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`.github/bandit-baseline.json`（第 3946 行）
- **密钥（已脱敏）**：`sk-ant...r678`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/.github/bandit-baseline.json
- **说明**：Anthropic Claude API 密钥。

```text
"issue_text": "Possible hardcoded password: 'sk-ant-abc123def456ghi789jkl012mno345pqr678'",
```

### 11. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`.github/bandit-baseline.json`（第 3956 行）
- **密钥（已脱敏）**：`sk-ant...CCCC`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/.github/bandit-baseline.json
- **说明**：Anthropic Claude API 密钥。

```text
"code": "676 \n677 SECRET = \"sk-ant-api03-CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC\"\n678 \n",
```

### 12. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`.github/bandit-baseline.json`（第 3966 行）
- **密钥（已脱敏）**：`sk-ant...CCCC`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/.github/bandit-baseline.json
- **说明**：Anthropic Claude API 密钥。

```text
"issue_text": "Possible hardcoded password: 'sk-ant-api03-CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC'",
```

### 13. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/conftest.py`（第 2334 行）
- **密钥（已脱敏）**：`sk-ant...a1b2`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/conftest.py
- **说明**：Anthropic Claude API 密钥。

```text
"sk-ant-a1b2c3d4a1b2c3d4a1b2c3d4a1b2c3d4a1b2",
```

### 14. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/conftest.py`（第 2335 行）
- **密钥（已脱敏）**：`sk-ant...a1b2`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/conftest.py
- **说明**：Anthropic Claude API 密钥。

```text
"sk-ant-a1b2c3d4a1b2c3d4a1b2c3d4a1b2c3d4a1b2"),
```

### 15. [HIGH] Google Gemini / GCP API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/conftest.py`（第 2350 行）
- **密钥（已脱敏）**：`AIzaa1...4abc`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/conftest.py
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"maps lookup with AIzaa1b2c3d4a1b2c3d4a1b2c3d4a1b2c3d4abc failed",
```

### 16. [HIGH] Google Gemini / GCP API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/conftest.py`（第 2351 行）
- **密钥（已脱敏）**：`AIzaa1...4abc`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/conftest.py
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
"AIzaa1b2c3d4a1b2c3d4a1b2c3d4a1b2c3d4abc"),
```

### 17. [MEDIUM] AWS Access Key ID

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/conftest.py`（第 2347 行）
- **密钥（已脱敏）**：`AKIAA1...C3D4`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/conftest.py
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
"signing with AKIAA1B2C3D4A1B2C3D4 failed",
```

### 18. [MEDIUM] AWS Access Key ID

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/conftest.py`（第 2348 行）
- **密钥（已脱敏）**：`AKIAA1...C3D4`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/conftest.py
- **说明**：AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。

```text
"AKIAA1B2C3D4A1B2C3D4"),
```

### 19. [MEDIUM] Generic API key assignment

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_chatgpt_auth.py`（第 613 行）
- **密钥（已脱敏）**：`at-fro...cess`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_chatgpt_auth.py
- **说明**：赋值给 API key 变量的疑似密钥。

```text
data["session"].update(access_token="at-from-the-other-process",
```

### 20. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_logging_setup.py`（第 234 行）
- **密钥（已脱敏）**：`sk-ant...a1b2`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_logging_setup.py
- **说明**：Anthropic Claude API 密钥。

```text
SECRET = "sk-ant-a1b2c3d4a1b2c3d4a1b2c3d4a1b2c3d4a1b2"
```

### 21. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_mcp_client.py`（第 56 行）
- **密钥（已脱敏）**：`sk-ant...AAAA`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_mcp_client.py
- **说明**：Anthropic Claude API 密钥。

```text
return "token sk-ant-api03-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
```

### 22. [HIGH] OpenAI API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_permission_context.py`（第 257 行）
- **密钥（已脱敏）**：`sk-abc...r678`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_permission_context.py
- **说明**：OpenAI 风格 sk- 密钥（也覆盖 DeepSeek、Moonshot 等同类前缀）。

```text
leaky = "found key sk-abc123def456ghi789jkl012mno345pqr678 in the page"
```

### 23. [HIGH] OpenAI API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_permission_context.py`（第 263 行）
- **密钥（已脱敏）**：`sk-abc...r678`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_permission_context.py
- **说明**：OpenAI 风格 sk- 密钥（也覆盖 DeepSeek、Moonshot 等同类前缀）。

```text
assert "sk-abc123def456ghi789jkl012mno345pqr678" not in result["content"]
```

### 24. [HIGH] OpenAI API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 32 行）
- **密钥（已脱敏）**：`sk-abc...r678`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：OpenAI 风格 sk- 密钥（也覆盖 DeepSeek、Moonshot 等同类前缀）。

```text
text = "my key is sk-abc123def456ghi789jkl012mno345pqr678 and more text"
```

### 25. [HIGH] OpenAI API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 34 行）
- **密钥（已脱敏）**：`sk-abc...r678`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：OpenAI 风格 sk- 密钥（也覆盖 DeepSeek、Moonshot 等同类前缀）。

```text
assert "sk-abc123def456ghi789jkl012mno345pqr678" not in result
```

### 26. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 40 行）
- **密钥（已脱敏）**：`sk-ant...u901`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：Anthropic Claude API 密钥。

```text
text = "token: sk-ant-abc123def456ghi789jkl012mno345pqr678stu901"
```

### 27. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 414 行）
- **密钥（已脱敏）**：`sk-ant...u901`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：Anthropic Claude API 密钥。

```text
result = {"stdout": "", "stderr": "Error: sk-ant-abc123def456ghi789jkl012mno345pqr678stu901"}
```

### 28. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 439 行）
- **密钥（已脱敏）**：`sk-ant...u901`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：Anthropic Claude API 密钥。

```text
"sk-ant-abc123def456ghi789jkl012mno345pqr678stu901"}}}
```

### 29. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 446 行）
- **密钥（已脱敏）**：`sk-ant...u901`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：Anthropic Claude API 密钥。

```text
"sk-ant-abc123def456ghi789jkl012mno345pqr678stu901"]}
```

### 30. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 464 行）
- **密钥（已脱敏）**：`sk-ant...u901`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：Anthropic Claude API 密钥。

```text
inner["v"] = "sk-ant-abc123def456ghi789jkl012mno345pqr678stu901"
```

### 31. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 472 行）
- **密钥（已脱敏）**：`sk-ant...u901`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：Anthropic Claude API 密钥。

```text
SECRET = "sk-ant-abc123def456ghi789jkl012mno345pqr678stu901"
```

### 32. [HIGH] OpenAI API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 545 行）
- **密钥（已脱敏）**：`sk-abc...r678`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：OpenAI 风格 sk- 密钥（也覆盖 DeepSeek、Moonshot 等同类前缀）。

```text
return {"result": "leaked: sk-abc123def456ghi789jkl012mno345pqr678"}
```

### 33. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 573 行）
- **密钥（已脱敏）**：`sk-ant...AAAA`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：Anthropic Claude API 密钥。

```text
SECRET = "invalid key: sk-ant-api03-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
```

### 34. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 618 行）
- **密钥（已脱敏）**：`sk-ant...BBBB`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：Anthropic Claude API 密钥。

```text
SECRET = "sk-ant-api03-BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
```

### 35. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 662 行）
- **密钥（已脱敏）**：`sk-ant...r678`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：Anthropic Claude API 密钥。

```text
result = {"content": "key=sk-ant-abc123def456ghi789jkl012mno345pqr678"}
```

### 36. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 692 行）
- **密钥（已脱敏）**：`sk-ant...r678`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：Anthropic Claude API 密钥。

```text
secret = "sk-ant-abc123def456ghi789jkl012mno345pqr678"
```

### 37. [HIGH] Anthropic API Key

- **仓库**：`YahyaHammad/Venastine-Research-Harness`
- **文件**：`tests/test_policy_enforcement.py`（第 723 行）
- **密钥（已脱敏）**：`sk-ant...CCCC`
- **链接**：https://github.com/YahyaHammad/Venastine-Research-Harness/blob/main/tests/test_policy_enforcement.py
- **说明**：Anthropic Claude API 密钥。

```text
SECRET = "sk-ant-api03-CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"
```

### 38. [MEDIUM] Generic API key assignment

- **仓库**：`AnyRouterHQ/cli`
- **文件**：`src/spawn.rs`（第 2387 行）
- **密钥（已脱敏）**：`sk-ar-...alue`
- **链接**：https://github.com/AnyRouterHQ/cli/blob/main/src/spawn.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
api_key: "sk-ar-v1-secret-value",
```

### 39. [MEDIUM] Generic API key assignment

- **仓库**：`AnyRouterHQ/cli`
- **文件**：`src/spawn.rs`（第 2707 行）
- **密钥（已脱敏）**：`sk-ar-...0000`
- **链接**：https://github.com/AnyRouterHQ/cli/blob/main/src/spawn.rs
- **说明**：赋值给 API key 变量的疑似密钥。

```text
api_key: "sk-ar-v1-secret000000000000",
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

