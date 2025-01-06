"""
Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessonans today you will be building a very simple version of this type of text game.
Use the Flowchart.
"""

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choise1 = input("Left or right? ").lower()
if choise1 == "right":
    print("Fall into a hole. \n Game Over")
else:
    print("Keep going ...")

choise2 = input("Swim or Wait? ").lower()
if choise2 != "wait":
    print("Attacked by a trout. \n Game Over")
else:
    print("Keep going ...")

choise3 = input("Which door? Blue, Red or Yellow ").lower()
if choise3 == "red":
    print("Burned by fire. \n Game Over")
elif choise3 == "blue":
    print("Eaten by beasts. \n Game Over.")
elif choise3 == "yellow":
    print("You Win!")
else:
    print("Game Over.")
