# medi_scan_ai/outcome_predictor.py

from typing import Dict

def calculate_overall_risk(predictions: Dict[str, str]) -> str:
    """
    Aggregate multiple disease predictions into an overall risk category.
    :param predictions: Dict of disease: prediction.
    :return: Risk level.
    """
    positive_count = sum(1 for result in predictions.values() if result == "Positive")
    
    if positive_count == 0:
        return "Low Risk"
    elif 1 <= positive_count <= 2:
        return "Moderate Risk"
    else:
        return "High Risk"
