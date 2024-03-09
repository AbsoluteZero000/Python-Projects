import random

choices = ['r', 'p', 's']
rules = {
    "r": "s",
    "p": "r",
    "s": "p"
}
def compute_winner(choice, user_choice):
    if(user_choice not in choices):
        return "Invalid Choice!?!?!"
    elif(choice == user_choice):
        return "Tie"
    elif rules.get(user_choice) == choice:
        return "You win!"
    else:
        return "The Computer Wins!"

# r > s, s > p, p > r

choice = random.choice(choices)

user_choice = input("enter your move\n1- Rock = r\n2- Paper = p\n3- Scissors = s\n")
print("You played: ", user_choice)
print("The computer played: ", choice)
print(compute_winner(choice, user_choice))
