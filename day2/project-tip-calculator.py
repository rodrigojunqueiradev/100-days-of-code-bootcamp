"""
Project 2 - Tip Calculator
If the bill was $150.00, split between 5 people, with 15% tip.
Each person should pay: (150 / 5) * 1.12
After formatting the result to 2 decimal places.
"""

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? "))
people = int(input("How many people to split the bill? "))

each_pay = (total / people) * (1 + (tip/100))

print(f"Each person should pay: $ {each_pay:.2f}")