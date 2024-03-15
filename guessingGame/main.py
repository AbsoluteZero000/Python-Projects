import random


mn, mx = 0, 10
randomNumber = int(random.random()*(mx+1) - 0.000001)

userInput = int(input(f"Welcome to the Guessing Game!\nPlease enter you guess between {mn} and {mx}: "))
if randomNumber == userInput:
    print("You guessed it Correctly!")
else:
    print("You didn't guess it Correctly :(")
    print(f"The Correct answer is {randomNumber}")
