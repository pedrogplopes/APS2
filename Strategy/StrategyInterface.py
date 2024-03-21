from abc import ABC, abstractmethod

class StrategyInterface(ABC):
    @abstractmethod
    def apply_strategy(self):
        pass