import random
from os import system

# Number guessing game
print("Welcome to the Number Guessing Game!")

keep_playing = True


def game():
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 10 if difficulty == "easy" else 5
    number_to_guess = random.randrange(1, 101)
    current_guessed_number = 0
    game_over = False

    def guess():
        print(f"You have {attempts} attempts remaining to guess the number.")
        return int(input("Make a guess: "))

    def evaluate_guess(your_guess):
        if your_guess == number_to_guess:
            print(f"You got it! The number was {number_to_guess}.")
            return True
        elif your_guess > number_to_guess:
            print("Too high.")
        elif your_guess < number_to_guess:
            print("Too low.")

        if attempts == 0:
            return True
        else:
            return False

    while not game_over:
        current_guessed_number = guess()
        attempts -= 1
        game_over = evaluate_guess(current_guessed_number)


while keep_playing:
    game()
    keep_playing = True if input(
        "Do you want to play again? Type 'y' or 'n': ") == "y" else False
