import random

word_list = ['rodrigo', 'tobi', 'lucky', 'bianca']

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

    if guess in correct_letters:
        print(f"You've already guesses {guess}")

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

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong letter, you have now {lives} lives.")
        if lives == 0:
            game_over = True
            print("You Lose")    

    if "_" not in display:
        game_over = True
        print("You Win")