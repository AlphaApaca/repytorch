"""PyTorch 官方 Tensors 教程的个人最小复现。

Source: https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html
Reviewed: 2026-09-21
Target remote environment: PyTorch 2.12.1+cu130 on RTX 5090.
"""

import torch
import numpy as np

def select_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def main() -> None:
    device = select_device()

    x = torch.arange(12, dtype=torch.float32, device=device).reshape(3, 4)
    offset = torch.tensor([10.0, 20.0, 30.0, 40.0], device=device)
    shifted = x + offset

    weights = torch.arange(8, dtype=torch.float32, device=device).reshape(4, 2)
    projected = x @ weights

    print(f"device: {x.device}")
    print(f"shape={tuple(x.shape)}, dtype={x.dtype}")
    print(f"second row: {x[1]}")
    print(f"broadcast result:\n{shifted}")
    print(f"matrix product shape: {tuple(projected.shape)}")
    print(f"matrix product:\n{projected}")

    expected_shifted = torch.tensor(
        [
            [10.0, 21.0, 32.0, 43.0],
            [14.0, 25.0, 36.0, 47.0],
            [18.0, 29.0, 40.0, 51.0],
        ],
        device=device,
    )
    expected_projected = torch.tensor(
        [[28.0, 34.0], [76.0, 98.0], [124.0, 162.0]],
        device=device,
    )
    torch.testing.assert_close(shifted, expected_shifted)
    torch.testing.assert_close(projected, expected_projected)
    print("张量形状、广播和矩阵乘法核对通过。")


if __name__ == "__main__":
    main()
