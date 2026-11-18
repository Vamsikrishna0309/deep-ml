import torch

def linear_forward(x: torch.Tensor, W: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    return x @ W.T +b
    # TODO: implement y = x W^T + b using PyTorch ops
    pass
