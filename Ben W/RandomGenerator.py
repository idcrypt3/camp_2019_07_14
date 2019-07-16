import random
def guessing_game():
    computer_number = random.randrange(0, 101)
    print(computer_number)

    guessed = False
    guesses = 0

    while not guessed:
        Random1 = random.randrange(0, 101)
        if Random1 == computer_number:
            print("Yay!! O                   nly took me " + str(guesses) + " guesses")
            break
        else:
            print("Darn. " + str(guesses) + " guesses")
            guesses += 1

guessing_game()
        


