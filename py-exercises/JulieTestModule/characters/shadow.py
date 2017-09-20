from characters.base import Character

class Shadow(Character):
    def __init__(self, name = 'Shadow', health = 1, power = 5, armor = 0, evade = 0, coincount = 4):
        super().__init__(name, health, power, armor, evade, coincount)
