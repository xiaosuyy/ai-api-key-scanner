#!/usr/bin/env python3
"""AI API Key Scanner 命令行入口。

支持四种扫描模式：
  --auto                 自动搜索 AI 相关仓库
  --user <user>          扫描指定用户的仓库
  --org  <org>           扫描指定组织的仓库
  --repo <owner/repo>    扫描单个仓库

示例：
  python scan_github.py --auto --max-repos 10
  python scan_github.py --repo openai/openai-python
"""

import argparse
import os
import sys
from typing import List, Tuple

import config
from github_scanner import GitHubClient, RepoScanner
from report_generator import (
    build_summary,
    generate_console_summary,
    write_reports,
)
import scan_history


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="扫描 GitHub 仓库中泄露的 AI API 密钥。",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--auto", action="store_true", help="自动搜索 AI 项目")
    mode.add_argument("--user", metavar="USER", help="扫描指定用户")
    mode.add_argument("--org", metavar="ORG", help="扫描指定组织")
    mode.add_argument("--repo", metavar="OWNER/REPO", help="扫描单个仓库")

    parser.add_argument(
        "--max-repos",
        type=int,
        default=config.DEFAULT_MAX_REPOS,
        help="最多扫描的仓库数（默认 %(default)s）",
    )
    parser.add_argument(
        "--output",
        default=config.OUTPUT_DIR,
        help="报告输出目录（默认 %(default)s）",
    )
    parser.add_argument(
        "--history-dir",
        default=config.HISTORY_DIR,
        help="历史记录目录（默认 %(default)s）",
    )
    parser.add_argument(
        "--token",
        default=None,
        help="GitHub Token，默认读取环境变量 {}".format(config.GITHUB_TOKEN_ENV),
    )
    parser.add_argument(
        "--no-history",
        action="store_true",
        help="不读取 / 写入历史记录（全部发现都视为新增）",
    )
    parser.add_argument(
        "--fail-on-findings",
        action="store_true",
        help="发现密钥时以非零状态码退出",
    )
    return parser.parse_args(argv)


def resolve_repos(client: GitHubClient, args: argparse.Namespace) -> Tuple[List[dict], str]:
    if args.auto:
        seen = {}
        per_query = max(1, args.max_repos // len(config.AI_SEARCH_QUERIES) + 1)
        for query in config.AI_SEARCH_QUERIES:
            for repo in client.search_repositories(query, per_query):
                full_name = repo.get("full_name")
                if full_name:
                    seen[full_name] = repo
        return list(seen.values())[: args.max_repos], "auto"

    if args.user:
        return client.list_user_repos(args.user, args.max_repos), "user"

    if args.org:
        return client.list_org_repos(args.org, args.max_repos), "org"

    repo = client.get_repo(args.repo)
    return ([repo] if repo else []), "repo"


def main(argv=None) -> int:
    args = parse_args(argv)
    token = args.token or os.getenv(config.GITHUB_TOKEN_ENV)
    if not token:
        print(
            "错误：需要 GitHub Token。请设置环境变量 {} 或使用 --token。".format(
                config.GITHUB_TOKEN_ENV
            ),
            file=sys.stderr,
        )
        return 2

    client = GitHubClient(token)
    scanner = RepoScanner(client)

    repos, scan_type = resolve_repos(client, args)
    if not repos:
        print("未找到可扫描的仓库，请检查目标参数。", file=sys.stderr)
        return 1

    print("开始扫描 {} 个仓库（模式：{}）...".format(len(repos), scan_type))

    all_findings = []
    files_scanned = 0
    for repo in repos:
        full_name = repo.get("full_name", "?")
        try:
            findings, count = scanner.scan_repo(repo)
        except Exception as exc:  # noqa: BLE001 - 单个仓库失败不应中断整体扫描
            print("  ! {} 扫描失败：{}".format(full_name, exc))
            continue
        files_scanned += count
        all_findings.extend(findings)
        print("  - {}：{} 条发现（{} 个文件）".format(full_name, len(findings), count))

    summary = build_summary(all_findings, len(repos), files_scanned)
    summary["scan_type"] = scan_type

    if args.no_history:
        new_findings = all_findings
    else:
        history = scan_history.load_history(args.history_dir)
        history, new_findings = scan_history.record_scan(
            history, scan_type, summary, all_findings
        )
        scan_history.save_history(history, args.history_dir)

    # 只有高/中置信度的新增发现才值得创建 Issue；低置信度仅保留在报告中。
    issue_findings = [
        f for f in new_findings if f.confidence in config.ISSUE_CONFIDENCES
    ]

    paths = write_reports(
        args.output, scan_type, all_findings, summary, issue_findings=issue_findings
    )

    print(generate_console_summary(summary))
    print("Markdown 报告：{}".format(paths["markdown"]))
    print("JSON 报告　　：{}".format(paths["json"]))
    print("本次新增发现：{}（其中需告警 {} 条）".format(
        len(new_findings), len(issue_findings)
    ))

    # 在 GitHub Actions 中输出结果，供后续步骤创建 Issue / 上传 Artifact。
    github_output = os.getenv("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as fh:
            fh.write("total_findings={}\n".format(summary["total_findings"]))
            fh.write("new_findings={}\n".format(len(new_findings)))
            fh.write("issue_count={}\n".format(len(issue_findings)))
            fh.write("report_path={}\n".format(paths["markdown"]))
            fh.write("issue_path={}\n".format(paths["issue"]))

    if args.fail_on_findings and all_findings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
