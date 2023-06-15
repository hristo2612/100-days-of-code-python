from secret_auction_art import logo
from os import system

print(logo)
print("------------ Welcome to the secret auction program. ------------\n")

participants = []
finished = False

# max(data, key=lambda x: x['age'])


def add_bid():
    global finished
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    participants.append({"name": name, "bid": bid})
    finished = False if input(
        "Are there any other bidders? Type 'yes' or 'no': ") == "yes" else True
    if not finished:
        system("clear")


def find_winner(participants):
    return max(participants, key=lambda participant: participant["bid"])


while not finished:
    add_bid()


winner = find_winner(participants=participants)
winner_name = winner["name"]
winner_bid = winner["bid"]
print(f"The winner is {winner_name} with a bid of ${winner_bid}.")
