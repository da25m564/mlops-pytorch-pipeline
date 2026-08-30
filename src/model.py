import torch.nn as nn
from torchvision import models


def get_model(architecture: str = "resnet18", num_classes: int = 10) -> nn.Module:
    """Create a classification model for CIFAR-10."""
    architecture = architecture.lower()
    if architecture == "resnet18":
        model = models.resnet18(weights=None)
        # Better stem for 32x32 CIFAR-10 images.
        model.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1, bias=False)
        model.maxpool = nn.Identity()
        model.fc = nn.Linear(model.fc.in_features, num_classes)
        return model
    raise ValueError(f"Unsupported architecture: {architecture}")
