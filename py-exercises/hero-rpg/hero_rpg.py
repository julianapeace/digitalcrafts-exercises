#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
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
        if self.health <= 0:
            print("The {} is dead.".format(self.name))
        if enemy.health <=0:
            print("The {} is dead.".format(enemy.name))

class Hero(Character):
    def __init__(self, name = 'Hero', health = 10, power = 5):
        super().__init__(name, health, power)

class Goblin(Character):
    def __init__(self, name = 'Goblin', health = 6, power = 2):
        super().__init__(name, health, power)

goblin = Goblin()
hero = Hero()

def main():
    hero.health = 10
    hero.power = 5
    goblin.health = 6
    goblin.power = 2

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)

main()
