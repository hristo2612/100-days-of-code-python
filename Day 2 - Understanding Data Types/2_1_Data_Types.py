# Working with primitive Data Types in Python ( Int & String )
two_digit_number = input("Type a two digit number: ")

number_one = two_digit_number[0]
number_two = two_digit_number[1]

result = str(int(number_one) + int(number_two))

print(f'{number_one} + {number_two} = {result}')
