guessed = False
while not guessed:
    guess = input("pick a number")
    if int(guess) == 14:
        guessed = True
print("good job")