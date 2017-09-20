from characters.base import Character
import random

class Hero(Character):
    def __init__(self, name = 'Hero', health = 10, power = 5):
        super().__init__(name, health, power)
    def attack(self, enemy):
        roll_dice = random.random()
        if roll_dice < 0.2:
            self.power = self.power*2
            enemy.health -= self.power
        else:
            enemy.health -= self.power
        print("{} does {} damage to the {}.".format(self.name, self.power, enemy.name))
        if self.alive() == False:
            print("The {} is dead.".format(self.name))
        if enemy.alive() == False:
            print("The {} is dead.".format(enemy.name))
