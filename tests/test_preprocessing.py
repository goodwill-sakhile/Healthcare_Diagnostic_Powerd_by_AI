# tests/test_preprocessing.py

import os
import numpy as np
import pandas as pd

from medi_scan_ai import data_preprocessing, config

def test_preprocess_image():
    # Use a sample image
    sample_image = os.path.join(config.SAMPLE_IMAGES_DIR, os.listdir(config.SAMPLE_IMAGES_DIR)[0])
    image = data_preprocessing.preprocess_image(sample_image)
    assert isinstance(image, np.ndarray)
    assert image.shape == (config.IMAGE_HEIGHT, config.IMAGE_WIDTH, config.IMAGE_CHANNELS)
    assert image.max() <= 1.0

def test_augment_image():
    sample_image = np.random.rand(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, config.IMAGE_CHANNELS)
    augmented = data_preprocessing.augment_image(sample_image)
    assert augmented.shape == sample_image.shape

def test_preprocess_structured_data():
    data = {
        "age": [45, 50, None],
        "cholesterol": [200, None, 180],
        "blood_pressure": [120, 130, 140]
    }
    df = pd.DataFrame(data)
    processed_df = data_preprocessing.preprocess_structured_data(df)
    assert not processed_df.isnull().values.any()
    assert processed_df.shape == df.shape
