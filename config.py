"""Central configuration for the AI API Key Scanner.

Everything tunable lives here so the scanner can run with zero configuration
on GitHub Actions. Fork the repository, add a token, and it just works.
"""

import os

# --------------------------------------------------------------------------- #
# GitHub
# --------------------------------------------------------------------------- #
GITHUB_API_URL = "https://api.github.com"
GITHUB_RAW_URL = "https://raw.githubusercontent.com"
GITHUB_TOKEN_ENV = "GH_SCAN_TOKEN"

# --------------------------------------------------------------------------- #
# General scan limits
# --------------------------------------------------------------------------- #
DEFAULT_MAX_REPOS = 10
PER_PAGE = 100
REQUEST_TIMEOUT = 30
MAX_FILE_SIZE_BYTES = 1_000_000      # skip files larger than ~1 MB
MAX_FILES_PER_REPO = 300             # stop fetching after this many files

# Repository search queries used by the "auto" mode to discover AI projects.
AI_SEARCH_QUERIES = [
    "topic:openai",
    "topic:llm",
    "topic:artificial-intelligence",
    "topic:chatgpt",
    "openai api in:readme",
    "anthropic claude in:readme",
]

# --------------------------------------------------------------------------- #
# Detection patterns
# --------------------------------------------------------------------------- #
# Each entry: name, regex, base confidence (high / medium / low), description.
# Patterns with a capturing group use group(1) as the secret value.
# 顺序很重要：越靠前的规则越先匹配，命中后同一行的相同值会被去重。
# 因此「有独特前缀」的规则放在通用 sk- 之前，上下文规则也放在通用 sk- 之前。
SENSITIVE_PATTERNS = [
    # ------------------------------------------------------------------ #
    # OpenAI 系列
    # ------------------------------------------------------------------ #
    {
        "name": "OpenAI Project API Key",
        "regex": r"sk-proj-[A-Za-z0-9_\-]{40,}",
        "confidence": "high",
        "description": "OpenAI 项目级 API 密钥。",
    },
    {
        "name": "OpenAI Service Account Key",
        "regex": r"sk-svcacct-[A-Za-z0-9_\-]{40,}",
        "confidence": "high",
        "description": "OpenAI 服务账号密钥。",
    },
    {
        "name": "OpenAI Admin Key",
        "regex": r"sk-admin-[A-Za-z0-9_\-]{40,}",
        "confidence": "high",
        "description": "OpenAI 管理员密钥。",
    },
    {
        "name": "Anthropic API Key",
        "regex": r"sk-ant-[A-Za-z0-9_\-]{24,}",
        "confidence": "high",
        "description": "Anthropic Claude API 密钥。",
    },
    # ------------------------------------------------------------------ #
    # 其他有独特前缀的服务商
    # ------------------------------------------------------------------ #
    {
        "name": "OpenRouter API Key",
        "regex": r"sk-or-v1-[A-Za-z0-9]{32,}",
        "confidence": "high",
        "description": "OpenRouter API 密钥。",
    },
    {
        "name": "xAI (Grok) API Key",
        "regex": r"xai-[A-Za-z0-9]{40,}",
        "confidence": "high",
        "description": "xAI Grok API 密钥。",
    },
    {
        "name": "Cerebras API Key",
        "regex": r"csk-[A-Za-z0-9]{40,}",
        "confidence": "high",
        "description": "Cerebras Cloud API 密钥。",
    },
    {
        "name": "NVIDIA NIM API Key",
        "regex": r"nvapi-[A-Za-z0-9_\-]{40,}",
        "confidence": "high",
        "description": "NVIDIA NIM / build.nvidia.com API 密钥。",
    },
    {
        "name": "Voyage AI API Key",
        "regex": r"(?<![A-Za-z0-9_])pa-[A-Za-z0-9_\-]{40,}",
        "confidence": "medium",
        "description": "Voyage AI 嵌入 API 密钥。",
    },
    {
        "name": "Pinecone API Key",
        "regex": r"(?<![A-Za-z0-9_])pcsk_[A-Za-z0-9_\-]{32,}",
        "confidence": "high",
        "description": "Pinecone 向量数据库 API 密钥。",
    },
    {
        "name": "LangSmith API Key",
        "regex": r"(?<![A-Za-z0-9_])lsv2_[A-Za-z0-9_]{30,}",
        "confidence": "high",
        "description": "LangSmith API 密钥。",
    },
    {
        "name": "ElevenLabs API Key",
        "regex": r"(?<![A-Za-z0-9_])sk_[a-f0-9]{32,}",
        "confidence": "high",
        "description": "ElevenLabs 语音 API 密钥。",
    },
    {
        "name": "Groq API Key",
        "regex": r"(?<![A-Za-z0-9_])gsk_[A-Za-z0-9]{40,}",
        "confidence": "high",
        "description": "Groq Cloud API 密钥。",
    },
    {
        "name": "Perplexity API Key",
        "regex": r"pplx-[A-Za-z0-9]{40,}",
        "confidence": "high",
        "description": "Perplexity API 密钥。",
    },
    {
        "name": "Google Gemini / GCP API Key",
        "regex": r"AIza[0-9A-Za-z_\-]{35}",
        "confidence": "high",
        "description": "Google API 密钥（Gemini、Vertex、Maps 等）。",
    },
    {
        "name": "Google OAuth Client Secret",
        "regex": r"GOCSPX-[A-Za-z0-9_\-]{20,}",
        "confidence": "medium",
        "description": "Google OAuth 客户端密钥。",
    },
    {
        "name": "Hugging Face Token",
        "regex": r"(?<![A-Za-z0-9_])hf_[A-Za-z0-9]{30,}",
        "confidence": "high",
        "description": "Hugging Face 访问令牌。",
    },
    {
        "name": "Replicate Token",
        "regex": r"(?<![A-Za-z0-9_])r8_[A-Za-z0-9]{30,}",
        "confidence": "medium",
        "description": "Replicate API 令牌。",
    },
    # ------------------------------------------------------------------ #
    # AI 场景常见凭证
    # ------------------------------------------------------------------ #
    {
        "name": "GitHub Personal Access Token",
        "regex": r"(?:ghp_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{50,})",
        "confidence": "high",
        "description": "GitHub PAT（Copilot / GitHub Models 等场景常用）。",
    },
    {
        "name": "AWS Access Key ID",
        "regex": r"AKIA[0-9A-Z]{16}",
        "confidence": "medium",
        "description": "AWS 访问密钥 ID（Bedrock / SageMaker 等场景）。",
    },
    # ------------------------------------------------------------------ #
    # 上下文规则：密钥本身无固定前缀，依据变量名 / 上下文识别。
    # 必须放在通用 sk- 规则之前，否则会被通用规则先命中。
    # ------------------------------------------------------------------ #
    {
        "name": "DeepSeek API Key",
        "regex": r"(?i)deepseek[^\n]{0,40}?(sk-[A-Za-z0-9]{20,})",
        "confidence": "high",
        "description": "DeepSeek API 密钥（依据上下文变量名识别）。",
    },
    {
        "name": "Moonshot (Kimi) API Key",
        "regex": r"(?i)(?:moonshot|kimi)[^\n]{0,40}?(sk-[A-Za-z0-9]{20,})",
        "confidence": "high",
        "description": "Moonshot / Kimi API 密钥（依据上下文识别）。",
    },
    {
        "name": "Alibaba DashScope (Qwen) API Key",
        "regex": r"(?i)(?:dashscope|qwen|aliyun|alibaba)[^\n]{0,40}?(sk-[A-Za-z0-9]{20,})",
        "confidence": "high",
        "description": "阿里云百炼 / 通义千问 API 密钥（依据上下文识别）。",
    },
    {
        "name": "Zhipu GLM API Key",
        "regex": r"(?i)(?:zhipu|bigmodel|glm)[^\n]{0,40}?([A-Za-z0-9]{16,}\.[A-Za-z0-9]{16,})",
        "confidence": "medium",
        "description": "智谱 GLM API 密钥（形如 id.secret）。",
    },
    # ------------------------------------------------------------------ #
    # 通用兜底
    # ------------------------------------------------------------------ #
    {
        "name": "OpenAI API Key",
        "regex": r"(?<![A-Za-z0-9])sk-[A-Za-z0-9]{32,}",
        "confidence": "high",
        "description": "OpenAI 风格 sk- 密钥（也覆盖 DeepSeek、Moonshot 等同类前缀）。",
    },
    {
        "name": "Generic API key assignment",
        "regex": (
            r"(?i)(?:api[_\-]?key|api[_\-]?secret|access[_\-]?token"
            r"|secret[_\-]?key|auth[_\-]?token)\s*[:=]\s*[\"']"
            r"([A-Za-z0-9_\-\.]{20,})[\"']"
        ),
        "confidence": "medium",
        "description": "赋值给 API key 变量的疑似密钥。",
    },
]

# Lower-cased substrings that almost always mean "placeholder", not a live key.
PLACEHOLDER_TOKENS = [
    "your",
    "example",
    "sample",
    "dummy",
    "placeholder",
    "changeme",
    "change_me",
    "replace",
    "redacted",
    "xxx",
    "zzz",
    "foobar",
    "abcdef",
    "1234567890",
    "api_key_here",
    "insert",
    "notreal",
    "fake",
    "todo",
]

# Lower-cased substrings in the surrounding line that de-prioritise a match.
EXAMPLE_CONTEXT_TOKENS = [
    "example",
    "sample",
    "dummy",
    "placeholder",
    "your_",
    "your-",
    "fake",
    "mock",
    "redacted",
    "documentation",
    "readme",
]

# File extensions worth downloading and scanning.
TEXT_EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".go", ".rb", ".php",
    ".cs", ".c", ".cpp", ".h", ".hpp", ".rs", ".kt", ".swift", ".scala",
    ".sh", ".bash", ".zsh", ".ps1", ".bat", ".cmd", ".pl", ".r",
    ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".env",
    ".properties", ".xml", ".md", ".txt", ".rst", ".sql", ".html", ".htm",
    ".css", ".scss", ".vue", ".svelte", ".dockerfile", "",
}

# File names worth scanning regardless of extension.
TEXT_FILENAMES = {
    ".env", ".env.local", ".env.example", ".env.sample",
    "dockerfile", "makefile", "config", "credentials",
}

# Path fragments that are pure noise for this scanner.
SKIP_PATH_FRAGMENTS = [
    "/node_modules/",
    "/vendor/",
    "/dist/",
    "/build/",
    "/.git/",
    "/test/fixtures/",
    "/__snapshots__/",
]

# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #
DEFAULT_OUTPUT_DIR = "scan_reports"
HISTORY_DIR = "scan_history"
HISTORY_FILE = "history.json"
MAX_HISTORY_ENTRIES = 100
ISSUE_MAX_FINDINGS = 25

SEVERITY_ORDER = {"high": 0, "medium": 1, "low": 2}

# Convenience: allow overriding the output dir from the environment.
OUTPUT_DIR = os.getenv("SCAN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
