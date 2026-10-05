"""把扫描结果渲染成 Markdown / JSON 报告，并写入磁盘。"""

import json
import os
from collections import Counter
from datetime import datetime, timezone
from typing import Dict, List, Optional

import config
from secret_detector import Finding


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def build_summary(findings: List[Finding], repos_scanned: int, files_scanned: int) -> dict:
    by_confidence = Counter(f.confidence for f in findings)
    by_pattern = Counter(f.pattern_name for f in findings)
    by_repo = Counter(f.repo for f in findings)
    return {
        "generated_at": _now_iso(),
        "repos_scanned": repos_scanned,
        "files_scanned": files_scanned,
        "total_findings": len(findings),
        "by_confidence": dict(by_confidence),
        "by_pattern": dict(by_pattern),
        "by_repo": dict(by_repo),
    }


def generate_markdown(findings: List[Finding], summary: dict, scan_type: str) -> str:
    lines: List[str] = []
    lines.append("# 🔍 AI API Key 扫描报告")
    lines.append("")
    lines.append("| 项目 | 值 |")
    lines.append("| --- | --- |")
    lines.append("| 扫描类型 | `{}` |".format(scan_type))
    lines.append("| 生成时间 | {} |".format(summary["generated_at"]))
    lines.append("| 扫描仓库数 | {} |".format(summary["repos_scanned"]))
    lines.append("| 扫描文件数 | {} |".format(summary["files_scanned"]))
    lines.append("| 发现数量 | {} |".format(summary["total_findings"]))
    lines.append("")

    if not findings:
        lines.append("✅ 本次扫描**未发现**疑似泄露的 AI API 密钥。")
        return "\n".join(lines) + "\n"

    lines.append("## 置信度统计")
    lines.append("")
    lines.append("| 置信度 | 数量 |")
    lines.append("| --- | --- |")
    for conf in ("high", "medium", "low"):
        count = summary["by_confidence"].get(conf, 0)
        if count:
            lines.append("| {} | {} |".format(conf.upper(), count))
    lines.append("")

    lines.append("## 发现明细")
    lines.append("")
    for idx, f in enumerate(findings, start=1):
        lines.append("### {}. [{}] {}".format(idx, f.confidence.upper(), f.pattern_name))
        lines.append("")
        lines.append("- **仓库**：`{}`".format(f.repo))
        lines.append("- **文件**：`{}`（第 {} 行）".format(f.file_path, f.line_number))
        lines.append("- **密钥（已脱敏）**：`{}`".format(f.masked))
        if f.file_url:
            lines.append("- **链接**：{}".format(f.file_url))
        if f.description:
            lines.append("- **说明**：{}".format(f.description))
        lines.append("")
        lines.append("```text")
        lines.append(f.line_content.strip()[:400])
        lines.append("```")
        lines.append("")

    lines.append("## 处置建议")
    lines.append("")
    lines.append("1. **立即轮换密钥**：登录对应服务商控制台，删除泄露密钥并生成新密钥。")
    lines.append("2. **排查调用记录**：检查是否有异常用量或费用。")
    lines.append("3. **清理 Git 历史**：使用 BFG Repo-Cleaner 或 git-filter-repo。")
    lines.append("4. **改用环境变量 / Secret**：例如 `os.getenv(\"OPENAI_API_KEY\")`。")
    lines.append("")
    return "\n".join(lines) + "\n"


def generate_issue_body(findings: List[Finding], summary: dict) -> str:
    lines: List[str] = []
    lines.append("## 🔐 发现疑似泄露的 AI API 密钥")
    lines.append("")
    lines.append("本次扫描共发现 **{}** 条疑似泄露（仓库 {} 个，文件 {} 个）。".format(
        len(findings), summary["repos_scanned"], summary["files_scanned"]
    ))
    lines.append("")
    lines.append("| 置信度 | 仓库 | 文件 | 行 | 密钥（脱敏） |")
    lines.append("| --- | --- | --- | --- | --- |")
    for f in findings[: config.ISSUE_MAX_FINDINGS]:
        lines.append("| {} | `{}` | `{}` | {} | `{}` |".format(
            f.confidence.upper(), f.repo, f.file_path, f.line_number, f.masked
        ))
    if len(findings) > config.ISSUE_MAX_FINDINGS:
        lines.append("")
        lines.append("_其余 {} 条已省略，请查看完整报告。_".format(
            len(findings) - config.ISSUE_MAX_FINDINGS
        ))
    lines.append("")
    lines.append("> ⚠️ 请立即轮换泄露的密钥，并检查相关调用记录。")
    lines.append("")
    return "\n".join(lines) + "\n"


def generate_console_summary(summary: dict) -> str:
    lines = [
        "",
        "=" * 60,
        "扫描完成 / Scan summary",
        "=" * 60,
        "扫描类型 / Type      : {}".format(summary.get("scan_type", "-")),
        "扫描仓库 / Repos     : {}".format(summary["repos_scanned"]),
        "扫描文件 / Files     : {}".format(summary["files_scanned"]),
        "发现数量 / Findings  : {}".format(summary["total_findings"]),
    ]
    for conf in ("high", "medium", "low"):
        count = summary["by_confidence"].get(conf, 0)
        if count:
            lines.append("  - {:<6}: {}".format(conf, count))
    lines.append("=" * 60)
    lines.append("")
    return "\n".join(lines)


def _finding_dict(f: Finding) -> dict:
    return f.to_dict()


def write_reports(
    output_dir: str,
    scan_type: str,
    findings: List[Finding],
    summary: dict,
    issue_findings: Optional[List[Finding]] = None,
) -> Dict[str, str]:
    os.makedirs(output_dir, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    base = "scan_{}_{}".format(scan_type, stamp)

    md_path = os.path.join(output_dir, base + ".md")
    json_path = os.path.join(output_dir, base + ".json")
    latest_md = os.path.join(output_dir, "latest.md")
    latest_json = os.path.join(output_dir, "latest.json")
    issue_path = os.path.join(output_dir, "latest_issue.md")

    summary_with_type = dict(summary)
    summary_with_type["scan_type"] = scan_type

    markdown = generate_markdown(findings, summary, scan_type)
    payload = {
        "summary": summary_with_type,
        "findings": [_finding_dict(f) for f in findings],
    }

    for path in (md_path, latest_md):
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(markdown)
    for path in (json_path, latest_json):
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, ensure_ascii=False)

    issue_target = findings if issue_findings is None else issue_findings
    with open(issue_path, "w", encoding="utf-8") as fh:
        fh.write(generate_issue_body(issue_target, summary))

    return {
        "markdown": md_path,
        "json": json_path,
        "latest_markdown": latest_md,
        "issue": issue_path,
    }
