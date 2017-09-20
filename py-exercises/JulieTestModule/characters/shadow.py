from characters.base import Character

class Shadow(Character):
    def __init__(self, name = 'Shadow', health = 1, power = 5):
        super().__init__(name, health, power)
