import random
from os import system
from higher_lower_art import logo
from higher_lower_art import vs
from higher_lower_data import data

game_over = False
score = 0


def game_loop():
    global score
    global game_over
    print(logo)
    contestant_one, contestant_two = random.sample(data, 2)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(
        f"Compare A: {contestant_one['name']}, a {contestant_one['description']}, from {contestant_one['country']}.")
    print(vs)
    print(
        f"Against B: {contestant_two['name']}, a {contestant_two['description']}, from {contestant_two['country']}.")
    right_answer = "A" if contestant_one['follower_count'] > contestant_two['follower_count'] else "B"
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if (answer == "A" or answer == "B") and right_answer == answer:
        score += 1
    else:
        game_over = True


def game_over_screen():
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")


while not game_over:
    game_loop()
    system("clear")


game_over_screen()
