import pytest
from src.simulation.engine import SimulationEngine

def test_simulation_run():
    engine = SimulationEngine({"max_ticks": 10})
    engine.run(5)
    assert engine.tick == 5
