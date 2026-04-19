#!/usr/bin/env python3
"""
Script to run a standard aging simulation.
"""

import sys
import argparse
from src.simulation.engine import SimulationEngine

def main():
    parser = argparse.ArgumentParser(description="Run AION aging simulation.")
    parser.add_argument("--ticks", type=int, default=1000, help="Number of ticks to run.")
    args = parser.parse_args()

    print(f"Starting simulation for {args.ticks} ticks...")
    engine = SimulationEngine({})
    engine.run(args.ticks)
    print("Simulation complete.")

if __name__ == "__main__":
    main()
