# 学习路线

路线以 PyTorch 官方 **Learn the Basics** 为主线，再补充独立练习、工程实践和面试复述。勾选一项前，应保留能被重新运行或重新讲解的证据。

## 完成标准

一个主题完成需要满足：

- [ ] 跑通并理解官方教程复现
- [ ] 合上教程独立写出核心代码
- [ ] 能预测关键张量的形状、设备和梯度
- [ ] 能说明至少一个常见错误及排查方法
- [ ] 在笔记中写出 30～60 秒的面试回答

## Phase 0：环境与工作流

- [x] VS Code Remote SSH 连接 AutoDL
- [x] GitHub 作为本机与服务器之间的代码同步渠道
- [x] 记录实际 Python、PyTorch、CUDA 和 GPU 信息
- [x] 在 RTX 5090 上完成 CUDA 矩阵乘法
- [ ] 在 MacBook Air M4 的 `repytorch` Conda 环境中完成 MPS 矩阵乘法

证据：[`scripts/check_gpu.py`](scripts/check_gpu.py) 与 [`learning_log/2026-09-21-setup.md`](learning_log/2026-09-21-setup.md)。

## Phase 1：Tensor 与 Autograd（进行中）

- [ ] 创建、dtype、shape、索引与切片
- [ ] 广播、逐元素运算与矩阵乘法
- [ ] CPU/GPU 设备迁移
- [x] `requires_grad`、`backward()` 与梯度核对
- [ ] 梯度累加、清零和计算图生命周期

当前入口：

- 官方教程复现：[`tutorials/official_basics/01_tensors/`](tutorials/official_basics/01_tensors/README.md)
- 独立练习：[`practice/fundamentals/01_tensor_autograd.py`](practice/fundamentals/01_tensor_autograd.py)

## Phase 2：数据管线

- [ ] `Dataset` 与自定义 `Dataset`
- [ ] `DataLoader`、batch、shuffle 与 worker
- [ ] transforms 与数据划分
- [ ] 检查样本、标签、batch 形状和数据泄漏

阶段成果：不看教程写一个小型数据集和加载器，并可视化或打印一个 batch。

## Phase 3：模型与训练

- [ ] `nn.Module`、参数注册和前向传播
- [ ] 常用损失函数与优化器
- [ ] 独立写出训练循环
- [ ] 验证循环、`train()`、`eval()` 与 `inference_mode()`
- [ ] 指标记录、随机种子和基本复现

阶段成果：从空文件写出 `zero_grad → forward → loss → backward → step`，并解释每一步。

## Phase 4：保存、恢复与 GPU 实践

- [ ] `state_dict` 保存与加载
- [ ] 从 checkpoint 恢复训练
- [ ] 显存观察、batch size 与 OOM 排查
- [ ] mixed precision 基础
- [ ] CPU 与 GPU 推理结果核对

阶段成果：保存一次训练状态，重新加载后得到一致预测，并继续训练。

## Phase 5：端到端项目

- [ ] 项目一：FashionMNIST MLP 基线
- [ ] 项目二：CIFAR-10 CNN
- [ ] 项目三：结合目标岗位选择的数据或模型任务

每个项目的交付要求见 [`projects/README.md`](projects/README.md)。

## Phase 6：求职复述与调试

- [ ] 完成核心问题清单
- [ ] 限时手写 Dataset、Module、训练循环和 checkpoint
- [ ] 整理亲自遇到的报错、根因和修复过程
- [ ] 选择一个项目，完成 3 分钟结构化讲解

问题清单见 [`notes/interview-questions.md`](notes/interview-questions.md)。
