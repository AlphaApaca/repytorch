# 独立练习

这里放合上教程后独立完成的小题。练习用于检验能否从空文件写出核心代码，并能解释输出和报错。

## 做题规则

1. 先在注释或纸上写出预期的 shape、device、关键数值或梯度。
2. 从导入开始独立编写，关键结果使用 `assert` 或 `torch.testing.assert_close` 核对。
3. 运行后用自己的话解释结果。
4. 至少修改一个条件，再观察结论是否仍成立。
5. 遇到错误时记录完整报错、根因和修复方法。

## 分类

- [`fundamentals/`](fundamentals/README.md)：Tensor、Autograd、数据管线、模型和训练循环。
- `debugging/`：遇到真实调试题时创建。
- `interview_drills/`：开始限时手写训练后创建。
