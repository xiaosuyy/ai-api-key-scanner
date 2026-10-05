#!/usr/bin/env bash
# 在 GitHub 上创建仓库并推送本项目。
#
# 用法:
#   GITHUB_TOKEN=ghp_xxx ./scripts/publish.sh <username> [repo-name]
#
# 需要一枚具备 repo 权限的 Personal Access Token。
set -euo pipefail

USERNAME="${1:-}"
REPO_NAME="${2:-ai-api-key-scanner}"
TOKEN="${GITHUB_TOKEN:-}"
DESCRIPTION="自动扫描 GitHub 仓库，发现泄露的 AI API 密钥"

if [[ -z "$USERNAME" || -z "$TOKEN" ]]; then
  echo "用法: GITHUB_TOKEN=ghp_xxx $0 <username> [repo-name]" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "[1/3] 校验 Token ..."
LOGIN="$(curl -fsS -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "User-Agent: ai-api-key-scanner" \
  https://api.github.com/user | sed -n 's/.*"login": *"\([^"]*\)".*/\1/p' | head -n1)"
echo "      已登录为: ${LOGIN:-未知}"

echo "[2/3] 创建仓库 ${USERNAME}/${REPO_NAME} ..."
curl -fsS -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "User-Agent: ai-api-key-scanner" \
  "https://api.github.com/user/repos" \
  -d "{\"name\":\"${REPO_NAME}\",\"description\":\"${DESCRIPTION}\",\"private\":false,\"has_issues\":true}" \
  >/dev/null && echo "      已创建。" || echo "      创建失败（可能已存在，将继续推送）。"

echo "[3/3] 推送到 GitHub ..."
REMOTE="https://github.com/${USERNAME}/${REPO_NAME}.git"
git remote remove origin 2>/dev/null || true
git remote add origin "$REMOTE"
git push "https://x-access-token:${TOKEN}@github.com/${USERNAME}/${REPO_NAME}.git" HEAD:main --force
git remote set-url origin "$REMOTE"

echo ""
echo "完成 ✅  https://github.com/${USERNAME}/${REPO_NAME}"
echo "下一步：在仓库 Settings → Secrets and variables → Actions 添加 GH_SCAN_TOKEN。"
