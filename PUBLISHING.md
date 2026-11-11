# 发布检查清单

这份清单也适用于其他自定义 skill。目标：公开仓库中只放可复用的 skill，不泄露本机配置和私人数据。

## 1. 公共内容检查

- [ ] `SKILL.md` 的 `name` 与目录名一致，`description` 同时说明“做什么”和“何时触发”。
- [ ] 没有作者本机的知识库、项目路径、用户名、令牌、邮箱或其他私人信息。
- [ ] 示例路径是通用占位符或明确示例，不是实际数据位置。
- [ ] 私人笔记、用户配置、缓存和构建产物没有进入仓库。
- [ ] `assets/` 中的引用都存在，示例不依赖作者本机文件。
- [ ] 外部依赖、网络访问和会写磁盘的行为已在 README 说明。
- [ ] 已选择许可证；本仓库默认 MIT。

## 2. 补全仓库信息

拿到 Git 地址后：

- [ ] 将 `docs/README.md` 中所有 `<owner>/<repo>` 替换为实际仓库。
- [ ] 在 `.claude-plugin/plugin.json` 添加 `repository`（以及可选的 `homepage`）。
- [ ] 将插件和市场的 `author` / `owner` 改为希望公开显示的名称。
- [ ] 确认 `.claude-plugin/plugin.json` 的 `version`；每次发布更新版本号。
- [ ] 如果复用于另一个 skill，同步修改插件名、市场名、显示名、描述和安装命令。

## 3. 本地验证

```bash
claude plugin validate . --strict
python -m unittest discover -s tests -v
```

至少再人工检查：

- [ ] 在没有环境变量和用户配置的全新环境中，会询问路径，而不是写入默认目录。
- [ ] 初始化支持带空格的绝对路径，重复执行不会覆盖已有 README。
- [ ] 环境变量优先于用户配置文件；无效 JSON 会报错而不是被覆盖。
- [ ] 只读 `--show` 不创建配置或知识库。
- [ ] 新会话能够发现 skill，相关请求能触发，纯执行任务不会被教学模式阻断。

## 4. 发布到 Git

在用户已提供仓库地址并明确授权发布后：

```bash
git init
git add .
git commit -m "Release study-teacher 1.0.0"
git branch -M main
git remote add origin <用户提供的Git地址>
git push -u origin main
```

如果目录已经是 Git 仓库，不要重复 `git init` 或覆盖已有 remote；先检查现状。推送前核对 `git diff --cached` 和 remote，空仓库与已有历史的仓库分别处理。

## 5. 验证公开安装

将 `<owner>/<repo>` 换成实际地址：

```bash
claude plugin marketplace add <owner>/<repo>
claude plugin install study-teacher@study-teacher-marketplace
claude plugin details study-teacher
```

在一个没有原开发环境配置的新会话里完成首次初始化，再验证新建、续接和复习流程。

## 后续发布其他 skill

可以复用本仓库结构：

```text
<skill-name>/
├── SKILL.md
├── docs/
│   └── README.md  # GitHub 可识别；不放在 skill 根目录可兼容 MiniMax lint
├── LICENSE
├── .gitignore
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── assets/       # 可选：输出模板
├── scripts/      # 可选：确定性工具
└── tests/        # 可选但推荐
```

若多个 skill 要作为一个插件一起发布，改用标准的 `skills/<skill-name>/SKILL.md` 布局；单 skill 仓库可像本项目一样通过 `"skills": ["./"]` 直接加载根目录。
