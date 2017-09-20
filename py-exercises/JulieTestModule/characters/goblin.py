from characters.base import Character

class Goblin(Character):
    def __init__(self, name = 'Goblin', health = 6, power = 2):
        super().__init__(name, health, power)
