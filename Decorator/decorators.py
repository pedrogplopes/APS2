from component_interface import Milkshake

class IngredientDecorator(Milkshake):
    def __init__(self, milkshake):
        self.milkshake = milkshake
    
    def get_description(self):
        return self.milkshake.get_description()
    
    def get_cost(self):
        return self.milkshake.get_cost()

class ChocolateStraw(IngredientDecorator):
    def __init__(self, milkshake):
        super().__init__(milkshake)
    
    def get_description(self):
        return self.milkshake.get_description() + ", Canudinho de chocolate"
    
    def get_cost(self):
        return self.milkshake.get_cost() + 1.50

class Chocolate(IngredientDecorator):
    def __init__(self, milkshake):
        super().__init__(milkshake)
    
    def get_description(self):
        return self.milkshake.get_description() + ", Calda de chocolate"
    
    def get_cost(self):
        return self.milkshake.get_cost() + 1.0

class Cookie(IngredientDecorator):
    def __init__(self, milkshake):
        super().__init__(milkshake)
    
    def get_description(self):
        return self.milkshake.get_description() + ", Biscoitos Oreo"
    
    def get_cost(self):
        return self.milkshake.get_cost() + 2.0

class WhippedCream(IngredientDecorator):
    def __init__(self, milkshake):
        super().__init__(milkshake)
    
    def get_description(self):
        return self.milkshake.get_description() + ", Chantilly"
    
    def get_cost(self):
        return self.milkshake.get_cost() + 2.50