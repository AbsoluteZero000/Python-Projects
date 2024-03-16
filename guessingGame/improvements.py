import random


def play_guessing_game(min_number, max_number):
    """Plays a number-guessing game within the given range."""

    attempts = 0
    random_number = random.randint(min_number, max_number)

    print("Welcome to the Guessing Game!\n")
    print(f"Guess a number between {min_number} and {max_number}.")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess == random_number:
                print("Congratulations! You guessed it correctly in", attempts, "attempts!")
                break

            elif user_guess < random_number:
                print("Too low! Try again.")

            else:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    attempts_list = []

    while True:
        play_guessing_game(0, 10)

        try:
            high_score = min(attempts_list) if attempts_list else None
            print(f"The current high score is {high_score}")
        except ValueError:
            print("No high score yet!")

        play_again = input("Do you want to play again (yes/no)? ").lower()
        if play_again not in ("yes", "y"):
            break


if __name__ == "__main__":
    main()
