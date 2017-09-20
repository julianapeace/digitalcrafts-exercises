#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


class Zombie(Character):
    def __init__(self, name = 'Zombie', health=10000, power = 2):
        super().__init__(name, health, power)
