"""
Phenotype Module.

Defines the physical manifestation of the Genetic Regulatory Network,
including somatic cells and tissue organization.
"""

class Phenotype:
    def __init__(self, grn):
        self.grn = grn
        self.age = 0
        self.health = 1.0

    def age_tick(self):
        """Advance the age and apply entropic decay."""
        self.age += 1
        self.health *= 0.999
