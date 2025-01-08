import random

word_list = ['rodrigo', 'tobi', 'lucky', 'bianca']

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1 - Create an empty String called "placeholder". For each letter in the chosen_word add a _ to placeholder.
# So if the chosen_word was "apple", placeholder should be _ _ _ _ _

placeholder = ""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

# TODO-2 - Create an empty string called "display". Loope through each letter in the chosen_word. If the letter at that position matches guess, then reveal that letter int he display at that position.

display = ''

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)