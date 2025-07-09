# scripts/predict_image.py

"""
Run prediction for an image-based disease.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from medi_scan_ai.disease_predictor import predict_image_disease

def main():
    image_path = input("Enter image file path: ")
    disease = input("Enter disease to predict (e.g., pneumonia, skin_cancer, retinopathy, brain_tumor): ")

    result = predict_image_disease(image_path, disease)
    print(f"{disease.title()} Prediction: {result}")

if __name__ == "__main__":
    main()
