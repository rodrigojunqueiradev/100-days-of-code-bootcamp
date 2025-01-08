import random

word_list = ['rodrigo', 'tobi', 'lucky', 'bianca']

# TODO-1 - Create a variable called 'lives' to keep tack of the number of liver left and set live to equal 6

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ''

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
           display += letter 
        else:
            display += "_"

    print(display)

    # TODO-2 - If guess is not a letter in the cosen_word, then reduce lives by 1.
    # If lives goes down to 0 then the game should end, and it should print "You Lose".

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong letter, you have now {lives} lives.")
        if lives == 0:
            game_over = True
            print("You Lose")    

    if "_" not in display:
        game_over = True
        print("You Win")