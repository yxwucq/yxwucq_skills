# yxwucq_skills

个人维护的 Codex Skills。这个仓库保存可跨项目、跨设备安装的技能源文件。

## 已有技能

| Skill | 用途 |
|---|---|
| [exploratory-scientific-plot](skills/exploratory-scientific-plot/SKILL.md) | 快速查看科研数据，生成轻量探索图，维护项目绘图 TOML |
| [formal-scientific-figure](skills/formal-scientific-figure/SKILL.md) | 制作用于 Markdown、PPT 或论文的正式科研图，提供完整 Figure legend |

两个技能参考 KOLF2.1J Perturbation Cell Atlas 的视觉风格：白底、清晰的数据结构、稳定配色与必要的直接标注。正式图的完整说明保存在随图 Markdown 中，长方法说明放在图外。

首次在新项目绘图时创建 `plot_style.toml`；已有项目先查找并沿用正在使用的绘图配置，保留已登记的组别颜色。修改样式时更新生效的 TOML 并重绘。探索版与正式版共用颜色语义，按用途切换尺寸、字号与导出配置。

## 在另一台设备安装

在 Codex 中直接发送：

> 使用 skill-installer，从 https://github.com/yxwucq/yxwucq_skills 安装 skills/exploratory-scientific-plot 和 skills/formal-scientific-figure。

也可以克隆本仓库后运行本地安装脚本（Python 3.9+，仅使用标准库）：

```bash
git clone https://github.com/yxwucq/yxwucq_skills.git
cd yxwucq_skills
python3 scripts/install_skills.py
```

安装目录默认是 `$CODEX_HOME/skills`；未设置 `CODEX_HOME` 时使用 `~/.codex/skills`。可用 `--dest` 指定其他目录。已存在的同名技能默认不会被覆盖。

安装后在下一条 Codex 消息中调用：

```text
使用 $exploratory-scientific-plot，先画一版探索图。
使用 $formal-scientific-figure，把结果整理成用于报告的正式图，并附完整 Figure legend。
```

## 更新和同步

本仓库是维护源文件的地方；设备上的安装目录是运行副本。同步 GitHub 和更新已安装技能是两个步骤，不会自动双向同步。

从 GitHub 获取更新并安装到当前设备：

```bash
git pull --ff-only
python3 scripts/install_skills.py --replace
```

`--replace` 会先将同名旧版本移到安装目录旁的 `skill-backups/`，再安装新版本，并输出备份位置。备份不放在技能发现目录内。仅安装某个技能可以追加 `--skill formal-scientific-figure`。

本地修改 `skills/` 中的文件后，用常规 Git 工作流提交并推送到本仓库；然后在需要使用修改的设备上重新运行安装脚本。`git push` 需要该设备已具备目标仓库的 GitHub 写入权限。

## 添加自己的新技能

在 `skills/<skill-name>/` 下放置 `SKILL.md` 和实际需要的 `assets/`、`references/`、`scripts/` 或 `agents/`。每个技能应能独立安装，使用相对路径引用自己的资源。根目录的安装脚本会发现 `skills/` 下包含 `SKILL.md` 的技能文件夹。

不要将 Codex 系统技能、账号配置、密钥、机器路径、分析原始数据或运行缓存放入这个仓库。项目专属的颜色配置留在各项目中；这里维护的是默认模板与使用规则。

## 参考素材

出处、固定代码版本与素材索引见各技能的 `references/sources.md`。论文 Fig. 1/2 保留来源链接，未打包出版原图；notebook 输出参考图随技能保留，并附上原代码仓库的 MIT 许可证。第三方许可仅适用于其对应素材。
