# Based on a users order calculate their final bill
"""
Small Pizza: $15 - S

Medium Pizza: $20 - M

Large Pizza: $25 - L

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1
"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Constants
small_pizza = 15
medium_pizza = 20
large_pizza = 25
sm_pepperoni_price = 2
pepperoni_price = 3
extra_cheese_price = 1

final_bill = 0

if size == "S":
    final_bill += small_pizza
elif size == "M":
    final_bill += medium_pizza
elif size == "L":
    final_bill += large_pizza

if add_pepperoni == "Y":
    if size == "S":
        final_bill += sm_pepperoni_price
    else:
        final_bill += pepperoni_price

if extra_cheese == "Y":
    final_bill += extra_cheese_price

print(f"Your final bill is ${final_bill}.")
