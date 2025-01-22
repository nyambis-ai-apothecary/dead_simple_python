"""
This module serves as a reference and
playground for exploring and practicing
different Python syntax features.
"""

def print_hello_world():
    """Prints the classic 'Hello, world!' message."""
    print("Hello, world!")

def get_input():
    """Gets input from the console"""
    name = input("What is your name? ")
    print("Hello, " + name)

def statements_and_expressions():
    """
    - Each line of code in Python that ends with a line break is a statement.
    - An expression is a section of code that evaluates to a single value.
    - 1. Assign the expression "Hello, world!" to message ... 
    - 2. then pass the expression message to print()
    """
    message = "Hello, world"
    print(message)

if __name__ == "__main__":
    """ You can call any function here to run it independently"""
    #print_hello_world()
    #get_input()
    statements_and_expressions()
