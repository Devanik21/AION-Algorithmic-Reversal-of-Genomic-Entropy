import pytest
import numpy as np
from src.analysis.entropy import calculate_shannon_entropy

def test_entropy_uniform():
    probs = np.array([0.5, 0.5])
    entropy = calculate_shannon_entropy(probs)
    assert np.isclose(entropy, 1.0)

def test_entropy_deterministic():
    probs = np.array([1.0, 0.0])
    entropy = calculate_shannon_entropy(probs)
    assert np.isclose(entropy, 0.0)
