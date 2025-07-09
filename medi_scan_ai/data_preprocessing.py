# medi_scan_ai/data_preprocessing.py

import cv2
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from . import config

def preprocess_image(image_path: str) -> np.ndarray:
    """
    Load and preprocess a single image.
    """
    image = cv2.imread(image_path)
    image = cv2.resize(image, (config.IMAGE_WIDTH, config.IMAGE_HEIGHT))
    image = image / 255.0  # Normalize to [0,1]
    return image

def augment_image(image: np.ndarray) -> np.ndarray:
    """
    Apply basic augmentation: flip, rotate, etc.
    """
    flipped = cv2.flip(image, 1)  # Horizontal flip
    return flipped

def preprocess_structured_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess structured patient data: handle missing values, scale.
    """
    df = df.fillna(df.mean())
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df)
    return pd.DataFrame(scaled_features, columns=df.columns)
