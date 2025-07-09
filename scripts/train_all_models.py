# scripts/train_all_models.py

"""
Train all MediScanAI models.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from medi_scan_ai.model_trainer import train_pneumonia_model  # Expand to others as you add them
from medi_scan_ai.image_loader import get_dataloader
from medi_scan_ai.utils import set_seed
from medi_scan_ai import config

def get_sample_data():
    """
    For demonstration: dummy image paths and labels.
    Replace with actual dataset loading.
    """
    image_paths = [os.path.join(config.SAMPLE_IMAGES_DIR, f) for f in os.listdir(config.SAMPLE_IMAGES_DIR)]
    labels = [0 for _ in image_paths]  # Dummy labels: 0 = Normal, 1 = Disease
    return image_paths, labels

def main():
    set_seed(config.SEED)
    print("Training Pneumonia Model...")
    image_paths, labels = get_sample_data()

    train_loader = get_dataloader(image_paths, labels, config.BATCH_SIZE)
    val_loader = None  # Add validation data loader if available

    train_pneumonia_model(train_loader, val_loader)

    # TODO: Add training calls for other diseases:
    # - Skin Cancer
    # - Retinopathy
    # - Brain Tumor
    # - Heart Disease

    print("All models trained and saved successfully!")

if __name__ == "__main__":
    main()
