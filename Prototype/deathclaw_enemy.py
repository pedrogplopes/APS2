from abc import ABCMeta, abstractmethod

class Deathclaw(metaclass=ABCMeta):
    def __init__(self):
        self.variant = "Deathclaw"
        self.hp = 500
        self.melee = 125

    @abstractmethod
    def clone(self):
        pass
