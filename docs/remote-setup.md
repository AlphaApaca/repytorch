# VS Code、AutoDL 与 Git 工作流

## 1. 用 VS Code 连接服务器

在 AutoDL 控制台复制实例提供的 SSH 主机、端口、用户名和密码。在本机安装 VS Code 的 **Remote - SSH** 扩展，然后把连接写入 `~/.ssh/config`：

```sshconfig
Host autodl-5090
    HostName <AutoDL 控制台给出的主机>
    User root
    Port <AutoDL 控制台给出的端口>
```

先在本机终端验证：

```bash
ssh autodl-5090
```

随后在 VS Code 中运行 `Remote-SSH: Connect to Host...`，选择 `autodl-5090`，并打开：

```text
/root/autodl-tmp/repytorch
```

连接后，VS Code 左下角会显示远端 SSH 状态。远端窗口里的终端、Python 扩展和文件浏览器都操作服务器文件。

参考：[AutoDL VS Code 教程](https://www.autodl.com/docs/vscode/)；[VS Code Remote SSH 文档](https://code.visualstudio.com/docs/remote/ssh)。

## 2. 代码同步

本项目采用下面的日常工作流：

```text
本机编辑 → git commit → git push → AutoDL 上 git pull → 使用 5090 运行
```

本机：

```bash
cd /Users/alpaca/workplace/repytorch
git status --short --branch
git add -A
git commit -m "描述本次学习内容"
git push
```

AutoDL：

```bash
cd /root/autodl-tmp/repytorch
git status --short --branch
git pull --ff-only
```

服务器主要用于拉取和运行，可以显著减少两端同时编辑造成的冲突。拉取前若 `git status` 显示服务器存在修改，先检查并保存这些修改。

偶尔传输单个文件时可以使用 `scp`：

```bash
scp -P <端口> <本机文件> root@<主机>:/root/autodl-tmp/repytorch/
```

数据集、权重和训练输出留在服务器的数据盘，并定期保存真正需要保留的结果；这些大文件已经被 `.gitignore` 排除。

## 3. Python 与 GPU

远端当前实测解释器为 `/root/miniconda3/bin/python`。在远端 VS Code 安装 Python 扩展，运行 `Python: Select Interpreter` 并选择该路径。

```bash
cd /root/autodl-tmp/repytorch
nvidia-smi
which python
python scripts/check_gpu.py
```

成功标志包括：

```text
CUDA available: True
GPU: NVIDIA GeForce RTX 5090
CUDA matrix multiplication: OK
```

`nvidia-smi` 显示驱动能够支持的 CUDA 版本，`torch.version.cuda` 显示当前 PyTorch 构建使用的 CUDA 版本，两者可以不同。

## 4. Codex 的使用位置

当前服务器登录 Codex 时返回地区不受支持的 403 错误，因此保留“Codex 在本机修改仓库，Git 将代码送到服务器运行”的方式。5090 用于运行 PyTorch 代码；Codex 模型由服务端运行。

更完整的日常命令见 [`COMMANDS.md`](../COMMANDS.md)。
