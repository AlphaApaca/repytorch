# 训练输出

`outputs/` 统一保存程序运行后生成的模型、checkpoint、指标、日志和临时图表。除本说明文件外，该目录中的内容均被 Git 忽略。

## 推荐结构

教程代码：

```text
outputs/tutorials/<教程名称>/
├── model.pth
└── metrics.json
```

端到端项目：

```text
outputs/projects/<项目名称>/<运行编号>/
├── checkpoints/
│   ├── best.pt
│   └── last.pt
├── config.json
├── metrics.json
└── logs/
```

运行编号可以使用日期和时间，例如 `2026-09-30_1530`。训练代码应通过 `Path.mkdir(parents=True, exist_ok=True)` 自动创建所需目录。

## 保存内容

- `best.pt`：验证指标最好的模型
- `last.pt`：最近一次训练状态，用于恢复训练
- `config.json`：超参数和随机种子
- `metrics.json`：训练与验证指标
- `logs/`：运行日志

大型模型和每次训练的完整结果不提交到 Git。需要长期保留时，应复制到持久化存储；需要展示的小型曲线或图片可以筛选后放入对应项目的 `assets/` 并提交。
