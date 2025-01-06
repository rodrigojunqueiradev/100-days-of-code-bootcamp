"""
Band Name Generator Project
1. Create a greeting for your program.
2. Ask the user for the city that they grew up in and store it in a variable.
3. Ask the user for the name of a pet and store it in a variable.
4. Combine the name of their city and pet and show them their band name.
"""

print("Hello, Stranger Musician")
print("Welcome to the Band Name Generator")
city = input("What city that you grew up? ")
petName = input("Whats your pet name? ")
bandName = city + " " + petName

print(f"This is your band name: {bandName}")