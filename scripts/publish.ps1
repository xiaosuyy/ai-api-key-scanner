<#
.SYNOPSIS
    在 GitHub 上创建仓库并推送本项目。

.DESCRIPTION
    通过 GitHub REST API 创建仓库，然后把当前仓库推送到远端。
    需要一枚具备 repo 权限的 Personal Access Token。

.EXAMPLE
    ./scripts/publish.ps1 -Username octocat -Token ghp_xxxxxxxxxxxx

.EXAMPLE
    ./scripts/publish.ps1 -Username octocat -Token ghp_xxxxxxxxxxxx -Private
#>
param(
    [Parameter(Mandatory = $true)][string]$Username,
    [Parameter(Mandatory = $true)][string]$Token,
    [string]$RepoName = "ai-api-key-scanner",
    [string]$Description = "自动扫描 GitHub 仓库，发现泄露的 AI API 密钥",
    [switch]$Private
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$headers = @{
    Authorization = "Bearer $Token"
    Accept        = "application/vnd.github+json"
    "User-Agent"  = "ai-api-key-scanner"
}

$body = @{
    name       = $RepoName
    description = $Description
    private    = [bool]$Private
    has_issues = $true
} | ConvertTo-Json

Write-Host "[1/3] 校验 Token ..."
$me = Invoke-RestMethod -Method Get -Uri "https://api.github.com/user" -Headers $headers
Write-Host "      已登录为：$($me.login)"

Write-Host "[2/3] 创建仓库 $Username/$RepoName ..."
try {
    Invoke-RestMethod -Method Post -Uri "https://api.github.com/user/repos" `
        -Headers $headers -Body $body -ContentType "application/json" | Out-Null
    Write-Host "      已创建。"
}
catch {
    Write-Host "      创建失败（可能已存在，将继续推送）：$($_.Exception.Message)"
}

Write-Host "[3/3] 推送到 GitHub ..."
$remote = "https://github.com/$Username/$RepoName.git"
git remote remove origin 2>$null
git remote add origin $remote
# 使用一次性的带 token 地址推送，推送后立即把远端恢复为干净地址，避免 token 落盘。
$pushUrl = "https://x-access-token:$Token@github.com/$Username/$RepoName.git"
try {
    git push $pushUrl "HEAD:main" --force
}
finally {
    git remote set-url origin $remote
}

Write-Host ""
Write-Host "完成 ✅  https://github.com/$Username/$RepoName"
Write-Host "下一步：在仓库 Settings → Secrets and variables → Actions 添加 GH_SCAN_TOKEN。"
