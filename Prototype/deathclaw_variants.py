from deathclaw_enemy import Deathclaw
import copy

class Regular(Deathclaw):
    def __init__(self):
        super().__init__()

    def clone(self):
        return copy.deepcopy(self)

class Legendary(Deathclaw):
    def __init__(self):
        super().__init__()
        self.variant = "Legendary Deathclaw"
        self.hp = 1000
        self.melee = 250

    def clone(self):
        return copy.deepcopy(self)


class Young(Deathclaw):
    def __init__(self):
        super().__init__()
        self.variant = "Young Deathclaw"
        self.hp = 350
        self.melee = 40

    def clone(self):
        return copy.deepcopy(self)


class Mother(Deathclaw):
    def __init__(self):
        super().__init__()
        self.variant = "Deathclaw Mother"
        self.hp = 700
        self.melee = 275

    def clone(self):
        return copy.deepcopy(self)


class Irradiated(Deathclaw):
    def __init__(self):
        super().__init__()
        self.variant = "Irradiated Deathclaw"
        self.hp = 550
        self.melee = 187

    def clone(self):
        return copy.deepcopy(self)
