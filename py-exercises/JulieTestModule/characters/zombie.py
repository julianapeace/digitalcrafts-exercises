from characters.base import Character

class Zombie(Character):
    def __init__(self, name = 'Zombie', health = 10, power = 2):
        super().__init__(name, health, power)
    def alive(self):
        super().alive()
        return True
