"""GitHub REST API 客户端 + 仓库扫描器。

只依赖 ``requests``，其余全部使用标准库，方便在 GitHub Actions 上零配置运行。
"""

import time
from typing import Dict, List, Optional, Tuple

import requests

import config
from secret_detector import Finding, SecretDetector


class GitHubClient:
    """对 GitHub REST API 的最小封装，内置限流退避。"""

    def __init__(self, token: Optional[str] = None, session=None):
        self.token = token
        self.session = session or requests.Session()
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "ai-api-key-scanner",
        }
        if token:
            headers["Authorization"] = "Bearer {}".format(token)
        self.session.headers.update(headers)

    # -- 底层请求 ---------------------------------------------------------- #
    def _request(self, method: str, path: str, **kwargs):
        url = path if path.startswith("http") else "{}{}".format(
            config.GITHUB_API_URL, path
        )
        response = None
        for _ in range(3):
            response = self.session.request(
                method, url, timeout=config.REQUEST_TIMEOUT, **kwargs
            )
            text = (response.text or "").lower()
            if response.status_code in (403, 429) and "rate limit" in text:
                reset = response.headers.get("X-RateLimit-Reset")
                try:
                    wait = max(1, int(reset) - int(time.time())) if reset else 30
                except (TypeError, ValueError):
                    wait = 30
                time.sleep(min(wait, 60))
                continue
            return response
        return response

    def _get_json(self, path: str, params: Optional[dict] = None):
        response = self._request("GET", path, params=params)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()

    # -- 仓库发现 ---------------------------------------------------------- #
    def search_repositories(self, query: str, max_results: int) -> List[dict]:
        results: List[dict] = []
        page = 1
        while len(results) < max_results:
            per_page = min(config.PER_PAGE, max_results - len(results))
            data = self._get_json(
                "/search/repositories",
                params={
                    "q": query,
                    "per_page": per_page,
                    "page": page,
                    "sort": "updated",
                },
            )
            if not data:
                break
            items = data.get("items", [])
            if not items:
                break
            results.extend(items)
            if len(items) < per_page:
                break
            page += 1
        return results[:max_results]

    def _paginate(self, path: str, max_results: int) -> List[dict]:
        results: List[dict] = []
        page = 1
        while len(results) < max_results:
            per_page = min(config.PER_PAGE, max_results - len(results))
            data = self._get_json(
                path,
                params={"per_page": per_page, "page": page, "sort": "updated"},
            )
            if not data:
                break
            results.extend(data)
            if len(data) < per_page:
                break
            page += 1
        return results[:max_results]

    def list_user_repos(self, user: str, max_results: int) -> List[dict]:
        return self._paginate("/users/{}/repos".format(user), max_results)

    def list_org_repos(self, org: str, max_results: int) -> List[dict]:
        return self._paginate("/orgs/{}/repos".format(org), max_results)

    def get_repo(self, full_name: str) -> Optional[dict]:
        return self._get_json("/repos/{}".format(full_name))

    # -- 文件读取 ---------------------------------------------------------- #
    def get_tree(self, full_name: str, branch: str) -> List[dict]:
        data = self._get_json(
            "/repos/{}/git/trees/{}".format(full_name, branch),
            params={"recursive": "1"},
        )
        if not data:
            return []
        return data.get("tree", [])

    def get_raw_file(self, full_name: str, branch: str, path: str) -> Optional[str]:
        url = "{}/{}/{}/{}".format(config.GITHUB_RAW_URL, full_name, branch, path)
        response = self._request("GET", url)
        if response.status_code != 200:
            return None
        return response.text


class RepoScanner:
    """遍历仓库文件树并运行密钥检测。"""

    def __init__(self, client: GitHubClient, detector: Optional[SecretDetector] = None):
        self.client = client
        self.detector = detector or SecretDetector()

    @staticmethod
    def _extension(filename: str) -> str:
        if "." not in filename:
            return ""
        return "." + filename.rsplit(".", 1)[1].lower()

    def is_candidate(self, item: dict) -> bool:
        if item.get("type") != "blob":
            return False
        size = item.get("size") or 0
        if size and size > config.MAX_FILE_SIZE_BYTES:
            return False

        path = item.get("path", "")
        lowered = path.lower()
        if any(frag in "/" + lowered for frag in config.SKIP_PATH_FRAGMENTS):
            return False

        filename = lowered.rsplit("/", 1)[-1]
        if filename in config.TEXT_FILENAMES:
            return True
        if self._extension(filename) in config.TEXT_EXTENSIONS:
            return True
        return False

    def scan_repo(self, repo_info: dict) -> Tuple[List[Finding], int]:
        full_name = repo_info.get("full_name")
        if not full_name:
            return [], 0

        branch = repo_info.get("default_branch") or "main"
        tree = self.client.get_tree(full_name, branch)

        findings: List[Finding] = []
        files_scanned = 0

        for item in tree:
            if files_scanned >= config.MAX_FILES_PER_REPO:
                break
            if not self.is_candidate(item):
                continue

            path = item["path"]
            content = self.client.get_raw_file(full_name, branch, path)
            if not content or "\x00" in content[:2048]:
                # 二进制或读取失败，跳过
                continue

            files_scanned += 1
            url = "https://github.com/{}/blob/{}/{}".format(full_name, branch, path)
            findings.extend(
                self.detector.scan_text(
                    content, repo=full_name, file_path=path, file_url=url
                )
            )

        return findings, files_scanned
