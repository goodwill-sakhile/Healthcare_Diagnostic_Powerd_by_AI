# tests/test_model.py

import torch

from medi_scan_ai.model_trainer import SimpleCNN

def test_simple_cnn_forward():
    model = SimpleCNN(num_classes=2)
    dummy_input = torch.rand(1, 3, 224, 224)
    output = model(dummy_input)
    assert output.shape == (1, 2)
