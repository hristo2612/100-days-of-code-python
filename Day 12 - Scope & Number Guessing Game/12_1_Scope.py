# Scope in Python

some_variable = 2  # We are creating a global variable


def some_function():
    some_variable = 5  # We are creating a local variable totally different from the global one
    print(some_variable)  # Prints out 5


print(some_variable)  # Prints out 2


# NOT RECOMMENDED: In order to re-assign a new value to the global variable we can use the global keyword like so:

other_variable = 4


def other_function():
    # This states that we should use the global variable instead of a local one for this namespace
    global other_variable
    other_variable = 10
    print(other_variable)  # Prints out 10


print(other_variable)  # Prints out 10


# Since changing global variables is not recommended inside local scope we can use a 'return' statement to assign the new value like so:

one_more_variable = 10


def one_more_function():
    return one_more_variable + 10


one_more_variable = one_more_function()
