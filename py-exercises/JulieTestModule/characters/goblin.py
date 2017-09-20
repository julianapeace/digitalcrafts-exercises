from characters.base import Character

class Goblin(Character):
    def __init__(self, name = 'Goblin', health = 6, power = 2, armor=0, evade=0, coincount = 5):
        super().__init__(name, health, power, armor, evade, coincount)
