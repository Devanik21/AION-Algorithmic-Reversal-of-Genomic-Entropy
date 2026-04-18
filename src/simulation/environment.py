"""
Environment Module.

Defines the spatial grid and resource distribution for the AION simulation.
"""

import numpy as np

class EnvironmentGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.resources = np.zeros((width, height))

    def diffuse(self):
        pass
