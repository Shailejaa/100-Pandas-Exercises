from hangman_art import stages, logo
from hangman_words import word_list
import random

print(logo)

##stages = ['''
##  +---+
##  |   |
##  O   |
## /|\  |
## / \  |
##      |
##=========
##''', '''
##  +---+
##  |   |
##  O   |
## /|\  |
## /    |
##      |
##=========
##''', '''
##  +---+
##  |   |
##  O   |
## /|\  |
##      |
##      |
##=========
##''', '''
##  +---+
##  |   |
##  O   |
## /|   |
##      |
##      |
##=========''', '''
##  +---+
##  |   |
##  O   |
##  |   |
##      |
##      |
##=========
##''', '''
##  +---+
##  |   |
##  O   |
##      |
##      |
##      |
##=========
##''', '''
##  +---+
##  |   |
##      |
##      |
##      |
##      |
##=========
##''']

chosen_word = random.choice(word_list)

display = []
for i in range(len(chosen_word)):
    display += "_"

lives = 6
# print(f"The word is {chosen_word}")
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've repeated the letter {guess} again.")
    if guess not in chosen_word:
        print("You've guessed a wrong letter.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")
        print(stages[lives])
    else:

        for j in range(len(chosen_word)):
            if chosen_word[j] == guess:
                display[j] = guess
                print(display)

        if "_" not in display:
            end_of_game = True
            print("You Win, yayy!")















