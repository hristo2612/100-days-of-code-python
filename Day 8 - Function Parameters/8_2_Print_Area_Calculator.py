# Calculate how many cans of paint we will need to paint a wall with x height and y width
from math import ceil


def paint_calc(width, height, cover):
    cans = (width * height) / cover
    cans = ceil(cans)
    print(f"You'll need {cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
