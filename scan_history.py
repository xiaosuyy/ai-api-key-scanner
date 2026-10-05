"""扫描历史记录：用于跨次扫描去重、避免重复创建 Issue。"""

import json
import os
from typing import List, Optional, Tuple

import config
from secret_detector import Finding


def _history_path(base_dir: Optional[str] = None) -> str:
    base = base_dir or config.HISTORY_DIR
    os.makedirs(base, exist_ok=True)
    return os.path.join(base, config.HISTORY_FILE)


def load_history(base_dir: Optional[str] = None) -> dict:
    path = _history_path(base_dir)
    if not os.path.exists(path):
        return {"scans": [], "known_fingerprints": []}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError):
        return {"scans": [], "known_fingerprints": []}
    data.setdefault("scans", [])
    data.setdefault("known_fingerprints", [])
    return data


def save_history(history: dict, base_dir: Optional[str] = None) -> str:
    path = _history_path(base_dir)
    history["scans"] = history.get("scans", [])[-config.MAX_HISTORY_ENTRIES :]
    history["known_fingerprints"] = sorted(set(history.get("known_fingerprints", [])))
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(history, fh, indent=2, ensure_ascii=False)
    return path


def record_scan(
    history: dict, scan_type: str, summary: dict, findings: List[Finding]
) -> Tuple[dict, List[Finding]]:
    """记录一次扫描并返回「本次新增」的发现。"""
    known = set(history.get("known_fingerprints", []))
    new_findings = [f for f in findings if f.fingerprint not in known]

    history.setdefault("scans", []).append(
        {
            "timestamp": summary["generated_at"],
            "scan_type": scan_type,
            "total_findings": summary["total_findings"],
            "new_findings": len(new_findings),
            "repos_scanned": summary["repos_scanned"],
        }
    )
    history["known_fingerprints"] = sorted(known | {f.fingerprint for f in findings})
    return history, new_findings
