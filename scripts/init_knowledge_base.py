#!/usr/bin/env python3
"""Configure the Study Teacher knowledge base using only the standard library."""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Optional, Tuple

ENV_PATH = "STUDY_TEACHER_KB_PATH"
CONFIG_KEY = "knowledge_base_path"
ROOT_README = """# Study Teacher 知识库

每个知识点使用一个独立文件夹，包含 README、术语表和按主题选择的文档。
学习档案只保存在本地；除非你明确选择，否则不会被上传或提交到 skill 仓库。
"""


class ConfigError(ValueError):
    """A configuration problem that can be shown directly to the user."""


def config_path() -> Path:
    return Path.home() / ".claude" / "study-teacher" / "config.json"


def normalize_path(raw_path: str) -> Path:
    if not isinstance(raw_path, str) or not raw_path.strip():
        raise ConfigError("知识库路径不能为空。")
    expanded = Path(os.path.expandvars(raw_path.strip())).expanduser()
    if not expanded.is_absolute():
        raise ConfigError(f"请使用绝对路径，收到：{raw_path}")
    return expanded.resolve(strict=False)


def read_config(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ConfigError(f"无法读取配置文件 {path}：{exc}") from exc
    if not isinstance(data, dict):
        raise ConfigError(f"配置文件必须是 JSON 对象：{path}")
    return data


def resolve_configured_path() -> Tuple[Optional[Path], str]:
    env_value = os.environ.get(ENV_PATH)
    if env_value and env_value.strip():
        return normalize_path(env_value), f"环境变量 {ENV_PATH}"

    path = config_path()
    data = read_config(path)
    if CONFIG_KEY not in data or data[CONFIG_KEY] in (None, ""):
        return None, "未配置"
    return normalize_path(data[CONFIG_KEY]), f"配置文件 {path}"


def save_config(path: Path, knowledge_base: Path) -> None:
    data = read_config(path)
    data[CONFIG_KEY] = str(knowledge_base)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def initialize(raw_path: str) -> Path:
    knowledge_base = normalize_path(raw_path)
    if knowledge_base.exists() and not knowledge_base.is_dir():
        raise ConfigError(f"知识库路径是文件，不是目录：{knowledge_base}")

    knowledge_base.mkdir(parents=True, exist_ok=True)
    readme = knowledge_base / "README.md"
    if not readme.exists():
        readme.write_text(ROOT_README, encoding="utf-8")

    save_config(config_path(), knowledge_base)
    return knowledge_base


def show_configuration() -> None:
    knowledge_base, source = resolve_configured_path()
    if knowledge_base is None:
        print("知识库：未配置")
        print(f"可用配置文件：{config_path()}")
        return
    print(f"知识库：{knowledge_base}")
    print(f"来源：{source}")
    print(f"目录存在：{'是' if knowledge_base.is_dir() else '否'}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="初始化或检查 Study Teacher 的本地知识库路径。"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--path", help="知识库绝对路径；支持 ~ 和环境变量。")
    group.add_argument(
        "--show", action="store_true", help="显示当前环境变量或文件配置，不修改文件。"
    )
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.show:
            show_configuration()
            return 0

        raw_path = args.path
        if raw_path is None:
            try:
                raw_path = input("学习笔记保存到哪个目录？请输入绝对路径：").strip()
            except EOFError as exc:
                raise ConfigError("未提供路径；非交互环境请使用 --path <绝对路径>。") from exc

        knowledge_base = initialize(raw_path)
        print(f"知识库已就绪：{knowledge_base}")
        print(f"配置已保存：{config_path()}")

        env_value = os.environ.get(ENV_PATH)
        if env_value and normalize_path(env_value) != knowledge_base:
            print(
                f"提醒：环境变量 {ENV_PATH} 指向 {normalize_path(env_value)}，"
                "它会覆盖刚保存的文件配置。",
                file=sys.stderr,
            )
        return 0
    except (ConfigError, OSError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    # Keep Chinese output readable when Windows pipes use a legacy code page.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    sys.exit(main())
