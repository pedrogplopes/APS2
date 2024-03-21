from CreateCharacterClass import CharacterFactory, AdeptFactory, EngineerFactory, VanguardFactory, InfiltratorFactory, SentinelFactory, SoldierFactory

class Client:
    def __init__(self):
        self.character_factories = []

    def add_factory(self, factory: CharacterFactory):
        self.character_factories.append(factory)

    def create_characters(self):
        for factory in self.character_factories:
            character = factory.create_character()
            character.display()

if __name__ == "__main__":
    client = Client()

    client.add_factory(AdeptFactory())
    client.add_factory(EngineerFactory())
    client.add_factory(VanguardFactory())
    client.add_factory(InfiltratorFactory())
    client.add_factory(SentinelFactory())
    client.add_factory(SoldierFactory())

    client.create_characters()