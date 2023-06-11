# Based on a number we provide find the treasure on the "map".
# The number is a two digit number. First digit is the Y coordinate, second one is the X coordinate
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

y = int(position[0]) - 1
x = int(position[1]) - 1

treasure_map = [row1, row2, row3]

treasure_map[x][y] = "X"

print(f"{row1}\n{row2}\n{row3}")
