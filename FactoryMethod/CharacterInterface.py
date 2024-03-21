from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def display(self):
        pass