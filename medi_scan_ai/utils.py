# medi_scan_ai/utils.py

import random
import numpy as np
import torch

def set_seed(seed: int):
    """
    Set random seeds for reproducibility.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def print_banner():
    """
    Print a nice CLI banner.
    """
    print("=" * 50)
    print("  MediScanAI - AI-Powered Healthcare Diagnostics")
    print("=" * 50)
