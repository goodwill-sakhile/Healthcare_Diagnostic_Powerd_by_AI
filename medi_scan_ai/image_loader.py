# medi_scan_ai/image_loader.py

import os
from typing import List, Tuple

import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image

from . import config

class MedicalImageDataset(Dataset):
    """
    Custom dataset for loading medical images and labels.
    """

    def __init__(self, image_paths: List[str], labels: List[int]):
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transforms.Compose([
            transforms.Resize((config.IMAGE_HEIGHT, config.IMAGE_WIDTH)),
            transforms.ToTensor(),
        ])

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image = Image.open(self.image_paths[idx]).convert("RGB")
        image = self.transform(image)
        label = self.labels[idx]
        return image, label

def get_dataloader(image_paths: List[str], labels: List[int], batch_size: int, shuffle: bool = True) -> DataLoader:
    dataset = MedicalImageDataset(image_paths, labels)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
    return loader
