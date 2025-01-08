"""
Love Calculator
💪 This is a difficult challenge! 💪 

You are going to write a function called calculate_love_score() that tests the compatibility between two names. To work out the love score between two people: 
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.
name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times 
R occurs 1 time 
U occurs 2 times 
E occurs 2 times 
Total = 5 

L occurs 1 time 
O occurs 0 times 
V occurs 0 times 
E occurs 2 times 
Total = 3 

Love Score = 53
"""



def calculate_love_score(name1, name2):

    true_love = ['T', 'R', 'U', 'E', 'L', 'O', 'V', 'E']

    #Combine the names in uppercase.
    name_combined = (name1 + name2).upper()

    #Create a dict for the occurs.
    letter_counts = {}

    #Occurs check
    for letter in name_combined:
        if letter in true_love:
            if letter not in letter_counts:
                letter_counts[letter] = 1
            else:
                letter_counts[letter] += 1

    total_occurrences = 0
    for letter, count in letter_counts.items():
        print(f"{letter} occurs {count} times")
        total_occurrences += count
    
    print(f"Love score: {total_occurrences}")

input_name1 = input("Name1: ").upper()
input_name2 = input("Name2: ").upper()

calculate_love_score(input_name1, input_name2)