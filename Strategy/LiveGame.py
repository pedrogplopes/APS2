from SetPlayerStrategy import SetPlayerStrategy
from ConcreteStrategies import DefensiveStrategy, AggressiveStrategy, StealthyStrategy

class LiveGame:
    def __init__(self):
        self.player1 = SetPlayerStrategy()
        self.player2 = SetPlayerStrategy()
        self.player3 = SetPlayerStrategy()

    def simulate_battle(self):
        print("Início de batalha:")
        print("Estratégia do Jogador 1:")
        self.player1.execute_strategy()
        print("Estratégia do Jogador 2:")
        self.player2.execute_strategy()
        print("Estratégia do Jogador 3:")
        self.player3.execute_strategy()

    def change_strategies(self):
        print("Mudando estratégias...")
        self.player1.set_strategy(DefensiveStrategy())
        self.player2.set_strategy(AggressiveStrategy())
        self.player3.set_strategy(StealthyStrategy())
        print("Novas estratégias:")
        print("Estratégia do Jogador 1:")
        self.player1.execute_strategy()
        print("Estratégia do Jogador 2:")
        self.player2.execute_strategy()
        print("Estratégia do Jogador 3:")
        self.player3.execute_strategy()
        print("Estratégia do Jogador 1:")
        self.player1.set_strategy(AggressiveStrategy())
        self.player1.execute_strategy()
        print("Estratégia do Jogador 2:")
        self.player2.set_strategy(DefensiveStrategy())
        self.player2.execute_strategy()
        print("Estratégia do Jogador 3:")
        self.player3.execute_strategy()

if __name__ == "__main__":
    game = LiveGame()
    game.simulate_battle()
    game.change_strategies()

""" Caso deseje incluir uma nova estratégia, é preciso criá-la em ConcreteStrategies, como:
class KamikazeStrategy(StrategyInterface):
    def apply_strategy(self): 
            print("Executando estratégia kamikaze.")

O jogador poderá então mudar sua estratégia com os comandos set e execute em LiveGame.
"""