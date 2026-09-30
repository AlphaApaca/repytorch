# PyTorch 基础面试问题

先口头回答，再用最小代码证明。回答目标是 30～60 秒内给出定义、机制、使用场景和一个常见坑。

## Tensor 与 Autograd

- broadcasting 的规则是什么？它什么时候会造成隐藏的形状错误？
- `view`、`reshape` 和 `permute` 有什么关系？连续内存为什么相关？
- 叶子张量是什么？哪些张量的 `.grad` 默认会被保留？
- PyTorch 为什么累加梯度？训练循环应在哪里清零？
- `detach()`、`no_grad()` 和 `inference_mode()` 分别解决什么问题？

## 数据与模型

- `Dataset` 和 `DataLoader` 分别负责什么？
- `shuffle`、`batch_size`、`num_workers` 会怎样影响训练？
- 自定义层为什么应继承 `nn.Module`？参数怎样被注册？
- `model.train()` 与 `model.eval()` 会影响哪些常见层？

## 训练、保存与 GPU

- 一次标准训练 step 包含哪些操作，顺序为什么这样安排？
- 验证阶段为什么通常关闭梯度？
- `state_dict` 包含什么？恢复训练还需要保存哪些状态？
- CPU 与 GPU 张量混用会发生什么？怎样系统排查 device mismatch？
- CUDA OOM 后应检查哪些因素？
