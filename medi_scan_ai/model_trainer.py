# medi_scan_ai/model_trainer.py

import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm

from .image_loader import get_dataloader
from . import config

class SimpleCNN(nn.Module):
    """
    Example CNN model for image classification.
    """
    def __init__(self, num_classes: int = 2):
        super(SimpleCNN, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),

            nn.Conv2d(32, 64, kernel_size=3),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2)
        )
        self.classifier = nn.Sequential(
            nn.Linear(64 * 54 * 54, 128),
            nn.ReLU(inplace=True),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

def train_pneumonia_model(train_loader, val_loader):
    """
    Train a CNN for Pneumonia detection.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SimpleCNN().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=config.LEARNING_RATE)

    for epoch in range(config.EPOCHS):
        model.train()
        running_loss = 0.0
        for inputs, labels in tqdm(train_loader):
            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        avg_loss = running_loss / len(train_loader)
        print(f"Epoch [{epoch+1}/{config.EPOCHS}], Loss: {avg_loss:.4f}")

    # Save the model
    torch.save(model.state_dict(), f"{config.MODEL_DIR}/{config.MODEL_NAMES['pneumonia']}")
    print("Pneumonia model saved successfully.")
