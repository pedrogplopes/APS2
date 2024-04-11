from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def perform_action(self) -> None:
        pass
