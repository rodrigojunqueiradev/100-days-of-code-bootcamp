"""
Rock Paper Scissors
You're going to build a Rock, Paper, Scissors game.
You'll need to use what you have learnt about randomisation and Lists to achieve this.
"""

import random

personal_choice = int(input("What do you choose? Type 0 to Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0, 2)
print(f"Computer choose: {computer_choice}")

if personal_choice >= 3 or personal_choice < 0:
    print("Invalid number. You lose.")

elif personal_choice == 0 and computer_choice == 2:
    print("You win!")

elif computer_choice == 0 and personal_choice == 2:
    print("You lose!")

elif computer_choice > personal_choice:
    print("You lose!")

elif personal_choice > computer_choice:
    print("You win!")

elif personal_choice == computer_choice:
    print("Draw!")