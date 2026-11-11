import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import init_knowledge_base as kb  # noqa: E402


class KnowledgeBaseConfigTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.home = self.root / "home"
        self.home.mkdir()
        self.home_patch = mock.patch.object(kb.Path, "home", return_value=self.home)
        self.home_patch.start()
        self.addCleanup(self.home_patch.stop)
        self.env_patch = mock.patch.dict(os.environ, {}, clear=True)
        self.env_patch.start()
        self.addCleanup(self.env_patch.stop)

    def config_file(self):
        return self.home / ".claude" / "study-teacher" / "config.json"

    def test_initialize_creates_directory_and_absolute_config(self):
        knowledge_base = self.root / "notes with spaces"
        result = kb.initialize(str(knowledge_base))

        self.assertEqual(result, knowledge_base.resolve())
        self.assertTrue((knowledge_base / "README.md").is_file())
        config = json.loads(self.config_file().read_text(encoding="utf-8"))
        self.assertEqual(config["knowledge_base_path"], str(knowledge_base.resolve()))

    def test_reinitialize_preserves_readme_and_other_config_keys(self):
        knowledge_base = self.root / "notes"
        readme = knowledge_base / "README.md"
        knowledge_base.mkdir()
        readme.write_text("我的旧笔记索引", encoding="utf-8")
        self.config_file().parent.mkdir(parents=True)
        self.config_file().write_text('{"custom": "keep"}', encoding="utf-8")

        kb.initialize(str(knowledge_base))
        kb.initialize(str(knowledge_base))

        self.assertEqual(readme.read_text(encoding="utf-8"), "我的旧笔记索引")
        config = json.loads(self.config_file().read_text(encoding="utf-8"))
        self.assertEqual(config["custom"], "keep")

    def test_relative_path_is_rejected_without_writes(self):
        with self.assertRaises(kb.ConfigError):
            kb.initialize("relative/notes")
        self.assertFalse(self.config_file().exists())

    def test_environment_variable_overrides_file(self):
        from_env = self.root / "from-env"
        from_file = self.root / "from-file"
        kb.initialize(str(from_file))
        os.environ[kb.ENV_PATH] = str(from_env)

        resolved, source = kb.resolve_configured_path()

        self.assertEqual(resolved, from_env.resolve())
        self.assertIn(kb.ENV_PATH, source)

    def test_show_is_read_only_when_unconfigured(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            kb.show_configuration()

        self.assertIn("未配置", output.getvalue())
        self.assertFalse(self.config_file().exists())

    def test_invalid_config_is_not_overwritten(self):
        self.config_file().parent.mkdir(parents=True)
        self.config_file().write_text("not json", encoding="utf-8")

        with self.assertRaises(kb.ConfigError):
            kb.initialize(str(self.root / "notes"))

        self.assertEqual(self.config_file().read_text(encoding="utf-8"), "not json")

    def test_path_expands_environment_variables(self):
        os.environ["STUDY_TEACHER_TEST_ROOT"] = str(self.root)
        result = kb.initialize("$STUDY_TEACHER_TEST_ROOT/expanded")
        self.assertEqual(result, (self.root / "expanded").resolve())


if __name__ == "__main__":
    unittest.main()
