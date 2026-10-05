"""SecretDetector 的单元测试（使用标准库 unittest，无额外依赖）。

运行：
    python -m unittest discover -s tests -v
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from secret_detector import SecretDetector  # noqa: E402


class TestSecretDetector(unittest.TestCase):
    def setUp(self):
        self.detector = SecretDetector()

    def test_detects_openai_project_key(self):
        text = 'OPENAI_API_KEY = "sk-proj-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGH"'
        findings = self.detector.scan_text(text)
        self.assertTrue(findings)
        self.assertEqual(findings[0].pattern_name, "OpenAI Project API Key")
        self.assertEqual(findings[0].confidence, "high")

    def test_detects_anthropic_key(self):
        text = 'key = "sk-ant-api03-abcdefghijklmnopqrstuvwxyz0123"'
        findings = self.detector.scan_text(text)
        names = [f.pattern_name for f in findings]
        self.assertIn("Anthropic API Key", names)

    def test_ignores_placeholder(self):
        text = 'OPENAI_API_KEY = "sk-proj-your-key-here-replace-this-value-00000000"'
        findings = self.detector.scan_text(text)
        self.assertEqual(findings, [])

    def test_masks_value(self):
        value = "sk-proj-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGH"
        self.assertEqual(SecretDetector.mask(value), "sk-pro...EFGH")

    def test_confidence_downgraded_in_example_context(self):
        text = '# example only: sk-proj-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGH'
        findings = self.detector.scan_text(text)
        self.assertTrue(findings)
        self.assertEqual(findings[0].confidence, "medium")

    def test_file_metadata_attached(self):
        text = 'token = "gsk_abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGH"'
        findings = self.detector.scan_text(
            text, repo="octocat/demo", file_path="a.py", file_url="http://x"
        )
        self.assertEqual(findings[0].repo, "octocat/demo")
        self.assertEqual(findings[0].file_path, "a.py")

    def test_fingerprint_is_stable(self):
        text = 'token = "gsk_abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGH"'
        f1 = self.detector.scan_text(text, repo="a/b", file_path="x.py")[0]
        f2 = self.detector.scan_text(text, repo="a/b", file_path="x.py")[0]
        self.assertEqual(f1.fingerprint, f2.fingerprint)

    def test_no_duplicate_findings_on_same_line(self):
        text = 'api_key = "gsk_abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGH"'
        findings = self.detector.scan_text(text)
        values = [f.value for f in findings]
        self.assertEqual(len(values), len(set(values)))


if __name__ == "__main__":
    unittest.main()
