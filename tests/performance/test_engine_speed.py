import time
from src.simulation.engine import SimulationEngine

def test_engine_speed():
    engine = SimulationEngine({})
    start = time.time()
    engine.run(100)
    duration = time.time() - start
    assert duration < 1.0 # Should be very fast
