# An interactive hangman game you can play from the console
import random
from os import system
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

# Choose a random word for the user to guess
chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)
lives = 6

# Display the blank & guessed letters
display = ['_' for _ in range(chosen_word_len)]


def guess():
    # Make python know that lives is reffering to the global 'lives' variable instead of the local scope
    global lives
    # Fill in the blanks
    guess = input("\nGuess a letter: ").lower()

    # Clear the previous console output
    system('clear')

    if guess in display:
        print(f"You already guessed '{guess}'")

    for index in range(chosen_word_len):
        letter = chosen_word[index]
        if guess == letter:
            display[index] = guess

    if guess not in chosen_word:
        lives -= 1
        print(
            f"You guessed '{guess}', that's not in the word. You lose a life.")

    print("\n")
    print(" ".join(display))
    print(stages[lives])


def game_ended():
    if '_' not in display or lives == 0:
        return True
    else:
        return False


def has_won():
    if '_' not in display:
        return True
    else:
        return False


while not game_ended():
    guess()

if has_won():
    print("You win!")
else:
    print(f"You lose. The word was '{chosen_word}'")
