# 🔍 AI API Key Scanner

**自动扫描 GitHub 仓库，发现泄露的 AI API 密钥**

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Actions](https://img.shields.io/badge/automation-GitHub%20Actions-2088FF.svg)](https://github.com/features/actions)

🚀 **完全基于 GitHub Actions，无需本地运行** | 💰 **公开仓库完全免费**

---

## 📖 简介

一个自动化安全扫描工具，用于发现 GitHub 仓库中泄露的 AI API 密钥
（OpenAI、Anthropic、Google Gemini、Hugging Face、Groq、Perplexity 等）。

### 核心特性

- ✅ **零配置运行** — Fork 后只需添加一个 Token
- ✅ **全自动化** — 每天定时自动扫描
- ✅ **智能检测** — 自动过滤示例代码与占位符，降低误报
- ✅ **详细报告** — 报告提交到仓库永久保存，同时上传 Artifacts 保留 90 天
- ✅ **即时告警** — 发现新问题时自动创建 Issue，并自动去重
- ✅ **灵活模式** — 支持 auto / user / org / repo 四种扫描模式
- ✅ **完全免费** — 公开仓库无限使用

---

## 🚀 快速开始

### 1. Fork / 创建仓库

将本仓库 Fork 或复制到你自己的账号下。

### 2. 创建 GitHub Token

1. 访问 <https://github.com/settings/tokens>
2. 点击 **Generate new token (classic)**
3. 配置：
   - Note：`AI Scanner Token`
   - Expiration：`90 days` 或更长
   - Scopes：✅ `public_repo`（必需）、✅ `read:org`（可选）
4. 生成并复制 Token（格式：`ghp_xxxxxxxxxxxx`）

### 3. 添加 Token 到仓库

1. 进入你仓库的 `Settings` → `Secrets and variables` → `Actions`
2. 点击 **New repository secret**
3. Name：`GH_SCAN_TOKEN`（必须大小写一致）
4. Value：粘贴你的 Token
5. 点击 **Add secret**

### 4. 启动扫描

**手动触发（推荐首次使用）**

1. 进入 `Actions` 页面
2. 选择 **AI API Key Scanner - Manual Scan**
3. 点击 **Run workflow**
4. 配置参数：
   - `scan_type`：`auto`（自动搜索 AI 项目）
   - `max_repos`：`10`（首次建议少量测试）
5. 点击 **Run workflow** 开始扫描

**自动运行**：配置完成后，工作流将在每天 UTC 02:00（北京时间 10:00）自动运行。

---

## 📊 查看结果

| 方式 | 位置 | 说明 |
| --- | --- | --- |
| 仓库报告 | `scan_reports/` | 扫描完成后自动提交，永久保存 |
| 运行日志 | Actions 页面 | 查看每次扫描的状态与摘要 |
| Artifacts | 运行详情页底部 | 报告副本，保留 90 天 |
| 自动 Issue | Issues 页面 | 发现问题时自动创建，带 `security` 标签 |

---

## 🎯 功能特性

### 智能检测

- 支持多种 AI 密钥格式：
  - OpenAI：`sk-...`、`sk-proj-...`、`sk-svcacct-...`、`sk-admin-...`
  - Anthropic：`sk-ant-...`
  - Google：`AIza...`、`GOCSPX-...`
  - Hugging Face：`hf_...`
  - Groq：`gsk_...` / Perplexity：`pplx-...` / Replicate：`r8_...`
  - OpenRouter：`sk-or-v1-...` / xAI (Grok)：`xai-...` / Cerebras：`csk-...`
  - NVIDIA NIM：`nvapi-...` / Voyage：`pa-...` / Pinecone：`pcsk_...`
  - LangSmith：`lsv2_...` / ElevenLabs：`sk_...`
  - 上下文识别：DeepSeek、Moonshot (Kimi)、阿里云百炼 (Qwen)、智谱 GLM
  - AI 场景常见凭证：GitHub PAT (`ghp_...` / `github_pat_...`)、AWS Access Key (`AKIA...`)
  - 通用密钥赋值（`api_key = "..."`）
- 自动过滤示例代码、占位符和低熵字符串
- 置信度评分（high / medium / low）

### 详细报告

- 包含仓库地址、文件路径、行号、代码片段
- 密钥脱敏展示，仅显示首尾字符
- 置信度统计与处置建议
- 报告保存于 `scan_reports/`，提交到仓库永久保存

### 自动告警与去重

- 发现问题自动创建 Issue
- 基于密钥指纹的历史记录，避免重复告警
- 仅对「本次新增」的发现创建 Issue

---

## 🛠️ 工作流说明

| 工作流 | 触发方式 | 适用场景 |
| --- | --- | --- |
| Manual Scan ⭐ | 仅手动 | 首次测试、按需扫描 |
| Auto Scan | 每天 UTC 02:00 或手动 | 日常自动监控 |
| Scheduled Scan | 每天 UTC 02:00 或手动 | 企业级定期审计，含统计摘要 |

---

## ⚙️ 自定义配置

### 修改扫描时间

编辑 `.github/workflows/scheduled-scan.yml`：

```yaml
on:
  schedule:
    - cron: '0 2 * * *'       # 每天 02:00 UTC（北京时间 10:00）
    # - cron: '0 */12 * * *'  # 每 12 小时
    # - cron: '0 2 * * 1'     # 每周一
```

> **时区说明**：GitHub Actions 使用 UTC，北京时间 = UTC + 8 小时。

### 修改扫描数量

```bash
python scan_github.py --auto --max-repos 100
```

### 添加自定义检测规则

编辑 `config.py` 中的 `SENSITIVE_PATTERNS`：

```python
SENSITIVE_PATTERNS.append({
    "name": "My Provider Key",
    "regex": r"myprov-[A-Za-z0-9]{32,}",
    "confidence": "high",
    "description": "自定义服务商密钥。",
})
```

### 本地运行（可选）

```bash
pip install -r requirements.txt
export GH_SCAN_TOKEN=ghp_xxxxxxxxxxxx

python scan_github.py --auto --max-repos 10
python scan_github.py --user octocat
python scan_github.py --org my-org --max-repos 50
python scan_github.py --repo owner/repo
```

---

## ❓ 常见问题

**Q：工作流没有自动运行？**
- 检查 Actions 是否已启用
- 手动触发一次以完成初始化
- 确认 Cron 时间设置正确

**Q：提示 "需要 GitHub Token"？**
- 确认 Secret 名称为 `GH_SCAN_TOKEN`（大小写一致）
- 检查 Token 是否过期
- 验证 Token 具备 `public_repo` 权限

**Q：遇到 API 速率限制？**
- 减少 `--max-repos` 参数
- 增大扫描间隔
- 等待 1 小时后重试

**Q：如何停止自动扫描？**
- Actions 页面 → 选择工作流 → "..." → "Disable workflow"

---

## 🛡️ 发现泄露密钥后的处理

1. **轮换密钥**：登录服务商控制台，删除泄露密钥并生成新密钥
2. **检查日志**：查看 API 调用记录，确认是否存在异常使用
3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo
4. **改进代码实践**：

```python
# ✅ 推荐：使用环境变量
import os
api_key = os.getenv("OPENAI_API_KEY")

# ❌ 错误：硬编码密钥
api_key = "sk-proj-xxxxxxxxxxxx"
```

并确保 `.gitignore` 包含：

```
.env
.env.local
config.json
secrets.json
*.key
*.pem
```

---

## ⚠️ 免责声明

- 本工具仅用于安全研究与合法的安全审计
- 使用者需对自己的行为负责
- 请遵守相关法律法规与 GitHub 使用条款
- 工具可能存在误报或漏报，建议人工复核

---

## 📄 许可证

本项目采用 MIT 许可证 — 详见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

本项目的功能设计参考了开源项目
[gaocaipeng/InCloudGitHub](https://github.com/gaocaipeng/InCloudGitHub)，
代码为本仓库独立实现。

---

### 🛡️ 让你的代码更安全！

Made with ❤️ for Security
