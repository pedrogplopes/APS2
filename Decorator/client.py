from concrete_components import VanillaMilkshake, ChocolateMilkshake
from decorators import ChocolateStraw, Chocolate, Cookie, WhippedCream

class Cliente:
    @staticmethod
    def create_milkshake(milkshake_base, *ingredientes):
        milkshake = milkshake_base
        for ingrediente in ingredientes:
            milkshake = ingrediente(milkshake)
        return milkshake

if __name__ == "__main__":
    # Criando milkshake de baunilha com canudinho de chocolate e chantilly
    milkshake1 = Cliente.create_milkshake(VanillaMilkshake(), ChocolateStraw, WhippedCream)
    print("Descrição:", milkshake1.get_description())
    print("Valor:", milkshake1.get_cost())
    print()

    # Criando milkshake de chocolate com canudinho de chocolate, calda de chocolate e biscoitos Oreo
    milkshake2 = Cliente.create_milkshake(ChocolateMilkshake(), ChocolateStraw, Chocolate, Cookie)
    print("Descrição:", milkshake2.get_description())
    print("Valor:", milkshake2.get_cost())