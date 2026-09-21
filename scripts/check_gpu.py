"""Confirm that this Python environment can run a small PyTorch CUDA operation."""

import platform
import sys


def main() -> int:
    print(f"Python: {platform.python_version()} ({sys.executable})")

    try:
        import torch
    except (ImportError, OSError) as exc:
        print(f"Could not import PyTorch: {exc}", file=sys.stderr)
        print("Select the AutoDL image's Python interpreter in VS Code, then retry.", file=sys.stderr)
        return 1

    print(f"PyTorch: {torch.__version__}")
    print(f"PyTorch CUDA build: {torch.version.cuda or 'none'}")

    cuda_available = torch.cuda.is_available()
    print(f"CUDA available: {cuda_available}")
    if not cuda_available:
        print("CUDA is unavailable to this Python process.", file=sys.stderr)
        print(
            "On the AutoDL instance, check that the GPU is running (`nvidia-smi`) "
            "and that VS Code is using the image's CUDA-enabled PyTorch interpreter.",
            file=sys.stderr,
        )
        return 1

    device = torch.device("cuda:0")
    print(f"GPU: {torch.cuda.get_device_name(device)}")

    try:
        a = torch.randn(512, 512, device=device)
        b = torch.randn(512, 512, device=device)
        result = a @ b
        torch.cuda.synchronize(device)
        print(f"CUDA matrix multiplication: OK (512 x 512; mean={result.mean().item():.4f})")
    except RuntimeError as exc:
        print(f"CUDA calculation failed: {exc}", file=sys.stderr)
        print("Check `nvidia-smi` and the active Python/PyTorch environment.", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
