import random

# Define options for the game
options = ["rock", "paper", "scissors"]

# Game loop
while True:
  # Get user input
  user_choice = input("Choose Rock, Paper, or Scissors: ")

  # Convert user input to lowercase for case-insensitive comparison
  user_choice = user_choice.lower()

  # Check for invalid input
  if user_choice not in options:
    print("Invalid choice. Please try again.")
    continue

  # Get computer's choice
  computer_choice = random.choice(options)

  # Print choices
  print(f"You chose: {user_choice}")
  print(f"Computer chose: {computer_choice}")

  # Determine winner (using the lowercased user_choice)
  if user_choice == computer_choice:
    print("It's a tie!")
  elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
  else:
    print("You lose!")

  # Ask to play again
  play_again = input("Play again? (yes/no): ").lower()
  if play_again != "yes":
    break

print("Thanks for playing!")
