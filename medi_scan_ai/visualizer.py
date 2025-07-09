# medi_scan_ai/visualizer.py

import numpy as np
import matplotlib.pyplot as plt

def show_image(image: np.ndarray, title: str = "Image"):
    """
    Display an image.
    """
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.show()

def plot_prediction_distribution(predictions: dict):
    """
    Plot a pie chart of disease prediction results.
    """
    labels = predictions.keys()
    sizes = [1 if val == "Positive" else 0 for val in predictions.values()]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.title("Disease Prediction Distribution")
    plt.show()
