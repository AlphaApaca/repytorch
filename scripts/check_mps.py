"""Check whether this Python environment can use Apple Metal through PyTorch MPS."""

import platform
import sys


def main() -> int:
    print(f"Machine: {platform.machine()}")
    print(f"macOS: {platform.mac_ver()[0]}")
    print(f"Python: {platform.python_version()} ({sys.executable})")

    try:
        import torch
    except (ImportError, OSError) as exc:
        print(f"Could not import PyTorch: {exc}", file=sys.stderr)
        print("Activate the project's .venv and install PyTorch, then retry.", file=sys.stderr)
        return 1

    print(f"PyTorch: {torch.__version__}")
    print(f"MPS built: {torch.backends.mps.is_built()}")
    print(f"MPS available: {torch.backends.mps.is_available()}")

    if not torch.backends.mps.is_available():
        print(
            "MPS is unavailable to this Python process. Run this script again from "
            "a normal Terminal or VS Code terminal, then check the active interpreter.",
            file=sys.stderr,
        )
        return 1

    device = torch.device("mps")
    try:
        a = torch.randn(512, 512, device=device)
        b = torch.randn(512, 512, device=device)
        result = a @ b
        torch.mps.synchronize()
        print(f"MPS matrix multiplication: OK (512 x 512; mean={result.mean().item():.4f})")
    except RuntimeError as exc:
        print(f"MPS calculation failed: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
