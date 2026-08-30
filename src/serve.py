import io
import os
from pathlib import Path

import torch
import torch.nn.functional as F
from fastapi import FastAPI, File, HTTPException, UploadFile
from PIL import Image
from torchvision import transforms

from model import get_model

app = FastAPI(title="CIFAR-10 Model Serving", version="1.0")
MODEL_PATH = Path(os.getenv("MODEL_PATH", "/app/checkpoints/classifier_v1.pt"))
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = None
class_names = []

transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.4914, 0.4822, 0.4465],
        std=[0.2470, 0.2435, 0.2616],
    ),
])


@app.on_event("startup")
def load_model() -> None:
    global model, class_names
    if not MODEL_PATH.exists():
        model = None
        return
    checkpoint = torch.load(MODEL_PATH, map_location=DEVICE, weights_only=False)
    model = get_model(
        checkpoint.get("architecture", "resnet18"),
        checkpoint.get("num_classes", 10),
    )
    model.load_state_dict(checkpoint["model_state_dict"])
    model.to(DEVICE)
    model.eval()
    class_names = checkpoint.get("class_names", [str(i) for i in range(10)])


@app.get("/health")
def health():
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "ok", "model_loaded": True}


@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    try:
        raw = await image.read()
        pil_image = Image.open(io.BytesIO(raw)).convert("RGB")
        tensor = transform(pil_image).unsqueeze(0).to(DEVICE)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Invalid image: {exc}") from exc

    with torch.no_grad():
        probabilities = F.softmax(model(tensor), dim=1).squeeze(0).cpu().tolist()

    best_idx = int(max(range(len(probabilities)), key=probabilities.__getitem__))
    return {
        "predicted_class": class_names[best_idx],
        "probabilities": {name: round(float(prob), 6) for name, prob in zip(class_names, probabilities)},
    }
