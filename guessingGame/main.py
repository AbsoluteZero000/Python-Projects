import random


mn, mx = 0, 10
attempts_list = []
while True:
    attempts = 0
    randomNumber = int(random.random()*(mx+1) - 0.000001)
    print("Welcome to the Guessing Game!\n")
    print(f"The current high score is {min(attempts_list)}" if len(attempts_list) > 0 else "There's no current high score")
    while True:
        userInput = int(input(f"Please enter you guess between {mn} and {mx}: "))
        try:
            if userInput < mn or userInput > mx:
                raise ValueError("invalid input try again")
        except ValueError as err:
            print(err)
        if randomNumber == userInput:
            print("You guessed it Correctly!")
            attempts_list.append(attempts)
            print(f"attempts = {attempts}")
            break
        else:
            print("You didn't guess it Correctly :(")
            if userInput > randomNumber:
                print("It's lower than the number you entered")
            else:
                print("It's higher than the number you entered")
            attempts+=1


    choice = input("Do you want to play again: ")
    if not (choice == "yes" or choice == 'y'):
        break
