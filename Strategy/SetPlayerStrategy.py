class SetPlayerStrategy:
    def __init__(self):
        self.player_strategy = None

    def set_strategy(self, strategy):
        self.player_strategy = strategy

    def execute_strategy(self):
        if self.player_strategy:
            self.player_strategy.apply_strategy()
        else:
            print("Nenhuma estratégia executada.")
