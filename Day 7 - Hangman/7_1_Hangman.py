# An interactive hangman game you can play from the console
import random

word_list = ["mustache", "giraffe", "car"]

# Choose a random word for the user to guess
chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called (display).
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = ['_' for _ in range(chosen_word_len)]
print(" ".join(display))
guess = input("Guess a letter: ").lower()

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for index in range(chosen_word_len):
    letter = chosen_word[index]
    if guess == letter:
        display[index] = guess

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(" ".join(display))
