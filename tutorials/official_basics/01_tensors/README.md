# 01 · Tensors

- 官方来源：[Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)
- 查看日期：2026-09-21
- 目标运行环境：Python 3.12.3，PyTorch 2.12.1+cu130，RTX 5090

## 本章目标

- 创建张量并读取 `shape`、`dtype` 和 `device`
- 使用索引与切片
- 解释广播发生在什么维度
- 区分逐元素乘法与矩阵乘法
- 确保参与运算的张量位于同一设备

## 运行前先预测

打开 [`walkthrough.py`](walkthrough.py)，先回答：

1. `x`、`offset`、`shifted` 和 `weights` 的形状分别是什么？
2. `x + offset` 为什么合法？`offset` 会沿哪个维度扩展？
3. `x @ weights` 的输出形状和值是什么？
4. CUDA 可用与不可用时，代码分别在哪个设备上运行？

然后执行：

```bash
python tutorials/official_basics/01_tensors/walkthrough.py
```

## 完成检查

- [ ] 不运行代码也能写出所有形状
- [ ] 能用一句话解释 broadcasting
- [ ] 能说明 `x * x` 与 `x @ x.T` 的区别
- [ ] 能自己增加一个切片并核对结果
- [ ] 合上教程完成 `practice/fundamentals/01_tensor_autograd.py`
