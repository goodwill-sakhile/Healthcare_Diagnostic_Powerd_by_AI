# medi_scan_ai/main.py

import argparse
import pandas as pd

from . import disease_predictor, outcome_predictor, utils

def main():
    utils.print_banner()

    parser = argparse.ArgumentParser(description="Run MediScanAI predictions.")
    parser.add_argument("--image_path", type=str, help="Path to image file.")
    parser.add_argument("--structured_data", type=str, help="Path to patient CSV.")
    parser.add_argument("--disease", type=str, choices=["pneumonia", "skin_cancer", "retinopathy", "brain_tumor", "heart_disease"])

    args = parser.parse_args()

    predictions = {}

    if args.image_path and args.disease != "heart_disease":
        result = disease_predictor.predict_image_disease(args.image_path, args.disease)
        print(f"{args.disease.title()} prediction: {result}")
        predictions[args.disease] = result

    if args.structured_data and args.disease == "heart_disease":
        df = pd.read_csv(args.structured_data)
        result = disease_predictor.predict_structured_data(df, args.disease)
        print(f"Heart Disease prediction: {result}")
        predictions[args.disease] = result

    if len(predictions) > 1:
        overall_risk = outcome_predictor.calculate_overall_risk(predictions)
        print(f"\nOverall Patient Risk: {overall_risk}")

if __name__ == "__main__":
    main()
