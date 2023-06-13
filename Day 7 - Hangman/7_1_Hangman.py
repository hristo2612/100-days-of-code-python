# An interactive hangman game you can play from the console
import random

word_list = ["mustache", "giraffe", "car"]

# Choose a random word for the user to guess
chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks "_". Then we can tell the user they've won.
display = ['_' for _ in range(chosen_word_len)]


def guess():
    # Fill in the blanks
    print(" ".join(display))
    guess = input("Guess a letter: ").lower()
    for index in range(chosen_word_len):
        letter = chosen_word[index]
        if guess == letter:
            display[index] = guess


def guessed_all_letters():
    if '_' not in display:
        return True
    else:
        return False


while not guessed_all_letters():
    guess()

print(" ".join(display))
print("You won!")
