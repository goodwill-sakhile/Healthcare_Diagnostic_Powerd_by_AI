# medi_scan_ai/config.py

import os

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data directories
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, "data", "processed")
MODEL_DIR = os.path.join(BASE_DIR, "data", "models")
SAMPLE_IMAGES_DIR = os.path.join(BASE_DIR, "data", "sample_images")

# Image parameters
IMAGE_HEIGHT = 224
IMAGE_WIDTH = 224
IMAGE_CHANNELS = 3

# Training parameters
BATCH_SIZE = 32
EPOCHS = 20
LEARNING_RATE = 0.001

# Model names
MODEL_NAMES = {
    "pneumonia": "pneumonia_cnn.pth",
    "skin_cancer": "skin_cancer_cnn.pth",
    "retinopathy": "retinopathy_cnn.pth",
    "brain_tumor": "brain_tumor_cnn.pth",
    "heart_disease": "heart_disease_rf.pkl"
}

# Random seed
SEED = 42
