import random

word_list = ['rodrigo', 'tobi', 'lucky', 'bianca']

# TODO-1 - Randomly choose a word from the word_lsit and assign ir to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variale called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guesses (guess) is one of the letters in the chosen_word. Print "right" if it is, "wrong" if it's not.

if guess in chosen_word:
    print('right')
else:
    print('wrong')