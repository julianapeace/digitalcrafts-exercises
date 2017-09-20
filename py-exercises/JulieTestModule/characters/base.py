import random

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        return self.health > 0

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

    def attack(self, enemy):
        enemy.health -= self.power
        print("{} does {} damage to the {}.".format(self.name, self.power, enemy.name))
        if self.alive() == False:
            print("The {} is dead.".format(self.name))
        if enemy.alive() == False:
            print("The {} is dead.".format(enemy.name))

    def heal(self):
        roll_dice = random.random()
        if self.alive and roll_dice < 0.2:
            self.health += 2
            print("{} gained 2 health.".format(self.name))
