"""
In this module, we explore greeetings and user input.
"""


def print_hello_world():
    """Print the classic 'Hello, world!' message."""
    print("Hello, world!")


def get_input():
    """Get input from the console and greet the user."""
    name = input("What is your name? ")
    print("Hello, " + name)


# Call the functions
print_hello_world()
get_input()
