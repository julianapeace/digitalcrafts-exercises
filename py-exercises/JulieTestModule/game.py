from characters.hero import Hero
from characters.goblin import Goblin
from characters.medic import Medic
from characters.shadow import Shadow
from characters.zombie import Zombie

goblin = Goblin()
hero = Hero()
medic = Medic()
shadow = Shadow()
zombie = Zombie()

#Who are you?
you = hero
enemy = zombie

def main():
    counter = 0
    while enemy.alive() and you.alive():
        you.print_status()
        enemy.print_status()

        print()
        print("What do you want to do?")
        print("1. fight monster")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            #you attack enemy
            if isinstance(enemy, Zombie):
                you.attack(enemy)
                print('{} cannot die.'.format(enemy.name))
            else:
                you.attack(enemy)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.health > 0 and isinstance(enemy, Zombie):
            # Goblin attacks hero
            if isinstance(you, Medic):
                enemy.attack(you)
                you.heal()
            elif isinstance(you, Shadow):
                if counter < 10:
                    counter += 1
                    print ("Attack failed!")
                elif counter > 9:
                    print("Attack success!")
                    enemy.attack(you)
                    counter = 0
            else:
                enemy.attack(you)
        else:
            enemy.attack(you)

main()
