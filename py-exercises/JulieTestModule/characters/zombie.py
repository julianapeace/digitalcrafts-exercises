from characters.base import Character

class Zombie(Character):
    def __init__(self, name = 'Zombie', health = 10, power = 2, armor = 0, evade = 0, coincount = 10):
        super().__init__(name, health, power, armor, evade, coincount)
    def alive(self):
        super().alive()
        return True
