from characters.base import Character
import random

class Hero(Character):
    def __init__(self, name = 'Hero', health = 10, power = 5, armor = 2, evade = 2, coincount = 8):
        super().__init__(name, health, power, armor, evade, coincount)

    def attack(self, enemy):
        roll_dice = random.random()
        print (roll_dice)
        if roll_dice < 0.2:
            self.power = self.power*2
            enemy.health -= self.power
        else:
            enemy.health -= self.power
        print("{} does {} damage to the {}.".format(self.name, self.power, enemy.name))
