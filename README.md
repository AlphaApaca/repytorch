# RePyTorch

这是一个面向求职复习的 PyTorch 学习仓库。目标是把每个主题整理成四类可检查的成果：跟随官方教程复现、合上教程独立练习、用自己的话解释，以及在完整项目中应用。

当前远端环境已实测为：

| 项目 | 版本 |
| --- | --- |
| GPU | NVIDIA GeForce RTX 5090，32607 MiB |
| Python | 3.12.3，`/root/miniconda3/bin/python` |
| PyTorch | 2.12.1+cu130 |
| PyTorch CUDA 构建 | 13.0 |

## 学习循环

每个主题按下面的顺序完成：

1. 在 [`tutorials/`](tutorials/README.md) 跟随官方材料，用自己的代码复现。
2. 在 [`practice/`](practice/README.md) 合上教程完成小题，并用断言核对结果。
3. 在 [`notes/`](notes/README.md) 记录原理、易错点和面试表达。
4. 在 [`learning_log/`](learning_log/README.md) 写下本次结果和下一步。
5. 学完一组相关知识后，在 [`projects/`](projects/README.md) 做一个端到端项目。

## 目录结构

```text
repytorch/
├── README.md                    # 项目入口
├── ROADMAP.md                   # 学习路线与完成标准
├── COMMANDS.md                  # 本机、Git、服务器和 GPU 命令速查
├── docs/
│   ├── local-mac.md             # M4、Conda、pip 与 MPS 配置
│   └── remote-setup.md          # VS Code、AutoDL 与 Git 同步说明
├── tutorials/
│   └── official_basics/         # PyTorch Learn the Basics 的个人复现
├── practice/
│   └── fundamentals/            # 不看教程完成的基础练习
├── outputs/
│   └── README.md                 # 模型与训练结果的保存规则
├── projects/                    # 可展示的端到端项目
├── notes/                       # 概念、踩坑与面试问答
├── learning_log/                # 按日期记录学习证据
└── scripts/
    └── check_gpu.py             # 环境与 CUDA 自检
```

`outputs/` 中只提交说明文件，模型、checkpoint 和训练日志均由程序按需生成并被 Git 忽略。具体规则见 [`outputs/README.md`](outputs/README.md)。`data/`、`runs/`、`checkpoints/` 等其他运行时目录也已被忽略。

## 现在从这里开始

在 AutoDL 服务器上拉取最新代码并运行自检：

```bash
cd /root/autodl-tmp/repytorch
git pull --ff-only
python scripts/check_gpu.py
```

然后完成当前主题的两份代码：

```bash
python tutorials/official_basics/01_tensors/walkthrough.py
python practice/fundamentals/01_tensor_autograd.py
```

运行前先写下对形状、设备和值的预测；运行后解释实际结果。当前进度和每阶段的完成条件见 [`ROADMAP.md`](ROADMAP.md)，日常命令见 [`COMMANDS.md`](COMMANDS.md)。

在 MacBook Air M4 上运行前，按照 [`docs/local-mac.md`](docs/local-mac.md) 激活 `repytorch` Conda 环境、安装 PyTorch 并验证 MPS。

## 仓库约定

- 官方教程复现文件要记录来源链接、查看日期和验证环境，代码与解释使用自己的表达。
- 基础练习优先使用 `.py`，在关键结果处添加断言；需要交互式可视化时再使用 notebook。
- 每学到一章再创建对应内容，保持目录中的文件都有实际用途。
- 项目出现共享代码、稳定配置和需要回归验证的逻辑后，再增加 `src/`、`configs/` 和 `tests/`。
