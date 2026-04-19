import pytest
import numpy as np
from src.models.grn import GeneticRegulatoryNetwork

def test_grn_initialization():
    grn = GeneticRegulatoryNetwork(10)
    assert grn.num_nodes == 10
    assert grn.state.shape == (10,)

def test_grn_reset():
    grn = GeneticRegulatoryNetwork(10)
    grn.state = np.ones(10)
    grn.reset_to_germline()
    assert np.all(grn.state == 0)
