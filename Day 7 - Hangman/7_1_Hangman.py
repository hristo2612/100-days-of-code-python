# An interactive hangman game you can play from the console
import random

# Hangman stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# List of random words
word_list = ["mustache", "giraffe", "car"]

# Choose a random word for the user to guess
chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)

lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Display the blank & guessed letters
display = ['_' for _ in range(chosen_word_len)]


def guess():
    # Make python know that lives is reffering to the global 'lives' variable instead of the local scope
    global lives
    # Fill in the blanks
    guess = input("Guess a letter: ").lower()
    for index in range(chosen_word_len):
        letter = chosen_word[index]
        if guess == letter:
            display[index] = guess

    if guess not in chosen_word:
        lives -= 1
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
    print("You lose.")
