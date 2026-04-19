"""
Entropy Analysis Module.

Calculates Shannon Entropy and tracks information loss over time
within the GRN to quantify biological aging.
"""

import numpy as np

def calculate_shannon_entropy(probabilities: np.ndarray) -> float:
    """Calculate Shannon entropy for a given probability distribution."""
    # Add small epsilon to avoid log(0)
    probabilities = probabilities / np.sum(probabilities)
    eps = 1e-10
    prob_safe = np.clip(probabilities, eps, 1.0)
    return -np.sum(prob_safe * np.log2(prob_safe))
