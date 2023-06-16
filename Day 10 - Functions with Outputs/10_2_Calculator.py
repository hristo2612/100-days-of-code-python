# A simple calculator with multiple calculations
from calculator_art import logo
import operator
from os import system

finished = False
first_number = True
calculations = {
    "first_number": 0,
    "second_number": 0,
    "result": 0
}


def perform_operation(first_number, second_number, operation):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    if operation in ops:
        return ops[operation](first_number, second_number)
    else:
        raise ValueError('Invalid operation. Available operations: +, -, *, /')


def calculate():
    global finished
    global first_number
    if first_number:
        print(logo)
        calculations["first_number"] = float(
            input("What's the first number?: "))
        print("+ or - or * or /")

    operation = input("Pick an operation: ")

    calculations["second_number"] = float(input("What's the next number?: "))

    calculations["result"] = perform_operation(
        calculations["first_number"], calculations["second_number"], operation)

    first = calculations["first_number"]
    second = calculations["second_number"]
    result = calculations["result"]
    print(f"{first} {operation} {second} = {result}")
    next_action = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. Or type 'quit': ")

    if next_action == "y":
        first_number = False
        calculations["first_number"] = calculations["result"]
    elif next_action == "n":
        first_number = True
        system("clear")
    else:
        finished = True


while not finished:
    calculate()
