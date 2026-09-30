# 在 Apple Silicon Mac 上运行 PyTorch

MacBook Air M4 足以运行本仓库的基础教程、Autograd、小型数据集和小模型。PyTorch 通过 **MPS（Metal Performance Shaders）** 使用 Apple GPU；macOS 不使用 CUDA，也不需要安装 CUDA Toolkit。

## 推荐方案：继续使用现有 Conda 环境

无需再创建 `.venv`。当前 `repytorch` 环境已经满足要求：

| 项目 | 当前结果 |
| --- | --- |
| 环境位置 | `/opt/homebrew/Caskroom/miniforge/base/envs/repytorch` |
| Python | 3.12.14 |
| 架构 | arm64 |
| pip | 26.2.1 |
| PyTorch | 尚未安装 |

激活环境并安装与服务器版本对应的 PyTorch：

```bash
cd /Users/alpaca/workplace/repytorch
conda activate repytorch
python -m pip install torch==2.12.1 torchvision==0.27.1
```

Conda 负责隔离 Python 环境，`python -m pip` 负责把 PyTorch 安装到当前环境。使用这种写法可以明确 pip 对应的是当前激活的 Python。

以后重新打开终端：

```bash
cd /Users/alpaca/workplace/repytorch
conda activate repytorch
```

退出环境：

```bash
conda deactivate
```

## 验证 MPS

激活 `repytorch` 后运行：

```bash
python scripts/check_mps.py
```

成功时应看到：

```text
MPS built: True
MPS available: True
MPS matrix multiplication: OK
```

也可以直接检查：

```bash
python -c 'import torch; print(torch.__version__); print(torch.backends.mps.is_built()); print(torch.backends.mps.is_available())'
```

在 VS Code 中运行 `Python: Select Interpreter`，选择名为 `repytorch` 的 Conda 环境。它的解释器路径是：

```text
/opt/homebrew/Caskroom/miniforge/base/envs/repytorch/bin/python
```

## 运行本仓库代码

仓库示例按 `CUDA → MPS → CPU` 的顺序自动选择设备：

```bash
python tutorials/official_basics/01_tensors/walkthrough.py
python practice/fundamentals/01_tensor_autograd.py
```

在 M4 上成功启用 GPU 后，输出应包含：

```text
device: mps
```

张量的设备信息也可能显示为 `mps:0`。

以后编写模型时使用相同模式：

```python
if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

model = model.to(device)
inputs = inputs.to(device)
targets = targets.to(device)
```

模型和参与同一次运算的张量必须位于同一设备。

## 当前环境说明

此前直接运行 `python3` 时，实际使用的是系统中的全局 Python 3.10.0，而不是 `repytorch` Conda 环境。全局环境里的 PyTorch 虽然包含 MPS 支持，但在 Codex 执行进程中没有获得可用 MPS 设备。这个结果不能代表 `repytorch` 环境最终的 MPS 状态。

完成安装后，请在普通 macOS Terminal 或 VS Code 终端中运行：

```bash
conda activate repytorch
python scripts/check_mps.py
```

以这次结果作为本机开发环境的最终判断。

如果仍然是 `False`，依次检查：

```bash
uname -m
which python
python --version
python -m pip show torch
xcode-select -p
```

`uname -m` 应为 `arm64`，`which python` 应指向 `.../envs/repytorch/bin/python`。

## 使用边界

- 小张量的 MPS 运行可能因为调度开销而比 CPU 更慢，不能只用一个很小的例子判断性能。
- MPS 不支持 `float64` 张量；本项目默认使用 `float32`。
- 某些算子可能暂时不支持 MPS。确认是算子兼容问题后，可以临时使用 CPU，或用 `PYTORCH_ENABLE_MPS_FALLBACK=1` 允许不支持的算子回落到 CPU。
- MacBook Air 使用统一内存且没有风扇，长时间训练应控制 batch size；大型训练继续使用 RTX 5090。

## 环境管理规则

- 继续使用现有 `repytorch` 环境，不需要同时维护 `.venv`。
- 安装包前先确认 `conda activate repytorch` 和 `which python`。
- 使用 `python -m pip`，确保包进入当前 Conda 环境。
- 不要再通过另一种渠道重复安装同一个 PyTorch 包，以免文件相互覆盖。
