"""Detect leaked AI API keys in arbitrary text.

The detector is intentionally dependency free (only the standard library) so it
can be unit tested and reused anywhere.
"""

import hashlib
import re
from dataclasses import dataclass
from typing import List, Optional, Sequence

import config


@dataclass
class Finding:
    """A single suspected secret leak."""

    pattern_name: str
    value: str
    masked: str
    confidence: str
    line_number: int
    line_content: str
    repo: str = ""
    file_path: str = ""
    file_url: str = ""
    description: str = ""

    @property
    def fingerprint(self) -> str:
        """Stable identifier used for de-duplication across scans."""
        raw = "|".join(
            [self.repo, self.file_path, str(self.line_number), self.value]
        )
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]

    def to_dict(self) -> dict:
        return {
            "pattern_name": self.pattern_name,
            "value_masked": self.masked,
            "confidence": self.confidence,
            "repo": self.repo,
            "file_path": self.file_path,
            "file_url": self.file_url,
            "line_number": self.line_number,
            "line_content": self.line_content.strip()[:400],
            "description": self.description,
            "fingerprint": self.fingerprint,
        }


class SecretDetector:
    """Scan text line by line and return :class:`Finding` objects."""

    def __init__(self, patterns: Optional[Sequence[dict]] = None):
        self.patterns = []
        for p in (patterns if patterns is not None else config.SENSITIVE_PATTERNS):
            self.patterns.append(
                (
                    p["name"],
                    re.compile(p["regex"]),
                    p.get("confidence", "medium"),
                    p.get("description", ""),
                )
            )

    # -- helpers ----------------------------------------------------------- #
    @staticmethod
    def mask(value: str) -> str:
        if len(value) <= 8:
            return value[:2] + "*" * max(0, len(value) - 2)
        return "{}...{}".format(value[:6], value[-4:])

    @staticmethod
    def _is_placeholder(value: str) -> bool:
        lowered = value.lower()
        if any(token in lowered for token in config.PLACEHOLDER_TOKENS):
            return True
        # Low-entropy values are almost never real keys.
        if len(set(lowered)) < 8:
            return True
        return False

    @staticmethod
    def _downgrade(confidence: str) -> str:
        return {"high": "medium", "medium": "low", "low": "low"}.get(
            confidence, "low"
        )

    # -- main API ---------------------------------------------------------- #
    def scan_text(
        self,
        text: str,
        repo: str = "",
        file_path: str = "",
        file_url: str = "",
    ) -> List[Finding]:
        findings: List[Finding] = []
        seen = set()

        for line_number, line in enumerate(text.splitlines(), start=1):
            if not line or len(line) > 4000:
                continue
            context = line.lower()

            for name, regex, confidence, description in self.patterns:
                for match in regex.finditer(line):
                    value = match.group(1) if regex.groups else match.group(0)
                    if not value or self._is_placeholder(value):
                        continue

                    dedup_key = (line_number, value)
                    if dedup_key in seen:
                        continue
                    seen.add(dedup_key)

                    effective = confidence
                    if any(tok in context for tok in config.EXAMPLE_CONTEXT_TOKENS):
                        effective = self._downgrade(confidence)

                    findings.append(
                        Finding(
                            pattern_name=name,
                            value=value,
                            masked=self.mask(value),
                            confidence=effective,
                            line_number=line_number,
                            line_content=line,
                            repo=repo,
                            file_path=file_path,
                            file_url=file_url,
                            description=description,
                        )
                    )

        findings.sort(
            key=lambda f: (
                config.SEVERITY_ORDER.get(f.confidence, 3),
                f.file_path,
                f.line_number,
            )
        )
        return findings
