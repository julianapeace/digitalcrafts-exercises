from characters.base import Character

class Medic(Character):
    def __init__(self, name = 'Medic', health = 10, power = 5, armor = 0, evade = 0, coincount = 5):
        super().__init__(name, health, power, armor, evade, coincount)
