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

    def test_detects_xai_key(self):
        text = 'XAI_API_KEY = "xai-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMN"'
        findings = self.detector.scan_text(text)
        names = [f.pattern_name for f in findings]
        self.assertIn("xAI (Grok) API Key", names)

    def test_detects_openrouter_key(self):
        text = 'OPENROUTER_KEY = "sk-or-v1-abcdefghijklmnopqrstuvwxyz0123456789"'
        findings = self.detector.scan_text(text)
        names = [f.pattern_name for f in findings]
        self.assertIn("OpenRouter API Key", names)

    def test_detects_github_pat(self):
        text = 'token = "ghp_abcdefghijklmnopqrstuvwxyz0123456789"'
        findings = self.detector.scan_text(text)
        names = [f.pattern_name for f in findings]
        self.assertIn("GitHub Personal Access Token", names)

    def test_detects_deepseek_key_by_context(self):
        text = 'DEEPSEEK_API_KEY = "sk-abcdefghijklmnopqrstuvwxyz0123456789"'
        findings = self.detector.scan_text(text)
        names = [f.pattern_name for f in findings]
        self.assertIn("DeepSeek API Key", names)

    def test_plain_sk_key_falls_back_to_openai_label(self):
        text = 'api_key = "sk-abcdefghijklmnopqrstuvwxyz0123456789"'
        findings = self.detector.scan_text(text)
        names = [f.pattern_name for f in findings]
        self.assertIn("OpenAI API Key", names)

    def test_cerebras_not_double_reported_as_openai(self):
        # csk- 中含有子串 sk-，不应被通用 OpenAI 规则重复命中
        text = 'key = "csk-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFG"'
        findings = self.detector.scan_text(text)
        names = [f.pattern_name for f in findings]
        self.assertIn("Cerebras API Key", names)
        self.assertNotIn("OpenAI API Key", names)

    def test_groq_not_matched_as_elevenlabs(self):
        # gsk_ 中含有子串 sk_，不应被 ElevenLabs 规则命中
        text = 'key = "gsk_0123456789abcdef0123456789abcdef01234567"'
        findings = self.detector.scan_text(text)
        names = [f.pattern_name for f in findings]
        self.assertIn("Groq API Key", names)
        self.assertNotIn("ElevenLabs API Key", names)

    def test_underscore_prefix_needs_boundary(self):
        # task_ 中的 sk_ 不是 ElevenLabs 密钥
        text = 'task_0123456789abcdef0123456789abcdef0123 = 1'
        findings = self.detector.scan_text(text)
        names = [f.pattern_name for f in findings]
        self.assertNotIn("ElevenLabs API Key", names)

    def test_filters_test_placeholder_value(self):
        # 形如 AKIA000TEST000KEY000A 的测试值应被过滤
        text = 'aws_access_key_id = "AKIA000TEST000KEY000A"'
        findings = self.detector.scan_text(text)
        names = [f.pattern_name for f in findings]
        self.assertNotIn("AWS Access Key ID", names)

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
