# A popular game in London within big banker folks.
# Every time they go to a restaurant when the time comes to pay the bill, they toss their business cards into a bowl.
# This way they play a russian roulette of who will pay the bill
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Using random.choice for the list retrieves a random item from the list itself
print(f"{random.choice(names)} is going to buy the meal today!")
