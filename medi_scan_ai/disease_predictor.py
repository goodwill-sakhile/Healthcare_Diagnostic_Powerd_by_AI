# medi_scan_ai/disease_predictor.py

import os
import torch
import torch.nn as nn
from PIL import Image
from torchvision import transforms

import joblib
import numpy as np
import pandas as pd

from .model_trainer import SimpleCNN
from . import config

def predict_image_disease(image_path: str, disease: str) -> str:
    """
    Predict disease from a single image.
    :param image_path: Path to the image file.
    :param disease: Disease name (must match MODEL_NAMES key).
    :return: Predicted class label.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SimpleCNN()
    model.load_state_dict(torch.load(
        os.path.join(config.MODEL_DIR, config.MODEL_NAMES[disease]), 
        map_location=device
    ))
    model.eval()

    transform = transforms.Compose([
        transforms.Resize((config.IMAGE_HEIGHT, config.IMAGE_WIDTH)),
        transforms.ToTensor(),
    ])

    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)

    return "Positive" if predicted.item() == 1 else "Negative"

def predict_structured_data(df: pd.DataFrame, disease: str) -> str:
    """
    Predict disease risk from structured data.
    Example: Heart Disease.
    """
    model_path = os.path.join(config.MODEL_DIR, config.MODEL_NAMES[disease])
    model = joblib.load(model_path)

    prediction = model.predict(df)
    return "Positive" if prediction[0] == 1 else "Negative"
