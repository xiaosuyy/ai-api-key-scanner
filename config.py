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
SENSITIVE_PATTERNS = [
    {
        "name": "OpenAI Project API Key",
        "regex": r"sk-proj-[A-Za-z0-9_\-]{40,}",
        "confidence": "high",
        "description": "OpenAI project-scoped API key.",
    },
    {
        "name": "Anthropic API Key",
        "regex": r"sk-ant-[A-Za-z0-9_\-]{24,}",
        "confidence": "high",
        "description": "Anthropic Claude API key.",
    },
    {
        "name": "OpenAI API Key",
        "regex": r"sk-[A-Za-z0-9]{32,}",
        "confidence": "high",
        "description": "Legacy OpenAI-style API key.",
    },
    {
        "name": "Groq API Key",
        "regex": r"gsk_[A-Za-z0-9]{40,}",
        "confidence": "high",
        "description": "Groq Cloud API key.",
    },
    {
        "name": "Perplexity API Key",
        "regex": r"pplx-[A-Za-z0-9]{40,}",
        "confidence": "high",
        "description": "Perplexity API key.",
    },
    {
        "name": "Google Gemini / GCP API Key",
        "regex": r"AIza[0-9A-Za-z_\-]{35}",
        "confidence": "high",
        "description": "Google API key (Gemini, Vertex, Maps, ...).",
    },
    {
        "name": "Hugging Face Token",
        "regex": r"hf_[A-Za-z0-9]{30,}",
        "confidence": "high",
        "description": "Hugging Face access token.",
    },
    {
        "name": "Replicate Token",
        "regex": r"r8_[A-Za-z0-9]{30,}",
        "confidence": "medium",
        "description": "Replicate API token.",
    },
    {
        "name": "Generic API key assignment",
        "regex": (
            r"(?i)(?:api[_\-]?key|api[_\-]?secret|access[_\-]?token"
            r"|secret[_\-]?key|auth[_\-]?token)\s*[:=]\s*[\"']"
            r"([A-Za-z0-9_\-\.]{20,})[\"']"
        ),
        "confidence": "medium",
        "description": "A secret-looking value assigned to an API-key variable.",
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
