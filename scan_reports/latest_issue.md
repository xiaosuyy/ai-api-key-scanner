## 🔐 发现疑似泄露的 AI API 密钥

本次扫描共发现 **8** 条疑似泄露（仓库 46 个，文件 8884 个）。

| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |
| --- | --- | --- | --- | --- |
| MEDIUM | `ortus-boxlang/bx-ai` | `src/test/java/ortus/boxlang/ai/providers/BedrockServiceTest.java` | 1915 | `sk-som...-key` |
| MEDIUM | `ortus-boxlang/bx-ai` | `src/test/java/ortus/boxlang/ai/providers/BedrockServiceTest.java` | 2593 | `AKIAMO...MODU` |
| MEDIUM | `ortus-boxlang/bx-ai` | `src/test/java/ortus/boxlang/ai/util/AwsCredentialProviderTest.java` | 215 | `AKIADE...LT12` |
| MEDIUM | `ortus-boxlang/bx-ai` | `src/test/java/ortus/boxlang/ai/util/AwsCredentialProviderTest.java` | 241 | `AKIADE...LT12` |
| MEDIUM | `memorycrystal/memorycrystal` | `plugin/__tests__/env-propagation.test.js` | 71 | `local-...oken` |
| MEDIUM | `memorycrystal/memorycrystal` | `plugin/__tests__/env-propagation.test.js` | 141 | `local-...oken` |
| MEDIUM | `memorycrystal/memorycrystal` | `plugin/compaction/crystal-summarizer.test.js` | 36 | `ambien...used` |
| HIGH | `hybrys-dev/Bit` | `crates/bit-core/src/recorder.rs` | 949 | `sk-ant...CRET` |

> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。

