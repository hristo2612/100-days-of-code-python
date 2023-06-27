from blackjack_art import logo
from os import system
import random

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
play_again = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_hand():

    def random_card():
        global cards
        return random.choice(cards)

    def get_score(cards):
        score = 0
        aces = 0

        for card in cards:
            if card == 11:  # if it's an ace
                aces += 1
                score += 11  # initially count ace as 11
            else:
                score += card

        # If score is over 21 and there is an ace in hand, count it as 1 instead
        while score > 21 and aces:
            score -= 10
            aces -= 1

        return score

    def is_busted(cards):
        if get_score(cards) > 21:
            return True
        else:
            return False

    # Populate computer's cards
    def fill_cards(cards):
        while get_score(cards) < 17:
            cards.append(random_card())
        return cards

    game_finished = False
    your_cards = [random_card(), random_card()]
    computer_cards = [random_card()]
    while not game_finished:
        print(
            f"    Your cards: {your_cards}, current score: {get_score(your_cards)}")
        print(f"    Computer's first card: {get_score(computer_cards)}")
        if is_busted(your_cards):
            game_finished = True
        else:
            add_card = True if input(
                "Type 'y' to get another card, type 'n' to pass: ") == "y" else False
            if add_card:
                your_cards.append(random_card())
            else:
                game_finished = True

    computer_cards = fill_cards(computer_cards)

    print(
        f"    Your final hand: {your_cards}, final score: {get_score(your_cards)}")

    if is_busted(your_cards):
        print("You went over. You lose 😤")
    elif get_score(your_cards) < get_score(computer_cards) and not is_busted(computer_cards):
        print(
            f"    Computer's final hand: {computer_cards}, final score: {get_score(computer_cards)}")
        print("You lose 😤.")
    elif get_score(your_cards) == get_score(computer_cards):
        print(
            f"    Computer's final hand: {computer_cards}, final score: {get_score(computer_cards)}")
        print("It's a draw.")
    else:
        print(
            f"    Computer's final hand: {computer_cards}, final score: {get_score(computer_cards)}")
        print("You win.")


def game_loop():
    global play_again

    play_again = True if input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y" else False

    if play_again:
        system("clear")
        print(logo)
        play_hand()


while play_again:
    game_loop()
