#Python Part 1 Exercise
def guess_a_number():
    secret_number = 9
    guess = 0
    while guess != secret_number:
        guess = int(input("I am thinking of a number between 1 and 10. What's the number?"))
        print ("Nope, try again.")
    print("Yes! You win!")

guess_a_number()
