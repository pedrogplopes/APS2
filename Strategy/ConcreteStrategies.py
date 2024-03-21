from StrategyInterface import StrategyInterface

class AggressiveStrategy(StrategyInterface):
    def apply_strategy(self):
        print("Executando estratégia agressiva.")

class DefensiveStrategy(StrategyInterface):
    def apply_strategy(self):
        print("Executando estratégia defensiva.")

class StealthyStrategy(StrategyInterface):
    def apply_strategy(self):
        print("Executando estratégia furtiva.")
