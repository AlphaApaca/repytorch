---
publish: true
date: 2026-10-02
category: note
tags: [PyTorch, DataLoader]
summary: "Dataset 与 DataLoader 的职责小记"
comments: true
---

# Datasets & DataLoaders

## 一句话解释

**Dataset** stores the samples and their corresponding labels, and **DataLoader** wraps an iterable around the Dataset to enable easy access to the samples.

Code for processing data samples can get messy and hard to maintain; we ideally want our dataset code to be decoupled from our model training code for better readability and modularity. Thus, PyTorch provides these two data primitives: **torch.utils.data.DataLoader** and **torch.utils.data.Dataset** that allow you to use pre-loaded datasets as well as your own data.

## 最小例子
```python
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import v2
import matplotlib.pyplot as plt

training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)])
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)])
)
```

```python
from torch.utils.data import DataLoader

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)
```

## 小巧思
### 我加载数据集时这个root="data"具体地址会是什么位置？需要我将数据集放置在项目的目录中吗？还是在环境中的目录下？
root="data" 是一个相对路径，它相对于你运行 Python 命令时所在的当前工作目录

### dataset可视化过程中的代码具体含义是？
```python
# Iterating and Visualizing the Dataset
labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}
figure = plt.figure(figsize=(8, 8)) # 创建一个宽 8 英寸、高 8 英寸的画布
cols, rows = 3, 3 #准备把画布划分为3 行 × 3 列 = 9 个位置
for i in range(1, cols * rows + 1): # 循环生成9个子图
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray") # 显示灰度照片
plt.show() #显示完整画布
```
从 FashionMNIST 训练集中随机选出 9 张图片，以 3 × 3 网格显示，并在每张图片上方标注服装类别。
FashionMNIST 中的标签是 0～9 的数字。这个字典用于将数字转换为便于阅读的类别名称
```python
labels_map[0]  # "T-Shirt"
labels_map[8]  # "Bag"
```
imshow()：显示图片
img.squeeze()：将图片变成 (28, 28)
cmap="gray"：使用灰度色彩映射
### size=(1,)是什么意思
```python
size=(1,)
```
`size` 是 `torch.randint()` 的关键字参数，`(1,)` 是一个**只有一个元素的元组**，用来指定输出 Tensor 的形状。
```python
torch.randint(len(training_data), size=(1,))
```
意思是：
> 随机生成一个形状为 `(1,)`、只包含一个随机整数的 Tensor。
例如：
```python
x = torch.randint(10, size=(1,))
print(x)
# tensor([7])
print(x.shape)
# torch.Size([1])
```
#### 为什么 `(1,)` 后面有逗号？
在 Python 中，单元素元组必须保留逗号：
```python
a = (1)
print(type(a))
# <class 'int'>
```
这里的 `(1)` 只是加了括号的整数。
而：
```python
a = (1,)
print(type(a))
# <class 'tuple'>
```
才是单元素元组。
因此：
```text
(1)  → 整数 1
(1,) → 只包含整数 1 的元组
```
#### `size` 决定输出形状
```python
torch.randint(10, size=(1,))
```
生成一维 Tensor，包含 1 个随机数：
```text
tensor([7])       shape=(1,)
```
```python
torch.randint(10, size=(3,))
```
生成一维 Tensor，包含 3 个随机数：
```text
tensor([7, 2, 9]) shape=(3,)
```
```python
torch.randint(10, size=(2, 3))
```
生成一个 2 行 3 列的二维 Tensor：
```text
tensor([
    [7, 2, 9],
    [1, 4, 6]
])
```
形状是：
```python
torch.Size([2, 3])
```
#### `.item()` 的作用
原始结果是一个只包含一个元素的 Tensor：
```python
sample_idx_tensor = torch.randint(
    len(training_data),
    size=(1,)
)
print(sample_idx_tensor)
# tensor([25137])
```
调用：
```python
sample_idx = sample_idx_tensor.item()
```
会将它转换为普通 Python 整数：
```python
print(sample_idx)
# 25137
print(type(sample_idx))
# <class 'int'>
```
所以完整代码：
```python
sample_idx = torch.randint(
    len(training_data),
    size=(1,)
).item()
```
可以理解为：
```text
生成一个随机整数 Tensor
        ↓
tensor([25137])
        ↓ .item()
普通 Python 整数 25137
```
之所以转换成普通整数，是因为它接下来要作为数据集索引：
```python
img, label = training_data[sample_idx]
```
另外也可以直接生成零维 Tensor：
```python
sample_idx = torch.randint(
    len(training_data),
    size=()
).item()
```
但教程使用 `size=(1,)` 更直观地表达“生成一个随机数”。

## 仍不确定的问题

创建datasets时的getitem具体发生了什么？
```python
class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = decode_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
```
transform具体是什么？