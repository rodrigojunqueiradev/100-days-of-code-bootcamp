"""
A dictionary in Python functions similarly to a dictionary in real life. It's a data structure that allows us to associate a key to a value and pair the two pieces of data together.
"""

# Example: 
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}

print(colours)
print(colours["apple"])
print(colours["pear"])
print(colours["banana"])

print("\n")

empty_dictionary = {}

for key in colours:
    print(f"{key} = {colours[key]}")

print("\n")

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

for key in programming_dictionary:
    print(f"{key} = {programming_dictionary[key]}")

print("\n")

# Edit an item:
programming_dictionary["Bug"] = "A moth in your computer."

for key in programming_dictionary:
    print(f"{key} = {programming_dictionary[key]}")