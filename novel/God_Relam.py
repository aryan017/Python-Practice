class world:
    def __init__(self,name):
        self.name=name

class divine_Region(world):
    def __init__(self,name,power_rank,profound_energy):
        super().__init__(name)
        self.power_rank=power_rank
        self.profound_energy=profound_energy
        