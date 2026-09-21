# PyTorch 基础复习

目标：把官方教程里的知识点变成自己能解释、能从空文件写出、能定位错误的小程序。当前项目从零开始，针对 AutoDL 的 RTX 5090、PyTorch 2.8.0、Python 3.12、CUDA 12.8 环境。

## 1. 从本机 VS Code 连接 AutoDL

1. 在 AutoDL 控制台启动实例，复制实例页面给出的 **SSH 登录命令、主机、端口和密码**。端口以控制台显示的为准，不要默认用 22。
2. 在本机 VS Code 安装 Microsoft 的 **Remote - SSH** 扩展。按 `⌘⇧P`，运行 `Remote-SSH: Add New SSH Host...`，粘贴 AutoDL 给出的 SSH 命令，并存入 `~/.ssh/config`。也可以自行写入：

   ```sshconfig
   Host autodl-5090
       HostName <控制台给出的主机>
       User root
       Port <控制台给出的端口>
   ```

3. 以下命令以 `autodl-5090` 作为 SSH 别名。如果直接粘贴了控制台的登录命令，先把 VS Code 生成的 `Host` 改成这个别名，并核对 `HostName`、`Port`。在本机终端运行 `ssh autodl-5090` 测试，再用 `Remote-SSH: Connect to Host...` 选择该别名。首次连接时核对主机信息，选择远端系统 **Linux**，按提示输入密码。
4. 连接后，左下角应显示 `SSH: autodl-5090`。此时 VS Code 的终端和文件浏览器都在远端。本机目录不会自动出现在远端。

连接细节可参考 [AutoDL 的 VS Code 教程](https://www.autodl.com/docs/vscode/)和 [VS Code Remote SSH 文档](https://code.visualstudio.com/docs/remote/ssh)。

### 把这份项目放到远端

在**本机终端**运行（下面的路径是当前这份项目在本机的位置）：

```bash
ssh autodl-5090 'mkdir -p /root/autodl-tmp/repytorch'
scp -r /Users/alpaca/workplace/repytorch/. autodl-5090:/root/autodl-tmp/repytorch/
```

然后在远端 VS Code 运行 `File: Open Folder...`，打开 `/root/autodl-tmp/repytorch`。AutoDL 将 `/root/autodl-tmp` 用作数据目录，实例关机通常仍保留数据，但实例释放后数据会清空；重要代码和笔记要同步到本机或自己的 Git 仓库。
上面的 `scp` 用于首次上传；之后若在远端修改了文件，先把新内容同步回本机，避免再次上传旧文件覆盖练习成果。

上传命令与目录规则见 [AutoDL SCP 文档](https://www.autodl.com/docs/scp/)和[实例数据说明](https://www.autodl.com/docs/instance_data/)。

### 日常同步怎么选

Remote SSH 打开远端目录后，保存文件就是直接写入服务器，因此不需要持续同步才能运行代码。建议把远端作为训练期间的工作目录，并用 Git 保存代码历史；数据集、模型权重和训练输出留在 `/root/autodl-tmp`，不要提交到 Git。

需要手动传输时，`scp` 适合偶尔整包复制；`rsync` 只传变化内容，更适合日常备份。已在 `~/.ssh/config` 配好 `autodl-5090` 后，可以先预览一次从本机到远端的同步：

```bash
rsync -avhn \
  --exclude '.git/' \
  --exclude '.venv/' \
  --exclude '__pycache__/' \
  --exclude 'data/' \
  --exclude 'datasets/' \
  --exclude 'outputs/' \
  --exclude 'runs/' \
  --exclude 'logs/' \
  --exclude 'checkpoints/' \
  --exclude 'wandb/' \
  /Users/alpaca/workplace/repytorch/ \
  autodl-5090:/root/autodl-tmp/repytorch/
```

确认预览结果后去掉 `n`，即把 `-avhn` 改为 `-avh` 执行。把远端练习备份回本机时交换源和目标：

```bash
rsync -avhn \
  --exclude '.git/' \
  --exclude '.venv/' \
  --exclude '__pycache__/' \
  --exclude 'data/' \
  --exclude 'datasets/' \
  --exclude 'outputs/' \
  --exclude 'runs/' \
  --exclude 'logs/' \
  --exclude 'checkpoints/' \
  --exclude 'wandb/' \
  autodl-5090:/root/autodl-tmp/repytorch/ \
  /Users/alpaca/workplace/repytorch/
```

同样先预览，再去掉 `n`。路径末尾的 `/` 表示同步目录里的内容。这里没有使用 `--delete`，因此不会因为源端缺少某个文件而自动删除目标端文件。不要同时在两端修改同一文件后直接运行 `rsync`；它不会像 Git 那样合并冲突。

如果没有配置 SSH 别名，一次性上传也可以直接使用 AutoDL 给出的主机和端口：

```bash
scp -rP <端口> \
  /Users/alpaca/workplace/repytorch/. \
  root@<主机>:/root/autodl-tmp/repytorch/
```

`scp` 的端口参数是大写 `-P`。密码只在终端提示处输入，不要写入项目文件。

若本机和远端都可能编辑代码，使用私有 Git 仓库会更可靠：Git 记录历史并在两边发生不同修改时明确报告冲突。当前项目还没有初始化 Git；准备好远端仓库后，可在本机初始化并推送，再在服务器的空目录中克隆。`.gitignore` 已排除数据集、训练输出和常见模型权重。

### 在远端 VS Code 使用 Codex

先连接 Remote SSH 并打开 `/root/autodl-tmp/repytorch`，再在这个远端窗口的扩展面板搜索 **Codex – OpenAI's coding agent**。如果出现 `Install in SSH: autodl-5090`，点击它；VS Code 会把需要访问远端工作区的扩展装到远端扩展主机。随后运行 `Codex: Open Codex Sidebar` 并按提示登录。

可以用一个只读请求检查执行位置：`请只运行 pwd、which python 和 nvidia-smi，不要修改文件。` 输出应指向 `/root/autodl-tmp/repytorch`，并看到远端 Python 和 5090。Codex 默认使用云端模型；5090 只会在运行你的 PyTorch 程序时被使用，并不会因为安装扩展而用来运行 Codex 模型。

直接远端使用时，远端实例需要能完成扩展安装、登录并访问 Codex 服务；本机的网络代理不会由 SSH 自动转发。如果远端网络不满足条件，可以让 Codex 编辑本机项目，再通过 Git 或上面的 `rsync` 将代码传到服务器运行。

在远端 VS Code 安装 **Python** 扩展；如果使用 `.ipynb`，再安装 **Jupyter** 扩展。运行 `Python: Select Interpreter`，选择下方 `which python` 返回的路径，避免 VS Code 选到另一个 Python 环境。

## 2. 检查确实在用 5090

在 VS Code 的**远端终端**中运行：

```bash
cd /root/autodl-tmp/repytorch
nvidia-smi
which python
python scripts/check_gpu.py
```

期望看到 PyTorch 2.8.0、PyTorch 构建对应的 CUDA 12.8、`CUDA available: True`，以及 RTX 5090 的设备名称；脚本还会实际在 GPU 上做一次矩阵乘法。`nvidia-smi` 显示的 CUDA Version 是驱动支持的版本，不要求与 `torch.version.cuda` 的数字完全相同。

若 GPU 检查失败，先比较远端终端的 `which python` 与 VS Code 选中的解释器，再看 `nvidia-smi` 和 `python -m pip show torch`。确认问题之前，不要覆盖镜像里预装的 PyTorch。

## 3. 第一站：张量与自动求导

先读官方教程的 [Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html) 和 [Automatic Differentiation](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)，随后运行：

```bash
python exercises/01_tensor_autograd.py
```

这个例子计算 `y = x @ w` 和 `loss = y.sum()`。运行前先猜出 `x`、`w`、`y` 的形状，以及 `w.grad` 的三个值；运行后解释为什么梯度等于 `x` 各列之和。再尝试：

- 把 `w` 改成形状为 `(3, 2)` 的矩阵，预测新的 `y.shape` 和梯度形状。
- 重新执行前向计算得到新的 `loss`，再调用一次 `backward()`，观察梯度累加；用 `w.grad.zero_()` 清空梯度后重复。不要直接对同一个计算图连续调用两次 `backward()`。
- 故意让 `x` 在 CPU、`w` 在 GPU，阅读设备不一致的报错并修复。

## 4. 后续复习顺序

以官方 [Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/) 为主线，每学一个主题就写一个最小例子，并在笔记中回答“输入形状、输出形状、设备、梯度从哪里来”。
教程网站会更新；遇到版本差异时，查 [PyTorch 2.8 API 文档](https://docs.pytorch.org/docs/2.8/index.html)。

| 阶段 | 内容 | 练习产出 |
| --- | --- | --- |
| 1 | Tensor、形状、广播、索引、设备、autograd | 用纸笔和代码核对一次矩阵乘法的梯度 |
| 2 | `Dataset`、`DataLoader`、批处理与数据划分 | 自己写一个小型 `Dataset`，打印一个 batch 的形状 |
| 3 | `nn.Module`、损失函数、优化器、训练循环 | 不看教程写出 `zero_grad → forward → loss → backward → step` |
| 4 | 验证与推理、`train()`/`eval()`、`inference_mode()` | 对比训练和验证流程，记录指标 |
| 5 | `state_dict` 保存和加载、复现 | 重新加载模型并核对同一输入的预测 |
| 6 | 完整小项目与面试复述 | 独立完成一个分类任务，解释每个设计选择和常见错误 |

对应的官方章节：[Data](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html) → [Build Model](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html) → [Optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) → [Save & Load](https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html)。刚开始用小数据和小模型即可；5090 主要用于确认设备使用正确、稍后体验训练速度和显存管理。

每一阶段建议留下一份可运行代码和一页自己的解释。面试前重点检查：梯度为什么会累加、`zero_grad()` 放在哪里、模型和数据如何迁移到同一设备、验证时为何调用 `eval()` 和关闭梯度、如何保存与恢复参数。
