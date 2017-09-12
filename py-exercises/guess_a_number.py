#Python Part 1 Exercise
def guess_a_number():
    secret_number = 9
    guess = 0
    while guess != secret_number:
        guess = int(input("I am thinking of a number between 1 and 10. What's the number?"))
        print ("Nope, try again.")
    print("Yes! You win!")

guess_a_number()

#Give High-Low Hint
def guess_a_number2():
    secret_number = 7
    guess = 0
    while guess != secret_number:
        guess = int(input("I am thinking of a number between 1 and 10. What's the number?"))
        if guess > secret_number:
            print(guess, "is too high.")
        else:
            print(guess, "is too low.")
    print("Yes! You win!")

guess_a_number2()

#Randomly Generated Secret Number
import random
def guess_a_random_number():
    secret_number = random.randint(1,10)
    guess = 0
    while guess != secret_number:
        guess = int(input("I am thinking of a number between 1 and 10. What's the number?"))
        if guess > secret_number:
            print(guess, "is too high.")
        elif guess < secret_number:
            print(guess, "is too low.")
    print("Yes! It is",secret_number,"You win!")

guess_a_random_number()

#Limit number of guesses
def guess_a_random_number_limit():
    secret_number = random.randint(1,10)
    chances = 5
    guess = 0
    print ("I am thinking of a number between 1 and 10. You have 5 guesses left.")
    while chances > 0:
        guess = int(input("What's the number?"))
        if guess > secret_number:
            print(guess, "is too high.")
        elif guess == secret_number:
            print("You win!")
            break
        else:
            print(guess, "is too low.")
        chances = chances - 1
        print("You have", chances, "guesses left.")

    print("You ran out of guesses!")

guess_a_random_number_limit()

#Bonus round
def guess_a_random_number_limit_bonus():
    secret_number = random.randint(1,10)
    chances = 5
    guess = 0
    print ("I am thinking of a number between 1 and 10. You have 5 guesses left.")
    while chances > 0:
        guess = int(input("What's the number?"))
        if guess > secret_number:
            print(guess, "is too high.")
        elif guess == secret_number:
            ans = (input("You win! Do you want to play again? Y/N")).upper()
            if ans == Y:
                guess_a_random_number_limit_bonus()
            else:
                break
        else:
            print(guess, "is too low.")
        chances = chances - 1
        print("You have", chances, "guesses left.")

    print("You ran out of guesses!")

guess_a_random_number_limit_bonus()
