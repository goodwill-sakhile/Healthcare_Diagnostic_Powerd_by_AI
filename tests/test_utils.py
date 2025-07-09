# tests/test_utils.py

import numpy as np
import torch

from medi_scan_ai.utils import set_seed

def test_set_seed_reproducibility():
    set_seed(42)
    arr1 = np.random.rand(5)
    set_seed(42)
    arr2 = np.random.rand(5)
    assert np.allclose(arr1, arr2)

    set_seed(42)
    tensor1 = torch.rand(5)
    set_seed(42)
    tensor2 = torch.rand(5)
    assert torch.allclose(tensor1, tensor2)
