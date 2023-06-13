# An interactive hangman game you can play from the console
import random

# Step 1
word_list = ["mustache", "giraffe", "car"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called (chosen_word)
chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called (guess). Make guess lowercase
guess = input("What is you guess?\n").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the (chosen_word)
for char in chosen_word:
    if guess == char:
        print("Right")
    else:
        print("Wrong")
