# Positional vs Keyword function arguments in python

def greet_with_name_and_location(name, location):
    print(f"Hello, {name}!")
    print(f"How is it going in {location}?")


# Positional Arguements
# the order of the arguments does matter
greet_with_name_and_location("Hristo", "Sofia")

# Keyword Arguments
# the order of the arguments does NOT matter
greet_with_name_and_location(location="Pleven", name="Kristina")
