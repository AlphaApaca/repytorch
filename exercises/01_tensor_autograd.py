"""第一天：用一个小例子检查张量形状、设备和自动求导。"""

import torch


def main() -> None:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    x = torch.arange(6, dtype=torch.float32, device=device).reshape(2, 3)
    w = torch.tensor([1.0, 2.0, 3.0], device=device, requires_grad=True)

    y = x @ w
    loss = y.sum()
    loss.backward()

    print(f"device: {device}")
    print(f"x.shape: {tuple(x.shape)}")
    print(f"w.shape: {tuple(w.shape)}")
    print(f"y.shape: {tuple(y.shape)}")
    print(f"loss: {loss.item():.1f}")
    print(f"w.grad: {w.grad}")

    expected_grad = x.sum(dim=0)
    torch.testing.assert_close(w.grad, expected_grad)
    print("梯度核对通过：w.grad 等于 x 每一列的和。")


if __name__ == "__main__":
    main()
