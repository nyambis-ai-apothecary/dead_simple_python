"""
This module serves as a reference and
playground for exploring and practicing
different Python syntax features.
"""


def print_hello_world():
    """Print the classic 'Hello, world!' message."""
    print("Hello, world!")


def get_input():
    """Get input from the console and greet the user."""
    name = input("What is your name? ")
    print("Hello, " + name)


def statements_and_expressions():
    """
    Demonstrate statements and expressions in Python.

    - Each line of code in Python that ends with a line break is a statement.
    - An expression is a section of code that evaluates to a single value.
    - Assign the expression "Hello, world!" to message and then pass
    the expression message to print().
    """
    message = "Hello, world"
    print(message)


def importance_whitespace():
    """
    Demonstrate the importance of whitespace in Python.

    A compound statement is made up of two or more clauses, each of which:
    - starts with a header
    - and a block of code called a suite.

    The program below prints different messages, depending on whether a name is provided.
    """
    name = "Jason"
    if name != "":  # if header
        message = "Hello, " + name + "!"  # suite line 1
        print(message)  # suite line 2
    print("I am a computer")


def pass_placeholder():
    """
    The pass statement is a null operation that does nothing.
    "Doing Nothing": It is used as a placeholder when a statement is required syntactically
    but you do not want to execute any code.
    """

    nyambi = True
    if nyambi:
        pass


if __name__ == "__main__":
    # print_hello_world()
    # get_input()
    # statements_and_expressions()
    # importance_whitespace()
    pass_placeholder()
