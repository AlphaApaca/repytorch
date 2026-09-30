# 基础练习

## 当前练习

### 01 · Tensor 与 Autograd

运行：

```bash
python practice/fundamentals/01_tensor_autograd.py
```

运行前预测 `x`、`w`、`y` 的形状，以及 `w.grad` 的三个值。通过基础版本后继续完成：

1. 把 `w` 改成形状为 `(3, 2)` 的矩阵，预测输出和梯度形状。
2. 重新执行一次前向传播和 `backward()`，观察梯度累加，再用 `w.grad.zero_()` 清空。
3. 故意把 `x` 和 `w` 放在不同设备，阅读报错并修复。
4. 解释为什么不能对已经释放的同一计算图直接再次调用 `backward()`。
