import sys
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from model import get_model


def test_resnet18_output_shape():
    model = get_model("resnet18", 10)
    batch = torch.randn(2, 3, 32, 32)
    output = model(batch)
    assert output.shape == (2, 10)
