import random

choice = ["stone", "scissor", "paper"]
win = {"stone":"scissor", "scissor":"paper", "paper":"stone"}

user_choice = input("Enter stone, scissor or paper: ").lower()

if user_choice not in choice:
    print("Error, choose only stone, scissor or paper")
else:
    computer_choice = random.choice(choice)
    print("Computer choice: ", computer_choice)

    if user_choice == computer_choice:
        print("DRAW")
    elif win[user_choice] == computer_choice:
        print("YOU WIN!")
    else:
        print("COMPUTER WIN")