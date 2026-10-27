# 参考素材与可核对的证据

论文：Nourreddine, S. 等，*A genome-scale CRISPRi perturbation atlas of human induced pluripotent stem cells*，Nature Biotechnology (2026)。

- [论文主页](https://www.nature.com/articles/s41587-026-03199-w)
- [公开代码仓库](https://github.com/y-doctor/KOLF2.1J_Perturbation_Cell_Atlas)
- 参考素材来自代码版本 `8f84531a784f24b14d7e2c9b80c375d7e78fd46c`，不是对仓库最新版本的声明。
- 整理日期：2026-10-27。notebook 原始输出从固定版本中提取，未重跑分析；论文原图通过下方来源链接查看。

## 先看哪些图

| 参考素材 | 对应位置 | 用途 |
|---|---|---|
| [论文 Fig. 1（来源链接）](https://www.nature.com/articles/s41587-026-03199-w/figures/1) | 总体实验与统计概览 | 蓝线/浅填充、淡色对照、直接提示、数据与说明分层 |
| [论文 Fig. 2（来源链接）](https://www.nature.com/articles/s41587-026-03199-w/figures/2) | 热图、图谱、柱状图、网络 | 多面板组织、同色功能标注、紧凑图例与色条 |
| [原始 MDE 输出](images/raw-mde.png) | Fig. 2e 的对应底图 | 点结构与分类色已具备；论文成图增加功能标注与标题等 |
| [原始热图输出](images/raw-cluster-heatmap.png) | Fig. 2b 对应输出 | 主体结构接近；留白、色条、类别说明的组织不同 |
| [原始柱状图输出](images/raw-enrichment-bars.png) | Fig. 2f 对应输出 | 粉/灰配色已具备；论文的文字、图例和统计标注有差异 |
| [原始骨架网络输出](images/raw-fitness-network.png) | Fig. 2g 对应输出 | 主体布局接近；竖向色条与论文横向紧凑色条形成对照 |
| [原始调控网络输出](images/raw-regulatory-network.png) | Fig. 2c 的相关分析输出 | 与论文节点形状/布局差别较大；不能当作精确前后版本 |

上述对照是视觉抽查。不同文件可能处于不同分析或出图版本，不能仅凭图片差异断言作者使用了哪种后期软件，或认为差异全来自手工编辑。

## 可追溯的代码设置

- [plotting.py](https://github.com/y-doctor/KOLF2.1J_Perturbation_Cell_Atlas/blob/8f84531a784f24b14d7e2c9b80c375d7e78fd46c/psp/pl/plotting.py)：Arial；蓝色 `#367CB7` 和浅填充 `#EDF6FF`；去除上/右边框；多处关闭网格。
- [data_analysis.py](https://github.com/y-doctor/KOLF2.1J_Perturbation_Cell_Atlas/blob/8f84531a784f24b14d7e2c9b80c375d7e78fd46c/psp/da/data_analysis.py)：`plot_mde` 使用 Plotly Bold 分类色、默认 `s=7`、`alpha=0.7`、白色细边；相关热图使用 `RdBu`；这些参数是具体函数的默认值，不是普遍标准。
- [主分析 notebook](https://github.com/y-doctor/KOLF2.1J_Perturbation_Cell_Atlas/blob/8f84531a784f24b14d7e2c9b80c375d7e78fd46c/psp/notebooks/Pan_Expressed_Genome_Analysis/KOLF_Perturbation_Atlas_Data_Analysis.ipynb)：灰色 `#b0b0b0` 与粉色 `#e75480` 柱形图，导出 SVG；热图另有 PNG 输出。
- [MDE_Views notebook](https://github.com/y-doctor/KOLF2.1J_Perturbation_Cell_Atlas/blob/8f84531a784f24b14d7e2c9b80c375d7e78fd46c/psp/notebooks/Pan_Expressed_Genome_Analysis/MDE_Views_and_DEG_Networks/MDE_Views.ipynb)：浅灰连线、无坐标轴、节点文字、`RdYlGn`/`GnBu` 连续映射以及 SVG 导出。
- [networks notebook](https://github.com/y-doctor/KOLF2.1J_Perturbation_Cell_Atlas/blob/8f84531a784f24b14d7e2c9b80c375d7e78fd46c/psp/notebooks/Pan_Expressed_Genome_Analysis/MDE_Views_and_DEG_Networks/networks.ipynb)：青绿 `#78c0af`、珊瑚色 `#e7857c` 表达调控方向，图例明确解释。

## 文件来源

论文图片原始 URL：

- [Fig. 1 PNG](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41587-026-03199-w/MediaObjects/41587_2026_3199_Fig1_HTML.png)
- [Fig. 2 PNG](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41587-026-03199-w/MediaObjects/41587_2026_3199_Fig2_HTML.png)

notebook PNG 从 `cells[i].outputs[j].data["image/png"]` 原样解码，索引从 0 开始：

| 文件 | notebook | cell / output |
|---|---|---|
| raw-mde.png | KOLF_Perturbation_Atlas_Data_Analysis.ipynb | 13 / 2 |
| raw-cluster-heatmap.png | KOLF_Perturbation_Atlas_Data_Analysis.ipynb | 8 / 2 |
| raw-enrichment-bars.png | KOLF_Perturbation_Atlas_Data_Analysis.ipynb | 29 / 1 |
| raw-fitness-network.png | MDE_Views.ipynb | 5 / 0 |
| raw-regulatory-network.png | networks.ipynb | 1 / 2 |

## 来源与使用边界

论文原图保留原出版物的权利归属，本仓库仅提供来源链接，不打包论文原图。随技能附带的 raw-*.png 来自上述 MIT 代码仓库的 notebook 输出；保留其出处和 [repository-LICENSE.txt](repository-LICENSE.txt)。该 MIT 许可不适用于论文出版图片，也不代表本仓库所有文件采用同一许可。

在新科研图中复用的是配色与视觉方法，不复用原论文数据、结论或生物学标签。

## 原样文件校验

- `raw-mde.png`：1599 × 1559；SHA-256 `06282fea661d32bb9043c43c01ec6526e0d0038b9480d9335f48974b40eda1b2`。
- `raw-cluster-heatmap.png`：1965 × 1965；SHA-256 `c3e7d81184bf96c08f84af0ff6519dd756f60a7de3aa16033e92ccb60a521280`。
- `raw-enrichment-bars.png`：1567 × 1171；SHA-256 `31c93cf13d635453fe3e68d312d09153b3126c4cb6221c54ef73cd9fcea39a8d`。
- `raw-fitness-network.png`：765 × 590；SHA-256 `708ab090a744e1327a22474b6fd0ecf4363730cbbc7ea114662a70e8bfc91a05`。
- `raw-regulatory-network.png`：4008 × 4062；SHA-256 `e322607a47b8f65f4e8f7c1a9d35cb9718ab59741ebda7a723db00cb3b78a837`。
