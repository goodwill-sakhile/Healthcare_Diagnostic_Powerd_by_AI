# scripts/predict_patient.py

"""
Run prediction for structured patient data.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from medi_scan_ai.disease_predictor import predict_structured_data

def main():
    csv_path = input("Enter patient CSV file path: ")

    df = pd.read_csv(csv_path)
    result = predict_structured_data(df, "heart_disease")
    print(f"Heart Disease Prediction: {result}")

if __name__ == "__main__":
    main()
