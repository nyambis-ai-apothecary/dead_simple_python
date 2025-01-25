"""
This module explores the use of logical operators.
"""


def conditional_statements():
    """
    Conditionals are compound statements composed of
    if, elif, and else clauses- each made up of a header
    and a suite.

    You can have as many elif conditionals as you want,
    sandwiched between if and else clauses.
    """

    command = "greet"

    if command == "greet":
        print("Hello!")
    elif command == "quit":
        print("Goodbye!")
    else:
        print("I don't understand")
