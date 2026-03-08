"""
Plant Disease Detection - Model Loading & Prediction
"""

import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

from classes import CLASS_NAMES, parse_label


def load_model(model_path="models/resnet50_plant.pth"):
    """Load the trained ResNet50 model with custom FC head."""
    model = models.resnet50(weights=None)
    num_ftrs = model.fc.in_features  # 2048
    model.fc = nn.Sequential(
        nn.Linear(num_ftrs, 512),
        nn.ReLU(),
        nn.Dropout(0.3),
        nn.Linear(512, 38),
    )
    model.load_state_dict(torch.load(model_path, map_location="cpu", weights_only=True))
    model.eval()
    return model


def preprocess_image(image_path):
    """Load and preprocess image for inference."""
    transform = transforms.Compose(
        [
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)


def predict(model, image_path):
    """Run prediction and return top-3 results."""
    input_tensor = preprocess_image(image_path)

    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = torch.softmax(outputs, dim=1)[0]

    top3_probs, top3_indices = torch.topk(probabilities, 3)
    results = []
    for prob, idx in zip(top3_probs, top3_indices):
        class_name = CLASS_NAMES[idx.item()]
        parsed = parse_label(class_name)
        results.append(
            {
                "class_name": class_name,
                "plant": parsed["plant"],
                "disease": parsed["disease"],
                "confidence": round(prob.item() * 100, 2),
            }
        )
    return results
