import pytest
import sys
import os

# Add the parent directory to the path so we can import AIoN
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_imports():
    """Test that all required modules can be imported."""
    try:
        import streamlit
        import numpy
        import pandas
        import plotly
        import scipy
        import networkx
        import tinydb
        import matplotlib
        import sklearn
        import seaborn
        import pydot
    except ImportError as e:
        pytest.fail(f"Failed to import a required module: {e}")

def test_aion_import():
    """Test that the main AIoN module can be imported."""
    try:
        import AIoN
    except ImportError as e:
        pytest.fail(f"Failed to import AIoN: {e}")
