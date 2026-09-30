# 官方教程复现

本目录跟随 PyTorch 官方 **Learn the Basics**。每一章使用自己的代码和解释完成复现，并保留官方来源。

## 章节地图

| 顺序 | 官方章节 | 本地位置 | 状态 |
| --- | --- | --- | --- |
| 00 | [Quickstart](https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html) | 学到时创建 `00_quickstart/` | 待开始 |
| 01 | [Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html) | [`01_tensors/`](official_basics/01_tensors/README.md) | 进行中 |
| 02 | [Datasets & DataLoaders](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html) | 学到时创建 `02_datasets_dataloaders/` | 待开始 |
| 03 | [Transforms](https://docs.pytorch.org/tutorials/beginner/basics/transforms_tutorial.html) | 学到时创建 `03_transforms/` | 待开始 |
| 04 | [Build the Neural Network](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html) | 学到时创建 `04_build_model/` | 待开始 |
| 05 | [Automatic Differentiation](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) | 学到时创建 `05_autograd/` | 待开始 |
| 06 | [Optimizing Model Parameters](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) | 学到时创建 `06_optimization/` | 待开始 |
| 07 | [Save and Load the Model](https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html) | 学到时创建 `07_save_load/` | 待开始 |

总入口：[PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/)。教程网页会持续更新；本仓库以远端实际安装的 PyTorch 版本验证代码。

## 每章的最小产出

```text
章节目录/
├── README.md       # 来源、目标、关键理解和自测题
└── walkthrough.py  # 自己重写并运行通过的最小复现
```

完成 walkthrough 后，在 `practice/` 写一份不看教程完成的练习。遇到值得保留的错误时，把“现象、原因、修复、如何预防”记录到 `notes/`。
