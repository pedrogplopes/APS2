from abc import ABC, abstractmethod
from CharacterInterface import Character
from CharacterClass import Adept, Engineer, Vanguard, Infiltrator, Sentinel, Soldier

class CharacterFactory(ABC):
    @abstractmethod
    def create_character(self) -> Character:
        pass

class AdeptFactory(CharacterFactory):
    def create_character(self) -> Character:
        return Adept()

class EngineerFactory(CharacterFactory):
    def create_character(self) -> Character:
        return Engineer()

class VanguardFactory(CharacterFactory):
    def create_character(self) -> Character:
        return Vanguard()
    
class InfiltratorFactory(CharacterFactory):
    def create_character(self) -> Character:
        return Infiltrator()
    
class SentinelFactory(CharacterFactory):
    def create_character(self) -> Character:
        return Sentinel()
    
class SoldierFactory(CharacterFactory):
    def create_character(self) -> Character:
        return Soldier()