from component_interface import Milkshake

class VanillaMilkshake(Milkshake):
    def get_description(self):
        return "Milkshake de Baunilha"
    
    def get_cost(self):
        return 5.0

class ChocolateMilkshake(Milkshake):
    def get_description(self):
        return "Milkshake de Chocolate"
    
    def get_cost(self):
        return 6.0