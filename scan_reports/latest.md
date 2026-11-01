# 🔍 AI API Key 扫描报告

| 项目 | 值 |
| --- | --- |
| 扫描类型 | `auto` |
| 生成时间 | 2026-11-01 08:33:29 UTC |
| 扫描仓库数 | 20 |
| 扫描文件数 | 2834 |
| 发现数量 | 33 |

## 置信度统计

| 置信度 | 数量 |
| --- | --- |
| HIGH | 30 |
| MEDIUM | 3 |

## 发现明细

### 1. [MEDIUM] Generic API key assignment

- **仓库**：`A1exZabr/apiunicon`
- **文件**：`test/catalog/session.test.ts`（第 38 行）
- **密钥（已脱敏）**：`catalo...cret`
- **链接**：https://github.com/A1exZabr/apiunicon/blob/main/test/catalog/session.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
session.saveTokens({ accessToken: "catalog-access-secret", refreshToken: "catalog-refresh-secret" }, ONLINE);
```

### 2. [MEDIUM] Generic API key assignment

- **仓库**：`A1exZabr/apiunicon`
- **文件**：`test/catalog/session.test.ts`（第 43 行）
- **密钥（已脱敏）**：`catalo...cret`
- **链接**：https://github.com/A1exZabr/apiunicon/blob/main/test/catalog/session.test.ts
- **说明**：赋值给 API key 变量的疑似密钥。

```text
accessToken: "catalog-access-secret",
```

### 3. [MEDIUM] Generic API key assignment

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/config/validator_test.go`（第 166 行）
- **密钥（已脱敏）**：`sk-or-...f456`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/config/validator_test.go
- **说明**：赋值给 API key 变量的疑似密钥。

```text
apiKey:    "sk-or-v1-abc123def456",
```

### 4. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 620 行）
- **密钥（已脱敏）**：`AIzaSy...YyIs`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs''',
```

### 5. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 621 行）
- **密钥（已脱敏）**：`AIzaSy...agEM`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM''',
```

### 6. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 622 行）
- **密钥（已脱敏）**：`AIzaSy...DrlU`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU''',
```

### 7. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 623 行）
- **密钥（已脱敏）**：`AIzaSy...hrh0`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0''',
```

### 8. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 624 行）
- **密钥（已脱敏）**：`AIzayD...bX4A`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A''',
```

### 9. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 625 行）
- **密钥（已脱敏）**：`AIzaSy...wX7c`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c''',
```

### 10. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 626 行）
- **密钥（已脱敏）**：`AIzaSy...mLd4`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4''',
```

### 11. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 627 行）
- **密钥（已脱敏）**：`AIzaSy...DQgY`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQgY''',
```

### 12. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 628 行）
- **密钥（已脱敏）**：`AIzaSy...4wtM`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyA5_iVawFQ8ABuTZNUdcwERLJv_a_p4wtM''',
```

### 13. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 629 行）
- **密钥（已脱敏）**：`AIzaSy...P5sQ`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyA4UrcGxgwQFTfaI3no3t7Lt1sjmdnP5sQ''',
```

### 14. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 630 行）
- **密钥（已脱敏）**：`AIzaSy...cS7g`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyDSb51JiIcB6OJpwwMicseKRhhrOq1cS7g''',
```

### 15. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 631 行）
- **密钥（已脱敏）**：`AIzaSy...vvuU`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyBF2RrAIm4a0mO64EShQfqfd2AFnzAvvuU''',
```

### 16. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 632 行）
- **密钥（已脱敏）**：`AIzaSy...NXsw`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyBcE-OOIbhjyR83gm4r2MFCu4MJmprNXsw''',
```

### 17. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 633 行）
- **密钥（已脱敏）**：`AIzaSy...FmqE`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyB8qGxt4ec15vitgn44duC5ucxaOi4FmqE''',
```

### 18. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules/gitleaks.toml`（第 634 行）
- **密钥（已脱敏）**：`AIzaSy...0nvY`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules/gitleaks.toml
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
'''AIzaSyA8vmApnrHNFE0bApF4hoZ11srVL_n0nvY''',
```

### 19. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...YyIs`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 20. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...agEM`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 21. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...DrlU`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 22. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...hrh0`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 23. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzayD...bX4A`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 24. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...wX7c`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 25. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...mLd4`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 26. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...DQgY`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 27. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...4wtM`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 28. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...P5sQ`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 29. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...cS7g`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 30. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...vvuU`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 31. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...NXsw`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 32. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...FmqE`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

### 33. [HIGH] Google Gemini / GCP API Key

- **仓库**：`belingud/gptcomet`
- **文件**：`internal/secretscan/rules_gen.go`（第 454 行）
- **密钥（已脱敏）**：`AIzaSy...0nvY`
- **链接**：https://github.com/belingud/gptcomet/blob/master/internal/secretscan/rules_gen.go
- **说明**：Google API 密钥（Gemini、Vertex、Maps 等）。

```text
Regexes: []string{`AIzaSyabcdefghijklmnopqrstuvwxyz1234567`, `AIzaSyAnLA7NfeLquW1tJFpx_eQCxoX-oo6YyIs`, `AIzaSyCkEhVjf3pduRDt6d1yKOMitrUEke8agEM`, `AIzaSyDMAScliyLx7F0NPDEJi1QmyCgHIAODrlU`, `AIzaSyD3asb-2pEZVqMkmL6M9N6nHZRR_znhrh0`, `AIzayDNSXIbFmlXbIE6mCzDLQAqITYefhixbX4A`, `AIzaSyAdOS2zB6NCsk1pCdZ4-P6GBdi_UUPwX7c`, `AIzaSyASWm6HmTMdYWpgMnjRBjxcQ9CKctWmLd4`, `AIzaSyANUvH9H9BsUccjsu2pCmEkOPjjaXeDQ
```

## 处置建议

1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。
2. **排查调用记录**：检查是否有异常用量或费用。
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。
4. **改用环境变量 / Secret**：例如 `os.getenv("OPENAI_API_KEY")`。

