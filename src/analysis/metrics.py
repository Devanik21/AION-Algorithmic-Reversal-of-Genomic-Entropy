"""
Evolutionary Metrics Module.

Provides functions to compute fitness, diversity, and complexity
for populations within the AION simulation.
"""

def compute_population_fitness(population) -> float:
    """Compute mean fitness of a population."""
    if not population:
        return 0.0
    return sum(p.fitness for p in population) / len(population)
