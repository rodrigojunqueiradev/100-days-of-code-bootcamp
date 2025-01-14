"""
You can mix and match various data types to achieve your desired structure.

Example:
my_dictionary = {
    key1: [List],
    key2: Value,
}
"""

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

for key in travel_log:
    print(travel_log[key])

# Printing Lille:
print(travel_log["France"][1])

print("\n")

nested_list = ["A", "B", ["C", "D"]]

# Print D:
print(nested_list[2][1])

print("\n")

# Nested dictionary in a dictionary:
travel_log2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin"],
        "total_visits": 5
    }
}

for key in travel_log2:
    print(f"{key}: {travel_log2[key]}")

# How to print Stuttgart:
print(travel_log2["Germany"]["cities_visited"][0])