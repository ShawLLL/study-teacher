<h1 align="center">你脑海的定制化助手，想要吗？得到！</h1>

<p align="center">
  <strong>Study Teacher｜别只让 AI 给你答案，让它真正把你教会。</strong>
</p>

<p align="center">
  一个把 Claude Code 变成学习老师的 Skill<br>
  直觉先行 · 场景练习 · 真话点评 · 本地笔记 · 跨会话续学
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-Skill-D97757" alt="Claude Code Skill">
  <img src="https://img.shields.io/badge/MiniMax_Code-Compatible-6C5CE7" alt="MiniMax Code Compatible">
  <img src="https://img.shields.io/badge/Notes-Local_Markdown-2E8B57" alt="Local Markdown Notes">
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="MIT License">
</p>

---

AI 很会给答案，但**看懂一个答案，不等于真正学会**。

Study Teacher 把“问一次、答一次”变成一条完整的学习路径：

**摸清基础 → 确认大纲 → 建立直觉 → 场景练习 → 追问深化 → 沉淀笔记 → 下次续学**

它不仅告诉你“是什么”，还会陪你弄清楚“为什么”“什么时候不适用”，以及“换一个场景，你还会不会”。

## 为什么不是直接问 AI？

| 一次性问答 | Study Teacher |
| --- | --- |
| 不知道从哪里开始，问一句学一句 | 先了解你的基础和目标，再共同确认学习大纲 |
| 公式、术语一起出现，看完似懂非懂 | 先讲一句话直觉，再解释术语，最后进入公式和细节 |
| 答案看懂了，换个问题又不会 | 用场景练习和渐进追问验证理解，而不是只让你点头 |
| AI 总是顺着你的方案说 | 直接指出优点、硬伤和代价，但不为了反驳而反驳 |
| 聊天结束，学习进度也散了 | 把大纲、进度和薄弱点保存为 Markdown，下次接着学 |

## 一位知道什么时候该闭嘴的老师

**该教的时候认真教，该让你思考的时候，不急着把答案喂给你。**

- **学习新知识**：直接、清晰地讲，不拿连续反问折磨你；进入练习后，再逐步提示。
- **请教方案**：先给诚实点评，再引导你自己找到更好的方案；卡住时会给完整兜底方案。
- **纯执行任务**：写、改、修、生成、翻译就直接做，不强行把每个请求都变成教学现场。
- **追问有上限**：同一问题默认最多追问 3 轮，明显卡住会提前给答案，不用“苏格拉底式提问”消耗耐心。

## 从“我想学”到“我真的会了”

### 1. 先摸清你，而不是复制一份通用教程

你的已有基础、目标深度、图示或理论偏好，都会影响后面的讲法。已经知道的跳过，没见过的术语及时补上。

### 2. 先建立直觉，再进入细节

每个模块遵循固定顺序：

> **一句话直觉 → 逐个角色与术语 → 公式、计算或实现**

如果公式里出现一个没解释过的符号，就先停下来补定义，不带着你一路裸奔。

### 3. 用练习发现“以为懂了”

刚学完就进入真实场景：做选择、解释理由、处理变化的条件。答对也会追问一层，确认你是真懂，而不是刚好猜对。

### 4. 把薄弱点留给下一次，而不是忘掉

学习档案记录大纲进度、术语、核心笔记和待复习清单。下次说“继续学”，先复习薄弱点，再从断点继续。

## 你可以这样开始

```text
我想系统学习 Transformer，我是零基础，一看到公式就头疼。
```

```text
继续学 Transformer，上次讲到哪了？先帮我复习薄弱点。
```

```text
帮我看看这个学习方案有什么硬伤，先别直接替我重做。
```

```text
我想学写短剧脚本，希望通过范例拆解和练习来学。
```

不只适合编程：知识原理、工具上手、写作创作、方案思辨，都可以按主题选择不同的学习方式与笔记结构。

## 快速安装

### Claude Code：插件安装（推荐）

在终端运行以下命令，从 GitHub 添加插件市场并安装：

```bash
claude plugin marketplace add ShawLLL/my-skill
claude plugin install study-teacher@study-teacher-marketplace
```

重新打开会话，然后直接说：

```text
我想系统学习一个主题。
```

也可以在安装时指定知识库：

```bash
claude plugin install study-teacher@study-teacher-marketplace \
  --config knowledge_base_path="<知识库绝对路径>"
```

<details>
<summary><strong>其他安装方式：独立 Skill / MiniMax Code</strong></summary>

### 独立 Skill

macOS / Linux：

```bash
git clone https://github.com/ShawLLL/my-skill.git ~/.claude/skills/study-teacher
```

Windows PowerShell：

```powershell
git clone https://github.com/ShawLLL/my-skill.git "$HOME\.claude\skills\study-teacher"
```

也可以复制到项目的 `.claude/skills/study-teacher/`，只在该项目启用。重新开始会话后生效。

独立安装可显式调用 `/study-teacher`；插件安装的命令名为 `/study-teacher:study-teacher`。自然语言触发不是必须依赖斜杠命令。

### MiniMax Code

可安装到 `~/.minimax/skills/study-teacher/`。支持 Claude Code 兼容读取的版本也可以直接共享 `~/.claude/skills/study-teacher/`，无需复制两份；以 MiniMax `skill` 工具返回的 `Location` 为准。

MiniMax Code 中请使用自然语言或原生 `skill` 工具触发，不使用 Claude 的插件配置界面或斜杠命令。

</details>

## 学习档案放在哪里？

**由你决定，没有作者电脑的固定路径，也不会默认写进 Skill 目录。**

普通问答和纯执行任务不需要配置。只有续接、复习或保存学习档案时，才需要选择知识库目录。

首次保存时，按提示提供一个绝对路径即可。也可以提前初始化：

```bash
python "<Skill目录>/scripts/init_knowledge_base.py" --path "<知识库绝对路径>"
```

初始化脚本只使用 Python 3 标准库，不访问网络；已有 README 和配置字段不会被覆盖。

<details>
<summary><strong>查看配置、手动配置与环境变量</strong></summary>

只读检查当前环境变量和用户文件配置：

```bash
python "<Skill目录>/scripts/init_knowledge_base.py" --show
```

`--show` 不读取 Claude 插件配置界面；插件配置的实际优先级更高。

不使用 Python 时，可手动创建 `~/.claude/study-teacher/config.json`：

```json
{
  "knowledge_base_path": "/absolute/path/to/knowledge-base"
}
```

Windows 推荐使用正斜杠，例如 `"D:/notes/knowledge-base"`；使用反斜杠时需要写成双反斜杠。手动配置时请自行创建并确认目录。

需要临时切换知识库时，可设置环境变量 `STUDY_TEACHER_KB_PATH`：

```bash
export STUDY_TEACHER_KB_PATH="$HOME/Documents/knowledge-base"
```

Windows PowerShell：

```powershell
$env:STUDY_TEACHER_KB_PATH = "D:\notes\knowledge-base"
```

配置优先级：

1. 插件配置 `knowledge_base_path`
2. 环境变量 `STUDY_TEACHER_KB_PATH`
3. `~/.claude/study-teacher/config.json`
4. 都未设置时，首次读写档案会询问并初始化

更换配置不会自动搬移旧知识库。目标目录不存在时会先确认再创建，已有学习笔记不会被清空或覆盖。

</details>

## 笔记不是附属品，而是下一次学习的入口

一个主题一个文件夹，按主题选择需要的文档，不套僵硬模板：

```text
<知识库>/<知识点>/
├── README.md           # 学习目标、大纲进度、待复习清单
├── 术语表.md           # 随学习持续补充
├── 逻辑图.md           # 可选：用 Mermaid 描述结构关系
├── 01-<模块>/
│   └── <按需文档>.md
└── <练习、范例或核心笔记>.md
```

学 Transformer，可以沉淀原理、权衡、应用场景和逻辑图；学短剧创作，则可以沉淀范例拆解、练习产出与点评记录。

**会话会结束，学习不必从头开始。**

## 本地优先，也尊重你的数据边界

- 学习档案默认只写入你配置的本地目录，不会被提交进这个 Skill 仓库。
- 初始化脚本不联网、不收集或上传数据。
- 没有隐藏的知识库同步，也不会替你搬移旧笔记。
- 本地笔记不等于模型离线；对话内容的数据处理仍遵循你使用的 AI 服务规则。

## 验证与贡献

本仓库包含知识库初始化脚本的标准库单元测试：

```bash
claude plugin validate . --strict
python -m unittest discover -s tests -v
```

欢迎通过 Issue 分享学习体验、教学反例和改进建议。发布其他 Skill 时，也可以复用 [发布检查清单](../PUBLISHING.md)。

## License

[MIT](../LICENSE) — 自由使用、修改和分享，保留许可证声明。

---

<p align="center">
  如果它让你从“我看过”走向“我真的懂了”，欢迎 Star、分享，或提出一个更好的教学场景。
</p>
