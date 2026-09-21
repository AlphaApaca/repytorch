# 常用命令速查

本项目采用下面的工作流：**本机编写并推送代码，AutoDL 服务器拉取代码并运行**。

## 当前已验证环境

验证日期：2026-09-21

| 项目 | 实测值 |
| --- | --- |
| GPU | NVIDIA GeForce RTX 5090，32607 MiB |
| NVIDIA 驱动 | 580.105.08 |
| Python | 3.12.3，`/root/miniconda3/bin/python` |
| PyTorch | 2.12.1+cu130 |
| PyTorch CUDA 构建 | 13.0 |
| CUDA 可用 | `True` |

上述实测版本与最初选择镜像时记录的 PyTorch 2.8.0、CUDA 12.8 不同。当前解释器已经成功完成 CUDA 运算，因此后续以实测结果为准；这通常意味着镜像内容已更新，或者当前选择的是镜像中的另一个解释器。

## 一次完整自检

在 AutoDL 远端终端执行：

```bash
cd /root/autodl-tmp/repytorch
nvidia-smi
which python
python scripts/check_gpu.py
python exercises/01_tensor_autograd.py
```

## 每次学习最常用的流程

### 1. 本机修改完成后推送

以下命令在**本机终端**执行：

```bash
cd /Users/alpaca/workplace/repytorch
git status --short --branch
git diff
git add -A
git diff --cached
git commit -m "描述这次学习内容"
git push
```

如果 `git status` 显示没有变化，就不需要执行 `add`、`commit` 和 `push`。

### 2. 服务器拉取并运行

以下命令在 **AutoDL 远端终端**执行：

```bash
cd /root/autodl-tmp/repytorch
git status --short --branch
git pull --ff-only
python scripts/check_gpu.py
```

服务器只负责拉取和运行时，尽量不要直接修改代码，这样最不容易产生 Git 冲突。

## 连接与目录

从本机连接服务器：

```bash
ssh autodl-5090
```

在远端进入项目并确认位置：

```bash
cd /root/autodl-tmp/repytorch
pwd
ls -la
```

查看磁盘空间：

```bash
df -h /root/autodl-tmp
du -sh data datasets outputs runs logs checkpoints 2>/dev/null
```

## Git 检查

查看当前分支和文件变化：

```bash
git status --short --branch
```

查看最近 5 次提交：

```bash
git log --oneline -5
```

服务器拉取最新代码：

```bash
git pull --ff-only
```

如果服务器上的 `git status` 显示有本地修改，先检查这些修改，不要直接覆盖或重置。

## Python 与 GPU 检查

查看 GPU、Python 和 PyTorch：

```bash
nvidia-smi
which python
python --version
python -m pip show torch
python scripts/check_gpu.py
```

持续观察 GPU，每秒刷新一次：

```bash
watch -n 1 nvidia-smi
```

按 `Ctrl+C` 退出监控。

如果空闲时偶尔看到 `GPU-Util 100%`、显存为 0 且没有进程，可能只是采样时序或宿主机活动。用上面的命令连续观察；如果长时间保持 100%，再检查 AutoDL 实例状态。

GPU 检查脚本的关键成功标志：

```text
CUDA available: True
GPU: NVIDIA GeForce RTX 5090
CUDA matrix multiplication: OK
```

`nvidia-smi` 中的 CUDA Version 表示驱动支持的 CUDA 版本；`torch.version.cuda` 表示当前 PyTorch 构建使用的 CUDA 版本。

## 运行练习

运行第一课：

```bash
cd /root/autodl-tmp/repytorch
python exercises/01_tensor_autograd.py
```

当前练习的关键正确结果：

```text
device: cuda
loss: 34.0
w.grad: tensor([3., 5., 7.], device='cuda:0')
梯度核对通过
```

以后运行其他练习：

```bash
python exercises/<练习文件名>.py
```

## 用 tmux 运行较长任务

创建名为 `train` 的会话：

```bash
tmux new -s train
```

在会话里启动程序，例如：

```bash
python train.py
```

暂时离开但让程序继续运行：先按 `Ctrl+B`，松开后再按 `D`。

查看已有会话：

```bash
tmux ls
```

重新进入：

```bash
tmux attach -t train
```

程序结束后关闭该会话：

```bash
tmux kill-session -t train
```

tmux 可以防止 SSH 断开导致任务退出，但不能让任务跨越实例关机、重启或释放继续运行。

## 常用终止操作

| 操作 | 按键 |
| --- | --- |
| 停止当前前台程序 | `Ctrl+C` |
| 退出 `watch` | `Ctrl+C` |
| 离开 tmux 但保持任务运行 | `Ctrl+B`，然后按 `D` |
| 退出 SSH 终端 | `exit` |
